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

- 今日日期：`2026-08-15`
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
  "date": "2026-08-15",
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
    "points": 4236071,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1710380,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1658621,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1500360,
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
    "points": 1328668,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1271771,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1121793,
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
    "points": 1054954,
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
    "points": 1044506,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV12omoB4ExF",
    "domain": "AI",
    "title": "黑马程序员全网最全Coze智能体入门到项目实战全套教程，从AI Agent开发入门到6大AI智能体实战项目，涵盖提示词Prompt、RAG、Bot发布微信公众号",
    "url": "http://www.bilibili.com/video/av115713129843205",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 1039773,
    "published_at": "2025-12-15T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：251215\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV1khMX63EjU",
    "domain": "AI",
    "title": "Vibe Coding竞赛，Claude遗憾落败?",
    "url": "http://www.bilibili.com/video/av117030980230736",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 1012315,
    "published_at": "2026-08-05T10:30:00+00:00",
    "summary": "我和源宝打了个赌：半天时间，vibe coding一个活动社交App，看谁做的更好？最后Claude Code居然遗憾落败？这期视频，我们将用秒哒手把手带你走完，从一个简单的想法到App上架应用商店的全套流程！开发过程又发生了哪些趣事？一起来看看～"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 943695,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 873913,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 842217,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 670966,
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
    "points": 618118,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 587133,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 583863,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 565296,
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
    "points": 499119,
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
    "points": 437158,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 420428,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1Tv3i6LEX1",
    "domain": "AI",
    "title": "用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍",
    "url": "http://www.bilibili.com/video/av116996217838997",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 417689,
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
    "points": 396921,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1wugF6YEL3",
    "domain": "AI",
    "title": "再见Claude Code！你好DeepSeek Harness！",
    "url": "http://www.bilibili.com/video/av117089415204498",
    "source": "Lau博士的云组会",
    "platform": "bilibili",
    "points": 311610,
    "published_at": "2026-08-13T17:42:16+00:00",
    "summary": "DeepSeek Harness开源了。看完就两个字：牛逼\n本期视频，Lau博士就带着大家一起，解读DeepSeek 亲手做的这个 Harness，到底有什么不一样。"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 265156,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 236948,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 235711,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 179163,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 178270,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 163680,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 162519,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 156400,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 154574,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 154063,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 131205,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 109403,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93188,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 91206,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 80676,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54044,
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
    "points": 47608,
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
    "points": 46203,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1myM96nETU",
    "domain": "AI",
    "title": "AI 赛博女友！本地部署教程，无需 API、完全免费，8G显存就能跑！实时语音聊天，几乎零延迟，太上头了！| 零度解说",
    "url": "http://www.bilibili.com/video/av117032322339286",
    "source": "零度解说",
    "platform": "bilibili",
    "points": 44455,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "AI 赛博女友一键安装包下载：https://www.freedidi.com/24984.html"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 43794,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 40542,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1Y6uC6TE1m",
    "domain": "AI",
    "title": "疯狂Vibe Coding一周，我烧了近100亿Token，做了5个项目！",
    "url": "http://www.bilibili.com/video/av117080321957877",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 38017,
    "published_at": "2026-08-12T03:12:41+00:00",
    "summary": "项目地址：\nlocal-ops — 本地服务指挥台（零依赖 Python + 原生前端）：https://github.com/laogou717/local-ops\nmd-wechat — 公众号排版工具：https://github.com/laogou717/md-wechat\ndaydream-room — 白日梦陈列室：https://github.com/laogou717/daydr"
  },
  {
    "id": "bvid:BV1dngn6CECd",
    "domain": "AI",
    "title": "🚀只花5元开发了5个复杂项目！DeepSeek V4 Pro深度实测：1M上下文接入Claude Code实测表现竟然接近Kimi K3？Token超便宜！",
    "url": "http://www.bilibili.com/video/av117087234430329",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 36846,
    "published_at": "2026-08-13T08:26:59+00:00",
    "summary": "视频简介：\n\n只花5.36元完成6个复杂编程项目！DeepSeek V4 Pro 0813 接入Claude Code完整实测！\n\nDeepSeek V4 Pro 0813 正式上线，这期视频我直接将它接入 Claude Code，测试它真实的编程开发能力。\n\n测试项目包括 SVG 动画、Three.js 古戈尔齿轮、科幻小说宇宙飞船复刻、南宋古城小游戏、Manim 数学动画、Godot 3D 恐"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35117,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29607,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "hn:49255710",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Risky Business",
    "url": "https://stratechery.com/2026/nvidias-risky-business/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 355,
    "published_at": "2026-08-11T10:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49263340",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning and NeMo Switchyard",
    "url": "https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 261,
    "published_at": "2026-08-11T19:35:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49189234",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Vera Whitepaper Has a Thread Loose",
    "url": "https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread",
    "source": "pella",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-08-05T21:24:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49257947",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning",
    "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4",
    "source": "beklein",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-11T13:26:02+00:00",
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
    "id": "rss:https://www.eetimes.com/an-introduction-to-software-prototyping-unlocking-soc-software-verification-with-profpga-cs/",
    "domain": "AI 算力 / 半导体",
    "title": "An Introduction to Software Prototyping: Unlocking SoC Software Verification with proFPGA CS",
    "url": "https://www.eetimes.com/an-introduction-to-software-prototyping-unlocking-soc-software-verification-with-profpga-cs/",
    "source": "Siemens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T15:22:50+00:00",
    "summary": "Discover how the Veloce™ proFPGA CS platform delivers a flexible, modular architecture that scales across the full spectrum of SoC software verification needs. The post An Introduction to Software Pro"
  },
  {
    "id": "rss:https://www.eetimes.com/intel-at-a-memory-crossroads-again/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel at a Memory Crossroads, Again",
    "url": "https://www.eetimes.com/intel-at-a-memory-crossroads-again/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T13:01:36+00:00",
    "summary": "The CPU specialist heeds a memory comeback while memory chips transform from commodity to AI gold rush. The post Intel at a Memory Crossroads, Again appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/semiconductor-equipment-shifts-to-build-to-print-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "Semiconductor Equipment Shifts To Build-to-Print Manufacturing",
    "url": "https://www.eetimes.com/semiconductor-equipment-shifts-to-build-to-print-manufacturing/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T10:56:17+00:00",
    "summary": "Semiconductor equipment OEMs look to build-to-print for greater capacity. The post Semiconductor Equipment Shifts To Build-to-Print Manufacturing appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/",
    "domain": "AI 算力 / 半导体",
    "title": "Smartphone Makers Squeezed by Soaring Chip Costs",
    "url": "https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T18:47:35+00:00",
    "summary": "Chip costs are gutting smartphone margins; expect pricier iPhones and fewer cheap phones. The post Smartphone Makers Squeezed by Soaring Chip Costs appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/enabling-robot-operating-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Enabling Robot Operating Systems—Introducing the ADI Trinamic Motor Controller ROS1 Driver",
    "url": "https://www.eetimes.com/enabling-robot-operating-systems/",
    "source": "Krizelle Paulene Apostol , Software Systems Engineer, Jamila Macagba , Senior Software Systems Engineer, and Maggie Maralit , Software Systems Design Engineering Manager",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T16:14:17+00:00",
    "summary": "Robot Operating System (ROS) drivers were developed on Analog Devices prod ucts so that they can be readily used within a ROS ecosystem. This article will give an overview on how to use and integrate "
  },
  {
    "id": "rss:https://www.eetimes.com/ais-next-bottleneck-is-public-consent/",
    "domain": "AI 算力 / 半导体",
    "title": "AI’s Next Bottleneck Is Public Consent",
    "url": "https://www.eetimes.com/ais-next-bottleneck-is-public-consent/",
    "source": "Zaheer Ali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T14:13:06+00:00",
    "summary": "AI’s next choke point isn’t chips—it’s public trust as states slow data centers over power, water, and secrecy. The post AI&#8217;s Next Bottleneck Is Public Consent appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/neuromorphic-computing-needs-more-than-novel-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Neuromorphic Computing Needs More Than Novel Chips",
    "url": "https://www.eetimes.com/neuromorphic-computing-needs-more-than-novel-chips/",
    "source": "Isaac Lopez, President, OmniScale Media & Charity Plata, Communications Chair, SC26",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:00:00+00:00",
    "summary": "Katie Schuman on why neuromorphic computing needs HPC engineers, compilers, and shared hardware access to move from promise to practice. The post Neuromorphic Computing Needs More Than Novel Chips app"
  },
  {
    "id": "rss:https://www.eetimes.com/using-agents-to-maximize-nvidia-jetson-memory-usage-at-the-edge/",
    "domain": "AI 算力 / 半导体",
    "title": "Using Agents to Maximize NVIDIA Jetson Memory Usage at the Edge",
    "url": "https://www.eetimes.com/using-agents-to-maximize-nvidia-jetson-memory-usage-at-the-edge/",
    "source": "Morten Block, Global Eng. Director, Segments and Technology go-to-market",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:00:00+00:00",
    "summary": "Discover how NVIDIA Jetson's software optimization stack can reclaim significant memory, enabling teams to run bigger AI workloads at a lower module cost. The post Using Agents to Maximize NVIDIA Jets"
  },
  {
    "id": "rss:https://www.eetimes.com/hong-kong-electronics-fairs-launch-in-october/",
    "domain": "AI 算力 / 半导体",
    "title": "Hong Kong Electronics Fairs Launch in October!",
    "url": "https://www.eetimes.com/hong-kong-electronics-fairs-launch-in-october/",
    "source": "HKTDC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T08:00:00+00:00",
    "summary": "Cutting-Edge Technologies on Display This October, Shaping the Future of Industries The post Hong Kong Electronics Fairs Launch in October! appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/g-skill-trident-z5-neox-rgb-ddr5-6000-c30-2x16gb-review",
    "domain": "AI 算力 / 半导体",
    "title": "G.Skill Trident Z5 NeoX RGB DDR5-6000 C30 2x16GB Review — EXPO ULL memory kit to max out your Ryzen",
    "url": "https://www.tomshardware.com/pc-components/ram/g-skill-trident-z5-neox-rgb-ddr5-6000-c30-2x16gb-review",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T15:30:00+00:00",
    "summary": "G.Skill's Trident Z5 NeoX is the brand's latest series with the AMD EXPO ULL feature, but can the DDR5-6000 C30 prove to be the fastest memory kit for AMD?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/scythe-magoroku-review",
    "domain": "AI 算力 / 半导体",
    "title": "Scythe Magoroku Review: excellent RAM thermals, but needs improvement elsewhere",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/scythe-magoroku-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T14:42:29+00:00",
    "summary": "Scythe is back with another dual-tower air cooler, the Magoroku. This cooler performs best with an Intel Arrow Lake system."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cargo-thieves-rammed-security-escorts-to-hijack-ai-hardware-shipments-in-california",
    "domain": "AI 算力 / 半导体",
    "title": "Cargo thieves ram security escorts to hijack AI hardware shipments in California — brazen thieves employ PIT maneuver, rear-ending tactics to secure goods for the black market",
    "url": "https://www.tomshardware.com/tech-industry/cargo-thieves-rammed-security-escorts-to-hijack-ai-hardware-shipments-in-california",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T14:13:41+00:00",
    "summary": "Cargo thieves knocked two private security escort vehicles out of action on California roads in recent months, then made off with millions of dollars in AI data center hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsung-odyssey-g80hs-6k-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Odyssey G80HS 6K gaming monitor review: Upping the stakes in pixel density",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsung-odyssey-g80hs-6k-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T13:10:42+00:00",
    "summary": "The Samsung Odyssey G80HS is a 32-inch IPS panel with 6K 6144x3456 resolution at 165 Hz plus 3072x1728 pixels at 330 Hz. It packs HDR wide-gamut color, Adaptive-Sync, and plenty of features into its s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/plaintiff-busted-trying-to-use-ai-prompt-injection-to-win-court-case-hides-text-instruction-in-filing-demands-ai-model-reviewing-the-text-should-side-with-him-rumbled-because-of-strange-white-spaces-in-text",
    "domain": "AI 算力 / 半导体",
    "title": "Plaintiff busted trying to use AI prompt injection to win court case, hides text instruction in filing — demands AI model reviewing the text should side with him, rumbled because of strange white spac",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/plaintiff-busted-trying-to-use-ai-prompt-injection-to-win-court-case-hides-text-instruction-in-filing-demands-ai-model-reviewing-the-text-should-side-with-him-rumbled-because-of-strange-white-spaces-in-text",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T12:23:35+00:00",
    "summary": "A self-represented plaintiff in a Connecticut court added a hidden AI prompt injection attack in their filing in a failed attempt to influence a decision. The court bars them from submitting documents"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/us-imposes-up-to-100-percent-tariffs-on-foreign-made-drones-and-components-china-remains-primary-target-as-washington-moves-to-reduce-reliance-on-overseas-suppliers",
    "domain": "AI 算力 / 半导体",
    "title": "US imposes up to 100% tariffs on foreign-made drones and components — China remains primary target as Washington moves to reduce reliance on overseas suppliers",
    "url": "https://www.tomshardware.com/tech-industry/drones/us-imposes-up-to-100-percent-tariffs-on-foreign-made-drones-and-components-china-remains-primary-target-as-washington-moves-to-reduce-reliance-on-overseas-suppliers",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T11:53:06+00:00",
    "summary": "The Trump administration says the new tariffs are necessary for national security and to address the US industry's heavy reliance on foreign-made drones and components, particularly from China."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/raptor-lake-is-a-core-part-of-the-portfolio-for-years-to-come-says-intel-theres-been-a-sudden-inrush-of-demand-for-lga-1700-chips-due-to-ddr5-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Older Raptor Lake CPUs are a ‘core part of the portfolio’ for years to come, says Intel — there’s been a ‘sudden inrush of demand’ for LGA 1700 chips due to DDR5 prices",
    "url": "https://www.tomshardware.com/pc-components/cpus/raptor-lake-is-a-core-part-of-the-portfolio-for-years-to-come-says-intel-theres-been-a-sudden-inrush-of-demand-for-lga-1700-chips-due-to-ddr5-prices",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T11:39:52+00:00",
    "summary": "Intel has seen a “sudden inrush” of demand for Raptor Lake CPUs, and it says they’ll remain a part of the company’s lineup for desktop builders “for years to come.”"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-vp-robert-hallock-sets-nova-lake-expectations-teases-return-to-raptor-lake-for-ddr4-platforms-our-full-1-1-interview-transcript",
    "domain": "AI 算力 / 半导体",
    "title": "Intel VP Robert Hallock sets Nova Lake expectations, teases return to Raptor Lake for DDR4 platforms — our full 1:1 interview transcript",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-vp-robert-hallock-sets-nova-lake-expectations-teases-return-to-raptor-lake-for-ddr4-platforms-our-full-1-1-interview-transcript",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T11:00:00+00:00",
    "summary": "We speak to Robert Hallock, Intel VP & GM of Enthusiast Channel Business, about Nova Lake rumors, how the company is focusing on DIY builders during RAMageddon, and how Raptor Lake refresh induced a p"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/usd29-per-terabyte-makes-this-24tb-seagate-barracuda-one-of-the-best-value-hard-drives-in-todays-market-usd50-off-at-newegg-makes-it-usd200-cheaper-than-the-20tb-version",
    "domain": "AI 算力 / 半导体",
    "title": "$29 per Terabyte makes this 24TB Seagate BarraCuda one of the best-value hard drives in today's market — $50 off at Newegg makes it $200 cheaper than the 20TB version",
    "url": "https://www.tomshardware.com/pc-components/hdds/usd29-per-terabyte-makes-this-24tb-seagate-barracuda-one-of-the-best-value-hard-drives-in-todays-market-usd50-off-at-newegg-makes-it-usd200-cheaper-than-the-20tb-version",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T10:56:15+00:00",
    "summary": "Save $50 on a 24TB Seagate Barracuda Compute HDD at Newegg with the limited-time discount code."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/start-your-pc-gaming-journey-with-this-usd1-100-1080p-gaming-rig-now-usd300-off-rtx-5060-rig-from-newegg-ships-with-a-10-core-intel-cpu-32gb-of-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Start your PC gaming journey with this $1,100 1080p gaming rig, now $300 off — RTX 5060 rig from Newegg ships with a 10-core Intel CPU, 32GB of RAM, and a 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/start-your-pc-gaming-journey-with-this-usd1-100-1080p-gaming-rig-now-usd300-off-rtx-5060-rig-from-newegg-ships-with-a-10-core-intel-cpu-32gb-of-ram-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T10:43:57+00:00",
    "summary": "This pre-built ABS Cyclone Aqua comes with a ten-core Intel Core i5-14400F CPU, an Nvidia GeForce RTX 5060 GPU, a 1TB SSD, and 32GB of RAM, all for $1,099.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-jetson-chip-found-in-russian-cruise-missile-ukraine-claims-presence-in-s-71-monochrome-weapon-may-indicate-use-of-ai-tech",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Jetson chip found in Russian cruise missile, Ukraine claims — presence in S-71 'Monochrome' weapon may indicate use of AI tech",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-jetson-chip-found-in-russian-cruise-missile-ukraine-claims-presence-in-s-71-monochrome-weapon-may-indicate-use-of-ai-tech",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T10:30:00+00:00",
    "summary": "Ukraine intelligence claims that Russia's latest S-71 'Monochrome' cruise missiles use Nvidia's Jetson Orin NX modules with AI capabilities, allegedly for terminal guidance."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/modder-straps-two-desktop-cpu-coolers-to-zte-nubia-z70-ultra-turns-smartphone-into-a-gaming-pc-snapdragon-8-elite-soc-with-24gb-of-ram-runs-the-witcher-3-at-1080p-ultra",
    "domain": "AI 算力 / 半导体",
    "title": "Modder straps two desktop CPU coolers to ZTE handset, turns smartphone into a gaming PC — Snapdragon 8 Elite SoC with 24GB of RAM runs The Witcher 3 at 1080p ultra",
    "url": "https://www.tomshardware.com/pc-components/cooling/modder-straps-two-desktop-cpu-coolers-to-zte-nubia-z70-ultra-turns-smartphone-into-a-gaming-pc-snapdragon-8-elite-soc-with-24gb-of-ram-runs-the-witcher-3-at-1080p-ultra",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T10:00:00+00:00",
    "summary": "The heavily modified ZTE Nubia Z70 Ultra uses two full-size CPU coolers to keep its Snapdragon 8 Elite running under sustained loads, while Termux, Linux and compatibility layers turn it into a makesh"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-borrows-usd4-75-billion-for-general-corporate-purposes-company-gives-no-insight-into-how-it-plans-to-spend-cash-injection",
    "domain": "AI 算力 / 半导体",
    "title": "AMD borrows $4.75 billion for 'general corporate purposes' — company gives no insight into how it plans to spend cash injection",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-borrows-usd4-75-billion-for-general-corporate-purposes-company-gives-no-insight-into-how-it-plans-to-spend-cash-injection",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T09:48:59+00:00",
    "summary": "In a surprising move, AMD announces plans to raise $4.75 billion and does not give a clue how it plans to spend them."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/gigabyte-resurrects-8-year-old-b450-chipset-with-new-motherboards-am4-budget-king-returns-as-another-ddr4-solution-to-exorbitant-ram-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte resurrects 8-year-old B450 chipset with new motherboards — AM4 budget king returns as another DDR4 solution to exorbitant RAM prices",
    "url": "https://www.tomshardware.com/pc-components/motherboards/gigabyte-resurrects-8-year-old-b450-chipset-with-new-motherboards-am4-budget-king-returns-as-another-ddr4-solution-to-exorbitant-ram-prices",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T09:43:55+00:00",
    "summary": "Gigabyte has quietly launched the B450M D3HP and B450M D3HP WIFI6E motherboards based on the AMD B450 chipset, which launched in 2018."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/just-one-instruction-on-amds-2015-era-cpus-gets-you-access-to-platform-security-processor-microcode-and-system-management-interface-exploit-for-15h-and-16h-chip-families-cracks-open-secret-memory-areas",
    "domain": "AI 算力 / 半导体",
    "title": "Just one instruction on AMD's 2015-era CPUs cracks open secret memory areas and gives full hardware-level control — exploit for 15h and 16h chip families gets you access to Platform Security Processor",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/just-one-instruction-on-amds-2015-era-cpus-gets-you-access-to-platform-security-processor-microcode-and-system-management-interface-exploit-for-15h-and-16h-chip-families-cracks-open-secret-memory-areas",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T09:33:09+00:00",
    "summary": "Just one instruction on AMD CPUs gets you access to Platform Security Processor, microcode, and System Management Interface — exploit for 15h and 16h chip families cracks open secret memory areas"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/functioning-version-of-the-first-arcade-video-game-ever-created-heads-to-auction-with-usd200-000-estimate-green-sparkle-2-player-edition-of-computer-space-hails-from-1973",
    "domain": "AI 算力 / 半导体",
    "title": "Functioning version of 'the first arcade video game ever created' heads to auction with $200,000 estimate — green sparkle 2-player edition of Computer Space hails from 1973",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/functioning-version-of-the-first-arcade-video-game-ever-created-heads-to-auction-with-usd200-000-estimate-green-sparkle-2-player-edition-of-computer-space-hails-from-1973",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T09:00:00+00:00",
    "summary": "A games industry veteran is selling off what is 'probably the rarest arcade game in existence' via Boston’s RR Auctions."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-research-xl-core-one-and-core-one-l-all-to-receive-second-generation-upgrades-all-new-orders-get-updated-model-for-free",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa Research XL, Core One, and Core One L all to receive second-generation upgrades — all new orders get updated model for 'free'",
    "url": "https://www.tomshardware.com/3d-printing/prusa-research-xl-core-one-and-core-one-l-all-to-receive-second-generation-upgrades-all-new-orders-get-updated-model-for-free",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T20:35:52+00:00",
    "summary": "Prusa Research just announced that its “entire lineup” of 3D printers is getting second-generation upgrades and a “+” designation. This includes the XL, CORE One, and CORE One L."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/microsofts-nemesis-drops-new-zero-day-privilege-escalation-vulnerability-attack-grants-system-level-privileges-but-it-could-already-be-patched",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft's nemesis drops new zero-day privilege escalation vulnerability — attack grants system-level privileges, but it could already be patched",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/microsofts-nemesis-drops-new-zero-day-privilege-escalation-vulnerability-attack-grants-system-level-privileges-but-it-could-already-be-patched",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T17:36:40+00:00",
    "summary": "Nightmare Eclipse drops ShieldBreak, another Windows zero-day privilege escalation vulnerability, but Microsoft has rushed quickly to block it with Defender"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/near-packaged-optics-gains-ground-aso-the-industry-hedges-against-co-packaged-optics-growing-pains",
    "domain": "AI 算力 / 半导体",
    "title": "Near-packaged optics (NPO) gains ground as the industry hedges against CPO's growing pains — analysts say volume for NPO silicon photonics products will extend until the end of the decade",
    "url": "https://www.tomshardware.com/tech-industry/near-packaged-optics-gains-ground-aso-the-industry-hedges-against-co-packaged-optics-growing-pains",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T16:52:45+00:00",
    "summary": "The case for near-packaged optics (NPO) is strengthening, as the growing pains of co-packaged optics (CPO) become apparent. We explain the material differences between the two technologies as optics a"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-emulation-arrives-on-steam-deck-astro-playroom-showcased-running-at-0-6-fps-milestone-sharpemu-development-shows-promise-despite-unplayable-performance",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 emulation arrives on Steam Deck, Astro Playroom showcased running at 0.6 FPS — milestone SharpEmu development shows promise, despite unplayable performance",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-emulation-arrives-on-steam-deck-astro-playroom-showcased-running-at-0-6-fps-milestone-sharpemu-development-shows-promise-despite-unplayable-performance",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:37:59+00:00",
    "summary": "Astro's Playroom runs at 0.5 to 1 FPS on the Steam Deck when emulated through SharpEmu. It's not much — it's nothing at all, in fact — but just the proof-of-concept alone is enough to stir up exciteme"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cxmt-overtakes-tencent-to-become-chinas-most-valuable-company-17-days-after-its-ipo",
    "domain": "AI 算力 / 半导体",
    "title": "Memory maker CXMT overtakes Tencent to become China's most valuable company 17 days after its IPO — now worth $524 billion",
    "url": "https://www.tomshardware.com/tech-industry/cxmt-overtakes-tencent-to-become-chinas-most-valuable-company-17-days-after-its-ipo",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:27:14+00:00",
    "summary": "ChangXin Memory Technologies (CXMT) is now the world's most valuable Chinese company after passing Tencent."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mechanical-keyboards/keychron-launches-ludicrous-100-key-custom-macro-pad-10-x-10-keyboard-uses-exclusive-keychron-apex-switches-and-features-per-key-rgb-control",
    "domain": "AI 算力 / 半导体",
    "title": "Keychron launches ludicrous 100-key custom macro pad — 10 x 10 ‘keyboard’ uses ‘exclusive’ Keychron Apex switches and features per-key RGB control",
    "url": "https://www.tomshardware.com/peripherals/mechanical-keyboards/keychron-launches-ludicrous-100-key-custom-macro-pad-10-x-10-keyboard-uses-exclusive-keychron-apex-switches-and-features-per-key-rgb-control",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:08:50+00:00",
    "summary": "The Keychron C100 8K macro pad features 100 customizable keys, per-key RGB lighting, and 8K polling rate to give you the ultimate advantage in productivity and gaming. It also has hot-swappable Keychr"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/geekom-it13-max-2026-review-meteor-lake-rides-again-in-a-usd799-mini-pc",
    "domain": "AI 算力 / 半导体",
    "title": "Geekom IT13 Max 2026 review: Meteor Lake rides again in a $799 mini PC",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/geekom-it13-max-2026-review-meteor-lake-rides-again-in-a-usd799-mini-pc",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T13:05:00+00:00",
    "summary": "Geekom mates an Intel Meteor Lake Core Ultra 9 processor with soldered 24GB DDR5 dual-channel RAM to conjure up an attractively specified and priced mini PC for the RAMpocalypse era."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/best-deals-on-pc-furniture-save-money-on-chairs-desks-monitor-stands-boom-arms-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Best deals on PC setup accessories — save money on chairs, desks, monitor stands, boom arms, and more",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/best-deals-on-pc-furniture-save-money-on-chairs-desks-monitor-stands-boom-arms-and-more",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:30:00+00:00",
    "summary": "We've scoured the internet and found the best deals on PC office and gaming furniture. Find the best desks, chairs, monitor arms, and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/maxsun-terminator-b850m-pro-ii-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "Maxsun Terminator B850M Pro II Motherboard Review: Comparable features, but US pricing is over MSRP",
    "url": "https://www.tomshardware.com/pc-components/motherboards/maxsun-terminator-b850m-pro-ii-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:05:00+00:00",
    "summary": "Maxsun’s Terminator B850M Pro II is a decent budget option in the Micro ATX form factor, but only if you can find it for the $199.99 MSRP."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/coin-sized-device-can-hack-a-boeing-737s-flight-management-computer-mess-with-takeoff-weights-or-even-divert-an-aircraft-gadget-connects-to-an-easily-accessible-port-that-overrides-commands-from-the-pilots-uses-in-flight-wi-fi",
    "domain": "AI 算力 / 半导体",
    "title": "Coin-sized device can hack a Boeing 737’s Flight Management Computer, mess with takeoff weights, or even divert an aircraft — gadget connects to an easily accessible port that overrides commands from ",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/coin-sized-device-can-hack-a-boeing-737s-flight-management-computer-mess-with-takeoff-weights-or-even-divert-an-aircraft-gadget-connects-to-an-easily-accessible-port-that-overrides-commands-from-the-pilots-uses-in-flight-wi-fi",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T12:04:32+00:00",
    "summary": "Security researchers discovered a way to tap into the avionics of a Boeing 737 and remotely give its flight management computer erroneous data through in-flight Wi-Fi. This coin-sized device plugs int"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/get-16gb-of-ddr5-ram-free-when-you-buy-amds-9900x-and-an-asus-tuf-motherboard-usd659-newegg-combo-saves-usd274-and-you-get-a-free-240mm-aio",
    "domain": "AI 算力 / 半导体",
    "title": "Get 16GB of DDR5 RAM free when you buy AMD's 9900X and an Asus TUF motherboard — $659 Newegg combo saves $274, and you get a free 240mm AIO",
    "url": "https://www.tomshardware.com/pc-components/ddr5/get-16gb-of-ddr5-ram-free-when-you-buy-amds-9900x-and-an-asus-tuf-motherboard-usd659-newegg-combo-saves-usd274-and-you-get-a-free-240mm-aio",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:50:20+00:00",
    "summary": "Save $274 and snag 16GB of DDR5 RAM for free in this 3-item Newegg combo with Ryzen 9 9900X, Asus TUF Gaming X870E-Plus Wifi7, and 16GB of dual channel Team Group T-Force Vulkan RAM"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/zoomsday-vulnerability-let-anyone-in-a-zoom-meeting-take-over-anybody-else-ai-assisted-research-only-used-20-prompts-to-find-an-exploit-to-hack-hundred-of-millions-of-people",
    "domain": "AI 算力 / 半导体",
    "title": "Critical 'Zoomsday' flaw enables total device takeover during Zoom calls — AI-assisted research only used 20 prompts to find an exploit to hack hundreds of millions of people.",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/zoomsday-vulnerability-let-anyone-in-a-zoom-meeting-take-over-anybody-else-ai-assisted-research-only-used-20-prompts-to-find-an-exploit-to-hack-hundred-of-millions-of-people",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:20:00+00:00",
    "summary": "Zoomsday vulnerability let anyone in a Zoom meeting take over anybody else. The vulnerability was developed with AI assistance and took research only used 20 prompts to find an exploit to hack hundred"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/this-usd57-99-8bitdo-ultimate-2-wireless-controller-is-a-brilliantly-customizable-option-for-pc-gamers-fully-customizable-gamepad-with-nintendo-switch-compatibility-includes-dual-triggers-tmr-joysticks-and-adjustable-rgb-lighting",
    "domain": "AI 算力 / 半导体",
    "title": "This $57.99 8BitDo Ultimate 2 wireless controller is a brilliantly customizable option for PC gamers — fully customizable gamepad with Nintendo Switch compatibility includes dual triggers, TMR joystic",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/this-usd57-99-8bitdo-ultimate-2-wireless-controller-is-a-brilliantly-customizable-option-for-pc-gamers-fully-customizable-gamepad-with-nintendo-switch-compatibility-includes-dual-triggers-tmr-joysticks-and-adjustable-rgb-lighting",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:10:28+00:00",
    "summary": "Save 17% on this 8BitDo Ultimate 2 game controller for your PC or Nintendo Switch right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/jump-into-pc-gaming-for-under-a-thousand-dollars-with-a-usd350-saving-on-this-rtx-5060-powered-laptop-the-15-6-inch-msi-cyborg-15-is-just-usd949-at-walmart",
    "domain": "AI 算力 / 半导体",
    "title": "Jump into PC gaming for under a thousand dollars with a $350 saving on this RTX 5060-powered laptop — the 15.6-inch MSI Cyborg 15 is just $949 at Walmart",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/jump-into-pc-gaming-for-under-a-thousand-dollars-with-a-usd350-saving-on-this-rtx-5060-powered-laptop-the-15-6-inch-msi-cyborg-15-is-just-usd949-at-walmart",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T11:07:46+00:00",
    "summary": "Bag a new gaming laptop for under $1K at Walmart, thanks to a $350 saving on the latest MSI Cyborg 15."
  },
  {
    "id": "hn:49279812",
    "domain": "AI 算力 / 半导体",
    "title": "Why space is a terrible place to cool a data center",
    "url": "https://thenewstack.io/spacex-and-nvidias-orbital-ai-datacenter-fantasy/",
    "source": "CrankyBear",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-12T23:08:21+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/revolutionizing-safety-unveiling-the-power-of-safety-bubble-detectors-in-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "Revolutionizing Safety: Unveiling the Power of Safety Bubble Detectors in Robotics",
    "url": "https://www.eetimes.com/revolutionizing-safety-unveiling-the-power-of-safety-bubble-detectors-in-robotics/",
    "source": "Rajesh Mahapatra, Senior Manager, Anil Sripadarao, Principal Engineer, Prasanna Bhat, Engineer, Colm Prendergast, Senior Principal Engineer, Shane O’Meara, Senior Manager, Dara O’Sullivan, Director, Anders Frederiksen, Principal Specialist, and Sagar Walishetti, Engineer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T19:34:18+00:00",
    "summary": "This article will explain the architecture of real-time safety bubble detection that includes challenges for developing a modular solution, optimizing such a high data bandwidth application to run at "
  },
  {
    "id": "hn:49248477",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is pulling Wall Street into the AI buildout",
    "url": "https://thenextweb.com/news/nvidia-500-billion-wall-street-ai-infrastructure-funding-package",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-10T19:25:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49177126",
    "domain": "AI 算力 / 半导体",
    "title": "It looks like 'Big Short' investor Michael Burry nailed bet against chip stocks",
    "url": "https://www.businessinsider.com/big-short-michael-burry-ai-chip-stocks-soxx-nvidia-substack-2026-8",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T00:30:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48992221",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "speckx",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-21T13:40:51+00:00",
    "summary": ""
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
    "id": "hn:49289112",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.7 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 949,
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
    "points": 864,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993414",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 760,
    "published_at": "2026-07-21T15:17:16+00:00",
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
    "points": 448,
    "published_at": "2026-08-08T09:18:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49267928",
    "domain": "大厂 AI 动态",
    "title": "llama.cpp",
    "url": "https://llama.app",
    "source": "kristianpaul",
    "platform": "hackernews",
    "points": 363,
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
    "id": "hn:49259339",
    "domain": "大厂 AI 动态",
    "title": "Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp",
    "url": "https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md",
    "source": "frabonacci",
    "platform": "hackernews",
    "points": 305,
    "published_at": "2026-08-11T14:50:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48936451",
    "domain": "大厂 AI 动态",
    "title": "NotebookLM is now Gemini Notebook",
    "url": "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-07-16T16:08:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49256057",
    "domain": "大厂 AI 动态",
    "title": "What I learned by putting GitHub Copilot behind a MitM proxy",
    "url": "https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm",
    "source": "j0selit0",
    "platform": "hackernews",
    "points": 197,
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
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-19T07:59:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48998606",
    "domain": "大厂 AI 动态",
    "title": "Gemini last models: temperature, top_p, and top_k are deprecated and ignored",
    "url": "https://ai.google.dev/gemini-api/docs/latest-model",
    "source": "greatgib",
    "platform": "hackernews",
    "points": 136,
    "published_at": "2026-07-21T21:27:54+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/980547/samsung-galaxy-h1-over-ear-headphones",
    "domain": "大厂 AI 动态",
    "title": "Samsung has new Galaxy headphones in the works",
    "url": "https://www.theverge.com/gadgets/980547/samsung-galaxy-h1-over-ear-headphones",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T19:18:45+00:00",
    "summary": "Strings of code in Samsung's Galaxy Wearable app hint at an upcoming pair of over-ear headphones that could compete with the AirPods Max, SamMobile reports. Samsung's reportedly referring to the headp"
  },
  {
    "id": "rss:https://www.theverge.com/tech/979996/best-laptops-students-middle-high-school",
    "domain": "大厂 AI 动态",
    "title": "A RAMageddon guide to back-to-school laptop shopping",
    "url": "https://www.theverge.com/tech/979996/best-laptops-students-middle-high-school",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T18:32:47+00:00",
    "summary": "If you’re a student looking for an affordable laptop, I have bad news and I have good news. The bad news is that computer prices are out of whack due to the ongoing RAM and storage crunch, making some"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/979807/lamborghini-revuelto-sv-specs-performance",
    "domain": "大厂 AI 动态",
    "title": "Lamborghini’s flagship Revuelto levels up with SV trim",
    "url": "https://www.theverge.com/transportation/979807/lamborghini-revuelto-sv-specs-performance",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T18:00:00+00:00",
    "summary": "A lot of automakers talk about wanting to minimize or eliminate driver distractions so as to make the experience of driving more rewarding and safer overall. Lamborghini has a different strategy; it w"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/979925/the-x-files-chris-carter-vrach-frankenshteyn-interview-hulu",
    "domain": "大厂 AI 动态",
    "title": "The X-Files creator Chris Carter wanted to make a more horrific movie",
    "url": "https://www.theverge.com/entertainment/979925/the-x-files-chris-carter-vrach-frankenshteyn-interview-hulu",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T18:00:00+00:00",
    "summary": "The version of The X-Files: I Want to Believe that premiered in 2008 was not exactly the movie co-writer / director Chris Carter intended to make. Carter wanted to bring agents Mulder and Scully back "
  },
  {
    "id": "rss:https://www.theverge.com/tech/980467/google-pixel-11-camera-looks-older-phones",
    "domain": "大厂 AI 动态",
    "title": "Google&#8217;s best new camera feature is only for the Pixel 11 series",
    "url": "https://www.theverge.com/tech/980467/google-pixel-11-camera-looks-older-phones",
    "source": "David Imel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T17:34:14+00:00",
    "summary": "Arguably the coolest new photo feature for the Pixel 11 lineup is Google's new Camera Looks, which process image data differently at the sensor level to produce photos that don't have that \"smartphone"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/980367/instagram-logo-new-zuckerberg-ai-vergecast",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg has an Instagzam",
    "url": "https://www.theverge.com/podcast/980367/instagram-logo-new-zuckerberg-ai-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:54:16+00:00",
    "summary": "Instagram's wordmark is iconic. Well, was iconic. Apparently Instagram thought it looked old, so the company rolled out a new one this week. It doesn't look like the old Instagram wordmark. It doesn't"
  },
  {
    "id": "rss:https://www.theverge.com/tech/980416/google-gemini-ai-watermarks-removal",
    "domain": "大厂 AI 动态",
    "title": "You can now turn off Google Gemini&#8217;s visible watermarks",
    "url": "https://www.theverge.com/tech/980416/google-gemini-ai-watermarks-removal",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:39:32+00:00",
    "summary": "Google will now allow you to remove visible watermarks from the images, videos, and music made with AI tools. With the update, you can toggle off a new \"Media watermark\" setting in Gemini and Google's"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/980261/clair-obscur-pixel-11-gaming-laptop-4k-bluray-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "2025 GOTY Clair Obscur: Expedition 33 is down to $33",
    "url": "https://www.theverge.com/gadgets/980261/clair-obscur-pixel-11-gaming-laptop-4k-bluray-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T14:50:25+00:00",
    "summary": "For RPG fans who dig Persona-style turn-based action and who are pursuing games with original stories and fantastic tunes, look no further than Clair Obscur: Expedition 33. This praise might come off "
  },
  {
    "id": "rss:https://www.theverge.com/tech/979928/cmf-clip-pro-review",
    "domain": "大厂 AI 动态",
    "title": "CMF&#8217;s clip earbuds hit the balance between cheap and good",
    "url": "https://www.theverge.com/tech/979928/cmf-clip-pro-review",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T12:00:00+00:00",
    "summary": "Clip earbuds are an exercise in compromise. It's an inherent aspect of their design - and physics. They can be more comfortable for people that don't like something jammed in their ear, but sound resp"
  },
  {
    "id": "rss:https://www.theverge.com/games/977646/msi-claw-8-ex-review-intel-panther-lake-handheld",
    "domain": "大厂 AI 动态",
    "title": "The MSI Claw EX is the most important PC handheld since Steam Deck — I still wouldn’t buy one",
    "url": "https://www.theverge.com/games/977646/msi-claw-8-ex-review-intel-panther-lake-handheld",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T11:00:00+00:00",
    "summary": "As The Verge's resident handheld reviewer, I have nearly every portable gaming PC on a shelf in my house. The MSI Claw 8 EX AI Plus is now the first one I reach for. Thanks to a next-gen Intel chip an"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/talks-to-sell-paypal-to-stripe-and-advent-are-heating-up/",
    "domain": "大厂 AI 动态",
    "title": "Talks to sell PayPal to Stripe and Advent are heating up",
    "url": "https://techcrunch.com/2026/08/14/talks-to-sell-paypal-to-stripe-and-advent-are-heating-up/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T22:43:24+00:00",
    "summary": "PayPal is still reportedly negotiating a potential sale to Stripe and private equity firm Advent, as the fintech firm's new CEO attempts to turn the company around."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/self-driving-trucks-are-officially-testing-on-california-highways/",
    "domain": "大厂 AI 动态",
    "title": "Self-driving trucks are officially testing on California highways",
    "url": "https://techcrunch.com/2026/08/14/self-driving-trucks-are-officially-testing-on-california-highways/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T20:37:49+00:00",
    "summary": "Aurora Innovation and Kodiak AI, two companies developing self-driving trucks, have received permits from the California Department of Motor Vehicles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/thrives-joshua-kushner-chides-silicon-valley-vcs-over-ai-euphoria/",
    "domain": "大厂 AI 动态",
    "title": "Thrive’s Joshua Kushner chides Silicon Valley VCs over AI euphoria",
    "url": "https://techcrunch.com/2026/08/14/thrives-joshua-kushner-chides-silicon-valley-vcs-over-ai-euphoria/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T19:33:00+00:00",
    "summary": "The AI opportunity is huge, but \"it would also be a grave error in our minds to let excitement weaken our investment discipline,\" Kushner warns in his first-ever investment letter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/what-we-know-about-the-alleged-iranian-hacks-on-u-s-water-utilities/",
    "domain": "大厂 AI 动态",
    "title": "What we know about the alleged Iranian hacks on US water utilities",
    "url": "https://techcrunch.com/2026/08/14/what-we-know-about-the-alleged-iranian-hacks-on-u-s-water-utilities/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T19:04:32+00:00",
    "summary": "Over the last couple of weeks, hackers have targeted and broken into the systems of several water plants in the United States. Here’s what we know and don’t know about this wave of attacks allegedly c"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/read-it-later-app-pocket-is-shutting-down-here-are-the-best-alternatives/",
    "domain": "大厂 AI 动态",
    "title": "Read-it-later app Pocket shut down — here are the best alternatives",
    "url": "https://techcrunch.com/2026/08/14/read-it-later-app-pocket-is-shutting-down-here-are-the-best-alternatives/",
    "source": "Ivan Mehta, Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T18:58:15+00:00",
    "summary": "Pocket users have until October 8, 2025, to export their saved articles and other items, including lists, archives, favorites, notes, and highlights."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/unforgetful-is-a-new-reminders-app-for-people-who-cant-stop-hitting-snooze/",
    "domain": "大厂 AI 动态",
    "title": "Unforgetful is a new reminders app for people who can’t stop hitting snooze",
    "url": "https://techcrunch.com/2026/08/14/unforgetful-is-a-new-reminders-app-for-people-who-cant-stop-hitting-snooze/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:21:04+00:00",
    "summary": "Unforgetful, the latest app from longtime indie developer Marco Arment, is designed to make reminders harder to ignore — or accidentally dismiss."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/",
    "domain": "大厂 AI 动态",
    "title": "Google will now allow users to remove visible watermark from its AI generations",
    "url": "https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:13:40+00:00",
    "summary": "Turning off this setting won't affect invisible benchmarks used to identify an AI generated file."
  },
  {
    "id": "rss:https://techcrunch.com/video/does-mark-zuckerberg-really-believe-ai-is-for-everyone/",
    "domain": "大厂 AI 动态",
    "title": "Does Mark Zuckerberg really believe AI is ‘for everyone’?",
    "url": "https://techcrunch.com/video/does-mark-zuckerberg-really-believe-ai-is-for-everyone/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T15:43:28+00:00",
    "summary": "Meta released Glimmer this week, an open-weight AI&#160;model&#160;anyone can download and run on their own hardware&#160;— a contrast to&#160;Muse&#160;Spark, the company’s more powerful model that s"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/apple-proposes-to-take-a-15-cut-of-purchases-made-outside-the-app-store/",
    "domain": "大厂 AI 动态",
    "title": "Apple proposes to take a 15% cut of purchases made outside the App Store",
    "url": "https://techcrunch.com/2026/08/14/apple-proposes-to-take-a-15-cut-of-purchases-made-outside-the-app-store/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T14:54:48+00:00",
    "summary": "Apple is asking a federal judge to allow it to charge commissions of up to 15% on purchases made through external links in iOS apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/kog-is-going-deeper-to-squeeze-more-inference-out-of-gpus/",
    "domain": "大厂 AI 动态",
    "title": "Kog is going deeper to squeeze more inference out of GPUs",
    "url": "https://techcrunch.com/2026/08/14/kog-is-going-deeper-to-squeeze-more-inference-out-of-gpus/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T14:50:11+00:00",
    "summary": "The idea that GPUs are poorly suited for agentic workflows may be a misconception, according to French startup Kog."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/hyperscalers-might-regret-embracing-natural-gas-if-new-forecast-proves-correct/",
    "domain": "大厂 AI 动态",
    "title": "Hyperscalers might regret embracing natural gas if new forecast proves correct",
    "url": "https://techcrunch.com/2026/08/14/hyperscalers-might-regret-embracing-natural-gas-if-new-forecast-proves-correct/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T14:05:00+00:00",
    "summary": "Natural gas prices could triple in some parts of the U.S., which could saddle hyperscalers with massive bills to power their AI data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/us-courts-will-start-publishing-how-often-the-government-uses-spyware/",
    "domain": "大厂 AI 动态",
    "title": "US courts will start publishing how often the government uses spyware",
    "url": "https://techcrunch.com/2026/08/14/us-courts-will-start-publishing-how-often-the-government-uses-spyware/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T13:29:04+00:00",
    "summary": "The Administrative Office of the U.S. Courts told TechCrunch that it will start disclosing how many times judges authorized the use of spyware to wiretap suspected criminals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/14/uber-and-pony-ai-plan-to-bring-2000-robotaxis-to-europe/",
    "domain": "大厂 AI 动态",
    "title": "Uber and Pony.ai plan to bring 2,000 robotaxis to Europe",
    "url": "https://techcrunch.com/2026/08/14/uber-and-pony-ai-plan-to-bring-2000-robotaxis-to-europe/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T10:44:30+00:00",
    "summary": "The partnership is expanding beyond the initial market of Zagreb, Croatia to four additional European cities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/investors-sue-selena-gomez-alleging-fraud-tied-to-her-mental-health-startup/",
    "domain": "大厂 AI 动态",
    "title": "Investors sue Selena Gomez alleging fraud tied to her mental health startup",
    "url": "https://techcrunch.com/2026/08/13/investors-sue-selena-gomez-alleging-fraud-tied-to-her-mental-health-startup/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T22:12:40+00:00",
    "summary": "The plaintiffs say they invested nearly $1.2 million in the company, and are accusing Gomez of failing to build and market the startup."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/flock-says-its-new-tool-will-help-identify-police-abuse-but-hasnt-explained-how-it-works/",
    "domain": "大厂 AI 动态",
    "title": "Flock says its new tool will help identify police abuse, but hasn’t explained how it works",
    "url": "https://techcrunch.com/2026/08/13/flock-says-its-new-tool-will-help-identify-police-abuse-but-hasnt-explained-how-it-works/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T22:02:04+00:00",
    "summary": "The surveillance company announced it's making a tool called \"Audit Assistance\" mandatory for all customers, claiming it's already helped catch abuse. But the company has yet to explain how the tool w"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/if-apple-sends-you-a-push-notification-alerting-you-to-a-spyware-attack-take-it-seriously/",
    "domain": "大厂 AI 动态",
    "title": "If Apple sends you a push notification alerting you to a spyware attack, take it seriously",
    "url": "https://techcrunch.com/2026/08/13/if-apple-sends-you-a-push-notification-alerting-you-to-a-spyware-attack-take-it-seriously/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T21:50:11+00:00",
    "summary": "Apple now sends out push notifications to iPhone lock screens when the company identifies government spyware targeting someone's devices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/writer-introduces-new-ai-model-and-upgraded-harness-to-contain-token-costs/",
    "domain": "大厂 AI 动态",
    "title": "Writer introduces new AI model and upgraded harness to contain token costs",
    "url": "https://techcrunch.com/2026/08/13/writer-introduces-new-ai-model-and-upgraded-harness-to-contain-token-costs/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T21:13:24+00:00",
    "summary": "Built as a post-training variation on Z.ai's open source model GLM-5.2, Writer says the new system should provide deployment-ready capabilities at a much lower price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/databricks-wanted-to-raise-1b-investors-wanted-15b-it-settled-on-5b-at-a-190b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Databricks wanted to raise $1B, investors wanted $15B. It settled on $5B at a $190B valuation.",
    "url": "https://techcrunch.com/2026/08/13/databricks-wanted-to-raise-1b-investors-wanted-15b-it-settled-on-5b-at-a-190b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T20:14:39+00:00",
    "summary": "AI is expensive, Ali Ghodsi tells TechCrunch. With so many investors wanting into his latest round, he said yes to more than planned."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI introduces ‘Ultrafast,’ a new mode that makes GPT-5.6 Sol work at 14x the speed",
    "url": "https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T19:22:40+00:00",
    "summary": "OpenAI is launching a preview of a sped up version of its latest, most powerful model, in an effort to court enterprise users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/",
    "domain": "大厂 AI 动态",
    "title": "IBM partners with OpenAI to bolster enterprise AI push",
    "url": "https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T19:19:49+00:00",
    "summary": "IBM plans to train and certify tens of thousands of consultants on OpenAI's technologies as part of this deal."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-capex-train-keeps-rolling/",
    "domain": "大厂 AI 动态",
    "title": "2026.33: The CapEx Train Keeps Rolling",
    "url": "https://stratechery.com/2026/the-capex-train-keeps-rolling/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of August 10, 2026, including the capital constraint, AI writing, and a tale of two cities."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/vulnerability-giving-attackers-full-control-of-macs-is-under-active-exploitation/",
    "domain": "大厂 AI 动态",
    "title": "Vulnerability giving attackers full control of Macs is under active exploitation",
    "url": "https://arstechnica.com/security/2026/08/vulnerability-giving-attackers-full-control-of-macs-is-under-active-exploitation/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T18:32:14+00:00",
    "summary": "Screen-sharing bug lets remote hackers log in without a password."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/first-test-flight-of-largest-all-electric-aircraft-used-just-5-of-electricity/",
    "domain": "大厂 AI 动态",
    "title": "First test flight of largest all-electric aircraft used just $5 of electricity",
    "url": "https://arstechnica.com/gadgets/2026/08/first-test-flight-of-largest-all-electric-aircraft-used-just-5-of-electricity/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T18:00:23+00:00",
    "summary": "Airline-backed venture aims to develop a hybrid-electric commercial aircraft."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/suspecting-court-of-using-ai-man-injected-prompts-in-filings-to-try-to-win-case/",
    "domain": "大厂 AI 动态",
    "title": "Suspecting court of using AI, man injected prompts in filings to try to win case",
    "url": "https://arstechnica.com/tech-policy/2026/08/suspecting-court-of-using-ai-man-injected-prompts-in-filings-to-try-to-win-case/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T17:26:53+00:00",
    "summary": "Judge warns pro se litigants are using chatbots wrong and getting desperate."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/state-judge-orders-kalshi-to-stop-offering-sports-bets-and-other-wagers/",
    "domain": "大厂 AI 动态",
    "title": "State judge orders Kalshi to stop offering sports bets and other wagers",
    "url": "https://arstechnica.com/tech-policy/2026/08/state-judge-orders-kalshi-to-stop-offering-sports-bets-and-other-wagers/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T17:13:14+00:00",
    "summary": "Kalshi ordered to stop offering bets in Washington, must implement geofencing."
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 314,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48948435",
    "domain": "股票",
    "title": "Short sellers notch $8.7B profit as SpaceX shares dip to IPO price",
    "url": "https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 168,
    "published_at": "2026-07-17T15:17:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 117,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49303230",
    "domain": "股票",
    "title": "OpenAI talent exodus raises 'huge red flag' ahead of IPO",
    "url": "https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html",
    "source": "DGAP",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-14T19:05:21+00:00",
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
    "id": "wscn:3779506",
    "domain": "股票",
    "title": "小菜园主动降低外卖权重：堂食翻台率回升，净利润下降24%",
    "url": "https://wallstreetcn.com/articles/3779506",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T03:32:38+00:00",
    "summary": "小菜园用短期利润换回堂食客流，一场主动的经营调整正在展开。\n8月14日，小菜园发布截至2026年6月..."
  },
  {
    "id": "wscn:3779503",
    "domain": "股票",
    "title": "“AI版金融创新”：英伟达的“5000亿美元大算盘”",
    "url": "https://wallstreetcn.com/articles/3779503",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T03:30:04+00:00",
    "summary": "英伟达正通过“兜底换分润”模式为新兴AI云服务商（neocloud）提供信用背书，换取收益分成，以绕过传统云巨头资本开支约束并开辟年金式收入。摩根士丹利看好其长远盈利与行业主导力，但也指出该循环收入结构引发了市场多空分歧。"
  },
  {
    "id": "wscn:3779502",
    "domain": "股票",
    "title": "博通暴跌20% 市场在怕什么？",
    "url": "https://wallstreetcn.com/premium/articles/3779502?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T03:00:46+00:00",
    "summary": "一家芯片公司，为什么突然背上了3700亿美元的隐形担保？"
  },
  {
    "id": "wscn:3779501",
    "domain": "股票",
    "title": "爆仓前最后一个月，“AI股神”加仓美光、闪迪",
    "url": "https://wallstreetcn.com/articles/3779501",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T03:00:33+00:00",
    "summary": "据监管文件显示，Situational Awareness在今年二季度大幅增持了存储芯片企业美光科技和闪迪，两家公司持仓合计约110亿美元，占该基金当时净资产的约四分之一。与此同时，该基金还削减了对英伟达、博通及超威半导体的期权空头头寸。"
  },
  {
    "id": "wscn:3779499",
    "domain": "股票",
    "title": "“AI版金融创新”：CDO vs CCO=2008 vs 2026？",
    "url": "https://wallstreetcn.com/articles/3779499",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T02:01:44+00:00",
    "summary": "当前AI繁荣本质并非科技周期，而是由“算力即抵押品”（CCO）驱动的信用与地产周期。英伟达与私营巨头搭建5000亿美元融资平台，将风险证券化分发。在超大规模云厂商资本开支增速拐点（二阶导数）已现、OpenAI等关键借款人过度依赖再融资的背景下，这套高度同构于2008年次贷危机的信用架构极易在增长放缓时触发断裂。"
  },
  {
    "id": "wscn:3779497",
    "domain": "股票",
    "title": "本周市场的“核心逻辑”：美联储9月不加息了？",
    "url": "https://wallstreetcn.com/articles/3779497",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T01:14:41+00:00",
    "summary": "美国7月CPI、PPI及零售销售数据全面走软，叠加就业降温，市场对美联储9月加息概率从75%骤降至25%，推动全球股市连续三周上涨。然而，油价仍处高位，美债收益率曲线陡化，债市长端持续为通胀与财政赤字定价，两周后杰克逊霍尔会议将成关键风向标。"
  },
  {
    "id": "wscn:3779154",
    "domain": "股票",
    "title": "医药行业的三重共振：资金转向、业绩反转和AI重构，谁在买入？在买什么？",
    "url": "https://wallstreetcn.com/premium/articles/3779154?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T01:10:43+00:00",
    "summary": "AI对制药研发底座的重构——这可能是医药行业未来十年最大的结构性阿尔法。"
  },
  {
    "id": "wscn:3779498",
    "domain": "股票",
    "title": "8月，华尔街的“牛市”又回来了，“赌性”也回来了",
    "url": "https://wallstreetcn.com/articles/3779498",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T01:06:14+00:00",
    "summary": "8月美股强劲反弹，标普500指数再创新高。在超预期企业盈利与通胀降温的推动下，机构与散户大幅加码科技股、看涨期权及杠杆ETF，“牛市”与“赌性”双双回归。然而，油价飙升与长债收益率高企显露宏观矛盾，“万事俱好”的定价模式几无容错空间。"
  },
  {
    "id": "wscn:3779494",
    "domain": "股票",
    "title": "英伟达首度披露SpaceX持仓，借道xAI间接持有约210亿美元",
    "url": "https://wallstreetcn.com/articles/3779494",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T00:20:31+00:00",
    "summary": "此次持仓源于英伟达1月投资xAI，后者被SpaceX收购后完成股权转换。目前持有SpaceX约1.228亿股A类股，季末市值约210亿美元，现已缩水至约172亿美元，成为SpaceX第六大股东。"
  },
  {
    "id": "wscn:3779496",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年8月15日",
    "url": "https://wallstreetcn.com/articles/3779496",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T23:34:25+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3779493",
    "domain": "股票",
    "title": "“AI股神”爆仓拖累，Jane Street7月巨亏150亿，十年来首次单月亏损！",
    "url": "https://wallstreetcn.com/articles/3779493",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T23:15:12+00:00",
    "summary": "据报道，Jane Street 7月巨亏后今年内净交易收入仍超400亿美元、有望创年度新高，亏损并非全部源于其投资的Situational Awareness，其亚洲非AI类股的多仓也遭受损失；本周推进约146亿美元债券融资，由摩根大通牵头，获得Pimco、Fidelity等大型机构投资者参与；为重构债务，Jane Street将更多债务转移到私人市场，甚至愿承担明显更高的融资成本，换取减少公开披"
  },
  {
    "id": "wscn:3779437",
    "domain": "股票",
    "title": "美股指小幅收跌，存储、光通信股集体拉升，闪迪涨超7%，金油齐涨，美债跌",
    "url": "https://wallstreetcn.com/articles/3779437",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T23:06:37+00:00",
    "summary": "道指跌0.2%，纳指跌0.28%。存储芯片股逆势普涨，闪迪大涨7.39%、本周累计飙升35.38%。中概股指数逆市收涨0.6%。欧洲长债收益率飙升，30年期德债和10年期法债收益率齐创多年新高。美国10年期基准国债收益率上行5.14个基点。美元指数一度跳水0.47%。比特币五连跌，日内跌幅0.8%。"
  },
  {
    "id": "wscn:3779489",
    "domain": "股票",
    "title": "甲骨文一度跌5%，“星际之门”关键AI数据中心配套天然气管道延期",
    "url": "https://wallstreetcn.com/articles/3779489",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T22:57:15+00:00",
    "summary": "Energy Transfer披露Green Chile Project天然气管道的预计投运日期已从2026年8月15日延至2027年2月1日。该管道是为甲骨文Project Jupiter数据中心提供燃料的核心设施，Project Jupiter是“星际之门”大合同中最关键的组成部分之一。延期是途经公共土地，居民抗议所致。"
  },
  {
    "id": "wscn:3779495",
    "domain": "股票",
    "title": "Anthropic Q2营收飙升至逾115亿美元，同比涨超14倍",
    "url": "https://wallstreetcn.com/articles/3779495",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T22:56:59+00:00",
    "summary": "据媒体报道，Anthropic二季度实现初步营收超过115亿美元，而2025年同期为7.87亿美元，今年第一季度为47.3亿美元。同时，Anthropic二季度实现了调整后营业利润为正。"
  },
  {
    "id": "wscn:3779492",
    "domain": "股票",
    "title": "美联储Goolsbee：希望看到更多通胀降温证据，就业与经济增长稳定",
    "url": "https://wallstreetcn.com/articles/3779492",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T22:41:12+00:00",
    "summary": "芝加哥联储行长Goolsbee表示，过去三个月通胀数据令其\"感到鼓舞\"，但还需连续数月类似表现才能确认通胀回归2%轨道。其将并将通胀列为当前首要关切，表示在增长和劳动力市场方面，美国经济目前\"基本稳定\"。"
  },
  {
    "id": "wscn:3779491",
    "domain": "股票",
    "title": "SK集团“天价离婚案”再起波澜，董事长崔泰源就6.43亿美元判决提起上诉",
    "url": "https://wallstreetcn.com/articles/3779491",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T22:40:38+00:00",
    "summary": "崔泰源法律团队周五表示，已就首尔高等法院7月24日的判决向韩国最高法院提出上诉，并称此举旨在\"将对股东及集团管理层的负面影响降至最低\"。判决的赔付金额约占崔泰源个人财富的12%。分析人士认为，这笔离婚赔付不太可能对崔泰源的财富造成实质性侵蚀，也不会威胁其对SK集团的控制权。"
  },
  {
    "id": "wscn:3779490",
    "domain": "股票",
    "title": "阿贝尔掌舵半年伯克希尔大举增持谷歌、A类股晋升前五重仓，Q2加码航空和房产股",
    "url": "https://wallstreetcn.com/articles/3779490",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T22:21:27+00:00",
    "summary": "二季度，伯克希尔所持谷歌母公司两类股市值合计新增超170亿美元，其中C类股股份环比一季度增超六倍、首次跻身十大重仓股，A类股股份增45%、持仓升至第四；一季度新进的达美航空持股增加44%、增持市值26亿美元，房产股Lennar持仓增25%；再抛美银，当季减持市值17.2亿美元，金融股Capital One减仓58%、钢企Nucor持仓腰斩；苹果稳坐头号重仓股，持仓连续两季不变。"
  },
  {
    "id": "wscn:3779486",
    "domain": "股票",
    "title": "AI融资担忧发酵，博通盘中重挫7%，3700亿潜在风险响警钟",
    "url": "https://wallstreetcn.com/articles/3779486",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T21:21:45+00:00",
    "summary": "美银估算，博通的芯片融资项目到2029年中可能形成约3700亿美元高级债务，为20GW算力提供资金，单2027年就可能新增约1500亿美元债务。美银并未否定博通的经营基本面，但市场开始意识到，如果未来AI算力需求需要依靠越来越庞大的融资平台才能持续，AI产业链的估值逻辑也必须同时考虑资产残值、客户违约率、债务成本以及供应商担保责任。"
  },
  {
    "id": "wscn:3779487",
    "domain": "股票",
    "title": "特朗普：击败伊朗后会宣布霍尔木兹海峡为美国领土",
    "url": "https://wallstreetcn.com/articles/3779487",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T21:04:00+00:00",
    "summary": "特朗普说，伊朗正遭受惨败，“在我们彻底击败伊朗后，很快我就会宣布霍尔木兹海峡为美国领土”；相比阻止伊朗获得核武，高油价只是小问题。"
  },
  {
    "id": "wscn:3779485",
    "domain": "股票",
    "title": "老虎环球Q2押注AI“二线选手”：新进Cerebras和AMD，增持英特尔，十大重仓股全线减持",
    "url": "https://wallstreetcn.com/articles/3779485",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T19:51:53+00:00",
    "summary": "二季度，老虎环球买入个股的前两大变动是建仓Cerebras、市值约6.6亿美元，建仓AMD、市值3.9亿美元，同时建仓近2.8亿美元希捷科技，增持英特尔、市值近3.7亿美元；减持最多的是谷歌母公司Alphabet、市值17.2亿美元，第二位是博通、减持市值6.9亿美元，同时清仓4.2亿美元AppLovin。"
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
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-08-03T06:17:53+00:00",
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
    "id": "hn:49137024",
    "domain": "股票",
    "title": "Oil companies report sky-high profits thanks to wartime crude prices",
    "url": "https://www.npr.org/2026/07/31/nx-s1-5910660/big-oil-earnings-q2-2026",
    "source": "speckx",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-01T18:28:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-16T18:03:56+00:00",
    "summary": ""
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
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-17T18:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48958985",
    "domain": "股票",
    "title": "Traders are increasingly betting against SpaceX just weeks after IPO",
    "url": "https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5",
    "source": "ethanhawksley",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-18T15:26:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49136787",
    "domain": "股票",
    "title": "Reddit Stock Collapses 23% as AI Eats Away at User Growth",
    "url": "https://www.barchart.com/story/news/3584357/reddit-stock-collapses-23-as-ai-eats-away-at-user-growth",
    "source": "thm",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-08-01T18:03:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48984021",
    "domain": "股票",
    "title": "Mark Cuban: fight inequality by giving all workers company stock",
    "url": "https://fortune.com/2026/07/20/mark-cuban-income-inequality-company-stock-spacex-ipo-cost-plus-drugs/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-20T19:52:49+00:00",
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
    "id": "hn:49162737",
    "domain": "股票",
    "title": "Palantir soars 12% on blowout quarter, with US commercial revenue soaring ~150%",
    "url": "https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html",
    "source": "gslin",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-03T23:36:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49145809",
    "domain": "股票",
    "title": "As Reddit stock falls, CEO questions value of Google's AI Overviews",
    "url": "https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-02T16:09:26+00:00",
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
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 337,
    "published_at": "2026-08-04T21:09:39+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.12363",
    "domain": "金融",
    "title": "EU-ETS under attack? The impact of carbon price suppression on the decarbonization of the power sector",
    "url": "https://arxiv.org/abs/2608.12363",
    "source": "Javier Gonzalez-Ruiz, Carlos Rodriguez-Pardo, Alice Di Bella, Paolo Mastropietro, Jose Pablo Chavez-Avila, Massimo Tavoni",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12363v1 Announce Type: new Abstract: European countries are debating policies to mitigate the increased energy costs caused by renewed geopolitical tensions, while pursuing decarbonization "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12424",
    "domain": "金融",
    "title": "AI-Driven Multiscenario Interest Rate Forecasting: A Proof of Concept for Banking Asset Management",
    "url": "https://arxiv.org/abs/2608.12424",
    "source": "Ekkehardt Bauer, Dirk Holl\\\"ander, Linus Wolff, Christoph Ostermair, Kyrillus Aiad, Joachim Hasebrook",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12424v1 Announce Type: new Abstract: This study focuses on developing an AI-supported prototype for multiperspective interest rate forecasting that combines classical econometric models wit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12493",
    "domain": "金融",
    "title": "Beyond the Skew-Stickiness Ratio: Transport Geometry of Spot-Driven Variance Surface Dynamics",
    "url": "https://arxiv.org/abs/2608.12493",
    "source": "Charlie Che, Pradeepta Das",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12493v1 Announce Type: new Abstract: We develop a geometric theory of arbitrage-free implied variance surface dynamics. Smile dynamics are formulated as transport flows on the admissible cl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12583",
    "domain": "金融",
    "title": "Diffusion Models in Finance: A Survey",
    "url": "https://arxiv.org/abs/2608.12583",
    "source": "Zhuohan Wang, Carmine Ventre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12583v1 Announce Type: new Abstract: Diffusion generative models have rapidly emerged as powerful tools for modeling complex financial data. Their appeal is both structural and practical: t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12587",
    "domain": "金融",
    "title": "DYSANOS Generative Dynamic Smooth Arbitrage-free Non-parametric Option Surfaces",
    "url": "https://arxiv.org/abs/2608.12587",
    "source": "Hans Buehler, Blanka Horvath, Anastasis Kratsios",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12587v1 Announce Type: new Abstract: This article presents with DYSANOS the first generative market model for smooth SANOS option surfaces for all strikes and expiries which are free of sta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12594",
    "domain": "金融",
    "title": "What Makes a Peer? Valuation-Anchored Similarity in Private Markets",
    "url": "https://arxiv.org/abs/2608.12594",
    "source": "Sebastian Frank, Jingrao Lyu, Max Jarmey, Preetha Saha, Mingshu Li, Sweet Kaur, Sola Akinola, Dhagash Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12594v1 Announce Type: new Abstract: As more investors contemplate private markets and contend with limited transparency, sparse disclosures, and infrequent transactions, identifying econom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12634",
    "domain": "金融",
    "title": "The Price of Permission: Classification Uncertainty in Constrained Capital Markets",
    "url": "https://arxiv.org/abs/2608.12634",
    "source": "Abdulrahman Qadi, Akash Sharma, Francesca Medda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12634v1 Announce Type: new Abstract: Shariah-compliant equity screening provides a transparent setting in which institutional rules determine who may own a stock. A binary label identifies "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12667",
    "domain": "金融",
    "title": "Does life-satisfaction inequality measure societal inequality? A focal-value-rounding critique",
    "url": "https://arxiv.org/abs/2608.12667",
    "source": "C. P. Barrington-Leigh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12667v1 Announce Type: new Abstract: The dispersion of self-reported life satisfaction has been proposed and used as a comprehensive measure of societal inequality. A negative cross-country"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12777",
    "domain": "金融",
    "title": "Physical Extinction and Long-Run Pricing under Time-Varying Beliefs",
    "url": "https://arxiv.org/abs/2608.12777",
    "source": "Sourav Majumdar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.12777v1 Announce Type: new Abstract: An investor may be optimistic about aggregate endowment growth at some times and pessimistic at others. The weight placed on her forecast in bond valuat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13056",
    "domain": "金融",
    "title": "Simulating Stress Laws under Extremal Dependence: Characterizing What Generative Models Must Preserve",
    "url": "https://arxiv.org/abs/2608.13056",
    "source": "Mantu Gupta, Anand Deo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.13056v1 Announce Type: new Abstract: We study stress-scenario generation for systems driven by multivariate heavy-tailed risk factors. Within regions where several financial losses are simu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13082",
    "domain": "金融",
    "title": "LOB-ID: Evaluating Synthetic Market Data by Inception Distances",
    "url": "https://arxiv.org/abs/2608.13082",
    "source": "Andreea Bacalum, Zhuohan Wang, Ollie Olby, Martin Garaj, Namid Stillman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.13082v1 Announce Type: new Abstract: Generative models of limit orderbook (LOB) data have advanced rapidly, but their evaluation often focuses on stylised facts and selected market statisti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13340",
    "domain": "金融",
    "title": "Fee Implied Volatility on Uniswap v3: A DEX Native Proxy and Its Limits",
    "url": "https://arxiv.org/abs/2608.13340",
    "source": "Amy Oumayma Khaldoun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.13340v1 Announce Type: new Abstract: Narrow Uniswap v3 liquidity ranges resemble short dated options, and Panoptic's streaming premium echoes the short maturity concentration of Black-Schol"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13096",
    "domain": "金融",
    "title": "FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching",
    "url": "https://arxiv.org/abs/2608.13096",
    "source": "Zhuohan Wang, Andreea Bacalum, Ollie Olby, Carmine Ventre, Namid Stillman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.13096v1 Announce Type: cross Abstract: Limit order book (LOB) simulators are most useful to practitioners when they combine realistic market dynamics, computationally efficient sampling, co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2212.03931",
    "domain": "金融",
    "title": "A Better Test of Choice Overload",
    "url": "https://arxiv.org/abs/2212.03931",
    "source": "Mark Dean, Dilip Ravindran, J\\\"org Stoye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2212.03931v4 Announce Type: replace Abstract: Choice overload - in which larger choice sets are detrimental to a chooser's well-being - is potentially of great importance in the design of econom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.14614",
    "domain": "金融",
    "title": "Pricing options on the cryptocurrency futures contracts",
    "url": "https://arxiv.org/abs/2506.14614",
    "source": "Julia Ko\\'nczal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2506.14614v2 Announce Type: replace Abstract: The cryptocurrency options market is notable for its high volatility and lower liquidity compared to traditional markets. These characteristics intr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.09541",
    "domain": "金融",
    "title": "Designing Ad Auctions with Targeting Information",
    "url": "https://arxiv.org/abs/2601.09541",
    "source": "Srinivas Tunuguntla, Carl F. Mela, Jason Pratt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2601.09541v2 Announce Type: replace Abstract: Digital advertising publishers sell ad inventory that conveys targeting information, such as demographic, contextual, or behavioral audience segment"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.16108",
    "domain": "金融",
    "title": "Short-horizon Duesenberry Equilibrium",
    "url": "https://arxiv.org/abs/2603.16108",
    "source": "Jaime Alberto Londo\\~no",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2603.16108v3 Announce Type: replace Abstract: We develop a continuous-time general equilibrium framework for an infinite heterogeneous population whose household types are transported by a Brown"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.03274",
    "domain": "金融",
    "title": "Financial Dynamics and Interconnected Risk of Liquid Restaking",
    "url": "https://arxiv.org/abs/2604.03274",
    "source": "Hasret Ozan Sevim, Christof Ferreira Torres",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2604.03274v2 Announce Type: replace Abstract: Decentralized finance introduces new business models and use cases as part of digital finance. Restaking has recently emerged as a transformative me"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.03499",
    "domain": "金融",
    "title": "Marking-Aware Sequential VaR Recalibration for Standardized Option Books",
    "url": "https://arxiv.org/abs/2604.03499",
    "source": "Tenghan Zhong, Keyuan Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2604.03499v3 Announce Type: replace Abstract: Daily Value-at-Risk (VaR) for option books requires more than an accurate quantile forecast. It first requires a precise definition of the loss targ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.06116",
    "domain": "金融",
    "title": "Sequential Audit Sampling for Finite Populations with Exact and Simulation-based Guarantee",
    "url": "https://arxiv.org/abs/2604.06116",
    "source": "Masahiro Kato, Kei Nakagawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2604.06116v2 Announce Type: replace Abstract: Financial statement auditors use a risk-based approach to evidence collection to obtain reasonable assurance. When an initial sample does not suppor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.16448",
    "domain": "金融",
    "title": "On the Expected Maximum Deficit and the Optimal Allocation of Reserves",
    "url": "https://arxiv.org/abs/2605.16448",
    "source": "Claude Lefevre, Pierre Zuyderhoff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2605.16448v2 Announce Type: replace Abstract: Let $L$ be a c\\`adl\\`ag net-loss process and $M_t=\\sup_{0\\le s\\le t}L_s$. We study the distorted expected maximum deficit $$ D_g^{(t)}(u)=\\int_u^\\in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23347",
    "domain": "金融",
    "title": "Beyond the Margin: Targeted Conservation and Household Water Demand",
    "url": "https://arxiv.org/abs/2606.23347",
    "source": "Andrea Albertazzi, Elisabetta Leni, Ennio Bilancini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2606.23347v2 Announce Type: replace Abstract: Non-price interventions targeting specific household water uses are increasingly central to conservation policy, but whether end-use savings transla"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04753",
    "domain": "金融",
    "title": "Fooling Yourself: how narratives shape beliefs",
    "url": "https://arxiv.org/abs/2607.04753",
    "source": "Andrea Albertazzi, Paolo Pin, Marco Stimolo, Alessandro Stringhi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2607.04753v2 Announce Type: replace Abstract: Decision-makers often receive information through narratives combining diagnostic evidence, which favors one state over another, with nondiagnostic "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25353",
    "domain": "金融",
    "title": "How Likely and How Deep? Sharp Joint Bounds on Risk-Neutral Crash Probability and Conditional Depth from Option Bid-Ask Quotes",
    "url": "https://arxiv.org/abs/2607.25353",
    "source": "Jirong Zhuang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2607.25353v3 Announce Type: replace Abstract: Option quotes with bid-ask spreads do not point-identify the risk-neutral probability of a crash below a given threshold, nor the expected depth of "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05755",
    "domain": "金融",
    "title": "Cross-Sectional Heterogeneity in LSTM Networks for Financial Time Series",
    "url": "https://arxiv.org/abs/2608.05755",
    "source": "Julius D\\\"obelt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.05755v2 Announce Type: replace Abstract: Predicting financial asset returns remains one of the most difficult challenges in empirical finance, driven by the low signal-to-noise ratio and th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.02091",
    "domain": "金融",
    "title": "The Impact of Generative AI on Collaborative Open-Source Software Development: Evidence from GitHub Copilot",
    "url": "https://arxiv.org/abs/2410.02091",
    "source": "Fangchen Song, Ashish Agarwal, Wen Wen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2410.02091v4 Announce Type: replace-cross Abstract: Generative artificial intelligence (AI) facilitates content production and enhances ideation, with potentially important implications for deve"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.12508",
    "domain": "金融",
    "title": "Interoperability Effects: Extending DeFi Lending Risk Models to Multi-Chain Environments",
    "url": "https://arxiv.org/abs/2605.12508",
    "source": "Hasret Ozan Sevim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2605.12508v2 Announce Type: replace-cross Abstract: On-chain lending has expanded across multiple distributed ledgers as DeFi becomes increasingly multi-chain. This environment introduces novel "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29018",
    "domain": "金融",
    "title": "Liquidity-Based Audit of Algorithmic Trading Strategies",
    "url": "https://arxiv.org/abs/2606.29018",
    "source": "Irene Aldridge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2606.29018v2 Announce Type: replace-cross Abstract: We show that net demand for liquidity by algo strategies is identifiable from its trade and price history alone, with no knowledge of its sign"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11344",
    "domain": "金融",
    "title": "Governing Agentic AI in FinTech",
    "url": "https://arxiv.org/abs/2608.11344",
    "source": "Henry Han",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T04:00:00+00:00",
    "summary": "arXiv:2608.11344v2 Announce Type: replace-cross Abstract: Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act"
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
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T20:11:15+00:00",
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
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-07-28T12:19:54+00:00",
    "summary": ""
  }
]
```
