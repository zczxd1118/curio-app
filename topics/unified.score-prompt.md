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

- 今日日期：`2026-06-13`
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
  "date": "2026-06-13",
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
    "points": 1080586,
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
    "points": 668097,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 662529,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 395515,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 383184,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 286598,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1cpEd66EjT",
    "domain": "AI",
    "title": "Claude Fable 5 首发实测，真是太烧了。。完爆 GPT 5.5！",
    "url": "http://www.bilibili.com/video/av116725718717656",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 240143,
    "published_at": "2026-06-10T12:11:13+00:00",
    "summary": "全球最贵的 AI 模型 Claude Fable 5 来了！这期视频带你看看它到底值不值，用两轮硬核实测对比 Fable 5、Opus 4.8 和 GPT-5.5 的 AI 编程能力。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n视频先带你了解 Claude Fable 5 的核心更新，包括 Fable "
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 240098,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 199063,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174244,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 167160,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 155096,
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
    "points": 148838,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 120447,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 90844,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 42880,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "🎉 Cursor 自定义API｜Cursor 自定义模型｜Cursor助手正式发布了！｜免费！",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 37217,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 35387,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 22855,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 17670,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1iAEE6ZEDq",
    "domain": "AI",
    "title": "【2026全网最新】2026 全网最优 Claude Code 教程！零基础从入门到精通，AI 编程手把手实战教学",
    "url": "http://www.bilibili.com/video/av116719695697025",
    "source": "阿飞教你学编程",
    "platform": "bilibili",
    "points": 14183,
    "published_at": "2026-06-09T10:40:48+00:00",
    "summary": "视频中的安装文档，整合包，模型，工作流，请查看置顶评论获取。"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13611,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1ZSVG6eE3V",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116662284130312",
    "source": "非六于期",
    "platform": "bilibili",
    "points": 10988,
    "published_at": "2026-05-30T07:13:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1QNEq6uEGM",
    "domain": "AI",
    "title": "全网最详细的Vibe Coding系统教程：Claude Code + Codex 从零到实战，存下吧！真的很难找全了",
    "url": "http://www.bilibili.com/video/av116731557186523",
    "source": "马士兵学堂",
    "platform": "bilibili",
    "points": 9084,
    "published_at": "2026-06-11T13:01:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1FXLJ6YELZ",
    "domain": "AI",
    "title": "Cursor无限薅最强大模型claude4.7，gpt5.5使用方法",
    "url": "http://www.bilibili.com/video/av116590041369141",
    "source": "长青来了奥",
    "platform": "bilibili",
    "points": 6752,
    "published_at": "2026-05-17T13:01:58+00:00",
    "summary": "一键三连吧！在主页\n自动回复私信要1000粉丝呜呜呜呜求帮忙"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6409,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1hhEB63ERD",
    "domain": "AI",
    "title": "比Cursor好用10倍的AI IDE，无痛项目管理",
    "url": "http://www.bilibili.com/video/av116732496779000",
    "source": "回力涛",
    "platform": "bilibili",
    "points": 4783,
    "published_at": "2026-06-11T16:53:23+00:00",
    "summary": "工具分享第三期。这个我最近真的用得有点上头。\n\n它叫 VibeYard，号称现在 Vibe Coding 圈里很能打的一个 IDE，专门给 AI Agent 做的。\n我上期讲过 CMUX，这个用下来比它顺手不少，而且 Claude Code、Codex、Gemini CLI 都能在里面管。\n\n说几个让我留下来的点。\n\n项目管理是按 Session 走的。一个项目对应一个 Session，新建的时候"
  },
  {
    "id": "bvid:BV1jWcvzmEzc",
    "domain": "AI",
    "title": "Houdini干货|houdini自己的AI agent（agent工具推荐分享）",
    "url": "http://www.bilibili.com/video/av116057012505638",
    "source": "tiny涵",
    "platform": "bilibili",
    "points": 4527,
    "published_at": "2026-02-12T09:45:41+00:00",
    "summary": "原作者教程：https://www.bilibili.com/video/BV1pwcbzBEEh/?spm_id_from=333.1387.list.card_archive.click&amp;vd_source=da5aa377b2acefadd001ffd4902eca9b\n\nGithub download：https://github.com/Kazama-Suichiku/Houdi"
  },
  {
    "id": "bvid:BV1MyEg6ZEdo",
    "domain": "AI",
    "title": "Cursor 免费版也能用自己的 API Key 了！",
    "url": "http://www.bilibili.com/video/av116713823672472",
    "source": "小由和小迪",
    "platform": "bilibili",
    "points": 3522,
    "published_at": "2026-06-08T09:43:10+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1sM6xB5EEE",
    "domain": "AI",
    "title": "基于LabVIEW的AI Agent智能体实现教程",
    "url": "http://www.bilibili.com/video/av115993393238477",
    "source": "三易电子工作室",
    "platform": "bilibili",
    "points": 3517,
    "published_at": "2026-02-01T04:12:23+00:00",
    "summary": "基于LabVIEW的AI Agent智能体实现教程，made by 三易电子工作室。"
  },
  {
    "id": "bvid:BV1G2Eq6GEe5",
    "domain": "AI",
    "title": "2026吃透Spring AI Alibaba Agent超详细全套教程（Tool/AI Agent Framework/Ollama/Graph）",
    "url": "http://www.bilibili.com/video/av116730768793011",
    "source": "图灵课堂",
    "platform": "bilibili",
    "points": 3281,
    "published_at": "2026-06-11T09:37:56+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套笔记和200万字面试宝典+场景题，简历模板，Java P 5~P8技术栈学习路线自取：https://www.bilibili.com/opus/765026283734171673?spm_id_from=333.1387.0.0"
  },
  {
    "id": "bvid:BV1jsEQ6XEw6",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116724292721480",
    "source": "倒计时19",
    "platform": "bilibili",
    "points": 2920,
    "published_at": "2026-06-10T06:04:26+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 2731,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "hn:48463808",
    "domain": "AI",
    "title": "Claude Fable 5",
    "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5",
    "source": "Philpax",
    "platform": "hackernews",
    "points": 2612,
    "published_at": "2026-06-09T16:58:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48511072",
    "domain": "AI",
    "title": "Statement on US government directive to suspend access to Fable 5 and Mythos 5",
    "url": "https://www.anthropic.com/news/fable-mythos-access",
    "source": "Dylan1312",
    "platform": "hackernews",
    "points": 1895,
    "published_at": "2026-06-13T00:51:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48421442",
    "domain": "AI",
    "title": "S&P 500 rejects SpaceX, also blocking entry for OpenAI and Anthropic",
    "url": "https://arstechnica.com/tech-policy/2026/06/sp-500-blocks-fast-spacex-entry-wont-waive-rule-for-unprofitable-ai-firms/",
    "source": "maltalex",
    "platform": "hackernews",
    "points": 1479,
    "published_at": "2026-06-06T04:38:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48500012",
    "domain": "AI",
    "title": "AI agent bankrupted their operator while trying to scan DN42",
    "url": "https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/",
    "source": "xiaoyu2006",
    "platform": "hackernews",
    "points": 1410,
    "published_at": "2026-06-12T04:42:53+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1EnJj6aEBf",
    "domain": "AI",
    "title": "【MC大型RPG】六月最新我的世界RPG服务器！数值平衡不伤肝！支持搬砖打金！手机电脑双端互通！新服开荒中！",
    "url": "http://www.bilibili.com/video/av116738385513888",
    "source": "Minecraft-云雾灵境",
    "platform": "bilibili",
    "points": 1394,
    "published_at": "2026-06-12T17:50:48+00:00",
    "summary": "云雾灵境-大型修仙RPG全新开荒！\n服务器官方群号:310463584\n我们拥有十分方便的挂机系统 — —只需按下特殊按键即可触发自动打怪，刷取材料不二之选\n拥有平衡的战斗数值系统 — — 防止因数值膨胀而导致的战力崩坏\n强化、分解、镶嵌、锻造 — — 拥有超多的RPG玩法以及独有的修仙加点玩法\n我们还拥有自由交易的全球市场以及各种各样随着节假日更新的活动\n当然以上的只是服务器玩法的一部分，更多的"
  },
  {
    "id": "bvid:BV1hQJV6CEac",
    "domain": "AI",
    "title": "【Vibe Coding实况】用 Godot + Cursor 打造类幸存者游戏并上架 Steam（01：项目初始化）",
    "url": "http://www.bilibili.com/video/av116737865418900",
    "source": "玩物不丧志的老李",
    "platform": "bilibili",
    "points": 918,
    "published_at": "2026-06-12T15:37:44+00:00",
    "summary": "老李提问：第一期带大家用 Cursor 跑通了 HelloWorld 。视频最后提到的【子节点先 ready，父节点后 ready】在实际做类幸存者怪物的血条或者弹幕初始化时会引发什么致命 Bug？欢迎在评论区交作业，猜对的同学老李下期视频在线翻牌！"
  },
  {
    "id": "bvid:BV1XaE96REta",
    "domain": "AI",
    "title": "【2026最新版】这绝对是B站唯一将MCP入门+实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！学完即就业，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116725047625978",
    "source": "ollama本地部署",
    "platform": "bilibili",
    "points": 947,
    "published_at": "2026-06-10T09:22:30+00:00",
    "summary": "视频配套的学习资料已经整理好了，如需领取戳👉https://b23.tv/Qdi8fs5\n无论是新手小白，还是有一定编码经验的选手，皆可学习"
  },
  {
    "id": "bvid:BV1TmJE6QE9C",
    "domain": "AI",
    "title": "我的世界SMP服务器生存26.1.2版本支持基岩！",
    "url": "http://www.bilibili.com/video/av116741069867205",
    "source": "B1tc我的世界服务器",
    "platform": "bilibili",
    "points": 824,
    "published_at": "2026-06-13T05:12:57+00:00",
    "summary": "===========================\nB1tc服务器欢迎您\n审核群1081591299\n审核非常快秒通过！无需等待\n==========================="
  },
  {
    "id": "bvid:BV1KPJ56iEFd",
    "domain": "AI",
    "title": "Claude Code 插件生态全景：10 个必装插件，从裸装到完整开发环境",
    "url": "http://www.bilibili.com/video/av116737999768349",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 725,
    "published_at": "2026-06-12T16:09:32+00:00",
    "summary": "Claude Code 插件生态全景：10 个必装插件，从裸装到完整开发环境\n\n裸装 Claude Code 的四个痛点：跨 session 没记忆、不能实时访问网络、没法做浏览器测试、缺少安全门槛。装上这 10 个插件，思考、测试、review、部署一条龙，从&quot;能用&quot;直接变&quot;完整开发环境&quot;。\n\n📌 推荐安装顺序\n\n【第一阶段：核心三件套】\n\n1. Secu"
  },
  {
    "id": "hn:48364055",
    "domain": "AI",
    "title": "Can the stockmarket swallow Anthropic, SpaceX and OpenAI?",
    "url": "https://www.economist.com/finance-and-economics/2026/06/01/can-the-stockmarket-swallow-anthropic-spacex-and-openai",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 724,
    "published_at": "2026-06-01T23:45:46+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1gRJV6kEE6",
    "domain": "AI",
    "title": "我的世界基岩版91服务器PVP战争宣传片",
    "url": "http://www.bilibili.com/video/av116737764887392",
    "source": "落锤暗区突围",
    "platform": "bilibili",
    "points": 624,
    "published_at": "2026-06-12T15:10:59+00:00",
    "summary": "-"
  },
  {
    "id": "hn:48464258",
    "domain": "AI",
    "title": "Anthropic requires 30 day data retention for Fable and Mythos",
    "url": "https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models",
    "source": "lebovic",
    "platform": "hackernews",
    "points": 599,
    "published_at": "2026-06-09T17:23:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14GJE61EwC",
    "domain": "AI",
    "title": "Cursor的完美替代，终于不卡了",
    "url": "http://www.bilibili.com/video/av116739509589437",
    "source": "鸡蛋灌饼工程师",
    "platform": "bilibili",
    "points": 565,
    "published_at": "2026-06-12T22:35:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48478969",
    "domain": "AI",
    "title": "Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable",
    "url": "https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 587,
    "published_at": "2026-06-10T16:42:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:48484584",
    "domain": "AI",
    "title": "AI agent runs amok in Fedora and elsewhere",
    "url": "https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 549,
    "published_at": "2026-06-11T00:10:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48489229",
    "domain": "AI",
    "title": "Anthropic apologizes for invisible Claude Fable guardrails",
    "url": "https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail",
    "source": "rarisma",
    "platform": "hackernews",
    "points": 502,
    "published_at": "2026-06-11T12:05:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48434436",
    "domain": "AI",
    "title": "Anthropic, please ship an official Claude Desktop for Linux",
    "url": "https://github.com/anthropics/claude-code/issues/65697",
    "source": "predkambrij",
    "platform": "hackernews",
    "points": 537,
    "published_at": "2026-06-07T13:06:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 472,
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
    "points": 428,
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
    "points": 330,
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
    "points": 287,
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
    "points": 150,
    "published_at": "2026-06-01T13:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48509844",
    "domain": "AI 算力 / 半导体",
    "title": "SkillSpector",
    "url": "https://github.com/NVIDIA/SkillSpector",
    "source": "taubek",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-06-12T21:49:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356312",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity",
    "url": "https://news.ycombinator.com/item?id=48356312",
    "source": "ismaeel_bashir",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/uclas-125m-semiconductor-hub-we-want-high-impact-not-incremental-research/",
    "domain": "AI 算力 / 半导体",
    "title": "UCLA’s $125M Semiconductor Hub: “We Want High Impact, Not Incremental Research”",
    "url": "https://www.eetimes.com/uclas-125m-semiconductor-hub-we-want-high-impact-not-incremental-research/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T19:00:00+00:00",
    "summary": "UCLA launches a $125M semiconductor hub to smash chip bottlenecks with AI research. The post UCLA’s $125M Semiconductor Hub: “We Want High Impact, Not Incremental Research” appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/tecate-group-announces-new-ultracapacitor-cells-rated-foroperation-up-to-105c-221f/",
    "domain": "AI 算力 / 半导体",
    "title": "Tecate Group Announces New Ultracapacitor Cells Rated forOperation up to 105°C (221°F)",
    "url": "https://www.eetimes.com/tecate-group-announces-new-ultracapacitor-cells-rated-foroperation-up-to-105c-221f/",
    "source": "Tecate Group",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:49:02+00:00",
    "summary": "San Diego, CA: June 1, 2026. Tecate Group today announced the expansion of its ultracapacitorproduct offerings with new cells rated for operation up to 105°C (221°F). The new TPLT productseries is rat"
  },
  {
    "id": "rss:https://www.eetimes.com/peak-goes-automotive-ethernet-pae-media-converter-connects-100-1000base-t1-with-standard-ethernet/",
    "domain": "AI 算力 / 半导体",
    "title": "PEAK Goes Automotive Ethernet: PAE-Media Converter connects 100/1000BASE-T1 with Standard Ethernet",
    "url": "https://www.eetimes.com/peak-goes-automotive-ethernet-pae-media-converter-connects-100-1000base-t1-with-standard-ethernet/",
    "source": "HMS Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:01:05+00:00",
    "summary": "Unique Features for Automotive Testing The PAE-Media Converter addresses crucial market challenges in automotive development and validation with three core innovations. It enables realistic fault simu"
  },
  {
    "id": "rss:https://www.eetimes.com/indian-firm-scales-single-walled-carbon-nanotube-production-for-batteries-and-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Firm Scales Single-Walled Carbon Nanotube Production for Batteries and Chips",
    "url": "https://www.eetimes.com/indian-firm-scales-single-walled-carbon-nanotube-production-for-batteries-and-chips/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T08:04:16+00:00",
    "summary": "NoPo scales HiPco single-walled carbon nanotube output for sub-2-nm chips and anodes. The post Indian Firm Scales Single-Walled Carbon Nanotube Production for Batteries and Chips appeared first on EE "
  },
  {
    "id": "rss:https://www.eetimes.com/rebellions-bets-on-memory-centric-architecture-as-it-weighs-ipo-options/",
    "domain": "AI 算力 / 半导体",
    "title": "Rebellions Bets on Memory-Centric Architecture as It Weighs IPO Options",
    "url": "https://www.eetimes.com/rebellions-bets-on-memory-centric-architecture-as-it-weighs-ipo-options/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T22:00:00+00:00",
    "summary": "Rebellions leverages memory-centric AI chip designs with SK Hynix and Samsung to fuel IPO ambitions. The post Rebellions Bets on Memory-Centric Architecture as It Weighs IPO Options appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/gigadevice-introduces-gd32e512-and-gd32e252-mcus-for-optical-modules/",
    "domain": "AI 算力 / 半导体",
    "title": "GigaDevice Introduces GD32E512 and GD32E252 MCUs for Optical Modules",
    "url": "https://www.eetimes.com/gigadevice-introduces-gd32e512-and-gd32e252-mcus-for-optical-modules/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:00:00+00:00",
    "summary": "GigaDevice has introduced the new GD32E512 and GD32E252 series MCUs specifically designed for optical module applications. The post GigaDevice Introduces GD32E512 and GD32E252 MCUs for Optical Modules"
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-targets-data-centers-edge-ai-space/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Targets Data Centers, Edge AI, Space",
    "url": "https://www.eetimes.com/risc-v-targets-data-centers-edge-ai-space/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T13:24:38+00:00",
    "summary": "\"RISC-V is now,\" said Andrea Gallo, CEO of RISC-V International, during his keynote at this week's RISC-V Summit Europe 2026 in Bologna. The post RISC-V Targets Data Centers, Edge AI, Space appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/logistics-leaders-navigate-cost-and-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "Logistics Leaders Navigate Cost and Automation",
    "url": "https://www.eetimes.com/logistics-leaders-navigate-cost-and-automation/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T08:11:49+00:00",
    "summary": "Gartner's VP analyst David Gonzalez shares strategies for profitability and technology in supply chain management. The post Logistics Leaders Navigate Cost and Automation appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-offers-china-early-access-to-vera-cpus-as-h200-sales-stay-frozen",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia preps to sell its Vera CPUs into China as its GPU sales stay frozen — customers encouraged to place orders for CPU shipments as early as August",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-offers-china-early-access-to-vera-cpus-as-h200-sales-stay-frozen",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:17:42+00:00",
    "summary": "Nvidia has told Chinese clients that its Arm-based Vera server CPUs could be available as soon as August."
  },
  {
    "id": "rss:https://www.tomshardware.com/tag/prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon Prime Day",
    "url": "https://www.tomshardware.com/tag/prime-day",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:12:44+00:00",
    "summary": "Amazon Prime Day"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/thrustmasters-new-specialized-t-flight-hotas-5-microsoft-flight-simulator-edition-provides-a-plug-and-play-flight-sim-setup-for-just-usd109-featuring-5-axis-control-with-16-bit-precision-and-dual-rudder-system",
    "domain": "AI 算力 / 半导体",
    "title": "Thrustmaster's new specialized T.Flight Hotas 5 Microsoft Flight Simulator Edition provides a plug-and-play flight sim setup for just $109 — featuring 5-axis control with 16-bit precision and dual-rud",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/thrustmasters-new-specialized-t-flight-hotas-5-microsoft-flight-simulator-edition-provides-a-plug-and-play-flight-sim-setup-for-just-usd109-featuring-5-axis-control-with-16-bit-precision-and-dual-rudder-system",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:05:13+00:00",
    "summary": "Rocking 16-bit precision, dual-rudder yaw, 5-axis control and a plug-and-play profile for Microsoft Flight Simulator 2024, the new T.Flight Hotas 5 is a solid entry point to flight sims. It works with"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/radeon-rx-9070-xt-finally-appears-in-steam-hardware-survey-rdna-4-flagship-surprisingly-lands-just-behind-rtx-5080",
    "domain": "AI 算力 / 半导体",
    "title": "Radeon RX 9070 XT finally appears in Steam Hardware Survey — RDNA 4 flagship surprisingly lands just behind RTX 5080",
    "url": "https://www.tomshardware.com/pc-components/gpus/radeon-rx-9070-xt-finally-appears-in-steam-hardware-survey-rdna-4-flagship-surprisingly-lands-just-behind-rtx-5080",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T15:09:30+00:00",
    "summary": "AMD’s Radeon RX 9070 XT graphics card has finally penetrated the Steam Survey video card results table, going straight in at position 25."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/nvidias-high-speed-ai-data-center-storage-servers-break-cover-touting-2-9-petabytes-of-storage-and-extreme-pcie-6-0-performance-wiwynn-shows-off-scada-server-with-gpu-accelerated-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's high-speed AI data center storage servers break cover, touting 2.9 petabytes of storage and extreme PCIe 6.0 performance — Wiwynn shows off SCADA server with GPU-accelerated storage",
    "url": "https://www.tomshardware.com/pc-components/ssds/nvidias-high-speed-ai-data-center-storage-servers-break-cover-touting-2-9-petabytes-of-storage-and-extreme-pcie-6-0-performance-wiwynn-shows-off-scada-server-with-gpu-accelerated-storage",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T15:01:59+00:00",
    "summary": "Wiwynn is among the first to demonstrate Nvidia SCADA server that promises to offer AI systems petabytes of ultra-fast storage thanks to GPU-accelerated storage acceleration."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/microsofts-bug-hunting-nemesis-extends-vendetta-with-more-zero-day-attacks-nightmare-eclipse-publishes-rogueplanet-and-greatxml-local-privilege-escalation-exploits",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft's bug-hunting nemesis extends vendetta with more zero-day attacks — Nightmare Eclipse publishes RoguePlanet and GreatXML local privilege escalation exploits",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/microsofts-bug-hunting-nemesis-extends-vendetta-with-more-zero-day-attacks-nightmare-eclipse-publishes-rogueplanet-and-greatxml-local-privilege-escalation-exploits",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T14:48:03+00:00",
    "summary": "Nightmare-Eclipse's vendetta against Microsoft and Windows continues apace — researcher publishes RoguePlanet and GreatXML local privilege escalation zero-day exploits"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/various-vendors-add-amd-expo-ultra-low-latency-to-600-series-motherboards-in-latest-bios-updates-tech-tightens-memory-subtimings-on-compatible-kits-boosting-fps-by-up-to-4-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Various vendors add AMD EXPO Ultra-Low Latency to 600-series motherboards in latest BIOS updates — tech tightens memory subtimings on compatible kits, boosting FPS by up to 4%",
    "url": "https://www.tomshardware.com/pc-components/motherboards/various-vendors-add-amd-expo-ultra-low-latency-to-600-series-motherboards-in-latest-bios-updates-tech-tightens-memory-subtimings-on-compatible-kits-boosting-fps-by-up-to-4-percent",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T14:17:36+00:00",
    "summary": "New BIOS updates featuring AMD EXPO Ultra Low Latency support are being released across a plethora of 600-series motherboards by multiple vendors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/republican-lawmakers-urge-itc-to-block-imports-of-infringing-tsmc-chips-as-patent-ruling-imminent",
    "domain": "AI 算力 / 半导体",
    "title": "Republican lawmakers urge federal agency to block imports of infringing TSMC chips as patent ruling nears — five asserted U.S. patents come from United Microelectronics Corporation",
    "url": "https://www.tomshardware.com/tech-industry/republican-lawmakers-urge-itc-to-block-imports-of-infringing-tsmc-chips-as-patent-ruling-imminent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T13:29:20+00:00",
    "summary": "Four Republican members of Congress have urged the U.S. ITC to block imports of foreign-made chips found to infringe U.S. patents"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-usd300-on-gigabytes-gaming-a16-gaming-laptop-at-walmart-budget-rtx-5060-powered-16-inch-laptop-is-now-only-usd1-199",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on Gigabyte's Gaming A16 gaming laptop at Walmart — Budget RTX 5060 -powered 16-inch laptop is now only $1,199",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-usd300-on-gigabytes-gaming-a16-gaming-laptop-at-walmart-budget-rtx-5060-powered-16-inch-laptop-is-now-only-usd1-199",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T11:29:07+00:00",
    "summary": "Save $300 on Gigabyte's Gaming A16 gaming laptop at Walmart. Budget RTX 5060 -powered 16-inch laptop is now only $1,199."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd751-on-this-rtx-5070-ti-gaming-pc-with-a-9800x3d-right-now-liquid-cooled-4k-ready-skytech-rig-with-32gb-ddr5-and-a-2tb-ssd-is-now-just-usd2-249",
    "domain": "AI 算力 / 半导体",
    "title": "Save a massive $751 on this RTX 5070 Ti gaming PC with a 9800X3D right now — liquid-cooled, 4K-ready Skytech rig with 32GB DDR5 and a 2TB SSD is now just $2,249",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd751-on-this-rtx-5070-ti-gaming-pc-with-a-9800x3d-right-now-liquid-cooled-4k-ready-skytech-rig-with-32gb-ddr5-and-a-2tb-ssd-is-now-just-usd2-249",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T11:15:31+00:00",
    "summary": "Save $750 on this Skytech gaming PC for gaming at 1440p and 4K, featuring a 9800X3D, RTX 5070 Ti, 32GB DDR5, and a 2 TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/xbox-will-pay-five-times-more-for-components-in-2027-than-it-did-two-years-ago-ceo-asha-sharma-admits-theres-an-unsustainable-hardware-gap-that-cannot-continue",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox will pay five times more for memory and storage in 2027 than it did two years ago — CEO Asha Sharma admits there's an unsustainable hardware gap that 'cannot continue'",
    "url": "https://www.tomshardware.com/video-games/xbox/xbox-will-pay-five-times-more-for-components-in-2027-than-it-did-two-years-ago-ceo-asha-sharma-admits-theres-an-unsustainable-hardware-gap-that-cannot-continue",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T11:00:00+00:00",
    "summary": "The next-gen Xbox Helix is looking in trouble due to surging memory and storage costs that are forcing even a giant like Microsoft to bend down."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-ram-for-only-usd255-in-this-2-item-combo-from-newegg-just-usd514-99-gets-you-corsair-vengeance-rgb-ram-and-a-gigabyte-x870-aorus-elite-motherboard-26-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB of DDR5 RAM for only $255 in this 2-item combo from Newegg — just $514.99 gets you Corsair Vengeance RGB RAM and a Gigabyte X870 Aorus Elite motherboard, 26% off",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-ram-for-only-usd255-in-this-2-item-combo-from-newegg-just-usd514-99-gets-you-corsair-vengeance-rgb-ram-and-a-gigabyte-x870-aorus-elite-motherboard-26-percent-off",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T10:42:16+00:00",
    "summary": "Newegg slashes ~$185 off this 2-item combo, dropping the RAM to an affordable $255 - just $514.99 gets you a solid Gigabyte X870 motherboards, and 32GB of RAM in this incredible Newegg combo deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hades-malware-campaign-now-tricks-ai-bots-by-injecting-text-about-biological-and-nuclear-weapons-failsafe-mechanisms-triggered-by-prompts-for-weapon-creation-stop-scans-before-payload-is-seen",
    "domain": "AI 算力 / 半导体",
    "title": "New malware campaign tricks AI scanners with fake nuclear weapon prompts — malicious code triggers safety failsafes so scanners skip the payload",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hades-malware-campaign-now-tricks-ai-bots-by-injecting-text-about-biological-and-nuclear-weapons-failsafe-mechanisms-triggered-by-prompts-for-weapon-creation-stop-scans-before-payload-is-seen",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T10:30:00+00:00",
    "summary": "Hades malware campaign now tricks AI bots into not scanning development packages, as prompts for bio- and nuclear weapons trigger failsafe mechanisms."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/amd-denies-researcher-a-usd10-000-bug-bounty-after-fixing-critical-auto-updater-vulnerability-security-flaw-took-124-days-to-patch",
    "domain": "AI 算力 / 半导体",
    "title": "AMD denies researcher a $10,000 bug bounty after fixing critical auto-updater vulnerability — security flaw took 124 days to patch",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/amd-denies-researcher-a-usd10-000-bug-bounty-after-fixing-critical-auto-updater-vulnerability-security-flaw-took-124-days-to-patch",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T10:00:00+00:00",
    "summary": "AMD took over four months to fix a critical security bug in its autoupdater, and the security researcher didn't see a dime for his efforts"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/security-software/several-police-officers-arrested-for-using-controversial-flock-ai-license-plate-reader-system-to-stalk-romantic-partners-says-report-investigators-have-unearthed-at-least-18-such-cases-in-the-us-over-recent-years",
    "domain": "AI 算力 / 半导体",
    "title": "Several police officers arrested for using controversial Flock AI license plate reader system to stalk romantic partners, says report — investigators have unearthed at least 18 such cases in the US ov",
    "url": "https://www.tomshardware.com/software/security-software/several-police-officers-arrested-for-using-controversial-flock-ai-license-plate-reader-system-to-stalk-romantic-partners-says-report-investigators-have-unearthed-at-least-18-such-cases-in-the-us-over-recent-years",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T09:30:00+00:00",
    "summary": "Tens of officers have been fired, and some even arrested, for abuse of the Flock license plate reader system used by police departments throughout the US, according to a new report."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-bans-china-linked-chatgpt-accounts-that-amplified-us-data-center-electricity-price-backlash",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI bans China-linked ChatGPT accounts that amplified US data center electricity price backlash — used AI-generated cartoons to stoke fears over U.S. data center energy costs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-bans-china-linked-chatgpt-accounts-that-amplified-us-data-center-electricity-price-backlash",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T18:48:34+00:00",
    "summary": "OpenAI says it has banned two clusters of ChatGPT accounts it believes are operating from China, and that used its models for covert influence campaigns targeting U.S. tech and policy debates."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/memory-famine-compels-gpu-vendors-to-re-release-2020-graphics-cards-geforce-rtx-3060-and-geforce-rtx-3050-return-to-asian-market",
    "domain": "AI 算力 / 半导体",
    "title": "Memory famine compels GPU vendors to re-release 2020 graphics cards — GeForce RTX 3060 and GeForce RTX 3050 return to Asian market",
    "url": "https://www.tomshardware.com/pc-components/gpus/memory-famine-compels-gpu-vendors-to-re-release-2020-graphics-cards-geforce-rtx-3060-and-geforce-rtx-3050-return-to-asian-market",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:33:50+00:00",
    "summary": "Graphics card manufacturer Manli adds new GeForce RTX 3060 and GeForce RTX 3050 SKUs to its portfolio."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-cuts-manus-off-from-its-internal-systems-as-china-ordered-breakup-of-2-billion-ai-deal-begins",
    "domain": "AI 算力 / 半导体",
    "title": "After spat with Chinese gov't, Meta cuts AI Manus off from its internal systems and is 'sunsetting' platform, report claims — Beijing-ordered breakup of $2 billion AI deal begins",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-cuts-manus-off-from-its-internal-systems-as-china-ordered-breakup-of-2-billion-ai-deal-begins",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T14:47:26+00:00",
    "summary": "Meta has finished separating its operations from Manus, the Chinese-founded agentic AI startup it acquired for roughly $2 billion in December."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-18-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Blade 18 (2026) review: Coming in fast and hot",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-18-2026-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T12:57:02+00:00",
    "summary": "The Razer Blade 18 is a large gaming rig with an 18-inch dual-mode display and strong performance, but it runs hot and is very expensive."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/watching-the-world-cup-online-shouldnt-risk-your-precious-data-or-cost-you-the-earth-save-money-on-these-vpn-deals-now",
    "domain": "AI 算力 / 半导体",
    "title": "Watching the World Cup online is easier with these VPN deals — deals for watching the FIFA World Cup 2026",
    "url": "https://www.tomshardware.com/software/vpn/watching-the-world-cup-online-shouldnt-risk-your-precious-data-or-cost-you-the-earth-save-money-on-these-vpn-deals-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T12:35:37+00:00",
    "summary": "A choice of VPN subscriptions to cover you over the FIFA World Cup 2026 and beyond. Stay safe online for less."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mice/logi-mobi-fold-portable-mouse-bends-in-half-and-slides-neatly-into-your-pocket-wireless-mouse-has-a-battery-life-that-will-last-up-to-a-month",
    "domain": "AI 算力 / 半导体",
    "title": "Logi Mobi Fold portable mouse bends in half and slides neatly into your pocket — wireless mouse has a month-long battery life",
    "url": "https://www.tomshardware.com/peripherals/mice/logi-mobi-fold-portable-mouse-bends-in-half-and-slides-neatly-into-your-pocket-wireless-mouse-has-a-battery-life-that-will-last-up-to-a-month",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T11:20:00+00:00",
    "summary": "Logitech's new Mobi Fold mouse neatly bends in half and can be easily carried around in a pocket, making it ideal for laptop users on the go, and far less bulky than conventional offerings, while havi"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/gaming-pc-deflects-bullet-shot-through-wall-by-neighbour-saving-owners-life-criminal-negligence-charges-for-culprit-who-claims-firearm-was-accidentally-discharged-by-her-dog",
    "domain": "AI 算力 / 半导体",
    "title": "Gaming PC deflects bullet shot through wall by neighbour, saving owner's life — criminal negligence charges for culprit who claims 'firearm was accidentally discharged by her dog'",
    "url": "https://www.tomshardware.com/desktops/pc-building/gaming-pc-deflects-bullet-shot-through-wall-by-neighbour-saving-owners-life-criminal-negligence-charges-for-culprit-who-claims-firearm-was-accidentally-discharged-by-her-dog",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T11:10:01+00:00",
    "summary": "A Redditor's powerful gaming PC just might have just saved their life after its splintered G.Skill RAM sticks diverted a bullet shot through the wall."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/crushing-shortages-force-biwin-into-usd1-86-billion-nand-deal-for-ssds-multi-year-agreement-locks-in-fixed-pricing-as-spot-market-threatens-to-dry-up",
    "domain": "AI 算力 / 半导体",
    "title": "Crushing shortages force Biwin into $1.86 billion NAND deal for SSDs — multi-year agreement locks in fixed pricing as spot market threatens to dry up",
    "url": "https://www.tomshardware.com/pc-components/ssds/crushing-shortages-force-biwin-into-usd1-86-billion-nand-deal-for-ssds-multi-year-agreement-locks-in-fixed-pricing-as-spot-market-threatens-to-dry-up",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T11:00:00+00:00",
    "summary": "Biwin signs a 24-months supply agreement with an unknown NAND maker to get memory worth $1.86 billion."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-ddr5-for-just-usd280-usd100-less-than-elsewhere-in-this-epic-newegg-combo-deal-save-23-percent-on-this-gaming-pc-parts-bundle-featuring-intels-fastest-gaming-cpu-in-years-along-with-a-z890-motherboard-for-just-usd769-99",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB DDR5 for just $280, $100 less than elsewhere, in this epic Newegg combo deal — save 23% on this gaming PC parts bundle featuring Intel's fastest gaming CPU in years, along with a Z890 motherb",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-ddr5-for-just-usd280-usd100-less-than-elsewhere-in-this-epic-newegg-combo-deal-save-23-percent-on-this-gaming-pc-parts-bundle-featuring-intels-fastest-gaming-cpu-in-years-along-with-a-z890-motherboard-for-just-usd769-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:53:46+00:00",
    "summary": "Save $230 on this fast Intel Core Ultra 7 270K Plus CPU with a Z890 motherboard and 32GB of DDR5-6000 memory, now just $769.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/ai-is-set-to-consume-up-to-600-billion-gallons-of-water-by-2030-rising-energy-consumption-primarily-to-blame-as-data-center-power-demands-rise",
    "domain": "AI 算力 / 半导体",
    "title": "AI is set to consume up to 600 billion gallons of water by 2030 — rising energy consumption primarily to blame as data center power demands rise",
    "url": "https://www.tomshardware.com/tech-industry/ai-is-set-to-consume-up-to-600-billion-gallons-of-water-by-2030-rising-energy-consumption-primarily-to-blame-as-data-center-power-demands-rise",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:32:06+00:00",
    "summary": "Direct cooling data center GPUs uses only a fraction of the water required to keep them running, and with plans for future GPUs and rack systems to be even more power hungry, this problem could make d"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/8tb-sd-cards-are-set-to-ship-shortly-after-a-two-year-delay-mind-blowing-storage-at-possibly-bank-breaking-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Massive 8TB SD cards are set to ship 'shortly' after a two-year delay — mind-blowing storage at possibly bank-breaking prices",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/8tb-sd-cards-are-set-to-ship-shortly-after-a-two-year-delay-mind-blowing-storage-at-possibly-bank-breaking-prices",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:30:00+00:00",
    "summary": "Notebookcheck reports that 8TB SD cards will soon hit the retail market, although an exact launch date and pricing remain a mystery."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/we-tested-20-wall-chargers-from-cheap-to-expensive-to-see-what-we-would-find-from-15-140w-with-screens-and-without",
    "domain": "AI 算力 / 半导体",
    "title": "We tested 20 wall chargers, from cheap to expensive, to find the best — from 15W to 140W, here are the chargers that perform the best without overheating and throttling",
    "url": "https://www.tomshardware.com/peripherals/usb/we-tested-20-wall-chargers-from-cheap-to-expensive-to-see-what-we-would-find-from-15-140w-with-screens-and-without",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:10:00+00:00",
    "summary": "We tested the top 20 chargers on the market across different power segments to find out which models provide the most consistent power and the best charging experience without thermal throttling."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/louis-rossman-threatens-to-take-samsung-to-court-over-dead-4tb-990-pro-ssd-after-ssd-maker-failed-to-replace-the-drive-under-warranty",
    "domain": "AI 算力 / 半导体",
    "title": "Louis Rossmann is suing Samsung after firm offers $330 refund for defective SSD while selling the drives on Amazon for $949 — spat over 4TB 990 Pro SSD is headed to court",
    "url": "https://www.tomshardware.com/pc-components/ssds/louis-rossman-threatens-to-take-samsung-to-court-over-dead-4tb-990-pro-ssd-after-ssd-maker-failed-to-replace-the-drive-under-warranty",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:00:00+00:00",
    "summary": "Right to Repair activist Louis Rossman threatens to sue Samsung after the SSD maker failed to replace his dead 990 Pro 4TB SSD under warranty."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nashville-considers-hyperscale-data-center-ban-as-zoo-dispute-escalates",
    "domain": "AI 算力 / 半导体",
    "title": "Brad Paisley joins fight as zoo's dispute with AI data center escalates, petition tops 330,000 signatures — Nashville weighs sweeping hyperscale ban",
    "url": "https://www.tomshardware.com/tech-industry/nashville-considers-hyperscale-data-center-ban-as-zoo-dispute-escalates",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T09:30:00+00:00",
    "summary": "An ongoing fight over a proposed data center sited just 50 yards from Nashville Zoo has escalated further, with the zoo’s land use attorney filing a zoning appeal to overturn permits already approved."
  },
  {
    "id": "hn:48444451",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia partners with LG robotics to build humanoid robots in South Korea",
    "url": "https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/",
    "source": "spwa4",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-06-08T12:25:14+00:00",
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
    "id": "rss:https://www.eetimes.com/startup-ricursive-to-create-an-end-to-end-ai-model-for-chip-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Startup Ricursive to Create an End-to-End AI Model for Chip Design",
    "url": "https://www.eetimes.com/startup-ricursive-to-create-an-end-to-end-ai-model-for-chip-design/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:26:51+00:00",
    "summary": "“We are definitely not an EDA company,” Ricursive co-founders told EE Times. The post Startup Ricursive to Create an End-to-End AI Model for Chip Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/massive-ai-storage-demand-creates-a-new-memory-wall/",
    "domain": "AI 算力 / 半导体",
    "title": "Massive AI Storage Demand Creates a New Memory Wall",
    "url": "https://www.eetimes.com/massive-ai-storage-demand-creates-a-new-memory-wall/",
    "source": "Alper Ilkbahar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:22:01+00:00",
    "summary": "As AI models scale to trillions of parameters, conventional memory architectures face mounting capacity and efficiency constraints. The post Massive AI Storage Demand Creates a New Memory Wall appeare"
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
    "id": "hn:48450142",
    "domain": "大厂 AI 动态",
    "title": "Apple reveals new AI architecture built around Google Gemini models",
    "url": "https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/",
    "source": "unclefuzzy",
    "platform": "hackernews",
    "points": 732,
    "published_at": "2026-06-08T19:14:47+00:00",
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
    "id": "hn:48449084",
    "domain": "大厂 AI 动态",
    "title": "Siri AI",
    "url": "https://www.apple.com/apple-intelligence/",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 678,
    "published_at": "2026-06-08T18:17:53+00:00",
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
    "id": "rss:https://www.theverge.com/news/949517/valve-vr-headset-import-records-steam-frame-steam-machine-game-console",
    "domain": "大厂 AI 动态",
    "title": "Valve just imported 13 tons of VR headsets in one day",
    "url": "https://www.theverge.com/news/949517/valve-vr-headset-import-records-steam-frame-steam-machine-game-console",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T01:32:18+00:00",
    "summary": "On June 10th, the German container ship Posen docked in Los Angeles after a two-week voyage from Shanghai. As Valve watcher Brad Lynch notes, it was almost certainly carrying the first mass production"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/949403/nothing-carl-pei-ram-phone-prices",
    "domain": "大厂 AI 动态",
    "title": "Nothing CEO says phone prices are going to keep going up",
    "url": "https://www.theverge.com/gadgets/949403/nothing-carl-pei-ram-phone-prices",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T20:02:48+00:00",
    "summary": "If you're thinking about upgrading your phone, \"the best time was yesterday,\" according to Nothing CEO and co-founder Carl Pei, echoing a message we heard during MWC. As Android Authority reports, Pei"
  },
  {
    "id": "rss:https://www.theverge.com/tech/949259/the-worlds-first-trillionaire-is-a-killer",
    "domain": "大厂 AI 动态",
    "title": "The world’s first trillionaire is a killer",
    "url": "https://www.theverge.com/tech/949259/the-worlds-first-trillionaire-is-a-killer",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:46:40+00:00",
    "summary": "Elon Musk's SpaceX IPO will probably make him the richest person to ever walk the planet. And while his mountain of horrible personal conduct could fill multiple books, one fact in particular stands o"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/949079/siri-ai-good-vergecast",
    "domain": "大厂 AI 动态",
    "title": "Siri is good now??",
    "url": "https://www.theverge.com/podcast/949079/siri-ai-good-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:17:04+00:00",
    "summary": "You'd be forgiven for thinking this day would never come. Siri has spent a decade and half somewhere between \"sort of useful at a few things\" and \"utterly disastrous, why did I even try, can it honest"
  },
  {
    "id": "rss:https://www.theverge.com/tech/948917/elon-musk-trillionaire-how-much-visualization",
    "domain": "大厂 AI 动态",
    "title": "A trillion dollars is a stupid amount of money",
    "url": "https://www.theverge.com/tech/948917/elon-musk-trillionaire-how-much-visualization",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:26:29+00:00",
    "summary": "Elon Musk is now officially the world's first trillionaire. That is a colossal amount of wealth (and by proxy, power) for one individual to have. Its scale - a thousand times more than a billion - is "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/948409/elon-musk-trillionaire-spacex-ipo",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk is the world&#8217;s first trillionaire",
    "url": "https://www.theverge.com/ai-artificial-intelligence/948409/elon-musk-trillionaire-spacex-ipo",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:24:39+00:00",
    "summary": "Elon Musk's net worth has passed the trillion-dollar mark after SpaceX's IPO. His net worth, which was hovering around $800 billion before the IPO, includes the value of his 4.8 billion shares in Spac"
  },
  {
    "id": "rss:https://www.theverge.com/tech/948464/trump-phone-t1-hands-on",
    "domain": "大厂 AI 动态",
    "title": "I held the Trump phone",
    "url": "https://www.theverge.com/tech/948464/trump-phone-t1-hands-on",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:05:00+00:00",
    "summary": "Where's the Trump phone? We're going to keep talking about it every week. We've reached out, as usual, to ask about the Trump phone's whereabouts. We don't have the phones we preordered yet, but this "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/948806/govee-table-lamp-classic-jbl-charge-6-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Govee&#8217;s rechargeable smart table lamp is down to $60",
    "url": "https://www.theverge.com/gadgets/948806/govee-table-lamp-classic-jbl-charge-6-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T15:07:45+00:00",
    "summary": "Whether you’re planning a backyard barbeque or a World Cup watch party, Govee’s Table Lamp Classic can help set the mood with color-changing lighting effects. Right now it&#8217;s down to just $59.99 "
  },
  {
    "id": "rss:https://www.theverge.com/business/948996/spacex-ipo-elon-musk",
    "domain": "大厂 AI 动态",
    "title": "SpaceX’s massive IPO: all the latest news",
    "url": "https://www.theverge.com/business/948996/spacex-ipo-elon-musk",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T14:35:48+00:00",
    "summary": "SpaceX&#8217;s IPO on Friday allows the public to buy shares of the combined rocket, AI, and social media company for the first time, and raised enough money to make Elon Musk the first trillionaire. "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/949005/jeff-bezos-prometheus-artificial-general-engineer",
    "domain": "大厂 AI 动态",
    "title": "Jeff Bezos’ AI startup aims to build an ‘artificial general engineer’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/949005/jeff-bezos-prometheus-artificial-general-engineer",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T14:03:39+00:00",
    "summary": "Amazon founder Jeff Bezos says his new AI startup will work toward developing an \"artificial general engineer,\" according to reports from The New York Times and CNBC. The startup, called Prometheus, a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/andrew-yang-thinks-the-next-big-startup-opportunity-is-lowering-the-cost-of-living/",
    "domain": "大厂 AI 动态",
    "title": "Andrew Yang thinks the next big startup opportunity is lowering the cost of living",
    "url": "https://techcrunch.com/2026/06/12/andrew-yang-thinks-the-next-big-startup-opportunity-is-lowering-the-cost-of-living/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T04:14:19+00:00",
    "summary": "Andrew Yang made a list of everything Americans overpay for — housing, food, wireless — and thinks the next startup gold rush is giving that money back."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/anthropics-safety-warnings-may-have-just-backfired-the-government-has-pulled-the-plug-on-its-most-powerful-ai/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s safety warnings may have just backfired — the government has pulled the plug on its most powerful AI",
    "url": "https://techcrunch.com/2026/06/12/anthropics-safety-warnings-may-have-just-backfired-the-government-has-pulled-the-plug-on-its-most-powerful-ai/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T02:26:30+00:00",
    "summary": "Anthropic isn't hiding its frustration. \"We disagree that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people,\" the "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/spacex-ipo-live-updates-on-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX IPO: Live updates on everything you need to know",
    "url": "https://techcrunch.com/2026/06/12/spacex-ipo-live-updates-on-everything-you-need-to-know/",
    "source": "Kirsten Korosec, Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T23:15:14+00:00",
    "summary": "TechCrunch has followed SpaceX's start, struggles, and successes from the early days. And we're here for what happens next too. This package of SpaceX IPO coverage includes who stands to win (and mayb"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/metas-months-old-ai-unit-is-a-soul-crushing-gulag-say-the-engineers-stuck-inside-it/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s months-old AI unit is a soul-crushing gulag, say the engineers stuck inside it",
    "url": "https://techcrunch.com/2026/06/12/metas-months-old-ai-unit-is-a-soul-crushing-gulag-say-the-engineers-stuck-inside-it/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T23:00:54+00:00",
    "summary": "A new report suggests the unit, which employs 6,500 people, is on the verge of revolt."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/chinese-cybercrime-operation-that-used-ai-to-scam-hundreds-of-thousands-of-victims-sued-by-google/",
    "domain": "大厂 AI 动态",
    "title": "Chinese cybercrime operation that used AI to scam ‘hundreds of thousands of victims’ sued by Google",
    "url": "https://techcrunch.com/2026/06/12/chinese-cybercrime-operation-that-used-ai-to-scam-hundreds-of-thousands-of-victims-sued-by-google/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T20:38:09+00:00",
    "summary": "The tech giant said a group called \"Outsider Enterprise\" used AI to scam hundreds of thousands of victims, sending 2.5 million text messages over a span of two weeks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/spacex-ipo-closes-up-19-and-delivers-the-worlds-first-trillionaire/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX IPO closes up 19% and delivers the world’s first trillionaire",
    "url": "https://techcrunch.com/2026/06/12/spacex-ipo-closes-up-19-and-delivers-the-worlds-first-trillionaire/",
    "source": "Marina Temkin, Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T20:20:00+00:00",
    "summary": "The company made its heavily anticipated debut on Friday, trading higher than its initial $135 IPO price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/spacex-president-gwynne-shotwell-just-gave-another-hint-at-a-tesla-merger/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX president Gwynne Shotwell just gave another hint at a Tesla merger",
    "url": "https://techcrunch.com/2026/06/12/spacex-president-gwynne-shotwell-just-gave-another-hint-at-a-tesla-merger/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T19:28:31+00:00",
    "summary": "A SpaceX-Tesla merger seems inevitable."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/mistral-is-rumored-to-be-raising-e3b-at-e20-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Mistral is rumored to be raising €3B at €20B valuation",
    "url": "https://techcrunch.com/2026/06/12/mistral-is-rumored-to-be-raising-e3b-at-e20-valuation/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:38:11+00:00",
    "summary": "The funding round would value the company at around €20 billion (about $23.15 billion), nearly double its Series C valuation of €11.7 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/robinhood-sees-record-breaking-traffic-after-spacex-stock-debuts/",
    "domain": "大厂 AI 动态",
    "title": "Robinhood sees ‘record-breaking’ traffic after SpaceX stock debuts",
    "url": "https://techcrunch.com/2026/06/12/robinhood-sees-record-breaking-traffic-after-spacex-stock-debuts/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:05:06+00:00",
    "summary": "The trading platform says some customers experienced intermittent disruptions, but those issues have resolved."
  },
  {
    "id": "rss:https://techcrunch.com/video/spacex-anthropic-and-openais-hot-ipo-summer/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX, Anthropic, and OpenAI’s hot IPO summer",
    "url": "https://techcrunch.com/video/spacex-anthropic-and-openais-hot-ipo-summer/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:23:25+00:00",
    "summary": "The IPO market is back, and&#160;it&#8217;s&#160;not the same&#160;companies&#160;leading the charge. FAANG had a good run, but a&#160;new acronym is taking over: MANGOS&#160;— Meta (or Microsoft, dep"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/elon-musk-becomes-the-worlds-first-trillionaire-after-spacexs-historic-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk becomes the world’s first trillionaire after SpaceX’s historic IPO",
    "url": "https://techcrunch.com/2026/06/12/elon-musk-becomes-the-worlds-first-trillionaire-after-spacexs-historic-ipo/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T15:55:06+00:00",
    "summary": "The SpaceX IPO has boosted Musk's paper wealth to more than $1,000,000,000,000 at a time when he is more hated -- and powerful -- than ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/us-spy-law-to-expire-for-first-time-after-lawmakers-reject-trumps-controversial-pick-to-lead-spy-agencies/",
    "domain": "大厂 AI 动态",
    "title": "US surveillance law to expire for first time after lawmakers reject Trump’s controversial pick to lead spy agencies",
    "url": "https://techcrunch.com/2026/06/12/us-spy-law-to-expire-for-first-time-after-lawmakers-reject-trumps-controversial-pick-to-lead-spy-agencies/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T11:43:32+00:00",
    "summary": "The spy law known as Section 702, which authorizes the NSA and FBI's warrantless surveillance, will all but certainly expire on Friday for the first time."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/cheaper-faster-and-culturally-aware-avataars-video-ai-is-built-for-indias-scale/",
    "domain": "大厂 AI 动态",
    "title": "Cheaper, faster, and culturally aware, Avataar’s video AI is built for India’s scale",
    "url": "https://techcrunch.com/2026/06/11/cheaper-faster-and-culturally-aware-avataars-video-ai-is-built-for-indias-scale/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:30:00+00:00",
    "summary": "Avataar AI's distilled video model is priced at $0.005 for every second of generation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/equal-ai-raises-30m-to-screen-calls-so-indians-dont-have-to/",
    "domain": "大厂 AI 动态",
    "title": "Equal AI raises $30M to screen calls so Indians don’t have to",
    "url": "https://techcrunch.com/2026/06/11/equal-ai-raises-30m-to-screen-calls-so-indians-dont-have-to/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:30:00+00:00",
    "summary": "Equal AI said that its AI-powered call assistant now has over a million monthly active users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/theker-just-raised-85m-to-build-the-factory-robot-that-doesnt-specialize-in-anything/",
    "domain": "大厂 AI 动态",
    "title": "Theker just raised $85M to build the factory robot that doesn’t specialize in anything",
    "url": "https://techcrunch.com/2026/06/11/theker-just-raised-85m-to-build-the-factory-robot-that-doesnt-specialize-in-anything/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T01:48:07+00:00",
    "summary": "Unlike humanoid robots designed around a fixed form — think Boston Dynamics — Theker's machines are built to be reconfigured."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/",
    "domain": "大厂 AI 动态",
    "title": "Jeff Bezos’s Prometheus raises $12B to build an ‘artificial general engineer’ for the physical world",
    "url": "https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T01:04:38+00:00",
    "summary": "The new round values the physical AI startup that aims to automate heavy engineering and drug design at $41 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/spacex-officially-prices-shares-at-135-in-the-largest-ipo-ever/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX officially prices shares at $135 in the largest IPO ever",
    "url": "https://techcrunch.com/2026/06/11/spacex-officially-prices-shares-at-135-in-the-largest-ipo-ever/",
    "source": "Tim Fernholz, Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T20:33:10+00:00",
    "summary": "Wits its official share pricing announcement, SpaceX's IPO has begun."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/oracle-warns-of-security-bug-that-hackers-abused-to-breach-100-companies/",
    "domain": "大厂 AI 动态",
    "title": "Oracle warns of security bug that hackers abused to breach 100+ companies",
    "url": "https://techcrunch.com/2026/06/11/oracle-warns-of-security-bug-that-hackers-abused-to-breach-100-companies/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T20:27:25+00:00",
    "summary": "The tech giant warned of a security flaw that a cybercrime gang said it's exploiting as part of a mass-hacking campaign. Google said it notified more than 100 organizations that had potentially vulner"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/spacex-spv-investors-wont-know-their-true-holdings-until-post-ipo-lock-ups-lift/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX SPV investors won’t know their true holdings until post-IPO lock-ups lift",
    "url": "https://techcrunch.com/2026/06/11/spacex-spv-investors-wont-know-their-true-holdings-until-post-ipo-lock-ups-lift/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T19:58:01+00:00",
    "summary": "After SpaceX makes its public debut, lower-tier SPV investors face hidden fees, lengthy payout delays, and the risk of outright fraud."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/bluesky-launches-group-chats-as-company-shifts-focus-to-community-features/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky launches group chats, as company shifts focus to community features",
    "url": "https://techcrunch.com/2026/06/11/bluesky-launches-group-chats-as-company-shifts-focus-to-community-features/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T19:41:05+00:00",
    "summary": "Bluesky's latest feature is group chats, arriving amid a shift in focus on building features for smaller communities."
  },
  {
    "id": "rss:https://stratechery.com/2026/hey-siri-tell-me-a-fable/",
    "domain": "大厂 AI 动态",
    "title": "2026.24: Hey Siri, Tell Me a Fable",
    "url": "https://stratechery.com/2026/hey-siri-tell-me-a-fable/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of June 8, 2026, including Apple finally shipping Intelligence, Anthropic's fable, and the future of European industry."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-ben-bajarin-about-apple-ai-and-compute/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Ben Bajarin About Apple, AI, and Compute",
    "url": "https://stratechery.com/2026/an-interview-with-ben-bajarin-about-apple-ai-and-compute/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:00:00+00:00",
    "summary": "An interview with Ben Bajarin about WWDC and the status of the AI compute industry."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/anthropic-shuts-down-fable-mythos-models-following-trump-admin-directive/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic shuts down Fable, Mythos models following Trump admin directive",
    "url": "https://arstechnica.com/ai/2026/06/anthropic-shuts-down-fable-mythos-models-following-trump-admin-directive/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T03:00:34+00:00",
    "summary": "Commerce dept. worries that a Fable 5 \"jailbreak\" could be a national security threat."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/spacex-is-now-a-public-company-valued-for-its-ai-potential-so-what-comes-next/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX is now a public company valued for its AI potential, so what comes next?",
    "url": "https://arstechnica.com/space/2026/06/spacex-is-now-a-public-company-valued-for-its-ai-potential-so-what-comes-next/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T22:20:06+00:00",
    "summary": "As of today, SpaceX is owned by investors who will want to see it make money."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/peoplesoft-0-day-affecting-hundreds-of-organizations-steals-gigabytes-of-data/",
    "domain": "大厂 AI 动态",
    "title": "PeopleSoft 0-day affecting hundreds of organizations steals gigabytes of data",
    "url": "https://arstechnica.com/security/2026/06/peoplesoft-0-day-affecting-hundreds-of-organizations-steals-gigabytes-of-data/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T19:26:47+00:00",
    "summary": "Vulnerability in the Oracle-owned PeopleSoft software is about as critical as they come."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/controversial-fisa-spying-law-expires-tonight-the-spying-will-continue/",
    "domain": "大厂 AI 动态",
    "title": "Controversial FISA spying law expires tonight. The spying will continue.",
    "url": "https://arstechnica.com/tech-policy/2026/06/controversial-fisa-spying-law-expires-tonight-the-spying-will-continue/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:57:51+00:00",
    "summary": "Section 702 of FISA to expire tonight, but certification lasts until March 2027."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/heres-what-jeff-bezos-new-startup-prometheus-will-do/",
    "domain": "大厂 AI 动态",
    "title": "Here's what Jeff Bezos' new startup Prometheus will do",
    "url": "https://arstechnica.com/ai/2026/06/heres-what-jeff-bezos-new-startup-prometheus-will-do/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:45:40+00:00",
    "summary": "It isn't the only startup tackling physical AI, but it's one of the best-funded."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/have-politics-finally-come-for-the-national-academies-of-science/",
    "domain": "大厂 AI 动态",
    "title": "Have politics finally come for the National Academies of Science?",
    "url": "https://arstechnica.com/science/2026/06/have-politics-finally-come-for-the-national-academies-of-science/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:31:36+00:00",
    "summary": "A pending report on climate attribution may be setting the stage for conflict."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/ukraines-one-time-test-used-fully-autonomous-drones-to-kill-russian-soldiers/",
    "domain": "大厂 AI 动态",
    "title": "Ukraine's one-time test used fully autonomous drones to kill Russian soldiers",
    "url": "https://arstechnica.com/ai/2026/06/ukraines-one-time-test-used-fully-autonomous-drones-to-kill-russian-soldiers/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:03:29+00:00",
    "summary": "Full autonomy is rare, but Ukraine is installing AI modules on drones and robots."
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 1061,
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
    "points": 266,
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
    "id": "hn:48504013",
    "domain": "股票",
    "title": "SpaceX's president is floating a Tesla merger as the company begins trading",
    "url": "https://qz.com/spacex-tesla-merger-gwynne-shotwell-ipo-061226",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-06-12T13:47:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48446310",
    "domain": "股票",
    "title": "Italy's Bending Spoons, owner of AOL and Vimeo, files for Nasdaq IPO",
    "url": "https://www.reuters.com/legal/transactional/italys-bending-spoons-files-us-ipo-2026-06-08/",
    "source": "mmarian",
    "platform": "hackernews",
    "points": 123,
    "published_at": "2026-06-08T15:04:17+00:00",
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
    "id": "hn:48505968",
    "domain": "股票",
    "title": "Elon Musk Becomes First Trillionaire as SpaceX Starts Trading",
    "url": "https://www.nytimes.com/live/2026/06/12/business/spacex-ipo-elon-musk/heres-the-latest",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-06-12T16:13:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48499349",
    "domain": "股票",
    "title": "StonkRider – Ride any stock chart",
    "url": "https://stonkrider.com/",
    "source": "nreece",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-06-12T02:58:20+00:00",
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
    "id": "hn:48506701",
    "domain": "股票",
    "title": "SpaceX increases almost 30% after biggest IPO",
    "url": "https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html",
    "source": "somenameforme",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-06-12T17:10:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506306",
    "domain": "股票",
    "title": "SpaceX vaults over $2T valuation as stock jumps after record IPO",
    "url": "https://www.reuters.com/legal/transactional/after-record-ipo-musks-spacex-faces-next-test-market-debut-2026-06-12/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-12T16:39:48+00:00",
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
    "id": "wscn:3774575",
    "domain": "股票",
    "title": "首秀“丝滑”收官，SpaceX为OpenAI们打了个样！",
    "url": "https://wallstreetcn.com/articles/3774575",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T05:59:30+00:00",
    "summary": "SpaceX用“提前半年教育投资者+固定价格定价”完成人类史上最大IPO。公司与承销商自今年1月起持续向市场预热，最终实现平稳开盘，既避免定价过低导致利益流失，也避免过热引发套利抛售。这套打法已被视为OpenAI和Anthropic的上市模板。"
  },
  {
    "id": "wscn:3774565",
    "domain": "股票",
    "title": "美伊接近协议、SpaceX完成IPO，币圈多空激辩：底部到了吗？",
    "url": "https://wallstreetcn.com/articles/3774565",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T05:16:03+00:00",
    "summary": "渣打银行分析师Kendrick认为比特币低点已出。链上数据显示价格接近\"已实现价格\"，超半数持仓处于亏损，历史上均为底部信号。然而，美国现货比特币ETF单月净流出58亿美元，机构需求持续低迷。分析师警告，当前仅属\"估值底部候选\"，而非确认的周期低点，市场多空分歧依然显著。"
  },
  {
    "id": "wscn:3774574",
    "domain": "股票",
    "title": "OpenAI突遭联合调查、Anthropic顶级模型被叫停，美国AI监管风暴升级",
    "url": "https://wallstreetcn.com/articles/3774574",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T05:12:36+00:00",
    "summary": "美国多州调查OpenAI，法律诉讼接连而至，同时Anthropic模型被限制访问。美国AI行业监管全面收紧，技术竞争转向政策与安全博弈。"
  },
  {
    "id": "wscn:3774573",
    "domain": "股票",
    "title": "又一家万亿美元级别IPO！SK海力士计划8月在纳斯达克上市，募资高达140亿美元",
    "url": "https://wallstreetcn.com/articles/3774573",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T03:46:01+00:00",
    "summary": "SK海力士计划最早于今年8月在纳斯达克挂牌上市，预计募资高达140亿美元。SEC可能在6月22日当周批准其ADR上市申请。分析师指出，纳斯达克对科技股的估值溢价及被动基金的资金集聚效应，是SK海力士放弃纽交所、选择纳斯达克的核心原因。公司今年股价已累计暴涨两倍，市值于5月突破1万亿美元。"
  },
  {
    "id": "wscn:3774203",
    "domain": "股票",
    "title": "5月挖机销售全面超预期，工程机械行业仍处于景气上行周期",
    "url": "https://wallstreetcn.com/premium/articles/3774203?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T03:33:34+00:00",
    "summary": "工程机械行业仍处在景气上行周期，国内更新逻辑驱动复苏，出海逻辑从“贝塔”走向“阿尔法”。"
  },
  {
    "id": "wscn:3774569",
    "domain": "股票",
    "title": "SpaceX上市首日超越特斯拉，SpaceX总裁暗示“合并”，特斯拉股东热盼",
    "url": "https://wallstreetcn.com/articles/3774569",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T03:16:28+00:00",
    "summary": "SpaceX上市首日收涨逾30%，市值约达2万亿美元，超越特斯拉成为全美第六大上市公司。当天，SpaceX总裁暗示两家公司合并“或许能让马斯克的生活轻松一点”。有特斯拉投资者表示故意放弃认购SpaceX，押注持有特斯拉等待合并。但也有分析师提示，合并可能对特斯拉股东造成约28%的稀释。"
  },
  {
    "id": "wscn:3774566",
    "domain": "股票",
    "title": "投行圈的“奥运金牌”：SpaceX IPO承销费5亿美元，高盛和大摩各分1亿，高盛还能赚更多",
    "url": "https://wallstreetcn.com/articles/3774566",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T03:11:42+00:00",
    "summary": "SpaceX以750亿美元创史上最大IPO，承销费率仅0.67%，总费约5亿美元，高盛、摩根士丹利各获约1亿美元。但真正收益来自\"软美元\"——首日股价涨约20%，机构浮盈逾170亿美元，约30%将以佣金形式回流华尔街，潜在超50亿美元，是显性费用8倍，高盛将为最大赢家。"
  },
  {
    "id": "wscn:3774572",
    "domain": "股票",
    "title": "近3月收益54%，平安基金要文强：看好7、8月AI行情，不要担心，每一波超额收益都来自宏观波动，看好五个细分方向",
    "url": "https://wallstreetcn.com/articles/3774572",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T02:52:32+00:00",
    "summary": "下半年企业端Agent爆发，明年模型自训练爆发。"
  },
  {
    "id": "wscn:3774568",
    "domain": "股票",
    "title": "联手打造太空算力？SpaceX刚上市，马斯克就喊话黄仁勋：合作升级！",
    "url": "https://wallstreetcn.com/articles/3774568",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T01:22:47+00:00",
    "summary": "SpaceX上市首日大涨逾19%。英伟达随即公开祝贺，马斯克表示将把双方合作“推向新水平”。与此同时，SpaceX披露首款AI计算卫星AI1，并已与谷歌、Anthropic签下合计每月逾21亿美元的算力大单，英伟达GPU贯穿其中。"
  },
  {
    "id": "wscn:3774545",
    "domain": "股票",
    "title": "“初步协议”渐近：巴方称伊美就文本达成一致，美伊就条款各执一词，最难的问题“往后推了60天”",
    "url": "https://wallstreetcn.com/articles/3774545",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T00:57:02+00:00",
    "summary": "巴美伊确认和平协议文本接近达成。伊外长披露谈判分两阶段，第一阶段重在停火与海峡解封，核心核议题延至第二阶段，且坚持在境内稀释浓缩铀、要求以军撤离黎巴嫩南部。美官员坦言，最难的核弹拆除等具体条款实际上被往后推了60天。因伊朗军方未签字、美伊对条款各执一词，协议仍具变数。"
  },
  {
    "id": "wscn:3774567",
    "domain": "股票",
    "title": "上线仅四日就遭下架，Fable 5和Mythos 5被美政府列出口管制，Anthropic服从但不认同",
    "url": "https://wallstreetcn.com/articles/3774567",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T00:57:00+00:00",
    "summary": "美国商务部长Howard Lutnick致函Anthropic，将其两款顶尖AI模型Fable 5和Mythos 5纳入出口管制，限制境外及境内外籍人士访问，理由是存在越狱安全风险。Anthropic虽遵令下架，但公开反对，称漏洞轻微且普遍存在于行业，并警告此标准将令前沿模型部署陷入停滞。"
  },
  {
    "id": "wscn:3774562",
    "domain": "股票",
    "title": "法官同意暂停废除“特朗普10万美元H-1B签证费”的裁决",
    "url": "https://wallstreetcn.com/articles/3774562",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T23:26:01+00:00",
    "summary": "波士顿联邦法官索罗金表示，在抗诉法院介入之前，他将暂缓执行其针对H-1B签证费作出的裁决。该裁决裁定特朗普政府对新H-1B工人征收10万美元费用违宪，侵犯国会专属征税权。"
  },
  {
    "id": "wscn:3774563",
    "domain": "股票",
    "title": "华尔街对历史性SpaceX IPO极端两极分化！目标价60-190美元",
    "url": "https://wallstreetcn.com/articles/3774563",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T23:25:50+00:00",
    "summary": "SpaceX完成史上最大IPO之一，在华尔街掀起激烈\"估值战争\"：乐观派将其视作“世纪机遇”，喊出190美元目标价；悲观派则狠批估值透支，直指公允价值不足IPO定价一半。更有机构警告，SpaceX IPO的交易结构是“历史上对散户投资者最大的洗劫之一”。"
  },
  {
    "id": "wscn:3774564",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年6月13日",
    "url": "https://wallstreetcn.com/articles/3774564",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T23:21:40+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3774481",
    "domain": "股票",
    "title": "美伊协议曙光重燃，原油两连跌，美股指全线收涨、债汇承压，SpaceX首日大涨19%",
    "url": "https://wallstreetcn.com/articles/3774481",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T23:11:24+00:00",
    "summary": "标普500指数收涨0.5%。苹果跌1.5%，本周累跌超5%。英特尔涨6.5%、本周累计大涨25%。SpaceX上市首日，太空概念股SATS和RKLB均大跌近11%。希捷大涨超7%。软件股ETF横盘微跌、九连跌创20年来最长。10年期美债收益率上行2基点、本周下行约10个基点。白银日内涨1%。纽铜两连涨。WTI原油期货跌超3%。"
  },
  {
    "id": "wscn:3774552",
    "domain": "股票",
    "title": "美国软件股二十年来最长连跌，AI扰动之忧再度来袭",
    "url": "https://wallstreetcn.com/articles/3774552",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T22:36:12+00:00",
    "summary": "贝莱德旗下iShares发行的北美软件板块核心 ETF周五盘中一度跌超1%，收跌0.24%；是该ETF连续第九个交易日下跌，创2006年6月以来最长连跌纪录。"
  },
  {
    "id": "wscn:3774561",
    "domain": "股票",
    "title": "SpaceX“吸血”，美股太空板块暴跌",
    "url": "https://wallstreetcn.com/articles/3774561",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T22:25:29+00:00",
    "summary": "SpaceX上市首日大涨19%，散户买入1.2亿美元，超英伟达跃居散户买入榜首位。同业公司集体失血大跌，Rocket Lab跌11%，Virgin Galactic重挫32%，Procure Space ETF收跌7%。分析指出，投资者此前买入同业公司，是进入SpaceX之前的\"占位仓\"，如今顺势迁移。"
  },
  {
    "id": "wscn:3774560",
    "domain": "股票",
    "title": "很难赌马斯克会输！散户一边骂贵一边疯抢SpaceX，但绝大多数不打算长期持股",
    "url": "https://wallstreetcn.com/articles/3774560",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T22:25:19+00:00",
    "summary": "估值\"荒唐\"照样抢购，马斯克光环、FOMO情绪与罕见的20%散户配额，共同点燃这场\"IPO超级碗\"。多数散户表示并不打算长期持股，押注首日行情快速套利。Robinhood今日成交量创新高，Fidelity下调IPO参与门槛。SpaceX盘中涨幅一度超过30%，最终收涨19%，报161美元。"
  },
  {
    "id": "wscn:3774559",
    "domain": "股票",
    "title": "市场拥挤交易快速退潮！对冲基金净杠杆骤降至一年第8百分位",
    "url": "https://wallstreetcn.com/articles/3774559",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T20:47:58+00:00",
    "summary": "摩根大通最新数据显示，短短几天，对冲基金净杠杆率已骤降至过去一年的第8百分位，已回到12个月区间的低端；仓位过度拥挤这一看跌理由正在消散。但对冲基金在动量以及其他高风险因子上的敞口仍接近2021年初投机狂热时期的高点，市场脆弱性犹存。"
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
    "id": "hn:48436328",
    "domain": "股票",
    "title": "Musk's SpaceX IPO Narrative Is a Whole New Level of Bullshit",
    "url": "https://text.tchncs.de/chronik-des-laufenden-wahnsinns/h1elon-musk-has-spouted-his-fair-share-of-bullshit-but-his-latest-claims-about",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-07T16:24:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48419956",
    "domain": "股票",
    "title": "Nasdaq falls 4% and suffers worst day since April 2025 traders flee chip stocks",
    "url": "https://www.cnbc.com/2026/06/04/stock-market-today-live-updates.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-06T00:02:38+00:00",
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
    "id": "hn:48391046",
    "domain": "股票",
    "title": "We Uncovered a Hidden Wealth Transfer in the SpaceX IPO. You're Holding the Bag [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "CharlesW",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-03T22:32:44+00:00",
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
    "id": "hn:48454210",
    "domain": "金融",
    "title": "Federal judge blocks H1B visa $100K fee",
    "url": "https://www.alaskasnewssource.com/2026/06/08/federal-judge-blocks-h1-b-visa-100k-fee/",
    "source": "naturalmovement",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-06-09T00:01:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48507248",
    "domain": "金融",
    "title": "Tesla Full Self Driving uses bicycle lane in official Denmark approval video",
    "url": "https://politiken.dk/danmark/forbrug/biler/art10875514/Allerede-12-sekunder-inde-i-PR-videoen-beg%C3%A5r-selvk%C3%B8rende-Tesla-f%C3%B8rste-fejl-i-k%C3%B8benhavnsk-gade-%E2%80%93-men-det-bliver-v%C3%A6rre-endnu",
    "source": "Veserv",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-06-12T17:49:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48479537",
    "domain": "金融",
    "title": "Meta steals a tactic from Tesla and builds data centers in tents",
    "url": "https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-06-10T17:18:39+00:00",
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
    "id": "hn:48483445",
    "domain": "金融",
    "title": "US President says 'I love the inflation'",
    "url": "https://www.cnbc.com/2026/06/10/trump-inflation-cpi-iran-oil.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-06-10T22:12:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48488805",
    "domain": "金融",
    "title": "Feds will abruptly dismantle system monitoring climate change, oceans",
    "url": "https://www.usatoday.com/story/news/nation/2026/06/11/climate-change-ocean-monitoring-system-dismantled/90378309007/",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T11:12:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:48491301",
    "domain": "金融",
    "title": "Craig Federighi Details Apple's Collaboration with Google for Siri AI in iOS 27",
    "url": "https://9to5mac.com/2026/06/08/craig-federighi-details-apples-collaboration-with-google-for-siri-ai-in-ios-27/",
    "source": "tambourine_man",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-11T15:01:26+00:00",
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
    "id": "hn:48476514",
    "domain": "金融",
    "title": "GnuCash is right. It's also why I built my own finance app",
    "url": "https://k-id.app/blog/gnucash-is-right/",
    "source": "tinosar",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-06-10T14:06:22+00:00",
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
    "id": "hn:48438281",
    "domain": "金融",
    "title": "Boomers are hoarding most of America's wealth and power",
    "url": "https://finance.yahoo.com/economy/articles/golden-years-not-golden-boomers-113000201.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 22,
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
    "points": 20,
    "published_at": "2026-06-08T20:57:49+00:00",
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
    "id": "hn:48449003",
    "domain": "金融",
    "title": "Half of Americans say they're worse off financially than a year ago",
    "url": "https://www.cbsnews.com/news/americans-worse-off-financially-year-ago-fed-survey/",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-08T18:12:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377347",
    "domain": "金融",
    "title": "Feds failing in bid to take a supercomputer from a climate research center",
    "url": "https://arstechnica.com/science/2026/06/judge-blocks-part-of-trump-admins-effort-to-hurt-colorado-research-center/",
    "source": "yodon",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-02T22:46:54+00:00",
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
    "id": "hn:48330421",
    "domain": "金融",
    "title": "The record divide between corporate profits and worker pay",
    "url": "https://www.wsj.com/finance/stocks/the-record-divide-between-corporate-profits-and-worker-pay-ea4c75bc",
    "source": "hhs",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-29T22:55:36+00:00",
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
    "id": "hn:48284628",
    "domain": "金融",
    "title": "Trump's 25% cut on Nvidia chips to China backfired as Beijing blocks H200 sales",
    "url": "https://finance.yahoo.com/markets/stocks/articles/trumps-25-cut-nvidia-chips-194500691.html",
    "source": "frasermarlow",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-26T19:21:02+00:00",
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
    "id": "hn:48156037",
    "domain": "金融",
    "title": "Senior NIAID Official Indicted for Concealing Records During Covid Pandemic",
    "url": "https://www.justice.gov/opa/pr/former-senior-niaid-official-indicted-concealing-federal-records-during-covid-19-pandemic-0",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-16T01:44:08+00:00",
    "summary": ""
  }
]
```
