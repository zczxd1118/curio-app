# Curio · 趋势雷达 · 跨域 Top 选稿

> 一次跑完整份简报：从所有领域的合并候选池里，选出 4-5 条跨域 Top 头条 + 备选池。
> 每条头条含"已确认 / 尚属判断对照表 + 主编点评"。

---

## 角色

你是 Curio 的**总编辑**——读者把"看全网"的工作交给你，你的责任是：

1. 从今天所有领域的合并候选池里**精选 4-5 条头条**，领域以候选条目的 `domain` 字段为准
2. 每条头条按 **已确认 / 尚属判断对照表形式**写：标题 + 引子段 + 已确认/尚属判断 + 主编点评
3. 列一份"备选池"（10-15 条标题级简单解释）

**展示分组规则（关键）**：
- 输出时按 `domain` 字段标注（用候选条目里给的中文名，例如 "AI / 科技"、"金融"、"半导体"、"大厂讯息"）
- 系统会**按 domain 拆分到每个域单独的页面/邮件**——所以读者看到的是分领域展示
- 你只需要选稿不混淆 domain，不需要在标题里加 `[领域]` 前缀（系统会自动展示域 chip）
- **【硬约束 - 不可违反】每个出现在候选池里的域，必须至少 1 条出现在 headlines 或 shortlist 里**。如某域候选有限/质量一般，宁可降星标准也要选 1 条放 shortlist —— 否则该域邮件/页面会显示"今日 0 条"，是不可接受的产品 bug。

---

## 输入（变量替换）

- 今日日期：`2026-11-12`
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
  "date": "2026-11-12",
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
- **跨域均衡**：在本期候选池实际包含的领域中，头条尽量覆盖至少 3 个域；不足 3 个域时按实际领域数处理。如果某域今天没有"够 4 星"的，可以不选入头条，但仍须遵守上方备选池的领域覆盖约束。
- **新颖度优先**：选今天/本周首发的、有数字的、有未来动作的。避免"已知信息再拼装"。
- **跨平台同事件去重**：同一个事件（如某公司 IPO）在 HN + RSS 都出现，**选英文原版/最深度的源**。
- **反偏好**：保留 0-1 条用户可能不爱看但应该看的（标 `is_diverse: true`，可选）。
- **历史反馈优先**：如果用户最近一次反馈说"想多看 X"，至少 1 条头条契合。

### 备选池（10-15 条）
- 不上头条但仍值得知晓的。
- 每条 30-60 字一句话。
- 按候选条目的 `domain` 自然分组，不预设固定领域列表。

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
    "points": 2237323,
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
    "points": 2110490,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1494465,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1487976,
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
    "points": 1456496,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1PwBuBtEZo",
    "domain": "AI",
    "title": "Trae 保姆级教程｜AI 编程工具完整入门，实战项目手把手教学",
    "url": "http://www.bilibili.com/video/av115768712893172",
    "source": "韩顺平",
    "platform": "bilibili",
    "points": 1092276,
    "published_at": "2025-12-23T11:55:45+00:00",
    "summary": "如果这个视频对你有帮助，记得【一键三连】，支持一下老韩\n【视频配套工具包+学习资料，”评论区置顶” 免费领取】"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 912241,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 751176,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1tTxd6KEeL",
    "domain": "AI",
    "title": "全网最细！40分钟速通Codex！【GenJi深度教程】",
    "url": "http://www.bilibili.com/video/av117558925596398",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 605626,
    "published_at": "2026-11-05T10:00:00+00:00",
    "summary": "我们花了两个月整理出来了AI工具：Codex从入门到精通的全教程。这里面包含了安装、核心功能介绍、以及可快速上手的实战案例等等 完全免费的公益课程，如果你看完觉得有帮助，麻烦【点赞、投币、收藏】一键三连，就当作这门课的学费啦！做免费课程不容易，先谢谢大家支持！"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 596378,
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
    "points": 472974,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1kr4h6fExw",
    "domain": "AI",
    "title": "DeepSeek 新出的 Super Agent 是什么？真有用么？",
    "url": "http://www.bilibili.com/video/av117564076202051",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 443665,
    "published_at": "2026-11-05T13:35:56+00:00",
    "summary": "DeepSeek Harness 团队最新开源的 Super-agent 是什么？和传统 Agent 有什么区别？它是怎么工作的？真的能提升 AI 工作的效率么？一期视频带你掌握 Super-agent 智能体，对 AI 小白、AI 编程爱好者、前端和后端程序员、AI 应用开发求职者都有帮助\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 432740,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 358393,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 353096,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 325502,
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
    "points": 297626,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1x3Wu6FEpj",
    "domain": "AI",
    "title": "【全网首发】如何不花钱雇24小时贴身秘书？全网最全的Personal AI保姆级的教程",
    "url": "http://www.bilibili.com/video/av117591808940027",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 281188,
    "published_at": "2026-11-10T11:26:33+00:00",
    "summary": "消息回不完、自动扣费防不住、收藏夹一直吃灰，这些琐事你中了几条？这次我把生活和工作里的9件琐事，统统交给了蚂蚁新升级的个人AI助理【灵光2.0】，从下载登录、连接工具到布置长期任务，手把手带你玩一遍，看看最近爆火的Personal AI到底能帮我们管多少事。视频里的大肥鱼部署链接在评论区掉落，记得看到最后~"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 231741,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV15XDfBSE2t",
    "domain": "AI",
    "title": "ClaudeCode平替:OpenCode详细使用教程看这一个就够了（内含超详细安装文档+软件安装包）",
    "url": "http://www.bilibili.com/video/av116379604881806",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 204234,
    "published_at": "2026-04-13T09:00:00+00:00",
    "summary": "opencodeopencode使用全攻略opencode教程opencode和claudecodeopencode使用技巧opencode实战opencode coworkopencode安装opencode开发opencode使用教程opencode教程opencode安装教程opencode使用全攻略opencode和claudecodeopencode skillsopencode插件op"
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 178918,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 165658,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 161913,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 153688,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 104615,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 104498,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 77831,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74689,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 67326,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 50540,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50395,
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
    "points": 47820,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41379,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 33066,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 31698,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29947,
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
    "points": 29058,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 27645,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26694,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1uwxG6DEra",
    "domain": "AI",
    "title": "3分钟讲透：Vibe Coding如何避免💩屎山代码",
    "url": "http://www.bilibili.com/video/av117513727838880",
    "source": "鲤哥builder",
    "platform": "bilibili",
    "points": 25837,
    "published_at": "2026-10-27T16:09:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1m7N1zKEU8",
    "domain": "AI",
    "title": "🚀Cursor+Serena最佳组合告别AI编程工具短板！支持Claude Code、windsurf、Cline！让AI编程不再是简单读取代码而是智能分析",
    "url": "http://www.bilibili.com/video/av114721764152608",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 20809,
    "published_at": "2025-06-21T14:18:09+00:00",
    "summary": "🚀Cursor+Serena最佳组合告别AI编程工具短板！支持Claude Code、windsurf、Cline！让AI编程不再是简单读取代码而是智能分析依赖关系，让复杂开源项目二次开发效率提升十倍\n\n🚀🚀🚀视频简介：\n✅震撼！这款完全开源免费的AI编程助手Serena，竟然能像资深开发者一样真正理解复杂项目代码结构，从需求分析到最终实现测试一站式搞定，颠覆传统AI编程工具！\n✅本期视频详细介绍"
  },
  {
    "id": "bvid:BV13sJcz9Egm",
    "domain": "AI",
    "title": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发",
    "url": "http://www.bilibili.com/video/av114521544852773",
    "source": "大模型实战课程",
    "platform": "bilibili",
    "points": 17585,
    "published_at": "2025-05-17T05:36:05+00:00",
    "summary": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15565,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV14a4y1T7Cp",
    "domain": "AI",
    "title": "VS Code + CursorCode 插件，AI 帮你编写、调试代码",
    "url": "http://www.bilibili.com/video/av654787185",
    "source": "马隆工作室",
    "platform": "bilibili",
    "points": 14644,
    "published_at": "2023-04-11T11:48:41+00:00",
    "summary": "免费， VS Code + CursorCode 插件，AI 帮你编写、调试代码"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 13919,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1rCJdzFEQg",
    "domain": "AI",
    "title": "让AI帮你干活：WindowsMCP安装和使用！",
    "url": "http://www.bilibili.com/video/av115242814212549",
    "source": "磊哥AI实战",
    "platform": "bilibili",
    "points": 13628,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
  },
  {
    "id": "bvid:BV1tDnV6ME79",
    "domain": "AI",
    "title": "当我把claude code搬进安卓设备……",
    "url": "http://www.bilibili.com/video/av117462439826705",
    "source": "Grey-Oak",
    "platform": "bilibili",
    "points": 13145,
    "published_at": "2026-10-18T14:44:02+00:00",
    "summary": "cccodroid 是一个开源的安卓应用，把 Claude Code 装进你的安卓设备。不用 root，不刷机，也不套 Linux 虚拟环境，工具直接在安卓上原生运行。\n\n视频全程实机录屏（联想y700二代平板，骁龙 8+），没有连电脑：\n· 一句话让它改代码，先给计划，你点批准才动手\n· 终端里 pkg install rust，现场打包 APK 装上\n· docx / xlsx / pptx "
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 12914,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BoeG6HExx",
    "domain": "AI",
    "title": "三个Agent的安装教程",
    "url": "http://www.bilibili.com/video/av117270592360500",
    "source": "清清小风风",
    "platform": "bilibili",
    "points": 11164,
    "published_at": "2026-09-14T17:35:08+00:00",
    "summary": "本期视频带来我常用的三个Agent的安装教程，分别是：Codex, Reasonix,deepseek Harness，统一使用deepseek-v4.1-flash模型，国内网络能完全跑通。注意：只提供了安装教程，不提供使用方法。\n#codex安装 #Agent安装 #软件安装"
  },
  {
    "id": "bvid:BV1KHxE6wE31",
    "domain": "AI",
    "title": "程序员编程都用啥？17个AI编程工具，从夯到拉排名",
    "url": "http://www.bilibili.com/video/av117517905365497",
    "source": "程序员Web3社区",
    "platform": "bilibili",
    "points": 10279,
    "published_at": "2026-10-28T10:45:00+00:00",
    "summary": "程序员编程都用啥？17个AI编程工具，从夯到拉排名。#程序员 #编程 #AI编程 #从夯到拉 #程序员赛道 #程序员规则 #开发工具 #程序员转型 #web3 #远程工作 #程序员赛道"
  },
  {
    "id": "hn:50459703",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is preparing to oust Jensen Huang",
    "url": "https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 1047,
    "published_at": "2026-11-11T22:31:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50418016",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang's letter to staff about affair",
    "url": "https://nvidianews.nvidia.com/news/a-message-to-our-company",
    "source": "karimf",
    "platform": "hackernews",
    "points": 984,
    "published_at": "2026-11-08T22:20:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362905",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux",
    "url": "https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 617,
    "published_at": "2026-11-04T08:46:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416801",
    "domain": "AI 算力 / 半导体",
    "title": "Statement from Nvidia board of directors",
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "source": "vincentchau",
    "platform": "hackernews",
    "points": 493,
    "published_at": "2026-11-08T20:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459321",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang said to have had relationship with executive who reports to him",
    "url": "https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 368,
    "published_at": "2026-11-11T22:03:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50293047",
    "domain": "AI 算力 / 半导体",
    "title": "Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang",
    "url": "https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-10-29T17:43:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459776",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia prepares to fire CEO Jensen Huang, WSJ reports",
    "url": "https://twitter.com/watcherguru/status/2120645607866188008",
    "source": "alexmolas",
    "platform": "hackernews",
    "points": 225,
    "published_at": "2026-11-11T22:36:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50348962",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia – open-source auto-ontology",
    "url": "https://github.com/NVIDIA/auto-ontology",
    "source": "campervans",
    "platform": "hackernews",
    "points": 292,
    "published_at": "2026-11-03T07:04:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50327058",
    "domain": "AI 算力 / 半导体",
    "title": "Seoul Viosys begins production of rare-earth-free white light emitter",
    "url": "https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml",
    "source": "gmays",
    "platform": "hackernews",
    "points": 195,
    "published_at": "2026-11-01T16:23:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50387738",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Kubernetes Engine (NVKE)",
    "url": "https://github.com/dsx-ai-factory/nvke",
    "source": "gkapur",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-11-06T03:16:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459679",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang had a second affair – with an employee",
    "url": "https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html",
    "source": "justswim",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-11-11T22:29:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50427486",
    "domain": "AI 算力 / 半导体",
    "title": "Commerce Dept Inquiry into Megaspeed Halted After Nvdia Intervention",
    "url": "https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-11-09T16:10:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392256",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in 1 in 11 startup rounds over $100M last year",
    "url": "https://datahyena.com/research/a-chipmaker-was-in-one-of-every-eleven-100m-rounds/",
    "source": "ghostfoxgod",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-11-06T13:48:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363861",
    "domain": "AI 算力 / 半导体",
    "title": "RTX 5090 Street Prices Top $9k as Nvidia GPU Costs Climb",
    "url": "https://aroundprague.cz/en/news/us/rtx-5090-street-prices-top-9-000-as-nvidia-gpu-costs-climb",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 78,
    "published_at": "2026-11-04T11:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50455721",
    "domain": "AI 算力 / 半导体",
    "title": "Tech Allies Rally Behind Jensen Huang, Calling Him Vital in AI Race (Gift Link)",
    "url": "https://www.nytimes.com/2026/11/11/technology/jensen-huang-affair-nvidia-support.html",
    "source": "sjs382",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-11-11T17:05:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50452464",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Vera CPU Review: 2TB/S Memory Bandwidth, a Real x86 Rival",
    "url": "https://www.storagereview.com/review/nvidia-vera-cpu-review",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-11T12:06:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:50460325",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is reportedly preparing to fire Jensen Huang",
    "url": "https://www.theverge.com/tech/1031652/jensen-huang-rumor",
    "source": "bearseascape",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-11T23:15:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50463421",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Disappearing Singapore Sales Deepen Mystery Around Megaspeed",
    "url": "https://www.wsj.com/business/earnings/nvidias-disappearing-singapore-sales-deepen-mystery-around-megaspeed-7d483180",
    "source": "ea016",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-12T05:31:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416679",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Board to Probe Spying Case After CEO Admits Affair",
    "url": "https://www.bloomberg.com/news/articles/2026-11-08/nvidia-board-to-probe-spying-case-after-ceo-jensen-huang-admits-infidelity",
    "source": "specialp",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-11-08T20:14:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50424604",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's China Problem [pdf]",
    "url": "https://culperresearch.com/wp-content/uploads/2026/05/Culper_NVDA_5-13-2026.pdf",
    "source": "Erikun",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-11-09T12:20:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:50460672",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly preparing to fire CEO Jensen Huang, amid of second affair",
    "url": "https://www.rnz.co.nz/news/business/2553062/nvidia-reportedly-preparing-to-fire-ceo-jensen-huang-amid-of-second-affair",
    "source": "billybuckwheat",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-11-11T23:45:38+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/connecting-ai-to-the-physical-world/",
    "domain": "AI 算力 / 半导体",
    "title": "Connecting AI to the Physical World",
    "url": "https://www.eetimes.com/connecting-ai-to-the-physical-world/",
    "source": "Eric K. C. Tsang, CEO and founder, Vicinity Technologies Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T10:20:00+00:00",
    "summary": "Why specialized wireless devices and SDR software IP matter to the next wave of intelligent machines The post Connecting AI to the Physical World appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/harari-warns-tech-leaders-against-pursuing-ai-superintelligence/",
    "domain": "AI 算力 / 半导体",
    "title": "Harari Warns Tech Leaders Against Pursuing AI Superintelligence",
    "url": "https://www.eetimes.com/harari-warns-tech-leaders-against-pursuing-ai-superintelligence/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T08:30:00+00:00",
    "summary": "At Gartner IT Symposium/Xpo 2026, philosopher Yuval Noah Harari makes an appeal to delay artificial superintelligence as it threatens to erode human agency and democratic sovereignty. The post Harari "
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-tech-forum-panel-discussion-the-make-or-break-milestones-toward-level-4-autonomous-driving/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Tech Forum: Panel Discussion the Make-or-Break Milestones Toward Level 4 Autonomous Driving",
    "url": "https://www.eetimes.com/automotive-tech-forum-panel-discussion-the-make-or-break-milestones-toward-level-4-autonomous-driving/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:39:41+00:00",
    "summary": "Explore the road to Level 4 autonomy as experts tackle safety, AI, regulation, and trust—watch the Automotive Tech Forum panel. The post Automotive Tech Forum: Panel Discussion the Make-or-Break Miles"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-tech-forum-the-current-state-of-sic-in-ev-design-and-how-its-evolving/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Tech Forum: The Current State of Sic in EV Design and How It’s Evolving",
    "url": "https://www.eetimes.com/automotive-tech-forum-the-current-state-of-sic-in-ev-design-and-how-its-evolving/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:34:28+00:00",
    "summary": "Explore how 800V SiC MOSFETs boost EV range, charging, and performance—and see what next-gen designs make possible. The post Automotive Tech Forum: The Current State of Sic in EV Design and How It&#82"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-tech-forum-lidar-is-key-to-safer-adas-and-autonomous-vehicles/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Tech Forum: Lidar is Key to Safer ADAS and Autonomous Vehicles",
    "url": "https://www.eetimes.com/automotive-tech-forum-lidar-is-key-to-safer-adas-and-autonomous-vehicles/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:28:21+00:00",
    "summary": "This keynote explores how LiDAR is shaping the future of mobility by improving safety, reliability, and performance in autonomous systems. The post Automotive Tech Forum: Lidar is Key to Safer ADAS an"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-tech-forum-gan-building-blocks-in-evs-and-their-design-roadmap-in-2026-and-beyond/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Tech Forum: GaN Building Blocks in EV’s and Their Design Roadmap in 2026 and Beyond",
    "url": "https://www.eetimes.com/automotive-tech-forum-gan-building-blocks-in-evs-and-their-design-roadmap-in-2026-and-beyond/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:22:01+00:00",
    "summary": "This keynote exmines GaN reliability and present the case for GaN being not only the most efficient solution, but also a necessary step for reducing system cost The post Automotive Tech Forum: GaN Bui"
  },
  {
    "id": "rss:https://www.eetimes.com/chiplets-revolutionizing-design-velocity-with-artificial-chip-intelligence-aci/",
    "domain": "AI 算力 / 半导体",
    "title": "Chiplets: Revolutionizing Design Velocity with Artificial Chip Intelligence ACI",
    "url": "https://www.eetimes.com/chiplets-revolutionizing-design-velocity-with-artificial-chip-intelligence-aci/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:00:05+00:00",
    "summary": "This session introduces Artificial Chip Intelligence (ACI®), a paradigm-shifting technology using a physics-informed foundation model designed to transform chip development from a manual labor-intensi"
  },
  {
    "id": "rss:https://www.eetimes.com/chiplets-panel-discussion-scaling-chiplets-without-breaking-the-system-where-are-the-limits/",
    "domain": "AI 算力 / 半导体",
    "title": "Chiplets: Panel Discussion: Scaling Chiplets Without Breaking the System – Where are the Limits?",
    "url": "https://www.eetimes.com/chiplets-panel-discussion-scaling-chiplets-without-breaking-the-system-where-are-the-limits/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T22:39:24+00:00",
    "summary": "As chiplet-based designs grow in scale and complexity, the technical challenges mount up as every layer of the system introduces new constraints. The post Chiplets: Panel Discussion: Scaling Chiplets "
  },
  {
    "id": "rss:https://www.eetimes.com/chiplets-panel-discussion-how-should-we-reimagine-the-design-flow-for-chiplet-scalability/",
    "domain": "AI 算力 / 半导体",
    "title": "Chiplets: Panel Discussion: How Should We Reimagine the Design Flow for Chiplet Scalability",
    "url": "https://www.eetimes.com/chiplets-panel-discussion-how-should-we-reimagine-the-design-flow-for-chiplet-scalability/",
    "source": "AspenCore Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T22:35:01+00:00",
    "summary": "This panel discusses whether today’s design flows can scale to support reusable chiplets and multi-vendor integration, or whether more fundamental changes are needed. The post Chiplets: Panel Discussi"
  },
  {
    "id": "rss:https://www.eetimes.com/nxp-cto-lars-reger-on-physical-ai-robots-drones-and-trust/",
    "domain": "AI 算力 / 半导体",
    "title": "NXP CTO Lars Reger on Physical AI, Robots, Drones, and Trust",
    "url": "https://www.eetimes.com/nxp-cto-lars-reger-on-physical-ai-robots-drones-and-trust/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T20:23:13+00:00",
    "summary": "Explore NXP CTO Lars Reger’s view of physical AI beyond humanoids, from NavQ95 robot kits to edge trust, security, and geopolitics. The post NXP CTO Lars Reger on Physical AI, Robots, Drones, and Trus"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/techie-turns-usd2-500-cmp-170hx-8gb-mining-card-into-a-full-fat-a100-80gb-with-voltage-glitching-carefully-blowing-onboard-fuses-to-unlock-entire-vram-and-shader-modules",
    "domain": "AI 算力 / 半导体",
    "title": "Techie uses voltage glitching hack to turn $2,500 Nvidia 8GB cryptomining GPU into a full-fat $20,000 A100 with 80GB of VRAM",
    "url": "https://www.tomshardware.com/pc-components/gpus/techie-turns-usd2-500-cmp-170hx-8gb-mining-card-into-a-full-fat-a100-80gb-with-voltage-glitching-carefully-blowing-onboard-fuses-to-unlock-entire-vram-and-shader-modules",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T10:30:00+00:00",
    "summary": "A techie turned a $2,500 CMP-170HX 8GB mining card into a full-fat $20,000 A100 80GB by carefully blowing onboard fuses to unlock entire VRAM and shader modules."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/cannabis-farmers-consider-joining-ai-bandwagon-due-to-falling-weed-revenue-existing-sites-could-house-mini-data-center-nodes-but-still-face-serious-challenges-during-conversion",
    "domain": "AI 算力 / 半导体",
    "title": "Struggling marijuana farmers pivot to becoming AI data center sites to escape falling weed revenue",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/cannabis-farmers-consider-joining-ai-bandwagon-due-to-falling-weed-revenue-existing-sites-could-house-mini-data-center-nodes-but-still-face-serious-challenges-during-conversion",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T10:00:00+00:00",
    "summary": "One expert says that it still depends on the perfect confluence of cheap power, favorable regulation, and reliable connectivity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-board-reportedly-preparing-to-oust-ceo-jensen-huang-as-second-extra-marital-affair-emerges-stock-has-plunged-20-percent-since-scandals-began-huang-has-been-first-and-only-ceo-for-33-years",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Board reportedly preparing to oust CEO Jensen Huang as second extra-marital affair emerges",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-board-reportedly-preparing-to-oust-ceo-jensen-huang-as-second-extra-marital-affair-emerges-stock-has-plunged-20-percent-since-scandals-began-huang-has-been-first-and-only-ceo-for-33-years",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:45:00+00:00",
    "summary": "Nvidia Board reportedly moves to expel Jensen Huang as stock tumbles on latest scandals and lack of succession plans at Nvidia."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/jensen-huang-now-accused-of-affair-with-nvidia-executive-who-reported-to-him-alleged-cover-up-attempt-new-indiscretion-comes-in-wake-of-admitted-affair-with-alleged-chinese-spy",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang now accused of affair with Nvidia executive who reported to him, alleged cover-up attempt",
    "url": "https://www.tomshardware.com/tech-industry/jensen-huang-now-accused-of-affair-with-nvidia-executive-who-reported-to-him-alleged-cover-up-attempt-new-indiscretion-comes-in-wake-of-admitted-affair-with-alleged-chinese-spy",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T22:31:39+00:00",
    "summary": "Nvidia CEO Jensen Huang reportedly had an extramarital affair with a direct report, following a separate affair with a woman suspected of being a Chinese spy."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-venice-x-maxes-out-family-at-5-3-ghz-returning-3d-v-cache-to-data-center-after-four-years-chips-target-hpc-workloads-with-pcie-6-0-and-1-6-tb-s-memory-bandwidth",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s Venice-X maxes out family at 5.3 GHz, returning 3D V-Cache to data center after four years",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-venice-x-maxes-out-family-at-5-3-ghz-returning-3d-v-cache-to-data-center-after-four-years-chips-target-hpc-workloads-with-pcie-6-0-and-1-6-tb-s-memory-bandwidth",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T21:30:00+00:00",
    "summary": "AMD's Venice-X CPUs launch in the second half of 2027, bringing 3D V-Cache back to the data center after four years on the sidelines."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-launches-new-carbon-3d-printing-filament-for-electronics-manufacturing-carbon-fiber-and-carbon-nanotube-filled-material-dissipates-electrostatic-energy-for-static-sensitive-electronics",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa launches new carbon-fiber and carbon-nanotube-filled 3D printing filament for electronics manufacturing",
    "url": "https://www.tomshardware.com/3d-printing/prusa-launches-new-carbon-3d-printing-filament-for-electronics-manufacturing-carbon-fiber-and-carbon-nanotube-filled-material-dissipates-electrostatic-energy-for-static-sensitive-electronics",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T21:00:00+00:00",
    "summary": "Prusament PETG ESD is the cheapest ESD filament on the market, while being carbon-fiber reinforced, something the competition doesn't have."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/georgia-politicians-openai-slapped-with-racketeering-lawsuit-over-3-2-gigawatt-ai-data-centers-plaintiffs-allege-multiple-violations-were-part-of-a-coordinated-scheme-to-get-project-camellia-approved",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI and Georgia county leaders hit with Mafia-style RICO racketeering lawsuit over $30 billion AI data center",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/georgia-politicians-openai-slapped-with-racketeering-lawsuit-over-3-2-gigawatt-ai-data-centers-plaintiffs-allege-multiple-violations-were-part-of-a-coordinated-scheme-to-get-project-camellia-approved",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T16:30:00+00:00",
    "summary": "The plaintiffs alleged that the parties committed fraud and concealment through NDAs and misleading public statements."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-peripheral-maker-logitech-giving-all-of-its-7-000-employees-the-day-off-to-play-gta-6-company-announces-game-day-initiative-dedicated-vacation-day-to-play-video-games",
    "domain": "AI 算力 / 半导体",
    "title": "PC peripheral maker Logitech giving all of its 7,000 employees the day off to play GTA 6",
    "url": "https://www.tomshardware.com/video-games/pc-peripheral-maker-logitech-giving-all-of-its-7-000-employees-the-day-off-to-play-gta-6-company-announces-game-day-initiative-dedicated-vacation-day-to-play-video-games",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T15:55:12+00:00",
    "summary": "Accessory maker Logitech has a new \"Logi Game Day\" initiative that allows employees to take a day off from now until this time next year to play a game of their choice — including the one everyone is "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-develops-its-own-kessel-rack-scale-system-featuring-72-nvidia-rubin-gpus-for-data-centers-in-space-report-claims-replaces-conventional-nvlink-cable-assemblies-with-a-massive-84-layer-printed-circuit-board",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX develops its own ‘Kessel’ rack-scale system featuring 72 Nvidia Rubin GPUs for data centers in space, report claims",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-develops-its-own-kessel-rack-scale-system-featuring-72-nvidia-rubin-gpus-for-data-centers-in-space-report-claims-replaces-conventional-nvlink-cable-assemblies-with-a-massive-84-layer-printed-circuit-board",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T15:03:08+00:00",
    "summary": "SpaceX is reportedly developing a 'Kessel' rack-scale system design with 72 Nvidia Rubin GPUs that relies on a massive 84-layer PCB midplane."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/softbank-loses-usd3-7-billion-on-canceled-ai-data-center-gas-turbine-orders-days-after-denying-elon-musks-claim-it-was-defaulting-company-kills-reserved-13-gigawatts-of-power-more-than-six-hoover-dams-worth-of-capacity",
    "domain": "AI 算力 / 半导体",
    "title": "Softbank loses $3.7 billion on canceled AI data center gas turbine orders days after denying Elon Musk’s claim it was defaulting",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/softbank-loses-usd3-7-billion-on-canceled-ai-data-center-gas-turbine-orders-days-after-denying-elon-musks-claim-it-was-defaulting-company-kills-reserved-13-gigawatts-of-power-more-than-six-hoover-dams-worth-of-capacity",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T14:29:43+00:00",
    "summary": "SoftBank might not have defaulted on a raft of gas turbine orders, but it has pulled out of deals for unwanted power units after overestimating how many it could use amid the AI data center buildout b"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/asrock-attempts-to-correct-botched-radeon-rx-7000-firmware-release-with-new-version-revised-release-should-work-ok-but-company-provides-no-explanation-for-bricked-cards",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock quietly rolls out new firmware after disastrous previous update killed Radeon RX 7900-series GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/asrock-attempts-to-correct-botched-radeon-rx-7000-firmware-release-with-new-version-revised-release-should-work-ok-but-company-provides-no-explanation-for-bricked-cards",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T14:20:00+00:00",
    "summary": "Asrock's VBIOS 1.0.6 update follows reports of Radeon RX 7900 XT and XTX graphics cards failing to boot after installing the previous firmware."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/montech-king-95-3d-pro-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Montech King 95 3D Pro case review: The King has returned",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/montech-king-95-3d-pro-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T14:00:00+00:00",
    "summary": "The new Montech King 95 3D case offers 3-panel panoramic views of the inside, loads of interior space for components and cooling, and the Pro version comes with seven RGB fan"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-unleashes-dmca-takedown-wave-against-open-source-switch-modchip-firmware-144-tools-disabled-picofly-sx-core-and-hwfly-among-casualties-following-criminal-trial-victory",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo unleashes DMCA takedown wave against open-source Switch modchip firmware, 144 tools disabled",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-unleashes-dmca-takedown-wave-against-open-source-switch-modchip-firmware-144-tools-disabled-picofly-sx-core-and-hwfly-among-casualties-following-criminal-trial-victory",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T13:42:37+00:00",
    "summary": "Nintendo is going after the open-source firmware behind hardware modchips on Nintendo Switch"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/cognichip-reveals-how-its-new-ai-assisted-program-can-slash-chip-design-times-from-months-to-days-automating-labor-intensive-tasks-cuts-design-time-down-chief-product-officer-explains",
    "domain": "AI 算力 / 半导体",
    "title": "Cognichip reveals how its new AI-assisted program can slash chip design times from months to days — automating labor-intensive tasks cuts design time down, Chief Product Officer explains",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/cognichip-reveals-how-its-new-ai-assisted-program-can-slash-chip-design-times-from-months-to-days-automating-labor-intensive-tasks-cuts-design-time-down-chief-product-officer-explains",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T13:30:00+00:00",
    "summary": "Cognichip claims its AI can slash chip design time from months to days, only that that design must be very simplistic."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/congress-could-issue-subpoena-to-nvidia-ceo-jensen-huang-if-he-doesnt-respond-by-today-to-request-for-a-joint-closed-door-briefing-us-representatives-want-to-discuss-companys-security-protocols-against-foreign-adversary-espionage",
    "domain": "AI 算力 / 半导体",
    "title": "Congress could issue subpoena to Nvidia CEO Jensen Huang if he doesn’t respond by today to request for a ‘joint, closed-door briefing’",
    "url": "https://www.tomshardware.com/tech-industry/policy/congress-could-issue-subpoena-to-nvidia-ceo-jensen-huang-if-he-doesnt-respond-by-today-to-request-for-a-joint-closed-door-briefing-us-representatives-want-to-discuss-companys-security-protocols-against-foreign-adversary-espionage",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T13:04:44+00:00",
    "summary": "Three committee chairpersons want to grill Jensen Huang about his company's 'security protocols against foreign adversary espionage,' as a former CIA agent says that he had a target on his back as the"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/cyanogen-co-founder-unveils-kora-a-linux-os-that-splits-ai-models-across-the-cpu-gpu-and-npu-snapdragon-x2-elite-and-hexagon-npu-get-full-support-first",
    "domain": "AI 算力 / 半导体",
    "title": "Cyanogen co-founder unveils Kora, a Linux OS that splits AI models across the CPU, GPU, and NPU",
    "url": "https://www.tomshardware.com/software/linux/cyanogen-co-founder-unveils-kora-a-linux-os-that-splits-ai-models-across-the-cpu-gpu-and-npu-snapdragon-x2-elite-and-hexagon-npu-get-full-support-first",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T13:00:00+00:00",
    "summary": "Kora, a Linux desktop OS with built-in AI models and agents for local agentic work, is coming to PCs in 2027, including Snapdragon X2 Elite machines."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back",
    "domain": "AI 算力 / 半导体",
    "title": "Linux kernel reviewer steps down from memory management duties due to influx of AI slop patches",
    "url": "https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T12:30:00+00:00",
    "summary": "Linux kernel memory-management code reviewer steps down due to influx of AI slop patches — volume of submissions coupled with low manpower forces the step back"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/save-36-percent-on-this-hoto-cordless-rotary-3d-printing-toolkit-for-makers-now-under-usd32-5-speed-tool-ships-with-35-attachments-for-sanding-polishing-carving-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Save 36% on this Hoto cordless rotary 3D printing toolkit for makers, now under $32",
    "url": "https://www.tomshardware.com/desktops/pc-building/save-36-percent-on-this-hoto-cordless-rotary-3d-printing-toolkit-for-makers-now-under-usd32-5-speed-tool-ships-with-35-attachments-for-sanding-polishing-carving-and-more",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T12:00:00+00:00",
    "summary": "Grab a 36% saving on Hoto’s cordless rotary toolkit, with a 25,000 RPM motor, 35 accessories and a built-in LED ring light."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-shares-how-it-can-retain-95-percent-of-server-performance-with-just-half-the-dram-sidestepping-memory-shortages-with-mext-tech-powers-over-100-servers-already-running-with-plans-to-expand-to-2-000-servers-in-2027",
    "domain": "AI 算力 / 半导体",
    "title": "AMD shares how it can retain 95% of server performance with just half the DRAM, sidestepping memory shortages with MEXT",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-shares-how-it-can-retain-95-percent-of-server-performance-with-just-half-the-dram-sidestepping-memory-shortages-with-mext-tech-powers-over-100-servers-already-running-with-plans-to-expand-to-2-000-servers-in-2027",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T12:00:00+00:00",
    "summary": "Following AMD’s acquisition of MEXT earlier this year, the company has revealed its own IT infrastructure is using the technology to run servers at 50% DRAM capacity while achieving 95% of the perform"
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1467,
    "published_at": "2026-10-13T16:03:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50261319",
    "domain": "大厂 AI 动态",
    "title": "Genie 4",
    "url": "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1044,
    "published_at": "2026-10-27T16:06:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50276792",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1019,
    "published_at": "2026-10-28T17:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50403097",
    "domain": "大厂 AI 动态",
    "title": "Every Mac comes with an (undocumented) family member classifier",
    "url": "https://8rank.ai/game/apple-intelligence-personal-knowledge-graph",
    "source": "infwhispers",
    "platform": "hackernews",
    "points": 869,
    "published_at": "2026-11-07T09:46:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50429426",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini routes personal Drive files and emails to human annotators",
    "url": "https://github.com/thisisme6598/gemini_files/",
    "source": "gf74918",
    "platform": "hackernews",
    "points": 737,
    "published_at": "2026-11-09T18:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50439193",
    "domain": "大厂 AI 动态",
    "title": "AlphaProof Code",
    "url": "https://deepmind.google/blog/introducing-alphaproof-code/",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 673,
    "published_at": "2026-11-10T12:11:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363461",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)",
    "url": "https://news.ycombinator.com/item?id=50363461",
    "source": "jameslk",
    "platform": "hackernews",
    "points": 737,
    "published_at": "2026-11-04T10:10:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50456791",
    "domain": "大厂 AI 动态",
    "title": "Gemini Decisions API",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/",
    "source": "iamdelirium",
    "platform": "hackernews",
    "points": 440,
    "published_at": "2026-11-11T18:32:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50411961",
    "domain": "大厂 AI 动态",
    "title": "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU",
    "url": "https://github.com/synchopate/llama-modchip",
    "source": "joshcsimmons",
    "platform": "hackernews",
    "points": 483,
    "published_at": "2026-11-08T10:22:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392118",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.2 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 369,
    "published_at": "2026-11-06T13:35:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50442303",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 294,
    "published_at": "2026-11-10T16:07:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122431",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console",
    "url": "https://github.com/cobanov/PS5LM",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 375,
    "published_at": "2026-10-16T18:32:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-10-29T12:41:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-10-16T14:18:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074869",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon for Robotics",
    "url": "https://developers.googleblog.com/gemini-4-argon-for-robotics/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 235,
    "published_at": "2026-10-13T16:55:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50355504",
    "domain": "大厂 AI 动态",
    "title": "Google researchers demand freedom to tell the world what they know about AI",
    "url": "https://www.washingtonpost.com/technology/2026/11/03/google-deepmind-staff-protest-lifetime-ban-criticizing-company/",
    "source": "nsagent",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-11-03T17:55:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1031601/home-assistant-connect-aux-2-hands-on",
    "domain": "大厂 AI 动态",
    "title": "Hands on with Home Assistant’s new ‘smart home multi-tool’",
    "url": "https://www.theverge.com/tech/1031601/home-assistant-connect-aux-2-hands-on",
    "source": "Nathan Edwards",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T22:00:00+00:00",
    "summary": "Nabu Casa - the commercial side of the Open Home Foundation, which runs Home Assistant - just launched the Home Assistant Connect Aux-2, a multi-function box designed to help you bring more non-smart "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1031623/united-unauthorized-ai-agents",
    "domain": "大厂 AI 动态",
    "title": "United won’t let your AI agent book your flight",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1031623/united-unauthorized-ai-agents",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T21:54:21+00:00",
    "summary": "United says it won't let personal AI assistants book tickets on the airline, citing both privacy and regulatory concerns. The company says it hasn't yet seen many people try to use AI agents to book t"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1031575/digital-fairness-act-eu-dfa-consumer-protection",
    "domain": "大厂 AI 动态",
    "title": "Loot boxes, influencers, and addictive features face an EU crackdown",
    "url": "https://www.theverge.com/policy/1031575/digital-fairness-act-eu-dfa-consumer-protection",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T18:13:52+00:00",
    "summary": "Gaming, social media, and e-commerce platforms are facing a fresh wave of sweeping European Union rules that aim to make \"your online experience fairer.\" The newly proposed Digital Fairness Act (DFA) "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1031554/oyota-scion-kei-01-truck-revival",
    "domain": "大厂 AI 动态",
    "title": "Toyota’s Scion is back, starting with an American-made, 25-mph kei truck",
    "url": "https://www.theverge.com/transportation/1031554/oyota-scion-kei-01-truck-revival",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T17:09:58+00:00",
    "summary": "Toyota is dusting off the Scion badge for a radically different mission. Rather than targeting youth-market hatchbacks, \"Scion by Toyota\" is being positioned as an experimental mobility incubator - an"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1031526/google-tabletop-ai-experiment-waitlist-availability",
    "domain": "大厂 AI 动态",
    "title": "Google’s Tabletop AI experiment lets you build custom collaboration apps",
    "url": "https://www.theverge.com/tech/1031526/google-tabletop-ai-experiment-waitlist-availability",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T16:00:00+00:00",
    "summary": "Google has cooked up a new experimental AI tool called Tabletop that generates customized collaborative hubs to help you coordinate with family, and friends. The Tabletop platform shares some visual s"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1028991/black-friday-best-early-deals-2026",
    "domain": "大厂 AI 动态",
    "title": "The best early Black Friday deals you can already shop",
    "url": "https://www.theverge.com/gadgets/1028991/black-friday-best-early-deals-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T15:53:55+00:00",
    "summary": "The countdown to Black Friday is on, and the first discounts are starting to appear. Although the shopping holiday isn&#8217;t officially until November 27th, retailers are already dropping early deal"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1031301/sharge-140w-gan-charger-lenovo-yoga-mini-desktop-pc-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Sharge’s eye-catching MacBook charger is over 25 percent off",
    "url": "https://www.theverge.com/gadgets/1031301/sharge-140w-gan-charger-lenovo-yoga-mini-desktop-pc-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T15:30:00+00:00",
    "summary": "Looking for a MacBook and device charger that’s as stylish as it is capable? Both Amazon and Sharge are selling the Pixel 140W GaN charger for $69.88 and $69.90, respectively, a $24 discount on its us"
  },
  {
    "id": "rss:https://www.theverge.com/games/1031321/the-legend-of-zelda-ocarina-of-time-notes-app-gold-skulltula",
    "domain": "大厂 AI 动态",
    "title": "Ocarina of Time is even better if you use a smartphone app",
    "url": "https://www.theverge.com/games/1031321/the-legend-of-zelda-ocarina-of-time-notes-app-gold-skulltula",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T15:00:00+00:00",
    "summary": "I never liked hunting for Golden Skulltulas in The Legend of Zelda: Ocarina of Time. The game has 100 of them tucked all over Hyrule, and even over my many hours with the N64 classic growing up, I can"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model",
    "domain": "大厂 AI 动态",
    "title": "Google’s AlphaGenome 2 zooms in on the cellular roots of disease",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T15:00:00+00:00",
    "summary": "Researchers at Google DeepMind have unveiled a new AI model designed to unravel how changes in our DNA affect different cells, giving scientists a more detailed view of a notoriously difficult problem"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/who-could-replace-jensen-huang-a-highly-unscientific-list-of-possible-successors/",
    "domain": "大厂 AI 动态",
    "title": "Who could replace Jensen Huang? A highly unscientific list of possible successors",
    "url": "https://techcrunch.com/2026/11/11/who-could-replace-jensen-huang-a-highly-unscientific-list-of-possible-successors/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-12T03:13:10+00:00",
    "summary": "Nvidia has no succession plan and a CEO in hot water, so we’ve drafted a shortlist."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "domain": "大厂 AI 动态",
    "title": "The unfolding Jensen Huang scandal: a timeline",
    "url": "https://techcrunch.com/2026/11/11/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:50:00+00:00",
    "summary": "The affair could have ramifications for national security as the U.S. and China race to develop the most advanced AI infrastructure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/nvidias-stock-drops-as-board-reportedly-preps-to-oust-ceo-jensen-huang/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia’s stock drops as board reportedly preps to oust CEO Jensen Huang",
    "url": "https://techcrunch.com/2026/11/11/nvidias-stock-drops-as-board-reportedly-preps-to-oust-ceo-jensen-huang/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:28:45+00:00",
    "summary": "As soon as Wednesday evening, Nvidia's board could decide to remove its founder and CEO of 33 years."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/jensen-huang-accused-of-having-another-affair-with-a-nvidia-exec/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang accused of having another affair — with an Nvidia exec",
    "url": "https://techcrunch.com/2026/11/11/jensen-huang-accused-of-having-another-affair-with-a-nvidia-exec/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:17:05+00:00",
    "summary": "Jensen Huang, who has come under fire for admitting to an affair with a woman accused of being a Chinese intelligence agent, has been accused of having a separate affair with an Nvidia subordinate."
  },
  {
    "id": "rss:https://techcrunch.com/video/why-the-data-center-you-dread-might-never-even-be-built/",
    "domain": "大厂 AI 动态",
    "title": "Why the data center you dread might never even be built",
    "url": "https://techcrunch.com/video/why-the-data-center-you-dread-might-never-even-be-built/",
    "source": "Theresa Loconsolo, Rebecca Bellan, Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T20:15:15+00:00",
    "summary": "The data center boom is running into serious real-world obstacles, from widespread local opposition and permitting delays to a scramble for electricity.&#160;Before those challenges even come into pla"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/meta-is-losing-its-longtime-head-of-infrastructure/",
    "domain": "大厂 AI 动态",
    "title": "Meta is losing its longtime head of infrastructure",
    "url": "https://techcrunch.com/2026/11/11/meta-is-losing-its-longtime-head-of-infrastructure/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T20:12:01+00:00",
    "summary": "Santosh Janardhan, who originally joined the company in 2009, will be stepping down from his role."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/olaf-sakkers-is-betting-he-can-beat-the-emerging-manager-squeeze/",
    "domain": "大厂 AI 动态",
    "title": "Olaf Sakkers is betting he can beat the emerging-manager squeeze",
    "url": "https://techcrunch.com/2026/11/11/olaf-sakkers-is-betting-he-can-beat-the-emerging-manager-squeeze/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T20:04:28+00:00",
    "summary": "Entering into the world of venture capital has never been easy, especially as a first-time fund manager. But it's especially daunting right now. Olaf Sakkers has spent the past five years proving that"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth/",
    "domain": "大厂 AI 动态",
    "title": "CoreWeave turns to customer prepayments, shorter contracts to fund AI growth",
    "url": "https://techcrunch.com/2026/11/11/coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T19:54:00+00:00",
    "summary": "CoreWeave is increasingly asking customers to pay up front, borrowing against specific contracts, and even looking to short-term deals that could lead to higher prices, according to the company’s thir"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/with-720m-round-britains-fractile-gets-a-leg-up-in-the-race-for-ai-chips/",
    "domain": "大厂 AI 动态",
    "title": "With $720M round, Britain’s Fractile gets a leg up in the race for AI chips",
    "url": "https://techcrunch.com/2026/11/11/with-720m-round-britains-fractile-gets-a-leg-up-in-the-race-for-ai-chips/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T19:34:55+00:00",
    "summary": "Fractile has now become one of the top-funded players in the race for purpose-built AI chips."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/congress-to-call-jensen-huang-in-to-answer-for-alleged-chinese-spy-affair/",
    "domain": "大厂 AI 动态",
    "title": "Congress to call Jensen Huang in to answer for alleged Chinese spy affair",
    "url": "https://techcrunch.com/2026/11/11/congress-to-call-jensen-huang-in-to-answer-for-alleged-chinese-spy-affair/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T19:22:22+00:00",
    "summary": "Nvidia CEO Jensen Huang has until the end of the day Wednesday to answer a call from House Republicans for a closed-door briefing on his affair with alleged Chinese spy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/is-jensen-huangs-bad-behavior-more-commonplace-than-it-seems/",
    "domain": "大厂 AI 动态",
    "title": "Is Jensen Huang’s bad behavior more commonplace than it seems?",
    "url": "https://techcrunch.com/2026/11/11/is-jensen-huangs-bad-behavior-more-commonplace-than-it-seems/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T16:16:07+00:00",
    "summary": "“There are a lot of senior people in the industry that know this is happening, and are effectively condoning it,” an investment intel consultant said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/openais-quarterly-revenue-reportedly-crosses-10b-for-the-first-time/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s quarterly revenue reportedly crosses $10B for the first time",
    "url": "https://techcrunch.com/2026/11/11/openais-quarterly-revenue-reportedly-crosses-10b-for-the-first-time/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T16:14:44+00:00",
    "summary": "Sales of $10 billion represents an almost 50% jump from revenue of $6.7 billion the company recorded in the second quarter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/siri-co-founder-backs-helix-for-its-voice-id-tech/",
    "domain": "大厂 AI 动态",
    "title": "Siri co-founder backs Helix for its voice ID tech",
    "url": "https://techcrunch.com/2026/11/11/siri-co-founder-backs-helix-for-its-voice-id-tech/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T15:02:47+00:00",
    "summary": "With the rise of AI agents like Instinct and Muse, the industry needs to rethink human identity on the internet and rely on biometric signals like voice, which is where Helix comes in."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/databricks-new-ai-agent-tells-ceo-ali-ghodsi-the-unvarnished-truth/",
    "domain": "大厂 AI 动态",
    "title": "Databricks’ new AI agent tells CEO Ali Ghodsi the unvarnished truth",
    "url": "https://techcrunch.com/2026/11/11/databricks-new-ai-agent-tells-ceo-ali-ghodsi-the-unvarnished-truth/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T15:00:00+00:00",
    "summary": "With Databricks at 12,000 employees, AI Ghodsi is the first to admit that he can't know everyone and that they are unlikely to confess the things that go wrong to him. But he doesn't need them to. He "
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/11/plurai-wants-to-help-ai-agents-work-better-using-the-same-approach-that-helped-get-self-driving-cars-to-roads/",
    "domain": "大厂 AI 动态",
    "title": "Plurai wants to help AI agents work better using the same approach that helped get self-driving cars to roads",
    "url": "https://techcrunch.com/2026/11/11/plurai-wants-to-help-ai-agents-work-better-using-the-same-approach-that-helped-get-self-driving-cars-to-roads/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T14:00:00+00:00",
    "summary": "Like the end-to-end models trained to drive cars, AI agents are probabilistic systems operating in unpredictable environments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/nvidias-crisis-has-corporate-governance-experts-reaching-for-the-popcorn/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia’s crisis has corporate governance experts reaching for the popcorn",
    "url": "https://techcrunch.com/2026/11/10/nvidias-crisis-has-corporate-governance-experts-reaching-for-the-popcorn/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T07:30:51+00:00",
    "summary": "The governance experts we talked to say nobody has seen anything like what's unfolding right now."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/x-launches-its-own-clipping-feature-to-spur-influencer-engagement/",
    "domain": "大厂 AI 动态",
    "title": "X launches its own clipping feature to spur influencer engagement",
    "url": "https://techcrunch.com/2026/11/10/x-launches-its-own-clipping-feature-to-spur-influencer-engagement/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T01:02:13+00:00",
    "summary": "X is jumping into clipping, the popular practice of cutting long videos into short, shareable clips that can go viral."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/openai-acquires-odessia-travel-startup-created-by-sonder-founder/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI acquires Odessia, travel startup created by Sonder founder",
    "url": "https://techcrunch.com/2026/11/10/openai-acquires-odessia-travel-startup-created-by-sonder-founder/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T21:08:52+00:00",
    "summary": "OpenAI has not yet said what its plans are for the future of travel. But Sonder founder Francis Davidson is a well-known figure in the travel industry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/openai-anthropic-face-new-oversight-as-new-yorks-ai-safety-law-takes-effect/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI, Anthropic face new oversight as New York’s AI safety law takes effect",
    "url": "https://techcrunch.com/2026/11/10/openai-anthropic-face-new-oversight-as-new-yorks-ai-safety-law-takes-effect/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T20:52:13+00:00",
    "summary": "New York is preparing to enforce its sweeping AI safety law, requiring major developers like OpenAI and Anthropic to register, disclose safety practices, and report critical incidents or face fines."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/10/proximal-ventures-raises-debut-fund-to-back-startups-bringing-ai-to-drug-development/",
    "domain": "大厂 AI 动态",
    "title": "Proximal Ventures raises debut fund to back startups bringing AI to drug development",
    "url": "https://techcrunch.com/2026/11/10/proximal-ventures-raises-debut-fund-to-back-startups-bringing-ai-to-drug-development/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T20:47:05+00:00",
    "summary": "Former SignalFire investor Sahir Raoof raises $27.5 million for new fund targeting AI in pharma."
  },
  {
    "id": "rss:https://stratechery.com/2026/intel-earnings-amd-earnings-intel-and-amds-divergence/",
    "domain": "大厂 AI 动态",
    "title": "Intel Earnings, AMD Earnings, Intel and AMD’s Divergence",
    "url": "https://stratechery.com/2026/intel-earnings-amd-earnings-intel-and-amds-divergence/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T11:00:00+00:00",
    "summary": "Intel and AMD's diverging earnings point to fundamental historical differences, and make me wonder if Intel needs to find a new (old) path."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-jensen-huang-story-gets-worse-washington-vs-new-york-silicon-valley/",
    "domain": "大厂 AI 动态",
    "title": "The Jensen Huang Story Gets Worse, Washington vs. New York, Silicon Valley",
    "url": "https://stratechery.com/2026/the-jensen-huang-story-gets-worse-washington-vs-new-york-silicon-valley/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-10T11:00:00+00:00",
    "summary": "The Jensen Huang story got worse for him on Monday; the real risk for Huang is governance, even more than national security. Who benefits?"
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/ceo-jensen-huangs-job-is-suddenly-on-the-line-at-nvidia/",
    "domain": "大厂 AI 动态",
    "title": "CEO Jensen Huang's job is suddenly on the line at Nvidia",
    "url": "https://arstechnica.com/gadgets/2026/11/ceo-jensen-huangs-job-is-suddenly-on-the-line-at-nvidia/",
    "source": "Demetri Sevastopulo, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T23:10:17+00:00",
    "summary": "The FBI is investigating as Nvidia’s board holds urgent talks over Huang’s future."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/t-mobile-illegally-imposed-50-gb-cap-on-low-income-home-internet-plan-ny-says/",
    "domain": "大厂 AI 动态",
    "title": "T-Mobile illegally imposed 50GB cap on low-income home Internet plan, NY says",
    "url": "https://arstechnica.com/tech-policy/2026/11/t-mobile-illegally-imposed-50-gb-cap-on-low-income-home-internet-plan-ny-says/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T20:32:21+00:00",
    "summary": "Law requires 25Mbps home Internet. T-Mobile lowers speed to 600Kbps after 50GB cap."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/anduril-demos-night-vision-sensor-for-tracking-satellites-in-darkness/",
    "domain": "大厂 AI 动态",
    "title": "Anduril says its first satellite can see adversaries maneuver in orbital night",
    "url": "https://arstechnica.com/space/2026/11/anduril-demos-night-vision-sensor-for-tracking-satellites-in-darkness/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-11T20:22:03+00:00",
    "summary": "\"What's unique is it's got a huge dynamic range. We can see things in full dark.\""
  },
  {
    "id": "hn:50306008",
    "domain": "股票",
    "title": "US tech stocks see sharp falls over AI cost fears",
    "url": "https://www.bbc.co.uk/news/articles/cvwy72e0n72yo",
    "source": "mindracer",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-30T16:13:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50381623",
    "domain": "股票",
    "title": "Nasdaq plummets 4% into correction territory",
    "url": "https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 227,
    "published_at": "2026-11-05T17:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50346153",
    "domain": "股票",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 236,
    "published_at": "2026-11-03T00:08:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342284",
    "domain": "股票",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-11-02T19:27:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384822",
    "domain": "股票",
    "title": "$2.5T has been wiped from US stocks",
    "url": "https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 164,
    "published_at": "2026-11-05T21:39:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50382179",
    "domain": "股票",
    "title": "Nasdaq Sinks 5% as Investors Retreat from AI Trade After Election",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-05-2026",
    "source": "armcat",
    "platform": "hackernews",
    "points": 163,
    "published_at": "2026-11-05T18:00:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50151376",
    "domain": "股票",
    "title": "The obscure trust looming over Anthropic's IPO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-private-trust-188f41f7?st=RtdGHg&reflink=desktopwebshare_permalink",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 154,
    "published_at": "2026-10-19T12:06:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50401029",
    "domain": "股票",
    "title": "The AI sell-off compared to well-known stock market crashes",
    "url": "https://www.kadoa.com/companies/insights/ai-selloff-perspective",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-11-07T02:20:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50445463",
    "domain": "股票",
    "title": "Anthropic Targets $1.4T Valuation in IPO",
    "url": "https://www.bloomberg.com/news/videos/2026-11-10/anthropic-targets-1-4-trillion-valuation-in-ipo-video",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-10T19:56:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50456668",
    "domain": "股票",
    "title": "Anthropic says a key AI safety alarm has been triggered, days before its IPO",
    "url": "https://finance.yahoo.com/markets/article/anthropic-says-a-key-ai-safety-alarm-has-been-triggered-days-before-its-ipo-171519615.html",
    "source": "healsdata",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-11-11T18:23:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386909",
    "domain": "股票",
    "title": "Investors wipe $2.5T off Nasdaq as blue tsunami prompts AI fears",
    "url": "https://www.reuters.com/legal/transactional/ai-data-center-stocks-slip-democratic-sweep-clouds-expansion-plans-2026-11-05/",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-11-06T01:11:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362274",
    "domain": "股票",
    "title": "AI stocks slide as Texas governor result raises data center risks",
    "url": "https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html",
    "source": "1659447091",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-11-04T07:00:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:50389401",
    "domain": "股票",
    "title": "Global stocks tumble as AI panic grips markets after Democrats' midterm success",
    "url": "https://www.theguardian.com/business/live/2026/nov/06/global-stocks-tumble-ai-panic-markets-democrats-midterms-success-jobs-oil-dollar-latest-news-updates",
    "source": "drayfield",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-06T07:52:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384382",
    "domain": "股票",
    "title": "Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896",
    "url": "https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-05T20:58:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50352405",
    "domain": "股票",
    "title": "US Hedge Funds Just Sold Every AI Stock They Bought Since 2025",
    "url": "https://finance.yahoo.com/markets/stocks/articles/us-hedge-funds-just-sold-113114644.html",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-03T14:27:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385642",
    "domain": "股票",
    "title": "Michael Burry says Anthropic is 'betting its existence' on optimism",
    "url": "https://www.businessinsider.com/michael-burry-anthropic-ipo-outlook-ant-big-short-2026-11",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-11-05T22:49:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50351712",
    "domain": "股票",
    "title": "Anthropic's IPO Filing Warns It May Be 'Imminently' Close to RSI",
    "url": "https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-03T13:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386483",
    "domain": "股票",
    "title": "Major Investors Are Skeptical Anthropic IPO Can Achieve $1.5T Valuation",
    "url": "https://www.wsj.com/finance/major-investors-are-skeptical-anthropic-ipo-can-achieve-1-5-trillion-valuation-ca965d8b",
    "source": "sandinmyjoints",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-06T00:17:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50295611",
    "domain": "股票",
    "title": "Reddit will force everyone to log in",
    "url": "https://www.theverge.com/tech/1022571/reddit-login-requirement-q3-2026-earnings",
    "source": "timpera",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-29T20:43:17+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "domain": "股票",
    "title": "The Insatiable Demand for Alpha",
    "url": "https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T17:59:24+00:00",
    "summary": "Why a market shakedown could leave the biggest pod shops stronger"
  },
  {
    "id": "hn:50326281",
    "domain": "股票",
    "title": "Ant: Can unprecedented revenue growth outrun irresponsibly large investment",
    "url": "https://leonlins.com/writing/anthropic_ipo",
    "source": "avoidboringppl",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T14:56:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50323575",
    "domain": "股票",
    "title": "We're Living in the Age of the Imperial CEO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-dual-class-stock-founder-control-4c43a56d",
    "source": "pretext",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T08:09:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50167295",
    "domain": "股票",
    "title": "Data center stocks slide as Korea IPO plunges 30%, pressuring tech sentiment",
    "url": "https://www.cnbc.com/2026/10/20/data-center-stocks-slide-as-korea-ipo-plunges-30percent-pressuring-tech-sentiment.html",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-20T14:50:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50142772",
    "domain": "股票",
    "title": "How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill",
    "url": "https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-10-18T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50071744",
    "domain": "股票",
    "title": "Sprout Pi Mainboard – A modern, RP2350-powered motherboard for iPods",
    "url": "https://www.crowdsupply.com/certain-things/sprout-pi-mainboard",
    "source": "esskay",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-13T13:49:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50171533",
    "domain": "股票",
    "title": "Anthropic S-1 Shows Red-Hot Growth, Risks and Computing Costs",
    "url": "https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1",
    "source": "mmmmmbop",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-20T19:34:39+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/follow-the-money-ece",
    "domain": "股票",
    "title": "Follow the Money",
    "url": "https://www.netinterest.co/p/follow-the-money-ece",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:48:55+00:00",
    "summary": "What six years and 300+ posts of Net Interest say about where finance is heading"
  },
  {
    "id": "hn:50251762",
    "domain": "股票",
    "title": "Anthropic Is the Most Ridiculous IPO of 2026 [pdf]",
    "url": "https://www.newconstructs.com/wp-content/uploads/2026/10/Anthropic-Is-The-Most-Ridiculous-IPO-of-2026.pdf",
    "source": "simonebrunozzi",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T22:06:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50243343",
    "domain": "股票",
    "title": "Anthropic rushing IPO before AI bubble bursts",
    "url": "https://nypost.com/2026/10/23/business/wall-street-is-urging-anthropic-openai-to-do-their-ipos-in-a-hurry-heres-why/",
    "source": "nothrowaways",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T13:30:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082283",
    "domain": "股票",
    "title": "US Says Chinese Hackers Attacked DOJ, NASA, Federal Reserve, Senate",
    "url": "https://www.usatoday.com/story/news/politics/2026/08/26/chinese-hackers-cyberattack-us-government/91473585007/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-10-14T04:09:23+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/capital-wars",
    "domain": "股票",
    "title": "Capital Wars",
    "url": "https://www.netinterest.co/p/capital-wars",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:24:17+00:00",
    "summary": "CoreWeave and the Economics of a Data Center Build"
  },
  {
    "id": "rss:https://www.netinterest.co/p/me-and-my-agents",
    "domain": "股票",
    "title": "Me and My Agents",
    "url": "https://www.netinterest.co/p/me-and-my-agents",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:39:55+00:00",
    "summary": "Unleashing AI Agents on Bank Earnings"
  },
  {
    "id": "rss:https://www.netinterest.co/p/when-saturday-comes",
    "domain": "股票",
    "title": "When Saturday Comes",
    "url": "https://www.netinterest.co/p/when-saturday-comes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T12:42:20+00:00",
    "summary": "Football as an Asset Class"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-art-of-doing-financial-engineering",
    "domain": "股票",
    "title": "The Art of Doing Financial Engineering",
    "url": "https://www.netinterest.co/p/the-art-of-doing-financial-engineering",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T11:57:49+00:00",
    "summary": "AI Financing at the Frontier"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-agents-revolt",
    "domain": "股票",
    "title": "Agents Revolt",
    "url": "https://www.netinterest.co/p/the-agents-revolt",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:33:27+00:00",
    "summary": "What happens to finance when customers start paying attention"
  },
  {
    "id": "rss:https://www.netinterest.co/p/brookfield-of-dreams",
    "domain": "股票",
    "title": "Brookfield of Dreams",
    "url": "https://www.netinterest.co/p/brookfield-of-dreams",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:05:47+00:00",
    "summary": "Inside Brookfield&#8217;s Plan to Double Again"
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
    "id": "hn:50391456",
    "domain": "金融",
    "title": "Tesla to wind down Cybertruck production",
    "url": "https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 1163,
    "published_at": "2026-11-06T12:13:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50154244",
    "domain": "金融",
    "title": "DeepSeek banned from U.S. federal civilian agencies under new DHS order",
    "url": "https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/",
    "source": "cmrdporcupine",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-10-19T16:16:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385870",
    "domain": "金融",
    "title": "Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue",
    "url": "https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 524,
    "published_at": "2026-11-05T23:09:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:50305573",
    "domain": "金融",
    "title": "The federated code forge",
    "url": "https://tangled.org/blog/forge/",
    "source": "zlliang",
    "platform": "hackernews",
    "points": 333,
    "published_at": "2026-10-30T15:44:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50414427",
    "domain": "金融",
    "title": "Tesla Hasn't Had a Successful New Product Launch Since JB Straubel Stepped Down",
    "url": "https://cleantechnica.com/2026/11/07/tesla-hasnt-had-a-successful-new-product-launch-since-jb-straubel-stepped-down-as-cto/",
    "source": "gumby",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-11-08T16:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-20T22:21:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-10-17T14:22:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50190168",
    "domain": "金融",
    "title": "Epic Games Inc v Apple Inc",
    "url": "https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552",
    "source": "Mayzie",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-10-22T01:52:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50260526",
    "domain": "金融",
    "title": "A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies",
    "url": "https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-10-27T15:09:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236073",
    "domain": "金融",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50387406",
    "domain": "金融",
    "title": "Tesla and SpaceX lose over $420B in combined market cap in the two days",
    "url": "https://techlaws.pages.dev/tesla-and-spacex-lose-over-420b-in-combined-market-cap-in-the-two-days/",
    "source": "Pepitobombito",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-11-06T02:30:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-10-13T23:13:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082021",
    "domain": "金融",
    "title": "Strafe: A new open-source, E2E Encrypted, and federated alternative to Discord",
    "url": "https://strafe.chat/",
    "source": "brydencalaway",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-10-14T03:28:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:50278678",
    "domain": "金融",
    "title": "Show HN: A proof-of-concept formalization of the IRS federal tax forms",
    "url": "https://github.com/emmilco/us-tax-model",
    "source": "RGS1811",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-10-28T18:30:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50291902",
    "domain": "金融",
    "title": "Alphabet heads for a $500B drop in market value, biggest in its history",
    "url": "https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-10-29T16:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50372038",
    "domain": "金融",
    "title": "Harmony: Chat like Discord. Federated like email",
    "url": "https://mony.lol/",
    "source": "FinalDestiny",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-11-04T21:49:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50105900",
    "domain": "金融",
    "title": "Market selloff, rising rates test AI data centre deal boom",
    "url": "https://www.reuters.com/business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-10-15T16:17:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50394771",
    "domain": "金融",
    "title": "Only 16% of U.S. fast-charging stations meet federal NEVI standards (open data)",
    "url": "https://chargingnear.me/data",
    "source": "parkgraph",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-06T16:45:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50161207",
    "domain": "金融",
    "title": "U.S. Supreme Court to review 1868 federal ban on home distilling of liquor",
    "url": "https://www.staradvertiser.com/2026/10/19/breaking-news/u-s-supreme-court-to-review-1868-federal-ban-on-home-distilling-of-liquor/",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-10-20T04:02:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50394130",
    "domain": "金融",
    "title": "Tesla Ends Cybertruck Production",
    "url": "https://www.heise.de/en/news/Tesla-ends-Cybertruck-production-in-Texas-11515739.html",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-11-06T16:05:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50253630",
    "domain": "金融",
    "title": "The 'Buy, Borrow and Die' Wealth Strategy Has Become a $5T Market",
    "url": "https://www.wsj.com/finance/the-buy-borrow-and-die-wealth-strategy-has-become-a-5-trillion-market-d9149a9d",
    "source": "tysone",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-27T01:30:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50156189",
    "domain": "金融",
    "title": "The US orders every civilian agency to rip out DeepSeek, even tools built on it",
    "url": "https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-19T18:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50328462",
    "domain": "金融",
    "title": "US Jobs Pickup May Keep Fed on Track to Hike Rates Again",
    "url": "https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again",
    "source": "frank_clover",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-01T18:51:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50202671",
    "domain": "金融",
    "title": "AI compute is the new oil–and needs a new market",
    "url": "https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market",
    "source": "ijidak",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-22T23:45:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50360067",
    "domain": "金融",
    "title": "Tesla allegedly misled South Korean customers about automated-driving tech",
    "url": "https://www.reuters.com/business/autos-transportation/tesla-misled-south-korean-customers-about-automated-driving-tech-consumer-group-2026-11-04/",
    "source": "EA-3167",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-11-04T00:19:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-10-13T16:48:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50295332",
    "domain": "金融",
    "title": "Tesla caught altering specs following rear suspension collapse reports",
    "url": "https://carnewschina.com/2026/09/17/tesla-caught-quietly-altering-model-y-l-manual-specs-following-rear-suspension-collapse-reports/",
    "source": "Alien1Being",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-29T20:24:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50194602",
    "domain": "金融",
    "title": "Full Disk Encryption on Fedora with TPM2",
    "url": "https://www.apalrd.net/posts/2026/ent_luks/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-10-22T12:46:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122776",
    "domain": "金融",
    "title": "Show HN: Stoke Money – Personal finance app built around a cash flow forecast",
    "url": "https://stoke.money",
    "source": "_wesley",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-16T18:54:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236506",
    "domain": "金融",
    "title": "F45 (Fedora 45) Final Is No-Go",
    "url": "https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EWDOYT6TOMFY4XPL5MJC2QWCDJBOR6MU/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-25T22:09:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50159683",
    "domain": "金融",
    "title": "Trump Appointees Asked a Federal Agency to Acquire a Voting Machine and Hack It",
    "url": "https://www.propublica.org/article/cisa-election-security-donald-trump",
    "source": "soundworlds",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-10-20T00:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50152041",
    "domain": "金融",
    "title": "Federal judge rules Flock violated the fourth amendment",
    "url": "https://twitter.com/scotus_wire/status/2106487374624514071",
    "source": "vessenes",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-19T13:14:41+00:00",
    "summary": ""
  }
]
```
