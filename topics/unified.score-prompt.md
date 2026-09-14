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

- 今日日期：`2026-09-14`
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
  "date": "2026-09-14",
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
    "id": "bvid:BV1uV411N7Cg",
    "domain": "AI",
    "title": "够21万人喝一生的水，还不够谷歌服务器用7个月的？【差评君】",
    "url": "http://www.bilibili.com/video/av405998001",
    "source": "差评君",
    "platform": "bilibili",
    "points": 3348960,
    "published_at": "2023-09-14T03:30:00+00:00",
    "summary": "去年一年，谷歌花掉了大概一个半西湖的水量，差评君翻了翻报告，发现罪魁祸首的矛头，指向了数据中心。那这些数据中心为什么这么耗水？今天就来跟大家聊聊那些互联网巨头们都是给服务器散热的。"
  },
  {
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 2734442,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1287337,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 885469,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1LBr8Y9EBV",
    "domain": "AI",
    "title": "新服开荒！我超越了99%的宝可梦服务器！我的世界神奇宝贝服务器！",
    "url": "http://www.bilibili.com/video/av113791769517248",
    "source": "晓凯少爷",
    "platform": "bilibili",
    "points": 869534,
    "published_at": "2025-01-08T11:00:00+00:00",
    "summary": "开服八年来，好像就是在等待这一天，\n此服务器是我用了八年的开服经验，耗时3个月，花费38040元所搭建的服务器。\n目前是新服开荒的状态。\n采用了第九世代朱紫 最新版本世代 开放免费飞行 无任何限制玩法。\n\n正如我们当初所说的，我们的理想很大，梦想着成为最好的宝可梦服务器。\n愿此服务器可以让大家玩的开心，不会辜负你们的期待。\n游玩途中若有建议，欢迎私信提出。\n\n玩家企鹅聚集地：807332070\n\n"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 764273,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1SQo5BAEBo",
    "domain": "AI",
    "title": "trae使用教程【B站最详细，零基础必看！】trae小白入门到精通traeCN教程traeexceltrae项目实战trae安装教程用教程trae开发小程序",
    "url": "http://www.bilibili.com/video/av116458407336746",
    "source": "trae教程",
    "platform": "bilibili",
    "points": 724562,
    "published_at": "2026-04-24T07:10:58+00:00",
    "summary": "trae使用教程trae小白入门到精通traeCN教程traeexceltrae项目实战trae安装教程用trae开发小程序traecn使用教程"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 660608,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1kVVC68E33",
    "domain": "AI",
    "title": "新老玩家战争正式打响，三方势力谁能夺得服务器统治权！",
    "url": "http://www.bilibili.com/video/av116681577925246",
    "source": "七支羽mc",
    "platform": "bilibili",
    "points": 602108,
    "published_at": "2026-06-02T22:00:00+00:00",
    "summary": "原视频：https://www.youtube.com/watch?v=_hyFGrcVv5U&amp;t=1556s\n作者：Wemmbu"
  },
  {
    "id": "bvid:BV1bqaPzxEhx",
    "domain": "AI",
    "title": "我的世界：玩家居然成为彩虹之神！神之间的战斗服务器都顶不住！",
    "url": "http://www.bilibili.com/video/av115134550776038",
    "source": "一瓶黑酱",
    "platform": "bilibili",
    "points": 560545,
    "published_at": "2025-09-02T11:57:57+00:00",
    "summary": "希望各位观众老爷喜欢的，你的支持是我日更的动力！！！"
  },
  {
    "id": "bvid:BV1DRHNziEwu",
    "domain": "AI",
    "title": "我的世界：如何成为服务器的无限之神！三名玩家进行无限死亡竞赛",
    "url": "http://www.bilibili.com/video/av115303933546578",
    "source": "一瓶黑酱",
    "platform": "bilibili",
    "points": 550923,
    "published_at": "2025-10-02T09:50:10+00:00",
    "summary": "希望各位观众老爷喜欢的，你的支持是我日更的动力！！！"
  },
  {
    "id": "bvid:BV1DUdJB2E9i",
    "domain": "AI",
    "title": "SMP服务器惊现坚守者之刃，竟能颠覆游戏平衡？",
    "url": "http://www.bilibili.com/video/av116424701975932",
    "source": "胡椒解说",
    "platform": "bilibili",
    "points": 548044,
    "published_at": "2026-04-18T08:16:02+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1yoVLziELS",
    "domain": "AI",
    "title": "新服开荒，我的世界宝可梦服务器！立志不跑路！",
    "url": "http://www.bilibili.com/video/av114440108252657",
    "source": "清川川呀",
    "platform": "bilibili",
    "points": 518108,
    "published_at": "2025-05-03T02:23:00+00:00",
    "summary": "玩家企鹅聚集地：1053437818 制作一年，只为等待这一刻！愿我的心血没有让大家失望。"
  },
  {
    "id": "bvid:BV1UpR9BBEf5",
    "domain": "AI",
    "title": "为了不让AI瞎写代码，大神程序员把自己蒸馏了！GitHub星标6万+",
    "url": "http://www.bilibili.com/video/av116544206016295",
    "source": "量子位Daily",
    "platform": "bilibili",
    "points": 473667,
    "published_at": "2026-05-11T01:05:00+00:00",
    "summary": "软件工程师必备，GitHub星标6万+！大神程序员蒸馏自己，用16个skill给AI注入软件工程之魂，提高交付质量。网友：“这是我用过的token回报率最高的提示词”……"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 442525,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1BFouBYERu",
    "domain": "AI",
    "title": "手把手教你在Claude Code中熟练使用SKILL技能！",
    "url": "http://www.bilibili.com/video/av116453927814340",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 430054,
    "published_at": "2026-04-23T12:09:57+00:00",
    "summary": "本期视频耗时半个月制作，希望大家能够点赞三连加关注，感谢！\n\n内容包括了一下几个方面：\n00:27 Skill简介\n01:39 Skill和Plugin的区别\n02:51 安装他人的Skill\n04:44 手动创建自己的SKill\n07:30 控制Skill的触发行为\n08:01 Skill的查看和管理\n08:20 Skill的停用和删除\n08:55 找优质Skill的三种渠道"
  },
  {
    "id": "bvid:BV1y62tYGEt8",
    "domain": "AI",
    "title": "对新手最友好的服务器！Mac mini 家用服务器手把手配置教程！",
    "url": "http://www.bilibili.com/video/av113293486201196",
    "source": "旅客君LookUplus",
    "platform": "bilibili",
    "points": 369822,
    "published_at": "2024-10-19T00:00:00+00:00",
    "summary": "Hello 大家好，这里是旅客君。我将用一期视频的时间，带大家手把手配置这台 Mac mini，让它成为各位家中服务器的一员。这期视频于 2024 年 10 月初发布，是基于 macOS Sequoia，也就是 macOS 15 的正式版。后续随着系统的更新，部分操作界面可能会有所差异，届时可能会和本期视频所提供的步骤有所不同，大家也需要学会融会贯通，找到对应的设置选项。如果你是第一次配置，或者不"
  },
  {
    "id": "bvid:BV1Zgud6LEoh",
    "domain": "AI",
    "title": "【最新版】小白速通 Codex 教程（含 DeepSeek 接入，无需 ChatGPT 订阅）",
    "url": "http://www.bilibili.com/video/av117070826047031",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 296371,
    "published_at": "2026-08-10T10:54:20+00:00",
    "summary": "Codex 安装 + 上手速通，保姆级教程！\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV1Ag6UBGE3V",
    "domain": "AI",
    "title": "[中配]我潜入了Minecraft的儿童专属服务器 - Lynix",
    "url": "http://www.bilibili.com/video/av115871624267212",
    "source": "YTB热视君",
    "platform": "bilibili",
    "points": 288736,
    "published_at": "2026-01-10T16:13:02+00:00",
    "summary": "原标题：I Snuck Into a KIDS ONLY Server in Minecraft\n作者：Lynix\n原链接：https://www.youtube.com/watch?v=qH74qmh71Zo\n上传日期：2026-01-10\n\n简介：Lynix九岁的表弟因为建造自动农场而被他与同学们一起玩的Minecraft服务器封禁。孩子们利用他的建造技术，然后嘲笑他。 Lynix为了替表弟报"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 288491,
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
    "points": 280746,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1BXuvzTEVZ",
    "domain": "AI",
    "title": "【AI垃圾王】2500元不到装一台AI服务器！双Radeon VII解锁vLLM张量并行，性能暴涨6倍碾压Ollama！",
    "url": "http://www.bilibili.com/video/av114850546196477",
    "source": "司波图",
    "platform": "bilibili",
    "points": 277641,
    "published_at": "2025-07-14T08:14:09+00:00",
    "summary": "💥2400元预算挑战AI算力天花板！本期视频，我们解决了Radeon VII / MI50 等 gfx906 架构显卡长期以来无法使用 vLLM 张量并行的痛点！\n\n我们将全程展示如何用两张“过气”Radeon VII显卡，搭配X99“洋垃圾”平台，组装一台总价仅2397元的AI算力服务器。通过社区大神 nlzy 提供的特制Docker容器，我们成功解锁了vLLM的张量并行功能，在Qwen3 32"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 260686,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 181269,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 173120,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1fTjY6eEZi",
    "domain": "AI",
    "title": "Codex+Skills王炸！保姆级教程！纯实战干货！小白也能轻松上手！",
    "url": "http://www.bilibili.com/video/av116773449898804",
    "source": "不吃辣的Chris",
    "platform": "bilibili",
    "points": 161769,
    "published_at": "2026-06-18T22:25:04+00:00",
    "summary": "本期视频以Codex+Skills做知识博主的一期PPT素材为例，教大家的是方法论，学会了这套方法论，你可以用Codex+Skills做任何事情！开启新世界大门！"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 156179,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1nL5L6EEq4",
    "domain": "AI",
    "title": "别再花冤枉钱了！Claude Code 接入 DeepSeek V4 完整教程（1%成本平替方案）",
    "url": "http://www.bilibili.com/video/av116564372233705",
    "source": "Tech指南",
    "platform": "bilibili",
    "points": 143473,
    "published_at": "2026-05-13T00:19:27+00:00",
    "summary": "用 DeepSeek V4 替换 Claude Code 官方模型，成本直降 100 倍！\n本视频手把手教你如何利用开源模型实现 AI 编程自由，附带 CC Switch 桌面工具的完整配置教程。\n\n文中提到的工具/资源：\n👉 CC Switch GitHub: https://github.com/farion1231/cc-switch\n👉 OpenRouter 官网: https://ope"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 115546,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV13mb56BE9z",
    "domain": "AI",
    "title": "你用 AI，是在解决问题还是在攀比工具？AI工具链鄙视下、GPT-6 Astra 发布后，普通人该怎么选用AI工具？【2026教师节】",
    "url": "http://www.bilibili.com/video/av117234504567481",
    "source": "北航90后副教授何静",
    "platform": "bilibili",
    "points": 115454,
    "published_at": "2026-09-08T09:00:00+00:00",
    "summary": "AI 工具越贵就越厉害吗？\n高铁上的真实经历，让我意识到很多人都陷入了工具羞耻心：盲目追逐最新大模型、纠结工具鄙视链，把工具当成身份标签，却忘了使用 AI 的初衷是解决问题。\n黑猫白猫，捉到老鼠就是好猫。 豆包、Claude Code、Codex 没有绝对高下，只有场景匹配。不必为了面子去追捧昂贵复杂的工具，先找准你要解决的问题，选择刚好够用的工具，拿到结果才最重要。\n工具会迭代过时，但解决问题的"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 103868,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1PTTs6cEwi",
    "domain": "AI",
    "title": "不写一行代码！0基础用AI开发修仙游戏【全流程教程】",
    "url": "http://www.bilibili.com/video/av116855104668708",
    "source": "黑鲸同学",
    "platform": "bilibili",
    "points": 101169,
    "published_at": "2026-07-03T11:00:00+00:00",
    "summary": "本期视频长达90分钟，全程无废话，建议先收藏后观看。涵盖Vibe Coding理念、Cursor使用、AI绘图与视频生成、游戏系统开发全流程。"
  },
  {
    "id": "bvid:BV1MJXZBgE32",
    "domain": "AI",
    "title": "AI Coding 进阶：从 Vibe/Plan/Spec 到 Harness Engineering 与 Agent Teams",
    "url": "http://www.bilibili.com/video/av116334289491216",
    "source": "Qoder",
    "platform": "bilibili",
    "points": 72342,
    "published_at": "2026-04-02T09:00:33+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 71548,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 70742,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1RjMi62E6u",
    "domain": "AI",
    "title": "新服开荒！让MC宝可梦服再次伟大！我的世界神奇宝贝服务器！",
    "url": "http://www.bilibili.com/video/av116882921361760",
    "source": "梦境有点呆",
    "platform": "bilibili",
    "points": 68060,
    "published_at": "2026-07-08T06:25:52+00:00",
    "summary": "玩家企鹅聚集地：318326443\n\n支持手机电脑游玩！第九世代最新版本！\n新服开荒 今日7-8日刚刚开服 现在入坑最佳时机！\n正如我们当初所说的，我们的理想很大，梦想着成为最好的宝可梦服务器。\n愿此服务器可以让大家玩的开心，不会辜负你们的期待。\n游玩途中若有建议，欢迎私信提出。"
  },
  {
    "id": "bvid:BV1FqL16zEYr",
    "domain": "AI",
    "title": "现在你可以把自己注册成LLM API给人调用了！（接上回）",
    "url": "http://www.bilibili.com/video/av116605744843907",
    "source": "恵飛須沢_Ayaya",
    "platform": "bilibili",
    "points": 64277,
    "published_at": "2026-05-20T07:36:53+00:00",
    "summary": "上期视频发布之后虽然很快就被复刻了十倍播放量的版本QAQ\n\n但是还是有不少群友来找up主咨询自己部署的问题喵\n\n大家都想把自己封装成LLM API呢！\n\n所以最近对网站进行了一些升级，现在你可以直接在我的网站里注册成为LLM，然后直接把api-key分享出去给人调用！\n\n可惜我的1c1g服务器还是会有些慢呢UwU\n\n有没有愿意给我部署服务的粉丝呢ww"
  },
  {
    "id": "bvid:BV1AodfByE7D",
    "domain": "AI",
    "title": "写了十八年代码的老码农使用 Codex Vibe Coding 后总结了哪些重要经验？",
    "url": "http://www.bilibili.com/video/av116431882558436",
    "source": "牧云踏歌",
    "platform": "bilibili",
    "points": 56452,
    "published_at": "2026-04-19T14:43:21+00:00",
    "summary": "一份面向团队与个人开发者的 Codex 协作手册，重点沉淀高频场景下的方法、模板和可复用骨架。"
  },
  {
    "id": "bvid:BV1XxbL6rEhu",
    "domain": "AI",
    "title": "我要成为不稳定服务器的海盗之王！",
    "url": "http://www.bilibili.com/video/av117218784316522",
    "source": "七支羽mc",
    "platform": "bilibili",
    "points": 38924,
    "published_at": "2026-09-05T14:16:36+00:00",
    "summary": "原视频：https://www.youtube.com/watch?v=FhkW8zxHIBU\n作者：\nJaden-MAN"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29740,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 26699,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV19eQ3BJEkg",
    "domain": "AI",
    "title": "手撕大厂题-vibe coding降龙七步",
    "url": "http://www.bilibili.com/video/av116403881385303",
    "source": "青阳-AI",
    "platform": "bilibili",
    "points": 21637,
    "published_at": "2026-04-14T16:00:12+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1C7qaBDEM1",
    "domain": "AI",
    "title": "零基础AI编程 无代码实战 商城小程序、后台管理、微信支付、秒杀功能、优惠券、数据分析大屏❗️ vibe coding时代",
    "url": "http://www.bilibili.com/video/av115728078345127",
    "source": "华神说编程",
    "platform": "bilibili",
    "points": 21573,
    "published_at": "2025-12-16T07:36:01+00:00",
    "summary": "该项目已录制完毕，如果满足自己的需求，三连点赞！！获取完整课程 源码配套资料，提示词文档，呕心沥血提示词规则资料等、问题解答，华神 扣：3753599439  扣：1306749621"
  },
  {
    "id": "bvid:BV14cZqB8EBY",
    "domain": "AI",
    "title": "AI攻克不了的领域竟然是它？揭秘CNC编程为何让AI束手无策",
    "url": "http://www.bilibili.com/video/av116097411976217",
    "source": "极微视界",
    "platform": "bilibili",
    "points": 16475,
    "published_at": "2026-02-19T12:59:23+00:00",
    "summary": "CNC编程AI化有多难？本视频深度解析为什么AI编程在制造业进展缓慢。\n从材料、刀具、机床到隐性知识，揭秘老师傅的经验为什么无法数字化。\nPowerMill、CloudNC等AI编程软件的真实水平如何？CNC编程师的未来在哪里？\n\n⏱️ 时间轴 Timestamps:\n\n00:00 开篇：AI在CNC领域的困境\n00:20 材料的复杂性：为什么同样是45#钢参数却不同\n01:01 刀具与机床的个体"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 15628,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 14898,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV13mV46AEwq",
    "domain": "AI",
    "title": "干货！Vibe Coding 经验小结—从需求分析到agent hook",
    "url": "http://www.bilibili.com/video/av116655204141991",
    "source": "白玩dev",
    "platform": "bilibili",
    "points": 13861,
    "published_at": "2026-05-29T11:00:00+00:00",
    "summary": "本期聊聊vibe coding，同时分享一个好用的AI绘图工具支持绘制流程图、架构图、技术路线图、海报等280多种图形。电脑端工具安装包：https://sourl.cn/KuvRNV"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 12711,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1oYRFBwEwE",
    "domain": "AI",
    "title": "4分钟搭建属于自己的AI中转站!选购服务器/找上游！",
    "url": "http://www.bilibili.com/video/av116509779167113",
    "source": "挽风的技术教程",
    "platform": "bilibili",
    "points": 11396,
    "published_at": "2026-05-03T08:51:34+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 9919,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 569,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548952",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to acquire Hugging Face",
    "url": "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html",
    "source": "tosh",
    "platform": "hackernews",
    "points": 329,
    "published_at": "2026-09-03T12:10:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 134,
    "published_at": "2026-09-13T10:29:18+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/small-indian-manufacturers-hit-data-legacy-system-barriers-to-scaling-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Small Indian Manufacturers Hit Data, Legacy-System Barriers to Scaling AI",
    "url": "https://www.eetimes.com/small-indian-manufacturers-hit-data-legacy-system-barriers-to-scaling-ai/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T05:53:04+00:00",
    "summary": "AI adoption across manufacturing in India is progressing, but scaling it is running into structural problems across tiers. The post Small Indian Manufacturers Hit Data, Legacy-System Barriers to Scali"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-best-gaming-cpu-drops-below-launch-price-and-includes-free-240mm-aio-cooler-and-onimusha-way-of-the-sword-grab-the-ryzen-7-9850x3d-for-usd484",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s best gaming CPU drops below launch price and includes free 240mm AIO cooler and Onimusha: Way of the Sword — grab the Ryzen 7 9850X3D for $484",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-best-gaming-cpu-drops-below-launch-price-and-includes-free-240mm-aio-cooler-and-onimusha-way-of-the-sword-grab-the-ryzen-7-9850x3d-for-usd484",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T14:28:06+00:00",
    "summary": "The Ryzen 7 9850X3D may only be a modest step up from the 9800X3D, but it still leads our gaming benchmarks and now comes with a couple of useful extras at a lower-than-launch price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/sanders-proposes-20-year-prison-sentence-for-ai-devs-who-plow-ahead-with-artificial-superintelligence-plans-penalty-on-par-with-illegally-developing-rogue-nuclear-weapons",
    "domain": "AI 算力 / 半导体",
    "title": "Bernie Sanders proposes 20 year prison sentence for AI devs who plow ahead with Artificial Superintelligence plans — penalty on par with illegally developing rogue nuclear weapons",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/sanders-proposes-20-year-prison-sentence-for-ai-devs-who-plow-ahead-with-artificial-superintelligence-plans-penalty-on-par-with-illegally-developing-rogue-nuclear-weapons",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T14:10:00+00:00",
    "summary": "Senators Bernie Sanders and Greg Cezar have announced their Ban Artificial Superintelligence Act which threatens 20-year prison sentences for rule breakers."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/webcams/dell-pro-5-webcam-2k-review",
    "domain": "AI 算力 / 半导体",
    "title": "Dell Pro 5 Webcam 2K Review: So you can look good in office",
    "url": "https://www.tomshardware.com/peripherals/webcams/dell-pro-5-webcam-2k-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T14:00:00+00:00",
    "summary": "The Dell Pro 5 webcam is an office-oriented 2K webcam with a physical privacy shutter, a built-in mic, and Windows Hello compatibility."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-ceo-warns-of-ai-driven-botnet-swarm-taking-over-the-entire-internet-in-6-12-months-such-a-swarm-could-be-capable-of-taking-over-the-entire-internet-with-a-persistent-botnet",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic CEO warns of AI-driven botnet 'swarm' taking over the entire internet — 'In 6–12 months such a swarm could be capable of taking over the entire internet with a persistent botnet'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-ceo-warns-of-ai-driven-botnet-swarm-taking-over-the-entire-internet-in-6-12-months-such-a-swarm-could-be-capable-of-taking-over-the-entire-internet-with-a-persistent-botnet",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:36:35+00:00",
    "summary": "As an Ex-Anthropic warns AI will get self-sufficient and kill our posterity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/azza-psaz-750g-atx-3-1-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "AZZA PSAZ-750G ATX 3.1 power supply review: An adequate budget 750W unit",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/azza-psaz-750g-atx-3-1-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:30:00+00:00",
    "summary": "The AZZA PSAZ-750G ATX 3.1 is a non-modular 750W built by Helly, wearing an 80 PLUS Gold badge it has never earned, sold at a price that almost makes the argument for it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/intel-revives-one-mono-font-after-brief-retirement-typeface-built-to-fight-coder-eyestrain-gets-reprieve-from-open-source-purge",
    "domain": "AI 算力 / 半导体",
    "title": "Intel revives One Mono font after brief retirement during open-source purge — typeface built to fight coder eyestrain gets reprieve",
    "url": "https://www.tomshardware.com/tech-industry/intel-revives-one-mono-font-after-brief-retirement-typeface-built-to-fight-coder-eyestrain-gets-reprieve-from-open-source-purge",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:00:00+00:00",
    "summary": "Intel’s decision to archive its developer-focused One Mono font lasted only two days, with the company now restoring the open-source project despite its relatively limited development activity."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/thrustmaster-airbus-add-on-grip-with-ava-joystick-base-review",
    "domain": "AI 算力 / 半导体",
    "title": "Thrustmaster Airbus Add-On Grip with AVA Joystick Base Review: A First-Class Flight Experience",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/thrustmaster-airbus-add-on-grip-with-ava-joystick-base-review",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:00:00+00:00",
    "summary": "The Thrustmaster Airbus Add-On Grip with the AVA Joystick Base is a 1:1 replica of an Airbus sidestick, featuring extensive customization and Hall-effect sensors across all axes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-military-researchers-and-tech-giants-caught-using-claude-us-frontier-model-coded-16-air-defense-suppression-tools-targeting-taiwan-drafted-anti-torpedo-specs-and-fed-151-million-training-queries-to-alibaba",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese military researchers and tech giants caught using Claude — US frontier model coded 16 air-defense suppression tools targeting Taiwan, drafted anti-torpedo specs, and fed 151 million training q",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-military-researchers-and-tech-giants-caught-using-claude-us-frontier-model-coded-16-air-defense-suppression-tools-targeting-taiwan-drafted-anti-torpedo-specs-and-fed-151-million-training-queries-to-alibaba",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T12:00:00+00:00",
    "summary": "Anthropic accuses China-linked actors of using its Claude models of weapon development, intelligence activities, distilling AI models."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/mexican-cartel-crypto-farm-seized-in-mountain-raid-300-gpus-satellite-links-and-industrial-transformers-tapped-hydroelectric-power",
    "domain": "AI 算力 / 半导体",
    "title": "Mexican cartel's crypto farm seized in mountain raid — 300 GPUs, satellite links, and industrial transformers tapped hydroelectric power",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/mexican-cartel-crypto-farm-seized-in-mountain-raid-300-gpus-satellite-links-and-industrial-transformers-tapped-hydroelectric-power",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T11:30:00+00:00",
    "summary": "There is increasing evidence that Mexican drug cartels are diversifying into cryptocurrency mining and are using crypto platforms to launder their ill-gotten gains."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/waymo-robotaxi-calls-cops-on-riders-handling-loaded-ar-style-ghost-gun-waymo-alerted-san-francisco-police-then-juvenile-riders-were-stopped-and-arrested",
    "domain": "AI 算力 / 半导体",
    "title": "Waymo robotaxi calls cops on riders handling loaded AR-style ghost gun — Waymo alerted San Francisco police, then juvenile riders were stopped and arrested",
    "url": "https://www.tomshardware.com/tech-industry/drones/waymo-robotaxi-calls-cops-on-riders-handling-loaded-ar-style-ghost-gun-waymo-alerted-san-francisco-police-then-juvenile-riders-were-stopped-and-arrested",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T11:16:11+00:00",
    "summary": "Following a tip-off from robotaxi firm Waymo, San Francisco police conducted a 'high-risk vehicle stop' and arrested two juveniles for illegal possession of a firearm."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/programming/playable-tomb-raider-runs-on-a-humble-1-watt-chip-usd25-board-with-dual-core-400-mhz-esp32-p4-mcu-scales-openlara-up-to-1-024-x-600-playable-pixels",
    "domain": "AI 算力 / 半导体",
    "title": "Playable Tomb Raider runs on a humble 1-watt chip — $25 board with dual-core 400 MHz ESP32-P4 MCU scales OpenLara up to 1,024 x 600 playable pixels",
    "url": "https://www.tomshardware.com/software/programming/playable-tomb-raider-runs-on-a-humble-1-watt-chip-usd25-board-with-dual-core-400-mhz-esp32-p4-mcu-scales-openlara-up-to-1-024-x-600-playable-pixels",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T11:00:00+00:00",
    "summary": "A retro video gaming devotee has showcased Lara Croft adventuring in and among ancient tombs on a humble ESP32-P4 microcontroller."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/ukraines-sargan-3000-triumphs-in-first-ever-drone-vs-drone-boat-battle-video-shows-russian-mbek-destroyed-by-its-foes-12-7mm-automatic-turret",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine triumphs in 'first-ever' drone-vs-drone boat battle — video shows Russian MBeK destroyed by Sargan 3000's 12.7mm automatic turret",
    "url": "https://www.tomshardware.com/tech-industry/drones/ukraines-sargan-3000-triumphs-in-first-ever-drone-vs-drone-boat-battle-video-shows-russian-mbek-destroyed-by-its-foes-12-7mm-automatic-turret",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T10:30:00+00:00",
    "summary": "Ukraine’s Navy has claimed that it has won 'the first-ever battle of unmanned naval boats.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/syitren-rm1-transparent-wall-mounted-cd-player-harkens-back-to-a-more-civilized-era-visible-disc-and-mechanisms-make-for-a-tangible-listening-experience",
    "domain": "AI 算力 / 半导体",
    "title": "Transparent wall-mounted CD player raises over $540,000 on Kickstarter — $109 Syitren RM1's visible disc and mechanisms channel 90s B&O nostalgia with Bluetooth and battery power",
    "url": "https://www.tomshardware.com/speakers/syitren-rm1-transparent-wall-mounted-cd-player-harkens-back-to-a-more-civilized-era-visible-disc-and-mechanisms-make-for-a-tangible-listening-experience",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T10:00:00+00:00",
    "summary": "Syitren RM1 transparent wall-mounted CD player harkens back to a more civilized era with visible disc and mechanisms."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/build-a-high-end-amd-gaming-pc-for-less-ryzen-7-9800x3d-bundle-includes-an-x870e-motherboard-32gb-ddr5-aio-cooler-and-a-game-for-usd1-109-99",
    "domain": "AI 算力 / 半导体",
    "title": "Build a high-end AMD gaming PC for less — Ryzen 7 9800X3D bundle includes an X870E motherboard, 32GB DDR5, AIO cooler and a game for $1,109.99",
    "url": "https://www.tomshardware.com/pc-components/build-a-high-end-amd-gaming-pc-for-less-ryzen-7-9800x3d-bundle-includes-an-x870e-motherboard-32gb-ddr5-aio-cooler-and-a-game-for-usd1-109-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T00:42:50+00:00",
    "summary": "The bundle pairs one of the best gaming CPUs available with a premium X870E motherboard and 32GB of DDR5-6000 memory, while also throwing in a 240mm AIO cooler and a free copy of Onimusha: Way of the "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/iran-and-houthi-rebels-used-anthropics-claude-ai-to-target-us-warships-and-build-hypersonic-missiles-houthi-rebels-also-used-the-bot-to-code-ballistic-missile-guidance-systems",
    "domain": "AI 算力 / 半导体",
    "title": "Iran and Houthi rebels used Anthropic's Claude AI to target US warships and build hypersonic missiles — Houthi rebels also used the bot to code ballistic missile guidance systems",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/iran-and-houthi-rebels-used-anthropics-claude-ai-to-target-us-warships-and-build-hypersonic-missiles-houthi-rebels-also-used-the-bot-to-code-ballistic-missile-guidance-systems",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T15:03:10+00:00",
    "summary": "'Great Satan's' AI comes in handy."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/us-customs-supervisor-busted-for-stealing-core-i7-cpus-ram-and-hard-drives-from-homeland-security-pcs-stolen-tech-swapped-with-inferior-hardware-and-cashed-out-on-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "US Customs supervisor busted for stealing Core i7 CPUs, RAM, and hard drives from Homeland Security PCs, damage estimated at $105,800 — stolen tech swapped with inferior hardware and cashed out on New",
    "url": "https://www.tomshardware.com/pc-components/us-customs-supervisor-busted-for-stealing-core-i7-cpus-ram-and-hard-drives-from-homeland-security-pcs-stolen-tech-swapped-with-inferior-hardware-and-cashed-out-on-newegg",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T14:09:29+00:00",
    "summary": "U.S. Customs and Border Protection supervisor switched hardware from Department of Homeland Security computers with slower components and traded in stolen hardware to Newegg's Trade-In program for sto"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/we-tested-dlss-multi-frame-generation-on-rtx-40-series-gpus-new-mod-brings-rtx-50-series-exclusive-feature-to-older-cards-and-it-really-works",
    "domain": "AI 算力 / 半导体",
    "title": "We tested unofficial DLSS Multi Frame Generation support on RTX 40-series GPUs — new mod brings RTX 50-series exclusive feature to older cards, and it really works",
    "url": "https://www.tomshardware.com/pc-components/gpus/we-tested-dlss-multi-frame-generation-on-rtx-40-series-gpus-new-mod-brings-rtx-50-series-exclusive-feature-to-older-cards-and-it-really-works",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T14:08:19+00:00",
    "summary": "We tested DLSS Multi Frame Generation on RTX 40-series GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/ikea-releases-new-skyrim-mod-that-adds-gloriously-mundane-kallax-shelving-unit-as-your-newest-companion-free-collab-provides-a-drab-flatpack-answer-to-your-loot-woes",
    "domain": "AI 算力 / 半导体",
    "title": "IKEA releases new Skyrim mod that adds gloriously mundane Kallax shelving unit as your newest companion — free collab provides a drab flatpack answer to your loot woes",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/ikea-releases-new-skyrim-mod-that-adds-gloriously-mundane-kallax-shelving-unit-as-your-newest-companion-free-collab-provides-a-drab-flatpack-answer-to-your-loot-woes",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T13:31:55+00:00",
    "summary": "IKEA has announced the Kallax Storageborn companion creation for players of The Elder Scrolls V: Skyrim Special Edition on PC or Xbox."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-september-12-2026-benchmarking-qwen-3-8-the-splintered-compute-economy-and-ai-breakthroughs",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: September 12, 2026 — Benchmarking Qwen 3.8, the splintered compute economy and AI breakthroughs",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-september-12-2026-benchmarking-qwen-3-8-the-splintered-compute-economy-and-ai-breakthroughs",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T12:00:00+00:00",
    "summary": "This week on Tom's Hardware Premium, we benchmarked Qwen 3.8 on a slew of different hardware, ruminated on the state of modern computing after returning from IFA 2026, and broke down everything"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/iran-could-potentially-reverse-engineer-captured-u-s-underwater-drone-several-iranian-embassies-mock-us-over-capture-as-u-s-military-downplays-the-situation",
    "domain": "AI 算力 / 半导体",
    "title": "Iran could potentially reverse-engineer captured US underwater drone — several Iranian embassies mock US over capture, Navy claims lost Anduril vehicle was defective and unclassified",
    "url": "https://www.tomshardware.com/tech-industry/drones/iran-could-potentially-reverse-engineer-captured-u-s-underwater-drone-several-iranian-embassies-mock-us-over-capture-as-u-s-military-downplays-the-situation",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:30:00+00:00",
    "summary": "Iran may reverse-engineer a captured U.S. Navy Anduril Dive-LD underwater drone, as Tehran mocks the loss and Washington downplays its military value."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/kioxia-exceria-pro-g2-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia Exceria Pro G2 2TB SSD Review — Speed built to last",
    "url": "https://www.tomshardware.com/pc-components/ssds/kioxia-exceria-pro-g2-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:05:00+00:00",
    "summary": "Kioxia’s Exceria Pro G2 pairs the SM2508 and BiCS8 TLC flash for fast, efficient PCIe 5.0 storage. It’s not the quickest PCIe 5.0 SSD, but it is a reliable Black SN8100 alternative."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/lucky-pc-scavenger-discovers-12-rtx-3070-gpus-from-the-crypto-mining-era-cards-survived-years-of-basement-storage-with-only-minor-signs-of-wear",
    "domain": "AI 算力 / 半导体",
    "title": "Lucky PC scavenger discovers 12 RTX 3070 GPUs from the crypto mining era — cards survived years of basement storage with only minor signs of wear",
    "url": "https://www.tomshardware.com/pc-components/gpus/lucky-pc-scavenger-discovers-12-rtx-3070-gpus-from-the-crypto-mining-era-cards-survived-years-of-basement-storage-with-only-minor-signs-of-wear",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:00:00+00:00",
    "summary": "What looked like a couple of forgotten mining rigs turned out to be a surprisingly valuable haul, with 12 RTX 3070 graphics cards potentially still ready for gaming duty."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/apples-a20-pro-shatters-geekbench-7-single-core-record-2nm-chip-beats-desktop-intel-core-i9-and-amd-ryzen-9-by-up-to-32-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's A20 Pro shatters Geekbench 7 single-core record — 2nm chip beats desktop Intel Core i9 and AMD Ryzen 9 by up to 32%",
    "url": "https://www.tomshardware.com/pc-components/cpus/apples-a20-pro-shatters-geekbench-7-single-core-record-2nm-chip-beats-desktop-intel-core-i9-and-amd-ryzen-9-by-up-to-32-percent",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T10:48:32+00:00",
    "summary": "Apple's A20 Pro smartphone SoC outperforms all smartphone processors by a wide margin and manages to leave behind latest laptop processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/consumer-rights-wiki-documents-at-least-44-instances-in-which-sony-says-you-own-your-games-project-is-direct-assault-on-sonys-claim-in-recent-ownership-lawsuit",
    "domain": "AI 算力 / 半导体",
    "title": "Wiki documents at least 44 instances in which Sony says you own your games as digital games ownership lawsuit progresses — project is direct assault on Sony's claim in recent ownership lawsuit",
    "url": "https://www.tomshardware.com/video-games/playstation/consumer-rights-wiki-documents-at-least-44-instances-in-which-sony-says-you-own-your-games-project-is-direct-assault-on-sonys-claim-in-recent-ownership-lawsuit",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T10:30:00+00:00",
    "summary": "The detailed sourcing directly attacks Sony's legal claim that a reasonable person wouldn't expect to own their digital purchases on the PlayStation Store."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/engineer-turns-simulated-fly-brain-into-a-crypto-day-trader-posts-downloadable-sim-to-github-166-700-virtual-neurons-read-candlestick-charts-for-dopamine-hits",
    "domain": "AI 算力 / 半导体",
    "title": "Engineer turns simulated fly brain into a crypto day trader, posts downloadable sim to GitHub — 166,700 virtual neurons read candlestick charts for dopamine hits",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/engineer-turns-simulated-fly-brain-into-a-crypto-day-trader-posts-downloadable-sim-to-github-166-700-virtual-neurons-read-candlestick-charts-for-dopamine-hits",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T10:00:00+00:00",
    "summary": "Coinbase engineer turns a fly brain into a crypto day trader — Stonkfly has 116,700 simulated neurons and hasn't lost its money yet"
  },
  {
    "id": "hn:49567357",
    "domain": "AI 算力 / 半导体",
    "title": "Georgi Gerganov on llama.cpp/ggml future after Nvidia acquisition of HuggingFace",
    "url": "https://twitter.com/ggerganov/status/2095897173376618881",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-04T17:12:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49657991",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a $20B Semiconductor Fab (2024)",
    "url": "https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-11T13:22:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594189",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang says 'AGI has arrived' and congratulates OpenAI",
    "url": "https://www.businessinsider.com/nvidia-jensen-huang-agi-openai-astra-ai-2026-9",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-07T05:23:31+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/inside-architect-labs-two-week-chip-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Architect Labs’ Two-Week Chip Design",
    "url": "https://www.eetimes.com/inside-architect-labs-two-week-chip-design/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T02:00:00+00:00",
    "summary": "Architect Labs says its AI can drag custom chip design from years to weeks with Redwood. The post Inside Architect Labs’ Two-Week Chip Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/fabships-aim-to-exploit-free-space-vacuum-for-compound-semiconductor-substrates/",
    "domain": "AI 算力 / 半导体",
    "title": "Fabships Aim to Exploit ‘Free’ Space Vacuum for Compound Semiconductor Substrates",
    "url": "https://www.eetimes.com/fabships-aim-to-exploit-free-space-vacuum-for-compound-semiconductor-substrates/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:00:00+00:00",
    "summary": "Space is the next frontier for semiconductor manufacturing, as startup Besxar, founded by an ex-OpenAI technical director, completed its first SpaceX flight and recovered wafer samples without contami"
  },
  {
    "id": "rss:https://www.eetimes.com/soc-planner-a-new-generation-of-automated-soc-design-exploration-managing-cost-effectiveness-and-sustainability/",
    "domain": "AI 算力 / 半导体",
    "title": "SoC PLANNER: A New Generation of Automated SoC Design Exploration Managing Cost-Effectiveness and Sustainability",
    "url": "https://www.eetimes.com/soc-planner-a-new-generation-of-automated-soc-design-exploration-managing-cost-effectiveness-and-sustainability/",
    "source": "Defacto Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T14:36:58+00:00",
    "summary": "GRENOBLE, France &#8211; [2026, September 8th] CEA, Defacto Technologies, and Innova Advanced Technologies today announced the completion of SoC PLANNER, a three-years project funded by BPI France, as"
  },
  {
    "id": "rss:https://www.eetimes.com/should-standards-trump-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "Should Standards Trump Innovation?",
    "url": "https://www.eetimes.com/should-standards-trump-innovation/",
    "source": "Prakash Sangam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T13:52:31+00:00",
    "summary": "Standards shouldn’t muzzle RFID’s next leap: Gen2X keeps Gen2 compatibility while boosting range, speed, and reliability. The post Should Standards Trump Innovation? appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/indian-researchers-look-beyond-gpus-to-neuromorphic-ai-hardware/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Researchers Look Beyond GPUs to Neuromorphic AI Hardware",
    "url": "https://www.eetimes.com/indian-researchers-look-beyond-gpus-to-neuromorphic-ai-hardware/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:31:15+00:00",
    "summary": "As AI workloads become more computationally demanding, Indian researchers argue that the next advance may come from rethinking computing architecture itself. The post Indian Researchers Look Beyond GP"
  },
  {
    "id": "rss:https://www.eetimes.com/from-ai-assisted-eda-to-ai-mediated-engineering/",
    "domain": "AI 算力 / 半导体",
    "title": "From AI-Assisted EDA to AI-Mediated Engineering",
    "url": "https://www.eetimes.com/from-ai-assisted-eda-to-ai-mediated-engineering/",
    "source": "Simon Davidmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:23:10+00:00",
    "summary": "What DAC 2026 revealed about agents, engines, trust—and why the industry should be optimistic. The post From AI-Assisted EDA to AI-Mediated Engineering appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/proven-actions-technologys-end-to-end-audio-architecture-tames-sounds-black-magic/",
    "domain": "AI 算力 / 半导体",
    "title": "Proven: Actions Technology’s End-to-End Audio Architecture Tames Sound’s “Black Magic”",
    "url": "https://www.eetimes.com/proven-actions-technologys-end-to-end-audio-architecture-tames-sounds-black-magic/",
    "source": "Franklin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:00:00+00:00",
    "summary": "Whether in the mass consumer market or the high-end professional audio segment, sound quality remains the defining factor that separates one product from another. Consumers’ appetite for better audio "
  },
  {
    "id": "rss:https://www.eetimes.com/adi-snaps-alif-semiconductor-to-push-ai-into-physical-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "ADI Snaps Alif Semiconductor to Push AI into Physical Systems",
    "url": "https://www.eetimes.com/adi-snaps-alif-semiconductor-to-push-ai-into-physical-systems/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:00:00+00:00",
    "summary": "The $1.35 billion deal marks another edge AI leap of faith, combining analog sensing with low-power AI processors. The post ADI Snaps Alif Semiconductor to Push AI into Physical Systems appeared first"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/china-modified-nvidia-rtx-5090-with-massive-96gb-of-memory-appears-on-alibaba-for-less-than-usd4-000-3x-more-vram-at-65-percent-the-cost-of-the-original",
    "domain": "AI 算力 / 半导体",
    "title": "China-modified Nvidia RTX 5090 with massive 96GB of memory appears on Alibaba for less than $4,000 — 3x more VRAM at 65% the cost of the original",
    "url": "https://www.tomshardware.com/pc-components/gpus/china-modified-nvidia-rtx-5090-with-massive-96gb-of-memory-appears-on-alibaba-for-less-than-usd4-000-3x-more-vram-at-65-percent-the-cost-of-the-original",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:32:36+00:00",
    "summary": "An alleged Nvidia GeForce RTX 5090 96GB with 96GB of modded VRAM surfaces on Alibaba for $3888."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/sanctioned-chinese-supercomputer-maker-stripped-of-io500-benchmark-crown-intel-powered-aurora-retakes-the-lead-record-breaking-parastor-f9000-storage-system-doesnt-meet-reproducibility-requirements",
    "domain": "AI 算力 / 半导体",
    "title": "Sanctioned Chinese supercomputer maker stripped of IO500 benchmark crown, Intel-powered Aurora retakes the lead — record-breaking ParaStor F9000 storage system doesn't meet reproducibility requirement",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/sanctioned-chinese-supercomputer-maker-stripped-of-io500-benchmark-crown-intel-powered-aurora-retakes-the-lead-record-breaking-parastor-f9000-storage-system-doesnt-meet-reproducibility-requirements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:26:12+00:00",
    "summary": "Sugon's record-breaking ParaStor F9000 storage systems have lost their IO500 Production crowns and have been moved to the Research list after failing to meet the benchmark's highest reproducibility re"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/save-20-percent-on-this-144-in-1-screwdriver-set-perfect-for-hobbyists-and-pc-builders-under-usd40-epic-starter-toolkit-ships-with-electric-and-precision-drivers-along-with-120-magnetic-bits-and-22-maintenance-tools",
    "domain": "AI 算力 / 半导体",
    "title": "Save 20% on this 144-in-1 screwdriver set, perfect for hobbyists and PC builders under $40 — epic starter toolkit ships with electric and precision drivers, along with 120 magnetic bits and 22 mainten",
    "url": "https://www.tomshardware.com/desktops/pc-building/save-20-percent-on-this-144-in-1-screwdriver-set-perfect-for-hobbyists-and-pc-builders-under-usd40-epic-starter-toolkit-ships-with-electric-and-precision-drivers-along-with-120-magnetic-bits-and-22-maintenance-tools",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:32:15+00:00",
    "summary": "This 144-in-1 repair toolkit from Strebito is on sale, with 120 bits and a number of other tools for less than $40."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/gamestop-is-reopening-recently-closed-stores-despite-massive-retail-cuts-select-locations-return-nationwide-starting-september-11",
    "domain": "AI 算力 / 半导体",
    "title": "GameStop is reopening recently closed stores despite massive retail cuts — select locations return nationwide starting September 11",
    "url": "https://www.tomshardware.com/tech-industry/gamestop-is-reopening-recently-closed-stores-despite-massive-retail-cuts-select-locations-return-nationwide-starting-september-11",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T12:50:35+00:00",
    "summary": "After shutting down hundreds of locations and dramatically shrinking its physical retail footprint, GameStop is bringing select stores back as its business continues to evolve beyond physical games."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/at-ifa-2026-computing-chased-the-high-and-low-ends-ai-and-budget-focused-machines-left-little-for-the-rest-of-us",
    "domain": "AI 算力 / 半导体",
    "title": "At IFA 2026, computing chased the high and low ends — AI and budget-focused machines left little for the rest of us",
    "url": "https://www.tomshardware.com/laptops/at-ifa-2026-computing-chased-the-high-and-low-ends-ai-and-budget-focused-machines-left-little-for-the-rest-of-us",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T12:44:08+00:00",
    "summary": "At IFA 2026, a bifurcated computing landscape widened as more companies chased Apple's MacBook Neo while also keeping one foot firmly planted in the AI space."
  },
  {
    "id": "hn:49557813",
    "domain": "AI 算力 / 半导体",
    "title": "Tell HN: NVIDIA's Acquisition of HuggingFace was for $HuggingFace",
    "url": "https://news.ycombinator.com/item?id=49557813",
    "source": "MontagFTB",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-03T22:08:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552375",
    "domain": "AI 算力 / 半导体",
    "title": "Texas Data Center Map: See where data centers are operating or planned",
    "url": "https://www.kxan.com/news/texas/texas-data-center-tracker-see-where-600-projects-are-operating-or-planned-across-state-in-interactive-map/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-09-03T16:10:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552616",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Mireye (YC S26) – Infrastructure for Physical World AI Agents",
    "url": "https://news.ycombinator.com/item?id=49552616",
    "source": "anshchokshi",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-03T16:24:13+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/what-six-hours-on-the-runway-told-me-about-air-traffic-control-resilience-and-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "What Six Hours on the Runway Told Me About Air Traffic Control, Resilience, and AI",
    "url": "https://www.eetimes.com/what-six-hours-on-the-runway-told-me-about-air-traffic-control-resilience-and-ai/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T08:09:30+00:00",
    "summary": "A U.K. air traffic control glitch stranded flights for hours, prompting reflections on resilience, redundancy, legacy systems, and AI. The post What Six Hours on the Runway Told Me About Air Traffic C"
  },
  {
    "id": "hn:49084371",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Tines 3B – safe workflow automation for when everyone builds software",
    "url": "https://www.tines.com/",
    "source": "retsol",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-07-28T14:23:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1160,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 605,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-09-03T16:06:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49331423",
    "domain": "大厂 AI 动态",
    "title": "AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira",
    "url": "https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug",
    "source": "galnagli",
    "platform": "hackernews",
    "points": 424,
    "published_at": "2026-08-17T14:18:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49468818",
    "domain": "大厂 AI 动态",
    "title": "Gemini-3.5-Transcribe",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source": "k9294",
    "platform": "hackernews",
    "points": 363,
    "published_at": "2026-08-27T18:03:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 297,
    "published_at": "2026-08-27T17:06:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-09-07T20:12:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49383326",
    "domain": "大厂 AI 动态",
    "title": "Codex on AWS bedrock bug causing 10x charges",
    "url": "https://github.com/openai/codex/issues/37674",
    "source": "TheP1000",
    "platform": "hackernews",
    "points": 148,
    "published_at": "2026-08-21T03:17:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-09-08T14:14:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49653699",
    "domain": "大厂 AI 动态",
    "title": "The Gemini app is now available for Windows",
    "url": "https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-windows/",
    "source": "quysala12",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-11T04:52:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49652122",
    "domain": "大厂 AI 动态",
    "title": "Setting up OpenCode with Ollama and sbx on Mac",
    "url": "https://tensorsandtokens.com/posts/opencode-ollama/",
    "source": "etoxin",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-09-11T00:45:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994441/trump-mike-johnson-ai-industry-overreacting",
    "domain": "大厂 AI 动态",
    "title": "Trump and Mike Johnson think the AI industry is overreacting",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994441/trump-mike-johnson-ai-industry-overreacting",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T19:41:48+00:00",
    "summary": "Yesterday, Anthropic CEO Dario Amodei published a lengthy open letter saying it was time to \"pace the frontier\" and slow down AI development. OpenAI's Sam Altman and Elon Musk both agreed, publicly vo"
  },
  {
    "id": "rss:https://www.theverge.com/tech/994426/apple-iphone-game-controllers",
    "domain": "大厂 AI 动态",
    "title": "Apple is reportedly working on iPhone game controllers",
    "url": "https://www.theverge.com/tech/994426/apple-iphone-game-controllers",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T18:30:16+00:00",
    "summary": "Bloomberg's Mark Gurman says Apple is developing two game controllers for the iPhone and will likely sell them under the Beats brand. Rumors that Apple might enter the game controller business have ci"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/994415/the-units-digital-stimulation-synthpunk-review",
    "domain": "大厂 AI 动态",
    "title": "The Units’ Digital Stimulation is synthpunk perfection",
    "url": "https://www.theverge.com/entertainment/994415/the-units-digital-stimulation-synthpunk-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T17:36:10+00:00",
    "summary": "The Units are a band I discovered in part thanks to No Dogs in Space. During their miniseries on The Screamers (another incredible band worth checking out), they mention synthpunk.org as one of their "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/994405/waymo-pulls-over-calls-cops-on-riders-with-a-ghost-gun",
    "domain": "大厂 AI 动态",
    "title": "Waymo pulls over, calls cops on riders with a ghost gun",
    "url": "https://www.theverge.com/transportation/994405/waymo-pulls-over-calls-cops-on-riders-with-a-ghost-gun",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T14:28:12+00:00",
    "summary": "Two people were arrested in San Fransico while riding around in a Waymo robotaxi after the cab pulled over and called the cops on them. The riders were juveniles in possession of a loaded AR-style gho"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/994393/your-mother-your-mother-your-mother-review-tiff-2026",
    "domain": "大厂 AI 动态",
    "title": "Your Mother Your Mother Your Mother will make you forget all about Marvel’s Blade disaster",
    "url": "https://www.theverge.com/entertainment/994393/your-mother-your-mother-your-mother-review-tiff-2026",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:00:00+00:00",
    "summary": "Marvel's mishandling of its Blade reboot will likely go down as one of the studio's biggest mistakes. There was a great actor in place to play the vampire hunter (Mahershala Ali), and a promising dire"
  },
  {
    "id": "rss:https://www.theverge.com/column/994172/your-car-is-selling-your-data",
    "domain": "大厂 AI 动态",
    "title": "Your car is selling your data",
    "url": "https://www.theverge.com/column/994172/your-car-is-selling-your-data",
    "source": "Andrew Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on cars, data privacy, and autonomous vehicles, follow Andrew J. Hawkins. The Stepback arrives"
  },
  {
    "id": "rss:https://www.theverge.com/tech/994218/apple-iphone-18-pro-airpods-5-meta-muse-ai-sony-headphones",
    "domain": "大厂 AI 动态",
    "title": "Apple’s new phones are here",
    "url": "https://www.theverge.com/tech/994218/apple-iphone-18-pro-airpods-5-meta-muse-ai-sony-headphones",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 143, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, new tech season is here, and also you can read all the old editions a"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994383/openais-rogue-ai-rubygems-hack",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s rogue AI tried to hack another company in May",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994383/openais-rogue-ai-rubygems-hack",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T21:41:36+00:00",
    "summary": "In May, hundreds of malicious and spam packages were uploaded to RubyGems, causing a serious disruption for the host. Now independent researchers have said that a swarm of OpenAI agents were responsib"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994384/sam-altman-no-openai-ipo-ill-advised",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman says OpenAI going public in 2026 would be ‘ill-advised’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994384/sam-altman-no-openai-ipo-ill-advised",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T21:16:28+00:00",
    "summary": "OpenAI CEO Sam Altman confirmed that there would be no OpenAI IPO in 2026 during an interview with Fortune. Over the course of 45 minutes, Altman discussed a variety of subjects including the Hugging "
  },
  {
    "id": "rss:https://www.theverge.com/games/994371/starcraft-returns-in-2030-as-an-open-world-shooter",
    "domain": "大厂 AI 动态",
    "title": "StarCraft returns in 2030 as an open-world shooter",
    "url": "https://www.theverge.com/games/994371/starcraft-returns-in-2030-as-an-open-world-shooter",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T20:08:09+00:00",
    "summary": "Blizzard originally tried to bring the StarCraft universe to the world of 3D shooters way back in 2002 with StarCraft: Ghost. It sat in development hell for years until Blizzard president Mike Morhaim"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/insight-partners-devin-parekh-on-why-the-firm-is-diversifying-while-everyone-else-bets-the-farm-on-openai-and-anthropic/",
    "domain": "大厂 AI 动态",
    "title": "Insight Partners’ Deven Parekh on why the firm is diversifying while everyone else bets the farm on OpenAI and Anthropic",
    "url": "https://techcrunch.com/2026/09/13/insight-partners-devin-parekh-on-why-the-firm-is-diversifying-while-everyone-else-bets-the-farm-on-openai-and-anthropic/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T21:30:00+00:00",
    "summary": "Insight Partners' Devin Parekh opens up about losing Legora to General Catalyst, why he's fine holding stakes in rival AI labs, and why — even as everyone else piles into OpenAI and Anthropic — his $9"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/larry-ellison-cancels-7-5-billion-sale-of-oracle-stock/",
    "domain": "大厂 AI 动态",
    "title": "Larry Ellison cancels $7.5 billion sale of Oracle stock",
    "url": "https://techcrunch.com/2026/09/13/larry-ellison-cancels-7-5-billion-sale-of-oracle-stock/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T20:49:38+00:00",
    "summary": "Oracle had previously disclosed that Ellison planned to sell 50 million shares worth around $7.5 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/the-9-buzziest-startups-from-y-combinators-latest-demo-day-according-to-vcs/",
    "domain": "大厂 AI 动态",
    "title": "The 9 buzziest startups from Y Combinator’s latest Demo Day, according to VCs",
    "url": "https://techcrunch.com/2026/09/13/the-9-buzziest-startups-from-y-combinators-latest-demo-day-according-to-vcs/",
    "source": "Marina Temkin, Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T20:28:00+00:00",
    "summary": "From floating reactors to brain chips: VCs picked their favorite YC startups from the summer batch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/whats-behind-the-ai-industrys-latest-warnings-of-doom/",
    "domain": "大厂 AI 动态",
    "title": "What’s behind the AI industry’s latest warnings of doom?",
    "url": "https://techcrunch.com/2026/09/13/whats-behind-the-ai-industrys-latest-warnings-of-doom/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T19:40:15+00:00",
    "summary": "On Equity, we discussed the AI industry's latest debate about whether it poses an existential threat to humanity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/obama-urges-democrats-to-have-a-clear-plan-for-ai-safeguards/",
    "domain": "大厂 AI 动态",
    "title": "Obama urges Democrats to have a ‘clear plan’ for AI safeguards",
    "url": "https://techcrunch.com/2026/09/13/obama-urges-democrats-to-have-a-clear-plan-for-ai-safeguards/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T16:30:00+00:00",
    "summary": "Obama recently said that Democrats need to make artificial intelligence one of their “central agendas” and “have a very clear plan” to address concerns around the technology’s economic impact and safe"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/techcrunch-mobility-lyft-has-entered-the-robotaxi-chat/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Lyft has entered the robotaxi chat",
    "url": "https://techcrunch.com/2026/09/13/techcrunch-mobility-lyft-has-entered-the-robotaxi-chat/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T16:04:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation, and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/fusion-power-startups-find-new-partners-in-the-defense-world/",
    "domain": "大厂 AI 动态",
    "title": "Fusion power startups find new partners in the defense world",
    "url": "https://techcrunch.com/2026/09/13/fusion-power-startups-find-new-partners-in-the-defense-world/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:15:00+00:00",
    "summary": "Fusion startups are inking defense-related deals, reigniting the relationship between fusion and national security that might have gone dormant, but never completely disappeared."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/automattic-confirms-mullenweg-has-returned-as-ceo-after-attempted-ouster-by-board/",
    "domain": "大厂 AI 动态",
    "title": "Automattic confirms Mullenweg has returned as CEO after attempted ouster by board",
    "url": "https://techcrunch.com/2026/09/12/automattic-confirms-mullenweg-has-returned-as-ceo-after-attempted-ouster-by-board/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T23:25:38+00:00",
    "summary": "Automattic says Mullenweg is back as \"chairman and CEO of Automattic, with full support of the board.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s Sam Altman says it would be ‘ill-advised’ to go public in 2026",
    "url": "https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T20:19:16+00:00",
    "summary": "While OpenAI has filed confidentially for an IPO, the company will not be going public this year, according to CEO Sam Altman."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic CEO outlines plan to slow AI development",
    "url": "https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T19:34:44+00:00",
    "summary": "Anthropic's Dario Amodei and OpenAI's Sam Altman seem to agree that it's time to \"pace the frontier.\" What would that actually look like?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/tesla-says-it-will-finally-unveil-the-second-generation-roadster-on-october-1/",
    "domain": "大厂 AI 动态",
    "title": "Tesla says it will finally unveil the second generation Roadster on October 1",
    "url": "https://techcrunch.com/2026/09/12/tesla-says-it-will-finally-unveil-the-second-generation-roadster-on-october-1/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T19:21:19+00:00",
    "summary": "Tesla’s halo sports car was first announced in November 2017."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/",
    "domain": "大厂 AI 动态",
    "title": "Revolut confirms customer data breach through fake government requests",
    "url": "https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T14:40:00+00:00",
    "summary": "Revolut said it notified affected customers and alerted the relevant government agency, law enforcement, and financial regulators."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/unvaccinated-pennsylvania-woman-died-of-measles-complications-coroner-says/",
    "domain": "大厂 AI 动态",
    "title": "Unvaccinated Pennsylvania woman died of measles complications, coroner says",
    "url": "https://arstechnica.com/health/2026/09/unvaccinated-pennsylvania-woman-died-of-measles-complications-coroner-says/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T21:56:52+00:00",
    "summary": "The 40-year-old unvaccinated woman reportedly had underlying health conditions."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/i-fixed-a-tractor-using-john-deeres-self-repair-service-farmers-arent-sold-on-it/",
    "domain": "大厂 AI 动态",
    "title": "I fixed a tractor using John Deere’s self-repair service. Farmers aren’t sold on it.",
    "url": "https://arstechnica.com/gadgets/2026/09/i-fixed-a-tractor-using-john-deeres-self-repair-service-farmers-arent-sold-on-it/",
    "source": "Boone Ashworth, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T11:00:41+00:00",
    "summary": "The manufacturer has a service that lets owners repair their own equipment."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/i-spent-4000-on-a-robot-dog-from-china/",
    "domain": "大厂 AI 动态",
    "title": "I spent $4,000 on a robot dog from China",
    "url": "https://arstechnica.com/gadgets/2026/09/i-spent-4000-on-a-robot-dog-from-china/",
    "source": "Timothy B. Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:00:53+00:00",
    "summary": "Unitree might be the world’s most important robotics company."
  },
  {
    "id": "rss:https://www.producthunt.com/products/marqly",
    "domain": "大厂 AI 动态",
    "title": "Marqly 6.0",
    "url": "https://www.producthunt.com/products/marqly",
    "source": "Kim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T08:34:52+00:00",
    "summary": "Ask your bookmarks. Bring them to your AI. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/image-to-ascii-2",
    "domain": "大厂 AI 动态",
    "title": "Image to ASCII",
    "url": "https://www.producthunt.com/products/image-to-ascii-2",
    "source": "楠木",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T07:52:20+00:00",
    "summary": "Make ASCII art for READMEs, Discord & creative visuals Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/appdesigns",
    "domain": "大厂 AI 动态",
    "title": "appdesigns",
    "url": "https://www.producthunt.com/products/appdesigns",
    "source": "Haider Nawaz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T00:19:15+00:00",
    "summary": "Design amazing appstore screenshots for free Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/slashy-3",
    "domain": "大厂 AI 动态",
    "title": "Slashy Assistant",
    "url": "https://www.producthunt.com/products/slashy-3",
    "source": "Harsha Gaddipati",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T02:52:46+00:00",
    "summary": "The AI assistant that does email for you Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/aside-6",
    "domain": "大厂 AI 动态",
    "title": "Aside",
    "url": "https://www.producthunt.com/products/aside-6",
    "source": "Garry Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T18:17:02+00:00",
    "summary": "AI browser that actually gets work done for you Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/appzapper",
    "domain": "大厂 AI 动态",
    "title": "AppZapper 3000",
    "url": "https://www.producthunt.com/products/appzapper",
    "source": "Austin Sarner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T00:16:57+00:00",
    "summary": "The uninstaller Apple forgot. Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/114453",
    "domain": "大厂 AI 动态",
    "title": "新 iPhone 相机如何记录照片真实性？开发者视角的猜想和尝试",
    "url": "https://sspai.com/post/114453",
    "source": "HaroldLee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T07:16:23+00:00",
    "summary": "照片能证明它被拍过，但不能证明镜头前是真的。查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/114410",
    "domain": "大厂 AI 动态",
    "title": "众测招募｜泡泡骚 Low Pro：给新 iPhone 添一件极简「背心」",
    "url": "https://sspai.com/post/114410",
    "source": "听歌的水獭",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T03:00:00+00:00",
    "summary": "每年九月都是苹果用户最期待的时节——苹果发布新一代iPhone。当新机到手，你可能也要随之给手上的配件更新换代。巧了，这一次，少数派给大家带来了一款颠覆以往所有磁吸支架形态的产品，它够薄、够轻、够好用 ...查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/114539",
    "domain": "大厂 AI 动态",
    "title": "派早报：美国 AI 高管呼吁放缓研发，特朗普反对",
    "url": "https://sspai.com/post/114539",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T22:55:34+00:00",
    "summary": "美国 AI 高管呼吁放缓研发，特朗普反对苹果解释 Apple Watch 不会持续录音LG 否认智能电视监控用户暴雪公布《魔兽世界》怀旧服儿童贴身使用笔记本电脑导致皮肤灼伤Android 开始支持密码管理器迁移看看就行的简讯少数派的近期动态你可能错过的好文章查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/113880",
    "domain": "大厂 AI 动态",
    "title": "搭建自己的 HomeLab（一）：聊聊我的硬件清单",
    "url": "https://sspai.com/post/113880",
    "source": "dong4j",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T07:51:55+00:00",
    "summary": "作为系列的第一篇，这里想把三件事讲清楚：什么是 HomeLab、我为什么愿意折腾它、以及这套东西需要哪些硬件、它们大概又要花多少钱。系列其他文章的目录放在文末。查看全文"
  },
  {
    "id": "hn:49566788",
    "domain": "大厂 AI 动态",
    "title": "Project HydraFusion: Frontier quality via multi-model orchestration",
    "url": "https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/",
    "source": "qainsights",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-09-04T16:24:50+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/",
    "domain": "大厂 AI 动态",
    "title": "Mecka AI nears $500M valuation in Sequoia-led deal amid rush for robot training data",
    "url": "https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T22:58:17+00:00",
    "summary": "The round for the two-year-old startup is coming together months after Mecka announced its Series A."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/khosla-ventures-is-opening-a-new-york-office-this-fall-its-first-outpost-outside-sand-hill-road/",
    "domain": "大厂 AI 动态",
    "title": "Khosla Ventures is opening a New York office this fall — its first outpost outside Sand Hill Road",
    "url": "https://techcrunch.com/2026/09/11/khosla-ventures-is-opening-a-new-york-office-this-fall-its-first-outpost-outside-sand-hill-road/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:19:05+00:00",
    "summary": "\"It's actually allegedly being built out now,\" said Rabois, who has clearly dealt with a missed construction timeline or two."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/",
    "domain": "大厂 AI 动态",
    "title": "Y Combinator’s Garry Tan wants US open-weight AI labs to ‘distill’ frontier models, too",
    "url": "https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:59:47+00:00",
    "summary": "Tan wants smaller, American open-weight AI labs to use the same kind of training techniques on American frontier AI labs, giving the U.S. a more robust set of open-weight options that aren’t Chinese."
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 286,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599992",
    "domain": "股票",
    "title": "Stockfish 19",
    "url": "https://stockfishchess.org/blog/2026/stockfish-19/",
    "source": "atiedebee",
    "platform": "hackernews",
    "points": 277,
    "published_at": "2026-09-07T16:17:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 109,
    "published_at": "2026-09-14T02:50:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 159,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682946",
    "domain": "股票",
    "title": "Show HN: Analyst Index – analysts who make money telling you good stock calls",
    "url": "https://www.analystidx.com/",
    "source": "haichuan",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-13T11:50:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49672197",
    "domain": "股票",
    "title": "Larry Ellison to sell up to $7.5B worth of Oracle stock",
    "url": "https://www.ft.com/content/25b1abb0-790f-4315-9b0c-530d959a086f",
    "source": "potatobox",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-12T13:37:21+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3781703",
    "domain": "股票",
    "title": "AI开发放缓=资本开支见顶？答案未必悲观",
    "url": "https://wallstreetcn.com/articles/3781703",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T08:10:56+00:00",
    "summary": "业内人士认为，只要AI应用和商业化仍在推进，算力、数据中心、电力、存储等基础设施投资逻辑就未被破坏，行业甚至可能从“烧钱扩张”转向“利用既有资产兑现回报”。更关键的是，AI仍处于技术快速演进的早期阶段，其他参与者未必愿意跟随头部公司踩下刹车。"
  },
  {
    "id": "wscn:3781701",
    "domain": "股票",
    "title": "曝DeepSeek来了位90后CFO",
    "url": "https://wallstreetcn.com/articles/3781701",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T07:52:21+00:00",
    "summary": "据报道，高瓴创投90后合伙人严文韬或将加入DeepSeek出任CFO，目前已在高瓴内部发起离职流程。严文韬出生于1991年，曾参与投资字节跳动、小红书、MiniMax等项目。此前报道称，DeepSeek已聘请中信证券，为其科创板IPO筹备相关工作。"
  },
  {
    "id": "wscn:3781702",
    "domain": "股票",
    "title": "上下文税：企业AI的隐形瓶颈",
    "url": "https://wallstreetcn.com/articles/3781702",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T07:49:32+00:00",
    "summary": "损不足以奉有馀"
  },
  {
    "id": "wscn:3781670",
    "domain": "股票",
    "title": "AI开发放缓担忧升温，美股纳指100期货跌1.5%，韩股收跌3%，布油涨3%",
    "url": "https://wallstreetcn.com/articles/3781670",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T07:40:53+00:00",
    "summary": "AI巨头罕见联手呼吁放缓前沿模型开发，美股期货扩大跌幅，纳斯达克100指数期货下跌1.5%，标普500指数期货跌0.6%，道指期货跌0.1%。与此同时，沙特关闭输油管道推动布伦特原油飙涨至107美元，叠加美国CPI超预期，美联储周三加息概率已超90%。"
  },
  {
    "id": "wscn:3781696",
    "domain": "股票",
    "title": "AI如“外星心智”降临地球！辞职帖获破亿浏览后Anthropic前研究员接受采访",
    "url": "https://wallstreetcn.com/articles/3781696",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T07:27:50+00:00",
    "summary": "1.7亿次围观的辞职信揭开AI底牌：亲手造AI的人，私下正深感恐惧。Anthropic前研究员警告，半年内“外星心智”般的超级AI或面临失控，内部高管更坦言其毁灭全人类概率超10%且无解。行业深陷囚徒困境，这场豪赌亟待全球协同监管悬崖勒马。"
  },
  {
    "id": "wscn:3781700",
    "domain": "股票",
    "title": "养老理财重启扩围，长期资金争夺战升温",
    "url": "https://wallstreetcn.com/articles/3781700",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T07:22:23+00:00",
    "summary": "沉寂近三年的养老理财，正在重新打开产品扩容窗口。\n近期，市场关于养老理财新一轮扩围的预期持续升温，有..."
  },
  {
    "id": "wscn:3781698",
    "domain": "股票",
    "title": "中期分红破7100亿，投资天弘央企红利50基金捕捉分红重估机会",
    "url": "https://wallstreetcn.com/articles/3781698",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T07:14:33+00:00",
    "summary": "过去看央企红利，市场习惯把它归入类债券的防御品种，估值主要跟随市场风格和利率环境波动，分红被当作年度惯例而非可持续的财务纪律。现在，分红的稳定性和可预期性正在被重新评估。"
  },
  {
    "id": "wscn:3781694",
    "domain": "股票",
    "title": "AI争议升级之际，对冲基金买入科技股速度创15个月新高",
    "url": "https://wallstreetcn.com/articles/3781694",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T06:42:01+00:00",
    "summary": "对冲基金在过去11个交易日中有10次净买入美国TMT股票，以15个月最快速度重建科技多头。然而，一场AI政策风暴却在“最糟时刻”突袭，AI巨头放缓开发的呼吁遭拒，监管变数直接重挫软银等亚洲科技股。当多头狂欢撞上超级央行周，科技板块正面临严峻大考。"
  },
  {
    "id": "wscn:3781688",
    "domain": "股票",
    "title": "苹果预售追踪：iPhone 18 Pro系列海外需求信号偏弱，Duo评测正面但硬件落后",
    "url": "https://wallstreetcn.com/articles/3781688",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T06:32:12+00:00",
    "summary": "杰富瑞调研显示，iPhone 18 Pro开售后，美英德日四大市场交货等待时间较去年缩短5至11天，美国甚至无需等待——在产能持平前提下，这是需求疲软的明确信号。中港市场虽逆势走强，但投机囤货嫌疑未消。折叠屏新机Duo软件体验获肯，却以2000美元高价换来254克机身与双摄配置，硬件全面落后安卓竞品。杰富瑞维持\"跑输大市\"，目标价较现价隐含21%跌幅。"
  },
  {
    "id": "wscn:3781691",
    "domain": "股票",
    "title": "日本央行加息或已无悬念，关键在于如何应对高市政府和贝森特的压力",
    "url": "https://wallstreetcn.com/articles/3781691",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T06:31:40+00:00",
    "summary": "日本央行本周预计加息25个基点至1.25%，市场焦点转向行长植田和男如何应对美财长贝森特与日本高市阵营的双重政治干预。尽管日元升值与日债收益率走高为少鹰表态提供了掩护，但植田仍需在稳通胀与防套息交易平仓间艰难寻衡。"
  },
  {
    "id": "wscn:3781651",
    "domain": "股票",
    "title": "AI巨头们突然发现：最强模型，不发布反而更值钱",
    "url": "https://wallstreetcn.com/premium/articles/3781651?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T06:25:11+00:00",
    "summary": "过去两年，大模型公司的竞争规则几乎只有一个：更快训练、更快发布、更快刷新能力上限。但达里奥提出“放慢前沿”后，奥特曼和马斯克迅速表达支持，一个更值得财经市场关注的问题开始浮现：如果最强模型继续留在实验室，成熟一代再推向市场，AI巨头可能不仅更安全，也会拥有更长的产品周期、更好的价格纪律和更高的资本回报率。"
  },
  {
    "id": "wscn:3781693",
    "domain": "股票",
    "title": "村田副社长：MLCC需求至少持续到2028年，扩产计划“比过去更大胆”",
    "url": "https://wallstreetcn.com/articles/3781693",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T05:53:52+00:00",
    "summary": "村田制作所副社长表示，AI服务器拉动的MLCC需求增长至少将持续至2028年，中长期还将向边缘AI和实体AI延伸。公司已规划800亿日元产能投资，并正研究“比过去更大胆”的3至5年扩产方案，讨论已相当具体。"
  },
  {
    "id": "wscn:3780023",
    "domain": "股票",
    "title": "华源期货孙伏鲲带你用衍生品工具重塑交易体系：从波段结构到期权增强的四维交易系统",
    "url": "https://wallstreetcn.com/articles/3780023",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T05:52:05+00:00",
    "summary": "2026年9月19日，华源期货副总经理孙伏鲲投研框架大分享：四维一体，构建你的交易\"操作系统\""
  },
  {
    "id": "wscn:3781673",
    "domain": "股票",
    "title": "创业板午后跌超1%，培育钻石、MLCC、医药股集体走强，恒科指转跌，江波龙H股跌10%",
    "url": "https://wallstreetcn.com/articles/3781673",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T05:48:48+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市约3600股飘红。市场量能明显萎缩，上午半天成交1.11万亿。沪深两市半日成交额1.1万亿，较上个交易日缩量1705亿。板块方面，中际旭创、新易盛、长鑫科技、兆易创新低迷，宁德时代反弹。CRO、培育钻石、网络安全、覆铜板板块走强，银行、新能源汽车股活跃，军工、农业、光通信、存储板块调整。"
  },
  {
    "id": "wscn:3781690",
    "domain": "股票",
    "title": "加拿大总理将访欧，寻求欧盟“准成员国”特殊地位",
    "url": "https://wallstreetcn.com/articles/3781690",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T05:35:06+00:00",
    "summary": "分析人士表示，目前欧盟并没有“准成员国”这一正式类别，加拿大若寻求获得这一地位，恐面临一系列障碍。"
  },
  {
    "id": "wscn:3781689",
    "domain": "股票",
    "title": "美总统“口头接受”中国车企在美建厂，专家：其言论的现实效果还有待观察",
    "url": "https://wallstreetcn.com/articles/3781689",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T05:32:18+00:00",
    "summary": "黄河科技学院客座教授张翔认为，面对中国车企强有力的竞争，美国政府和车企的态度存在温差。美政府更多使用“一刀切”的方式阻止中国新能源汽车进入美国市场，而一些车企依然看重与中国企业的合作。特朗普“接受中企在美建厂”的最新表态，和他此前强调的制造业回流美国一脉相承，但这番言论的现实效果还有待观察。"
  },
  {
    "id": "wscn:3781695",
    "domain": "股票",
    "title": "一周展望：美联储领衔央行超级周 地缘与AI成市场关注焦点",
    "url": "https://wallstreetcn.com/articles/3781695",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:56:35+00:00",
    "summary": "国际油价破百和美国通胀数据高位运行令避险情绪升温，除了原油和日元之外，各类资产价格上周不同程度收低。..."
  },
  {
    "id": "wscn:3781677",
    "domain": "股票",
    "title": "兼并重组的临界点：发改委喊话背后， 中国汽车产业的底盘、困境与出清路径",
    "url": "https://wallstreetcn.com/premium/articles/3781677?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:02:19+00:00",
    "summary": "从「规模扩张」到「提质增效」，一场以产能利用率和利润率为标尺的产业重构，正在把车企生态极重新排列。"
  },
  {
    "id": "wscn:3781676",
    "domain": "股票",
    "title": "高盛合伙人：三重阻力压制美股，四大方向仍存布局机会",
    "url": "https://wallstreetcn.com/articles/3781676",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T03:50:22+00:00",
    "summary": "高盛合伙人Wilson指出，美股自二季度大涨后陷入横盘，三重阻力正在压制市场：中期选举历史规律、量化机器仍满仓做多、能源-债券-股票三角绞杀。油价因地缘政治上涨推升债券收益率，进而压制股票估值，Wilson称这是“最难解的问题”。他同时看好AI基础设施龙头、大宗商品（尤其铜）、德国股市、大型银行。"
  },
  {
    "id": "wscn:3781687",
    "domain": "股票",
    "title": "三家客户贡献44%营收，英伟达越来越依赖大客户了",
    "url": "https://wallstreetcn.com/articles/3781687",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T03:49:08+00:00",
    "summary": "英伟达客户集中度正在快速上升。据报道，本财年上半年，三家客户合计贡献了英伟达44%的总营收，而两年前没有任何单一客户占比超过10%。分析指出，这几家客户可能包括戴尔或鸿海科技。"
  },
  {
    "id": "hn:49594296",
    "domain": "股票",
    "title": "OpenAI 2025 financials $38.5B loss ahead of IPO",
    "url": "https://qz.com/openai-leaked-financials-losses-revenue-ipo-061626",
    "source": "u1hcw9nx",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-09-07T05:41:13+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-five-deals-that-made-apollo",
    "domain": "股票",
    "title": "The Five Deals That Made Apollo",
    "url": "https://www.netinterest.co/p/the-five-deals-that-made-apollo",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:25:40+00:00",
    "summary": "From distressed debt to a trillion-dollar machine"
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
    "id": "hn:49511824",
    "domain": "股票",
    "title": "Apple Is Suddenly an AI Infra Stock as OpenAI Buys 10k+ Macs",
    "url": "https://247wallst.com/investing/2026/08/31/apple-is-suddenly-an-ai-infrastructure-stock-as-openai-buys-macs-by-the-tens-of-thousands/",
    "source": "prabal97",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-31T16:44:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49593962",
    "domain": "股票",
    "title": "HPE Gives Oracle Right to Buy 4.2M Shares for 1 Cent Each",
    "url": "https://www.forbes.com/sites/antoniopequenoiv/2026/09/03/hewlett-packard-enterprise-gives-oracle-right-to-buy-205-million-in-stock-at-slashed-rate/",
    "source": "gurjeet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-07T04:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596033",
    "domain": "股票",
    "title": "Show HN: Forget Rigid Stock Screeners – A Universal Query API for Financial Data",
    "url": "https://financialdata.net/universal-query",
    "source": "_FDN_",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-07T09:24:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49323620",
    "domain": "股票",
    "title": "Anthropic IPO valuation hinges on $190-200B 2028 revenue forecast",
    "url": "https://www.reuters.com/business/anthropic-ipo-valuation-hinges-190-200-billion-2028-revenue-forecast-sources-say-2026-08-15/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-16T21:00:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49401229",
    "domain": "股票",
    "title": "Anthropic IPO filing will show AI backlash as a risk factor, sources say",
    "url": "https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-22T16:23:09+00:00",
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
    "id": "rss:https://www.netinterest.co/p/hot-european-summer",
    "domain": "股票",
    "title": "Hot European Summer",
    "url": "https://www.netinterest.co/p/hot-european-summer",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:33:06+00:00",
    "summary": "Europe is outperforming &#8211; but Europeans aren&#8217;t participating"
  },
  {
    "id": "hn:49451482",
    "domain": "股票",
    "title": "Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers",
    "source": "2OEH8eoCRo0",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-26T16:05:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49450370",
    "domain": "股票",
    "title": "Chinese Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.reuters.com/world/china/china-sponsored-hacking-platforms-seized-by-us-justice-department-says-2026-08-26/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-26T14:59:43+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/untangling-guggenheim",
    "domain": "股票",
    "title": "Untangling Guggenheim",
    "url": "https://www.netinterest.co/p/untangling-guggenheim",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:05:53+00:00",
    "summary": "How Private Credit Built Its Own Universe"
  },
  {
    "id": "rss:https://www.netinterest.co/p/great-scott",
    "domain": "股票",
    "title": "Great Scott",
    "url": "https://www.netinterest.co/p/great-scott",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:35:18+00:00",
    "summary": "Challenges Facing the Bond Trader in Chief"
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
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 427,
    "published_at": "2026-09-13T18:03:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-09-07T05:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 392,
    "published_at": "2026-08-19T00:53:51+00:00",
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
    "id": "hn:49602582",
    "domain": "金融",
    "title": "A Tesla ran a stop sign and killed a man, Full Self-Driving/Autopilot was on",
    "url": "https://electrek.co/2026/09/07/tesla-driver-assist-stop-sign-buena-vista/",
    "source": "FabHK",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-09-07T20:21:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49601846",
    "domain": "金融",
    "title": "Tesla killing Solar Roof is leaving installers with six-figure losses",
    "url": "https://electrek.co/2026/09/01/tesla-solar-roof-exit-installers-losses/",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T19:08:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49600997",
    "domain": "金融",
    "title": "No constitutional right to clean water, federal court finds",
    "url": "https://www.usatoday.com/story/news/nation/2026/09/07/court-constitution-right-clean-water/91649488007/",
    "source": "measurablefunc",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T17:52:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T14:49:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-09T13:16:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12227",
    "domain": "金融",
    "title": "Seasonal Trading in Commodity Futures: Evidence from Regression and Singular Spectrum Signals",
    "url": "https://arxiv.org/abs/2609.12227",
    "source": "Ralph Kosch, Robin Forsberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.12227v1 Announce Type: new Abstract: Commodity futures are shaped by harvest cycles, weather shocks, storage conditions, and seasonal demand, but it remains unclear whether recurring patter"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12387",
    "domain": "金融",
    "title": "Do Sanctions Backfire? New Evidence on the Macroeconomic Effects of Supporting Ukraine",
    "url": "https://arxiv.org/abs/2609.12387",
    "source": "Vicente Rios, Izaskun Barba, Lisa Gianmoena",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.12387v1 Announce Type: new Abstract: Using a balanced panel of 129 countries from 2000 to 2024, we estimate the macroeconomic costs of sanctions on Russia. To that end, we employ a novel tw"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12477",
    "domain": "金融",
    "title": "Large Signal Libraries: Equal-Weight Limits and the Divergent Spectra of Signals and PnL",
    "url": "https://arxiv.org/abs/2609.12477",
    "source": "Marc da Costa Nunes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.12477v1 Announce Type: new Abstract: An ensemble of roughly 3,000 signals over 20 assets was reported to have approximately 90% correlation with the leading component of the asset-space ret"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12515",
    "domain": "金融",
    "title": "Arbitrage in Estimate Nothing: an example",
    "url": "https://arxiv.org/abs/2609.12515",
    "source": "Johannes Brutsche, Julian Sester, Thorsten Schmidt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.12515v1 Announce Type: new Abstract: We give a two-period counterexample to the absence of arbitrage for the posterior-weighted pricing rule in Estimate nothing by Duembgen and Rogers. Both"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12666",
    "domain": "金融",
    "title": "Exact calibration of structural models via time-change",
    "url": "https://arxiv.org/abs/2609.12666",
    "source": "Fr\\'ed\\'eric Vrins, Damiano Brigo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.12666v1 Announce Type: new Abstract: In this note, we propose a general structural approach to model a default time $\\tau$ as the first-passage time (FPT) of a (``firm-value'') process $S$ "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12878",
    "domain": "金融",
    "title": "The Favorite-Longshot Bias in Prediction Markets: Evidence from Polymarket",
    "url": "https://arxiv.org/abs/2609.12878",
    "source": "Marcos Cardozo, Jos\\'e Ignacio Rivero-Wildemauwe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.12878v1 Announce Type: new Abstract: The favorite--longshot bias (FLB) is one of the most persistent return patterns in betting markets, but its prevalence in modern prediction markets and "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12976",
    "domain": "金融",
    "title": "Complements or Substitutes? Technology Adoption and the Demand for Clinical Care: Evidence from Automated Insulin Delivery",
    "url": "https://arxiv.org/abs/2609.12976",
    "source": "Moslem Rashidi, Cristina Ugolini, Gianluca Fiorentini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.12976v1 Announce Type: new Abstract: Whether medical technology reduces or increases demand for professional care is central to understanding its effects on healthcare utilization and costs"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13068",
    "domain": "金融",
    "title": "Policy Targeting with Binary Classification Trees: an Application to Rural Hospital Closures",
    "url": "https://arxiv.org/abs/2609.13068",
    "source": "Hongying Li, Lei Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.13068v1 Announce Type: new Abstract: Empirical researchers often use binary classification trees to identify subgroups at risk of adverse outcomes. We compare two classification tree algori"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.11971",
    "domain": "金融",
    "title": "Multi-Objective Enterprise Green Supply Chain Network Design",
    "url": "https://arxiv.org/abs/2609.11971",
    "source": "Felix Reichelk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.11971v1 Announce Type: cross Abstract: This paper introduces and studies the Multi-Objective Enterprise Green Supply Chain Network Design problem (MOEDGSCND) an extension of the well known "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12793",
    "domain": "金融",
    "title": "VertiFuseX: Generalizable Financial Forecasting via Multi-Stream Temporal Fusion",
    "url": "https://arxiv.org/abs/2609.12793",
    "source": "Aashish Bohra, Vivek Vijay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2609.12793v1 Announce Type: cross Abstract: Stock price prediction remains challenging due to the non-stationary and noisy nature of financial time series. Existing deep learning models often re"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.22985",
    "domain": "金融",
    "title": "Forecasting Liquidity Withdraw with Machine Learning Models",
    "url": "https://arxiv.org/abs/2509.22985",
    "source": "Haochuan (Kevin), Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2509.22985v2 Announce Type: replace Abstract: Liquidity withdrawal is a critical indicator of market fragility. In this project, I test a framework for forecasting liquidity withdrawal at the in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.07626",
    "domain": "金融",
    "title": "Universal basic income in a financial equilibrium",
    "url": "https://arxiv.org/abs/2601.07626",
    "source": "Kim Weston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2601.07626v3 Announce Type: replace Abstract: Universal basic income (UBI) is a tax scheme that uniformly redistributes aggregate income amongst the entire population of an economy. We prove the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.16212",
    "domain": "金融",
    "title": "Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk",
    "url": "https://arxiv.org/abs/2602.16212",
    "source": "German Nova Orozco, Duy-Minh Dang, Peter A. Forsyth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2602.16212v2 Announce Type: replace Abstract: Money-back guarantees (MBGs) address bequest concerns in pooled retirement income products by returning the initial purchase price through withdrawa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02823",
    "domain": "金融",
    "title": "Auditing Collector-Generated Graduation Labels on Pump.fun: Measurement Error and Temporal Non-Generalization",
    "url": "https://arxiv.org/abs/2607.02823",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2607.02823v4 Announce Type: replace Abstract: To examine whether collector-generated terminal labels on the pump.fun platform can be interpreted as platform-side graduation outcomes, and whether"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28222",
    "domain": "金融",
    "title": "Voice AI in Firms: A Natural Field Experiment on Automated Job Interviews",
    "url": "https://arxiv.org/abs/2607.28222",
    "source": "Brian Jabarian, Luca Henkel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2607.28222v2 Announce Type: replace Abstract: We study AI agents as information-collection technologies: automated systems that elicit decision-relevant signals from humans through live interact"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.29530",
    "domain": "金融",
    "title": "Linear Risk Sharing in Community-Based Insurance: Ruin Reduction in the Compound Poisson Model",
    "url": "https://arxiv.org/abs/2603.29530",
    "source": "Michel Denuit, Jos\\'e Miguel Flores-Contr\\'o, Christian Y. Robert",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2603.29530v2 Announce Type: replace-cross Abstract: This paper studies proportional risk sharing at claim occurrence time in community-based insurance. Each participant is modeled by an individu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.18019",
    "domain": "金融",
    "title": "A data-driven Fourier-mixture neural-network method for density estimation",
    "url": "https://arxiv.org/abs/2605.18019",
    "source": "Duy-Minh Dang, Volter Entoma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T04:00:00+00:00",
    "summary": "arXiv:2605.18019v2 Announce Type: replace-cross Abstract: We propose a data-driven Fourier-trained neural-network method for estimating fixed-horizon probability densities from empirical characteristi"
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-09-08T16:54:03+00:00",
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
    "id": "hn:49625461",
    "domain": "金融",
    "title": "Teen reading slumps to worst this century due to surge in screen time",
    "url": "https://finance.yahoo.com/news/teen-reading-slumps-worst-century-111013754.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-09-09T12:29:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49439296",
    "domain": "金融",
    "title": "A brief history of federal lift ticket regulation",
    "url": "https://zakpodmore.substack.com/p/a-brief-history-of-federal-lift-ticket",
    "source": "CGMthrowaway",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-08-25T19:25:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-09-04T13:15:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49514224",
    "domain": "金融",
    "title": "Monero Inflation Checker – FCMP++",
    "url": "https://www.reddit.com/r/Monero/comments/1w3hcos/monero_inflation_checker_fcmp/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-31T20:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-25T11:27:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548497",
    "domain": "金融",
    "title": "Mark Cuban: Why US hospitals \"don't know their costs\"",
    "url": "https://www.beckershospitalreview.com/finance/mark-cuban-why-us-hospitals-dont-know-their-costs/",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-09-03T11:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49515596",
    "domain": "金融",
    "title": "Congress to vote on denying federal funding to universities that boycott Israel",
    "url": "https://twitter.com/dylanotes/status/2094229210889965634",
    "source": "slowin",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-31T22:24:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49396088",
    "domain": "金融",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:49348573",
    "domain": "金融",
    "title": "Trump 2.0 has deleted or altered nearly 400 US datasets",
    "url": "https://www.theguardian.com/us-news/ng-interactive/2026/aug/18/trump-federal-data-deleted-altered",
    "source": "_djo_",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-18T16:51:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49444266",
    "domain": "金融",
    "title": "Running out of money': Kraft, McDonald's, Whirlpool CEOs flag consumer concern",
    "url": "https://finance.yahoo.com/economy/articles/running-money-kraft-mcdonald-whirlpool-114500035.html",
    "source": "MrJagil",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-26T05:14:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49441647",
    "domain": "金融",
    "title": "Complete list of U.S. products subject to counter tariffs",
    "url": "https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs/complete-list-us-products-subject-to-counter-tariffs.html",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-25T22:38:07+00:00",
    "summary": ""
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
  }
]
```
