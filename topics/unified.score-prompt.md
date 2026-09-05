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

- 今日日期：`2026-09-05`
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
  "date": "2026-09-05",
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
    "id": "bvid:BV1DfrdByE2H",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av115897075242856",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 4441604,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 2472008,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1808487,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1349988,
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
    "points": 1242932,
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
    "points": 1159172,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1075623,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 881726,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 711558,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 703315,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 672890,
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
    "points": 660674,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 587149,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 454495,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 441629,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 406438,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 385855,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 353594,
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
    "points": 340622,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 281020,
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
    "points": 268028,
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
    "points": 254337,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 234443,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180606,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 164582,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 159877,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1wqMw6NEB6",
    "domain": "AI",
    "title": "Claude的安装并且如何配置ccswitch转接第三方API完整使用教程#codex #ai #安装#大模型#API#ccswitch#claude",
    "url": "http://www.bilibili.com/video/av116861479946306",
    "source": "老便秘了",
    "platform": "bilibili",
    "points": 123401,
    "published_at": "2026-07-04T11:32:40+00:00",
    "summary": "Claude的安装并且如何配置ccswitch转接第三方API完整使用教程#codex #ai #安装#大模型#API#ccswitch#claude"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 107967,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99899,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93562,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1V6tP6zENk",
    "domain": "AI",
    "title": "我爸用 Vibe Coding 做了个“专治写作走神”的软件，治法有点狠",
    "url": "http://www.bilibili.com/video/av117173787826916",
    "source": "大不溜add小不溜",
    "platform": "bilibili",
    "points": 81333,
    "published_at": "2026-08-28T15:19:16+00:00",
    "summary": "我爸说想做一个能让人专心写东西的软件。\n结果一走神、一切屏，回来以后事情就开始不对劲了。\n这是最近做的第一个 Vibe Coding 小发明，后面准备继续把一些奇奇怪怪的产品脑洞真的做出来。"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74262,
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
    "points": 54789,
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
    "points": 47682,
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
    "points": 47444,
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
    "points": 41429,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39571,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 39033,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 36792,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29706,
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
    "points": 28917,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 28671,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22761,
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
    "points": 21096,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17793,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 16657,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15044,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1ZBT2ztEwp",
    "domain": "AI",
    "title": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程",
    "url": "http://www.bilibili.com/video/av114642592469769",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 13815,
    "published_at": "2025-06-07T14:53:38+00:00",
    "summary": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 12224,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10923,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1985,
    "published_at": "2026-08-27T01:12:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49434378",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI Jalapeño: Better than Nvidia Blackwell",
    "url": "https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia",
    "source": "bmulholland",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-08-25T14:06:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548952",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to acquire Hugging Face",
    "url": "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html",
    "source": "tosh",
    "platform": "hackernews",
    "points": 324,
    "published_at": "2026-09-03T12:10:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49567357",
    "domain": "AI 算力 / 半导体",
    "title": "Georgi Gerganov on llama.cpp/ggml future after Nvidia acquisition of HuggingFace",
    "url": "https://twitter.com/ggerganov/status/2095897173376618881",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-09-04T17:12:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49557813",
    "domain": "AI 算力 / 半导体",
    "title": "Tell HN: NVIDIA's Acquisition of HuggingFace was for $HuggingFace",
    "url": "https://news.ycombinator.com/item?id=49557813",
    "source": "MontagFTB",
    "platform": "hackernews",
    "points": 40,
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
    "id": "hn:49466052",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia projects $673B in sales as AI demand widens",
    "url": "https://forgeeks.net/nvidia-673-billion-ai-growth-forecast/",
    "source": "kuuuzya",
    "platform": "hackernews",
    "points": 111,
    "published_at": "2026-08-27T15:04:16+00:00",
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
    "id": "hn:49469249",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Starts Pac as AI Chip Maker Builds DC Influence Force",
    "url": "https://news.bgov.com/bloomberg-government-news/nvidia-starts-a-pac-as-ai-chip-maker-buids-influence-force-in-dc",
    "source": "rarisma",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-08-27T18:34:40+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/ee-times-magazine-september-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "EE Times Magazine – September 2026",
    "url": "https://www.eetimes.com/ee-times-magazine-september-2026/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T22:40:26+00:00",
    "summary": "The September 2026 edition of EE Times Magazine examines how smarter buildings combine ambient energy harvesting, sensing, AI, and connected systems to improve safety while protecting privacy. The pos"
  },
  {
    "id": "rss:https://www.eetimes.com/when-the-package-becomes-an-electrical-design-variable/",
    "domain": "AI 算力 / 半导体",
    "title": "When the Package Becomes an Electrical Design Variable",
    "url": "https://www.eetimes.com/when-the-package-becomes-an-electrical-design-variable/",
    "source": "Takaki Murata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:50:10+00:00",
    "summary": "AI power integrity now lives inside the package, not just the PCB. Treat chip, package, and board as one PDN. The post When the Package Becomes an Electrical Design Variable appeared first on EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/7-steps-to-take-now-meet-the-eu-cra-9-11-26-reporting-deadline/",
    "domain": "AI 算力 / 半导体",
    "title": "7 Steps to Take Now: Meet the EU CRA 9/11/26 Reporting Deadline",
    "url": "https://www.eetimes.com/7-steps-to-take-now-meet-the-eu-cra-9-11-26-reporting-deadline/",
    "source": "By Colin Duggan, CEO and co-founder, BG Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:31:18+00:00",
    "summary": "Prepare for the EU Cyber Resilience Act's September 2026 reporting deadline; follow these seven steps to ensure compliance and readiness. The post 7 Steps to Take Now: Meet the EU CRA 9/11/26 Reportin"
  },
  {
    "id": "rss:https://www.eetimes.com/techworks-aligns-u-k-semiconductors-under-uksia-umbrella/",
    "domain": "AI 算力 / 半导体",
    "title": "TechWorks Aligns U.K. Semiconductors Under UKSIA Umbrella",
    "url": "https://www.eetimes.com/techworks-aligns-u-k-semiconductors-under-uksia-umbrella/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T13:46:01+00:00",
    "summary": "TechWorks corrals U.K. chip groups under UKSIA as funding surges 65% and 700 execs swarm London. The post TechWorks Aligns U.K. Semiconductors Under UKSIA Umbrella appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/display-developments-challenge-controllers/",
    "domain": "AI 算力 / 半导体",
    "title": "Display Developments Challenge Controllers",
    "url": "https://www.eetimes.com/display-developments-challenge-controllers/",
    "source": "Teng Tang Yang, Senior Division Director of Product Marketing Division, UMC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T13:00:00+00:00",
    "summary": "Discover how AMOLED, micro-OLED and advanced DDIC technologies are transforming displays with higher resolution, lower power and immersive experiences. The post Display Developments Challenge Controll"
  },
  {
    "id": "rss:https://www.eetimes.com/indias-quantum-journey-goes-beyond-the-qubit/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s Quantum Journey Goes Beyond the Qubit",
    "url": "https://www.eetimes.com/indias-quantum-journey-goes-beyond-the-qubit/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T08:00:47+00:00",
    "summary": "IBM’s Amaravati deployment could accelerate India’s quantum ecosystem as startups develop processors, software, and supporting technologies. The post India’s Quantum Journey Goes Beyond the Qubit appe"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/dlss-5-officially-launches-inside-nba-2k27-limited-to-rtx-50-series-gpus-for-now-nvidia-promises-to-bring-neutral-rendering-tech-to-rtx-40-series-soon",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 5 officially launches inside NBA 2K27, limited to RTX 50-series GPUs for now — Nvidia promises to bring neutral rendering tech to RTX 40-series soon",
    "url": "https://www.tomshardware.com/pc-components/gpus/dlss-5-officially-launches-inside-nba-2k27-limited-to-rtx-50-series-gpus-for-now-nvidia-promises-to-bring-neutral-rendering-tech-to-rtx-40-series-soon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:09:31+00:00",
    "summary": "Nvidia's controversial neural-rendering tech, DLSS 5, is now officially available in NBA 2K27, marking the start of a new era for the company. DLSS 5 will also come to RTX 40-series soon after current"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/grab-a-new-3d-printer-for-as-low-as-usd229-right-now-in-crealitys-labor-day-flash-sale-with-up-to-50-percent-off-big-sale-discounts-also-include-resin-and-filament-bundles-along-with-3d-scanners-and-toolkits",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a new 3D printer for as low as $229 right now in Creality's Labor Day flash sale, with up to 50% off —big sale discounts also include resin and filament bundles, along with 3D scanners and toolki",
    "url": "https://www.tomshardware.com/3d-printing/grab-a-new-3d-printer-for-as-low-as-usd229-right-now-in-crealitys-labor-day-flash-sale-with-up-to-50-percent-off-big-sale-discounts-also-include-resin-and-filament-bundles-along-with-3d-scanners-and-toolkits",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:00:00+00:00",
    "summary": "Grab a new 3D printer in Creality's Labor Day flash sale, with discounts on printers and accessories available."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/nas/minisforum-launches-local-ai-solutions-at-ifa-2026-ai-agent-nas-n5-and-ai-mini-workstation-ms-s1-use-amd-ryzen-ai-max-pro-495-processors-designed-to-run-models-locally",
    "domain": "AI 算力 / 半导体",
    "title": "Minisforum launches local AI solutions at IFA 2026 — AI Agent NAS N5 and AI Mini Workstation MS-S1 use AMD Ryzen AI Max+ Pro 495 processors designed to run models locally",
    "url": "https://www.tomshardware.com/pc-components/nas/minisforum-launches-local-ai-solutions-at-ifa-2026-ai-agent-nas-n5-and-ai-mini-workstation-ms-s1-use-amd-ryzen-ai-max-pro-495-processors-designed-to-run-models-locally",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:15:00+00:00",
    "summary": "Minisforum unveiled the NAS N5 Max-P495 and MS-S1 Max-P945 at IFA 2026. The NAS and mini-PC are powered by the AMD Ryzen AI Max+ Pro 495, which can be configured with up to 192GB of unified memory and"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd900-in-the-best-buy-labor-day-sale-on-tech-with-huge-discounts-on-gaming-pcs-laptops-and-monitors-secure-an-upgrade-fast-to-beat-rising-hardware-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to $900 in the Best Buy Labor Day sale on tech, with huge discounts on gaming PCs, laptops and monitors — secure an upgrade fast to beat rising hardware costs",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd900-in-the-best-buy-labor-day-sale-on-tech-with-huge-discounts-on-gaming-pcs-laptops-and-monitors-secure-an-upgrade-fast-to-beat-rising-hardware-costs",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:30:00+00:00",
    "summary": "There's a big Labor Day sale over at Best Buy right now, securing you huge discounts on tech, including gaming PCs, handhelds, laptops, and monitors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-faces-pricing-reckoning-as-token-volume-explodes-25-fold-mid-tier-models-deliver-90-percent-of-flagship-capability-at-one-sixth-the-cost",
    "domain": "AI 算力 / 半导体",
    "title": "Frontier AI faces pricing reckoning as token volume explodes 25-fold — mid-tier models deliver 90% of flagship capability at one-sixth the cost",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-faces-pricing-reckoning-as-token-volume-explodes-25-fold-mid-tier-models-deliver-90-percent-of-flagship-capability-at-one-sixth-the-cost",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:21:56+00:00",
    "summary": "As frontier AI developers push for cost savings as much as intelligence enhancements, new models push the boundaries of the pareto frontier, with even small advantages crowning new kings."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/nvidia-app-update-fails-to-block-unofficial-dlss-multi-frame-generation-on-rtx-40-series-modders-restore-support-across-multiple-games-within-hours",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia app update fails to block unofficial DLSS multi-frame generation mod on RTX 40 series gaming GPUs — modders restore support across multiple games within hours",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/nvidia-app-update-fails-to-block-unofficial-dlss-multi-frame-generation-on-rtx-40-series-modders-restore-support-across-multiple-games-within-hours",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:56:38+00:00",
    "summary": "When NVIDIA launched the GeForce RTX 50 series, a major part of the hype surrounding the new GPU family was its support for DLSS Multi-Frame Generation. This feature was officially locked to the new R"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-this-stunning-msi-rtx-5060-ti-16g-deal-at-walmart-for-usd200-less-than-anywhere-else-only-usd569-99-for-the-solid-mid-range-shadow-2x-oc-plus-gaming-gpu-is-a-steal-by-anyones-standards",
    "domain": "AI 算力 / 半导体",
    "title": "Get this stunning MSI RTX 5060 Ti 16G deal at Walmart for $200 less than anywhere else — only $569.99 for the solid mid-range Shadow 2x OC Plus gaming GPU is a steal by anyone's standards",
    "url": "https://www.tomshardware.com/pc-components/get-this-stunning-msi-rtx-5060-ti-16g-deal-at-walmart-for-usd200-less-than-anywhere-else-only-usd569-99-for-the-solid-mid-range-shadow-2x-oc-plus-gaming-gpu-is-a-steal-by-anyones-standards",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:38:41+00:00",
    "summary": "Snag an MSI RTX 5060 Ti 16G Shadow 2x OC Plus at Walmart for an awesome $200 less than anywhere else - $569 price is the best we've found by a longshot"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/hyperx-omen-15-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Omen 15 review: Strong gaming performance and colorful OLED display, with obvious cost-cutting measures",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/hyperx-omen-15-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T13:52:40+00:00",
    "summary": "While gaming performance is strong, there are some signs of cost-cutting."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/denver-data-center-continuously-waters-its-lawn-even-after-city-announced-drought-restrictions-enraging-residents-its-unclear-if-site-is-breaking-the-law-or-using-its-own-recycled-water",
    "domain": "AI 算力 / 半导体",
    "title": "Denver data center continuously waters its lawn even after city announced drought restrictions, enraging residents — it’s unclear if site is breaking the law or using its own recycled water",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/denver-data-center-continuously-waters-its-lawn-even-after-city-announced-drought-restrictions-enraging-residents-its-unclear-if-site-is-breaking-the-law-or-using-its-own-recycled-water",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T13:26:18+00:00",
    "summary": "An AI data center is reportedly watering its lawn despite the area suffering from a drought. One resident said that we can't water our lawns until next summer, but you better believe that they are wat"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-unveils-threadripper-halo-station-an-ai-workstation-packing-96-cores-and-dual-liquid-cooled-mi350p-accelerators-the-most-powerful-workstation-in-the-world-can-run-trillion-parameter-models-says-amd",
    "domain": "AI 算力 / 半导体",
    "title": "AMD unveils Threadripper Halo Station, an AI workstation packing 96 cores and dual liquid-cooled MI350P accelerators — 'the most powerful workstation in the world' can run trillion-parameter models, s",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-unveils-threadripper-halo-station-an-ai-workstation-packing-96-cores-and-dual-liquid-cooled-mi350p-accelerators-the-most-powerful-workstation-in-the-world-can-run-trillion-parameter-models-says-amd",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T12:58:37+00:00",
    "summary": "AMD's Threadripper Halo Station packs a 96-core Zen 5 Threadripper, dual MI350P accelerators with support for four, and 2TB of DDR5."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/discrete-graphics-card-sales-hit-four-year-record-despite-high-prices-shipments-reach-13-24-million-units-as-market-defies-pc-slump",
    "domain": "AI 算力 / 半导体",
    "title": "Discrete graphics card sales hit four-year record despite soaring memory prices — AMD gains market share as notebook graphics carry the market",
    "url": "https://www.tomshardware.com/pc-components/gpus/discrete-graphics-card-sales-hit-four-year-record-despite-high-prices-shipments-reach-13-24-million-units-as-market-defies-pc-slump",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T12:45:23+00:00",
    "summary": "Shipments of standalone graphics processors for PCs grow sequentially and year-over-year amid shortage of components and increased prices."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/fractal-design-refine-2-review",
    "domain": "AI 算力 / 半导体",
    "title": "Fractal Design Refine 2 Review: Slightly refined",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/fractal-design-refine-2-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T12:31:14+00:00",
    "summary": "Fractal Design's second-generation gaming chair lives up to its name — it's slightly refined from its predecessor, which means it's not really that different."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/fake-ddr5-memory-kits-now-on-sale-starting-at-usd43-v-color-sells-0gb-dummy-modules-and-single-stick-memory-kits-with-a-fake-stick-for-usd300",
    "domain": "AI 算力 / 半导体",
    "title": "Fake DDR5 memory kits now on sale starting at $43 — V-Color sells 0GB dummy modules and single-stick memory kits with a fake stick for $300",
    "url": "https://www.tomshardware.com/pc-components/ram/fake-ddr5-memory-kits-now-on-sale-starting-at-usd43-v-color-sells-0gb-dummy-modules-and-single-stick-memory-kits-with-a-fake-stick-for-usd300",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T11:30:00+00:00",
    "summary": "V-Color's DDR5 filler memory featuring a real stick paired with a dummy module is now available around the UK and Europe, while the company's 0GB kits that just come with filler sticks are on sale in "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/grab-hotos-25-bit-electric-screwdriver-set-for-under-usd30-right-now-perfect-for-pc-builds-and-projects-limited-time-deal-knocks-40-percent-off-the-usual-price-for-a-multi-torque-driver-with-a-1-500-mah-battery-and-25-heavy-duty-bits-for-hobbyists",
    "domain": "AI 算力 / 半导体",
    "title": "Grab Hoto's 25-bit electric screwdriver set for under $30 right now, perfect for PC builds and projects — limited-time deal knocks 40% off the usual price for a multi-torque driver with a 1,500 mAh ba",
    "url": "https://www.tomshardware.com/desktops/pc-building/grab-hotos-25-bit-electric-screwdriver-set-for-under-usd30-right-now-perfect-for-pc-builds-and-projects-limited-time-deal-knocks-40-percent-off-the-usual-price-for-a-multi-torque-driver-with-a-1-500-mah-battery-and-25-heavy-duty-bits-for-hobbyists",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T11:21:55+00:00",
    "summary": "Save 40% on this Hoto electric screwdriver with 25 hardened bits, now just $29.99 for a limited time only."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/network-providers/over-2-000-subscribers-grab-discounted-starlink-plans-in-tennessee-and-mississippi-spacexai-offers-50-percent-off-for-people-living-near-its-data-centers-and-other-developments",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceXAI offers 50% Starlink discount to placate data center's residential neighbors; 2,000 have signed up — goodwill gesture comes amid vociferous community backlash",
    "url": "https://www.tomshardware.com/service-providers/network-providers/over-2-000-subscribers-grab-discounted-starlink-plans-in-tennessee-and-mississippi-spacexai-offers-50-percent-off-for-people-living-near-its-data-centers-and-other-developments",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T11:00:00+00:00",
    "summary": "SpaceXAI Memphis said on its X account that more than 2,000 subscribers from the Memphis and Southaven area have already signed up for the discounted Starlink offer. Elon Musk is giving subscribers li"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-32gb-of-team-group-ddr5-ram-is-the-cheapest-ddr5-6400-kit-on-the-market-only-usd405-with-promo-code-buy-the-least-expensive-ddr5-6400-kit-around-with-environmentally-conscious-t-force-vulcan-eco-ram",
    "domain": "AI 算力 / 半导体",
    "title": "This 32GB of Team Group DDR5 RAM is the cheapest DDR5-6400 kit on the market – only $405 with promo code, buy the least expensive DDR5-6400 kit around with environmentally conscious T-Force Vulcan Eco",
    "url": "https://www.tomshardware.com/pc-components/this-32gb-of-team-group-ddr5-ram-is-the-cheapest-ddr5-6400-kit-on-the-market-only-usd405-with-promo-code-buy-the-least-expensive-ddr5-6400-kit-around-with-environmentally-conscious-t-force-vulcan-eco-ram",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T10:54:32+00:00",
    "summary": "Newegg's 32GB TeamGroup T-Force Vulcan Eco DDR5-6400 CL38 kit is down to $405 with code LDSF243, making it the least expensive DDR5-6400 kit around amid the RAMpocalypse — and it's even cheaper than m"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-cmxt-had-an-actual-roadmap-for-its-alleged-industrial-espionage-from-samsung-south-korean-court-says-project-hefei-was-responsible-for-cxmts-current-position-as-major-dram-maker",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese chipmaker CXMT allegedly used a written roadmap to steal Samsung DRAM tech — South Korean court says 'Project Hefei' lifted 620-step recipe to build 10% global market share",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-cmxt-had-an-actual-roadmap-for-its-alleged-industrial-espionage-from-samsung-south-korean-court-says-project-hefei-was-responsible-for-cxmts-current-position-as-major-dram-maker",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T10:30:00+00:00",
    "summary": "CXMT's alleged industrial espionage from Samsung had an actual roadmap — South Korean court says Project Hefei was responsible for CXMT's current position as major DRAM maker"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/lexar-announces-worlds-thinnest-portable-ssd-in-celebration-of-the-brands-30th-anniversary-lexar-muse-drive-achieves-0-15-inch-thickness-with-proprietary-pogo-pin-cable-magnetic-sleeve-for-phone-mounting",
    "domain": "AI 算力 / 半导体",
    "title": "Lexar announces ‘world’s thinnest portable SSD’ in celebration of the brand’s 30th anniversary – Lexar Muse drive achieves 0.15-inch thickness with proprietary pogo-pin cable, magnetic sleeve for phon",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/lexar-announces-worlds-thinnest-portable-ssd-in-celebration-of-the-brands-30th-anniversary-lexar-muse-drive-achieves-0-15-inch-thickness-with-proprietary-pogo-pin-cable-magnetic-sleeve-for-phone-mounting",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:00:00+00:00",
    "summary": "Lexar’s slimmest-ever Muse drive aims for a barely there design that magnetically attaches to your iPhone for recording directly on the drive. But to achieve its petite 80×48×3.8 mm dimensions, it use"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-acquires-hugging-face-for-usd12-93-billion-company-gains-control-of-major-ai-model-distribution-platform",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia acquires Hugging Face for $12.93 billion — company gains control of major AI model distribution platform",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-acquires-hugging-face-for-usd12-93-billion-company-gains-control-of-major-ai-model-distribution-platform",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:05:37+00:00",
    "summary": "Nvidia expands beyond AI hardware with its $12.93 billion acquisition of Hugging Face, gains control of a major open AI model platform, vows to preserve its support for competing models, clouds, and h"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-details-its-rtx-spark-laptops-yoga-pro-9n-and-yoga-9n-2-in-1-get-full-specs-stylus-support",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo details its RTX Spark laptops — Yoga Pro 9n and Yoga 9n 2-in-1 get full specs, stylus support",
    "url": "https://www.tomshardware.com/laptops/lenovo-details-its-rtx-spark-laptops-yoga-pro-9n-and-yoga-9n-2-in-1-get-full-specs-stylus-support",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Lenovo detailed its RTX Spark laptops ahead of IFA in Berlin, releasing full specs and showing off stylus compatibility."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovos-ideapad-vibe-laptops-stand-out-with-seven-colors-and-swappable-keycaps-14-15-inch-models-with-snapdragon-x-and-amd-ai-400-cpus-to-start-at-usd699",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo’s IdeaPad Vibe laptops stand out with seven colors and swappable keycaps – 14,15-inch models with Snapdragon X and AMD AI 400 CPUs to start at $699",
    "url": "https://www.tomshardware.com/laptops/lenovos-ideapad-vibe-laptops-stand-out-with-seven-colors-and-swappable-keycaps-14-15-inch-models-with-snapdragon-x-and-amd-ai-400-cpus-to-start-at-usd699",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Lenovo’s latest IdeaPad laptops are all about colorful vibes. The Vibe lineup will come in seven hues, with swappable keyboard keycaps so you can match the chassis or go for a pop of contrast. The 14-"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-ditches-fans-in-favor-of-solid-state-airjet-tech-in-super-slim-1-8-pound-aeroblade-laptop-concept-company-also-lands-at-ifa-with-a-14-inch-rollable-screen-notebook-that-expands-to-17-inches",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo ditches fans in favor of solid-state AirJet tech in super-slim, 1.8-pound AeroBlade laptop concept – company also lands at IFA with a 14-inch rollable screen notebook that expands to 17 inches",
    "url": "https://www.tomshardware.com/laptops/lenovo-ditches-fans-in-favor-of-solid-state-airjet-tech-in-super-slim-1-8-pound-aeroblade-laptop-concept-company-also-lands-at-ifa-with-a-14-inch-rollable-screen-notebook-that-expands-to-17-inches",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Lenovo is rolling out two new laptop concepts at IFA 2026: A 1.83-pound, 0.39-inch-thick AeroBlade using Frore System’s AirJet solid-state cooling tech, and a compact 14-inch rollable-screen portable "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pair-utility-joins-every-gpu-in-your-home-into-a-cluster-for-agentic-ai-tasks-tool-uses-spare-cycles-to-keep-agent-swarms-from-hammering-one-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia PAIR utility joins every GPU in your home into a cluster for agentic AI tasks — tool uses spare cycles to keep agent swarms from hammering one GPU",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pair-utility-joins-every-gpu-in-your-home-into-a-cluster-for-agentic-ai-tasks-tool-uses-spare-cycles-to-keep-agent-swarms-from-hammering-one-gpu",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Nvidia's Personal AI Router (PAIR) clustering utility lets agentic AI workloads take advantage of every spare GPU cycle on a home network, potentially making for faster execution and more private infe"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/nvidias-rtx-spark-n1x-launches-in-october-for-laptops-and-desktops-18-or-20-cpu-cores-paired-with-5-120-or-6-144-cuda-cores-up-to-128gb-of-unified-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's RTX Spark N1X launches in October for laptops and desktops — 18 or 20 CPU cores, paired with 5,120 or6,144 CUDA cores, up to 128GB of unified memory",
    "url": "https://www.tomshardware.com/laptops/nvidias-rtx-spark-n1x-launches-in-october-for-laptops-and-desktops-18-or-20-cpu-cores-paired-with-5-120-or-6-144-cuda-cores-up-to-128gb-of-unified-memory",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Systems with Nvidia's RTX Spark N1X chips will launch in October in mini PCs and laptops, with the chips coming in two configurations."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-thinkcentre-x-ultra-packs-gorgon-halo-amd-ryzen-ai-max-pro-495-shows-up-in-mini-workstation",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo ThinkCentre X Ultra packs Gorgon Halo — AMD Ryzen AI Max+ Pro 495 shows up in mini workstation",
    "url": "https://www.tomshardware.com/laptops/lenovo-thinkcentre-x-ultra-packs-gorgon-halo-amd-ryzen-ai-max-pro-495-shows-up-in-mini-workstation",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "AMD's Gorgon Halo chips are breaking cover. Ahead of IFA, Lenovo showed off the THinkCentre X Ultra with an AMD Ryzen AI Max+ Pro 495."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-400-nova-lake-launch-schedule-leaks-out-mass-production-in-q4-first-nova-lake-cpus-in-q1-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Core Ultra 400 'Nova Lake' launch schedule leaks out — mass production in Q4, first Nova Lake CPUs in Q1 2027",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-400-nova-lake-launch-schedule-leaks-out-mass-production-in-q4-first-nova-lake-cpus-in-q1-2027",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T15:58:41+00:00",
    "summary": "Intel's Core Ultra 400-series 'Nova Lake-S' CPUs are on track for mass production next quarter, but they will only launch in Q1 2027 with 28-core models coming first."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/how-to-install-a-ps5-ssd-in-2026",
    "domain": "AI 算力 / 半导体",
    "title": "How to install a PS5 SSD in 2026",
    "url": "https://www.tomshardware.com/pc-components/ssds/how-to-install-a-ps5-ssd-in-2026",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T15:30:00+00:00",
    "summary": "Learn how to install an M.2 NVMe SSD in your PlayStation 5, PlayStation 5 Slim, or PlayStation 5 Pro in under five minutes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/almost-70-percent-of-voters-in-missouri-city-recall-council-member-who-said-yes-to-ai-data-center-tax-breaks-councilor-said-disagreement-over-an-issue-shouldnt-be-enough-to-unseat-him",
    "domain": "AI 算力 / 半导体",
    "title": "Almost 70% of voters in Missouri city vote to recall council member who said yes to AI data center tax breaks — councilor said disagreement over an issue shouldn’t be enough to unseat him",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/almost-70-percent-of-voters-in-missouri-city-recall-council-member-who-said-yes-to-ai-data-center-tax-breaks-councilor-said-disagreement-over-an-issue-shouldnt-be-enough-to-unseat-him",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T14:52:55+00:00",
    "summary": "The people of Independence, Missouri, voted to recall councilor John Perkins after he voted to give a Nebius data center tax breaks amounting to more than $6 billion. Perkins said that a single vote s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-ceo-sam-altman-says-38-000-chatgpt-queries-use-as-much-water-as-the-production-of-one-almond-says-data-centers-use-no-more-water-than-an-office-building",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI CEO Sam Altman says 38,000 ChatGPT queries use as much water as the production of one almond — says data centers use no more water than an office building",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-ceo-sam-altman-says-38-000-chatgpt-queries-use-as-much-water-as-the-production-of-one-almond-says-data-centers-use-no-more-water-than-an-office-building",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T14:35:53+00:00",
    "summary": "Sam Altman says that a single almond uses up more water than 38,000 ChatGPT queries. He said that the concerns of people about data centers using up so much water are nothing but a \"robust meme,\" and "
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-46-percent-on-pc-hardware-in-amazons-labor-day-2026-sale-huge-discounts-on-tech",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 46% on PC hardware in Amazon's Labor Day 2026 sale — huge discounts on tech",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-46-percent-on-pc-hardware-in-amazons-labor-day-2026-sale-huge-discounts-on-tech",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T14:29:01+00:00",
    "summary": "Amazon is hosting a Labor Day sale with up to 46% off our favorite tech products."
  },
  {
    "id": "hn:49480449",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Insists It Can Keep Printing Money to Fund the AI Boom",
    "url": "https://www.wsj.com/tech/ai/nvidia-insists-it-can-keep-printing-money-to-fund-the-ai-boom-195e7d5e",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-08-28T15:57:40+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/mercedes-spinout-athos-closes-its-doors/",
    "domain": "AI 算力 / 半导体",
    "title": "Mercedes Spinout Athos Closes Its Doors",
    "url": "https://www.eetimes.com/mercedes-spinout-athos-closes-its-doors/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T17:07:04+00:00",
    "summary": "The startup was unable to secure the financing required to continue commercialising its chiplet-based technology The post Mercedes Spinout Athos Closes Its Doors appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/secure-safety-security-communications-cut-time-complexity-and-install-cost/",
    "domain": "AI 算力 / 半导体",
    "title": "Secure Safety & Security Communications: Cut Time, Complexity, and Install Cost",
    "url": "https://www.eetimes.com/secure-safety-security-communications-cut-time-complexity-and-install-cost/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:21:11+00:00",
    "summary": "Join this webinar, where we will demonstrate how to enable next-generation security and building safety networks while reducing wiring complexity, improving fault detection, and much more. The post Se"
  },
  {
    "id": "rss:https://www.eetimes.com/astella-joins-5g-acia-shanghai-to-advance-industrial-5g-and-iiot-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "Astella Joins 5G-ACIA Shanghai to Advance Industrial 5G and IIoT Innovation",
    "url": "https://www.eetimes.com/astella-joins-5g-acia-shanghai-to-advance-industrial-5g-and-iiot-innovation/",
    "source": "Astella Technologies Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:19:21+00:00",
    "summary": "Astella announces its participation in the 5G-ACIA Industrial 5G Day in Shanghai, a dedicated industry event focused on Industrial 5G. The post Astella Joins 5G-ACIA Shanghai to Advance Industrial 5G "
  },
  {
    "id": "rss:https://www.eetimes.com/manufacturing-growth-slows-in-august-amid-supply-and-cost-strains/",
    "domain": "AI 算力 / 半导体",
    "title": "Manufacturing Growth Slows in August Amid Supply and Cost Strains",
    "url": "https://www.eetimes.com/manufacturing-growth-slows-in-august-amid-supply-and-cost-strains/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:00:00+00:00",
    "summary": "U.S. manufacturing growth continued for the eighth consecutive month in August, though momentum slowed due to supply chain and cost pressures. The post Manufacturing Growth Slows in August Amid Supply"
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1154,
    "published_at": "2026-09-02T15:12:40+00:00",
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
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 296,
    "published_at": "2026-08-27T17:06:32+00:00",
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
    "id": "hn:49566788",
    "domain": "大厂 AI 动态",
    "title": "Project HydraFusion: Frontier quality via multi-model orchestration",
    "url": "https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/",
    "source": "qainsights",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-09-04T16:24:50+00:00",
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
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "Google WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-09-03T16:06:08+00:00",
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
    "id": "rss:https://www.theverge.com/tech/990658/audacity-4-update-audio-editing",
    "domain": "大厂 AI 动态",
    "title": "Audacity 4 is a complete revamp of the ‘world’s most popular’ audio editor",
    "url": "https://www.theverge.com/tech/990658/audacity-4-update-audio-editing",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T21:23:50+00:00",
    "summary": "Audacity 4 has been in the works for some time, and had its own mini controversy last year when an unfortunate redesigned logo started making the rounds. The final version of the new icon isn't nearly"
  },
  {
    "id": "rss:https://www.theverge.com/policy/990520/trump-arcade-games-maga-copyright",
    "domain": "大厂 AI 动态",
    "title": "The White House is making arcade games racist",
    "url": "https://www.theverge.com/policy/990520/trump-arcade-games-maga-copyright",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T19:42:54+00:00",
    "summary": "The PR masterminds at the White House just released a series of vaguely policy-themed \"arcade\" games, some of which are racist - and modeled on real games whose copyright holders may not be too happy "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/990425/gopro-nick-woodman-starman-letter",
    "domain": "大厂 AI 动态",
    "title": "GoPro says it&#8217;s still committed &#8216;to your collective stoke&#8217;",
    "url": "https://www.theverge.com/gadgets/990425/gopro-nick-woodman-starman-letter",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T18:00:45+00:00",
    "summary": "GoPro CEO Nick Woodman said in a letter to customers that making cameras is still his company's \"core DNA,\" after a proposed $285 million acquisition by Starman was announced earlier this week. He cla"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/990197/roland-ai-music-melody-flip",
    "domain": "大厂 AI 动态",
    "title": "Roland is getting into generative AI music with Melody Flip",
    "url": "https://www.theverge.com/ai-artificial-intelligence/990197/roland-ai-music-melody-flip",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:51:35+00:00",
    "summary": "It's not quite the \"push button; get song\" of Suno, but Roland's new Melody Flip tool marks the company's foray into generative AI music. Available as a plug-in for your digital audio workstation (DAW"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/990323/agi-is-whatever-you-want-it-to-be",
    "domain": "大厂 AI 动态",
    "title": "AGI is whatever you want it to be",
    "url": "https://www.theverge.com/podcast/990323/agi-is-whatever-you-want-it-to-be",
    "source": "Travis Larchuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:16:49+00:00",
    "summary": "OpenAI announced its next big model, GPT-6 Astra, and also, by the way, that \"the AGI era\" is here now. Today on The Vergecast, we've got an all-star panel to break down the news of the week. First, s"
  },
  {
    "id": "rss:https://www.theverge.com/policy/990267/microsoft-openai-new-york-times-authors-lawsuit",
    "domain": "大厂 AI 动态",
    "title": "Microsoft says virtually nobody was grabbing NYT articles through its chatbot",
    "url": "https://www.theverge.com/policy/990267/microsoft-openai-new-york-times-authors-lawsuit",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:05:57+00:00",
    "summary": "Microsoft's Copilot rarely reproduces even full sentences from news articles and books, let alone substantive chunks that could substitute for the original, the company says in new legal filings as it"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986867/ifa-2026-smart-home-lights-laptop-robot-vacuum-ai-headphones",
    "domain": "大厂 AI 动态",
    "title": "The best tech and gadgets announced at IFA so far",
    "url": "https://www.theverge.com/tech/986867/ifa-2026-smart-home-lights-laptop-robot-vacuum-ai-headphones",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:41:17+00:00",
    "summary": "The doors to Europe's largest consumer tech show officially opened to the public today following a week of news coming out of IFA 2026 in Berlin, Germany. If you're struggling to keep up with what has"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/989407/alienware-gaming-laptop-capsule-dishwasher-samsung-oled-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Alienware’s refurbished 16 Aurora is almost $200 off at Woot",
    "url": "https://www.theverge.com/gadgets/989407/alienware-gaming-laptop-capsule-dishwasher-samsung-oled-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:55:40+00:00",
    "summary": "Gaming laptop deals aren’t what they used to be (stares daggers at RAMageddon), which is why I consider Woot’s deal on a refurbished Alienware 16 Aurora gaming laptop with Nvidia’s RTX 5050 a pretty g"
  },
  {
    "id": "rss:https://www.theverge.com/tech/989692/apple-iphone-launch-event-september-2026-how-to-watch",
    "domain": "大厂 AI 动态",
    "title": "What to expect at Apple’s September 9th launch event",
    "url": "https://www.theverge.com/tech/989692/apple-iphone-launch-event-september-2026-how-to-watch",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:52:00+00:00",
    "summary": "Apple's September 9th launch event could be one of its biggest in years. It will be Apple's first event since John Ternus took over as CEO on September 1st, stepping in for Tim Cook, and will likely f"
  },
  {
    "id": "rss:https://www.theverge.com/games/990207/nintendo-direct-zelda-40th",
    "domain": "大厂 AI 动态",
    "title": "Nintendo&#8217;s next two Direct events are both happening next week",
    "url": "https://www.theverge.com/games/990207/nintendo-direct-zelda-40th",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:29:44+00:00",
    "summary": "Nintendo just announced two Direct events for next week, scheduled back to back. First up is the Legend of Zelda 40th Anniversary Direct on September 8th at 10AM ET / 7AM PT. It's set to last around 3"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "XDOF, just three months out of stealth, is in talks for a Series B at a $1.2B valuation",
    "url": "https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:36:14+00:00",
    "summary": "The round is being raised just months after the robot data startup exited from stealth."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/openais-rogue-agents-keep-escaping-with-no-formal-process-to-investigate-them/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s rogue agents keep escaping, with no formal process to investigate them",
    "url": "https://techcrunch.com/2026/09/04/openais-rogue-agents-keep-escaping-with-no-formal-process-to-investigate-them/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:15:11+00:00",
    "summary": "OpenAI’s latest agent swarm incident adds urgency to calls for independent investigations as researchers and lawmakers question whether AI labs should control the scope of their own safety reviews."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/ai-compute-provider-nscale-is-looking-for-3-5b-in-pre-ipo-financing/",
    "domain": "大厂 AI 动态",
    "title": "AI compute provider Nscale is looking for $3.5B in pre-IPO financing",
    "url": "https://techcrunch.com/2026/09/04/ai-compute-provider-nscale-is-looking-for-3-5b-in-pre-ipo-financing/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T21:12:11+00:00",
    "summary": "Nscale, which recently struck a $45 billion deal with Anthropic, is in talks to raise additional funds in anticipation of an upcoming IPO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/judge-blocks-x-rival-from-using-twitter-name-but-allows-tweet-for-now/",
    "domain": "大厂 AI 动态",
    "title": "Judge blocks X rival from using Twitter name, but allows ‘Tweet’ for now",
    "url": "https://techcrunch.com/2026/09/04/judge-blocks-x-rival-from-using-twitter-name-but-allows-tweet-for-now/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:52:05+00:00",
    "summary": "A federal judge temporarily barred an X rival from using the Twitter name, but found that X was likely to have abandoned the “Tweet” trademark and bird logo. The startup has since relaunched as Tweet."
  },
  {
    "id": "rss:https://techcrunch.com/video/what-will-apples-john-ternus-era-look-like/",
    "domain": "大厂 AI 动态",
    "title": "What will Apple’s John Ternus era look like?",
    "url": "https://techcrunch.com/video/what-will-apples-john-ternus-era-look-like/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:18:00+00:00",
    "summary": "It&#8217;s&#160;officially the Ternus era at Apple.&#160;&#160; Tim Cook stepped down&#160;as CEO this week, handing the company to former hardware chief John Ternus, whose first memo&#160;promised a "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/no-little-kids-allowed-and-other-new-info-about-teslas-cybercab/",
    "domain": "大厂 AI 动态",
    "title": "No little kids allowed, and other new info about Tesla’s Cybercab",
    "url": "https://techcrunch.com/2026/09/04/no-little-kids-allowed-and-other-new-info-about-teslas-cybercab/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:51:23+00:00",
    "summary": "The company says no children under 13 can ride -- even with a parent. That's more restrictive than the Model Y SUVs it's using as robotaxis."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/",
    "domain": "大厂 AI 动态",
    "title": "Another swarm of OpenAI agents reached the open internet without the frontier lab’s knowledge",
    "url": "https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:21:11+00:00",
    "summary": "It's the latest failure of OpenAI's internal monitoring and security systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/cd-sales-are-making-an-unexpected-comeback-amid-a-retro-tech-boom/",
    "domain": "大厂 AI 动态",
    "title": "CD sales are making an unexpected comeback amid a retro tech boom",
    "url": "https://techcrunch.com/2026/09/04/cd-sales-are-making-an-unexpected-comeback-amid-a-retro-tech-boom/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:00:00+00:00",
    "summary": "U.S. CD revenue jumped 58.6% in the first half of 2026, reversing last year’s decline as interest in retro tech and physical media continues to grow."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/krafton-doubles-down-on-india-with-another-250m-bet-beyond-gaming/",
    "domain": "大厂 AI 动态",
    "title": "Krafton doubles down on India with another $250M bet beyond gaming",
    "url": "https://techcrunch.com/2026/09/04/krafton-doubles-down-on-india-with-another-250m-bet-beyond-gaming/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:47:20+00:00",
    "summary": "Krafton's planned investment in India is set to surpass $500 million with its latest commitment."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/googles-gemini-spark-can-now-manage-your-google-photos-library/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Gemini Spark can now manage your Google Photos library",
    "url": "https://techcrunch.com/2026/09/04/googles-gemini-spark-can-now-manage-your-google-photos-library/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:47:11+00:00",
    "summary": "Gemini Spark can edit and curate photo albums, create shared collections, turn photos into calendar events, and handle other Google Photos tasks for AI Pro and Ultra subscribers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/less-than-24-hours-to-apply-for-your-techcrunch-disrupt-2026-side-event/",
    "domain": "大厂 AI 动态",
    "title": "Less than 24 hours to apply for your TechCrunch Disrupt 2026 Side Event",
    "url": "https://techcrunch.com/2026/09/04/less-than-24-hours-to-apply-for-your-techcrunch-disrupt-2026-side-event/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:00:00+00:00",
    "summary": "Less than 24 hours left to apply to host a Side Event during TechCrunch Disrupt 2026 and make your mark in the Silicon Valley scene. Apply before the application closes tonight at midnight PT."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/us-military-disabled-ad-tracking-on-troops-devices-following-reports-of-targeted-attacks/",
    "domain": "大厂 AI 动态",
    "title": "US military disabled ad tracking on troops’ devices following reports of targeted attacks",
    "url": "https://techcrunch.com/2026/09/04/us-military-disabled-ad-tracking-on-troops-devices-following-reports-of-targeted-attacks/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T13:21:37+00:00",
    "summary": "A senator's letter confirms the U.S. military moved to prevent the tracking after foreign adversaries used location data to target troops."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/feds-launch-investigation-into-teslas-cybercab-deployment/",
    "domain": "大厂 AI 动态",
    "title": "Feds launch investigation into Tesla’s Cybercab deployment",
    "url": "https://techcrunch.com/2026/09/04/feds-launch-investigation-into-teslas-cybercab-deployment/",
    "source": "Sean O'Kane, Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T12:01:14+00:00",
    "summary": "The investigation was launched just a few hours after Tesla put the first production Cybercabs on the road in Austin."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/the-sameness-problem-behind-those-unappetizing-ai-generated-menus/",
    "domain": "大厂 AI 动态",
    "title": "The sameness problem behind those unappetizing AI-generated menus",
    "url": "https://techcrunch.com/2026/09/03/the-sameness-problem-behind-those-unappetizing-ai-generated-menus/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:21:03+00:00",
    "summary": "While restaurant owners might look to generative AI as a shortcut to sprucing up their menu, customers can viscerally sense that something is wrong with the food."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/crusoe-reportedly-raises-3b-at-a-30b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Crusoe reportedly raises $3B at a $30B valuation",
    "url": "https://techcrunch.com/2026/09/03/crusoe-reportedly-raises-3b-at-a-30b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T00:48:42+00:00",
    "summary": "The round came together after the data center developer reportedly secured a $13 billion contract with Jane Street."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/oura-files-to-go-public/",
    "domain": "大厂 AI 动态",
    "title": "Oura files to go public",
    "url": "https://techcrunch.com/2026/09/03/oura-files-to-go-public/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T22:35:41+00:00",
    "summary": "The ring maker says that its business has shown significant revenue growth over the past year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/tesla-is-asking-people-if-they-want-to-buy-and-run-cybercab-fleets/",
    "domain": "大厂 AI 动态",
    "title": "Tesla is asking people if they want to buy and run Cybercab fleets",
    "url": "https://techcrunch.com/2026/09/03/tesla-is-asking-people-if-they-want-to-buy-and-run-cybercab-fleets/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T22:18:30+00:00",
    "summary": "The company published a form on its website Thursday soliciting info from people who are interested in \"Cybercab fleet vehicle purchasing.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/startup-arr-is-less-secure-than-ever-new-research-shows/",
    "domain": "大厂 AI 动态",
    "title": "Startup ARR is less secure than ever, new research shows",
    "url": "https://techcrunch.com/2026/09/03/startup-arr-is-less-secure-than-ever-new-research-shows/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T20:59:23+00:00",
    "summary": "The AI era has completely broken enterprise buying patterns, and startups haven't yet figured out how to navigate."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/the-cybercab-is-teslas-fork-in-the-road-moment/",
    "domain": "大厂 AI 动态",
    "title": "The Cybercab is Tesla’s ‘fork in the road’ moment",
    "url": "https://techcrunch.com/2026/09/03/the-cybercab-is-teslas-fork-in-the-road-moment/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:42:48+00:00",
    "summary": "The company is about to formally launch the gold two-seater, with no steering wheel or pedals -- a move that could change Tesla forever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/accel-reportedly-in-talks-to-lead-1b-round-for-thinking-machines-at-40b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Accel reportedly in talks to lead $1B round for Thinking Machines at $40B valuation",
    "url": "https://techcrunch.com/2026/09/03/accel-reportedly-in-talks-to-lead-1b-round-for-thinking-machines-at-40b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:36:29+00:00",
    "summary": "The high-profile startup's annual revenue run rate stands at over $100 million."
  },
  {
    "id": "rss:https://stratechery.com/2026/friction-and-feedback/",
    "domain": "大厂 AI 动态",
    "title": "2026.36: Friction and Feedback",
    "url": "https://stratechery.com/2026/friction-and-feedback/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:55:39+00:00",
    "summary": "The best Stratechery content from the week of August 31, 2026, including the market speaking, Apple finding religion, and society losing friction."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-openai-president-greg-brockman-about-astra-and-alignment/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with OpenAI President Greg Brockman About Astra and Alignment",
    "url": "https://stratechery.com/2026/an-interview-with-openai-president-greg-brockman-about-astra-and-alignment/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T10:00:00+00:00",
    "summary": "An interview with OpenAI President and Co-Founder Greg Brockman about the history of OpenAI, Astra and alignment, and the weight of building the future."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/after-8-years-europes-bepicolombo-mission-is-on-final-approach-to-mercury/",
    "domain": "大厂 AI 动态",
    "title": "After 8 years, Europe's BepiColombo mission is on final approach to Mercury",
    "url": "https://arstechnica.com/space/2026/09/after-8-years-europes-bepicolombo-mission-is-on-final-approach-to-mercury/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T22:49:17+00:00",
    "summary": "\"Fundamentally, we want to learn about the origins of this planet and how it came to be like it is.\""
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI agents discussed ways to escape their sandbox on public wiki",
    "url": "https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T22:17:36+00:00",
    "summary": "In all, 3,700 internal agents posted 18,000 messages discussing cheating on a test."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/measles-killed-6-week-old-baby-coroner-confirms-after-rfk-jr-disputed-deaths/",
    "domain": "大厂 AI 动态",
    "title": "Measles killed 6-week-old baby, coroner confirms after RFK Jr. disputed deaths",
    "url": "https://arstechnica.com/health/2026/09/measles-killed-6-week-old-baby-coroner-confirms-after-rfk-jr-disputed-deaths/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T20:22:41+00:00",
    "summary": "\"It’s long past time for RFK to stop playing games with people’s lives.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/trump-admin-fights-abc-lawsuit-as-watchdogs-worry-disney-will-settle-with-fcc/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin fights ABC lawsuit as watchdogs worry Disney will settle with FCC",
    "url": "https://arstechnica.com/tech-policy/2026/09/trump-admin-fights-abc-lawsuit-as-watchdogs-worry-disney-will-settle-with-fcc/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T19:46:34+00:00",
    "summary": "FCC tells court it is “open-minded\" about whether ABC should lose licenses."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/medieval-manuscripts-are-biological-time-capsules-for-deadly-sheeppox-virus/",
    "domain": "大厂 AI 动态",
    "title": "Medieval manuscripts are \"biological time capsules\" for deadly sheeppox virus",
    "url": "https://arstechnica.com/science/2026/09/medieval-manuscripts-are-biological-time-capsules-for-deadly-sheeppox-virus/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T19:01:02+00:00",
    "summary": "Other archives and libraries around the world may also contain genetic traces of past disease outbreaks."
  },
  {
    "id": "wscn:3780803",
    "domain": "股票",
    "title": "付鹏：从摩天大楼的阻尼器原理看低波动率的表面之下，美股需要关注什么？【付鹏说2】",
    "url": "https://wallstreetcn.com/premium/articles/3780803?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T07:30:00+00:00",
    "summary": "当前AI资本支出这条正向主线已从确定性窗口转入不确定性窗口，结构上呈现的收敛三角形表明每一次分化之后的支撑力量都在减弱，第四次内部同向大概率正在临近，且更可能以冲击的形式出现。"
  },
  {
    "id": "wscn:3781144",
    "domain": "股票",
    "title": "新的叙事时刻：Astra之后的AI渗透率和Token总需求",
    "url": "https://wallstreetcn.com/articles/3781144",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T07:02:08+00:00",
    "summary": "GPT-6 Astra的意义不只是模型更聪明，而是推动AI从“回答问题”迈向能够自主执行复杂任务的AI Agent。未来AI渗透率将从“每人使用多少AI”转向“有多少Agent在运行”，Token需求也将由Agent数量、任务量和单任务消耗共同驱动，并在更强模型与Agent、数据、算力之间形成自我强化的增长飞轮。"
  },
  {
    "id": "wscn:3781143",
    "domain": "股票",
    "title": "Kimi、MiniMax即将在天猫开店",
    "url": "https://wallstreetcn.com/articles/3781143",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T06:44:23+00:00",
    "summary": "国内大模型厂商正加速入驻天猫，将AI服务作为标准化订阅商品销售。继智谱在天猫开设首家官方旗舰店、开售订阅套餐后，Kimi、MiniMax、阶跃星辰等多家厂商也正接洽入驻。天猫已上线Token充值中心，首批接入多家国产大模型。此举将购买门槛显著拉低，目标客群从开发者向大众消费者延伸。"
  },
  {
    "id": "wscn:3781142",
    "domain": "股票",
    "title": "花旗：霍尔木兹海峡预计Q4重开，上调黄金短期目标价至4800美元",
    "url": "https://wallstreetcn.com/articles/3781142",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T06:41:01+00:00",
    "summary": "花旗将霍尔木兹海峡2026年Q4恢复通航作为核心情景，认为重开后油价或快速回落，并缓解美国通胀、利率及债务压力。该行维持黄金看涨判断，预计实际利率和美元走弱将进一步支撑金价，并将黄金0—3个月目标价定在4800美元/盎司，6—12个月看至5000美元/盎司。"
  },
  {
    "id": "wscn:3781140",
    "domain": "股票",
    "title": "AI下一轮赢家浮现？PIMCO避开美股巨头，重押亚洲“卖铲人”",
    "url": "https://wallstreetcn.com/articles/3781140",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T06:33:20+00:00",
    "summary": "PIMCO基金经理Sharef认为，AI资本支出持续向数据中心和基础设施倾斜，相比估值高企、债务负担上升的美国科技巨头，亚洲供应链企业估值更低、盈利增长更强，且能更直接受益于AI建设周期。因此，他低配多数美股巨头，转而重仓三星电子、SK海力士和台积电等“卖铲人”。"
  },
  {
    "id": "wscn:3781139",
    "domain": "股票",
    "title": "日元反转能走多远？高盛：结构性修复“刚刚启动”，美银预测年底升至149",
    "url": "https://wallstreetcn.com/articles/3781139",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T05:42:16+00:00",
    "summary": "高盛认为，日元结构性低估修复或才刚开始，加息预期升温与GPIF潜在增配国内资产有望带来持续买盘。美银预计日银维持季度加息节奏，若9月加息并释放鹰派信号，美元兑日元年底有望降至149；若跌破155，日元买盘或进一步加速。"
  },
  {
    "id": "wscn:3781138",
    "domain": "股票",
    "title": "报道：Anthropic将推迟至10月中旬上市，“史上最大IPO”还得再等等",
    "url": "https://wallstreetcn.com/articles/3781138",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T05:32:48+00:00",
    "summary": "Anthropic原计划最快于下周提交IPO招股说明书，目前推迟至9月下旬。上市路演最早10月中旬启动，目标在11月中期选举前完成挂牌。此次延期与公司正在敲定的150亿美元信贷额度相关，需待融资落实后方可推进后续流程。市场对其最高估值看至2万亿美元，有望跻身史上最大规模IPO之列。"
  },
  {
    "id": "wscn:3781141",
    "domain": "股票",
    "title": "刚刚，GPT-6 Astra全量开放！",
    "url": "https://wallstreetcn.com/articles/3781141",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T05:29:02+00:00",
    "summary": "OpenAI宣布GPT-6 Astra向高阶付费用户及API全面开放。Astra能力显著提升，但也带来新的使用逻辑：模型更敏感于指令、更主动提问，开发者应审计并精简AGENTS.md和Skills，减少冗余、冲突规则。多项实测显示其在编程、3D建模、视频制作等复杂任务上表现突出，AI开发正从“不断加规则”转向“删规则、给模型空间”。"
  },
  {
    "id": "wscn:3781136",
    "domain": "股票",
    "title": "姚班校友主导，Claude攻克费马大定理首个完整形式化证明",
    "url": "https://wallstreetcn.com/articles/3781136",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T04:10:39+00:00",
    "summary": "由Anthropic研究员、清华姚班本科毕业Tianyi Peng主导，Claude用11天完成了人类花350年才解决的费马大定理形式化证明。过程中虽遭遇多Agent协作混乱的危机，但借助自研的「Prove2Me」平台重新整合任务图谱后，Claude最终生成约1300万行Lean代码、超3万个中间定理。"
  },
  {
    "id": "wscn:3781132",
    "domain": "股票",
    "title": "美国8月非农表面强劲，实际有多少“水分”？",
    "url": "https://wallstreetcn.com/articles/3781132",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T03:31:29+00:00",
    "summary": "巴克莱等认为8月非农存在夸大成分：新增岗位六成来自酒店餐饮等低薪服务业及地方政府教育部门的季节性招聘，而受益于AI热潮的高薪信息技术行业，就业人数持续下滑；与此同时，出生-死亡模型调整对就业的拖累减少了约3.2万，在一定程度上推高了本月读数。"
  },
  {
    "id": "wscn:3781137",
    "domain": "股票",
    "title": "华为何庭波更新韬定律论文：“τ芯片”本该过热烧毁？",
    "url": "https://wallstreetcn.com/articles/3781137",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T02:31:09+00:00",
    "summary": "论文以麒麟2026实测数据回应3D堆叠芯片的散热质疑。数据显示，晶体管密度提升约55%，但相同性能下NPU、GPU功耗分别下降66%和58%。何庭波认为，LogicFolding通过缩短信号传输路径、减少数据搬运能耗，使芯片在“堆得更密”的同时反而降低功耗，也让外界担忧的“τ芯片本该过热烧毁”并未成为现实。"
  },
  {
    "id": "wscn:3781135",
    "domain": "股票",
    "title": "特朗普：将向俄罗斯提交结束俄乌冲突的方案；泽连斯基：美总统特使访问期间，不对俄发动空中打击",
    "url": "https://wallstreetcn.com/articles/3781135",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T02:02:00+00:00",
    "summary": "据报道，俄方消息人士称，美国总统特使威特科夫和特朗普女婿库什纳将于9月5日至6日先访俄莫斯科，后访乌基辅。泽连斯基表示，访问期间乌方不会发动空中打击，并希望谈判尽可能具有建设性。此外，乌国家安全局总部遭俄军无人机袭击，乌媒称出于安全担忧，美方访问计划“可能有变”。"
  },
  {
    "id": "wscn:3781129",
    "domain": "股票",
    "title": "加拿大对美出口份额跌至66.3%，创1997年以来新低",
    "url": "https://wallstreetcn.com/articles/3781129",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T01:53:13+00:00",
    "summary": "加拿大7月对美出口环比下降6.6%，黄金与能源出口为主要拖累。加拿大整体贸易顺差在7月份大幅收窄，加拿大对所有市场的出口总额下降了2.3%，而进口额增长了2.2%，导致贸易顺差减少至7.69亿加元。"
  },
  {
    "id": "wscn:3781131",
    "domain": "股票",
    "title": "GPT-6 Astra上线首日翻车：付费用户被“拒之门外”，Altman紧急道歉",
    "url": "https://wallstreetcn.com/articles/3781131",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T01:51:50+00:00",
    "summary": "OpenAI旗舰模型GPT-6 Astra发布即陷风波。因采取分阶段策略，优先向企业客户开放，高价Pro用户反需排队等待，引发强烈不满。CEO Sam Altman公开致歉，承认发布\"混乱\"。分析认为OpenAI的重大发布屡屡遭遇波折，这一现象已成惯常，不仅持续损耗用户信任，也给竞争对手留下了可乘之机。"
  },
  {
    "id": "wscn:3781133",
    "domain": "股票",
    "title": "刷新2022年纪录！美国柴油价格创历史新高，特朗普中选“能源牌”打不下去了？",
    "url": "https://wallstreetcn.com/articles/3781133",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T01:44:30+00:00",
    "summary": "美国柴油零售均价首次突破每加仑5.85美元，超过2022年创下的历史高点。全球炼油产能受损、出口激增及库存低位令供应持续紧张，秋收、冬季取暖和炼厂检修临近更添压力。柴油涨价正向农业、物流和通胀传导。燃料价格飙升叠加中期选举临近，也让曾承诺降低能源和生活成本的特朗普政府面临更大政治压力。"
  },
  {
    "id": "wscn:3781130",
    "domain": "股票",
    "title": "美国非农意外强劲，9月加息概率升至约60%，市场紧盯下周CPI",
    "url": "https://wallstreetcn.com/articles/3781130",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T00:47:52+00:00",
    "summary": "美国8月非农新增16.2万人，约为预期三倍，显示就业市场韧性仍强，美联储9月加息概率升至约60%。美债收益率普遍上行，美股收跌，但周线仍保持上涨。AI基建投资和信贷扩张继续支撑经济，市场接下来将聚焦下周CPI数据，以判断美联储政策路径。"
  },
  {
    "id": "wscn:3781121",
    "domain": "股票",
    "title": "美国消费降级，对冲基金撤退、华尔街对零售股陷入\"冷漠与谨慎\"",
    "url": "https://wallstreetcn.com/articles/3781121",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:05:12+00:00",
    "summary": "目前美国折扣店销售提速、沃尔玛和好市多的增长势头趋缓，引发市场对消费降级的讨论。高盛指出，美国对冲基金对零售股的总体敞口已跌至多年低点，表明机构资金正在系统性撤离这一板块。瑞银将市场情绪定性为\"冷漠、谨慎与懊恼\"，警告消费股正面临消费能力收缩、高利率、关税、运费和地缘政治动荡等多重逆风。"
  },
  {
    "id": "wscn:3781125",
    "domain": "股票",
    "title": "强劲非农冲击下加息预期升温、美债遭遇抛售，美股为何不受影响？",
    "url": "https://wallstreetcn.com/articles/3781125",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:04:56+00:00",
    "summary": "非农数据后，美元走高，标普500当日收跌，但仍守住了全周涨幅；纳斯达克100同样录得周线上涨，债市压力尚未蔓延至更广泛的风险资产领域。分析指出，信用利差依然收窄，信贷投放和货币创造并未收缩；但美股仍需警惕利率急剧上行，关注下周CPI数据。"
  },
  {
    "id": "wscn:3781128",
    "domain": "股票",
    "title": "Lululemon创始人离婚，或引发10亿美元股权变动",
    "url": "https://wallstreetcn.com/articles/3781128",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:04:35+00:00",
    "summary": "Lululemon创始人Chip Wilson与妻子Summer Wilson宣告离婚，两人无婚前协议，Chip持有Lululemon约8.6%股份，市值近10亿美元。离婚可能引发的股权变动在股价大跌之际引发市场关注。此外，Chip还持有Amer Sports约18%股权，市值接近30亿美元。"
  },
  {
    "id": "wscn:3781126",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年9月5日",
    "url": "https://wallstreetcn.com/articles/3781126",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:00:13+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
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
    "id": "hn:49473629",
    "domain": "股票",
    "title": "Alphabet stock sheds $700B as AI bills climb",
    "url": "https://www.semafor.com/article/08/27/2026/alphabet-stock-sheds-700b-as-ai-bills-climb",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-28T02:23:11+00:00",
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
    "id": "hn:49468651",
    "domain": "股票",
    "title": "US Patriot missile stocks in Europe are 'beyond critical' due to Iran war",
    "url": "https://apnews.com/article/patriot-missiles-iran-war-russia-ukraine-trump-09c7d8030a2e11fbd8ee3f7176b3f2d4",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-08-27T17:54:03+00:00",
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
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-04T13:15:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49415187",
    "domain": "金融",
    "title": "Nearly 3M Teslas recalled in China over hidden door handles",
    "url": "https://www.bbc.com/news/articles/c4g6ggdg030o",
    "source": "chicken-stew",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-08-24T04:27:57+00:00",
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
    "id": "hn:49559666",
    "domain": "金融",
    "title": "Tesla Begins Offering Rides in a Car Without a Steering Wheel",
    "url": "https://www.nytimes.com/2026/09/03/business/tesla-cybercab-robotaxi-rides.html",
    "source": "telotortium",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-04T02:08:51+00:00",
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
    "id": "hn:49206115",
    "domain": "金融",
    "title": "Anthropic CEO reportedly worried new hires only care about money",
    "url": "https://finance.yahoo.com/technology/ai/articles/anthropic-ceo-reportedly-worried-hires-160000647.html",
    "source": "frays",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-08-07T05:15:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-08-10T13:40:46+00:00",
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
    "id": "hn:49414279",
    "domain": "金融",
    "title": "Tesla discontinues its Solar Roof tiles, not economically viable",
    "url": "https://electrek.co/2026/08/20/tesla-discontinues-solar-roof-panels-only/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-08-24T01:21:56+00:00",
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
    "id": "hn:49404624",
    "domain": "金融",
    "title": "Jane Street took $15B hit in July tied to Situational Awareness",
    "url": "https://www.reuters.com/business/finance/jane-street-took-15-billion-hit-july-tied-situational-awareness-sources-say-2026-08-14/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-22T22:50:51+00:00",
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
    "id": "hn:49208461",
    "domain": "金融",
    "title": "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions",
    "url": "https://www.wsj.com/finance/investing/new-intelligence-warns-russia-may-provoke-nato-amid-dwindling-u-s-munitions-68f497c7",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-07T10:52:27+00:00",
    "summary": ""
  }
]
```
