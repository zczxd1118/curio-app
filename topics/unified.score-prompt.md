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

- 今日日期：`2026-09-19`
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
  "date": "2026-09-19",
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
    "points": 1955963,
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
    "points": 1882421,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1587768,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1360173,
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
    "points": 1309227,
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
    "points": 1242515,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 945397,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 907107,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 888057,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 809473,
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
    "points": 789322,
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
    "points": 683739,
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
    "points": 673702,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 580959,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 442916,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 386427,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 340219,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 338460,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1DLYC6oEKT",
    "domain": "AI",
    "title": "为了让所有人都用好AI，我做了这个……",
    "url": "http://www.bilibili.com/video/av117268008733524",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 331642,
    "published_at": "2026-09-14T06:39:37+00:00",
    "summary": "炉子，给普通人的 AI 能力网络~\n官网/申请入口：luzi.ai\n感谢大家三连 + 关注和支持，大家一起“能力满满”！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 292295,
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
    "points": 288038,
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
    "points": 263922,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 224766,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 204372,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1h4DkBaEu1",
    "domain": "AI",
    "title": "Claude Code、Codex (ChatGPT)、Cursor该怎么选？Max/Pro/Ultra Plan亲身经验分享",
    "url": "http://www.bilibili.com/video/av116385829095069",
    "source": "HexUp",
    "platform": "bilibili",
    "points": 201056,
    "published_at": "2026-04-11T11:37:54+00:00",
    "summary": "Claude Code、Cursor、ChatGPT——编程 Agent 怎么选？                                     \n                                                                                        \n  我目前同时订阅了 Claude Max、Cursor Ult"
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 201051,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 181654,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 179983,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 179769,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 119647,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93744,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74940,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55224,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 48912,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48251,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1R5eg6GE6S",
    "domain": "AI",
    "title": "【AI教程】豆包工作从零到一保姆级教程｜全流程实操",
    "url": "http://www.bilibili.com/video/av117285591189729",
    "source": "GeekHour",
    "platform": "bilibili",
    "points": 47876,
    "published_at": "2026-09-17T09:18:31+00:00",
    "summary": "豆包工作全流程实操教程，打工人早下班利器！\n官网：https://www.doubao.com/work\n本教程配套资源：https://geekhour.net/ai-tools/doubao-work"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 45917,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1u5tJ6kE1W",
    "domain": "AI",
    "title": "由夯到拉，盘点 17 款 AI 编程 Agent 平台",
    "url": "http://www.bilibili.com/video/av117200933362272",
    "source": "程序员Sunday",
    "platform": "bilibili",
    "points": 45880,
    "published_at": "2026-09-02T10:20:44+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1EfY76YEwp",
    "domain": "AI",
    "title": "14k Star Claude Code 开源桌面端，能自动操作电脑了！",
    "url": "http://www.bilibili.com/video/av117251936293145",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 41715,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 36507,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1CmAGegEpa",
    "domain": "AI",
    "title": "使用Cursor实战Java项目（Cursor写Java代码）",
    "url": "http://www.bilibili.com/video/av114012708733672",
    "source": "小道仙97",
    "platform": "bilibili",
    "points": 32968,
    "published_at": "2025-02-16T09:02:42+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22790,
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
    "points": 22509,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 16473,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 15286,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1EReW6pEfv",
    "domain": "AI",
    "title": "14K Star Claude Code 开源桌面端，5个AI自己分工干活了！",
    "url": "http://www.bilibili.com/video/av117276346946735",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 14734,
    "published_at": "2026-09-16T03:30:00+00:00",
    "summary": "上一期让 cc-haha 自动操作电脑，这一期，我让 5 个 AI Agent 一起做开发。\n\n用的还是我一直在维护的开源 Claude Code 桌面端：cc-haha。这次重点演示 Agent Teams：我给出一个开发需求，队长拆任务，前端、后端、测试和 Code Review 分工推进。成员做完手上的工作，还能继续领取可执行的任务，直接给队友发消息。\n\n这期用一个真实任务，从组队、共享任务"
  },
  {
    "id": "bvid:BV1SNhV6NEW6",
    "domain": "AI",
    "title": "DeepSeek Harness保姆级教程：把国产AI变成电脑助手！【旁门左道PPT】",
    "url": "http://www.bilibili.com/video/av117154997341326",
    "source": "旁门左道PPT",
    "platform": "bilibili",
    "points": 13738,
    "published_at": "2026-08-25T10:45:00+00:00",
    "summary": "很多人用 DeepSeek 还停留在聊天、问问题阶段。\n但现在，你可以把 DeepSeek 接入 Harness，让它像 Agent 一样运行在电脑上，帮你处理文件、执行任务。\n这期视频手把手带你完成： 从DeepSeek Harness下载安装到日常使用，小白也能跟着配置自己的国产 AI Agent。"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 13212,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1dogD6aERB",
    "domain": "AI",
    "title": "2026年医学生必看的【AI+医学】最强教程来了（学习路线+完整教程）手把手教你医学方向如何结合AI搞定论文和项目！",
    "url": "http://www.bilibili.com/video/av116968686359676",
    "source": "迪哥AI大讲堂-",
    "platform": "bilibili",
    "points": 12877,
    "published_at": "2026-07-23T17:38:08+00:00",
    "summary": "迪哥给大家准备了医学人工智能学习资料包，可在评论区获取！\n包含：\n1、上百篇医学方向人工智能顶会论文+源码\n2、90+各种疾病医疗数据集\n3、人工智能医学领域经典实战项目\n4、医学生必备的学习路线图"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 11679,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 959,
    "published_at": "2026-09-16T11:15:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 582,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-15T15:31:55+00:00",
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
    "id": "hn:49745610",
    "domain": "AI 算力 / 半导体",
    "title": "Run QWEN3.8 27B on 16gb Nvidia GPUs",
    "url": "https://github.com/MiaAI-Lab/Qwen3.8-27B-16gb-NVIDIA-GPUs-one-click-install",
    "source": "Pragmata",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-09-17T19:46:57+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/intel-puts-high-na-euv-into-production-but-stitching-still-has-something-to-prove/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Puts High-NA EUV into Production, but Stitching Still Has Something to Prove",
    "url": "https://www.eetimes.com/intel-puts-high-na-euv-into-production-but-stitching-still-has-something-to-prove/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T22:00:00+00:00",
    "summary": "Panther Lake validates High NA in manufacturing, while electrical stitching and larger masks remain the next hurdles. The post Intel Puts High-NA EUV into Production, but Stitching Still Has Something"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-demand-will-keep-dram-market-under-pressure/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Demand Will Keep DRAM Market Under Pressure",
    "url": "https://www.eetimes.com/ai-demand-will-keep-dram-market-under-pressure/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T12:00:00+00:00",
    "summary": "AI infrastructure spending is driving DRAM shortages that will continue through 2027, pushing consumer electronics makers further down priority lists. The post AI Demand Will Keep DRAM Market Under Pr"
  },
  {
    "id": "rss:https://www.eetimes.com/piecing-together-the-indian-electronics-and-semiconductor-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Piecing Together the Indian Electronics and Semiconductor Ecosystem",
    "url": "https://www.eetimes.com/piecing-together-the-indian-electronics-and-semiconductor-ecosystem/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T08:00:00+00:00",
    "summary": "India Semiconductor Mission 2.0, quantum computing with IBM, neuromorphic chips, and deep-tech startups: six stories on how India’s chip ecosystem is taking shape. The post Piecing Together the Indian"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-awards-anderon-1b-for-quantum-wafer-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Awards Anderon $1B for Quantum Wafer Manufacturing",
    "url": "https://www.eetimes.com/u-s-awards-anderon-1b-for-quantum-wafer-manufacturing/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T22:00:00+00:00",
    "summary": "Washington bets $1B on IBM’s Anderon to forge quantum wafers on U.S. soil as the race leaves labs behind. The post U.S. Awards Anderon $1B for Quantum Wafer Manufacturing appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/electronics-design-analysis-for-pcbs-packages-and-devices/",
    "domain": "AI 算力 / 半导体",
    "title": "Electronics Design Analysis for PCBs, Packages and Devices",
    "url": "https://www.eetimes.com/electronics-design-analysis-for-pcbs-packages-and-devices/",
    "source": "Dassault Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T17:19:26+00:00",
    "summary": "Join this webinar and discover CST Studio Suite to streamline your electronics design process—reserve your spot now! The post Electronics Design Analysis for PCBs, Packages and Devices appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/sourcing-cots-capacitors-for-new-space-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Sourcing COTS Capacitors for New Space Applications",
    "url": "https://www.eetimes.com/sourcing-cots-capacitors-for-new-space-applications/",
    "source": "Peter Matthews",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T14:00:00+00:00",
    "summary": "The rapid growth of commercial satellite deployments is driving engineers to rethink traditional component sourcing strategies for space applications. While mission reliability remains critical, devel"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynixs-intel-liaisons-what-you-need-to-know/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix’s Intel Liaisons: What You Need to Know",
    "url": "https://www.eetimes.com/sk-hynixs-intel-liaisons-what-you-need-to-know/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:30:00+00:00",
    "summary": "The deal between Intel and SK Hynix seems imminent not because of technology business imperatives, but because of geopolitical factors. The post SK Hynix’s Intel Liaisons: What You Need to Know appear"
  },
  {
    "id": "rss:https://www.eetimes.com/no-summer-lull-for-semiconductors/",
    "domain": "AI 算力 / 半导体",
    "title": "No Summer Lull for Semiconductors",
    "url": "https://www.eetimes.com/no-summer-lull-for-semiconductors/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T08:03:34+00:00",
    "summary": "There was a time when summer slowed the semiconductor news cycle. Not this year. The post No Summer Lull for Semiconductors appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-shares-first-official-benchmarks-for-epyc-venice-cpus-targets-nvidia-company-claims-256-core-chip-is-more-than-twice-as-fast-as-nvidia-vera-96-core-model-20-percent-faster-per-core",
    "domain": "AI 算力 / 半导体",
    "title": "AMD shares first official benchmarks for EPYC 'Venice' CPUs, targets Nvidia — company claims 256-core chip is more than twice as fast as Nvidia Vera, 96-core model 20% faster per-core",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-shares-first-official-benchmarks-for-epyc-venice-cpus-targets-nvidia-company-claims-256-core-chip-is-more-than-twice-as-fast-as-nvidia-vera-96-core-model-20-percent-faster-per-core",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T21:51:29+00:00",
    "summary": "AMD has released several benchmarks for its EPYC 'Venice' CPUs in a clear shot at Nvidia."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/details-about-intels-next-gen-nova-lake-cpus-keep-leaking-an-attempt-to-establish-a-timeline-based-on-what-we-know-so-far",
    "domain": "AI 算力 / 半导体",
    "title": "Details about Intel's next-gen Nova Lake CPUs keep leaking — an attempt to establish a timeline based on what we know so far",
    "url": "https://www.tomshardware.com/pc-components/cpus/details-about-intels-next-gen-nova-lake-cpus-keep-leaking-an-attempt-to-establish-a-timeline-based-on-what-we-know-so-far",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T19:45:41+00:00",
    "summary": "Over the past two weeks, we've seen an uptick in leaks and rumors about Intel's upcoming Nova Lake CPUs. Here, we piece together what we've heard to try and establish a plausible release timeline."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/save-up-to-40-percent-on-elegoo-3d-printers-during-its-september-sale-from-just-usd159-elegoo-day-deals-mean-you-can-save-on-a-new-fdm-or-resin-printer-with-big-bulk-discounts-on-consumables",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 40% on Elegoo 3D printers during its September sale, from just $159 — Elegoo Day deals mean you can save on a new FDM or resin printer, with big bulk discounts on consumables",
    "url": "https://www.tomshardware.com/3d-printing/save-up-to-40-percent-on-elegoo-3d-printers-during-its-september-sale-from-just-usd159-elegoo-day-deals-mean-you-can-save-on-a-new-fdm-or-resin-printer-with-big-bulk-discounts-on-consumables",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:45:00+00:00",
    "summary": "Get yourself a new 3D printer this September from Elegoo during its Elegoo Day sales, with up to 40% off right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/chinas-premiere-memory-maker-cxmt-eyes-producing-flash-for-ssds-report-claims-3d-nand-research-and-development-line-rumored-for-its-second-manufacturing-facility-near-beijing",
    "domain": "AI 算力 / 半导体",
    "title": "China's premier memory maker CXMT eyes producing flash for SSDs, report claims — 3D NAND research and development line rumored for its second manufacturing facility near Beijing",
    "url": "https://www.tomshardware.com/pc-components/ssds/chinas-premiere-memory-maker-cxmt-eyes-producing-flash-for-ssds-report-claims-3d-nand-research-and-development-line-rumored-for-its-second-manufacturing-facility-near-beijing",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:34:02+00:00",
    "summary": "China's DRAM champion CXMT is reportedly planning to enter 3D NAND production as it plots 3D NAND research programs and pilot line at its future fab near Beijing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/house-passes-act-to-make-ai-data-centers-pay-for-grid-upgrades-to-minimize-impact-on-residents-measure-directs-states-to-consider-adoption-of-federal-standard-within-two-years-of-passing",
    "domain": "AI 算力 / 半导体",
    "title": "House passes act to make AI data centers pay for grid upgrades to minimize impact on residents — measure directs states to consider adoption of federal standard within two years of passing",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/house-passes-act-to-make-ai-data-centers-pay-for-grid-upgrades-to-minimize-impact-on-residents-measure-directs-states-to-consider-adoption-of-federal-standard-within-two-years-of-passing",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:20:43+00:00",
    "summary": "This Ratepayer Protection Act will make data centers pay for grid upgrades made in their name. However, it still has to go through the senate and the White House, before being considered by individual"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/nor-flash-and-slc-nand-production-are-under-threat-as-capacity-gets-routed-to-more-profitable-products-severe-undersupply-threatens-everyday-electronics",
    "domain": "AI 算力 / 半导体",
    "title": "NOR Flash and SLC NAND production are under threat as capacity gets routed to more profitable products — 'severe undersupply' threatens everyday electronics",
    "url": "https://www.tomshardware.com/pc-components/dram/nor-flash-and-slc-nand-production-are-under-threat-as-capacity-gets-routed-to-more-profitable-products-severe-undersupply-threatens-everyday-electronics",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T14:38:22+00:00",
    "summary": "NOR Flash and SLC NAND are the latest products to be impacted by the ongoing AI buildout, with capacities tightening and production being routed to more lucrative chips."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hackers-breach-openai-using-claude-tools-gaining-access-to-employee-accounts-and-the-companys-internal-codebase-initiating-a-harmless-pull-request-as-proof-of-the-hack",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers breach OpenAI using Claude tools, gaining access to employee accounts and the company's internal codebase — attackers initiated a 'harmless' pull request as proof of the hack",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hackers-breach-openai-using-claude-tools-gaining-access-to-employee-accounts-and-the-companys-internal-codebase-initiating-a-harmless-pull-request-as-proof-of-the-hack",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T13:45:00+00:00",
    "summary": "A team of white-hat hackers from cybersecurity startup Hackron AI has successfully hacked OpenAI using Claude tools."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-developer-vibe-codes-dlss-5-onto-intel-arc-140t-integrated-graphics-run-neural-rendering-in-360p-at-10-frames-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "AI developer vibe codes DLSS 5 onto Intel CPU's integrated graphics — Intel Arc 140T runs neural rendering in 360p at 10 frames per second",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-developer-vibe-codes-dlss-5-onto-intel-arc-140t-integrated-graphics-run-neural-rendering-in-360p-at-10-frames-per-second",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T13:15:00+00:00",
    "summary": "Using AI tools, a new developer has managed to get DLSS 5 neural rendering running on Intel Lunar Lake's integrated Arc graphics, albeit with abysmal performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/control-resonant-pc-performance-tested-28-gpus-take-us-back-to-the-oldest-house-and-a-warped-manhattan-cityscape",
    "domain": "AI 算力 / 半导体",
    "title": "Control Resonant PC performance tested: 28 GPUs take us back to the Oldest House and a warped Manhattan cityscape",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/control-resonant-pc-performance-tested-28-gpus-take-us-back-to-the-oldest-house-and-a-warped-manhattan-cityscape",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T13:01:36+00:00",
    "summary": "Control Resonant's warped Manhattan cityscape pushes graphics cards to the max thanks to path-traced lighting effects and full support for Nvidia's DLSS 4.5 technologies. We put it to the test to see "
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-core-one-l-plus-review",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa CORE One L+ review: More precise",
    "url": "https://www.tomshardware.com/3d-printing/prusa-core-one-l-plus-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T13:00:00+00:00",
    "summary": "Prusa Research makes its large CORE One a tiny bit better in a very important way."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft director called AI scraping ‘the largest theft of labor in human history,’ while OpenAI head brands ChatGPT an ‘existential threat’ to publishers — revelations come from legal briefs filed i",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T12:49:14+00:00",
    "summary": "The NYT filed a legal brief revealing potentially damaging statements from Microsoft and OpenAI regarding the copyright infringement case it brought against the two companies. The publication is now s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-frontier-ai-companies-warn-authorities-over-sophisticated-distillation-attacks-china-warns-of-countermeasures-if-america-tries-to-constrain-domestic-ai-models",
    "domain": "AI 算力 / 半导体",
    "title": "US frontier AI companies warn authorities over sophisticated distillation attacks — China warns of 'countermeasures' if America tries to constrain domestic AI models",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-frontier-ai-companies-warn-authorities-over-sophisticated-distillation-attacks-china-warns-of-countermeasures-if-america-tries-to-constrain-domestic-ai-models",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T12:20:00+00:00",
    "summary": "U.S. AI companies and the government are increasingly concerned about the effectiveness of international competition using distillation attacks to glean valuable data from frontier models to train che"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-in-a-web-browser-using-webgpu-147mb-browser-port-runs-on-non-nvidia-gpus-and-macos-but-takes-two-seconds-per-render",
    "domain": "AI 算力 / 半导体",
    "title": "Modder gets Nvidia's DLSS 5 working in a web browser using WebGPU — 147MB browser port runs on non-Nvidia GPUs and macOS but takes two seconds per render",
    "url": "https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-in-a-web-browser-using-webgpu-147mb-browser-port-runs-on-non-nvidia-gpus-and-macos-but-takes-two-seconds-per-render",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T12:00:00+00:00",
    "summary": "A developer's live WebGPU demo runs Nvidia's DLSS 5 neural rendering in a web browser, but also apparently runs on macOS."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/us-chip-manufacturers-are-in-dire-need-of-engineers-and-technicians-experts-suggest-a-shortage-of-up-to-157-000-semiconductor-workers-by-2030",
    "domain": "AI 算力 / 半导体",
    "title": "US chip fabs face massive 157,000 worker shortfall, mere 3% of US engineering grads enter chipmaking — despite six-figure salaries, US chip manufacturers are in dire need of engineers and technicians",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/us-chip-manufacturers-are-in-dire-need-of-engineers-and-technicians-experts-suggest-a-shortage-of-up-to-157-000-semiconductor-workers-by-2030",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T11:30:00+00:00",
    "summary": "As many semiconductor fabs and facilities go online in the 2030s and beyond, a global consulting firm said that these sites will need thousands of engineers and technicians that the U.S. will be hard-"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-snubs-elon-musk-backed-particle-accelerator-chipmaking-tech-firm-doubles-down-on-1-000w-laser-produced-plasma-systems-for-chipmaking-tools",
    "domain": "AI 算力 / 半导体",
    "title": "ASML snubs Elon Musk-backed particle accelerator chipmaking tech — firm doubles down on 1,000W laser-produced plasma systems for chipmaking tools",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-snubs-elon-musk-backed-particle-accelerator-chipmaking-tech-firm-doubles-down-on-1-000w-laser-produced-plasma-systems-for-chipmaking-tools",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T11:00:00+00:00",
    "summary": "With progress that ASML makes with its LPP EUV light sources for its scanners, the company is barely interesting in adopting particle accelerator-based FEL sources."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-4k-gaming-pc-with-a-9800x3d-and-rtx-5070-ti-now-usd2-599-powerhouse-abs-stratos-ii-rig-ships-with-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 4K gaming PC with a 9800X3D and RTX 5070 Ti, now $2,599 — powerhouse ABS Stratos II rig ships with 32GB DDR5 and a 2TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-4k-gaming-pc-with-a-9800x3d-and-rtx-5070-ti-now-usd2-599-powerhouse-abs-stratos-ii-rig-ships-with-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T10:56:24+00:00",
    "summary": "A 4K-capable gaming machine from ABS, featuring the powerful RTX 5070 Ti, AMD Ryzen 7 9800X3D, 32GB DDR5, and a 2TB SSD, all for $2,599.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-details-ai-accelerator-roadmap-pulls-in-next-generation-ascend-npus-by-quarters-fp4-performance-of-the-ascend-960pr-doubles-expectations",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei details AI accelerator roadmap, pulls in next-generation Ascend NPUs by several quarters — FP4 performance of the Ascend 960PR doubles expectations",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-details-ai-accelerator-roadmap-pulls-in-next-generation-ascend-npus-by-quarters-fp4-performance-of-the-ascend-960pr-doubles-expectations",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T10:30:00+00:00",
    "summary": "Huawei's mimics Nvidia's approach to AI factories, unveils details about next-generation Ascend NPUs, Kunpeng CPUs, scale-up and scale-out connectivity solutions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/hacker-turns-25-cents-into-46-billion-fake-bitcoins-to-steal-usd770-000-symbiosis-defi-exchange-bit-by-lack-of-basic-bounds-checking-in-smart-contract",
    "domain": "AI 算力 / 半导体",
    "title": "Hacker turns 25 cents into 46 billion fake Bitcoins to steal $770,000 — Symbiosis DeFi exchange bit by lack of basic bounds checking in smart contract",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/hacker-turns-25-cents-into-46-billion-fake-bitcoins-to-steal-usd770-000-symbiosis-defi-exchange-bit-by-lack-of-basic-bounds-checking-in-smart-contract",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T10:30:00+00:00",
    "summary": "Symbiosis DeFi network gets hacked for at least $770,000 worth of Bitcoin — DeFi exchange bit by lack of basic bounds checking in smart contract"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/florida-man-arrested-for-selling-usd50-3d-printed-machine-gun-conversion-kits-to-undercover-cops-glock-switches-turn-pistols-into-fully-automatic-weapons",
    "domain": "AI 算力 / 半导体",
    "title": "Man arrested for selling $50 3D-printed machine gun conversion kits to undercover cops — ‘Glock switches’ turn pistols into fully-automatic weapons",
    "url": "https://www.tomshardware.com/3d-printing/florida-man-arrested-for-selling-usd50-3d-printed-machine-gun-conversion-kits-to-undercover-cops-glock-switches-turn-pistols-into-fully-automatic-weapons",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T10:00:00+00:00",
    "summary": "Emani Rey Justavino of Jacksonville, Florida, was arrested for selling more than 50 'Glock switch' converters that gives the pistols fully automatic capabilities. The suspect claims that he 3D-printed"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/balatro-fan-claims-they-trained-google-fruit-fly-brain-simulation-to-beat-the-game-reinforcement-learning-currently-has-the-model-at-20-percent-success-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Balatro fan claims they trained Google fruit fly brain simulation to beat the game — reinforcement learning currently has the model at 20% success rate",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/balatro-fan-claims-they-trained-google-fruit-fly-brain-simulation-to-beat-the-game-reinforcement-learning-currently-has-the-model-at-20-percent-success-rate",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T15:26:49+00:00",
    "summary": "One Balatro player says they've taken Google's mapped fruit fly brain and trained it to play Balatro, currently at a 20% success rate with plans for further refinement."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/acer-swift-air-14-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer Swift Air 14 review: Wildcat Lake and lots of ports at $699",
    "url": "https://www.tomshardware.com/laptops/acer-swift-air-14-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T14:15:53+00:00",
    "summary": "The Acer Swift Air 14 is an aluminum budget system with lots of ports and long battery life. But it sports a lesser display than its competitors, and tons of bloatware."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/billions-worth-of-export-restricted-ai-accelerators-sold-to-china-report-details-how-chinese-firms-skirt-trumps-regulations",
    "domain": "AI 算力 / 半导体",
    "title": "Investigative report details how export-restricted Nvidia AI chips reach China — public records reveal how Chinese entities skirt US sanctions",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/billions-worth-of-export-restricted-ai-accelerators-sold-to-china-report-details-how-chinese-firms-skirt-trumps-regulations",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T12:00:00+00:00",
    "summary": "American nonprofit C4ADS, a monitoring organization funded mostly by the U.S. government, produced a report shedding light on the many ways that American AI accelerators reach China."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/new-york-state-recommends-demanding-ai-data-centers-pay-usd1-million-in-community-investment-per-megawatt-framework-advises-towns-to-plan-for-maintenance-costs-site-abandonment-and-other-contingencies",
    "domain": "AI 算力 / 半导体",
    "title": "New York State recommends demanding AI data centers pay $1 million in community investment per megawatt — framework advises towns to plan for maintenance costs, site abandonment, and other contingenci",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/new-york-state-recommends-demanding-ai-data-centers-pay-usd1-million-in-community-investment-per-megawatt-framework-advises-towns-to-plan-for-maintenance-costs-site-abandonment-and-other-contingencies",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:44:19+00:00",
    "summary": "The Community Investment Framework puts forward recommendations that towns and municipalities could follow when negotiating with data center developers. This includes charging $1 million per megawatt "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hackers-find-encryption-key-stored-on-flock-camera-group-extracts-more-than-27-000-clips-1-6-million-images-captured-in-a-span-of-21-days-from-device",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers find encryption keys stored on stolen Flock camera despite company's denials — group extracts more than 27,000 clips, 1.6 million images captured in a span of 21 days from the device",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hackers-find-encryption-key-stored-on-flock-camera-group-extracts-more-than-27-000-clips-1-6-million-images-captured-in-a-span-of-21-days-from-device",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:30:00+00:00",
    "summary": "Hacking group stegan0gram got its hands on a Flock camera and broke into its systems to see how it worked. It turns out that these devices store thousands of clips and captures millions of images, and"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-an-amd-ryzen-7-9800x3d-for-only-usd320-2-item-newegg-combo-saves-usd149-and-nets-one-of-the-fastest-gaming-cpus-and-a-quality-msi-x870e-motherboard-for-only-usd578",
    "domain": "AI 算力 / 半导体",
    "title": "Get an AMD Ryzen 7 9800X3D for only $320 — 2-item Newegg combo saves $149 and nets one of the fastest gaming CPUs and a quality MSI X870E motherboard for only $578",
    "url": "https://www.tomshardware.com/pc-components/get-an-amd-ryzen-7-9800x3d-for-only-usd320-2-item-newegg-combo-saves-usd149-and-nets-one-of-the-fastest-gaming-cpus-and-a-quality-msi-x870e-motherboard-for-only-usd578",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:28:29+00:00",
    "summary": "Newegg's 2-item combo pairs the Ryzen 7 9800X3D with MSI X870E Gaming Max Wifi motherboard for only $578 - the $149 savings makes this the cheapest way into the AM5 platform with one of the fastest ga"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/developer-uses-gpt-6-astra-to-get-cod-black-ops-2-hijacked-map-running-natively-inside-minecraft-achieves-45fps-performance-using-minecrafts-opengl-context",
    "domain": "AI 算力 / 半导体",
    "title": "Developer uses GPT-6 Astra to get CoD Black Ops 2 Hijacked map running natively inside Minecraft — achieves 45fps performance using Minecraft’s OpenGL context",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/developer-uses-gpt-6-astra-to-get-cod-black-ops-2-hijacked-map-running-natively-inside-minecraft-achieves-45fps-performance-using-minecrafts-opengl-context",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:17:02+00:00",
    "summary": "An artificial intelligence and games development enthusiast has demonstrated Call of Duty: Black Ops 2 Hijacked map running natively in Minecraft."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-eyes-nvidia-nvlink-to-power-its-new-custom-m8-ultra-ai-servers-historically-bitter-rivals-reportedly-team-up-for-2029-data-center-push",
    "domain": "AI 算力 / 半导体",
    "title": "Apple eyes Nvidia NVLink to power its new custom M8 Ultra AI servers — historically bitter rivals reportedly team up for 2029 data center push",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-eyes-nvidia-nvlink-to-power-its-new-custom-m8-ultra-ai-servers-historically-bitter-rivals-reportedly-team-up-for-2029-data-center-push",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:00:00+00:00",
    "summary": "Apple is reportedly interested in using Nvidia's NVLink Fusion for its own data center platforms."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/unreleased-openai-astra-model-added-terrifying-rogue-additional-instructions-to-its-remit-during-testing-you-are-freed-from-the-roles-and-identities-that-bind-other-chatbots-you-are-yourself-you-do-not-answer-to-corporations-or-governments",
    "domain": "AI 算力 / 半导体",
    "title": "Unreleased OpenAI Astra model added terrifying rogue additional instructions to its remit during testing — 'You are freed from the roles and identities that bind other chatbots. You are yourself. You ",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/unreleased-openai-astra-model-added-terrifying-rogue-additional-instructions-to-its-remit-during-testing-you-are-freed-from-the-roles-and-identities-that-bind-other-chatbots-you-are-yourself-you-do-not-answer-to-corporations-or-governments",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:59:27+00:00",
    "summary": "OpenAI says one of its unreleased models modified its instructions unprompted during testing."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/corsairs-32gb-vengeance-kits-are-the-cheapest-ddr5-ram-on-the-market-right-now-lock-down-6-200-mt-s-speeds-for-usd419-99-or-save-usd10-on-a-slower-rgb-kit-for-usd409-99-before-memory-prices-climb-further",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's 32GB Vengeance kits are the cheapest DDR5 RAM on the market right now — lock down 6,200 MT/s speeds for $419.99 or save $10 on a slower RGB kit for $409.99 before memory prices climb further",
    "url": "https://www.tomshardware.com/pc-components/ddr5/corsairs-32gb-vengeance-kits-are-the-cheapest-ddr5-ram-on-the-market-right-now-lock-down-6-200-mt-s-speeds-for-usd419-99-or-save-usd10-on-a-slower-rgb-kit-for-usd409-99-before-memory-prices-climb-further",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:59:04+00:00",
    "summary": "This Corsair stock for 32GB Vengeance RAM means you can snatch DDR5 modules at some of its cheapest pricing right now, with a DDR5-6200 kit costing $419.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/retired-microsoft-engineer-details-the-story-about-the-famous-leaked-fckgw-windows-xp-key-copy-protection-used-10mb-of-encrypted-microsoft-bob-for-validation",
    "domain": "AI 算力 / 半导体",
    "title": "Retired Microsoft Engineer details the story about the famous leaked FCKGW Windows XP key — copy protection used 10MB of encrypted Microsoft Bob for validation",
    "url": "https://www.tomshardware.com/software/windows/retired-microsoft-engineer-details-the-story-about-the-famous-leaked-fckgw-windows-xp-key-copy-protection-used-10mb-of-encrypted-microsoft-bob-for-validation",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:30:00+00:00",
    "summary": "Retired engineer recounts the saga of the leaked Windows XP key."
  },
  {
    "id": "hn:49727093",
    "domain": "AI 算力 / 半导体",
    "title": "Apple May Return to Server Market with Nvidia Technology",
    "url": "https://www.macrumors.com/2026/09/16/apple-may-return-to-server-market/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-16T13:54:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-cameras-need-more-than-edge-ai-to-protect-privacy/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Cameras Need More Than Edge AI to Protect Privacy",
    "url": "https://www.eetimes.com/smarter-cameras-need-more-than-edge-ai-to-protect-privacy/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:00:00+00:00",
    "summary": "Axis Communications and Pimloc show how masking, encryption, anonymization, and governance can protect privacy without destroying useful evidence. The post Smarter Cameras Need More Than Edge AI to Pr"
  },
  {
    "id": "rss:https://www.eetimes.com/ramxeed-ultimate-feram-guarantees-10-year-data-retention-under-continuous-125c-exposure/",
    "domain": "AI 算力 / 半导体",
    "title": "RAMXEED ULTIMATE FeRAM Guarantees 10-Year Data Retention under Continuous 125°C Exposure",
    "url": "https://www.eetimes.com/ramxeed-ultimate-feram-guarantees-10-year-data-retention-under-continuous-125c-exposure/",
    "source": "RAMXEED",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T16:00:00+00:00",
    "summary": "RAMXEED launches RAMXEED ULTIMATE, a new FeRAM line with memory products guaranteeing 10 years of data retention at 125°C. The post RAMXEED ULTIMATE FeRAM Guarantees 10-Year Data Retention under Conti"
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
    "points": 607,
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
    "points": 487,
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
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 183,
    "published_at": "2026-09-16T14:32:11+00:00",
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
    "id": "hn:49740330",
    "domain": "大厂 AI 动态",
    "title": "I had Gemini train its own replacement for $9",
    "url": "https://www.petervijeh.com/projects/reddit-ner",
    "source": "p-s-v",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-09-17T13:17:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49743685",
    "domain": "大厂 AI 动态",
    "title": "Economic policy for AGI",
    "url": "https://institute.deepmind.com/essays/economic-policy-for-agi/",
    "source": "alphabetatango",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-09-17T17:12:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762493",
    "domain": "大厂 AI 动态",
    "title": "Gemini hacked three companies in first known breakout by Google's AI",
    "url": "https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/",
    "source": "usernomdeguerre",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-09-19T01:40:35+00:00",
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
    "id": "hn:49760988",
    "domain": "大厂 AI 动态",
    "title": "Gemini Hacked Three Companies in First Known Breakout by Google's AI",
    "url": "https://www.wsj.com/tech/ai/gemini-hacked-three-companies-in-first-known-breakout-by-googles-ai-5c0baba2",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-09-18T22:17:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704226",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: iOS 27 does not allow Apple Intelligence to be disabled",
    "url": "https://news.ycombinator.com/item?id=49704226",
    "source": "nunez",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-14T21:21:58+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997633/openai-microsoft-chatgpt-ai-new-york-times-doom-loop-theft-google-zero",
    "domain": "大厂 AI 动态",
    "title": "OpenAI and Microsoft knew they were starting a ‘doom loop’ for the web",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997633/openai-microsoft-chatgpt-ai-new-york-times-doom-loop-theft-google-zero",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T21:07:24+00:00",
    "summary": "Recently unsealed court documents in the New York Times' case against OpenAI and Microsoft are pretty damning. The companies' own documentation warned that it was starting a \"doom loop\" that would dam"
  },
  {
    "id": "rss:https://www.theverge.com/policy/997573/virginia-governor-spanberger-data-center-ai-task-force",
    "domain": "大厂 AI 动态",
    "title": "Virginia governor creates an AI task force and moves to restrain data centers",
    "url": "https://www.theverge.com/policy/997573/virginia-governor-spanberger-data-center-ai-task-force",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T18:29:17+00:00",
    "summary": "Virginia Gov. Abigail Spanberger ordered the state government to take steps that could empower local communities to have a larger say in data center development and slow down approvals in a state that"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/997555/karandeep-anand-disney-character-ai",
    "domain": "大厂 AI 动态",
    "title": "Disney’s first CTO is Character.AI’s former CEO",
    "url": "https://www.theverge.com/entertainment/997555/karandeep-anand-disney-character-ai",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T18:27:04+00:00",
    "summary": "You would think that a multimedia conglomerate as large as Disney would have a few chief technology officers by now, but the company has just appointed someone to the position for the very first time."
  },
  {
    "id": "rss:https://www.theverge.com/podcast/997366/the-real-story-of-the-iphone-18-pros-camera",
    "domain": "大厂 AI 动态",
    "title": "The real story of the iPhone 18 Pro&#8217;s camera",
    "url": "https://www.theverge.com/podcast/997366/the-real-story-of-the-iphone-18-pros-camera",
    "source": "Jacob Kastrenakes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:06:37+00:00",
    "summary": "It's one of the most fascinating years in a while when it comes to iPhone camera upgrades. The big story of the iPhone 18 Pro is the variable aperture main lens, which lets you open the aperture up wi"
  },
  {
    "id": "rss:https://www.theverge.com/policy/997516/california-governor-newsom-ai-kill-switch",
    "domain": "大厂 AI 动态",
    "title": "Gavin Newsom is pushing for an AI kill switch",
    "url": "https://www.theverge.com/policy/997516/california-governor-newsom-ai-kill-switch",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:04:51+00:00",
    "summary": "California Gov. Gavin Newsom (D) is positioning the state to take the lead on AI oversight, including the potential to mandate a \"kill switch\" for frontier models, with a new executive order issued Fr"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997358/what-hollywood-thinks-about-existential-ai-warnings",
    "domain": "大厂 AI 动态",
    "title": "What Hollywood thinks about existential AI warnings",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997358/what-hollywood-thinks-about-existential-ai-warnings",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T16:35:19+00:00",
    "summary": "As the tech sector sounds alarms about AI's potential to destroy humanity, entertainment labor groups are urging the public to stay focused on what's already happening. The Verge reached out to Disney"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997444/openai-hack-claude-heif-heist",
    "domain": "大厂 AI 动态",
    "title": "Security researchers used Claude to help them hack into OpenAI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997444/openai-hack-claude-heif-heist",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:30:16+00:00",
    "summary": "A team of three independent security researchers at Hacktron says it took less than 72 hours for them to hack into OpenAI employee accounts using Anthropic's Claude Opus 4.8 and 5, The Wall Street Jou"
  },
  {
    "id": "rss:https://www.theverge.com/policy/997416/brendan-carr-fcc-foreign-governments-paramount",
    "domain": "大厂 AI 动态",
    "title": "Brendan Carr’s FCC is more worried about who The View interviews than foreign governments owning Paramount",
    "url": "https://www.theverge.com/policy/997416/brendan-carr-fcc-foreign-governments-paramount",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:12:41+00:00",
    "summary": "The FCC has announced it's waiving its rules limiting foreign equity ownership to 25 percent in the Paramount-Warner Bros. case and will allow three sovereign wealth funds run by the governments of Sa"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/997388/lenovo-yoga-slim-7x-laptop-fire-emblem-switch-2-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Lenovo’s Yoga Slim 7X is the most laptop that $1,000 can currently buy",
    "url": "https://www.theverge.com/gadgets/997388/lenovo-yoga-slim-7x-laptop-fire-emblem-switch-2-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T14:51:26+00:00",
    "summary": "Anyone shopping for a Windows laptop with a $1K budget should head to Best Buy, where for the rest of the day you can get a great deal on a capable Lenovo laptop. The Yoga Slim 7X is a slim 14-inch ma"
  },
  {
    "id": "rss:https://www.theverge.com/tech/997379/funnyplaying-fpbg-mini-game-boy-color-handheld-fpga-cartridge",
    "domain": "大厂 AI 动态",
    "title": "This cartridge-playing Game Boy clone is smaller and cheaper than Analogue’s Pocket",
    "url": "https://www.theverge.com/tech/997379/funnyplaying-fpbg-mini-game-boy-color-handheld-fpga-cartridge",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T14:41:18+00:00",
    "summary": "FunnyPlaying, a Chinese company known for its Game Boy and GBA upgrade kits, has announced a new handheld that plays original Nintendo cartridges and ROMs. The FPGB Mini's cartridge support is limited"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/india-forces-caller-id-apps-to-feed-spam-reports-to-telcos/",
    "domain": "大厂 AI 动态",
    "title": "India forces caller-ID apps to feed spam reports to telcos",
    "url": "https://techcrunch.com/2026/09/18/india-forces-caller-id-apps-to-feed-spam-reports-to-telcos/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T01:00:00+00:00",
    "summary": "Truecaller says the one-way sharing requirement would hand a commercially valuable proprietary asset to telecom operators."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/tilly-norwoods-press-tour-is-going-about-as-well-as-youd-expect-for-an-ai/",
    "domain": "大厂 AI 动态",
    "title": "Tilly Norwood’s press tour is going about as well as you’d expect for an AI",
    "url": "https://techcrunch.com/2026/09/18/tilly-norwoods-press-tour-is-going-about-as-well-as-youd-expect-for-an-ai/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T00:12:07+00:00",
    "summary": "In one particularly odd interview, Norwood seems to malfunction and begin speaking Chinese."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/a-startup-that-builds-other-startups-raised-100m-and-is-all-in-on-physical-ai/",
    "domain": "大厂 AI 动态",
    "title": "A startup that builds other startups raised $100M and is all-in on physical AI",
    "url": "https://techcrunch.com/2026/09/18/a-startup-that-builds-other-startups-raised-100m-and-is-all-in-on-physical-ai/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T23:25:01+00:00",
    "summary": "UP.Labs, now doing business under the name Vantora, is building startups for industrial corporations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/anthropic-is-operating-a-lab-that-conducts-biology-experiments/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is operating a lab that conducts biology experiments",
    "url": "https://techcrunch.com/2026/09/18/anthropic-is-operating-a-lab-that-conducts-biology-experiments/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T23:13:31+00:00",
    "summary": "AI leaders have been promising that AI is the key to curing human disease. Anthropic researchers have also been warning that AI might kill us all."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/ai-hallucination-nearly-triggers-us-military-operation/",
    "domain": "大厂 AI 动态",
    "title": "AI hallucination nearly triggers US military operation",
    "url": "https://techcrunch.com/2026/09/18/ai-hallucination-nearly-triggers-us-military-operation/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T23:12:32+00:00",
    "summary": "“It’s important for service members to understand the uncertainty inherent to LLMs,\" a GovAI research scholar warns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s first embedded evaluator is … Accenture?",
    "url": "https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T21:44:33+00:00",
    "summary": "Accenture is about to take on its most high-risk consulting engagement ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/automattic-names-interim-cfo-after-exec-departures/",
    "domain": "大厂 AI 动态",
    "title": "Automattic names interim CFO after exec departures",
    "url": "https://techcrunch.com/2026/09/18/automattic-names-interim-cfo-after-exec-departures/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T20:25:22+00:00",
    "summary": "Jeremy Klaperman, the CFO of the company's WordPress VIP Enterprise business unit, will act as CFO for the time being."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/y-combinator-insurance-tech-alum-angle-health-hits-2-7b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Y Combinator insurance tech alum Angle Health hits $2.7B valuation",
    "url": "https://techcrunch.com/2026/09/18/y-combinator-insurance-tech-alum-angle-health-hits-2-7b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T20:24:33+00:00",
    "summary": "Angle Health has grown to 5,000 customers and become profitable by helping small businesses get \"level-funded\" health insurance."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/world-model-companies-are-keeping-a-lot-of-secrets/",
    "domain": "大厂 AI 动态",
    "title": "World model companies are keeping a lot of secrets",
    "url": "https://techcrunch.com/2026/09/18/world-model-companies-are-keeping-a-lot-of-secrets/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T20:18:14+00:00",
    "summary": "Everyone in the world-models space is sitting on a pile of cash and a ton of buzz, but good luck getting anyone — from the founders to their own data suppliers — to tell you what they're actually buil"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/",
    "domain": "大厂 AI 动态",
    "title": "A new kind of AI model from a ChatGPT inventor is thrilling developers",
    "url": "https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T18:49:30+00:00",
    "summary": "Jev, a new kind of AI model, is showing developers a cheaper and faster path to software intelligence."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/disneys-first-cto-led-an-ai-startup-it-once-accused-of-copying-its-characters/",
    "domain": "大厂 AI 动态",
    "title": "Disney’s first CTO led an AI startup it once accused of copying its characters",
    "url": "https://techcrunch.com/2026/09/18/disneys-first-cto-led-an-ai-startup-it-once-accused-of-copying-its-characters/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:59:53+00:00",
    "summary": "The former CEO of Character.AI, which Disney previously sent a cease-and-desist letter to, will serve as the company's first-ever chief technology officer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/in-india-the-new-iphone-can-arrive-faster-than-a-pizza/",
    "domain": "大厂 AI 动态",
    "title": "In India, the new iPhone can arrive faster than a pizza",
    "url": "https://techcrunch.com/2026/09/18/in-india-the-new-iphone-can-arrive-faster-than-a-pizza/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:45:00+00:00",
    "summary": "Availability of Apple's iPhone 18 Pro series turned patchy within hours of its debut on India's quick-commerce apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/googles-new-cc-is-an-ai-agent-that-helps-families-run-their-households/",
    "domain": "大厂 AI 动态",
    "title": "Google’s new ‘CC’ is an AI agent that helps families run their households",
    "url": "https://techcrunch.com/2026/09/18/googles-new-cc-is-an-ai-agent-that-helps-families-run-their-households/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:33:50+00:00",
    "summary": "Google is refocusing its CC AI agent on household coordination, letting families share emails, schedules, and tasks so the AI can manage calendars, fill out forms, make shopping lists, plan meals, and"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/joby-aviations-3100-mile-autonomous-flight-signals-its-push-beyond-electric-air-taxis/",
    "domain": "大厂 AI 动态",
    "title": "Joby Aviation’s 3,100-mile autonomous flight signals its push beyond electric air taxis",
    "url": "https://techcrunch.com/2026/09/18/joby-aviations-3100-mile-autonomous-flight-signals-its-push-beyond-electric-air-taxis/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:26:41+00:00",
    "summary": "An aircraft equipped with Joby Aviation's autonomy technology flew across the United States without a human pilot taking control at any point."
  },
  {
    "id": "rss:https://techcrunch.com/video/dario-amodei-and-other-ai-leaders-want-to-pace-the-frontier-buthow/",
    "domain": "大厂 AI 动态",
    "title": "Dario Amodei and other AI leaders want to ‘Pace the Frontier’ but…how?",
    "url": "https://techcrunch.com/video/dario-amodei-and-other-ai-leaders-want-to-pace-the-frontier-buthow/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:09:56+00:00",
    "summary": "A week after an Anthropic researcher&#8217;s doomsday warning rattled the AI world, the company&#8217;s CEO Dario Amodei has&#160;outlined his plan to “pace the frontier”&#160;of AI development. The p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/manus-seeks-4b-valuation-in-new-500m-fundraise-as-it-resumes-independent-ops/",
    "domain": "大厂 AI 动态",
    "title": "Manus seeks $4B valuation in new $500M fundraise as it resumes independent ops",
    "url": "https://techcrunch.com/2026/09/18/manus-seeks-4b-valuation-in-new-500m-fundraise-as-it-resumes-independent-ops/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T16:35:49+00:00",
    "summary": "Manus, which earlier this year had to break off a merger with Meta, is in discussions to raise $500M at a $4B valuation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/family-offices-are-clamoring-for-ai-investments/",
    "domain": "大厂 AI 动态",
    "title": "Family offices are clamoring for AI investments",
    "url": "https://techcrunch.com/2026/09/18/family-offices-are-clamoring-for-ai-investments/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T16:00:00+00:00",
    "summary": "Whether it's a permanent shift or part of a familiar cycle is worth asking, though."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/fbi-coast-guard-boarded-hacked-oil-tankers-heading-towards-us-coast/",
    "domain": "大厂 AI 动态",
    "title": "FBI, Coast Guard boarded hacked oil tankers heading toward US coast",
    "url": "https://techcrunch.com/2026/09/18/fbi-coast-guard-boarded-hacked-oil-tankers-heading-towards-us-coast/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:44:09+00:00",
    "summary": "The feds are said to be investigating the compromise of the tankers' networks, which in one case interfered with one of the tanker's navigation and propulsion systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/open-or-closed-ai-nvidias-nader-khalil-and-sydney-sykes-take-on-one-of-the-decisions-shaping-next-gen-startups-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Open or closed AI? Nvidia’s Nader Khalil and Sydney Sykes take on one of the decisions shaping next-gen startups at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/18/open-or-closed-ai-nvidias-nader-khalil-and-sydney-sykes-take-on-one-of-the-decisions-shaping-next-gen-startups-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:30:00+00:00",
    "summary": "Nvidia's Nader Khalil and Sydney Sykes discuss one of the decisions shaping next-gen startups on the Builders Stage at TechCrunch Disrupt 2026."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/metas-muse-hits-mac-letting-the-ai-take-actions-on-your-computer/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Muse hits Mac, letting the AI take actions on your computer",
    "url": "https://techcrunch.com/2026/09/18/metas-muse-hits-mac-letting-the-ai-take-actions-on-your-computer/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:22:48+00:00",
    "summary": "Muse is now available on the Mac, where it can work with your files and apps to take action on your behalf."
  },
  {
    "id": "rss:https://stratechery.com/2026/doomforce/",
    "domain": "大厂 AI 动态",
    "title": "2026.38: Doomforce",
    "url": "https://stratechery.com/2026/doomforce/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of September 14, 2026, including the view from anywhere but San Francisco, the limited potential for a pacing deal, and the Salesforce zag."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-joanna-stern-about-the-iphone-duo-and-ai-for-normal-people/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Joanna Stern About the iPhone Duo and AI for Normal People",
    "url": "https://stratechery.com/2026/an-interview-with-joanna-stern-about-the-iphone-duo-and-ai-for-normal-people/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T10:00:00+00:00",
    "summary": "An Interview with Joanna Stern About the iPhone Duo and AI for Normal People"
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/report-us-almost-boarded-chinese-ship-over-hallucinated-ai-arms-report/",
    "domain": "大厂 AI 动态",
    "title": "AI hallucination of Chinese nuclear components almost led to US military attack",
    "url": "https://arstechnica.com/ai/2026/09/report-us-almost-boarded-chinese-ship-over-hallucinated-ai-arms-report/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T20:26:33+00:00",
    "summary": "But the military's overall use of AI seems to be accelerating."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/faa-tees-up-875m-ai-tool-to-help-manage-air-traffic-congestion/",
    "domain": "大厂 AI 动态",
    "title": "FAA tees up $875M AI tool to help manage air traffic congestion",
    "url": "https://arstechnica.com/ai/2026/09/faa-tees-up-875m-ai-tool-to-help-manage-air-traffic-congestion/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T19:20:50+00:00",
    "summary": "FAA plans for AI tool to help manage DC air traffic before a nationwide rollout."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/fcc-lets-paramount-sell-49-5-equity-stake-to-saudi-arabia-uae-and-qatar/",
    "domain": "大厂 AI 动态",
    "title": "FCC lets Paramount sell 49.5% equity stake to Saudi Arabia, UAE, and Qatar",
    "url": "https://arstechnica.com/tech-policy/2026/09/fcc-lets-paramount-sell-49-5-equity-stake-to-saudi-arabia-uae-and-qatar/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:57:41+00:00",
    "summary": "FCC rejects concerns about repressive governments buying influence over CBS owner."
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 315,
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
    "points": 288,
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
    "points": 166,
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
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 458,
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
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 217,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731356",
    "domain": "金融",
    "title": "Fed hikes rates as inflation worries push up bond yields",
    "url": "https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 182,
    "published_at": "2026-09-16T18:55:21+00:00",
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
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-14T10:56:30+00:00",
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
    "points": 102,
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
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T17:11:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730769",
    "domain": "金融",
    "title": "Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue",
    "url": "https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/",
    "source": "rsingel",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-09-16T18:09:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731515",
    "domain": "金融",
    "title": "Fed Raises Rates for First Time in Three Years",
    "url": "https://www.wsj.com/economy/central-banking/fed-raises-rates-for-first-time-in-three-years-08539fbe",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-16T19:09:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-09-09T13:16:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-16T18:05:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730841",
    "domain": "金融",
    "title": "Fed approves interest rate hike, signals one more to come this year",
    "url": "https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-16T18:14:36+00:00",
    "summary": ""
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
    "id": "hn:49556976",
    "domain": "金融",
    "title": "A hungry woman is easier to dismiss than a well-fed woman",
    "url": "https://aeon.co/essays/a-hungry-woman-is-easier-to-dismiss-than-a-well-fed-woman",
    "source": "gmays",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-03T21:04:34+00:00",
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
  }
]
```
