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

- 今日日期：`2026-08-24`
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
  "date": "2026-08-24",
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
    "points": 1726947,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1175712,
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
    "points": 1095819,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 859160,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 622826,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 585142,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 578731,
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
    "points": 439552,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 251555,
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
    "points": 245539,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1i9Z8YhEja",
    "domain": "AI",
    "title": "学 AI，看这个视频就够了！最全程序员 AI 指南：AI核心概念、实用AI工具、AI编程技巧、AI开发技术",
    "url": "http://www.bilibili.com/video/av114262957626976",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 186639,
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
    "points": 179747,
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
    "points": 179113,
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
    "points": 164115,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161229,
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
    "points": 159528,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 158194,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 142136,
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
    "points": 97210,
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
    "points": 93336,
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
    "points": 91779,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63587,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47644,
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
    "points": 46730,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 45881,
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
    "points": 40973,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35159,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 31000,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29656,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1vwXPYkEGx",
    "domain": "AI",
    "title": "Cursor+mcp配置，手把手教你配置任意MCP服务，学不会你打我，小白保姆级教程~MCP服务配置指南 - 提升AI编程助手能力",
    "url": "http://www.bilibili.com/video/av114193181183930",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 27199,
    "published_at": "2025-03-20T05:51:23+00:00",
    "summary": "我的知识星球，https://t.zsxq.com/jVAk9\n\n📌 本期教程通过实战演示，教你在Cursor中配置和使用MCP服务器，特别是filesystem MCP服务，解决Cursor无法写入文件的常见问题。\n⏱️ 内容概要：\n00:00 介绍MCP及其重要性\n02:00 Cursor抽风问题与MCP解决方案\n04:00 配置第一个MCP服务器（filesystem）\n07:00 Wind"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 26719,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22734,
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
    "points": 20007,
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
    "points": 17970,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17740,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1NEuF6YEi3",
    "domain": "AI",
    "title": "小白从0到1搭建AI Agent｜不会代码也能做",
    "url": "http://www.bilibili.com/video/av117035308683606",
    "source": "然冉创业说",
    "platform": "bilibili",
    "points": 16844,
    "published_at": "2026-08-04T04:20:58+00:00",
    "summary": "欢迎关注公粽号，然冉创业说\n很高兴认识你~"
  },
  {
    "id": "bvid:BV1Wbtcz8ESV",
    "domain": "AI",
    "title": "一个视频彻底掌握ClaudeCode Agent",
    "url": "http://www.bilibili.com/video/av114981458677770",
    "source": "创哥的AI实验室",
    "platform": "bilibili",
    "points": 14752,
    "published_at": "2025-08-06T11:03:46+00:00",
    "summary": "一个视频介绍透ClaudeCode subagent的概念、定位、用法、跟自定义命令的区别与关联等等。这应该是全网最详细ClaudeCode subagent教学视频！\n\t\n﻿#cursor﻿ ﻿#ai编程﻿ ﻿#程序员﻿ ﻿#ClaudeCode﻿ ﻿#claudecode﻿"
  },
  {
    "id": "bvid:BV1iFYazEELw",
    "domain": "AI",
    "title": "Ai Agent工程师前景如何？【渡一教育】",
    "url": "http://www.bilibili.com/video/av115053063831903",
    "source": "渡一前端教科频道",
    "platform": "bilibili",
    "points": 13721,
    "published_at": "2025-08-27T03:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11042,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10901,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1GvmzBUEfj",
    "domain": "AI",
    "title": "【AI杂谈】3 claude code概念讲解与配置",
    "url": "http://www.bilibili.com/video/av115718414668601",
    "source": "左-岚",
    "platform": "bilibili",
    "points": 9592,
    "published_at": "2025-12-14T14:38:05+00:00",
    "summary": "飞书的ai杂谈目录下\nhttps://my.feishu.cn/wiki/space/7600816265116011716\n\n米醋工作室 AI 开发环境配置完整指南https://www.micu.wiki/t/topic/571\nClaude Code 常见问题与故障排查https://www.micu.wiki/t/topic/570\nClaude Code 核心概念详解\nhttps://w"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9405,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 9237,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8789,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1NUV86FEPX",
    "domain": "AI",
    "title": "【Claude Code】Claude Code自动更新到最新版请求报错解决方案分享——关闭自动更新、回退历史版本",
    "url": "http://www.bilibili.com/video/av116657318138948",
    "source": "月下Hugo",
    "platform": "bilibili",
    "points": 7971,
    "published_at": "2026-05-29T10:16:17+00:00",
    "summary": "Hugotools节点最新版获取地址：https://b23.tv/VPkN8i6\n\nHugoTools节点使用教程： https://b23.tv/PR665QZ\n\nComfyUI中超级好用的提示词管理节点——HugoPromptManager节点：https://b23.tv/BLNqQgT\n\nComfyUI-HugoPromptManager节点获取地址：https://b23.tv/J7s"
  },
  {
    "id": "bvid:BV1zcTTznEL8",
    "domain": "AI",
    "title": "MCP应用：为小智增加在线点歌服务",
    "url": "http://www.bilibili.com/video/av114635462156272",
    "source": "无敌哥-AI治理架构师",
    "platform": "bilibili",
    "points": 7395,
    "published_at": "2025-06-06T08:30:10+00:00",
    "summary": "除了对话、人脸识别、摄像头识别场景多模态交互外！其实，听音乐是我们的刚需，今天就给小智加上！背后利用了MCP ，话说MCP 真实为小智增加了无线可能！大家有啥想法，可以尽管提哈！"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7022,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6908,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6692,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1NxcCzEEBq",
    "domain": "AI",
    "title": "【Claude Code 实战】一次搞懂 OpenSpec，让专案每次迭代都有依据",
    "url": "http://www.bilibili.com/video/av116217436182465",
    "source": "西技大神",
    "platform": "bilibili",
    "points": 6671,
    "published_at": "2026-03-12T18:04:11+00:00",
    "summary": ""
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
    "points": 254,
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
    "id": "hn:49387755",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO scores 100% on the ARC-AGI-3 interactive reasoning benchmark",
    "url": "https://twitter.com/NVIDIAAI/status/2090786258981466231",
    "source": "dsrtslnd23",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-08-21T13:26:03+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/grab-the-asus-prime-radeon-rx-9070-oc-for-usd629-99-save-usd120-on-this-16gb-gaming-gpu-for-reliable-1440p-and-4k-gaming",
    "domain": "AI 算力 / 半导体",
    "title": "Grab the Asus Prime Radeon RX 9070 OC for $629.99 — save $120 on this 16GB gaming GPU for reliable 1440p and 4K gaming",
    "url": "https://www.tomshardware.com/pc-components/gpus/grab-the-asus-prime-radeon-rx-9070-oc-for-usd629-99-save-usd120-on-this-16gb-gaming-gpu-for-reliable-1440p-and-4k-gaming",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T14:07:45+00:00",
    "summary": "The Asus Prime Radeon RX 9070 OC is available for just $629.99 on Amazon, delivering strong 1440p performance, 16GB of VRAM, a 2,610MHz boost clock, and a triple-fan cooling system at a $120 discount."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/self-driving-ford-f-250-truck-with-shotgun-equipped-drone-killing-turret-tested-by-us-army-autonomous-system-designed-to-blast-fast-moving-drones-at-between-10-and-100-meters-range",
    "domain": "AI 算力 / 半导体",
    "title": "Self-driving Ford F-250 truck with shotgun-equipped drone-killing turret tested by US Army — autonomous system designed to blast fast-moving drones at between 10 and 100 meters range",
    "url": "https://www.tomshardware.com/tech-industry/drones/self-driving-ford-f-250-truck-with-shotgun-equipped-drone-killing-turret-tested-by-us-army-autonomous-system-designed-to-blast-fast-moving-drones-at-between-10-and-100-meters-range",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T13:19:17+00:00",
    "summary": "The US Army tested an autonomous breaching vehicle with an onboard counter-UAS turret during a live-fire exercise at Fort Bragg on August 18."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/nvidia-reportedly-warns-biggest-customers-of-15-percent-price-hikes-on-ai-servers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly warns biggest customers of 15% price hikes on AI servers — memory costs continue to soar",
    "url": "https://www.tomshardware.com/pc-components/dram/nvidia-reportedly-warns-biggest-customers-of-15-percent-price-hikes-on-ai-servers",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T13:15:00+00:00",
    "summary": "The increases will take effect on Grace Blackwell and Vera Rubin systems shipping early next year."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/nvidias-gb300-powered-dgx-station-desktop-tower-listed-for-nearly-usd100-000-online-enterprise-ai-powerhouse-now-available-to-buy-for-mere-mortals-with-lots-of-cash",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s GB300-powered DGX Station desktop tower listed for nearly $100,000 online — Enterprise AI powerhouse now available to buy for mere mortals with lots of cash",
    "url": "https://www.tomshardware.com/desktops/nvidias-gb300-powered-dgx-station-desktop-tower-listed-for-nearly-usd100-000-online-enterprise-ai-powerhouse-now-available-to-buy-for-mere-mortals-with-lots-of-cash",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T13:00:00+00:00",
    "summary": "Nvidia's most powerful desktop offering, the GB300 DGX Station, is available to buy starting from just $94,930 and you can spec it up to $108,350. It offers 748GB of unified memory shared across the 7"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/fake-gta-vi-iso-circulates-on-the-internet-a-few-days-after-leak-internet-sleuths-claim-113gb-download-is-padded-malware-testers-claim-file-is-99-99-percent-empty-zeroes-with-50kb-virus-embedded",
    "domain": "AI 算力 / 半导体",
    "title": "Fake GTA VI ISO circulates on the internet a few days after leak, internet sleuths claim 113GB download is padded malware — testers claim file is 99.99% empty zeroes with 50KB virus embedded",
    "url": "https://www.tomshardware.com/video-games/fake-gta-vi-iso-circulates-on-the-internet-a-few-days-after-leak-internet-sleuths-claim-113gb-download-is-padded-malware-testers-claim-file-is-99-99-percent-empty-zeroes-with-50kb-virus-embedded",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T12:45:00+00:00",
    "summary": "A 113GB GTA VI ISO file is circulating on the internet, with its file name making it seem like it was the game build that Cyberleek is allegedly in possession of. But upon further investigation, it ap"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/fcc-pulls-hoverair-versa-certification-three-days-after-launch",
    "domain": "AI 算力 / 半导体",
    "title": "Modular pocket gimbal camera that transforms into a self-flying drone retroactively banned by FCC, certification revoked — Agency closes foreign UAS loophole on 230g HoverAir Versa",
    "url": "https://www.tomshardware.com/tech-industry/drones/fcc-pulls-hoverair-versa-certification-three-days-after-launch",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T12:30:00+00:00",
    "summary": "The Versa, a 230g pocket gimbal camera that snaps into a separate propeller chassis for flight, raised more than $230,000 at its debut."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/tp-link-deco-7-pro-be13000-wi-fi-7-mesh-router-review",
    "domain": "AI 算力 / 半导体",
    "title": "TP-Link Deco 7 Pro BE13000 Wi-Fi 7 mesh router review: Value pricing, but average performance",
    "url": "https://www.tomshardware.com/networking/routers/tp-link-deco-7-pro-be13000-wi-fi-7-mesh-router-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T12:05:00+00:00",
    "summary": "The Deco 7 Pro BE13000 is attractively priced on the hardware front, but a subscription is needed to enable many features of the mesh system."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/group-plans-one-week-playstation-blackout-to-protest-sonys-plan-to-end-physical-game-production-calls-for-players-to-turn-off-their-consoles-or-log-out-of-psn-from-august-23-to-30",
    "domain": "AI 算力 / 半导体",
    "title": "Group plans one-week PlayStation blackout to protest Sony’s plan to end physical game production — calls for players to turn off their consoles or log out of PSN from August 23 to 30",
    "url": "https://www.tomshardware.com/video-games/playstation/group-plans-one-week-playstation-blackout-to-protest-sonys-plan-to-end-physical-game-production-calls-for-players-to-turn-off-their-consoles-or-log-out-of-psn-from-august-23-to-30",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T12:00:00+00:00",
    "summary": "A game preservation group is asking PlayStation users to stay away from their consoles for a week in protest of Sony's plan to axe physical game disc production. However, others say this is too soft, "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/humanoid-robots-shatter-usain-bolts-100m-record-hits-23-8-mph-before-crashing-into-foam-pads-video-shows-tiangong-ultra-logging-9-39-second-sprint-before-colliding-with-padded-wall",
    "domain": "AI 算力 / 半导体",
    "title": "Humanoid robots shatter Usain Bolt's 100m record, hits 23.8 mph before crashing into foam pads — video shows Tiangong Ultra logging 9.39-second sprint before colliding with padded wall",
    "url": "https://www.tomshardware.com/tech-industry/robotics/humanoid-robots-shatter-usain-bolts-100m-record-hits-23-8-mph-before-crashing-into-foam-pads-video-shows-tiangong-ultra-logging-9-39-second-sprint-before-colliding-with-padded-wall",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T11:45:00+00:00",
    "summary": "Two robots at the 2026 World Humanoid Robot Games in Beijing beat Usain Bolt's 2009 100-meter dash world record. The Tiangong Ultra set a record of 9.39 seconds, while the Honor Lightning achieved a 9"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/startup-to-use-drones-to-keep-clouds-away-from-solar-farms-our-ultimate-goal-is-to-reduce-the-intensity-of-severe-storms-and-hurricanes-chemical-free-tech-promises-up-to-30-percent-power-boost-for-usd30-to-usd60-an-hour",
    "domain": "AI 算力 / 半导体",
    "title": "Startup to use drones to keep clouds away from solar farms, 'Our ultimate goal is to reduce the intensity of severe storms and hurricanes' — chemical-free tech promises up to 30% power boost for $30 t",
    "url": "https://www.tomshardware.com/tech-industry/drones/startup-to-use-drones-to-keep-clouds-away-from-solar-farms-our-ultimate-goal-is-to-reduce-the-intensity-of-severe-storms-and-hurricanes-chemical-free-tech-promises-up-to-30-percent-power-boost-for-usd30-to-usd60-an-hour",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T11:30:00+00:00",
    "summary": "Meteoric plans to deploy drones and use mechanical action to dissipate low and mid-altitude clouds covering solar power plants. The startup says that it already has a working prototype that cut artifi"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-strix-xg32uqwms-32-inch-4k-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Strix XG32UQWMS 4K OLED gaming monitor review: Fast and flexible performance",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-strix-xg32uqwms-32-inch-4k-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T11:05:00+00:00",
    "summary": "Asus’ ROG Strix XG32UQWMS delivers speed and flexibility with a 32-inch 4K Tandem OLED panel, dual-refresh modes, 240 Hz and 480 Hz in FHD resolution, plus wide-gamut color, HDR 500 True Black and Ada"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/lucky-shopper-finds-pny-rtx-5080-for-just-usd702-at-walmart-saves-almost-usd800-compared-to-current-retail-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Lucky shopper finds RTX 5080 for just $702 at Walmart — saves almost $800 compared to current retail prices",
    "url": "https://www.tomshardware.com/pc-components/gpus/lucky-shopper-finds-pny-rtx-5080-for-just-usd702-at-walmart-saves-almost-usd800-compared-to-current-retail-prices",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T11:00:00+00:00",
    "summary": "Walmart’s clearance aisle delivers another remarkable GPU bargain, with a shopper finding a PNY RTX 5080 for nearly half its current retail price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/death-threats-hit-data-center-opponents-as-towns-cancel-votes-and-close-public-comment",
    "domain": "AI 算力 / 半导体",
    "title": "Officials nationwide face death threats and gunfire over AI data center projects — More than 500 towns restrict builds as councils shutter public comment",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/death-threats-hit-data-center-opponents-as-towns-cancel-votes-and-close-public-comment",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T10:30:00+00:00",
    "summary": "Recent data published in the Soufan Center's July IntelBrief found hundreds of posts with threat language between July 2025 and July 2026, and a volume surge beginning in April."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/enthusiast-mods-gtx-1080-ti-with-a-dual-tower-cpu-cooler-sees-up-to-32-c-reduction-in-temps-mod-yields-30w-power-savings-and-9-percent-higher-fps",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast mods GTX 1080 Ti with a dual-tower CPU cooler, sees up to 32°C reduction in temps — Mod yields 30W power savings and 9% higher FPS",
    "url": "https://www.tomshardware.com/pc-components/gpus/enthusiast-mods-gtx-1080-ti-with-a-dual-tower-cpu-cooler-sees-up-to-32-c-reduction-in-temps-mod-yields-30w-power-savings-and-9-percent-higher-fps",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T10:00:00+00:00",
    "summary": "What if you could have twice the CPU cooler in your computer? If that's a question that piques your interest, then TrashBench has answered your curiosity in droves with an experiment that ended up wor"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/maxell-partners-with-disk-union-to-release-ud-60u-special-edition-cassettes-black-and-red-ud-tapes-could-be-ideal-for-use-in-your-c64-datassette",
    "domain": "AI 算力 / 半导体",
    "title": "Maxell brings back classic 1970s cassette tapes — 1970s ferric formula is custom-made for vintage PC data drives",
    "url": "https://www.tomshardware.com/pc-components/storage/maxell-partners-with-disk-union-to-release-ud-60u-special-edition-cassettes-black-and-red-ud-tapes-could-be-ideal-for-use-in-your-c64-datassette",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T09:30:00+00:00",
    "summary": "Maxell and Disk Union collaborate to release special edition UD-60U cassette tapes in Japan."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/webcams/the-worlds-first-webcam-was-switched-off-25-years-ago-today-128x128-grayscale-feed-predated-the-world-wide-web-to-monitor-a-cambridge-coffee-pot",
    "domain": "AI 算力 / 半导体",
    "title": "The world's first webcam was switched off 25 years ago today — 128x128 grayscale feed predated the World Wide Web to monitor a Cambridge coffee pot",
    "url": "https://www.tomshardware.com/peripherals/webcams/the-worlds-first-webcam-was-switched-off-25-years-ago-today-128x128-grayscale-feed-predated-the-world-wide-web-to-monitor-a-cambridge-coffee-pot",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T09:00:00+00:00",
    "summary": "It has been a quarter century since the world’s first webcam was turned off for good. The Trojan Room Coffee Pot was retired on Wednesday, August 22, 2001, after 10 years of service at Cambridge Unive"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-blames-rgb-peripherals-for-crashing-windows-11-rgb-software-is-causing-blue-screens-crashes-and-game-freezes",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft blames RGB peripherals for crashing Windows 11 — RGB software is causing blue screens, crashes, and game freezes",
    "url": "https://www.tomshardware.com/software/windows/microsoft-blames-rgb-peripherals-for-crashing-windows-11-rgb-software-is-causing-blue-screens-crashes-and-game-freezes",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T16:21:34+00:00",
    "summary": "RGB software is reportedly wreaking havoc on Windows PCs. The drivers used by these applications can trip up anti-cheat software, causing your games or entire system to crash. For now, the only soluti"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/25-years-after-the-death-of-3dfx-the-voodoo-3-gets-a-linux-driver-update-classic-voodoo-gpus-can-now-boot-without-a-pc-bios",
    "domain": "AI 算力 / 半导体",
    "title": "25 years after the death of 3dfx, the Voodoo 3 gets a Linux driver update — classic Voodoo GPUs can now boot without a PC BIOS",
    "url": "https://www.tomshardware.com/software/linux/25-years-after-the-death-of-3dfx-the-voodoo-3-gets-a-linux-driver-update-classic-voodoo-gpus-can-now-boot-without-a-pc-bios",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T15:48:10+00:00",
    "summary": "It's been a quarter-century since the firm folded, but the graphics chips still have utility in esoteric use cases."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/case-fans/snap-on-lcd-brings-mini-displays-to-any-120mm-pc-fan-thermalrights-fan-frame-vision-1-lets-you-display-information-and-custom-themes-on-your-case-fans",
    "domain": "AI 算力 / 半导体",
    "title": "Snap-on LCD brings mini displays to any 120mm PC fan — Thermalright's Fan Frame Vision-1 lets you display information and custom themes on your case fans",
    "url": "https://www.tomshardware.com/pc-components/case-fans/snap-on-lcd-brings-mini-displays-to-any-120mm-pc-fan-thermalrights-fan-frame-vision-1-lets-you-display-information-and-custom-themes-on-your-case-fans",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:49:09+00:00",
    "summary": "The Thermalright Fan Frame Vision-1 is a clip-on 3.69-inch screen that snaps directly in front of your PC case fans. These accessories let you display temperature, fan speed, and other information acr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/ascii-cyberpunk-city-prototype-runs-on-rust-webassembly-engine-and-webgl-shaders",
    "domain": "AI 算力 / 半导体",
    "title": "Walk through a 3D cyberpunk city built purely from ASCII characters — a text-based metropolis runs on a 283KB Rust WebAssembly engine feeding a WebGL renderer",
    "url": "https://www.tomshardware.com/tech-industry/ascii-cyberpunk-city-prototype-runs-on-rust-webassembly-engine-and-webgl-shaders",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:37:14+00:00",
    "summary": "Solo developer Grow Now! Games has put a playable browser build of its walkable ASCII cyberpunk city online, powered by a 283KB Rust WebAssembly engine and rendered in WebGL."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/logitech-faces-lawsuit-for-withholding-usd61m-in-tariff-refunds-from-customers-lawsuit-claims-company-extracted-up-to-usd97m-from-consumers-in-2026-through-tariff-justified-price-increases",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech faces lawsuit for withholding $61M in tariff refunds from customers — lawsuit claims company extracted up to $97M from consumers in 2026 through tariff-justified price increases",
    "url": "https://www.tomshardware.com/peripherals/logitech-faces-lawsuit-for-withholding-usd61m-in-tariff-refunds-from-customers-lawsuit-claims-company-extracted-up-to-usd97m-from-consumers-in-2026-through-tariff-justified-price-increases",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:13:50+00:00",
    "summary": "Consumers who bought products from Logitech after it increased its prices due to tariffs still haven't received their refunds, even after the U.S. government returned $61 million to the company. Now t"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/razer-hyperflux-v2-review-the-best-wireless-charging-mat-for-razer-mice",
    "domain": "AI 算力 / 半导体",
    "title": "Razer HyperFlux V2 Review: The best wireless charging mat for Razer mice",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/razer-hyperflux-v2-review-the-best-wireless-charging-mat-for-razer-mice",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:08:39+00:00",
    "summary": "Razer's HyperFlux V2 is a wireless charging mouse pad that works with current mice from Razer's Basilisk, Cobra, and Naga lines."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/us-authorities-say-siemens-controllers-used-for-water-and-other-infrastructure-are-being-targeted-by-hackers-agencies-claim-threat-actors-use-ai-tools-to-generate-exploitation-scripts",
    "domain": "AI 算力 / 半导体",
    "title": "US authorities say Siemens controllers used for water and other infrastructure are being targeted by hackers — agencies claim threat actors use AI tools to generate exploitation scripts",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/us-authorities-say-siemens-controllers-used-for-water-and-other-infrastructure-are-being-targeted-by-hackers-agencies-claim-threat-actors-use-ai-tools-to-generate-exploitation-scripts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:57:17+00:00",
    "summary": "Siemens S7 PLCs, commonly used in critical infrastructure, are reportedly being targeted by hackers and could potentially lead to disruption of industrial processes, safety incidents, downtime or equi"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/save-usd532-on-a-480-hz-oled-gaming-monitor-amazon-drops-a-massive-53-percent-discount-on-the-lg-ultragear-27gx790a-b",
    "domain": "AI 算力 / 半导体",
    "title": "Save $532 on a 480 Hz OLED gaming monitor — Amazon drops a massive 53% discount on the LG UltraGear 27GX790A-B",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/save-usd532-on-a-480-hz-oled-gaming-monitor-amazon-drops-a-massive-53-percent-discount-on-the-lg-ultragear-27gx790a-b",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:50:07+00:00",
    "summary": "The LG UltraGear 27GX790A-B packs a 27-inch 1440p WOLED panel with a 480 Hz refresh rate, 0.03ms response time, and support for DisplayHDR True Black 400."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-22-2026-foundries-supercomputers-china-and-how-to-not-overpay-on-a-motherboard",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: August 22, 2026 — foundries, supercomputers, China, and how to not overpay on a motherboard",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-22-2026-foundries-supercomputers-china-and-how-to-not-overpay-on-a-motherboard",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:00:00+00:00",
    "summary": "We recap this week's Tom's Hardware Premium articles, including our latest advice on your next motherboard purchase, a look inside Samsung's Fab roadmaps, and much more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/desktop-cpu-shipments-crater-20-percent-amid-high-component-costs-but-amd-gains-record-share-despite-ugly-desktop-processor-market-intel-floods-laptop-market-with-millions-of-cpus-but-amd-still-sets-all-time-share-records",
    "domain": "AI 算力 / 半导体",
    "title": "Desktop CPU shipments crater 20% amid high component costs, but AMD gains record share despite 'ugly' desktop processor market — Intel floods laptop market with millions of CPUs, but AMD still sets al",
    "url": "https://www.tomshardware.com/pc-components/cpus/desktop-cpu-shipments-crater-20-percent-amid-high-component-costs-but-amd-gains-record-share-despite-ugly-desktop-processor-market-intel-floods-laptop-market-with-millions-of-cpus-but-amd-still-sets-all-time-share-records",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T12:30:00+00:00",
    "summary": "As Intel boosts output of data center and notebook CPUs, AMD manages to outgrow it and keep capturing market share from its arch-rival."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage-unit-auction-winner-finds-retro-pentium-4-pc-with-a-see-through-uv-reactive-psu-y2k-time-capsule-discovered-among-100-laptops-and-hundreds-of-ram-sticks",
    "domain": "AI 算力 / 半导体",
    "title": "Storage unit auction winner finds retro Pentium 4 PC with a see-through, UV-reactive PSU — Y2K time capsule discovered among 100 laptops and hundreds of RAM sticks",
    "url": "https://www.tomshardware.com/pc-components/storage-unit-auction-winner-finds-retro-pentium-4-pc-with-a-see-through-uv-reactive-psu-y2k-time-capsule-discovered-among-100-laptops-and-hundreds-of-ram-sticks",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T12:00:00+00:00",
    "summary": "This vintage PC build looks like it came straight out of the 90s with a bold, in-your-face look that make sure you can't mistake it for anything but a gamer's lifeline. What you're looking at is an Ap"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/gigabyte-rtx-3070-owner-discovers-protective-film-on-vrm-thermal-pads-after-nearly-five-years-claims-removal-and-repasting-dropped-gpu-hotspot-temperatures-by-30-c",
    "domain": "AI 算力 / 半导体",
    "title": "Gamer uncovers factory plastic left on RTX 3070 VRM pads after five years, causing overheating — claims removal and repasting dropped GPU hotspot temperatures by 30°C",
    "url": "https://www.tomshardware.com/pc-components/gpus/gigabyte-rtx-3070-owner-discovers-protective-film-on-vrm-thermal-pads-after-nearly-five-years-claims-removal-and-repasting-dropped-gpu-hotspot-temperatures-by-30-c",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:30:00+00:00",
    "summary": "A Gigabyte RTX 3070 owner discovered protective films covering its VRM thermal pads, after nearly five years of use potentially causing excessive temperatures and frequent black screens."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/asrock-steel-legend-sl-1200p-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock Steel Legend SL-1200P power supply review: A winning combination of genuine Platinum efficiency and a stand-out design",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/asrock-steel-legend-sl-1200p-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:05:00+00:00",
    "summary": "The ASRock Steel Legend SL-1200P is a visually distinct, technically capable 1200W unit with genuine Platinum efficiency, dual 12V-2x6 outputs, and a few thoughtful engineering touches that set it apa"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/take-two-subpoenas-microsoft-for-windows-device-ids-of-everyone-in-three-discord-servers-in-gta-6-leak-hunt",
    "domain": "AI 算力 / 半导体",
    "title": "GTA 6 leaks prompt Take-Two to subpoena Microsoft for Windows device IDs of everyone in three Discord servers — daily gameplay leaks shatter cloud of secrecy around the much-hyped game",
    "url": "https://www.tomshardware.com/video-games/console-gaming/take-two-subpoenas-microsoft-for-windows-device-ids-of-everyone-in-three-discord-servers-in-gta-6-leak-hunt",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:00:00+00:00",
    "summary": "Take-Two Interactive filed two DMCA subpoenas demanding that Microsoft and Discord identify the person or people behind the \"CyberLeek\" persona."
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
    "id": "hn:49393647",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia just showed that the harness, not the AI model, is now the real hero",
    "url": "https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/",
    "source": "dthread3",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-21T20:52:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49388268",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO achieves 100% in ARC-AGI-3",
    "url": "https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/",
    "source": "rochansinha",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-21T14:05:37+00:00",
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
    "id": "rss:https://www.eetimes.com/chinas-nand-specialist-ymtc-moves-closer-to-ipo/",
    "domain": "AI 算力 / 半导体",
    "title": "China’s NAND Specialist YMTC Moves Closer to IPO",
    "url": "https://www.eetimes.com/chinas-nand-specialist-ymtc-moves-closer-to-ipo/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T18:00:00+00:00",
    "summary": "YMTC must raise capital to explore demand for AI-driven memory while balancing domestic and overseas markets. The post China’s NAND Specialist YMTC Moves Closer to IPO appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/the-human-brain-versus-ai-similar-results-very-different-machines/",
    "domain": "AI 算力 / 半导体",
    "title": "The Human Brain Versus AI: Similar Results, Very Different Machines",
    "url": "https://www.eetimes.com/the-human-brain-versus-ai-similar-results-very-different-machines/",
    "source": "Lauro Rizzatti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T07:43:42+00:00",
    "summary": "Contrast 20 watts with a megawatt: The brain and the LLM aren’t in the same race. The post The Human Brain Versus AI: Similar Results, Very Different Machines appeared first on EE Times."
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
    "id": "hn:49325115",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Uses Old Fabs to Make New Chips [video]",
    "url": "https://www.youtube.com/watch?v=cDxVYQrxeiQ",
    "source": "eig",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-08-17T00:07:42+00:00",
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
    "id": "rss:https://www.theverge.com/23987993/gta-6-news-trailers-rockstar-games",
    "domain": "大厂 AI 动态",
    "title": "GTA VI: all the news on Rockstar’s next entry in the Grand Theft Auto series",
    "url": "https://www.theverge.com/23987993/gta-6-news-trailers-rockstar-games",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T19:14:37+00:00",
    "summary": "It’s been over a decade and two console generations since GTA V came out, and its sequel is still a work in progress. GTA VI has faced multiple delays, with developer Rockstar Games bumping back its p"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/983177/jane-schoenbrun-were-all-going-to-the-worlds-fair-horror-movie-review",
    "domain": "大厂 AI 动态",
    "title": "We’re All Going to the World’s Fair is an intimate coming-of-age horror film",
    "url": "https://www.theverge.com/entertainment/983177/jane-schoenbrun-were-all-going-to-the-worlds-fair-horror-movie-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T15:00:00+00:00",
    "summary": "Jane Schoenbrun's latest film, Teenage Sex and Death at Camp Miasma, is making a splash in theaters right now. So it seems like the perfect time to revisit their first film, We're All Going to the Wor"
  },
  {
    "id": "rss:https://www.theverge.com/column/983410/grand-theft-auto-vi-exists-in-its-own-universe",
    "domain": "大厂 AI 动态",
    "title": "Grand Theft Auto VI exists in its own universe",
    "url": "https://www.theverge.com/column/983410/grand-theft-auto-vi-exists-in-its-own-universe",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on GTA VI and the state of the video game industry, follow Andrew Webster. The Stepback arrive"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/983322/musical-spirograph-generative-composition",
    "domain": "大厂 AI 动态",
    "title": "Doodle generative compositions in your browser with Musical Spirograph",
    "url": "https://www.theverge.com/entertainment/983322/musical-spirograph-generative-composition",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T17:00:00+00:00",
    "summary": "I remember having a Spirograph as a kid and being obsessed with it. Its geometric patterns are hypnotic and gorgeous. I also love generative music composition. So bringing those two things together in"
  },
  {
    "id": "rss:https://www.theverge.com/report/980452/w-kamau-bell-whos-with-me-comedy-interview",
    "domain": "大厂 AI 动态",
    "title": "W. Kamau Bell has the most practical ‘most indispensable tool’",
    "url": "https://www.theverge.com/report/980452/w-kamau-bell-whos-with-me-comedy-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T15:00:00+00:00",
    "summary": "W. Kamau Bell is one of those people who has always just seemed to be there. From Totally Biased, to Politically Re-Active, United Shades of America, and We Need to Talk About Cosby, his blend of come"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983598/amazon-price-increase-echo-kindle-fire-tv",
    "domain": "大厂 AI 动态",
    "title": "Amazon just hiked the prices for Echo, Fire TV, and Kindle products by up to 60 percent",
    "url": "https://www.theverge.com/tech/983598/amazon-price-increase-echo-kindle-fire-tv",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:41:01+00:00",
    "summary": "Citing \"significant increases in memory and storage component costs,\" Amazon has raised prices on Echos, Kindles, Fire TVs, and Eeros by up to 60 percent, as first reported by Fortune. The cheapest pr"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983554/hp-omnibook-3-16-snapdragon-laptop-review",
    "domain": "大厂 AI 动态",
    "title": "An okay laptop with 16GB of RAM is better than a nice laptop with 8GB, and this $520 HP OmniBook proves it",
    "url": "https://www.theverge.com/tech/983554/hp-omnibook-3-16-snapdragon-laptop-review",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T13:00:00+00:00",
    "summary": "Laptop prices are out of whack. $500 used to get you a tolerable laptop, and $900 got you a really good one. They often had similar CPU, RAM, and storage options because that stuff was comparatively c"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983375/fairphone-6-plus-framework-12-laptop-mutiny-mortal-shell-2",
    "domain": "大厂 AI 动态",
    "title": "Two great new repairable gadgets",
    "url": "https://www.theverge.com/tech/983375/fairphone-6-plus-framework-12-laptop-mutiny-mortal-shell-2",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 141, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, I'm newish here too, and also you can read all the old editions at th"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/23/whos-behind-the-new-stealth-model-ox-alpha/",
    "domain": "大厂 AI 动态",
    "title": "Who’s behind the new ‘stealth model’ Ox Alpha?",
    "url": "https://techcrunch.com/2026/08/23/whos-behind-the-new-stealth-model-ox-alpha/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T20:01:36+00:00",
    "summary": "A mysterious new AI model called Ox Alpha has driven certain corners of the internet into a frenzy of speculation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/23/uber-faces-fine-of-nearly-1b-over-automated-driver-suspensions/",
    "domain": "大厂 AI 动态",
    "title": "Uber faces fine of nearly $1B over automated driver suspensions",
    "url": "https://techcrunch.com/2026/08/23/uber-faces-fine-of-nearly-1b-over-automated-driver-suspensions/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T19:30:00+00:00",
    "summary": "The Dutch Data Protection Authority is fining Uber €825 million in the second largest penalty issued under Europe’s GDPR."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/23/linkdazes-smart-calendar-is-built-to-run-a-household-not-just-track-a-schedule/",
    "domain": "大厂 AI 动态",
    "title": "Linkdaze’s smart calendar is built to run a household, not just track a schedule",
    "url": "https://techcrunch.com/2026/08/23/linkdazes-smart-calendar-is-built-to-run-a-household-not-just-track-a-schedule/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T19:14:08+00:00",
    "summary": "Linkdaze's smart digital calendar stands out for not putting its features behind a paywall, including an AI meal planner tool."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/23/techcrunch-mobility-the-custom-chip-driving-waymos-robotaxi-ambitions/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: The custom chip driving Waymo’s robotaxi ambitions",
    "url": "https://techcrunch.com/2026/08/23/techcrunch-mobility-the-custom-chip-driving-waymos-robotaxi-ambitions/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T16:03:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility — your central hub for news and insights on the future of transportation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/23/flock-ceo-calls-for-compromise-as-surveillance-company-faces-growing-backlash/",
    "domain": "大厂 AI 动态",
    "title": "Flock CEO calls for ‘compromise’ as surveillance company faces growing backlash",
    "url": "https://techcrunch.com/2026/08/23/flock-ceo-calls-for-compromise-as-surveillance-company-faces-growing-backlash/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T15:30:00+00:00",
    "summary": "Flock Safety faces a growing public outcry over concerns that its surveillance technology could be misused."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/",
    "domain": "大厂 AI 动态",
    "title": "Is it legal to train AI models on copyrighted books? It’s complicated",
    "url": "https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T15:00:00+00:00",
    "summary": "Most published authors have, without their knowledge or consent, contributed to the development of the same AI tools that threaten to undermine their livelihoods. That seems illegal, right?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/two-years-after-launch-walmarts-flipkart-is-closing-in-on-indias-quick-commerce-leaders/",
    "domain": "大厂 AI 动态",
    "title": "Two years after launch, Walmart’s Flipkart is closing in on India’s quick-commerce leaders",
    "url": "https://techcrunch.com/2026/08/22/two-years-after-launch-walmarts-flipkart-is-closing-in-on-indias-quick-commerce-leaders/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T03:00:00+00:00",
    "summary": "Flipkart's quick-commerce venture is delivering 1.1 million to 1.2 million orders a day, nearly triple its November volume."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/harvards-699-startup-bootcamp-offers-ai-avatars-of-its-instructors/",
    "domain": "大厂 AI 动态",
    "title": "Harvard’s $699 startup bootcamp offers AI avatars of its instructors",
    "url": "https://techcrunch.com/2026/08/22/harvards-699-startup-bootcamp-offers-ai-avatars-of-its-instructors/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T21:46:56+00:00",
    "summary": "In the HBS Foundry program, AI avatars provide feedback during practice pitches and board meetings."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/will-the-dojs-investigation-into-a16z-spook-other-vcs/",
    "domain": "大厂 AI 动态",
    "title": "Will the DOJ’s investigation into a16z spook other VCs?",
    "url": "https://techcrunch.com/2026/08/22/will-the-dojs-investigation-into-a16z-spook-other-vcs/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T20:24:20+00:00",
    "summary": "On the latest episode of Equity, we wonder why the DOJ is investigating startup board seats."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/",
    "domain": "大厂 AI 动态",
    "title": "Inherent, founded by DeepMind alumni, says its AI ‘teammate’ just outperformed Anthropic and OpenAI at replicating research",
    "url": "https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T19:00:00+00:00",
    "summary": "Built by DeepMind alumni, British AI lab Inherent released Faraday, an AI agent whose ability to replicate scientific papers could be a stepping stone for innovation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says California should strengthen its AI safety bill",
    "url": "https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T16:30:34+00:00",
    "summary": "OpenAI is calling for California to strengthen SB 53, an AI safety bill that the company previously opposed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/",
    "domain": "大厂 AI 动态",
    "title": "Frontier AI labs still won’t say how they’d contain a rogue model",
    "url": "https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T16:00:00+00:00",
    "summary": "A new study finds leading AI labs have few publicly documented plans for containing rogue models, raising questions about preparedness as AI systems increasingly demonstrate unexpected and potentially"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/us-battery-startups-have-found-a-lifeline-in-defense/",
    "domain": "大厂 AI 动态",
    "title": "US battery startups have found a lifeline in defense",
    "url": "https://techcrunch.com/2026/08/22/us-battery-startups-have-found-a-lifeline-in-defense/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T15:20:00+00:00",
    "summary": "U.S. battery startups pulled in $500 million in grants from the Department of Energy, throwing a lifeline to an industry that was on the ropes after EV incentives were slashed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/22/pixel-11-pro-xl-review-snappier-cameras-cant-hide-an-iterative-upgrade/",
    "domain": "大厂 AI 动态",
    "title": "Pixel 11 Pro XL review: Snappier cameras can’t hide an iterative upgrade",
    "url": "https://techcrunch.com/2026/08/22/pixel-11-pro-xl-review-snappier-cameras-cant-hide-an-iterative-upgrade/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T14:00:00+00:00",
    "summary": "Google’s Pixel 11 Pro XL brings snappier cameras and genuinely useful AI features like Rambler, but its iterative upgrades may not be enough to tempt recent Pixel owners."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/due-to-need-for-absolute-success-china-delays-critical-moon-launch-to-2027/",
    "domain": "大厂 AI 动态",
    "title": "Due to need for 'absolute success,' China delays critical Moon launch to 2027",
    "url": "https://arstechnica.com/space/2026/08/due-to-need-for-absolute-success-china-delays-critical-moon-launch-to-2027/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T14:30:16+00:00",
    "summary": "\"The Chang’e 7 mission does not meet the conditions for launch.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/volcanoes-that-made-history/",
    "domain": "大厂 AI 动态",
    "title": "Volcanoes that made history",
    "url": "https://arstechnica.com/science/2026/08/volcanoes-that-made-history/",
    "source": "Alexandra Witze, Knowable Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T11:02:54+00:00",
    "summary": "Enormous eruptions altered Earth’s climate and societies all over the globe."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/memories-stick-around-even-after-half-the-synapses-are-gone/",
    "domain": "大厂 AI 动态",
    "title": "Putting mice into hibernation causes a major loss of synapses",
    "url": "https://arstechnica.com/science/2026/08/memories-stick-around-even-after-half-the-synapses-are-gone/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:22:32+00:00",
    "summary": "Hibernation cuts down on synapses, but mice seem to retain memories anyway."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/dismantling-the-roadless-rule-threatens-to-disrupt-wildlife-and-water-in-us/",
    "domain": "大厂 AI 动态",
    "title": "Dismantling the Roadless Rule threatens to disrupt wildlife and water in US",
    "url": "https://arstechnica.com/science/2026/08/dismantling-the-roadless-rule-threatens-to-disrupt-wildlife-and-water-in-us/",
    "source": "Mariah Meek and Travis Belote, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T11:08:53+00:00",
    "summary": "Lands free of roads are under threat from the Trump administration’s proposed rollback."
  },
  {
    "id": "rss:https://www.producthunt.com/products/openlogi",
    "domain": "大厂 AI 动态",
    "title": "OpenLogi",
    "url": "https://www.producthunt.com/products/openlogi",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T17:13:58+00:00",
    "summary": "A local-first alternative to Logitech Options+ Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/113767",
    "domain": "大厂 AI 动态",
    "title": "派早报：九家车企召回近 430 万辆不易识别应急拉手汽车",
    "url": "https://sspai.com/post/113767",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T23:13:55+00:00",
    "summary": "九家车企召回近 430 万辆不易识别应急拉手汽车英伟达达成 70 亿美元合作，研发顶级开放权重模型高院发布著作权新司法解释，网络转载不允许先转后付买家利用仅退款漏洞倒卖 13 万元火鸡面被刑拘国际加紧制定统一月球时间个人消费贷贴息政策扩展覆盖买车、装修等看看就行的小道消息少数派的近期动态你可能错过的好文章查看全文"
  },
  {
    "id": "rss:https://sspai.com/prime/story/surface-pro-7-linux-ai-dashboard",
    "domain": "大厂 AI 动态",
    "title": "AI 时代的 Surface Pro 7 改造指南：看板、轻量工作站与 Linux 笔记本",
    "url": "https://sspai.com/prime/story/surface-pro-7-linux-ai-dashboard",
    "source": "neyham",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T07:25:29+00:00",
    "summary": "手头这台闲置的SurfacePro7在桌角放了挺长一段时间。当年买它看重的是二合一的便携形态，但放在Windows11下只要长时间亮屏就一定会过热、偶尔跳屏，基本处于不可用的状态。直到前阵子在网上看到 ...查看全文本文为会员文章，出自《单篇文章》，订阅后可阅读全文。"
  },
  {
    "id": "rss:https://sspai.com/post/113002",
    "domain": "大厂 AI 动态",
    "title": "让 PC 与 HomePod 互联：音频串流工具 WinAirCast",
    "url": "https://sspai.com/post/113002",
    "source": "isayyeah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-23T03:00:00+00:00",
    "summary": "打破生态壁垒，让好的设备发挥出它应有的价值，这就是 WinAirCast 的初衷。我们希望为 Windows 用户提供一款稳定、低延迟且现代化的音频串流工具。查看全文"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983500/hoverair-versa-halted-us-fcc-drone-ban-indiegogo",
    "domain": "大厂 AI 动态",
    "title": "HoverAir’s transforming modular drone has already been halted in the US",
    "url": "https://www.theverge.com/tech/983500/hoverair-versa-halted-us-fcc-drone-ban-indiegogo",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:14:11+00:00",
    "summary": "I am so sorry, fellow US gadget fans: the FCC's drone ban appears to have struck again. The HoverAir Versa - a baby steadycam with snap-on propeller wings that transform it into a drone - has already "
  },
  {
    "id": "rss:https://www.theverge.com/tech/983531/tiktok-settle-doj-lawsuit-coppa",
    "domain": "大厂 AI 动态",
    "title": "TikTok will pay $400 million to settle DOJ child privacy lawsuit",
    "url": "https://www.theverge.com/tech/983531/tiktok-settle-doj-lawsuit-coppa",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:13:34+00:00",
    "summary": "The US Department of Justice announced on Friday that TikTok will pay $400 million to settle a lawsuit filed in 2024 over allegedly violating the Children's Online Privacy Protection Act (COPPA). In t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/",
    "domain": "大厂 AI 动态",
    "title": "Michael Polansky is training an AI model on skin that’s still alive",
    "url": "https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T01:31:04+00:00",
    "summary": "Michael Polansky — better known publicly as Lady Gaga's partner and a former top deputy to Sean Parker — has quietly spent years building an AI-driven startup that keeps living human skin tissue alive"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/japanese-space-tech-startup-letara-expands-beyond-satellite-thrusters-with-16m/",
    "domain": "大厂 AI 动态",
    "title": "Japanese space tech startup Letara expands beyond satellite thrusters with $16M",
    "url": "https://techcrunch.com/2026/08/21/japanese-space-tech-startup-letara-expands-beyond-satellite-thrusters-with-16m/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T01:03:06+00:00",
    "summary": "Japanese space startup Letara is betting its hybrid rocket technology can move beyond small satellite thrusters into a broader market for space, defense and security, after raising ¥2.6 billion ($16 m"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/anthropics-opus-4-6-is-a-smut-machine/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Opus 4.6 is a smut-machine",
    "url": "https://techcrunch.com/2026/08/21/anthropics-opus-4-6-is-a-smut-machine/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:07:25+00:00",
    "summary": "Anthropic forbids its Claude models from generating sexually explicit content. But a series of tests conducted by TechCrunch found that it didn't take much to get past the restriction."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/nvidia-partners-with-data-center-developer-cloverleaf/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia partners with data center developer Cloverleaf",
    "url": "https://techcrunch.com/2026/08/21/nvidia-partners-with-data-center-developer-cloverleaf/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:37:38+00:00",
    "summary": "Nvidia continues to pour money into data center development — just as AI data centers bring lots of money into Nvidia."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/how-ai-accounting-startup-rillet-raised-100m-and-became-a-unicorn-in-48-hours/",
    "domain": "大厂 AI 动态",
    "title": "How AI accounting startup Rillet raised $100M and became a unicorn in 48 hours",
    "url": "https://techcrunch.com/2026/08/21/how-ai-accounting-startup-rillet-raised-100m-and-became-a-unicorn-in-48-hours/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:10:01+00:00",
    "summary": "Rillet CEO Nicolas Kopp shared growth numbers at a board meeting and set off a fundraising frenzy from Iconiq, Sequoia and others. Without even trying."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/apple-is-reportedly-cutting-hundreds-of-jobs-from-siri-vision-pro-teams/",
    "domain": "大厂 AI 动态",
    "title": "Apple is reportedly cutting hundreds of jobs from Siri, Vision Pro teams",
    "url": "https://techcrunch.com/2026/08/21/apple-is-reportedly-cutting-hundreds-of-jobs-from-siri-vision-pro-teams/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:58:07+00:00",
    "summary": "Apple has admitted that some roles are being impacted as it shifts its focus away from certain initiatives."
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
    "id": "hn:49397022",
    "domain": "股票",
    "title": "Ask HN: What is the evidence for a stock market bubble in AI?",
    "url": "https://news.ycombinator.com/item?id=49397022",
    "source": "roschdal",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-22T06:07:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49396088",
    "domain": "股票",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
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
    "id": "wscn:3780116",
    "domain": "股票",
    "title": "AH股齐跌：创业板跌超3%，煤炭爆发，算力硬件下挫，恒科指跌逾3%，阿里大跌近10%",
    "url": "https://wallstreetcn.com/articles/3780116",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:55:19+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超4300股飘绿，上午半天成交1.38万亿。沪深两市半日成交额1.37万亿，较上个交易日放量近1200亿。板块方面，算力硬件产业链回调，CPO、PCB、服务器方向领跌；医药生物股跌幅居前，CRO方向下挫明显。煤炭、银行、黄金、种业板块逆势走强。"
  },
  {
    "id": "wscn:3780134",
    "domain": "股票",
    "title": "市值蒸发1900亿，宇树IPO只风光了半天？",
    "url": "https://wallstreetcn.com/articles/3780134",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:48:37+00:00",
    "summary": "宇树科技上市首日开盘暴涨629%，市值一度冲上4400亿元，随后四个交易日蒸发逾1900亿。一位买在800元的投资人成了朋友圈\"接盘侠\"，创始人王兴兴敲钟全程面无表情。繁华背后，73%的人形机器人收入仍依赖科研教育采购，真正的工厂量产尚未到来。"
  },
  {
    "id": "wscn:3780123",
    "domain": "股票",
    "title": "高盛大幅上调全球晶圆厂设备支出：存储与先进代工成主引擎",
    "url": "https://wallstreetcn.com/articles/3780123",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:48:30+00:00",
    "summary": "高盛最新报告将2026至2028年全球晶圆厂设备支出预测大幅上调至1500亿、2180亿及2810亿美元，增速预期远超此前判断。台积电N2制程扩产、三星SK Hynix押注HBM4、SpaceX与特斯拉Terafab项目168亿美元承诺，多重引擎共振，半导体资本开支景气周期有望一路延续至2028年。"
  },
  {
    "id": "wscn:3780132",
    "domain": "股票",
    "title": "Lazada回应东南亚电商竞争：将减少低品质商品投入，强化品牌路线",
    "url": "https://wallstreetcn.com/articles/3780132",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:37:31+00:00",
    "summary": "“一键轻出海”"
  },
  {
    "id": "wscn:3780128",
    "domain": "股票",
    "title": "摩根士丹利：美债规模40万亿将给经济“踩下刹车”，但“不会崩盘”，个人和企业负债表仍健康",
    "url": "https://wallstreetcn.com/articles/3780128",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:34:49+00:00",
    "summary": "美国债务突破40万亿美元，摩根士丹利却给出\"不必恐慌\"的判断——企业杠杆率十年持平、居民抵押贷款锁定历史低息、净资产持续改善，构成抵御冲击的三重缓冲。真正的\"断裂点\"不在债务本身，而在债券收益率何时对股票形成实质竞争。盈利增速一旦减速，美股脆弱性将骤然上升。"
  },
  {
    "id": "wscn:3780099",
    "domain": "股票",
    "title": "英伟达涨价15%：再来一次“苹果式”涨价血洗市场，还是硬件链的又一次狂欢？",
    "url": "https://wallstreetcn.com/premium/articles/3780099?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:14:17+00:00",
    "summary": "英伟达部分大客户已被告知2027年初出货的Vera Rubin与Grace Blackwell AI服务器涨价\"超过15%\"。表面看是成本转嫁，实际是AI算力定价权从英伟达单点垄断向\"英伟达×三星/SK海力士/美光\"事实性联合定价的结构性迁移。"
  },
  {
    "id": "wscn:3780126",
    "domain": "股票",
    "title": "欧洲工业空心化加速？大众汽车拟裁员5万人，为史上最大重组计划",
    "url": "https://wallstreetcn.com/articles/3780126",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:10:39+00:00",
    "summary": "大众汽车CEO Oliver Blume宣布，集团正在推进史上最大规模转型计划，拟裁员5万人，相关细节将于本周正式披露。工会领袖Christiane Benner将该计划斥为“强硬挑衅”，称管理层信任已严重受损。野村分析师警告，欧洲工业持续空心化正在催生更深层的政治动荡。"
  },
  {
    "id": "wscn:3780131",
    "domain": "股票",
    "title": "企业AI最后一公里：三路人马在此交锋",
    "url": "https://wallstreetcn.com/articles/3780131",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:09:54+00:00",
    "summary": "寻找自己的位置"
  },
  {
    "id": "wscn:3780129",
    "domain": "股票",
    "title": "国常会定调适度超前，投资天弘通信设备基金争取双轮驱动机会",
    "url": "https://wallstreetcn.com/articles/3780129",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:08:42+00:00",
    "summary": "产业链的扩产动作也在同步跟进。8月22日，长沙长芯微高端光学器件产线正式投产，聚焦高速光模块芯片等前沿产品，应用于光通信、量子通信等领域。易德龙2026年上半年通信设备业务营收2.62亿元，同比增长29.66%，受益于AI服务器、算力基础设施建设浪潮。从运营商投资到光器件扩产，再到设备企业业绩，这条链条的各个环节正在形成相互印证的信号。"
  },
  {
    "id": "wscn:3780127",
    "domain": "股票",
    "title": "科创板大IPO来了！投资天弘中证半导体材料设备主题指数基金捕捉利好机会",
    "url": "https://wallstreetcn.com/articles/3780127",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:06:58+00:00",
    "summary": "这一链条的真实性，正在被多重产业信号交叉确认。SEMI预计2026年全球半导体制造设备销售额将创下1659亿美元的历史新高，同比增长23.2%，增长势头持续至2028年；全球WFE销售额也被上调至1439亿美元，2027、2028年预计分别增长21.8%和14.1%。AI相关投资驱动先进逻辑、存储及先进封装同步扩产，设备需求的上行不是单一来源支撑。"
  },
  {
    "id": "wscn:3780125",
    "domain": "股票",
    "title": "存储芯片项目落地海口，投资天弘科创板芯片设计基金迎产业重估机会",
    "url": "https://wallstreetcn.com/articles/3780125",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T03:03:38+00:00",
    "summary": "过去看存储芯片，市场习惯把它当作周期性大宗商品，价格随供需波动，投资逻辑主要围绕短期涨价周期展开。现在，存储芯片正从周期性商品转变为战略性基础设施，合约模式从年度合约转向3至5年长协，客户预付订金锁定产能，国产存储产业链在政策与需求双重驱动下加速扩张，投资逻辑转向长期成长与自主可控。"
  },
  {
    "id": "wscn:3780121",
    "domain": "股票",
    "title": "三星制定“三阶段HBM路线图”：迈向真正的3D ZHBM，将DRAM直接堆叠在计算芯片上",
    "url": "https://wallstreetcn.com/articles/3780121",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T02:49:31+00:00",
    "summary": "三星在Hot Chips大会上发布三阶段HBM演进路线图，目标直指将DRAM垂直堆叠于计算芯片之上的“zHBM”架构。三星称，zHBM相比HBM4E可实现70%功耗降低、230%带宽提升，并为GPU额外释放100W热功耗余量。"
  },
  {
    "id": "wscn:3780120",
    "domain": "股票",
    "title": "中信证券：人民币定价逻辑重构，6.6-7.0为政策合意区间",
    "url": "https://wallstreetcn.com/articles/3780120",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T02:49:31+00:00",
    "summary": "中信证券认为，本轮人民币升值绝非单纯“低估修复”，而是定价主导因素从“中美利差”向“贸易顺差”的实质切换！外部美元信用担忧提供顺风，内部超7600亿美元待结汇资金成为最强动能。随着汇率逼近企业持汇成本线，结汇意愿的爆发将助推汇率稳步迈入政策合意区间为6.6-7.0，升值方向未变但斜率受管控。"
  },
  {
    "id": "wscn:3780122",
    "domain": "股票",
    "title": "对话付鹏：一场治标不治本的日元汇率保卫战，跳出 “失去的三十年”，日本K型经济已开启新周期？",
    "url": "https://wallstreetcn.com/premium/articles/3780122?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T02:41:05+00:00",
    "summary": "跳出 “失去的三十年”：日元汇率、加息与日股 K 型结构反应了什么？"
  },
  {
    "id": "wscn:3780118",
    "domain": "股票",
    "title": "高盛：AI动能衰退，欧日银行股与黄金股等硬资产成下一轮交易主线",
    "url": "https://wallstreetcn.com/articles/3780118",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T02:31:35+00:00",
    "summary": "AI交易\"躺赢\"时代终结，高盛警告半导体与AI板块动量已从多头转入空头，软件取而代之；2026年动量因子单日5%以上跌幅次数超过过去五年总和。高盛认为，利率红利叠加估值洼地，利好欧日银行股，美国财政部扩大国债回购计划所带来的美元走弱预期，将驱动金矿股的下一轮上涨，并提示被市场严重低估的法国政治尾部风险。"
  },
  {
    "id": "wscn:3780119",
    "domain": "股票",
    "title": "AI开发者平台Hugging Face寻求出售，估值或超130亿美元",
    "url": "https://wallstreetcn.com/articles/3780119",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T02:20:02+00:00",
    "summary": "这一估值较其2023年的最新融资估值45亿美元大幅跃升，涨幅接近三倍。此次出售探索折射出市场对AI生态系统基础设施层的重新定价。继Stripe斥资约80亿美元收购OpenRouter后，市场再度印证：战略买家愿为AI核心平台支付高溢价，即便其并不开发前沿模型。"
  },
  {
    "id": "wscn:3780109",
    "domain": "股票",
    "title": "7月下旬抄底、上周再度转向抛售！对冲基金卖出美股，以“关税战”以来最快的速度",
    "url": "https://wallstreetcn.com/articles/3780109",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T01:48:47+00:00",
    "summary": "在连续数周大举买入后，上周骤然转向，净卖出规模创\"关税日\"以来最大，高盛数据显示净杠杆率大幅下滑3.0个百分点至48.3%，为一年新低。信息技术遭最大规模抛售，公用事业创五年罕见净卖出记录。摩根士丹利证实，这是过去12个月全球股票抛售第二大周。英伟达财报与杰克逊霍尔会议，将成市场下一个关键考验。"
  },
  {
    "id": "wscn:3780114",
    "domain": "股票",
    "title": "股东回报计划“令人失望”，三星大跌7%，日韩股市双双下跌",
    "url": "https://wallstreetcn.com/articles/3780114",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T01:45:17+00:00",
    "summary": "三星电子股东回报方案重分红、轻回购，令市场大失所望，股价单日重挫逾6.5%，韩国Kospi指数跌1.4%，亚太科技板块全线承压。摩根大通直言方案\"毫无惊喜\"，大量细节更被推迟至明年1月敲定，不确定性叠加英伟达涨价、美加贸易破裂等多重利空，亚太市场情绪持续走弱。"
  },
  {
    "id": "wscn:3779983",
    "domain": "股票",
    "title": "阿里再投800亿港元，中国CSP的黄金周期才刚开始，还是泡沫前夜？",
    "url": "https://wallstreetcn.com/premium/articles/3779983?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T01:44:03+00:00",
    "summary": "阿里财报刚刚证明中国云业务重新加速：6月季度AI云与算力收入同比增长45%，AI相关产品收入达到123.76亿元，云业务EBITA利润率升至12%；几天后，公司又以112.7港元配售7.1亿股，募资800亿港元，全部投入全栈AI能力与基础设施。金山云同期也交出AI云高增、经营利润率转正的答卷。收入与盈利改善已经出现，但巨额融资把问题推向更深一层：中国CSP正在迎来高回报的资本开支周期，还是走向一场"
  },
  {
    "id": "wscn:3780113",
    "domain": "股票",
    "title": "美银Hartnett警告：贝森特若压不住长端利率，美元暴跌与资产抛售将接踵而至",
    "url": "https://wallstreetcn.com/articles/3780113",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T01:42:45+00:00",
    "summary": "Hartnett警告：若贝森特无法将30年期美债收益率压至5%以下，美元将大幅下跌，市场将转向做空风险资产、做空杠杆（AI超大规模算力、私人信贷）及做空周期性资产（金融股）。Hartnett对黄金及冷门长久期资产持多头立场，并以“成功是预期，失败不可想象”来形容当前政策赌注的极端性。"
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
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 391,
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
    "id": "rss:https://arxiv.org/abs/2608.20377",
    "domain": "金融",
    "title": "If It Walks Like an Arbitrage: Protocol-Agnostic Detection with Decidable Structural Equivalence",
    "url": "https://arxiv.org/abs/2608.20377",
    "source": "Adam Khayam, Hamid Kolli, Mohamed Iguernalala, \\c{C}agdas Bozman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.20377v1 Announce Type: new Abstract: Ethereum transactions admit a canonical structural form. Each execution trace is built into an abstract syntax tree of token transfers grouped by call-f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20589",
    "domain": "金融",
    "title": "Calibrating Inelastic Markets to Options: The Lean Marketron and the Generalized Langevin Equation",
    "url": "https://arxiv.org/abs/2608.20589",
    "source": "Andrey Itkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.20589v1 Announce Type: new Abstract: The Marketron model of \\cite{HalperinItkin2025Mark} and its option pricing extension in \\cite{HalperinItkinMarketron2} suffer from structural non-identi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20698",
    "domain": "金融",
    "title": "Priority Transparency, Admission Chances, and Information Acquisition in School Choice",
    "url": "https://arxiv.org/abs/2608.20698",
    "source": "Georgy Artemov, Siqi Pan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.20698v1 Announce Type: new Abstract: We study, theoretically and experimentally, how transparency about students' priorities and admission chances shapes their incentives to acquire informa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20842",
    "domain": "金融",
    "title": "Rethinking Synthetic Scenario Realism: Compatibility, Not Fidelity, Drives Hedging Performance",
    "url": "https://arxiv.org/abs/2608.20842",
    "source": "Ryuji Hashimoto, Masanori Hirano, Ryota Ozaki, Kentaro Imajo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.20842v1 Announce Type: new Abstract: Deep hedging is a data-driven approach to learn hedging strategies. It relies on synthetic price paths generator, as real market data is often limited f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21274",
    "domain": "金融",
    "title": "Recommendation Quality and the Concentration of Consumption: Experimental Evidence from Netflix",
    "url": "https://arxiv.org/abs/2608.21274",
    "source": "Guy Aridor, Winston Chou, Nathan Kallus, Antoine Scheid, Allen Tren, Kevin Zielincki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.21274v1 Announce Type: new Abstract: We study an experiment with 8.5 million users on Netflix's recommender system to measure how improvements in recommendation technology affect the set of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20727",
    "domain": "金融",
    "title": "A Multiscale Ball Test for Conditional Mean Independence",
    "url": "https://arxiv.org/abs/2608.20727",
    "source": "Simon Rudkin, Wanling Rudkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.20727v1 Announce Type: cross Abstract: Tests of conditional mean independence can lose power when departures are confined to a bounded part of a multivariate predictor space and the relevan"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21128",
    "domain": "金融",
    "title": "Structural Estimation of Marketing Mix Model Parameters from Geo-Experiments",
    "url": "https://arxiv.org/abs/2608.21128",
    "source": "Niklas Heusch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.21128v1 Announce Type: cross Abstract: Marketing Mix Models (MMMs) are widely used for marketing measurement and budget allocation, but face fundamental identification challenges: due to en"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21130",
    "domain": "金融",
    "title": "A Synthetic Benchmark Dataset with Endogenous Marketing Spend for Validating Marketing Mix Models",
    "url": "https://arxiv.org/abs/2608.21130",
    "source": "Niklas Heusch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.21130v1 Announce Type: cross Abstract: Marketing Mix Models (MMMs) estimate the incremental sales effect of advertising from observational time series, yet they are rarely validated against"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05011",
    "domain": "金融",
    "title": "Reaction-boundary variance and adjoint-consistent local-volatility projection",
    "url": "https://arxiv.org/abs/2607.05011",
    "source": "Chris Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2607.05011v3 Announce Type: replace Abstract: We derive an operational-time variance kernel for a latent-order-book reaction boundary and use it to separate three objects usually collapsed in ca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07479",
    "domain": "金融",
    "title": "Marginally Useful: An Information-Gap Identity in Conformal Prediction",
    "url": "https://arxiv.org/abs/2608.07479",
    "source": "Peter Cotton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T04:00:00+00:00",
    "summary": "arXiv:2608.07479v2 Announce Type: replace Abstract: Conformal prediction has been touted as a more formal, rigorous approach to adding uncertainty to a forecast. The sole objective of this note is to "
  },
  {
    "id": "hn:49391382",
    "domain": "金融",
    "title": "Tesla sunsets its Solar Roof tiles",
    "url": "https://www.theverge.com/tech/983167/tesla-solar-roof-tiles-discontinued",
    "source": "doener",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-21T17:32:57+00:00",
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
    "id": "hn:49304409",
    "domain": "金融",
    "title": "Make a 6-Tesla-class high-temperature superconducting dipole magnet at 4.2 K",
    "url": "https://journals.aps.org/prab/abstract/10.1103/4nhs-bkwh",
    "source": "supermagnet",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-08-14T20:49:29+00:00",
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
    "id": "hn:49214813",
    "domain": "金融",
    "title": "US Sold Euros to Save the Yen, Europe Found Out After",
    "url": "https://finance.yahoo.com/markets/currencies/articles/us-sold-euros-save-yen-033819315.html",
    "source": "amarcheschi",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-07T18:54:58+00:00",
    "summary": ""
  }
]
```
