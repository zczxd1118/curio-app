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

- 今日日期：`2026-06-04`
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
  "date": "2026-06-04",
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
    "points": 590359,
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
    "points": 366411,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 334128,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 232478,
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
    "points": 223937,
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
    "points": 197184,
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
    "points": 173257,
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
    "points": 151123,
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
    "points": 141972,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 131392,
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
    "points": 92485,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 91329,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV1KX9jB8E9M",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！比付费效果强十倍",
    "url": "http://www.bilibili.com/video/av116328887225403",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 70901,
    "published_at": "2026-04-01T10:12:34+00:00",
    "summary": "视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "domain": "AI",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 57657,
    "published_at": "2025-06-28T02:37:22+00:00",
    "summary": "视频主题&amp;项目背景\n主题： 分享个人如何使用cursor 从0到1开发一个比较大的项目，使用的技术栈是vue+小程序+java\n项目\n一个B2B的订货商城及供应链全流程管理，包含的端有：\n小程序商城端\n供应商端\n仓储物流端\n司机配送端\n销售端\n后台管理系统\n以上小程序端都是使用webview的方式\n核心功能：\n商城的基本功能: 正逆向订单、商品、购物车、优惠券、积分、钱包、充值、工单等\n供"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 55915,
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
    "points": 52221,
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
    "points": 50479,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV13K1YBtE6e",
    "domain": "AI",
    "title": "【GMM】MCP 使用说明",
    "url": "http://www.bilibili.com/video/av115485010168640",
    "source": "3DM小莫",
    "platform": "bilibili",
    "points": 35862,
    "published_at": "2025-11-03T09:19:08+00:00",
    "summary": "MCP 支持 是 Gloss Mod Manager（GMM ）在 1.62.0 新增的一个功能， 你需要至少更新到 1.62 才能使用此功能；\n\n你可以使用任何支持 MCP 的客户端 和 AI 使用它, 但建议你的 AI 最大 Token 至少有 32K, 否则部分功能可能会受影响。\n\n相关代码已经开源，欢迎参与维护:  https://github.com/GlossMod/Gloss-Mod"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 33745,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 33415,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 29726,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29517,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1yFgCzBEgq",
    "domain": "AI",
    "title": "【Cursor+draw.io】AI轻松生成专业流程图，工作效率提升20倍！",
    "url": "http://www.bilibili.com/video/av114773169604135",
    "source": "AI辅导员小宇",
    "platform": "bilibili",
    "points": 29097,
    "published_at": "2025-06-30T16:07:37+00:00",
    "summary": "不会写代码也能用AI自动生成专业级流程图？这款神器让你秒变&quot;流程图大师&quot;，甩设计师十条街！\n本期重磅干货教你：\n✅ drawio神器免费安装与10秒上手教学\n✅ Cursor+AI自动生成XML代码秘技\n✅ 从文本文件一键生成完美流程图\n✅ 截图→AI逆向工程→复制任何流程图\n✅ 独家赠送专业模板包，一键套用省时省力\n再也不用为画流程图加班熬夜！普通人10分钟=设计师8小时，这"
  },
  {
    "id": "bvid:BV1v8mtBpEwK",
    "domain": "AI",
    "title": "Kiro 上手必看：从Vibe 到 Spec 全攻略！",
    "url": "http://www.bilibili.com/video/av115695564102585",
    "source": "AI编程瓜哥",
    "platform": "bilibili",
    "points": 20632,
    "published_at": "2025-12-10T13:49:11+00:00",
    "summary": "一眼懂，Vibe coding 和Spec Coding，双模式实战。"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17211,
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
    "points": 16941,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 14373,
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
    "points": 13477,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1vc7YzkEws",
    "domain": "AI",
    "title": "小智AI MCP外置视觉系统重磅升级2.0所有设备0成本0改造接入摄像头视觉系统硬件平权，代码开源！人形机器人？语音小盒子？通通给我接入AI小智MCP服务！",
    "url": "http://www.bilibili.com/video/av114620815642839",
    "source": "闪猫侠机器人",
    "platform": "bilibili",
    "points": 13089,
    "published_at": "2025-06-04T01:09:18+00:00",
    "summary": "闪猫MCP服务平台：http://mcp.shanmaotech.cn\n官网www.shanmaotech.cn\nQQ技术交流群：795042597"
  },
  {
    "id": "bvid:BV1ZHAozLE7b",
    "domain": "AI",
    "title": "【SynthPilot】全网首发！2026年最新基于AI的FPGA开发教程，Agent自主编程/调试全链路闭环，500+工具接入Vivado",
    "url": "http://www.bilibili.com/video/av116164755790661",
    "source": "晓川科研站",
    "platform": "bilibili",
    "points": 12893,
    "published_at": "2026-03-03T10:26:33+00:00",
    "summary": "全网首个AI Agent FPGA开发教程。SynthPilot通过MCP协议打通Vivado全链路，AI自主写码、综合、读报告、改Bug、迭代——真正的Agent模式闭环开发。从零开始，带你见证FPGA开发方式的代际变革。\n获取工具:synthpilot.dev\n晓川交流群:1007696121"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 12731,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1L9VZ6bE2r",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！！",
    "url": "http://www.bilibili.com/video/av116673893893645",
    "source": "马小洋qwer",
    "platform": "bilibili",
    "points": 10020,
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
    "points": 8928,
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
    "points": 8760,
    "published_at": "2026-05-27T16:33:52+00:00",
    "summary": "本期体验 DeepSeek-Reasonix 这个开源项目，主要看客户端界面、模型模式、会话导入、MCP 配置、记忆与缓存等功能。内容基于个人使用记录，不做夸张结论，适合对 DeepSeek 生态和 AI 编程工具感兴趣的朋友参考。"
  },
  {
    "id": "bvid:BV1CJR1BBEeo",
    "domain": "AI",
    "title": "【保姆级】设计师如何用Vibe Coding免费建站？不写代码也能做出专业级作品集",
    "url": "http://www.bilibili.com/video/av116521909093386",
    "source": "4KD",
    "platform": "bilibili",
    "points": 8776,
    "published_at": "2026-05-05T12:14:39+00:00",
    "summary": "一天一个离职小技巧\n\n使用Vibe Coding构建属于自己的作品集网站，告别传统的PDF、PPT\n\n图片转链接：https://postimages.org/\n视频转链接：https://www.aconvert.com/cn/\n免费网站发布：https://app.netlify.com/"
  },
  {
    "id": "bvid:BV1caVh6fE6Z",
    "domain": "AI",
    "title": "【2026最新版】绝对是B站讲的最细的Claude Code教程，从国内环境安装出发，项目开发及个人使用总结带你玩转 Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116656764358481",
    "source": "AI大模型_",
    "platform": "bilibili",
    "points": 8017,
    "published_at": "2026-05-29T07:53:39+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 7992,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1eUVJ6EEB9",
    "domain": "AI",
    "title": "2026搞懂Java+AI大模型全套教程 | Spring AI+RAG+AI Agent+DeepSeek+航空AI智能客服项目实战，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116668374254145",
    "source": "程序员诸葛",
    "platform": "bilibili",
    "points": 7671,
    "published_at": "2026-05-31T09:12:07+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套笔记和100万字面试宝典+场景题，简历模板，Java P 5~P8技术栈学习路线自取：https://t.bilibili.com/783606020197842963"
  },
  {
    "id": "bvid:BV19jL46gEab",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116611415541849",
    "source": "Agent搭建",
    "platform": "bilibili",
    "points": 7413,
    "published_at": "2026-05-21T07:43:25+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1FXVz67Epw",
    "domain": "AI",
    "title": "【Claude Code】B站讲得最好的Claude Code教程，没有之一！国内直连保姆级教学，从安装到项目实战，开启Vibe Coding革命【附脚本】",
    "url": "http://www.bilibili.com/video/av116679279379085",
    "source": "马士兵学堂",
    "platform": "bilibili",
    "points": 6935,
    "published_at": "2026-06-02T07:27:09+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6950,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 6796,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1AnVm6GEcy",
    "domain": "AI",
    "title": "用嘴编程（Vibe Coding）时代来了，2026程序员正在“消失”！",
    "url": "http://www.bilibili.com/video/av116685386418858",
    "source": "码士集团_马小菲",
    "platform": "bilibili",
    "points": 6704,
    "published_at": "2026-06-03T09:17:15+00:00",
    "summary": "马士兵1v1免费程序员IT职业规划：转型AI大模型，方向迷茫，面试突击，跳槽涨薪，大龄问题(中年危机)，裁员找工作，考研失败，想规划就业路线/学习路线/大厂路线/转行IT..."
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6346,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1qdRWBeESq",
    "domain": "AI",
    "title": "Antigravity IDE零基础保姆级教程 mcp、skill、rules、workflows、agent完整案例演示、免费claude gemini模型",
    "url": "http://www.bilibili.com/video/av116526640274279",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 6185,
    "published_at": "2026-05-06T08:20:20+00:00",
    "summary": "Antigravity 是什么，和 Cursor/Claude Code/Codex 的区别\n安装、登录、主界面（Editor、Agent Manager、Browser、Terminal）\nAgent 工作流程 &amp; Artifacts\n浏览器能力：让 AI 自己看页面\nMCP（连接外部工具）、Skills（工作说明书）、Rules（规则）\n权限安全建议 + 完整实操案例（个人作品集网站）"
  },
  {
    "id": "bvid:BV1tbVZ62Eg8",
    "domain": "AI",
    "title": "【Agent】这可能是B站唯一将Agent Skills入门到实战彻底讲明白的教程！全程干货，零基础也能直接上手！存下吧，比啃书好太多了！学完直接就业！",
    "url": "http://www.bilibili.com/video/av116674162528110",
    "source": "大模型基础知识",
    "platform": "bilibili",
    "points": 6067,
    "published_at": "2026-06-01T09:42:04+00:00",
    "summary": "【Agent】这可能是B站唯一将Agent Skills入门到实战彻底讲明白的教程！全程干货，零基础也能直接上手！存下吧，比啃书好太多了！学完直接就业！拿走不谢！"
  },
  {
    "id": "bvid:BV1VVQdBCExR",
    "domain": "AI",
    "title": "小米龙虾miclaw体验测评及配置教程，自定义LLM和MCP",
    "url": "http://www.bilibili.com/video/av116277163265800",
    "source": "屎壳郎智能科技",
    "platform": "bilibili",
    "points": 6088,
    "published_at": "2026-03-23T06:52:29+00:00",
    "summary": "接上一期视频，很多小伙伴安装完miclaw后不知道怎么配置和把玩。本期视频将详细告诉你如何配置基础信息，添加自定义LLM和MCP服务。逐步把小龙虾宝宝养成大龙虾。"
  },
  {
    "id": "bvid:BV1ZSVG6eE3V",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116662284130312",
    "source": "非六于期",
    "platform": "bilibili",
    "points": 6041,
    "published_at": "2026-05-30T07:13:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LEVz66EJS",
    "domain": "AI",
    "title": "AI编程Claude code入门到精通保姆级教程，从安装配置、多Claude协作、企业级案例实战一次性全讲明白！Claude code超详细教程",
    "url": "http://www.bilibili.com/video/av116679581372297",
    "source": "程序员诸葛",
    "platform": "bilibili",
    "points": 5972,
    "published_at": "2026-06-02T08:46:16+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n视频笔记和AI大模型笔记代码/学习大纲/面试真题自取：https://www.bilibili.com/read/cv39745782/?jump_opus=1"
  },
  {
    "id": "bvid:BV1CEVm6kE53",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116685336021756",
    "source": "大模型官方课程",
    "platform": "bilibili",
    "points": 5917,
    "published_at": "2026-06-03T09:14:12+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 459,
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
    "points": 424,
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
    "points": 285,
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
    "points": 99,
    "published_at": "2026-06-01T13:05:02+00:00",
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
    "id": "rss:https://www.eetimes.com/taiwan-minister-emphasizes-collaboration-and-future-focus-on-photonics-wbg-and-quantum/",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan Minister Emphasizes Collaboration and Future Focus on Photonics, WBG, and Quantum",
    "url": "https://www.eetimes.com/taiwan-minister-emphasizes-collaboration-and-future-focus-on-photonics-wbg-and-quantum/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T06:00:00+00:00",
    "summary": "In an exclusive video interview, NSTC Minister Wu shares Taiwan's four-pillar shift from chipmaker to AI enabler. The post Taiwan Minister Emphasizes Collaboration and Future Focus on Photonics, WBG, "
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
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/msi-claw-8-ex-ai-brings-intel-arc-g3-extreme-to-handhelds-8-inch-120-hz-display-and-new-ergonomic-grips",
    "domain": "AI 算力 / 半导体",
    "title": "MSI Claw 8 EX AI+ brings Intel Arc G3 Extreme to handhelds — 8-inch, 120 Hz display and new ergonomic grips",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/msi-claw-8-ex-ai-brings-intel-arc-g3-extreme-to-handhelds-8-inch-120-hz-display-and-new-ergonomic-grips",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T16:48:46+00:00",
    "summary": "The MSI Claw 8 EX AI+ brought comfort and performance to Computex with massive prongs and Intel Arc G3 Extreme."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-280-on-this-4k-ready-alienware-aurora-desktop-pc-with-rtx-5080-high-performance-gaming-at-your-fingertips-for-usd2-919",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1,280 on this 4K-ready Alienware Aurora desktop PC with RTX 5080 — high-performance gaming at your fingertips for $2,919",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-280-on-this-4k-ready-alienware-aurora-desktop-pc-with-rtx-5080-high-performance-gaming-at-your-fingertips-for-usd2-919",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T16:37:56+00:00",
    "summary": "Save $1,280 off this Dell Alienware Aurora gaming PC with an RTX 5080 graphics card inside."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/lian-lis-edge-platinum-v2-psus-have-an-led-dust-indicator-magnetic-filter-and-a-snap-on-fan-and-usb-header-hub-edge-lines-trademark-90-degree-power-connector-also-returns",
    "domain": "AI 算力 / 半导体",
    "title": "Lian Li's Edge Platinum V2 PSUs have an LED dust indicator, magnetic filter, and a snap-on fan and USB header hub — Edge line's trademark 90-degree power connector also returns",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/lian-lis-edge-platinum-v2-psus-have-an-led-dust-indicator-magnetic-filter-and-a-snap-on-fan-and-usb-header-hub-edge-lines-trademark-90-degree-power-connector-also-returns",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T16:07:56+00:00",
    "summary": "Lian Li's Edge V2 PSUs add a dust-detecting LED indicator, a removable filter, and a snap-on hub for fans and USB devices. They should arrive in September, at up to 1350 watts."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/asrock-shows-off-a-slew-of-new-aios-power-supplies-and-10th-anniversary-hardware-a-monster-3kw-taichi-power-supply-for-ai-and-hybrid-taichi-aqua-aio-custom-loop-stand-out-in-the-crowd",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock shows off a slew of new AIOs, Power Supplies, and 10th Anniversary hardware — a monster 3KW Taichi power supply for AI and hybrid Taichi Aqua AIO/custom loop stand out in the crowd",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/asrock-shows-off-a-slew-of-new-aios-power-supplies-and-10th-anniversary-hardware-a-monster-3kw-taichi-power-supply-for-ai-and-hybrid-taichi-aqua-aio-custom-loop-stand-out-in-the-crowd",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T16:00:00+00:00",
    "summary": "Tom's Hardware stopped by the ASRock booth, and was greeted by a wide variety of products at this year's Computex."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/samsung-shows-first-hbm5-mockup-at-computex-with-heat-path-block-cooling",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung shows first HBM5 mockup with Heat Path Block cooling — thermal race with SK hynix shaping up",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/samsung-shows-first-hbm5-mockup-at-computex-with-heat-path-block-cooling",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:30:51+00:00",
    "summary": "Samsung displayed its first physical mockup of HBM5 memory at Computex 2026 in Taipei, pairing the eighth-generation AI memory with a new in-package cooling structure."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/computex-2026-day-two-wrap-up-intel-atones-for-arrow-lake-wi-fi-8-comes-into-focus",
    "domain": "AI 算力 / 半导体",
    "title": "Computex 2026 Day Two Wrap-Up: Intel atones for Arrow Lake, Wi-Fi 8 comes into focus",
    "url": "https://www.tomshardware.com/pc-components/cpus/computex-2026-day-two-wrap-up-intel-atones-for-arrow-lake-wi-fi-8-comes-into-focus",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:28:56+00:00",
    "summary": "Computex 2026 is in full swing in Taipei"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/corsair-launches-lightweight-budget-friendly-hs35-v3-gaming-headsets",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair launches lightweight budget-friendly HS35 v3 gaming headsets — wired version weighs a cool 230 grams",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/corsair-launches-lightweight-budget-friendly-hs35-v3-gaming-headsets",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:20:00+00:00",
    "summary": "Corsair launched its HS35 v3 lightweight gaming headsets — wired and wireless — at Computex 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/heatsinks/noctua-shows-off-improved-thermosiphon-prototype-passively-circulated-liquid-cooler-gets-q3-2027-projected-launch-date",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua shows off improved thermosiphon prototype — passively circulated liquid cooler gets Q3 2027 projected launch date",
    "url": "https://www.tomshardware.com/pc-components/heatsinks/noctua-shows-off-improved-thermosiphon-prototype-passively-circulated-liquid-cooler-gets-q3-2027-projected-launch-date",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:08:33+00:00",
    "summary": "Noctua showed off a refined version of its passively circulated thermosiphon liquid cooler at Computex 2026 with an improved evaporator design. The company is confident enough in its progress with thi"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsung-rolls-out-2026-odyssey-gaming-monitors-including-5k-and-6k-models-27-to-32-inches-with-up-to-330-hz-refresh-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung rolls out 2026 Odyssey gaming monitors, including 5K and 6K models — 27 to 32 inches with up to 330 Hz refresh rate",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsung-rolls-out-2026-odyssey-gaming-monitors-including-5k-and-6k-models-27-to-32-inches-with-up-to-330-hz-refresh-rate",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:00:26+00:00",
    "summary": "The Odyssey G8 (G80HS) features a 32-inch 6K IPS panel"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-executives-react-to-nvidias-rtx-spark-youre-just-wrong-if-you-dont-get-a-strix-halo-notebook",
    "domain": "AI 算力 / 半导体",
    "title": "AMD executives react to Nvidia’s RTX Spark — ‘you’re just wrong if you don’t get a Strix Halo notebook’",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-executives-react-to-nvidias-rtx-spark-youre-just-wrong-if-you-dont-get-a-strix-halo-notebook",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:00:00+00:00",
    "summary": "AMD welcomes Nvidia into the market with RTX Spark, saying that its Strix Halo and upcoming Gorgon Halo products will be superior."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/counterfeit-g-skill-and-v-color-ddr5-modules-hit-chinese-marketplaces-impacting-company-sales-cheap-contraband-memory-using-identical-pcbs-and-heat-spreaders-almost-impossible-to-spot",
    "domain": "AI 算力 / 半导体",
    "title": "Counterfeit G.Skill and V-Color DDR5 modules hit Chinese marketplaces, impacting company sales — cheap contraband memory using identical PCBs and heat spreaders almost impossible to spot",
    "url": "https://www.tomshardware.com/pc-components/dram/counterfeit-g-skill-and-v-color-ddr5-modules-hit-chinese-marketplaces-impacting-company-sales-cheap-contraband-memory-using-identical-pcbs-and-heat-spreaders-almost-impossible-to-spot",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T13:32:40+00:00",
    "summary": "Counterfeit memory modules with G.Skill and V-Color badges sold at Chinese marketplaces use identical PCBs and heat spreaders, are hard to identify."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/nzxt-showcases-h6-mid-tower-chassis-new-ultra-rgb-fans-and-a-white-h2-offering-boundless-rgb-customization-options-take-this-case-to-a-whole-new-level",
    "domain": "AI 算力 / 半导体",
    "title": "NZXT showcases H6 mid-tower chassis, new Ultra RGB fans, and a white H2 offering — boundless RGB customization options take this case to a whole new level",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/nzxt-showcases-h6-mid-tower-chassis-new-ultra-rgb-fans-and-a-white-h2-offering-boundless-rgb-customization-options-take-this-case-to-a-whole-new-level",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T13:31:33+00:00",
    "summary": "Tom's Hardware stopped by NZXT at Computex 2026 to get a look at their latest offerings."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-unveils-project-solara-ai-a-chip-to-cloud-platform-built-to-power-a-new-generation-of-agent-first-enterprise-devices-hardware-designed-to-run-ai-agents-instead-of-traditional-apps",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft unveils Project Solara AI, a chip-to-cloud platform built to power a new generation of 'agent-first' enterprise devices — hardware designed to run AI agents instead of traditional apps",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-unveils-project-solara-ai-a-chip-to-cloud-platform-built-to-power-a-new-generation-of-agent-first-enterprise-devices-hardware-designed-to-run-ai-agents-instead-of-traditional-apps",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T12:19:40+00:00",
    "summary": "Microsoft has unveiled Project Solara, an Android-based chip-to-cloud platform for AI-first enterprise devices. The system combines Qualcomm and MediaTek hardware, Azure-hosted agents, and adaptive in"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-signs-ai-executive-order-seeking-30-day-government-access-to-frontier-models-before-release",
    "domain": "AI 算力 / 半导体",
    "title": "Trump signs AI executive order seeking 30-day government access to frontier models before release — voluntary framework will include classified benchmark to determine which models qualify",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-signs-ai-executive-order-seeking-30-day-government-access-to-frontier-models-before-release",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T11:50:49+00:00",
    "summary": "President Donald Trump signed an executive order on Tuesday that asks AI companies to give the federal government early access to their most capable models."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/land-an-rtx-5060-powered-oled-gaming-laptop-for-just-usd1-099-hps-omen-transcend-features-an-intel-core-ultra-7-255h-16-core-cpu-3k-resolution-and-wifi-7",
    "domain": "AI 算力 / 半导体",
    "title": "Land an RTX 5060-powered OLED gaming laptop for just $1,099 — HP's Omen Transcend features an Intel Core Ultra 7 255H 16-core CPU, 3K resolution, and WiFi 7",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/land-an-rtx-5060-powered-oled-gaming-laptop-for-just-usd1-099-hps-omen-transcend-features-an-intel-core-ultra-7-255h-16-core-cpu-3k-resolution-and-wifi-7",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T11:31:43+00:00",
    "summary": "A solid gaming laptop for just a smidgen over $1000. HP's Omen Transcend 14 with RTX 5060 is one of the best deals in HP's current flash sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/save-a-massive-90-percent-on-a-two-year-privadovpn-subscription-and-get-three-extra-months-for-free-huge-usd266-saving-on-this-affordable-vpn-with-a-strict-no-logs-policy-that-you-can-try-risk-free-for-30-days-for-just-usd30",
    "domain": "AI 算力 / 半导体",
    "title": "Save a massive 90% on a two-year PrivadoVPN subscription and get three extra months for free — huge $266 saving on this affordable VPN with a strict no-logs policy that you can try risk-free for 30 da",
    "url": "https://www.tomshardware.com/software/vpn/save-a-massive-90-percent-on-a-two-year-privadovpn-subscription-and-get-three-extra-months-for-free-huge-usd266-saving-on-this-affordable-vpn-with-a-strict-no-logs-policy-that-you-can-try-risk-free-for-30-days-for-just-usd30",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T11:28:58+00:00",
    "summary": "Secure a PrivadoVPN sub for just $30, down from as high as $296.73, giving you a two-year membership with a 90% discount along with three extra months completely free."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/korean-tech-workers-splash-cash-on-luxury-brands-after-bumper-bonus-payouts-luxury-goods-sales-rocket-nearly-150-percent-in-gyeonggi-province-semiconductor-belt",
    "domain": "AI 算力 / 半导体",
    "title": "Korean tech workers splash cash on luxury brands after bumper bonus payouts — luxury goods sales rocket nearly 150% in Gyeonggi Province semiconductor belt",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/korean-tech-workers-splash-cash-on-luxury-brands-after-bumper-bonus-payouts-luxury-goods-sales-rocket-nearly-150-percent-in-gyeonggi-province-semiconductor-belt",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T11:15:00+00:00",
    "summary": "South Korean media has noted a surge in spending on luxury goods following big bonus payouts to semiconductor workers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/noctuas-first-ever-aio-features-a-silenced-asetek-emma-v2-pump-and-nf-a12-14-fans-240mm-nl-lc1-starts-at-usd250-goes-up-to-usd325-for-420mm-cooler",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua's first-ever AIO features a silenced Asetek Emma V2 pump and NF-A12/14 fans — 240mm NL-LC1 starts at around $250, could cost $325 for 420mm cooler",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/noctuas-first-ever-aio-features-a-silenced-asetek-emma-v2-pump-and-nf-a12-14-fans-240mm-nl-lc1-starts-at-usd250-goes-up-to-usd325-for-420mm-cooler",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T10:59:00+00:00",
    "summary": "Noctua is officially entering the AIO market on June 16 with its new \"NL-LC1\" liquid cooler that starts at 220 EUR (around $250) for the 240mm variant. It features a customized Asetek Emma V2 pump wit"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-2-interviews-roundtables-and-the-first-day-at-the-nanggang-exhibition-center",
    "domain": "AI 算力 / 半导体",
    "title": "Tom's Hardware Unfiltered: Computex 2026, Day 2 — Interviews, roundtables, and the first day at the Nanggang Exhibition Center",
    "url": "https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-2-interviews-roundtables-and-the-first-day-at-the-nanggang-exhibition-center",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T10:39:54+00:00",
    "summary": "As Computex 2026 fully kicks off, our team finally enters the halls of the Nanggang Exhibition Center in Taipei in the latest in our series of daily blogs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building",
    "domain": "AI 算力 / 半导体",
    "title": "32GB of DDR5 now costs $375 minimum — AI shortage continues to squeeze PC building",
    "url": "https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T10:38:51+00:00",
    "summary": "32GB of DDR5 RAM can now no longer be found for less than $374.97."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/corsair-shows-off-gaming-mouse-with-dedicated-stream-deck-launch-button-wireless-mouse-also-gets-almost-50-hours-of-8k-battery-life",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair shows off gaming mouse with dedicated Stream Deck launch button — wireless mouse also gets almost 50 hours of 8K battery life",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/corsair-shows-off-gaming-mouse-with-dedicated-stream-deck-launch-button-wireless-mouse-also-gets-almost-50-hours-of-8k-battery-life",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T10:30:00+00:00",
    "summary": "Corsair showed off its Stream Deck-integrated gaming mouse, the Nightsword v2 Wireless SD, which has a dedicated Stream Deck launch button."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/memory-chip-crisis-hits-action-camera-industry-gopro-says-that-its-in-substantial-doubt-about-the-companys-ability-to-continue-in-regulatory-filings",
    "domain": "AI 算力 / 半导体",
    "title": "GoPro warns 'substantial doubt about the company’s ability to continue' in regulatory filings — AI memory shortage hits action camera maker",
    "url": "https://www.tomshardware.com/pc-components/ram/memory-chip-crisis-hits-action-camera-industry-gopro-says-that-its-in-substantial-doubt-about-the-companys-ability-to-continue-in-regulatory-filings",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T10:10:00+00:00",
    "summary": "Higher memory costs and lower sales is hitting GoPro hard. The company isn't filing for bankruptcy yet, but it might end up doing that if it does not resolve the issue sooner."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/amd-says-new-expo-ultra-low-latency-ddr5-memory-should-be-effectively-the-same-price-as-current-kits-feature-will-work-on-existing-chipsets-but-will-require-new-dimms",
    "domain": "AI 算力 / 半导体",
    "title": "AMD says new EXPO ‘Ultra Low Latency’ DDR5 memory should be 'effectively the same price' as current kits — feature will work on existing chipsets, but will require new DIMMs",
    "url": "https://www.tomshardware.com/pc-components/ram/amd-says-new-expo-ultra-low-latency-ddr5-memory-should-be-effectively-the-same-price-as-current-kits-feature-will-work-on-existing-chipsets-but-will-require-new-dimms",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T10:00:00+00:00",
    "summary": "AMD provides us with a bit more detail about its upcoming EXPO Ultra Low Latency mode, which should be available from leading memory partners soon."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-5-7-ghz-s-features-12-p-cores-and-a-desktop-class-lga1700-socket-unusual-server-cpu-prioritizes-clock-speed-over-core-count",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's 5.7 GHz Xeon 6377P features 12 P-cores and a desktop-class LGA1700 socket — unusual server CPU prioritizes clock speed over core count",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-5-7-ghz-s-features-12-p-cores-and-a-desktop-class-lga1700-socket-unusual-server-cpu-prioritizes-clock-speed-over-core-count",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T10:00:00+00:00",
    "summary": "Intel has unveiled the Xeon 6377P, a 12-core Bartlett Lake server processor featuring a 5.7 GHz boost clock, ECC support, and a 95W TDP. The unusual Xeon targets entry-level enterprise workloads where"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/github-copilot-customers-suffer-from-sticker-shock-as-microsoft-switches-to-usage-based-pricing-customers-report-up-to-100-fold-price-hikes",
    "domain": "AI 算力 / 半导体",
    "title": "Github Copilot customers report up to 100-fold price hikes — AI sticker shock bites as Microsoft switches to usage-based pricing",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/github-copilot-customers-suffer-from-sticker-shock-as-microsoft-switches-to-usage-based-pricing-customers-report-up-to-100-fold-price-hikes",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T09:55:12+00:00",
    "summary": "Github Copilot customers suffer from sticker shock syndrome as Microsoft switches to usage-based pricing — customers reporting ten- to hundred-fold price hikes"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/amds-gorgon-halo-pushes-on-device-ai-memory-to-192gb-as-dram-prices-hit-15-year-high",
    "domain": "AI 算力 / 半导体",
    "title": "The rise of local agentic computing faces a brutal reality: rising DRAM prices — RTX Spark, Gorgon Halo chips subject to 63% DRAM contract price hike this quarter",
    "url": "https://www.tomshardware.com/pc-components/dram/amds-gorgon-halo-pushes-on-device-ai-memory-to-192gb-as-dram-prices-hit-15-year-high",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T09:47:58+00:00",
    "summary": "DRAM contract prices are forecast to climb another 58% to 63% this quarter."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/astera-labs-showcases-320-lane-pcie-6-0-switch-for-vendor-agnostic-scaling-in-data-centers-up-to-80-accelerators-can-be-scaled-up-using-pcie-alone",
    "domain": "AI 算力 / 半导体",
    "title": "Astera Labs showcases 320-lane PCIe 6.0 switch for vendor-agnostic scaling in data centers — up to 80 accelerators can be scaled up using PCIe alone",
    "url": "https://www.tomshardware.com/desktops/servers/astera-labs-showcases-320-lane-pcie-6-0-switch-for-vendor-agnostic-scaling-in-data-centers-up-to-80-accelerators-can-be-scaled-up-using-pcie-alone",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T09:24:32+00:00",
    "summary": "Astera Labs has shown off the Scorpio X-Series 320-lane PCIe switch that promises to enable vendor-agnostic scale-up capability for AI infrastructure and disaggregated data center infrastructure."
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
    "id": "hn:48352951",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Announces RTX Spark",
    "url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date",
    "source": "rayhaanj",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-01T05:26:06+00:00",
    "summary": ""
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
    "points": 119,
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
    "points": 53,
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
    "id": "rss:https://www.theverge.com/tech/942054/shokz-clip-on-opendots-2-air-earbuds-wireless-headphones",
    "domain": "大厂 AI 动态",
    "title": "Shokz upgraded its open earbuds with better sound and a lighter design",
    "url": "https://www.theverge.com/tech/942054/shokz-clip-on-opendots-2-air-earbuds-wireless-headphones",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T07:00:00+00:00",
    "summary": "Shokz has announced two new versions of its open earbuds. Like the original OpenDots One that launched in May 2025, the new Shokz OpenDots 2 and OpenDots Air are both designed to be worn clipped to th"
  },
  {
    "id": "rss:https://www.theverge.com/games/942808/nintendo-switch-2-replaceable-battery-eu",
    "domain": "大厂 AI 动态",
    "title": "Nintendo confirms it will sell a new Switch 2 with replaceable battery in the EU",
    "url": "https://www.theverge.com/games/942808/nintendo-switch-2-replaceable-battery-eu",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T00:04:04+00:00",
    "summary": "Nintendo is planning to launch versions of Switch 2 hardware in the EU that will let users easily replace the battery. To meet its obligations from a new EU regulation that's set to go into effect on "
  },
  {
    "id": "rss:https://www.theverge.com/tech/942761/apple-texas-age-verification-app-store",
    "domain": "大厂 AI 动态",
    "title": "Apple is bringing age verification to Texas this week",
    "url": "https://www.theverge.com/tech/942761/apple-texas-age-verification-app-store",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T21:49:51+00:00",
    "summary": "Apple will introduce age verification in the App Store for users in Texas starting on Thursday, June 4th. The move, as spotted by MacRumors, comes just days after a federal appeals court allowed Texas"
  },
  {
    "id": "rss:https://www.theverge.com/tech/942748/wiim-releases-first-soundbar",
    "domain": "大厂 AI 动态",
    "title": "WiiM expands its whole-home ecosystem with a new soundbar",
    "url": "https://www.theverge.com/tech/942748/wiim-releases-first-soundbar",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T21:12:51+00:00",
    "summary": "WiiM, the audio company that's challenged the idea that audiophile-level performance requires a small loan, is expanding its whole-home ecosystem with the WiiM Bar, which releases in July. Much like i"
  },
  {
    "id": "rss:https://www.theverge.com/tech/942588/nvidia-rtx-spark-n2x-n3x-r2-d2-star-trek-star-wars-plan",
    "domain": "大厂 AI 动态",
    "title": "Nvidia is already planning N2X and N3X chips — the goal is the Star Trek computer",
    "url": "https://www.theverge.com/tech/942588/nvidia-rtx-spark-n2x-n3x-r2-d2-star-trek-star-wars-plan",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T20:03:50+00:00",
    "summary": "Just in case you were wondering, Nvidia's RTX Spark isn't supposed to be a one-off. The company is not just flirting with becoming the fifth high-profile vendor of consumer laptop chips to see if peop"
  },
  {
    "id": "rss:https://www.theverge.com/23769840/best-bluetooth-trackers",
    "domain": "大厂 AI 动态",
    "title": "The best Bluetooth trackers for Apple and Android phones",
    "url": "https://www.theverge.com/23769840/best-bluetooth-trackers",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T19:00:00+00:00",
    "summary": "Some people rarely lose things. Wallets are always exactly where they’re supposed to be, keys never go missing, and remotes never slip between the couch cushions. And then there’s the rest of us — the"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/939362/best-magsafe-qi2-2-batteries-power-banks",
    "domain": "大厂 AI 动态",
    "title": "The best Qi2 batteries for iPhone and Pixel",
    "url": "https://www.theverge.com/gadgets/939362/best-magsafe-qi2-2-batteries-power-banks",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T18:00:00+00:00",
    "summary": "Compact power banks have gotten a lot faster in the past year — and it’s not just their USB-C charging speeds that have received a boost. The newest Qi2.2-certified models can wirelessly charge an iPh"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/942629/as-ai-gets-better-it-reveals-an-empty-promise",
    "domain": "大厂 AI 动态",
    "title": "As AI gets better, it reveals an empty promise",
    "url": "https://www.theverge.com/ai-artificial-intelligence/942629/as-ai-gets-better-it-reveals-an-empty-promise",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T17:45:35+00:00",
    "summary": "This week we've got tandem hands-ons with Google's new Gemini AI agent - Spark - from my colleagues David Pierce and Jay Peters. Their takeaways are similar: It's so effective that it's scary. Spark k"
  },
  {
    "id": "rss:https://www.theverge.com/tech/942547/amazon-search-bar-ai-images",
    "domain": "大厂 AI 动态",
    "title": "Amazon&#8217;s search bar will invent AI-generated products you can&#8217;t buy",
    "url": "https://www.theverge.com/tech/942547/amazon-search-bar-ai-images",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T16:07:31+00:00",
    "summary": "Amazon's updated search bar will now show you AI-generated images of products as you describe them. For now, the in-app feature only surfaces AI images of clothing and home goods, allowing you to tap "
  },
  {
    "id": "rss:https://www.theverge.com/games/942520/playstation-wolverine-god-of-war-laufey-state-of-play-june-2026",
    "domain": "大厂 AI 动态",
    "title": "PlayStation is getting back to what it’s good at",
    "url": "https://www.theverge.com/games/942520/playstation-wolverine-god-of-war-laufey-state-of-play-june-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:30:15+00:00",
    "summary": "PlayStation used its most recent State of Play showcase to make it clear where its focus is. After a series of costly live-service stumbles, it's getting back to focusing on premium, narrative-driven,"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/benchmark-raises-its-first-ever-growth-fund-as-part-of-2b-capital-raise/",
    "domain": "大厂 AI 动态",
    "title": "Benchmark raises its first-ever growth fund as part of $2B capital raise",
    "url": "https://techcrunch.com/2026/06/03/benchmark-raises-its-first-ever-growth-fund-as-part-of-2b-capital-raise/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T03:52:15+00:00",
    "summary": "The legendary abandons its more than 20 year tradition of keeping its funds to about $425 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/firstclub-doubles-valuation-to-255m-in-nine-months-on-quality-first-grocery-bet/",
    "domain": "大厂 AI 动态",
    "title": "Quick commerce FirstClub doubles valuation to $255M in nine months",
    "url": "https://techcrunch.com/2026/06/03/firstclub-doubles-valuation-to-255m-in-nine-months-on-quality-first-grocery-bet/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T00:30:00+00:00",
    "summary": "The Bengaluru startup has crossed 1 million orders and reached a $50 million annualized GMV run rate within a year of launch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/lovable-signs-multi-year-deal-with-google-cloud-to-up-usage-5x-source-says/",
    "domain": "大厂 AI 动态",
    "title": "Lovable signs multiyear deal with Google Cloud to up usage 5x, source says",
    "url": "https://techcrunch.com/2026/06/03/lovable-signs-multi-year-deal-with-google-cloud-to-up-usage-5x-source-says/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T22:56:51+00:00",
    "summary": "Lovable and Google signed an expanded multiyear deal that involves a 5x expansion of Lovable's footprint on Google Cloud, and expanded access to Anthropic Claude."
  },
  {
    "id": "rss:https://techcrunch.com/video/defense-tech-is-flooded-with-money-but-whos-built-to-last/",
    "domain": "大厂 AI 动态",
    "title": "Defense tech is flooded with money, but who’s built to last?",
    "url": "https://techcrunch.com/video/defense-tech-is-flooded-with-money-but-whos-built-to-last/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T20:51:41+00:00",
    "summary": "Defense tech is red hot right now.&#160;Anduril&#160;and&#160;Mach Industries&#160;just doubled and quadrupled their valuations, respectively,&#160;and the U.S.&#160;government is proposing&#160;a&#16"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/uber-to-put-500-data-collection-vehicles-on-the-road-this-year/",
    "domain": "大厂 AI 动态",
    "title": "Uber to put 500 data-collection vehicles on the road this year",
    "url": "https://techcrunch.com/2026/06/03/uber-to-put-500-data-collection-vehicles-on-the-road-this-year/",
    "source": "Sean O'Kane, Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T20:08:28+00:00",
    "summary": "The modified Ioniq 5 will be loaded with sensors to capture data for Uber's new AV Labs division."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/alphabets-record-breaking-85b-raise-for-googles-ai-business-is-a-helluva-good-signal/",
    "domain": "大厂 AI 动态",
    "title": "Alphabet’s record-breaking $85B raise for Google’s AI business is a helluva good signal",
    "url": "https://techcrunch.com/2026/06/03/alphabets-record-breaking-85b-raise-for-googles-ai-business-is-a-helluva-good-signal/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T19:38:32+00:00",
    "summary": "If Alphabet's record-breaking $85 billion stock sale signals investor appetite for AI-related offerings, we can see that investors are ready to chow."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/meta-mercifully-spun-out-vr-fitness-game-supernatural-instead-of-just-killing-it/",
    "domain": "大厂 AI 动态",
    "title": "Meta mercifully spun out VR fitness game Supernatural instead of just killing it",
    "url": "https://techcrunch.com/2026/06/03/meta-mercifully-spun-out-vr-fitness-game-supernatural-instead-of-just-killing-it/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T19:22:53+00:00",
    "summary": "Meta appears to have listened to the Supernatural users who protested the app's sad fate after sweeping layoffs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/substacks-new-reply-rules-feature-lets-creators-control-how-people-respond/",
    "domain": "大厂 AI 动态",
    "title": "Substack’s new ‘Reply Rules’ feature lets creators control how people respond",
    "url": "https://techcrunch.com/2026/06/03/substacks-new-reply-rules-feature-lets-creators-control-how-people-respond/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T19:08:55+00:00",
    "summary": "Substack's new Reply Rules feature is currently available for all English-language publications and is designed to give creators greater control over how their audiences respond."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/googles-dreambeans-its-weirdest-named-ai-tool-to-date-will-turn-your-life-into-a-cartoon/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Dreambeans, its weirdest-named AI tool to date, will turn your life into a cartoon",
    "url": "https://techcrunch.com/2026/06/03/googles-dreambeans-its-weirdest-named-ai-tool-to-date-will-turn-your-life-into-a-cartoon/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T19:07:42+00:00",
    "summary": "Dreambeans is a curated list of AI-illustrated \"stories\" culled from the personal data in your Google account."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/ultrahuman-says-hackers-accessed-customers-wellness-data-via-internal-tool/",
    "domain": "大厂 AI 动态",
    "title": "Ultrahuman says hackers accessed customers’ wellness data via internal tool",
    "url": "https://techcrunch.com/2026/06/03/ultrahuman-says-hackers-accessed-customers-wellness-data-via-internal-tool/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T17:30:52+00:00",
    "summary": "The breach at wearable ring maker Ultrahuman stemmed from credentials stolen from a malware-infected employee laptop."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/carvana-ties-up-with-bezos-backed-slate-auto-as-it-plans-new-car-sales/",
    "domain": "大厂 AI 动态",
    "title": "Carvana ties up with Bezos-backed Slate Auto as it plans new car sales",
    "url": "https://techcrunch.com/2026/06/03/carvana-ties-up-with-bezos-backed-slate-auto-as-it-plans-new-car-sales/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T17:25:51+00:00",
    "summary": "Carvana was granted a warrant to buy shares in Slate last year, according to documents obtained by TechCrunch. Guggenheim Partners CEO Mark Walter is heavily invested in both companies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/instagram-is-alerting-users-who-were-targeted-by-hackers-during-ai-chatbot-attacks/",
    "domain": "大厂 AI 动态",
    "title": "Instagram is alerting users who were targeted by hackers during AI chatbot attacks",
    "url": "https://techcrunch.com/2026/06/03/instagram-is-alerting-users-who-were-targeted-by-hackers-during-ai-chatbot-attacks/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T16:12:06+00:00",
    "summary": "Hackers appeared to take over victims’ accounts even after Meta said it fixed its AI-powered support chatbot, which granted hackers access to victims’ accounts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/amazon-will-show-ai-product-images-when-you-search-for-some-reason/",
    "domain": "大厂 AI 动态",
    "title": "Amazon will show AI product images when you search for some reason",
    "url": "https://techcrunch.com/2026/06/03/amazon-will-show-ai-product-images-when-you-search-for-some-reason/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:50:26+00:00",
    "summary": "Amazon will use visual search and AI to show AI-generated product images that match your search queries. The retailer says it will help guide users to products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/still-facing-copyright-lawsuits-ai-music-generator-suno-raises-another-400m/",
    "domain": "大厂 AI 动态",
    "title": "Still facing copyright lawsuits, AI music generator Suno raises another $400M",
    "url": "https://techcrunch.com/2026/06/03/still-facing-copyright-lawsuits-ai-music-generator-suno-raises-another-400m/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:31:42+00:00",
    "summary": "The prominent AI music-generation startup is now valued at over $5.4 billion -- about seven months ago, it raised at a $2.45 billion valuation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/these-two-founders-left-goldman-and-meta-to-build-voice-ai-for-markets-everyone-else-overlooked/",
    "domain": "大厂 AI 动态",
    "title": "These two founders left Goldman and Meta to build voice AI for markets everyone else overlooked",
    "url": "https://techcrunch.com/2026/06/03/these-two-founders-left-goldman-and-meta-to-build-voice-ai-for-markets-everyone-else-overlooked/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T15:00:00+00:00",
    "summary": "The startup's own stack for Africa and Middle East is now handling more than 17,000 calls per day."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/gitlab-cuts-14-of-staff-as-it-scales-its-platform-to-serve-ai-workloads/",
    "domain": "大厂 AI 动态",
    "title": "GitLab cuts 14% of staff as it scales its platform to serve AI workloads",
    "url": "https://techcrunch.com/2026/06/03/gitlab-cuts-14-of-staff-as-it-scales-its-platform-to-serve-ai-workloads/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T14:59:30+00:00",
    "summary": "The company is reducing its workforce as it exits 22 countries, reduces management layers, and invests in its infrastructure to scale its platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/",
    "domain": "大厂 AI 动态",
    "title": "Publishers will be able to opt out of AI Search, thanks to new regulation",
    "url": "https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T14:58:33+00:00",
    "summary": "U.K. regulators are requiring Google offer a tool allowing website publishers to opt-out of generative AI search features. The option will be tested in the U.K. then rolled out globally."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/tiktok-launches-tiktok-pro-events-an-app-for-cultural-moments-like-the-fifa-world-cup/",
    "domain": "大厂 AI 动态",
    "title": "TikTok launches TikTok Pro Events, an app for cultural moments like the FIFA World Cup",
    "url": "https://techcrunch.com/2026/06/03/tiktok-launches-tiktok-pro-events-an-app-for-cultural-moments-like-the-fifa-world-cup/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T14:04:38+00:00",
    "summary": "The app allows users to engage with other fans, explore trending videos, and access curated creator feeds."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/the-worst-hacks-and-breaches-of-2026-so-far/",
    "domain": "大厂 AI 动态",
    "title": "The worst hacks and breaches of 2026 (so far)",
    "url": "https://techcrunch.com/2026/06/03/the-worst-hacks-and-breaches-of-2026-so-far/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T14:02:45+00:00",
    "summary": "From a massive DOGE data breach and the hacking of critical energy and water systems to the hack of an FBI surveillance system, here are the most damaging security incidents and data breaches of 2026."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/03/meet-wander-a-stumbleupon-inspired-tool-for-discovering-the-small-web/",
    "domain": "大厂 AI 动态",
    "title": "Meet Wander, a StumbleUpon-inspired tool for discovering the ‘small web’",
    "url": "https://techcrunch.com/2026/06/03/meet-wander-a-stumbleupon-inspired-tool-for-discovering-the-small-web/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T14:00:58+00:00",
    "summary": "This open source community project lets you create a StumbleUpon-like experience for recommending your favorite sites."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-nvidia-ai-pc-project-solara-microsoft-ai/",
    "domain": "大厂 AI 动态",
    "title": "The Nvidia AI PC, Project Solara, Microsoft AI",
    "url": "https://stratechery.com/2026/the-nvidia-ai-pc-project-solara-microsoft-ai/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-03T10:00:00+00:00",
    "summary": "The Nvidia AI PC feels like a relic of another AI era; Microsoft's vision for devices at Build was much more compelling."
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
    "id": "hn:48373909",
    "domain": "股票",
    "title": "Morningstar values SpaceX at $780B, half its IPO target",
    "url": "https://www.reuters.com/business/media-telecom/morningstar-values-spacex-780-billion-half-its-ipo-target-2026-06-02/",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 210,
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
    "points": 82,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48394034",
    "domain": "股票",
    "title": "The SpaceX IPO Will Be the Theft of the Century",
    "url": "https://montanaskeptic.substack.com/p/the-spacex-ipo-will-be-the-theft",
    "source": "400thecat",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-06-04T04:52:37+00:00",
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
    "points": 46,
    "published_at": "2026-06-03T21:06:30+00:00",
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
    "id": "hn:48382926",
    "domain": "股票",
    "title": "Goldman Sachs CEO says markets in 'greed' mode as AI companies seek billions",
    "url": "https://www.cnbc.com/2026/06/02/goldman-ceo-david-solomon-greed-mode-ai-firms-ipos.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-03T12:08:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48383625",
    "domain": "股票",
    "title": "Dell inks $9.7B Pentagon contract after Trump acquires stock",
    "url": "https://www.washingtonpost.com/politics/2026/05/28/dell-inks-97-billion-pentagon-contract-after-trump-acquires-stock-praises-company/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-03T13:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390904",
    "domain": "股票",
    "title": "SpaceX Sets Price for $1.77T IPO",
    "url": "https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html",
    "source": "gen220",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-06-03T22:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48368083",
    "domain": "股票",
    "title": "Ask HN: What is your opinion on index rule changes to accommodate Mega-Cap IPOs?",
    "url": "https://news.ycombinator.com/item?id=48368083",
    "source": "figmert",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-06-02T09:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377119",
    "domain": "股票",
    "title": "Short Seller (Andrew Left) Convicted for $21M Stock Market Manipulation Scheme",
    "url": "https://www.justice.gov/opa/pr/activist-short-seller-convicted-21m-stock-market-manipulation-scheme",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-02T22:19:48+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3773858",
    "domain": "股票",
    "title": "博通AI指引“不够炸裂”引发抛售，华尔街却喊错杀：真正爆发在2027年后",
    "url": "https://wallstreetcn.com/articles/3773858",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T07:51:56+00:00",
    "summary": "德银认为，市场低估了博通的长期潜力：订单能见度已延伸至2028年，本身已释放积极信号，预计2027财年AI营收达到1250亿美元，高于公司指引，2028年将飙升至1900亿美元，这才是博通AI故事的真正主轴。"
  },
  {
    "id": "wscn:3773323",
    "domain": "股票",
    "title": "mSAP：M10如何引领PCB新材料迭代升级？",
    "url": "https://wallstreetcn.com/premium/articles/3773323?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T07:45:40+00:00",
    "summary": "随着AI算力架构由CoWoS向CoWoP升级，PCB产业链正经历一场技术与价值的双重跃迁。mSAP工艺已成为1.6T及以上光模块的必选，而M8-M10等级的高速CCL材料正成为行业竞争的制高点。"
  },
  {
    "id": "wscn:3773843",
    "domain": "股票",
    "title": "AI交易降温，韩股重挫1.8%，现货黄金上涨1%，比特币跳水",
    "url": "https://wallstreetcn.com/articles/3773843",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T07:43:46+00:00",
    "summary": "纳斯达克100指数期货下滑0.5%，此前博通在盘后交易中重挫14%，最新业绩展望大幅低于投资者预期，并发出向AI客户转型进展慢于市场预期的信号。比特币滑落至约64000美元，为今年2月以来最低；黄金因逢低买盘涌入上涨约1%；布伦特原油下跌约1%至97美元/桶附近。"
  },
  {
    "id": "wscn:3773860",
    "domain": "股票",
    "title": "5年100亿美元！IBM加码量子计算，目标2029年交付世界第一台“大规模容错量子计算机”",
    "url": "https://wallstreetcn.com/articles/3773860",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T07:41:40+00:00",
    "summary": "IBM宣布未来五年投入超100亿美元，加速量子计算产业化进程，目标在2029年交付全球首台大规模容错量子计算机。美国政府此前已提供10亿美元专项资助，支持其在纽约设立美国首家纯量子代工厂Anderon。结合园区扩建与平台化商业模式，IBM正构建涵盖硬件、制造与生态的完整量子战略。"
  },
  {
    "id": "wscn:3773859",
    "domain": "股票",
    "title": "商务部：美滥用出口管制冲击全球半导体产供链稳定",
    "url": "https://wallstreetcn.com/articles/3773859",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T07:14:04+00:00",
    "summary": "新闻发言人表示，近年来美方不断以国家安全为由滥用出口管制，严重损害中国企业正当权益，严重破坏国际经贸秩序，严重冲击全球半导体产业链供应链稳定，中方对此一贯反对。中方反对各种形式的单边限制措施，包括以“强迫劳动”为由对华实施的一系列贸易限制措施，对此中方已多次表达严正立场。"
  },
  {
    "id": "wscn:3773851",
    "domain": "股票",
    "title": "单日大跌超10%，软银重押OpenAI的代价开始显现？",
    "url": "https://wallstreetcn.com/articles/3773851",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T07:12:25+00:00",
    "summary": "软银单日暴跌逾11%，将孙正义的AI豪赌推上风口浪尖。这家日本科技巨头有息债务高达1040亿美元，对OpenAI的押注占比或达投资组合30%。标普已将其信用展望下调至负面，分析师直言：\"买入软银，本质上是杠杆押注OpenAI。\"WeWork百亿美元的前车之鉴犹在，这场豪赌究竟是财富杠杆，还是流动性危机的引爆点？"
  },
  {
    "id": "wscn:3773856",
    "domain": "股票",
    "title": "金融市场、风控干将履新，浙商银行高管班子完成最后拼图",
    "url": "https://wallstreetcn.com/articles/3773856",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:59:20+00:00",
    "summary": "6月3日，浙商银行发布公告称，公司收到国家金融监督管理总局批复，周伟新、潘华枫担任该行副行长的任职资..."
  },
  {
    "id": "wscn:3773855",
    "domain": "股票",
    "title": "海尔25年来首次减持青岛银行，产业股东退居、国资格局渐成",
    "url": "https://wallstreetcn.com/articles/3773855",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:58:50+00:00",
    "summary": "25年前，海尔以产业资本身份参与青岛银行前身的改制重组；25年后，这笔长期投资首次迎来兑现时刻。\n6..."
  },
  {
    "id": "wscn:3773849",
    "domain": "股票",
    "title": "拨开大宗商品的迷雾，了解最真实的市场【对话培风客 上篇】",
    "url": "https://wallstreetcn.com/premium/articles/3773849?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:58:20+00:00",
    "summary": "逼仓的真相就是：钱比货多"
  },
  {
    "id": "wscn:3773854",
    "domain": "股票",
    "title": "掌舵七年后到龄退休，贵阳银行董事长卸任、行长代履职责",
    "url": "https://wallstreetcn.com/articles/3773854",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:58:06+00:00",
    "summary": "6月3日，贵阳银行发布公告称，董事长张正海因到龄退休，已向董事会提交辞职报告，辞任后，张正海不再担任..."
  },
  {
    "id": "wscn:3773853",
    "domain": "股票",
    "title": "中标利率异常引发“乌龙指”猜测，农发行紧急取消一笔政策性金融债发行",
    "url": "https://wallstreetcn.com/articles/3773853",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:57:35+00:00",
    "summary": "近日，银行间债券市场出现了一幕并不常见的场景。\n6月2日，农发行续发的一期政策性金融债招标结果公布后..."
  },
  {
    "id": "wscn:3773834",
    "domain": "股票",
    "title": "台积电魏哲家：数年内都无法满足芯片需求，资本开支高点“我也不知道”、“没看到停下的指标”",
    "url": "https://wallstreetcn.com/articles/3773834",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:54:55+00:00",
    "summary": "股东大会上，董事长魏哲家预计，台积电全年营收增速维持超30%预期；Q2毛利率指引65.5%至67.5%。他坦言资本支出高峰“我也不知道”，但强调“现在没看到停止的指标”；员工分红连续三年增超30%，承诺“没有天花板”。他指出，token消耗量激增推升算力需求，自动驾驶与机器人更构成下一波长期增长引擎。"
  },
  {
    "id": "wscn:3773847",
    "domain": "股票",
    "title": "博通：大佬vs大佬，ASIC阵营要分家了？",
    "url": "https://wallstreetcn.com/articles/3773847",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:31:13+00:00",
    "summary": "市场开始重新审视ASIC阵营内部分化：博通偏“网络+ASIC”，Marvell受互连叙事强化，而云厂商自研加速或导致供应链重构，“大佬之间的分化”正在显现。"
  },
  {
    "id": "wscn:3773846",
    "domain": "股票",
    "title": "美股已无恐慌，只剩FOMO！华尔街机构：这一幕像极了1998年",
    "url": "https://wallstreetcn.com/articles/3773846",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:27:53+00:00",
    "summary": "美股科技板块正经历1990年以来最强劲10周涨幅，累计飙升44.6%，VIX跌至年内最低，市场恐惧已荡然无存，唯剩\"踏空焦虑\"。然而警报已然拉响：RSI触及82、较200日均线偏离28%的极端组合，历史上仅出现十次，多数以回调告终。更令人警惕的是，时间轴恰与1998年7月高度吻合——彼时科技板块随后重挫逾20%。"
  },
  {
    "id": "wscn:3773844",
    "domain": "股票",
    "title": "警惕“羊群效应”！韩国财长：必要时出手干预汇市，对杠杆化炒股感到担心",
    "url": "https://wallstreetcn.com/articles/3773844",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:19:25+00:00",
    "summary": "韩元跌至两个月低点、股市高位上行之际，韩国财政部长联合央行与金融监管机构紧急发声：必要时将\"立即采取措施\"遏制外汇过度波动，并点名警示股市杠杆风险。融资贷款余额创20年新高、散户未成年开户暴增十倍，韩国政策层对泡沫的容忍度正逼近临界点。"
  },
  {
    "id": "wscn:3773842",
    "domain": "股票",
    "title": "报道：日本央行正考虑在6月加息，并有可能在2026年年内再次加息",
    "url": "https://wallstreetcn.com/articles/3773842",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:13:29+00:00",
    "summary": "报道称，日本央行官员可能在6月16日政策会议上讨论将基准利率上调25个基点至1%的方案。官员们认为此后仍存在进一步加息空间，理由是实际利率依然处于低位，且通胀上行风险持续存在。"
  },
  {
    "id": "wscn:3773749",
    "domain": "股票",
    "title": "稀土乘风起：国之重器战略升级，管控提级扩大供需缺口",
    "url": "https://wallstreetcn.com/premium/articles/3773749?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T06:03:48+00:00",
    "summary": "2026年稀土市场呈现“供给刚性锁死、需求多点开花”的双轮驱动格局。缅甸停产导致中重稀土供应出现实质性断档，国内配额增速放缓至个位数，供给弹性被系统性压缩；需求端新能源汽车、工业机器人、节能家电稳步增长，叠加人形机器人打开远期万亿级应用空间，氧化镨钕价格中枢有望保持高位震荡。"
  },
  {
    "id": "wscn:3773845",
    "domain": "股票",
    "title": "鸿海宣布与英特尔达成战略合作，将共同开发AI平台",
    "url": "https://wallstreetcn.com/articles/3773845",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T05:36:00+00:00",
    "summary": "英特尔联手鸿海、SambaNova亮相Computex 2026，推出机架级AI基础设施，同步发布首款采用18A制程的Xeon 6+处理器。随着AI从训练转向推理，CPU与GPU比例正由1:4向1:1演变，英特尔借势布局，意在抢夺推理时代数据中心的核心算力话语权。"
  },
  {
    "id": "wscn:3773839",
    "domain": "股票",
    "title": "SemiAnalysis深度详解马斯克的“太空算力梦”：真正的瓶颈是什么？何时能上天？",
    "url": "https://wallstreetcn.com/articles/3773839",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:54:43+00:00",
    "summary": "马斯克的\"太空算力梦\"正从科幻走向经济测算，但账并不好算。SemiAnalysis最新报告显示，目前同等GPU集群太空部署成本是地面的3.6倍，\"免费太阳能\"\"免费散热\"均存在严重高估。基准情景下成本平价要等到2040年，而真正卡住AI扩张的，是芯片而非电力。地面数据中心新增容量在2028年见顶，同时芯片生产扩张继续推进，成本平价可能提前至2030年代初。"
  },
  {
    "id": "wscn:3773841",
    "domain": "股票",
    "title": "微信给AI手机留了一道门",
    "url": "https://wallstreetcn.com/articles/3773841",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:21:48+00:00",
    "summary": "微信妥协了？"
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
    "id": "hn:48304589",
    "domain": "股票",
    "title": "SpaceX IPO: Did Musk Rig the Stock Market? [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-05-28T04:42:25+00:00",
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
    "id": "hn:48315925",
    "domain": "股票",
    "title": "Dell Gets a $9.7B Defense Contract. Trump's Portfolio Stands to Benefit",
    "url": "https://www.nytimes.com/2026/05/28/us/politics/trump-dell-stock-purchases.html",
    "source": "spankibalt",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-05-28T21:42:12+00:00",
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
    "id": "hn:48384810",
    "domain": "金融",
    "title": "Tesla retroactively added 'supervised' to FSD contracts owners signed years ago",
    "url": "https://electrek.co/2026/06/03/tesla-retroactively-modified-fsd-contracts-supervised/",
    "source": "breve",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-06-03T14:43:52+00:00",
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
    "points": 28,
    "published_at": "2026-06-02T15:58:07+00:00",
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
    "id": "rss:https://arxiv.org/abs/2606.04153",
    "domain": "金融",
    "title": "A new decomposition approach to modeling financial returns: Conditioning sign on magnitude",
    "url": "https://arxiv.org/abs/2606.04153",
    "source": "Ars\\`ene Brou, Richard Luger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04153v1 Announce Type: new Abstract: Changes in volatility contain valuable information about the likelihood of positive versus negative returns. We propose a new approach to modeling finan"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04235",
    "domain": "金融",
    "title": "A Certified Higher Order Quantum Framework for CSA and Margin-Aware Collateral Optimization",
    "url": "https://arxiv.org/abs/2606.04235",
    "source": "Tao Jin, Stuart Florescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04235v1 Announce Type: new Abstract: Collateral allocation for uncleared derivatives is a legally constrained and operationally discrete optimization problem. Institutions must satisfy marg"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04258",
    "domain": "金融",
    "title": "Anticipatory Portfolio Optimization",
    "url": "https://arxiv.org/abs/2606.04258",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04258v1 Announce Type: new Abstract: A portfolio is \\emph{anticipatory} when its optimizer acts on a richer model than the myopic, price-taking estimator used to calibrate it. Enrichment ma"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04715",
    "domain": "金融",
    "title": "How the interpolation of life tables affects the decomposition of life insurance surplus",
    "url": "https://arxiv.org/abs/2606.04715",
    "source": "Mintod\\^e Nicod\\`eme Atchad\\'e, Marcus C. Christiansen, Friedrich Hubalek, Gero Junike",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04715v1 Announce Type: new Abstract: The surplus of a life insurance policy depends on both systematic changes in mortality risk and financial changes. We propose to decompose the surplus b"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04217",
    "domain": "金融",
    "title": "Polymarket-v1 Database",
    "url": "https://arxiv.org/abs/2606.04217",
    "source": "Boka Qin, Rui Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04217v1 Announce Type: cross Abstract: We introduce the Polymarket-v1 Database: the complete on-chain trade archive of Polymarket's first-generation CTF Exchange on Polygon, spanning 2022-1"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04574",
    "domain": "金融",
    "title": "Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning",
    "url": "https://arxiv.org/abs/2606.04574",
    "source": "Damian Lebied\\'z, Robert \\'Slepaczuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04574v1 Announce Type: cross Abstract: This study aims to determine whether the application of Deep Reinforcement Learning (DRL) as a specialized execution overlay can enhance pair trading "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04576",
    "domain": "金融",
    "title": "ReSGA: A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall",
    "url": "https://arxiv.org/abs/2606.04576",
    "source": "Yichi Zhang, Ke Zhu, Zhoufan Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04576v1 Announce Type: cross Abstract: Learning Value-at-Risk (VaR) and Expected Shortfall (ES) is important for managing financial risks effectively. Existing approaches with limited param"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04916",
    "domain": "金融",
    "title": "Worker Utility as Hysteresis: A Preisach Model of Transaction Acceptance in Gig Labour Markets",
    "url": "https://arxiv.org/abs/2606.04916",
    "source": "Piotr Frydrych",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04916v1 Announce Type: cross Abstract: Worker utility is not observed -- only its consequence is. Each gig transaction produces a single bit: accepted or rejected. We argue this structure p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04959",
    "domain": "金融",
    "title": "Fairness and Strategy-Proofness in Automated Market Makers",
    "url": "https://arxiv.org/abs/2606.04959",
    "source": "Frank M. V. Feys",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04959v1 Announce Type: cross Abstract: No deployed automated market maker lets its liquidity providers vote on the trading function. We show this is structural, not an oversight. On the wei"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04978",
    "domain": "金融",
    "title": "Probing Outcome-Level Resemblance and Mechanism-Level Alignment in LLM Risk Decisions: Evidence from the St. Petersburg Game",
    "url": "https://arxiv.org/abs/2606.04978",
    "source": "Chensong Huang, Changyu Chen, Chenwei Lin, Hanjia Lyu, Xian Xu, Jiebo Luo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.04978v1 Announce Type: cross Abstract: LLMs can appear cautious in risk decision-making tasks, yet cautious-looking outputs do not necessarily indicate alignment with human decision-making "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05138",
    "domain": "金融",
    "title": "Generating Financial Time Series by Matching Random Convolutional Features",
    "url": "https://arxiv.org/abs/2606.05138",
    "source": "Konrad J. Mueller, Nikita Zozoulenko, Ben Wood, Thomas Cass, Lukas Gonon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.05138v1 Announce Type: cross Abstract: Generating realistic financial time series is challenging as training data is often limited to a single historical path. With such scarce data, overfi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2310.12272",
    "domain": "金融",
    "title": "Peer Effects in Consideration and Preferences",
    "url": "https://arxiv.org/abs/2310.12272",
    "source": "Nail Kashaev, Natalia Lazzati, Ruli Xiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2310.12272v4 Announce Type: replace Abstract: We develop a general model of discrete choice that incorporates peer effects in preferences and consideration sets. We characterize the equilibrium "
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.03504",
    "domain": "金融",
    "title": "Capacity, Technology Portfolios, and the Paradox of Concentration",
    "url": "https://arxiv.org/abs/2407.03504",
    "source": "Michele Fioretti, Junnan He, Jorge Tamayo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2407.03504v3 Announce Type: replace Abstract: Does limiting the largest firm's capacity always lower prices? We model firms competing in supply schedules with multiple technologies, each defined"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.18723",
    "domain": "金融",
    "title": "Deviations from Normality in a Financial Model without Short-selling",
    "url": "https://arxiv.org/abs/2505.18723",
    "source": "Nahuel I. Arca",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2505.18723v2 Announce Type: replace Abstract: We present a variation of the well-known binomial model of asset prices. This variation is based on the interaction of a finite number of investors "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.09598",
    "domain": "金融",
    "title": "Ancestral origins of environmental (in)attention",
    "url": "https://arxiv.org/abs/2509.09598",
    "source": "C\\'esar Barilla, Palaash Bhargava",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2509.09598v2 Announce Type: replace Abstract: How does the climatic experience of past generations affect today's attitudes towards environmental issues? Using empirical evidence spanning multip"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.20047",
    "domain": "金融",
    "title": "Pricing Variance Swap for Multi-Asset Stochastic Volatility Models",
    "url": "https://arxiv.org/abs/2510.20047",
    "source": "Semere Gebresilassie, Mulue Gebreslasie, Minglian Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2510.20047v2 Announce Type: replace Abstract: This paper develops a novel framework for modeling variance swap of multi-asset stochastic volatility models by employing determinant-based instanta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.14852",
    "domain": "金融",
    "title": "Recovering State Prices from Options",
    "url": "https://arxiv.org/abs/2601.14852",
    "source": "Tjeerd De Vries",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2601.14852v2 Announce Type: replace Abstract: Extracting the joint risk-neutral distribution from option prices has remained an open problem since Ross (1976). We propose a projection-based esti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.14378",
    "domain": "金融",
    "title": "A Computational Framework for Financial Structures",
    "url": "https://arxiv.org/abs/2602.14378",
    "source": "Antonio Scala, Andrea Monaco",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2602.14378v2 Announce Type: replace Abstract: Financial structures transform stochastic cash-flow representations of underlying economic activities into ordered payments across multiple claims t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.02503",
    "domain": "金融",
    "title": "Pay Beliefs and the Amenity-Pay Tradeoff",
    "url": "https://arxiv.org/abs/2606.02503",
    "source": "Martin Eckhoff Andresen, Manudeep Bhuller, Alfred L{\\o}vgren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.02503v2 Announce Type: replace Abstract: This paper studies how workers' beliefs about pay shape the tradeoffs between pay and workplace amenities. We design a multi-stage incentivized surv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2107.01629",
    "domain": "金融",
    "title": "From Live to Recording: Consumer Demand and Response to Price Across the Livestreaming Lifecycle",
    "url": "https://arxiv.org/abs/2107.01629",
    "source": "Ziwei Cong, Jia Liu, Puneet Manchanda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2107.01629v3 Announce Type: replace-cross Abstract: Livestreaming has evolved into a thriving industry where creators can directly monetize and engage with their audiences and followers. In prac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.02369",
    "domain": "金融",
    "title": "Fair Distribution of Digital Payments: Balancing Transaction Flows for Regulatory Compliance",
    "url": "https://arxiv.org/abs/2601.02369",
    "source": "Ashlesha Hota, Shashwat Kumar, Daman Deep Singh, Abolfazl Asudeh, Palash Dey, Abhijnan Chakraborty",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2601.02369v2 Announce Type: replace-cross Abstract: The concentration of digital payment transactions in just two UPI apps like PhonePe and Google Pay has raised concerns of duopoly in India s d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.19225",
    "domain": "金融",
    "title": "FinTradeBench: A Financial Reasoning Benchmark for LLMs",
    "url": "https://arxiv.org/abs/2603.19225",
    "source": "Yogesh Agrawal, Aniruddha Dutta, Md Mahadi Hasan, Santu Karmaker, Aritra Dutta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2603.19225v3 Announce Type: replace-cross Abstract: Real-world financial decision-making is a challenging problem that requires reasoning over heterogeneous signals, including company fundamenta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.17623",
    "domain": "金融",
    "title": "Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization: An Operational Decomposition Audit",
    "url": "https://arxiv.org/abs/2605.17623",
    "source": "Luis Lozano",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2605.17623v2 Announce Type: replace-cross Abstract: We audit the operational decomposition of D-Wave's hybrid quantum-classical portfolio-optimization service on cardinality-constrained mean-var"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.01979",
    "domain": "金融",
    "title": "A Simple Hierarchical Causality Primer",
    "url": "https://arxiv.org/abs/2606.01979",
    "source": "Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T04:00:00+00:00",
    "summary": "arXiv:2606.01979v2 Announce Type: replace-cross Abstract: We provide a brief primer for the idea behind formalising hierarchical causality in the context of complex systems. Here actors are not simply"
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
  }
]
```
