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

- 今日日期：`2026-08-19`
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
  "date": "2026-08-19",
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
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1726558,
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
    "points": 1333978,
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
    "points": 1146963,
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
    "points": 1074063,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1o4gw6ZExs",
    "domain": "AI",
    "title": "我是怎么用AI干活的？",
    "url": "http://www.bilibili.com/video/av117092535768773",
    "source": "林亦LYi",
    "platform": "bilibili",
    "points": 1049227,
    "published_at": "2026-08-14T12:00:00+00:00",
    "summary": "AI 办公到底能干些啥？它真的能颠覆我们的工作方式，以至于让大厂押上身家也要卷吗？"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 627111,
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
    "points": 592562,
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
    "points": 584595,
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
    "points": 536528,
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
    "points": 438159,
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
    "points": 418770,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 352257,
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
    "points": 243540,
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
    "points": 241416,
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
    "points": 185485,
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
    "points": 179446,
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
    "points": 170675,
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
    "points": 163912,
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
    "points": 161415,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161096,
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
    "points": 159261,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 136259,
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
    "points": 131755,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 97038,
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
    "points": 93265,
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
    "points": 91513,
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
    "points": 87815,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74151,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 74150,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63551,
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
    "points": 47632,
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
    "points": 46458,
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
    "points": 44867,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1Y6uC6TE1m",
    "domain": "AI",
    "title": "疯狂Vibe Coding一周，我烧了近100亿Token，做了5个项目！",
    "url": "http://www.bilibili.com/video/av117080321957877",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 42326,
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
    "points": 40758,
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
    "points": 38933,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35141,
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
    "points": 30260,
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
    "points": 29638,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 26789,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 26563,
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
    "points": 22717,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 22481,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 21975,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21321,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 19645,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17779,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV11EJn6JEk9",
    "domain": "AI",
    "title": "claude+ccswitch配置glm5.2",
    "url": "http://www.bilibili.com/video/av116742495999581",
    "source": "cctryflow",
    "platform": "bilibili",
    "points": 13738,
    "published_at": "2026-06-13T11:13:45+00:00",
    "summary": "智谱文档：https://docs.bigmodel.cn/cn/coding-plan/latest-model"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 12770,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12248,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
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
    "points": 247,
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
    "points": 29,
    "published_at": "2026-08-18T07:02:04+00:00",
    "summary": ""
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
    "id": "rss:https://www.eetimes.com/the-charging-inlet-has-become-a-system-rethinking-ev-charge-control-electronics/",
    "domain": "AI 算力 / 半导体",
    "title": "The Charging Inlet Has Become a System: Rethinking EV Charge-Control Electronics",
    "url": "https://www.eetimes.com/the-charging-inlet-has-become-a-system-rethinking-ev-charge-control-electronics/",
    "source": "Raphi Zadicario, Product Manager and Chief Architect, Lumissil Microsystems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T12:00:00+00:00",
    "summary": "Explore how integrated charge-control architecture reduces complexity while supporting J3400, MCS, and global EV platforms. The post The Charging Inlet Has Become a System: Rethinking EV Charge-Contro"
  },
  {
    "id": "rss:https://www.eetimes.com/fluid-side-observability-expands-ai-hardware-reliability/",
    "domain": "AI 算力 / 半导体",
    "title": "Fluid-Side Observability Expands AI Hardware Reliability",
    "url": "https://www.eetimes.com/fluid-side-observability-expands-ai-hardware-reliability/",
    "source": "Rupesh Mainali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T11:34:10+00:00",
    "summary": "As AI systems increasingly rely on liquid cooling, coolant condition is emerging as a reliability signal. The post Fluid-Side Observability Expands AI Hardware Reliability appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/appeals-court-orders-fresh-review-of-djis-chinese-military-company-designation",
    "domain": "AI 算力 / 半导体",
    "title": "DJI scores a win in fight against US ban, appeals court orders fresh review of firm's 'Chinese military company' designation — drone maker will stay on Pentagon list while a judge examines classified ",
    "url": "https://www.tomshardware.com/tech-industry/appeals-court-orders-fresh-review-of-djis-chinese-military-company-designation",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T15:40:10+00:00",
    "summary": "The DC Circuit reversed one of four findings, ruling that a lower court upheld a fully redacted justification without reading the classified record behind it."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/start-your-3d-printing-journey-with-bambu-labs-awesome-p1s-printer-and-ams-color-printing-module-bundle-for-the-all-time-low-price-of-usd499-in-best-buys-60th-anniversary-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Start your 3D printing journey with Bambu Labs' awesome P1S printer and AMS color-printing module bundle for the all-time low price of $499 in Best Buy's 60th Anniversary Sale",
    "url": "https://www.tomshardware.com/3d-printing/start-your-3d-printing-journey-with-bambu-labs-awesome-p1s-printer-and-ams-color-printing-module-bundle-for-the-all-time-low-price-of-usd499-in-best-buys-60th-anniversary-sale",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T15:31:40+00:00",
    "summary": "Step into 3D printing with Bambu Lab's P1S and AMS combo bundle for $499. Back on sale at its lowest-ever price point."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-next-gen-nova-lake-chips-may-skip-bllc-for-mobile-skus-and-debut-on-razor-lake-hx-instead-leaker-claims-new-rumor-says-razor-lake-family-reportedly-uses-tsmcs-n2x-node",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's next-gen Nova Lake chips may skip game-boosting X3D cache rival for mobile SKUs and debut on Razor Lake-HX instead, leaker claims — new rumor says Razor Lake family reportedly uses TSMC's N2X ",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-next-gen-nova-lake-chips-may-skip-bllc-for-mobile-skus-and-debut-on-razor-lake-hx-instead-leaker-claims-new-rumor-says-razor-lake-family-reportedly-uses-tsmcs-n2x-node",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:18:57+00:00",
    "summary": "Nova Lake desktop CPUs look to be the exclusive recipient of bLLC, Intel's answer to AMD's X3D, as the company looks to debut bLLC on mobile with Razor Lake-HX, and possibly Razor Lake-AX. As such, th"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-claims-its-2026-rack-scale-ai-solution-is-4x-more-energy-efficient-than-its-2024-ai-platform-company-says-its-pacing-ahead-of-20x-efficiency-by-2030",
    "domain": "AI 算力 / 半导体",
    "title": "AMD claims its 2026 rack-scale AI solution is 4X more energy efficient than its 2024 AI platform — company says it's pacing ahead of 20X efficiency by 2030",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-claims-its-2026-rack-scale-ai-solution-is-4x-more-energy-efficient-than-its-2024-ai-platform-company-says-its-pacing-ahead-of-20x-efficiency-by-2030",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:00:00+00:00",
    "summary": "AMD says its 2025 rack-scale AI system is 4X more energy efficient compared to its 2024 AI solution, though does not produce actual benchmark results."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg32ucwm-32-inch-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Swift PG32UCWM 32-inch OLED gaming monitor review: A flagship display with premium performance and imagery",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg32ucwm-32-inch-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T13:00:00+00:00",
    "summary": "Asus delivers another flagship OLED with the ROG Swift PG32UCWM. It pulls out all the stops with a 32-inch Tandem RGB Stripe panel, 4K resolution, 240 Hz with 480 Hz/FHD dual mode, HDR10, Dolby Vision"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/adata-xpg-novakey-rgb-ddr5-6000-c30-2x16gb-review-turning-salvage-into-pure-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Adata XPG Novakey RGB DDR5-6000 C30 2x16GB Review — Turning salvage into pure performance",
    "url": "https://www.tomshardware.com/pc-components/ram/adata-xpg-novakey-rgb-ddr5-6000-c30-2x16gb-review-turning-salvage-into-pure-performance",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T12:30:00+00:00",
    "summary": "Amid the memory crunch, Adata unleashes its new XPG Novakey RGB memory kit series. But can the new lineup convince consumers to pick it up?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/how-to-choose-a-new-motherboard-without-overpaying-scoping-out-the-features-you-need-and-what-you-might-never-use-as-component-costs-soar",
    "domain": "AI 算力 / 半导体",
    "title": "How to choose a new motherboard without overpaying — scoping out the features you need, and what you might never use as component costs soar",
    "url": "https://www.tomshardware.com/pc-components/motherboards/how-to-choose-a-new-motherboard-without-overpaying-scoping-out-the-features-you-need-and-what-you-might-never-use-as-component-costs-soar",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T12:00:00+00:00",
    "summary": "How much motherboard is too much? We look at what you actually get as prices climb — from VRMs and connectivity to premium features and diminishing returns."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/famed-overclocker-1usmus-updates-hydra-overclocking-tool-with-up-to-3000-mhz-memory-offset-new-update-gives-vram-and-power-limit-controls-to-rtx-50-series-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Overclocker updates Hydra overclocking tool with VRAM and power limit controls for RTX 50-series GPUs — new update gives up to +3000 MHz memory offset",
    "url": "https://www.tomshardware.com/pc-components/gpus/famed-overclocker-1usmus-updates-hydra-overclocking-tool-with-up-to-3000-mhz-memory-offset-new-update-gives-vram-and-power-limit-controls-to-rtx-50-series-gpus",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T11:40:00+00:00",
    "summary": "Overclocker 1usmus has released a new update for their Hydra overclocking tool that features VRAM and power limit controls for RTX 50-series GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd",
    "domain": "AI 算力 / 半导体",
    "title": "China's homegrown AI accelerators to supply 90% of the country's domestic market, analysts suggest — Cambricon and Huawei expected to be the biggest winners in the shift away from Nvidia and AMD",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T11:20:00+00:00",
    "summary": "China could become almost self-sufficient in high-end AI accelerators in 2026 as Chinese IHVs led by Huawei expected to supply 90% of AI processors used domestically."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/gamestop-customer-earned-over-usd10-000-in-store-credit-from-a-stack-of-broken-consoles-traded-hundreds-of-playstations-xboxes-game-boys-switches-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "GameStop customer earned over $10,000 in store credit from a stack of broken consoles — traded 'hundreds' of PlayStations, Xboxes, Game Boys, Switches, and more",
    "url": "https://www.tomshardware.com/video-games/console-gaming/gamestop-customer-earned-over-usd10-000-in-store-credit-from-a-stack-of-broken-consoles-traded-hundreds-of-playstations-xboxes-game-boys-switches-and-more",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T11:12:05+00:00",
    "summary": "One man’s trash is another’s treasure, and GameStop just paid out over $10,000 for hundreds of broken consoles."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-buys-spirit-airlines-data-for-ai-training-for-just-usd10-million-purchase-includes-hundreds-of-millions-of-emails-microsoft-teams-chats-billions-of-flight-pricing-records-and-anonymized-passenger-records",
    "domain": "AI 算力 / 半导体",
    "title": "Google buys Spirit Airlines data for AI training for just $10 million — purchase includes hundreds of millions of emails, Microsoft Teams chats, billions of flight pricing records, and anonymized pass",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-buys-spirit-airlines-data-for-ai-training-for-just-usd10-million-purchase-includes-hundreds-of-millions-of-emails-microsoft-teams-chats-billions-of-flight-pricing-records-and-anonymized-passenger-records",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T11:02:02+00:00",
    "summary": "A U.S. bankruptcy court auctioned off Spirit Airlines' treasure trove of data, with Google making the winning bid. The tech giant is paying $10 million for various information, including hundreds of m"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/judges-who-use-ai-to-make-decisions-still-protected-by-judicial-immunity-court-ruling-protects-outcomes-regardless-of-ai-usage",
    "domain": "AI 算力 / 半导体",
    "title": "Judge allegedly outsourced entire ruling to AI and still can't be sued — federal court upholds blanket judicial immunity",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/judges-who-use-ai-to-make-decisions-still-protected-by-judicial-immunity-court-ruling-protects-outcomes-regardless-of-ai-usage",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T11:00:00+00:00",
    "summary": "A U.S. federal court has ruled that a judge accused of relying entirely on AI to make a judicial decision can still retain judicial immunity from civil lawsuits, although the ruling does not determine"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/expand-your-nas-with-a-third-off-this-seagate-8tb-ironwolf-hdd-32-percent-discount-in-best-buys-60th-anniversary-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Expand your NAS with a third off this Seagate 8TB IronWolf HDD — 32% discount in Best Buy's 60th Anniversary sale",
    "url": "https://www.tomshardware.com/pc-components/hdds/expand-your-nas-with-a-third-off-this-seagate-8tb-ironwolf-hdd-32-percent-discount-in-best-buys-60th-anniversary-sale",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T10:45:18+00:00",
    "summary": "Save $167 on an 8TB Seagate IronWolf HDD at Best Buy in their 60th Anniversary sales event."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/best-buy-has-slashed-usd1-350-off-this-outstanding-oled-rtx-5080-laptop-16-inch-lenovo-legion-pro-7i-features-a-24-core-arrow-lake-cpu-and-32gb-of-ddr5-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Best Buy has slashed $1,350 off this 'outstanding' OLED RTX 5080 laptop — 16-inch Lenovo Legion Pro 7i features a 24-core Arrow Lake CPU and 32GB of DDR5 RAM",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/best-buy-has-slashed-usd1-350-off-this-outstanding-oled-rtx-5080-laptop-16-inch-lenovo-legion-pro-7i-features-a-24-core-arrow-lake-cpu-and-32gb-of-ddr5-ram",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T10:31:02+00:00",
    "summary": "Get $1,350 off this Lenovo Legion Pro 7i with RTX 5080."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/secret-tracking-device-placed-in-rare-book-ends-up-in-amazon-processing-facility-destroying-books-to-train-ai-models-is-all-the-vegas-warehouse-does",
    "domain": "AI 算力 / 半导体",
    "title": "Secret tracking device placed in rare book ends up in Amazon processing facility — destroying books to train AI models is 'all' the Vegas warehouse does",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/secret-tracking-device-placed-in-rare-book-ends-up-in-amazon-processing-facility-destroying-books-to-train-ai-models-is-all-the-vegas-warehouse-does",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T10:30:00+00:00",
    "summary": "404 Media placed an AirTag inside a shipment of 1,000 books, which landed at an Amazon facility that reportedly spends all day cutting the spine off of, and scanning, books."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/operating-systems/china-reportedly-orders-state-agencies-to-uninstall-its-government-only-edition-of-windows-10",
    "domain": "AI 算力 / 半导体",
    "title": "China reportedly orders state agencies to uninstall its government-only edition of Windows 10 — Beijing accelerates planned retirement over data security concerns",
    "url": "https://www.tomshardware.com/software/operating-systems/china-reportedly-orders-state-agencies-to-uninstall-its-government-only-edition-of-windows-10",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T10:11:42+00:00",
    "summary": "China's Ministry of State Security has told some state-linked organizations to remove a customized version of Windows 10 from their machines."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/othisis-test-fires-3d-printed-fully-cryogenic-reusable-rocket-engine-indian-startup-leverages-slm-printing-to-create-its-first-working-prototype",
    "domain": "AI 算力 / 半导体",
    "title": "Firm test-fires 3D-printed, fully cryogenic reusable rocket engine — Indian startup leverages SLM printing to create its first working prototype",
    "url": "https://www.tomshardware.com/3d-printing/othisis-test-fires-3d-printed-fully-cryogenic-reusable-rocket-engine-indian-startup-leverages-slm-printing-to-create-its-first-working-prototype",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T10:00:00+00:00",
    "summary": "Othisis, an Indian startup that's only been in business for two years, has demonstrated a fully 3D-printed, reusable rocket engine."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-crypto-mining-gpus-hacked-to-restore-locked-away-vram-in-order-to-feed-ai-boom-software-mod-unlocks-64gb-of-vram-on-usd250-cmp-170hx",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia crypto mining GPUs hacked to restore locked-away VRAM — software mod unlocks 64GB of VRAM on $250 CMP 170HX",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-crypto-mining-gpus-hacked-to-restore-locked-away-vram-in-order-to-feed-ai-boom-software-mod-unlocks-64gb-of-vram-on-usd250-cmp-170hx",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T09:30:00+00:00",
    "summary": "CMP Unlocker enables previously disabled VRAM on Nvidia's five-year-old CMP 170HX cryptocurrency mining graphics card."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/best-buy-repairs-customers-gaming-laptop-by-simply-removing-half-the-ram-claims-unit-in-question-only-accepts-32gb-ram-of-ram-despite-selling-it-as-a-64gb-configuration",
    "domain": "AI 算力 / 半导体",
    "title": "Best Buy 'repairs' customer's gaming laptop by simply removing half the RAM— claims unit in question only accepts 32 GB of RAM despite listing a 64GB configuration",
    "url": "https://www.tomshardware.com/pc-components/ram/best-buy-repairs-customers-gaming-laptop-by-simply-removing-half-the-ram-claims-unit-in-question-only-accepts-32gb-ram-of-ram-despite-selling-it-as-a-64gb-configuration",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T09:00:00+00:00",
    "summary": "A Redditor claims that Best Buy ‘repaired’ a blue-screen-afflicted under-warranty laptop by simply removing one of its two SODIMMs, and when it passed tests, simply sent it back with half the memory i"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/geekom-admits-to-shipping-malware-laced-network-drivers-for-amd-mini-pcs-company-responds-with-guidance-removes-malicious-package",
    "domain": "AI 算力 / 半导体",
    "title": "Geekom admits to shipping malware-laced network drivers for AMD mini PCs — company responds with guidance, removes malicious package",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/geekom-admits-to-shipping-malware-laced-network-drivers-for-amd-mini-pcs-company-responds-with-guidance-removes-malicious-package",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T17:18:04+00:00",
    "summary": "Geekom admits to shipping malware-laced network drivers for AMD mini-PCs — maker requests takedown of report on the situation"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-sells-its-gaming-studio-for-at-least-1-5-billion-to-help-fund-ai-buildout",
    "domain": "AI 算力 / 半导体",
    "title": "Alibaba is selling its gaming studio for at least $1.5 billion to help fund AI buildout, mirroring Micron's exit from consumer business — dumps entire stake in Lingxi Games, which made 'Three Kingdoms",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-sells-its-gaming-studio-for-at-least-1-5-billion-to-help-fund-ai-buildout",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T15:39:28+00:00",
    "summary": "Alibaba has agreed to sell its game development unit, Lingxi Games, to Asian private equity firm Trustar Capital, according to an internal staff memo."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/cloud-storage/judge-clears-nine-pbs-to-retrieve-70-years-of-archival-tv-data-court-rules-station-owns-50tb-of-data-in-iron-mountain-servers-after-host-went-under",
    "domain": "AI 算力 / 半导体",
    "title": "Judge clears Nine PBS to retrieve 70 years of archival TV data — court rules station owns 50TB of data in Iron Mountain servers after host went under",
    "url": "https://www.tomshardware.com/software/cloud-storage/judge-clears-nine-pbs-to-retrieve-70-years-of-archival-tv-data-court-rules-station-owns-50tb-of-data-in-iron-mountain-servers-after-host-went-under",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T14:31:31+00:00",
    "summary": "There’s light at the end of the tunnel for Nine PBS after a judge has cleared the way for it to retrieve archival data and programming from Iron Mountain."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399",
    "domain": "AI 算力 / 半导体",
    "title": "Memory prices climb 500% in 12 months, up to 10x the lowest ever tracked prices — 128GB of DDR5 now $3,399",
    "url": "https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T13:52:30+00:00",
    "summary": "Analysis of historical price data trends indicates that the memory crisis has driven RAM prices to never-before-seen heights."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/new-data-centers-on-americas-largest-grid-face-first-in-line-blackouts-unless-they-bring-their-own-power",
    "domain": "AI 算力 / 半导体",
    "title": "America's largest grid wants to cut power to new data centers first during shortages — 50MW-plus data centers must bring their own electricity generation to avoid shutoffs",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/new-data-centers-on-americas-largest-grid-face-first-in-line-blackouts-unless-they-bring-their-own-power",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T13:11:38+00:00",
    "summary": "PJM Interconnection has asked federal regulators to approve rules that would cut power to new data centers ahead of households during supply shortages."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/asus-rog-edition-20-gaming-pc-build-a-pretty-powerhouse-pc-that-next-to-no-one-can-afford",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Edition 20 gaming PC build – A pretty powerhouse PC that next to no one can afford",
    "url": "https://www.tomshardware.com/desktops/pc-building/asus-rog-edition-20-gaming-pc-build-a-pretty-powerhouse-pc-that-next-to-no-one-can-afford",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T13:00:00+00:00",
    "summary": "What’s it like to build a PC with some of the most expensive components on the market? Asus sent us its ROG 20th anniversary components so we could find out for ourselves."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/intels-arc-pro-b70-workstation-gpu-is-now-up-to-48-percent-more-expensive-than-it-was-just-a-month-ago-32gb-battlemage-workstation-card-climbs-toward-usd2-000",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Arc Pro B70 workstation GPU is now up to 48% more expensive than it was just a month ago — 32GB Battlemage workstation card climbs toward $2,000",
    "url": "https://www.tomshardware.com/pc-components/gpus/intels-arc-pro-b70-workstation-gpu-is-now-up-to-48-percent-more-expensive-than-it-was-just-a-month-ago-32gb-battlemage-workstation-card-climbs-toward-usd2-000",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T11:40:00+00:00",
    "summary": "Intel's best Battlemage GPU is now even more expensive due to its large 32GB memory pool that's very useful for AI workloads."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/goldeneye-007-for-n64-has-been-100-percent-decompiled-success-of-half-decade-project-opens-up-possibilities-for-complex-mods-and-ports",
    "domain": "AI 算力 / 半导体",
    "title": "GoldenEye 007 for N64 has been '100% decompiled' — success of half-decade project opens up possibilities for complex mods and ports",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/goldeneye-007-for-n64-has-been-100-percent-decompiled-success-of-half-decade-project-opens-up-possibilities-for-complex-mods-and-ports",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T11:28:17+00:00",
    "summary": "A reverse engineering and retro gaming enthusiast has finally succeeded in their goal of decompiling GoldenEye 007, the monumental James Bond adventure shooter from Rare."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/largest-tribe-in-the-us-bans-hyperscale-data-centers-on-its-lands",
    "domain": "AI 算力 / 半导体",
    "title": "Cherokee Nation bans hyperscale data centers on its lands, won't support projects without consultation — energy and water consumption, air quality, noise, and cultural resource protection among concer",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/largest-tribe-in-the-us-bans-hyperscale-data-centers-on-its-lands",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T11:27:32+00:00",
    "summary": "Cherokee Nation, with more than 475,000 citizens, has banned hyperscale data center development on its tribally owned and trust lands."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/photonics/ai-data-center-optical-interconnect-market-to-hit-usd144-billion-by-2030-an-over-ten-fold-increase-from-2024-figures-according-to-new-projections-silicon-photonics-expected-to-account-for-nearly-two-thirds-of-revenue-driven-by-co-packaged-optics",
    "domain": "AI 算力 / 半导体",
    "title": "AI data center optical interconnect market to hit $144 billion by 2030, an over ten-fold increase from 2024 figures, according to new projections — silicon photonics expected to account for nearly two",
    "url": "https://www.tomshardware.com/tech-industry/photonics/ai-data-center-optical-interconnect-market-to-hit-usd144-billion-by-2030-an-over-ten-fold-increase-from-2024-figures-according-to-new-projections-silicon-photonics-expected-to-account-for-nearly-two-thirds-of-revenue-driven-by-co-packaged-optics",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T11:20:00+00:00",
    "summary": "A new CIC forecast projects that the data center optical interconnect market will grow from $13.7 billion in 2024 to $144.4 billion by 2030, with silicon photonics accounting for 63.7% of revenue."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/viewsonic-vg1457-dual-screen-portable-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "ViewSonic VG1457 dual-screen portable monitor review: compact size and weight, but lackluster color",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/viewsonic-vg1457-dual-screen-portable-monitor-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T11:05:00+00:00",
    "summary": "ViewSonic nailed the design with the VG1457, but should have put some more effort into sourcing higher quality display panels."
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
    "points": 967,
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
    "points": 449,
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
    "id": "rss:https://www.theverge.com/gadgets/981611/steelseries-arctis-nova-3p-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "SteelSeries’ comfy wireless gaming headset is nearly half off",
    "url": "https://www.theverge.com/gadgets/981611/steelseries-arctis-nova-3p-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T20:01:01+00:00",
    "summary": "While many gaming headsets come with extra features, the tradeoff is that they’re often uncomfortable and heavy. A lightweight, affordable alternative that can connect to a bunch of platforms is avail"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/981644/robin-williams-instagram-account-ai",
    "domain": "大厂 AI 动态",
    "title": "Robin Williams’ Instagram account brought back to fight ‘AI abuse’",
    "url": "https://www.theverge.com/entertainment/981644/robin-williams-instagram-account-ai",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T19:48:26+00:00",
    "summary": "Robin Williams' children are taking over their father's Instagram account after his daughter spoke out against the use of his AI likeness, as reported earlier by The Wrap. In a post on Tuesday, Zak, Z"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/981640/openai-security-changes-ai-hugging-face-hack",
    "domain": "大厂 AI 动态",
    "title": "OpenAI lays out new security changes after its AI hacked Hugging Face",
    "url": "https://www.theverge.com/ai-artificial-intelligence/981640/openai-security-changes-ai-hugging-face-hack",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T19:28:30+00:00",
    "summary": "OpenAI is announcing security updates following the July news that its AI broke out of a sandboxed environment and accidentally hacked Hugging Face, including improvements to its research environments"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/981525/galaxy-buds-3-pro-dji-pocket-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s Galaxy Buds 3 Pro are almost half off today",
    "url": "https://www.theverge.com/gadgets/981525/galaxy-buds-3-pro-dji-pocket-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T17:47:04+00:00",
    "summary": "If you’re looking for a feature-packed pair of earbuds that won’t break your wallet, Best Buy has the Samsung Galaxy Buds 3 Pro on sale for $139.99. That’s $40 lower than the current Amazon price, and"
  },
  {
    "id": "rss:https://www.theverge.com/tech/981562/sony-playstation-pulse-elevate-wireless-gaming-speakers-launch-date-preorder",
    "domain": "大厂 AI 动态",
    "title": "PlayStation&#8217;s wireless gaming speakers launch in November",
    "url": "https://www.theverge.com/tech/981562/sony-playstation-pulse-elevate-wireless-gaming-speakers-launch-date-preorder",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T17:18:57+00:00",
    "summary": "Sony's Pulse Elevate wireless gaming speakers are launching on November 12th and will cost $219.99, the company announced on Tuesday. Announced nearly a year ago, the speakers are compatible with a PS"
  },
  {
    "id": "rss:https://www.theverge.com/tech/981504/apple-app-store-eu-rules-core-technology-commission",
    "domain": "大厂 AI 动态",
    "title": "Apple squashes EU beef with new App Store rules",
    "url": "https://www.theverge.com/tech/981504/apple-app-store-eu-rules-core-technology-commission",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T16:48:26+00:00",
    "summary": "Apple is once again overhauling App Store rules in the European Union, which the company says will resolve its \"disagreements with the Commission over business terms and alternative distribution.\" As "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/981398/tesla-cybercab-launch-robotaxi-fsd-safe-ready",
    "domain": "大厂 AI 动态",
    "title": "Tesla is finally launching the Cybercab — let’s hope it’s ready",
    "url": "https://www.theverge.com/transportation/981398/tesla-cybercab-launch-robotaxi-fsd-safe-ready",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T16:26:29+00:00",
    "summary": "The Tesla Cybercab, that golden two-seater central to Elon Musk's robo-supremacist ambitions, is finally nearing it's public launch. Whether or not the no-steering wheel and no-pedal vehicle is actual"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/981418/peacock-price-increase-august-2026",
    "domain": "大厂 AI 动态",
    "title": "Peacock is raising prices by up to $3",
    "url": "https://www.theverge.com/streaming/981418/peacock-price-increase-august-2026",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:11:39+00:00",
    "summary": "Peacock is raising prices across its streaming plans once again, with the company's cheapest ad-supported Select tier going from $7.99 to $8.99 / month, as reported earlier by Variety. The Premium pla"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/981131/coyote-vs-acme-david-zaslac-warner-bros-discovery",
    "domain": "大厂 AI 动态",
    "title": "Coyote vs. Acme is even funnier because Warner Bros. Discovery tried to kill it",
    "url": "https://www.theverge.com/entertainment/981131/coyote-vs-acme-david-zaslac-warner-bros-discovery",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T13:35:35+00:00",
    "summary": "There's an argument to be made that people wouldn't be all that interested in Coyote vs. Acme if it weren't for the way David Zaslav tried to kill it. By trying to shelve the project, Warner Bros. Dis"
  },
  {
    "id": "rss:https://www.theverge.com/news/981381/comcast-xfinity-shield-wifi-motion-sensing",
    "domain": "大厂 AI 动态",
    "title": "Comcast is turning millions of its routers into motion detectors",
    "url": "https://www.theverge.com/news/981381/comcast-xfinity-shield-wifi-motion-sensing",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T13:30:00+00:00",
    "summary": "Comcast is bringing Wi-Fi motion sensing to millions of routers that are already in customers' homes, turning the devices into activity monitors. A new update to the Xfinity Internet app, arriving tod"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/cursor-capitalizes-on-github-frustration-launches-rival-hosting-platform/",
    "domain": "大厂 AI 动态",
    "title": "Cursor capitalizes on GitHub frustration, launches rival hosting platform",
    "url": "https://techcrunch.com/2026/08/18/cursor-capitalizes-on-github-frustration-launches-rival-hosting-platform/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T22:14:25+00:00",
    "summary": "Cursor, known for its AI Code Editor, is launching a new code-hosting platform to rival developers' long preferred favorite, GitHub."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/dojs-probe-into-andreessen-horowitz-over-board-seats-baffles-vcs/",
    "domain": "大厂 AI 动态",
    "title": "DOJ’s probe into Andreessen Horowitz over board seats baffles VCs",
    "url": "https://techcrunch.com/2026/08/18/dojs-probe-into-andreessen-horowitz-over-board-seats-baffles-vcs/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T20:36:20+00:00",
    "summary": "Since portfolio companies often pivot and expand into competing markets, investors view occasional conflicts of interest as unavoidable for large VC firms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/tiktok-explores-peer-to-peer-payments-via-dms-report-says/",
    "domain": "大厂 AI 动态",
    "title": "TikTok explores peer-to-peer payments via DMs, report says",
    "url": "https://techcrunch.com/2026/08/18/tiktok-explores-peer-to-peer-payments-via-dms-report-says/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T20:03:56+00:00",
    "summary": "If rolled out, the feature would use the social media service’s TikTok Pay offering, which is already available in Southeast Asia for TikTok Shop purchases."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/openai-institutes-new-safeguards-after-hugging-face-breach/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI institutes new safeguards after Hugging Face breach",
    "url": "https://techcrunch.com/2026/08/18/openai-institutes-new-safeguards-after-hugging-face-breach/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T18:00:00+00:00",
    "summary": "The new safeguards include more detailed monitoring of models during the development process, as well as greater emphasis on alignment and security during the post-training process."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/save-up-to-300-on-your-techcrunch-disrupt-2026-pass-until-august-21/",
    "domain": "大厂 AI 动态",
    "title": "Save up to $300 on your TechCrunch Disrupt 2026 pass until August 21",
    "url": "https://techcrunch.com/2026/08/18/save-up-to-300-on-your-techcrunch-disrupt-2026-pass-until-august-21/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T17:31:01+00:00",
    "summary": "If you’ve been circling around Disrupt, then now’s the best time to lock in your pass and start getting ready to join the rest of the startup community gathering in San Francisco from October 13-15 at"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/etcheds-valuation-doubles-to-21b-in-a-month/",
    "domain": "大厂 AI 动态",
    "title": "Etched’s valuation doubles to $21B in a month",
    "url": "https://techcrunch.com/2026/08/18/etcheds-valuation-doubles-to-21b-in-a-month/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T17:21:58+00:00",
    "summary": "Jane Street has installed Etched's first shipped AI cluster system, and was so impressed, it led another massive round, the startup says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/apple-overhauls-its-eu-app-store-fees-loosens-rules-for-alternative-app-stores/",
    "domain": "大厂 AI 动态",
    "title": "Apple overhauls its EU App Store fees, loosens rules for alternative app stores",
    "url": "https://techcrunch.com/2026/08/18/apple-overhauls-its-eu-app-store-fees-loosens-rules-for-alternative-app-stores/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T17:12:13+00:00",
    "summary": "Apple is simplifying its EU App Store fees, replacing its per-install fee with a 5% commission for apps distributed outside the App Store and making it easier for developers to operate alternative app"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/comcast-adds-motion-sensing-to-millions-of-its-newer-routers-with-a-privacy-catch/",
    "domain": "大厂 AI 动态",
    "title": "Comcast adds motion sensing to millions of its newer routers, with a privacy catch",
    "url": "https://techcrunch.com/2026/08/18/comcast-adds-motion-sensing-to-millions-of-its-newer-routers-with-a-privacy-catch/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T16:39:05+00:00",
    "summary": "A new feature added to Comcast's newest routers can detect if there is motion inside your home without needing traditional motion sensors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/why-apples-camera-equipped-airpods-may-not-be-the-pervert-pods-consumers-fear/",
    "domain": "大厂 AI 动态",
    "title": "Why Apple’s camera-equipped AirPods may not be the ‘pervert pods’ consumers fear",
    "url": "https://techcrunch.com/2026/08/18/why-apples-camera-equipped-airpods-may-not-be-the-pervert-pods-consumers-fear/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T16:19:10+00:00",
    "summary": "Apple’s leaked camera-equipped AirPods might avoid the privacy pitfalls of other AI wearables by preventing users from recording photos and videos."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/bluesky-says-its-recent-outage-was-caused-by-another-ddos-attack/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky says its recent outage was caused by another DDoS attack",
    "url": "https://techcrunch.com/2026/08/18/bluesky-says-its-recent-outage-was-caused-by-another-ddos-attack/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T15:59:48+00:00",
    "summary": "This is the latest large-scale DDoS attack to hit the social networking site this year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/peacock-is-raising-prices-across-all-of-its-streaming-plans/",
    "domain": "大厂 AI 动态",
    "title": "Peacock is raising prices across all of its streaming plans",
    "url": "https://techcrunch.com/2026/08/18/peacock-is-raising-prices-across-all-of-its-streaming-plans/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T15:26:31+00:00",
    "summary": "\"These price changes allow Peacock to continue to create the best experience for its viewers, remain competitive in the marketplace, and deliver unique content across all genres,\" the company wrote on"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/anthro-energy-breaks-ground-on-factory-that-could-pave-the-road-to-solid-state-batteries/",
    "domain": "大厂 AI 动态",
    "title": "Anthro Energy breaks ground on factory that could pave the road to solid-state batteries",
    "url": "https://techcrunch.com/2026/08/18/anthro-energy-breaks-ground-on-factory-that-could-pave-the-road-to-solid-state-batteries/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:00:00+00:00",
    "summary": "Battery materials startup Anthro Energy has broken ground on a Louisville factory to make electrolytes, including those for solid-state batteries."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/warps-new-system-is-an-out-of-the-box-software-factory-for-ai-development/",
    "domain": "大厂 AI 动态",
    "title": "Warp’s new system is an out-of-the-box software factory for AI development",
    "url": "https://techcrunch.com/2026/08/18/warps-new-system-is-an-out-of-the-box-software-factory-for-ai-development/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:00:00+00:00",
    "summary": "On Tuesday, Warp introduced Warp Factories, a new infrastructure system designed to make building AI software factories as easy as possible."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/openai-launches-a-safer-chatgpt-for-teens-years-after-teens-started-using-it/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches a safer ChatGPT for teens — years after teens started using it",
    "url": "https://techcrunch.com/2026/08/18/openai-launches-a-safer-chatgpt-for-teens-years-after-teens-started-using-it/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T13:50:30+00:00",
    "summary": "ChatGPT for Teens adds age-appropriate safety measures, parental controls, and learning tools designed to steer teens away from harmful content — and from using AI to cheat on their homework."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/perplexitys-free-ai-offer-left-it-with-millions-more-users-in-india/",
    "domain": "大厂 AI 动态",
    "title": "Perplexity’s free AI offer left it with millions more users in India",
    "url": "https://techcrunch.com/2026/08/18/perplexitys-free-ai-offer-left-it-with-millions-more-users-in-india/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T13:45:40+00:00",
    "summary": "Perplexity's India revenue rose about 60% after the Airtel offer ended for new users, even as downloads declined."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/apples-new-macos-update-reportedly-contains-a-video-of-airpods-with-a-camera/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s new macOS update reportedly contains a video of AirPods with a camera",
    "url": "https://techcrunch.com/2026/08/18/apples-new-macos-update-reportedly-contains-a-video-of-airpods-with-a-camera/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T13:28:51+00:00",
    "summary": "A video in a macOS Tahoe release candidate version shows a user wearing AirPods, looking at a book, and talking to Siri."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/daniel-eks-body-scanning-startup-neko-health-opens-first-us-office-in-new-york/",
    "domain": "大厂 AI 动态",
    "title": "Daniel Ek’s body-scanning startup Neko Health opens first US office, in New York",
    "url": "https://techcrunch.com/2026/08/18/daniel-eks-body-scanning-startup-neko-health-opens-first-us-office-in-new-york/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T13:00:00+00:00",
    "summary": "The scanning and bloodwork health startup founded by Spotify's founder will officially launch in New York in about a month."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/reach-capital-raises-265m-fund-v-to-back-ai-founders-building-to-expand-human-potential/",
    "domain": "大厂 AI 动态",
    "title": "Reach Capital raises $265M Fund V to back AI founders building to ‘expand human potential’",
    "url": "https://techcrunch.com/2026/08/18/reach-capital-raises-265m-fund-v-to-back-ai-founders-building-to-expand-human-potential/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T11:00:00+00:00",
    "summary": "Reach Capital announced Tuesday an oversubscribed $265 million Fund V."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/fairphone-is-launching-its-latest-repairable-phone-in-the-us-too/",
    "domain": "大厂 AI 动态",
    "title": "Fairphone is launching its latest repairable phone in the US too",
    "url": "https://techcrunch.com/2026/08/18/fairphone-is-launching-its-latest-repairable-phone-in-the-us-too/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T11:00:00+00:00",
    "summary": "The Fairphone 6+ is a midrange Android offering, but given the increasing prices of consumer gadgets amid the ongoing component shortages, a repairable device that can be made to last for years may pr"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/18/einride-strikes-deal-to-add-500-tesla-semis-to-its-fleet/",
    "domain": "大厂 AI 动态",
    "title": "Einride strikes deal to add 500 Tesla Semis to its fleet",
    "url": "https://techcrunch.com/2026/08/18/einride-strikes-deal-to-add-500-tesla-semis-to-its-fleet/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T10:30:00+00:00",
    "summary": "The deal will triple the size of Einride's fleet while sweetening the company's sales pitch for its Saga AI software. The Tesla Semis will be available to customers across North America."
  },
  {
    "id": "rss:https://stratechery.com/2026/nvidia-backs-openai-data-center-anthropic-news-google-buys-spirit-airlines-data/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia Backs OpenAI Data Center, Anthropic News, Google Buys Spirit Airlines Data",
    "url": "https://stratechery.com/2026/nvidia-backs-openai-data-center-anthropic-news-google-buys-spirit-airlines-data/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T10:00:00+00:00",
    "summary": "Nvidia makes another deal, this time with a frontier lab; Anthropic's revenue continues to amaze; and maybe data finally is oil."
  },
  {
    "id": "rss:https://stratechery.com/2026/stripe-acquiring-openrouter-aggregating-ai-flipping-the-business-model/",
    "domain": "大厂 AI 动态",
    "title": "Stripe Acquiring OpenRouter, Aggregating AI?, Flipping the Business Model",
    "url": "https://stratechery.com/2026/stripe-acquiring-openrouter-aggregating-ai-flipping-the-business-model/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T10:00:00+00:00",
    "summary": "Stripe is reportedly acquiring OpenRouter, an implicit bet on a future market of models and the chance at Aggregation."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/sabotage-experts-lawmakers-blast-rfk-jr-for-destroying-healthcare-research/",
    "domain": "大厂 AI 动态",
    "title": "\"Sabotage\": Experts, lawmakers blast RFK Jr. for destroying healthcare research",
    "url": "https://arstechnica.com/health/2026/08/sabotage-experts-lawmakers-blast-rfk-jr-for-destroying-healthcare-research/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T22:32:46+00:00",
    "summary": "US healthcare is broken. Under RFK Jr., the research agency working to fix it is, too."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/ukrainian-drones-overwhelm-russian-tanks-new-active-protection-system-for-now/",
    "domain": "大厂 AI 动态",
    "title": "Ukrainian drones overwhelm Russian tanks’ new active protection system—for now",
    "url": "https://arstechnica.com/gadgets/2026/08/ukrainian-drones-overwhelm-russian-tanks-new-active-protection-system-for-now/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T22:18:13+00:00",
    "summary": "Tanks with defensive tech for shooting down drones are still proving vulnerable."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/its-christmastime-at-spacex-as-company-salvages-starship-from-indian-ocean/",
    "domain": "大厂 AI 动态",
    "title": "Against all odds, SpaceX finally tugs Starship into port after 24 days at sea",
    "url": "https://arstechnica.com/space/2026/08/its-christmastime-at-spacex-as-company-salvages-starship-from-indian-ocean/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T19:01:09+00:00",
    "summary": "\"A team of SpaceX engineers is on their way to conduct additional analysis on the vehicle.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/disney-sues-fcc-and-its-chair-escalating-fight-against-trumps-chief-censor/",
    "domain": "大厂 AI 动态",
    "title": "Disney sues FCC and its chair, escalating fight against Trump's chief censor",
    "url": "https://arstechnica.com/tech-policy/2026/08/disney-sues-fcc-and-its-chair-escalating-fight-against-trumps-chief-censor/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T18:11:26+00:00",
    "summary": "FCC demands \"total capitulation\" in Trump censorship campaign, Disney suit says."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/peacock-raises-prices-by-18-percent-after-becoming-profitable/",
    "domain": "大厂 AI 动态",
    "title": "Peacock raises prices by 18 percent after becoming profitable",
    "url": "https://arstechnica.com/gadgets/2026/08/peacock-raises-prices-by-18-percent-after-becoming-profitable/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T16:42:30+00:00",
    "summary": "Peacock's quarterly profitability isn't guaranteed."
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
    "points": 31,
    "published_at": "2026-08-18T08:06:58+00:00",
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
    "id": "wscn:3779765",
    "domain": "股票",
    "title": "“避税Alpha”--华尔街最火的“对冲基金新策略”，帮超级富豪获取“零税率”",
    "url": "https://wallstreetcn.com/articles/3779765",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T03:35:17+00:00",
    "summary": "华尔街正掀起“避税Alpha”狂欢，美国富豪正把“少缴税”“零缴税”变成一门量化生意。量化巨头通过做空主动制造账面亏损，精准冲销天价税单，配合遗产法实现资产终极“零缴税”。该赛道吸金已超万亿美元，尽管监管利剑悬顶，这场顶级富豪专属的资本游戏依然火爆。"
  },
  {
    "id": "wscn:3779770",
    "domain": "股票",
    "title": "AI热潮的终局，是19世纪铁路泡沫？",
    "url": "https://wallstreetcn.com/articles/3779770",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T03:34:15+00:00",
    "summary": "科技分析师Thompson警告：AI不是伪命题，但资本链条可能先于回报断裂。他以19世纪铁路泡沫类比当下——钱的问题比电力和算力更紧迫，融资已从自由现金流烧穿债务市场，逼近股权融资边界。本轮AI泡沫若破裂，最有可能留下的遗产是电力基础设施。"
  },
  {
    "id": "wscn:3779686",
    "domain": "股票",
    "title": "对话付鹏：AI生产力叙事进入证伪空档期？市场正迎来关键窗口期！",
    "url": "https://wallstreetcn.com/premium/articles/3779686?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T03:33:22+00:00",
    "summary": "AI 动生产力提升的市场主线进入证伪空档期，当前AI实现工具效率提升，企业级垂直应用仍缺火候；大厂资本开支推高现金流压力叠加高利率环境，引发宏观、产业、市场层面共振调整"
  },
  {
    "id": "wscn:3779763",
    "domain": "股票",
    "title": "被市场忽视的小米AI",
    "url": "https://wallstreetcn.com/articles/3779763",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T03:18:19+00:00",
    "summary": "巴克莱最新报告直指小米AI战略被市场\"严重低估\"——横跨手机、家电、汽车的硬件生态正悄然构建差异化AI矩阵，而这一战略价值在当前股价中几乎归零。二季度营收虽承压，但电动车交付超预期，手机均价创历史新高。维持增持评级，目标价30美元，较现价隐含82%上行空间。"
  },
  {
    "id": "wscn:3779767",
    "domain": "股票",
    "title": "蚂蚁分拆融资启幕：AI挂帅，金融托底",
    "url": "https://wallstreetcn.com/articles/3779767",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T03:13:05+00:00",
    "summary": "蚂蚁集团时隔六年重启资本运作，旗下蚂蚁国际、OceanBase、蚂蚁数科及蚂蚁灵波相继启动外部融资。蚂蚁国际已完成12亿美元A轮融资，最快年内赴港上市；OceanBase和蚂蚁数科亦在筹备融资，上市预期升温。在硬科技与AI主导市场叙事的背景下，蚂蚁能否借AI转型重回估值巅峰，仍有待检验。"
  },
  {
    "id": "wscn:3779754",
    "domain": "股票",
    "title": "“债市风暴”席卷美欧日，长债收益率逼近数十年高点，高盛交易台：美联储“或被迫加息”",
    "url": "https://wallstreetcn.com/articles/3779754",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T02:40:26+00:00",
    "summary": "此轮风暴由通胀忧虑、财政扩张与需求结构性萎缩三重压力驱动，实际收益率为主要推手。高盛交易台警告，债券供给压力空前——AI相关发债规模已达4890亿美元——叠加传统买家系统性萎缩，实际利率被迫走高。高盛欧洲交易主管直言，美联储或被迫在数据走弱时仍加息以锚定长端利率。"
  },
  {
    "id": "wscn:3779764",
    "domain": "股票",
    "title": "创业板跌超4%，宇树IPO首日大涨500%，芯片、算力齐跌，银行逆势活跃，恒科指跌超1%，百度大跌12%",
    "url": "https://wallstreetcn.com/articles/3779764",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T02:28:29+00:00",
    "summary": "早盘人形机器人概念震荡下挫，中大力德、巨轮智能触及跌停，上纬新材、丰光精密、绿的谐波、昊志机电多股跌超10%。存储芯片集体下跌，德明利、兆易创新、大普微等跌幅居前。银行股活跃，中信银行、重庆银行、成都银行等纷纷走高。"
  },
  {
    "id": "wscn:3779762",
    "domain": "股票",
    "title": "梁文锋打新宇树科技浮盈11亿，雷军赚152亿，美团系浮盈333亿，大疆痛失超250亿",
    "url": "https://wallstreetcn.com/articles/3779762",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T02:26:52+00:00",
    "summary": "根据计算梁文锋旗下机构战略配售浮盈超11亿元，雷军顺为资本浮盈超152亿元，美团系作为最大外部股东浮盈超333亿元。大疆则因2018年放弃约1012万元投资，按开盘价测算痛失超250亿元。"
  },
  {
    "id": "wscn:3779761",
    "domain": "股票",
    "title": "宇树科技上市首日高开630%，中一签赚近50w，市值超4400亿",
    "url": "https://wallstreetcn.com/articles/3779761",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T02:00:02+00:00",
    "summary": "本次宇树科技公开发行股票4044.64万股，占发行后总股本的10%，募集资金总额约60.99亿元。发行后总股本约4.04亿股，其中上市初期无限售流通股数量仅3008.7720万股，占总股本比例约7.44%。"
  },
  {
    "id": "wscn:3779755",
    "domain": "股票",
    "title": "“AI股神”崩盘记：闻到“血腥味”后，华尔街“秃鹫”开启围猎",
    "url": "https://wallstreetcn.com/articles/3779755",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T01:58:45+00:00",
    "summary": "当一名对冲基金经理在出租车上接到\"急售Anthropic股权\"的电话，华尔街的猎杀游戏便已开始。\"AI先知\"Aschenbrenner的Situational Awareness基金，在银行连环追保、空头围剿与夜间火线谈判中，72小时内造成约350亿美元损失，登顶全球基金史上最大交易亏损榜首。"
  },
  {
    "id": "wscn:3779759",
    "domain": "股票",
    "title": "宇树科技上市展望：机器人锚之所在，量产与商业化加速拐点",
    "url": "https://wallstreetcn.com/premium/articles/3779759?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T01:50:06+00:00",
    "summary": "宇树科技是全球少数实现规模化盈利的人形机器人企业。"
  },
  {
    "id": "wscn:3779678",
    "domain": "股票",
    "title": "SpaceX5个月“爆肝”至1.7GW：模块化会否重写AIDC建设规则？",
    "url": "https://wallstreetcn.com/premium/articles/3779678?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T01:19:10+00:00",
    "summary": "SemiAnalysis对SpaceX极限建设速度的拆解，以及阿里CUBE 5.0将大型AIDC交付压缩至100天，使模块化再成市场焦点。随着项目迈向数百MW乃至GW级，电力、熟练工人和现场施工正成为建设约束。模块化把大量机电工作前移到工厂，将串行工程改造成并行制造，并开始兼顾速度、成本和质量。当AIDC从一次性工程转向可复制产品，产业链利润会向哪里迁移？"
  },
  {
    "id": "wscn:3779757",
    "domain": "股票",
    "title": "Anthropic ARR 650亿引多方解读分歧，机构称增速放缓论据不足",
    "url": "https://wallstreetcn.com/articles/3779757",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T01:14:15+00:00",
    "summary": "Anthropic年化收入650亿美元的报道遭多方质疑，此前第三方机构给出700-800亿，专家调研显示7月高达780亿。杰富瑞指出统计口径存在六种解释可能，增速放缓结论依据不足。"
  },
  {
    "id": "wscn:3779756",
    "domain": "股票",
    "title": "中国首次火箭陆地回收成功，蓝箭航天通过“第二次大考”",
    "url": "https://wallstreetcn.com/articles/3779756",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T01:14:10+00:00",
    "summary": "蓝箭航天朱雀三号遥二火箭完成国内首次入轨级运载火箭一子级着陆腿垂直回收与陆地回收，验证了\"液氧甲烷+不锈钢箭体+着陆腿垂直回收\"技术路线可行性。通过重点优化着陆动力方案，蓝箭成功通过“第二次大考”，验证了可重复使用技术路线，并为其IPO提供支撑。未来，核心挑战将全面转向火箭复飞与常态化商业运营。"
  },
  {
    "id": "wscn:3779758",
    "domain": "股票",
    "title": "不和京东健康拼卖药，平安好医生换了条路",
    "url": "https://wallstreetcn.com/articles/3779758",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T01:03:22+00:00",
    "summary": "8月18日晚，平安好医生发布2026年中期业绩，上半年实现收入24.84亿元，同比微降0.7%；同期..."
  },
  {
    "id": "wscn:3779750",
    "domain": "股票",
    "title": "芯片股抛售蔓延亚洲，日股跌逾2%，韩股大跌6%、暂停程序化卖盘5分钟",
    "url": "https://wallstreetcn.com/articles/3779750",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T00:56:05+00:00",
    "summary": "隔夜美股半导体板块跌势持续向亚洲市场蔓延，MSCI亚太指数下跌逾1%，日本东证指数跌幅扩大至2.4%，日经225指数跌幅同样超2%。韩国首尔综指跌逾6%，韩国交易所随即启动SIDECAR机制，暂停程序化卖盘以遏制抛售势头。"
  },
  {
    "id": "wscn:3779567",
    "domain": "股票",
    "title": "专利悬崖将至，BD 交易加速：MNC 如何用\"下一代大药\"重建自免护城河？",
    "url": "https://wallstreetcn.com/premium/articles/3779567?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T00:34:23+00:00",
    "summary": "全球自免（自身免疫性疾病）赛道正站在一个结构性拐点上。七大跨国药企（MNC，即跨国制药巨头）的核心自免大单品 2026 年上半年合计销售额突破 700 亿美元、同比增长 9%。"
  },
  {
    "id": "wscn:3779733",
    "domain": "股票",
    "title": "争夺IPO业务！大银行竞相给Anthropic授信，规模已达100亿美元",
    "url": "https://wallstreetcn.com/articles/3779733",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T00:26:12+00:00",
    "summary": "按目前Anthropic的邀约方案，最积极参与该信贷额度的银行单家承诺放贷约12.5亿美元。超过100亿美元的额度将至少是去年Anthropic获得信贷额度的四倍。这场授信竞赛的逻辑清晰：在大型资本市场交易前夕，银行在贷款中的出资规模越高，往往意味着在后续IPO中获得更核心角色的可能性越大。"
  },
  {
    "id": "wscn:3779747",
    "domain": "股票",
    "title": "美国债市遭“重锤”，华尔街：这一次恐非“暂时”，看起来很像2007",
    "url": "https://wallstreetcn.com/articles/3779747",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T00:22:55+00:00",
    "summary": "周二美国30年期国债收益率一度触及2007年以来最高，10年期收益率逼近年内高点。通胀担忧、企业债发行潮、财政赤字扩大及美联储政策不确定性多重因素叠加，市场普遍认为超低利率时代或已终结。分析人士警告，财报季结束后债市动荡或将对股市构成更直接挑战。"
  },
  {
    "id": "wscn:3779753",
    "domain": "股票",
    "title": "重大突破！我国首次实现火箭陆地回收",
    "url": "https://wallstreetcn.com/articles/3779753",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T00:21:19+00:00",
    "summary": "朱雀三号遥二火箭成功完成我国首次重复使用运载火箭一子级着陆腿回收，从立项到回收仅历时三年。火箭一子级成本占全箭约70%，重复使用次数越多发射成本越低，这一技术突破有望大幅压缩低轨星座组网成本，加速“六张网”建设进程。"
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
    "id": "rss:https://www.netinterest.co/p/shuffling-risk",
    "domain": "股票",
    "title": "Shuffling Risk",
    "url": "https://www.netinterest.co/p/shuffling-risk",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-10T15:10:44+00:00",
    "summary": "An Asset Class Reborn"
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
    "points": 283,
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
    "id": "hn:49335163",
    "domain": "金融",
    "title": "Meta faces 'astronomical' consequences as legal fight reaches critical moment",
    "url": "https://www.cnbc.com/2026/08/17/meta-attorneys-general-california-federal-trial-astronomical-consequences.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 85,
    "published_at": "2026-08-17T18:06:30+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.14760",
    "domain": "金融",
    "title": "The Price of Submission",
    "url": "https://arxiv.org/abs/2608.14760",
    "source": "Johan Fourie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.14760v1 Announce Type: new Abstract: Economics journals ration access to peer review with time and money. A July 2026 census of 500 RePEc-ranked economics journals accepting unsolicited sub"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14859",
    "domain": "金融",
    "title": "Disclosed Human-Capital Disruption and Firm-Specific Risk",
    "url": "https://arxiv.org/abs/2608.14859",
    "source": "Ang Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.14859v1 Announce Type: new Abstract: Human capital is a central organizational input, but standard financial data reveal little about firm-specific disruptions to workforce availability, co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14930",
    "domain": "金融",
    "title": "A Neurofinance Framework for Subjective Temporal Perception, Risk, and Investment Behavior",
    "url": "https://arxiv.org/abs/2608.14930",
    "source": "Pascal Stiefenhofer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.14930v1 Announce Type: new Abstract: Neurofinance shows that financial valuation depends on evolving neural states, while temporal experience is itself state dependent. Yet intertemporal mo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15097",
    "domain": "金融",
    "title": "Pricing Temperature-Index Insurance under Long Memory and Stochastic Time Change",
    "url": "https://arxiv.org/abs/2608.15097",
    "source": "Nader Karimi, Foad Shokrollahi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15097v1 Announce Type: new Abstract: This paper develops a unit-consistent actuarial framework for pricing capped cumulative temperature-index insurance under long-range dependence and stoc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15212",
    "domain": "金融",
    "title": "Is the medium the message? Social disclosure channels and firm risk",
    "url": "https://arxiv.org/abs/2608.15212",
    "source": "Andreas G. F. Hoepner, Blerita Korca, Frank Schiemann, Fabiola I. Schneider",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15212v1 Announce Type: new Abstract: Investors interpret social disclosures from a risk perspective, yet relevant information can reach them through channels that differ sharply in regulato"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15667",
    "domain": "金融",
    "title": "Scalable Pontryagin-Guided Adjoint-to-Control Recovery for Constrained Dynamic Portfolio Choice",
    "url": "https://arxiv.org/abs/2608.15667",
    "source": "Jaegi Jeon, Jeonggyu Huh, Hyeng Keun Koo, Byung Hwa Lim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15667v1 Announce Type: new Abstract: We develop a scalable adjoint-to-control framework for continuous-time portfolio choice under smooth pointwise constraints. A feasible direct-policy-opt"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15743",
    "domain": "金融",
    "title": "Behavioral Participating Insurance: Optimal Investment under Probability Distortion and Aspiration Constraints",
    "url": "https://arxiv.org/abs/2608.15743",
    "source": "Hao Liu, Yang Liu, Zhenyu Shen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15743v1 Announce Type: new Abstract: We study optimal investment for insurers managing participating (profit-sharing) contracts under probability distortion and probability benchmark (aspir"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15876",
    "domain": "金融",
    "title": "The Yeoman's Portfolio: Measuring Historical Risk Preferences Using Crop Choice",
    "url": "https://arxiv.org/abs/2608.15876",
    "source": "Remy Levin, Daniela Vidart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15876v1 Announce Type: new Abstract: We design a method for measuring the risk preferences of agents in the deep past. The method combines a structural model of crop choice as a portfolio a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15981",
    "domain": "金融",
    "title": "The Geography of Research: The Trade-Off Between Knowledge Production and Access",
    "url": "https://arxiv.org/abs/2608.15981",
    "source": "Sitian Liu, Yichen Su",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15981v1 Announce Type: new Abstract: Research activity generates highly localized positive spillovers, yet in the U.S. it has become increasingly spatially misaligned with population and ec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.16749",
    "domain": "金融",
    "title": "Rough Volatility Across Assets",
    "url": "https://arxiv.org/abs/2608.16749",
    "source": "Saad Mouti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.16749v1 Announce Type: new Abstract: We measure volatility roughness across asset classes using a common data infrastructure and pipeline. Our data covers 3,926 United States equities, 34 C"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.16827",
    "domain": "金融",
    "title": "Biases-Informed Job Search Guidance: Characterization, Implications, and Targeting Support",
    "url": "https://arxiv.org/abs/2608.16827",
    "source": "Bruno Cr\\'epon, Aur\\'elien Frot, Christophe Gaillac",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.16827v1 Announce Type: new Abstract: Job seekers' expectations about reemployment are increasingly used to study job search, but what their biases reveal about underlying beliefs and prefer"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.16842",
    "domain": "金融",
    "title": "When ratios fall: A dynamic approach to contingent convertibles",
    "url": "https://arxiv.org/abs/2608.16842",
    "source": "Li Chen, Liang Wang, Weixuan Xia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.16842v1 Announce Type: new Abstract: We propose a novel valuation framework for contingent convertible (CoCo) bonds based on the issuing bank's Common Equity Tier 1 (CET1) ratio, which is w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.16849",
    "domain": "金融",
    "title": "Targeting Support Using Job Seekers' Biases: A Randomized Experiment",
    "url": "https://arxiv.org/abs/2608.16849",
    "source": "Bruno Cr\\'epon, Aur\\'elien Frot, Christophe Gaillac",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.16849v1 Announce Type: new Abstract: Most digital job-search assistance encourages unemployed workers to broaden their search toward related occupations, targeting one important source of s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.16856",
    "domain": "金融",
    "title": "zLend: A Dual-Scope Cash-Flow Reconstruction Framework for On-Chain Credit Underwriting",
    "url": "https://arxiv.org/abs/2608.16856",
    "source": "Girish G N, Ashutosh Sahoo, Akshay SP, Gurukiran S, Dhanashekar Kandaswamy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.16856v1 Announce Type: new Abstract: Decentralized lending lacks a credit bureau: a borrower's capacity to repay must be inferred entirely from public on-chain activity, without income veri"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15447",
    "domain": "金融",
    "title": "Detecting Money Laundering in Rwandan Mobile Money: A Machine Learning Framework",
    "url": "https://arxiv.org/abs/2608.15447",
    "source": "Emmanuel Nahimana, Ya\\'e Ulrich Gaba",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15447v1 Announce Type: cross Abstract: Mobile money has widened financial access across Sub-Saharan Africa and enlarged the surface for money-laundering and terrorism-financing (ML/TF) acti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15597",
    "domain": "金融",
    "title": "Toward Decentralized Carbon Trading in Indonesia: A Public-Blockchain Architecture for Tokenized Real-World Assets",
    "url": "https://arxiv.org/abs/2608.15597",
    "source": "Rischan Mafrur, Fadli Ikhsan Pratama, Khadijah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15597v1 Announce Type: cross Abstract: Indonesia has established a regulated carbon market supported by national registry infrastructure and the IDXCarbon exchange. Carbon units can be issu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15640",
    "domain": "金融",
    "title": "A contribution to the critique of blockchain censorship",
    "url": "https://arxiv.org/abs/2608.15640",
    "source": "Ruichao Jiang, Michelle Yeo, Long Wen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15640v1 Announce Type: cross Abstract: We study the blockchain censorship attack introduced in [21], which shows that joining the attack is a dominant strategy. We show that, by introducing"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15841",
    "domain": "金融",
    "title": "Self-Supervised Auxiliary Task Discovery for Stable Reinforcement Learning in Stock Trading",
    "url": "https://arxiv.org/abs/2608.15841",
    "source": "Arishi Orra, Himanshu Choudhary, Manoj Thakur",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.15841v1 Announce Type: cross Abstract: Reinforcement learning has gained increasing attention as a data-driven approach for stock trading. However, learning a policy that is both profitable"
  },
  {
    "id": "rss:https://arxiv.org/abs/2112.07278",
    "domain": "金融",
    "title": "A compensatory model for quantile estimation and application to VaR",
    "url": "https://arxiv.org/abs/2112.07278",
    "source": "Xiaoyuan Tian, Shuzhen Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2112.07278v2 Announce Type: replace Abstract: Unlike the standard two-step workflow of estimating a time series distribution and extracting quantiles from it, this paper proposes a compensatory "
  },
  {
    "id": "rss:https://arxiv.org/abs/2401.08064",
    "domain": "金融",
    "title": "A mechanistic model of trust based on neural information processing",
    "url": "https://arxiv.org/abs/2401.08064",
    "source": "Scott E. Allen, Ren\\'e F. Kizilcec, A. David Redish",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2401.08064v3 Announce Type: replace Abstract: Trust is central to human social interactions, manifesting as a critical information processing step in taking actions that make one vulnerable to a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.09546",
    "domain": "金融",
    "title": "A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading",
    "url": "https://arxiv.org/abs/2407.09546",
    "source": "Yuan Li, Bingqiao Luo, Qian Wang, Nuo Chen, Xu Liu, Bingsheng He",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2407.09546v2 Announce Type: replace Abstract: The utilization of Large Language Models (LLMs) in financial trading has primarily been concentrated within the stock market, aiding in economic and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.07037",
    "domain": "金融",
    "title": "Cognitive Load and Information Processing in Financial Markets: Theory and Evidence from Disclosure Complexity",
    "url": "https://arxiv.org/abs/2507.07037",
    "source": "Yimin Du, Guolin Tang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2507.07037v2 Announce Type: replace Abstract: Cognitive-load research in financial markets generally treats disclosure complexity as a property of the document and information acquisition as a d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.15911",
    "domain": "金融",
    "title": "Sleeping Kelly",
    "url": "https://arxiv.org/abs/2510.15911",
    "source": "Ben Abramowitz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2510.15911v3 Announce Type: replace Abstract: The Sleeping Beauty problem is a problem of imperfect recall that has received considerable attention. One approach to solving the Sleeping Beauty p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.20279",
    "domain": "金融",
    "title": "The Economics of Model Collapse: Equilibrium, Welfare, and Optimal Provenance Subsidies in Synthetic Data Markets",
    "url": "https://arxiv.org/abs/2605.20279",
    "source": "Gustav Olaf Yunus Laitinen-Fredriksson Lundstr\\\"om-Imanov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2605.20279v2 Announce Type: replace Abstract: Generative artificial intelligence is rapidly transforming the supply side of training data: an increasing share of new tokens, images, and structur"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.20281",
    "domain": "金融",
    "title": "The Economics of AI Inference: Inflation Dynamics, Welfare Costs, and Optimal Monetary Policy under the Inference-Cost Phillips Curve",
    "url": "https://arxiv.org/abs/2605.20281",
    "source": "Gustav Olaf Yunus Laitinen-Fredriksson Lundstr\\\"om-Imanov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2605.20281v2 Announce Type: replace Abstract: We develop a unified microeconomic and monetary theory of artificial intelligence inference costs and their pass-through to inflation, welfare, and "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15999",
    "domain": "金融",
    "title": "U.S. Technological Containment and the Rise of China's Open AI Ecosystem",
    "url": "https://arxiv.org/abs/2606.15999",
    "source": "Wang Jin, Nadav Kunievsky, Bowen Lou, Tianshu Sun, James Evans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2606.15999v2 Announce Type: replace Abstract: Over the past decade, U.S. policies have increasingly aimed to preserve artificial intelligence (AI) leadership by promoting domestic free-market po"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02785",
    "domain": "金融",
    "title": "Inside the Kin Network: Consanguineous Marriage, Patriarchal Bargaining, and Women's Acceptance of Intimate Partner Violence in Pakistan",
    "url": "https://arxiv.org/abs/2607.02785",
    "source": "Sana Khalil, Angela Warner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2607.02785v2 Announce Type: replace Abstract: Women in Pakistan report greater acceptance of intimate partner violence (IPV) than men in several domestic situations. This study examines whether "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02823",
    "domain": "金融",
    "title": "Pump.fun Graduation Regime Windows: Survival Analysis of 832,941 Token Launches and the Social-Presence Effect",
    "url": "https://arxiv.org/abs/2607.02823",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2607.02823v3 Announce Type: replace Abstract: Kaplan-Meier and Cox proportional-hazards survival analysis of 832,941 Solana pump.fun token launches, observed 2026-05-08 to 2026-06-10. Pooled gra"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04529",
    "domain": "金融",
    "title": "Low-rank and graphon limits for dynamic threshold distress contagion in heterogeneous financial networks",
    "url": "https://arxiv.org/abs/2608.04529",
    "source": "Pengbin Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.04529v2 Announce Type: replace Abstract: We study a recoverable dynamic distress model for financial institutions connected by a weighted directed exposure network. Counterparty distress af"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06134",
    "domain": "金融",
    "title": "Large-Market Discipline in Combinatorial Double Auctions: No Assembly, Bundle Selection, and Complementarities",
    "url": "https://arxiv.org/abs/2608.06134",
    "source": "Konstantinos E. Zachariadis, Yongxin Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T04:00:00+00:00",
    "summary": "arXiv:2608.06134v2 Announce Type: replace Abstract: We study double auctions for markets in which goods are valuable in bundles, such as data, model weights, and fine-tuned AI assets. A key friction i"
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
  }
]
```
