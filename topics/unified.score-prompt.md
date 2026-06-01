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
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 948689,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 859213,
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
    "points": 659982,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 565191,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 560941,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 412173,
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
    "points": 382812,
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
    "points": 364762,
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
    "points": 316843,
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
    "points": 307964,
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
    "points": 237633,
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
    "points": 229460,
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
    "points": 220929,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 172901,
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
    "points": 163938,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 149381,
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
    "points": 140195,
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
    "points": 140018,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 91831,
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
    "points": 84512,
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
    "points": 81729,
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
    "points": 69738,
    "published_at": "2026-04-01T10:12:34+00:00",
    "summary": "视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1CDVu6TEnv",
    "domain": "AI",
    "title": "Vibe coding成瘾。一开始觉得很兴奋，但是玩多了就有一种游戏开挂的感觉。像这个小demo古法编程怎么也要写两天，AI来写15分钟搞定了，一开始挺期待的…",
    "url": "http://www.bilibili.com/video/av116661831208897",
    "source": "工科男孙老师",
    "platform": "bilibili",
    "points": 61158,
    "published_at": "2026-05-30T05:23:02+00:00",
    "summary": "Vibe coding成瘾。一开始觉得很兴奋，但是玩多了就有一种游戏开挂的感觉。像这个小demo古法编程怎么也要写两天，AI来写15分钟搞定了，一开始挺期待的，过去没时间玩的东西现在都能很快搞定，但是做完毫无快感。就像是上班后买了大学时心心念念的psp游戏机，但是再也没有借同学的那种快感了。"
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "domain": "AI",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 57498,
    "published_at": "2025-06-28T02:37:22+00:00",
    "summary": "视频主题&amp;项目背景\n主题： 分享个人如何使用cursor 从0到1开发一个比较大的项目，使用的技术栈是vue+小程序+java\n项目\n一个B2B的订货商城及供应链全流程管理，包含的端有：\n小程序商城端\n供应商端\n仓储物流端\n司机配送端\n销售端\n后台管理系统\n以上小程序端都是使用webview的方式\n核心功能：\n商城的基本功能: 正逆向订单、商品、购物车、优惠券、积分、钱包、充值、工单等\n供"
  },
  {
    "id": "bvid:BV1NBV56DEBA",
    "domain": "AI",
    "title": "Codex依赖症重症患者采访",
    "url": "http://www.bilibili.com/video/av116665119479370",
    "source": "AIwood爱屋研究室",
    "platform": "bilibili",
    "points": 54111,
    "published_at": "2026-05-31T01:30:00+00:00",
    "summary": "剧情纯属虚构，如有雷同，算你NB！"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 50813,
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
    "points": 50129,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1ZrXLYyEFx",
    "domain": "AI",
    "title": "自己动手写一个MCP Server，你就知道MCP怎么回事了",
    "url": "http://www.bilibili.com/video/av114183114856586",
    "source": "AI橙爆了",
    "platform": "bilibili",
    "points": 49066,
    "published_at": "2025-03-18T11:15:52+00:00",
    "summary": "视频制作不易，请一键三连！私我领取文档源码"
  },
  {
    "id": "bvid:BV1fGFsznEas",
    "domain": "AI",
    "title": "vibe coding 10分钟做一个塔罗牌游戏",
    "url": "http://www.bilibili.com/video/av116029028042969",
    "source": "鸭鸭摘花",
    "platform": "bilibili",
    "points": 44967,
    "published_at": "2026-02-07T11:20:13+00:00",
    "summary": "一个简单的教程 一行代码不写 做一个塔罗牌游戏"
  },
  {
    "id": "bvid:BV13K1YBtE6e",
    "domain": "AI",
    "title": "【GMM】MCP 使用说明",
    "url": "http://www.bilibili.com/video/av115485010168640",
    "source": "3DM小莫",
    "platform": "bilibili",
    "points": 35517,
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
    "points": 33187,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 28702,
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
    "points": 26178,
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
    "points": 24139,
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
    "points": 21994,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1MxVY6rELF",
    "domain": "AI",
    "title": "🚀Opus 4.8 + Dynamic Workflows自动生成Harness指挥上百个subagents并行工作，Claude Code开发效率倍增！",
    "url": "http://www.bilibili.com/video/av116658005874381",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 17802,
    "published_at": "2026-05-29T13:11:34+00:00",
    "summary": "Opus 4.8 + Dynamic Workflows自动生成Harness指挥上百个subagents并行工作，廉价Haiku+旗舰Opus搭配！Claude Code效率倍增一天干完一个月的活\n\n视频简介：\n\n不用手写Harness了！Anthropic发布Dynamic Workflows功能彻底改写Harness Engineering，AI 编程进入新阶段！！ 直接抹平Harness高"
  },
  {
    "id": "bvid:BV1NYVG6jEKE",
    "domain": "AI",
    "title": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通",
    "url": "http://www.bilibili.com/video/av116662133132089",
    "source": "字节软件测试",
    "platform": "bilibili",
    "points": 14619,
    "published_at": "2026-05-30T06:39:27+00:00",
    "summary": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通"
  },
  {
    "id": "bvid:BV1W9cZzxEYs",
    "domain": "AI",
    "title": "AI 当助手！Claude 深度协助 UE5 游戏开发全流程",
    "url": "http://www.bilibili.com/video/av116209752277031",
    "source": "叁昧火游戏",
    "platform": "bilibili",
    "points": 14519,
    "published_at": "2026-03-11T12:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13gVb6KEEC",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI大模型零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116656244261441",
    "source": "Agent智能体搭建-",
    "platform": "bilibili",
    "points": 13699,
    "published_at": "2026-05-29T05:45:53+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 13531,
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
    "points": 13436,
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
    "points": 12748,
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
    "points": 12594,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV15BGX63E2K",
    "domain": "AI",
    "title": "【5.28最新发布】claude桌面版安装教程！一周快速入门claude code保姆级教程！",
    "url": "http://www.bilibili.com/video/av116651194385987",
    "source": "是蒜七丫",
    "platform": "bilibili",
    "points": 11376,
    "published_at": "2026-05-28T08:19:55+00:00",
    "summary": "求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三"
  },
  {
    "id": "bvid:BV1jsV861EVM",
    "domain": "AI",
    "title": "【2026胎教级】Claude Code全栈教程，从入门到精通，搞定所有开发场景，小白10分钟搞定，全程干货无废话，存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116657502687649",
    "source": "程序员黑梦",
    "platform": "bilibili",
    "points": 11265,
    "published_at": "2026-05-29T11:08:50+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oNVH6xEWS",
    "domain": "AI",
    "title": "Claude Code 国内直连保姆级教程｜10分钟从入门到精通，原理+安装+实战全覆盖，解锁Vibe Coding编程新范式",
    "url": "http://www.bilibili.com/video/av116667602503393",
    "source": "码士集团-小晨晨晨",
    "platform": "bilibili",
    "points": 9392,
    "published_at": "2026-05-31T06:14:34+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 9137,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 8896,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1bwVp67Ekg",
    "domain": "AI",
    "title": "【Agent】全B站最全最细的Agent开发教程，2026最新！全程干货，允许白嫖！从入门到企业级实战掌握Agent智能体开发核心内容！学完直接就业！",
    "url": "http://www.bilibili.com/video/av116651680924759",
    "source": "AI应用全栈开发",
    "platform": "bilibili",
    "points": 8637,
    "published_at": "2026-05-28T10:22:23+00:00",
    "summary": "【视频配套籽料、零基础学习路线、实战项目案例、电子书+问题解答 在 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含AI大模型入门、AI开发环境搭建等一些基础概念、Agent、Langchain、LangGraph和私有化部署\n无论是新手小白，还是有经验的友友，皆可学习\n视频对你有用的话，还请 一键三连【长按点赞】支持一下UP哦！你的支持是我更新的动力~"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 7914,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "hn:48352939",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark",
    "url": "https://www.nvidia.com/en-us/products/rtx-spark/",
    "source": "shenli3514",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-06-01T05:24:40+00:00",
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
    "id": "hn:48352693",
    "domain": "AI 算力 / 半导体",
    "title": "A powerful new chapter for Windows PCs, accelerated by Nvidia RTX Spark",
    "url": "https://blogs.windows.com/windowsexperience/2026/05/31/introducing-a-powerful-new-chapter-for-windows-pcs-accelerated-by-nvidia-rtx-spark/",
    "source": "WalterSobchak",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-06-01T04:45:20+00:00",
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
    "id": "hn:48352951",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Announces RTX Spark",
    "url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date",
    "source": "rayhaanj",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-06-01T05:26:06+00:00",
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
    "id": "hn:48352705",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Microsoft Reinvent Windows PCs for the Age of Personal AI",
    "url": "https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark",
    "source": "goshx",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-01T04:47:29+00:00",
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
    "id": "rss:https://www.eetimes.com/beyond-the-factory-floor-xr-training-for-the-next-industrial-era/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond the Factory Floor: XR Training for the Next Industrial Era",
    "url": "https://www.eetimes.com/beyond-the-factory-floor-xr-training-for-the-next-industrial-era/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T07:30:00+00:00",
    "summary": "EU-funded project MASTER is using extended reality to transform how industrial robotics is taught and deployed. The post Beyond the Factory Floor: XR Training for the Next Industrial Era appeared firs"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/negative-time-experiment-clears-peer-review-as-photons-appear-to-leave-an-atom-cloud-before-entering",
    "domain": "AI 算力 / 半导体",
    "title": "Negative time experiment clears peer review as photons appear to leave an atom cloud before entering — groundbreaking quantum 'negative time' proven after 1 million test runs",
    "url": "https://www.tomshardware.com/tech-industry/negative-time-experiment-clears-peer-review-as-photons-appear-to-leave-an-atom-cloud-before-entering",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:30:00+00:00",
    "summary": "A University of Toronto experiment showing that photons can spend a negative amount of time inside a cloud of atoms has been published in Physical Review Letters."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/acers-pm131qt-portable-monitor-is-a-12-3-inch-touchscreen-with-magnetic-mounting-a-built-in-kickstand-and-5-point-touch-1920-x-720-ips-screen-has-pogo-pins-for-a-keyboard-and-is-designed-for-secondary-and-in-vehicle-use",
    "domain": "AI 算力 / 半导体",
    "title": "Acer’s PM131QT portable monitor is a 12.3-inch touchscreen with magnetic mounting, a built-in kickstand, and 5-point touch – 1920 x 720 IPS screen has pogo pins for a keyboard, and is designed for sec",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/acers-pm131qt-portable-monitor-is-a-12-3-inch-touchscreen-with-magnetic-mounting-a-built-in-kickstand-and-5-point-touch-1920-x-720-ips-screen-has-pogo-pins-for-a-keyboard-and-is-designed-for-secondary-and-in-vehicle-use",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:00:00+00:00",
    "summary": "Are you looking for a compact monitor for multiple uses around the home and on the go? Acer’s new PM131QT might be just what you’re looking for."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/resourceful-runner-can-race-my-own-ghost-using-homemade-meta-ray-ban-display-app-also-adds-bonus-coins-mini-leaderboard-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Resourceful runner 'can race my own ghost' using homemade Meta Ray-Ban Display app — also adds bonus coins, mini leaderboard, and more",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/resourceful-runner-can-race-my-own-ghost-using-homemade-meta-ray-ban-display-app-also-adds-bonus-coins-mini-leaderboard-and-more",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:48:30+00:00",
    "summary": "Video demonstrates brand-new gamified running app for the Meta Ray-Ban Display glasses."
  },
  {
    "id": "rss:https://www.tomshardware.com/news/live/computex-2026-",
    "domain": "AI 算力 / 半导体",
    "title": "Computex 2026 Live: Every update and announcement from day one in Taipei",
    "url": "https://www.tomshardware.com/news/live/computex-2026-",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:39:37+00:00",
    "summary": "Every update live from Taipei as Computex continues in Taiwan."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/amd-promises-13-percent-uplift-with-new-expo-ultra-low-latency-overclocking-on-ddr5-dimms-automatic-memory-overclocking-delivers-4-percent-improvement-over-standard-expo-says-amd",
    "domain": "AI 算力 / 半导体",
    "title": "AMD promises 13% uplift with new EXPO ‘Ultra Low Latency’ overclocking on DDR5 DIMMs — automatic memory overclocking delivers 4% improvement over standard EXPO, says AMD",
    "url": "https://www.tomshardware.com/pc-components/ram/amd-promises-13-percent-uplift-with-new-expo-ultra-low-latency-overclocking-on-ddr5-dimms-automatic-memory-overclocking-delivers-4-percent-improvement-over-standard-expo-says-amd",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:30:00+00:00",
    "summary": "AMD’s upcoming EXPO ‘Ultra Low Latency’ automatic memory overclocking promises a 13% improvement over standard DDR5 speeds, as well as a 4% jump compared to standard EXPO."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-warns-it-has-a-healthy-dose-of-paranoia-over-nvidia-entrance-into-pc-market-company-says-rtx-spark-is-great-for-the-market-while-touting-the-virtues-of-x86",
    "domain": "AI 算力 / 半导体",
    "title": "Intel warns it has 'a healthy dose of paranoia' over Nvidia entrance into PC market — company says RTX Spark is 'great for the market' while touting the virtues of x86",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-warns-it-has-a-healthy-dose-of-paranoia-over-nvidia-entrance-into-pc-market-company-says-rtx-spark-is-great-for-the-market-while-touting-the-virtues-of-x86",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:30:00+00:00",
    "summary": "Intel reacts to Nvidia’s RTX Spark announcement, and says that it’s treating the green giant’s entrance into consumer SoCs with “a healthy dose of skepticism.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/we-went-hands-on-with-qualcomms-new-usd300-and-up-arm-laptop-platform-mystery-eight-core-cpu-in-active-cooled-snapdragon-c-laptop-surfaces-in-acer-aspire-go-15",
    "domain": "AI 算力 / 半导体",
    "title": "We went hands-on with Qualcomm's new '$300 and up' ARM laptop platform with mystery eight-core CPU — active-cooled Snapdragon C laptop surfaces in Acer Aspire Go 15",
    "url": "https://www.tomshardware.com/laptops/we-went-hands-on-with-qualcomms-new-usd300-and-up-arm-laptop-platform-mystery-eight-core-cpu-in-active-cooled-snapdragon-c-laptop-surfaces-in-acer-aspire-go-15",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "We've learned a few new details of the Snapdragon C platform at Computex 2026 by opening up a few Windows utilities on a demo unit."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/dlss-4-5-ray-reconstruction-update-arrives-in-august-for-better-ray-tracing-visuals-broader-training-data-set-and-second-gen-transformer-architecture-combine-for-improved-image-quality",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 4.5 Ray Reconstruction update arrives in August for better ray tracing visuals — broader training data set and second-gen transformer architecture combine for improved image quality",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/dlss-4-5-ray-reconstruction-update-arrives-in-august-for-better-ray-tracing-visuals-broader-training-data-set-and-second-gen-transformer-architecture-combine-for-improved-image-quality",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T09:30:00+00:00",
    "summary": "At Computex 2026, Nvidia announced DLSS 4.5 Ray Reconstruction, an updated version of its neural RT denoiser with a second-gen transformer architecture and a broader training data set for better outpu"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-display-rounds-out-the-powerful-package",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft Surface Laptop Ultra weilds Nvidia's RTX Spark superchip with 128GB of RAM, 20 Arm CPU cores, and a Blackwell GPU — 15-inch mini-LED PixelSense Ultra display rounds out the powerful package",
    "url": "https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-display-rounds-out-the-powerful-package",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T09:00:00+00:00",
    "summary": "Powered by Nvidia's RTX Spark Superchip, the Surface Laptop Ultra features 20 Arm CPU cores, 6,144 CUDA cores, and up to 128GB of unified memory"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex 2026 — three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T05:55:07+00:00",
    "summary": "Along with its first-generation RTX Spark platform for desktop and laptop PCs, Nvidia CEO Jensen Huang revealed the company's commitment to future generations of those platforms on its future roadmaps"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex 2026 – new platform promises to turn Windows into an agentic AI OS with Arm CPU, Blackwell GPU, and 128GB unified memory",
    "url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:52:13+00:00",
    "summary": "At Computex 2026, Nvidia CEO Jensen Huang unveiled the RTX Spark Superchip, a new Arm laptop and desktop platform that powers agentic AI on Windows with a 20-core Arm CPU, powerful 6144-CUDA-core Blac"
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
    "id": "hn:47989883",
    "domain": "大厂 AI 动态",
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
    "id": "hn:48297467",
    "domain": "大厂 AI 动态",
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
    "id": "rss:https://www.theverge.com/gadgets/940794/first-nvidia-rtx-spark-laptops-roundup-computex-2026",
    "domain": "大厂 AI 动态",
    "title": "These are the first Nvidia RTX Spark laptops",
    "url": "https://www.theverge.com/gadgets/940794/first-nvidia-rtx-spark-laptops-roundup-computex-2026",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:29:52+00:00",
    "summary": "Nvidia has officially entered the world of consumer laptop chips with the RTX Spark, and several device makers already have hardware lined up for it. Microsoft, Asus, HP, MSI, Lenovo, and Dell are exp"
  },
  {
    "id": "rss:https://www.theverge.com/games/940722/asus-xbox-ally-x20-special-edition-oled-screen",
    "domain": "大厂 AI 动态",
    "title": "Asus just announced the OLED Xbox Ally X of my dreams",
    "url": "https://www.theverge.com/games/940722/asus-xbox-ally-x20-special-edition-oled-screen",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "If you asked me what I'd change about the Xbox Ally X handheld - aside from fixing Windows, I mean - I'd tell you two key things. First, give me a bigger, better screen. Even a little bit bigger, so g"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940584/microsoft-surface-laptop-ultra-nvidia-rtx-spark-pictures",
    "domain": "大厂 AI 动态",
    "title": "This is the Microsoft Surface Laptop Ultra with Nvidia RTX Spark",
    "url": "https://www.theverge.com/tech/940584/microsoft-surface-laptop-ultra-nvidia-rtx-spark-pictures",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:36:41+00:00",
    "summary": "Once upon a time, Microsoft had to write off $900 million betting an Arm-based Nvidia chip could power its first flagship Windows portable, the original Microsoft Surface. But today, it's trying again"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940524/amd-computex-am5-promise-2029-rx9070gre-7700x3d-5800x3d",
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
    "title": "Here’s your first look at ‘A Minecraft Movie Squared’ with Kirsten Dunst as Alex",
    "url": "https://www.theverge.com/entertainment/940523/minecraft-movie-squared-sequel-kirsten-dunst-alex",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T19:28:11+00:00",
    "summary": "The A Minecraft Movie sequel officially has a title: A Minecraft Movie Squared. What's more, we now know that Kirsten Dunst will star as Alex, the game's female character option, and that Matt Berry i"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/unastella-a-south-korean-rocket-startup-that-launched-from-home-raises-24m/",
    "domain": "大厂 AI 动态",
    "title": "Unastella, a South Korean rocket startup that launched from home, raises $24M",
    "url": "https://techcrunch.com/2026/06/01/unastella-a-south-korean-rocket-startup-that-launched-from-home-raises-24m/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "The Seoul-based rocket startup is developing its own launch vehicles and engines."
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/",
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
    "title": "TikTok’s road to becoming a super app",
    "url": "https://techcrunch.com/2026/05/30/tiktoks-road-to-becoming-a-super-app/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T13:00:00+00:00",
    "summary": "TikTok may be working to become the app that people use for most of their digital activities."
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
    "id": "rss:https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/",
    "domain": "大厂 AI 动态",
    "title": "An OpenAI model solved a famous math problem that stumped humans for 80 years",
    "url": "https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/",
    "source": "Kai Williams",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:00:00+00:00",
    "summary": "I tried to explain OpenAI’s solution more clearly than OpenAI did."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/05/on-its-40th-anniversary-we-reassess-1986s-spacecamp/",
    "domain": "大厂 AI 动态",
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
    "domain": "大厂 AI 动态",
    "title": "They call it stupid hot for a reason: Heat muddles animal brains",
    "url": "https://arstechnica.com/science/2026/05/they-call-it-stupid-hot-for-a-reason-heat-muddles-animal-brains/",
    "source": "Marta Zaraska",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T10:00:07+00:00",
    "summary": "As temperatures rise, some creatures pick fights while others struggle to learn."
  },
  {
    "id": "rss:https://www.producthunt.com/products/typeahead",
    "domain": "大厂 AI 动态",
    "title": "Typeahead",
    "url": "https://www.producthunt.com/products/typeahead",
    "source": "Hiten Shah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T23:47:44+00:00",
    "summary": "AI autocomplete for every app on your Mac Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/open-caffeine",
    "domain": "大厂 AI 动态",
    "title": "Open Caffeine",
    "url": "https://www.producthunt.com/products/open-caffeine",
    "source": "Hoon Choi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T03:48:12+00:00",
    "summary": "Keep your Mac awake Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/skylive",
    "domain": "大厂 AI 动态",
    "title": "Skylive",
    "url": "https://www.producthunt.com/products/skylive",
    "source": "Samuel Angel Gallo Ocampo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T23:30:09+00:00",
    "summary": "Never miss a celestial event, anywhere on Earth Discussion | Link"
  },
  {
    "id": "hn:48314363",
    "domain": "股票",
    "title": "Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions",
    "url": "https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/",
    "source": "ianrahman",
    "platform": "hackernews",
    "points": 234,
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
    "id": "hn:48343303",
    "domain": "股票",
    "title": "The SpaceX IPO is great for Elon Musk and terrible for you",
    "url": "https://www.theverge.com/ai-artificial-intelligence/940001/elon-musk-spacex-ipo-ai",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-05-31T05:34:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48281983",
    "domain": "股票",
    "title": "Show HN: A website that tracks every stock trade Congress makes",
    "url": "https://congress.kadoa.com/",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-05-26T16:28:56+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3773581",
    "domain": "股票",
    "title": "美团：下半年订单增长可能会放缓",
    "url": "https://wallstreetcn.com/articles/3773581",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:32:20+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3773578",
    "domain": "股票",
    "title": "高盛：空头大撤退！对冲基金以半年最快速度追涨美股",
    "url": "https://wallstreetcn.com/articles/3773578",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:17:05+00:00",
    "summary": "高盛报告显示，上周对冲基金对美股的净买入规模创六个月新高。衡量其风险偏好的关键指标多空净杠杆率已升至55.3%，处于近一年来的第89百分位，表明基金正以较高信心“上杠杆”做多。资金流向上，金融股获显著净买入，而工业股空头敞口已升至高位。"
  },
  {
    "id": "wscn:3773579",
    "domain": "股票",
    "title": "从“周期大宗商品”到“战略核心资产”，摩根大通：本轮存储超级周期将“更高、更长”",
    "url": "https://wallstreetcn.com/articles/3773579",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:16:17+00:00",
    "summary": "摩根大通大幅上调全球存储市场预期，预计2028年市场规模将达1.7万亿美元。AI需求正从GPU向CPU全面扩散，推动服务器内存需求超预期增长，HBM供需缺口有望持续至2028年。随着存储在云厂商资本开支中的占比突破50%，行业正从周期性商品转变为AI基础设施核心资产。"
  },
  {
    "id": "wscn:3773576",
    "domain": "股票",
    "title": "MLCC 会成为下一个存储吗？",
    "url": "https://wallstreetcn.com/articles/3773576",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:14:50+00:00",
    "summary": "华泰证券表示，英伟达Rubin架构驱动AI服务器MLCC量价齐升，单机柜价值量跃升至2.2万-4万美元，村田等龙头已提价15%-35%。供需格局类似HBM，但MLCC资本壁垒远低于存储，中长期供给存风险。当前板块PE达43.3倍，溢价充分，后续需紧盯盈利兑现，AI高容龙头、通用品份额较高的厂商、以及A股高容/电感国产化进程三条主线。"
  },
  {
    "id": "wscn:3773577",
    "domain": "股票",
    "title": "一家中小跨境电商的AI拼连接样本",
    "url": "https://wallstreetcn.com/articles/3773577",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:14:00+00:00",
    "summary": "AI开始接管脏活累活。"
  },
  {
    "id": "wscn:3773575",
    "domain": "股票",
    "title": "老黄的Token经济学翻车了！微软亚马逊通通跳车",
    "url": "https://wallstreetcn.com/articles/3773575",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:13:29+00:00",
    "summary": "企业AI支出正从狂热转向理性。一家神秘公司月耗5亿美元Claude账单，亚马逊则因员工为冲榜滥用AI而取消内部工具排行榜。微软收缩Claude Code授权，Uber四个月烧光全年预算。黄仁勋“多用Token即省钱”的Token经济学，正被一张张巨额账单和低ROI的现实挑战。"
  },
  {
    "id": "wscn:3773580",
    "domain": "股票",
    "title": "延续小阳春热度！5月上海二手房成交超2.8万套，刷新6年来同期新高",
    "url": "https://wallstreetcn.com/articles/3773580",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T11:09:15+00:00",
    "summary": "业内分析人士认为，二手房市场开始从“以价换量”模式进入“量价齐稳”的新阶段；新房市场伴随供应回暖，置换链条也越来越顺畅，市场普遍看好房企半年度业绩冲刺带来的成交行情。"
  },
  {
    "id": "wscn:3773570",
    "domain": "股票",
    "title": "黄仁勋的“Agent工厂”里，装了什么新故事？",
    "url": "https://wallstreetcn.com/articles/3773570",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T09:35:03+00:00",
    "summary": "黄仁勋把叙事重心从“芯片全家桶”转向了“Agent工厂”。随着Vera Rubin量产及DGX Station、DSX等发布，英伟达正围绕智能体重构从芯片、模型到人形机器人的完整技术体系。"
  },
  {
    "id": "wscn:3773571",
    "domain": "股票",
    "title": "美团Q1营收同比增5.6%超预期，环比大幅减亏超百亿｜财报见闻",
    "url": "https://wallstreetcn.com/articles/3773571",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T09:21:03+00:00",
    "summary": "美团2026年Q1营收910亿元，经调整净亏损49.7亿元，25年Q4为亏损151亿元。受竞争加剧影响，核心本地商业由盈转亏，营销开支激增51.1%至230亿元。新业务收入增21.3%，亏损收窄。AI投入加码，战略转向生态价值对冲补贴战，环比修复信号显现。"
  },
  {
    "id": "wscn:3773574",
    "domain": "股票",
    "title": "6名中金分析师变身Skill  券商AI竞争再加速",
    "url": "https://wallstreetcn.com/articles/3773574",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T09:19:29+00:00",
    "summary": "6月1日，中金点睛宣布新增上线6位分析师Skill，并在Agent模式中开放调用；\n用户完成注册后，..."
  },
  {
    "id": "wscn:3773573",
    "domain": "股票",
    "title": "73天极速！宇树科技IPO过会，A股具身智能第一股呼之欲出！",
    "url": "https://wallstreetcn.com/articles/3773573",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T09:15:06+00:00",
    "summary": "按发行比例不低于10%测算，公司整体估值至少达420亿元，业内普遍预期实际市值将远高于此。"
  },
  {
    "id": "wscn:3773569",
    "domain": "股票",
    "title": "黄仁勋的棋局：AI算力的每一条路，都有英伟达在等候",
    "url": "https://wallstreetcn.com/articles/3773569",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T08:41:33+00:00",
    "summary": "黄仁勋在中国台北宣布两件事：CUDA首次塞进笔记本，万亿参数推理搬上企业桌面。这不是英伟达在抢云厂商生意，而是把收费口从一个扩成三个——数据中心、背包、桌边，无论AI跑在哪里，英伟达都守在路口等着收钱。"
  },
  {
    "id": "wscn:3773572",
    "domain": "股票",
    "title": "英伟达亮出三张“新王牌”",
    "url": "https://wallstreetcn.com/articles/3773572",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T08:39:24+00:00",
    "summary": "英伟达在GTC大会上推出三项重大更新：旗舰AI平台Vera Rubin正式量产，打破延期传闻；推出专为代理式AI设计的Vera CPU，使CPU与GPU销售价值比趋近1:1，直接挑战英特尔与AMD；联合微软发布基于ARM架构的消费级AI PC芯片RTX Spark。花旗视此为积极信号，维持买入评级与300美元目标价。"
  },
  {
    "id": "wscn:3773543",
    "domain": "股票",
    "title": "创业板跌超2%，AI PC、AI应用逆势活跃，算力硬件齐跌，恒科指涨超1%，科网股普涨",
    "url": "https://wallstreetcn.com/articles/3773543",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T08:39:20+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3700股飘红，今日成交2.89万亿。沪深两市成交额2.88万亿，较上一个交易日缩量超4400亿。板块方面，半导体、算力硬件产业链深度回调，GPU、CPO、PCB方向领跌，光刻机、光纤方向跌幅靠前；稀土、商业航天、创新药概念股走弱。煤炭、电力、传媒板块走强，AI PC、AI应用题材活跃。"
  },
  {
    "id": "wscn:3773350",
    "domain": "股票",
    "title": "硅基通胀与碳基崩溃：一头灰犀牛正在被养成",
    "url": "https://wallstreetcn.com/premium/articles/3773350?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T08:16:56+00:00",
    "summary": "当灰犀牛冲进交易大厅的时候，市场是否已经做好了准备？"
  },
  {
    "id": "wscn:3773568",
    "domain": "股票",
    "title": "英特尔押注玻璃基板：印度33亿美元建厂，年产能7万片",
    "url": "https://wallstreetcn.com/articles/3773568",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T08:15:56+00:00",
    "summary": "英特尔联手3DGS豪掷33亿美元，在印度奥里萨邦布局玻璃基板工厂，年产能预计达7万片。与此同时，新墨西哥州量产基地亦在筹备中，两地并行提速商业化进程。台积电、三星、SKC同台竞技，玻璃基板正从实验室走向规模化战场，下一代AI芯片封装的材料革命悄然加速。"
  },
  {
    "id": "wscn:3773558",
    "domain": "股票",
    "title": "创历史新高！韩国5月芯片出口372亿美元",
    "url": "https://wallstreetcn.com/articles/3773558",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T08:09:33+00:00",
    "summary": "AI芯片需求引爆韩国出口狂潮：5月出口额同比飙升53.2%至875亿美元，创1984年以来最快增速，芯片单月出口首破370亿美元、同比近乎翻三倍，连续三月站稳300亿美元关口。三星、SK Hynix坐享AI基建红利，分析师预计这一强劲势头将贯穿全年。"
  },
  {
    "id": "wscn:3773564",
    "domain": "股票",
    "title": "伊朗战争意外加速全球LNG产能扩张，供应过剩不远了？",
    "url": "https://wallstreetcn.com/articles/3773564",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T08:08:40+00:00",
    "summary": "霍尔木兹海峡封锁使全球LNG供应骤减两成、3月亚洲基准价飙升至30美元。但分析指出，因亚洲买家正转往域外寻求能源安全，恐引发北美等地的项目建设热潮；叠加买方转向太阳能和煤炭，中长期反将加速LNG第三波更大规模、更持久的供应过剩。"
  },
  {
    "id": "wscn:3773537",
    "domain": "股票",
    "title": "AI热情主导市场，英伟达盘前涨超2%，软件股大涨，美光股价站上1000美元，油价攀升",
    "url": "https://wallstreetcn.com/articles/3773537",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T08:07:28+00:00",
    "summary": "美股盘前存储芯片股走高，美光科技涨超3%，闪迪涨超2%。Arm美股盘前涨超8%。英伟达美股盘前涨超2%。布伦特原油涨破每桶93美元，基准10年期美国国债收益率上涨3个基点至4.47%，美元时隔三个交易日首度走强，黄金下跌0.4%至每盎司约4520美元。"
  },
  {
    "id": "wscn:3773559",
    "domain": "股票",
    "title": "本轮“抱团”行情是否松动？",
    "url": "https://wallstreetcn.com/articles/3773559",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T07:46:36+00:00",
    "summary": "5月最后一周，A股风格悄然生变：科技抱团松动，消费白马、地产、煤电集体反弹。成交额前5%个股占全市场近50%，创2021年以来最高；沪深300逾七成成分股跑输指数。中泰证券判断，6月指数仍有冲高可能，却是典型\"鱼尾行情\"：空间越来越小，赚钱效应越来越差。历史上，极致抱团后的低位补涨，往往不是主升中段，而是行情末端的最后一棒。"
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
    "id": "hn:48270880",
    "domain": "股票",
    "title": "SpaceX's IPO Filing Shows Elon's Twitter 'Business Genius' Was a Fantasy",
    "url": "https://www.techdirt.com/2026/05/22/spacexs-ipo-filing-shows-elons-twitter-business-genius-was-a-fantasy/",
    "source": "velik_m",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-05-25T19:50:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48304589",
    "domain": "股票",
    "title": "SpaceX IPO: Did Musk Rig the Stock Market? [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-05-28T04:42:25+00:00",
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
    "id": "hn:48242934",
    "domain": "股票",
    "title": "Cheap AI Could Derail OpenAI and Anthropic's IPOs",
    "url": "https://www.cnbc.com/2026/05/20/cheap-ai-could-derail-openai-and-anthropics-ipos.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-05-22T23:37:17+00:00",
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
    "id": "hn:48046818",
    "domain": "股票",
    "title": "SpaceX IPO gives Musk power and curbs shareholder rights",
    "url": "https://www.reuters.com/sustainability/boards-policy-regulation/spacex-ipo-gives-musk-sweeping-power-curbs-shareholder-rights-2026-05-06/",
    "source": "denis1",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-05-07T08:17:33+00:00",
    "summary": ""
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
    "id": "hn:48198551",
    "domain": "金融",
    "title": "Tesla's lithium refinery discharges 231,000 gallons of polluted wastewater a day",
    "url": "https://www.autonocion.com/us/tesla-lithium-refinery-texas/",
    "source": "atombender",
    "platform": "hackernews",
    "points": 498,
    "published_at": "2026-05-19T19:52:49+00:00",
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
    "id": "hn:48349067",
    "domain": "金融",
    "title": "Nearly Half of Home Insurance Claims Result in Zero Payout",
    "url": "https://www.wsj.com/finance/the-home-insurance-coin-flip-nearly-half-of-claims-result-in-zero-payout-4b49acaf",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 21,
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
    "id": "hn:47987931",
    "domain": "金融",
    "title": "Modern C++ Programming: Busato",
    "url": "https://github.com/federico-busato/Modern-CPP-Programming",
    "source": "KnuthIsGod",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-05-02T16:40:29+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30363",
    "domain": "金融",
    "title": "Enhancing Regime Shift Detection Using Unstructured Data: A Study on the Treasury Market",
    "url": "https://arxiv.org/abs/2605.30363",
    "source": "Mingxuan Yi, Vidal Mehra, Jing Chen, John Cartlidge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30363v1 Announce Type: new Abstract: Regime shifts in financial markets reorganise the joint dynamics of asset prices and macro variables, breaking any single-regime calibration. They are n"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30435",
    "domain": "金融",
    "title": "Global Science Sustains U.S. Innovation",
    "url": "https://arxiv.org/abs/2605.30435",
    "source": "Christopher R. Esposito",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30435v1 Announce Type: new Abstract: Like physical products, new technologies are developed using globally sourced inputs. Yet while the supply chains behind physical goods are well underst"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30464",
    "domain": "金融",
    "title": "Distributional Portfolio Optimization (DPO): A Unified Framework for Distributions over Weights, Returns, and Parameters",
    "url": "https://arxiv.org/abs/2605.30464",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30464v1 Announce Type: new Abstract: Classical portfolio optimization treats expected returns, covariances, and allocations as deterministic. Modern practice replaces at least one by a dist"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30562",
    "domain": "金融",
    "title": "Option Pricing under Stochastic Volatility and Jumps:A PIDE Framework with Empirical Evidence",
    "url": "https://arxiv.org/abs/2605.30562",
    "source": "Abigail Anokyewaa Mensah, Ayush Jha, Hongwei Mei, Rui Wang, Svetlozar T. Rachev, Frank J. Fabozzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30562v1 Announce Type: new Abstract: We develop a partial integro-differential equation (PIDE) framework for option pricing under joint stochastic volatility and jump dynamics, and evaluate"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30567",
    "domain": "金融",
    "title": "Valuation of GLWB-LTC Annuities with L\\'evy Equity Dynamics, Stochastic Interest Rates and Health-State Transitions",
    "url": "https://arxiv.org/abs/2605.30567",
    "source": "Andrea Molent",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30567v1 Announce Type: new Abstract: This paper develops a valuation framework for guaranteed lifetime withdrawal benefit (GLWB) contracts with long-term care (LTC) features when the refere"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30643",
    "domain": "金融",
    "title": "Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making",
    "url": "https://arxiv.org/abs/2605.30643",
    "source": "Bouna Niang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30643v1 Announce Type: new Abstract: Hit ratio is a common service metric for electronic corporate bond market making, but raw hit-ratio targets can be economically misleading when client f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30672",
    "domain": "金融",
    "title": "Residual Supply and the Price of Risk Absorption",
    "url": "https://arxiv.org/abs/2605.30672",
    "source": "Ziyao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30672v1 Announce Type: new Abstract: When redeeming open-end funds sell and natural buyers do not step in at once, some limited-capital investor must take the other side and carry the inven"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30683",
    "domain": "金融",
    "title": "Towards an Ideometrics-Based General Theory of Human Progress",
    "url": "https://arxiv.org/abs/2605.30683",
    "source": "Igor Rudan, Steven Kerr",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30683v1 Announce Type: new Abstract: This paper proposes ideometrics as the foundation for a generalised and potentially testable theory of human progress and civilisational progress, thus "
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30943",
    "domain": "金融",
    "title": "Inspectable Neural Markov Models for Non-Stationary Time Series",
    "url": "https://arxiv.org/abs/2605.30943",
    "source": "Jan Rovirosa, Jesse Schmolze",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30943v1 Announce Type: new Abstract: Modeling non-stationary stochastic systems requires balancing the representational capacity of deep learning with the structural transparency of classic"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30442",
    "domain": "金融",
    "title": "When market boundaries weaken: Network reconfiguration and regime-dependent cross-asset spillovers",
    "url": "https://arxiv.org/abs/2605.30442",
    "source": "Ruixue Jing, Luis Enrique Correa Rocha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30442v1 Announce Type: cross Abstract: Cryptocurrencies are increasingly adopted as investment assets, making their interactions with traditional financial markets central to cross-asset di"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30720",
    "domain": "金融",
    "title": "Kalimati Vegetable Price Index Forecasting with a Momentum Corrected Online Stacking Ensemble",
    "url": "https://arxiv.org/abs/2605.30720",
    "source": "Sahaj Raj Malla",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30720v1 Announce Type: cross Abstract: Forecasting agricultural commodity prices in emerging economies is difficult due to high volatility, frequent supply disruptions, and strong cultural "
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.08503",
    "domain": "金融",
    "title": "Optimal Contract Design with Quadratic Effort Cost",
    "url": "https://arxiv.org/abs/2503.08503",
    "source": "Xinfu Chen, Shuaijie Qian, Guan Qiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2503.08503v3 Announce Type: replace Abstract: The existence of an optimal contract of the principal-agent problem is a central issue in contract design. According to Cvitani\\'c et al. [2], such "
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.20429",
    "domain": "金融",
    "title": "Estimating the housing production function with unobserved land heterogeneity",
    "url": "https://arxiv.org/abs/2504.20429",
    "source": "Yusuke Adachi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2504.20429v3 Announce Type: replace Abstract: Housing supply in dense cities depends on the ability of builders to substitute capital for scarce land. This margin is difficult to estimate becaus"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.04545",
    "domain": "金融",
    "title": "Measuring Social Media Network Effects",
    "url": "https://arxiv.org/abs/2507.04545",
    "source": "Sinan Aral, Seth G Benzell, Avinash Collis, Christos Nicolaides",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2507.04545v2 Announce Type: replace Abstract: Network effects -- the utility gains from additional consumers of a good -- are widely regarded as critical to the digital economy. Yet recent theor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.15617",
    "domain": "金融",
    "title": "Price Pass-Through of Austria's Single-Use Plastics Producer Charges: Evidence from Retail Offer Spells",
    "url": "https://arxiv.org/abs/2510.15617",
    "source": "Felix Reichel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2510.15617v4 Announce Type: replace Abstract: Single use plastics (SUPs) impose substantial environmental costs. Following Directive (EU) 2019/904, Austria introduced producer charges and mandat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.14150",
    "domain": "金融",
    "title": "Trade relationships during and after a crisis",
    "url": "https://arxiv.org/abs/2601.14150",
    "source": "Alejandra Martinez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2601.14150v3 Announce Type: replace Abstract: This paper provides causal evidence that temporary supply disruptions reshape firms' relationship portfolios in international trade. Using exogenous"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.29317",
    "domain": "金融",
    "title": "Should I State or Should I Show? Aligning AI with Human Preferences",
    "url": "https://arxiv.org/abs/2603.29317",
    "source": "Keaton Ellis, Wanying Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2603.29317v2 Announce Type: replace Abstract: As AI agents become more autonomous, properly aligning their objectives with human preferences becomes increasingly important. We study how effectiv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.20636",
    "domain": "金融",
    "title": "Continuous Timing Signals for Growth-Defensive Style Allocation: Factor Attribution, Risk Matching, and Out-of-Sample Evidence",
    "url": "https://arxiv.org/abs/2605.20636",
    "source": "Zheli Xiong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.20636v2 Announce Type: replace Abstract: This paper studies conditional allocation between a growth/technology ETF basket, denoted by $G$, and a defensive income/value-oriented ETF basket, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.13323",
    "domain": "金融",
    "title": "AI Behavioral Science",
    "url": "https://arxiv.org/abs/2509.13323",
    "source": "Matthew O. Jackson, Qiaozhu Me, Stephanie W. Wang, Yutong Xie, Walter Yuan, Seth Benzell, Erik Brynjolfsson, Colin F. Camerer, James Evans, Brian Jabarian, Jon Kleinberg, Juanjuan Meng, Sendhil Mullainathan, Asuman Ozdaglar, Thomas Pfeiffer, Moshe Tennenholtz, Robb Willer, Diyi Yang, Teng Ye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2509.13323v2 Announce Type: replace-cross Abstract: We outline a foundation for a new field of ``AI Behavioral Science,'' covering three perspectives. First, as AI becomes ubiquitous and is incr"
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
    "id": "hn:47992303",
    "domain": "金融",
    "title": "Wyoming celebrates 'nuclear Renaissance' as feds approve license for a reactor",
    "url": "https://text.npr.org/nx-s1-5798892",
    "source": "mooreds",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-05-03T01:18:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48004992",
    "domain": "金融",
    "title": "Feds Fine Durham Energy Efficiency Co $722M",
    "url": "https://www.theassemblync.com/news/business/american-efficient-ferc-durham-fine/",
    "source": "ChuckMcM",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-05-04T05:32:21+00:00",
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
  }
]
```
