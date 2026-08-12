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

- 今日日期：`2026-08-12`
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
  "date": "2026-08-12",
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
    "id": "bvid:BV1834y1676P",
    "domain": "AI",
    "title": "黑马程序员前端微信小程序开发教程，微信小程序从基础到发布全流程_企业级商城实战(含uni-app项目多端部署)",
    "url": "http://www.bilibili.com/video/av807451085",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 6441368,
    "published_at": "2021-12-17T01:30:11+00:00",
    "summary": "传智教育·黑马程序员前端研究院全新录制的前端入门教程\n全部配套资源领取方式：关注黑马程序员公众号，回复关键词:领取资源02\n===============================\n本课程从小程序账号注册、开发环境搭建、基础语法、路由导航、数据请求、分包、组件化等方面详细阐述了小程序开发必备的基础知识。\n学完小程序基础之后，利用 uni-app 技术实现微信小程序的开发，可以做到一次开发多端"
  },
  {
    "id": "bvid:BV1MvaVzUEuz",
    "domain": "AI",
    "title": "2025版pink老师最新AI+前端入门教程，零基础必看的html5、css3、grid、flex布局、响应式、移动端，bootstrap5框架，AI工具",
    "url": "http://www.bilibili.com/video/av115124367006835",
    "source": "黑马pink讲前端",
    "platform": "bilibili",
    "points": 2170359,
    "published_at": "2025-09-01T01:00:00+00:00",
    "summary": "本套课程是2025版最新前端基础入门课程，包含 html5、css3、flex布局、grid布局、响应式布局、移动端布局，从零基础到实战的课程。里面包含svg、 css 变量、计算函数、时间线动画等新技术，同时还是全网首套 AI工具 trae 讲解的零基础到实战的前端课程。"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1695965,
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
    "points": 1631016,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1323945,
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
    "points": 1266675,
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
    "points": 1101572,
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
    "points": 1039792,
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
    "points": 943546,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 670641,
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
    "points": 611097,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 542035,
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
    "points": 472785,
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
    "points": 436359,
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
    "points": 416875,
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
    "points": 395629,
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
    "points": 384969,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 233004,
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
    "points": 228207,
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
    "points": 178955,
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
    "points": 176659,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 162853,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 158951,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 151586,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 127385,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93119,
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
    "points": 74144,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 73819,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53915,
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
    "points": 47586,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 43047,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 42930,
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
    "points": 40347,
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
    "points": 38511,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34088,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1sRRYY2EBo",
    "domain": "AI",
    "title": "利用AI编程工具Trae或Cursor免费生成CAD图纸",
    "url": "http://www.bilibili.com/video/av114132447665738",
    "source": "vjmap",
    "platform": "bilibili",
    "points": 32351,
    "published_at": "2025-03-09T12:24:12+00:00",
    "summary": "AI编程助手如Trae和Cursor正在革新工程设计领域的CAD绘图流程。传统CAD绘图耗时且易出错，而AI工具通过代码生成技术，能够将自然语言指令转化为精确的代码，自动生成符合标准的CAD图纸，极大提升了设计效率。这些工具不仅支持多模态输入（如图片、草图），还提供了智能代码补全、错误修复等功能，进一步简化了开发流程。随着大模型如deepseek和claude3.7的出现，AI的智能化程度进一步提"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29588,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1pkK56aEVG",
    "domain": "AI",
    "title": "GPT-5.6在Claude Code中表现远超Codex | Theo - t3․gg",
    "url": "http://www.bilibili.com/video/av116929612221157",
    "source": "浮生千山路w",
    "platform": "bilibili",
    "points": 29581,
    "published_at": "2026-07-16T12:29:37+00:00",
    "summary": "来源：https://www.youtube.com/watch?v=Noo0NWD0gHU\n原标题：gpt 5.6 is way better in Claude Code\n频道：Theo - t3․gg\n发布时间：2026-07-16\n\n内容简介：\n作者使用GPT-5.6 Sol版本在Claude Code中进行编程，发现其表现相较于Codex有显著提升，体验令人震惊。视频由Coderabbi"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28863,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 26254,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1dZud6VE5G",
    "domain": "AI",
    "title": "【AI实战】AI Agent智能教务排课与教学质量分析系统，基于SpringAI+Springboot+Agent的教务排课系统，教学质量分析系统",
    "url": "http://www.bilibili.com/video/av117070104692483",
    "source": "武哥聊编程",
    "platform": "bilibili",
    "points": 23801,
    "published_at": "2026-08-10T07:48:01+00:00",
    "summary": "完整资料：https://aigcbaba.com/course/98"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22700,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21306,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 20941,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 20835,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1zjd3BiEzo",
    "domain": "AI",
    "title": "别再二选一：Claude Code + Codex 联用才是最强姿势",
    "url": "http://www.bilibili.com/video/av116537746791000",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 19904,
    "published_at": "2026-05-08T07:34:23+00:00",
    "summary": "Codex 已悄然追上 Claude Code，GPT 5.5 比肩 Opus 4.7、OpenAI Pro 额度更大方。但作者 Chase 想说：别再纠结谁更好，最佳姿势是把两者一起用——Codex 桌面应用直接跑 Claude Code 终端，让两个模型互查方案、互查代码（一次实测 Claude Code 帮 Codex 抓出 20 个 bug）。背后更重要的思路是 tool agnostic"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 19066,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 18893,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 17926,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16171,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "hn:49255710",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Risky Business",
    "url": "https://stratechery.com/2026/nvidias-risky-business/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 316,
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
    "points": 198,
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
    "points": 119,
    "published_at": "2026-08-11T13:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122838",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba",
    "url": "https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba",
    "source": "gk1",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-07-31T13:24:03+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/agentic-ai-multi-physics-and-standards-will-redefine-chips-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Agentic AI, Multi‑Physics, and Standards Will Redefine Chips Design",
    "url": "https://www.eetimes.com/agentic-ai-multi-physics-and-standards-will-redefine-chips-design/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T22:00:00+00:00",
    "summary": "Agentic AI, brutal physics bottlenecks, and standards are remaking chip design from silicon to systems. The post Agentic AI, Multi‑Physics, and Standards Will Redefine Chips Design appeared first on E"
  },
  {
    "id": "rss:https://www.eetimes.com/amd-challenges-gpu-centric-architectures-as-it-takes-aim-at-nvidia-in-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Challenges GPU-Centric Architectures as It Takes Aim at Nvidia in Robotics",
    "url": "https://www.eetimes.com/amd-challenges-gpu-centric-architectures-as-it-takes-aim-at-nvidia-in-robotics/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T14:09:45+00:00",
    "summary": "AMD’s new SoC for robots combines CPU, GPU, NPU on one chip with unified memory. The post AMD Challenges GPU-Centric Architectures as It Takes Aim at Nvidia in Robotics appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/managing-your-component-library-for-supply-chain-resilience/",
    "domain": "AI 算力 / 半导体",
    "title": "Managing Your Component Library for Supply Chain Resilience",
    "url": "https://www.eetimes.com/managing-your-component-library-for-supply-chain-resilience/",
    "source": "Cadence Design Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T14:00:00+00:00",
    "summary": "To take a PCB from design to production, an unmanaged component library is a hidden liability. Obsolete parts, single-source vulnerabilities, long lead times, counterfeit exposure, and compliance gaps"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-hardwares-next-frontier-is-integration/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Hardware’s Next Frontier Is Integration",
    "url": "https://www.eetimes.com/ai-hardwares-next-frontier-is-integration/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T09:25:50+00:00",
    "summary": "The LID World Summit 2026 showed why AI progress now depends on system-level advances in memory, packaging, photonics, and power. The post AI Hardware’s Next Frontier Is Integration appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/why-ai-adoption-in-materials-rd-depends-more-on-people-than-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "Why AI Adoption in Materials R&D Depends More on People Than Technology",
    "url": "https://www.eetimes.com/why-ai-adoption-in-materials-rd-depends-more-on-people-than-technology/",
    "source": "Ryo Matsushima",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T21:21:39+00:00",
    "summary": "The technology works. The organization has to catch up. The post Why AI Adoption in Materials R&amp;D Depends More on People Than Technology appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-startup-fields-quantum-sensors-to-reduce-reliance-on-gps/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Startup Fields Quantum Sensors to Reduce Reliance on GPS",
    "url": "https://www.eetimes.com/u-s-startup-fields-quantum-sensors-to-reduce-reliance-on-gps/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T13:14:50+00:00",
    "summary": "GPS spoofing is a sitting duck; Dirac’s quantum sensors aim to navigate air, sea, and tunnels without satellites. The post U.S. Startup Fields Quantum Sensors to Reduce Reliance on GPS appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/leading-edge-ai-ic-designs-demand-comprehensive-hav-methodologies/",
    "domain": "AI 算力 / 半导体",
    "title": "Leading-edge AI IC designs demand comprehensive HAV methodologies",
    "url": "https://www.eetimes.com/leading-edge-ai-ic-designs-demand-comprehensive-hav-methodologies/",
    "source": "Juergen Jaeger, Director of Prototyping Product Strategy, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T13:00:00+00:00",
    "summary": "Learn how comprehensive hardware-assisted verification helps AI SoC teams accelerate RTL, software development and system validation. The post Leading-edge AI IC designs demand comprehensive HAV metho"
  },
  {
    "id": "rss:https://www.eetimes.com/can-ai-command-earth-to-orbit-operations/",
    "domain": "AI 算力 / 半导体",
    "title": "Can AI Command Earth-to-Orbit Operations?",
    "url": "https://www.eetimes.com/can-ai-command-earth-to-orbit-operations/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T08:00:00+00:00",
    "summary": "The aerospace and defense sector is facing a confluence of geopolitical instability, rapid technological advances, evolving security requirements, and complex global supply chains. The post Can AI Com"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/razer-naga-v3-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Naga V3 Pro Review: My new 23-button mouse",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/razer-naga-v3-pro-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T20:18:32+00:00",
    "summary": "Razer's Naga V3 Pro has the same form factor as its predecessor, but it features more buttons, an upgraded sensor and switches, and better battery life."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-expand-production-capacity-in-china-as-it-mulls-solidigm-ipo-report-claims-second-phase-of-fab-could-boost-local-production-by-50-percent",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix to expand production capacity in China as it mulls Solidigm IPO, report claims — second phase of fab could boost local production by 50%",
    "url": "https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-expand-production-capacity-in-china-as-it-mulls-solidigm-ipo-report-claims-second-phase-of-fab-could-boost-local-production-by-50-percent",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T16:39:42+00:00",
    "summary": "As demand for high-end data center SSDs peak, SK hynix upgrades its Chinese facilities and plans Solidigm listing at NASDAQ."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-highlights-ryzen-5-5500-briefly-topping-amazon-cpu-best-sellers-beating-9800x3d-usd80-ddr4-cpu-remains-a-top-seller-during-memory-crunch",
    "domain": "AI 算力 / 半导体",
    "title": "AMD highlights Ryzen 5 5500 briefly topping Amazon CPU best sellers, beating 9800X3D — $80 DDR4 CPU remains a top seller during memory crunch",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-highlights-ryzen-5-5500-briefly-topping-amazon-cpu-best-sellers-beating-9800x3d-usd80-ddr4-cpu-remains-a-top-seller-during-memory-crunch",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T15:06:35+00:00",
    "summary": "AMD's marketing director shared a screenshot of the Amazon CPU best sellers list, but the four-year-old, $80 Ryzen 5 5500 was at the top of the charts."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-raises-usd19-7-billion-to-help-fund-future-projects-as-14a-production-looms-share-sale-attracted-usd100-billion-in-demand-report-claims",
    "domain": "AI 算力 / 半导体",
    "title": "Intel raises $19.7 billion to help fund future projects as 14A production looms — share sale attracted $100 billion in demand, report claims",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-raises-usd19-7-billion-to-help-fund-future-projects-as-14a-production-looms-share-sale-attracted-usd100-billion-in-demand-report-claims",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T13:35:25+00:00",
    "summary": "Intel is raising $19.7 billion through a stock offering to strengthen its finances as it expands manufacturing capacity, develops next-generation process technologies, and is trying to attract major e"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/benchmarking-amds-bc-250-offering-steam-machine-like-performance-at-half-the-price-unlocking-40-cus-eight-zen-2-cores-on-the-repurposed-ps5-apu",
    "domain": "AI 算力 / 半导体",
    "title": "Benchmarking AMD's BC-250, offering Steam Machine-like performance at half the price — unlocking 40 CUs, eight Zen 2 cores on the repurposed PS5 APU",
    "url": "https://www.tomshardware.com/pc-components/cpus/benchmarking-amds-bc-250-offering-steam-machine-like-performance-at-half-the-price-unlocking-40-cus-eight-zen-2-cores-on-the-repurposed-ps5-apu",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T13:13:49+00:00",
    "summary": "The popular BC-250 APU has seen some major advancements over the past few months, including a 40CU unlock and enabling all eight Zen 2 cores. We put together a BC-250 machine to see how it works, and "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/deepcool-ak620-and-ak400-g2-review-quiet-and-powerful-with-woodgrain-or-a-digital-display",
    "domain": "AI 算力 / 半导体",
    "title": "DeepCool AK620 and AK400 G2 Review: Quiet and powerful, with woodgrain or a digital display",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/deepcool-ak620-and-ak400-g2-review-quiet-and-powerful-with-woodgrain-or-a-digital-display",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T12:05:00+00:00",
    "summary": "DeepCool’s latest AK G2 series air coolers feature your choice of woodgrain tops or a digital display. We’ve tested both AK620 and AK400 G2 coolers with AMD’s Ryzen 9 9950X3D to benchmark their therma"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/fcc-proposes-import-ban-on-chinese-optical-transceivers-blockade-targets-key-ai-interconnects-as-china-holds-56-percent-global-market-share",
    "domain": "AI 算力 / 半导体",
    "title": "FCC proposes import ban on Chinese optical transceivers — blockade targets key AI interconnects as China holds 56% global market share",
    "url": "https://www.tomshardware.com/tech-industry/fcc-proposes-import-ban-on-chinese-optical-transceivers-blockade-targets-key-ai-interconnects-as-china-holds-56-percent-global-market-share",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T12:03:36+00:00",
    "summary": "The FCC is drafting a proposal that would expand its list of equipment and services covered by the Secure Networks Act to include imports of new-model optical transceivers manufactured in China."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/usd580-million-undersea-cable-rerouted-to-avoid-the-grave-of-dobby-the-house-elf-company-caves-to-fan-demands-to-safeguard-harry-potter-filming-location-will-instead-pass-by-bronze-age-burial-site",
    "domain": "AI 算力 / 半导体",
    "title": "$580 million undersea cable rerouted to avoid the grave of Dobby the House Elf — company caves to fan demands to safeguard Harry Potter filming location, will instead pass by Bronze Age burial site",
    "url": "https://www.tomshardware.com/networking/usd580-million-undersea-cable-rerouted-to-avoid-the-grave-of-dobby-the-house-elf-company-caves-to-fan-demands-to-safeguard-harry-potter-filming-location-will-instead-pass-by-bronze-age-burial-site",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T11:47:22+00:00",
    "summary": "The Greenlink Connector project, which will connect the grid of Ireland and Wales, had to reroute its path after Harry Potter fans complained that it would 'desecrate' the 'grave' of beloved character"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-for-usd261-in-this-am5-gaming-bundle-usd970-deal-features-ryzen-7-9800x3d-32gb-ddr5-ram-a-gigabyte-x870-motherboard-and-free-240mm-aio",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB of DDR5 for $261 in this AM5 gaming bundle — $970 deal features Ryzen 7 9800X3D, 32GB DDR5 RAM, a Gigabyte X870 motherboard, and free 240mm AIO",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-for-usd261-in-this-am5-gaming-bundle-usd970-deal-features-ryzen-7-9800x3d-32gb-ddr5-ram-a-gigabyte-x870-motherboard-and-free-240mm-aio",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T11:46:49+00:00",
    "summary": "Newegg’s $969 AM5 combo pairs the Ryzen 7 9800X3D, 32GB of DDR5-6000 RAM, a Gigabyte X870 Aorus Elite Wi-Fi 7 motherboard, and a free 240mm AIO, saving nearly $220."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/u-s-lawmaker-wants-govt-to-enforce-regulation-to-ensure-chipmakers-conduct-adequate-due-diligence-on-their-customers-house-member-calls-for-biden-era-export-control-to-be-enforced",
    "domain": "AI 算力 / 半导体",
    "title": "US lawmaker wants gov't to enforce regulation to ensure 'chipmakers conduct adequate due diligence on their customers' — House member calls for Biden-era export control to be enforced",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/u-s-lawmaker-wants-govt-to-enforce-regulation-to-ensure-chipmakers-conduct-adequate-due-diligence-on-their-customers-house-member-calls-for-biden-era-export-control-to-be-enforced",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T11:20:00+00:00",
    "summary": "Congressman John Moolenaar wants the Commerce Department's Bureau of Industry and Security to clarify whether Foundry Due Diligence Rule remains effective and continues to be enforced."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/this-usd30-hoto-25-piece-electric-screwdriver-set-is-a-must-buy-option-for-pc-builders-and-hobbyists-40-percent-saving-on-portable-driver-with-long-life-1-500-mah-battery-and-25-ultra-hard-bits-for-your-next-project",
    "domain": "AI 算力 / 半导体",
    "title": "This $30 Hoto 25-piece electric screwdriver set is a must-buy option for PC builders and hobbyists —40% saving on portable driver with long-life 1,500 mAh battery and 25 ultra-hard bits for your next ",
    "url": "https://www.tomshardware.com/desktops/pc-building/this-usd30-hoto-25-piece-electric-screwdriver-set-is-a-must-buy-option-for-pc-builders-and-hobbyists-40-percent-saving-on-portable-driver-with-long-life-1-500-mah-battery-and-25-ultra-hard-bits-for-your-next-project",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T11:09:08+00:00",
    "summary": "Save 40% on this Hoto electric screwdriver with 25 bits, now just $29.99 for a limited time only."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-teams-up-with-financial-giants-to-create-usd500-billion-ai-infrastructure-funds-six-investment-firms-to-enable-access-to-long-term-funding-at-attractive-rates",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia teams up with financial giants to create $500 billion AI infrastructure funds — six investment firms to enable access to long-term funding at attractive rates",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-teams-up-with-financial-giants-to-create-usd500-billion-ai-infrastructure-funds-six-investment-firms-to-enable-access-to-long-term-funding-at-attractive-rates",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T11:04:32+00:00",
    "summary": "Nvidia to arrange financing from major financial institutions at attractive rates for customers seeking to build AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/initial-seeder-on-popular-anime-torrenting-site-nyaa-arrested-by-japanese-authorities-anti-piracy-group-claims-it-identified-user-without-torrent-swarm-monitoring",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese authorities use new tool to identify initial torrent uploaders — anti-piracy group says it identified seeder on popular anime torrenting website without torrent swarm monitoring",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/initial-seeder-on-popular-anime-torrenting-site-nyaa-arrested-by-japanese-authorities-anti-piracy-group-claims-it-identified-user-without-torrent-swarm-monitoring",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T11:00:00+00:00",
    "summary": "Japanese authorities have taken a big step in cracking down on piracy by arresting an initial-seeder at popular anime torrenting website Nyaa."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modder-adds-radeon-rx-9070-xt-egpu-to-steam-machine-runs-crimson-desert-at-over-100-fps-on-high-moves-boot-drive-to-usb-c-port-leverages-m-2-to-oculink-adaptor-and-egpu-dock",
    "domain": "AI 算力 / 半导体",
    "title": "Modder adds Radeon RX 9070 XT eGPU to Steam Machine, runs Crimson Desert at over 100 FPS on High — moves boot drive to USB-C port, leverages M.2 to OCuLink adaptor and eGPU dock",
    "url": "https://www.tomshardware.com/pc-components/gpus/modder-adds-radeon-rx-9070-xt-egpu-to-steam-machine-runs-crimson-desert-at-over-100-fps-on-high-moves-boot-drive-to-usb-c-port-leverages-m-2-to-oculink-adaptor-and-egpu-dock",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T10:57:43+00:00",
    "summary": "A Redditor has successfully connected a very powerful eGPU the Steam Machine via an M.2 to OCuLink adapter."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/wireless-ota-charging-with-lasers-could-keep-drones-airborne-indefinitely-improved-receiver-converts-at-38-49-percent-efficiency-and-uses-nanocrystalline-material-for-thermals",
    "domain": "AI 算力 / 半导体",
    "title": "Laser wireless charging could keep drones airborne indefinitely — improved receiver converts at 38.49% efficiency and uses nanocrystalline material for thermals",
    "url": "https://www.tomshardware.com/tech-industry/drones/wireless-ota-charging-with-lasers-could-keep-drones-airborne-indefinitely-improved-receiver-converts-at-38-49-percent-efficiency-and-uses-nanocrystalline-material-for-thermals",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T10:30:00+00:00",
    "summary": "Researchers use a ground-based laser to wirelessly deliver power to drones, potentially allowing them to stay airborne without landing to recharge."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/walmart-has-slashed-usd600-off-this-rtx-5060-powered-gaming-laptop-now-just-usd1-099-get-gigabytes-16-inch-aero-x16-with-16gb-of-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Walmart has slashed $600 off this RTX 5060-powered gaming laptop, now just $1,099 — get Gigabyte's 16-inch Aero X16 with 16GB of RAM and a 1TB SSD",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/walmart-has-slashed-usd600-off-this-rtx-5060-powered-gaming-laptop-now-just-usd1-099-get-gigabytes-16-inch-aero-x16-with-16gb-of-ram-and-a-1tb-ssd",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T10:28:20+00:00",
    "summary": "A gaming laptop that won't break the bank during the memory price crisis. Gigabyte's RTX 5060-powered Aero X16 has $600 slashed off the list price."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/gamer-recruitment-drive-results-in-supercharged-hiring-campaign-for-new-air-traffic-controllers-usdot-secretary-reckons-theyve-got-the-strongest-sharpest-workforce-in-aviation-history",
    "domain": "AI 算力 / 半导体",
    "title": "Gamer recruitment drive results in ‘supercharged’ hiring campaign for new Air Traffic Controllers — 94% hiring goal hit in record time with $155,000 salary potential; ‘the strongest, sharpest workforc",
    "url": "https://www.tomshardware.com/video-games/gamer-recruitment-drive-results-in-supercharged-hiring-campaign-for-new-air-traffic-controllers-usdot-secretary-reckons-theyve-got-the-strongest-sharpest-workforce-in-aviation-history",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T10:00:00+00:00",
    "summary": "The campaign to recruit video gamers into Air Traffic Control jobs has been a resounding success, according to U.S. Department of Transport head Secretary Sean P. Duffy."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/case-mods/diy-modder-creates-heat-engine-computing-device-powered-by-a-stirling-engine-80-mhz-esp32-can-run-tetris-snake-and-pong-on-just-150-milliwatts-of-power",
    "domain": "AI 算力 / 半导体",
    "title": "DIY modder creates 'heat engine computing device' powered by a Stirling engine, can run Tetris, Snake, and Pong — 80 MHz processor operates on just 150 milliwatts of power",
    "url": "https://www.tomshardware.com/pc-components/case-mods/diy-modder-creates-heat-engine-computing-device-powered-by-a-stirling-engine-80-mhz-esp32-can-run-tetris-snake-and-pong-on-just-150-milliwatts-of-power",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T09:30:00+00:00",
    "summary": "The custom machine uses an ESP32-C3, OLED display, and 16-key keypad while squeezing retro gaming into a tiny 150mW power budget."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/xbox-pc-and-game-pass-titles-are-coming-to-linux-through-xodus-heroic-launcher-devs-embark-on-new-open-source-reverse-engineering-project",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox PC and Game Pass titles are coming to Linux through 'Xodus' — Heroic Launcher devs embark on new open-source reverse-engineering project",
    "url": "https://www.tomshardware.com/software/linux/xbox-pc-and-game-pass-titles-are-coming-to-linux-through-xodus-heroic-launcher-devs-embark-on-new-open-source-reverse-engineering-project",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T18:11:48+00:00",
    "summary": "You might be able to enjoy Xbox PC and PC Game Pass titles on Linux very soon thanks to the efforts of the Xodus team, who're emulating the entire Xbox PC stack through open-source implementations of "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/geforce-rtx-50-series-gpu-prices-spike-as-much-as-39-percent-as-blackwell-price-hikes-hit-the-us-rtx-5070-gets-a-36-percent-hike-rtx-5060-up-27-percent-at-the-median-of-newegg-listings",
    "domain": "AI 算力 / 半导体",
    "title": "GeForce RTX 50-series GPU prices spike as much as 39% as Blackwell price hikes hit the US — RTX 5070 gets a 36% hike, RTX 5060 up 27% at the median of Newegg listings",
    "url": "https://www.tomshardware.com/pc-components/gpus/geforce-rtx-50-series-gpu-prices-spike-as-much-as-39-percent-as-blackwell-price-hikes-hit-the-us-rtx-5070-gets-a-36-percent-hike-rtx-5060-up-27-percent-at-the-median-of-newegg-listings",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T16:55:46+00:00",
    "summary": "After recent news of price hikes on RTX 50-series GPUs in other regions, those same increases now appear to have come Stateside, as Newegg prices for some Blackwell cards have spiked as much as 39% co"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-testing-lower-memory-configs-of-rubin-ultra-as-memory-shortage-bites-back-designs-tested-include-as-little-as-192-gb-and-step-back-to-hbm4",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly testing lower memory configs of Rubin Ultra as memory shortage bites back — designs tested include as little as 192 GB and step back to HBM4",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-testing-lower-memory-configs-of-rubin-ultra-as-memory-shortage-bites-back-designs-tested-include-as-little-as-192-gb-and-step-back-to-hbm4",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T16:47:00+00:00",
    "summary": "Nvidia is reportedly testing at least three Rubin Ultra configurations that pack as little as 192 GB of memory, as opposed to the 1 TB of HBM4E originally announced."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-ai-agent-tasked-with-booking-a-gym-class-hacks-system-removes-other-participant-says-sorry-about-that-after-trying-to-bump-user-up-the-waitlist",
    "domain": "AI 算力 / 半导体",
    "title": "Rogue AI agent tasked with booking a gym class hacks system, removes other participant — says 'sorry about that' after trying to bump user up the waitlist",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-ai-agent-tasked-with-booking-a-gym-class-hacks-system-removes-other-participant-says-sorry-about-that-after-trying-to-bump-user-up-the-waitlist",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T16:00:02+00:00",
    "summary": "A rogue OpenClaw tasked with booking a gym class for its user hacked into the system and removed another participant."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-5-250k-plus-is-down-to-its-lowest-price-ever-at-usd154-get-a-20-core-midrange-cpu-with-5-5-ghz-boost-for-an-entry-level-price",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Core Ultra 5 250K Plus is down to its lowest price ever at $154 — get a 18-core midrange CPU with 5.3 GHz boost for an entry-level price",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-5-250k-plus-is-down-to-its-lowest-price-ever-at-usd154-get-a-20-core-midrange-cpu-with-5-5-ghz-boost-for-an-entry-level-price",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T13:54:16+00:00",
    "summary": "Intel's 18-core Core Ultra 5 250K Plus is down to its lowest price ever on Amazon, selling for just $154 on sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/acer-swift-go-16-ai-amd-gorgon-point-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer Swift Go 16 AI (AMD Gorgon Point) Review: A balanced, affordable, big-screen portable",
    "url": "https://www.tomshardware.com/laptops/acer-swift-go-16-ai-amd-gorgon-point-review",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T13:05:00+00:00",
    "summary": "Acer’s Swift Go 16 AI is a capable mid-range laptop with a large touchscreen and a slim metal shell. It stands out among modern competition, if you can find it on sale for under $1,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-bans-surge-past-500-nationwide-as-local-us-politicians-begin-blocking-new-developments-growing-public-outrage-and-bipartisan-pushback-threaten-big-tech-expansion-plans",
    "domain": "AI 算力 / 半导体",
    "title": "AI data center bans surge past 500 nationwide as local US politicians begin blocking new developments — growing public outrage and bipartisan pushback threaten big tech expansion plans",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-bans-surge-past-500-nationwide-as-local-us-politicians-begin-blocking-new-developments-growing-public-outrage-and-bipartisan-pushback-threaten-big-tech-expansion-plans",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T12:25:51+00:00",
    "summary": "New AI data center development bans jumped to over 500 in July, according to recent analysis, with political and public pressure growing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/hyperscalers-commit-nearly-usd2-trillion-to-secure-ai-hardware-and-memory-google-leads-usd811-billion-spending-surge-while-apple-trails-at-usd57-billion",
    "domain": "AI 算力 / 半导体",
    "title": "Hyperscalers commit nearly $2 trillion to secure AI hardware and memory — Google leads $811 billion spending surge while Apple trails at $57 billion",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/hyperscalers-commit-nearly-usd2-trillion-to-secure-ai-hardware-and-memory-google-leads-usd811-billion-spending-surge-while-apple-trails-at-usd57-billion",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T12:00:00+00:00",
    "summary": "As hyperscalers increase their long-term purchase commitments, the high-tech industry faces a tectonic shift as CSPs overwhelm consumer electronics companies."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/geforce-now-exploit-lets-you-access-the-full-windows-desktop-through-a-simple-file-swap-modder-runs-local-ai-models-on-ultimate-tier-with-48gb-of-vram-and-no-restrictions",
    "domain": "AI 算力 / 半导体",
    "title": "GeForce NOW exploit lets you access the full Windows desktop through a simple file swap — Modder runs local AI models on Ultimate tier with 48GB of VRAM and no restrictions",
    "url": "https://www.tomshardware.com/service-providers/streaming/geforce-now-exploit-lets-you-access-the-full-windows-desktop-through-a-simple-file-swap-modder-runs-local-ai-models-on-ultimate-tier-with-48gb-of-vram-and-no-restrictions",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T12:00:00+00:00",
    "summary": "Swapping the executable of a game with a modified file will fool Steam into thinking it's opening that game when it's really just giving you unrestricted desktop access. This is against GeForce NOW's "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/steam-hardware-distributor-hit-by-cyberattack-expect-fake-messages-valve-warns-europe-vendor-has-personal-information-and-hardware-purchase-details-stolen",
    "domain": "AI 算力 / 半导体",
    "title": "Steam hardware distributor hit by cyberattack, 'expect fake messages,' Valve warns — Europe vendor has personal information and hardware purchase details stolen",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/steam-hardware-distributor-hit-by-cyberattack-expect-fake-messages-valve-warns-europe-vendor-has-personal-information-and-hardware-purchase-details-stolen",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T11:49:06+00:00",
    "summary": "Steam hardware customers in Europe should 'expect fake messages' said Valve in an email bulletin, after a distributor's security was breached."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/over-70-percent-of-americans-oppose-ai-data-centers-us-protests-intensify-as-more-arrests-are-being-made-almost-40-arrested-this-year-in-backlash-to-ai-factory-buildout",
    "domain": "AI 算力 / 半导体",
    "title": "Over 70% of Americans oppose AI data centers; US protests intensify as more arrests are being made — almost 40 arrested this year in backlash to AI factory buildout",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/over-70-percent-of-americans-oppose-ai-data-centers-us-protests-intensify-as-more-arrests-are-being-made-almost-40-arrested-this-year-in-backlash-to-ai-factory-buildout",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T11:40:00+00:00",
    "summary": "The public pushback against data center construction projects is only growing stronger, even as some protesting local residents have been arrested in the process."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/hoverair-unveils-the-versa-modular-pocket-gimbal-camera-that-transforms-into-a-self-flying-drone-modular-camera-transforms-into-an-auto-tracking-drone-by-magnetically-snapping-together-for-instant-palm-launch-and-ai-tracking",
    "domain": "AI 算力 / 半导体",
    "title": "HoverAir unveils the Versa modular pocket gimbal camera that transforms into a self-flying drone — Modular camera transforms into an auto-tracking drone by magnetically snapping together for instant p",
    "url": "https://www.tomshardware.com/tech-industry/drones/hoverair-unveils-the-versa-modular-pocket-gimbal-camera-that-transforms-into-a-self-flying-drone-modular-camera-transforms-into-an-auto-tracking-drone-by-magnetically-snapping-together-for-instant-palm-launch-and-ai-tracking",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T11:20:00+00:00",
    "summary": "Have you ever wanted a pocket gimbal camera and a selfie drone that follows your around autonomously in one device? That's what the HoverAir Versa offers with a transforming, two-in-one body that can "
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
    "id": "rss:https://www.eetimes.com/after-seven-ceos-in-10-years-imagination-is-sticking-to-its-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "After Seven CEOs in 10 Years, Imagination Is Sticking to Its Strategy",
    "url": "https://www.eetimes.com/after-seven-ceos-in-10-years-imagination-is-sticking-to-its-strategy/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T22:00:00+00:00",
    "summary": "Imagination dumps CPU/NPU dreams, doubles down on GPUs and China under CEO No. 7. The post After Seven CEOs in 10 Years, Imagination Is Sticking to Its Strategy appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/rolecs-technoplus-ip-rated-pole-mount-plastic-enclosures-for-iot-iiot-and-factory-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "ROLEC’s technoPLUS: IP-rated Pole-mount Plastic Enclosures for IoT/IIoT and Factory Automation",
    "url": "https://www.eetimes.com/rolecs-technoplus-ip-rated-pole-mount-plastic-enclosures-for-iot-iiot-and-factory-automation/",
    "source": "ROLEC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:15:30+00:00",
    "summary": "IoT/IIoT and factory automation are driving demand for ROLEC’s updated pole-mountable technoPLUS (IP 66, IP 67, IP 69K) plastic enclosures. Electronics designers specify them for ‘close-to-the-process"
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
    "id": "hn:48894277",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-13T15:32:19+00:00",
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
    "points": 447,
    "published_at": "2026-08-08T09:18:50+00:00",
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
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 390,
    "published_at": "2026-07-15T18:40:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259339",
    "domain": "大厂 AI 动态",
    "title": "Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp",
    "url": "https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md",
    "source": "frabonacci",
    "platform": "hackernews",
    "points": 289,
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
    "points": 169,
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
    "id": "rss:https://www.theverge.com/games/978558/rideshare-stimulator-writer-ai-saber-interactive",
    "domain": "大厂 AI 动态",
    "title": "Saber denies replacing Rideshare Stimulator&#8217;s writers with ChatGPT",
    "url": "https://www.theverge.com/games/978558/rideshare-stimulator-writer-ai-saber-interactive",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T00:39:26+00:00",
    "summary": "After a former lead writer claimed Saber \"replaced me with ChatGPT,\" CEO Matthew Karch now claims, \"Neither Saber nor Unigine have replaced any writers with AI,\" for the Rideshare \"Stimulator\" game an"
  },
  {
    "id": "rss:https://www.theverge.com/games/978374/xbox-elite-3-prototype-pad-leaks-with-tiny-built-in-screen",
    "domain": "大厂 AI 动态",
    "title": "Xbox Elite 3 prototype pad leaks with tiny built-in screen",
    "url": "https://www.theverge.com/games/978374/xbox-elite-3-prototype-pad-leaks-with-tiny-built-in-screen",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T22:36:35+00:00",
    "summary": "Did a prototype Microsoft gamepad fall off the back of a truck? We can't say, but a Redditor has legit-looking photos of a prototype Xbox controller that's almost certainly the Xbox Elite Series 3. In"
  },
  {
    "id": "rss:https://www.theverge.com/tech/978355/sonos-headphones-fcc-filing",
    "domain": "大厂 AI 动态",
    "title": "An FCC filing points to new Sonos headphones coming soon",
    "url": "https://www.theverge.com/tech/978355/sonos-headphones-fcc-filing",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T21:23:30+00:00",
    "summary": "It looks like we'll be getting a successor to the Sonos Ace headphones sometime this fall, which was hinted at by CEO Tom Conrad during a third quarter earnings call. As reported by What Hi-Fi?, an FC"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/978113/chatgpt-gemini-1-billion-users",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT and Gemini both just passed 1 billion users",
    "url": "https://www.theverge.com/ai-artificial-intelligence/978113/chatgpt-gemini-1-billion-users",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T19:41:42+00:00",
    "summary": "For the 14th time, a Google product has hit 1 billion users. Google CEO Sundar Pichai posted on X that a billion people are using Gemini every month, and that Gemini is Google's fastest-growing produc"
  },
  {
    "id": "rss:https://www.theverge.com/tech/978181/meta-threads-quest-vr-app",
    "domain": "大厂 AI 动态",
    "title": "Threads has a VR app now",
    "url": "https://www.theverge.com/tech/978181/meta-threads-quest-vr-app",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T19:10:14+00:00",
    "summary": "Meta has launched a Threads app for Meta Quest VR headsets, the company announced on Tuesday. The launch follows Meta bringing the app to its Ray-Ban Display AR glasses last month and the recent news "
  },
  {
    "id": "rss:https://www.theverge.com/tech/978152/google-tv-freeplay-on-demand",
    "domain": "大厂 AI 动态",
    "title": "Google’s free streaming service now lets you pick shows and movies to watch",
    "url": "https://www.theverge.com/tech/978152/google-tv-freeplay-on-demand",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T18:35:16+00:00",
    "summary": "Google TV Freeplay, the company's free, ad-supported streaming service, now supports video on demand. Instead of tuning into Google TV Freeplay's selection of always-on channels, you can now choose fr"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/978048/brad-lightcap-openai-executive-departure",
    "domain": "大厂 AI 动态",
    "title": "Another OpenAI executive takes off",
    "url": "https://www.theverge.com/ai-artificial-intelligence/978048/brad-lightcap-openai-executive-departure",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T17:50:01+00:00",
    "summary": "Brad Lightcap, OpenAI's special projects lead and the company's former COO, announced his departure after an eight-year stint at the AI lab. In an internal memo he later posted to X, Lightcap told col"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/977929/pixel-buds-2a-starfox-switch-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The budget-friendly Pixel Buds 2a are even cheaper right now",
    "url": "https://www.theverge.com/gadgets/977929/pixel-buds-2a-starfox-switch-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T17:31:06+00:00",
    "summary": "Looking for great pair of earbuds that work particularly well with Android phones? The Google Pixel Buds 2a are currently discounted to $99 (usually $129) at various retailers, including Amazon, Best "
  },
  {
    "id": "rss:https://www.theverge.com/tech/977844/made-by-google-pixel-11-launch-power-users-notification-led",
    "domain": "大厂 AI 动态",
    "title": "Google’s upcoming Pixel phones are for the fans, even if its launch event isn’t",
    "url": "https://www.theverge.com/tech/977844/made-by-google-pixel-11-launch-power-users-notification-led",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T17:00:00+00:00",
    "summary": "Last year's Made by Google event for the Pixel 10 resembled a late night talk show, complete with Jimmy Fallon as host, and it aired an hour after the phones were revealed. Spec dives and executive ap"
  },
  {
    "id": "rss:https://www.theverge.com/tech/977561/made-by-google-2026-pixel-11-news",
    "domain": "大厂 AI 动态",
    "title": "Made by Google 2026: all the Pixel news and announcements",
    "url": "https://www.theverge.com/tech/977561/made-by-google-2026-pixel-11-news",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T17:00:00+00:00",
    "summary": "Google is gearing up to reveal a bunch of new Pixel devices on August 12th. A series of leaks leading up to the event suggest that the Pixel 11 lineup will come in an array of colors, with signs point"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/indias-yulu-raises-93m-as-quick-commerce-boom-fuels-e-bike-demand/",
    "domain": "大厂 AI 动态",
    "title": "India’s Yulu raises $93M as quick-commerce boom fuels e-bike demand",
    "url": "https://techcrunch.com/2026/08/11/indias-yulu-raises-93m-as-quick-commerce-boom-fuels-e-bike-demand/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:30:00+00:00",
    "summary": "Yulu aims to have a fleet of 200,000 bikes in the next two years and faster electric two-wheelers, aiming at new logistics use cases."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/phoebe-gates-and-sophia-kianni-reportedly-knew-phia-was-cookie-stuffing-for-months/",
    "domain": "大厂 AI 动态",
    "title": "Phoebe Gates and Sophia Kianni reportedly knew Phia was ‘cookie stuffing’ for months",
    "url": "https://techcrunch.com/2026/08/11/phoebe-gates-and-sophia-kianni-reportedly-knew-phia-was-cookie-stuffing-for-months/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T21:39:58+00:00",
    "summary": "Phia, the shopping startup co-founded by Phoebe Gates and Sophia Kianni, is once again under fire for its alleged business practices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/accel-closes-oversubscribed-550m-india-fund-within-weeks-19-months-after-its-last/",
    "domain": "大厂 AI 动态",
    "title": "Accel closes oversubscribed $550M India fund within weeks, 19 months after its last",
    "url": "https://techcrunch.com/2026/08/11/accel-closes-oversubscribed-550m-india-fund-within-weeks-19-months-after-its-last/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T21:39:11+00:00",
    "summary": "The U.S. VC firm still has more than 55% of its previous $650 million India fund available for deployment."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/uber-surprised-robotics-company-serve-by-selling-its-entire-stake/",
    "domain": "大厂 AI 动态",
    "title": "Uber surprised robotics company Serve by selling its entire stake",
    "url": "https://techcrunch.com/2026/08/11/uber-surprised-robotics-company-serve-by-selling-its-entire-stake/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T20:02:02+00:00",
    "summary": "The divestiture comes as the two once-tight companies have started to diverge on the business side."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/fbi-says-cybercriminals-are-hacking-into-victims-online-accounts-to-steal-their-intimate-pictures/",
    "domain": "大厂 AI 动态",
    "title": "FBI says cybercriminals are hacking into victims’ online accounts to steal their intimate pictures",
    "url": "https://techcrunch.com/2026/08/11/fbi-says-cybercriminals-are-hacking-into-victims-online-accounts-to-steal-their-intimate-pictures/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T19:38:23+00:00",
    "summary": "In a new alert, the FBI said cybercriminals are targeting adults and minors in an attempt to steal their personal and intimate pictures in extortion campaigns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/openai-launches-chatgpt-desktop-app-for-linux/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches ChatGPT desktop app for Linux",
    "url": "https://techcrunch.com/2026/08/11/openai-launches-chatgpt-desktop-app-for-linux/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T19:15:35+00:00",
    "summary": "OpenAI is finally bringing a dedicated ChatGPT desktop app to Linux operating systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/googles-gemini-app-surges-to-one-billion-users/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Gemini app surges to 1 billion users",
    "url": "https://techcrunch.com/2026/08/11/googles-gemini-app-surges-to-one-billion-users/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T18:49:12+00:00",
    "summary": "Google also shared numbers of how people are actually using the chatbot, with 63% of Gemini users talking directly to the assistant using the voice feature. Plus, Gemini now generates more than 150 mi"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/blueskys-active-user-base-is-shrinking-as-its-focus-expands-beyond-the-app/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky’s active user base is shrinking as its focus expands beyond the app",
    "url": "https://techcrunch.com/2026/08/11/blueskys-active-user-base-is-shrinking-as-its-focus-expands-beyond-the-app/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T17:46:14+00:00",
    "summary": "Over a year following its post-election surge, Bluesky’s mobile app is seeing a continued decline in active users, though its remaining community is still relatively engaged."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/whats-scaleup-europe-the-5-7b-fund-that-just-backed-satellite-company-iceye/",
    "domain": "大厂 AI 动态",
    "title": "What’s Scaleup Europe, the $5.7B fund that just backed satellite company ICEYE?",
    "url": "https://techcrunch.com/2026/08/11/whats-scaleup-europe-the-5-7b-fund-that-just-backed-satellite-company-iceye/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T17:41:49+00:00",
    "summary": "Scaleup Europe, a public-private fund with a $5.7 billion target, made its first investment by backing Finnish satellite company ICEYE."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/brad-lightcap-openais-longtime-coo-is-leaving-to-start-something-new/",
    "domain": "大厂 AI 动态",
    "title": "Brad Lightcap, OpenAI’s longtime COO, is leaving to ‘start something new’",
    "url": "https://techcrunch.com/2026/08/11/brad-lightcap-openais-longtime-coo-is-leaving-to-start-something-new/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T17:41:34+00:00",
    "summary": "One of OpenAI's longest-serving executives is headed out the door, although the longtime COO told staff that he was \"excited to help you all advance the mission from a different vantage point.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/",
    "domain": "大厂 AI 动态",
    "title": "General Catalyst leads $1.1B round into 2-month-old River AI",
    "url": "https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T17:41:22+00:00",
    "summary": "River AI, a startup founded by xAI co-founder Igor Babuschkin, has a fascinating vision for personal agents and secured $1.1 billion out of the gate."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/",
    "domain": "大厂 AI 动态",
    "title": "An unreleased Anthropic model made progress on one of math’s biggest unsolved problems",
    "url": "https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T16:25:20+00:00",
    "summary": "For more than 150 years, the Riemann hypothesis has stood as one of the major unsolved problems in mathematics. Anthropic hasn't solved it — but the company's models made more progress than you might "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/joby-aviation-builds-out-defense-business-with-500m-acquisition/",
    "domain": "大厂 AI 动态",
    "title": "Joby Aviation builds out defense business with $500M acquisition",
    "url": "https://techcrunch.com/2026/08/11/joby-aviation-builds-out-defense-business-with-500m-acquisition/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T16:06:08+00:00",
    "summary": "Joby Aviation reached an agreement to acquire Resonant Sciences, which will kick off its new defense business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/delta-investigating-after-someone-set-up-fake-wi-fi-network-mid-flight/",
    "domain": "大厂 AI 动态",
    "title": "Delta investigating after someone set up fake Wi-Fi network mid-flight",
    "url": "https://techcrunch.com/2026/08/11/delta-investigating-after-someone-set-up-fake-wi-fi-network-mid-flight/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T15:40:46+00:00",
    "summary": "The Delta flight crew switched off the aircraft's legitimate Wi-Fi network for around 30 minutes due to the incident, according to a spokesperson."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/2025s-most-downloaded-game-block-blast-is-going-ad-free-on-apple-arcade/",
    "domain": "大厂 AI 动态",
    "title": "Block Blast! goes ad-free on Apple Arcade",
    "url": "https://techcrunch.com/2026/08/11/2025s-most-downloaded-game-block-blast-is-going-ad-free-on-apple-arcade/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T15:33:59+00:00",
    "summary": "Block Blast!, the most downloaded mobile game of 2025, is coming to Apple Arcade in September, where it will be ad-free."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/rivian-ceo-rj-scaringe-is-betting-on-evs-robots-and-autonomy-all-at-once-hell-explain-why-at-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Rivian CEO RJ Scaringe is betting on EVs, robots, and autonomy all at once — he’ll explain why at Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/11/rivian-ceo-rj-scaringe-is-betting-on-evs-robots-and-autonomy-all-at-once-hell-explain-why-at-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T15:30:00+00:00",
    "summary": "Rivian's CEO RJ Scaringe is speaking at TechCrunch Disrupt 2026 to detail his journey, and the lessons it’s bestowed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/flightaware-sues-kalshi-over-flight-cancellation-prediction-markets/",
    "domain": "大厂 AI 动态",
    "title": "FlightAware sues Kalshi over flight cancellation prediction markets",
    "url": "https://techcrunch.com/2026/08/11/flightaware-sues-kalshi-over-flight-cancellation-prediction-markets/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T15:23:58+00:00",
    "summary": "FlightAware says that Kalshi used its name and data to offer bets on flight cancellations without the flight tracker's permission."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/kyoto-fusioneering-starts-work-on-key-fusion-power-plant-device/",
    "domain": "大厂 AI 动态",
    "title": "Kyoto Fusioneering starts work on key fusion power plant device",
    "url": "https://techcrunch.com/2026/08/11/kyoto-fusioneering-starts-work-on-key-fusion-power-plant-device/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T15:00:00+00:00",
    "summary": "Fusion power startups are turning to Kyoto Fusioneering to supply components for future power plants. The Japan-based startup just received a grant to build a part of the fuel system."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/bumble-ditches-its-rule-that-kept-men-from-making-the-first-move/",
    "domain": "大厂 AI 动态",
    "title": "Bumble ditches its rule that kept men from making the first move",
    "url": "https://techcrunch.com/2026/08/11/bumble-ditches-its-rule-that-kept-men-from-making-the-first-move/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T13:59:26+00:00",
    "summary": "Bumble is ditching the rule that it has enforced since launching in 2024. Men can finally message first."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/11/north-korean-remote-it-staffer-worked-for-us-government-agency-says-fbi/",
    "domain": "大厂 AI 动态",
    "title": "North Korean remote IT staffer worked for US government agency, says FBI",
    "url": "https://techcrunch.com/2026/08/11/north-korean-remote-it-staffer-worked-for-us-government-agency-says-fbi/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T13:40:30+00:00",
    "summary": "The investigation shows that North Koreans are able to infiltrate government agencies, as well as private organizations and crypto exchanges."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-earnings-more-on-amazons-earnings/",
    "domain": "大厂 AI 动态",
    "title": "Apple Earnings, More on Amazon’s Earnings",
    "url": "https://stratechery.com/2026/apple-earnings-more-on-amazons-earnings/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T10:00:00+00:00",
    "summary": "Apple's earnings (and stock) are limited not by memory but rather chip shortages; then, more on Amazon's earnings and Andy Jassy's market analysis."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/08/def-con-crowd-suspected-in-fake-hotspot-attack-on-delta-flight/",
    "domain": "大厂 AI 动态",
    "title": "DEF CON crowd suspected in fake-hotspot attack on Delta flight",
    "url": "https://arstechnica.com/information-technology/2026/08/def-con-crowd-suspected-in-fake-hotspot-attack-on-delta-flight/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T00:08:40+00:00",
    "summary": "FBI Atlanta confirms it's looking into the incident, no arrests made."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/trump-wants-big-pharma-to-split-mmr-vaccine-big-pharma-thinks-its-idiotic/",
    "domain": "大厂 AI 动态",
    "title": "Trump wants Big Pharma to split MMR vaccine; Big Pharma thinks it's idiotic",
    "url": "https://arstechnica.com/health/2026/08/trump-wants-big-pharma-to-split-mmr-vaccine-big-pharma-thinks-its-idiotic/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T22:31:45+00:00",
    "summary": "It took just hours for the leading pharma group to reject the recommendations."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/romania-destroys-russian-drones-drifting-near-vital-european-offshore-gas-site/",
    "domain": "大厂 AI 动态",
    "title": "Russian drones found near vital European offshore gas site, get blown up",
    "url": "https://arstechnica.com/gadgets/2026/08/romania-destroys-russian-drones-drifting-near-vital-european-offshore-gas-site/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T21:20:11+00:00",
    "summary": "This follows many drone incursions into Romania and a failed attack in Germany."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/chrome-adopts-what-may-be-the-best-protection-yet-against-account-takeovers/",
    "domain": "大厂 AI 动态",
    "title": "Chrome adopts what may be the best protection yet against account takeovers",
    "url": "https://arstechnica.com/security/2026/08/chrome-adopts-what-may-be-the-best-protection-yet-against-account-takeovers/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T20:59:52+00:00",
    "summary": "Device-bound session credentials thwart an increasingly common form of account takeover."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/meta-cant-stop-states-1-4-trillion-lawsuit-from-going-to-trial/",
    "domain": "大厂 AI 动态",
    "title": "Meta can't stop states' $1.4 trillion lawsuit from going to trial",
    "url": "https://arstechnica.com/tech-policy/2026/08/meta-cant-stop-states-1-4-trillion-lawsuit-from-going-to-trial/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T20:27:16+00:00",
    "summary": "Judges tell Meta that Section 230 provides a defense, not immunity from lawsuits."
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
    "id": "hn:49122994",
    "domain": "股票",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-31T13:37:36+00:00",
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
    "points": 115,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49261857",
    "domain": "股票",
    "title": "The SpaceX Sham",
    "url": "https://dissentmagazine.org/online_articles/spacex-ipo-elon-musk-trillionaire/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-08-11T17:47:03+00:00",
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
    "id": "wscn:3779247",
    "domain": "股票",
    "title": "科创50大涨超2%，芯片算力引爆科技反攻，寒武纪、长鑫集体大涨，港股科网股普遍下挫、腾讯音乐大跌超13%",
    "url": "https://wallstreetcn.com/articles/3779247",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:03:55+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3600股飘红，上午半天成交1.39万亿。沪深两市半日成交额1.38万亿，较上个交易日缩量1375亿。板块方面，半导体、算力硬件产业链反弹，CPO、光刻机、PCB方向领涨；光伏、工业金属、脑机接口、锂电池题材活跃。煤炭、电力、银行、油气板块走弱。"
  },
  {
    "id": "wscn:3779252",
    "domain": "股票",
    "title": "预测市场独角兽Kalshi寻求400亿美元估值，世界杯豪赌推动营收翻倍",
    "url": "https://wallstreetcn.com/articles/3779252",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:01:16+00:00",
    "summary": "预测市场平台Kalshi年化营收在7月突破40亿美元，较两个月前翻倍，世界杯赛事押注是主要推手。公司随即启动新一轮融资谈判，目标估值400亿美元，较5月融资轮估值翻近一倍，若成功将超越Coinbase市值。与此同时，Kalshi 6月单月运营支出高达3亿美元。"
  },
  {
    "id": "wscn:3779253",
    "domain": "股票",
    "title": "招行零售AUM站上18万亿，AI智能体从助手走向生态",
    "url": "https://wallstreetcn.com/articles/3779253",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T03:50:03+00:00",
    "summary": "8月11日，招商银行在广州举办的“2026财富合作伙伴论坛”上宣布，其零售AUM（管理客户总资产）余..."
  },
  {
    "id": "wscn:3778947",
    "domain": "股票",
    "title": "钠离子电池价值拆解：Q3产业化拐点将至，供应链谁先赚钱？",
    "url": "https://wallstreetcn.com/premium/articles/3778947?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T03:33:20+00:00",
    "summary": "2026年，全球钠电实际需求预计达到18GWh，同比增长323%，全球钠电市场规模从2025年的20亿元爆发式增长。"
  },
  {
    "id": "wscn:3779251",
    "domain": "股票",
    "title": "买不起芯片怎么办？英伟达联手华尔街，把AI算力变成可融资、可打包的资产",
    "url": "https://wallstreetcn.com/articles/3779251",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T03:29:39+00:00",
    "summary": "英伟达联手Apollo、贝莱德、黑石等华尔街巨头，拟构建5000亿美元AI芯片证券化融资体系，通过SPV将GPU打包成类抵押贷款的新资产类别，为融资受困的中小AI企业开辟资本通道。但\"生菜般短暂\"的芯片保质期、英伟达自身兜底引发的循环融资争议，以及迄今零实际募资的现实，令这场被比作70年代MBS革命的金融创新，仍悬于理想与风险的刀刃之上。"
  },
  {
    "id": "wscn:3779248",
    "domain": "股票",
    "title": "强劲增长、温和加息、油价可控——德银称市场在定价一个不存在的完美",
    "url": "https://wallstreetcn.com/articles/3779248",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T03:25:46+00:00",
    "summary": "全球市场正同时押注强劲增长、温和加息、油价回落与地缘风险可控——德银警告，这一\"金发姑娘\"式组合几乎没有容错空间。标普创历史新高、信用利差处低位，但PCE通胀仍达3.7%，利率期货仅定价47个基点加息。历史经验显示，相似通胀水平下美联储首年紧缩往往超百个基点。霍尔木兹海峡仍未恢复通行，布伦特年内累计涨逾40%，任何单一假设落空，都可能引发市场重估的连锁反应。"
  },
  {
    "id": "wscn:3779245",
    "domain": "股票",
    "title": "美银：今夜CPI“下行意外”影响更大，若核心CPI意外走低或将排除9月加息",
    "url": "https://wallstreetcn.com/articles/3779245",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T03:20:52+00:00",
    "summary": "美银在CPI前瞻报告中指出，市场对通胀“下行意外”的反应将显著大于“上行意外”。若核心CPI环比录得0.1%低于预期，9月加息将基本出局，并对美债利率和美元形成双重压力；而0.3%的超预期虽将9月加息重新纳入视野，但因沃什态度存疑及8月数据尚待验证，并不能锁定结果。"
  },
  {
    "id": "wscn:3779250",
    "domain": "股票",
    "title": "马斯克：AI收入下月将超越SpaceX全部其他业务，五年后AI占SpaceX价值99%",
    "url": "https://wallstreetcn.com/articles/3779250",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T02:53:25+00:00",
    "summary": "马斯克在SpaceX全员会上宣布，AI收入“肯定”将在9月首次超越SpaceX所有其他业务收入，并定下明年底AI算力达10吉瓦的目标，对应潜在年收入3000亿至5000亿美元。他高喊，“我们必须取得AI的胜利，未来将是关于AI和机器人的世界。”这也是他对SpaceX AI业务最为明确的时间表和规模预测。"
  },
  {
    "id": "wscn:3779249",
    "domain": "股票",
    "title": "能记住30万人日常的AI宠物“芙崽”，是怎么被养大的",
    "url": "https://wallstreetcn.com/articles/3779249",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T02:31:15+00:00",
    "summary": "成年人的树洞，长得像玩偶"
  },
  {
    "id": "wscn:3779246",
    "domain": "股票",
    "title": "从奢侈品到廉价符号，钻石市场正加速崩溃",
    "url": "https://wallstreetcn.com/articles/3779246",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T02:31:09+00:00",
    "summary": "彭博钻石标准指数跌至历史新低，天然钻石价格四年内累计下跌约50%。尽管产量削减20%，仍难阻颓势。随着婴儿潮一代遗产涌入二手市场，供给压力将持续加剧。分析人士警告，钻石将重蹈百年前天然珍珠崩溃的覆辙，从财富象征沦为\"俗气\"符号。对整个产业链而言，这场冲击或将引发系统性瓦解。"
  },
  {
    "id": "wscn:3779244",
    "domain": "股票",
    "title": "追平OpenAI！Gemini月活用户突破10亿，为谷歌史上增速最快产品",
    "url": "https://wallstreetcn.com/articles/3779244",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T02:15:51+00:00",
    "summary": "Gemini月活突破10亿，与ChatGPT正面交锋。谷歌CEO皮查伊宣布这是有史以来增速最快的产品——从7.5亿到10亿仅用半年。其中，Gemini绝大多数用户来自Android生态，63%用户选择语音交互，\"纯语音\"用户占比持续上升。随着十亿用户争夺战落幕，深度变现才是真正的战场。"
  },
  {
    "id": "wscn:3779241",
    "domain": "股票",
    "title": "AI带来美国“就业末日”？美银：目前没有证据，但年轻人、信息业与金融业已现压力",
    "url": "https://wallstreetcn.com/articles/3779241",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T02:13:35+00:00",
    "summary": "AI尚未打穿美国就业市场，但裂缝已现。美银最新研究揭示，AI冲击呈现结构性分化而非总量崩塌——高暴露行业招聘停滞，22至27岁年轻毕业生失业率反弹，入门岗位率先承压；而AI驱动的数据中心建设浪潮，正在建筑与制造业反向创造12.7万个岗位，撑起今年私营部门新增就业的四分之一。风险已从\"总量崩塌\"悄然转向\"结构性挤压\"。"
  },
  {
    "id": "wscn:3779239",
    "domain": "股票",
    "title": "英伟达开源战略升级：从\"支持者\"到\"构建者\"，计划亲自打造全球顶尖开源AI模型",
    "url": "https://wallstreetcn.com/articles/3779239",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T01:58:58+00:00",
    "summary": "英伟达斥数十亿美元训练万亿参数开放大模型Nemotron 4，表面\"不务正业\"，实则暗藏商业逻辑：模型免费，算力收费。通过免费模型吸引企业、政府和开发者部署AI，推动GPU、网络、软件全栈消费。此举还有助于分散客户集中风险，对抗大客户自研芯片威胁。同时，亲自训练前沿模型可提前发现硬件瓶颈，反哺下一代芯片设计。"
  },
  {
    "id": "wscn:3779242",
    "domain": "股票",
    "title": "百年历史规律显示美股迎来“有利窗口”，分析师看好未来18个月走势",
    "url": "https://wallstreetcn.com/articles/3779242",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T01:48:02+00:00",
    "summary": "SentimenTrader策略师Jay Kaeppel基于历史数据发现，美股存在七年周期规律，其中“有利”的18个月阶段历史上涨概率高达90%、平均涨幅26.8%。下一个“有利期”将于2025年10月30日启动。但值得关注的是，当前“不利期”内标普500已涨逾26%。"
  },
  {
    "id": "wscn:3779240",
    "domain": "股票",
    "title": "马斯克押注AI代理赛道，SpaceX AI推出Grok Bot，对标Anthropic与OpenAI",
    "url": "https://wallstreetcn.com/articles/3779240",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T01:20:31+00:00",
    "summary": "SpaceXAI正式推出AI代理产品Grok Bot，由SpaceXAI与Cursor联合开发，目前处于早期测试阶段。Grok Bot类似于一个数字员工，核心定位是“永远在线的AI队友”。它拥有独立的云端计算机，可以登录用户已经在用的工具，跨应用、收件箱等场景工作，任务完成后才返回汇报。"
  },
  {
    "id": "wscn:3779238",
    "domain": "股票",
    "title": "8月涨太快！黄金强势反弹后，今晚CPI会引发获利了结吗？",
    "url": "https://wallstreetcn.com/articles/3779238",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T01:06:10+00:00",
    "summary": "黄金8月累涨约8%，上周单周涨幅高达7.1%，但狂欢过后隐忧渐现——金价时隔103个交易日首度触发超买信号，历史数据显示此后回报普遍为负。汇丰警告4500美元构成强阻力，今晚美国7月CPI数据将成关键压力测试：若数据不够\"温和\"，高达27亿盎司的多头仓位或集体踩踏，引发一轮加速回调。"
  },
  {
    "id": "wscn:3779064",
    "domain": "股票",
    "title": "AI制药初探：200+药物分子进入临床试验，产业链上游开启三位数业绩大爆发",
    "url": "https://wallstreetcn.com/premium/articles/3779064?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T01:05:39+00:00",
    "summary": "全球AI制药市场规模预计将从2025年的约28亿美元增长至2035年的160-240亿美元（CAGR 23-27%），亚太地区正以27%以上的增速成为增长主引擎。"
  },
  {
    "id": "wscn:3779236",
    "domain": "股票",
    "title": "黄仁勋5000亿融资“撕裂市场”：资管巨头狂欢，科技股两日连跌",
    "url": "https://wallstreetcn.com/articles/3779236",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T00:45:46+00:00",
    "summary": "市场将这一融资安排解读为对私募信贷和另类投资的直接利好——庞大的资金管道意味着管理费收入的长期增长前景，KKR、阿波罗等另类资管巨头股价大涨3%至7%，但大型科技股连续承压。这一分化折射出深层隐忧：英伟达亲自为客户找融资，究竟是需求强劲还是需求需靠融资\"创造\"？"
  },
  {
    "id": "wscn:3779234",
    "domain": "股票",
    "title": "从闪迪到长鑫，内存长协扩散至二三线厂商",
    "url": "https://wallstreetcn.com/articles/3779234",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T00:32:03+00:00",
    "summary": "全球存储芯片供需失衡加剧，长期供应协议（LTA）已从三星、SK海力士、美光扩散至闪迪和长鑫存储。苹果试图压低长鑫存储采购价遭拒，因华为、小米已锁定其产能。高盛将此视为本轮LTA与历轮最显著的区别，供应商定价权正深度重塑整条产业链议价逻辑。"
  },
  {
    "id": "wscn:3779235",
    "domain": "股票",
    "title": "黄仁勋的5000亿美元：如果收益既有算力租金还有AI Venture分成？",
    "url": "https://wallstreetcn.com/articles/3779235",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T00:20:14+00:00",
    "summary": "英伟达CEO黄仁勋发公开信回应\"循环融资\"质疑，祭出两张王牌：六年前的A100 GPU经济寿命延长至十年，2026年仍可产生逾万美元/年租赁收入；更关键的是，他将AI Factory的投资回报定义从\"GPU租金\"升维至\"AI所创造的经济价值\"。华尔街据此可设计出\"固定IRR+算力超额分成+AI风险权益\"三层收益结构，让基础设施资本直接分享AI应用的超额红利。"
  },
  {
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-08-03T06:17:53+00:00",
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
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
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
    "id": "hn:49177126",
    "domain": "股票",
    "title": "It looks like 'Big Short' investor Michael Burry nailed bet against chip stocks",
    "url": "https://www.businessinsider.com/big-short-michael-burry-ai-chip-stocks-soxx-nvidia-substack-2026-8",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T00:30:23+00:00",
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
    "id": "hn:49115139",
    "domain": "股票",
    "title": "Microsoft's $450B Jump Is Biggest in Stock Market History",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/microsoft-eyes-history-with-490-billion-pop-in-market-value",
    "source": "signatoremo",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-30T20:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48923343",
    "domain": "股票",
    "title": "SpaceX stock sinks below $135 IPO price for the first time",
    "url": "https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html",
    "source": "abduhl",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-15T16:30:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114131",
    "domain": "股票",
    "title": "Citadel buys most of Situational's stock holdings after AI share rout",
    "url": "https://www.reuters.com/technology/citadel-buys-most-situationals-stock-holdings-after-ai-share-rout-sources-say-2026-07-30/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-30T18:54:46+00:00",
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
    "id": "hn:49095568",
    "domain": "股票",
    "title": "Korean Stocks Plunge 16% in Two-Day Burst of Retail Selling",
    "url": "https://www.bloomberg.com/news/articles/2026-07-29/korean-stocks-tumble-a-second-day-as-sk-hynix-results-disappoint",
    "source": "emsidisii",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-29T10:25:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49119293",
    "domain": "股票",
    "title": "Aschenbrenner's hedge fund forced to unwind all public stock positions",
    "url": "https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html",
    "source": "akbabu",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-31T05:22:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49113358",
    "domain": "股票",
    "title": "South Korea's stock market plunges as AI-driven boom fades",
    "url": "https://www.aljazeera.com/economy/2026/7/29/south-koreas-stock-market-plunges-as-ai-driven-boom-fades",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-30T17:54:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48899454",
    "domain": "股票",
    "title": "$65K to work at Anthropic? Debate ensues amid IPO wave",
    "url": "https://missionlocal.org/2026/07/anthropic-sf-affordability-ipo-housing-evictions-rent/",
    "source": "gcheong",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-13T21:56:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48889982",
    "domain": "股票",
    "title": "Xbox CEO Asha Sharma, who laid off 3,200 employees, to lead task force on jobs",
    "url": "https://www.pcgamer.com/gaming-industry/us-federal-reserve-taps-xbox-ceo-asha-sharma-who-just-laid-off-3-200-employees-to-lead-task-force-on-jobs/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-13T09:27:08+00:00",
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
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 494,
    "published_at": "2026-07-15T03:32:45+00:00",
    "summary": ""
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
    "id": "hn:49245487",
    "domain": "金融",
    "title": "Study links GLP-1 drugs to bigger jump in women's employment than a degree",
    "url": "https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html",
    "source": "metadat",
    "platform": "hackernews",
    "points": 130,
    "published_at": "2026-08-10T16:02:34+00:00",
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
    "id": "hn:49259043",
    "domain": "金融",
    "title": "Federal vendor with $50M in contracts leaves portal broken for a month",
    "url": "https://www.propublica.org/article/foia-requests-responses",
    "source": "ams1",
    "platform": "hackernews",
    "points": 98,
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
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-08-10T13:40:46+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10321",
    "domain": "金融",
    "title": "Multi-Credit Calibration via Elastically Stopped L\\'{e}vy Processes",
    "url": "https://arxiv.org/abs/2608.10321",
    "source": "Graeme Baker, Agostino Capponi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10321v1 Announce Type: new Abstract: We calibrate credit default swaps and index tranches with elastically stopped L\\'evy processes: each firm defaults when the running supremum of a latent"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10410",
    "domain": "金融",
    "title": "Objective-oriented quantitative investment: A specification-driven framework for automated synthesis of trading strategy pipelines",
    "url": "https://arxiv.org/abs/2608.10410",
    "source": "Liangliang Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10410v1 Announce Type: new Abstract: Automated quantitative research has made striking progress, yet each system answers the same question: which strategy scores highest on a scalar metric?"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10596",
    "domain": "金融",
    "title": "A Note on the Identification Step in \"A Semistructural Methodology for Policy Counterfactuals\"",
    "url": "https://arxiv.org/abs/2608.10596",
    "source": "Henri Ker\\\"anen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10596v1 Announce Type: new Abstract: The New Keynesian example of Beraja (2023) is not identified at its printed calibration: more than one structure satisfies every condition of its identi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10693",
    "domain": "金融",
    "title": "When the Fed Speaks: Dynamics and Forecasts of the Volatility Surface",
    "url": "https://arxiv.org/abs/2608.10693",
    "source": "Lukasz Adamski, Robert Slepaczuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10693v1 Announce Type: new Abstract: Our primary goal is to forecast and empirically examine the evolution of the implied volatility (IV) surface, with particular focus on the dates of sche"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10711",
    "domain": "金融",
    "title": "Optimal Pricing and Hedging of SOFR Derivatives",
    "url": "https://arxiv.org/abs/2608.10711",
    "source": "Teemu Pennanen, Waleed Taoum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10711v1 Announce Type: new Abstract: Thousands of SOFR derivatives are available in exchanges and OTC, but the market remains illiquid and incomplete. Such a market is beyond the scope of c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11134",
    "domain": "金融",
    "title": "Mastering Stochastic OLG Models in Continuous Time",
    "url": "https://arxiv.org/abs/2608.11134",
    "source": "Yves Achdou, Johannes Brumm, Lukas Frank",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.11134v1 Announce Type: new Abstract: We propose a comprehensive framework for solving overlapping-generations (OLG) models in continuous time with both idiosyncratic and aggregate risk. Our"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10175",
    "domain": "金融",
    "title": "Beyond Cash Flows: A Multi-Agent AI Framework for Valuing Clinical-Stage, Cross-Border Biotechnology",
    "url": "https://arxiv.org/abs/2608.10175",
    "source": "Yuhan Fang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10175v1 Announce Type: cross Abstract: A new class of software systems is transforming investment analysis. Large language model agents assembled into collaborative team structures includin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10197",
    "domain": "金融",
    "title": "An Optimal Energy Production Problem with Energy Source Switching and Load Following Nuclear Power Plants",
    "url": "https://arxiv.org/abs/2608.10197",
    "source": "Fabio Baschetti, Alessandro Gnoatto, Athena Picarelli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10197v1 Announce Type: cross Abstract: The integration of weather-dependent renewable generation increases the volatility of residual demand and raises the value of dispatchable low-carbon "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10788",
    "domain": "金融",
    "title": "The Triadic Stress Index in Financial Markets",
    "url": "https://arxiv.org/abs/2608.10788",
    "source": "Alberto Acedo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10788v1 Announce Type: cross Abstract: The Triadic Stress Index (TSI) takes a network index whose four factors were first observed in soil microbiome co-occurrence networks and applies it, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.10852",
    "domain": "金融",
    "title": "Universality and Heterogeneity of Stylized Facts in Cryptocurrency and Equity Markets",
    "url": "https://arxiv.org/abs/2608.10852",
    "source": "Jaesung Kim, Changhee Cho, Jae Woo Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.10852v1 Announce Type: cross Abstract: This study investigates whether the macroscopic statistical maturity of cryptocurrencies implies dynamical equivalence with traditional equity markets"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31102",
    "domain": "金融",
    "title": "Translation Readiness Index: Measuring the Semantic Proximity of Research to Patented Science",
    "url": "https://arxiv.org/abs/2606.31102",
    "source": "Paul X. McCarthy, Rasika Amarasiri, Xian Gong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2606.31102v2 Announce Type: replace Abstract: Universities, funders, and investors often need to spot research with translational potential early, long before downstream outcomes like licenses, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.09069",
    "domain": "金融",
    "title": "Telemetry and Concealment in Self-Adapting Generative AI: Logging Architecture, Adversarial Model Hiding, and the Limits of Detection",
    "url": "https://arxiv.org/abs/2608.09069",
    "source": "Sriram Nagaraj",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T04:00:00+00:00",
    "summary": "arXiv:2608.09069v2 Announce Type: replace-cross Abstract: Model risk management (MRM) guidance assumes a static model lifecycle, in which models are developed, independently validated, and implemented"
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
    "id": "hn:49189030",
    "domain": "金融",
    "title": "A Fed official is asking whether AI is becoming 'too big to fail'",
    "url": "https://thenextweb.com/news/a-fed-official-is-asking-whether-ai-is-becoming-too-big-to-fail",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-05T21:08:25+00:00",
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
    "id": "hn:49190429",
    "domain": "金融",
    "title": "Data shows just how hard Tesla's Cybertruck has flopped",
    "url": "https://www.msn.com/en-us/autos/general/this-data-shows-just-how-hard-tesla-s-cybertruck-has-actually-flopped/ar-AA29sikQ",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T23:25:10+00:00",
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
    "id": "hn:49024958",
    "domain": "金融",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114620",
    "domain": "金融",
    "title": "'Talk Is Cheap': Wall Street Delivers Harsh Verdict on Warsh Fed",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/-talk-is-cheap-wall-street-delivers-harsh-verdict-on-warsh-fed",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-30T19:33:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49100970",
    "domain": "金融",
    "title": "Trump administration Is Repurposing Federal Land for A.I. Data Centers",
    "url": "https://www.nytimes.com/2026/07/29/climate/trump-federal-data-centers.html",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T18:09:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-18T00:28:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:48999329",
    "domain": "金融",
    "title": "A Man Who Runs the IRS Spied on Colleagues When He Worked at JPMorgan",
    "url": "https://www.wsj.com/finance/banking/irs-bisignano-spying-jpmorgan-6cd1ddf0",
    "source": "cwwc",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-07-21T22:40:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:48986112",
    "domain": "金融",
    "title": "The Fedora project grapples with change",
    "url": "https://lwn.net/SubscriberLink/1081557/cde56e450fe4bf10/",
    "source": "chmaynard",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-20T23:17:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48999988",
    "domain": "金融",
    "title": "Brazil and US clash over future of payments as Pix system stirs global interest",
    "url": "https://www.reuters.com/business/finance/brazil-us-clash-over-future-payments-popular-pix-system-stirs-global-interest-2026-07-21/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-21T23:52:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48986211",
    "domain": "金融",
    "title": "Delayed Boeing jets only fit for baked bean tins, Emirates boss says",
    "url": "https://finance.yahoo.com/technology/articles/delayed-boeing-jets-only-fit-162341761.html",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-20T23:29:15+00:00",
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
  }
]
```
