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

- 今日日期：`2026-07-01`
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
  "date": "2026-07-01",
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
    "points": 1381483,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 940082,
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
    "points": 812488,
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
    "points": 669166,
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
    "points": 665153,
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
    "points": 496982,
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
    "points": 473675,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1ngJH6yEKH",
    "domain": "AI",
    "title": "会说话就能搭 Agent 工作流？feat.一人公司如何用 WorkBuddy 提升效率",
    "url": "http://www.bilibili.com/video/av116741590031138",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 444062,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "#WorkBuddy #腾讯 #AI\n#Agent工作流 #人工智能 #效率提升 #一人公司 #黑科技\n#AI工作流"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 383720,
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
    "points": 378066,
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
    "points": 286812,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 250375,
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
    "points": 247112,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 179069,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175904,
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
    "points": 161771,
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
    "points": 160070,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1CDVu6TEnv",
    "domain": "AI",
    "title": "Vibe coding成瘾。一开始觉得很兴奋，但是玩多了就有一种游戏开挂的感觉。像这个小demo古法编程怎么也要写两天，AI来写15分钟搞定了，一开始挺期待的…",
    "url": "http://www.bilibili.com/video/av116661831208897",
    "source": "工科男孙老师",
    "platform": "bilibili",
    "points": 138878,
    "published_at": "2026-05-30T05:23:02+00:00",
    "summary": "Vibe coding成瘾。一开始觉得很兴奋，但是玩多了就有一种游戏开挂的感觉。像这个小demo古法编程怎么也要写两天，AI来写15分钟搞定了，一开始挺期待的，过去没时间玩的东西现在都能很快搞定，但是做完毫无快感。就像是上班后买了大学时心心念念的psp游戏机，但是再也没有借同学的那种快感了。"
  },
  {
    "id": "bvid:BV1SY7C6nEwU",
    "domain": "AI",
    "title": "【开源】我制作了一个vibe coding键盘",
    "url": "http://www.bilibili.com/video/av116696660576856",
    "source": "工科男孙老师",
    "platform": "bilibili",
    "points": 121184,
    "published_at": "2026-06-05T10:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 111054,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 105572,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99484,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1NCEB6AExH",
    "domain": "AI",
    "title": "Claude Fable 5强得离谱 单条提示词生成三款游戏 - tef",
    "url": "http://www.bilibili.com/video/av116732630932080",
    "source": "黑纹白斑马",
    "platform": "bilibili",
    "points": 99205,
    "published_at": "2026-06-11T17:27:51+00:00",
    "summary": "原视频：Claude Fable 5 is INSANE.\n原作者：tef\n发布日期：2026-06-11\n视频链接：https://www.youtube.com/watch?v=0DVUjpClqgI\n\n✨ 想看英文原声？请关注 @英文白斑马\n\n00:00 视频开篇与测试介绍\nup主介绍新发布的Claude Fable 5宣称可通过单条提示词生成游戏，本次视频将测试其生成三款知名游戏的能力。\n"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92317,
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
    "points": 73460,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oTkuBoEW5",
    "domain": "AI",
    "title": "业余程序员才Vibe Coding",
    "url": "http://www.bilibili.com/video/av115921586751411",
    "source": "晓舟报告",
    "platform": "bilibili",
    "points": 72432,
    "published_at": "2026-01-21T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 61589,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 58982,
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
    "points": 57019,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52619,
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
    "points": 47288,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 44714,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 40862,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1FzfoYSE4f",
    "domain": "AI",
    "title": "影刀AI Power零基础教程：02 智能体——打造企业AI超级员工",
    "url": "http://www.bilibili.com/video/av113888003622214",
    "source": "影刀RPA",
    "platform": "bilibili",
    "points": 40534,
    "published_at": "2025-02-06T02:00:00+00:00",
    "summary": "AI智能体：场景化智能助手，打造企业AI超级员工\n影刀AI Power，帮助企业将AI用起来。让每个员工都能拥有AI能力，在工作中使用AI解决问题。\n\n影刀AP企业版免费试用申请：http://s.winrobot360.com/g02tp\n影刀AP社区版使用：https://www.yingdao.com/ai-power/"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29848,
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
    "points": 28694,
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
    "points": 27950,
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
    "points": 27578,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 24585,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22579,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "domain": "AI",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "platform": "bilibili",
    "points": 20615,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17456,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 16836,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 14516,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 13703,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "小狗瑞恩Ryan",
    "platform": "bilibili",
    "points": 12437,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1rkLf6kEhf",
    "domain": "AI",
    "title": "为什么Vibe coding尽可能用原生Claude code和codex？",
    "url": "http://www.bilibili.com/video/av116768953604774",
    "source": "像素范",
    "platform": "bilibili",
    "points": 11641,
    "published_at": "2026-06-18T03:24:21+00:00",
    "summary": "AI性能真相：模型只差5%，harness能差30%，所以尽量还是试试目前比较前沿，有自己独立harness的模型。"
  },
  {
    "id": "bvid:BV1TtwCehEzG",
    "domain": "AI",
    "title": "cursor新手必会的怎么回退代码 防止改错改乱代码 提高效率开发",
    "url": "http://www.bilibili.com/video/av113855472605087",
    "source": "项目禅",
    "platform": "bilibili",
    "points": 11240,
    "published_at": "2025-01-19T14:29:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 11090,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10605,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
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
    "id": "rss:https://www.eetimes.com/u-s-eyes-china-expanding-role-in-latin-america/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Eyes China’s Expanding Role in Latin America",
    "url": "https://www.eetimes.com/u-s-eyes-china-expanding-role-in-latin-america/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T21:00:00+00:00",
    "summary": "As U.S. regulators focus on supply chain transparency, China's expanding presence in Latin America has emerged as a major strategic challenge. The post U.S. Eyes China&#8217;s Expanding Role in Latin "
  },
  {
    "id": "rss:https://www.eetimes.com/panel-with-arteris-gf-tenstorrent-risc-v-ecosystem-growth-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Panel with Arteris, GlobalFoundries, Tenstorrent: RISC-V Ecosystem Growth for Physical AI",
    "url": "https://www.eetimes.com/panel-with-arteris-gf-tenstorrent-risc-v-ecosystem-growth-for-physical-ai/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:53:48+00:00",
    "summary": "RISC-V heavyweights tackle physical AI, edge autonomy, and TOPS-per-watt—watch how robots chase their killer app. The post Panel with Arteris, GlobalFoundries, Tenstorrent: RISC-V Ecosystem Growth for"
  },
  {
    "id": "rss:https://www.eetimes.com/europes-path-to-defense-resilience-lies-in-technological-independence/",
    "domain": "AI 算力 / 半导体",
    "title": "Europe’s Path to Defense Resilience Lies in Technological Independence",
    "url": "https://www.eetimes.com/europes-path-to-defense-resilience-lies-in-technological-independence/",
    "source": "Florian Pivit",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T12:34:57+00:00",
    "summary": "If Europe wants true defense resilience, it must reduce its dependence on big foreign tech ecosystems. The post Europe’s Path to Defense Resilience Lies in Technological Independence appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/satvu-targets-industrial-intelligence-with-thermal-imaging/",
    "domain": "AI 算力 / 半导体",
    "title": "SatVu Targets Industrial Intelligence with Thermal Imaging",
    "url": "https://www.eetimes.com/satvu-targets-industrial-intelligence-with-thermal-imaging/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:20:00+00:00",
    "summary": "With HotSat-2 in orbit and fresh funding, U.K. startup SatVu is demonstrating how high-resolution thermal satellite data can reveal real-world industrial activity. The post SatVu Targets Industrial In"
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/xtool-says-its-01-omni-printer-can-print-it-all-firm-steps-into-the-world-of-uv-printing-for-output-on-all-surfaces-at-up-to-5mm-thick",
    "domain": "AI 算力 / 半导体",
    "title": "xTool says its 01 Omni Printer can ‘print it all’ — firm steps into the world of UV printing for output on 'all surfaces' at up to 5mm thick",
    "url": "https://www.tomshardware.com/maker-stem/xtool-says-its-01-omni-printer-can-print-it-all-firm-steps-into-the-world-of-uv-printing-for-output-on-all-surfaces-at-up-to-5mm-thick",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T19:45:55+00:00",
    "summary": "xTool launched its 01 Omni Printer today at a special event in Berlin. The digital-to-physical tool firm claims this device is the “world’s first 4-in-1 printer,” and said it was ready for makers to “"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-confirms-low-power-cpu-cores-in-linux-kernel-patch-zen-6-chips-could-follow-in-intels-footsteps-with-new-core-type-for-background-tasks",
    "domain": "AI 算力 / 半导体",
    "title": "AMD confirms low-power CPU cores in Linux kernel patch — Zen 6 chips could follow in Intel's footsteps with new core type for background tasks",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-confirms-low-power-cpu-cores-in-linux-kernel-patch-zen-6-chips-could-follow-in-intels-footsteps-with-new-core-type-for-background-tasks",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:50:50+00:00",
    "summary": "AMD confirms plans to incorporate low-power CPU cores into next-generation heterogeneous CPUs to lower power consumption and improve energy efficiency."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/microsofts-flagship-windows-pc-lineup-will-drop-reportedly-drop-budget-options-firm-prunes-surface-go-and-surface-laptop-go",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft's flagship Windows PC lineup will drop reportedly drop budget options — firm prunes Surface Go and Surface Laptop Go",
    "url": "https://www.tomshardware.com/laptops/microsofts-flagship-windows-pc-lineup-will-drop-reportedly-drop-budget-options-firm-prunes-surface-go-and-surface-laptop-go",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:41:31+00:00",
    "summary": "Microsoft is further pruning its Surface line, with the Surface Laptop Go 3 and Surface Go 4 going out of stock without clear follow-ups."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/windows-defender-bluehammer-vulnerability-now-exploited-as-part-of-malware-campaigns-cisa-issues-warning-despite-patch-release-on-april-14",
    "domain": "AI 算力 / 半导体",
    "title": "Windows Defender 'BlueHammer' vulnerability now exploited as part of malware campaigns — CISA issues warning despite patch release on April 14",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/windows-defender-bluehammer-vulnerability-now-exploited-as-part-of-malware-campaigns-cisa-issues-warning-despite-patch-release-on-april-14",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:20:59+00:00",
    "summary": "Windows Defender \"BlueHammer\" vulnerability now exploited as part of malware campaigns — event demonstrates lack of security awareness despite existence of patches"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/meta-releases-version-two-of-its-brain-computer-interface-that-can-turn-thoughts-into-keypresses-non-invasive-magnetoencephalography-scanner-can-measure-changes-in-brain-activity",
    "domain": "AI 算力 / 半导体",
    "title": "Meta releases version two of its brain-computer interface that can turn thoughts into keypresses — non-invasive magnetoencephalography scanner can measure changes in brain activity",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/meta-releases-version-two-of-its-brain-computer-interface-that-can-turn-thoughts-into-keypresses-non-invasive-magnetoencephalography-scanner-can-measure-changes-in-brain-activity",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T13:34:35+00:00",
    "summary": "Meta just released the second version of its Brain2Qwerty non-invasive BCI, showing promising improvements that could lead to clinical trials. This system aims to build an interface that does not requ"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu-in-favor-of-dual-gpu-design-report-claims-complex-design-purportedly-scrapped-over-manufacturing-execution-concerns",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly cancels quad-die Rubin Ultra GPU in favor of dual-GPU design, report claims — complex design purportedly scrapped over 'manufacturing execution concerns'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu-in-favor-of-dual-gpu-design-report-claims-complex-design-purportedly-scrapped-over-manufacturing-execution-concerns",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T12:45:00+00:00",
    "summary": "Nvidia reportedly abandons quad-dire Rubin Ultra GPUs in favor of dual-die Rubin Ultra due to 'manufacturing execution concerns.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-free-glm-5-2-tops-the-open-weight-ai-rankings-on-all-huawei-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese Z.ai's latest model tops AI ranking charts amid Anthropic Fable 5 ban — blacklisted China firm's popular open-weight GLM-5.2 AI model powered by Huawei silicon",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-free-glm-5-2-tops-the-open-weight-ai-rankings-on-all-huawei-silicon",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:58:10+00:00",
    "summary": "Within a week of Fable's ban, GLM-5.2 had climbed to the top of the openly available leaderboards."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-epic-razer-wolverine-v3-controller-for-a-record-low-amazon-price-now-just-usd64-99-big-46-percent-saving-on-this-esports-friendly-gamepad-for-your-pc-or-console-with-next-gen-tmr-thumbsticks-and-an-ultra-fast-8-000hz-polling-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this epic Razer Wolverine V3 controller for a record-low Amazon price, now just $64.99 — big 46% saving on this esports-friendly gamepad for your PC or console with next-gen TMR thumbsticks and a",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-epic-razer-wolverine-v3-controller-for-a-record-low-amazon-price-now-just-usd64-99-big-46-percent-saving-on-this-esports-friendly-gamepad-for-your-pc-or-console-with-next-gen-tmr-thumbsticks-and-an-ultra-fast-8-000hz-polling-rate",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:34:05+00:00",
    "summary": "This esports pro-friendly Razer Wolverine V3 Tournament Edition controller is on sale for a record low Amazon Price, now just $64.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-raids-super-micro-and-two-supply-chain-partners-in-widening-nvidia-smuggling-probe",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan raids Supermicro and two supply-chain partners in widening Nvidia smuggling probe — nine sites hit as six people summoned for questioning",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-raids-super-micro-and-two-supply-chain-partners-in-widening-nvidia-smuggling-probe",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:18:43+00:00",
    "summary": "Taiwan officials raided Supermicro Computer's Taiwan office on Monday, alongside the homes of six individuals and three affiliated company sites"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/cargo-thieves-target-ai-data-center-supplies-in-usd1-3-million-heists-usd300-000-worth-of-copper-wire-and-usd1-million-worth-of-equipment-recovered-outside-chicago",
    "domain": "AI 算力 / 半导体",
    "title": "Cargo thieves target AI data center supplies in $1.3 million heists — $300,000 worth of copper wire and $1 million worth of equipment recovered outside Chicago",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/cargo-thieves-target-ai-data-center-supplies-in-usd1-3-million-heists-usd300-000-worth-of-copper-wire-and-usd1-million-worth-of-equipment-recovered-outside-chicago",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:06:17+00:00",
    "summary": "Authorities recover $1.3 million worth of data center supplies and equipment in a truck stop near Chicago. Equipment like this is a prime target for theft rings given its high value, but it's also lik"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/meta-fights-soaring-hardware-costs-by-reusing-old-ddr4-server-memory-in-new-ddr5-only-servers-custom-cxl-2-0-chip-marries-legacy-ddr4-2400-with-cutting-edge-ddr5-6400",
    "domain": "AI 算力 / 半导体",
    "title": "Meta fights soaring hardware costs by reusing old DDR4 server memory in new DDR5-only servers — custom CXL 2.0 chip marries legacy DDR4-2400 with cutting-edge DDR5-6400",
    "url": "https://www.tomshardware.com/pc-components/dram/meta-fights-soaring-hardware-costs-by-reusing-old-ddr4-server-memory-in-new-ddr5-only-servers-custom-cxl-2-0-chip-marries-legacy-ddr4-2400-with-cutting-edge-ddr5-6400",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:00:00+00:00",
    "summary": "Meta develops its custom Vistara CXL memory expander to use DDR4 memory with new servers running AMD EPYC 'Turin' processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsungs-9100-pro-ssd-1tb-is-still-available-at-its-prime-day-price-thanks-to-39-percent-discount-cheaper-and-faster-than-the-990-pro-and-the-lowest-price-weve-seen-in-months",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's 9100 Pro SSD 1TB is still available at its excellent Prime Day price thanks to 39% discount — cheaper and faster than the 990 Pro and the lowest price we've seen in months",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsungs-9100-pro-ssd-1tb-is-still-available-at-its-prime-day-price-thanks-to-39-percent-discount-cheaper-and-faster-than-the-990-pro-and-the-lowest-price-weve-seen-in-months",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T10:30:02+00:00",
    "summary": "The Samsung 9100 Pro SSD is still sporting its Prime Day price. Grab one at this low price while you can."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/hamsteros-jams-a-32-bit-gui-operating-system-in-a-1-44-mb-single-floppy-for-386-era-hardware-retro-os-should-make-for-easy-living-with-dos-machines-and-software",
    "domain": "AI 算力 / 半导体",
    "title": "HamsterOS jams a 32-bit GUI operating system in a single 1.44 MB floppy disk — retro OS for 386-era hardware should make for easy living with DOS machines and software",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/hamsteros-jams-a-32-bit-gui-operating-system-in-a-1-44-mb-single-floppy-for-386-era-hardware-retro-os-should-make-for-easy-living-with-dos-machines-and-software",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T10:30:00+00:00",
    "summary": "HamsterOS fits on just a single 1.44 MB floppy disk, and it's set for a full release this November."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/maker-kicks-off-oomwoo-an-open-source-robot-vacuum-you-can-3d-print-and-build-yourself",
    "domain": "AI 算力 / 半导体",
    "title": "Oomwoo is a new open-source robot vacuum you can 3D print yourself, sidesteps cloud security risks by running fully offline — project combines Raspberry Pi, 2D LiDAR, and a 3D-printed chassis",
    "url": "https://www.tomshardware.com/3d-printing/maker-kicks-off-oomwoo-an-open-source-robot-vacuum-you-can-3d-print-and-build-yourself",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T10:00:00+00:00",
    "summary": "Maker's Pet has launched oomwoo, an open-source robot vacuum that owners build themselves."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/designer-turns-niche-e-ink-dev-board-into-a-60hz-game-boy-handheld-960x540-display-powered-by-ultra-low-cost-esp32-s3-microcontroller",
    "domain": "AI 算力 / 半导体",
    "title": "Designer turns discontinued E-Ink dev board into a 60Hz Game Boy handheld — dual-core chip runs at 100% to power handheld, 960x540 display employs ultra-low-cost ESP32-S3 microcontroller",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/designer-turns-niche-e-ink-dev-board-into-a-60hz-game-boy-handheld-960x540-display-powered-by-ultra-low-cost-esp32-s3-microcontroller",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T09:30:00+00:00",
    "summary": "The hardware is discontinued and the experience isn't perfect, but the fact that the emulator exists at all is a true technical achievement."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/amd-expo-ull-ram-drops-at-jaw-dropping-usd1-099-despite-promises-of-it-being-effectively-the-same-price-ddr5-6000-c26-32gb-kit-sports-80-percent-ull-tax",
    "domain": "AI 算力 / 半导体",
    "title": "AMD EXPO ULL RAM drops at jaw-dropping $1,099 despite promises of it being 'effectively the same price' — DDR5-6000 C26 32GB kit sports 80% ULL tax",
    "url": "https://www.tomshardware.com/pc-components/ram/amd-expo-ull-ram-drops-at-jaw-dropping-usd1-099-despite-promises-of-it-being-effectively-the-same-price-ddr5-6000-c26-32gb-kit-sports-80-percent-ull-tax",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:16:12+00:00",
    "summary": "Newegg has started selling G.Skill’s Trident Z5 NeoX memory kits featuring AMD ULL technology, and the prices are already high."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/cuda-emulator-for-amd-gpus-zluda-loses-funding-with-v6-release-embattled-project-goes-back-to-hobby-status-but-now-includes-32-bit-physx-support",
    "domain": "AI 算力 / 半导体",
    "title": "CUDA emulator for AMD GPUs Zluda loses funding with v6 release — embattled project goes back to hobby status but now includes 32-bit PhysX support",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/cuda-emulator-for-amd-gpus-zluda-loses-funding-with-v6-release-embattled-project-goes-back-to-hobby-status-but-now-includes-32-bit-physx-support",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T18:29:21+00:00",
    "summary": "Zluda is back to a hobby, as the open-source project has lost commercial funding with version 6 but added early 32-bit PhysX support."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/valve-threatens-legal-action-against-dbrand-over-its-unsanctioned-portal-2-inspired-companion-cube-edgy-accessories-manufacturer-kills-product-after-asking-for-licensing-deal-admits-it-didnt-have-the-right-to-make-it",
    "domain": "AI 算力 / 半导体",
    "title": "Valve threatens legal action against Dbrand over its unsanctioned Portal 2-inspired Companion Cube — edgy accessories manufacturer kills product after asking for licensing deal, admits it didn't have ",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/valve-threatens-legal-action-against-dbrand-over-its-unsanctioned-portal-2-inspired-companion-cube-edgy-accessories-manufacturer-kills-product-after-asking-for-licensing-deal-admits-it-didnt-have-the-right-to-make-it",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:26:18+00:00",
    "summary": "Valve has asked Dbrand to stop selling its Portal 2-themed Companion Cube cases for the Steam Machine, since it never asked the company permission to begin with."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/legacy-nvidia-rtx-3060-12gb-returns-to-retail-five-years-after-original-launch-priced-at-usd339-resurrected-gpu-strategy-that-jensen-called-a-good-idea-apparently-comes-to-fruition",
    "domain": "AI 算力 / 半导体",
    "title": "Legacy Nvidia RTX 3060 12GB returns to retail five years after original launch, priced at $339 — resurrected GPU strategy that Jensen called a 'good idea' apparently comes to fruition",
    "url": "https://www.tomshardware.com/pc-components/gpus/legacy-nvidia-rtx-3060-12gb-returns-to-retail-five-years-after-original-launch-priced-at-usd339-resurrected-gpu-strategy-that-jensen-called-a-good-idea-apparently-comes-to-fruition",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T17:11:15+00:00",
    "summary": "After Nvidia CEO Jensen Huang said that \"it's a good idea\" to consider re-introducing older GPUs made on trailing process nodes, the five-year-old RTX 3060 is back on e-tailer shelves, priced at $339."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/south-korea-unveils-usd520-billion-investment-plan-with-samsung-and-sk-hynix-to-expand-memory-chip-dominance-plan-includes-four-new-fabs-and-hbm-facilities-amid-strong-government-support",
    "domain": "AI 算力 / 半导体",
    "title": "South Korea unveils $520 billion investment plan with Samsung and SK Hynix to expand memory chip dominance — plan includes four new fabs and HBM facilities, amid strong government support",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/south-korea-unveils-usd520-billion-investment-plan-with-samsung-and-sk-hynix-to-expand-memory-chip-dominance-plan-includes-four-new-fabs-and-hbm-facilities-amid-strong-government-support",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T14:12:23+00:00",
    "summary": "President Lee unveiled an 800 trillion won ($520B) public-private plan for four new Samsung and SK Hynix fabs, dwarfing the US CHIPS Act tenfold."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/steamroller-becomes-first-prebuilt-gaming-pc-to-ship-with-steamos-ryzen-9600x-radeon-rx-7600-16gb-ddr5-ram-system-available-for-preorder-at-usd1-299",
    "domain": "AI 算力 / 半导体",
    "title": "Steamroller becomes first prebuilt gaming PC to ship with SteamOS — Ryzen 9600X, Radeon RX 7600, 16GB DDR5 RAM system available for preorder at $1,299",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/steamroller-becomes-first-prebuilt-gaming-pc-to-ship-with-steamos-ryzen-9600x-radeon-rx-7600-16gb-ddr5-ram-system-available-for-preorder-at-usd1-299",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:30:00+00:00",
    "summary": "Steamroller is the first commercially available prebuilt gaming PC running SteamOS, pairing standard desktop components with future upgradeability."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-sk-hynix-and-micron-sued-over-alleged-dram-price-fixing-amid-record-memory-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung, SK hynix, and Micron sued over alleged DRAM price fixing amid record memory costs — lawsuit claims coordinated HBM shift was cover to curtail DDR3 and DDR4 production",
    "url": "https://www.tomshardware.com/tech-industry/samsung-sk-hynix-and-micron-sued-over-alleged-dram-price-fixing-amid-record-memory-costs",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:18:54+00:00",
    "summary": "Samsung, SK hynix, and Micron were sued on June 25th in the U.S. District Court for the Northern District of California."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/imecs-2026-roadmap-details-0-3nm-nodes-by-2038-cfet-transistors-become-viable-at-0-7nm-company-redefines-moores-law-as-cell-sizes-gain-importance-for-density",
    "domain": "AI 算力 / 半导体",
    "title": "Imec's 2026 roadmap details 0.3nm nodes by 2038, CFET transistors become viable at 0.7nm — company redefines Moore's Law as cell sizes gain importance for density",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/imecs-2026-roadmap-details-0-3nm-nodes-by-2038-cfet-transistors-become-viable-at-0-7nm-company-redefines-moores-law-as-cell-sizes-gain-importance-for-density",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T13:15:14+00:00",
    "summary": "As CPP shrinking stalls, chipmakers find a new way to increase transistor density. Imec foresees 0.3nm in 2038, CFET insertion in 2038, HLSI era."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd1-100-on-this-rtx-5080-gaming-pc-with-a-9800x3d-from-hp-now-just-usd2-499-liquid-cooled-omen-35l-rig-unlocks-4k-gameplay-with-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save a massive $1,100 on this RTX 5080 gaming PC with a 9800X3D from HP, now just $2,499 — liquid-cooled Omen 35L rig unlocks 4K gameplay with 32GB DDR5 and a 2TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd1-100-on-this-rtx-5080-gaming-pc-with-a-9800x3d-from-hp-now-just-usd2-499-liquid-cooled-omen-35l-rig-unlocks-4k-gameplay-with-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T11:15:36+00:00",
    "summary": "Save $1,100 on this HP Omen 45L gaming rig, fitted with a 9800X3D, RTX 5080, 32GB of DDR5 RAM, and 2TB in SSD storage, all for just $2,499.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/pick-up-hotos-ultra-useful-3d-printing-tool-for-just-usd29-save-40-percent-on-this-35-piece-cordless-rotary-tool-to-give-your-creations-a-finishing-touch",
    "domain": "AI 算力 / 半导体",
    "title": "Pick up Hoto's ultra-useful 3D printing tool for just $29 — save 40% on this 35-piece Cordless Rotary Tool to give your creations a finishing touch",
    "url": "https://www.tomshardware.com/desktops/pc-building/pick-up-hotos-ultra-useful-3d-printing-tool-for-just-usd29-save-40-percent-on-this-35-piece-cordless-rotary-tool-to-give-your-creations-a-finishing-touch",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T11:12:00+00:00",
    "summary": "Save on these brilliant Hoto tools for PC builders and hobbyists. Hoto's cordless rotary tool is now only $29."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/chinas-hollow-core-fiber-trial-pushes-51-3-tb-s-over-128-miles-without-signal-regeneration-milestone-targets-ai-era-networking-bottlenecks",
    "domain": "AI 算力 / 半导体",
    "title": "China’s hollow-core fiber trial pushes 51.3 Tb/s over 128 miles without signal regeneration — milestone targets AI-era networking bottlenecks",
    "url": "https://www.tomshardware.com/networking/chinas-hollow-core-fiber-trial-pushes-51-3-tb-s-over-128-miles-without-signal-regeneration-milestone-targets-ai-era-networking-bottlenecks",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T10:00:00+00:00",
    "summary": "YOFC, China Telecom, and Dekoli claim a 51.3 Tb/s hollow-core fiber field-trial record over 206.5 km, using 1.2 Tb/s-per-wavelength WDM transmission without repeaters or remote-pumped amplifiers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/pong-game-that-recompiles-itself-every-frame-wins-the-ioccc29-obfuscated-c-contest",
    "domain": "AI 算力 / 半导体",
    "title": "Pong game recompiles its own source code every frame — winning entry at IOCCC29 was generated by a custom compiler",
    "url": "https://www.tomshardware.com/tech-industry/pong-game-that-recompiles-itself-every-frame-wins-the-ioccc29-obfuscated-c-contest",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T09:30:00+00:00",
    "summary": "Jonah Uellenberg won the Ping Pong Prize at the 29th International Obfuscated C Code Contest earlier this month, with a version of Pong that recompiles its own source code on every frame."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pnys-performance-32gb-ddr5-5600-ram-becomes-the-cheapest-2x16gb-kit-ddr5-kit-gets-a-usd70-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's Vengeance 32GB DDR5-5200 RAM becomes the cheapest 2x16GB kit— DDR5 kit still $379",
    "url": "https://www.tomshardware.com/pc-components/pnys-performance-32gb-ddr5-5600-ram-becomes-the-cheapest-2x16gb-kit-ddr5-kit-gets-a-usd70-discount",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T14:32:37+00:00",
    "summary": "This 32GB DDR5 memory kit won't impress enthusiasts with its timings or design, but its aggressive price makes it difficult to overlook."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/lenovo-says-the-ramageddon-is-the-new-normal-outlines-survival-guide-at-isc-2026-an-exec-said-it-will-never-be-like-it-was-last-year",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo says the 'RAMageddon' is the new normal, outlines survival guide — at ISC 2026 an exec said 'it will never be like it was last year'",
    "url": "https://www.tomshardware.com/pc-components/ram/lenovo-says-the-ramageddon-is-the-new-normal-outlines-survival-guide-at-isc-2026-an-exec-said-it-will-never-be-like-it-was-last-year",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T13:50:59+00:00",
    "summary": "At the International Supercomputing Conference this past week, Lenovo reportedly said the memory market 'it will never be like it was last year.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/diy-3d-printed-steam-machine-a-like-uses-diagonal-mobo-mounting-parts-include-a-mini-itx-motherboard-rtx-5060-and-a-flex-atx-psu",
    "domain": "AI 算力 / 半导体",
    "title": "AMD engineer 3D-prints Steam Machine-a-like with diagonal mobo mounting — parts include a Mini ITX motherboard, RTX 5060, and a flex ATX PSU",
    "url": "https://www.tomshardware.com/desktops/pc-building/diy-3d-printed-steam-machine-a-like-uses-diagonal-mobo-mounting-parts-include-a-mini-itx-motherboard-rtx-5060-and-a-flex-atx-psu",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:36:37+00:00",
    "summary": "The Terk Box v1.1 looks like the closest DIY alternative to Valve's Steam Machine yet. 3D print source files are available."
  },
  {
    "id": "rss:https://www.eetimes.com/synaptics-acquisition-by-onsemi-affirms-edge-ai-is-for-real/",
    "domain": "AI 算力 / 半导体",
    "title": "Synaptics Acquisition by Onsemi Affirms Edge AI Is for Real",
    "url": "https://www.eetimes.com/synaptics-acquisition-by-onsemi-affirms-edge-ai-is-for-real/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T14:41:31+00:00",
    "summary": "Here is why a power and sensing specialist has snapped AI-native compute assets to foray into the physical AI world. The post Synaptics Acquisition by Onsemi Affirms Edge AI Is for Real appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/the-pqc-silicon-is-here-today-for-tomorrows-quantum-threats/",
    "domain": "AI 算力 / 半导体",
    "title": "The PQC Silicon Is Here Today for Tomorrow’s Quantum Threats",
    "url": "https://www.eetimes.com/the-pqc-silicon-is-here-today-for-tomorrows-quantum-threats/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T08:38:45+00:00",
    "summary": "Two new security chips aim to future-proof devices for the quantum era by integrating hardware accelerators that support PQC algorithms. The post The PQC Silicon Is Here Today for Tomorrow’s Quantum T"
  },
  {
    "id": "rss:https://www.eetimes.com/next%e2%80%91gen-adas-ad-architectures-power-networking-safety-sensors/",
    "domain": "AI 算力 / 半导体",
    "title": "Next‑Gen ADAS/AD Architectures: Power, Networking, Safety & Sensors",
    "url": "https://www.eetimes.com/next%e2%80%91gen-adas-ad-architectures-power-networking-safety-sensors/",
    "source": "Infineon Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T08:13:23+00:00",
    "summary": "Join this webinar and learn how high‑performance semiconductor technologies support centralized sensor fusion and reliable ADAS systems. The post Next‑Gen ADAS/AD Architectures: Power, Networking, Saf"
  },
  {
    "id": "rss:https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions/",
    "domain": "AI 算力 / 半导体",
    "title": "Jim Keller: ‘AI Still Obeys the Old Laws of Compute’",
    "url": "https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T22:00:00+00:00",
    "summary": "Invoking Rent's Rule and Amdahl's Law, Keller argues that memory and communication, not bigger processors, will define the future of AI infrastructure The post Jim Keller: ‘AI Still Obeys the Old Laws"
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
    "id": "rss:https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit",
    "domain": "大厂 AI 动态",
    "title": "Meta is adding ridiculous &#8216;rate limits&#8217; and a soft paywall to its smart glasses",
    "url": "https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T00:51:03+00:00",
    "summary": "Would you pay $20 a month for access to AI hardware you already own? That appears to be one of Meta's next bets. This week, it quietly announced that your glasses' Conversation Focus feature will soon"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/958964/anthropic-claude-fable-5-is-back",
    "domain": "大厂 AI 动态",
    "title": "Anthropic&#8217;s long-sidelined Fable 5 is greenlit to return",
    "url": "https://www.theverge.com/ai-artificial-intelligence/958964/anthropic-claude-fable-5-is-back",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T00:03:55+00:00",
    "summary": "After weeks of negotiating with the Trump administration, Anthropic is finally going to be able to bring Claude Fable 5 back online. In a post on X, Anthropic said it plans to begin restoring access W"
  },
  {
    "id": "rss:https://www.theverge.com/tech/959894/dish-chapter-11-bankruptcy",
    "domain": "大厂 AI 动态",
    "title": "Dish files for bankruptcy, but not shutting down",
    "url": "https://www.theverge.com/tech/959894/dish-chapter-11-bankruptcy",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T22:46:52+00:00",
    "summary": "Dish, the company that operates Dish TV and Sling TV, has filed for Chapter 11 bankruptcy,\" as reported earlier by Reuters. The plan will allow the EchoStar-owned company to continue to wind down its "
  },
  {
    "id": "rss:https://www.theverge.com/tech/959847/amazon-ftc-identity-theft-fine",
    "domain": "大厂 AI 动态",
    "title": "Amazon fined $2.25 million for failing to help identity theft victims",
    "url": "https://www.theverge.com/tech/959847/amazon-ftc-identity-theft-fine",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T21:20:01+00:00",
    "summary": "The Federal Trade Commission fined Amazon $2.25 million to settle claims that the company failed to help customers who fell victim to identity theft, as reported earlier by Bloomberg. In its complaint"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/959687/acer-swift-go-16-ai-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Acer&#8217;s Swift Go 16 is a lot of laptop for $900",
    "url": "https://www.theverge.com/gadgets/959687/acer-swift-go-16-ai-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:00:00+00:00",
    "summary": "As high memory and storage prices have driven up the cost of everything from consoles to computers, finding a competent laptop for under $1,000 has become a challenge. Thankfully, the Acer Swift Go 16"
  },
  {
    "id": "rss:https://www.theverge.com/tech/959778/google-notebooklm-ai-clips",
    "domain": "大厂 AI 动态",
    "title": "Google’s NotebookLM can sum up your research in a TikTok-style clip",
    "url": "https://www.theverge.com/tech/959778/google-notebooklm-ai-clips",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T19:24:51+00:00",
    "summary": "Google's NotebookLM is adding a new way to catch up on your notes: TikTok-style AI videos. The new feature is rolling out to Google AI Ultra and Pro subscribers, allowing NotebookLM to generate 60-sec"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/906880/lg-ultragear-tandem-oled-1440p-gaming-monitor-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "LG’s 27-inch Tandem OLED gaming monitor is cheaper than ever",
    "url": "https://www.theverge.com/gadgets/906880/lg-ultragear-tandem-oled-1440p-gaming-monitor-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T18:42:00+00:00",
    "summary": "The price of LG’s UltraGear 27GX700A-B 1440p gaming monitor that came out last August has dropped to nearly its best price yet. You can grab it at Amazon for $484.99 or at LG for $499.99 (originally $"
  },
  {
    "id": "rss:https://www.theverge.com/games/959713/io-interactive-project-fantasy-layoffs",
    "domain": "大厂 AI 动态",
    "title": "007 First Light&#8217;s developer lays off staff but claims its next franchise will continue",
    "url": "https://www.theverge.com/games/959713/io-interactive-project-fantasy-layoffs",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T18:14:05+00:00",
    "summary": "IO Interactive, the studio behind the Hitman series and 007 First Light, announced that it is laying off staff after a relationship with an \"external partner\" on its next big franchise, Project Fantas"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/959657/moto-tag-2-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Moto&#8217;s Tag 2 tracker is $20 for a limited time",
    "url": "https://www.theverge.com/gadgets/959657/moto-tag-2-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T17:38:23+00:00",
    "summary": "Announced at CES 2026, the Moto Tag 2 has finally arrived in the US. The Bluetooth tracker with improved battery life over its predecessor, plus UWB sensing for more accurate tracking, is available th"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/959684/netflix-wonka-golden-ticket-gene-wilder",
    "domain": "大厂 AI 动态",
    "title": "Netflix is using an AI-generated Gene Wilder voice in its Willy Wonka reality show",
    "url": "https://www.theverge.com/streaming/959684/netflix-wonka-golden-ticket-gene-wilder",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T17:19:15+00:00",
    "summary": "A new teaser trailer confirmed that Wonka's The Golden Ticket will premiere on Netflix on September 23rd, following its Squid Game reality show in the trend of creating real competitions based on fict"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/",
    "domain": "大厂 AI 动态",
    "title": "The ‘Father of the Internet’ is finally retiring",
    "url": "https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T03:15:37+00:00",
    "summary": "Vinton Cerf, one of the creators of the protocols underlying the internet, will step down as Google's chief internet evangelist next week."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/",
    "domain": "大厂 AI 动态",
    "title": "Trump drops restrictions on Anthropic’s Mythos and Fable models",
    "url": "https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T02:16:06+00:00",
    "summary": "The Trump administration's erratic approach to AI policymaking has left companies across the industry with little clarity about what will govern future model releases."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/wayve-launches-85m-employee-tender-offer-at-8-5b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Wayve launches $85M employee tender offer at $8.5B valuation",
    "url": "https://techcrunch.com/2026/06/30/wayve-launches-85m-employee-tender-offer-at-8-5b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T02:04:40+00:00",
    "summary": "Wayve’s offering is part of a growing trend of AI startups using employee tenders as a strategic tool to attract and retain talent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/last-chance-to-apply-startup-battlefield-australia-applications-close-july-6/",
    "domain": "大厂 AI 动态",
    "title": "Startup Battlefield Australia application closes in days: Apply before July 6",
    "url": "https://techcrunch.com/2026/06/30/last-chance-to-apply-startup-battlefield-australia-applications-close-july-6/",
    "source": "Isabelle Johannessen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T23:00:00+00:00",
    "summary": "What if one pitch changed everything? The next company nobody has heard of yet is building something that will matter. It could be yours."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/openclaw-is-finally-available-on-android-and-ios/",
    "domain": "大厂 AI 动态",
    "title": "OpenClaw is finally available on Android and iOS",
    "url": "https://techcrunch.com/2026/06/30/openclaw-is-finally-available-on-android-and-ios/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T21:53:28+00:00",
    "summary": "The free open source agentic program is finally invading your phone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/the-deepmind-trio-who-built-a-poker-ai-are-now-making-money-for-quant-hedge-funds/",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind trio who built a poker AI are now making money for quant hedge funds",
    "url": "https://techcrunch.com/2026/06/30/the-deepmind-trio-who-built-a-poker-ai-are-now-making-money-for-quant-hedge-funds/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:33:48+00:00",
    "summary": "EquiLibre Technologies, a Prague-based AI lab founded by three ex-DeepMind researchers, is now valued at more than $500 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/",
    "domain": "大厂 AI 动态",
    "title": "Realta Fusion generates electricity directly from a fusion reaction, an apparent first",
    "url": "https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T19:12:43+00:00",
    "summary": "“We can take power from a plasma,” Kieran Furlong, co-founder and CEO of Realta Fusion, told TechCrunch. The milestone shows “what’s possible,” he added."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/google-introduces-a-faster-cheaper-image-generator-with-nano-banana-2-lite/",
    "domain": "大厂 AI 动态",
    "title": "Google introduces a faster, cheaper image generator with Nano Banana 2 Lite",
    "url": "https://techcrunch.com/2026/06/30/google-introduces-a-faster-cheaper-image-generator-with-nano-banana-2-lite/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T19:02:38+00:00",
    "summary": "Google is updating its image generator to make it faster and cheaper, making it a more useful tool for creators looking to make AI content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/clicks-shows-off-its-blackberry-inspired-phone-in-a-new-hands-on-video/",
    "domain": "大厂 AI 动态",
    "title": "Clicks shows off its BlackBerry-inspired phone in a new hands-on video",
    "url": "https://techcrunch.com/2026/06/30/clicks-shows-off-its-blackberry-inspired-phone-in-a-new-hands-on-video/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T18:34:22+00:00",
    "summary": "A new video shows the final production version of the upcoming Clicks Communicator, a BlackBerry-like smartphone that runs modern apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia competitor Etched hits $5B valuation, $1B in sales for AI chip",
    "url": "https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T18:13:02+00:00",
    "summary": "Nvidia AI chip competitor Etched says it has already booked $1 billion under contract for the inference systems powered by its chip."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic launches Claude Sonnet 5 as a cheaper way to run agents",
    "url": "https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T18:00:00+00:00",
    "summary": "Anthropic’s Claude Sonnet 5 brings stronger agentic capabilities, lower pricing, and improved safety, positioning the model as a cheaper alternative to Opus, GPT-5.5, and Gemini Pro."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/acti-puts-ai-agents-directly-into-your-smartphone-keyboard/",
    "domain": "大厂 AI 动态",
    "title": "Acti puts AI agents directly into your smartphone keyboard",
    "url": "https://techcrunch.com/2026/06/30/acti-puts-ai-agents-directly-into-your-smartphone-keyboard/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T17:52:46+00:00",
    "summary": "Acti is betting the smartphone keyboard is the next home for AI assistants. The startup's new keyboard for iOS and Android works across apps and lets users create custom AI-powered shortcuts using nat"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/threads-adds-new-features-to-live-chats-as-it-expands-access/",
    "domain": "大厂 AI 动态",
    "title": "Threads adds new features to Live Chats as it expands access",
    "url": "https://techcrunch.com/2026/06/30/threads-adds-new-features-to-live-chats-as-it-expands-access/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T17:00:00+00:00",
    "summary": "The updates include translations, new tools for hosts, and more."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/anthropics-claude-science-bets-on-workflow-not-a-new-model-to-win-over-scientists/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Claude Science bets on workflow, not a new model, to win over scientists",
    "url": "https://techcrunch.com/2026/06/30/anthropics-claude-science-bets-on-workflow-not-a-new-model-to-win-over-scientists/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T17:00:00+00:00",
    "summary": "Anthropic's Claude Science is a workbench that gives scientists one environment to do computational research, saving them from the need to bounce between databases, pipelines, and tools."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/blue-origin-still-doesnt-know-why-its-new-glenn-rocket-blew-up-last-month/",
    "domain": "大厂 AI 动态",
    "title": "Blue Origin still doesn’t know why its New Glenn rocket blew up last month",
    "url": "https://techcrunch.com/2026/06/30/blue-origin-still-doesnt-know-why-its-new-glenn-rocket-blew-up-last-month/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:09:57+00:00",
    "summary": "But the company is still claiming that New Glenn will return to flight this year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/",
    "domain": "大厂 AI 动态",
    "title": "Tesla starts testing Cybercab without pedals or a steering wheel in Austin",
    "url": "https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T15:32:50+00:00",
    "summary": "The company may finally be ready to try to deliver on Elon Musk's years-long promise of launching a robotaxi network of its own."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/",
    "domain": "大厂 AI 动态",
    "title": "X now offers an MCP server to make its platform easier for AI tools to use",
    "url": "https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T15:08:42+00:00",
    "summary": "X has launched a hosted MCP server, making it easier for developers to connect AI applications with the company’s API."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/",
    "domain": "大厂 AI 动态",
    "title": "Arcturus could halve the grid’s electrical losses using its nano-infused metals",
    "url": "https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T15:01:42+00:00",
    "summary": "Stealthy startup Arcturus uses lasers to infuse carbon nanomaterials into copper, dramatically improving its ability to conduct electricity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/podcasting-platform-riverside-enters-the-newsletter-publishing-game/",
    "domain": "大厂 AI 动态",
    "title": "Podcasting platform Riverside enters the newsletter publishing game",
    "url": "https://techcrunch.com/2026/06/30/podcasting-platform-riverside-enters-the-newsletter-publishing-game/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T15:00:00+00:00",
    "summary": "Users will be able use AI to create newsletters based on their recordings."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/",
    "domain": "大厂 AI 动态",
    "title": "Amazon launches new $1 billion FDE org, following OpenAI and Anthropic",
    "url": "https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T15:00:00+00:00",
    "summary": "Engineers on the new team will embed within companies to deploy purpose-built agents, focusing on fast deployments and customer self-sufficiency."
  },
  {
    "id": "rss:https://stratechery.com/2026/summer-break-week-of-june-29/",
    "domain": "大厂 AI 动态",
    "title": "Summer Break: Week of June 29",
    "url": "https://stratechery.com/2026/summer-break-week-of-june-29/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T10:00:00+00:00",
    "summary": "Stratechery is on summer break the week of June 29. There will be no Weekly Article or Updates. The next Update will be on Monday, July 6. Dithering,&#160;Sharp Tech, and&#160;Sharp China&#160;will al"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/june-research-roundup-6-cool-science-stories-we-almost-missed/",
    "domain": "大厂 AI 动态",
    "title": "June research roundup: 6 cool science stories we almost missed",
    "url": "https://arstechnica.com/science/2026/06/june-research-roundup-6-cool-science-stories-we-almost-missed/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T22:11:10+00:00",
    "summary": "Also, the science of poop's distinctive shape, boron buckyballs, and the secret to a soccer feint."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/reddit-will-require-you-to-log-in-to-use-old-reddit-com/",
    "domain": "大厂 AI 动态",
    "title": "Reddit will require you to log in to use old.reddit.com",
    "url": "https://arstechnica.com/gadgets/2026/06/reddit-will-require-you-to-log-in-to-use-old-reddit-com/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T21:46:35+00:00",
    "summary": "Logged-out Old Reddit access is “significant source of abusive scraping.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/exec-blames-malware-threat-for-amazon-blocking-sideloading-on-new-fire-sticks/",
    "domain": "大厂 AI 动态",
    "title": "Amazon blames piracy apps with malware for killing new Fire Stick sideloading",
    "url": "https://arstechnica.com/gadgets/2026/06/exec-blames-malware-threat-for-amazon-blocking-sideloading-on-new-fire-sticks/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T21:04:53+00:00",
    "summary": "New Fire Stick OS helps Amazon block third-party homepage launchers, ad blockers."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/nasa-may-send-a-backup-nuclear-powered-mars-rover-to-the-moon/",
    "domain": "大厂 AI 动态",
    "title": "NASA may send a backup, nuclear-powered Mars rover to the Moon",
    "url": "https://arstechnica.com/space/2026/06/nasa-may-send-a-backup-nuclear-powered-mars-rover-to-the-moon/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:50:14+00:00",
    "summary": "\"That would be an awesome capability.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/google-kills-tenor-gif-api-forcing-changes-at-x-discord-and-more/",
    "domain": "大厂 AI 动态",
    "title": "Google kills Tenor GIF API, forcing changes at X, Discord, and more",
    "url": "https://arstechnica.com/gadgets/2026/06/google-kills-tenor-gif-api-forcing-changes-at-x-discord-and-more/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:38:51+00:00",
    "summary": "Tenor still connects to Google apps, but other platforms must look elsewhere for GIFs."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/apple-takes-epic-fight-over-app-store-fees-to-the-supreme-court/",
    "domain": "大厂 AI 动态",
    "title": "Apple takes Epic fight over app store fees to the Supreme Court",
    "url": "https://arstechnica.com/tech-policy/2026/06/apple-takes-epic-fight-over-app-store-fees-to-the-supreme-court/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:20:29+00:00",
    "summary": "Supreme Court will weigh if Apple contempt finding in Epic case is “erroneous.”"
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/ai-browsers-can-be-lulled-into-a-dream-world-where-guardrails-no-longer-apply/",
    "domain": "大厂 AI 动态",
    "title": "New attack provides one more reason why AI browsers are a bad idea",
    "url": "https://arstechnica.com/security/2026/06/ai-browsers-can-be-lulled-into-a-dream-world-where-guardrails-no-longer-apply/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:03:14+00:00",
    "summary": "Telling an LLM that 2 + 2 = 5 is enough to make it follow forbidden instructions."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/googles-new-nano-banana-2-lite-image-model-is-its-fastest-and-cheapest-yet/",
    "domain": "大厂 AI 动态",
    "title": "Google's new Nano Banana 2 Lite image model is its fastest and cheapest yet",
    "url": "https://arstechnica.com/ai/2026/06/googles-new-nano-banana-2-lite-image-model-is-its-fastest-and-cheapest-yet/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T18:36:10+00:00",
    "summary": "They may not look as good, but Nano Banana 2 Lite images only take a few seconds to create."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/rfk-jr-stacks-fda-panel-with-peptide-peddlers-as-fda-scientists-oppose-access/",
    "domain": "大厂 AI 动态",
    "title": "RFK Jr. stacks FDA panel with peptide peddlers as FDA scientists oppose access",
    "url": "https://arstechnica.com/health/2026/06/rfk-jr-stacks-fda-panel-with-peptide-peddlers-as-fda-scientists-oppose-access/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T18:25:10+00:00",
    "summary": "Peptide drugs are popular, but FDA scientists warn they're untested, may be harmful."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/trumps-plan-to-redesign-every-gov-website-leads-to-ai-designed-horrors/",
    "domain": "大厂 AI 动态",
    "title": "Trump's plan to redesign every .gov website leads to AI-designed horrors",
    "url": "https://arstechnica.com/tech-policy/2026/06/trumps-plan-to-redesign-every-gov-website-leads-to-ai-designed-horrors/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:59:02+00:00",
    "summary": "A year in, National Design Studio delays plan to update government web standards."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/the-us-going-100-ev-by-2040-would-save-more-than-100k-lives-study-says/",
    "domain": "大厂 AI 动态",
    "title": "The US going 100% EV by 2040 would save more than 100k lives, study says",
    "url": "https://arstechnica.com/cars/2026/06/the-us-going-100-ev-by-2040-would-save-more-than-100k-lives-study-says/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:03:44+00:00",
    "summary": "Much of it comes from heavy-duty trucks and buses that burn diesel."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/spacex-may-donate-stock-to-trumps-savings-accounts-for-kids-report-says/",
    "domain": "大厂 AI 动态",
    "title": "Trump asked Musk for SpaceX stock to seed US kids’ savings accounts, report says",
    "url": "https://arstechnica.com/tech-policy/2026/06/spacex-may-donate-stock-to-trumps-savings-accounts-for-kids-report-says/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T15:38:08+00:00",
    "summary": "Sources suggest Musk may be mulling big donation to Trump Accounts."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/florida-bans-local-governments-from-pursuing-net-zero-emissions-goals/",
    "domain": "大厂 AI 动态",
    "title": "Florida bans local governments from pursuing net-zero emissions goals",
    "url": "https://arstechnica.com/science/2026/06/florida-bans-local-governments-from-pursuing-net-zero-emissions-goals/",
    "source": "Amy Green, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T13:40:16+00:00",
    "summary": "Gov. Ron DeSantis calls it a crackdown on \"radical climate policies.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/ars-live-whats-the-latest-in-the-aftermath-of-the-new-glenn-catastrophe/",
    "domain": "大厂 AI 动态",
    "title": "Ars Live, today: The latest on the aftermath of the New Glenn catastrophe",
    "url": "https://arstechnica.com/space/2026/06/ars-live-whats-the-latest-in-the-aftermath-of-the-new-glenn-catastrophe/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T13:15:59+00:00",
    "summary": "Join us on the livestream at 1 pm ET and ask questions about the aftermath of New Glenn."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/06/us-offers-10-million-for-info-on-group-behind-signal-and-whatsapp-hacking-spree/",
    "domain": "大厂 AI 动态",
    "title": "US offers $10 million for info on group behind Signal and WhatsApp hacking spree",
    "url": "https://arstechnica.com/information-technology/2026/06/us-offers-10-million-for-info-on-group-behind-signal-and-whatsapp-hacking-spree/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T22:05:33+00:00",
    "summary": "Operation by two Russia-state groups has been ongoing since at least March."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/",
    "domain": "大厂 AI 动态",
    "title": "South Korea to spend $1T on more memory chip production and humanoid robots",
    "url": "https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T21:09:43+00:00",
    "summary": "South Korea targets physical AI lead and commercial humanoid robots by 2028."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/solar-outproduced-coal-in-april-but-not-on-the-grid/",
    "domain": "大厂 AI 动态",
    "title": "US renewable boom passes key milestone in April",
    "url": "https://arstechnica.com/science/2026/06/solar-outproduced-coal-in-april-but-not-on-the-grid/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:12:30+00:00",
    "summary": "Small-scale solar helped renewables hit nearly triple coal's generation in the US."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/supreme-court-ruling-guts-governments-use-of-geofence-warrants/",
    "domain": "大厂 AI 动态",
    "title": "Supreme Court ruling guts government’s use of geofence warrants",
    "url": "https://arstechnica.com/tech-policy/2026/06/supreme-court-ruling-guts-governments-use-of-geofence-warrants/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:04:04+00:00",
    "summary": "SCOTUS falls short of deeming geofence warrants unconstitutional, though."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/sony-erases-digital-content-from-libraries-were-reminded-we-dont-own-what-we-buy/",
    "domain": "大厂 AI 动态",
    "title": "Sony erases digital content from libraries; we're reminded we don’t own what we buy",
    "url": "https://arstechnica.com/gadgets/2026/06/sony-erases-digital-content-from-libraries-were-reminded-we-dont-own-what-we-buy/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T19:10:57+00:00",
    "summary": "Sony has been scaling down its digitial store for a few years."
  },
  {
    "id": "wscn:3775758",
    "domain": "股票",
    "title": "狂飙牛市中的杠杆隐忧：韩股风险会蔓延吗？",
    "url": "https://wallstreetcn.com/premium/articles/3775758?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:54:20+00:00",
    "summary": "韩股杠杆高度集中于芯片巨头，放大波动与熔断风险，但基本面强劲，短期去杠杆后中期走势看盈利。"
  },
  {
    "id": "wscn:3775943",
    "domain": "股票",
    "title": "中国最大的独立生态词元供应商硅基流动递表港交所",
    "url": "https://wallstreetcn.com/articles/3775943",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:54:08+00:00",
    "summary": "2025年营收增超六倍，但算力成本攀升致毛利转负。"
  },
  {
    "id": "wscn:3775921",
    "domain": "股票",
    "title": "沪指午后回落接近转跌，券商爆发，创业板跌超2%，“光”齐跌，光伏逆变器大跌，阳光电源一度跌停",
    "url": "https://wallstreetcn.com/articles/3775921",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:45:02+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超4500股飘红，上午半天成交2.44万亿。沪、深两市半日成交额2.42万亿，较上个交易日放量超3100亿。板块方面，券商股领涨大市，金融科技、氟化工、医药生物、人形机器人、锂矿、跨境支付、AI应用、网络安全、车路云等概念股纷纷走强。光伏、算力硬件题材回调。"
  },
  {
    "id": "wscn:3775942",
    "domain": "股票",
    "title": "KOSPI指数盘中跌近4%，韩国政府紧急辟谣“芯片巨头利润共享”传言",
    "url": "https://wallstreetcn.com/articles/3775942",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:41:19+00:00",
    "summary": "韩国Kospi盘中一度大跌近4%。韩国贸工资源部表示，网络上流传的“首尔已向三星电子和SK海力士发函、要求设立政府主导的利润共享相关智库”的说法“完全不实”，并宣布将把蓄意散布不实信息的行为移交调查当局处理。"
  },
  {
    "id": "wscn:3775932",
    "domain": "股票",
    "title": "市场等待沃什讲话与非农数据，韩股收跌2%，美元走强，黄金再跌1%",
    "url": "https://wallstreetcn.com/articles/3775932",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:38:38+00:00",
    "summary": "韩国首尔综指收跌2.04%，报8303.41点。美元指数上涨0.2%，此前上季度累计涨幅为0.6%。黄金现货下跌1.1%，至每盎司约3966美元。白银和铂金亦同步回落。日元跌至162.77兑1美元，本周早些时候曾触及40年低点。"
  },
  {
    "id": "wscn:3775937",
    "domain": "股票",
    "title": "管理层优先考虑“价格和利润率”，NAND扩产有限，高盛再上调铠侠目标价",
    "url": "https://wallstreetcn.com/articles/3775937",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:21:44+00:00",
    "summary": "高盛将铠侠控股目标价从9.3万日元大幅上调至11.6万日元，重申买入评级，较现价隐含31%上行空间。NAND供需持续偏紧、新产能释放推迟至2028年后，叠加管理层坚守\"价格优先于出货量\"策略，高盛将FY3/29营业利润预测上调29%，预计FY3/27一季度业绩将全面超预期。铠侠过去12个月股价累计暴涨3406%。"
  },
  {
    "id": "wscn:3775941",
    "domain": "股票",
    "title": "兰州银行近3亿股两拍皆空，股东风险再受瞩",
    "url": "https://wallstreetcn.com/articles/3775941",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:19:59+00:00",
    "summary": "6月30日，兰州银行公告称，公司第三大股东华邦控股集团持有的2.9745亿股股份，在第二次司法拍卖中..."
  },
  {
    "id": "wscn:3775940",
    "domain": "股票",
    "title": "中炬高新上半年净利预增超五成，渠道调整进入收获期",
    "url": "https://wallstreetcn.com/articles/3775940",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:18:26+00:00",
    "summary": "调味品业务放量"
  },
  {
    "id": "wscn:3775933",
    "domain": "股票",
    "title": "三星HBM4E良率突破70%，第七代AI内存开发进入稳定阶段",
    "url": "https://wallstreetcn.com/articles/3775933",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:10:32+00:00",
    "summary": "三星AI内存再出“王炸”！HBM4E测试良率破70%迈入稳定期，下一代DRAM工艺剑指11月量产认证，提前锁定英伟达新一代AI芯片红利。"
  },
  {
    "id": "wscn:3775934",
    "domain": "股票",
    "title": "美联储“不讲话了”！德银：静默期往往伴随政策转折点",
    "url": "https://wallstreetcn.com/articles/3775934",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:08:53+00:00",
    "summary": "美联储官员议后集体\"沉默\"，德意志银行敲响警报。德银研究发现，当前FOMC会后发言密度异常偏低，与2019年7月降息启动、2022年1月激进加息转向、2023年7月加息收尾三大历史转折节点高度吻合。主席沃什刻意淡化前瞻指引，并专设工作组重塑沟通机制——这场沉默，或许正是下一次重大政策转向的前奏。"
  },
  {
    "id": "wscn:3775935",
    "domain": "股票",
    "title": "美股狂欢到极致，连最坚定的多头都开始防范“夏季风暴”",
    "url": "https://wallstreetcn.com/articles/3775935",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T06:00:03+00:00",
    "summary": "随着季末再平衡压力、企业回购窗口关闭、美联储政策路径不明以及杠杆头寸急剧膨胀等风险因素叠加，市场对第三季度\"夏季风暴\"的警惕情绪正在升温。多位华尔街策略师在维持多头立场的同时，已开始提示5%至20%回撤风险。"
  },
  {
    "id": "wscn:3775925",
    "domain": "股票",
    "title": "快递行业的预期差：单票价格环比下降不等于反内卷失效，圆通超预期财报为行业正名",
    "url": "https://wallstreetcn.com/premium/articles/3775925?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T05:55:50+00:00",
    "summary": "圆通半年报业绩超预期并非偶然，而是“反内卷”政策成效与企业降本增效共振的结果。"
  },
  {
    "id": "wscn:3775938",
    "domain": "股票",
    "title": "MLCC龙头国巨涨价，代理商回应：属实",
    "url": "https://wallstreetcn.com/articles/3775938",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T05:54:29+00:00",
    "summary": "深圳市河锋鑫科技有限公司工作人员告诉记者，国巨电容产品本次原厂价格涨幅大约为50%，现货市场的价格涨幅相应会更大。“这次是原厂通知涨价，实际上，现货市场从今年5月到现在一直涨价，高端电容产品的价格一个月时间内最高涨幅接近10倍。最近经常出现延迟供货的情况，除了国巨，MLCC各大品牌都有延迟供货。”"
  },
  {
    "id": "wscn:3775930",
    "domain": "股票",
    "title": "美国最大电网PJM推进数据中心供电方案，电力容量价格两年暴涨逾1000%",
    "url": "https://wallstreetcn.com/articles/3775930",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T05:34:44+00:00",
    "summary": "美国最大电网运营商PJM容量电价两年内暴涨逾1000%，AI数据中心爆炸式用电需求正将区域电网推向临界点。PJM成员最新投票推进\"兜底采购\"方案，并要求数据中心二选一：自掏腰包为电网扩容，或接受高峰时段强制断电。科技巨头与电网运营商之间的供电博弈，正式进入白热化阶段。"
  },
  {
    "id": "wscn:3775931",
    "domain": "股票",
    "title": "打破行业惯例！报道：SK海力士长约价格“不设上限”，定价博弈全面白热化",
    "url": "https://wallstreetcn.com/articles/3775931",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T05:20:09+00:00",
    "summary": "SK海力士长约（LTA）打破惯例不设“价格上限”，成为市场唯一能在供需收紧时完整享受现货大涨红利的存储厂商。同时其将长约期限拉长至3至5年。对比而言，美光新长约虽以2026年二季度市价设置上限，但其价格底线对应的毛利率远超历史峰值，两大巨头定价模式各异，但均折射出话语权系统性增强。"
  },
  {
    "id": "wscn:3775748",
    "domain": "股票",
    "title": "半导体扩产超级周期“黄金窗口”：材料与设备的万亿拐点红利",
    "url": "https://wallstreetcn.com/premium/articles/3775748?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:54:34+00:00",
    "summary": "三星、SK海力士正开启存储芯片领域史无前例的扩产浪潮，全球存储资本开支2026/2027年预计分别达1103亿和1685亿美元，同比增长63%/53%。"
  },
  {
    "id": "wscn:3775928",
    "domain": "股票",
    "title": "中国旺旺增收不增利，渠道换挡先压利润",
    "url": "https://wallstreetcn.com/articles/3775928",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:44:52+00:00",
    "summary": "调低分红比例"
  },
  {
    "id": "wscn:3775927",
    "domain": "股票",
    "title": "走出中国市场的低谷，耐克还需要几个赛季",
    "url": "https://wallstreetcn.com/articles/3775927",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:39:16+00:00",
    "summary": "艰难修复"
  },
  {
    "id": "wscn:3775911",
    "domain": "股票",
    "title": "Anthropic攻入微软腹地：Claude Tag接入Teams揭开企业软件生态重构序幕",
    "url": "https://wallstreetcn.com/articles/3775911",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:02:10+00:00",
    "summary": "Anthropic将企业协作工具Claude Tag继接入Slack后，进一步集成至Microsoft Teams，完成企业协作双平台布局。微软、Salesforce开放核心生态，本质是防御用户流失的务实选择，但Claude Tag将直接冲击Copilot等自有AI产品。"
  },
  {
    "id": "wscn:3775851",
    "domain": "股票",
    "title": "日韩MLCC再涨价：AI服务器用量暴涨13倍，产品紧缺正全产业扩散",
    "url": "https://wallstreetcn.com/premium/articles/3775851?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T03:59:49+00:00",
    "summary": "村田7月1日起AI/车规MLCC涨价10-40%，三星电机高容现货涨50-80%，太阳诱电涨6-13%。行业预判紧缺将延续到2028年。"
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
    "id": "rss:https://arxiv.org/abs/2606.30685",
    "domain": "金融",
    "title": "Cascading Impacts of the USA--China Trade War on Global Oilseed Supply Chain",
    "url": "https://arxiv.org/abs/2606.30685",
    "source": "Diksha Gupta, Ritwick Mishra, Achla Marathe, Krista Danielle Yu, Anil Vullikanti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.30685v1 Announce Type: new Abstract: Global supply chains are highly interconnected, making them vulnerable to cascading disruptions induced by trade policy shocks. Understanding how such d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31102",
    "domain": "金融",
    "title": "Translation Readiness Index: Measuring Patent-Paper Proximity from Scientific Publication Text",
    "url": "https://arxiv.org/abs/2606.31102",
    "source": "Paul X. McCarthy, Rasika Amarasiri, Xian Gong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.31102v1 Announce Type: new Abstract: Universities, funders, investors, and policy agencies often need to identify research with translational relevance before patents, licenses, startups, o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31122",
    "domain": "金融",
    "title": "Generating Plausible Stress Scenarios via Large Deviations",
    "url": "https://arxiv.org/abs/2606.31122",
    "source": "Anand Deo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.31122v1 Announce Type: new Abstract: Financial stress tests based on handpicked scenarios can mislead risk management by overlooking genuinely dangerous configurations or overemphasising sh"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31251",
    "domain": "金融",
    "title": "Regime-Conditional Distributional Comparison of Trading Strategies: A GAMLSS/ZAGA Framework Applied to the S&P 500",
    "url": "https://arxiv.org/abs/2606.31251",
    "source": "Krzysztof Ozimek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.31251v1 Announce Type: new Abstract: Conventional comparisons of algorithmic trading strategies reduce each performance metric to a single number over the full backtest horizon, thereby dis"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31387",
    "domain": "金融",
    "title": "Signature-Based Optimal Execution for Statistical Arbitrage with Path-Dependent Trading Signals",
    "url": "https://arxiv.org/abs/2606.31387",
    "source": "Gianmarco Morbelli, Sven Karbach, Mike Derksen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.31387v1 Announce Type: new Abstract: We develop a signature-based framework for optimal execution in statistical arbitrage strategies with path-dependent predictive signals. Both the alpha "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31469",
    "domain": "金融",
    "title": "Same Firms, Different Verdicts: ESG Rating Choice and the Measurement of Greenwashing",
    "url": "https://arxiv.org/abs/2606.31469",
    "source": "Praveen Kumar Ashok Kumar, Rafa{\\l} Sieradzki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.31469v1 Announce Type: new Abstract: This paper investigates the Aggregate Confusion hypothesis (Berg, Kolbel, and Rigobon, 2022) at the firm level by measuring the Disclosure-Performance G"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31475",
    "domain": "金融",
    "title": "Real-time identification of the onset of financial rogue waves",
    "url": "https://arxiv.org/abs/2606.31475",
    "source": "Rosie Hayward, Orla Lennon, Fabio Biancalana",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.31475v1 Announce Type: new Abstract: Extreme events in financial systems, often captured by indicators such as volatility, remain difficult to identify close to their onset. Volatility shar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31675",
    "domain": "金融",
    "title": "Settlement Manipulation in Prediction Markets",
    "url": "https://arxiv.org/abs/2606.31675",
    "source": "David Dai, Ruizhe Jia, Shihao Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.31675v1 Announce Type: new Abstract: Prediction markets increasingly list contracts settling on an asset price that holders can move by trading the underlying. We build a model showing that"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.32011",
    "domain": "金融",
    "title": "Competition and Anomalies Redux: Evidence from U.S. Auto Dealers",
    "url": "https://arxiv.org/abs/2606.32011",
    "source": "David Huffman, Lamar Pierce, Germ\\'an Reyes, Alex Rees-Jones",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.32011v1 Announce Type: new Abstract: We examine a choice between bonus contracts offered to dealers of a U.S. auto manufacturer. In our data, dealers select the non-profit-maximizing option"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30779",
    "domain": "金融",
    "title": "Pareto Efficient Insurance with Multiple Policyholders, Multiple Insurers, and Multiple Indemnity Environments",
    "url": "https://arxiv.org/abs/2606.30779",
    "source": "Zijun Meng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.30779v1 Announce Type: cross Abstract: This paper proves a sum-minimization characterization of Pareto efficient insurance with multiple policyholders, multiple insurers, and multiple indem"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.30986",
    "domain": "金融",
    "title": "The Organizational Behavior of Agentic AI: Collective Intelligence in Human-Agent Workflows",
    "url": "https://arxiv.org/abs/2606.30986",
    "source": "Canhui Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.30986v1 Announce Type: cross Abstract: Agentic artificial intelligence is increasingly deployed not as a single assistant but as a collective of planners, solvers, reviewers, memory manager"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31188",
    "domain": "金融",
    "title": "Social Statements: A Proposal for a Social-Value Balance Sheet and Profit-Loss Statement",
    "url": "https://arxiv.org/abs/2606.31188",
    "source": "Takeshi Kato, Yoshinori Hiroi, Sae Horiguchi, Tetsushi Koike, Shingo Hashimoto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.31188v1 Announce Type: cross Abstract: This study proposes a new set of a firm's \"social statements\" that represent social value, in contrast to conventional financial statements that repre"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.15080",
    "domain": "金融",
    "title": "Fast reliable pricing and calibration of the rough Heston model",
    "url": "https://arxiv.org/abs/2508.15080",
    "source": "Svetlana Boyarchenko, Marco de Innocentis, Sergei Levendorski\\u{i}",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2508.15080v3 Announce Type: replace Abstract: The paper is an extended and modified version of the preprint S.Boyarchenko and S.Levendorski\\u{i} ``Correct implied volatility shapes and reliable "
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.17481",
    "domain": "金融",
    "title": "Universalization and the Origins of Fiscal Capacity",
    "url": "https://arxiv.org/abs/2510.17481",
    "source": "Esteban Mu\\~noz-Sobrado",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2510.17481v3 Announce Type: replace Abstract: This paper proposes a model of tax compliance and fiscal capacity grounded in universalization reasoning. Citizens partially internalize the consequ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12446",
    "domain": "金融",
    "title": "Temporal Coarse-Graining of Latent Default-Probability Paths Generates Effective Default Correlation",
    "url": "https://arxiv.org/abs/2606.12446",
    "source": "Shintaro Mori",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.12446v2 Announce Type: replace Abstract: We show that persistent dynamics of a latent default-probability path can generate effective default correlation through temporal coarse-graining. I"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.21539",
    "domain": "金融",
    "title": "Attributing Forecast Gaps to Component Models in Complex Model Suites",
    "url": "https://arxiv.org/abs/2606.21539",
    "source": "Xuan Mei, Junze Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.21539v2 Announce Type: replace Abstract: Complex model suites composed of multiple interacting component models are widely used in financial forecasting and risk management. In model perfor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.21880",
    "domain": "金融",
    "title": "Human Capital, AI, and Labor Commoditization",
    "url": "https://arxiv.org/abs/2606.21880",
    "source": "Auyon Siddiq, Niuniu Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.21880v2 Announce Type: replace Abstract: Has generative AI changed how labor markets value human capital? We study this question using contract-level data from Upwork, a large online labor "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23596",
    "domain": "金融",
    "title": "Anatomy of the Market: A Body-Tail Test of Factor Models",
    "url": "https://arxiv.org/abs/2606.23596",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.23596v4 Announce Type: replace Abstract: In an ideal stochastic discount factor, zero pricing errors and maximum Sharpe ratio coincide; in a low-dimensional approximation they need not. I t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2107.11575",
    "domain": "金融",
    "title": "Peace Through Side Payments",
    "url": "https://arxiv.org/abs/2107.11575",
    "source": "Jingfeng Lu, Zongwei Lu, Christian Riis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2107.11575v4 Announce Type: replace-cross Abstract: We study strategic bargaining for peaceful settlement before conflict escalates into war (modeled as an all-pay auction), comparing two protoc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.25610",
    "domain": "金融",
    "title": "Match classification in the last round of four-team round-robin tournaments",
    "url": "https://arxiv.org/abs/2605.25610",
    "source": "L\\'aszl\\'o Csat\\'o, Andr\\'as Gyimesi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2605.25610v2 Announce Type: replace-cross Abstract: Classification of matches played in the last rounds of sports competitions is a well-established tool for evaluating tournament designs. Both "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19501",
    "domain": "金融",
    "title": "DeXposure-Claw: An Agentic System for DeFi Risk Supervision",
    "url": "https://arxiv.org/abs/2606.19501",
    "source": "Aijie Shu, Bowei Chen, Wenbin Wu, Cathy Yi-Hsuan Chen, Fengxiang He",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.19501v2 Announce Type: replace-cross Abstract: Decentralized finance exposes supervisors to fast-moving, networked credit risks. General-purpose LLM agents fit this setting poorly: they ove"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23032",
    "domain": "金融",
    "title": "IPO Finance Agent: Benchmark of LLM Financial Analysts Beyond Finance Agent v2, with Automated Rubric Generation, on the SpaceX (SPCX) IPO",
    "url": "https://arxiv.org/abs/2606.23032",
    "source": "Mostapha Benhenda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.23032v3 Announce Type: replace-cross Abstract: Finance Agent v2 (by Vals AI) has emerged as the reference benchmark for evaluating both Anthropic Claude and OpenAI ChatGPT frontier language"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29793",
    "domain": "金融",
    "title": "Fund2Persona: A Framework for Building and Refining Financial Advisor Personas from Fund Disclosure Data",
    "url": "https://arxiv.org/abs/2606.29793",
    "source": "Suhwan Park, Hoyoung Lee, Zhangyang Wang, Alejandro Lopez-Lira, Young Cha, Chanyeol Choi, Jaewon Choi, Yongjae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T04:00:00+00:00",
    "summary": "arXiv:2606.29793v2 Announce Type: replace-cross Abstract: Demand for personalized financial advising is growing, but consistent advisor expertise is difficult to obtain, scale, and encode in LLM syste"
  }
]
```
