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

- 今日日期：`2026-08-16`
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
  "date": "2026-08-16",
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
    "points": 4245681,
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
    "points": 1714168,
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
    "points": 1666065,
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
    "points": 1329968,
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
    "points": 1273237,
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
    "points": 1127448,
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
    "points": 1059187,
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
    "points": 671075,
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
    "points": 620241,
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
    "points": 584113,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 574106,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 571569,
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
    "points": 506359,
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
    "points": 437367,
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
    "points": 420494,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 397407,
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
    "points": 385095,
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
    "points": 351995,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1j8TQ6FEf8",
    "domain": "AI",
    "title": "纯手搓一部AI漫剧一个月收获3.1w！附教程！全流程操作演示！让零基础也能学会AI漫剧制作技巧！更多AI漫剧工具提示词+变现方法及全套教程都整啦！拿走不谢~",
    "url": "http://www.bilibili.com/video/av116872418756172",
    "source": "小柚子讲AI漫剧",
    "platform": "bilibili",
    "points": 320952,
    "published_at": "2026-07-06T09:55:54+00:00",
    "summary": "本套教程从零开始讲解，手把手教学，无论是新手小白，还是有一定经验的选手，皆可学习~\n配套工具软件 | 素材 | AIGC SeeDance2.0 即梦AI 学习路线\n分享给各位还在寻找资料宝子们！一键三联抱走吖\n视频制作不易，同学们觉得对你有帮助的话记得点点关注，一键三连【666】感谢支持！！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸voov",
    "platform": "bilibili",
    "points": 307541,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 238147,
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
    "points": 237802,
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
    "points": 179233,
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
    "points": 164580,
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
    "points": 163745,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 157591,
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
    "points": 154631,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 132267,
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
    "points": 114248,
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
    "points": 93197,
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
    "points": 82614,
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
    "points": 74031,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 71512,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63515,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 58028,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54082,
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
    "points": 47617,
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
    "points": 46261,
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
    "points": 46179,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "AI 赛博女友一键安装包下载：https://www.freedidi.com/24984.html"
  },
  {
    "id": "bvid:BV1W7gP6CEEV",
    "domain": "AI",
    "title": "🚀实测DeepSeek Harness从基础到高级用法！WebUI远程控制、多模型接入、执行轨迹、插件系统、任务分支、代码分析！比Claude Code更强？",
    "url": "http://www.bilibili.com/video/av117093206923174",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 44765,
    "published_at": "2026-08-14T09:46:31+00:00",
    "summary": "视频简介：\n\nDeepSeek突然开源Harness！一切皆插件+Web UI+多模型，我实测后发现它真可能挑战Claude Code和Codex\n\nDeepSeek 在 V4 Pro 之后紧接着开源了 DeepSeek Harness，它最核心的理念就是“一切皆插件”。\n\n这期视频从零开始安装并完整实测 DeepSeek Harness，包括 Web UI、远程访问、多模型接入、插件系统、不同 "
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 44067,
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
    "points": 40593,
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
    "points": 38782,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 35251,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34126,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 33192,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1sRRYY2EBo",
    "domain": "AI",
    "title": "利用AI编程工具Trae或Cursor免费生成CAD图纸",
    "url": "http://www.bilibili.com/video/av114132447665738",
    "source": "vjmap",
    "platform": "bilibili",
    "points": 32380,
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
    "points": 29615,
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
    "points": 28875,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1RtEb6HEVa",
    "domain": "AI",
    "title": "[YSM服务器] 定制多|社交和谐|伪创造|女仆|养老|种田|枪魔法|日活60流畅|方块小镇|路地裹 暑假服务器招新啦",
    "url": "http://www.bilibili.com/video/av116708304033318",
    "source": "兔加索",
    "platform": "bilibili",
    "points": 28441,
    "published_at": "2026-06-07T10:18:21+00:00",
    "summary": "我的世界YSM服务器，很多定制mod，聊天界面/csol躲猫猫/你画我猜/tab/二次元游戏菜单/定制网易云界面/线上商店/公共地标等等，游戏免费飞行,免费mod建材，不限制跑图，地图无限大硬盘容量大不删档，轻度生电，地形无错乱，tps稳定流畅] 1064988136下载游玩哦,腐竹耐心友善\n\n内容粗略介绍:↓\n建筑类:小方块|方块小镇|路地裹|cocricot|miniaturia|mca更多楼"
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
    "id": "hn:49306491",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://www.ft.com/content/6f66a76d-0b2d-4301-886c-87ecc046731b",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-15T01:02:55+00:00",
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
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-this-rtx-5070-gaming-pc-for-just-usd1-499-saving-usd600-off-list-price-acer-nitro-85-prebuilt-comes-with-16gb-of-ram-core-ultra-7-265f-and-a-1tb-pcie-4-0-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this RTX 5070 gaming PC for just $1,499, saving $600 off list price — Acer Nitro 85 prebuilt comes with 16GB of RAM, Core Ultra 7 265F, and a 1TB PCIe 4.0 SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-this-rtx-5070-gaming-pc-for-just-usd1-499-saving-usd600-off-list-price-acer-nitro-85-prebuilt-comes-with-16gb-of-ram-core-ultra-7-265f-and-a-1tb-pcie-4-0-ssd",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T20:53:34+00:00",
    "summary": "The Acer Nitro 85 gaming desktop is currently on sale for $1,499, which is $600 off its regular price for a PC that would otherwise cost you $2,000 to spec out yourself."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/peer-reviewed-study-of-443000-backblaze-drivers-ranks-hgst-most-reliable-and-toshiba-least",
    "domain": "AI 算力 / 半导体",
    "title": "Peer-reviewed study of 443,000 Backblaze hard drives ranks HGST most reliable and Toshiba the least — Analysis of 1.66 million drive-years finds Seagate and Toshiba HDDs fail at roughly twice the rate",
    "url": "https://www.tomshardware.com/pc-components/hdds/peer-reviewed-study-of-443000-backblaze-drivers-ranks-hgst-most-reliable-and-toshiba-least",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T15:30:10+00:00",
    "summary": "Backblaze's quarterly reports compare whichever drives are available at the time."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/futuristic-mosquito-zapping-laser-now-available-to-buy-video-shows-device-in-action-tiny-device-shoots-down-bugs-like-a-personal-air-defense-system-but-costs-usd1-000",
    "domain": "AI 算力 / 半导体",
    "title": "Futuristic mosquito-zapping laser now available to buy, video shows device in action — tiny device shoots down bugs like a personal air defense system, but costs $1,000",
    "url": "https://www.tomshardware.com/peripherals/futuristic-mosquito-zapping-laser-now-available-to-buy-video-shows-device-in-action-tiny-device-shoots-down-bugs-like-a-personal-air-defense-system-but-costs-usd1-000",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T15:04:47+00:00",
    "summary": "This anti-mosquito air defense laser system has successfully passed the crowdfunding stage and is now readily available on the market. It costs around $1,000, but it will be money well spent if it can"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-this-nvidia-rtx-5070-ti-gaming-pc-for-usd2-099-before-it-sells-out-prebuilt-powerhouse-includes-a-core-ultra-7-265kf-32gb-ram-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this Nvidia RTX 5070 Ti gaming PC for $2,099 before it sells out —prebuilt powerhouse includes a Core Ultra 7 265KF, 32GB RAM, 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-this-nvidia-rtx-5070-ti-gaming-pc-for-usd2-099-before-it-sells-out-prebuilt-powerhouse-includes-a-core-ultra-7-265kf-32gb-ram-1tb-ssd",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:23:36+00:00",
    "summary": "The Acer Predator Orion 6000 gaming desktop is currently on sale for $2,099, $700 off its regular price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-turns-usd5b-intel-stock-bet-into-usd30b-windfall-filing-reveals-new-usd21b-spacex-stake-and-complete-exit-from-arm-stock",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia turns $5B Intel stock bet into $30B windfall — filing reveals new $21B SpaceX stake and complete exit from Arm stock",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-turns-usd5b-intel-stock-bet-into-usd30b-windfall-filing-reveals-new-usd21b-spacex-stake-and-complete-exit-from-arm-stock",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:16:35+00:00",
    "summary": "Nvidia quietly makes strategic and financial investments in clients, partners, and suppliers: CoreWeave, Coherent, Intel, Nokia, and SpaceX."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/vlc-media-player-bug-reportedly-causes-33-second-delay-when-playing-mp3-files-on-windows-developers-say-microsoft-defender-is-to-blame",
    "domain": "AI 算力 / 半导体",
    "title": "Devs blame Windows for VLC media player bug that causes 33-second delay when playing MP3 files — creators allege Microsoft Defender blocking plugin cache is to blame",
    "url": "https://www.tomshardware.com/software/windows/vlc-media-player-bug-reportedly-causes-33-second-delay-when-playing-mp3-files-on-windows-developers-say-microsoft-defender-is-to-blame",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:30:00+00:00",
    "summary": "VLC developers say a Windows 11 issue involving Microsoft Defender can interfere with the media player's plugin cache and cause unusually long playback delays."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-vs-ryzen-7-7800x3d-faceoff",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 7700X3D vs Ryzen 7 7800X3D faceoff — seeing double with Zen 4 X3D",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-vs-ryzen-7-7800x3d-faceoff",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:25:00+00:00",
    "summary": "AMD's Ryzen 7 7700X3D takes on the old favorite across performance, pricing, and power consumption."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/white-house-authorizes-private-companies-to-hack-foreign-cybercrime-groups",
    "domain": "AI 算力 / 半导体",
    "title": "White House authorizes private companies to launch 'hack-back' cyberattacks that destroy data and systems, targeting foreign cybercrime organizations — vetted organizations can now conduct offensive c",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/white-house-authorizes-private-companies-to-hack-foreign-cybercrime-groups",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:00:00+00:00",
    "summary": "President Trump signed a memorandum on August 12 establishing the first U.S. program that lets vetted private companies conduct offensive cyber operations."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-14-2026-testing-the-bc-250-our-interview-with-intels-robert-hallock-and-a-big-week-for-optical",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: August 14, 2026 — Testing the BC-250, our interview with Intel's Robert Hallock, and a big week for optical",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-14-2026-testing-the-bc-250-our-interview-with-intels-robert-hallock-and-a-big-week-for-optical",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T12:30:00+00:00",
    "summary": "This week, we tested AMD's BC-250 in gaming workloads, published an unredacted interview with an AMD executive, and published a slew of articles surrounding a new flashpoint in the ongoing AI buildout"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/flight-ready-drones-3d-printed-and-built-on-aircraft-carrier-during-us-navy-exercise-a-containerized-factory-on-uss-essex-functioned-despite-rough-seas-and-12-foot-waves",
    "domain": "AI 算力 / 半导体",
    "title": "US Navy 3D prints combat-ready drones and 1,000+ parts aboard aircraft carrier during exercise — containerized factory fabricated 80-mph FPVs and critical spares despite rough seas and 12-foot waves",
    "url": "https://www.tomshardware.com/tech-industry/drones/flight-ready-drones-3d-printed-and-built-on-aircraft-carrier-during-us-navy-exercise-a-containerized-factory-on-uss-essex-functioned-despite-rough-seas-and-12-foot-waves",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T12:10:00+00:00",
    "summary": "During a two-week journey to Hawaii, a containerized factory aboard the USS Essex 3D-printed a dozen flight-ready drones, as well as over 1,000 parts including vital spares for Apache helicopters."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/ocypus-sigma-l36-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Ocypus Sigma L36 Pro Review: How is this LCD AIO so cheap?",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/ocypus-sigma-l36-pro-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T12:05:00+00:00",
    "summary": "The Ocypus Sigma L36 Pro is a high-performance AIO that includes a fancy 3.5-inch display and a low price tag. We’ve tested this liquid cooler paired with AMD’s Ryzen 9 9950X3D CPU to benchmark therma"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sk-hynix-is-allegedly-out-of-replacement-ssds-for-warranty-returns-chipmakers-original-price-refund-leaves-buyers-stranded-in-the-storage-shortage",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix runs out of replacement SSDs and defaults to original purchase price refunds — fine-print warranty clause shortchanges buyers as drive prices double",
    "url": "https://www.tomshardware.com/pc-components/ssds/sk-hynix-is-allegedly-out-of-replacement-ssds-for-warranty-returns-chipmakers-original-price-refund-leaves-buyers-stranded-in-the-storage-shortage",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:50:00+00:00",
    "summary": "A Redditor reports a case in which SK hynix reportedly offers a refund for a malfunctioning SSD at the original purchase price instead of a direct replacement."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-says-pc-market-is-a-tale-of-two-kingdoms-with-mainstream-taking-a-beating-vp-suggests-a-split-between-mainstream-and-enthusiast-sockets-across-the-industry",
    "domain": "AI 算力 / 半导体",
    "title": "Intel says PC market is ‘a tale of two kingdoms’ with mainstream ‘taking a beating’ — VP suggests a split between mainstream and enthusiast sockets across the industry",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-says-pc-market-is-a-tale-of-two-kingdoms-with-mainstream-taking-a-beating-vp-suggests-a-split-between-mainstream-and-enthusiast-sockets-across-the-industry",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:30:00+00:00",
    "summary": "Intel VP Robert Hallock suggests the PC industry is going to see a split between mainstream and enthusiast sockets if current market conditions don’t let up."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/nanya-engineer-used-360-degree-cam-hidden-in-snacks-in-attempt-to-steal-dram-process-tech-for-china-it-security-team-pinpointed-perp-due-to-cameras-leaky-wireless-signals",
    "domain": "AI 算力 / 半导体",
    "title": "Engineer used 360-degree cam hidden in bag of snacks in attempt to steal DRAM process tech for China — IT security team pinpointed perp due to camera's leaky wireless signals",
    "url": "https://www.tomshardware.com/pc-components/dram/nanya-engineer-used-360-degree-cam-hidden-in-snacks-in-attempt-to-steal-dram-process-tech-for-china-it-security-team-pinpointed-perp-due-to-cameras-leaky-wireless-signals",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:00:00+00:00",
    "summary": "Nanya engineer tried to steal DRAM process technology, manufacturing methods to pass them to a Chinese rival and get a higher-paid job, but gets caught and now faces time in prison."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/anti-drone-chain-gun-with-50mm-precision-guided-ammunition-unveiled-northrop-grummans-raid-hunter-is-designed-to-wipe-out-drone-swarms-and-cruise-missiles",
    "domain": "AI 算力 / 半导体",
    "title": "Anti-drone chain gun with 50mm precision-guided ammunition unveiled — Northrop Grumman's Raid Hunter is designed to wipe out drone swarms and cruise missiles",
    "url": "https://www.tomshardware.com/tech-industry/drones/anti-drone-chain-gun-with-50mm-precision-guided-ammunition-unveiled-northrop-grummans-raid-hunter-is-designed-to-wipe-out-drone-swarms-and-cruise-missiles",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T10:30:00+00:00",
    "summary": "US aerospace, defense, and security giant Northrop Grumman thinks its Raid Hunter will provide short-range, layered air defense against the increasingly complex aerial threats we are seeing in modern "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/catastrophic-optical-disc-shattering-blamed-on-cleaning-chemicals-and-packing-foam-another-data-preservation-concern-to-add-to-bit-rot-and-laser-rot",
    "domain": "AI 算力 / 半导体",
    "title": "Catastrophic optical disc shattering blamed on cleaning chemicals and packing foam — another data preservation concern to add to bit rot and laser rot",
    "url": "https://www.tomshardware.com/pc-components/storage/catastrophic-optical-disc-shattering-blamed-on-cleaning-chemicals-and-packing-foam-another-data-preservation-concern-to-add-to-bit-rot-and-laser-rot",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T09:30:00+00:00",
    "summary": "Bitrot isn't the only worry, CDs and DVDs are also susceptible to damage caused by cleaning or foam off-gassing chemicals."
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
    "id": "hn:49289112",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.7 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 961,
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
    "id": "hn:49256057",
    "domain": "大厂 AI 动态",
    "title": "What I learned by putting GitHub Copilot behind a MitM proxy",
    "url": "https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm",
    "source": "j0selit0",
    "platform": "hackernews",
    "points": 199,
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
    "id": "rss:https://www.theverge.com/gadgets/980448/polaroid-go-second-generation-film-pack-bundle-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Polaroid’s tiny instant camera is $72 and includes a free pack of film",
    "url": "https://www.theverge.com/gadgets/980448/polaroid-go-second-generation-film-pack-bundle-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T03:00:00+00:00",
    "summary": "Smartphone cameras are convenient, but they lack the charm of analog instant cameras. If you’re trying to relive the nostalgia of waiting for an instant photo to develop, Amazon is selling the second-"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/980720/matt-groening-simpsons-hit-run-d23",
    "domain": "大厂 AI 动态",
    "title": "Matt Groening lets slip that Simpsons: Hit &#038; Run might be making a comeback",
    "url": "https://www.theverge.com/entertainment/980720/matt-groening-simpsons-hit-run-d23",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T21:56:13+00:00",
    "summary": "At D23, when asked about the potential for a sequel to the cult classic The Simpsons: Hit &#38; Run game, Matt Groening replied, \"I think the original game is coming back in some form,\" before current"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/980502/roleplay-as-an-ai-chatbot",
    "domain": "大厂 AI 动态",
    "title": "Have a laugh at AI’s expense by roleplaying as a chatbot",
    "url": "https://www.theverge.com/entertainment/980502/roleplay-as-an-ai-chatbot",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T20:45:00+00:00",
    "summary": "Your AI Slop Bores Me is brilliant in its simplicity. There are two tabs: human and LARP as an AI. On one side you enter a request. On the other, you submit an answer. But the important thing is that "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/980275/elektron-model-cycles-model-samples-groovebox-electronic-music-instruments-review",
    "domain": "大厂 AI 动态",
    "title": "Don&#8217;t overlook Elektron&#8217;s budget electronic music instruments",
    "url": "https://www.theverge.com/gadgets/980275/elektron-model-cycles-model-samples-groovebox-electronic-music-instruments-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T17:00:00+00:00",
    "summary": "When I'm asked what to buy if you want to get into making electronic music, I often recommend Elektron's budget-minded Model:Samples and Model:Cycles grooveboxes. They don't grab headlines the way Tee"
  },
  {
    "id": "rss:https://www.theverge.com/report/980288/switched-on-pop-nate-sloan-charlie-harding-podcast-netflix-interview",
    "domain": "大厂 AI 动态",
    "title": "Switched on Pop’s Nate Sloan and Charlie Harding love fresh vegetables and guitar pedals",
    "url": "https://www.theverge.com/report/980288/switched-on-pop-nate-sloan-charlie-harding-podcast-netflix-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T15:00:00+00:00",
    "summary": "As if you needed more reason to love Carly Rae Jepsen's \"Call Me Maybe\" beyond its pop perfection, it is also, according to lore, the genesis for Switched on Pop, one of the best music podcasts out th"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/980666/star-wars-ahsoka-season-2-and-starfighter-get-teased-at-d23",
    "domain": "大厂 AI 动态",
    "title": "Star Wars: Ahsoka season 2 and Starfighter get teased at D23",
    "url": "https://www.theverge.com/entertainment/980666/star-wars-ahsoka-season-2-and-starfighter-get-teased-at-d23",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:58:27+00:00",
    "summary": "Season two of Star Wars: Ahsoka is still months away, but Lucasfilm still took the opportunity to tease it a bit at D23. The company dropped the first trailer for the new season ahead of its January 2"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/980633/x-men-marvel-star-wars-pixar-disney-d23",
    "domain": "大厂 AI 动态",
    "title": "Disney D23 2026: Everything announced for Star Wars, Marvel, and more",
    "url": "https://www.theverge.com/streaming/980633/x-men-marvel-star-wars-pixar-disney-d23",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:20:33+00:00",
    "summary": "The annual Disney fan event showed off the cast of Marvel&#8217;s X-Men movie, plus a new trailer for Avengers: Doomsday, and our first look at the VisionQuest TV show for Disney Plus. For Star Wars f"
  },
  {
    "id": "rss:https://www.theverge.com/tech/979850/ohsnap-snap-grip-stand-review",
    "domain": "大厂 AI 动态",
    "title": "I finally found a magnetic phone grip I never want to remove",
    "url": "https://www.theverge.com/tech/979850/ohsnap-snap-grip-stand-review",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:10:16+00:00",
    "summary": "I told myself I wouldn't buy an OhSnap accessory for my phone. Every one I'd tested was nice, but felt overpriced and slightly flawed. After I weighed in on the $40 Snap Grip 5 last year, I wound up s"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/980635/marvel-new-x-men-movie-cast",
    "domain": "大厂 AI 动态",
    "title": "Marvel reveals the new X-Men cast, including Inde Navarrette and Adam Driver",
    "url": "https://www.theverge.com/entertainment/980635/marvel-new-x-men-movie-cast",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:03:14+00:00",
    "summary": "With Spider-Man: Brand New Day behind us, and its reveal of Sadie Sink as Jean Grey, Marvel is finally ready to officially welcome the X-Men into the MCU. At the D23 event in Anaheim yesterday, the co"
  },
  {
    "id": "rss:https://www.theverge.com/tech/976390/xteink-x3-x4-x4-pro-e-reader-libby-plug-ins-drm-crosspoint-reader",
    "domain": "大厂 AI 动态",
    "title": "Xteink’s tiny e-readers are getting access to free books through Libby",
    "url": "https://www.theverge.com/tech/976390/xteink-x3-x4-x4-pro-e-reader-libby-plug-ins-drm-crosspoint-reader",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:00:00+00:00",
    "summary": "One of the big tradeoffs with Xteink's pocket-friendly e-readers is a lack of easy access to ebooks. On a Kindle or Kobo you can download tens of thousands of titles through each device's respective o"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/woman-claims-her-stepfather-used-grok-to-transform-childhood-photo-into-explicit-imagery/",
    "domain": "大厂 AI 动态",
    "title": "Woman claims her stepfather used Grok to transform childhood photo into explicit imagery",
    "url": "https://techcrunch.com/2026/08/15/woman-claims-her-stepfather-used-grok-to-transform-childhood-photo-into-explicit-imagery/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T21:29:19+00:00",
    "summary": "The woman claimed that AI tools are \"taking everyday life and turning it into child sexual abuse.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/anthropic-shares-more-details-about-how-claudes-new-watermarks-will-work/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic shares more details about how Claude’s new watermarks will work",
    "url": "https://techcrunch.com/2026/08/15/anthropic-shares-more-details-about-how-claudes-new-watermarks-will-work/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T18:58:39+00:00",
    "summary": "How will the watermarking actually work? Can it be hidden with editing? And how does this affect code?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX officially closes its Cursor acquisition",
    "url": "https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T16:30:00+00:00",
    "summary": "AI coding startup Cursor is now officially a part of SpaceX."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/how-to-tell-if-your-ai-platforms-accounts-have-been-hacked/",
    "domain": "大厂 AI 动态",
    "title": "How to tell if your AI platforms’ accounts have been hacked",
    "url": "https://techcrunch.com/2026/08/15/how-to-tell-if-your-ai-platforms-accounts-have-been-hacked/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T16:10:00+00:00",
    "summary": "A guide on how to check if hackers have broken into your accounts on the most popular AI platforms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/15/every-fusion-startup-that-has-raised-over-100m/",
    "domain": "大厂 AI 动态",
    "title": "Every fusion startup that has raised over $100M",
    "url": "https://techcrunch.com/2026/08/15/every-fusion-startup-that-has-raised-over-100m/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:15:20+00:00",
    "summary": "Fusion startups have raised $7.1 billion to date, with the majority of it going to a handful of companies."
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
    "id": "rss:https://arstechnica.com/culture/2026/08/visionquest-trailer-kicks-off-disneys-d23-fan-event/",
    "domain": "大厂 AI 动态",
    "title": "VisionQuest trailer kicks off Disney's D23 fan event",
    "url": "https://arstechnica.com/culture/2026/08/visionquest-trailer-kicks-off-disneys-d23-fan-event/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T21:21:27+00:00",
    "summary": "Also: Ahsoka S2 teaser, Doomsday trailer, news about MCU's X-Men and Star Wars: Starfighter"
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/ukraine-strikes-major-russian-rocket-factory-with-cruise-missiles/",
    "domain": "大厂 AI 动态",
    "title": "Ukraine strikes major Russian rocket factory with cruise missiles",
    "url": "https://arstechnica.com/space/2026/08/ukraine-strikes-major-russian-rocket-factory-with-cruise-missiles/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T15:46:05+00:00",
    "summary": "\"Flamingo missiles were used. A good achievement.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/so-much-solar-digging-into-the-list-of-every-us-power-plant-that-went-online-this-year/",
    "domain": "大厂 AI 动态",
    "title": "So much solar: Digging into the list of every US power plant that went online this year",
    "url": "https://arstechnica.com/science/2026/08/so-much-solar-digging-into-the-list-of-every-us-power-plant-that-went-online-this-year/",
    "source": "Dan Gearino, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:09:57+00:00",
    "summary": "Utility-scale solar leads by a mile, followed by batteries. Fossil fuels, not so much."
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
    "id": "hn:49311379",
    "domain": "股票",
    "title": "OpenAI talent exodus raises 'huge red flag' ahead of IPO",
    "url": "https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-08-15T15:25:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49305685",
    "domain": "股票",
    "title": "Backtesting Congress members stock trades by the disclosure date",
    "url": "https://investingpaths.com/tools/congress",
    "source": "ProdRatSuperior",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-14T23:08:56+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779525",
    "domain": "股票",
    "title": "五大因素叠加发酵，摩根大通：全球粮食危机或将在明年爆发",
    "url": "https://wallstreetcn.com/articles/3779525",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T03:30:39+00:00",
    "summary": "摩根大通警告，受战争、天气、仓储、水资源和浪费五个因素叠加驱动，全球粮食危机可能于2027年上半年爆发。预计全球食品通胀率将从2026年上半年的2.8%升至2027年上半年的5%。超级厄尔尼诺与能源冲击叠加，将使食品CPI额外上升约1.5个百分点，印度、印尼、巴西等新兴市场首当其冲。"
  },
  {
    "id": "wscn:3779524",
    "domain": "股票",
    "title": "常春藤名校的太空豪赌：哈佛披露22亿SpaceX仓位，为最大单一股票头寸",
    "url": "https://wallstreetcn.com/articles/3779524",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T02:48:57+00:00",
    "summary": "哈佛大学投资管理公司披露持有SpaceX股份22亿美元，成为其43亿美元美股组合中最大单一股票头寸。这笔持仓源于哈佛通过风险投资基金对SpaceX的早期布局，SpaceX今年6月上市后大幅增值。加州大学同期披露约10亿美元SpaceX持仓，多所高校捐赠基金过去十年都在深度押注私募科技资产。"
  },
  {
    "id": "wscn:3779522",
    "domain": "股票",
    "title": "伯克希尔二季度13F持仓变阵：增持谷歌、达美航空，连续两季减持美银",
    "url": "https://wallstreetcn.com/articles/3779522",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T02:12:57+00:00",
    "summary": "巴菲特卸任后，伯克希尔二季度“变阵”信号明显：重仓谷歌母公司Alphabet大幅加仓，合并市值近378亿美元，一举跃升第三大持仓；达美航空、住宅建筑商同步加码，科技与地产布局提速。与此同时，美国银行连续两季遭减持，星座品牌被彻底清仓——新掌门阿贝尔的投资风格，正悄然重塑这艘巨轮的航向。"
  },
  {
    "id": "wscn:3779068",
    "domain": "股票",
    "title": "5年扩产周期接近尾声，箱瓦纸为何在淡季涨了300元？",
    "url": "https://wallstreetcn.com/premium/articles/3779068?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T02:06:05+00:00",
    "summary": "2026年二季度以来，箱板纸与瓦楞纸在传统淡季连续提价，2月至7月累计涨幅均超过300元/吨，部分龙头二季度盈利也率先回升。问题在于，这究竟只是天气扰动与旺季预期共振下的短期反弹，还是经历数年扩产和价格战后，行业供需格局开始真正改善？如果箱瓦纸已进入新一轮修复周期，利润又会更多流向哪些企业？"
  },
  {
    "id": "wscn:3779521",
    "domain": "股票",
    "title": "海峡控制权“各说各话”：特朗普放话“拿下”霍尔木兹，伊朗称已与阿曼就通行方案达成协议",
    "url": "https://wallstreetcn.com/articles/3779521",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T02:00:46+00:00",
    "summary": "伊朗宣布已与阿曼就霍尔木兹海峡新航道达成协议，但外长明确划线：这与海峡重开是两回事，重开须视美国能否履行条件而定。就在前一天，特朗普刚扬言“很快将宣布霍尔木兹为美国领土”，伊朗随即强硬反击：相关言论“完全源于其个人幻觉”。专家评论称，美伊双方目前形成了一种“看似都在主导、实际上谁也无法独占”的局面。"
  },
  {
    "id": "wscn:3779445",
    "domain": "股票",
    "title": "下周重磅日程：中国7月经济数据，阿里、小米、天孚通信、兆易创新、长飞光纤财报，宇树科技上市在即",
    "url": "https://wallstreetcn.com/articles/3779445",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T01:55:09+00:00",
    "summary": "财报超级周来袭，阿里、百度、快手、小米集中放榜；A股兆易创新、天孚通信、长飞光纤、科大讯飞验证存储、光模块与AI应用等主线。产业面，世界机器人大会、宇树科技上市在即、人形机器人运动会三连催化，机器人链事件密度达年内峰值。宏观面，中国7月工业、社零等经济数据与美联储7月会议纪要发布。此外，美方将称对伊实施“前所未见”措施。"
  },
  {
    "id": "wscn:3779438",
    "domain": "股票",
    "title": "干预退潮、加息接棒：为什么日央行提前进入加息快车道？",
    "url": "https://wallstreetcn.com/premium/articles/3779438?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T01:44:40+00:00",
    "summary": "美日干预效果退潮，加息接棒成稳汇率关键；日央行被迫加快加息，但财政约束限制空间，9月加息及指引决定日元能否趋势修复。"
  },
  {
    "id": "wscn:3779518",
    "domain": "股票",
    "title": "AI债务狂潮背后：700亿美元表外隐性负债引发债券投资者担忧",
    "url": "https://wallstreetcn.com/articles/3779518",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T01:08:36+00:00",
    "summary": "随着英伟达宣布5000亿美元AI融资合作，债券市场对AI公司约700亿美元表外债务的担忧骤然升温。这一结构允许英伟达、博通等芯片巨头为客户债务兜底，却无需将负债计入自身账表。多家机构警告这是顺周期的金融工程，一旦行业下行将集中引爆风险。"
  },
  {
    "id": "wscn:3779519",
    "domain": "股票",
    "title": "段永平、景林都卖了，高瓴却买了",
    "url": "https://wallstreetcn.com/articles/3779519",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T01:07:06+00:00",
    "summary": "私募巨头美股持仓曝光，AI投资惊现大分歧！高瓴半仓重押生物科技，逆势加仓英伟达等AI基建；而景林、高毅及段永平却大举抛售甚至清仓。算力狂飙之后，机构正重估AI盈利底色，投资全面步入“分歧时代”。"
  },
  {
    "id": "wscn:3779410",
    "domain": "股票",
    "title": "Anthropic将以2万亿美元定价上市！？市场在赌什么？",
    "url": "https://wallstreetcn.com/premium/articles/3779410?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T00:51:41+00:00",
    "summary": "裁判只有一个：毛利率。"
  },
  {
    "id": "wscn:3779517",
    "domain": "股票",
    "title": "洪灝：中国AI行情进入第二阶段，高质量公司表现更好",
    "url": "https://wallstreetcn.com/articles/3779517",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T14:15:17+00:00",
    "summary": "许多科技股经过回调后，估值变得更合理。"
  },
  {
    "id": "wscn:3779516",
    "domain": "股票",
    "title": "林肯调整美国供应，中国市场仍是关键",
    "url": "https://wallstreetcn.com/articles/3779516",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:53:11+00:00",
    "summary": "复杂市场。"
  },
  {
    "id": "wscn:3779515",
    "domain": "股票",
    "title": "不挂路虎标的神行者8，要和理想、问界抢用户",
    "url": "https://wallstreetcn.com/articles/3779515",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T13:50:56+00:00",
    "summary": "用中国供应链去填空档。"
  },
  {
    "id": "wscn:3779502",
    "domain": "股票",
    "title": "博通暴跌20% 市场在怕什么？",
    "url": "https://wallstreetcn.com/premium/articles/3779502?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T12:35:53+00:00",
    "summary": "一家芯片公司，为什么突然背上了3700亿美元的隐形担保？"
  },
  {
    "id": "wscn:3779514",
    "domain": "股票",
    "title": "最优“AI泡沫交易”：同时做多“傲慢”与“偏见”",
    "url": "https://wallstreetcn.com/articles/3779514",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:58:24+00:00",
    "summary": "美银认为AI泡沫下最优策略是同时做多“傲慢”（AI科技）与“偏见”（被市场冷落的失意资产），并做空AI债券。尽管美银牛熊指标处于极端区间，但资金正流向黄金与大宗商品，私人客户股票仓位创新高。面对债务压力与收益率变量，规避美元与债券仍是主线。"
  },
  {
    "id": "wscn:3779513",
    "domain": "股票",
    "title": "中期选举压力是否还能触发“TACO”？",
    "url": "https://wallstreetcn.com/articles/3779513",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T11:02:59+00:00",
    "summary": "中期选举博弈格局渐明，中信证券研判认为\"民主党夺众议院、共和党守参议院\"是最大概率结果。两院分治虽将给特朗普施政增添摩擦，但弹劾定罪、司法任命受阻等极端风险仍难成真——市场寄望于\"TACO\"约束倒逼特朗普在关税与地缘问题上让步的逻辑，或已高估选情压力的实际效力。"
  },
  {
    "id": "wscn:3779512",
    "domain": "股票",
    "title": "博通一夜跌6%：AI的下一道坎，是融资成本",
    "url": "https://wallstreetcn.com/articles/3779512",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T09:31:10+00:00",
    "summary": "市场已开始认真定价一个更深层的变量：当融资成为边际算力的主要来源，AI产业链的每一分利润，都将被悄悄计入利息成本。真正考验并非系统性违约，而是融资成本上行对AI产业链利润率的持续侵蚀，博通下一份财报将见分晓。"
  },
  {
    "id": "wscn:3779510",
    "domain": "股票",
    "title": "a16z史上最大投资！All in Uber创始人，下注工业AI“从比特到原子”",
    "url": "https://wallstreetcn.com/articles/3779510",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T08:08:00+00:00",
    "summary": "Uber联合创始人Travis Kalanick带着新公司Atoms高调复出，斩获a16z合伙人Ben Horowitz执掌以来最大单笔投资。Atoms立足“从比特到原子”的底层逻辑，将软件、传感器与机器人整合为工业AI系统，重点推进食品自动化、采矿作业与自主导航三大物理世界场景，开启传统工业智能化颠覆。"
  },
  {
    "id": "wscn:3779509",
    "domain": "股票",
    "title": "520元/股！宇树科技，未上市先疯抢！场外“暗盘”兴起，谁在豪赌？",
    "url": "https://wallstreetcn.com/articles/3779509",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T07:26:28+00:00",
    "summary": "宇树科技尚未上市，场外\"暗盘\"已报价520元/股，是发行价的3.4倍。这场游走于法律边缘的新股\"黄牛\"交易，不仅暗藏违约风险，更涉嫌非法经营与账户借用违规。专家直指：这是一级市场制度性红利的私下套利，本质是高风险对赌，投资者切莫因贪念踏入法律雷区。"
  },
  {
    "id": "wscn:3779447",
    "domain": "股票",
    "title": "美农业部意外下调玉米单产：全球粮食安全进入高风险区？",
    "url": "https://wallstreetcn.com/premium/articles/3779447?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-15T06:35:18+00:00",
    "summary": "美国农业部下调玉米单产，全球粮食库存持续收紧，极端天气、黑海与中东冲突，以及贸易保护主义或放大粮价风险。"
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
