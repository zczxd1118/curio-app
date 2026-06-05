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

- 今日日期：`2026-06-05`
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
  "date": "2026-06-05",
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
    "points": 935157,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 599715,
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
    "points": 366899,
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
    "points": 342055,
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
    "points": 313642,
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
    "points": 233424,
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
    "points": 224802,
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
    "points": 210637,
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
    "points": 173361,
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
    "points": 151659,
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
    "points": 144297,
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
    "points": 142656,
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
    "points": 140749,
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
    "points": 131762,
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
    "points": 95768,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 61509,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 55972,
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
    "points": 52780,
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
    "points": 50601,
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
    "points": 48786,
    "published_at": "2026-03-10T10:18:17+00:00",
    "summary": "深度解析GitHub热门项目mcp2cli——一个能把任何MCP服务器或OpenAPI规范变成命令行工具的Python项目。它用&quot;懒发现&quot;机制，把MCP协议的token浪费从数十万降到几千，节省高达99%。整个核心实现只有一个Python文件，却支持三种接入模式、OAuth认证和智能缓存。发布仅一天就获得372颗星，但社区也有激烈争议：CLI真的能取代MCP吗？准确率会不会受影"
  },
  {
    "id": "bvid:BV1thQPYfEYC",
    "domain": "AI",
    "title": "全流程演示Cursor + Blender MCP实现自动3D建模",
    "url": "http://www.bilibili.com/video/av114155835103525",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 42887,
    "published_at": "2025-03-13T15:31:17+00:00",
    "summary": "自动3D建模这个例子，是不是让大家一下子就看懂MCP的用途了。\n.\n后面会实测更多Cursor+MCP的更多玩法，欢迎继续围观\n.\n欢迎加入我的知识星球，有问必答：https://t.zsxq.com/fD4Fb\n.\nblender mcp项目：https://github.com/ahujasid/blender-mcp/tree/main"
  },
  {
    "id": "bvid:BV1AodfByE7D",
    "domain": "AI",
    "title": "写了十八年代码的老码农使用 Codex Vibe Coding 后总结了哪些重要经验？",
    "url": "http://www.bilibili.com/video/av116431882558436",
    "source": "牧云踏歌",
    "platform": "bilibili",
    "points": 41836,
    "published_at": "2026-04-19T14:43:21+00:00",
    "summary": "一份面向团队与个人开发者的 Codex 协作手册，重点沉淀高频场景下的方法、模板和可复用骨架。"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 37590,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1ASRjBxEVx",
    "domain": "AI",
    "title": "6 小时 Vibe Coding 全记录，做个 Web 版 Typora",
    "url": "http://www.bilibili.com/video/av116503185722308",
    "source": "Koala聊开源",
    "platform": "bilibili",
    "points": 36933,
    "published_at": "2026-05-02T04:56:51+00:00",
    "summary": "在这期视频中，我们带着大家一起体验了 6 小时 Vibe Coding 马拉松，在这个过程中，我们通过 TDD + Harness 方法，逐步完成了一个 Web 版 Typora 的移植。视频从项目目标的明确到技术选型，展示了如何在实践中解决一系列复杂问题，如何用测试驱动约束 Agent 行为，并逐步优化架构。通过多个核心测试的突破，我们最终实现了多个 Typora 语法行为的复刻。"
  },
  {
    "id": "bvid:BV13K1YBtE6e",
    "domain": "AI",
    "title": "【GMM】MCP 使用说明",
    "url": "http://www.bilibili.com/video/av115485010168640",
    "source": "3DM小莫",
    "platform": "bilibili",
    "points": 36013,
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
    "points": 33930,
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
    "points": 29538,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22480,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 22178,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1duRMBDEh9",
    "domain": "AI",
    "title": "手把手带你从0搭建第二大脑｜Obsidian × AI Agent 全流程实操教程",
    "url": "http://www.bilibili.com/video/av116498135916107",
    "source": "Martina在进化",
    "platform": "bilibili",
    "points": 18575,
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
    "points": 17222,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1HaVh6fEhn",
    "domain": "AI",
    "title": "AI编程进阶必修课！Claude Code+Harness AI 工程化实战！电商项目全流程落地，规范开发、代码治理、简历加分一站式吃透",
    "url": "http://www.bilibili.com/video/av116656764421367",
    "source": "图灵程序员诸葛",
    "platform": "bilibili",
    "points": 16306,
    "published_at": "2026-05-29T08:01:23+00:00",
    "summary": "大模型资料看这里聆取https://www.bilibili.com/read/cv49754608/?jump_opus=1"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 14705,
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
    "points": 13493,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12177,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1AnVm6GEcy",
    "domain": "AI",
    "title": "用嘴编程（Vibe Coding）时代来了，2026程序员正在“消失”！",
    "url": "http://www.bilibili.com/video/av116685386418858",
    "source": "码士集团_马小菲",
    "platform": "bilibili",
    "points": 11442,
    "published_at": "2026-06-03T09:17:15+00:00",
    "summary": "马士兵1v1免费程序员IT职业规划：转型AI大模型，方向迷茫，面试突击，跳槽涨薪，大龄问题(中年危机)，裁员找工作，考研失败，想规划就业路线/学习路线/大厂路线/转行IT..."
  },
  {
    "id": "bvid:BV1hEVd6yEcn",
    "domain": "AI",
    "title": "【2026最新】全B站最详细AI Agent开发教程，手把手教你搭建企业级Agent智能体！从入门到实战，学完即就业，带你玩转AI Agent！",
    "url": "http://www.bilibili.com/video/av116673440909829",
    "source": "Agent开发",
    "platform": "bilibili",
    "points": 10498,
    "published_at": "2026-06-01T06:35:48+00:00",
    "summary": "【2026最新】全B站最详细AI Agent开发教程，手把手教你搭建企业级Agent智能体！从入门到实战，学完即就业，带你玩转AI Agent！"
  },
  {
    "id": "bvid:BV1RtGU6hEDd",
    "domain": "AI",
    "title": "DeepSeek-Reasonix 【保姆级教程】：专为 DeepSeek 打造的 AI 编程 Agent客户端，长会话成本到底能省多少？",
    "url": "http://www.bilibili.com/video/av116647486556383",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 9387,
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
    "points": 9007,
    "published_at": "2026-05-05T12:14:39+00:00",
    "summary": "一天一个离职小技巧\n\n使用Vibe Coding构建属于自己的作品集网站，告别传统的PDF、PPT\n\n图片转链接：https://postimages.org/\n视频转链接：https://www.aconvert.com/cn/\n免费网站发布：https://app.netlify.com/"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 8933,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1caVh6fE6Z",
    "domain": "AI",
    "title": "【2026最新版】绝对是B站讲的最细的Claude Code教程，从国内环境安装出发，项目开发及个人使用总结带你玩转 Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116656764358481",
    "source": "AI大模型_",
    "platform": "bilibili",
    "points": 8648,
    "published_at": "2026-05-29T07:53:39+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 8573,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8022,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV19jL46gEab",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116611415541849",
    "source": "Agent搭建",
    "platform": "bilibili",
    "points": 7442,
    "published_at": "2026-05-21T07:43:25+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1cCVZ6NEym",
    "domain": "AI",
    "title": "这绝对是B站讲的最全最细的VibeCoding系统教程，手把手带你从环境安装到实战，包含所有干货！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673944492771",
    "source": "峰识在大模型",
    "platform": "bilibili",
    "points": 6952,
    "published_at": "2026-06-01T08:53:14+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV1ZSVG6eE3V",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116662284130312",
    "source": "非六于期",
    "platform": "bilibili",
    "points": 6970,
    "published_at": "2026-05-30T07:13:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6355,
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
    "points": 6324,
    "published_at": "2026-05-06T08:20:20+00:00",
    "summary": "Antigravity 是什么，和 Cursor/Claude Code/Codex 的区别\n安装、登录、主界面（Editor、Agent Manager、Browser、Terminal）\nAgent 工作流程 &amp; Artifacts\n浏览器能力：让 AI 自己看页面\nMCP（连接外部工具）、Skills（工作说明书）、Rules（规则）\n权限安全建议 + 完整实操案例（个人作品集网站）"
  },
  {
    "id": "bvid:BV1sbdcBmEFM",
    "domain": "AI",
    "title": "分享一下 GLM 5.1 + Claude Code 的实际使用体验",
    "url": "http://www.bilibili.com/video/av116531287561507",
    "source": "oil欧呦",
    "platform": "bilibili",
    "points": 6169,
    "published_at": "2026-05-07T03:59:46+00:00",
    "summary": "这期分享一下我这两天深度使用 GLM-5.1 的真实感受：在 Claude Code 里通过 CC Switch 切换模型，用它优化 CityCraft Skill、从 0 到 1 做 Selector Skill，也测试了 Codebase to Course 这类更吃理解能力的任务。\n\n整体感受是代码能力和交流感都不错，价格也很香，但长上下文下的指令准确性和原生多模态还有提升空间。"
  },
  {
    "id": "bvid:BV1VVQdBCExR",
    "domain": "AI",
    "title": "小米龙虾miclaw体验测评及配置教程，自定义LLM和MCP",
    "url": "http://www.bilibili.com/video/av116277163265800",
    "source": "屎壳郎智能科技",
    "platform": "bilibili",
    "points": 6106,
    "published_at": "2026-03-23T06:52:29+00:00",
    "summary": "接上一期视频，很多小伙伴安装完miclaw后不知道怎么配置和把玩。本期视频将详细告诉你如何配置基础信息，添加自定义LLM和MCP服务。逐步把小龙虾宝宝养成大龙虾。"
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 463,
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
    "points": 425,
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
    "points": 99,
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
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/bots-have-now-passed-human-traffic-online-cloudflare-boss-laments-says-agentic-traffic-wasnt-expected-to-eclipse-real-people-until-next-year",
    "domain": "AI 算力 / 半导体",
    "title": "‘Bots have now passed human traffic online,’ Cloudflare boss laments — says agentic traffic wasn’t expected to eclipse real people until next year",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/bots-have-now-passed-human-traffic-online-cloudflare-boss-laments-says-agentic-traffic-wasnt-expected-to-eclipse-real-people-until-next-year",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T11:35:00+00:00",
    "summary": "The rapid increase in agentic internet traffic means “bots have now passed human traffic online for the first time in the Internet's history,” remarked CEO and co-founder of Cloudflare, Matthew Prince"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amds-helios-mi455x-ai-platform-breaks-cover-initial-systems-use-ualink-over-ethernet-interconnects-amds-vera-rubin-rival-surfaces-but-the-downsides-of-ethernet-could-hamstring-performance",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's Helios MI455X AI platform breaks cover, initial systems use UALink-over-Ethernet interconnects — AMD's Vera Rubin rival surfaces, but the downsides of Ethernet could hamstring performance",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amds-helios-mi455x-ai-platform-breaks-cover-initial-systems-use-ualink-over-ethernet-interconnects-amds-vera-rubin-rival-surfaces-but-the-downsides-of-ethernet-could-hamstring-performance",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T11:26:38+00:00",
    "summary": "AMD’s Helios set to compete against Nvidia’s NVL72 VR200 rack-scale system later this year, but its UALink-over-Ethernet interconnection may affect performance in certain workloads before real UALink "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-ceo-sam-altman-admits-ai-token-costs-are-becoming-a-huge-issue-company-seeks-improved-value-as-overspending-becomes-a-meme",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI CEO Sam Altman admits AI token costs are becoming 'a huge issue' — company seeks improved value as overspending becomes a meme",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-ceo-sam-altman-admits-ai-token-costs-are-becoming-a-huge-issue-company-seeks-improved-value-as-overspending-becomes-a-meme",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T11:17:32+00:00",
    "summary": "OpenAI's clients are complaining about out-of-control AI spending, and they're asking Sam Altman to make it more efficient so they don't blow their annual AI budgets in just one quarter."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/production-of-ddr4-memory-and-motherboards-is-restarting-amid-unprecedented-memory-shortages-pc-industry-preparing-for-a-world-without-ddr5",
    "domain": "AI 算力 / 半导体",
    "title": "Production of DDR4 memory and motherboards is restarting amid unprecedented memory shortages — PC industry preparing for a world without DDR5",
    "url": "https://www.tomshardware.com/pc-components/ram/production-of-ddr4-memory-and-motherboards-is-restarting-amid-unprecedented-memory-shortages-pc-industry-preparing-for-a-world-without-ddr5",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T11:06:05+00:00",
    "summary": "Back to the (stone) DDR4 age."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/usd559-nvidia-rtx-5070-gpu-deal-is-the-cheapest-model-available-1440p-high-performance-gaming-at-just-usd10-above-msrp",
    "domain": "AI 算力 / 半导体",
    "title": "$559 Nvidia RTX 5070 GPU deal is the cheapest model available — 1440p high-performance gaming at just $10 above MSRP",
    "url": "https://www.tomshardware.com/pc-components/gpus/usd559-nvidia-rtx-5070-gpu-deal-is-the-cheapest-model-available-1440p-high-performance-gaming-at-just-usd10-above-msrp",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T11:01:06+00:00",
    "summary": "Quickly grab the cheapest RTX 5070 GPU available right now. Lenovo deal strips $80 off the list price."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/hp-has-slashed-an-astonishing-usd2-600-off-this-rtx-5080-gaming-pc-nearly-50-percent-off-get-an-epic-omen-35l-rig-with-a-9900x3d-64gb-ddr5-and-4tb-of-ssd-storage-for-just-usd2-899-99",
    "domain": "AI 算力 / 半导体",
    "title": "HP has slashed an astonishing $2,600 off this RTX 5080 gaming PC, nearly 50% off — get an epic Omen 35L rig with a 9900X3D, 64GB DDR5, and 4TB of SSD storage for just $2,899.99",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/hp-has-slashed-an-astonishing-usd2-600-off-this-rtx-5080-gaming-pc-nearly-50-percent-off-get-an-epic-omen-35l-rig-with-a-9900x3d-64gb-ddr5-and-4tb-of-ssd-storage-for-just-usd2-899-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T10:50:18+00:00",
    "summary": "An unthinkable $2,600 saving can be had right now on this HP Omen 45L gaming rig, fitted with a 9900X3D, RTX 5080, 64GB of DDR5 RAM, and 4TB in SSD storage, all for just $2,899.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/frore-shows-off-liquidjet-nexus-coldplate-for-nvidia-vera-rubin-other-ai-accelerators-offers-up-claimed-10-percent-token-generation-boost-over-rival-liquid-cooling-solutions",
    "domain": "AI 算力 / 半导体",
    "title": "Frore shows off LiquidJet Nexus coldplate for Nvidia Vera Rubin, other AI accelerators — offers up claimed 10% token generation boost over rival liquid-cooling solutions",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/frore-shows-off-liquidjet-nexus-coldplate-for-nvidia-vera-rubin-other-ai-accelerators-offers-up-claimed-10-percent-token-generation-boost-over-rival-liquid-cooling-solutions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T10:38:52+00:00",
    "summary": "Frore’s LiquidJet Nexus promises to enable 10% more token generation on Blackwell Ultra when compared to existing liquid-cooling solutions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/microsoft-ceo-says-new-ai-data-centers-use-as-little-water-annually-as-a-restaurant-closed-loop-cooling-system-aims-to-slash-consumption-from-millions-of-gallons-as-ai-infrastructure-faces-mounting-environmental-scrutiny",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft CEO says new AI data centers use as little water annually as a restaurant — closed-loop cooling system aims to slash consumption from millions of gallons as AI infrastructure faces mounting ",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/microsoft-ceo-says-new-ai-data-centers-use-as-little-water-annually-as-a-restaurant-closed-loop-cooling-system-aims-to-slash-consumption-from-millions-of-gallons-as-ai-infrastructure-faces-mounting-environmental-scrutiny",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T10:20:00+00:00",
    "summary": "Microsoft CEO claims the company's new AI data centers use only as much water as a single restaurant annually, thanks to a closed-loop cooling system designed to dramatically reduce consumption."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/surface-laptop-ultra-targets-110w-tdp-for-rtx-spark-superchip-microsoft-reveals-power-budget-of-its-high-end-15-system-in-hands-on-session",
    "domain": "AI 算力 / 半导体",
    "title": "Surface Laptop Ultra targets 110W TDP for RTX Spark Superchip — Microsoft reveals power budget of its high-end 15\" system in hands-on session",
    "url": "https://www.tomshardware.com/laptops/surface-laptop-ultra-targets-110w-tdp-for-rtx-spark-superchip-microsoft-reveals-power-budget-of-its-high-end-15-system-in-hands-on-session",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T10:00:00+00:00",
    "summary": "The RTX Spark Superchip still holds many mysteries, but we now have a better idea of its TDP. Microsoft revealed to Tom's Hardware that the Surface Laptop Ultra with this SoC inside will target a 110W"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-3-the-heat-bites-as-our-team-races-across-taipei",
    "domain": "AI 算力 / 半导体",
    "title": "Tom's Hardware Unfiltered: Computex 2026, Day 3 — the heat bites as our team races across Taipei",
    "url": "https://www.tomshardware.com/tech-industry/toms-hardware-unfiltered-computex-2026-day-3-the-heat-bites-as-our-team-races-across-taipei",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T09:54:07+00:00",
    "summary": "Our team in Taipei feels the heat in another extremely busy day covering Computex 2026, which is busier than ever before."
  },
  {
    "id": "rss:https://www.tomshardware.com/raspberry-pi/aviation-enthusiast-uses-raspberry-pi-and-abs-b-radio-to-create-viral-real-time-airport-tracker-open-source-skylight-intercepts-aircraft-signals-and-projects-flight-paths-onto-your-ceiling",
    "domain": "AI 算力 / 半导体",
    "title": "Aviation enthusiast uses Raspberry Pi and ADS-B radio to create viral real-time airport tracker — open-source 'Skylight' intercepts aircraft signals and projects flight paths onto your ceiling",
    "url": "https://www.tomshardware.com/raspberry-pi/aviation-enthusiast-uses-raspberry-pi-and-abs-b-radio-to-create-viral-real-time-airport-tracker-open-source-skylight-intercepts-aircraft-signals-and-projects-flight-paths-onto-your-ceiling",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T09:49:59+00:00",
    "summary": "Software engineer Cameron Paczek has developed Skylight, a project that receives ADS-B signals from an RTL-SDR radio antenna and shows the airplanes flying above you on a projector aimed at your ceili"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/teamgroup-shows-off-external-ssd-with-wireless-self-destruct-function-t-create-expert-p35sg-external-ssd-can-be-wiped-with-a-single-text-message",
    "domain": "AI 算力 / 半导体",
    "title": "TeamGroup shows off external SSD with wireless ‘self-destruct’ function — T-Create Expert P35SG External SSD can be wiped with a single text message",
    "url": "https://www.tomshardware.com/pc-components/ssds/teamgroup-shows-off-external-ssd-with-wireless-self-destruct-function-t-create-expert-p35sg-external-ssd-can-be-wiped-with-a-single-text-message",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T09:00:00+00:00",
    "summary": "TeamGroup released a plethora of new SSDs and RAM kits at Computex 2026, offering a mixture of design, performance, and security."
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
    "id": "hn:48364983",
    "domain": "大厂 AI 动态",
    "title": "Angry devs vow to flee GitHub Copilot as metered billing takes hold",
    "url": "https://www.theregister.com/ai-and-ml/2026/06/02/github-copilot-users-threaten-exit-as-metered-billing-kicks-in/5249826",
    "source": "jay_kyburz",
    "platform": "hackernews",
    "points": 55,
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
    "id": "rss:https://www.theverge.com/games/943657/valve-steam-machine-frame-summer-launch-verified",
    "domain": "大厂 AI 动态",
    "title": "Valve says it&#8217;s ready to launch the Steam Machine this summer",
    "url": "https://www.theverge.com/games/943657/valve-steam-machine-frame-summer-launch-verified",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T22:48:53+00:00",
    "summary": "Valve now says that the delayed Steam Machine PC and Steam Frame VR headset are set to launch sometime this summer. In a Thursday blog post detailing its Verified programs for both pieces of hardware,"
  },
  {
    "id": "rss:https://www.theverge.com/tech/943445/cyberdeck-tiktok",
    "domain": "大厂 AI 动态",
    "title": "Cyberdecks used to look like little laptops, but now they&#8217;re getting more personal",
    "url": "https://www.theverge.com/tech/943445/cyberdeck-tiktok",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T20:07:31+00:00",
    "summary": "DIYer and TikTok user Annike Tan, who goes by @ubeboobey, can carry her cyberdeck around without anyone noticing because it doesn't look like a computer at all. Tan, who has been featured in The Cut a"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/943234/kevin-oleary-agrees-to-downsize-massive-utah-data-center",
    "domain": "大厂 AI 动态",
    "title": "Kevin O’Leary agrees to downsize massive Utah data center",
    "url": "https://www.theverge.com/ai-artificial-intelligence/943234/kevin-oleary-agrees-to-downsize-massive-utah-data-center",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T18:38:04+00:00",
    "summary": "Kevin O'Leary agreed to halve the size of his planned 40,000-acre data center in Utah amid mounting pressure from residents and activists, as reported earlier by local affiliate ABC4. The Shark Tank s"
  },
  {
    "id": "rss:https://www.theverge.com/tech/943233/google-search-profiles-custom-page",
    "domain": "大厂 AI 动态",
    "title": "Google is letting social media stars customize their search result page",
    "url": "https://www.theverge.com/tech/943233/google-search-profiles-custom-page",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T18:32:23+00:00",
    "summary": "Google now lets big creators and publishers in the US claim dedicated profiles in Search to highlight things like videos, articles, and their other profiles online. But this feature won't be available"
  },
  {
    "id": "rss:https://www.theverge.com/games/943147/amazon-gaming-strategy-james-bond-snoop-dogg-luna",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s new plan for games: James Bond and AI Snoop Dogg",
    "url": "https://www.theverge.com/games/943147/amazon-gaming-strategy-james-bond-snoop-dogg-luna",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T17:01:15+00:00",
    "summary": "Amazon's gaming strategy has never really been clear. It's been very active in the space: acquiring Twitch, launching its Luna cloud gaming service nearly six years ago, investing heavily in MMOs duri"
  },
  {
    "id": "rss:https://www.theverge.com/tech/942617/belkin-gaming-charging-grip-nintendo-switch-2-joy-con-controller",
    "domain": "大厂 AI 动态",
    "title": "Belkin’s new Joy-Con grips also boost the Switch 2’s battery life",
    "url": "https://www.theverge.com/tech/942617/belkin-gaming-charging-grip-nintendo-switch-2-joy-con-controller",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:00:00+00:00",
    "summary": "Most of Belkin's Switch 2 accessories are designed to either protect or power up Nintendo's latest handheld, like its Charging Case Pro that actually does both at the same time. Its new multitasking C"
  },
  {
    "id": "rss:https://www.theverge.com/tech/942897/cash-app-tags-magic-wand-contactless-payments-price-launch",
    "domain": "大厂 AI 动态",
    "title": "Cash App made a magic wand for contactless payments",
    "url": "https://www.theverge.com/tech/942897/cash-app-tags-magic-wand-contactless-payments-price-launch",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:00:00+00:00",
    "summary": "The convenience of contactless payments can already feel magical, but Cash App is really leaning into that with its latest accessory. The mobile payment service is launching the Cash App Wand: an NFC-"
  },
  {
    "id": "rss:https://www.theverge.com/tech/943108/microsoft-build-2026-windows-love-notepad",
    "domain": "大厂 AI 动态",
    "title": "Windows is back on the Microsoft menu",
    "url": "https://www.theverge.com/tech/943108/microsoft-build-2026-windows-love-notepad",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:00:00+00:00",
    "summary": "I can't remember the last time Microsoft kicked off a Build keynote with Windows front and center, but that's exactly what CEO Satya Nadella did this week. Nadella didn't address the issues Microsoft "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/942999/remarkable-paper-pro-vizio-soundbar-marathon-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Remarkable’s refurbished Paper Pro bundle is hundreds off",
    "url": "https://www.theverge.com/gadgets/942999/remarkable-paper-pro-vizio-soundbar-marathon-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T15:46:07+00:00",
    "summary": "Color E Ink tablets aren’t usually affordable. I’m not going to say that Woot’s price on a refurbished “good as new” Remarkable Paper Pro is cheap, but it’s pretty fantastic compared to buying one new"
  },
  {
    "id": "rss:https://www.theverge.com/tech/943066/tsmc-ai-demand-struggles",
    "domain": "大厂 AI 动态",
    "title": "TSMC struggles to keep up with AI demand: &#8216;We can only support so much&#8217;",
    "url": "https://www.theverge.com/tech/943066/tsmc-ai-demand-struggles",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T14:15:44+00:00",
    "summary": "Taiwan Semiconductor Manufacturing Co. - the world's biggest semiconductor-maker - is struggling to meet demands from American customers even with its factory buildout in the US, according to reports "
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
    "id": "rss:https://techcrunch.com/2026/06/04/startup-battlefield-is-returning-to-australia-heres-what-happened-the-last-time-we-came-to-sydney/",
    "domain": "大厂 AI 动态",
    "title": "Startup Battlefield is returning to Australia — here’s what happened the last time we came to Sydney",
    "url": "https://techcrunch.com/2026/06/04/startup-battlefield-is-returning-to-australia-heres-what-happened-the-last-time-we-came-to-sydney/",
    "source": "Isabelle Johannessen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T20:55:38+00:00",
    "summary": "On August 19, Startup Battlefield is returning to Sydney in partnership with Stripe, one of the world's most iconic technology companies. We're taking over Stripe Tour Sydney for a night that the Aust"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/",
    "domain": "大厂 AI 动态",
    "title": "Meta steals a tactic from Tesla and builds data centers in tents",
    "url": "https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T19:33:09+00:00",
    "summary": "Meta may have found one way to slash its massive data center bill: tents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/apple-approves-poke-as-the-first-ai-agent-on-its-messages-for-business-platform/",
    "domain": "大厂 AI 动态",
    "title": "Apple approves Poke as the first AI agent on its Messages for Business platform",
    "url": "https://techcrunch.com/2026/06/04/apple-approves-poke-as-the-first-ai-agent-on-its-messages-for-business-platform/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T19:20:58+00:00",
    "summary": "Poke, the startup that lets people use AI agents through simple text messages, has become the first AI agent approved for Apple’s Messages for Business platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/helion-the-sam-altman-backed-fusion-startup-raises-465m-to-build-a-power-plant-for-microsoft/",
    "domain": "大厂 AI 动态",
    "title": "Helion, the Sam Altman-backed fusion startup, raises $465M to build a power plant for Microsoft",
    "url": "https://techcrunch.com/2026/06/04/helion-the-sam-altman-backed-fusion-startup-raises-465m-to-build-a-power-plant-for-microsoft/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T18:54:08+00:00",
    "summary": "Fusion startup Helion is racing to complete a power plant for Microsoft by 2028. A fresh infusion of cash should help with that."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/metas-oversight-board-says-account-bans-lack-due-process-transparency/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Oversight Board says account bans lack due process, transparency",
    "url": "https://techcrunch.com/2026/06/04/metas-oversight-board-says-account-bans-lack-due-process-transparency/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:47:12+00:00",
    "summary": "Meta's board cites \"due process\" concerns over account bans. It's also pushing Meta to offer clear information about violations and its use in AI in making its determinations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/meta-rolls-out-a-new-ai-creator-assistant-on-facebook/",
    "domain": "大厂 AI 动态",
    "title": "Meta rolls out a new AI creator assistant on Facebook",
    "url": "https://techcrunch.com/2026/06/04/meta-rolls-out-a-new-ai-creator-assistant-on-facebook/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:32:48+00:00",
    "summary": "Creators often have to parse through charts and dashboards to understand their performance, but with the new AI assistant, they can get quick answers to questions like \"When should I post?\" and \"What "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/what-to-expect-from-wwdc-2026-siris-highly-anticipated-revamp-and-apple-intelligence-updates/",
    "domain": "大厂 AI 动态",
    "title": "What to expect from WWDC 2026: Siri’s highly anticipated revamp and Apple Intelligence updates",
    "url": "https://techcrunch.com/2026/06/04/what-to-expect-from-wwdc-2026-siris-highly-anticipated-revamp-and-apple-intelligence-updates/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:31:12+00:00",
    "summary": "Apple's WWDC nears: Here's what you can look forward to."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/a-burglar-used-a-waymo-to-steal-yoga-clothes-in-sf-and-got-away-with-it/",
    "domain": "大厂 AI 动态",
    "title": "A burglar used a Waymo to steal yoga clothes in San Francisco — and got away with it",
    "url": "https://techcrunch.com/2026/06/04/a-burglar-used-a-waymo-to-steal-yoga-clothes-in-sf-and-got-away-with-it/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:16:37+00:00",
    "summary": "The incident helps shed some new light on how Waymo treats and stores the footage captured by its robotaxis."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/cash-app-launches-a-wand-for-tap-and-pay/",
    "domain": "大厂 AI 动态",
    "title": "Cash App launches a wand for tap-and-pay",
    "url": "https://techcrunch.com/2026/06/04/cash-app-launches-a-wand-for-tap-and-pay/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T16:00:00+00:00",
    "summary": "Digital wallet app Cash App is launching a new gadget on Thursday, seemingly inspired by the social media trend that involves paying for items in the real world with a tap of a homemade magic wand, wh"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/waymos-spent-robotaxi-batteries-will-be-used-as-grid-storage/",
    "domain": "大厂 AI 动态",
    "title": "Waymo’s spent robotaxi batteries will be used as grid storage",
    "url": "https://techcrunch.com/2026/06/04/waymos-spent-robotaxi-batteries-will-be-used-as-grid-storage/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T15:48:41+00:00",
    "summary": "The company announced a deal with B2U Storage Solutions to repurpose the battery packs as Waymo pulls them off the road."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/ramp-raises-750m-at-44b-valuation-as-investors-hunger-for-fintechs-with-an-ai-story/",
    "domain": "大厂 AI 动态",
    "title": "Ramp raises $750M at $44B valuation as investors hunger for fintechs with an AI story",
    "url": "https://techcrunch.com/2026/06/04/ramp-raises-750m-at-44b-valuation-as-investors-hunger-for-fintechs-with-an-ai-story/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T15:08:34+00:00",
    "summary": "Ramp has nearly tripled its valuation over the past year as investors scramble to grab a part of the fast-growing startup."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/is-silicon-valley-ready-to-put-robots-in-peoples-homes-hello-robot-is/",
    "domain": "大厂 AI 动态",
    "title": "Is Silicon Valley ready to put robots in people’s homes? Hello Robot is.",
    "url": "https://techcrunch.com/2026/06/04/is-silicon-valley-ready-to-put-robots-in-peoples-homes-hello-robot-is/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T15:05:00+00:00",
    "summary": "The California startup released the fourth-generation of its home assistance robot, Stretch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/chinese-spies-are-using-linkedin-to-lure-westerners-into-sharing-sensitive-information/",
    "domain": "大厂 AI 动态",
    "title": "Chinese spies are using LinkedIn to lure Westerners into sharing sensitive information",
    "url": "https://techcrunch.com/2026/06/04/chinese-spies-are-using-linkedin-to-lure-westerners-into-sharing-sensitive-information/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T14:57:41+00:00",
    "summary": "The advisory warns that Chinese spies are using public job search platforms to recruit people with access to non-public information."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/04/apple-touts-1-4-trillion-in-app-store-billings-and-sales-90-without-a-commission/",
    "domain": "大厂 AI 动态",
    "title": "Apple touts $1.4 trillion in App Store billings and sales, 90% without a commission",
    "url": "https://techcrunch.com/2026/06/04/apple-touts-1-4-trillion-in-app-store-billings-and-sales-90-without-a-commission/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T14:05:58+00:00",
    "summary": "Apple's App Store generated $1.4 trillion in sales, up from $1.3 trillion last year, with $149 billion in sales for digital goods."
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
    "id": "rss:https://arstechnica.com/ai/2026/06/the-skeptics-guide-to-humanoid-robots-going-viral-on-the-internet/",
    "domain": "大厂 AI 动态",
    "title": "The skeptic’s guide to humanoid robots going viral on the Internet",
    "url": "https://arstechnica.com/ai/2026/06/the-skeptics-guide-to-humanoid-robots-going-viral-on-the-internet/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T22:23:36+00:00",
    "summary": "Robot demonstrations can distort public perceptions of robotic capabilities."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/att-and-verizon-lose-supreme-court-case-over-fines-for-selling-location-data/",
    "domain": "大厂 AI 动态",
    "title": "AT&T and Verizon lose Supreme Court case over fines for selling location data",
    "url": "https://arstechnica.com/tech-policy/2026/06/att-and-verizon-lose-supreme-court-case-over-fines-for-selling-location-data/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T21:25:19+00:00",
    "summary": "FCC did not violate carriers' right to jury trial, court says in 8-1 ruling."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/these-llms-are-the-best-at-resisting-russian-propaganda/",
    "domain": "大厂 AI 动态",
    "title": "These LLMs are the best at resisting Russian propaganda",
    "url": "https://arstechnica.com/ai/2026/06/these-llms-are-the-best-at-resisting-russian-propaganda/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T20:44:31+00:00",
    "summary": "Estonian government benchmark shows how dozens of models combat Russia's \"strategic narratives.\""
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 458,
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
    "points": 137,
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
    "points": 89,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390053",
    "domain": "股票",
    "title": "Iran war drains US oil stocks to lowest level since 2004",
    "url": "https://www.ft.com/content/d0be73c8-b8d8-4ffd-874e-e97a6ecffef7",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-06-03T21:06:30+00:00",
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
    "id": "hn:48382926",
    "domain": "股票",
    "title": "Goldman Sachs CEO says markets in 'greed' mode as AI companies seek billions",
    "url": "https://www.cnbc.com/2026/06/02/goldman-ceo-david-solomon-greed-mode-ai-firms-ipos.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 23,
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
    "points": 19,
    "published_at": "2026-06-03T13:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48404734",
    "domain": "股票",
    "title": "Fidelity lowers SpaceX IPO entry requirement from $500,000 to just $2,000",
    "url": "https://finance.yahoo.com/markets/stocks/articles/fidelity-cuts-spacex-ipo-eligibility-183319186.html",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-04T21:15:18+00:00",
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
    "id": "wscn:3773945",
    "domain": "股票",
    "title": "代码暴增300%，成果只多30%：AI红利遭遇尴尬现实",
    "url": "https://wallstreetcn.com/articles/3773945",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T07:03:51+00:00",
    "summary": "AI正在制造一场效率幻觉：代码产出激增300%，实际软件发布量仅提升30%；全球AI支出突破1万亿美元，四成企业成本节约不足10%。更危险的是，44%大型企业正用\"尚未兑现的AI收益\"为下一轮投资埋单。技术跑通了，价值没到来，而估值重构的账单，或终将到期。"
  },
  {
    "id": "wscn:3773948",
    "domain": "股票",
    "title": "日本实际工资连升四个月，野村：6月加息“几乎确定”",
    "url": "https://wallstreetcn.com/articles/3773948",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T06:56:51+00:00",
    "summary": "日本4月实际工资同比涨1.9%，连续四个月正增长，创2021年底以来最长连涨纪录，名义工资增速亦超预期。野村证券称6月加息\"几乎确定\"，春斗成果正加速传导至薪资单。然而，家庭支出连续五个月下滑、生产者价格涨幅创12年新高，工资亮眼背后，消费疲软隐忧难掩。"
  },
  {
    "id": "wscn:3773952",
    "domain": "股票",
    "title": "黄仁勋抵达韩国，称“机器人是韩国下一个主要产业”！",
    "url": "https://wallstreetcn.com/articles/3773952",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T06:55:56+00:00",
    "summary": "黄仁勋此行旨在与三星、SK等企业协调供应链，深化半导体（韩企已获HBM4资格）及AI生态合作，并启动研发中心招聘；他还将录制知名脱口秀。值得注意的是，抵韩当日韩国股市及半导体双雄暴跌，但民众关注度极高，更有专属网站实时追踪其行程与概念股走势。"
  },
  {
    "id": "wscn:3773946",
    "domain": "股票",
    "title": "AI热潮降温，韩股重挫5.5%、SK海力士跌近10%，现货白银跌超2.5%",
    "url": "https://wallstreetcn.com/articles/3773946",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T06:36:56+00:00",
    "summary": "韩国首尔综指收跌5.5%，SK海力士跌近10%，三星电子跌超6%。与此同时，纳斯达克100指数期货下跌1%，预示该指数将录得连续第三日下跌；MSCI亚洲股票指数下跌1.6%。现货白银失守72美元/盎司，日内跌超2.5%。"
  },
  {
    "id": "wscn:3773947",
    "domain": "股票",
    "title": "豆包不用负责",
    "url": "https://wallstreetcn.com/articles/3773947",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T06:25:42+00:00",
    "summary": "平权，或是方差"
  },
  {
    "id": "wscn:3773944",
    "domain": "股票",
    "title": "老人卖保险炒股、杠杆创纪录！韩国股市泡沫信号频现，央行开始盯紧杠杆",
    "url": "https://wallstreetcn.com/articles/3773944",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T06:23:25+00:00",
    "summary": "韩国股市受AI驱动暴涨，但融资余额激增至38万亿韩元创历史新高，散户投机及老年人高杠杆入场令市场泡沫化风险加剧。新任韩国央行行长承诺，将加强对融资融券业务的监控。同时释放出强烈鹰派立场，大摩等机构预测韩国央行7月将开启连续加息。韩国KOSPI指数收跌5.54%，SK海力士跌近10%。"
  },
  {
    "id": "wscn:3773943",
    "domain": "股票",
    "title": "AI巨头们急于IPO，本质上是一场让普通人接盘的资本“逃生游戏”？",
    "url": "https://wallstreetcn.com/articles/3773943",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T06:10:52+00:00",
    "summary": "Anthropic秘密递交IPO申请，OpenAI紧随入场，两大AI巨头争相叩开公开市场大门。亮眼估值背后，却是持续亏损、客户弃用潮与幻觉问题三重阴影。这场上市热潮究竟是技术红利的全民共享，还是早期投资者将风险精准转嫁给普通人的出逃游戏？"
  },
  {
    "id": "wscn:3773942",
    "domain": "股票",
    "title": "从拼容量到拼散热！HBM5时代，三大存储巨头打响“散热保卫战”",
    "url": "https://wallstreetcn.com/articles/3773942",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T05:57:48+00:00",
    "summary": "三星推出HPB技术，在D2D PHY区域构建独立硅基热路径；SK海力士发布iHBM方案，将冷却元件直接集成至封装内；美光则主打低功耗与无源垂直TSV沟槽冷却。散热已成为3D封装竞争的新维度。"
  },
  {
    "id": "wscn:3773923",
    "domain": "股票",
    "title": "创业板跌超2%，芯片半导体集体调整，京东方再涨停，恒科指跌超1%，AI大模型股重挫",
    "url": "https://wallstreetcn.com/articles/3773923",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T05:40:45+00:00",
    "summary": "个股涨多跌少，沪深京三市超3900股飘红，上午半天成交1.9万亿。沪深两市半日成交额1.88万亿，较上个交易日放量近1600亿。板块方面，光伏玻璃、6G、射频天线、商业航天、BC电池概念领涨，石化、海运、工程机械板块表现亮眼，电力、半导体、电脑硬件方向低迷。"
  },
  {
    "id": "wscn:3773929",
    "domain": "股票",
    "title": "SpaceX还是没能提前加入标普500指数：纳指、罗素“开绿灯”，标普不跟",
    "url": "https://wallstreetcn.com/articles/3773929",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T05:37:15+00:00",
    "summary": "标普、道琼斯宣布维持现行规则，拒绝为超大市值IPO开辟\"快速入场\"通道，与纳斯达克、富时罗素分道扬镳。这意味着，SpaceX在挂牌交易后至少一年内无缘标普500指数。该公司去年巨亏、流通股仅5%，三项门槛无一达标。"
  },
  {
    "id": "wscn:3773935",
    "domain": "股票",
    "title": "A股进入震荡期，市场如何进行风格切换？",
    "url": "https://wallstreetcn.com/articles/3773935",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T05:23:21+00:00",
    "summary": "A股进入震荡区间，东吴证券表示，这并不意味着市场将迎来全面的\"高切低\"行情，更可能是在战略安全类资产（STAR）内部轮动，科技降温后，煤炭、石化、航运等能源和基建类安全资产有望接力，待流动性回归，科技主线料将王者归来。"
  },
  {
    "id": "wscn:3773941",
    "domain": "股票",
    "title": "姚顺雨首次亮相腾讯大会：为什么加入腾讯",
    "url": "https://wallstreetcn.com/articles/3773941",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T05:22:37+00:00",
    "summary": "AI是一个长期游戏，下半场才刚刚开始"
  },
  {
    "id": "wscn:3773940",
    "domain": "股票",
    "title": "汤道生 x 姚顺雨：腾讯AI下半场",
    "url": "https://wallstreetcn.com/articles/3773940",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T05:11:32+00:00",
    "summary": "汤道生提出了一个非常犀利的问题“你觉得腾讯AI慢了吗？”姚顺雨笑称，“这个问题应该我问你”，然后给出了自己的回答。姚顺雨认为，如果要问AI是短期游戏还是长期游戏？他的判断是长期游戏，“下半场才刚开始，我不认为ChatGPT和Anthropic永远都是第一位，今天就像70年代PC刚出现时的阶段一样。”"
  },
  {
    "id": "wscn:3773938",
    "domain": "股票",
    "title": "“存款搬家”新路径曝光  银行理财固收+产品获青睐",
    "url": "https://wallstreetcn.com/articles/3773938",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:27:42+00:00",
    "summary": "一边是提前止盈潮汹涌而来，一边是费率战硝烟四起，在天量存款到期、居民财富再配置的窗口下，理财行业正加..."
  },
  {
    "id": "wscn:3773848",
    "domain": "股票",
    "title": "连续跑输17年！商品/股票超级周期何时走出历史大底？",
    "url": "https://wallstreetcn.com/premium/articles/3773848?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:14:30+00:00",
    "summary": "大宗商品被长期低估，但本轮上涨由供应挤压驱动，短期风险上升，商品/股票第一波行情接近尾声，后市将结构性分化。"
  },
  {
    "id": "wscn:3773937",
    "domain": "股票",
    "title": "坚持“为民办实事” 专业陪伴守护民生——平安理财开展金融教育系列活动",
    "url": "https://wallstreetcn.com/articles/3773937",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:11:18+00:00",
    "summary": "日前，在深圳市福田区香蜜湖街道竹园社区，一场以“金融为爱守护，每个你都是重要的人”为主题的特别公益活..."
  },
  {
    "id": "wscn:3773873",
    "domain": "股票",
    "title": "陶瓷基板：英伟达钦点！AI时代散热瓶颈的材料破局者",
    "url": "https://wallstreetcn.com/premium/articles/3773873?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:04:01+00:00",
    "summary": "作为有源光器件核心载体的陶瓷基板与陶瓷管壳，凭借其优异的高频特性、低介电损耗、极高热导率及完美的气密性保护，正从传统电信市场的“特种元器件”蜕变为AI算力时代的“刚需高壁垒红利赛道” 。在英伟达新一代Rubin/Ultra等高功耗芯片架构中，陶瓷基板在HDI板及CoWoS封装中的“混压方案”与“高价值量替换”正迎来历史性技术奇点 。"
  },
  {
    "id": "wscn:3773933",
    "domain": "股票",
    "title": "AI成本从\"无人在意\"到\"巨大问题\"，Altman公开承认行业烧钱危机",
    "url": "https://wallstreetcn.com/articles/3773933",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T03:24:36+00:00",
    "summary": "Sam Altman公开承认，AI运行成本已从年初\"无人提起\"变成企业客户的\"巨大问题\"。OpenAI最大客户单月消耗1000亿tokens，Uber全年AI预算四个月耗尽。使用量百万倍级暴增正在击穿企业预算，控费、模型分层、智能路由成新常态，AI行业从增长叙事转向单位经济。"
  },
  {
    "id": "wscn:3773931",
    "domain": "股票",
    "title": "半年“狂赚”1000万亿，人均“入账”2000万，这一轮韩股造富规模史无前例",
    "url": "https://wallstreetcn.com/articles/3773931",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T03:13:24+00:00",
    "summary": "韩国KOSPI指数年内暴涨109%，家庭股票账面增值突破1000万亿韩元，相当于全年GDP的40%、人均账面财富增加近2000万韩元。财富正从金融体系向消费传导：百货销售暴增17%，新车注册量飙升41%。但这场盛宴高度集中：散户踏空主升浪，杠杆ETF疯狂膨胀，半数市值压注两只股票。列车已满载狂热驶出，终点在哪，无人知晓。"
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
    "id": "hn:48368083",
    "domain": "股票",
    "title": "Ask HN: What is your opinion on index rule changes to accommodate Mega-Cap IPOs?",
    "url": "https://news.ycombinator.com/item?id=48368083",
    "source": "figmert",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-02T09:55:55+00:00",
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
    "id": "hn:48360414",
    "domain": "金融",
    "title": "Making Debian or Fedora persistent live images",
    "url": "https://sigwait.org/~alex/blog/2026/05/28/smdBC8.html",
    "source": "henry_flower",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-06-01T18:02:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48406282",
    "domain": "金融",
    "title": "S&P Global keeps fast index entry rules unchanged as SpaceX listing looms",
    "url": "https://www.reuters.com/business/finance/sp-global-keeps-fast-entry-proposal-unchanged-spacex-listing-looms-2026-06-04/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-06-04T23:55:20+00:00",
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
    "id": "rss:https://arxiv.org/abs/2606.05383",
    "domain": "金融",
    "title": "Can AI Refute Economic Theory? Evidence from Beyond the Knowledge Cutoff",
    "url": "https://arxiv.org/abs/2606.05383",
    "source": "Alexis Akira Toda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.05383v1 Announce Type: new Abstract: Can artificial intelligence (AI) refute economic theory? I document experiments in which I asked several AI models (Gemini, Refine, Claude, and ChatGPT)"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05392",
    "domain": "金融",
    "title": "Dual Representation of Robust Risk Measures and Uncertainty Sets",
    "url": "https://arxiv.org/abs/2606.05392",
    "source": "Marlon R. Moresco, Marcelo Righi, Silvana M. Pesenti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.05392v1 Announce Type: new Abstract: We consider robust risk measures that arise as worst-case values of convex risk measures evaluated on uncertainty sets. We characterize continuity prope"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05623",
    "domain": "金融",
    "title": "Bankruptcy Prediction from 10-K Narratives: Evidence from Interpretable Text Scores and Accounting Baselines",
    "url": "https://arxiv.org/abs/2606.05623",
    "source": "Zhen Zhang, Moxuan Zheng, Tongchen Zhang, Luyun Lin, Yiqing Wang, Lixing Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.05623v1 Announce Type: new Abstract: Bankruptcy is a low-frequency but high-impact corporate event, making early risk identification important for creditors, investors, regulators, and risk"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05631",
    "domain": "金融",
    "title": "Stress Amplified Resilience: ESG and Joint Fragility in Equity Markets",
    "url": "https://arxiv.org/abs/2606.05631",
    "source": "Minxuan Hu, Jiayu Yi, Ziheng Chen, Wenxi Sun, Qishi Zhan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.05631v1 Announce Type: new Abstract: Market stress rarely harms investors through one channel alone. Losses, volatility spikes, and deteriorating tradability often arrive together. We exami"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05882",
    "domain": "金融",
    "title": "The Impact of Market Informedness on Market Makers' Profitability",
    "url": "https://arxiv.org/abs/2606.05882",
    "source": "Konrad Och\\k{e}dzan, Nino Antulov-Fantulin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.05882v1 Announce Type: new Abstract: This paper examines the impact of market informedness on the profitability of market makers. In contrast to the existing literature, the analysis is con"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05900",
    "domain": "金融",
    "title": "Derivative-Informed Operator Learning for Finance: On-the-Fly Greeks, Surfaces, Hedging, and Control",
    "url": "https://arxiv.org/abs/2606.05900",
    "source": "Miquel Noguer I Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.05900v1 Announce Type: new Abstract: Financial decision systems require fast surrogate models for pricing, calibration, hedging, XVA, stress testing, and portfolio optimization. Standard ne"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05991",
    "domain": "金融",
    "title": "Forecasting of volatility and risk premia in electricity markets",
    "url": "https://arxiv.org/abs/2606.05991",
    "source": "Thomas K. Kloster, Fred Espen Benth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.05991v1 Announce Type: new Abstract: We study forecasting of the realized covariation in electricity markets. The realized covariation in this context is a matrix-valued representation of t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.06089",
    "domain": "金融",
    "title": "Leveraging LLMs for Unstructured Claims Data Analysis",
    "url": "https://arxiv.org/abs/2606.06089",
    "source": "Robert D. Lieberthal (Lieberthal and Associates, LLC), Richard Tran (MDSight, LLC), Vietbao Phan (Thomas Jefferson University), Jawand Singh (Lieberthal and Associates, LLC, William and Mary University), Elizabeth Sottung (Thomas Jefferson University)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.06089v1 Announce Type: new Abstract: Actuaries rely primarily on structured numerical data for reserving and ratemaking, while valuable predictive information in unstructured text including"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.06190",
    "domain": "金融",
    "title": "Multi-Scale Markov Switching GARCH",
    "url": "https://arxiv.org/abs/2606.06190",
    "source": "Jayesh Chaudhary",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.06190v1 Announce Type: new Abstract: Financial volatility exhibits substantial non-stationarity, making single-regime models inadequate for characterising changing market conditions. This p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.06413",
    "domain": "金融",
    "title": "Competition in Dealer Markets with Internalisation and Externalisation",
    "url": "https://arxiv.org/abs/2606.06413",
    "source": "Robert Boyce, Eyal Neuman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.06413v1 Announce Type: new Abstract: We model a market with multiple dealers who compete for client order flow by dynamically updating their bid and ask quotes for a risky asset. Dealers ai"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05733",
    "domain": "金融",
    "title": "Zero-Copy Semantic Contagion: An In-Memory Streaming Architecture for Evolving Attention Graphs",
    "url": "https://arxiv.org/abs/2606.05733",
    "source": "Kabir Murjani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2606.05733v1 Announce Type: cross Abstract: Per-ticker forecasting models dominate financial time-series work yet remain blind to cross-company propagation: a foundry disruption in Taiwan does n"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.12010",
    "domain": "金融",
    "title": "FDI versus R\\&amp;D in an endogenous growth model",
    "url": "https://arxiv.org/abs/2501.12010",
    "source": "Thanh Tam Nguyen-Huu (EM Normandie), Ngoc-Sang Pham (EM Normandie)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2501.12010v3 Announce Type: replace Abstract: We investigate the role of foreign direct investment (FDI) and research and development (R\\&amp;D) in the transitional dynamics of host countries us"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.19006",
    "domain": "金融",
    "title": "Is attention truly all we need? An empirical study of asset pricing in pretrained RNN sparse and global attention models",
    "url": "https://arxiv.org/abs/2508.19006",
    "source": "Shanyan Lai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2508.19006v2 Announce Type: replace Abstract: This study investigates the pre-trained RNN attention models with the mainstream attention mechanisms, such as additive attention, Luong's three att"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.19663",
    "domain": "金融",
    "title": "Long-Range Dependence in Financial Markets: Empirical Evidence and Generative Modeling Challenges",
    "url": "https://arxiv.org/abs/2509.19663",
    "source": "Yifan He, Svetlozar Rachev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2509.19663v2 Announce Type: replace Abstract: This study provides a comprehensive empirical investigation of long-range dependence (LRD) in financial markets and evaluates the ability of deep ge"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.28257",
    "domain": "金融",
    "title": "Nonlinear Factor Decomposition via Kolmogorov-Arnold Networks: A Spectral Approach to Asset Return Analysis",
    "url": "https://arxiv.org/abs/2603.28257",
    "source": "David Breazu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2603.28257v2 Announce Type: replace Abstract: KAN-PCA is an autoencoder that uses a KAN as encoder and a linear map as decoder. It generalizes classical PCA by replacing linear projections with "
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.23587",
    "domain": "金融",
    "title": "Moments by Integrating the Moment-Generating Function",
    "url": "https://arxiv.org/abs/2410.23587",
    "source": "Peter Reinhard Hansen, Chen Tong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2410.23587v5 Announce Type: replace-cross Abstract: We introduce a general integral framework for computing fractional, complex, absolute, and logarithmic moments from the moment-generating func"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.16821",
    "domain": "金融",
    "title": "Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention",
    "url": "https://arxiv.org/abs/2601.16821",
    "source": "Harrison Katz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2601.16821v3 Announce Type: replace-cross Abstract: Compositional time series frequently exhibit structural breaks due to external shocks, policy changes, or market disruptions. Standard methods"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.26634",
    "domain": "金融",
    "title": "Electricity price forecasting across Norway's five bidding zones in the post-crisis era",
    "url": "https://arxiv.org/abs/2604.26634",
    "source": "My Thi Diem Phan, Trung Tuyen Truong, Hoai Phuong Ha, Dat Thanh Nguyen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2604.26634v2 Announce Type: replace-cross Abstract: Norway's electricity market is heavily dominated by hydropower, but the 2021-2022 energy crisis and stronger integration with Continental Euro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.27887",
    "domain": "金融",
    "title": "PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management",
    "url": "https://arxiv.org/abs/2605.27887",
    "source": "Yuxuan Zhao, Sijia Chen, Ningxin Su",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T04:00:00+00:00",
    "summary": "arXiv:2605.27887v2 Announce Type: replace-cross Abstract: Large language models (LLMs) have shown strong performance across diverse financial tasks, yet portfolio management (PM), a critical financial"
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
    "id": "hn:48040639",
    "domain": "金融",
    "title": "Google to sell TPU chips to select customers",
    "url": "https://finance.yahoo.com/markets/stocks/article/google-to-sell-tpu-chips-to-select-customers-in-latest-shot-at-nvidia-214900221.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-05-06T19:34:54+00:00",
    "summary": ""
  }
]
```
