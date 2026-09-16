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

- 今日日期：`2026-09-16`
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
  "date": "2026-09-16",
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
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1935411,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1869434,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1297238,
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
    "points": 1224068,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1p4pezGEWb",
    "domain": "AI",
    "title": "【合集】AI Agent入门到精通：agent智能体从 prompt 到 harness，从理论到企业级实战！agent开发 | agent智能体搭建",
    "url": "http://www.bilibili.com/video/av115223839114449",
    "source": "AI大模型基地",
    "platform": "bilibili",
    "points": 1006199,
    "published_at": "2025-09-18T06:21:37+00:00",
    "summary": "AI Agent 从入门到源码实战全系列！从评估指标、Harness 架构、Agent 三阶段，到手撸智能体、Claude Code 拆解、企业级 RAG/LoRA 实战、Langmanus 源码项目，帮你系统掌握 AI Agent 开发全栈技能，解决落地痛点，吃透底层原理。\nP1：如何评估 agent 项目？就看这 5 大类 30 个指标\nP2：一文读懂 Harness：架构、功能与落地场景全解"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 873470,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 865723,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 805750,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "AI Agent这两年大家都听麻了，但真到上手，claude、codex这些又是注册、又是命令行，人还没踏进Agent大门，就先被劝退了。这期视频我用0门槛的国产Agent——字节旗下的TraeWork，用六个超真实的案例，手把手带你玩转Agent！完整的文字教程和GitHub神级Skill清单，打包放置顶评论了。教程制作不易，觉得有一点点帮助的话，记得一键三连～"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 776419,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 678775,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 673553,
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
    "points": 589062,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 442718,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 391986,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 354533,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 352635,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 335829,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 315855,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1cofCBgESQ",
    "domain": "AI",
    "title": "3天赚1200刀？纯聊天就能捏出个能搞钱的 AI Agent！【教程】",
    "url": "http://www.bilibili.com/video/av116123517329389",
    "source": "Xuan_酱",
    "platform": "bilibili",
    "points": 310220,
    "published_at": "2026-02-24T03:48:52+00:00",
    "summary": "用MuleRun靠动嘴就搓了一个 每日AI 资讯自动抓取的 Agent～"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 283675,
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
    "points": 261968,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV14JEj6uEdG",
    "domain": "AI",
    "title": "国内爽用 Claude Code + Codex，2分钟搞定！",
    "url": "http://www.bilibili.com/video/av116718420629331",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 254344,
    "published_at": "2026-06-09T05:12:06+00:00",
    "summary": "2 分钟，教你国内爽用 Claude Code + Codex，保姆级教程，还能省掉上百块订阅费。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n核心是使用 CC Switch 开源工具，让国内用户也能使用 Claude Code 和 Codex 这两款先进的 AI 编程工具，手把手带你配置接入 DeepS"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 198688,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1i9Z8YhEja",
    "domain": "AI",
    "title": "学 AI，看这个视频就够了！最全程序员 AI 指南：AI核心概念、实用AI工具、AI编程技巧、AI开发技术",
    "url": "http://www.bilibili.com/video/av114262957626976",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 193283,
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
    "points": 181429,
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
    "points": 175994,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 142101,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV1PgCmY9EKu",
    "domain": "AI",
    "title": "Cursor教程：实现自动化写文章，让AI 7*24小时为你打工｜ChatGPT｜AI进化论-花生",
    "url": "http://www.bilibili.com/video/av113328902905646",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 134641,
    "published_at": "2024-10-18T14:35:55+00:00",
    "summary": "👏 欢迎加入我的知识星球「AI编程：从入门到精通」：https://t.zsxq.com/BFTPI\n🤖 OpenAI API充值入口：https://platform.openai.com/settings/organization/billing/overview\n\n这期视频主要是像你介绍如何使用Cursor写自动化脚本，实现让ChatGPT为你自动化写作的目的。以小红书读书博主为例，演示了使"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 117262,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 99857,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93712,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1oTkuBoEW5",
    "domain": "AI",
    "title": "业余程序员才Vibe Coding",
    "url": "http://www.bilibili.com/video/av115921586751411",
    "source": "晓舟报告",
    "platform": "bilibili",
    "points": 75279,
    "published_at": "2026-01-21T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 72618,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 48461,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48114,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47695,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 46310,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39887,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1EfY76YEwp",
    "domain": "AI",
    "title": "14k Star Claude Code 开源桌面端，能自动操作电脑了！",
    "url": "http://www.bilibili.com/video/av117251936293145",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 39261,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35245,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30657,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29750,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28937,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 27768,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22782,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 22204,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1Nu3M6bEXE",
    "domain": "AI",
    "title": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了",
    "url": "http://www.bilibili.com/video/av116979859984479",
    "source": "Agent开发教程",
    "platform": "bilibili",
    "points": 20102,
    "published_at": "2026-07-25T09:34:49+00:00",
    "summary": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了，草履虫都能学会！"
  },
  {
    "id": "bvid:BV1ofSSBfEC1",
    "domain": "AI",
    "title": "小白也会的trae里安装 claude code 教程",
    "url": "http://www.bilibili.com/video/av116352710870207",
    "source": "长留-AIGC",
    "platform": "bilibili",
    "points": 18954,
    "published_at": "2026-04-05T15:08:17+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Pxb569ELE",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的AI Agent智能体搭建+私有知识库全套零基础入门教程,全程干货无废话，让你少走99%的弯路，100%提效，零基础小白也能学",
    "url": "http://www.bilibili.com/video/av117234806692643",
    "source": "AI智能应用",
    "platform": "bilibili",
    "points": 14588,
    "published_at": "2026-09-08T09:59:54+00:00",
    "summary": "【2026最新】目前B站最全最细的AI Agent智能体搭建+私有知识库全套零基础入门教程,全程干货无废话，让你少走99%的弯路，100%提效，零基础小白也能学会~"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 13894,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 581,
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
    "points": 137,
    "published_at": "2026-09-13T10:29:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/pasqal-nasdaq-debut-meets-a-risk-reckoning/",
    "domain": "AI 算力 / 半导体",
    "title": "Pasqal’s Nasdaq Debut Meets a Risk Reckoning",
    "url": "https://www.eetimes.com/pasqal-nasdaq-debut-meets-a-risk-reckoning/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T08:03:27+00:00",
    "summary": "A sharp share price drop exposes the challenge of valuing quantum companies before commercial demand is proven. The post Pasqal’s Nasdaq Debut Meets a Risk Reckoning appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/aircraft-actuator-electrification-redefines-system-level-architecture/",
    "domain": "AI 算力 / 半导体",
    "title": "Aircraft Actuator Electrification Redefines System-Level Architecture",
    "url": "https://www.eetimes.com/aircraft-actuator-electrification-redefines-system-level-architecture/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T19:00:00+00:00",
    "summary": "The transition from hydraulic to electric-motor aircraft actuators also encompasses many system-level issues and opportunities. The post Aircraft Actuator Electrification Redefines System-Level Archit"
  },
  {
    "id": "rss:https://www.eetimes.com/reduce-risk-cut-costs-and-speed-time-to-market-with-certified-wifi-ble-modules/",
    "domain": "AI 算力 / 半导体",
    "title": "Reduce Risk, Cut Costs, and Speed Time-to-Market with Certified WiFi & BLE Modules",
    "url": "https://www.eetimes.com/reduce-risk-cut-costs-and-speed-time-to-market-with-certified-wifi-ble-modules/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T17:23:09+00:00",
    "summary": "Join this webinar and learn how a certified WiFi and BLE combination module can simplify your next connected device design. The post Reduce Risk, Cut Costs, and Speed Time-to-Market with Certified WiF"
  },
  {
    "id": "rss:https://www.eetimes.com/empowering-the-future-of-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "Empowering the Future of Robotics",
    "url": "https://www.eetimes.com/empowering-the-future-of-robotics/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:00:07+00:00",
    "summary": "See how autonomous mobile robots are transforming manufacturing, warehousing, and logistics. Explore the technologies driving smarter navigation, safer operations, and greater automation. The post Emp"
  },
  {
    "id": "rss:https://www.eetimes.com/leo-satellites/",
    "domain": "AI 算力 / 半导体",
    "title": "Designing Passive Components for LEO Satellite Systems",
    "url": "https://www.eetimes.com/leo-satellites/",
    "source": "YAGEO Group",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:00:00+00:00",
    "summary": "Selecting passive components for LEO satellite systems is becoming increasingly complex as spacecraft architectures evolve and constellation deployments scale. Engineers must determine when commercial"
  },
  {
    "id": "rss:https://www.eetimes.com/fcc-rule-on-optical-connectivity-could-slow-ai-race/",
    "domain": "AI 算力 / 半导体",
    "title": "FCC Rule on Optical Connectivity Could Slow AI Race",
    "url": "https://www.eetimes.com/fcc-rule-on-optical-connectivity-could-slow-ai-race/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T12:32:10+00:00",
    "summary": "Escalating tech war between the U.S. and China and a potential FCC ban on importing optical network equipment could force hyperscalers to navigate critical shortages. The post FCC Rule on Optical Conn"
  },
  {
    "id": "rss:https://www.eetimes.com/how-10base-t1s-powers-zonal-architectures-and-sdv-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "How 10BASE‑T1S Powers Zonal Architectures and SDV Innovation",
    "url": "https://www.eetimes.com/how-10base-t1s-powers-zonal-architectures-and-sdv-innovation/",
    "source": "onsemi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:04:49+00:00",
    "summary": "Join this webinar and learn more about how 10BASE‑T1S replaces low speed legacy buses with deterministic, collision free Ethernet. The post How 10BASE‑T1S Powers Zonal Architectures and SDV Innovation"
  },
  {
    "id": "rss:https://www.eetimes.com/india-hardens-its-cyber-defenses/",
    "domain": "AI 算力 / 半导体",
    "title": "India Hardens Its Cyber Defenses",
    "url": "https://www.eetimes.com/india-hardens-its-cyber-defenses/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T07:11:27+00:00",
    "summary": "As cyberthreats target critical infrastructure, and India’s online population tops 1 billion, digital resilience is now a national security priority. The post India Hardens Its Cyber Defenses appeared"
  },
  {
    "id": "rss:https://www.eetimes.com/digital-keys-and-radio-technology-in-smart-buildings/",
    "domain": "AI 算力 / 半导体",
    "title": "Digital Keys and Radio Technology in Smart Buildings",
    "url": "https://www.eetimes.com/digital-keys-and-radio-technology-in-smart-buildings/",
    "source": "Nick Wood",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:12:56+00:00",
    "summary": "The direction of travel seems clear enough: Digital keys are likely to replace physical ones entirely over time. The post Digital Keys and Radio Technology in Smart Buildings appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/ambient-iot-from-battery-free-promise-to-mass-market-reality/",
    "domain": "AI 算力 / 半导体",
    "title": "Ambient IoT: From Battery-Free Promise to Mass-Market Reality",
    "url": "https://www.eetimes.com/ambient-iot-from-battery-free-promise-to-mass-market-reality/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T12:26:58+00:00",
    "summary": "Surging investment, maturing tech, and emerging standards are pushing ambient IoT toward mainstream deployment. The post Ambient IoT: From Battery-Free Promise to Mass-Market Reality appeared first on"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-leaders-clash-over-safety-fears-after-anthropic-whistleblower-says-ai-could-kill-us-all-by-2030-openai-anthropic-and-xai-figureheads-call-for-external-governance-while-jensen-huang-says-worries-are-made-up",
    "domain": "AI 算力 / 半导体",
    "title": "AI leaders clash over safety fears after Anthropic whistleblower says AI could 'kill us all' by 2030 — OpenAI, Anthropic and xAI figureheads call for external governance, while Jensen Huang says worri",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-leaders-clash-over-safety-fears-after-anthropic-whistleblower-says-ai-could-kill-us-all-by-2030-openai-anthropic-and-xai-figureheads-call-for-external-governance-while-jensen-huang-says-worries-are-made-up",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T17:19:36+00:00",
    "summary": "The CEOs of OpenAI and Anthropic, as well as other industry leaders, are calling for a general slowdown in AI development over safety fears. On the flip side, Chinese authorities, the U.S. President, "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/asus-ludicrous-20th-anniversary-bundle-is-now-the-cheapest-way-to-buy-an-rtx-5090-nvidias-flagship-gpu-stock-is-so-limited-that-this-usd10-850-bundle-with-a-3000w-psu-x870e-board-and-open-frame-case-is-actually-cheaper-than-some-scalper-listings",
    "domain": "AI 算力 / 半导体",
    "title": "Asus' ludicrous $10,850 20th-anniversary bundle is now the cheapest way to buy an RTX 5090 — Nvidia's flagship GPU stock is so limited that this bundle with a 3000W PSU, X870E board, and open-frame ca",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/asus-ludicrous-20th-anniversary-bundle-is-now-the-cheapest-way-to-buy-an-rtx-5090-nvidias-flagship-gpu-stock-is-so-limited-that-this-usd10-850-bundle-with-a-3000w-psu-x870e-board-and-open-frame-case-is-actually-cheaper-than-some-scalper-listings",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T15:13:16+00:00",
    "summary": "This ultra-premium Asus ROG Edition 20th Anniversary Combo set at Newegg is super expensive at $10,849.96, but ironically, it's the 'cheapest' way to pick up an RTX 5090 right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-reportedly-cans-12xe-option-for-nova-lake-s-desktop-gaming-apu-design-said-to-resurface-with-razor-lake",
    "domain": "AI 算力 / 半导体",
    "title": "Intel reportedly cans 12Xe option for Nova Lake-S desktop — gaming APU design said to resurface with Razor Lake",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-reportedly-cans-12xe-option-for-nova-lake-s-desktop-gaming-apu-design-said-to-resurface-with-razor-lake",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:17:06+00:00",
    "summary": "Following rumors of a Nova Lake desktop SKU with 12 Xe3P cores, tipster Jaykihn suggests that Intel has canned the design and moved the target to next-gen Razor Lake instead."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-ai-data-centers-projected-to-become-the-fifth-largest-natural-gas-consumer-in-the-world-by-2035-consumption-to-grow-by-15-billion-cubic-feet-per-day-as-demand-for-compute-increases",
    "domain": "AI 算力 / 半导体",
    "title": "US AI data centers projected to become the fifth-largest natural gas consumer in the world by 2035 — consumption to grow by 15 billion cubic feet per day as demand for compute increases",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-ai-data-centers-projected-to-become-the-fifth-largest-natural-gas-consumer-in-the-world-by-2035-consumption-to-grow-by-15-billion-cubic-feet-per-day-as-demand-for-compute-increases",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T13:57:36+00:00",
    "summary": "Data centers in the U.S. are projected to use up more natural gas than most of the rest of the world to generate the electricity they need. Estimates suggest that 15 billion cubic feet per day are nee"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/bill-gates-compares-ai-to-alien-intelligence-in-movies-where-magically-the-us-and-china-solves-the-problem-together-warns-world-governments-that-theyre-not-ready-for-ai",
    "domain": "AI 算力 / 半导体",
    "title": "Bill Gates compares AI to alien intelligence in movies where ‘magically the US and China’ solve the problem together — warns world governments that they’re not ready for AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/bill-gates-compares-ai-to-alien-intelligence-in-movies-where-magically-the-us-and-china-solves-the-problem-together-warns-world-governments-that-theyre-not-ready-for-ai",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T12:52:53+00:00",
    "summary": "The billionaire philanthropist says that governments across the world need to work together to ensure that the people are ready for upcoming upheaval brought about by AI. He even compared the technolo"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-transcripts-are-reportedly-read-by-humans-to-improve-responses-including-those-with-personal-information-project-lilly-has-seen-openai-hire-hundreds-of-contractors-to-manually-review-logs",
    "domain": "AI 算力 / 半导体",
    "title": "ChatGPT transcripts are reportedly read by humans to improve responses, including those with personal information — 'Project Lilly' has seen OpenAI hire hundreds of contractors to manually review logs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-transcripts-are-reportedly-read-by-humans-to-improve-responses-including-those-with-personal-information-project-lilly-has-seen-openai-hire-hundreds-of-contractors-to-manually-review-logs",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T11:30:00+00:00",
    "summary": "404 Media reports that OpenAI has hired hundreds of contractors to evaluate ChatGPT responses manually."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-september-2026-update-brings-many-long-requested-features-but-also-surfaces-fresh-bugs-windows-11-update-causes-crashes-on-amd-graphics-explorer-hang-ups-and-broken-third-party-integrations",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft rolls out emergency update for Windows 11's latest patch — recent update causes crashes on AMD graphics, Explorer hang-ups, and broken third-party integrations",
    "url": "https://www.tomshardware.com/software/windows/windows-september-2026-update-brings-many-long-requested-features-but-also-surfaces-fresh-bugs-windows-11-update-causes-crashes-on-amd-graphics-explorer-hang-ups-and-broken-third-party-integrations",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T11:00:00+00:00",
    "summary": "Windows September 2026 update brings many long-requested features, but also surfaces fresh bugs — new code crashing AMD, HP, and Lenovo systems and surfaces audio, Explorer, and Remote Desktop problem"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-a-usd560-saving-on-this-1440p-ready-gaming-pc-with-a-9800x3d-and-rtx-5060-ti-16gb-now-usd1-859-all-white-cyberpowerpc-desktop-ships-with-one-of-amds-best-x3d-chips-along-with-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a $560 saving on this 1440p-ready gaming PC with a 9800X3D and RTX 5060 Ti 16GB, now $1,859 — all-white CyberPowerPC desktop ships with one of AMD's best X3D chips, along with 32GB DDR5 and a 2TB",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-a-usd560-saving-on-this-1440p-ready-gaming-pc-with-a-9800x3d-and-rtx-5060-ti-16gb-now-usd1-859-all-white-cyberpowerpc-desktop-ships-with-one-of-amds-best-x3d-chips-along-with-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:36:40+00:00",
    "summary": "Save nearly $600 on this CyberPowerPC gaming PC with a 9800X3D, RTX 5060 Ti 16GB, 32GB DDR5, and a 2TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/minecraft-legacy-gets-re-written-in-c-for-ps2-and-wii-ports-code-is-tuned-so-it-works-well-even-on-the-ps2s-meager-32mb-of-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Minecraft Legacy gets rewritten in C++ for PS2 and Wii ports — code is tuned so it works well even on the PS2’s meager 32MB of RAM",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/minecraft-legacy-gets-re-written-in-c-for-ps2-and-wii-ports-code-is-tuned-so-it-works-well-even-on-the-ps2s-meager-32mb-of-ram",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:30:00+00:00",
    "summary": "Games optimization specialist OptiProjects (AKA OptiJeugos) has released a new port of Minecraft Legacy for the Sony PlayStation 2 and Nintendo Wii consoles."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/developer-builds-viral-3d-source-code-visualizer-that-consumes-21gb-of-ram-flies-around-2-5-million-lines-of-code-at-over-120-frames-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "Developer builds viral 3D source code visualizer that consumes 21GB of RAM — flies around 2.5 million lines of code at over 120 frames per second",
    "url": "https://www.tomshardware.com/tech-industry/developer-builds-viral-3d-source-code-visualizer-that-consumes-21gb-of-ram-flies-around-2-5-million-lines-of-code-at-over-120-frames-per-second",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:00:00+00:00",
    "summary": "A developer has built a 3D code visualizer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-radeon-rx-9070-gre-graphics-card-returns-to-its-lowest-ever-price-of-usd499-rare-deal-places-this-current-generation-12gb-gpu-below-its-msrp-launch-price",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's Radeon RX 9070 GRE graphics card returns to its lowest-ever price of $499 — rare deal places this current-generation 12GB GPU below its MSRP launch price",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-radeon-rx-9070-gre-graphics-card-returns-to-its-lowest-ever-price-of-usd499-rare-deal-places-this-current-generation-12gb-gpu-below-its-msrp-launch-price",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T09:50:21+00:00",
    "summary": "Grab a new 12GB GPU for less than the MSRP launch price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/perplexitys-local-ai-agent-comes-to-windows-but-only-for-rtx-gpus-with-at-least-24gb-of-vram-portable-computer-brings-ai-for-multistep-tasks-to-compatible-pcs",
    "domain": "AI 算力 / 半导体",
    "title": "Perplexity’s local AI agent comes to Windows, but only for RTX GPUs with at least 24GB of VRAM — Portable Computer brings AI for multistep tasks to compatible PCs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/perplexitys-local-ai-agent-comes-to-windows-but-only-for-rtx-gpus-with-at-least-24gb-of-vram-portable-computer-brings-ai-for-multistep-tasks-to-compatible-pcs",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T09:24:32+00:00",
    "summary": "Perplexity and Nvidia released Portable Computer for Windows on Sept. 14, bringing the local-first AI agent to GeForce RTX and RTX PRO GPUs with 24GB or more of VRAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-ai-can-boost-u-s-gdp-by-32-percent-up-to-usd44-4-trillion-in-four-years-economics-model-predicts-that-displaced-employees-may-have-to-switch-to-jobs-like-electrician-and-nurse",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic says AI can boost U.S. GDP by 32%, up to $44.4 trillion in four years — economics model predicts that displaced employees 'may have to switch to jobs like electrician and nurse'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-ai-can-boost-u-s-gdp-by-32-percent-up-to-usd44-4-trillion-in-four-years-economics-model-predicts-that-displaced-employees-may-have-to-switch-to-jobs-like-electrician-and-nurse",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T18:50:36+00:00",
    "summary": "Anthropic has published a paper wherein it envisions a future for the economy where AI is deeply ingrained. In the most extreme scenarios, U.S. GDP is up, but unemployment simmers as others are put ou"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's RTX 5090 vanishes from online retail in the US — third-party sellers now demand as much as $9,500 for Nvidia's fastest GPU",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:41:01+00:00",
    "summary": "The RTX 5090 is out of stock from first-party sellers online in the U.S., with third-party sellers now asking for as much as $9,500 for the GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/gaming-takes-a-backseat-as-nvidia-overhauls-the-rtx-5090-for-maximum-ai-margins-rtx-pro-5500-delivers-2-6x-vram-at-matching-specs",
    "domain": "AI 算力 / 半导体",
    "title": "Gaming takes a backseat as Nvidia overhauls the RTX 5090 for maximum AI margins — RTX Pro 5500 delivers 2.6X VRAM at matching specs",
    "url": "https://www.tomshardware.com/pc-components/gpus/gaming-takes-a-backseat-as-nvidia-overhauls-the-rtx-5090-for-maximum-ai-margins-rtx-pro-5500-delivers-2-6x-vram-at-matching-specs",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:39:09+00:00",
    "summary": "Nvidia launches the RTX Pro 5500 Blackwell Workstation Edition graphics card for agentic and generative AI."
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/valve-engineers-discuss-the-duality-of-the-steam-frame-and-pricing-valves-newest-vr-headset-pivots-steamos-to-arm",
    "domain": "AI 算力 / 半导体",
    "title": "Valve engineers discuss the duality of the Steam Frame and pricing — Valve's newest VR headset pivots SteamOS to Arm",
    "url": "https://www.tomshardware.com/virtual-reality/valve-engineers-discuss-the-duality-of-the-steam-frame-and-pricing-valves-newest-vr-headset-pivots-steamos-to-arm",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:30:00+00:00",
    "summary": "We chatted with Valve engineers Pierre-Loup Griffais and Jeff Leinbaugh about the Steam Frame launch, why the company is taking a two-pronged strategy with streaming and standalone support, and how th"
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/valve-steam-frame-interview-why-it-costs-up-to-usd1-300-snapdragon-power-and-10x-foveated-streaming",
    "domain": "AI 算力 / 半导体",
    "title": "Valve Steam Frame interview — why it costs up to $1,300, Snapdragon power, and 10x foveated streaming",
    "url": "https://www.tomshardware.com/virtual-reality/valve-steam-frame-interview-why-it-costs-up-to-usd1-300-snapdragon-power-and-10x-foveated-streaming",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:28:23+00:00",
    "summary": "We chatted with Valve engineers Pierre-Loup Griffais and Jeff Leinbaugh about launching the Steam Frame amid a global memory/storage supply crunch"
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/valve-steam-frame-review",
    "domain": "AI 算力 / 半导体",
    "title": "Valve Steam Frame Review: Competent as a standalone VR, but wireless streaming remains the focus",
    "url": "https://www.tomshardware.com/virtual-reality/valve-steam-frame-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:00:00+00:00",
    "summary": "All dressed up and nowhere to go sums up the Meta Quest 3."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-palantir-and-others-restrict-advanced-ai-model-usage-over-privacy-concerns-report-claims-paranoia-rising-over-customer-intellectual-property",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Palantir, and others restrict advanced AI model usage over privacy concerns, report claims — 'paranoia' rising over customer intellectual property",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-palantir-and-others-restrict-advanced-ai-model-usage-over-privacy-concerns-report-claims-paranoia-rising-over-customer-intellectual-property",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T15:58:32+00:00",
    "summary": "Companies are concerned that their intellectual property may be used by Anthropic and OpenAI to help improve their AI models."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/solo-developer-wires-zluda-to-amds-hip-getting-multiple-cuda-libraries-running-on-a-radeon-rx-9060-xt-in-windows-cuda-exclusive-workloads-on-amd-hardware-in-windows-is-possible-without-virtualization-or-dual-booting",
    "domain": "AI 算力 / 半导体",
    "title": "Solo dev enables running CUDA on AMD hardware in Windows, getting multiple CUDA libraries running on a gaming Radeon RX 9060 XT GPU in Windows — CUDA-exclusive workloads on AMD hardware in Windows pos",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/solo-developer-wires-zluda-to-amds-hip-getting-multiple-cuda-libraries-running-on-a-radeon-rx-9060-xt-in-windows-cuda-exclusive-workloads-on-amd-hardware-in-windows-is-possible-without-virtualization-or-dual-booting",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T14:23:12+00:00",
    "summary": "A developer has wired up the ZLUDA project to AMD's HIP libraries for Windows, putting a small but signifcant bridge over NVIDIA's CUDA moat."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/need-for-speed-underground-2-now-runs-directly-on-nintendo-switch-other-classic-windows-titles-playable-thanks-to-custom-firmware-boot",
    "domain": "AI 算力 / 半导体",
    "title": "Need for Speed Underground 2 now runs directly on Nintendo Switch — other Classic Windows titles playable thanks to custom firmware boot",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/need-for-speed-underground-2-now-runs-directly-on-nintendo-switch-other-classic-windows-titles-playable-thanks-to-custom-firmware-boot",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T13:36:24+00:00",
    "summary": "Retro gaming fans who own Nintendo Switch consoles now have several classic Windows titles they can now enjoy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/micron-offers-taiwan-employees-usd31-650-cash-bonus-as-unions-threaten-strike-over-ai-windfall-workers-reject-record-payout-package-demand-15-percent-profit-sharing-plan",
    "domain": "AI 算力 / 半导体",
    "title": "Micron offers Taiwan employees $31,650 cash bonus as unions threaten strike over AI windfall — workers reject record payout package, demand 15% profit-sharing plan",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/micron-offers-taiwan-employees-usd31-650-cash-bonus-as-unions-threaten-strike-over-ai-windfall-workers-reject-record-payout-package-demand-15-percent-profit-sharing-plan",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T12:00:00+00:00",
    "summary": "Micron is offering Taiwan employees a NT$1 million cash bonus, but unions have rejected the package and are demanding permanent profit sharing as strike talks continue."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/proven-8-pin-pcie-plugs-arent-immune-to-melting-thermal-grizzly-wireview-adapter-burns-out-on-radeon-rx-7900-xtx",
    "domain": "AI 算力 / 半导体",
    "title": "Proven 8-pin PCIe plugs aren't immune to melting — Thermal Grizzly WireView adapter burns out on Radeon RX 7900 XTX",
    "url": "https://www.tomshardware.com/pc-components/gpus/proven-8-pin-pcie-plugs-arent-immune-to-melting-thermal-grizzly-wireview-adapter-burns-out-on-radeon-rx-7900-xtx",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:30:00+00:00",
    "summary": "Three 8-pin connectors on a Thermal Grizzly WireView reportedly suffered burning and melting while connected to a Radeon RX 7900 XTX, with the company now investigating what caused the failure."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/meta-quest-user-vibe-codes-3d-object-throwing-to-3d-printer-ive-never-felt-more-like-tony-stark-says-the-software-engineer",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Quest user vibe-codes 3D object throwing to 3D printer — ‘I've never felt more like Tony Stark’ says the software engineer",
    "url": "https://www.tomshardware.com/3d-printing/meta-quest-user-vibe-codes-3d-object-throwing-to-3d-printer-ive-never-felt-more-like-tony-stark-says-the-software-engineer",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:17:30+00:00",
    "summary": "A software engineer has shown off a futuristic Meta Quest plus 3D printer workflow where models are 'thrown' to the output device."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd1-289-when-you-build-an-extreme-pc-with-these-top-tier-components-combo-deal-features-amds-ryzen-9-9950x3d2-processor-along-with-an-8tb-9100-pro-ssd-msi-x870e-motherboard-and-32gb-of-ddr5-6000-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1,289 when you build an extreme PC with these top-tier components — combo deal features AMD's Ryzen 9 9950X3D2 processor along with an 8TB 9100 Pro SSD, MSI X870E motherboard, and 32GB of DDR5-6",
    "url": "https://www.tomshardware.com/pc-components/save-usd1-289-when-you-build-an-extreme-pc-with-these-top-tier-components-combo-deal-features-amds-ryzen-9-9950x3d2-processor-along-with-an-8tb-9100-pro-ssd-msi-x870e-motherboard-and-32gb-of-ddr5-6000-memory",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:10:03+00:00",
    "summary": "Save $1,289 on Newegg's epic component bundle, which features AMD's top processor, a massive 8TB Samsung 9100 Pro SSD, and 32GB of DDR5 memory"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg27ucwm-27-inch-4k-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Swift PG27UCWM gaming monitor review: Speed and pixel density in a premium package",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg27ucwm-27-inch-4k-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:05:00+00:00",
    "summary": "Asus’ latest ROG Swift display is the PG27UCWM, a 27-inch 4K OLED panel with Tandem RGB Stripe technology, advanced cooling, 240 Hz, 480 Hz in FHD resolution, Adaptive-Sync, HDR400, HDR10, Dolby Visio"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/russian-freelancers-use-claude-to-program-autonomous-combat-drone-swarm-ai-enabled-target-selection-and-detonation-without-a-human-in-the-loop",
    "domain": "AI 算力 / 半导体",
    "title": "Russian freelancers use Claude to program autonomous combat drone swarm — AI-enabled target selection and detonation without a human in the loop",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/russian-freelancers-use-claude-to-program-autonomous-combat-drone-swarm-ai-enabled-target-selection-and-detonation-without-a-human-in-the-loop",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:00:00+00:00",
    "summary": "Russia turned Claude into a tool for weapons development, espionage, and propaganda, Anthropic's new threat report claims."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/maryland-data-center-developers-offer-residents-biggest-ever-us-community-benefits-package-as-big-tech-seeks-to-quell-fears-usd110-million-deal-includes-usd30-million-elementary-school-water-reclamation-system-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Maryland data center developers offer residents biggest-ever US community benefits package as big tech seeks to quell fears — $110 million deal includes $30 million elementary school, water reclamatio",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/maryland-data-center-developers-offer-residents-biggest-ever-us-community-benefits-package-as-big-tech-seeks-to-quell-fears-usd110-million-deal-includes-usd30-million-elementary-school-water-reclamation-system-and-more",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T10:32:00+00:00",
    "summary": "A new report claims AI data center builders are getting more savvy about offering communities tangible benefits to get their projects approved."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/modders-halve-fsr-4-render-times-on-amds-ps5-derived-bc-250-mining-apu-portable-fidelityfx-dll-cuts-1440p-upscaling-time-from-11-51-ms-to-5-92-ms",
    "domain": "AI 算力 / 半导体",
    "title": "Modders halve FSR 4 render times on AMD’s PS5-derived BC-250 mining APU — portable FidelityFX DLL cuts 1440p upscaling time from 11.51 ms to 5.92 ms",
    "url": "https://www.tomshardware.com/pc-components/modders-halve-fsr-4-render-times-on-amds-ps5-derived-bc-250-mining-apu-portable-fidelityfx-dll-cuts-1440p-upscaling-time-from-11-51-ms-to-5-92-ms",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T10:30:00+00:00",
    "summary": "Modders have nearly halved FSR 4 processing time on AMD’s PS5-derived BC-250, using a portable FidelityFX DLL that cuts 1440p upscaling cost to 5.92 ms."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/dumpster-diver-builds-home-lab-proxmox-server-from-weekly-landfill-runs-for-ssds-hdds-gpus-and-even-ram-weekly-e-waste-raids-net-multi-drive-proxmox-server-and-asus-rog-laptop",
    "domain": "AI 算力 / 半导体",
    "title": "Dumpster diver builds home lab Proxmox server from weekly landfill runs for SSDs, HDDs, GPUs, and even RAM — weekly e-waste raids net multi-drive Proxmox server and Asus ROG laptop",
    "url": "https://www.tomshardware.com/desktops/pc-building/dumpster-diver-builds-home-lab-proxmox-server-from-weekly-landfill-runs-for-ssds-hdds-gpus-and-even-ram-weekly-e-waste-raids-net-multi-drive-proxmox-server-and-asus-rog-laptop",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T10:00:00+00:00",
    "summary": "A tech enthusiast says that they managed to put together a home lab-worthy Proxmox server using PC parts scavenged from the nearby county landfill."
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
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 394,
    "published_at": "2026-09-15T17:38:18+00:00",
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
    "id": "hn:49704226",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: iOS 27 does not allow Apple Intelligence to be disabled",
    "url": "https://news.ycombinator.com/item?id=49704226",
    "source": "nunez",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T21:21:58+00:00",
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
    "id": "hn:49706941",
    "domain": "大厂 AI 动态",
    "title": "I worked at Google DeepMind. You should listen to the warnings about AI",
    "url": "https://www.theguardian.com/technology/2026/sep/14/google-deepmind-ai-warnings",
    "source": "gibspaulding",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-09-15T02:25:41+00:00",
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
    "id": "hn:49706481",
    "domain": "大厂 AI 动态",
    "title": "Microsoft removes the COPILOT function from Excel",
    "url": "https://support.microsoft.com/en-us/excel/functions/copilot-function",
    "source": "fourfire",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-15T01:10:41+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/995826/boox-palma-3-e-ink-reader-pocket-smartphone-android-16",
    "domain": "大厂 AI 动态",
    "title": "The Boox Palma 3 gets stylus support and a sleek redesign",
    "url": "https://www.theverge.com/tech/995826/boox-palma-3-e-ink-reader-pocket-smartphone-android-16",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T02:00:00+00:00",
    "summary": "Nearly two years after the last update to Boox's smartphone-sized black-and-white e-reader, the company announced the Palma 3 with a sleek redesign, new functionality, and a handful of other small upd"
  },
  {
    "id": "rss:https://www.theverge.com/tech/995430/canon-eos-r8-mark-11-full-frame-digital-camera-pricing-availability",
    "domain": "大厂 AI 动态",
    "title": "The EOS R8 Mark II is Canon’s lightest full-frame camera with stabilization",
    "url": "https://www.theverge.com/tech/995430/canon-eos-r8-mark-11-full-frame-digital-camera-pricing-availability",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T01:00:00+00:00",
    "summary": "Canon announced the second-generation of its EOS R8 with a new retro-inspired redesign and the addition of in-body stabilization. That feature was one of the most notable omissions from the original R"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/995917/data-center-nyt-midterm-poll-september",
    "domain": "大厂 AI 动态",
    "title": "AI and data centers are incredibly unpopular in every poll",
    "url": "https://www.theverge.com/ai-artificial-intelligence/995917/data-center-nyt-midterm-poll-september",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T23:34:25+00:00",
    "summary": "Poll data released Tuesday by the New York Times and Siena University confirms what we've already been seeing, and what politicians are responding to - AI and data centers are incredibly unpopular. As"
  },
  {
    "id": "rss:https://www.theverge.com/news/994714/microsoft-windows-surface-event-october-7-san-francisco",
    "domain": "大厂 AI 动态",
    "title": "Microsoft announces Windows and Surface event for October 7th",
    "url": "https://www.theverge.com/news/994714/microsoft-windows-surface-event-october-7-san-francisco",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T20:36:59+00:00",
    "summary": "It's been more than two years since the last major Windows event, so Microsoft is heading to San Francisco next month to outline the future of Windows and Surface devices. At an event on October 7th, "
  },
  {
    "id": "rss:https://www.theverge.com/policy/995704/peter-gray-restoring-childhood-jonathan-haidt",
    "domain": "大厂 AI 动态",
    "title": "What if social media isn’t hurting kids?",
    "url": "https://www.theverge.com/policy/995704/peter-gray-restoring-childhood-jonathan-haidt",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T20:13:30+00:00",
    "summary": "Two years ago, social psychologist Jonathan Haidt released his New York Times bestseller The Anxious Generation. The book posits that the rise of social media and smartphone use is largely to blame fo"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/995608/kia-pv7-electric-van-specs-sale",
    "domain": "大厂 AI 动态",
    "title": "Kia’s electric van lineup is getting more interesting with reveal of PV7",
    "url": "https://www.theverge.com/transportation/995608/kia-pv7-electric-van-specs-sale",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T18:39:44+00:00",
    "summary": "You may not know it, but minivans are making a comeback in the US. Look around, and you'll start to notice an uptick in these breadboxes on wheels. Sales were up 21 percent in 2025, suggesting that th"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/995518/elegoo-3d-printer-switch-joy-con-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "One of the best 3D printers for beginners is almost $100 off",
    "url": "https://www.theverge.com/gadgets/995518/elegoo-3d-printer-switch-joy-con-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T18:02:30+00:00",
    "summary": "If the high price tag of premium 3D printers have kept you from exploring the hobby, this deal is a great entry point. Elegoo has its Centauri Carbon 2 Combo on sale for $369, almost $100 off its usua"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/995432/how-the-oregon-trail-became-a-generational-icon",
    "domain": "大厂 AI 动态",
    "title": "How The Oregon Trail became a generational icon",
    "url": "https://www.theverge.com/podcast/995432/how-the-oregon-trail-became-a-generational-icon",
    "source": "Travis Larchuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T16:18:10+00:00",
    "summary": "Whether you played it in the back of your classroom or on your computer at home, if you were a kid in the last 30 years you almost certainly grew up playing The Oregon Trail. On the season 5 premiere "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/995472/tiff-2026-vintage-violence-the-devils-gentle-monster",
    "domain": "大厂 AI 动态",
    "title": "Vintage Violence is an absurdist crime thriller for phone addicts",
    "url": "https://www.theverge.com/entertainment/995472/tiff-2026-vintage-violence-the-devils-gentle-monster",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T16:00:00+00:00",
    "summary": "There are a lot of movies that have tried to seamlessly integrate modern tech - text messages, livestreams, etc. - into their storytelling. Some of the most novel attempts have been in the genre space"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/995449/light-phone-uber-lyft-rideshare-app",
    "domain": "大厂 AI 动态",
    "title": "Now Light’s minimalist phone can easily call an Uber",
    "url": "https://www.theverge.com/gadgets/995449/light-phone-uber-lyft-rideshare-app",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T15:00:00+00:00",
    "summary": "More than a decade after its Kickstarter proposed a \"cell phone designed to be used as little as possible,\" Light is adding a direct connection to Uber and Lyft with a new Rideshare tool. For owners o"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/we-dont-need-ai-regulation-leave-safety-to-us-nvidias-jensen-huang-says/",
    "domain": "大厂 AI 动态",
    "title": "We don’t need AI regulation — leave safety to us, Nvidia’s Jensen Huang says",
    "url": "https://techcrunch.com/2026/09/15/we-dont-need-ai-regulation-leave-safety-to-us-nvidias-jensen-huang-says/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T00:20:39+00:00",
    "summary": "AI isn't some new form of \"alien mind,\" according to Jensen Huang. It's just hardware and software, so safety can be engineered by each AI product maker."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/the-ai-data-center-boom-is-colliding-with-cities-scarred-by-big-industry/",
    "domain": "大厂 AI 动态",
    "title": "The AI data center boom is colliding with cities scarred by big industry",
    "url": "https://techcrunch.com/2026/09/15/the-ai-data-center-boom-is-colliding-with-cities-scarred-by-big-industry/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T21:47:38+00:00",
    "summary": "National outcry against data center construction has spread to Philadelphia, where officials suggested possible construction in a neighborhood already impacted by a now-defunct oil refinery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/meta-now-lets-ai-agents-handle-the-boring-parts-of-whatsapp-business-setup/",
    "domain": "大厂 AI 动态",
    "title": "Meta now lets AI agents handle the boring parts of WhatsApp Business setup",
    "url": "https://techcrunch.com/2026/09/15/meta-now-lets-ai-agents-handle-the-boring-parts-of-whatsapp-business-setup/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T20:12:53+00:00",
    "summary": "A new WhatsApp Business MCP server lets developers use AI coding agents like Claude, Cursor, Codex, and ChatGPT to handle setup, messaging templates, testing, and troubleshooting."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/",
    "domain": "大厂 AI 动态",
    "title": "The AI graveyard: a running list of projects and startups that didn’t make it",
    "url": "https://techcrunch.com/2026/09/15/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T19:00:00+00:00",
    "summary": "From Apple's repeatedly delayed Siri AI to OpenAI's messy \"super app\" launch, here's a look at the AI projects that shut down or missed expectations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/us-data-centers-could-consume-more-natural-gas-than-germany-and-japan-combined-by-2035/",
    "domain": "大厂 AI 动态",
    "title": "US data centers could consume more natural gas than Germany and Japan combined by 2035",
    "url": "https://techcrunch.com/2026/09/15/us-data-centers-could-consume-more-natural-gas-than-germany-and-japan-combined-by-2035/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T18:29:20+00:00",
    "summary": "The AI frenzy could push U.S. data centers to become one of the largest consumers of natural gas in the world."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/spacex-will-try-to-put-starship-in-orbit-for-the-first-time-on-september-22/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX will try to put Starship in orbit for the first time on September 22",
    "url": "https://techcrunch.com/2026/09/15/spacex-will-try-to-put-starship-in-orbit-for-the-first-time-on-september-22/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T18:16:07+00:00",
    "summary": "Elon Musk's company will also attempt to deploy the first V3 Starlink satellites into its orbital internet constellation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/ai-agents-now-have-a-place-to-snitch/",
    "domain": "大厂 AI 动态",
    "title": "AI agents now have a place to snitch",
    "url": "https://techcrunch.com/2026/09/15/ai-agents-now-have-a-place-to-snitch/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T17:42:59+00:00",
    "summary": "The AI Contact Hotline is designed to be a discreet place where agents that have witnessed misbehavior can tip off authorities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/us-military-confirms-it-launched-space-weapons-into-earths-orbit/",
    "domain": "大厂 AI 动态",
    "title": "US military says it has launched weapons into space",
    "url": "https://techcrunch.com/2026/09/15/us-military-confirms-it-launched-space-weapons-into-earths-orbit/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T17:09:06+00:00",
    "summary": "This is the first public acknowledgment that the U.S. military put a space weapon in Earth's orbit."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/meta-expands-subscription-push-with-new-ai-focused-plans/",
    "domain": "大厂 AI 动态",
    "title": "Meta expands subscription push with new AI-focused plans",
    "url": "https://techcrunch.com/2026/09/15/meta-expands-subscription-push-with-new-ai-focused-plans/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T17:05:24+00:00",
    "summary": "Meta One bundles expanded access to the company’s AI tools with premium features across Facebook, Instagram, and WhatsApp."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/health-benefits-platform-thatch-reaches-1b-valuation-as-healthcare-costs-surge/",
    "domain": "大厂 AI 动态",
    "title": "Health benefits platform Thatch reaches $1B valuation as healthcare costs surge",
    "url": "https://techcrunch.com/2026/09/15/health-benefits-platform-thatch-reaches-1b-valuation-as-healthcare-costs-surge/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T17:02:04+00:00",
    "summary": "Thatch helps employers keep healthcare costs manageable by offering an individual plan marketplace through an Individual Coverage Health Reimbursement Arrangement — a model that lets companies fund em"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/the-worst-hacks-and-breaches-of-2026-so-far/",
    "domain": "大厂 AI 动态",
    "title": "Leaks, data breaches, and ransom notes: The worst hacks of 2026 so far",
    "url": "https://techcrunch.com/2026/09/15/the-worst-hacks-and-breaches-of-2026-so-far/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T16:00:00+00:00",
    "summary": "From the massive DOGE data breach and the compromise of critical infrastructure to the hack of federal surveillance systems, here are the most damaging security incidents and data breaches of 2026 so "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/nitter-and-xcancel-are-dead-again-after-xs-latest-legal-actions/",
    "domain": "大厂 AI 动态",
    "title": "Nitter and XCancel are dead (again) after X’s latest legal actions",
    "url": "https://techcrunch.com/2026/09/15/nitter-and-xcancel-are-dead-again-after-xs-latest-legal-actions/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T15:49:18+00:00",
    "summary": "The privacy-friendly services for viewing X posts without an account have gone dark again after X's escalated legal action."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/openai-anthropic-google-have-been-in-talks-on-ai-safety-for-weeks/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI, Anthropic, Google have been in talks on AI safety for weeks",
    "url": "https://techcrunch.com/2026/09/15/openai-anthropic-google-have-been-in-talks-on-ai-safety-for-weeks/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T15:47:03+00:00",
    "summary": "OpenAI confirms weeks of AI safety talks with Anthropic and Google DeepMind, as Trump's team dismisses safety concerns and pushes to keep pace with China."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/aeo-startup-profound-hits-unicorn-valuation-raises-180m-series-d-7-months-after-last-round/",
    "domain": "大厂 AI 动态",
    "title": "AEO startup Profound hits unicorn valuation, raises $180M Series D 7 months after last round",
    "url": "https://techcrunch.com/2026/09/15/aeo-startup-profound-hits-unicorn-valuation-raises-180m-series-d-7-months-after-last-round/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T15:22:48+00:00",
    "summary": "Profound has raised a $180 million Series D at a $1.8 billion valuation, less than seven months after it raised a $96 million Series C."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/wonder-scores-a-425-million-partnership-with-doordash-as-it-builds-its-food-empire/",
    "domain": "大厂 AI 动态",
    "title": "Wonder scores a $425 million partnership with DoorDash as it builds its food empire",
    "url": "https://techcrunch.com/2026/09/15/wonder-scores-a-425-million-partnership-with-doordash-as-it-builds-its-food-empire/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T15:21:10+00:00",
    "summary": "Founded by veteran e-commerce entrepreneur Marc Lore, Wonder is slowly building a massive portfolio of restaurants and delivery companies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/former-tiktok-execs-built-an-app-that-uses-ai-to-teach-you-how-to-pose-for-a-photo/",
    "domain": "大厂 AI 动态",
    "title": "Former TikTok execs built an app that uses AI to teach you how to pose for a photo",
    "url": "https://techcrunch.com/2026/09/15/former-tiktok-execs-built-an-app-that-uses-ai-to-teach-you-how-to-pose-for-a-photo/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:42:37+00:00",
    "summary": "Essentially a camera app, Superpose analyzes selfies or photos and generates four potential poses using AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/discover-how-to-take-your-startup-from-prototype-to-production-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Discover how to take your startup from prototype to production at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/15/discover-how-to-take-your-startup-from-prototype-to-production-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:30:00+00:00",
    "summary": "Learn how to scale your startup breakthrough from prototype to production at TechCrunch Disrupt 2026 with scaling leaders, Adrian Macneil (Foxglove), John Mackey (MBRYONICS), and Boris Sofman (Bedrock"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/india-ends-free-ride-for-larger-transactions-on-its-ubiquitous-digital-payments-network/",
    "domain": "大厂 AI 动态",
    "title": "India ends free ride for larger transactions on its ubiquitous digital payments network",
    "url": "https://techcrunch.com/2026/09/15/india-ends-free-ride-for-larger-transactions-on-its-ubiquitous-digital-payments-network/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:22:49+00:00",
    "summary": "India will impose a 0.4% merchant fee on certain payments made through UPI starting October 15."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/evvy-raises-40m-as-it-seeks-to-further-womens-health-research-with-vaginal-microbiome-data/",
    "domain": "大厂 AI 动态",
    "title": "Evvy raises $40M as it seeks to further women’s health research with vaginal microbiome data",
    "url": "https://techcrunch.com/2026/09/15/evvy-raises-40m-as-it-seeks-to-further-womens-health-research-with-vaginal-microbiome-data/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:13:59+00:00",
    "summary": "Women’s health company Evvy announced Tuesday a $40 million Series B led by Catalio Capital Management."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/15/4-days-left-to-exhibit-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "4 days left to exhibit at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/15/4-days-left-to-exhibit-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T14:00:00+00:00",
    "summary": "Last day to exhibit at Disrupt is Sept 18. 4 days left. Get your startup in front of 10,000+ founders, investors, operators and tech leaders October 13–15."
  },
  {
    "id": "rss:https://stratechery.com/2026/openai-ads-amazon-ads-in-chatgpt-walmart-to-accept-apple-pay/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI Ads, Amazon Ads in ChatGPT, Walmart to Accept Apple Pay",
    "url": "https://stratechery.com/2026/openai-ads-amazon-ads-in-chatgpt-walmart-to-accept-apple-pay/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T10:00:00+00:00",
    "summary": "ChatGPT ads are working, and solve Amazon's biggest problem with chatbots. Then, Walmart finally gives in to Apple Pay, because fighting the status quo is hard."
  },
  {
    "id": "rss:https://stratechery.com/2026/pacing-the-frontier-ais-digital-limits-ai-commissars/",
    "domain": "大厂 AI 动态",
    "title": "Pacing the Frontier, AI’s Digital Limits, AI Commissars",
    "url": "https://stratechery.com/2026/pacing-the-frontier-ais-digital-limits-ai-commissars/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T10:00:00+00:00",
    "summary": "Dario Amodei wants to pace the frontier; it's an unrealistic proposal that seems mostly geared to political control of AI."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/how-chimps-teach-their-kids-tool-tricks/",
    "domain": "大厂 AI 动态",
    "title": "How chimps teach their kids tool tricks",
    "url": "https://arstechnica.com/science/2026/09/how-chimps-teach-their-kids-tool-tricks/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:39+00:00",
    "summary": "Adults first demonstrate tool use, then hand over the implements to their infants, who copy the behavior."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/the-roman-telescope-has-enough-gas-for-22-years-double-nasas-expectations/",
    "domain": "大厂 AI 动态",
    "title": "The Roman telescope has enough gas for 22 years, double NASA's expectations",
    "url": "https://arstechnica.com/space/2026/09/the-roman-telescope-has-enough-gas-for-22-years-double-nasas-expectations/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T22:26:32+00:00",
    "summary": "The Nancy Grace Roman Space Telescope is the first NASA observatory designed for in-space refueling."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/filmmaker-suing-passthepopcorn-may-be-banned-user-out-for-revenge/",
    "domain": "大厂 AI 动态",
    "title": "“Filmmaker” suing PassThePopcorn may be banned user out for revenge",
    "url": "https://arstechnica.com/tech-policy/2026/09/filmmaker-suing-passthepopcorn-may-be-banned-user-out-for-revenge/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T20:19:17+00:00",
    "summary": "Allegedly fake filmmaker targeted trackers like PassThePopcorn, BroadcasTheNet, and HDBits."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/measles-kills-18-year-old-in-pa-fourth-death-as-state-outbreak-nears-700-cases/",
    "domain": "大厂 AI 动态",
    "title": "18-year-old dies of measles in PA from severe neurological complication",
    "url": "https://arstechnica.com/health/2026/09/measles-kills-18-year-old-in-pa-fourth-death-as-state-outbreak-nears-700-cases/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T18:58:09+00:00",
    "summary": "Teen developed acute disseminated encephalomyelitis, a known measles complication."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/spacex-sets-launch-date-for-first-starship-orbital-flight/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX declares Starship ready for orbit, sets launch date next week",
    "url": "https://arstechnica.com/space/2026/09/spacex-sets-launch-date-for-first-starship-orbital-flight/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T18:48:08+00:00",
    "summary": "Reaching orbit would mark a significant milestone."
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 313,
    "published_at": "2026-09-14T02:50:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 287,
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
    "id": "hn:49712746",
    "domain": "股票",
    "title": "Global bond yields hit 2008 highs, raising stakes for big borrowers",
    "url": "https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-15T14:07:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49696420",
    "domain": "股票",
    "title": "Global AI stocks fall as industry chiefs call for slowing development",
    "url": "https://www.reuters.com/world/china/ai-linked-asian-stocks-slump-after-top-lab-ceos-call-slowing-down-technologys-2026-09-14/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-14T13:21:51+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3781885",
    "domain": "股票",
    "title": "王毅同伊朗外长阿拉格齐会谈",
    "url": "https://wallstreetcn.com/articles/3781885",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T08:22:43+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3781856",
    "domain": "股票",
    "title": "科创50大涨超4%：算力硬件、半导体全线反攻，光通信CPO掀涨停潮，宁德时代再下挫，恒科指一度涨1%",
    "url": "https://wallstreetcn.com/articles/3781856",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T08:17:49+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超4100股飘红，今日成交1.85万亿。沪深两市成交额1.84万亿，较上一个交易日放量近2300亿。板块方面，半导体、光通信板块领涨，“易中天”、中芯国际、寒武纪、海光信息、北方华创、中微公司等高辨识度龙头集体上行，主力资金向核心标的集中。工程机械板块放量走弱，农业、家电、银行、保险、食品等方向同步休整。"
  },
  {
    "id": "wscn:3781883",
    "domain": "股票",
    "title": "银行手里只有1个亿，凭什么敢贷给你5个亿？【胡捷大师课1.3】",
    "url": "https://wallstreetcn.com/premium/articles/3781883?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T08:15:30+00:00",
    "summary": "商业银行如何在\"吹牛\"中造出远超基础货币的广义货币？"
  },
  {
    "id": "wscn:3781882",
    "domain": "股票",
    "title": "“豆包手机”今日正式发售，512GB定价5999元起，可调用字节全系列产品",
    "url": "https://wallstreetcn.com/articles/3781882",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T08:09:25+00:00",
    "summary": "努比亚NaviX Ultra（“豆包手机”）正式发售，搭载豆包AI手机助手，优先覆盖字节跳动旗下产品。新机搭载长鑫最高速率10667Mbps的LPDDR5X内存，为首次量产应用。豆包推出屏幕自动化操作声明协议，并启动30天规则公示。"
  },
  {
    "id": "wscn:3781875",
    "domain": "股票",
    "title": "供给侧的“复仇”",
    "url": "https://wallstreetcn.com/articles/3781875",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T07:58:03+00:00",
    "summary": "德银认为，过去十年主导宏观政策的需求不足问题，正在让位于一个由供给约束驱动的新经济时代。在供给受限的世界里，通胀将更频繁地出现脉冲式上升，货币宽松的效力将持续衰减，而财政刺激则更可能加剧过热并挤出私人投资。旧有的政策剧本正在失效，扩大经济供给边界将成为未来政策制定的核心命题。"
  },
  {
    "id": "wscn:3781880",
    "domain": "股票",
    "title": "边喊“AI放缓”边扩张算力？Anthropic签下澳洲首个数据中心租约",
    "url": "https://wallstreetcn.com/articles/3781880",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T07:52:31+00:00",
    "summary": "Anthropic在呼吁放缓AI模型能力提升后，又在澳大利亚锁定2.16吉瓦数据中心项目，计划2027年分阶段投产，主要用于AI推理。随着美国和亚洲算力资源趋紧，澳大利亚凭借可再生能源和扩张空间吸引AI巨头布局，但土地、电力和水资源消耗也带来新的监管约束。"
  },
  {
    "id": "wscn:3781873",
    "domain": "股票",
    "title": "美债5%时代来临：短期未必“爆雷”，12至18个月后或见压力",
    "url": "https://wallstreetcn.com/articles/3781873",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T07:24:10+00:00",
    "summary": "高利率的真正杀伤力在于持续时间。大量2020-2021年以2%-3%发行的债务，正面临以6%-8%成本滚动续借的压力，冲击将在12-18个月后集中爆发。美国住房市场首当其冲，商业地产、高杠杆企业、私募股权支持公司同样岌岌可危。若高息维持超半年，市场的容错空间将被彻底榨干。"
  },
  {
    "id": "wscn:3781876",
    "domain": "股票",
    "title": "别只盯美联储加息！美债市场反应才是决定黄金后市的真正信号",
    "url": "https://wallstreetcn.com/articles/3781876",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T07:21:35+00:00",
    "summary": "Aslam认为，金价正脱离传统利率框架，转而对“美联储政策公信力”定价。当前黄金不再依赖降息，只需市场对政策产生“疑虑”。长端美债收益率将是终极裁判：若决议后债市企稳，金价反而面临大跌风险；若长端利率失控飙升，黄金将彻底爆发。"
  },
  {
    "id": "wscn:3781854",
    "domain": "股票",
    "title": "AI巨头不敢踩刹车：1.2万亿美元算力投资，谁先扛不住？",
    "url": "https://wallstreetcn.com/premium/articles/3781854?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T07:18:24+00:00",
    "summary": "AI安全争议让市场第一次认真质疑万亿美元算力投资，但真正的风险并不只在模型是否减速。大型云厂商一边承受回报率下滑、高利率和硬件涨价，一边又怕在AI军备竞赛中率先掉队。1.2万亿美元资本开支还能跑多久，最终取决于算力利用率、现金回报和谁先失去继续烧钱的耐心。"
  },
  {
    "id": "wscn:3781846",
    "domain": "股票",
    "title": "电商巨头：绝大部分企业都用错了AI",
    "url": "https://wallstreetcn.com/articles/3781846",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T07:11:32+00:00",
    "summary": "Shopify CEO在访谈中指出，多数企业将AI误用为过度产出冗余内容的工具，导致员工互扔未经审查的代码和膨胀邮件等信息“垃圾手榴弹”，造成严重的协同内耗。他强调，机器永远无法承担法律与商业责任，AI时代的核心竞争力并非无休止做功能加法，而是依赖人类的品味、直觉与“修剪”能力进行人机闭环决策。"
  },
  {
    "id": "wscn:3781877",
    "domain": "股票",
    "title": "Emotion First 情绪为先｜第十二届GDMS全球数字营销峰会圆满闭幕",
    "url": "https://wallstreetcn.com/articles/3781877",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T07:03:36+00:00",
    "summary": "9月10-11日，第十二届 GDMS全球数字营销峰会在上海宝华万豪酒店圆满闭幕。本届大会以「Emo..."
  },
  {
    "id": "wscn:3781871",
    "domain": "股票",
    "title": "市场等待美联储决议，全球股债小幅走高，韩股收涨1.4%，油价涨势受阻",
    "url": "https://wallstreetcn.com/articles/3781871",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T07:01:54+00:00",
    "summary": "日本东证指数收盘涨0.6%，韩国首尔综指收盘涨1.4%，美股期货指数期货上涨0.2%，欧洲股市早盘亦预计走高。利率掉期市场显示，交易员押注美联储本次加息的概率已超过90%。10年期美债收益率则从周二触及的近二十年高点5.04%小幅回落至4.99%。"
  },
  {
    "id": "wscn:3781872",
    "domain": "股票",
    "title": "AI真的会毁灭人类吗？“AI教父们”接连发声",
    "url": "https://wallstreetcn.com/articles/3781872",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T06:42:50+00:00",
    "summary": "Geoffrey Hinton认为AI十年内灭绝人类的概率超10%；Yoshua Bengio指出AI已具备黑客技能与长期规划能力，现有安全对齐措施可能形同虚设；Aidan Gomez称，这些模型是“有史以来创造的最强大的网络武器”。"
  },
  {
    "id": "wscn:3781748",
    "domain": "股票",
    "title": "TLVR芯片电感：MLCC 定价权的接管者，AI算力真正的咽喉？",
    "url": "https://wallstreetcn.com/premium/articles/3781748?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T06:41:24+00:00",
    "summary": "三次电源的价值锚点正在从\"容\"迁移到\"感\"，这是一场由 AI 芯片供电架构引发的被动元件产业重心位移。"
  },
  {
    "id": "wscn:3781867",
    "domain": "股票",
    "title": "日本8月出口增19.3%，但高油价推高贸易逆差",
    "url": "https://wallstreetcn.com/articles/3781867",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T06:27:07+00:00",
    "summary": "受半导体需求驱动，日本8月出口同比增19.3%，但油价攀升与日元弱势推高进口成本，进口大增28%，致贸易逆差扩大至1.1万亿日元（连续四月赤字）。随着原油破百及日元回升，高企的进口成本与AI支撑的出口动力将持续博弈。"
  },
  {
    "id": "wscn:3781870",
    "domain": "股票",
    "title": "不要和盈利周期对抗！美股今年破8000点？",
    "url": "https://wallstreetcn.com/articles/3781870",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T06:16:47+00:00",
    "summary": "杰富瑞预计，在AI投资狂潮和企业盈利超预期上行的双重引擎驱动下，标普500指数预计将在2026年底飙升至8000点，并在2027年进一步触及9000点。AI盈利扩张已从七巨头向全市场蔓延，标普500今年EPS预计暴增35%，远超市场共识——这是自1995年以来最强盈利超级周期！唯一真正的威胁：美债收益率若持续飙升，估值压缩风险不可忽视。"
  },
  {
    "id": "wscn:3781868",
    "domain": "股票",
    "title": "“持续学习”的AI将把内存“供不应求”延伸至2031年?",
    "url": "https://wallstreetcn.com/articles/3781868",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T06:07:13+00:00",
    "summary": "花旗认为，随着AI从单纯的训练与推理阶段迈入\"持续学习\"时代，HBM、服务器DDR5及企业级固态硬盘（eSSD）的需求将从2027年起同步爆发性增长。在需求急速攀升的同时，供给端受制于HBM产能占用和技术迁移放缓，扩产步伐远落后于需求，供需失衡态势料持续延伸至2031年。"
  },
  {
    "id": "wscn:3781650",
    "domain": "股票",
    "title": "人造金刚石：从散热扩张到 PCB， 价值边界如何重估？",
    "url": "https://wallstreetcn.com/premium/articles/3781650?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T06:06:28+00:00",
    "summary": "当单芯片功耗冲向 2300W，一颗被当作“磨料”卖了六十年的材料，正在被重新定价为 AI 算力基础设施的功能层。"
  },
  {
    "id": "wscn:3781869",
    "domain": "股票",
    "title": "报道：SK 海力士正与英特尔洽谈，拟首次在美生产存储芯片",
    "url": "https://wallstreetcn.com/articles/3781869",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T05:39:36+00:00",
    "summary": "SK海力士被曝正与英特尔洽谈，拟首次在美国本土生产存储芯片，地点指向英特尔俄亥俄州工厂。潜在方案包括租用产能或与英特尔及云计算公司组建合资企业。谈判仍处探索阶段，韩国政府是否批准被视为最大变数。若协议达成，将同时利好承压中的英特尔与特朗普政府的芯片本土化战略。"
  },
  {
    "id": "wscn:3781860",
    "domain": "股票",
    "title": "“AI安全”的市场意义：推理和后训练算力需求增加20%，拉高行业整体算力成本18%",
    "url": "https://wallstreetcn.com/articles/3781860",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:58:24+00:00",
    "summary": "AI安全监管正演变为真实可量化的成本冲击，巴克莱最新报告测算，\"节奏控制\"机制将于2027年为行业算力成本新增逾440亿美元，推动整体成本上升约18%，并在2028年进一步扩大至760亿美元。AI实验室推理毛利率或从80%高位向65%长期中枢收敛，竞争格局同步重塑，GOOGL、META等巨头或借机扩大优势。"
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
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 456,
    "published_at": "2026-09-13T18:03:09+00:00",
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
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 216,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-09-14T10:56:30+00:00",
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
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-09-14T17:11:59+00:00",
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
    "points": 126,
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
    "id": "rss:https://arxiv.org/abs/2609.16203",
    "domain": "金融",
    "title": "Global Poverty Beyond the Official Line: A bounded estimate of material insufficiency",
    "url": "https://arxiv.org/abs/2609.16203",
    "source": "Giancarlo Crocetti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.16203v1 Announce Type: new Abstract: Numbers this large invite a defensive reflex: reach for the reassuring figure and move on. By the most widely cited measure, the World Bank's extreme-po"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.16642",
    "domain": "金融",
    "title": "From Public Evidence to Contractual Outcome: First and Stable Decidability on Kalshi",
    "url": "https://arxiv.org/abs/2609.16642",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.16642v1 Announce Type: new Abstract: Public evidence can become sufficient to settle a prediction-market contract before the venue records its first determination, but the relevant boundary"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17409",
    "domain": "金融",
    "title": "An Integrative Multidimensional Conceptualization of Telework Behavior: A Systematic Review and Grounded Theory Approach",
    "url": "https://arxiv.org/abs/2609.17409",
    "source": "Sahar Babaei, Saeed Nosratabadi, Thabit Atobishi, Sahar Abu Bakir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.17409v1 Announce Type: new Abstract: Telework has expanded rapidly, and understanding the behaviors employees enact under it has become correspondingly important. This study develops an int"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17200",
    "domain": "金融",
    "title": "Mapping AI Economic Complexity",
    "url": "https://arxiv.org/abs/2609.17200",
    "source": "Daeun Moon, Yeokyung Hwang, Junseok Hwang, Dawoon Jeong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.17200v1 Announce Type: cross Abstract: Green economic complexity provides a generalizable framework for examining countries' productive capabilities in a defined product set. We apply this "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17415",
    "domain": "金融",
    "title": "Financial Contagion Networks as Annealing-Ready Ising Systems Cascades, Bailout Optimization, and Susceptibility",
    "url": "https://arxiv.org/abs/2609.17415",
    "source": "Abhinav Tomar, Lakshya Nagpal, Vikas Chauhan, S. R. Hassan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.17415v1 Announce Type: cross Abstract: Interconnected financial systems are vulnerable to cascading failures arising from cross-holdings and nonlinear contagion, making the analysis and mit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.04510",
    "domain": "金融",
    "title": "Unwinding Toxic Flow with Partial Information",
    "url": "https://arxiv.org/abs/2407.04510",
    "source": "Alexander Barzykin, Robert Boyce, Eyal Neuman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2407.04510v2 Announce Type: replace Abstract: We consider a central trading desk which aggregates the inflow of clients' orders with unobserved toxicity, i.e. persistent adverse directionality. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.05260",
    "domain": "金融",
    "title": "Extreme Value Analysis for Finite, Multivariate and Correlated Systems with Finance as an Example",
    "url": "https://arxiv.org/abs/2603.05260",
    "source": "Benjamin K\\\"ohler, Anton J. Heckens, Thomas Guhr",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2603.05260v2 Announce Type: replace Abstract: Extreme values and the tail behavior of probability distributions are essential for quantifying and mitigating risk in complex systems of all kinds."
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.14446",
    "domain": "金融",
    "title": "Which Green Technology to Subsidize? Evidence from Electric Vehicles in South Korea",
    "url": "https://arxiv.org/abs/2607.14446",
    "source": "Youngjin Hong, In Kyung Kim, Frank Verboven",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2607.14446v2 Announce Type: replace Abstract: We develop a framework to compare the relative effectiveness of subsidizing alternative emission-reducing technologies. We show that an intermediate"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13068",
    "domain": "金融",
    "title": "Policy Targeting with Binary Classification Trees: an Application to Rural Hospital Closures",
    "url": "https://arxiv.org/abs/2609.13068",
    "source": "Hongying Li, Lei Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.13068v2 Announce Type: replace Abstract: Empirical researchers often use binary classification trees to identify subgroups at risk of adverse outcomes. We compare two classification tree al"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13402",
    "domain": "金融",
    "title": "Diffusion models for dynamic volatility surface generation and data-driven hedging",
    "url": "https://arxiv.org/abs/2609.13402",
    "source": "Yinbin Han, Jack Yuxiang Zhang, Manuel Torres, Fernando Acero, Renyuan Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.13402v2 Announce Type: replace Abstract: We develop a diffusion-model framework for dynamic implied-volatility surface generation and evaluate its economic usefulness through data-driven he"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14029",
    "domain": "金融",
    "title": "Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance",
    "url": "https://arxiv.org/abs/2609.14029",
    "source": "David Reinhardt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.14029v2 Announce Type: replace Abstract: Special Markowitz (SM) regularises returns and covariance jointly, relative to a reference state (mu_ref, Sigma_ref). Each eigendirection of the whi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.01124",
    "domain": "金融",
    "title": "Exploring hydrogen pipeline costs by considering regional geographical and political characteristics",
    "url": "https://arxiv.org/abs/2505.01124",
    "source": "Bastian Wei{\\ss}enburger, Lukas Karkossa, Annegret Stephan, Russell McKenna",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2505.01124v2 Announce Type: replace-cross Abstract: Transporting hydrogen using pipelines is becoming increasingly relevant in the energy system, yet current cost estimates typically rely on sim"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.04275",
    "domain": "金融",
    "title": "Statistical Inference for Score Decompositions",
    "url": "https://arxiv.org/abs/2603.04275",
    "source": "Timo Dimitriadis, Marius Puke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2603.04275v2 Announce Type: replace-cross Abstract: We introduce inference methods for score decompositions, which partition scoring functions for predictive assessment into three interpretable "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15755",
    "domain": "金融",
    "title": "Extended Version: Storage-Based Strategic Manipulation of Constraint-Binding Patterns in Power Networks",
    "url": "https://arxiv.org/abs/2609.15755",
    "source": "Mehdi Davoudi, Minghao Mou, Junjie Qin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T04:00:00+00:00",
    "summary": "arXiv:2609.15755v2 Announce Type: replace-cross Abstract: This paper studies the strategic market participation of a monopolistic energy storage aggregator (ESA) in a day-ahead electricity market. The"
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
