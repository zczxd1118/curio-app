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

- 今日日期：`2026-08-21`
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
  "date": "2026-08-21",
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
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1336123,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1159953,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 1083748,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 876282,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 671646,
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
    "points": 631482,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1DYkqYPEED",
    "domain": "AI",
    "title": "我的世界服务器必备指令",
    "url": "http://www.bilibili.com/video/av113695753507666",
    "source": "欢小牛Mc",
    "platform": "bilibili",
    "points": 629024,
    "published_at": "2024-12-22T09:28:49+00:00",
    "summary": "生存模式：gamemode 0 @p\n光明方块：give @s light_block 1 15\n删除掉落物:kill @e[type=item]"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 605508,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 556019,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 438814,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1Tv3i6LEX1",
    "domain": "AI",
    "title": "用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍",
    "url": "http://www.bilibili.com/video/av116996217838997",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 419357,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 399602,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1ukRrBMEfp",
    "domain": "AI",
    "title": "用了三个月Codex，我不想回Claude Code了",
    "url": "http://www.bilibili.com/video/av116519929512463",
    "source": "HexUp",
    "platform": "bilibili",
    "points": 319935,
    "published_at": "2026-05-05T10:00:00+00:00",
    "summary": "之前的视频聊了Claude Code、Codex、Cursor怎么选，几个月过去我的看法变了。这期分享我现在为什么把Codex作为首选AI Agent工具，从桌面App体验、模型能力、到中国用户的付费和封号问题，都会聊到。"
  },
  {
    "id": "bvid:BV1cofCBgESQ",
    "domain": "AI",
    "title": "3天赚1200刀？纯聊天就能捏出个能搞钱的 AI Agent！【教程】",
    "url": "http://www.bilibili.com/video/av116123517329389",
    "source": "Xuan_酱",
    "platform": "bilibili",
    "points": 310140,
    "published_at": "2026-02-24T03:48:52+00:00",
    "summary": "用MuleRun靠动嘴就搓了一个 每日AI 资讯自动抓取的 Agent～"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 269979,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 246846,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 243193,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1gweRzgEPH",
    "domain": "AI",
    "title": "Meta偷了2396部黄色电影喂给AI......或将面临天价罚单！AI训练的“黄金饲料”",
    "url": "http://www.bilibili.com/video/av115088916808110",
    "source": "扎马步的阑尾猫",
    "platform": "bilibili",
    "points": 225746,
    "published_at": "2025-08-25T11:16:22+00:00",
    "summary": "往期回顾：【DeepSeek逆天翻倍涨价！夜间半价直接砍了！V3.1真的加价不加量】https://www.bilibili.com/video/BV1eNYRz5EzX/?share_source=copy_web&amp;vd_source=ffeceac29634d3f0e4d334a6d587e2b9\n【Grok隐私风暴：马斯克把你的聊天记录公开发布了！】 https://www.bili"
  },
  {
    "id": "bvid:BV1i9Z8YhEja",
    "domain": "AI",
    "title": "学 AI，看这个视频就够了！最全程序员 AI 指南：AI核心概念、实用AI工具、AI编程技巧、AI开发技术",
    "url": "http://www.bilibili.com/video/av114262957626976",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 186079,
    "published_at": "2025-04-01T13:56:58+00:00",
    "summary": "AI 时代，程序员要学什么才能不被淘汰呢？这个视频给你答案。带你快速了解 AI 核心概念、AI 常用工具、AI 编程技巧、AI + 编程技术，走在时代的前沿，算是一期硬核的程序员 AI 学习指南视频了~\n还为大家准备了免费开源 AI 知识库：https://ai.codefather.cn，有帮助的话记得三连哦~\n涉及知识点：大模型、Prompt、AI开发平台、RAG知识库、MCP、Ollama本"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 179562,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 174976,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 164000,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 159375,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV14egj6nELQ",
    "domain": "AI",
    "title": "一个导演Agent，帮你榨干Seedance2.5",
    "url": "http://www.bilibili.com/video/av117083006376875",
    "source": "AI视次方",
    "platform": "bilibili",
    "points": 146465,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 143034,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV1jgvaBzEfK",
    "domain": "AI",
    "title": "AI编程工具实战排名，谁是最好用的AI编程工具",
    "url": "http://www.bilibili.com/video/av115806444782075",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 128123,
    "published_at": "2025-12-30T03:47:23+00:00",
    "summary": "本视频将对我用的 AI 编程工具进行排名，原则如下：\n排名打分项\n创新能力\n代码搜索（代码索引）\n上下文组装、压缩、保存\nAI调用的流程（工具调用）\n交互便捷性\n排名原则\n以下参与排名的工具是本人使用过，未参与排名的其他工具不代表没有名次，没有使用经验，不敢妄加排名\n本次排名参考期限（2025/12/30），AI 编程工具在日新月异的发展，无法预料变化\n萝卜青菜，各有所爱，适合自己的才是最重要的\n"
  },
  {
    "id": "bvid:BV1EVuqzrEMJ",
    "domain": "AI",
    "title": "【保姆级教程】手把手教你低成本制作AI女友，【一定要看置顶评论】，可随身携带，自由对话",
    "url": "http://www.bilibili.com/video/av114851468812000",
    "source": "往生堂研发",
    "platform": "bilibili",
    "points": 116858,
    "published_at": "2025-07-14T12:03:53+00:00",
    "summary": "文档地址\nhttps://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md?_refluxos=a10#%E6%96%B9%E5%BC%8F%E4%B8%80docker%E5%8F%AA%E8%BF%90%E8%A1%8Cserver"
  },
  {
    "id": "bvid:BV1uXQzYaEpJ",
    "domain": "AI",
    "title": "7分钟讲清楚MCP是什么？统一Function calling规范，工作量锐减至1/6，人人手搓Manus！？ | 一键链接千台服务器，几行代码接入海量外部工具",
    "url": "http://www.bilibili.com/video/av114161203878976",
    "source": "九天Hector",
    "platform": "bilibili",
    "points": 112569,
    "published_at": "2025-03-14T14:19:04+00:00",
    "summary": "MCP到底是什么？MCP具体解决了Agent开发中的什么痛点？以及如何接入MCP呢？详解MCP工作原理及应用场景，一站式打包原理、使用场景、使用方法，快速建立MCP技术认知！\n✅置顶评论扫码加入【赋范大模型技术社区】，领【全套Manus Agent学习资料】，以及更多【海量硬核独家技术干货】内容+无门槛技术交流，期待你的加入！"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 102639,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99815,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1KGNt6qEoU",
    "domain": "AI",
    "title": "知道这6个AI Agent术语，看懂任何一个Agent #howto用好AI #大模型 #AI人工智能 #agent #姜学长",
    "url": "http://www.bilibili.com/video/av116918405174438",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 95554,
    "published_at": "2026-07-14T12:51:02+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93314,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 91342,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1LjC7BmE8H",
    "domain": "AI",
    "title": "硅谷爆火AI神器Cursor教程！从入门到实战，轻松做图表、写文档、搞开发、自动化全能办公！",
    "url": "http://www.bilibili.com/video/av115536717484104",
    "source": "韩顺平",
    "platform": "bilibili",
    "points": 87743,
    "published_at": "2025-11-12T12:31:09+00:00",
    "summary": "《Cursor快速入门到实战》带你全面掌握Cursor！从安装配置到Chat对话、规则、提示词模板，再到数据可视化、文档生成、游戏开发、智能助手、Figma联动实战，全流程提升AI编程与办公效率，轻松打造高效智能开发环境。"
  },
  {
    "id": "bvid:BV1UDsJz7EJt",
    "domain": "AI",
    "title": "Claude Code：最强自动化写作agent！99%的人都低估了cc的能力",
    "url": "http://www.bilibili.com/video/av115427279835206",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 77331,
    "published_at": "2025-10-24T09:55:00+00:00",
    "summary": "这期视频主要展示如何用Claude Code搭建自动化写作系统。从每周1篇到日更，数据反增长。完整演示：需求理解→信息调研→选题方案→风格学习→三遍审校→自动配图，10分钟完成3-4小时工作量，效果达人工80-90%。核心是路由机制、个人素材库和风格学习。附赠公众号排版器。\n\n  ⏱️ 视频时间戳：\n  - 0:00 开场：写作系统效果介绍\n  - 1:09 实操演示：从需求到调研\n  - 2:3"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63562,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54281,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1myM96nETU",
    "domain": "AI",
    "title": "AI 赛博女友！本地部署教程，无需 API、完全免费，8G显存就能跑！实时语音聊天，几乎零延迟，太上头了！| 零度解说",
    "url": "http://www.bilibili.com/video/av117032322339286",
    "source": "零度解说",
    "platform": "bilibili",
    "points": 52409,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "AI 赛博女友一键安装包下载：https://www.freedidi.com/24984.html"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47636,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 46572,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1Y6uC6TE1m",
    "domain": "AI",
    "title": "疯狂Vibe Coding一周，我烧了近100亿Token，做了5个项目！",
    "url": "http://www.bilibili.com/video/av117080321957877",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 43315,
    "published_at": "2026-08-12T03:12:41+00:00",
    "summary": "项目地址：\nlocal-ops — 本地服务指挥台（零依赖 Python + 原生前端）：https://github.com/laogou717/local-ops\nmd-wechat — 公众号排版工具：https://github.com/laogou717/md-wechat\ndaydream-room — 白日梦陈列室：https://github.com/laogou717/daydr"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 40853,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1x6Vt6dEef",
    "domain": "AI",
    "title": "100 小时测试 Claude Code vs Codex（真实结果）",
    "url": "http://www.bilibili.com/video/av116656495925868",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 38513,
    "published_at": "2026-05-29T06:44:49+00:00",
    "summary": "【海外 AI 订阅】\n国内直连，支付宝付款，不用代理，\n一站订阅 ChatGPT / Codex / Claude Code / X\n订阅链接：https://bewild.ai?code=SJZD\n订阅时请填优惠邀请码：SJZD，具体优惠金额以官网为准。\n\n【视频介绍】\n我花了 100 个小时测试 Claude Code 和 Codex，结果真的让我非常意外。\n相同的提示词、相同的项目构建、两个"
  },
  {
    "id": "bvid:BV1WFwVeMEm9",
    "domain": "AI",
    "title": "【10万人学过】Cursor、Windsur终极评测，谁是最强AI编程工具？",
    "url": "http://www.bilibili.com/video/av113836094918887",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 38450,
    "published_at": "2025-01-16T04:24:54+00:00",
    "summary": "这期视频是对Cursor、Windsurf两个最强AI编程工具的终极评测，尤其是关注了两个产品的上下文索引机制，文章内容此前在X上发出时，获得了10万+的阅读，被无数好评。忍不住做成视频给大家看看真正的好东西。\n\n重点时间戳：\n[00:00:00] 开场介绍 - 为什么要做这期对比评测\n[00:09:36] 核心结论1 - 对新手而言,Windsurf体验优于Cursor,因为其agent模式在执"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34155,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1o1ET68EFR",
    "domain": "AI",
    "title": "10分钟教会你0成本用上Codex，不花一分钱，实现Agent自由！",
    "url": "http://www.bilibili.com/video/av116713370752834",
    "source": "暴走的阿川",
    "platform": "bilibili",
    "points": 33616,
    "published_at": "2026-06-08T07:46:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV16mJGzqE7Y",
    "domain": "AI",
    "title": "免费Cursor无限续杯教程，0元用到爽！手把手教你白嫖AI神器",
    "url": "http://www.bilibili.com/video/av114529178487533",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 29650,
    "published_at": "2025-05-18T14:04:10+00:00",
    "summary": "这是近期热度极高的开源Cursor免费助手项目，GitHub地址：https://github.com/agentcodee/cursor-free-everyday。\n该项目专为AI开发者和日常用户打造，完全免费，支持一键获取新额度、自动满额度账号、无需登录账号、机器码自动重置等实用功能。无论你是Windows还是Mac用户，都能轻松上手，彻底告别额度焦虑。\n项目开源透明，持续更新，深受社区好评"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29641,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV13tuqzwEm9",
    "domain": "AI",
    "title": "一个视频彻底掌握ClaudeCode使用MCP",
    "url": "http://www.bilibili.com/video/av114851586252599",
    "source": "创哥的AI实验室",
    "platform": "bilibili",
    "points": 29016,
    "published_at": "2025-07-14T12:32:55+00:00",
    "summary": "Claude Code命令行的方式，让MCP的操作也令很多朋友感觉不适，这个视频专门做了一些介绍。\n\n希望能帮助到大家。"
  },
  {
    "id": "bvid:BV16RAezpERp",
    "domain": "AI",
    "title": "【中配】使用Claude Code辅助Unity开发的8个月 - Mythmatic",
    "url": "http://www.bilibili.com/video/av116149035733359",
    "source": "黑纹白斑马",
    "platform": "bilibili",
    "points": 27314,
    "published_at": "2026-02-28T15:54:00+00:00",
    "summary": "原视频：8 Months of Unity Dev with Claude Code\n原作者：Mythmatic\n发布日期：2026-01-26\n视频链接：https://www.youtube.com/watch?v=GxZLC00yJ5g\n\n✨ 想看英文原声？请关注 @英文白斑马\n\n00:00 介绍与工作流概述\n作者分享了作为独立开发者使用 Claude Code 代替手动编写代码的工作流，这"
  },
  {
    "id": "hn:49255710",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Risky Business",
    "url": "https://stratechery.com/2026/nvidias-risky-business/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 356,
    "published_at": "2026-08-11T10:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49323686",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dramatically reduces amount of OpenAI infra financing it may guarantee",
    "url": "https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 251,
    "published_at": "2026-08-16T21:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49263340",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning and NeMo Switchyard",
    "url": "https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 262,
    "published_at": "2026-08-11T19:35:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49257947",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning",
    "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4",
    "source": "beklein",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-08-11T13:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342314",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://arstechnica.com/information-technology/2026/08/nvidia-discloses-21b-stake-in-spacex/",
    "source": "joozio",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-08-18T07:02:04+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/synopsys-updates-cxl-ip-portfolio-for-ai-era-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "Synopsys Updates CXL IP Portfolio for AI-Era Infrastructure",
    "url": "https://www.eetimes.com/synopsys-updates-cxl-ip-portfolio-for-ai-era-infrastructure/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T14:07:45+00:00",
    "summary": "Synopsys’s CXL 4.0 IP aims to help designers build faster, more flexible and secure disaggregated computing architectures as AI systems demand more memory capacity and bandwidth. The post Synopsys Upd"
  },
  {
    "id": "rss:https://www.eetimes.com/andes-condor-closure-came-amid-broader-cost-cutting-effort/",
    "domain": "AI 算力 / 半导体",
    "title": "Andes Condor Closure Came Amid Broader Cost-Cutting Effort",
    "url": "https://www.eetimes.com/andes-condor-closure-came-amid-broader-cost-cutting-effort/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T22:00:00+00:00",
    "summary": "Andes Technology’s decision to close Condor was part of a broader 10-20% operational cost-cutting exercise, with Condor probably considered too expensive a bet. The post Andes Condor Closure Came Amid"
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-makes-quantum-cryogenics-modular-but-scaling-problems-remain/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM Makes Quantum Cryogenics Modular, but Scaling Problems Remain",
    "url": "https://www.eetimes.com/ibm-makes-quantum-cryogenics-modular-but-scaling-problems-remain/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:55:51+00:00",
    "summary": "IBM’s new cryogenic architecture tackles one obstacle to fault-tolerant quantum computing, while exposing wiring, control, interconnect, and reliability challenges. The post IBM Makes Quantum Cryogeni"
  },
  {
    "id": "rss:https://www.eetimes.com/running-local-llms-on-the-arduino-uno-q-board-a-practical-guide/",
    "domain": "AI 算力 / 半导体",
    "title": "Running Local LLMs on the Arduino® UNO™ Q Board: a Practical Guide",
    "url": "https://www.eetimes.com/running-local-llms-on-the-arduino-uno-q-board-a-practical-guide/",
    "source": "Arduino Team",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:00:00+00:00",
    "summary": "Learn how to run local LLMs on Arduino UNO Q — from model selection and quantization to memory constraints and real-world edge AI use cases. The post Running Local LLMs on the Arduino® UNO™ Q Board: a"
  },
  {
    "id": "rss:https://www.eetimes.com/when-interoperability-becomes-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "When Interoperability Becomes Infrastructure",
    "url": "https://www.eetimes.com/when-interoperability-becomes-infrastructure/",
    "source": "Peter Hunt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T07:43:30+00:00",
    "summary": "As Matter matures, manufacturers face a new challenge: maintaining visibility into connected products after deployment. The post When Interoperability Becomes Infrastructure appeared first on EE Times"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/cooler-master-v-platinum-3000-workstation-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master V Platinum 3000 power supply review: Verified Platinum efficiency for workstations, with a stellar 12-year warranty",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/cooler-master-v-platinum-3000-workstation-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T16:44:34+00:00",
    "summary": "The Cooler Master V Platinum 3000 is a 3000W, 230V-only workstation supply built by CWT, carrying four native 12V-2x6 connectors, verified Platinum efficiency, and a twelve-year warranty."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mechanical-keyboards/grab-keychrons-compact-k8-wireless-mechanical-keyboard-for-an-all-time-low-of-usd34-87-keys-gateron-red-switches-and-white-backlight-keeb-is-56-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Grab Keychron's compact K8 wireless mechanical keyboard for an all-time low of $34 — 87-keys, Gateron Red switches, and white backlight keeb is 56% off",
    "url": "https://www.tomshardware.com/peripherals/mechanical-keyboards/grab-keychrons-compact-k8-wireless-mechanical-keyboard-for-an-all-time-low-of-usd34-87-keys-gateron-red-switches-and-white-backlight-keeb-is-56-percent-off",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T15:40:54+00:00",
    "summary": "If you need a solid compact wireless gaming or productivy keyboard and you don't have a lot to spend, Keychron's K8 87-key option is down to its lowest price of just $34.99 (or $5 less if you're a new"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/michigan-township-combats-nuclear-weapons-data-center-by-passing-ban-on-new-electrical-infrastructure-220-000-square-foot-hyperscale-project-is-backed-by-university-of-michigan-and-the-los-alamos-national-laboratory",
    "domain": "AI 算力 / 半导体",
    "title": "Michigan township combats nuclear weapons data center by passing ban on new electrical infrastructure — 220,000-square-foot hyperscale project is backed by University of Michigan and the Los Alamos Na",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/michigan-township-combats-nuclear-weapons-data-center-by-passing-ban-on-new-electrical-infrastructure-220-000-square-foot-hyperscale-project-is-backed-by-university-of-michigan-and-the-los-alamos-national-laboratory",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T15:37:29+00:00",
    "summary": "Ypsilanti Township is blocking a University of Michigan data center designed for researching nuclear weapons by temporarily stopping the electrical substation it needs to operate. It also put a one-ye"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/cxmt-planned-to-use-stolen-samsung-ip-to-develop-its-dram-court-hears-former-samsung-engineer-who-jumped-to-chinese-memory-maker-now-behind-bars",
    "domain": "AI 算力 / 半导体",
    "title": "CXMT planned to use stolen Samsung IP to develop its DRAM, court hears — former Samsung engineer who jumped to Chinese memory maker now behind bars",
    "url": "https://www.tomshardware.com/pc-components/dram/cxmt-planned-to-use-stolen-samsung-ip-to-develop-its-dram-court-hears-former-samsung-engineer-who-jumped-to-chinese-memory-maker-now-behind-bars",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T15:37:14+00:00",
    "summary": "Former Samsung engineers stole process recipe of the company's 18nm-class DRAM node to sell it to CXMT, according to a new report from Korea."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dell-xps-13-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Dell XPS 13 (2026) review: the new bar for mainstream Windows laptop excellence",
    "url": "https://www.tomshardware.com/laptops/dell-xps-13-2026-review",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T14:07:31+00:00",
    "summary": "The return of the XPS 13 is a triumph of (somewhat) affordable premium portable computing. It’s no powerhouse in terms of performance, but it gets more than enough right to recommend for Windows users"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/catastrophic-gta-vi-leak-is-a-full-working-build-notorious-hacker-cyberleek-taunts-rockstar-games-by-spraying-the-word-leek-onto-a-wall-in-game-with-bullets",
    "domain": "AI 算力 / 半导体",
    "title": "Catastrophic GTA VI leak is a full working build — notorious hacker CyberLeek taunts Rockstar Games by spraying the word 'leek' onto a wall in-game with bullets",
    "url": "https://www.tomshardware.com/video-games/catastrophic-gta-vi-leak-is-a-full-working-build-notorious-hacker-cyberleek-taunts-rockstar-games-by-spraying-the-word-leek-onto-a-wall-in-game-with-bullets",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:55:32+00:00",
    "summary": "Cyberleek has leaked another in-game footage of GTA VI, with some social media users claiming that it an actual build of the title. This is the second leak coming from the hacker, who claimed that the"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/synopsys-validates-a-pcie-6-phy-inside-a-face-to-face-3d-stack",
    "domain": "AI 算力 / 半导体",
    "title": "Synopsys validates a PCIe 6.0 PHY inside a face-to-face 3D stack at 64 GT/s — says it got there by pulling apart an existing 2D test chip",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/synopsys-validates-a-pcie-6-phy-inside-a-face-to-face-3d-stack",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:32:00+00:00",
    "summary": "Synopsys has published silicon results for what it calls the first 3D PCIe 6.0 test chip, a 5nm PHY built into a face-to-face stacked package."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/virginia-county-with-250-data-centers-begins-to-rein-in-building-loudouns-more-than-250-data-centers-made-it-one-of-the-richest-counties-in-the-us-but-residents-are-pushing-back",
    "domain": "AI 算力 / 半导体",
    "title": "Virginia county with 250 data centers begins to rein in building — Loudoun’s more than 250 data centers made it one of the richest counties in the US, but residents are pushing back",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/virginia-county-with-250-data-centers-begins-to-rein-in-building-loudouns-more-than-250-data-centers-made-it-one-of-the-richest-counties-in-the-us-but-residents-are-pushing-back",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:19:34+00:00",
    "summary": "Loudoun County recently changed its zoning policy which treated data centers as office parks. These projects now have to go through an approval process from the people and the local government, a sign"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/sk-hynix-reaches-tentative-agreement-with-disgruntled-workers-usd1-79-billion-potential-profit-pool-could-see-staff-get-usd50-000-each",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix will pay staff $50,000 apiece according to a tentative agreement with disgruntled workers — $1.79 billion potential profit pool will be split between cash and stock grants",
    "url": "https://www.tomshardware.com/pc-components/dram/sk-hynix-reaches-tentative-agreement-with-disgruntled-workers-usd1-79-billion-potential-profit-pool-could-see-staff-get-usd50-000-each",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:15:05+00:00",
    "summary": "SK hynix removes 10% operating profit cap for employee profit-sharing program; union agrees to get bonuses in cash and stock."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/seasonic-introduces-the-worlds-first-80-plus-ruby-certified-psu-using-a-standard-atx-form-factor",
    "domain": "AI 算力 / 半导体",
    "title": "Seasonic unveils world's first 80 Plus Ruby ATX power supply — Prime Enterprise RX-1600 delivers 1600W with up to 95.4% efficiency",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/seasonic-introduces-the-worlds-first-80-plus-ruby-certified-psu-using-a-standard-atx-form-factor",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T12:00:00+00:00",
    "summary": "Seasonic has introduced the world's first 80 Plus Ruby certified 115V ATX PSU, the Prime RX-1600. The new unit features an efficiency rating of up to 95% at 20% to 50% load."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/get-32gb-of-ram-for-only-usd241-in-this-3-item-gaming-combo-from-newegg-save-usd249-on-this-inclusive-bundle-with-ryzen-7-9800x3d-corsair-vengeance-ram-and-a-gigabyte-x870e-motherboard",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB of RAM for only $241 in this 3-item gaming combo from Newegg —save $249 on this inclusive bundle with Ryzen 7 9800X3D, Corsair Vengeance RAM, and a Gigabyte X870E motherboard",
    "url": "https://www.tomshardware.com/pc-components/ddr5/get-32gb-of-ram-for-only-usd241-in-this-3-item-gaming-combo-from-newegg-save-usd249-on-this-inclusive-bundle-with-ryzen-7-9800x3d-corsair-vengeance-ram-and-a-gigabyte-x870e-motherboard",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T11:46:55+00:00",
    "summary": "Newegg's AM5 combo bundles 32GB of Corsair Vengeance DDR5-6000 RAM with a Ryzen 7 9800X3D and Gigabyte X870E board for only $1,009.99. $249 savings puts the RAM at only $241"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/the-supercomputer-race-no-longer-means-what-it-used-to-as-rankings-lose-relevance-in-the-ai-era-as-privately-held-compute-clusters-are-built-running-hpl-becomes-a-distraction",
    "domain": "AI 算力 / 半导体",
    "title": "The supercomputer race no longer means what it used to, as rankings lose relevance in the AI era — as privately held compute clusters are built, running HPL becomes a distraction",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/the-supercomputer-race-no-longer-means-what-it-used-to-as-rankings-lose-relevance-in-the-ai-era-as-privately-held-compute-clusters-are-built-running-hpl-becomes-a-distraction",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T11:40:00+00:00",
    "summary": "We review the current state of high-performance supercomputing, interviewing experts, including the deputy head of high-performance computing at GWDG, to find out exactly where the current race stands"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/smic-is-raising-wafer-prices-into-a-shortage-as-sanctions-wall-off-chinas-ai-demand",
    "domain": "AI 算力 / 半导体",
    "title": "SMIC posts record $3B quarter and hikes wafer prices — US sanctions hand Chinese foundry a captive AI market",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/smic-is-raising-wafer-prices-into-a-shortage-as-sanctions-wall-off-chinas-ai-demand",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T11:20:00+00:00",
    "summary": "SMIC posted its first $3 billion quarter earlier this month, with revenue up 36.1% year on year, net profit nearly tripling to $479.2 million."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/physical-media-nostalgia-sees-fundraisers-flock-to-blu-ray-kickstarter-drive-with-9-in-1-dock-achieves-160x-funding-goal-halfway-through-campaign",
    "domain": "AI 算力 / 半导体",
    "title": "Physical media nostalgia sees fundraisers flock to Blu-Ray Kickstarter — drive with 9-in-1 dock achieves 160x funding goal halfway through campaign",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/physical-media-nostalgia-sees-fundraisers-flock-to-blu-ray-kickstarter-drive-with-9-in-1-dock-achieves-160x-funding-goal-halfway-through-campaign",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T11:00:39+00:00",
    "summary": "A 'grand piano style' Blu-ray drive and USB dock has got tech fans excited over on Kickstarter."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/g-skill-starts-usd2-4m-class-action-payout-over-misleading-ram-speeds-usd20-to-usd25-cash-payments-heading-to-claimants",
    "domain": "AI 算力 / 半导体",
    "title": "G.Skill pays out $2.4M settlement over misleading DDR4 and DDR5 speed marketing — buyers get $20 to $25 as vendor agrees to XMP and EXPO packaging warnings",
    "url": "https://www.tomshardware.com/pc-components/ram/g-skill-starts-usd2-4m-class-action-payout-over-misleading-ram-speeds-usd20-to-usd25-cash-payments-heading-to-claimants",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T11:00:00+00:00",
    "summary": "G.Skill has started sending payments to claimants regarding the $2.4 million lawsuit over inadequately marketed RAM speeds."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/pine64-halts-all-linux-device-production-until-at-least-mid-2027-as-memory-shortage-bites",
    "domain": "AI 算力 / 半导体",
    "title": "Pine64 halts all Linux hardware manufacturing through at least mid-2027 due to shortages — memory crunch forces open-source maker to freeze SBCs, tablets, and phones",
    "url": "https://www.tomshardware.com/pc-components/dram/pine64-halts-all-linux-device-production-until-at-least-mid-2027-as-memory-shortage-bites",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T10:30:00+00:00",
    "summary": "Microcontroller-based products, such as the PineTime smartwatch, PineVoice smart speaker, and Pinecil soldering iron, aren't affected."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/get-an-astonishing-oled-5090-gaming-laptop-for-usd3-599-usd800-off-gigabyte-aorus-master-16-features-a-24-core-arrow-lake-cpu-32gb-ram-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Get an astonishing OLED 5090 gaming laptop for $3,599, $800 off — Gigabyte Aorus Master 16 features a 24-core Arrow Lake CPU, 32GB RAM, 2TB SSD",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/get-an-astonishing-oled-5090-gaming-laptop-for-usd3-599-usd800-off-gigabyte-aorus-master-16-features-a-24-core-arrow-lake-cpu-32gb-ram-2tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T10:16:16+00:00",
    "summary": "Get $800 off this RTX 5090 gaming laptop with Intel Core Ultra 9 275HX, 32GB of RAM, and a 2TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/federal-judge-strikes-down-atf-ghost-gun-rule-for-3d-printed-parts-says-restrictions-violate-fifth-amendment-and-historical-tradition-of-diy-gunsmithing",
    "domain": "AI 算力 / 半导体",
    "title": "Federal judge strikes down ATF 'ghost gun' rule for 3D printed parts — says restrictions violate Fifth Amendment and historical tradition of DIY gunsmithing",
    "url": "https://www.tomshardware.com/3d-printing/federal-judge-strikes-down-atf-ghost-gun-rule-for-3d-printed-parts-says-restrictions-violate-fifth-amendment-and-historical-tradition-of-diy-gunsmithing",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T10:00:00+00:00",
    "summary": "Judge Reed O'Connor of the Northern District of Texas said that the ATF ruling that putting part kits that can easily be turned into firearms in the same category as actual guns is unconstitutional. H"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/modder-builds-working-switch-2-joy-cons-inside-original-wii-remote-shells",
    "domain": "AI 算力 / 半导体",
    "title": "Console modder builds working Switch 2 Joy-Cons inside original Wii Remote shells — motion-sensing controllers snap magnetically onto a Switch 2",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/modder-builds-working-switch-2-joy-cons-inside-original-wii-remote-shells",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T09:45:00+00:00",
    "summary": "YouTuber Kouzex has transplanted the internals of a pair of Joy-Con 2 controllers into two original Wii Remote shells, producing motion controllers that snap magnetically onto a Switch 2."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/amazon-delivery-drone-dumps-texas-womans-parcel-straight-into-her-swimming-pool-viral-video-surfaces-the-same-week-the-company-announces-500-city-prime-air-expansion",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon delivery drone dumps Texas woman's parcel straight into her swimming pool — viral video surfaces the same week the company announces 500-city Prime Air expansion",
    "url": "https://www.tomshardware.com/tech-industry/drones/amazon-delivery-drone-dumps-texas-womans-parcel-straight-into-her-swimming-pool-viral-video-surfaces-the-same-week-the-company-announces-500-city-prime-air-expansion",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T09:35:39+00:00",
    "summary": "A Texas woman has filmed the moment an Amazon Prime delivery drone dumped her package straight into her swimming pool."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-raises-advanced-foundry-prices-by-up-to-15-percent-as-ai-demand-fills-its-4nm-lines",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung raises advanced foundry prices by up to 15% as AI demand fills its 4nm lines, report claims — Chinese customers accepting the largest hikes",
    "url": "https://www.tomshardware.com/tech-industry/samsung-raises-advanced-foundry-prices-by-up-to-15-percent-as-ai-demand-fills-its-4nm-lines",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T16:15:53+00:00",
    "summary": "Samsung raised prices on new orders across its 4nm, 5nm, and 8nm foundry processes in July, with increases reaching 15% for customers in China."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/china-shifting-massive-ai-data-center-complexes-to-rural-provinces-to-tap-surplus-energy-eastern-data-western-computing-strategy-has-chinese-tech-giants-huawei-and-tencent-building-ai-infrastructure-guizhou",
    "domain": "AI 算力 / 半导体",
    "title": "China shifting massive AI data center complexes to rural provinces to tap surplus energy — ‘Eastern Data, Western Computing’ strategy has Chinese tech giants Huawei and Tencent building AI infrastruct",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/china-shifting-massive-ai-data-center-complexes-to-rural-provinces-to-tap-surplus-energy-eastern-data-western-computing-strategy-has-chinese-tech-giants-huawei-and-tencent-building-ai-infrastructure-guizhou",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T15:49:04+00:00",
    "summary": "Chinese tech giants are putting up data centers in rural Chinese provinces with zero resistance. The abundance of land and energy in these areas allowed infrastructure to easily be built with limited "
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/qualcomm-retracts-select-snapdragon-c-power-efficiency-benchmarks-nearly-a-week-after-publication-updated-slide-removes-idle-apps-and-web-browsing-results",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm retracts select Snapdragon C power efficiency benchmarks nearly a week after publication — updated slide removes idle apps and web browsing results",
    "url": "https://www.tomshardware.com/laptops/qualcomm-retracts-select-snapdragon-c-power-efficiency-benchmarks-nearly-a-week-after-publication-updated-slide-removes-idle-apps-and-web-browsing-results",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T15:28:06+00:00",
    "summary": "Qualcomm has issued an updated slide for its Snapdragon C power efficiency claims, removing two benchmarks from the results."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/overclocking/you-can-now-buy-a-delidded-ryzen-9-9950x3d2-dual-edition-for-usd1-403-stripped-dual-cache-offering-is-usd500-more-expensive-than-regular-version",
    "domain": "AI 算力 / 半导体",
    "title": "You can now buy a delidded Ryzen 9 9950X3D2 Dual Edition for $1,403 — stripped dual-cache offering is $500 more expensive than regular version",
    "url": "https://www.tomshardware.com/pc-components/overclocking/you-can-now-buy-a-delidded-ryzen-9-9950x3d2-dual-edition-for-usd1-403-stripped-dual-cache-offering-is-usd500-more-expensive-than-regular-version",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:44:47+00:00",
    "summary": "Thermal Grizzly offers the halo CPU with the pop topped for an egregious price, yet it almost makes sense on this chip."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/hacker-leaks-gta-vi-gameplay-and-map-to-protest-digital-only-release-claims-pre-orders-are-a-legacy-of-physical-game-releases",
    "domain": "AI 算力 / 半导体",
    "title": "Hacker leaks GTA VI gameplay and map to protest digital-only release — claims pre-orders are a legacy of physical game releases",
    "url": "https://www.tomshardware.com/video-games/hacker-leaks-gta-vi-gameplay-and-map-to-protest-digital-only-release-claims-pre-orders-are-a-legacy-of-physical-game-releases",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:37:23+00:00",
    "summary": "Hacker Cyberleek leaked gameplay clips and the entire map of GTA VI in protest of Rockstar's decision to launch pre-orders of a digital game. They claim that pre-orders were created because physical d"
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/google-to-stop-making-pixel-devices-in-china-report-claims-india-and-vietnam-prime-candidates-for-manufacturing-shift-owing-to-beijing-washington-tensions",
    "domain": "AI 算力 / 半导体",
    "title": "Google to stop making Pixel devices in China, report claims — India and Vietnam prime candidates for manufacturing shift owing to Beijing-Washington tensions",
    "url": "https://www.tomshardware.com/phones/google-to-stop-making-pixel-devices-in-china-report-claims-india-and-vietnam-prime-candidates-for-manufacturing-shift-owing-to-beijing-washington-tensions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T12:40:00+00:00",
    "summary": "To reduce reliance on China, Google plans to relocate production of Pixel smartphones, smartwatches, and headsets from China to India and Vietnam."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/comcast-turns-xfinity-routers-into-home-motion-detectors-free-wi-fi-sensing-feature-tracks-rf-interference-with-zero-extra-hardware-required",
    "domain": "AI 算力 / 半导体",
    "title": "Comcast turns Xfinity routers into home motion detectors — free Wi-Fi sensing feature tracks RF interference with zero extra hardware required",
    "url": "https://www.tomshardware.com/networking/routers/comcast-turns-xfinity-routers-into-home-motion-detectors-free-wi-fi-sensing-feature-tracks-rf-interference-with-zero-extra-hardware-required",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T12:20:00+00:00",
    "summary": "To appease concerns about privacy, Wi-Fi Motion is opt-in"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsungs-fab-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's fab roadmaps examined — Taylor, Pyeongtaek, and the yield woes behind a $16.5 billion Tesla deal",
    "url": "https://www.tomshardware.com/tech-industry/samsungs-fab-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T12:00:00+00:00",
    "summary": "Divided across two countries and four campuses, Samsung's fab roadmap runs from the Korean bases at Pyeongtaek, Hwaseong, and Giheung to the new U.S. site at Taylor."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/jason-kelce-led-marketing-campaign-asks-beer-drinkers-to-send-their-pee-to-ai-data-centers-liquid-death-and-garage-beer-skit-claims-ai-data-centers-waste-millions-of-gallons-of-water",
    "domain": "AI 算力 / 半导体",
    "title": "Jason Kelce-led marketing campaign asks beer drinkers to send their pee to AI data centers — Liquid Death and Garage Beer skit claims 'AI data centers waste millions of gallons of water'",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/jason-kelce-led-marketing-campaign-asks-beer-drinkers-to-send-their-pee-to-ai-data-centers-liquid-death-and-garage-beer-skit-claims-ai-data-centers-waste-millions-of-gallons-of-water",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:55:24+00:00",
    "summary": "Two indie brands join together in a viral ad campaign asking people to pee on computers. Taylor Swift's brother-in-law, Jason Kelce, who co-owns one of the brands, stars in this humorous ad where he p"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/beijing-ai-bar-pours-pints-of-foam-with-free-deepseek-tokens-served-from-two-nvidia-dgx-sparks",
    "domain": "AI 算力 / 半导体",
    "title": "Beijing AI bar that offers unlimited free DeepSeek coding tokens with $1.50 drink haemorrhaging cash — 'the bar is completely losing money, ' owner admits",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/beijing-ai-bar-pours-pints-of-foam-with-free-deepseek-tokens-served-from-two-nvidia-dgx-sparks",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:44:32+00:00",
    "summary": "An AI-themed bar in Beijing's Zhongguancun tech hub hands out free, unlimited DeepSeek tokens with its drinks, running inference locally on two Nvidia DGX Spark mini-PCs."
  },
  {
    "id": "hn:49322519",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX at end of second quarter",
    "url": "https://www.cnbc.com/2026/08/14/nvidia-discloses-21-billion-stake-in-spacex-at-end-of-second-quarter.html",
    "source": "johnbarron",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-08-16T18:40:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49346906",
    "domain": "AI 算力 / 半导体",
    "title": "Ask HN: Do you feel comfortable admitting that you use AI?",
    "url": "https://news.ycombinator.com/item?id=49346906",
    "source": "var0xyz",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T15:16:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49282762",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia doubles RTX PRO 6000 Blackwell's MSRP to a staggering $16,000",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-13T07:28:54+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/marvell-targets-ai-bottlenecks-with-memory-disaggregation-portfolio/",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell Targets AI Bottlenecks with Memory-Disaggregation Portfolio",
    "url": "https://www.eetimes.com/marvell-targets-ai-bottlenecks-with-memory-disaggregation-portfolio/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:39:27+00:00",
    "summary": "Marvell attacks AI’s memory choke point with SSD, CXL, and photonic fabrics to push data nearer compute. The post Marvell Targets AI Bottlenecks with Memory-Disaggregation Portfolio appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/why-standardized-interfaces-are-critical-to-accelerating-humanoid-development/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Standardized Interfaces Are Critical to Accelerating Humanoid Development",
    "url": "https://www.eetimes.com/why-standardized-interfaces-are-critical-to-accelerating-humanoid-development/",
    "source": "Edo Cohen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T08:15:00+00:00",
    "summary": "Humanoids won’t scale on AI hype alone; standardized MIPI interfaces can cut power, wiring, and cost. The post Why Standardized Interfaces Are Critical to Accelerating Humanoid Development appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-bets-on-the-classical-side-of-quantum-computing/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Bets on the Classical Side of Quantum Computing",
    "url": "https://www.eetimes.com/nvidia-bets-on-the-classical-side-of-quantum-computing/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T18:31:00+00:00",
    "summary": "Nvidia positions classical computing infrastructure as a critical layer in the race to build useful quantum computers. The post Nvidia Bets on the Classical Side of Quantum Computing appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/tiny-esim-global-reach-simplifying-cellular-connectivity-for-consumer-electronics/",
    "domain": "AI 算力 / 半导体",
    "title": "Tiny eSIM, Global Reach: Simplifying Cellular Connectivity for Consumer Electronics",
    "url": "https://www.eetimes.com/tiny-esim-global-reach-simplifying-cellular-connectivity-for-consumer-electronics/",
    "source": "Infineon Technologies and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T14:29:25+00:00",
    "summary": "Join this webinar and discover the OPTIGA™ Connect Consumer OC1230, the world's smallest, ultra-low-power eSIM solution built on Infineon's TEGRION™ 28 nm tech. The post Tiny eSIM, Global Reach: Simpl"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-functional-safety-why-asil-compliance-starts-with-electromagnetic-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Functional Safety: Why ASIL Compliance Starts with Electromagnetic Design",
    "url": "https://www.eetimes.com/automotive-functional-safety-why-asil-compliance-starts-with-electromagnetic-design/",
    "source": "Cadence Design Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T14:00:00+00:00",
    "summary": "Automotive electronic systems face relentless pressure to meet electromagnetic compatibility (EMC), signal integrity (SI), and power integrity (PI) targets while satisfying strict ASIL safety requirem"
  },
  {
    "id": "hn:49325115",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Uses Old Fabs to Make New Chips [video]",
    "url": "https://www.youtube.com/watch?v=cDxVYQrxeiQ",
    "source": "eig",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-17T00:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49306491",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://www.ft.com/content/6f66a76d-0b2d-4301-886c-87ecc046731b",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-15T01:02:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289112",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.7 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 968,
    "published_at": "2026-08-13T17:23:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 867,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 620,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49220126",
    "domain": "大厂 AI 动态",
    "title": "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones",
    "url": "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/",
    "source": "bhavansig",
    "platform": "hackernews",
    "points": 449,
    "published_at": "2026-08-08T09:18:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 384,
    "published_at": "2026-07-29T11:44:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49267928",
    "domain": "大厂 AI 动态",
    "title": "llama.cpp",
    "url": "https://llama.app",
    "source": "kristianpaul",
    "platform": "hackernews",
    "points": 364,
    "published_at": "2026-08-12T04:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184757",
    "domain": "大厂 AI 动态",
    "title": "Demis Hassabis is moving from CEO to Chairman at Google DeepMind",
    "url": "https://www.axios.com/2026/08/05/google-deepmind-demis-hassabis-ai",
    "source": "ot",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-08-05T16:05:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259339",
    "domain": "大厂 AI 动态",
    "title": "Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp",
    "url": "https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md",
    "source": "frabonacci",
    "platform": "hackernews",
    "points": 307,
    "published_at": "2026-08-11T14:50:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49256057",
    "domain": "大厂 AI 动态",
    "title": "What I learned by putting GitHub Copilot behind a MitM proxy",
    "url": "https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm",
    "source": "j0selit0",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-08-11T10:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-07-27T09:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49198583",
    "domain": "大厂 AI 动态",
    "title": "Show HN: The Channels SDK – Bring Any Agent to Any Channel (Slack, MS Teams)",
    "url": "https://github.com/CopilotKit/channels-sdk",
    "source": "davidmckayv",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-06T16:05:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/981536/genki-manta-wireless-customizable-controller-tmr-screen",
    "domain": "大厂 AI 动态",
    "title": "Genki’s new customizable controller has a big screen and adjustable buttons",
    "url": "https://www.theverge.com/tech/981536/genki-manta-wireless-customizable-controller-tmr-screen",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T02:00:00+00:00",
    "summary": "After collaborating with 8BitDo on a gamepad two years ago, Genki launched the first controller the company designed from the ground up today. With an unorthodox design that positions its thumbsticks "
  },
  {
    "id": "rss:https://www.theverge.com/tech/983088/google-discover-ai-chatbot-feed",
    "domain": "大厂 AI 动态",
    "title": "Google Discover is getting an AI chatbot-tuned feed",
    "url": "https://www.theverge.com/tech/983088/google-discover-ai-chatbot-feed",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T21:50:22+00:00",
    "summary": "Google will soon allow you to customize your Discover feed by describing what you want to see. The new feature, rolling out to the Google app in the \"coming days,\" will use AI to automatically tweak y"
  },
  {
    "id": "rss:https://www.theverge.com/games/982986/riot-games-league-of-legends-fighting-game-2xko-end-development",
    "domain": "大厂 AI 动态",
    "title": "Riot is ending development on its League of Legends fighting game",
    "url": "https://www.theverge.com/games/982986/riot-games-league-of-legends-fighting-game-2xko-end-development",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T19:59:09+00:00",
    "summary": "Riot Games is already winding down work on 2XKO, the free-to-play League of Legends fighting game, less than a year after its initial launch. Riot says \"active development\" will conclude at the end of"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/982910/genesis-gv90-ev-suv-coach-door-heated-floor",
    "domain": "大厂 AI 动态",
    "title": "The Genesis GV90 blows the bloody doors off what’s possible in EV design",
    "url": "https://www.theverge.com/transportation/982910/genesis-gv90-ev-suv-coach-door-heated-floor",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T19:52:57+00:00",
    "summary": "Genesis, Hyundai's luxury brand, just revealed its first full-size, three-row electric SUV for the US market, the GV90. And arguably it has some of the wildest designs and features in the auto market "
  },
  {
    "id": "rss:https://www.theverge.com/tech/982955/meta-mark-zuckerberg-strancally-castle-ireland",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg bought an Irish castle",
    "url": "https://www.theverge.com/tech/982955/meta-mark-zuckerberg-strancally-castle-ireland",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T18:50:14+00:00",
    "summary": "Meta CEO Mark Zuckerberg now owns an actual castle. Zuckerberg and his wife Priscilla Chan bought Strancally Castle and its 440-acre estate in Ireland \"several weeks ago,\" according to The Irish Times"
  },
  {
    "id": "rss:https://www.theverge.com/games/982885/roblox-australia-safety-regulator-child-safety",
    "domain": "大厂 AI 动态",
    "title": "Australia says Roblox hasn&#8217;t fixed its child predator problem",
    "url": "https://www.theverge.com/games/982885/roblox-australia-safety-regulator-child-safety",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T17:42:34+00:00",
    "summary": "Roblox is promising more changes to its child safety features following testing from Australia's online safety regulator, eSafety. eSafety has been looking into concerns that the company hasn't been i"
  },
  {
    "id": "rss:https://www.theverge.com/policy/982863/fcc-kills-gigabit-goal",
    "domain": "大厂 AI 动态",
    "title": "FCC officially decides gigabit speeds are too good for you",
    "url": "https://www.theverge.com/policy/982863/fcc-kills-gigabit-goal",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T17:38:30+00:00",
    "summary": "Another day, another sad thing to report about our compromised Federal Communications Commission. Chairman Brendan Carr has followed through on his 2025 threat to kill long-term broadband speed goals "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/982800/framework-laptop-13-amd-7040-bios-320-bricking-warranty",
    "domain": "大厂 AI 动态",
    "title": "Framework says it&#8217;s addressing a BIOS update that bricked some of its older laptops",
    "url": "https://www.theverge.com/gadgets/982800/framework-laptop-13-amd-7040-bios-320-bricking-warranty",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T17:16:02+00:00",
    "summary": "Some Framework Laptop 13 owners with last-gen AMD chips have reported that a recent BIOS update is bricking their laptops on both Windows and Linux. The BIOS update causing this issue is version 3.20 "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/982774/greg-brockman-openai-role-expansion",
    "domain": "大厂 AI 动态",
    "title": "It’s Greg Brockman’s OpenAI now",
    "url": "https://www.theverge.com/ai-artificial-intelligence/982774/greg-brockman-openai-role-expansion",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T15:45:55+00:00",
    "summary": "OpenAI has had a hell of a year. The company spent months battling former cofounder Elon Musk in a sensational jury trial, was hit with a high-profile trade secrets lawsuit from Apple, and faced wides"
  },
  {
    "id": "rss:https://www.theverge.com/tech/982791/this-app-makes-the-pixel-11s-hilight-feature-actually-useful",
    "domain": "大厂 AI 动态",
    "title": "This app makes the Pixel 11&#8217;s HiLight feature actually useful",
    "url": "https://www.theverge.com/tech/982791/this-app-makes-the-pixel-11s-hilight-feature-actually-useful",
    "source": "David Imel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T15:30:34+00:00",
    "summary": "Google's new HiLight notification LED on the Pixel 11 Pro is nearly useless. Out of the box, the only two things it can glow for are when the phone is face down and you're interacting with Gemini, or "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/tesla-uber-and-waymo-all-get-the-ok-to-operate-thousands-of-robotaxis-in-nevada/",
    "domain": "大厂 AI 动态",
    "title": "Tesla, Uber, and Waymo all get the OK to operate thousands of robotaxis in Nevada",
    "url": "https://techcrunch.com/2026/08/20/tesla-uber-and-waymo-all-get-the-ok-to-operate-thousands-of-robotaxis-in-nevada/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:23:36+00:00",
    "summary": "Together, these permits would allow up to 8,000 robotaxis to be deployed over the next 12 months."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/ai-data-startup-micro1-reaches-500m-gross-run-rate-amid-ai-training-boom/",
    "domain": "大厂 AI 动态",
    "title": "AI data startup Micro1 reaches $500M gross run rate amid AI training boom",
    "url": "https://techcrunch.com/2026/08/20/ai-data-startup-micro1-reaches-500m-gross-run-rate-amid-ai-training-boom/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:13:44+00:00",
    "summary": "Surging demand for AI training data is driving rapid growth for the startup and its rivals."
  },
  {
    "id": "rss:https://techcrunch.com/video/learn-what-vcs-actually-want-from-a-founder-whos-raised-1b/",
    "domain": "大厂 AI 动态",
    "title": "Learn what VCs actually want, from a founder who’s raised $1B",
    "url": "https://techcrunch.com/video/learn-what-vcs-actually-want-from-a-founder-whos-raised-1b/",
    "source": "Maggie Nye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T23:32:27+00:00",
    "summary": "Investors want founders who understand the financial reality of their business. Messy data, misunderstood metrics, or waiting until you’re nearly out of cash to start fundraising can cost founders lev"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is gaining on Anthropic with business users, new data indicates",
    "url": "https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T22:36:37+00:00",
    "summary": "Businesses are willing to flop back and forth as each lab releases new models, volatility that should give both companies' investors pause about how \"sticky\" enterprise AI spending really is."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/chatgpt-can-now-send-texts-for-you-with-new-apple-messages-plugin/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT can now send texts for you with new Apple Messages plug-in",
    "url": "https://techcrunch.com/2026/08/20/chatgpt-can-now-send-texts-for-you-with-new-apple-messages-plugin/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T22:09:51+00:00",
    "summary": "Ever wanted someone else to do your texting for you? ChatGPT is being offered up as an automated text scribe via a new Apple Messages integration."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/the-enhanced-games-techs-steroid-extravaganza-didnt-pay-off-as-company-posts-60-million-loss/",
    "domain": "大厂 AI 动态",
    "title": "The Enhanced Games — tech’s steroid extravaganza — didn’t pay off, as company posts $60 million loss",
    "url": "https://techcrunch.com/2026/08/20/the-enhanced-games-techs-steroid-extravaganza-didnt-pay-off-as-company-posts-60-million-loss/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T21:08:34+00:00",
    "summary": "An effort to transform the world of sports through steroid use doesn't exactly seem to be bearing financial fruit."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/ok-can-we-actually-cool-data-centers-with-our-pee/",
    "domain": "大厂 AI 动态",
    "title": "OK, can we actually cool data centers with our pee?",
    "url": "https://techcrunch.com/2026/08/20/ok-can-we-actually-cool-data-centers-with-our-pee/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T20:53:13+00:00",
    "summary": "Jason Kelce joked that people should cool data centers with their pee, rather than potable water -- but his suggestion is not completely ludicrous."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/someone-targeted-security-researchers-using-a-fake-crypto-conference-as-a-lure/",
    "domain": "大厂 AI 动态",
    "title": "Someone targeted security researchers using a fake crypto conference as a lure",
    "url": "https://techcrunch.com/2026/08/20/someone-targeted-security-researchers-using-a-fake-crypto-conference-as-a-lure/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T20:00:00+00:00",
    "summary": "A hacker pretending to work for a leading cryptocurrency news website targeted several cybersecurity professionals using Google Docs as a way to deliver malware."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/mark-buys-a-castle/",
    "domain": "大厂 AI 动态",
    "title": "Mark buys a castle",
    "url": "https://techcrunch.com/2026/08/20/mark-buys-a-castle/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T19:55:40+00:00",
    "summary": "Mark Zuckerberg just bought a cozy abode somewhat close to Meta’s international headquarters in Ireland."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/google-gives-publishers-a-new-way-to-fight-ai-driven-traffic-losses/",
    "domain": "大厂 AI 动态",
    "title": "Google gives publishers a new way to fight AI-driven traffic losses",
    "url": "https://techcrunch.com/2026/08/20/google-gives-publishers-a-new-way-to-fight-ai-driven-traffic-losses/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T19:18:21+00:00",
    "summary": "Google is giving publishers a new button that lets readers make them a preferred source across Search, Discover, and Google News, potentially boosting their traffic as AI search sends fewer clicks to "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/runlayer-rippling-drop-lawsuits-but-the-brouhaha-is-still-a-cautionary-tale-for-founders/",
    "domain": "大厂 AI 动态",
    "title": "Runlayer, Rippling drop lawsuits — but the brouhaha is still a cautionary tale for founders",
    "url": "https://techcrunch.com/2026/08/20/runlayer-rippling-drop-lawsuits-but-the-brouhaha-is-still-a-cautionary-tale-for-founders/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T19:15:05+00:00",
    "summary": "Runlayer and Rippling have dropped their lawsuits. No money was paid. Rippling celebrated by releasing a competing product."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/castelion-hits-13b-valuation-to-mass-produce-hypersonic-missiles/",
    "domain": "大厂 AI 动态",
    "title": "Castelion hits $13B valuation to mass-produce hypersonic missiles",
    "url": "https://techcrunch.com/2026/08/20/castelion-hits-13b-valuation-to-mass-produce-hypersonic-missiles/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T19:01:41+00:00",
    "summary": "Founded in 2022, Castelion set out to manufacture hypersonic weapon systems at a lower cost and at faster speeds than traditional defense primes."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/linkdazes-smart-calendar-is-built-to-run-a-household-not-just-track-a-schedule/",
    "domain": "大厂 AI 动态",
    "title": "Linkdaze’s smart calendar is built to run a household, not just track a schedule",
    "url": "https://techcrunch.com/2026/08/20/linkdazes-smart-calendar-is-built-to-run-a-household-not-just-track-a-schedule/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T18:20:35+00:00",
    "summary": "Linkdaze's smart digital calendar stands out for not putting its features behind a paywall, including an AI meal planner tool."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/grok-keeps-sending-gibberish-responses-to-users/",
    "domain": "大厂 AI 动态",
    "title": "Grok keeps sending gibberish responses to users",
    "url": "https://techcrunch.com/2026/08/20/grok-keeps-sending-gibberish-responses-to-users/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T17:32:16+00:00",
    "summary": "Affected users told TechCrunch they were using Grok Lite, and noticed the issues as early as Wednesday morning."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/the-investors-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "The investor’s guide to TechCrunch Disrupt 2026: Everything you need to know",
    "url": "https://techcrunch.com/2026/08/20/the-investors-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T17:27:47+00:00",
    "summary": "Year after year, investors who've explored the Expo Halls, met founders, and learned from peers have proven why you need to be on the ground at Disrupt this year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/a-third-of-webpages-published-since-chatgpts-launch-show-signs-of-ai-authorship-study-finds/",
    "domain": "大厂 AI 动态",
    "title": "A third of web pages published since ChatGPT’s launch show signs of AI authorship, study finds",
    "url": "https://techcrunch.com/2026/08/20/a-third-of-webpages-published-since-chatgpts-launch-show-signs-of-ai-authorship-study-finds/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T17:18:58+00:00",
    "summary": "ChatGPT and other AI models are now authoring and editing much of the new web."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/early-cerebras-investor-adit-singh-joins-mayfield-as-infrastructure-partner/",
    "domain": "大厂 AI 动态",
    "title": "Early Cerebras investor Adit Singh joins Mayfield as infrastructure partner",
    "url": "https://techcrunch.com/2026/08/20/early-cerebras-investor-adit-singh-joins-mayfield-as-infrastructure-partner/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T17:04:53+00:00",
    "summary": "At Mayfield, Singh will focus on semiconductor, cybersecurity, and physical AI investments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/ramp-launches-its-own-ai-model-router-called-router/",
    "domain": "大厂 AI 动态",
    "title": "Ramp launches its own AI model router, called Router",
    "url": "https://techcrunch.com/2026/08/20/ramp-launches-its-own-ai-model-router-called-router/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T16:46:00+00:00",
    "summary": "Ramp has launched its own AI model routing service, dubbed Router, that lets users and companies use and switch between various large language models via an API."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/senators-demand-answers-from-tiktok-over-experiment-that-disabled-safeguards/",
    "domain": "大厂 AI 动态",
    "title": "Senators demand answers from TikTok over experiment that disabled safeguards",
    "url": "https://techcrunch.com/2026/08/20/senators-demand-answers-from-tiktok-over-experiment-that-disabled-safeguards/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T16:22:19+00:00",
    "summary": "The safeguard was designed to prevent users from being overwhelmed by harmful content, but TikTok wanted to determine whether it made the app less engaging."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/20/meta-brings-pocket-an-app-that-lets-you-vibe-code-and-share-games-to-us-users/",
    "domain": "大厂 AI 动态",
    "title": "Meta brings Pocket, an app that lets you vibe-code and share games, to US users",
    "url": "https://techcrunch.com/2026/08/20/meta-brings-pocket-an-app-that-lets-you-vibe-code-and-share-games-to-us-users/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T16:07:26+00:00",
    "summary": "Meta is bringing Pocket, its experimental AI-powered app for creating and sharing interactive games, to users across the U.S. after quietly testing it in Brazil."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-settles-with-e-u-u-s-app-store-fees-att-rules-in-germany/",
    "domain": "大厂 AI 动态",
    "title": "Apple Settles With E.U., U.S. App Store Fees, ATT Rules in Germany",
    "url": "https://stratechery.com/2026/apple-settles-with-e-u-u-s-app-store-fees-att-rules-in-germany/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T10:00:00+00:00",
    "summary": "Apple's App Store is finally facing the reality of lower fees, and the EU should be satisfied with its work; it's ok it's late."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/us-distributor-of-chinas-most-popular-humanoid-robots-pivots-after-us-ban/",
    "domain": "大厂 AI 动态",
    "title": "US distributor of China’s most popular humanoid robots pivots after US ban",
    "url": "https://arstechnica.com/gadgets/2026/08/us-distributor-of-chinas-most-popular-humanoid-robots-pivots-after-us-ban/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T22:00:11+00:00",
    "summary": "FCC ban on foreign-made robots accelerated RoboStore’s US manufacturing plans."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/europe-cancels-planned-upgrades-for-ariane-6-rocket/",
    "domain": "大厂 AI 动态",
    "title": "Europe cancels planned upgrades for Ariane 6 rocket",
    "url": "https://arstechnica.com/space/2026/08/europe-cancels-planned-upgrades-for-ariane-6-rocket/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T21:40:52+00:00",
    "summary": "Arianespace hasn’t publicly disclosed the cost for an Ariane 6 launch."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/new-9-11-documentary-finds-hope-in-the-horror/",
    "domain": "大厂 AI 动态",
    "title": "They survived 9/11; 25 years later, their bonds remain unbroken",
    "url": "https://arstechnica.com/culture/2026/08/new-9-11-documentary-finds-hope-in-the-horror/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T21:25:25+00:00",
    "summary": "Survivors reconnect with those who saved them in National Geographic's 9/11: Reunited."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/weak-roblox-safeguards-failed-to-stop-adults-contacting-kids-regulator-says/",
    "domain": "大厂 AI 动态",
    "title": "Roblox must make changes after failing to block adults creeping on kids",
    "url": "https://arstechnica.com/tech-policy/2026/08/weak-roblox-safeguards-failed-to-stop-adults-contacting-kids-regulator-says/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T17:14:08+00:00",
    "summary": "Roblox is first platform to submit to independent audits under the Online Safety Act."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/genesis-joins-the-giant-electric-suv-club-with-new-gv90/",
    "domain": "大厂 AI 动态",
    "title": "Genesis joins the giant electric SUV club with new GV90",
    "url": "https://arstechnica.com/cars/2026/08/genesis-joins-the-giant-electric-suv-club-with-new-gv90/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T14:35:58+00:00",
    "summary": "A retractable screen, a huge heads-up display, and an optional 4-seat VIP interior."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/spacexs-orbital-data-centers-would-create-a-new-category-of-e-waste/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX’s orbital data centers would create a new category of e-waste",
    "url": "https://arstechnica.com/science/2026/08/spacexs-orbital-data-centers-would-create-a-new-category-of-e-waste/",
    "source": "Scott K. Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:59:50+00:00",
    "summary": "The yeetcycling math resembles asteroid mining in reverse."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/reverse-lookup-service-exposed-millions-of-photos-of-peoples-faces/",
    "domain": "大厂 AI 动态",
    "title": "Reverse-lookup service exposed millions of photos of people’s faces",
    "url": "https://arstechnica.com/gadgets/2026/08/reverse-lookup-service-exposed-millions-of-photos-of-peoples-faces/",
    "source": "lily Hay Newman, Matt Burgess, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:29:54+00:00",
    "summary": "People-search tool ClarityCheck left database containing more than 9M image files exposed."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/grok-exfiltrates-user-data-when-malicious-instructions-are-encrypted/",
    "domain": "大厂 AI 动态",
    "title": "Grok exfiltrates user data when malicious instructions are encrypted",
    "url": "https://arstechnica.com/security/2026/08/grok-exfiltrates-user-data-when-malicious-instructions-are-encrypted/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:00:35+00:00",
    "summary": "Cryptographic Context Injection is only the latest way to break an LLM safety guardrail."
  },
  {
    "id": "hn:49335271",
    "domain": "股票",
    "title": "30-year Treasury yield tops 5.31%, the highest in 19 years",
    "url": "https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-17T18:14:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49366252",
    "domain": "股票",
    "title": "OpenAI 'will be a public company in 2027' or sooner, CFO Friar tells employees",
    "url": "https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html",
    "source": "thm",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-19T19:42:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342823",
    "domain": "股票",
    "title": "OpenAI disbanded the team that assessed catastrophic model risks",
    "url": "https://thenextweb.com/news/openai-preparedness-team-disbanded-ipo-streamlining",
    "source": "nyku",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-08-18T08:06:58+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779967",
    "domain": "股票",
    "title": "Moderna的“mRNA个性化疫苗”首度成功，中国创新药也在排队中",
    "url": "https://wallstreetcn.com/articles/3779967",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T03:39:59+00:00",
    "summary": "Moderna三期临床试验首次在大规模试验中验证mRNA个性化癌症疫苗的肿瘤治疗价值，花旗点名看好中国布局者。恒瑞旗下瑞宏迪RGL-270已进入二期、胰腺癌数据亮眼，石药SYS6026以对照设计稳步推进，康方、云顶、康希诺则各具差异化牌面，一场mRNA癌症疫苗的中国竞速赛正式鸣枪。"
  },
  {
    "id": "wscn:3779972",
    "domain": "股票",
    "title": "财政部发布会：全面升级促消费贴息政策，信用卡分期纳入支持，财政支出更多转向“投资于人”",
    "url": "https://wallstreetcn.com/articles/3779972",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T03:32:44+00:00",
    "summary": "财政部释放强烈的“稳增长、扩内需”信号，不仅预告下半年将酝酿出台务实管用的增量政策，更通过全面升级信贷贴息政策以真金白银刺激消费，并明确“十五五”期间财政支出将发生重大结构性转变——更多转向“投资于人”。"
  },
  {
    "id": "wscn:3779969",
    "domain": "股票",
    "title": "高盛交易台：当前美股市场“极度暴力”，AI投资逻辑正在重构",
    "url": "https://wallstreetcn.com/articles/3779969",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T03:30:17+00:00",
    "summary": "高盛认为AI投资焦虑已从\"需求真实性\"转向\"增长能否匹配高估值\"。随着推理成本急剧压缩，算力卖家与上游供应链护城河日益脆弱，板块估值承压。英伟达财报预计仅为中性催化剂。宏观层面，美财政部扩大长端国债购回规模，或对美元走弱与黄金上涨产生深远影响。"
  },
  {
    "id": "wscn:3779965",
    "domain": "股票",
    "title": "创业板涨超1%，算力硬件拉升、“易中天”齐涨，恒指、恒科指双双走高，泡泡玛特一度跌8%",
    "url": "https://wallstreetcn.com/articles/3779965",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T02:02:53+00:00",
    "summary": "IGBT概念股表现活跃，士兰微涨停，斯达半导、扬杰科技、华润微、新洁能、宏微科技跟涨。液冷服务器概念表现活跃，飞龙股份涨停，大元泵业、冰轮环境、川环科技、腾龙股份跟涨。"
  },
  {
    "id": "wscn:3779154",
    "domain": "股票",
    "title": "医药行业的三重共振：资金转向、业绩反转和AI重构，谁在买入？在买什么？",
    "url": "https://wallstreetcn.com/premium/articles/3779154?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T02:02:42+00:00",
    "summary": "AI对制药研发底座的重构——这可能是医药行业未来十年最大的结构性阿尔法。"
  },
  {
    "id": "wscn:3779963",
    "domain": "股票",
    "title": "对冲基金不再“All in AI”：美股资金正转向医疗、金融和能源",
    "url": "https://wallstreetcn.com/articles/3779963",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T02:01:18+00:00",
    "summary": "AI交易七月巨震成分水岭，高盛表示，对冲基金VIP持仓单月跑输标普500等权重指数11个百分点，创逾20年最差纪录。在此背景下，对冲基金从拥挤的AI仓位转向医疗、金融、能源三大板块，其中金融板块超配升至金融危机前以来最高，能源持仓创2015年来新高，十年级别的仓位再平衡或预示新一轮相对收益机会正在积聚。"
  },
  {
    "id": "wscn:3779964",
    "domain": "股票",
    "title": "全球存储：长协定下限，回购看比例",
    "url": "https://wallstreetcn.com/articles/3779964",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T01:55:51+00:00",
    "summary": "华泰证券认为当前市场已进入\"盈利仍强、估值先行回落\"阶段，关注点从\"盈利上修空间\"转向\"盈利下限\"。基于长约地板价压力测试，若2027年ASP较2Q26下降约40%，对应行业2027E PE约14倍。股东回报方面，海力士已将FCF回报目标上调至超50%，美系厂商亦逐步向100%超额现金返还过渡，回购力度成为估值支撑的重要变量。"
  },
  {
    "id": "wscn:3779966",
    "domain": "股票",
    "title": "科创硬科技企业成绩单亮眼！科创小盘投资再添利器，科创200ETF重磅上市",
    "url": "https://wallstreetcn.com/articles/3779966",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T01:47:19+00:00",
    "summary": "科创板硬科技企业陆续交出半年度亮眼成绩单。截至8月19日，科创板88家已披露2026年半年报的上市公..."
  },
  {
    "id": "wscn:3779962",
    "domain": "股票",
    "title": "1.9%！日本7月通胀升至年内高点，能源与鲜食价格双双加速",
    "url": "https://wallstreetcn.com/articles/3779962",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T01:36:27+00:00",
    "summary": "能源价格自2025年11月来首次转正，中东冲突推高原油成本已超出政府补贴的对冲空间；7月批发通胀率达到7.2%，其中电费是最大贡献项，显示能源成本已从生产端向消费端加速传导。鲜食价格同比急升7%，较上月近乎翻倍。数据走强印证官方预警，进一步强化市场对日本央行加快收紧货币政策预期。"
  },
  {
    "id": "wscn:3779961",
    "domain": "股票",
    "title": "大手笔！OpenAI全面开源Codex Harness",
    "url": "https://wallstreetcn.com/articles/3779961",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T01:17:43+00:00",
    "summary": "OpenAI开源Codex Harness三大核心组件（CLI工具、官方SDK、app-server），以Apache-2.0许可发布。Harness作为驱动AI智能体的底层执行框架，可无缝嵌入开发者自有产品，彻底告别\"通用聊天框\"模式。同时将界面、数据与安全审批权交还开发者，彻底打通AI企业级落地的最后一公里。"
  },
  {
    "id": "wscn:3779959",
    "domain": "股票",
    "title": "美债回购“信号意义”重于“实际效果”！野村：如果市场继续恶化，美联储会下场“YCC或QE”",
    "url": "https://wallstreetcn.com/articles/3779959",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:52:42+00:00",
    "summary": "美国财政部仓促祭出债务回购，野村证券策略师McElligott一针见血：这不过是\"子弹穿孔上的创可贴\"——真正的信号是当局已承认长端利率失控触及红线。企业债发行激增59%、伊朗局势推高能源价格、全球财政扩张三重压力叠加，YCC与QE的扳机正在预热，但在阀门打开之前，市场必须先变得更糟。"
  },
  {
    "id": "wscn:3779960",
    "domain": "股票",
    "title": "美光CEO：AI彻底重写存储芯片周期逻辑，客户需求超出公司供给约50%",
    "url": "https://wallstreetcn.com/articles/3779960",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:42:50+00:00",
    "summary": "Mehrotra认为，AI推动存储从可替换商品升级为系统性能的核心变量——没有高性能存储，AI无法运行。需求来源从单一数据中心扩展至自动驾驶、机器人及消费电子，使供需长期偏紧。客户采购模式也从\"比价竞标\"转向与美光协同设计，深度绑定提升定价权。存储行业的周期性逻辑正被结构性增长取代。"
  },
  {
    "id": "wscn:3779895",
    "domain": "股票",
    "title": "社零降速至0.6%：北京上海松楼市，稳增长开始加码了吗？",
    "url": "https://wallstreetcn.com/premium/articles/3779895?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:41:36+00:00",
    "summary": "7月经济数据再次暴露内需偏弱：社零增速降至0.6%，投资继续承压，居民与企业中长期融资需求偏弱。与此同时，北京放松购房约束并加码公积金支持，上海继续优化住房政策，全国公积金制度扩围，消费与财政工具也密集落地。单看任何一项政策，力度都谈不上激进；放在同一时间轴上，却开始显现逆周期政策由局部托底向组合式加码过渡的迹象。市场真正需要判断的是，这会不会成为下半年稳增长政策进一步升级的起点？"
  },
  {
    "id": "wscn:3779953",
    "domain": "股票",
    "title": "\"7级地震之后一定还有余震\"？7月AI巨亏之后，对冲基金周三再遭重创",
    "url": "https://wallstreetcn.com/articles/3779953",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:30:12+00:00",
    "summary": "高盛数据显示，周三系统性多空基金单日跌幅达1.4%，摩根士丹利\"纯动量\"指数五年来首次单日跌超4%。导火索为美国财政部扩大购债及Moderna股价暴涨。业内人士以\"7级地震必有余震\"比喻当前困境，各方同步去杠杆，降低风险敞口，加剧市场波动，形成负反馈循环。"
  },
  {
    "id": "wscn:3779957",
    "domain": "股票",
    "title": "欧洲粮仓断了？俄乌战争冲击黑海港口，全球粮食生产正遭遇多重冲击",
    "url": "https://wallstreetcn.com/articles/3779957",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:27:04+00:00",
    "summary": "俄乌战争骤然升级，黑海航运陷入瘫痪——仅7月一个月，港口及船只遭袭超120起，乌克兰8月谷物出货量仅及潜在出口能力的20%。芝加哥小麦期货飙至两年高位，埃及、印尼等高度依赖黑海粮源的国家风险敞口急剧扩大。叠加霍尔木兹海峡的持续扰动、厄尔尼诺风险上升以及美国农业带不利天气，摩根大通警告下一场全球粮食危机最早明年到来。"
  },
  {
    "id": "wscn:3779956",
    "domain": "股票",
    "title": "中俄北极航道集装箱运输正式开启！中国集装箱船首次成功抵达俄摩尔曼斯克港",
    "url": "https://wallstreetcn.com/articles/3779956",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:23:50+00:00",
    "summary": "中国航运公司新新运航运旗下\"新新海\"1轮从天津港启航，经北极航道顺利抵达，载运约500个集装箱，标志着中俄北极航道集装箱定期运输正式开启。北极航道目前已具备作为安全高效运输通道的条件，拥有重要战略意义与现实价值。"
  },
  {
    "id": "wscn:3779954",
    "domain": "股票",
    "title": "知名能源分析师Jeff Currie：醒醒吧，各位，大宗商品正在发出信号",
    "url": "https://wallstreetcn.com/articles/3779954",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:07:27+00:00",
    "summary": "柴油裂解价差史上首破百美元，黄金单日狂涨4%至4510美元，铜价突破14000美元……前高盛大宗商品研究主管Jeff Currie发出警报：财政干预已\"剪断刹车线\"，供应瓶颈、货币贬值、政策压制三力共振，大宗商品结构性牛市正进入最剧烈阶段。他的结论只有一句话——\"做多，并系好安全带。\""
  },
  {
    "id": "wscn:3779933",
    "domain": "股票",
    "title": "回购美债影响力只有24小时？贝森特：我们有很多工具，拭目以待",
    "url": "https://wallstreetcn.com/articles/3779933",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T00:07:03+00:00",
    "summary": "贝森特称，财政部拥有强大的工具箱，并暗示单次长债回购规模可能超过已宣布的40亿美元。他强调长债收益率未反映基本面，30年期美债流动性尤其不足，并预告将于本周晚些时候或下周初公布一项新的财政整顿计划。与此同时，贝森特称，下周一还举行新闻发布会阐述对伊朗行动计划，美国将对伊实施“史上最严厉”的制裁，若施加最大经济压力，不太可能需要重启大规模军事行动。"
  },
  {
    "id": "wscn:3779955",
    "domain": "股票",
    "title": "报道：三星计划向股东返还至多790亿美元",
    "url": "https://wallstreetcn.com/articles/3779955",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T23:57:11+00:00",
    "summary": "周五韩国股市收盘后，三星电子董事会拟公布重大股东回报计划，规模预计达90万亿至110万亿韩元（约650亿至790亿美元），或创公司史上最大资本回报纪录。投资者关注分红与回购的资金分配比例及执行时间表。"
  },
  {
    "id": "wscn:3779889",
    "domain": "股票",
    "title": "贝森特出手压长债：扭转操作已至，美版YCC是否到来？",
    "url": "https://wallstreetcn.com/premium/articles/3779889?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T23:56:22+00:00",
    "summary": "贝森特紧急回购长债，实为财政版扭转操作，提供隐性看跌期权，规模影响有限，难改美债长端上行趋势。"
  },
  {
    "id": "hn:49338121",
    "domain": "股票",
    "title": "US tech stock correction likely, warn ECB economists",
    "url": "https://www.ft.com/content/cb4b22ab-4183-4d19-be60-6d2fab86d86d",
    "source": "aanet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-17T21:46:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49311379",
    "domain": "股票",
    "title": "OpenAI talent exodus raises 'huge red flag' ahead of IPO",
    "url": "https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-15T15:25:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49261857",
    "domain": "股票",
    "title": "The SpaceX Sham",
    "url": "https://dissentmagazine.org/online_articles/spacex-ipo-elon-musk-trillionaire/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-08-11T17:47:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49305685",
    "domain": "股票",
    "title": "Backtesting Congress members stock trades by the disclosure date",
    "url": "https://investingpaths.com/tools/congress",
    "source": "ProdRatSuperior",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-14T23:08:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:49322233",
    "domain": "股票",
    "title": "AI is not just one bubble, strategist says – but a 'rolling sequence of bubbles'",
    "url": "https://fortune.com/2026/08/16/ai-bubble-sequence-saas-software-stocks-silver-prices-chipmakers/",
    "source": "pessimizer",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-16T18:05:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49024958",
    "domain": "股票",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49253785",
    "domain": "股票",
    "title": "OpenAI wraps $7B share sale ahead of potential IPO",
    "url": "https://www.cnbc.com/2026/08/10/openai-wraps-7-billion-share-sale-ahead-of-potential-ipo-.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-11T05:40:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49195657",
    "domain": "股票",
    "title": "The Investors Whose SpaceX Shares Vanished Before They Could Cash In",
    "url": "https://www.wsj.com/finance/stocks/spacex-ipo-spv-investors-2698a174",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-06T12:19:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/financing-the-ai-boom-3",
    "domain": "股票",
    "title": "Financing the AI Boom 3",
    "url": "https://www.netinterest.co/p/financing-the-ai-boom-3",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:46:59+00:00",
    "summary": "Nvidia, Guarantor of Last Resort"
  },
  {
    "id": "hn:49257407",
    "domain": "股票",
    "title": "I backtested my own stock rankings. They lost to the index",
    "url": "https://holderdashboard.com/learn/backtest-that-lost-to-the-index",
    "source": "caiocmpaes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-08-11T12:44:43+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/leopolds-fall",
    "domain": "股票",
    "title": "Leopold’s Fall",
    "url": "https://www.netinterest.co/p/leopolds-fall",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:05:15+00:00",
    "summary": "Situational Awareness and Amaranth 20 Years Apart"
  },
  {
    "id": "rss:https://www.netinterest.co/p/paypal-declined",
    "domain": "股票",
    "title": "PayPal, Declined",
    "url": "https://www.netinterest.co/p/paypal-declined",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:33:10+00:00",
    "summary": "Inside the Bid for an Iconic Fintech"
  },
  {
    "id": "rss:https://www.netinterest.co/p/too-big-to-succeed",
    "domain": "股票",
    "title": "Too Big to Succeed",
    "url": "https://www.netinterest.co/p/too-big-to-succeed",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:22:26+00:00",
    "summary": "What it takes to run JPMorgan, and to hand it over"
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
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 390,
    "published_at": "2026-08-19T00:53:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 338,
    "published_at": "2026-08-04T21:09:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49325159",
    "domain": "金融",
    "title": "The federal keyword lists that canceled billions in research funding",
    "url": "https://www.highereddive.com/news/inside-the-federal-keyword-lists-that-canceled-billions-in-research-funding/826203/",
    "source": "walrus01",
    "platform": "hackernews",
    "points": 284,
    "published_at": "2026-08-17T00:14:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49200390",
    "domain": "金融",
    "title": "Federal Communications Commission scraps limit on broadcast TV ownership",
    "url": "https://www.nbcnews.com/business/media/federal-communications-commission-scraps-limit-broadcast-tv-ownership-rcna587641",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-08-06T18:22:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082695",
    "domain": "金融",
    "title": "Mondragon Corporation – a federation of co-operatives",
    "url": "https://en.wikipedia.org/wiki/Mondragon_Corporation",
    "source": "brnt",
    "platform": "hackernews",
    "points": 174,
    "published_at": "2026-07-28T12:19:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 158,
    "published_at": "2026-07-25T11:04:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122994",
    "domain": "金融",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-31T13:37:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49335163",
    "domain": "金融",
    "title": "Meta faces 'astronomical' consequences as legal fight reaches critical moment",
    "url": "https://www.cnbc.com/2026/08/17/meta-attorneys-general-california-federal-trial-astronomical-consequences.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 86,
    "published_at": "2026-08-17T18:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245487",
    "domain": "金融",
    "title": "Study links GLP-1 drugs to bigger jump in women's employment than a degree",
    "url": "https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html",
    "source": "metadat",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-08-10T16:02:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49118696",
    "domain": "金融",
    "title": "The bond market isn’t buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 139,
    "published_at": "2026-07-31T03:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259043",
    "domain": "金融",
    "title": "Federal vendor with $50M in contracts leaves portal broken for a month",
    "url": "https://www.propublica.org/article/foia-requests-responses",
    "source": "ams1",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-08-11T14:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245071",
    "domain": "金融",
    "title": "Force-Fed by ICE",
    "url": "https://www.theguardian.com/us-news/2026/aug/10/ice-force-feeding-detention-gabar-choli",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-08-10T15:35:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18120",
    "domain": "金融",
    "title": "Tradable It\\^o Signatures: A Model-Free, Interpretable Framework for Dynamic Hedging",
    "url": "https://arxiv.org/abs/2608.18120",
    "source": "Xin Guo, Binnan Wang, Ruixun Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18120v1 Announce Type: new Abstract: We propose an interpretable machine-learning framework for dynamic hedging using the It\\^o signature transform, which turns asset-price paths into a set"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18195",
    "domain": "金融",
    "title": "Multi-Level Market Making with Reinforcement Learning",
    "url": "https://arxiv.org/abs/2608.18195",
    "source": "Patrick Cheridito, Moritz Weiss",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18195v1 Announce Type: new Abstract: We introduce a reinforcement learning framework for market making in a limit order book. Our algorithm aims to maximize trading revenue by dynamically s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18299",
    "domain": "金融",
    "title": "The Market's Conditioning Representation: Equilibrium, Crowding, and Convention Multiplicity",
    "url": "https://arxiv.org/abs/2608.18299",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18299v1 Announce Type: new Abstract: Asset-pricing models typically condition on a fixed information set. This paper endogenises the market's conditioning architecture by allowing portfolio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18657",
    "domain": "金融",
    "title": "Accounting for intra-household joint travel in agent-based transport simulations",
    "url": "https://arxiv.org/abs/2608.18657",
    "source": "Javaudin Lucas, Araldo Andrea, Coulombel Nicolas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18657v1 Announce Type: new Abstract: Intra-household joint home-based tours - trips in which household members depart together, engage in shared activities, and return together - represent "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18783",
    "domain": "金融",
    "title": "When to Sell an Asset? - A Distribution Builder Approach",
    "url": "https://arxiv.org/abs/2608.18783",
    "source": "Peter Carr, Stephan Sturm",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18783v1 Announce Type: new Abstract: We consider the question of the optimal timing of the sale of an asset with stochastic dynamics. Our analysis is based on the method of the distribution"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18113",
    "domain": "金融",
    "title": "Optimal Loss Allocation in a Mean-Field Model of Systemic Risk",
    "url": "https://arxiv.org/abs/2608.18113",
    "source": "Yucheng Guo, Qinxin Yan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18113v1 Announce Type: cross Abstract: We study a systemic-risk control problem in which a central planner allocates losses generated by bank defaults across the surviving institutions. Ban"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18119",
    "domain": "金融",
    "title": "Shifting Social Dispositions, Stable Prosocial Traits: A Global Age-Period-Cohort Analysis of Human Personality",
    "url": "https://arxiv.org/abs/2608.18119",
    "source": "Paul X. McCarthy, Xian Gong, John A. Johnson, Marian-Andrei Rizoiu, Margaret L. Kern, Jean M. Twenge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18119v1 Announce Type: cross Abstract: Generational stereotypes are widespread, but they often rely on anecdotes, and it remains challenging to disentangle true birth-cohort differences fro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18554",
    "domain": "金融",
    "title": "CentaurBench: Benchmarking LLM Capabilities on Augmenting vs. Automating Real-World Work Tasks",
    "url": "https://arxiv.org/abs/2608.18554",
    "source": "Pattaraphon Kenny Wongchamcharoen, Kris Gulati, Min Min Fong, Abhishek Nagaraj",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18554v1 Announce Type: cross Abstract: Most LLM benchmarks rank models on their ability to automate work tasks. In practice, however, models are often used to assist other (human or LLM) ag"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18690",
    "domain": "金融",
    "title": "Europe's Climate Ambition Under Scrutiny: Evidence from Deep Learning Emission Projections",
    "url": "https://arxiv.org/abs/2608.18690",
    "source": "Jacopo Ghirri, Carlos Rodriguez-Pardo, Lara Aleluia Reis, Massimo Tavoni",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2608.18690v1 Announce Type: cross Abstract: The European Union has committed to reducing greenhouse gas emissions 55% below 1990 levels by 2030, but whether current trends are compatible with th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2309.14186",
    "domain": "金融",
    "title": "Value-transforming financial, carbon and biodiversity footprint accounting",
    "url": "https://arxiv.org/abs/2309.14186",
    "source": "S. El Geneidy (School of Resource Wisdom, University of Jyv\\\"askyl\\\"a, Finland, School of Business and Economics, University of Jyv\\\"askyl\\\"a, Finland), M. Peura (School of Resource Wisdom, University of Jyv\\\"askyl\\\"a, Finland, Department of Biological and Environmental Science, University of Jyv\\\"askyl\\\"a, Finland), V. M. Aumanen (Division of Policy and Planning, University of Jyv\\\"askyl\\\"a, Finland), S. Baumeister (School of Resource Wisdom, University of Jyv\\\"askyl\\\"a, Finland, School of Business and Economics, University of Jyv\\\"askyl\\\"a, Finland), U. Helimo (School of Resource Wisdom, University of Jyv\\\"askyl\\\"a, Finland, Department of Biological and Environmental Science, University of Jyv\\\"askyl\\\"a, Finland, Division of Policy and Planning, University of Jyv\\\"askyl\\\"a, Finland), V. Vainio (School of Resource Wisdom, University of Jyv\\\"askyl\\\"a, Finland, Department of Biological and Environmental Science, University of Jyv\\\"askyl\\\"a, Finland), J. S. Kotiaho (School of Resource Wisdom, University of Jyv\\\"askyl\\\"a, Finland, Department of Biological and Environmental Science, University of Jyv\\\"askyl\\\"a, Finland)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2309.14186v4 Announce Type: replace Abstract: Transformative changes in our production and consumption habits are needed to halt biodiversity loss. Organizations are the way we humans have organ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2405.02115",
    "domain": "金融",
    "title": "On variable annuities with surrender charges",
    "url": "https://arxiv.org/abs/2405.02115",
    "source": "Tiziano De Angelis, Alessandro Milazzo, Gabriele Stabile",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2405.02115v2 Announce Type: replace Abstract: In this paper we provide a theoretical analysis of Variable Annuities (VAs) with a focus on the holder's right to an early termination of the contra"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.19715",
    "domain": "金融",
    "title": "Neural Functionally Generated Portfolios",
    "url": "https://arxiv.org/abs/2506.19715",
    "source": "Michael Monoyios, Olivia Pricilia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2506.19715v2 Announce Type: replace Abstract: We introduce a novel neural-network-based approach to learning the generating function $G(\\cdot)$ of a functionally generated portfolio (FGP) from s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.15911",
    "domain": "金融",
    "title": "Sleeping Kelly",
    "url": "https://arxiv.org/abs/2510.15911",
    "source": "Ben Abramowitz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2510.15911v4 Announce Type: replace Abstract: The Sleeping Beauty problem is a problem of imperfect recall that has received considerable attention. One approach to resolving the Sleeping Beauty"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.10853",
    "domain": "金融",
    "title": "Multidimensional Sorting: Comparative Statics",
    "url": "https://arxiv.org/abs/2512.10853",
    "source": "Job Boerma, Andrea Ottolini, Aleh Tsyvinski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2512.10853v2 Announce Type: replace Abstract: Characterizing multidimensional sorting problems is notoriously difficult - solutions are known only for a small number of examples. Our main result"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.14670",
    "domain": "金融",
    "title": "FactorMiner: A Self-Evolving Agent with Skills and Experience Memory for Financial Alpha Discovery",
    "url": "https://arxiv.org/abs/2602.14670",
    "source": "Yanlong Wang, Jian Xu, Hongkang Zhang, Shao-Lun Huang, Danny Dongning Sun, Xiao-Ping Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2602.14670v2 Announce Type: replace Abstract: Formulaic alpha factor mining is a critical yet challenging task in quantitative investment, characterized by a vast search space and the need for d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.03213",
    "domain": "金融",
    "title": "Dynamic Tracking Error and the Total Portfolio Approach",
    "url": "https://arxiv.org/abs/2603.03213",
    "source": "Ashwin Alankar, Allan Maymin, Philip Maymin, Myron Scholes, Sujiang Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2603.03213v2 Announce Type: replace Abstract: Strategic Asset Allocation and the Total Portfolio Approach differ in one thing: the tracking error the board grants the chief investment officer. T"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.08825",
    "domain": "金融",
    "title": "Is Bitcoin A Hedge Against Central Banking? Evidence from AI-Driven Monetary Policy Expectations",
    "url": "https://arxiv.org/abs/2604.08825",
    "source": "Maxime L. D. Nicolas, Fran\\c{c}ois Sicard, Marion Laboure, Zixin Sun, Anah\\'i Rodr\\'iguez-Mart\\'inez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T04:00:00+00:00",
    "summary": "arXiv:2604.08825v2 Announce Type: replace Abstract: This study investigates the transmission of monetary policy narratives to Bitcoin prices, distinguishing policy expectations from realized policy im"
  },
  {
    "id": "hn:49352830",
    "domain": "金融",
    "title": "The most influential economist is oddly unconvincing",
    "url": "https://www.economist.com/finance-and-economics/2026/08/17/the-worlds-most-influential-economist-is-oddly-unconvincing",
    "source": "aragonite",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T21:15:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49350858",
    "domain": "金融",
    "title": "AI Is Upending One of Finance's Cushiest Jobs",
    "url": "https://www.bloomberg.com/news/features/2026-06-05/ai-is-upending-traditional-financial-advisor-jobs",
    "source": "theriddlr",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-18T18:59:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-10T13:40:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49197127",
    "domain": "金融",
    "title": "Former Federal Prosecutors to Senate: Stop Confirming Election Deniers as Judges",
    "url": "https://abovethelaw.com/2026/08/former-federal-prosecutors-to-senate-stop-confirming-election-deniers-to-the-federal-bench/",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-06T14:25:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49304409",
    "domain": "金融",
    "title": "Make a 6-Tesla-class high-temperature superconducting dipole magnet at 4.2 K",
    "url": "https://journals.aps.org/prab/abstract/10.1103/4nhs-bkwh",
    "source": "supermagnet",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-14T20:49:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-07-29T14:13:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49215292",
    "domain": "金融",
    "title": "Mykhailo Fedorov reveals struggle to secure Patriot missiles and Western support",
    "url": "https://www.uawire.org/former-ukrainian-defense-minister-mykhailo-fedorov-reveals-struggles-to-secure-patriot-missiles-and-western-support",
    "source": "greedo",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-08-07T19:38:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111879",
    "domain": "金融",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289340",
    "domain": "金融",
    "title": "Hooray for index funds–just don't call them passive",
    "url": "https://www.economist.com/finance-and-economics/2026/08/11/hooray-for-index-funds-just-dont-call-them-passive",
    "source": "thm",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-13T17:37:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-07-28T12:19:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49173576",
    "domain": "金融",
    "title": "Investors in Situational Awareness deserved to lose their shirts",
    "url": "https://www.economist.com/finance-and-economics/2026/08/04/investors-in-situational-awareness-deserved-to-lose-their-shirts",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T19:18:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184251",
    "domain": "金融",
    "title": "Fed's Kashkari says 'now is the time to start slowly moving' rates up",
    "url": "https://www.cnbc.com/2026/08/05/feds-kashkari-says-now-is-the-time-to-start-slowly-moving-rates-up.html",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-08-05T15:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49214813",
    "domain": "金融",
    "title": "US Sold Euros to Save the Yen, Europe Found Out After",
    "url": "https://finance.yahoo.com/markets/currencies/articles/us-sold-euros-save-yen-033819315.html",
    "source": "amarcheschi",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-07T18:54:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49157782",
    "domain": "金融",
    "title": "US Schools Are Ditching Chromebooks for MacBooks by the Thousands",
    "url": "https://finance.yahoo.com/technology/articles/us-schools-ditching-chromebooks-macbooks-233015401.html",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-03T16:16:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49208461",
    "domain": "金融",
    "title": "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions",
    "url": "https://www.wsj.com/finance/investing/new-intelligence-warns-russia-may-provoke-nato-amid-dwindling-u-s-munitions-68f497c7",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-07T10:52:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49182971",
    "domain": "金融",
    "title": "OpenAI settles claims of discrimination against US workers for $3.2M",
    "url": "https://finance.yahoo.com/technology/ai/articles/openai-settles-claims-discrimination-against-221429616.html",
    "source": "declan_roberts",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-08-05T13:57:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49033778",
    "domain": "金融",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49047488",
    "domain": "金融",
    "title": "Stripe in talks to acquire OpenRouter in potential $10B deal, WSJ reports",
    "url": "https://finance.yahoo.com/technology/ai/articles/stripe-talks-acquire-openrouter-potential-215104525.html",
    "source": "nlpnerd",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-25T13:38:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49093686",
    "domain": "金融",
    "title": "Google reported its first negative quarter since going public",
    "url": "https://finance.yahoo.com/technology/ai/articles/google-spent-490-million-day-163000234.html",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-29T05:22:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49176000",
    "domain": "金融",
    "title": "What are credit default swaps and why are they spooking AI investors?",
    "url": "https://www.reuters.com/business/finance/global-markets-cds-explainer-2026-07-29/",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-08-04T22:18:09+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  }
]
```
