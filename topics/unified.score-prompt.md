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

- 今日日期：`2026-06-09`
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
  "date": "2026-06-09",
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
    "points": 632745,
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
    "points": 368826,
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
    "points": 368309,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 249384,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 237039,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BXuvzTEVZ",
    "domain": "AI",
    "title": "【AI垃圾王】2500元不到装一台AI服务器！双Radeon VII解锁vLLM张量并行，性能暴涨6倍碾压Ollama！",
    "url": "http://www.bilibili.com/video/av114850546196477",
    "source": "司波图",
    "platform": "bilibili",
    "points": 235012,
    "published_at": "2025-07-14T08:14:09+00:00",
    "summary": "💥2400元预算挑战AI算力天花板！本期视频，我们解决了Radeon VII / MI50 等 gfx906 架构显卡长期以来无法使用 vLLM 张量并行的痛点！\n\n我们将全程展示如何用两张“过气”Radeon VII显卡，搭配X99“洋垃圾”平台，组装一台总价仅2397元的AI算力服务器。通过社区大神 nlzy 提供的特制Docker容器，我们成功解锁了vLLM的张量并行功能，在Qwen3 32"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 173812,
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
    "points": 153743,
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
    "points": 145515,
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
    "points": 141602,
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
    "points": 133048,
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
    "points": 108874,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1j67k6oENA",
    "domain": "AI",
    "title": "Claude Ultracode 超码 上线 | 操控100个Agent并行开发  保姆级实战教程",
    "url": "http://www.bilibili.com/video/av116697163896598",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 99574,
    "published_at": "2026-06-05T11:05:27+00:00",
    "summary": "Ultracode 功能太好用了，就是Claude Code昨天新出的“超码”功能，如果你Vibe Coding ，那这个技巧一定要掌握。他解决了Claude Code 一次性跑不完大型任务的问题。\n本期视频很长，但看完你的AI Coding能力将超越整个团队。并且把视频内容整理成了文字版，放在评论区，方便你学习使用。视频很干，可以先喝口水润润喉咙。"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 86125,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1wiL16gEKv",
    "domain": "AI",
    "title": "【AI漫剧教程】吊打付费！目前B站最全最细的AI漫剧喂饭教程！手把手教你从0到1制作AI漫剧！七天就能从小白到大神，带你从零基础入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116605761619869",
    "source": "AIGC全套系统教学",
    "platform": "bilibili",
    "points": 71059,
    "published_at": "2026-05-20T07:46:19+00:00",
    "summary": "持续更新中~评论区获取课程资料哟~求一键三连~谢谢各位观众老爷！！！！"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 56220,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 50996,
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
    "points": 49387,
    "published_at": "2026-03-10T10:18:17+00:00",
    "summary": "深度解析GitHub热门项目mcp2cli——一个能把任何MCP服务器或OpenAPI规范变成命令行工具的Python项目。它用&quot;懒发现&quot;机制，把MCP协议的token浪费从数十万降到几千，节省高达99%。整个核心实现只有一个Python文件，却支持三种接入模式、OAuth认证和智能缓存。发布仅一天就获得372颗星，但社区也有激烈争议：CLI真的能取代MCP吗？准确率会不会受影"
  },
  {
    "id": "bvid:BV13HEw6rEDa",
    "domain": "AI",
    "title": "【2026最新】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116691140872014",
    "source": "绕着宇宙飞一圈",
    "platform": "bilibili",
    "points": 34509,
    "published_at": "2026-06-04T09:39:37+00:00",
    "summary": "求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！"
  },
  {
    "id": "bvid:BV1thXHY2EXh",
    "domain": "AI",
    "title": "Cursor+three.js，简单提示词也能生成交互式3D",
    "url": "http://www.bilibili.com/video/av114205059521179",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 33417,
    "published_at": "2025-03-22T08:11:40+00:00",
    "summary": "上周发布了 Cursor+Blender MCP 快速实现3D建模的教程，但由于目前MCP还不是特别稳定，加上配置有点麻烦不一定能一次成功，所以不少小伙伴被劝退了。\n.\n后面我发现借助three.js，就能让大家通过简单的提示词，轻松实现一些还不错的交互式3D场景，非常适合放在一些教学或者科普场景。大家快去试试吧 ~ \n.\n欢迎加入我的知识星球，有问必答：https://t.zsxq.com/fD"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29600,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV16BkEBtEjW",
    "domain": "AI",
    "title": "老张公开课：算力、GPU、AI服务器详解（上）",
    "url": "http://www.bilibili.com/video/av115927962159456",
    "source": "It_server技术分享",
    "platform": "bilibili",
    "points": 25116,
    "published_at": "2026-01-20T14:51:01+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 17643,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17268,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1Y2Ex6kEEf",
    "domain": "AI",
    "title": "vibe coding｜监控Claude/Codex实时任务的桌面宠物来啦～你的桌宠还在只会提醒喝水吗？ 【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116707985330558",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 16855,
    "published_at": "2026-06-07T08:58:03+00:00",
    "summary": "vibe coding了个桌面宠物给claude/codex当监工啦\n\n每次用 Claude Code / Codex 写代码，AI 在那闷头跑任务、转圈圈，我不一直盯着就根本不知道到哪了、卡没卡住，干等着很浪费时间，去做别的事吧又很容易错过结果，任务多起来完全没有直观的全局视角！\n\n于是我做了个桌面宠物工具，让它实时&quot;演&quot;出我的 AI 在干啥👇\n🐾 AI思考时 → 写字记笔记"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 15781,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 15714,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 13800,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13564,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1woEJ6rEi5",
    "domain": "AI",
    "title": "翻遍整个B站，这绝对是2026讲的最好的AI Agent智能体教程，手把手教你从0基础开始搭建企业级Agent智能体，全程干货无废话，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116703220535567",
    "source": "AI学习课堂",
    "platform": "bilibili",
    "points": 13086,
    "published_at": "2026-06-06T12:49:16+00:00",
    "summary": "【视频配套籽料,学习路线、系统学习，实战项目案例、电子书+问题解答问题解答请看”平论区置顶”自取哦】\n视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 12916,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12181,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1uhLS6FE7i",
    "domain": "AI",
    "title": "Excel迎来最大改变：Claude装进来之后，手动做表成为历史了，6个真实场景全演示｜销售分析/财务审查/PDF提取",
    "url": "http://www.bilibili.com/video/av116607758112186",
    "source": "小巧见",
    "platform": "bilibili",
    "points": 11901,
    "published_at": "2026-05-20T16:10:14+00:00",
    "summary": "很多人装了Claude，但不知道把它用在哪里。\n\n今天告诉你一个具体的答案：Excel。\n\n这期视频我把Claude放进6个真实的办公场景里演示：\n✅ 自定义格式指令，再也不用手动调格式\n✅ 100页PDF年报，直接提取资产负债表\n✅ 销售数据分析，不写公式直接得答案\n✅ 财务模型审查，自动找出硬编码和公式错误\n✅ 一键生成PPT汇报幻灯片\n✅ 销售汇总表，一句话搞定\n\n📌 评论区打「模板」，我把"
  },
  {
    "id": "bvid:BV1cCVZ6NEym",
    "domain": "AI",
    "title": "这绝对是B站讲的最全最细的VibeCoding系统教程，手把手带你从环境安装到实战，包含所有干货！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673944492771",
    "source": "峰识在大模型",
    "platform": "bilibili",
    "points": 11574,
    "published_at": "2026-06-01T08:53:14+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV1HFRgBvEVv",
    "domain": "AI",
    "title": "claude接入小米mimo模型基础教程（无claude安装教程）",
    "url": "http://www.bilibili.com/video/av116499343738499",
    "source": "栉旎",
    "platform": "bilibili",
    "points": 11458,
    "published_at": "2026-05-01T12:37:49+00:00",
    "summary": "claude接入小米mimo模型全流程，"
  },
  {
    "id": "bvid:BV1yT8qzMEbd",
    "domain": "AI",
    "title": "基于SpringAI开发Java版mcp服务",
    "url": "http://www.bilibili.com/video/av114942720148945",
    "source": "程序员Cafe",
    "platform": "bilibili",
    "points": 11222,
    "published_at": "2025-07-30T15:05:27+00:00",
    "summary": "如何用Java开发一个mcp服务？如何把已有的spingboot微服务改造成mcp服务呢？如何在mcp客户端调用mcp服务？\n今天来一个保姆级教学"
  },
  {
    "id": "bvid:BV1F5QhYxENy",
    "domain": "AI",
    "title": "Cursor+Claude3.7+Stm32：零代码嵌入式开发实战",
    "url": "http://www.bilibili.com/video/av114171102365070",
    "source": "AI炼丹之陆",
    "platform": "bilibili",
    "points": 11056,
    "published_at": "2025-03-16T08:21:07+00:00",
    "summary": "Cursor黑科技+Claude3.7，陀螺仪代码自动生成实测 \n深度评测：Cursor+Claude3.7在STM32开发中的真实表现——以MPU6050项目为例"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 10542,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1N2doBCE4T",
    "domain": "AI",
    "title": "小云雀短剧 Agent 功能解析：全流程定制化短剧创作实测",
    "url": "http://www.bilibili.com/video/av116430959806340",
    "source": "AllenTV_AiGC",
    "platform": "bilibili",
    "points": 10519,
    "published_at": "2026-04-19T11:06:04+00:00",
    "summary": "哈喽各位！今天带大家浅玩一下小云雀短剧 Agent。本以为是普通 AI 工具，没想到功能是真的强，短剧制作全流程都能深度定制修改，效率直接拉满。这期就带大家快速体验一遍，看看有多好用～"
  },
  {
    "id": "bvid:BV1ZSVG6eE3V",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116662284130312",
    "source": "非六于期",
    "platform": "bilibili",
    "points": 9354,
    "published_at": "2026-05-30T07:13:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1hEVY6jEGT",
    "domain": "AI",
    "title": "最新【Claude pro Max】保姆级充值教程 Claude code国内购买教程 注册+订阅一个视频教会你",
    "url": "http://www.bilibili.com/video/av116657754277772",
    "source": "小轩AI-",
    "platform": "bilibili",
    "points": 9322,
    "published_at": "2026-05-29T12:07:14+00:00",
    "summary": "aipayok.com"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 8967,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV18TVs6QETE",
    "domain": "AI",
    "title": "Claude 尼区订阅教程（2026 最新）：低价开通 Claude Pro 完整指南",
    "url": "http://www.bilibili.com/video/av116652385572199",
    "source": "专心做教程",
    "platform": "bilibili",
    "points": 7304,
    "published_at": "2026-05-28T13:19:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV17b7664ERM",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116696257924741",
    "source": "AI产品实战",
    "platform": "bilibili",
    "points": 6919,
    "published_at": "2026-06-05T07:19:09+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6958,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1UDPWzgEFH",
    "domain": "AI",
    "title": "AI帮你写完+测完，编程丝滑到飞起！Cursor 一镜到底全流程：规则 → 方案 → Agent编码 → 自动化测试 | 2026 独立开发者必备神器",
    "url": "http://www.bilibili.com/video/av116182002701930",
    "source": "南哥AGI研习社",
    "platform": "bilibili",
    "points": 6632,
    "published_at": "2026-03-06T11:33:46+00:00",
    "summary": "YouTube、B站频道关于AI Coding Cursor等开发经验分享，所有资源全部开源免费\n\n🙏🏻如果内容对你有帮助，拜托给我的视频点个赞，你们的支持就是我持续开源分享的功力                    \n个人项目GitHub地址：https://github.com/NanGePlus                    \n个人项目Gitee地址：https://gitee.c"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6379,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 5842,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1DaEb6UEuN",
    "domain": "AI",
    "title": "2026吃透Agent Skills (Claude Skills)教程，手把手带你从0基础开始搭建企业级AI Agent智能体，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116708320808288",
    "source": "徐庶架构师",
    "platform": "bilibili",
    "points": 5281,
    "published_at": "2026-06-07T10:27:49+00:00",
    "summary": "一个冷知识：点赞是免费的！但是可以让辛苦做视频的UP主开心快乐一整天！！！\n视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1BJvSBxEjw",
    "domain": "AI",
    "title": "用 Rust 构建你的第一个 AI Agent —— 完整教程（本地 LLM + 网络搜索）",
    "url": "http://www.bilibili.com/video/av115818809525301",
    "source": "ppt的bug",
    "platform": "bilibili",
    "points": 5357,
    "published_at": "2026-01-02T02:15:00+00:00",
    "summary": "https://www.youtube.com/watch?v=dVj9Wtg9MXQ\n🦀 使用 Rig 框架和 Ollama，用 Rust 构建一个可用于生产环境的 AI 研究型 Agent！\n 本完整教程将手把手带你创建一个智能代理，它能够进行网页搜索并综合整理信息——全部在你的本地机器上运行，无需任何 API 成本。\n在本视频中，你将学到：\n✅ 如何设计和组织一个 Rust AI Agent"
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 470,
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
    "points": 427,
    "published_at": "2026-06-01T05:24:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48424605",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is proposing a beast of a CPU system for Windows PCs",
    "url": "https://twitter.com/lemire/status/2062880075117113739",
    "source": "tosh",
    "platform": "hackernews",
    "points": 329,
    "published_at": "2026-06-06T12:52:18+00:00",
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
    "id": "hn:48444451",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia partners with LG robotics to build humanoid robots in South Korea",
    "url": "https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/",
    "source": "spwa4",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-06-08T12:25:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356312",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity",
    "url": "https://news.ycombinator.com/item?id=48356312",
    "source": "ismaeel_bashir",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48431367",
    "domain": "AI 算力 / 半导体",
    "title": "The Russian who invented semiconductors 25 years before the USA",
    "url": "https://www.semidoped.com/p/til-the-man-who-invented-the-future",
    "source": "johncole",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-06-07T03:00:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48439316",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei executive credits bans for accelerating domestic chip independence",
    "url": "https://www.techradar.com/pro/huaweis-chairman-officially-thanks-the-us-government-for-enabling-chinas-semiconductor-industry-chain-to-truly-grow",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-06-07T22:38:25+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-summit-europe-2026-industry-and-academia-unite-in-bologna-to-advance-open-hardware/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Summit Europe 2026: Industry and Academia Unite in Bologna to Advance Open Hardware",
    "url": "https://www.eetimes.com/risc-v-summit-europe-2026-industry-and-academia-unite-in-bologna-to-advance-open-hardware/",
    "source": "RISC-V Summit",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T16:10:19+00:00",
    "summary": "RISC-V Summit Europe is coming to Bologna, Italy, with a program that reflects just how far the ecosystem has come since we gathered in Paris a year ago. Taking place June 8–12 2026 at the Palazzo dei"
  },
  {
    "id": "rss:https://www.eetimes.com/chips-act-2-0-inside-europes-semiconductor-rethink/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Europe’s Chip Rethink: Why Fabs Weren’t Enough and Why Spain Matters",
    "url": "https://www.eetimes.com/chips-act-2-0-inside-europes-semiconductor-rethink/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T12:00:00+00:00",
    "summary": "Spain is emerging as a more influential player in Europe’s next chip debate—through design startups, photonics, quantum technologies, and a growing talent base. The post Inside Europe’s Chip Rethink: "
  },
  {
    "id": "rss:https://www.eetimes.com/antenna-first-design-the-rf-shift-iot-cannot-avoid/",
    "domain": "AI 算力 / 半导体",
    "title": "Antenna-First Design: The RF Shift IoT Cannot Avoid",
    "url": "https://www.eetimes.com/antenna-first-design-the-rf-shift-iot-cannot-avoid/",
    "source": "Senior Director of Engineering at Ignion",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T08:00:00+00:00",
    "summary": "Wireless IoT devices are shrinking while adding bands and certification complexity. Antenna integration can't wait until after layout lock. The post Antenna-First Design: The RF Shift IoT Cannot Avoid"
  },
  {
    "id": "rss:https://www.eetimes.com/connectivity-revolution-or-evolution-inside-data-centers/",
    "domain": "AI 算力 / 半导体",
    "title": "Connectivity Revolution or Evolution Inside Data Centers?",
    "url": "https://www.eetimes.com/connectivity-revolution-or-evolution-inside-data-centers/",
    "source": "Teresa Monteiro and Rimlee Deb Roy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:00:00+00:00",
    "summary": "AI transforms intra-data center networking, accelerating optical innovation while extending decades-long evolution in high-performance connectivity. The post Connectivity Revolution or Evolution Insid"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/levelplay-shows-off-magnetically-attached-fans-that-are-reversible-connect-via-pogo-pins-and-usb-c-plus-an-aio-that-trades-a-screen-for-a-big-knob",
    "domain": "AI 算力 / 半导体",
    "title": "Levelplay shows off magnetically attached fans that are reversible, connect via pogo pins and USB-C – plus an AIO that trades a screen for a big knob",
    "url": "https://www.tomshardware.com/pc-components/cooling/levelplay-shows-off-magnetically-attached-fans-that-are-reversible-connect-via-pogo-pins-and-usb-c-plus-an-aio-that-trades-a-screen-for-a-big-knob",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T19:32:35+00:00",
    "summary": "Levelplay took to Computex with some interesting cooling concepts, like magnetic fans that can be reversed in seconds, and an AIO that puts a big tactile knob for fan control on top of your CPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinese-startup-claims-photonic-chip-production-without-duv-lithography-says-nanoimprint-process-cuts-costs-by-90-percent-8-inch-wafers-produced-without-conventional-optical-lithography",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese startup claims photonic chip production without DUV lithography, says nanoimprint process cuts costs by 90% — 8-inch wafers produced without conventional optical lithography",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinese-startup-claims-photonic-chip-production-without-duv-lithography-says-nanoimprint-process-cuts-costs-by-90-percent-8-inch-wafers-produced-without-conventional-optical-lithography",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:54:45+00:00",
    "summary": "Chinese startup Prinano claims it produced 8-inch photonic chip wafers without DUV lithography, using nanoimprint technology that cuts costs by 90%."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/macos/apple-demonstrates-cross-platform-siri-upgrades-in-macos-27-golden-gate-at-wwdc-update-brings-liquid-glass-improvements-and-unifies-ai-strategy",
    "domain": "AI 算力 / 半导体",
    "title": "Apple demonstrates cross-platform Siri upgrades in macOS 27 Golden Gate at WWDC — update brings Liquid Glass improvements and unifies AI strategy",
    "url": "https://www.tomshardware.com/software/macos/apple-demonstrates-cross-platform-siri-upgrades-in-macos-27-golden-gate-at-wwdc-update-brings-liquid-glass-improvements-and-unifies-ai-strategy",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:40:17+00:00",
    "summary": "At WWDC, Apple revealed its upcoming macOS update, macOS 27 Golden Gate, with a more refined Liquid Glass design and cross-platform Siri and Apple Intelligence features."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-expands-new-game-boosting-ibot-software-with-seven-more-games-up-to-a-27-percent-improvement-team-blue-claims-12-percent-average-jump-in-newly-supported-titles",
    "domain": "AI 算力 / 半导体",
    "title": "Intel expands new game-boosting iBOT software with seven more games, up to a 27% improvement — Team Blue claims 12% average jump in newly-supported titles",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-expands-new-game-boosting-ibot-software-with-seven-more-games-up-to-a-27-percent-improvement-team-blue-claims-12-percent-average-jump-in-newly-supported-titles",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T17:49:06+00:00",
    "summary": "Intel is expanding its performance-boosting iBOT feature with seven new games."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/most-new-us-ai-data-centers-are-going-up-on-drought-land",
    "domain": "AI 算力 / 半导体",
    "title": "Most new U.S. AI data centers are being built in drought zones — two-thirds of 809 planned projects set for areas with water shortages",
    "url": "https://www.tomshardware.com/tech-industry/most-new-us-ai-data-centers-are-going-up-on-drought-land",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T16:39:27+00:00",
    "summary": "About two-thirds of the 809 data centers planned across the U.S. are slated for land that has been in drought over the past year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/farmer-donates-land-for-a-park-city-sells-it-for-data-center-development-usd10-gift-became-usd10m-for-city-government-with-usd30m-tax-expected-over-next-decade",
    "domain": "AI 算力 / 半导体",
    "title": "Farmer donates land for a park, city sells it for data center development — $10 gift became $10M for city government, with $30M tax expected over next decade",
    "url": "https://www.tomshardware.com/tech-industry/farmer-donates-land-for-a-park-city-sells-it-for-data-center-development-usd10-gift-became-usd10m-for-city-government-with-usd30m-tax-expected-over-next-decade",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T16:24:05+00:00",
    "summary": "Texas farmland originally donated in 1999 to be used only as a public park has been sold to a data center developer for $10 million."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/demand-for-data-center-cpus-has-surged-and-ai-agents-are-responsible-why-the-cpu-to-gpu-ratio-is-more-important-than-ever-for-hyperscalers",
    "domain": "AI 算力 / 半导体",
    "title": "Demand for data center CPUs has surged, and AI agents are responsible – why the CPU to GPU ratio is more important than ever for hyperscalers",
    "url": "https://www.tomshardware.com/pc-components/cpus/demand-for-data-center-cpus-has-surged-and-ai-agents-are-responsible-why-the-cpu-to-gpu-ratio-is-more-important-than-ever-for-hyperscalers",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T15:15:55+00:00",
    "summary": "The massive AI gold rush has a new bottleneck set in its sights, CPUs. But what's driving the demand? We interview industry experts to find out."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/asml-staff-want-to-boycott-musk",
    "domain": "AI 算力 / 半导体",
    "title": "Disgruntled ASML employees threaten to boycott Elon Musk conference appearance — staff express ire at political involvement and 'Nazi sympathies'",
    "url": "https://www.tomshardware.com/tech-industry/asml-staff-want-to-boycott-musk",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T13:27:58+00:00",
    "summary": "ASML has confirmed that a group of disgruntled workers is pushing back hard against an invitation for Elon Musk to address the equipment maker’s closed annual tech conference."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/travlfi-journeygo-5g-mobile-hotspot-review",
    "domain": "AI 算力 / 半导体",
    "title": "Travlfi JourneyGo 5G mobile hotspot review – Affordably priced, but lacking in performance and features",
    "url": "https://www.tomshardware.com/networking/routers/travlfi-journeygo-5g-mobile-hotspot-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T13:11:43+00:00",
    "summary": "The Travlfi JourneyGo 5G makes a good first impression with its $299 price and lightweight design, but that shine wears off quickly."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/finland-concludes-baltic-cable-sabotage-investigation-with-four-suspects-referred-to-prosecutors",
    "domain": "AI 算力 / 半导体",
    "title": "Four suspects identified in Finland undersea cable damage investigation — criminal case referred to prosecutors for consideration of charges",
    "url": "https://www.tomshardware.com/networking/finland-concludes-baltic-cable-sabotage-investigation-with-four-suspects-referred-to-prosecutors",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T12:32:55+00:00",
    "summary": "Finland's National Bureau of Investigation has concluded its criminal investigation into the damage to two undersea telecommunications cables in the Gulf of Finland on December 31st."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/bag-a-huge-usd308-saving-on-a-two-year-expressvpn-advanced-sub-and-get-four-bonus-months-on-top-for-free-78-percent-discount-gets-you-this-fast-no-logs-vpn-service-with-support-for-12-simultaneous-connections-for-just-usd83",
    "domain": "AI 算力 / 半导体",
    "title": "Bag a huge $308 saving on a two-year ExpressVPN Advanced sub and get four bonus months on top for free — 78% discount gets you this fast no-logs VPN service with support for 12 simultaneous connection",
    "url": "https://www.tomshardware.com/software/vpn/bag-a-huge-usd308-saving-on-a-two-year-expressvpn-advanced-sub-and-get-four-bonus-months-on-top-for-free-78-percent-discount-gets-you-this-fast-no-logs-vpn-service-with-support-for-12-simultaneous-connections-for-just-usd83",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T11:41:23+00:00",
    "summary": "Save over $300 on this two-year ExpressVPN Advanced subscription, with support for 12 simultaneous devices, advanced web protection, and a bunch of other tools for just $83.72, with four months extra "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/nvidia-and-sk-hynix-ink-multi-year-memory-co-development-and-supply-agreement-seeks-to-address-extended-development-cycles",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and SK hynix ink multi-year memory co-development and supply agreement — seeks to address extended development cycles",
    "url": "https://www.tomshardware.com/pc-components/dram/nvidia-and-sk-hynix-ink-multi-year-memory-co-development-and-supply-agreement-seeks-to-address-extended-development-cycles",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T11:23:57+00:00",
    "summary": "Nvidia and SK hynix have inked a multi-year collaboration agreement under which the companies will co-develop next-generation memory technologies for Nvidia's upcoming platforms and SK hynix will supp"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-introduced-the-first-processor-in-the-x86-series-and-the-first-8086-microprocessor-on-this-day-in-1978-cpu-was-designed-as-a-temporary-substitute-for-the-delayed-iapx-432-project",
    "domain": "AI 算力 / 半导体",
    "title": "Intel introduced ‘the first processor in the x86 series and the first 8086 microprocessor’ on this day in 1978 — CPU was designed as a temporary substitute for the delayed iAPX 432 project",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-introduced-the-first-processor-in-the-x86-series-and-the-first-8086-microprocessor-on-this-day-in-1978-cpu-was-designed-as-a-temporary-substitute-for-the-delayed-iapx-432-project",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T11:21:46+00:00",
    "summary": "June 8, 1978, marked the birth of the x86 architecture with the arrival of the 16-bit Intel 8086 CPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/executives-are-cutting-jobs-for-an-ai-future-that-hasnt-fully-arrived-yet-even-as-productivity-gains-remain-difficult-to-prove-data-neither-confirms-nor-refutes-an-ai-unemployment-apocalypse",
    "domain": "AI 算力 / 半导体",
    "title": "Executives are cutting jobs for an AI future that hasn't fully arrived yet, even as productivity gains remain difficult to prove — data neither confirms nor refutes an AI unemployment apocalypse",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/executives-are-cutting-jobs-for-an-ai-future-that-hasnt-fully-arrived-yet-even-as-productivity-gains-remain-difficult-to-prove-data-neither-confirms-nor-refutes-an-ai-unemployment-apocalypse",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T11:20:00+00:00",
    "summary": "A growing number of CEOs expect AI-driven layoffs, but economic data paints a more complex picture as companies cut junior roles before proving AI delivers meaningful productivity gains."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amazon-is-offering-a-usd324-nvidia-rtx-5060-gpu-deal-in-a-lightning-sale-making-it-the-cheapest-model-available-1080p-gaming-on-a-budget",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon is offering a $324 Nvidia RTX 5060 GPU deal in a lightning sale, making it the cheapest model available — 1080p gaming on a budget",
    "url": "https://www.tomshardware.com/pc-components/gpus/amazon-is-offering-a-usd324-nvidia-rtx-5060-gpu-deal-in-a-lightning-sale-making-it-the-cheapest-model-available-1080p-gaming-on-a-budget",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T11:06:53+00:00",
    "summary": "Grab an RTX 5060 GPU deal while you still can. The $324 deal is selling out fast in Amazon's limited-time sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/anycubic-photon-mono-4-dips-below-usd190-saving-you-21-percent-off-its-retail-price-amazon-deal-saves-usd50-on-this-entry-level-resin-3d-printer",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic Photon Mono 4 dips below $190 saving you 21% off its retail price — Amazon deal saves $50 on this entry-level resin 3D printer",
    "url": "https://www.tomshardware.com/pc-components/anycubic-photon-mono-4-dips-below-usd190-saving-you-21-percent-off-its-retail-price-amazon-deal-saves-usd50-on-this-entry-level-resin-3d-printer",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T14:22:50+00:00",
    "summary": "The Anycubic Photon Mono 4 is on-sale at $189.99, giving you a $50 discount and saving you 21% off its retail price."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/msi-gigabyte-debut-new-5k-27-inch-mini-led-monitors-with-2-304-dimming-zones-and-glossy-panel-both-models-double-the-native-180-hz-refresh-rate-to-330-hz-at-1440p",
    "domain": "AI 算力 / 半导体",
    "title": "MSI, Gigabyte debut new 5K 27-inch Mini-LED monitors with 2,304 dimming zones and glossy panel — both models double the native 180 Hz refresh rate to 330 Hz at 1440p",
    "url": "https://www.tomshardware.com/monitors/msi-gigabyte-debut-new-5k-27-inch-mini-led-monitors-with-2-304-dimming-zones-and-glossy-panel-both-models-double-the-native-180-hz-refresh-rate-to-330-hz-at-1440p",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T14:19:42+00:00",
    "summary": "New Mini-LED monitors from MSI and Gigabyte featuring 5K panels with 2,304 dimming zones and glossy coatings have just been announced. These feature dual- and even triple-mode support, along with full"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/ukraines-birds-adapt-to-battlefield-environment-weaving-optical-fiber-nests-for-warmth-canny-feathered-friends-repurpose-scraps-of-this-spun-off-insulator-material",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine’s birds adapt to battlefield environment, weaving nests out of drone fiber-optic cables — resourceful wildlife adapts to miles of littered drone fibers",
    "url": "https://www.tomshardware.com/networking/ukraines-birds-adapt-to-battlefield-environment-weaving-optical-fiber-nests-for-warmth-canny-feathered-friends-repurpose-scraps-of-this-spun-off-insulator-material",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T13:55:53+00:00",
    "summary": "Birds in Donbas have been discovered feathering their nests with optical fiber."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-rdna-5-gaming-gpus-are-coming-late-next-year-according-to-aibs-at-computex-manufacturers-expect-new-team-red-cards-in-the-second-half-of-2027-alongside-nvidia",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's RDNA 5 gaming GPUs are coming late next year, according to AIBs at Computex — manufacturers expect new Team Red cards in the second half of 2027 alongside Nvidia",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-rdna-5-gaming-gpus-are-coming-late-next-year-according-to-aibs-at-computex-manufacturers-expect-new-team-red-cards-in-the-second-half-of-2027-alongside-nvidia",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T13:30:00+00:00",
    "summary": "AIB partners for AMD at the Computex 2026 show floor have said they expect next-gen RDNA 5 gaming GPUs to land sometime in the second half of 2027, or maybe even in early 2028. That launch schedule li"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/asml-beocmes-europes-most-valuable-company-ever-as-analysts-bet-on-higher-euv-output",
    "domain": "AI 算力 / 半导体",
    "title": "ASML becomes Europe's most valuable company ever as analysts bet on higher EUV output — its market cap hit $674 billion this week",
    "url": "https://www.tomshardware.com/tech-industry/asml-beocmes-europes-most-valuable-company-ever-as-analysts-bet-on-higher-euv-output",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T13:05:00+00:00",
    "summary": "ASML closed Wednesday, June 3rd, as the most valuable company in European history, reaching a market cap of $668 billion."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-signs-usd920m-monthly-compute-deal-with-spacex-companys-projected-annual-data-center-revenue-to-exceed-its-combined-proceeds-from-starlink-launch-services-and-ai-in-2025",
    "domain": "AI 算力 / 半导体",
    "title": "Google signs $920M monthly compute deal with SpaceX — company’s projected annual data center revenue to exceed its combined proceeds from Starlink, launch services, and AI in 2025",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-signs-usd920m-monthly-compute-deal-with-spacex-companys-projected-annual-data-center-revenue-to-exceed-its-combined-proceeds-from-starlink-launch-services-and-ai-in-2025",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T12:45:00+00:00",
    "summary": "Google's $920-million-a-month deal with SpaceX will let it secure 110,000 Nvidia GPUs starting October 2026. This is the second data center deal that SpaceX has secured in a matter of weeks, especiall"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/retropad-is-a-full-feature-parity-version-of-notepad-from-xp-in-just-2-749-bytes-x86-assembly-coded-apps-comes-from-windows-legend-dave-w-plummer",
    "domain": "AI 算力 / 半导体",
    "title": "RetroPad is a ‘full-feature-parity version of Notepad from XP’ in just 2,749 bytes — x86 assembly coded apps comes from Windows legend Dave W Plummer",
    "url": "https://www.tomshardware.com/software/windows/retropad-is-a-full-feature-parity-version-of-notepad-from-xp-in-just-2-749-bytes-x86-assembly-coded-apps-comes-from-windows-legend-dave-w-plummer",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T12:20:00+00:00",
    "summary": "A 'full-feature-parity version of Notepad' has been written in x86 assembly and it weighs in at under 3KB."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/russias-rassvet-constellation-loses-its-first-satellite-to-orbital-decay",
    "domain": "AI 算力 / 半导体",
    "title": "Russia’s new ‘Starlink‑Style’ Rassvet fleet loses its first satellite after weeks — Object 4 drops out of orbit but 15 others remain",
    "url": "https://www.tomshardware.com/tech-industry/russias-rassvet-constellation-loses-its-first-satellite-to-orbital-decay",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T12:00:00+00:00",
    "summary": "Object 4, one of 16 satellites in the first operational batch of Russia's Rassvet broadband network, re-entered Earth's atmosphere on approximately June 6th."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/developer-gets-half-life-running-at-30-fps-on-a-2007-nokia-n95",
    "domain": "AI 算力 / 半导体",
    "title": "Developer gets Half-Life running at 30 FPS on a Nokia N95 — proves 2007 phones can just about match 1998 PCs",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/developer-gets-half-life-running-at-30-fps-on-a-2007-nokia-n95",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:33:09+00:00",
    "summary": "Argentine developer Dante Leoncini has gotten the original Half-Life running at 30 FPS on a Nokia N95, the Symbian slider phone that launched in 2007."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/youtube-slams-1-7-volts-into-6700k-in-an-attempt-to-stop-the-cpu-from-bottlenecking-an-rtx-3080-pushes-gpu-utilization-from-60-percent-to-74-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Ludicrous overclock slams 1.7 volts into 6700K in an attempt to stop CPU from bottlenecking an RTX 3080 — 5.2 GHz on aging four-core pushes GPU utilization from 60% to 74%",
    "url": "https://www.tomshardware.com/pc-components/cpus/youtube-slams-1-7-volts-into-6700k-in-an-attempt-to-stop-the-cpu-from-bottlenecking-an-rtx-3080-pushes-gpu-utilization-from-60-percent-to-74-percent",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:00:00+00:00",
    "summary": "YouTuber challenges himself to alleviate a CPU bottleneck with a Core i7-6700K paired with an RTX 3080 through overclocking."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-reaches-almost-45-percent-cpu-share-in-the-latest-steam-hardware-survey-for-windows-gaming-pcs-ryzen-is-steadily-gaining-ground-against-intels-legacy-domination",
    "domain": "AI 算力 / 半导体",
    "title": "AMD reaches almost 45% CPU share in the latest Steam Hardware Survey for Windows gaming PCs — Ryzen is steadily gaining ground against Intel's legacy domination",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-reaches-almost-45-percent-cpu-share-in-the-latest-steam-hardware-survey-for-windows-gaming-pcs-ryzen-is-steadily-gaining-ground-against-intels-legacy-domination",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:00:00+00:00",
    "summary": "The latest Steam Hardware Survey is out and it's showing positive signs of growth for AMD, while Intel is unfortunately on a decline. The Red Team posted its best-ever CPU market share numbers in May "
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/elegoo-jupiter-2-resin-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "Elegoo Jupiter 2 Resin 3D Printer review: The giant returns for round two",
    "url": "https://www.tomshardware.com/3d-printing/elegoo-jupiter-2-resin-3d-printer-review",
    "source": "Matt Farmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:00:00+00:00",
    "summary": "Elegoo’s Jupiter 2 is a resin powerhouse with a large print area and 16K high-quality 3D printing at a reasonable price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-adds-igpu-less-mobile-chips-to-core-200h-lineup-raptor-lake-based-core-7-230h-and-core-5-205h-sport-disabled-graphics-for-small-form-factor-desktop-boards",
    "domain": "AI 算力 / 半导体",
    "title": "Intel adds iGPU-less mobile chips to Core 200H lineup — Raptor Lake-based Core 7 230H and Core 5 205H sport disabled graphics for small form factor desktop boards",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-adds-igpu-less-mobile-chips-to-core-200h-lineup-raptor-lake-based-core-7-230h-and-core-5-205h-sport-disabled-graphics-for-small-form-factor-desktop-boards",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T10:00:00+00:00",
    "summary": "Intel introduces two new Raptor Lake CPUs in its Core 200H series lineup featuring disabled integrated graphics chips. The new CPUs are likely geared towards SFF desktops rather than laptops and 2-in-"
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
    "id": "hn:48430986",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC CEO: I envy their 80% gross margins, but I would never do that",
    "url": "https://www.thestreet.com/investing/stocks/tsmc-taiwan-semiconductor-ceo-sends-blunt-message-to-memory-chip-rivals",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-07T01:53:27+00:00",
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
    "id": "rss:https://www.tomshardware.com/pc-components/chipsets/amd-b650-expansion-cards-hit-retail-starting-at-usd199-add-four-m-2-pcie-4-0-slots-and-11-usb-ports-to-any-pc-with-a-pcie-slot",
    "domain": "AI 算力 / 半导体",
    "title": "AMD B650 expansion cards hit retail starting at $199 — add four M.2 PCIe 4.0 slots and 11 USB ports to any PC with a PCIe slot",
    "url": "https://www.tomshardware.com/pc-components/chipsets/amd-b650-expansion-cards-hit-retail-starting-at-usd199-add-four-m-2-pcie-4-0-slots-and-11-usb-ports-to-any-pc-with-a-pcie-slot",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T16:29:46+00:00",
    "summary": "A couple of new add-in cards exemplify the trend of slapping AMD's Promontory 21 chipset onto a card for extra I/O expansion."
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
    "id": "hn:48449084",
    "domain": "大厂 AI 动态",
    "title": "Siri AI",
    "url": "https://www.apple.com/apple-intelligence/",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 525,
    "published_at": "2026-06-08T18:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48450142",
    "domain": "大厂 AI 动态",
    "title": "Apple reveals new AI architecture built around Google Gemini models",
    "url": "https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/",
    "source": "unclefuzzy",
    "platform": "hackernews",
    "points": 521,
    "published_at": "2026-06-08T19:14:47+00:00",
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
    "id": "hn:48413924",
    "domain": "大厂 AI 动态",
    "title": "Leak Reveals Microsoft Wants Its AI to Be 'Addictive'",
    "url": "https://kotaku.com/microsoft-ai-scout-addictive-satya-nadella-404-media-copilot-2000702924",
    "source": "thm",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-06-05T15:32:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48449424",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Hacked to Deliver Malware to Claude and Gemini Users",
    "url": "https://www.404media.co/microsoft-hacked-to-deliver-malware-to-claude-and-gemini-users/",
    "source": "guessmyname",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-08T18:34:04+00:00",
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
    "id": "rss:https://www.theverge.com/tech/946458/instagram-is-finally-letting-everyone-reorganize-their-grid",
    "domain": "大厂 AI 动态",
    "title": "Instagram is finally letting everyone reorganize their profile grid",
    "url": "https://www.theverge.com/tech/946458/instagram-is-finally-letting-everyone-reorganize-their-grid",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T23:58:30+00:00",
    "summary": "Nearly a year after it was announced, Instagram says it's delivering the ability to rearrange the posts in your profile grid. It had been available to some people in test groups, but as of June 8th, i"
  },
  {
    "id": "rss:https://www.theverge.com/tech/946446/apples-screen-time-updates-are-too-little-too-late",
    "domain": "大厂 AI 动态",
    "title": "Apple’s Screen Time updates are too little, too late",
    "url": "https://www.theverge.com/tech/946446/apples-screen-time-updates-are-too-little-too-late",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T23:41:00+00:00",
    "summary": "Apple spending a big chunk of its WWDC keynote on parental controls was surprising for several reasons. But the biggest is that, despite all the airtime, it didn't announce much new beyond a redesigne"
  },
  {
    "id": "rss:https://www.theverge.com/tech/946391/apple-ios-27-developer-beta-1-wwdc-2026-5-things",
    "domain": "大厂 AI 动态",
    "title": "5 things I already love from the iOS 27 beta",
    "url": "https://www.theverge.com/tech/946391/apple-ios-27-developer-beta-1-wwdc-2026-5-things",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T23:30:00+00:00",
    "summary": "iOS 27 has only been out for a few hours, and I've been messing around with the developer beta on my iPhone 16 Pro. I was most interested in trying out the new Siri AI, but unfortunately, I'm still on"
  },
  {
    "id": "rss:https://www.theverge.com/tech/946345/apple-safari-ai-update-extensions",
    "domain": "大厂 AI 动态",
    "title": "Apple is using AI to fix Safari’s extension problem",
    "url": "https://www.theverge.com/tech/946345/apple-safari-ai-update-extensions",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T22:14:17+00:00",
    "summary": "Apple is trying to solve one of Safari's biggest weaknesses with AI. Safari has long lacked the robust library of extensions that its rivals have, mainly due to the stringent development requirements "
  },
  {
    "id": "rss:https://www.theverge.com/tech/946329/tvos-27-absent-wwdc",
    "domain": "大厂 AI 动态",
    "title": "Where was tvOS 27 at WWDC?",
    "url": "https://www.theverge.com/tech/946329/tvos-27-absent-wwdc",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T22:04:42+00:00",
    "summary": "Every year, Apple's Worldwide Developers Conference gives us a first look at what's coming next to the company's many operating systems. But missing from today's keynote, apart from a single graphic l"
  },
  {
    "id": "rss:https://www.theverge.com/policy/946331/apple-parental-controls-child-accounts-wwdc",
    "domain": "大厂 AI 动态",
    "title": "Apple’s new parental controls are for keeping Apple out of trouble",
    "url": "https://www.theverge.com/policy/946331/apple-parental-controls-child-accounts-wwdc",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T21:48:08+00:00",
    "summary": "When Apple put child safety front and center at WWDC on Monday, its stated goal was helping parents fine-tune their kids' online experiences and avoid excessive screen time. But amid a global debate o"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/946335/openai-ipo-s-1-confidential",
    "domain": "大厂 AI 动态",
    "title": "OpenAI files for IPO, following Anthropic",
    "url": "https://www.theverge.com/ai-artificial-intelligence/946335/openai-ipo-s-1-confidential",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T21:38:29+00:00",
    "summary": "OpenAI on Monday checked off a preliminary step in the IPO race that it and rival Anthropic have been competing in for the better part of a year: The company announced it has confidentially submitted "
  },
  {
    "id": "rss:https://www.theverge.com/tech/946260/apple-wwdc-2026-ios-ipados-macos-watchos-visionos-27-features-missed",
    "domain": "大厂 AI 动态",
    "title": "44 things coming to your Apple devices that you might have missed",
    "url": "https://www.theverge.com/tech/946260/apple-wwdc-2026-ios-ipados-macos-watchos-visionos-27-features-missed",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T20:26:52+00:00",
    "summary": "This year's WWDC keynote was all about AI. But with all the attention on Apple Intelligence and Siri AI, the company breezed by - or neglected to mention - a bunch of cool, smaller features across its"
  },
  {
    "id": "rss:https://www.theverge.com/news/946147/apple-watchos-27-ipados-27-supported-devices-dropped",
    "domain": "大厂 AI 动态",
    "title": "Apple drops support for a long list of Apple Watches with latest OS updates",
    "url": "https://www.theverge.com/news/946147/apple-watchos-27-ipados-27-supported-devices-dropped",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T19:45:00+00:00",
    "summary": "I hope you have a modern Apple Watch or iPad, because otherwise watchOS 27 and iPadOS 27 won't run on your device. Apple often drops support for older devices with its latest software updates, but thi"
  },
  {
    "id": "rss:https://www.theverge.com/tech/943145/apple-watch-watchos-27-wwdc-2026",
    "domain": "大厂 AI 动态",
    "title": "Apple announces watchOS 27, now with Siri AI",
    "url": "https://www.theverge.com/tech/943145/apple-watch-watchos-27-wwdc-2026",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T19:34:10+00:00",
    "summary": "Apple just announced watchOS 27, the next version of its Apple Watch operating system, introducing support for Siri AI, a redesigned \"dynamic\" app grid, and improvements to health and fitness tracking"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/zeptos-ipo-filing-reveals-fast-growth-bigger-losses-and-a-valuation-question-nobodys-answered-yet/",
    "domain": "大厂 AI 动态",
    "title": "Zepto’s IPO filing reveals fast growth, bigger losses, and a valuation question nobody’s answered yet",
    "url": "https://techcrunch.com/2026/06/08/zeptos-ipo-filing-reveals-fast-growth-bigger-losses-and-a-valuation-question-nobodys-answered-yet/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T05:07:17+00:00",
    "summary": "Zepto's advertising revenue jumped 151%, outpacing the company's 104% growth in operating revenue."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/why-apples-slow-and-steady-ai-bet-is-starting-to-look-pretty-smart/",
    "domain": "大厂 AI 动态",
    "title": "Why Apple’s slow-and-steady AI bet is starting to look pretty smart",
    "url": "https://techcrunch.com/2026/06/08/why-apples-slow-and-steady-ai-bet-is-starting-to-look-pretty-smart/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T01:56:48+00:00",
    "summary": "Can Apple's new AI glow up put to bed accusations that it's losing an all-important industry race?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/mercors-brendan-foody-calls-out-sequoia-over-dual-pricing-valuation-tricks/",
    "domain": "大厂 AI 动态",
    "title": "Mercor’s Brendan Foody calls out Sequoia, accusing it of ‘dual-pricing’ valuation tricks",
    "url": "https://techcrunch.com/2026/06/08/mercors-brendan-foody-calls-out-sequoia-over-dual-pricing-valuation-tricks/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T00:45:56+00:00",
    "summary": "Sequoia is just one of the top firms that sells same equity at two different prices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/as-openai-files-for-ipo-sam-altmans-eye-scanning-company-is-doing-layoffs-report-says/",
    "domain": "大厂 AI 动态",
    "title": "As OpenAI files for IPO, Sam Altman’s eye-scanning company is doing layoffs, report says",
    "url": "https://techcrunch.com/2026/06/08/as-openai-files-for-ipo-sam-altmans-eye-scanning-company-is-doing-layoffs-report-says/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T22:41:45+00:00",
    "summary": "Tools for Humanity, Sam Altman's identity verification company, is reportedly struggling to generate revenue and will downsize its staff."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apples-wwdc-ai-demos-looked-more-real-after-250m-false-ad-settlement/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s WWDC AI demos looked more real after $250M false ad settlement",
    "url": "https://techcrunch.com/2026/06/08/apples-wwdc-ai-demos-looked-more-real-after-250m-false-ad-settlement/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T22:39:57+00:00",
    "summary": "The vibe of Apple's 2026 WWDC keynote felt like a spouse proudly listing all the honey-do-list items tackled. One subtle example: the many AI demos of someone standing, phone in hand."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/following-anthropic-openai-files-confidentially-for-ipo/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI files confidentially for IPO, following Anthropic",
    "url": "https://techcrunch.com/2026/06/08/following-anthropic-openai-files-confidentially-for-ipo/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T21:29:57+00:00",
    "summary": "The filing comes a little more than a week after its main rival, Anthropic, also filed to go public, ramping up the race between the two AI firms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apple-plays-catch-up-at-wwdc/",
    "domain": "大厂 AI 动态",
    "title": "Apple plays catch-up at WWDC",
    "url": "https://techcrunch.com/2026/06/08/apple-plays-catch-up-at-wwdc/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T21:15:42+00:00",
    "summary": "Apple spent much of its WWDC keynote highlighting fixes, performance improvements, and long-requested features before unveiling its upgraded AI-powered Siri, signaling that the company wants users to "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apple-bets-cheaper-ai-will-woo-small-developers/",
    "domain": "大厂 AI 动态",
    "title": "Apple bets cheaper AI will woo small developers",
    "url": "https://techcrunch.com/2026/06/08/apple-bets-cheaper-ai-will-woo-small-developers/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T20:53:55+00:00",
    "summary": "As AI experimentation grows more expensive, Apple is waiving cloud API costs for developers with fewer than 2 million first-time App Store downloads."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/waymo-bought-apples-self-driving-car-proving-ground-for-220m/",
    "domain": "大厂 AI 动态",
    "title": "Waymo bought Apple’s self-driving car proving ground for $220M",
    "url": "https://techcrunch.com/2026/06/08/waymo-bought-apples-self-driving-car-proving-ground-for-220m/",
    "source": "Kirsten Korosec, Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T20:50:55+00:00",
    "summary": "Waymo has acquired a massive 5,500-acre proving ground in Arizona owned by Route 14 Investment Partners LLC, a Delaware shell company associated with Apple, according to documents filed with Maricopa "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s open source tools were hacked to steal passwords of AI developers",
    "url": "https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T20:03:44+00:00",
    "summary": "Microsoft shut down dozens of GitHub code repositories for Azure and AI coding tools after a reported hack."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/",
    "domain": "大厂 AI 动态",
    "title": "WWDC 2026: Everything announced on Siri AI, iOS 27, Apple Intelligence and more",
    "url": "https://techcrunch.com/2026/06/08/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/",
    "source": "Morgan Little, Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T19:41:32+00:00",
    "summary": "Apple primarily made the case for an improved experience with its longstanding Siri assistant, which like most other announcements had a hefty helping of AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/pentagon-says-alibaba-baidu-byd-and-unitree-support-chinas-military/",
    "domain": "大厂 AI 动态",
    "title": "Pentagon says Alibaba, Baidu, BYD, and Unitree support China’s military",
    "url": "https://techcrunch.com/2026/06/08/pentagon-says-alibaba-baidu-byd-and-unitree-support-chinas-military/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:57:49+00:00",
    "summary": "The Trump administration released the updated version of the list four months ago and then quickly pulled it without explaining why"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apple-just-taught-your-iphone-to-finish-your-sentences-your-photos-and-your-workflows/",
    "domain": "大厂 AI 动态",
    "title": "Apple just taught your iPhone to finish your sentences, your photos, and your workflows",
    "url": "https://techcrunch.com/2026/06/08/apple-just-taught-your-iphone-to-finish-your-sentences-your-photos-and-your-workflows/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:48:45+00:00",
    "summary": "Apple is adding new AI-powered features to Safari, Shortcuts, and Password apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apple-will-let-you-build-workflows-using-ai-in-its-new-shortcuts-app/",
    "domain": "大厂 AI 动态",
    "title": "Apple will let you build workflows using AI in its new Shortcuts app",
    "url": "https://techcrunch.com/2026/06/08/apple-will-let-you-build-workflows-using-ai-in-its-new-shortcuts-app/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:45:12+00:00",
    "summary": "Shortcuts gets an AI upgrade, letting you describe the workflow you want in a prompt."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apples-image-playground-doesnt-suck-anymore/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s Image Playground doesn’t suck anymore",
    "url": "https://techcrunch.com/2026/06/08/apples-image-playground-doesnt-suck-anymore/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:38:07+00:00",
    "summary": "Apple's AI image generator is getting a makeover that could make it more competitive."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apples-photos-app-is-getting-new-ai-editing-features/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s Photos app is getting new AI editing features",
    "url": "https://techcrunch.com/2026/06/08/apples-photos-app-is-getting-new-ai-editing-features/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:36:04+00:00",
    "summary": "A new spatial \"Reframe\" feature will let users use AI to adjust perspectives."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apple-gives-siri-its-own-dedicated-app/",
    "domain": "大厂 AI 动态",
    "title": "Apple gives Siri its own dedicated app",
    "url": "https://techcrunch.com/2026/06/08/apple-gives-siri-its-own-dedicated-app/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:33:42+00:00",
    "summary": "Siri is finally getting its own app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apple-is-fixing-the-headache-of-splitting-the-bill-with-its-new-siri-in-camera-feature/",
    "domain": "大厂 AI 动态",
    "title": "Apple is fixing the headache of splitting the bill with its new Siri in Camera feature",
    "url": "https://techcrunch.com/2026/06/08/apple-is-fixing-the-headache-of-splitting-the-bill-with-its-new-siri-in-camera-feature/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:23:04+00:00",
    "summary": "\"If you're grabbing a bite with friends and point your iPhone at the bill, then [you can] select what you ordered to split the tab with Apple Cash,\" said Apple VP of Software Sebastien Marineau-Mes."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apple-puts-parents-back-in-control-of-kids-iphone-use/",
    "domain": "大厂 AI 动态",
    "title": "Apple puts parents back in control of kids’ iPhone use",
    "url": "https://techcrunch.com/2026/06/08/apple-puts-parents-back-in-control-of-kids-iphone-use/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:07:32+00:00",
    "summary": "Apple is putting control back into the hands of parents with more granular screen time features."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/08/apples-health-app-can-now-tell-you-if-youre-in-perimenopause/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s Health app can now tell you if you’re in perimenopause",
    "url": "https://techcrunch.com/2026/06/08/apples-health-app-can-now-tell-you-if-youre-in-perimenopause/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:03:05+00:00",
    "summary": "Cycle tracker will now notify women when their cycle patterns are suggestive of perimenopause."
  },
  {
    "id": "rss:https://stratechery.com/2026/google-buys-compute-from-spacex-broadcoms-outlook-apples-ai-politics/",
    "domain": "大厂 AI 动态",
    "title": "Google Buys Compute From SpaceX, Broadcom’s Outlook, Apple’s AI Politics",
    "url": "https://stratechery.com/2026/google-buys-compute-from-spacex-broadcoms-outlook-apples-ai-politics/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T10:00:00+00:00",
    "summary": "Google's deal with SpaceX, and Broadcom's earnings, both seem bullish for Nvidia. Then, what I'm looking for at WWDC."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/fcc-lifts-looming-deadline-for-amazon-leo-satellite-broadband-constellation/",
    "domain": "大厂 AI 动态",
    "title": "FCC lifts looming deadline for Amazon Leo satellite broadband constellation",
    "url": "https://arstechnica.com/space/2026/06/fcc-lifts-looming-deadline-for-amazon-leo-satellite-broadband-constellation/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T00:59:40+00:00",
    "summary": "The waiver \"serves the public interest by promoting a second large satellite broadband constellation.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/tests-suggest-russian-satellites-can-jam-gps-on-a-continental-scale/",
    "domain": "大厂 AI 动态",
    "title": "Tests suggest Russian satellites can jam GPS on a continental scale",
    "url": "https://arstechnica.com/space/2026/06/tests-suggest-russian-satellites-can-jam-gps-on-a-continental-scale/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T21:56:28+00:00",
    "summary": "Mystery of GPS interference across Europe raises questions about Russian motives."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/macos-27-requires-apple-silicon-as-apple-draws-down-the-intel-mac-era/",
    "domain": "大厂 AI 动态",
    "title": "macOS 27 requires Apple Silicon, as Apple draws down the Intel Mac era",
    "url": "https://arstechnica.com/gadgets/2026/06/macos-27-requires-apple-silicon-as-apple-draws-down-the-intel-mac-era/",
    "source": "Andrew Cunningham",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T21:03:56+00:00",
    "summary": "You'll need an M1 or better to run the next release of macOS."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/ios-27-and-ipados-27-dont-drop-support-for-any-iphones-and-just-a-few-ipads/",
    "domain": "大厂 AI 动态",
    "title": "iOS 27 and iPadOS 27 don't drop support for any iPhones—and just a few iPads",
    "url": "https://arstechnica.com/gadgets/2026/06/ios-27-and-ipados-27-dont-drop-support-for-any-iphones-and-just-a-few-ipads/",
    "source": "Andrew Cunningham",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T20:55:58+00:00",
    "summary": "This promises to be a solid release for aging iPhones."
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 1056,
    "published_at": "2026-06-04T22:48:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48455233",
    "domain": "股票",
    "title": "We Think the SpaceX IPO Is Overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued?content_id=20768396545",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 202,
    "published_at": "2026-06-09T01:56:40+00:00",
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
    "id": "hn:48446310",
    "domain": "股票",
    "title": "Italy's Bending Spoons, owner of AOL and Vimeo, files for Nasdaq IPO",
    "url": "https://www.reuters.com/legal/transactional/italys-bending-spoons-files-us-ipo-2026-06-08/",
    "source": "mmarian",
    "platform": "hackernews",
    "points": 117,
    "published_at": "2026-06-08T15:04:17+00:00",
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
    "id": "hn:48394034",
    "domain": "股票",
    "title": "The SpaceX IPO will be the theft of the century",
    "url": "https://montanaskeptic.substack.com/p/the-spacex-ipo-will-be-the-theft",
    "source": "400thecat",
    "platform": "hackernews",
    "points": 142,
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
    "id": "hn:48385866",
    "domain": "股票",
    "title": "SpaceX's IPO is a disaster waiting to happen for your pension fund",
    "url": "https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/",
    "source": "anonymousDan",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48452224",
    "domain": "股票",
    "title": "OpenAI Confidentially Files for IPO",
    "url": "https://www.cnbc.com/2026/06/08/openai-confidentially-files-for-ipo-prepping-wall-street-for-ai-debut.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-08T21:16:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436328",
    "domain": "股票",
    "title": "Musk's SpaceX IPO Narrative Is a Whole New Level of Bullshit",
    "url": "https://text.tchncs.de/chronik-des-laufenden-wahnsinns/h1elon-musk-has-spouted-his-fair-share-of-bullshit-but-his-latest-claims-about",
    "source": "doener",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-06-07T16:24:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451099",
    "domain": "股票",
    "title": "Why Morningstar believes the SpaceX IPO is overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued",
    "source": "ForHackernews",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-08T20:07:20+00:00",
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
    "id": "wscn:3774200",
    "domain": "股票",
    "title": "通胀冲向4%，债市逼沃什亮剑：敢不敢对特朗普说“不”？",
    "url": "https://wallstreetcn.com/articles/3774200",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:44:32+00:00",
    "summary": "周三即将公布的CPI预计逼近4.2%、债市抢先定价加息、特朗普却高喊降息——美联储新主席凯文·沃什的首场FOMC会议已成三方博弈的决战场。政策声明措辞、点阵图走向、风险分布倾斜，三个信号将同步揭示他能否在白宫意志与市场信任之间守住央行独立性的最后防线。"
  },
  {
    "id": "wscn:3774199",
    "domain": "股票",
    "title": "苹果AI终于跨过第一道坎，但马拉松才刚开始",
    "url": "https://wallstreetcn.com/articles/3774199",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:44:12+00:00",
    "summary": "苹果WWDC 2026让华尔街多空阵营正面交锋：大摩、高盛力挺AI战略成形、iCloud变现路径清晰，目标价高达360美元；瑞银、巴克莱却直指\"进化非革命\"，空方目标价低至253美元。逾8.5亿台设备被排除、35%市场缺席、三大近期催化剂依次排开。苹果这场AI马拉松，今秋才是真正的发令枪。"
  },
  {
    "id": "wscn:3774175",
    "domain": "股票",
    "title": "沪指收复4000点，创业板涨超3%，芯片半导体集体爆发，恒科指涨逾1%，科网股反弹，“双焦”大跌，焦煤跌停",
    "url": "https://wallstreetcn.com/articles/3774175",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:22:56+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超2900股飘绿，上午半天成交1.63万亿。沪深两市半日成交额1.61万亿，较上个交易日缩量近1600亿。板块方面，半导体产业链爆发，PCB、硅片、晶圆、光刻机方向领涨；CPO、HBM、AI应用、固态电池、光伏题材活跃。煤炭、油气、白酒、零售板块走弱。"
  },
  {
    "id": "wscn:3774191",
    "domain": "股票",
    "title": "阿斯利康加入减肥药赛道：口服药减重11.8%",
    "url": "https://wallstreetcn.com/articles/3774191",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:19:20+00:00",
    "summary": "阿斯利康的口服减肥药elecoglipron二期数据亮眼，36周内减重11.8%。虽效果略逊于礼来，但5%的副作用退出率远低于礼来的17%，且无需空腹。目前该药已进三期，正推进与心肾药联合开发以形成差异化竞争。"
  },
  {
    "id": "wscn:3774195",
    "domain": "股票",
    "title": "张瑜：五问“厄尔尼诺”",
    "url": "https://wallstreetcn.com/articles/3774195",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:17:09+00:00",
    "summary": "历史数据显示，高温强降雨将推高鲜菜鲜果价格，扰动工业生产与建筑施工月度数据，并显著拉升电力需求——2016年超强厄尔尼诺期间，7-9月居民用电增速从5.4%骤升至24.9%，前车之鉴值得警惕。后续来看，一方面，可以继续跟踪厄尔尼诺的演进情况，另一方面，可通过货车通行、食品高频等数据跟踪对经济、通胀的影响。"
  },
  {
    "id": "wscn:3774194",
    "domain": "股票",
    "title": "烧掉1万亿美元后，美国公司开始给DeepSeek充值",
    "url": "https://wallstreetcn.com/articles/3774194",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:14:32+00:00",
    "summary": "美国企业AI账单正在失控——Uber四个月烧光全年Token预算，Salesforce一年付给Anthropic约3亿美元。就在此刻，DeepSeek登顶美国企业订阅榜。更罕见的是，这些企业不是下载开源权重自己跑，而是直接付钱、直连服务器传输数据。连首席经济学家也直言：\"我没有料到美国公司会去用DeepSeek。\""
  },
  {
    "id": "wscn:3774198",
    "domain": "股票",
    "title": "一个月内集中下架，健康险“理财化”已产品退场",
    "url": "https://wallstreetcn.com/articles/3774198",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:10:47+00:00",
    "summary": "曾经在互联网保险渠道热销的“高现价+医疗金账户”健康险产品，正在快速退出市场。\n截至6月初，复星联合..."
  },
  {
    "id": "wscn:3774181",
    "domain": "股票",
    "title": "增速19.4%！AI需求强劲，中国5月出口全面超预期",
    "url": "https://wallstreetcn.com/articles/3774181",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:04:37+00:00",
    "summary": "数据显示，5月计算机及零部件出口同比增幅从4月的47%进一步加速至66%，创2010年以来最快增速；集成电路出口同比激增111%，创下2013年以来最大单月涨幅。进口端同样表现强劲，企业积极购入境外芯片与设备，其中韩国对华半导体出口在5月同比暴涨逾200%。"
  },
  {
    "id": "wscn:3774197",
    "domain": "股票",
    "title": "知名科技记者爆料：Anthropic明天将发布“公开版本Mythos”",
    "url": "https://wallstreetcn.com/articles/3774197",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T06:01:26+00:00",
    "summary": "科技记者Alex Heath透露，Anthropic计划于明日向公众发布Mythos模型的公开版本，可能更名为“Claude Fable 5”。为防范其强悍的网络安全双重用途风险，该公开版本将内置“实质性安全护栏”，开放尺度低于此前仅对合伙人开放的内部版本，但将大幅提升多轮复杂任务的处理能力。"
  },
  {
    "id": "wscn:3774176",
    "domain": "股票",
    "title": "AI短暂抛售潮后市场大反弹，韩股大涨逾8%，SK海力士涨超15％，油价走低",
    "url": "https://wallstreetcn.com/articles/3774176",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T05:48:42+00:00",
    "summary": "MSCI亚太股票指数攀升2.5%，此前一天录得3月以来最大单日跌幅。韩国Kospi领涨亚太，最高涨幅逾8%，芯片龙头SK海力士一度飙升逾14%，三星电子涨幅也曾达9.1%。布伦特原油下跌0.8%至每桶约93.50美元。"
  },
  {
    "id": "wscn:3774193",
    "domain": "股票",
    "title": "日经新闻：日本央行6月预计加息至1%，10月或紧接再行动",
    "url": "https://wallstreetcn.com/articles/3774193",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T05:46:05+00:00",
    "summary": "据日经报道，央行拟于本月16日将基准利率从0.75%上调至1.0%，行长植田和男将亲自提案且预计获多数通过。前央行高官警告，最快10月或再度加息，直言\"央行已落后于曲线\"。与此同时，日本央行拟2027年4月后暂停缩减国债购买，在加息路径上保留政策弹性。"
  },
  {
    "id": "wscn:3774109",
    "domain": "股票",
    "title": "纵向一体化覆铜板：龙头能否吃掉全部利润？",
    "url": "https://wallstreetcn.com/premium/articles/3774109?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T05:41:35+00:00",
    "summary": "自2026年初以来，CCL行业已历经多轮密集涨价，累计涨幅超40%，较年初上涨40%。本轮涨价的根本驱动力来自需求端AI算力爆发、成本端核心原材料全面紧缺、以及供给端产能结构性挤兑的三重共振。具备纵向一体化能力（自供电子布、铜箔、树脂）的CCL企业，在涨价周期中能够同时享受覆铜板产品涨价和上游原材料涨价的双重红利，利润弹性远高于同行业平均水平。"
  },
  {
    "id": "wscn:3774192",
    "domain": "股票",
    "title": "OpenAI跟进Anthropic：必要时放缓前沿AI开发，呼吁建立国际机构",
    "url": "https://wallstreetcn.com/articles/3774192",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T05:28:36+00:00",
    "summary": "OpenAI与Anthropic罕见表态支持\"必要时放缓\"前沿AI开发，并倡议建立国际协调机制，为行业史上首次。然而批评者直指这是监管俘获策略——Anthropic年化营收即将从90亿飙至500亿美元，且已秘密提交IPO文件——\"刹车派\"与\"加速者\"竟是同一张面孔。"
  },
  {
    "id": "wscn:3774189",
    "domain": "股票",
    "title": "又一半导体巨头要登陆港交所了",
    "url": "https://wallstreetcn.com/articles/3774189",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T05:03:50+00:00",
    "summary": "市场将如何定价"
  },
  {
    "id": "wscn:3773871",
    "domain": "股票",
    "title": "硅片行业的“结构性牛市”：AI芯片“喂饱”硅片巨头，国产硅片迎来黄金窗口",
    "url": "https://wallstreetcn.com/premium/articles/3773871?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:50:18+00:00",
    "summary": "硅片涨价真相：不是全面短缺，而是“冰火两重天”。"
  },
  {
    "id": "wscn:3774188",
    "domain": "股票",
    "title": "指数动态焕新蓄力科创成长，天弘三大指数产品把握调样红利",
    "url": "https://wallstreetcn.com/articles/3774188",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:14:11+00:00",
    "summary": "针对普通理财人群，无需耗费大量精力深耕个股研究、纠结择时点位，在匹配自身风险承受能力的前提下，通过定投布局天弘创业板、天弘科创 50、天弘科创创业 50三只指数产品，即可借力指数天然的调样优化机制，自动完成持仓优胜劣汰，一键布局科创板、创业板优质科创企业成长价值。"
  },
  {
    "id": "wscn:3774182",
    "domain": "股票",
    "title": "摩根大通：全球原油库存6月下旬进入压力区间，9月触底",
    "url": "https://wallstreetcn.com/articles/3774182",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T03:47:19+00:00",
    "summary": "摩根大通报告显示，全球原油市场表面平静之下，库存正在加速消耗。自3月以来全球库存已累计下降约4.5亿桶，预计6月下旬进入压力区间，9月触及运营底线。基准情景下霍尔木兹6月重开，布伦特全年维持约100美元；若封锁延续，四季度均价将额外上涨15美元。"
  },
  {
    "id": "wscn:3774185",
    "domain": "股票",
    "title": "本轮美股牛市与历史泡沫顶峰相比还差多远？",
    "url": "https://wallstreetcn.com/articles/3774185",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T03:43:47+00:00",
    "summary": "高盛首席美股策略师Ben Snider最新报告揭示，当前市场亢奋程度已升至历史第86百分位，逼近但未及2000年互联网泡沫与2021年牛市顶峰。标普500近两个月狂飙15%，创50年来波动率调整后最强反弹纪录。四大顶峰信号尚未全面触发，但每一项都比年初更接近警戒线——窗口仍开着，却正在慢慢收窄。"
  },
  {
    "id": "wscn:3774184",
    "domain": "股票",
    "title": "\"替代低价值人力资本\"！华尔街AI化提速，应届毕业生与AI抢饭碗",
    "url": "https://wallstreetcn.com/articles/3774184",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T03:43:41+00:00",
    "summary": "AI正在重塑华尔街用人逻辑，首当其冲的是刚入职场的年轻人。摩根大通、花旗等巨头大举投入AI建设的同时压缩初级招聘，客服、合规、交易监控岗位加速被替代。更值得警惕的是：部分银行或借AI之名行裁员之实，将成本削减包装成技术升级。金融业的入场券，正变得越来越难拿。"
  },
  {
    "id": "wscn:3774186",
    "domain": "股票",
    "title": "险资抱团叠加分红潮起，保险板块底部夯实，平安凭服务生态领跑新周期",
    "url": "https://wallstreetcn.com/articles/3774186",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T03:26:54+00:00",
    "summary": "当下资本市场，低利率环境持续发酵，资金四处寻觅稳健资产。保险板块在经历长时间估值蛰伏后，两大风向标式..."
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
    "id": "hn:48419956",
    "domain": "股票",
    "title": "Nasdaq falls 4% and suffers worst day since April 2025 traders flee chip stocks",
    "url": "https://www.cnbc.com/2026/06/04/stock-market-today-live-updates.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-06T00:02:38+00:00",
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
    "id": "hn:48404734",
    "domain": "股票",
    "title": "Fidelity lowers SpaceX IPO entry requirement from $500,000 to just $2,000",
    "url": "https://finance.yahoo.com/markets/stocks/articles/fidelity-cuts-spacex-ipo-eligibility-183319186.html",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-04T21:15:18+00:00",
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
    "id": "hn:48454210",
    "domain": "金融",
    "title": "Federal judge blocks H1B visa $100K fee",
    "url": "https://www.alaskasnewssource.com/2026/06/08/federal-judge-blocks-h1-b-visa-100k-fee/",
    "source": "naturalmovement",
    "platform": "hackernews",
    "points": 140,
    "published_at": "2026-06-09T00:01:37+00:00",
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
    "points": 89,
    "published_at": "2026-06-01T18:02:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436542",
    "domain": "金融",
    "title": "Ripping a DVD, a federal crime in 1999, requires $22 and free software in 2026",
    "url": "https://ringmast4r.substack.com/p/in-1999-this-was-a-federal-crime",
    "source": "akkartik",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-07T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48438281",
    "domain": "金融",
    "title": "Boomers are hoarding most of America's wealth and power",
    "url": "https://finance.yahoo.com/economy/articles/golden-years-not-golden-boomers-113000201.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-06-07T20:35:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451917",
    "domain": "金融",
    "title": "Federal judge rules Trump's $100k fee for H-1B visas unlawful",
    "url": "https://www.theguardian.com/us-news/2026/jun/08/trump-h-1b-visa-fee-invalidated",
    "source": "xpl",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-06-08T20:57:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48384810",
    "domain": "金融",
    "title": "Tesla retroactively added 'supervised' to FSD contracts owners signed years ago",
    "url": "https://electrek.co/2026/06/03/tesla-retroactively-modified-fsd-contracts-supervised/",
    "source": "breve",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-06-03T14:43:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48449003",
    "domain": "金融",
    "title": "Half of Americans say they're worse off financially than a year ago",
    "url": "https://www.cbsnews.com/news/americans-worse-off-financially-year-ago-fed-survey/",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-08T18:12:50+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07575",
    "domain": "金融",
    "title": "Forward-Looking Stress Testing Under Macro Scenarios: Stable SVaR Estimation Using a Hybrid GPR-HS Framework with SACS",
    "url": "https://arxiv.org/abs/2606.07575",
    "source": "Ujjwala Vadrevu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.07575v1 Announce Type: new Abstract: Regulatory stress testing frameworks, including the Comprehensive Capital Analysis and Review (CCAR) and the Internal Capital Adequacy Assessment Proces"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08207",
    "domain": "金融",
    "title": "Opportunity-Normalized Residence-Workplace Matching and the Scale-Sensitive Structure of Urban Commuting",
    "url": "https://arxiv.org/abs/2606.08207",
    "source": "Mingzhi Xiao, Yuki Takayama",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08207v1 Announce Type: new Abstract: Urban spatial structure is commonly evaluated through the spatial distribution of homes and jobs or through aggregate commuting outcomes. Yet these appr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08209",
    "domain": "金融",
    "title": "Markets Are Not Random, They Are Hard to Predict",
    "url": "https://arxiv.org/abs/2606.08209",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08209v1 Announce Type: new Abstract: Financial returns are often called ``random,'' but the word conflates ontic chance, epistemic ignorance, strategic feedback, and model instability. This"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08228",
    "domain": "金融",
    "title": "Post-Rejection Follow-up Sampling: A Methodology for Counterfactual Outcome Measurement in Algorithmic DEX Trading",
    "url": "https://arxiv.org/abs/2606.08228",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08228v1 Announce Type: new Abstract: Algorithmic trading systems on decentralised exchanges (DEXs) reject most candidate tokens they evaluate. The counterfactual outcome of rejected candida"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08232",
    "domain": "金融",
    "title": "Hour-Aware Adaptive Risk Management for Autonomous Memecoin Trading: A Multi-Layer Intelligence Framework",
    "url": "https://arxiv.org/abs/2606.08232",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08232v1 Announce Type: new Abstract: This paper measures hour-of-day effects, filter precision, fragility, and realised yield in a 15-day paper-traded deployment of an autonomous memecoin t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08265",
    "domain": "金融",
    "title": "Unintended Consequences of Recommender System Interventions: Evidence from a Field Experiment",
    "url": "https://arxiv.org/abs/2606.08265",
    "source": "Shilei Luo, Song Yao, Dennis J. Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08265v1 Announce Type: new Abstract: Platform content interventions in recommendation systems are typically evaluated as static \"nudges\", ignoring that the systems adaptively learn from the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08283",
    "domain": "金融",
    "title": "Macro Economists in the Machine: A Multi-Agent LLM Framework for Commodity-Related ETF Portfolio Construction",
    "url": "https://arxiv.org/abs/2606.08283",
    "source": "Yiqing Wang, Dehao Dai, Ding Ma, Kerui Geng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08283v1 Announce Type: new Abstract: We test whether large language models (LLMs) add value in commodity portfolio construction when the information set and implementation rules are held fi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08419",
    "domain": "金融",
    "title": "The Winner's Bliss in Common-Value Auctions under Horizontal Differentiation",
    "url": "https://arxiv.org/abs/2606.08419",
    "source": "Jiawei Chen, Anh Nguyen, Matthew Shum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08419v1 Announce Type: new Abstract: We study common-value auctions in which bidders have horizontally differentiated preferences. In a specific two-bidder parameterization, winning conveys"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08534",
    "domain": "金融",
    "title": "A Taxonomy of Real-World Asset Tokenization for Blockchain-Based Financial Infrastructure",
    "url": "https://arxiv.org/abs/2606.08534",
    "source": "Giorgio Vella, Luca Pennella, Mark C. Ballandies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08534v1 Announce Type: new Abstract: Real-world asset (RWA) tokenization has emerged as a prominent application of blockchain technology, enabling off-chain financial and non-financial asse"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08569",
    "domain": "金融",
    "title": "Stock Investment: The p-index Approach",
    "url": "https://arxiv.org/abs/2606.08569",
    "source": "Xinzhao Xie, Bopei Nie, Kuo-Ping Chang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08569v1 Announce Type: new Abstract: This paper has used European put option to construct the p-index risk measure to evaluate the performance of different investment strategies in China's "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08586",
    "domain": "金融",
    "title": "Cross-sectional topological anomaly scores and intraday return predictability in the S&P 500: A BallMapper, decoder-conditional VAE, and Function-on-Function regression approach",
    "url": "https://arxiv.org/abs/2606.08586",
    "source": "Krzysztof Ozimek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08586v1 Announce Type: new Abstract: Anomaly detection methods in financial time series score statistically unusual observations in observable data, not topologically misexpected persistent"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09003",
    "domain": "金融",
    "title": "Proof of Stake economy under centralized exchanges--a mean field model",
    "url": "https://arxiv.org/abs/2606.09003",
    "source": "Wenpin Tang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09003v1 Announce Type: new Abstract: We consider the interaction between centralized trading and decentralized Proof of Stake (PoS) blockchain ecosystems. Motivated by the increasing domina"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09025",
    "domain": "金融",
    "title": "Continuous Cash-Overlay Filters for a Static Growth--Defensive Risk Sleeve: Slow-Tail Compensation, V-Shape Crash Brakes, Walk-Forward Validation, and Max-Cash Combination",
    "url": "https://arxiv.org/abs/2606.09025",
    "source": "Zheli Xiong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09025v1 Announce Type: new Abstract: This paper studies a cash-overlay allocation problem between a static growth-defensive risky sleeve and interest-bearing cash. The risky sleeve is fixed"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09190",
    "domain": "金融",
    "title": "Planning resilient hydrogen supply chains under disruption risk",
    "url": "https://arxiv.org/abs/2606.09190",
    "source": "Silvian M. Radke, Philipp C. Verpoort, Falko Ueckerdt, Felix M\\\"usgens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09190v1 Announce Type: new Abstract: Despite growing concerns over energy security, infrastructure planning and modelling for emerging green fuel supply chains often neglect risks from supp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09274",
    "domain": "金融",
    "title": "Reverse Stress Testing for Multivariate Scenarios: A Conditional Framework for Stressed Time Series",
    "url": "https://arxiv.org/abs/2606.09274",
    "source": "Michele Sparviero, Lorenzo Viola",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09274v1 Announce Type: new Abstract: This paper develops a methodological framework for reverse stress testing (RST) in which a multivariate stress scenario, coherent with the empirical dep"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09454",
    "domain": "金融",
    "title": "Axiomatic Market Making",
    "url": "https://arxiv.org/abs/2606.09454",
    "source": "Frank M. V. Feys",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09454v1 Announce Type: new Abstract: This paper axiomatizes the bid-ask market maker's quoting rule. A quoting rule maps the maker's state, namely inventory, belief, variance, trade intensi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09472",
    "domain": "金融",
    "title": "Parameter Sensitivity Analysis of Hierarchical Spatial Economy: Trade Strategy around Brexit",
    "url": "https://arxiv.org/abs/2606.09472",
    "source": "Kiyohiro Ikeda, Yosuke Kogure, Hiroki Aizawa, Yuki Takayama",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09472v1 Announce Type: new Abstract: This paper presents a systematic framework for analyzing the economic parameter sensitivity of a hierarchical spatial economy within economic geography "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09478",
    "domain": "金融",
    "title": "Volatility Forecasting and Return Prediction under Market Regimes: Evidence from High-Frequency Chinese Equity Data",
    "url": "https://arxiv.org/abs/2606.09478",
    "source": "Xinyue Fang, Robert \\'Slepaczuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09478v1 Announce Type: new Abstract: This study investigates whether regime-dependent volatility forecasting and machine-learning-based return prediction can be jointly integrated to improv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09564",
    "domain": "金融",
    "title": "Option prices from operational-time reaction-boundary lattices",
    "url": "https://arxiv.org/abs/2606.09564",
    "source": "Chris Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09564v1 Announce Type: new Abstract: We consider the role of a continuum operational time u and its mapping to calendar time t and how these relate to event time for option pricing problems"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09642",
    "domain": "金融",
    "title": "The Dispossessed: Large-Scale Land Acquisitions, Elite Capture, and Dissent in Africa",
    "url": "https://arxiv.org/abs/2606.09642",
    "source": "Jonathan Dries",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09642v1 Announce Type: new Abstract: Over the past two decades, millions of hectares of land in Africa have been transferred to investors, raising fears of displacement and conflict. This p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07727",
    "domain": "金融",
    "title": "Benchmarking Quantum Algorithmic Resilience for CVaR Portfolio Optimization: The Expressibility-Coherence Trade-off",
    "url": "https://arxiv.org/abs/2606.07727",
    "source": "Prashik N. Somkuwar, K. Srinivasan, G. Raghavan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.07727v1 Announce Type: cross Abstract: Quantum combinatorial optimization offers theoretical advantages for complex financial modeling, but physical implementation on Noisy Intermediate Sca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08141",
    "domain": "金融",
    "title": "A Structural Matrix Autoregressive Model for the Joint Dynamics of Volume, Volatility, and Returns",
    "url": "https://arxiv.org/abs/2606.08141",
    "source": "Andrea Bucci, Giulio Palomba, Eduardo Rossi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08141v1 Announce Type: cross Abstract: This paper proposes a Structural Matrix Autoregressive (SMAR) model for the joint analysis of asset returns, realized volatility, and trading volume i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08285",
    "domain": "金融",
    "title": "Beyond Agent Architecture: Execution Assumptions and Reproducibility in LLM-Based Trading Systems",
    "url": "https://arxiv.org/abs/2606.08285",
    "source": "Junyi Yao, Zihao Zheng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08285v1 Announce Type: cross Abstract: Large language models (LLMs) and agentic systems are increasingly proposed for financial trading, yet their reported performance remains difficult to "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08379",
    "domain": "金融",
    "title": "TT-DAC-PS: Twin-Target Deterministic Actor-Critic with Policy Smoothing for Optimal Trade Execution",
    "url": "https://arxiv.org/abs/2606.08379",
    "source": "Ilia Zaznov, Atta Badii, Julian Kunkel, Alfonso Dufour",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08379v1 Announce Type: cross Abstract: This study addresses the optimal execution of large stock sell programs by introducing TT-DAC-PS (Twin-Target Deterministic Actor-Critic with Policy S"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08791",
    "domain": "金融",
    "title": "Evaluating AI Investment Strategies",
    "url": "https://arxiv.org/abs/2606.08791",
    "source": "Irene Aldridge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08791v1 Announce Type: cross Abstract: We study the problem of auditing a black-box algorithmic decision-maker from observable inputs and outputs alone. Our main result is an exact decompos"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08998",
    "domain": "金融",
    "title": "The Token Not Taken: Sampling, State, and the Variability of AI Agent Outputs",
    "url": "https://arxiv.org/abs/2606.08998",
    "source": "Muhammad Zia Hydari, Raja Iqbal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.08998v1 Announce Type: cross Abstract: Agentic AI systems can behave differently across runs: the same request may produce a different plan, a different tool call, a different code edit, or"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09104",
    "domain": "金融",
    "title": "Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio Optimization via Bayesian VAR and Elliptical Black-Litterman",
    "url": "https://arxiv.org/abs/2606.09104",
    "source": "Daniil Mikriukov (University of Liverpool, Xi'an Jiaotong-Liverpool University), Ruoyu Sun (Xi'an Jiaotong-Liverpool University), Angelos Stefanidis (Xi'an Jiaotong-Liverpool University), Jionglong Su (Xi'an Jiaotong-Liverpool University), Zhengyong Jiang (Xi'an Jiaotong-Liverpool University)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09104v1 Announce Type: cross Abstract: Deep reinforcement learning (DRL) frameworks for portfolio optimization have shown promise for their ability to learn allocation rules dynamically fro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09420",
    "domain": "金融",
    "title": "Benchmarking Deep Time Series Models for Equity Portfolios",
    "url": "https://arxiv.org/abs/2606.09420",
    "source": "Aoxin Zhang, Yuhan Cheng, Kwanting Leung",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09420v1 Announce Type: cross Abstract: Benchmarking forecasting architectures for daily equity portfolios is not just a prediction exercise. It also asks which model remains usable after pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09463",
    "domain": "金融",
    "title": "The Changing Global Division of Labor in Software: Emergence and Diffusion of New Programming Skills across IT Hubs",
    "url": "https://arxiv.org/abs/2606.09463",
    "source": "Johannes Wachs, Xiangnan Feng, Simone Daniotti, Frank Neffke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09463v1 Announce Type: cross Abstract: With the rise of new industries, often new jobs emerge. Evolutionary Economic Geography and in particular Industry Life Cycle perspectives predict tha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09820",
    "domain": "金融",
    "title": "Weighted universal approximation of differentiable maps on infinite-dimensional manifolds",
    "url": "https://arxiv.org/abs/2606.09820",
    "source": "Philipp Schmocker, Josef Teichmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T04:00:00+00:00",
    "summary": "arXiv:2606.09820v1 Announce Type: cross Abstract: We generalize the universal approximation theorem for functional input neural networks (FNN) to differentiable maps by including the approximation of "
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
    "id": "hn:48401755",
    "domain": "金融",
    "title": "Fedora 43 Upgrade revealed 20 years old Outlook Security Bug",
    "url": "https://fedoramagazine.org/fedora-43-upgrade-revealed-20-years-old-outlook-security-bug/",
    "source": "thewebguyd",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-04T17:24:22+00:00",
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
    "id": "hn:48403461",
    "domain": "金融",
    "title": "Open Letter to President of Russian Federation from President of Ukraine",
    "url": "https://www.president.gov.ua/en/news/vidkritij-list-prezidentu-rosijskoyi-federaciyi-vid-preziden-104769",
    "source": "defly",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-04T19:27:18+00:00",
    "summary": ""
  }
]
```
