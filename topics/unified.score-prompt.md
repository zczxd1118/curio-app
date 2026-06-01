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
- **每个域至少 1 条头条**（4-5 条头条要分布在 ≥3 个域，避免某个域读者打开邮件看到空白）

---

## 输入（变量替换）

- 今日日期：`2026-06-01`
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
  "date": "2026-06-01",
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
    "points": 851248,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 659845,
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
    "points": 556977,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 382798,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 364517,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1GX9dYWEPw",
    "domain": "AI",
    "title": "我居然能在MC里玩到这么好玩的摸金服务器！",
    "url": "http://www.bilibili.com/video/av114108926068217",
    "source": "物骨",
    "platform": "bilibili",
    "points": 312304,
    "published_at": "2025-03-06T21:00:00+00:00",
    "summary": "视频内容均来自《LRL服务器》\n服务器游玩方式看评论区置顶\n无需正版，不卖数值，爆率嘎嘎高，不会跑路"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 305164,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1wuQEBDEN8",
    "domain": "AI",
    "title": "【2026 最新版】｜字节大佬亲授 Claude Code 全栈教程，从入门到精通全覆盖，小白 10 分钟上手，干货无废话，建议收藏！",
    "url": "http://www.bilibili.com/video/av116408209967652",
    "source": "跟着李迟学AI",
    "platform": "bilibili",
    "points": 237457,
    "published_at": "2026-04-15T10:23:31+00:00",
    "summary": "这也是2026B站最新最系统的Claude Code + 自动化工作流教学课程，小白10分钟轻松上手！\n求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 229074,
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
    "points": 220488,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中使用Claude Code agent并配置DeepSeek v4 model【闲谈】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸voov",
    "platform": "bilibili",
    "points": 190457,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "setting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, &quot;value&quot;: &quot;xxxx&"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 172856,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 159965,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 153005,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 149208,
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
    "points": 139949,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 139937,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 94180,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 91825,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 83611,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 80284,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 72787,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1KX9jB8E9M",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！比付费效果强十倍",
    "url": "http://www.bilibili.com/video/av116328887225403",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 69571,
    "published_at": "2026-04-01T10:12:34+00:00",
    "summary": "视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 62161,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "domain": "AI",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 57482,
    "published_at": "2025-06-28T02:37:22+00:00",
    "summary": "视频主题&amp;项目背景\n主题： 分享个人如何使用cursor 从0到1开发一个比较大的项目，使用的技术栈是vue+小程序+java\n项目\n一个B2B的订货商城及供应链全流程管理，包含的端有：\n小程序商城端\n供应商端\n仓储物流端\n司机配送端\n销售端\n后台管理系统\n以上小程序端都是使用webview的方式\n核心功能：\n商城的基本功能: 正逆向订单、商品、购物车、优惠券、积分、钱包、充值、工单等\n供"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 50630,
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
    "points": 50092,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1fGFsznEas",
    "domain": "AI",
    "title": "vibe coding 10分钟做一个塔罗牌游戏",
    "url": "http://www.bilibili.com/video/av116029028042969",
    "source": "鸭鸭摘花",
    "platform": "bilibili",
    "points": 44911,
    "published_at": "2026-02-07T11:20:13+00:00",
    "summary": "一个简单的教程 一行代码不写 做一个塔罗牌游戏"
  },
  {
    "id": "bvid:BV1V8Gv6XE1T",
    "domain": "AI",
    "title": "【OpenClaw保姆级教程】最新版小龙虾OpenClaw完整安装教学，一个视频搞懂OpenClaw本地部署/接入微信/飞书/钉钉（附完整操作文档）",
    "url": "http://www.bilibili.com/video/av116621699979136",
    "source": "Agent喂饭级教程",
    "platform": "bilibili",
    "points": 38059,
    "published_at": "2026-05-23T03:20:10+00:00",
    "summary": "全新版本，大家记得三连获取安装资料哦"
  },
  {
    "id": "bvid:BV1dZDQBwEJo",
    "domain": "AI",
    "title": "从夯到拉锐评Maple Story各大服务器【冒险岛】",
    "url": "http://www.bilibili.com/video/av116390593828662",
    "source": "青空白尘",
    "platform": "bilibili",
    "points": 36947,
    "published_at": "2026-04-12T11:00:00+00:00",
    "summary": "饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋饺子醋"
  },
  {
    "id": "bvid:BV13K1YBtE6e",
    "domain": "AI",
    "title": "【GMM】MCP 使用说明",
    "url": "http://www.bilibili.com/video/av115485010168640",
    "source": "3DM小莫",
    "platform": "bilibili",
    "points": 35478,
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
    "points": 33121,
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
    "points": 29469,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 28649,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1e7VA6vEJU",
    "domain": "AI",
    "title": "【2026最新】绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116640356304890",
    "source": "码士集团-马小安",
    "platform": "bilibili",
    "points": 25673,
    "published_at": "2026-05-26T10:22:46+00:00",
    "summary": "绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！\n配套课件笔记/PPT已备好，另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~"
  },
  {
    "id": "bvid:BV116P7zXEkE",
    "domain": "AI",
    "title": "纯小白教学：用vibecoding做个人网站",
    "url": "http://www.bilibili.com/video/av116160209093711",
    "source": "阿囤囤-庞滚滚",
    "platform": "bilibili",
    "points": 24101,
    "published_at": "2026-03-02T15:11:36+00:00",
    "summary": "不需要🪜哦～"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 21973,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1v8mtBpEwK",
    "domain": "AI",
    "title": "Kiro 上手必看：从Vibe 到 Spec 全攻略！",
    "url": "http://www.bilibili.com/video/av115695564102585",
    "source": "AI编程瓜哥",
    "platform": "bilibili",
    "points": 20460,
    "published_at": "2025-12-10T13:49:11+00:00",
    "summary": "一眼懂，Vibe coding 和Spec Coding，双模式实战。"
  },
  {
    "id": "bvid:BV15RPpzSEJM",
    "domain": "AI",
    "title": "斯坦福大学:Vibe Coding(AI编程最新课程)",
    "url": "http://www.bilibili.com/video/av116180459389189",
    "source": "世界课程精选站",
    "platform": "bilibili",
    "points": 19863,
    "published_at": "2026-03-06T05:00:15+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 17632,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1W9cZzxEYs",
    "domain": "AI",
    "title": "AI 当助手！Claude 深度协助 UE5 游戏开发全流程",
    "url": "http://www.bilibili.com/video/av116209752277031",
    "source": "叁昧火游戏",
    "platform": "bilibili",
    "points": 14497,
    "published_at": "2026-03-11T12:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV19eQ3BJEkg",
    "domain": "AI",
    "title": "手撕大厂题-vibe coding降龙七步",
    "url": "http://www.bilibili.com/video/av116403881385303",
    "source": "青阳-AI",
    "platform": "bilibili",
    "points": 13726,
    "published_at": "2026-04-14T16:00:12+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 13437,
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
    "points": 13431,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1ZHAozLE7b",
    "domain": "AI",
    "title": "【SynthPilot】全网首发！2026年最新基于AI的FPGA开发教程，Agent自主编程/调试全链路闭环，500+工具接入Vivado",
    "url": "http://www.bilibili.com/video/av116164755790661",
    "source": "晓川科研站",
    "platform": "bilibili",
    "points": 12725,
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
    "points": 12583,
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
    "points": 12169,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1NYVG6jEKE",
    "domain": "AI",
    "title": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通",
    "url": "http://www.bilibili.com/video/av116662133132089",
    "source": "字节软件测试",
    "platform": "bilibili",
    "points": 11767,
    "published_at": "2026-05-30T06:39:27+00:00",
    "summary": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通"
  },
  {
    "id": "bvid:BV1yT8qzMEbd",
    "domain": "AI",
    "title": "基于SpringAI开发Java版mcp服务",
    "url": "http://www.bilibili.com/video/av114942720148945",
    "source": "程序员Cafe",
    "platform": "bilibili",
    "points": 11048,
    "published_at": "2025-07-30T15:05:27+00:00",
    "summary": "如何用Java开发一个mcp服务？如何把已有的spingboot微服务改造成mcp服务呢？如何在mcp客户端调用mcp服务？\n今天来一个保姆级教学"
  },
  {
    "id": "bvid:BV1jsV861EVM",
    "domain": "AI",
    "title": "【2026胎教级】Claude Code全栈教程，从入门到精通，搞定所有开发场景，小白10分钟搞定，全程干货无废话，存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116657502687649",
    "source": "程序员黑梦",
    "platform": "bilibili",
    "points": 10863,
    "published_at": "2026-05-29T11:08:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48212493",
    "domain": "AI 商业 / 投融资",
    "title": "An OpenAI model has disproved a central conjecture in discrete geometry",
    "url": "https://openai.com/index/model-disproves-discrete-geometry-conjecture/",
    "source": "tedsanders",
    "platform": "hackernews",
    "points": 1429,
    "published_at": "2026-05-20T19:05:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48182754",
    "domain": "AI 商业 / 投融资",
    "title": "Elon Musk has lost his lawsuit against Sam Altman and OpenAI",
    "url": "https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/",
    "source": "nycdatasci",
    "platform": "hackernews",
    "points": 1096,
    "published_at": "2026-05-18T17:38:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48198291",
    "domain": "AI 商业 / 投融资",
    "title": "OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool",
    "url": "https://openai.com/index/advancing-content-provenance/",
    "source": "smooke",
    "platform": "hackernews",
    "points": 332,
    "published_at": "2026-05-19T19:34:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210226",
    "domain": "AI 商业 / 投融资",
    "title": "OpenAI Is Preparing to File for an IPO Soon",
    "url": "https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 205,
    "published_at": "2026-05-20T16:24:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48012162",
    "domain": "AI 商业 / 投融资",
    "title": "Securing a DoD contractor: Finding a multi-tenant authorization vulnerability",
    "url": "https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup",
    "source": "bearsyankees",
    "platform": "hackernews",
    "points": 221,
    "published_at": "2026-05-04T17:46:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:48217052",
    "domain": "AI 商业 / 投融资",
    "title": "OpenAI to confidentially file for IPO as soon as Friday",
    "url": "https://www.cnbc.com/2026/05/20/openai-ipo-filing.html",
    "source": "doppp",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-05-21T02:24:35+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theinformation.com/articles/microsofts-ai-independence-day",
    "domain": "AI 商业 / 投融资",
    "title": "Microsoft’s AI Independence Day",
    "url": "https://www.theinformation.com/articles/microsofts-ai-independence-day",
    "source": "Qianer Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T21:56:26+00:00",
    "summary": "Two months after Microsoft’s conscious uncoupling from OpenAI, Microsoft wants to prove it’s thriving as an AI provider that doesn’t have to rely on the ChatGPT maker’s technology.&nbsp;Microsoft’s an"
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/anthropic-cuts-list-firms-unauthorized-trading-shares",
    "domain": "AI 商业 / 投融资",
    "title": "Anthropic Cuts List of Firms Unauthorized for Trading in Its Shares",
    "url": "https://www.theinformation.com/briefings/anthropic-cuts-list-firms-unauthorized-trading-shares",
    "source": "Jason Dean",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T20:49:25+00:00",
    "summary": "Anthropic reduced the list of secondary markets it says aren’t authorized to buy or sell its shares, scaling back guidance that had prompted confusion. The company revised guidance on its website abou"
  },
  {
    "id": "rss:https://www.theinformation.com/articles/forward-deployed-engineers-rage",
    "domain": "AI 商业 / 投融资",
    "title": "Why Forward Deployed Engineers Are the Rage",
    "url": "https://www.theinformation.com/articles/forward-deployed-engineers-rage",
    "source": "Kevin McLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T15:00:53+00:00",
    "summary": "AI researchers may have the hottest job in tech, but forward-deployed engineers who put the AI to good use are becoming indispensable too. The military-inspired job title, which Palantir began using i"
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/softbank-invest-75-billion-euros-ai-data-centers-france",
    "domain": "AI 商业 / 投融资",
    "title": "Softbank to Invest Up To 75 Billion Euros on AI Data Centers in France",
    "url": "https://www.theinformation.com/briefings/softbank-invest-75-billion-euros-ai-data-centers-france",
    "source": "Jason Dean",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T21:13:10+00:00",
    "summary": "SoftBank Group announced a commitment to develop and operate five gigawatts of AI data center capacity in France, with an investment of up to 75 billion euros, or about $87.5 billion. The commitment i"
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/spacex-awarded-4-billion-contract-u-s-space-force",
    "domain": "AI 商业 / 投融资",
    "title": "SpaceX Is Awarded $4 billion Contract with U.S. Space Force",
    "url": "https://www.theinformation.com/briefings/spacex-awarded-4-billion-contract-u-s-space-force",
    "source": "Jason Dean",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T19:52:16+00:00",
    "summary": "The U.S. Space Force awarded a $4.16 billion contract to SpaceX as part of a program to deploy space-based sensors to track and target airborne threats. The deal for the Space-Based Airborne Moving Ta"
  },
  {
    "id": "rss:https://www.theinformation.com/articles/defense-tech-grows",
    "domain": "AI 商业 / 投融资",
    "title": "Defense Tech Grows Up",
    "url": "https://www.theinformation.com/articles/defense-tech-grows",
    "source": "Leo Schwartz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T16:01:06+00:00",
    "summary": "Welcome, Weekenders! In this newsletter:• The Big Read:&nbsp;Can OpenAI’s revenue chief&nbsp;catch Anthropic in enterprise tech?•&nbsp;Plus, Recommendations—our weekly pop culture picks: “Deep Cover: "
  },
  {
    "id": "rss:https://www.theinformation.com/articles/openais-revenue-chief-barnstorms-business-customers",
    "domain": "AI 商业 / 投融资",
    "title": "OpenAI’s Revenue Chief Barnstorms for Business Customers",
    "url": "https://www.theinformation.com/articles/openais-revenue-chief-barnstorms-business-customers",
    "source": "Laura Bratton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T13:00:38+00:00",
    "summary": "Before former Slack CEO Denise Dresser joined OpenAI in December as its chief revenue officer, the company’s efforts to sell its products to business customers were sometimes clunky. Earlier in 2025, "
  },
  {
    "id": "wscn:3773548",
    "domain": "AI 商业 / 投融资",
    "title": "黄仁勋：Vera Rubin全面量产，AI Agent是重点方向，挑战英特尔剑指下一代AI PC入口",
    "url": "https://wallstreetcn.com/articles/3773548",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:38:35+00:00",
    "summary": "黄仁勋表示，英伟达将推出面向AI智能体的CPU Vera和全新AI模型Nemotron 3 Ultra。此外英伟达公布面向WINDOWS系统个人电脑的新款处理器，挑战英特尔，剑指下一代AI PC入口。"
  },
  {
    "id": "wscn:3773547",
    "domain": "AI 商业 / 投融资",
    "title": "SpaceX领衔，4万亿美元IPO冲击，市场能消化吗？高盛：没问题，美银：泡沫已逼近历史极值",
    "url": "https://wallstreetcn.com/articles/3773547",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:29:43+00:00",
    "summary": "美银首席策略师Hartnett警告，SpaceX、OpenAI、Anthropic逾4万亿美元市值集中上市，将抽干市场流动性，AI板块集中度已逼近1880年代铁路泡沫极值；高盛则以1.3万亿美元企业回购与指数强制建仓需求反驳，认为市场足以消化。"
  },
  {
    "id": "wscn:3773543",
    "domain": "AI 商业 / 投融资",
    "title": "A股三大股指集体下跌，煤炭掀涨停潮，AI PC、AI应用活跃，算力硬件齐跌，恒科指涨超1%，科网股普涨",
    "url": "https://wallstreetcn.com/articles/3773543",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:04:55+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3800股飘红，上午半天成交1.97万亿。沪深两市半日成交额1.96万亿，较上个交易日缩量1617亿。板块方面，半导体、算力硬件产业链调整，CPO、PCB、GPU方向领跌；稀土、创新药、白酒、金融跌幅靠前。煤炭、油气、电力、文化传媒走强，AI应用、电商、网络安全题材活跃。"
  },
  {
    "id": "wscn:3773546",
    "domain": "AI 商业 / 投融资",
    "title": "高盛上调铜目标价！美国“囤货潮”加剧全球供应紧张",
    "url": "https://wallstreetcn.com/articles/3773546",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:41:45+00:00",
    "summary": "高盛大幅上调LME铜价预测，2026年底目标价升至13735美元/吨，2027年均价升至13800美元。核心驱动来自两端：美国上半年铜进口超预期，预计全年库存累积达90万吨，“美国以外”铜市场缺口或达64万吨；同时Grasberg和Kamoa-Kakula两大铜矿复产推迟至2028年。"
  },
  {
    "id": "wscn:3773538",
    "domain": "AI 商业 / 投融资",
    "title": "从流量狂欢到利润为王：化妆品行业的五年之痛与复苏信号",
    "url": "https://wallstreetcn.com/premium/articles/3773538?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:41:20+00:00",
    "summary": "行业困境反转的曙光出现了吗？"
  },
  {
    "id": "wscn:3773537",
    "domain": "AI 商业 / 投融资",
    "title": "AI热情主导市场，日韩股市齐创新高，韩股一度触发熔断，三星电子大涨10%",
    "url": "https://wallstreetcn.com/articles/3773537",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:31:18+00:00",
    "summary": "日经225首破67000点，三星电子单日暴涨10%创历史新高，软银市值盘中超越丰田，台股同步刷新纪录高位。韩国年内涨幅跻身全球前列，Nasdaq 100期货亦同步上扬。然而油价反弹、美伊谈判僵局暗藏变数，狂欢之下风险犹存。"
  },
  {
    "id": "wscn:3773541",
    "domain": "AI 商业 / 投融资",
    "title": "30年美债收益率再破5%，“一切都廉价”的时代落幕了",
    "url": "https://wallstreetcn.com/articles/3773541",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:05:58+00:00",
    "summary": "30年期美债收益率再度突破5%，这一次市场的反应与2023年明显不同——投资者开始真正接受高利率将长期持续的现实。分析指出，这背后是一个更深层的结构性转变：支撑美国过去50年低通胀、低利率的三大支柱——廉价资本、廉价劳动力、廉价能源——正在同步瓦解。而AI的走向，将是决定未来通胀走势的最大未知数。"
  },
  {
    "id": "wscn:3773542",
    "domain": "AI 商业 / 投融资",
    "title": "美债交易员押注美联储加息，五月非农将成关键检验",
    "url": "https://wallstreetcn.com/articles/3773542",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T02:51:43+00:00",
    "summary": "五月非农就业报告本周五即将揭晓，预计新增9万人，若数据强劲叠加PCE同比高达3.8%，市场或将为更激进加息路径定价。十年期美债收益率徘徊4.44%，机构分歧加剧，短端债券成避险首选。"
  },
  {
    "id": "wscn:3773544",
    "domain": "AI 商业 / 投融资",
    "title": "OpenAI正式成立机器人团队，进军实体世界AI",
    "url": "https://wallstreetcn.com/articles/3773544",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T02:43:32+00:00",
    "summary": "OpenAI联合创始人Greg Brockman宣布成立“OpenAI Robotics”团队并公开招聘，Sam Altman同日将机器人列为公司核心战略优先级，近期目标锁定建筑和基础设施领域的技工辅助，长期设定是“人人拥有个人机器人”。但公司目前没有公布任何具体产品、合作伙伴或时间表。"
  },
  {
    "id": "wscn:3772999",
    "domain": "AI 商业 / 投融资",
    "title": "日落之后：英国的生死大考【付鹏说 深度文章】",
    "url": "https://wallstreetcn.com/premium/articles/3772999?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T02:31:41+00:00",
    "summary": "英国正站在系统性危机的临界点上"
  },
  {
    "id": "wscn:3773539",
    "domain": "AI 商业 / 投融资",
    "title": "史上最大IPO SpaceX：强行改写指数规则，散户或成定价关键",
    "url": "https://wallstreetcn.com/articles/3773539",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T02:24:06+00:00",
    "summary": "SpaceX计划以至少1.8万亿美元估值、750亿美元募资规模冲击IPO史上最大上市，其体量之巨已迫使纳斯达克等主要指数机构紧急修改纳入规则，大幅缩减加入指数的等待期。被动资金自动买入需求或达200亿美元，30%份额拟向散户开放。这场史无前例的资本盛宴，将重塑华尔街规则，并决定OpenAI等AI独角兽的上市命运。"
  },
  {
    "id": "wscn:3773540",
    "domain": "AI 商业 / 投融资",
    "title": "中国5月RatingDog制造业PMI 51.8，连续第六个月扩张，通胀压力出现缓解",
    "url": "https://wallstreetcn.com/articles/3773540",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T01:45:20+00:00",
    "summary": "核心亮点是投入与产出品价格涨幅双双回落，企业通胀及成本压力出现边际缓解。此外，因交货期延长企业增加库存；就业微降，但市场前景仍偏乐观。"
  },
  {
    "id": "wscn:3773531",
    "domain": "AI 商业 / 投融资",
    "title": "戴尔暴涨，大摩“认错”：对硬件周期过于保守了",
    "url": "https://wallstreetcn.com/articles/3773531",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T01:40:58+00:00",
    "summary": "摩根士丹利高调认错，将对戴尔的减持评级与170美元目标价打入审查，目前股价已涨至420美元。AI需求从GPU蔓延至传统基础设施，且这一趋势仍处于早期阶段，“传统PC大厂”的低估值框架或将彻底重写。"
  },
  {
    "id": "wscn:3773536",
    "domain": "AI 商业 / 投融资",
    "title": "科技背后的买卖盘",
    "url": "https://wallstreetcn.com/articles/3773536",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T01:37:47+00:00",
    "summary": "科技板块资金暗战激烈：主动基金大举增持光纤、押注通信，散户却反向涌入电子、存储，与机构形成千亿级筹码对倒；险资悄然清仓光纤，北上资金同步加码，多空分歧罕见撕裂。两融杠杆向存储、光模块集中，科技龙头IPO历史上屡屡抽血同板块——多空力量交织之下，这场流动性博弈远比表面更复杂。"
  },
  {
    "id": "wscn:3773532",
    "domain": "AI 商业 / 投融资",
    "title": "AI PC海啸引爆周末：英伟达亲自下场！大厂预计重塑万亿PC产业生态！",
    "url": "https://wallstreetcn.com/premium/articles/3773532?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T01:36:58+00:00",
    "summary": "ComputeX 2026大会将成为人类PC产业发展史上的一个分水岭时刻。记住这个时刻。"
  },
  {
    "id": "wscn:3773535",
    "domain": "AI 商业 / 投融资",
    "title": "油价跌了黄金也没涨，市场开始担心一个新问题",
    "url": "https://wallstreetcn.com/articles/3773535",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T01:06:47+00:00",
    "summary": "德银认为，黄金正面临一个新问题：通胀来源更广泛、更顽固，叠加全球央行加息预期升温、实际利率上升，令金价持续承压，且与油价走势明显背离。全球债市同步抛售、ETF需求同比萎缩78%是当前最大压力来源。市场目前最关注的变量，是新美联储主席沃什能否在6月议息会议上软化鹰派立场。"
  },
  {
    "id": "wscn:3773533",
    "domain": "AI 商业 / 投融资",
    "title": "高盛也支持“存储PE估值”，上调海力士、三星和铠侠“三巨头”目标价",
    "url": "https://wallstreetcn.com/articles/3773533",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T01:02:06+00:00",
    "summary": "高盛认为，AI驱动需求持续性、供给受限及长期供货协议（LTA）三大结构性变化，正推动存储行业向AI基础设施赛道转型。预计供需短缺将延续至2028年。此前大摩和小摩就指出，存储巨头正站在估值范式切换的历史节点上，盈利可预测性比肩台积电，当前7.3倍远期P/E存在历史性修复空间。"
  },
  {
    "id": "wscn:3773504",
    "domain": "AI 商业 / 投融资",
    "title": "国内债市或延续上涨，货币政策保持流动性充裕---W22国内宏观脱水",
    "url": "https://wallstreetcn.com/premium/articles/3773504?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T01:00:45+00:00",
    "summary": "国内债市上涨行情或有望延续，尽管经济呈现先强后弱，但基本面仍对债市形成托底，流动性有望持续充裕，更多..."
  },
  {
    "id": "wscn:3773526",
    "domain": "AI 商业 / 投融资",
    "title": "百亿基金集体“创新高”：一场必要的估值修复",
    "url": "https://wallstreetcn.com/articles/3773526",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T00:35:52+00:00",
    "summary": "如何客观看待主动权益基金的时刻临近"
  },
  {
    "id": "hn:48111143",
    "domain": "AI 商业 / 投融资",
    "title": "Show HN: Agentic interface for mainframes and COBOL",
    "url": "https://www.hypercubic.ai/hopper",
    "source": "sai18",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-05-12T17:10:22+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://stratechery.com/2026/luceing-their-mind/",
    "domain": "AI 商业 / 投融资",
    "title": "2026.22: Luceing Their Mind",
    "url": "https://stratechery.com/2026/luceing-their-mind/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of May 25, 2026, including why everyone hates Luce, how to monetize AI answers, and social mobility in China."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/",
    "domain": "AI 商业 / 投融资",
    "title": "An Interview with Eric Seufert About Models and Ads, and AI’s Upside for Humanity",
    "url": "https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T10:00:00+00:00",
    "summary": "An Interview with Eric Seufert about building models for generative AI, why Meta's foundational models are so important, and why understanding advertising leads to optimism about humanity's future."
  },
  {
    "id": "rss:https://www.netinterest.co/p/strategy-follows-structure",
    "domain": "AI 商业 / 投融资",
    "title": "Strategy Follows Structure",
    "url": "https://www.netinterest.co/p/strategy-follows-structure",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T16:47:05+00:00",
    "summary": "Fidelity, Capital, Vanguard and the Ownership Structures That Made Them"
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/meta-plans-ai-pendant-part-ambitious-wearables-expansion",
    "domain": "AI 商业 / 投融资",
    "title": "Meta Plans an AI Pendant as Part of Ambitious Wearables Expansion",
    "url": "https://www.theinformation.com/briefings/meta-plans-ai-pendant-part-ambitious-wearables-expansion",
    "source": "Jyoti Mann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T23:54:23+00:00",
    "summary": "Meta Platforms&nbsp;plans&nbsp;to start testing an AI pendant in the next year as part of an ambitious roadmap for wearable devices aimed at reversing the huge losses in its hardware division. An inte"
  },
  {
    "id": "rss:https://www.theinformation.com/articles/meta-memo-outlines-ambitious-hardware-plans-including-new-ai-pendant",
    "domain": "AI 商业 / 投融资",
    "title": "Meta Memo Outlines Ambitious Hardware Plans, Including New AI Pendant",
    "url": "https://www.theinformation.com/articles/meta-memo-outlines-ambitious-hardware-plans-including-new-ai-pendant",
    "source": "Jyoti Mann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T23:38:22+00:00",
    "summary": "Meta Platforms&nbsp;plans to start testing an AI pendant in the next year as part of an ambitious roadmap for wearable devices aimed at reversing the huge losses in its hardware division. An internal "
  },
  {
    "id": "rss:https://www.theinformation.com/articles/spacex-celebrating-blue-origin-explosion",
    "domain": "AI 商业 / 投融资",
    "title": "Why SpaceX Isn’t Celebrating the Blue Origin Explosion",
    "url": "https://www.theinformation.com/articles/spacex-celebrating-blue-origin-explosion",
    "source": "Theo Wayt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T22:31:35+00:00",
    "summary": "By now, you’ve probably seen the unbelievable video of Blue Origin’s New Glenn rocket exploding on its launchpad in Florida on Thursday night. On its face, Blue Origin’s pain would seem to be Elon Mus"
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/kalshi-coinbase-approved-offer-crypto-perpetuals-u-s",
    "domain": "AI 商业 / 投融资",
    "title": "Kalshi, Coinbase Approved to Offer Crypto Perpetuals in U.S.",
    "url": "https://www.theinformation.com/briefings/kalshi-coinbase-approved-offer-crypto-perpetuals-u-s",
    "source": "Yueqi Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T17:58:20+00:00",
    "summary": "Prediction market Kalshi won approval from U.S. regulators to offer crypto trading through bitcoin perpetuals, a type of highly-leveraged derivatives product, confirming an April report by The Informa"
  },
  {
    "id": "rss:https://www.theinformation.com/articles/chinas-bytedance-developing-new-ai-chips-like-nvidia-partner-groq",
    "domain": "AI 商业 / 投融资",
    "title": "China’s ByteDance Developing New AI Chips Like Those from Nvidia Partner Groq",
    "url": "https://www.theinformation.com/articles/chinas-bytedance-developing-new-ai-chips-like-nvidia-partner-groq",
    "source": "Juro Osawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T13:00:35+00:00",
    "summary": "TikTok owner ByteDance is developing a new chip to run artificial intelligence models as part of an aggressive expansion of its homegrown AI infrastructure. The new AI chip is intended to have a struc"
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/blue-origin-new-glenn-rocket-explodes-test",
    "domain": "AI 商业 / 投融资",
    "title": "Blue Origin New Glenn Rocket Explodes During Test",
    "url": "https://www.theinformation.com/briefings/blue-origin-new-glenn-rocket-explodes-test",
    "source": "Nick Wingfield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T02:20:30+00:00",
    "summary": "Jeff Bezos’ space company Blue Origin suffered a serious setback Thursday evening when its New Glenn rocket exploded on a launch pad in Florida during a test. Video clips of the incident show a giant "
  },
  {
    "id": "rss:https://www.theinformation.com/articles/base-power-talks-raise-funds-12-billion-valuation",
    "domain": "AI 商业 / 投融资",
    "title": "Base Power in Talks to Raise Funds at $12 Billion Valuation",
    "url": "https://www.theinformation.com/articles/base-power-talks-raise-funds-12-billion-valuation",
    "source": "Julia Hornstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T01:39:36+00:00",
    "summary": "Base Power, a three-year-old home-battery startup, is in talks to raise funds at a $12 billion valuation, according to a person with knowledge of the discussions. Ribbit Capital, which backed Base Pow"
  },
  {
    "id": "rss:https://www.theinformation.com/articles/boomers-beware-spacex-stock",
    "domain": "AI 商业 / 投融资",
    "title": "Boomers, Beware of SpaceX Stock",
    "url": "https://www.theinformation.com/articles/boomers-beware-spacex-stock",
    "source": "Anita Ramaswamy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T23:59:34+00:00",
    "summary": "Greetings! Anita here. It’s been a relatively slow week for SpaceX news, but that will soon change. Musk’s rocketship company is expected to launch its investor roadshow next week ahead of a mid-June "
  },
  {
    "id": "rss:https://www.theinformation.com/articles/big-laws-ai-threat-harvey-legora",
    "domain": "AI 商业 / 投融资",
    "title": "Big Law’s AI Threat to Harvey, Legora",
    "url": "https://www.theinformation.com/articles/big-laws-ai-threat-harvey-legora",
    "source": "Julia Hornstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T23:47:01+00:00",
    "summary": "Despite fears that advanced tools from Anthropic and OpenAI would soon make legal apps like Harvey and Legora irrelevant, recent revenue milestones at those startups suggest they are doing just fine. "
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/dell-shares-soar-nearly-40-surge-ai-server-sales",
    "domain": "AI 商业 / 投融资",
    "title": "Dell Shares Rise Nearly 40% After Surge in AI Server Sales",
    "url": "https://www.theinformation.com/briefings/dell-shares-soar-nearly-40-surge-ai-server-sales",
    "source": "Kevin McLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T23:08:07+00:00",
    "summary": "Customer demand for AI is pouring jet fuel on Dell’s server, storage and networking businesses, as its overall revenue grew 88% to $43.8 billion during its April quarter compared to last year, beating"
  },
  {
    "id": "rss:https://www.theinformation.com/articles/lowes-says-semantic-data-boosting-ai-agents",
    "domain": "AI 商业 / 投融资",
    "title": "Lowe’s Says ‘Semantic’ Data is Boosting Its AI Agents",
    "url": "https://www.theinformation.com/articles/lowes-says-semantic-data-boosting-ai-agents",
    "source": "Kevin McLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T20:09:41+00:00",
    "summary": "Microsoft, Databricks, SAP and other AI software providers are fighting over control and access to enterprise data known as the semantic layer, as we reported last week.&nbsp;Semantic layers are essen"
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/illinois-legislature-passes-landmark-ai-safety-bill",
    "domain": "AI 商业 / 投融资",
    "title": "Illinois Legislature Passes Landmark AI Safety Bill",
    "url": "https://www.theinformation.com/briefings/illinois-legislature-passes-landmark-ai-safety-bill",
    "source": "Leo Schwartz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T19:22:32+00:00",
    "summary": "On Wednesday, the Illinois House of Representatives passed a bill that will require major AI companies to submit their model safety plans for third-party audits, as well as creating whistleblower prot"
  },
  {
    "id": "rss:https://www.theinformation.com/briefings/anthropic-releases-new-flagship-ai-model",
    "domain": "AI 商业 / 投融资",
    "title": "Anthropic Releases New Flagship AI Model",
    "url": "https://www.theinformation.com/briefings/anthropic-releases-new-flagship-ai-model",
    "source": "Stephanie Palazzolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T19:11:41+00:00",
    "summary": "Anthropic on Thursday announced its new flagship AI model, Claude Opus 4.8, which showed improvements in standardized AI performance evaluations in coding, financial analysis and other fields. The com"
  },
  {
    "id": "rss:https://stratechery.com/2026/the-spacex-ipo-and-data-centers-in-space/",
    "domain": "AI 商业 / 投融资",
    "title": "The SpaceX IPO and Data Centers in Space",
    "url": "https://stratechery.com/2026/the-spacex-ipo-and-data-centers-in-space/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T10:00:00+00:00",
    "summary": "There isn't a financial model that justifies the SpaceX IPO, but data centers in space are plausible, and that might be enough."
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
    "id": "hn:48343372",
    "domain": "AI 算力 / 半导体",
    "title": "Dell Confirms XPS Laptop with Nvidia N1X at Computex",
    "url": "https://videocardz.com/newz/dell-confirms-xps-laptop-with-nvidia-n1x-at-computex",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-05-31T05:58:07+00:00",
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
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-xeon-6-clearwater-forest-puts-18a-in-the-data-center-with-up-to-288-cores-576-mb-of-l3-cache-new-xeon-6990e-is-30-percent-faster-per-thread-than-192-core-amd-epyc-9965-says-intel",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Xeon 6+ ‘Clearwater Forest’ puts 18A in the data center with up to 288 cores, 576 MB of L3 cache — new Xeon 6990E+ is 30% faster per thread than 192-core AMD Epyc 9965, says Intel",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-xeon-6-clearwater-forest-puts-18a-in-the-data-center-with-up-to-288-cores-576-mb-of-l3-cache-new-xeon-6990e-is-30-percent-faster-per-thread-than-192-core-amd-epyc-9965-says-intel",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel is putting its 18A node into the data center with new Xeon 6+ Clearwater Forest CPUs, which pack up to 288 E-cores for dense compute."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-cpus-officially-launching-in-2027-on-intel-18a-p-next-gen-p-core-xeon-features-pcie-6-0-50-percent-higher-core-counts-and-twice-the-memory-bandwidth",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Xeon 7 ‘Diamond Rapids’ CPUs officially launching in 2027 on Intel 18A-P — next-gen P-core Xeon features PCIe 6.0, 50% higher core counts, and twice the memory bandwidth",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-cpus-officially-launching-in-2027-on-intel-18a-p-next-gen-p-core-xeon-features-pcie-6-0-50-percent-higher-core-counts-and-twice-the-memory-bandwidth",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel has officially confirmed its next-gen Xeon 7 Diamond Rapids CPUs are coming in 2027, featuring 50% higher core counts and twice the memory bandwidth of Xeon 6 in a bid to compete against AMD’s u"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/intel-details-long-awaited-crescent-island-ai-gpu-at-computex-boasts-up-to-480-gb-of-lpddr5x-to-combat-memory-shortages-company-shares-more-details-of-its-xe3p-inference-accelerator-at-computex",
    "domain": "AI 算力 / 半导体",
    "title": "Intel details long-awaited Crescent Island AI GPU at Computex, boasts up to 480 GB of LPDDR5X to combat memory shortages — company shares more details of its Xe3P inference accelerator at Computex",
    "url": "https://www.tomshardware.com/pc-components/gpus/intel-details-long-awaited-crescent-island-ai-gpu-at-computex-boasts-up-to-480-gb-of-lpddr5x-to-combat-memory-shortages-company-shares-more-details-of-its-xe3p-inference-accelerator-at-computex",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel revealed more details of its next-gen Data Center GPU, code-named Crescent Island, at Computex 2026. This inference-optimized chip will feature up to 480GB of LPDDR5X memory for efficient handli"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-formerly-china-exclusive-radeon-rx-9070-gre-goes-global-for-usd549-on-june-2-rdna-4-gpu-will-bridge-the-gap-between-rx-9060-xt-and-rx-9070",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s formerly China-exclusive Radeon RX 9070 GRE goes global for $549 on June 2 — RDNA 4 GPU will bridge the gap between RX 9060 XT and RX 9070",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-formerly-china-exclusive-radeon-rx-9070-gre-goes-global-for-usd549-on-june-2-rdna-4-gpu-will-bridge-the-gap-between-rx-9060-xt-and-rx-9070",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T02:00:21+00:00",
    "summary": "AMD has officially launched the Radeon RX 9070 GRE for $549, an RDNA 4 graphics card that was previously exclusive to the Chinese market."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-keynote-computex-2026-gtc-taipei-where-to-watch",
    "domain": "AI 算力 / 半导体",
    "title": "Watch Nvidia's Computex 2026 keynote here — Jensen Huang takes the stage for Computex and GTC Taipei at 8pm PT / 11pm ET on May 31",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-keynote-computex-2026-gtc-taipei-where-to-watch",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T00:21:39+00:00",
    "summary": "Nvidia CEO Jensen Huang is set to take the stage at Computex 2026 and GTC Taipei. Here's how to watch the keynote address, where we could hear more about the rumored N1X."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least",
    "domain": "AI 算力 / 半导体",
    "title": "AMD confirms AM5 support through 2029 — Zen 4 and 5 platform will likely see two more generations, at least",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T00:00:00+00:00",
    "summary": "AMD confirmed it will support its current AM5 socket through 2029, extending the timeline by two years and likely lining up at least two more generations on the socket."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-brings-back-ryzen-7-5800x3d-launches-ryzen-7-7700x3d-to-combat-rising-component-prices-eight-core-x3d-cpus-arrive-under-usd350-for-am4-or-am5-ddr4-or-ddr5",
    "domain": "AI 算力 / 半导体",
    "title": "AMD brings back Ryzen 7 5800X3D, launches Ryzen 7 7700X3D to combat rising component prices — eight-core X3D CPUs arrive under $350 for AM4 or AM5, DDR4 or DDR5",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-brings-back-ryzen-7-5800x3d-launches-ryzen-7-7700x3d-to-combat-rising-component-prices-eight-core-x3d-cpus-arrive-under-usd350-for-am4-or-am5-ddr4-or-ddr5",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T00:00:00+00:00",
    "summary": "AMD is rereleasing the Ryzen 7 5800X3D and introducing the Ryzen 7 7700X3D, both eight-core chips with 3DV-Cache targeting midrange gamers who’ve been under the thumb of rising component prices."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienware-debuts-39-34-inch-oled-gaming-monitors-rgb-stripe-tandem-and-penta-tandem-tech-should-boost-color-performance-and-text-clarity",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware debuts 39, 34-inch OLED gaming monitors — RGB Stripe Tandem and Penta Tandem tech should boost color performance and text clarity",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienware-debuts-39-34-inch-oled-gaming-monitors-rgb-stripe-tandem-and-penta-tandem-tech-should-boost-color-performance-and-text-clarity",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T23:00:00+00:00",
    "summary": "Alienware hits the ground running at Computex with four new gaming monitors covering OLED and VA panel types."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dell-xps-13-targets-macbook-neo-with-intels-wildcat-lake-usd699-starting-price-usd599-for-students",
    "domain": "AI 算力 / 半导体",
    "title": "Dell XPS 13 targets MacBook Neo with Intel's Wildcat Lake — $699 starting price, $599 for students",
    "url": "https://www.tomshardware.com/laptops/dell-xps-13-targets-macbook-neo-with-intels-wildcat-lake-usd699-starting-price-usd599-for-students",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T23:00:00+00:00",
    "summary": "Dell's XPS 13 is going after Apple's MacBook Neo with a $699 starting price, some higher specs, and Intel's new Wildcat Lake processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's long-awaited N1/N1X SoC specs leak ahead of Computex launch — N1 to feature up to 20 Arm-based cores, standard N1 equipped with 12- and 10-core configs",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T15:47:07+00:00",
    "summary": "The N1X reportedly comes in two SKUs: a top-end 20-core option with 6,144 CUDA cores matching the desktop RTX 5070, and a cut-down 18-core option with 5,120 CUDA cores. The standard N1 also has two co"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/core-i7-14700f-gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd470-discount-neweggs-abs-cyclone-aqua-prebuilt-is-usd1-329-with-code",
    "domain": "AI 算力 / 半导体",
    "title": "Core i7-14700F gaming PC with RTX 5060, 32GB of RAM, and 1TB of storage gets $470 discount — Newegg's ABS Cyclone Aqua prebuilt is $1,329 with code",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/core-i7-14700f-gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd470-discount-neweggs-abs-cyclone-aqua-prebuilt-is-usd1-329-with-code",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T15:01:35+00:00",
    "summary": "Newegg's ABS Cyclone Aqua prebuilt combines Intel's 20-core Core i7-14700F with Nvidia's RTX 5060, and 32GB of DDR5 memory for less than the cost of building a comparable system"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/softbank-to-spend-up-to-75-billion-on-french-ai-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "SoftBank to spend up to $87 billion on French AI data centers — country offers ample nuclear grid that US sites lack",
    "url": "https://www.tomshardware.com/tech-industry/softbank-to-spend-up-to-75-billion-on-french-ai-data-centers",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T14:48:09+00:00",
    "summary": "SoftBank carries over $130 billion in debt and took a $40 billion bridge loan in March to fund its latest OpenAI investment."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/new-one-meter-cubed-3d-printer-pumps-out-large-scale-prints-at-3kg-an-hour-modix-mama-1000-also-needs-a-big-wallet-with-prices-starting-at-usd35-000",
    "domain": "AI 算力 / 半导体",
    "title": "New one-meter-cubed 3D printer pumps out large-scale prints at 3kg an hour — Modix MAMA-1000 also needs a big wallet with prices starting at $35,000",
    "url": "https://www.tomshardware.com/3d-printing/new-one-meter-cubed-3d-printer-pumps-out-large-scale-prints-at-3kg-an-hour-modix-mama-1000-also-needs-a-big-wallet-with-prices-starting-at-usd35-000",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T13:59:24+00:00",
    "summary": "The MAMA-1000 pellet 3D printer from Modix prints with a whopping 3kg an hour throughput."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-yoga-slim-7x-review",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo Yoga Slim 7x review: Snapdragon X2 Elite makes its case",
    "url": "https://www.tomshardware.com/laptops/lenovo-yoga-slim-7x-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T13:56:36+00:00",
    "summary": "The Yoga Slim 7x brings Snapdragon performance, long battery life, and an OLED display provided you’re fine with ARM apps and USB-C everything."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsoft-veteran-recalls-the-last-time-nvidia-and-arm-was-the-future-of-windows-shares-a-video-of-the-first-time-windows-ran-on-nvidia-tegra-arm-from-2010",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft veteran recalls the last time Nvidia and Arm was the future of Windows — shares a video of ‘the first time Windows ran on Nvidia Tegra Arm’ from 2010",
    "url": "https://www.tomshardware.com/pc-components/microsoft-veteran-recalls-the-last-time-nvidia-and-arm-was-the-future-of-windows-shares-a-video-of-the-first-time-windows-ran-on-nvidia-tegra-arm-from-2010",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T13:05:00+00:00",
    "summary": "Microsoft veteran Steven Sinofsky is here to remind folks that excitement about a new PC era fueled by Nvidia and Arm culminated in the Surface RT 16 years ago."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding",
    "domain": "AI 算力 / 半导体",
    "title": "New AI-compute cryptocurrency Pearl sparks a GPU mining rush but profitability is already sliding — RTX 5090 daily revenue has halved to $17.19 since April",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T12:40:00+00:00",
    "summary": "A new cryptocurrency called Pearl has set off a short-lived GPU mining rush."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/robot-kits/the-ultimate-mosquito-killer-uses-lasers-and-ai-custom-model-trained-to-detect-and-lock-lasers-on-these-pests",
    "domain": "AI 算力 / 半导体",
    "title": "The 'ultimate mosquito killer' uses lasers and AI — custom model trained to detect and lock lasers on these pests",
    "url": "https://www.tomshardware.com/maker-stem/robot-kits/the-ultimate-mosquito-killer-uses-lasers-and-ai-custom-model-trained-to-detect-and-lock-lasers-on-these-pests",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T12:20:00+00:00",
    "summary": "A computer vision and robotics expert has created and trained what he boasts is “the ultimate mosquito killer” using machine learning and a laser."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/sound-cards/orpheus-ii-isa-soundcard-returns-due-to-popular-demand-aimed-at-dos-and-early-windows-users-this-card-includes-hardware-to-support-every-major-audio-standard",
    "domain": "AI 算力 / 半导体",
    "title": "Orpheus II ISA soundcard returns due to ‘popular demand’ — aimed at DOS and early Windows users, this card includes hardware to support every major audio standard",
    "url": "https://www.tomshardware.com/pc-components/sound-cards/orpheus-ii-isa-soundcard-returns-due-to-popular-demand-aimed-at-dos-and-early-windows-users-this-card-includes-hardware-to-support-every-major-audio-standard",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T12:00:00+00:00",
    "summary": "Want real Sound Blaster, Gravis UltraSound, OPL3 FM synthesis, and MPU-401 MIDI support? You got it."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/you-can-still-run-the-original-nvidia-control-panel-by-grabbing-it-from-the-microsoft-store-today-app-remains-useful-to-adjust-a-handful-of-rtx-pro-and-quadro-features-and-may-be-handy-for-troubleshooting",
    "domain": "AI 算力 / 半导体",
    "title": "You can still run the original Nvidia Control Panel by grabbing it from the Microsoft Store today — app remains useful to adjust a handful of RTX Pro and Quadro features, and may be handy for troubles",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/you-can-still-run-the-original-nvidia-control-panel-by-grabbing-it-from-the-microsoft-store-today-app-remains-useful-to-adjust-a-handful-of-rtx-pro-and-quadro-features-and-may-be-handy-for-troubleshooting",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T11:30:00+00:00",
    "summary": "The old Nvidia Control Panel is now a separate, optional download, but is it worth grabbing?"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/bill-gates-once-starred-in-a-bizarre-doom-promo-to-push-windows-95-back-in-1993-tech-mogul-wore-a-trench-coat-wielded-a-shotgun-and-shot-a-demon-saying-who-do-you-want-to-execute-today",
    "domain": "AI 算力 / 半导体",
    "title": "Bill Gates once starred in a bizarre Doom promo to push Windows 95 back in 1993 — tech mogul wore a trench coat, wielded a shotgun, and shot a demon, saying 'Who do you want to execute today?'",
    "url": "https://www.tomshardware.com/software/windows/bill-gates-once-starred-in-a-bizarre-doom-promo-to-push-windows-95-back-in-1993-tech-mogul-wore-a-trench-coat-wielded-a-shotgun-and-shot-a-demon-saying-who-do-you-want-to-execute-today",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T11:00:00+00:00",
    "summary": "Bill Gates gives a possessed Doom heavy weapon dude both barrels in a rediscovered Windows 95 plus DirectX gaming presentation."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/california-assembly-passes-3d-printer-bill-that-would-criminalize-bypassing-mandated-gun-blocking-software",
    "domain": "AI 算力 / 半导体",
    "title": "California Assembly passes 3D printer bill that would criminalize bypassing mandated gun-blocking software",
    "url": "https://www.tomshardware.com/3d-printing/california-assembly-passes-3d-printer-bill-that-would-criminalize-bypassing-mandated-gun-blocking-software",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T17:10:16+00:00",
    "summary": "California's Assembly has passed AB 2047, the California Firearm Printing Prevention Act, sending the amended bill to the state Senate."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/a-robot-startup-is-wreaking-havoc-on-short-term-rentals-in-san-francisco-airbnb-hosts-allege-guests-secretly-tested-robots-indoors-left-the-units-completely-trashed",
    "domain": "AI 算力 / 半导体",
    "title": "A robot startup is wreaking havoc on short-term rentals in San Francisco — Airbnb hosts allege 'guests' secretly tested robots indoors, left the units completely trashed",
    "url": "https://www.tomshardware.com/tech-industry/a-robot-startup-is-wreaking-havoc-on-short-term-rentals-in-san-francisco-airbnb-hosts-allege-guests-secretly-tested-robots-indoors-left-the-units-completely-trashed",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T17:09:50+00:00",
    "summary": "Picture this: you're the owner of a dainty place in San Francisco. You put it up on Airbnb, considering the area is sprawling with AI bros, thinking you'd get a pretty good return on your investment. "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x-and-nvidia-rtx-5060-combo-is-only-usd439-deal-includes-a-free-cpu-cooler-totaling-out-to-usd150-in-savings-for-a-great-budget-setup",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 5800X and Nvidia RTX 5060 combo is only $439 — deal includes a free CPU cooler, totaling out to $150 in savings for a great budget setup",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x-and-nvidia-rtx-5060-combo-is-only-usd439-deal-includes-a-free-cpu-cooler-totaling-out-to-usd150-in-savings-for-a-great-budget-setup",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T14:49:34+00:00",
    "summary": "If you've been looking to upgrade from an older system or just want to build a new one but 2026 prices have stopped you, we've got just the deal. The CPU and GPU are the two most important parts of a "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/atx12vo-v3-standard-shrinks-the-connector-and-maximizes-power-efficiency-new-8-pin-connector-also-brings-smarter-power-supply-monitoring",
    "domain": "AI 算力 / 半导体",
    "title": "ATX12VO V3 standard shrinks the connector and maximizes power efficiency — new 8-pin connector also brings smarter power supply monitoring",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/atx12vo-v3-standard-shrinks-the-connector-and-maximizes-power-efficiency-new-8-pin-connector-also-brings-smarter-power-supply-monitoring",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T14:10:35+00:00",
    "summary": "Intel's next-generation 12V-only PSU standard reportedly adds PMBus support, smaller connectors, and improved power efficiency."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/msis-new-32-oled-monitor-can-switch-between-4k-360-hz-1440p-520-hz-and-1080p-680-hz-featuring-a-penta-tandem-qd-oled-panel-with-rgb-stripe-subpixels",
    "domain": "AI 算力 / 半导体",
    "title": "MSI's new 32-inch OLED monitor can switch between 4K 360 Hz, 1440p 520 Hz, and 1080p 680 Hz — featuring a 'Penta Tandem' QD-OLED panel with RGB stripe subpixels",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/msis-new-32-oled-monitor-can-switch-between-4k-360-hz-1440p-520-hz-and-1080p-680-hz-featuring-a-penta-tandem-qd-oled-panel-with-rgb-stripe-subpixels",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T13:30:00+00:00",
    "summary": "Have you ever thought that going from 4K to 1080p on a dual-mode monitor was just too much of compromise for higher refresh rates? Well, worry not, as MSI has just answered your prayers with a 4K 360 "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nikon-plans-to-undercut-asml-on-price-to-win-back-chipmaking-lithography-customers",
    "domain": "AI 算力 / 半导体",
    "title": "Nikon weaponizes lower prices to break ASML's lithography monopoly — tech giant leverages in-house manufacturing to slash prices to lure back American chipmakers",
    "url": "https://www.tomshardware.com/tech-industry/nikon-plans-to-undercut-asml-on-price-to-win-back-chipmaking-lithography-customers",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T13:00:00+00:00",
    "summary": "Nikon will try to claw back lithography customers by selling argon fluoride (ArF) tools for less than the market leader, ASML."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/kevin-oleary-claims-chinese-propaganda-is-to-blame-for-anti-datacenter-sentiment-industry-proponents-and-trump-administration-reinforce-claims-of-foreign-interference",
    "domain": "AI 算力 / 半导体",
    "title": "Kevin O'Leary claims Chinese propaganda is to blame for anti-datacenter backlash, 'hundreds of millions of dollars' being spent to kill US dominance in AI — industry proponents and Trump administratio",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/kevin-oleary-claims-chinese-propaganda-is-to-blame-for-anti-datacenter-sentiment-industry-proponents-and-trump-administration-reinforce-claims-of-foreign-interference",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T12:30:00+00:00",
    "summary": "Kevin O'Leary claims Chinese propaganda to blame for anti-datacenter sentiment."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/huawei-chairman-thanks-the-us-for-supercharging-chinas-semiconductor-industry-washingtons-export-controls-encouraged-chinese-firms-to-invest-in-r-and-d-and-build-their-own-tech-stack-competing-with-american-technologies",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei chairman thanks the US for export restrictions on chips, says it supercharged China’s semiconductor industry — Washington’s export controls encouraged Chinese firms to invest in R&D and build t",
    "url": "https://www.tomshardware.com/tech-industry/huawei-chairman-thanks-the-us-for-supercharging-chinas-semiconductor-industry-washingtons-export-controls-encouraged-chinese-firms-to-invest-in-r-and-d-and-build-their-own-tech-stack-competing-with-american-technologies",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T12:00:00+00:00",
    "summary": "Huawei's current Rotating Chairman thanked the United States for its export bans, which boosted the progress of China's semiconductor industry. He made the comment after unveiling the groundbreaking L"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/the-usd60-retro-gaming-handheld-that-escaped-china-has-been-brought-back-home-lenovos-g02-pulled-from-sale-amid-copyright-drama-and-regional-restrictions",
    "domain": "AI 算力 / 半导体",
    "title": "Sellers circumvent Lenovo’s retro handheld ban with cheap wholesale storefronts — $41 gray-market G02 units pop up on Alibaba following initial storefront purge, systems were pulled from sale amid cop",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/the-usd60-retro-gaming-handheld-that-escaped-china-has-been-brought-back-home-lenovos-g02-pulled-from-sale-amid-copyright-drama-and-regional-restrictions",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T11:30:00+00:00",
    "summary": "Lenovo has pulled the G02 from sale on different Chinese e-commerce platforms after the company discovered that it was being sold outside of China."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/lucky-pc-builder-snipes-usd2-000-rog-astral-rtx-5080-on-facebook-marketplace-for-usd500-gets-a-nearly-75-percent-discount-card-that-works-perfectly",
    "domain": "AI 算力 / 半导体",
    "title": "Lucky PC builder snipes $2,000 ROG Astral RTX 5080 on Facebook Marketplace for $500 — gets a nearly 75% discount card that 'works perfectly'",
    "url": "https://www.tomshardware.com/pc-components/gpus/lucky-pc-builder-snipes-usd2-000-rog-astral-rtx-5080-on-facebook-marketplace-for-usd500-gets-a-nearly-75-percent-discount-card-that-works-perfectly",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T11:00:00+00:00",
    "summary": "A Redditor scored an RTX 5080 for $500 after they found it on Facebook Marketplace while browsing for deals. Another buyer even offered $800 for the GPU as the OP was on the way to pick up the item, b"
  },
  {
    "id": "hn:48291230",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Vera CPU Benchmarks: Olympus Cores Delivering Great Performance",
    "url": "https://www.phoronix.com/review/nvidia-vera-benchmarks",
    "source": "naves",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-05-27T08:15:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48323697",
    "domain": "AI 算力 / 半导体",
    "title": "The Nvidia Tax",
    "url": "https://www.cringely.com/2026/05/29/the-nvidia-tax/",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-05-29T14:41:43+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/the-stratosphere-race-haps-move-from-experiment-to-commercial-reality/",
    "domain": "AI 算力 / 半导体",
    "title": "The Stratosphere Race: HAPS Move from Experiment to Commercial Reality",
    "url": "https://www.eetimes.com/the-stratosphere-race-haps-move-from-experiment-to-commercial-reality/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T22:00:00+00:00",
    "summary": "Autonomous high-altitude platform stations are getting ready to bridge ground networks and LEO satellites. The post The Stratosphere Race: HAPS Move from Experiment to Commercial Reality appeared firs"
  },
  {
    "id": "rss:https://www.eetimes.com/gartner-says-supply-chain-confront-geopolitical-and-ai-challenges/",
    "domain": "AI 算力 / 半导体",
    "title": "Gartner Says Supply Chain Confront Geopolitical and AI Challenges",
    "url": "https://www.eetimes.com/gartner-says-supply-chain-confront-geopolitical-and-ai-challenges/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T14:16:57+00:00",
    "summary": "Gartner Supply Chain Symposium highlights strategies to navigate chaos, orchestrate agility, and accelerate Innovation. The post Gartner Says Supply Chain Confront Geopolitical and AI Challenges appea"
  },
  {
    "id": "rss:https://www.eetimes.com/qilimanjaro-pushes-analog-quantum-as-ai-compute-demands-surge/",
    "domain": "AI 算力 / 半导体",
    "title": "Qilimanjaro Pushes Analog Quantum as AI Compute Demands Surge",
    "url": "https://www.eetimes.com/qilimanjaro-pushes-analog-quantum-as-ai-compute-demands-surge/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T08:30:00+00:00",
    "summary": "Qilimanjaro says analog quantum systems could reduce error correction and accelerate AI, optimization, and simulation. On May 28, its analog system joined the digital quantum computer at the Barcelona"
  },
  {
    "id": "rss:https://www.eetimes.com/majestic-labs-raises-100m-for-memory-pooling-ai-server/",
    "domain": "AI 算力 / 半导体",
    "title": "Majestic Labs Raises $100M for Memory Pooling AI Server",
    "url": "https://www.eetimes.com/majestic-labs-raises-100m-for-memory-pooling-ai-server/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T22:00:00+00:00",
    "summary": "Server architecture will offer up to 100 TB of DRAM per accelerator. The post Majestic Labs Raises $100M for Memory Pooling AI Server appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/ai-in-design-verification-from-experimentation-to-measurable-capability/",
    "domain": "AI 算力 / 半导体",
    "title": "AI in Design Verification: From Experimentation to Measurable Capability",
    "url": "https://www.eetimes.com/ai-in-design-verification-from-experimentation-to-measurable-capability/",
    "source": "Mike Bartley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T14:28:52+00:00",
    "summary": "AI in design verification no longer asks if AI helps tasks, but does it measurably improve real verification flows? The post AI in Design Verification: From Experimentation to Measurable Capability ap"
  },
  {
    "id": "rss:https://www.eetimes.com/chiplets-ecosystems-and-europes-post-fab-semiconductor-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "Chiplets, Ecosystems, and Europe’s Post-Fab Semiconductor Strategy",
    "url": "https://www.eetimes.com/chiplets-ecosystems-and-europes-post-fab-semiconductor-strategy/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T08:38:29+00:00",
    "summary": "“Can Europe realistically compete on leading-edge fabs alone?” Maria Marced said. “No.” The post Chiplets, Ecosystems, and Europe’s Post-Fab Semiconductor Strategy appeared first on EE Times."
  },
  {
    "id": "hn:48245087",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Removes Gaming Revenue Category from Financial Reports",
    "url": "https://www.guru3d.com/story/nvidia-removes-gaming-revenue-category-from-financial-reports/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-05-23T05:50:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48284628",
    "domain": "AI 算力 / 半导体",
    "title": "Trump's 25% cut on Nvidia chips to China backfired as Beijing blocks H200 sales",
    "url": "https://finance.yahoo.com/markets/stocks/articles/trumps-25-cut-nvidia-chips-194500691.html",
    "source": "frasermarlow",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-26T19:21:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48274048",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan Overtakes India as Fifth-Largest Stock Market",
    "url": "https://www.bloomberg.com/news/articles/2026-05-26/tsmc-s-relentless-rise-powers-taiwan-s-market-value-above-india",
    "source": "leopoldj",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-26T01:49:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48195039",
    "domain": "AI 算力 / 半导体",
    "title": "How Corrupt Is Trump? Here Are the Numbers",
    "url": "https://www.thebulwark.com/p/how-corrupt-is-trump-here-are-the-numbers-trades-chips-nvidia-pardons-settlement-fund",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-05-19T15:55:21+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/vicinity-unveils-trave-ai-native-sdr-platform-at-5g-acia-frankfurt/",
    "domain": "AI 算力 / 半导体",
    "title": "Vicinity Unveils “TRAVE” — AI-Native SDR Platform at 5G-ACIA Frankfurt",
    "url": "https://www.eetimes.com/vicinity-unveils-trave-ai-native-sdr-platform-at-5g-acia-frankfurt/",
    "source": "Vicinity Technologies Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T01:00:00+00:00",
    "summary": "Vicinity Technologies Limited has officially unveiled TRAVE, its next-generation AI-native 5G/6G Software Defined Radio (SDR) platform, during the 5G-ACIA 5G User Conference in Frankfurt. The post Vic"
  },
  {
    "id": "rss:https://www.eetimes.com/canada-university-of-saskatchewan-acquires-quantum-computer/",
    "domain": "AI 算力 / 半导体",
    "title": "Canada’s University of Saskatchewan Acquires Quantum Computer",
    "url": "https://www.eetimes.com/canada-university-of-saskatchewan-acquires-quantum-computer/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T19:00:00+00:00",
    "summary": "University of Saskatchewan will leverage quantum computing for health, defense, energy, and agriculture research. The post Canada’s University of Saskatchewan Acquires Quantum Computer appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/intelligent-configurable-i-o-edge-autonomy-thermal-efficiency-and-higher-uptime-in-industrial-control-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Intelligent, Configurable I/O: Edge Autonomy, Thermal Efficiency, and Higher Uptime in Industrial Control Systems",
    "url": "https://www.eetimes.com/intelligent-configurable-i-o-edge-autonomy-thermal-efficiency-and-higher-uptime-in-industrial-control-systems/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T14:00:00+00:00",
    "summary": "This paper explores how configurable and intelligent I/O technologies are transforming industrial control systems by enabling greater flexibility, improved thermal performance, and higher system uptim"
  },
  {
    "id": "rss:https://www.eetimes.com/startup-boosts-scale-up-to-1000-gpus-in-a-single-domain/",
    "domain": "AI 算力 / 半导体",
    "title": "Startup Boosts Scale-Up to 1000+ GPUs in a Single Domain",
    "url": "https://www.eetimes.com/startup-boosts-scale-up-to-1000-gpus-in-a-single-domain/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T12:00:00+00:00",
    "summary": "Delos Data wants to enable practical scale-up domains of 1000+ GPUs in flexible topology designs. The post Startup Boosts Scale-Up to 1000+ GPUs in a Single Domain appeared first on EE Times."
  },
  {
    "id": "hn:47989883",
    "domain": "大厂讯息",
    "title": "VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage",
    "url": "https://github.com/microsoft/vscode/pull/310226",
    "source": "indrora",
    "platform": "hackernews",
    "points": 1513,
    "published_at": "2026-05-02T19:57:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196570",
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
    "title": "Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS",
    "url": "https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/",
    "source": "ChrisArchitect",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-05-27T17:24:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48080702",
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
    "title": "Zuckerberg 'personally authorized' Meta's copyright infringement, publishers say",
    "url": "https://apnews.com/article/meta-mark-zuckerberg-ai-publishers-lawsuit-llama-5609846d4d840014974a847b01079c32",
    "source": "jethronethro",
    "platform": "hackernews",
    "points": 156,
    "published_at": "2026-05-05T22:07:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48084710",
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
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
    "domain": "大厂讯息",
    "title": "Update on \"Co-authored-by: Copilot\" in commit messages",
    "url": "https://github.com/microsoft/vscode/issues/314311",
    "source": "extesy",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-05-06T03:15:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/940584/microsoft-surface-laptop-ultra-nvidia-rtx-spark-pictures",
    "domain": "大厂讯息",
    "title": "This is the Microsoft Surface Laptop Ultra with Nvidia RTX Spark",
    "url": "https://www.theverge.com/tech/940584/microsoft-surface-laptop-ultra-nvidia-rtx-spark-pictures",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:36:41+00:00",
    "summary": "Once upon a time, Microsoft had to write off $900 million betting an Arm-based Nvidia chip could power its first flagship Windows portable, the original Microsoft Surface. But today, it's trying again"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date",
    "domain": "大厂讯息",
    "title": "Nvidia announces RTX Spark as ‘the most efficient PC chip ever built’",
    "url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:28:53+00:00",
    "summary": "This fall, Nvidia will officially become a consumer PC chipmaker like Intel, AMD, Apple, and Qualcomm, putting a complete computing chip - not just graphics - into the very heart of laptops and mini-P"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940524/amd-computex-am5-promise-2029-rx9070gre-7700x3d-5800x3d",
    "domain": "大厂讯息",
    "title": "AMD’s new pitch: our old tech is so good you should just keep using it",
    "url": "https://www.theverge.com/tech/940524/amd-computex-am5-promise-2029-rx9070gre-7700x3d-5800x3d",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T00:00:00+00:00",
    "summary": "Computex 2026 is underway in Taiwan, and we're expecting all manner of flashy computers with jaw-dropping prices (or no prices at all) as the entire industry navigates RAMageddon. But for desktop PC g"
  },
  {
    "id": "rss:https://www.theverge.com/games/938956/alienware-computex-tandem-qd-oled-penta-rgb-stripe-gaming-monitors-specs",
    "domain": "大厂讯息",
    "title": "The QD-OLED gaming monitor that started it all got a big upgrade",
    "url": "https://www.theverge.com/games/938956/alienware-computex-tandem-qd-oled-penta-rgb-stripe-gaming-monitors-specs",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T23:00:00+00:00",
    "summary": "Alienware is taking to this year's Computex 2026 in Taipei to announce some cool gaming monitors, most notably two exciting OLED options that are coming at different points this year. First off, the c"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940498/dell-xps-13-student-laptop-intel-wildcat-panther-lake-computex-price",
    "domain": "大厂讯息",
    "title": "Dell is bringing back the XPS 13 as a MacBook Neo competitor — with a temporary discount to $599",
    "url": "https://www.theverge.com/tech/940498/dell-xps-13-student-laptop-intel-wildcat-panther-lake-computex-price",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T23:00:00+00:00",
    "summary": "Dell is making good on its tease from CES and finally announcing a new XPS 13. The XPS 13 returns as a budget-friendly option, launching in July at a promotional student price of $599 - though that in"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940572/apples-strategy-smart-glasses-smart-watches",
    "domain": "大厂讯息",
    "title": "Apple’s strategy for smart glasses is the same as smart watches",
    "url": "https://www.theverge.com/tech/940572/apples-strategy-smart-glasses-smart-watches",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T21:33:11+00:00",
    "summary": "Apple isn't just looking to take on Meta in the smart glasses market; it's looking to upend eyewear as a whole, according to Bloomberg's Mark Gurman. When the Apple Watch launched, it wasn't simply co"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940540/how-to-watch-nvidias-computex-keynote",
    "domain": "大厂讯息",
    "title": "How to watch Nvidia&#8217;s Computex keynote",
    "url": "https://www.theverge.com/tech/940540/how-to-watch-nvidias-computex-keynote",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T20:20:35+00:00",
    "summary": "NVIDIA's CEO Jensen Huang is set to take the stage for his GTC Taipei keynote at 8PM PT / 11PM ET. You can watch all the announcements here and embedded below. Rumors have been flying about what to ex"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/940523/minecraft-movie-squared-sequel-kirsten-dunst-alex",
    "domain": "大厂讯息",
    "title": "Here’s your first look at ‘A Minecraft Movie Squared’ with Kirsten Dunst as Alex",
    "url": "https://www.theverge.com/entertainment/940523/minecraft-movie-squared-sequel-kirsten-dunst-alex",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T19:28:11+00:00",
    "summary": "The A Minecraft Movie sequel officially has a title: A Minecraft Movie Squared. What's more, we now know that Kirsten Dunst will star as Alex, the game's female character option, and that Matt Berry i"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/940449/feeble-little-horse-bitknot-music-album-review",
    "domain": "大厂讯息",
    "title": "Feeble Little Horse leans into digital weirdness on bitknot",
    "url": "https://www.theverge.com/entertainment/940449/feeble-little-horse-bitknot-music-album-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T16:00:00+00:00",
    "summary": "From the opening moments of bitknot, it's obvious that Feeble Little Horse has found an entirely new gear. Where on Girl with Fish the blown-out textures were more '90s indie rock and shoegaze, on the"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/940486/united-flight-236-bluetooth-speaker-name-bomb",
    "domain": "大厂讯息",
    "title": "United flight forced to turn around because of a Bluetooth speaker name",
    "url": "https://www.theverge.com/transportation/940486/united-flight-236-bluetooth-speaker-name-bomb",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T15:50:02+00:00",
    "summary": "United flight 236 from Newark to Palma de Mallorca on Saturday night was forced to turn around just an hour after takeoff due to security concerns around a Bluetooth signal. Multiple Redditors claimed"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/",
    "domain": "大厂讯息",
    "title": "Erin Brockovich takes aim at data center secrecy",
    "url": "https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T21:05:14+00:00",
    "summary": "Environmental activist Erin Brockovich has a new mission."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/this-weekends-two-biggest-movies-were-both-directed-by-youtubers/",
    "domain": "大厂讯息",
    "title": "This weekend’s two biggest movies were both directed by YouTubers",
    "url": "https://techcrunch.com/2026/05/31/this-weekends-two-biggest-movies-were-both-directed-by-youtubers/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T18:34:58+00:00",
    "summary": "The YouTube-to-prestige-horror pipeline is looking very strong."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/this-is-fine-artist-kc-green-reaches-agreement-with-ai-startup-artisan/",
    "domain": "大厂讯息",
    "title": "‘This is fine’ artist KC Green reaches agreement with AI startup Artisan",
    "url": "https://techcrunch.com/2026/05/31/this-is-fine-artist-kc-green-reaches-agreement-with-ai-startup-artisan/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T18:28:17+00:00",
    "summary": "The startup has apparently taken down the ads using KC Green's \"This is fine\" meme."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/techcrunch-mobility-it-doesnt-matter-that-people-hate-the-ferrari-luce/",
    "domain": "大厂讯息",
    "title": "TechCrunch Mobility: It doesn’t matter that people hate the Ferrari Luce",
    "url": "https://techcrunch.com/2026/05/31/techcrunch-mobility-it-doesnt-matter-that-people-hate-the-ferrari-luce/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, how AI is playing a part."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/making-sense-of-the-debate-over-ai-psychosis/",
    "domain": "大厂讯息",
    "title": "Making sense of the debate over AI psychosis",
    "url": "https://techcrunch.com/2026/05/31/making-sense-of-the-debate-over-ai-psychosis/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T15:30:00+00:00",
    "summary": "On the latest episode of Equity, we debate whether tech CEOs are \"uniquely prone to AI psychosis.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/black-founders-raise-highest-amount-of-quarterly-funding-since-2022-but-theres-a-catch/",
    "domain": "大厂讯息",
    "title": "Black founders raise highest amount of quarterly funding since 2022, but there’s a catch",
    "url": "https://techcrunch.com/2026/05/31/black-founders-raise-highest-amount-of-quarterly-funding-since-2022-but-theres-a-catch/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T15:00:00+00:00",
    "summary": "Speaking to TechCrunch, Crunchbase’s head of research Gené Teare, said the factors holding back Black founders include “access to networks, relationships, and early introductions.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/i-went-to-the-so-called-steroid-olympics-to-understand-why-silicon-valley-is-obsessed-with-peptides/",
    "domain": "大厂讯息",
    "title": "What happens in Vega$: steroids, swimmers, and a billion-dollar hustle",
    "url": "https://techcrunch.com/2026/05/31/i-went-to-the-so-called-steroid-olympics-to-understand-why-silicon-valley-is-obsessed-with-peptides/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T13:00:00+00:00",
    "summary": "The Enhanced Games — a singular sporting competition where a majority of the athletes were on performance enhancing drugs — may herald a new business model that the tech industry is ready to embrace."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/",
    "domain": "大厂讯息",
    "title": "SoftBank says it will invest up to €75 billion to build French data centers",
    "url": "https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T21:45:00+00:00",
    "summary": "The goal, the firm said, is to develop and operate up to 5 gigawatts of additional data center capacity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/snap-alums-unveil-ghost-angels-fund/",
    "domain": "大厂讯息",
    "title": "Snap alums unveil Ghost Angels fund",
    "url": "https://techcrunch.com/2026/05/30/snap-alums-unveil-ghost-angels-fund/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T17:00:00+00:00",
    "summary": "A group of 20 Snap alumni has come together to launch a fund called Ghost Angels to back the next generation of social media."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/",
    "domain": "大厂讯息",
    "title": "‘What a joke’: Github Copilot’s new token-based billing spurs consternation among devs",
    "url": "https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T16:30:00+00:00",
    "summary": "The golden age of Microsoft's Github Copilot appears to be at an end."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/meta-is-reportedly-developing-an-ai-pendant/",
    "domain": "大厂讯息",
    "title": "Meta is reportedly developing an AI pendant",
    "url": "https://techcrunch.com/2026/05/30/meta-is-reportedly-developing-an-ai-pendant/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T15:59:58+00:00",
    "summary": "Meta seems to be making big bets on AI-powered hardware."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/i-put-googles-24-7-ai-assistant-gemini-spark-to-work-and-its-actually-pretty-useful/",
    "domain": "大厂讯息",
    "title": "I put Google’s 24/7 AI assistant Gemini Spark to work, and it’s actually pretty useful",
    "url": "https://techcrunch.com/2026/05/30/i-put-googles-24-7-ai-assistant-gemini-spark-to-work-and-its-actually-pretty-useful/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T15:30:00+00:00",
    "summary": "Gemini Spark helps automate everyday tasks, from inbox summaries to local event planning, but it’s unclear why Google made it a separate product."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/the-groupthink-boom-what-three-top-vcs-really-think-about-the-ai-frenzy/",
    "domain": "大厂讯息",
    "title": "The groupthink boom: what three top VCs really think about the AI frenzy",
    "url": "https://techcrunch.com/2026/05/30/the-groupthink-boom-what-three-top-vcs-really-think-about-the-ai-frenzy/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T14:49:27+00:00",
    "summary": "\"If you're 22 years old in San Francisco and building something in AI, there may be a seed term sheet in your inbox — but if you're 19, oh my God, this means you're really good; you might already have"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/as-the-browser-wars-heat-up-here-are-the-hottest-alternatives-to-chrome-and-safari-in-2026/",
    "domain": "大厂讯息",
    "title": "As the browser wars heat up, here are the hottest alternatives to Chrome and Safari in 2026",
    "url": "https://techcrunch.com/2026/05/30/as-the-browser-wars-heat-up-here-are-the-hottest-alternatives-to-chrome-and-safari-in-2026/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T13:00:00+00:00",
    "summary": "We’ve compiled an overview of some of the top alternative browsers available today aiming to challenge Chrome and Safari."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/this-300-pizza-oven-can-easily-help-elevate-your-summer-pizza-nights/",
    "domain": "大厂讯息",
    "title": "This $300 pizza oven can easily help elevate your summer pizza nights",
    "url": "https://techcrunch.com/2026/05/30/this-300-pizza-oven-can-easily-help-elevate-your-summer-pizza-nights/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T13:00:00+00:00",
    "summary": "The Ninja Artisan Outdoor Pizza Oven is aimed at people who want delicious pizza nights without having to deal with things like propane or wood pellets, unlike many other pizza ovens."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/tiktoks-road-to-becoming-a-super-app/",
    "domain": "大厂讯息",
    "title": "TikTok’s road to becoming a super app",
    "url": "https://techcrunch.com/2026/05/30/tiktoks-road-to-becoming-a-super-app/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T13:00:00+00:00",
    "summary": "TikTok may be working to become the app that people use for most of their digital activities."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/05/on-its-40th-anniversary-we-reassess-1986s-spacecamp/",
    "domain": "大厂讯息",
    "title": "On its 40th anniversary, we reassess 1986's SpaceCamp",
    "url": "https://arstechnica.com/culture/2026/05/on-its-40th-anniversary-we-reassess-1986s-spacecamp/",
    "source": "Eric Berger & Lee Hutchinson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T11:15:12+00:00",
    "summary": "Is it a hidden gem, a cult classic, or hopelessly dumb? We vote \"all of the above.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/05/they-call-it-stupid-hot-for-a-reason-heat-muddles-animal-brains/",
    "domain": "大厂讯息",
    "title": "They call it stupid hot for a reason: Heat muddles animal brains",
    "url": "https://arstechnica.com/science/2026/05/they-call-it-stupid-hot-for-a-reason-heat-muddles-animal-brains/",
    "source": "Marta Zaraska",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T10:00:07+00:00",
    "summary": "As temperatures rise, some creatures pick fights while others struggle to learn."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/05/grifters-cynics-and-true-believers-the-family-tree-of-vaccine-opponents/",
    "domain": "大厂讯息",
    "title": "Grifters, cynics, and true believers: The family tree of vaccine opponents",
    "url": "https://arstechnica.com/science/2026/05/grifters-cynics-and-true-believers-the-family-tree-of-vaccine-opponents/",
    "source": "Diana Gitig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T11:00:05+00:00",
    "summary": "A new book looks into the long history of people who have opposed vaccines."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/05/environmentalists-turn-out-in-force-to-oppose-trump-coal-ash-rollbacks/",
    "domain": "大厂讯息",
    "title": "Environmentalists turn out in force to oppose Trump coal ash rollbacks",
    "url": "https://arstechnica.com/tech-policy/2026/05/environmentalists-turn-out-in-force-to-oppose-trump-coal-ash-rollbacks/",
    "source": "Arcelia Martin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T10:00:38+00:00",
    "summary": "Trump admin wants to rely on states for coal ash monitoring, enforcement, allow them to bypass national standards."
  },
  {
    "id": "rss:https://www.producthunt.com/products/marqly",
    "domain": "大厂讯息",
    "title": "Marqly 5.0",
    "url": "https://www.producthunt.com/products/marqly",
    "source": "Kim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T09:30:11+00:00",
    "summary": "Your AI-powered bookmark manager Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/oura",
    "domain": "大厂讯息",
    "title": "Oura Ring 5",
    "url": "https://www.producthunt.com/products/oura",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T18:05:21+00:00",
    "summary": "The world’s smallest smart ring, now even better Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3824416083825027?f=rss",
    "domain": "大厂讯息",
    "title": "获国家队采购、联名比音勒芬，「PLAYTOP」想用东方美学演绎户外功能服饰｜早期项目",
    "url": "https://36kr.com/p/3824416083825027?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:19:10+00:00",
    "summary": "当户外运动品牌纷纷在“防晒”“速干”“保暖”等参数上展开竞赛时，一家成立仅三年的新锐品牌，开始在功能的基础上，将“东方美学”元素融入一件功能衣中。 成立于2022年的「PLAYTOP」，是一家将东方美学与天然功能材料融合的户外品牌，瞄准25-40岁追求颜值与舒适体验的高智菁英人群。2025年雪季，PLAYTOP做到了小红书滑雪速干衣用户主动搜索排名第一。 目前，PLAYTOP已获得12项独家专利及"
  }
]
```
