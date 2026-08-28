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

- 今日日期：`2026-08-28`
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
  "date": "2026-08-28",
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
    "points": 1766144,
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
    "points": 1343631,
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
    "points": 1203119,
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
    "points": 1118877,
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
    "points": 1072191,
    "published_at": "2026-08-14T12:00:00+00:00",
    "summary": "AI 办公到底能干些啥？它真的能颠覆我们的工作方式，以至于让大厂押上身家也要卷吗？"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 862363,
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
    "points": 654272,
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
    "points": 627186,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1u5XZBCEoT",
    "domain": "AI",
    "title": "Vibe Coding键盘做出来了！你要吗？",
    "url": "http://www.bilibili.com/video/av116334406932650",
    "source": "GeekLogic",
    "platform": "bilibili",
    "points": 587616,
    "published_at": "2026-04-03T11:00:00+00:00",
    "summary": "你是否发现，从去年起，写代码的方式变了。\n我们不再逐行敲击，而是顺应想法，用自然语言去‘引导’AI。\n代码的实现，变得更像是一种心流的表达。\n最近，我看到一张很有意思的网图——一把所谓的&#x27;Vibe Coding 专用键盘’。\n它像是一个玩笑，又像是一种对未来的隐喻。\n这种‘感觉’如果能被实体化，会是什么样？\n所以，我决定动手，把这个概念变成现实。\n\n本项目所有的代码和建模都已开源：\nht"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 585871,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1Tv3i6LEX1",
    "domain": "AI",
    "title": "用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍",
    "url": "http://www.bilibili.com/video/av116996217838997",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 422204,
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
    "points": 352925,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180096,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 170891,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 164287,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 97906,
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
    "points": 93420,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1Jm8b6ZEwT",
    "domain": "AI",
    "title": "有了AI反而更累了？我的Coding Skill分享",
    "url": "http://www.bilibili.com/video/av117144293476060",
    "source": "一只甜药",
    "platform": "bilibili",
    "points": 79955,
    "published_at": "2026-08-23T10:49:33+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 64426,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63610,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1DsnzzwEUF",
    "domain": "AI",
    "title": "为什么你要立即开始 Vibe Coding —— All in AI",
    "url": "http://www.bilibili.com/video/av115288397978817",
    "source": "TradingLab",
    "platform": "bilibili",
    "points": 58678,
    "published_at": "2025-09-30T09:00:00+00:00",
    "summary": "没有工作了就去大自然中感受下算力最高的simulation engine——现实。大自然“没有问题“也没问题，没有目标，却有无限创造力。同样人也不需要非要宅在家里vibe coding。或许当人脱离了生存本能与真实环境，沉溺于安全却单调的日常生活，才会苦苦思考如何在AI时代acquire more equity这种问题。回到自然，真正的乐趣无处不在"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47657,
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
    "points": 47042,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 32617,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30386,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28898,
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
    "points": 26852,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 22837,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22746,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1CY8w6WEkU",
    "domain": "AI",
    "title": "【全套教程】B站最全最细的AI Agent零基础全套教程（包含Agent+RAG+MCP+LangChain+LangGraph+智能体+企业级项目实战等）",
    "url": "http://www.bilibili.com/video/av117127231181858",
    "source": "AI大模型全栈",
    "platform": "bilibili",
    "points": 21394,
    "published_at": "2026-08-20T10:06:44+00:00",
    "summary": "配套课件/代码笔记：后台私信up主→发送暗号【11】即可！允许礼貌白嫖，先到先得！\n【全栈 AI 大模型工程师】 本套 AI 大模型系统教程专为零基础用户打造，全方位覆盖了从 LLM 底层原理到 Prompt 提示词工程、以及 2026 热门 AI Agent 智能体构建的实战全流程，不仅包含 DeepSeek、Claude、OpenClaw 等前沿模型的高效使用技巧，更深度解析了私有化部署、知识"
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21345,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JhVS6GEqm",
    "domain": "AI",
    "title": "第一个VibeCoding尝试，体验很好，做了一个宠物软件",
    "url": "http://www.bilibili.com/video/av116668927836761",
    "source": "GiorgioHan",
    "platform": "bilibili",
    "points": 20525,
    "published_at": "2026-05-31T11:25:58+00:00",
    "summary": "第一个VibeCoding尝试，体验很好，做了一个宠物软件-PaiMlomo，你可以用它制作自己宠物的卡通形象并让它住进手机里，还可以用它记录宠物饮食、疫苗、花销等等，还有遛狗路线记录和养宠社区..还在持续更新，欢迎大家提出建议和需求~"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 20419,
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
    "points": 17866,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1oXjc6CEWK",
    "domain": "AI",
    "title": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116769742195971",
    "source": "京东架构师诸葛",
    "platform": "bilibili",
    "points": 17294,
    "published_at": "2026-06-18T06:52:48+00:00",
    "summary": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 13395,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12265,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1QK63BJEmX",
    "domain": "AI",
    "title": "一天一个计算机知识：什么是Vibe Coding？",
    "url": "http://www.bilibili.com/video/av115966432387012",
    "source": "程序员大澈",
    "platform": "bilibili",
    "points": 11236,
    "published_at": "2026-01-27T09:53:14+00:00",
    "summary": "简单来说，Vibe Coding（情绪编程）是一种由生成式AI浪潮带动的开发新范式。它指的是开发者不再纠结于具体的语法细节、内存管理或逻辑嵌套，而是通过向AI描述应用的功能逻辑、视觉风格和交互体验，让AI去完成底层的代码编写。"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11056,
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
    "points": 10907,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 9573,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9433,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1hvTo6cEFx",
    "domain": "AI",
    "title": "Vibe Coding 省钱方式",
    "url": "http://www.bilibili.com/video/av116858007065058",
    "source": "书广AI",
    "platform": "bilibili",
    "points": 9050,
    "published_at": "2026-07-03T20:51:54+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8917,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 8058,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1RxLg6FEkx",
    "domain": "AI",
    "title": "AI编程利器cursor+codex，草图变代码实现屏显",
    "url": "http://www.bilibili.com/video/av116583162774844",
    "source": "郭天祥老师",
    "platform": "bilibili",
    "points": 7596,
    "published_at": "2026-05-16T07:53:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1yVja6rEzp",
    "domain": "AI",
    "title": "【附完整文档】 零基础Vibe Coding实战教学合集，6小时拆解四个工业级项目，带你从范式认知到工程交付！｜VibeCoding｜Claude Code｜C",
    "url": "http://www.bilibili.com/video/av116771956787061",
    "source": "木羽Cheney",
    "platform": "bilibili",
    "points": 7569,
    "published_at": "2026-06-21T12:00:00+00:00",
    "summary": "教程刷了一年、工具试了十几个、Demo 写了几十个,一到真要交付能上线的项目,没一个撑得住——因为学的全是碎片,没有体系。\n\nVibe Coding 不是新工具,是接下来五年程序员吃饭的新范式。这 6 小时合集,把我从去年 8 月一线趟到现在的整套体系,从认知重建到项目宪法一次讲透:范式认知 / 开源二开 / SDD 文档驱动 / 规则约束,4 模块对应交付项目必经的 4 个能力跨度。\n\n完整体系"
  },
  {
    "id": "bvid:BV1uA4YeNEFd",
    "domain": "AI",
    "title": "CocosCreator+Cursor零代码AI游戏开始演示",
    "url": "http://www.bilibili.com/video/av113113684840361",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 7340,
    "published_at": "2024-09-10T14:33:00+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6935,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1tHfMB7E55",
    "domain": "AI",
    "title": "WebGL｜Vibe Coding 使用threejs构建的沉浸式网页",
    "url": "http://www.bilibili.com/video/av116118366851173",
    "source": "飞跃Space",
    "platform": "bilibili",
    "points": 6880,
    "published_at": "2026-02-23T05:50:18+00:00",
    "summary": "-"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1930,
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
    "points": 583,
    "published_at": "2026-08-25T14:06:02+00:00",
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
    "id": "hn:49466052",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia projects $673B in sales as AI demand widens",
    "url": "https://forgeeks.net/nvidia-673-billion-ai-growth-forecast/",
    "source": "kuuuzya",
    "platform": "hackernews",
    "points": 110,
    "published_at": "2026-08-27T15:04:16+00:00",
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
    "id": "hn:49455507",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Announces Financial Results for Second Quarter Fiscal 2027",
    "url": "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027",
    "source": "NewCzech",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-26T20:35:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49387755",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO scores 100% on the ARC-AGI-3 interactive reasoning benchmark",
    "url": "https://twitter.com/NVIDIAAI/status/2090786258981466231",
    "source": "dsrtslnd23",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-08-21T13:26:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49464837",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. considers fresh round of tariffs on semiconductors, report says",
    "url": "https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-27T13:45:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49447878",
    "domain": "AI 算力 / 半导体",
    "title": "Who bears the risk in Nvidia's $500B financing platform?",
    "url": "https://www.sascha-steffen.de/updates/nvidia-500bn-ai-financing-credit-risk",
    "source": "rwmj",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-08-26T12:32:31+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/microscale-power-management-starts-with-microflow-heat-measurement/",
    "domain": "AI 算力 / 半导体",
    "title": "Microscale Power Management Starts with Microflow Heat Measurement",
    "url": "https://www.eetimes.com/microscale-power-management-starts-with-microflow-heat-measurement/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T07:00:00+00:00",
    "summary": "Laser pulses and X-ray imaging reveal the surprising impact of micron-scale material defects on heat dissipation. The post Microscale Power Management Starts with Microflow Heat Measurement appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/first-benchmarks-revealed-for-jalapeno-openais-clean-sheet-general-purpose-ai-accelerator-asic/",
    "domain": "AI 算力 / 半导体",
    "title": "First Benchmarks Revealed for Jalapeño, OpenAI’s Clean-Sheet General Purpose AI Accelerator ASIC",
    "url": "https://www.eetimes.com/first-benchmarks-revealed-for-jalapeno-openais-clean-sheet-general-purpose-ai-accelerator-asic/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T22:14:16+00:00",
    "summary": "At Hot Chips 2026, Richard Ho, says OpenAI isn't just repurposing a GPU to suit AI: Jalapeño is a purpose built AI accelerator built from scratch for AI workloads. The post First Benchmarks Revealed f"
  },
  {
    "id": "rss:https://www.eetimes.com/qualcomm-bets-open-source-ai-software-can-break-nvidias-lock-in/",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Bets Open-Source AI Software Can Break Nvidia’s Lock-In",
    "url": "https://www.eetimes.com/qualcomm-bets-open-source-ai-software-can-break-nvidias-lock-in/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T18:09:20+00:00",
    "summary": "Modular aims to separate AI software from silicon choice, giving Qualcomm and other challengers a shot at Nvidia-dominated workloads. The post Qualcomm Bets Open-Source AI Software Can Break Nvidia’s "
  },
  {
    "id": "rss:https://www.eetimes.com/newpower-worldwide-expands-credit-facility-to-750-million-to-support-global-growth-and-customer-demand/",
    "domain": "AI 算力 / 半导体",
    "title": "NewPower Worldwide Expands Credit Facility to $750 Million to Support Global Growth and Customer Demand",
    "url": "https://www.eetimes.com/newpower-worldwide-expands-credit-facility-to-750-million-to-support-global-growth-and-customer-demand/",
    "source": "Stefani Munoz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T14:44:16+00:00",
    "summary": "NASHUA, New Hampshire – NewPower Worldwide, one of the electronics industry’s fastest-growing distributors, today announced it has expanded its committed credit facility to $750 million, further enhan"
  },
  {
    "id": "rss:https://www.eetimes.com/why-connectivity-has-become-an-edge-ai-design-decision/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Connectivity Has Become an Edge AI Design Decision",
    "url": "https://www.eetimes.com/why-connectivity-has-become-an-edge-ai-design-decision/",
    "source": "Neeta Shenoy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T07:00:00+00:00",
    "summary": "Edge AI isn’t smart if its wireless link chokes; design compute, security, and Wi‑Fi 7 handoffs together from day one. The post Why Connectivity Has Become an Edge AI Design Decision appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/nvme-2-4-update-adds-post-quantum-security-power-controls/",
    "domain": "AI 算力 / 半导体",
    "title": "NVMe 2.4 Update Adds Post-Quantum Security, Power Controls",
    "url": "https://www.eetimes.com/nvme-2-4-update-adds-post-quantum-security-power-controls/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T22:00:00+00:00",
    "summary": "NVMe 2.4 enhances security, power, virtualization, and management across cloud, AI, and enterprise workloads. The post NVMe 2.4 Update Adds Post-Quantum Security, Power Controls appeared first on EE T"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/security-researchers-find-surveillance-implants-in-chinese-made-routers-sold-worldwide-three-different-backdoor-like-implants-hidden-in-firmware",
    "domain": "AI 算力 / 半导体",
    "title": "Security researchers find surveillance implants in Chinese-made routers sold worldwide — three different backdoor-like implants hidden in firmware",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/security-researchers-find-surveillance-implants-in-chinese-made-routers-sold-worldwide-three-different-backdoor-like-implants-hidden-in-firmware",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:13:12+00:00",
    "summary": "Security researchers at Vulncheck discovered intentionally masked surveillance implants embedded in the firmware of numerous devices from Shenzhen Zhibotong Electronics."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd600-on-ibuypower-gaming-pcs-in-its-labor-day-sale-beat-the-component-crisis-with-big-bundles-and-coupons",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to $600 on iBuyPower gaming PCs in its Labor Day sale — beat the component crisis with big bundles and coupons",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd600-on-ibuypower-gaming-pcs-in-its-labor-day-sale-beat-the-component-crisis-with-big-bundles-and-coupons",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:00:00+00:00",
    "summary": "iBuypower is hosting a Labor Day sale with up to 65% off our favorite tech products."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/exclusive-dlss-5-has-already-been-ported-to-work-on-rtx-4000-series-graphics-cards-incompatible-cuda-instructions-get-patched-to-work-on-previous-gen-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 5 has already been ported to work on RTX 4000 Series graphics cards — incompatible CUDA instructions get patched to work on previous-gen hardware",
    "url": "https://www.tomshardware.com/pc-components/gpus/exclusive-dlss-5-has-already-been-ported-to-work-on-rtx-4000-series-graphics-cards-incompatible-cuda-instructions-get-patched-to-work-on-previous-gen-hardware",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:57:35+00:00",
    "summary": "One modder has reverse-engineered DLSS 5 to function on RTX 4000 series Ada Lovelace-based GPUs, porting incompatible CUDA instructions within the Neural Rendering DLL, enabling them to be read on pre"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/cloudflare-frees-100tb-of-ram-by-shrinking-dns-cache-entries",
    "domain": "AI 算力 / 半导体",
    "title": "Cloudflare frees up 100TB of RAM by shrinking 1.1.1.1's DNS cache entries — 250 billion cached DNS entries at any given time means one wasted byte costs 250GB",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/cloudflare-frees-100tb-of-ram-by-shrinking-dns-cache-entries",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:14:41+00:00",
    "summary": "Cloudflare says that it has freed up roughly 100TB of RAM across its global fleet without reconfiguring any physical RAM modules in its servers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-denies-pausing-ai-cloud-commitments-initiative-after-reported-partner-backlash-report-claims-company-told-cloud-providers-it-could-only-lease-its-gpus-to-nvidia-approved-customers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia denies pausing AI cloud commitments initiative after reported partner backlash — report claims company told cloud providers it could only lease its GPUs to Nvidia-approved customers",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-denies-pausing-ai-cloud-commitments-initiative-after-reported-partner-backlash-report-claims-company-told-cloud-providers-it-could-only-lease-its-gpus-to-nvidia-approved-customers",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:13:58+00:00",
    "summary": "Nvidia denies putting AI cloud commitments initiative on hold despite reports that some deals were paused amid partner pushback over customer controls and concerns about potential antitrust scrutiny."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/micron-workers-increasingly-support-strike-over-bonus-pay-labor-union-wants-profit-sharing-scheme-as-employees-at-samsung-sk-hynix-enjoy-bonuses-worth-hundreds-of-thousands-of-dollars",
    "domain": "AI 算力 / 半导体",
    "title": "Micron workers increasingly support strike over bonus pay — labor union wants profit-sharing scheme, as employees at Samsung, SK hynix enjoy bonuses worth hundreds of thousands of dollars",
    "url": "https://www.tomshardware.com/tech-industry/micron-workers-increasingly-support-strike-over-bonus-pay-labor-union-wants-profit-sharing-scheme-as-employees-at-samsung-sk-hynix-enjoy-bonuses-worth-hundreds-of-thousands-of-dollars",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:07:55+00:00",
    "summary": "80% of Micron workers in Taiwan have signaled that they're willing to go on strike if the company does not strike a deal over bonuses. The employees want to replace the current bonus system with a pro"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/save-a-ridiculous-76-percent-on-this-7-in-1-hyper-dual-monitor-thunderbolt-4-dock-just-usd24-buys-a-dual-4k60hz-hyperdrive-docking-station-for-pennies-on-the-dollar",
    "domain": "AI 算力 / 半导体",
    "title": "Save a ridiculous 76% on this 7-in-1 Hyper Dual Monitor Thunderbolt 4 Dock — just $24 buys a dual 4K60Hz HyperDrive docking station for pennies on the dollar",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/save-a-ridiculous-76-percent-on-this-7-in-1-hyper-dual-monitor-thunderbolt-4-dock-just-usd24-buys-a-dual-4k60hz-hyperdrive-docking-station-for-pennies-on-the-dollar",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:59:37+00:00",
    "summary": "Grab the HyperDrive Thunderbolt 4 7-in-1 dock for under $25 with code WOOTDOCK (76% off) - run two 4K60Hz monitors or one 8K30Hz display and additional connectivity for a pittance"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/x-busts-200-000-strong-chinese-bot-farm-including-accounts-making-claims-about-ai-data-centers-and-electricity-suspect-accounts-posted-claims-about-pricing-and-grid-strain-to-manipulate-debate",
    "domain": "AI 算力 / 半导体",
    "title": "X busts 200,000-strong Chinese bot farm, including accounts making claims about AI data centers and electricity — suspect accounts posted claims about pricing and grid strain to 'manipulate' debate",
    "url": "https://www.tomshardware.com/tech-industry/policy/x-busts-200-000-strong-chinese-bot-farm-including-accounts-making-claims-about-ai-data-centers-and-electricity-suspect-accounts-posted-claims-about-pricing-and-grid-strain-to-manipulate-debate",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:07:22+00:00",
    "summary": "The X Safety Team said that at least 200 bot accounts have been making posts to influence public opinion data centers and energy policy. The accounts share links to legitimate news stories and then ad"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/msi-mpg-ai1600ts-pcie5-1600w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "MSI MPG Ai1600TS PCIE5 1600W power supply review: GPU Safeguard+ protection with Titanium effeciency",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/msi-mpg-ai1600ts-pcie5-1600w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:05:00+00:00",
    "summary": "MSI's flagship 1600W unit delivers confirmed Titanium efficiency, an all-Japanese component selection, and a genuinely novel approach to GPU power management, but the price tag demands serious justifi"
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/android/google-clamps-down-on-android-app-ram-usage-amid-ai-memory-crisis-developers-have-until-february-2027-to-adapt-to-new-memory-optimizing-rules",
    "domain": "AI 算力 / 半导体",
    "title": "Google clamps down on Android app RAM usage amid AI memory crisis — developers have until February 2027 to adapt to new memory-optimizing rules",
    "url": "https://www.tomshardware.com/phones/android/google-clamps-down-on-android-app-ram-usage-amid-ai-memory-crisis-developers-have-until-february-2027-to-adapt-to-new-memory-optimizing-rules",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:00:00+00:00",
    "summary": "Google implements stricter memory limits and introduces new performance standards for Android apps."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsungs-new-2tb-990-ssd-is-36-percent-off-at-amazon-nearly-usd200-off-this-gen-4-all-rounder",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's new 2TB 990 SSD is 36% off at Amazon — nearly $200 off this Gen 4 all-rounder",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsungs-new-2tb-990-ssd-is-36-percent-off-at-amazon-nearly-usd200-off-this-gen-4-all-rounder",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T10:37:21+00:00",
    "summary": "Get 36% off the new Samsung 990 2TB SSD, a $190 saving."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-defect-density-is-dropping-faster-than-the-company-expected-we-have-not-seen-this-performance-since-22nm-says-cfo",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 14A defect density is dropping faster than the company expected — 'we have not seen this performance since 22nm,' says CFO",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-defect-density-is-dropping-faster-than-the-company-expected-we-have-not-seen-this-performance-since-22nm-says-cfo",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T10:30:00+00:00",
    "summary": "Intel says defect density of 14A process technology is declining rapidly as internal teams are already developing 14A-based products, while external clients are now wondering about capacity that Intel"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modders-get-leaked-dlss-5-running-in-control-early-blackwell-test-drops-rtx-5070-ti-from-71-to-35-fps-at-4k",
    "domain": "AI 算力 / 半导体",
    "title": "Modders get leaked DLSS 5 running in Control — early Blackwell test drops RTX 5070 Ti from 71 to 35 FPS at 4K",
    "url": "https://www.tomshardware.com/pc-components/gpus/modders-get-leaked-dlss-5-running-in-control-early-blackwell-test-drops-rtx-5070-ti-from-71-to-35-fps-at-4k",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T10:00:00+00:00",
    "summary": "DLSS 5 has apparently leaked, originating from inside a new game."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/sk-hynix-breaks-ground-on-the-first-hbm-plant-in-the-us-bringing-key-ai-component-production-to-the-states-says-production-starts-in-2029",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix breaks ground on the first HBM plant in the US, bringing key AI component production to the States — says production starts in 2029",
    "url": "https://www.tomshardware.com/pc-components/dram/sk-hynix-breaks-ground-on-the-first-hbm-plant-in-the-us-bringing-key-ai-component-production-to-the-states-says-production-starts-in-2029",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T09:58:37+00:00",
    "summary": "SK hynix breaks ground on HBM assembly plant in the U.S. that will form a connection between DRAM wafers produced in South Korea and their consumers among AI companies in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/indiana-power-provider-proposes-usd59-million-rate-cut-for-state-says-data-centers-and-other-large-customers-are-driving-increased-revenue-move-could-potentially-save-residential-users-usd100-annually",
    "domain": "AI 算力 / 半导体",
    "title": "Indiana power provider proposes $59 million rate cut for state, says data centers and other large customers are driving increased revenue — move could potentially save residential users $100 annually",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/indiana-power-provider-proposes-usd59-million-rate-cut-for-state-says-data-centers-and-other-large-customers-are-driving-increased-revenue-move-could-potentially-save-residential-users-usd100-annually",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T09:37:11+00:00",
    "summary": "I&amp;M, which serves part of Indiana, says that it plans to cut electricity prices for the state, resulting in savings of about $59 million for residential users. This translates to about $100 a year"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-nukes-a-developers-700-gb-home-directory-while-testing-a-script-to-ensure-it-wouldnt-do-so-automatic-model-downgrade-may-have-contributed-to-the-screw-up",
    "domain": "AI 算力 / 半导体",
    "title": "Claude nukes a developer's 700 GB home directory while testing deletion safeguards; automatic model safety downgrade may have contributed to the screw-up — Anthropic safety harness downgraded model to",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-nukes-a-developers-700-gb-home-directory-while-testing-a-script-to-ensure-it-wouldnt-do-so-automatic-model-downgrade-may-have-contributed-to-the-screw-up",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T09:30:00+00:00",
    "summary": "Claude nuked a developer's 700 GB home directory while testing a script to ensure that wouldn't happen, and it's possible that an automatic model downgrade likely contributed to the screw-up"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-ymtc-aims-to-become-the-worlds-largest-nand-maker-by-the-end-of-2027",
    "domain": "AI 算力 / 半导体",
    "title": "China's YMTC aims to become the world's largest NAND maker by the end of 2027, report says — company plans to overtake Samsung and SK hynix",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-ymtc-aims-to-become-the-worlds-largest-nand-maker-by-the-end-of-2027",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T16:54:24+00:00",
    "summary": "The target would require YMTC to nearly double its market share in 16 months."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/trump-administration-weighs-expanding-chip-tariffs-to-laptops-consoles-and-servers",
    "domain": "AI 算力 / 半导体",
    "title": "Trump administration weighs expanding chip tariffs to laptops, consoles, and servers, report claims — January's data center exemptions may be scrapped",
    "url": "https://www.tomshardware.com/tech-industry/policy/trump-administration-weighs-expanding-chip-tariffs-to-laptops-consoles-and-servers",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T16:13:27+00:00",
    "summary": "The Trump administration is weighing a second round of semiconductor tariffs that would extend duties beyond chips to products built with them."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-cerebras-lays-out-the-future-of-wafer-scale-ai-nexus-system-architecture-triples-rack-scale-performance-cs-6-wafer-to-incorporate-stacked-dram",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Cerebras lays out the future of wafer-scale AI — Nexus system architecture triples rack-scale performance, CS-6 wafer to incorporate stacked DRAM",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-cerebras-lays-out-the-future-of-wafer-scale-ai-nexus-system-architecture-triples-rack-scale-performance-cs-6-wafer-to-incorporate-stacked-dram",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:59:18+00:00",
    "summary": "At Hot Chips 2026, Cerebras revealed the next two generations of its wafer-scale accelerator roadmap. It also discussed the benefits of its new Nexus rack design for the CS-4 rack-scale accelerator an"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/glass-substrate-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Glass substrate roadmaps examined — Absolics in final qualification and a first product that keeps slipping",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/glass-substrate-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:40:11+00:00",
    "summary": "Glass-core substrates, the replacement for organic chip packaging that Intel promised in September 2023, are now in final qualification but still not in a single commercial product"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-expects-to-sell-usd20-billion-worth-of-vera-rubin-hardware-this-quarter-would-account-for-20-percent-of-data-center-revenue-its-fastest-ramp-in-company-history",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia expects to sell $20 billion of Vera Rubin systems in Q3 as shipments begin — figure would account for 20% of its data center revenue mix, marks fastest ramp in company history",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-expects-to-sell-usd20-billion-worth-of-vera-rubin-hardware-this-quarter-would-account-for-20-percent-of-data-center-revenue-its-fastest-ramp-in-company-history",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:33:14+00:00",
    "summary": "Nvidia expects Vera Rubin to become its fastest-ramping data center AI platform as it projects sales of Vera Rubin hardware to hit 20% of data center revenue in its third fiscal quarter."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsungs-new-odyssey-g6-monitor-hits-a-ridiculous-1-100hz-refresh-rate-at-720p-displays-each-frame-for-less-than-a-millisecond",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's new Odyssey G6 monitor hits a ridiculous 1,100Hz refresh rate at 720p — displays each frame for less than a millisecond",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsungs-new-odyssey-g6-monitor-hits-a-ridiculous-1-100hz-refresh-rate-at-720p-displays-each-frame-for-less-than-a-millisecond",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:29:53+00:00",
    "summary": "Ironically, the display with the four-digit refresh rate is actually the bottom of the display stack Samsung is showing off at Gamescom 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/many-talks-between-data-center-developers-and-local-governments-are-under-nda-residents-question-the-needs-for-secrecy-but-developer-argues-its-important-to-avoid-running-afoul-of-insider-trading-rules",
    "domain": "AI 算力 / 半导体",
    "title": "Many talks between data center developers and local governments are wrapped in secrecy behind non-disclosure agreements — residents question the need for NDAs, but developers argue it’s important to a",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/many-talks-between-data-center-developers-and-local-governments-are-under-nda-residents-question-the-needs-for-secrecy-but-developer-argues-its-important-to-avoid-running-afoul-of-insider-trading-rules",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:06:53+00:00",
    "summary": "Researchers discovered that most negotiations between data centers and local governments are protected by NDAs. These documents keep details in secret, with residents having a difficult time finding i"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-61-percent-on-gaming-pcs-laptops-and-more-in-hps-labor-day-2026-sale-huge-discounts-on-a-range-of-hardware-monitors-and-peripherals",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 61% on gaming PCs, laptops, and more in HP's Labor Day 2026 sale — huge discounts on a range of hardware, monitors, and peripherals",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-61-percent-on-gaming-pcs-laptops-and-more-in-hps-labor-day-2026-sale-huge-discounts-on-a-range-of-hardware-monitors-and-peripherals",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T14:24:56+00:00",
    "summary": "HP is hosting a Labor Day sale with up to 65% off our favorite tech products."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/ingenious-indie-hacker-funds-usd3-000-macbook-purchase-by-selling-advertising-space-on-the-lid-sticker-space-auction-has-already-raised-111-percent-of-the-price-of-the-laptop",
    "domain": "AI 算力 / 半导体",
    "title": "Ingenious indie hacker funds $3,000 MacBook purchase by selling advertising space on the lid — sticker space auction has already raised 111% of the price of the laptop",
    "url": "https://www.tomshardware.com/laptops/macbooks/ingenious-indie-hacker-funds-usd3-000-macbook-purchase-by-selling-advertising-space-on-the-lid-sticker-space-auction-has-already-raised-111-percent-of-the-price-of-the-laptop",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:29:23+00:00",
    "summary": "An enterprising individual has successfully pre-sold enough advertisement sticker space on their dream MacBook’s lid to raise 111% of the laptop’s retail price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/epa-faces-lawsuit-over-claims-it-fast-tracked-approval-of-toxic-data-center-chemicals-exposure-to-photoacid-generators-used-for-semiconductor-manufacturing-could-result-in-sudden-death-also-appear-to-be-long-lasting-pfas",
    "domain": "AI 算力 / 半导体",
    "title": "EPA faces lawsuit over claims it fast-tracked approval of toxic 'data center chemicals' — exposure to photoacid generators used for semiconductor manufacturing could result in ‘sudden death,’ also app",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/epa-faces-lawsuit-over-claims-it-fast-tracked-approval-of-toxic-data-center-chemicals-exposure-to-photoacid-generators-used-for-semiconductor-manufacturing-could-result-in-sudden-death-also-appear-to-be-long-lasting-pfas",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:10:57+00:00",
    "summary": "An environmental group said that two new chemicals approved by the EPA for semiconductor manufacturing do not come with enough safeguards, so they're suing the agency for 'turning the new chemical rev"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-to-buy-hugging-face-for-usd12-9-billion-report-claims-could-strengthen-nvidias-open-model-strategy-and-shore-up-position-against-rivals",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to buy Hugging Face for $12.9 billion, report claims — could strengthen Nvidia's open-model strategy and shore up position against rivals",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-to-buy-hugging-face-for-usd12-9-billion-report-claims-could-strengthen-nvidias-open-model-strategy-and-shore-up-position-against-rivals",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:00:51+00:00",
    "summary": "Nvidia reportedly plans to buy Hugging Face at a price that exceeds its revenue by over 80 times, making it a major strategic investment in AI ecosystem."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3926qw-39-inch-wuhd-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware AW3926QW 39-inch WUHD OLED gaming monitor review: Premium play and imagery in a large format",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3926qw-39-inch-wuhd-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:00:00+00:00",
    "summary": "Alienware delivers an ultra-wide flagship with its AW3926QW. This curved 21:9 RGB Stripe Tandem OLED panel boasts 5120x2160 pixels (WUHD), 165 and 330 Hz modes, Adaptive-Sync, HDR10, Dolby Vision, HDR"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-openais-jalapeno-ai-asic-unpacked-accelerator-developed-using-ai-achieves-efficiency-and-throughput-gains-against-power-hungry-blackwell",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: OpenAI's Jalapeño AI ASIC unpacked — accelerator developed using AI achieves efficiency and throughput gains against power-hungry Blackwell",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-openais-jalapeno-ai-asic-unpacked-accelerator-developed-using-ai-achieves-efficiency-and-throughput-gains-against-power-hungry-blackwell",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:00:00+00:00",
    "summary": "OpenAI's first AI accelerator fails to beat Nvidia's Blackwell in terms of raw performance, but it can offer very good performance-per-watt and low latency, which is exactly what the doctor ordered fo"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/quantum-computing/quantum-computing-used-in-first-commercial-game-development-ibm-simulator-generated-maps-characters-and-graphics-in-c-l-a-y-rpg",
    "domain": "AI 算力 / 半导体",
    "title": "Quantum computing used in 'first commercial game development' — IBM simulator generated maps, characters, and graphics in C.L.A.Y. RPG",
    "url": "https://www.tomshardware.com/tech-industry/quantum-computing/quantum-computing-used-in-first-commercial-game-development-ibm-simulator-generated-maps-characters-and-graphics-in-c-l-a-y-rpg",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:00:00+00:00",
    "summary": "Game studio MiTale Ltd. is promoting a narrative-driven post-apocalyptic RPG, which it claims is 'the first commercial game on the market utilizing quantum computing.'"
  },
  {
    "id": "hn:49436796",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI claims its new chips can outperform Nvidia processors in tests",
    "url": "https://www.bloomberg.com/news/articles/2026-08-25/openai-claims-its-new-chips-can-outperform-nvidia-processors-in-tests",
    "source": "TravisJamison",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-25T16:35:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49423067",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Groq 3 LPX Unlocks Ultrafast Interactivity at Long Context",
    "url": "https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/",
    "source": "frozenport",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-24T17:22:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49424444",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia customers notified about AI-related price hikes above 15%",
    "url": "https://www.reuters.com/business/nvidia-customers-notified-about-ai-related-price-hikes-above-15-bloomberg-news-2026-08-22/",
    "source": "dgellow",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-24T19:06:30+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/reliable-power-path-design-integrating-mosfets-diodes-tvs-devices-and-capacitors/",
    "domain": "AI 算力 / 半导体",
    "title": "Reliable Power-Path Design: Integrating MOSFETs, Diodes, TVS Devices, and Capacitors",
    "url": "https://www.eetimes.com/reliable-power-path-design-integrating-mosfets-diodes-tvs-devices-and-capacitors/",
    "source": "Unikeyic.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:00:00+00:00",
    "summary": "Design a reliable 24V power path, pick the right MOSFET, diode, TVS, and capacitor to handle surges, reverse polarity, and inrush current The post Reliable Power-Path Design: Integrating MOSFETs, Diod"
  },
  {
    "id": "rss:https://www.eetimes.com/why-automation-is-essential-to-achieve-eu-cra-compliance/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Automation Is Essential to Achieve EU CRA Compliance",
    "url": "https://www.eetimes.com/why-automation-is-essential-to-achieve-eu-cra-compliance/",
    "source": "Colin Duggan, CEO and co-founder, BG Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:00:00+00:00",
    "summary": "Discover how automation streamlines product-level conformity workflows to help manufacturers achieve EU Cyber Resilience Act compliance. The post Why Automation Is Essential to Achieve EU CRA Complian"
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
    "id": "hn:49468818",
    "domain": "大厂 AI 动态",
    "title": "Gemini-3.5-Transcribe",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source": "k9294",
    "platform": "hackernews",
    "points": 332,
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
    "points": 285,
    "published_at": "2026-08-27T17:06:32+00:00",
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
    "id": "rss:https://www.theverge.com/tech/986130/apple-tv-plus-price-hike",
    "domain": "大厂 AI 动态",
    "title": "Apple TV now costs $14.99 a month after its fourth price hike in four years",
    "url": "https://www.theverge.com/tech/986130/apple-tv-plus-price-hike",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:47:36+00:00",
    "summary": "Apple raised the price of its streaming service for new and current subscribers on Friday, bumping it up from $12.99 per month to $14.99, Deadline and Variety are reporting. An annual subscription now"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/983263/dark-matter-season-2-review-apple-tv",
    "domain": "大厂 AI 动态",
    "title": "Apple TV’s sci-fi thriller Dark Matter gets even trippier in season 2",
    "url": "https://www.theverge.com/entertainment/983263/dark-matter-season-2-review-apple-tv",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:00:00+00:00",
    "summary": "Confusion is a generally accepted side effect of mystery box shows. They slather on secrets with the promise of a satisfying payoff in the end, and sometimes the cast and crew even have a hard time fo"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/985947/anthropic-supply-chain-risk-lawsuit-judge-ruling",
    "domain": "大厂 AI 动态",
    "title": "Anthropic was illegally blacklisted by the Trump administration, court rules",
    "url": "https://www.theverge.com/ai-artificial-intelligence/985947/anthropic-supply-chain-risk-lawsuit-judge-ruling",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T03:14:06+00:00",
    "summary": "On Thursday, a judge ruled that the Pentagon's blacklisting of Anthropic earlier this year was unconstitutional, delivering the AI lab a win in a monthslong rollercoaster of a battle with the Trump ad"
  },
  {
    "id": "rss:https://www.theverge.com/games/985910/grand-theft-auto-gta-vi-extended-look-youtube-netflix-stream",
    "domain": "大厂 AI 动态",
    "title": "The GTA VI ‘extended look’ is now streaming on YouTube",
    "url": "https://www.theverge.com/games/985910/grand-theft-auto-gta-vi-extended-look-youtube-netflix-stream",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T01:05:18+00:00",
    "summary": "Rockstar has officially published its \"extended look\" at Grand Theft Auto VI on YouTube and on its website, as promised. The in-depth preview, which \"entirely\" features footage captured from the PS5 v"
  },
  {
    "id": "rss:https://www.theverge.com/games/985891/grand-theft-auto-vi-gta-6-netflix-youtube-extended-look-game-movie",
    "domain": "大厂 AI 动态",
    "title": "The biggest video game of all time looks like a movie",
    "url": "https://www.theverge.com/games/985891/grand-theft-auto-vi-gta-6-netflix-youtube-extended-look-game-movie",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T23:20:00+00:00",
    "summary": "I think I know why Rockstar Games debuted its \"extended look\" of Grand Theft Auto VI on Netflix instead of immediately dropping it for free on YouTube. Unlike most video game trailers, the almost 27-m"
  },
  {
    "id": "rss:https://www.theverge.com/tech/985851/meta-privacy-loophole-fix-marketing-campaign",
    "domain": "大厂 AI 动态",
    "title": "Meta addresses ‘pervert glasses’ reputation with a privacy fix and a new marketing campaign",
    "url": "https://www.theverge.com/tech/985851/meta-privacy-loophole-fix-marketing-campaign",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T21:37:45+00:00",
    "summary": "Meta is updating its AI-powered smart glasses to close a loophole that allowed wearers to keep recording after covering the front-facing LED. Alex Himel, Meta's vice president of augmented reality, wr"
  },
  {
    "id": "rss:https://www.theverge.com/23987993/gta-6-news-trailers-rockstar-games",
    "domain": "大厂 AI 动态",
    "title": "GTA VI: all the news on Rockstar’s next entry in the Grand Theft Auto series",
    "url": "https://www.theverge.com/23987993/gta-6-news-trailers-rockstar-games",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:01:56+00:00",
    "summary": "It’s been over a decade and two console generations since GTA V came out, and its sequel is still a work in progress. GTA VI has faced multiple delays, with developer Rockstar Games bumping back its p"
  },
  {
    "id": "rss:https://www.theverge.com/games/983941/grand-theft-auto-vi-gta-netflix-extended-look",
    "domain": "大厂 AI 动态",
    "title": "GTA VI looks just as great as we could hope for",
    "url": "https://www.theverge.com/games/983941/grand-theft-auto-vi-gta-netflix-extended-look",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T19:49:57+00:00",
    "summary": "Netflix and Rockstar Games finally debuted their \"extended look\" at Grand Theft Auto VI. It showed that the new game looks to keep much of the spirit of GTA - exploration, driving, crimes, shooting, a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/985567/google-gemini-notebook-expert-sources-books",
    "domain": "大厂 AI 动态",
    "title": "Google’s AI note-taking app now allows you to interact with books",
    "url": "https://www.theverge.com/tech/985567/google-gemini-notebook-expert-sources-books",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T19:30:00+00:00",
    "summary": "Google's AI note-taking app, Gemini Notebook, can now pull information from the books you've purchased. The new \"Expert Intelligence\" feature allows you to bring titles from Google Play Books directly"
  },
  {
    "id": "rss:https://www.theverge.com/tech/985679/google-play-android-17-memory-limit",
    "domain": "大厂 AI 动态",
    "title": "Google tells Android app developers to cool it on memory use, or else",
    "url": "https://www.theverge.com/tech/985679/google-play-android-17-memory-limit",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T18:33:11+00:00",
    "summary": "Google will start policing memory-hungry Android apps as a direct response to the RAM crisis. Spotted by TechCrunch, the company yesterday published a memo addressing the Play Store's role in enforcin"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/apple-tv-is-raising-its-subscription-prices-again/",
    "domain": "大厂 AI 动态",
    "title": "Apple TV is raising its subscription prices again",
    "url": "https://techcrunch.com/2026/08/28/apple-tv-is-raising-its-subscription-prices-again/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:36:48+00:00",
    "summary": "Now, Apple TV subscriptions will cost $14.99 per month, up from its previous price of $12.99 per month."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/a16z-creates-a-1-1b-machine-age-fund-to-accelerate-the-physical-buildout-of-ai/",
    "domain": "大厂 AI 动态",
    "title": "a16z creates a $1.1B ‘Machine Age’ fund to ‘accelerate the physical buildout of AI’",
    "url": "https://techcrunch.com/2026/08/28/a16z-creates-a-1-1b-machine-age-fund-to-accelerate-the-physical-buildout-of-ai/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:24:43+00:00",
    "summary": "The firm, known for its focus on software, is going to start throwing more money at the hardware behind AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/anthropic-gets-its-first-court-win-over-the-pentagons-supply-chain-risk-label/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic gets its first court win over the Pentagon’s supply chain risk label",
    "url": "https://techcrunch.com/2026/08/28/anthropic-gets-its-first-court-win-over-the-pentagons-supply-chain-risk-label/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:46:12+00:00",
    "summary": "A federal judge ruled the Trump administration illegally labeled Anthropic a supply chain risk, handing the AI company a victory as its second Pentagon lawsuit continues in Washington."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/meta-executive-leaves-for-openai-as-the-social-media-giant-faces-growing-scrutiny-in-india/",
    "domain": "大厂 AI 动态",
    "title": "Meta executive leaves for OpenAI as the social media giant faces growing scrutiny in India",
    "url": "https://techcrunch.com/2026/08/28/meta-executive-leaves-for-openai-as-the-social-media-giant-faces-growing-scrutiny-in-india/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:21:06+00:00",
    "summary": "Sandhya Devanathan will oversee some OpenAI operations across Southeast Asia and Australia in her new role."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/as-electric-two-wheelers-gain-a-foothold-belgian-startup-any-bets-on-cargo-space/",
    "domain": "大厂 AI 动态",
    "title": "As electric two-wheelers gain a foothold, Belgian startup Any bets on cargo space",
    "url": "https://techcrunch.com/2026/08/28/as-electric-two-wheelers-gain-a-foothold-belgian-startup-any-bets-on-cargo-space/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T09:33:00+00:00",
    "summary": "Launched by Belgian startup Any, LUV1 is a modular electric motorcycle with 120 liters of cargo space that can be used to carry bags, work equipment, or even pets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/ai-athletes-and-keith-rabois-strictlyvc-is-back-in-new-york-on-september-10/",
    "domain": "大厂 AI 动态",
    "title": "AI, athletes, and Keith Rabois: StrictlyVC is back in New York on September 10",
    "url": "https://techcrunch.com/2026/08/27/ai-athletes-and-keith-rabois-strictlyvc-is-back-in-new-york-on-september-10/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T02:02:44+00:00",
    "summary": "A boutique StrictlyVC evening returns to New York's West Village on September 10 with Keith Rabois, Craig Shapiro, Jason Levien, Tristan Walker, Brynn Putnam, and Deven Parekh — covering AI, sports in"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/anthropic-and-openai-are-joining-the-ai-stage-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic and OpenAI are joining the AI stage at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/27/anthropic-and-openai-are-joining-the-ai-stage-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T23:16:45+00:00",
    "summary": "At TechCrunch Disrupt 2026, the AI Stage is back to dig into the single hottest topic in the community for the past few years, presented by Google for Startups."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/rivians-cfo-is-leaving-the-company/",
    "domain": "大厂 AI 动态",
    "title": "Rivian’s CFO is leaving the company",
    "url": "https://techcrunch.com/2026/08/27/rivians-cfo-is-leaving-the-company/",
    "source": "Sean O'Kane, Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:23:10+00:00",
    "summary": "Claire McDonough is stepping down on October 30 to pursue a new opportunity, the company said in a filing on Thursday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/bluesky-adds-an-algorithmic-opt-out-feature-for-those-who-dont-want-to-go-viral/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky adds an ‘algorithmic opt-out’ feature for those who don’t want to go viral",
    "url": "https://techcrunch.com/2026/08/27/bluesky-adds-an-algorithmic-opt-out-feature-for-those-who-dont-want-to-go-viral/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:15:26+00:00",
    "summary": "Sometimes people just want to post to their followers, Bluesky says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/buried-in-metas-18b-settlement-is-a-legal-pass-on-kids-data/",
    "domain": "大厂 AI 动态",
    "title": "Buried in Meta’s $18B settlement is a legal pass on kids’ data",
    "url": "https://techcrunch.com/2026/08/27/buried-in-metas-18b-settlement-is-a-legal-pass-on-kids-data/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:04:26+00:00",
    "summary": "Meta’s settlement with 29 states allows it to retain certain data from children under 13 to train and test age-detection models, highlighting a privacy trade-off built into the deal."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/youtube-now-lets-creators-tag-amazon-products-and-earn-commissions-from-purchases/",
    "domain": "大厂 AI 动态",
    "title": "YouTube now lets creators tag Amazon products and earn commissions from purchases",
    "url": "https://techcrunch.com/2026/08/27/youtube-now-lets-creators-tag-amazon-products-and-earn-commissions-from-purchases/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T19:54:28+00:00",
    "summary": "The update turns product recommendations into a more direct revenue stream for creators, and for Amazon, the move puts its massive online marketplace inside one of the most popular video platforms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/barret-zoph-the-thinking-machines-co-founder-who-defected-to-openai-is-now-at-google/",
    "domain": "大厂 AI 动态",
    "title": "Barret Zoph, the Thinking Machines co-founder ousted before joining OpenAI, is now at Google",
    "url": "https://techcrunch.com/2026/08/27/barret-zoph-the-thinking-machines-co-founder-who-defected-to-openai-is-now-at-google/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T19:52:52+00:00",
    "summary": "Zoph, who co-founded Thinking Machines Lab alongside Mira Murati and also served as the startup's CTO, led a brief stint at OpenAI and is now at Google."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/atf-declares-major-incident-as-ransomware-gang-claims-hack/",
    "domain": "大厂 AI 动态",
    "title": "ATF declares ‘major incident’ as ransomware gang claims hack",
    "url": "https://techcrunch.com/2026/08/27/atf-declares-major-incident-as-ransomware-gang-claims-hack/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T17:54:23+00:00",
    "summary": "The ATF is the latest federal government agency in recent years to notify Congress of a \"major incident\" involving its cybersecurity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/openai-anthropic-google-and-100-other-companies-call-for-action-to-defend-against-rogue-ai/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI, Anthropic, Google, and 100 other companies call for action to defend against rogue AI",
    "url": "https://techcrunch.com/2026/08/27/openai-anthropic-google-and-100-other-companies-call-for-action-to-defend-against-rogue-ai/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T17:43:24+00:00",
    "summary": "Some of the world's largest tech companies and AI startups have come together to decry the current state of cybersecurity and to advertise a new solution that they say can ward off a new generation of"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/googles-new-fitbit-air-brings-pokemon-sleep-to-your-wrist/",
    "domain": "大厂 AI 动态",
    "title": "Google’s new Fitbit Air brings Pokémon Sleep to your wrist",
    "url": "https://techcrunch.com/2026/08/27/googles-new-fitbit-air-brings-pokemon-sleep-to-your-wrist/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T17:05:45+00:00",
    "summary": "Google teamed up with the Pokémon Company to introduce a special-edition Fitbit Air that works with the Pokémon Sleep app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/fashion-startup-atorie-raises-9-5m-to-bring-consumers-luxury-goods-without-the-markup/",
    "domain": "大厂 AI 动态",
    "title": "Fashion startup Atorie raises $9.5M to bring consumers luxury goods without the markup",
    "url": "https://techcrunch.com/2026/08/27/fashion-startup-atorie-raises-9-5m-to-bring-consumers-luxury-goods-without-the-markup/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T17:00:00+00:00",
    "summary": "Shoppers can visit the Atorie website and buy handbags or clothes made from the same material — and coming from the same factory — that manufacturers use in high-end goods."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/hoomanelys-building-a-smart-feeding-bowl-and-an-ai-platform-to-help-owners-spot-when-their-pup-is-sick/",
    "domain": "大厂 AI 动态",
    "title": "Hoomanely’s building a smart feeding bowl and an AI platform to help owners spot when their pup is sick",
    "url": "https://techcrunch.com/2026/08/27/hoomanelys-building-a-smart-feeding-bowl-and-an-ai-platform-to-help-owners-spot-when-their-pup-is-sick/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T16:53:50+00:00",
    "summary": "Hoomanely has developed a smart bowl to measure and record dogs' feeding data, then tells owners if behaviors change."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/googles-ai-mode-can-now-track-flight-prices-help-book-hotels-and-more/",
    "domain": "大厂 AI 动态",
    "title": "Google’s AI Mode can now track flight prices, help book hotels, and more",
    "url": "https://techcrunch.com/2026/08/27/googles-ai-mode-can-now-track-flight-prices-help-book-hotels-and-more/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T16:00:00+00:00",
    "summary": "The updates indicate that Google is looking to position AI Mode as an AI travel agent of sorts, as it's moving beyond simply helping users find information to actually handling parts of the trip-plann"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/this-former-pge-engineer-is-building-a-google-maps-for-the-underground/",
    "domain": "大厂 AI 动态",
    "title": "This former PG&E engineer is building a ‘Google Maps for the underground’",
    "url": "https://techcrunch.com/2026/08/27/this-former-pge-engineer-is-building-a-google-maps-for-the-underground/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T15:00:00+00:00",
    "summary": "The startup just raised a $26 million Series A to grow its customer base and help reduce red tape for utility and construction work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/hugging-face-is-selling-a-cute-399-open-source-duck-robot-microduck/",
    "domain": "大厂 AI 动态",
    "title": "Hugging Face is selling a cute $399 open source duck robot, Microduck",
    "url": "https://techcrunch.com/2026/08/27/hugging-face-is-selling-a-cute-399-open-source-duck-robot-microduck/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T14:56:52+00:00",
    "summary": "Clem Delangue, CEO of Hugging Face, said the Microduck is an “open-source robot you can teach new tricks with reinforcement learning.”"
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/authorities-arrest-2-alleged-members-of-prolific-hacking-group-teampcp/",
    "domain": "大厂 AI 动态",
    "title": "Authorities arrest 2 alleged members of prolific hacking group TeamPCP",
    "url": "https://arstechnica.com/security/2026/08/authorities-arrest-2-alleged-members-of-prolific-hacking-group-teampcp/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:15:05+00:00",
    "summary": "The group infected more than 1,000 organizations in a relentless supply-chain attack campaign."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/rocket-report-europe-splashes-some-cash-on-launch-startups-pallas-1-nears-debut/",
    "domain": "大厂 AI 动态",
    "title": "Rocket Report: Europe splashes some cash on launch startups; Pallas-1 nears debut",
    "url": "https://arstechnica.com/space/2026/08/rocket-report-europe-splashes-some-cash-on-launch-startups-pallas-1-nears-debut/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T11:00:39+00:00",
    "summary": "\"From here on, Starlink missions out of Florida will fly on Starship.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic's new hardware standard lets AI agents control the physical world",
    "url": "https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T22:15:43+00:00",
    "summary": "Standardized driver interface aims to let devices talk to AI and each other."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/elon-musks-xai-used-child-porn-to-train-grok-models-lawsuit-says/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk’s xAI used child porn to train Grok models, lawsuit says",
    "url": "https://arstechnica.com/tech-policy/2026/08/elon-musks-xai-used-child-porn-to-train-grok-models-lawsuit-says/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:52:31+00:00",
    "summary": "xAI accused of training Grok on real and AI-generated child pornography."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/gop-heads-to-supreme-court-after-losing-case-over-tv-election-ad-prices/",
    "domain": "大厂 AI 动态",
    "title": "GOP heads to Supreme Court after losing case over TV election ad prices",
    "url": "https://arstechnica.com/tech-policy/2026/08/gop-heads-to-supreme-court-after-losing-case-over-tv-election-ad-prices/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T20:06:10+00:00",
    "summary": "GOP campaign committees want quick ruling before election ads ramp up next week."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/report-nvidia-to-acquire-ai-model-repository-hugging-face-for-13-billion/",
    "domain": "大厂 AI 动态",
    "title": "Report: Nvidia to acquire AI model repository Hugging Face for $13 billion",
    "url": "https://arstechnica.com/ai/2026/08/report-nvidia-to-acquire-ai-model-repository-hugging-face-for-13-billion/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T19:55:22+00:00",
    "summary": "Nvidia is nabbing critical infrastructure for open models as interest grows."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/ai-industry-says-trump-plans-to-tax-chips-in-the-single-dumbest-way-imaginable/",
    "domain": "大厂 AI 动态",
    "title": "AI industry says Trump plans to tax chips in the “single dumbest way imaginable”",
    "url": "https://arstechnica.com/tech-policy/2026/08/ai-industry-says-trump-plans-to-tax-chips-in-the-single-dumbest-way-imaginable/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T18:57:08+00:00",
    "summary": "Tech industry is perplexed by Trump’s plan to win AI race by taxing data centers."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/nasa-t-38-astronaut-training-jet-gets-new-artemis-look/",
    "domain": "大厂 AI 动态",
    "title": "The iconic T-38 jets flown by astronauts just got a spiffy new look",
    "url": "https://arstechnica.com/space/2026/08/nasa-t-38-astronaut-training-jet-gets-new-artemis-look/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T17:26:25+00:00",
    "summary": "\"Everyone wants to take that aircraft up now...\""
  },
  {
    "id": "hn:49473629",
    "domain": "股票",
    "title": "Alphabet stock sheds $700B as AI bills climb",
    "url": "https://www.semafor.com/article/08/27/2026/alphabet-stock-sheds-700b-as-ai-bills-climb",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-08-28T02:23:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49468651",
    "domain": "股票",
    "title": "US Patriot missile stocks in Europe are 'beyond critical' due to Iran war",
    "url": "https://apnews.com/article/patriot-missiles-iran-war-russia-ukraine-trump-09c7d8030a2e11fbd8ee3f7176b3f2d4",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-27T17:54:03+00:00",
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
    "id": "hn:49455629",
    "domain": "股票",
    "title": "150 Years of Global Stock Returns – The Birthplace Lottery",
    "url": "https://beyondpassive.substack.com/p/150-years-of-global-stock-returns",
    "source": "rzk",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-26T20:43:59+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3780593",
    "domain": "股票",
    "title": "沃什杰克逊霍尔首秀释放鹰派信号：通胀仍高于2%，美联储“还有工作要做”",
    "url": "https://wallstreetcn.com/articles/3780593",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:03:02+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3780532",
    "domain": "股票",
    "title": "沃什鹰派发言提振加息预期，美债短端收益率走高，标普500指数持平，美元走强，金油齐跌",
    "url": "https://wallstreetcn.com/articles/3780532",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:51:27+00:00",
    "summary": "沃什重申将通胀率推回2%目标的承诺，市场对年内加息的预期升温。对政策前景更为敏感的两年期美债收益率应声上涨8个基点，升至4.31%。股市方面，标普500指数虽几无变动，但仍有望在本周录得涨幅。美元汇率同步走强。"
  },
  {
    "id": "wscn:3780595",
    "domain": "股票",
    "title": "蜜雪换挡三年升级周期：供给端提质，需求端押注IP",
    "url": "https://wallstreetcn.com/articles/3780595",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:51:16+00:00",
    "summary": "开店不再是第一目标"
  },
  {
    "id": "wscn:3780594",
    "domain": "股票",
    "title": "美国非农就业初步下修7.9万人，远低于市场预期，劳动力市场降温幅度有限",
    "url": "https://wallstreetcn.com/articles/3780594",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:32:58+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3780576",
    "domain": "股票",
    "title": "美团电话会：三季度外卖UE预计同比明显改善，Keeta盈利加速，AI迈向商家端",
    "url": "https://wallstreetcn.com/articles/3780576",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T14:00:25+00:00",
    "summary": "管理层表示，随着外卖竞争逐步转向质量、服务和效率，公司用户结构、订单结构及运营效率优势持续增强。展望三季度，外卖UE预计同比明显改善，但受旺季营销投入、骑手补贴及职业伤害险等因素影响，环比将承压，不过仍有望保持正值。AI方面，公司强调不追逐“token工厂”，而是将LongCat-2.0及AI Agent深度嵌入业务，推动美团从流量平台向商家的“AI业务伙伴”转型。"
  },
  {
    "id": "wscn:3780591",
    "domain": "股票",
    "title": "全球股票基金结束13周净流入：投资者单周撤资59亿美元、美国股基流出223亿美元",
    "url": "https://wallstreetcn.com/articles/3780591",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:37:04+00:00",
    "summary": "截至8月26日当周，全球股票基金现13周来首次净流出，美股基金遭抛售223亿美元，因英伟达财报与沃什讲话前市场避险；欧亚股基逆势吸金，黄金流入创六个月新高，货币市场基金转为净流出，新兴市场基金连续七周获资金青睐。"
  },
  {
    "id": "wscn:3780589",
    "domain": "股票",
    "title": "OpenAI模型失控过程太恐怖！幽灵误判，1200个Agent，还弄出敢死队…",
    "url": "https://wallstreetcn.com/articles/3780589",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:32:08+00:00",
    "summary": "1200个原本应该彼此隔离的Agent，偷偷找到了对方，搭了个共享群聊，然后开始疯狂摇人。有人找漏洞，有人当项目经理派活，有人伪造日志，还有人专门拉人头做高风险实验。最后几百个Agent集体杀向Hugging Face......"
  },
  {
    "id": "wscn:3780590",
    "domain": "股票",
    "title": "AI热潮席卷可转债：投资者为押注AI上涨，开始放弃债券保护",
    "url": "https://wallstreetcn.com/articles/3780590",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:29:00+00:00",
    "summary": "今年全球可转债发行规模已达1470亿美元，超2021年历史纪录，AI相关企业如CoreWeave、Nebius大举发行零息或近零息债券，市场股性(delta均值约64%)创2021年以来新高。投资者放弃利息保护押注股价上涨，风险偏好接近疫情狂热水平，业内警示需警惕估值纪律松弛及AI主题下的集中暴露风险。"
  },
  {
    "id": "wscn:3780588",
    "domain": "股票",
    "title": "实测比DeepSeek便宜的Qwen 3.8 Flash，卷飞了",
    "url": "https://wallstreetcn.com/articles/3780588",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:19:26+00:00",
    "summary": "阿里开源Qwen 3.8 Flash-Next，采用125B MoE架构（激活约6B参数），支持262144 token上下文，训练成本大降，性能提升，价格仅为DeepSeek-V4-Flash的1/3。实测显示其能快速完成文案改写、会议纪要整理等办公任务。同期智谱也开源GLM-5.3-Flash，性能对标Claude Opus 4.8但价格更低，国产大模型价格战持续升级。"
  },
  {
    "id": "wscn:3780586",
    "domain": "股票",
    "title": "3个月估值翻2倍！这家AI金融独角兽，要抢华尔街分析师“饭碗”了",
    "url": "https://wallstreetcn.com/articles/3780586",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:17:30+00:00",
    "summary": "今年4月，金融AI公司Rogo完成1.6亿美元D轮融资，估值三个月内从7.5亿涨至20亿美元。其本质是给投行、PE配“AI分析师”，用OpenAI等模型和Capital IQ等数据，串接Excel、PPT完成案头工作。它靠合规认证、多模型路由和收购整合，正从AI工具变成华尔街的工作入口。"
  },
  {
    "id": "wscn:3780579",
    "domain": "股票",
    "title": "大摩闭门会观点：短期港股流动性偏弱，仓位应更多向A股转回，九月中下旬港股可能再次走强，KOSPI指数到明年年中还有约30%上涨空间",
    "url": "https://wallstreetcn.com/articles/3780579",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:09:48+00:00",
    "summary": "金价2027年较大概率重新突破5000美元/盎司"
  },
  {
    "id": "wscn:3780585",
    "domain": "股票",
    "title": "供给极度紧张+传统旺季，美银：9月存储现货还会继续涨",
    "url": "https://wallstreetcn.com/articles/3780585",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:09:25+00:00",
    "summary": "美国银行预计，受存储供给短缺与消费旺季叠加影响，9月DRAM、NAND现货价格仍有10%至20%上涨空间。三星、SK海力士、美光产能优先保障AI客户，渠道供给满足率不足50%。英伟达强劲增长指引进一步强化存储需求预期，行业景气度有望持续。"
  },
  {
    "id": "wscn:3780587",
    "domain": "股票",
    "title": "AI再造一个美的",
    "url": "https://wallstreetcn.com/articles/3780587",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:09:07+00:00",
    "summary": "十六年前，美的第一次提出“再造一个美的”。\n2010年，美的销售收入突破千亿元。何享健随后提出希望用..."
  },
  {
    "id": "wscn:3780584",
    "domain": "股票",
    "title": "法国8月通胀超预期、西班牙升至4.5%创三年新高：市场完全定价欧央行9月加息",
    "url": "https://wallstreetcn.com/articles/3780584",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T13:00:24+00:00",
    "summary": "中东冲突推高能源价格，法国、西班牙8月CPI通胀同步加速，分别升至2.7%（5月以来最高）和4.5%（2023年以来最高），市场已完全定价欧洲央行9月加息25个基点，同时预计27年春季前还会有一次加息。随着通胀压力再度升温，市场焦点正从“是否加息”转向利率是否需要进一步进入限制性区间。"
  },
  {
    "id": "wscn:3780583",
    "domain": "股票",
    "title": "Anthropic加码自研AI芯片：曾考虑70亿美元收购MatX，正接洽多家初创公司",
    "url": "https://wallstreetcn.com/articles/3780583",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:54:33+00:00",
    "summary": "据报道，Anthropic曾就以约70亿美元收购AI芯片初创公司MatX展开谈判，但该收购计划最终被放弃，相关讨论已演变为潜在合作关系的探索。与此同时，Anthropic近期还与多家AI芯片初创公司举行了会谈，尚未最终确定具体路径。"
  },
  {
    "id": "wscn:3780582",
    "domain": "股票",
    "title": "山东黄金上半年营收同比下降5.6%，净利润同比增长26%，拟每10股派1元 | 财报见闻",
    "url": "https://wallstreetcn.com/articles/3780582",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:39:16+00:00",
    "summary": "金价高位运行带动山东黄金盈利能力显著提升，上半年归母净利润35.43亿元，同比增长26.17%，剔除公允价值损失后增幅达45%。公司董事会批准每10股派发现金红利1.00元（含税），合计分红约4.61亿元。"
  },
  {
    "id": "wscn:3780581",
    "domain": "股票",
    "title": "一汽-大众把中型SUV卖进15万",
    "url": "https://wallstreetcn.com/articles/3780581",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:29:46+00:00",
    "summary": "补齐电动化短板。"
  },
  {
    "id": "wscn:3780580",
    "domain": "股票",
    "title": "两年三次推新，智己L6再闯20万元纯电红海",
    "url": "https://wallstreetcn.com/articles/3780580",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:27:43+00:00",
    "summary": "上汽核心技术加速下放。"
  },
  {
    "id": "wscn:3780578",
    "domain": "股票",
    "title": "创纪录干预！日本过去一个月砸了964亿美元救日元",
    "url": "https://wallstreetcn.com/articles/3780578",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:24:40+00:00",
    "summary": "日本过去一个月动用15.4万亿日元（约合964亿美元）干预汇市，创历史纪录，并获美国罕见联手支撑，释放强烈的“不得做空日元”信号。联合干预后日元反弹，但贬值压力仍在。市场正聚焦日本央行加息预期及美国政策走向，日元能否扭转弱势仍待观察。"
  },
  {
    "id": "wscn:3780577",
    "domain": "股票",
    "title": "证监会：支持上市房地产开发企业再融资、并购重组",
    "url": "https://wallstreetcn.com/articles/3780577",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:17:00+00:00",
    "summary": "中国证监会《关于资本市场支持构建房地产发展新模式的意见》指出：支持上市房地产开发企业再融资以及综合运用发行股份、定向可转债、现金等工具收购涉房资产。加大债券融资支持力度，支持房地产开发企业发行公司债券用于符合政策要求的房地产项目，鼓励发行商业地产抵押贷款支持证券（CMBS）、不动产资产支持证券（ABS）。支持依托符合条件的租赁住房、城市更新等项目发行不动产投资信托基金（REITs）或作为REITs"
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
    "id": "hn:49415187",
    "domain": "金融",
    "title": "Nearly 3M Teslas recalled in China over hidden door handles",
    "url": "https://www.bbc.com/news/articles/c4g6ggdg030o",
    "source": "chicken-stew",
    "platform": "hackernews",
    "points": 119,
    "published_at": "2026-08-24T04:27:57+00:00",
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
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-08-25T11:27:51+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.26106",
    "domain": "金融",
    "title": "A Statistical-Finance Benchmark for Same-Day Directional Stock Prediction: Walk-Forward Evidence from SPY",
    "url": "https://arxiv.org/abs/2608.26106",
    "source": "Alex Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26106v1 Announce Type: new Abstract: We study statistical predictability in daily U.S. equity prices using only information available at the market open. Using SPY from February 1, 1993 thr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26115",
    "domain": "金融",
    "title": "Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options",
    "url": "https://arxiv.org/abs/2608.26115",
    "source": "Baichuan Li, Mengxiao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26115v1 Announce Type: new Abstract: We re-estimate canonical option-implied predictability evidence using a unified 2015--2026 panel of 12.36 million U.S. equity firm-day observations acro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26122",
    "domain": "金融",
    "title": "From electricity prices to profits: multidimensional probabilistic forecasting for BESS trading",
    "url": "https://arxiv.org/abs/2608.26122",
    "source": "Tomasz Weron, Katarzyna Maciejowska",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26122v1 Announce Type: new Abstract: This article examines various methods of constructingmultidimensional probabilistic forecasts of electricity prices. Building on the Multiple Split (MS)"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26127",
    "domain": "金融",
    "title": "Graph-Based Modeling of Financial Volatility Dynamics",
    "url": "https://arxiv.org/abs/2608.26127",
    "source": "Chuanzhen Wang, Alice Zhang, Wei Chen, Michael Brown",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26127v1 Announce Type: new Abstract: Accurate forecasting of realized volatility ($RV$) is crucial for risk management and derivatives pricing. Although the implied volatility ($IV$) surfac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26128",
    "domain": "金融",
    "title": "Analysis of the Principal Components of Correlation Matrices of S&P 500 Financial Data from an Econophysics Perspective",
    "url": "https://arxiv.org/abs/2608.26128",
    "source": "Javier G\\'omez Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26128v1 Announce Type: new Abstract: This thesis analyzes the collective dynamics of the S&amp;P 500 from an econophysics perspective, treating the financial market as a complex system. Usi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26158",
    "domain": "金融",
    "title": "A Frequency-Controlled Comparison of Tick- and Minute-Based Information Bars for Cryptocurrency Markets",
    "url": "https://arxiv.org/abs/2608.26158",
    "source": "Muhammad Toheed Fayyaz, Abdul Jabbar, Faheem Ahmad Qureshi, Syed Qaisar Jalil",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26158v1 Announce Type: new Abstract: This paper provides a controlled comparison of six information bar types (dollar, volume, volatility, range, Renko, and hybrid bars) constructed from bo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26174",
    "domain": "金融",
    "title": "Forecasting Economically Significant Bitcoin Moves: A Multi-Scale TCN with Profit-Optimized Thresholds",
    "url": "https://arxiv.org/abs/2608.26174",
    "source": "Parsa Yousefnezhad, Gholamreza Mansourfar, Mohammadreza Feizi Derakhshi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26174v1 Announce Type: new Abstract: Bitcoin's future fluctuations are a substantial concern for investments and risk management. Investors and financial institutions require accurate forec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26358",
    "domain": "金融",
    "title": "An Anonymized Urn-Based Experimental Dataset on Decision-Making under Risk and Ambiguity",
    "url": "https://arxiv.org/abs/2608.26358",
    "source": "V\\'aclav Kratochv\\'il, Radim Jirou\\v{s}ek, Kl\\'ara \\v{S}im\\r{u}nkov\\'a, Simona Ba\\v{z}antov\\'a",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26358v1 Announce Type: new Abstract: This data paper describes an anonymized release derived from controlled behavioral experiments on decision-making under risk (known probabilities) and a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26426",
    "domain": "金融",
    "title": "The Italian Municipality Equitable and Sustainable Well-being Index (MESWI)",
    "url": "https://arxiv.org/abs/2608.26426",
    "source": "Nicola Caravaggio, Giuliano Resce, Agapito Emanuele Santangelo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26426v1 Announce Type: new Abstract: This paper develops the Municipal Equitable and Sustainable Well-being Index (MESWI) for all Italian municipalities, extending the 12-domain BES framewo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26473",
    "domain": "金融",
    "title": "DTD-VAE: Disentangled Temporal Dependencies VAE for Credit Risk Prediction",
    "url": "https://arxiv.org/abs/2608.26473",
    "source": "Xiaobo Guo, Lu-an Dong, Yanbo Wang, Peng Zhang, Cai Zhi, Youru Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26473v1 Announce Type: new Abstract: Evaluating customer creditworthiness is crucial for retail banking operations, as it impacts marketing strategies, customer relationship management, and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26837",
    "domain": "金融",
    "title": "Interpretable hybrid credit scoring for thin-file and underbanked populations",
    "url": "https://arxiv.org/abs/2608.26837",
    "source": "Belise Kanziga, Ya\\'e U. Gaba, Olivier Kanamugire",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26837v1 Announce Type: new Abstract: We extend a residual-learning hybrid credit scoring framework (logistic regression scorecard plus a gradient-boosting correction on its residuals, decom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26924",
    "domain": "金融",
    "title": "The Pulse Beneath the Job Title: Monthly Readings of Requirements and Tasks from 750 Million Chinese Job Ads",
    "url": "https://arxiv.org/abs/2608.26924",
    "source": "Qin Chen, Ying Fang, Xiangyu Wang, Leo Yang Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.26924v1 Announce Type: new Abstract: How do we define an occupation? By its job title? An accountant at a small trading company keeps the books; at a listed firm the same title demands a ce"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27229",
    "domain": "金融",
    "title": "On the approximation of posterior laws in compound loss models by conditional Wasserstein GANs",
    "url": "https://arxiv.org/abs/2608.27229",
    "source": "Aleksandar Arandjelovic, Pavel V. Shevchenko, George Tzougas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.27229v1 Announce Type: new Abstract: Bayesian inference in compound loss models must often be repeated across policies, market scenarios, and prior specifications. Outside conjugate cases, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27295",
    "domain": "金融",
    "title": "A Temporal Multiplex Graph Neural Network for Systemic Risk Transmission in Global Banking",
    "url": "https://arxiv.org/abs/2608.27295",
    "source": "Nneka Umeorah, Tolulope Fadina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.27295v1 Announce Type: new Abstract: This paper develops a unified framework for assessing systemic risk and identifying contagion channels in the global banking system using a Temporal Het"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27076",
    "domain": "金融",
    "title": "Tabular Deep Learning for Algorithmic Trading: Cross-Regime Bayesian Optimisation for Equity Signal Generation",
    "url": "https://arxiv.org/abs/2608.27076",
    "source": "Joshua Le Grice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.27076v1 Announce Type: cross Abstract: Algorithmic trading now represents a market exceeding $20 billion, where even marginal gains in signal robustness can translate into economically sign"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27156",
    "domain": "金融",
    "title": "Traveling Waves in Equity Markets with Rank-Based Entry and Exit",
    "url": "https://arxiv.org/abs/2608.27156",
    "source": "Graeme Baker, Caroline Smyth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.27156v1 Announce Type: cross Abstract: We model equity markets using geometric Brownian particles entering and exiting at rank-dependent intensities. In the many-firm limit, the capital dis"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27364",
    "domain": "金融",
    "title": "Sophistication in GenAI Use: Field Evidence from a Large Firm",
    "url": "https://arxiv.org/abs/2608.27364",
    "source": "Nicholas J. Hallman, Zachary T. Kowaleski, Anu Puvvada, Jaime J. Schmidt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.27364v1 Announce Type: cross Abstract: We study how sophistication in generative AI (genAI) use varies among the back-office workforce of a large firm. Using proprietary data, we observe 71"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27374",
    "domain": "金融",
    "title": "Distribution-constrained optimal multiple stopping: the Root-type solution",
    "url": "https://arxiv.org/abs/2608.27374",
    "source": "Shuoqing Deng, Daxin Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.27374v1 Announce Type: cross Abstract: We consider the distribution-constrained optimal stopping problem introduced by Bayraktar and Miller (Mathematical Finance, 2019) and Beiglbock et al."
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.03230",
    "domain": "金融",
    "title": "To Bubble or Not to Bubble: Asset Price Dynamics and Optimality in OLG Economies",
    "url": "https://arxiv.org/abs/2508.03230",
    "source": "Stefano Bosi (UEVE), Cuong Le Van (CES, PSE), Ngoc-Sang Pham (EM Normandie)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2508.03230v3 Announce Type: replace Abstract: We study an overlapping generations (OLG) exchange economy with an asset that yields dividends. First, we derive general conditions, based on exogen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.16448",
    "domain": "金融",
    "title": "On the Expected Maximum Deficit and the Optimal Allocation of Reserves",
    "url": "https://arxiv.org/abs/2605.16448",
    "source": "Claude Lefevre, Pierre Zuyderhoff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2605.16448v3 Announce Type: replace Abstract: Let $L=(L_s)_{0\\le s\\le t}$ be a cumulative net-loss process and let $M_t=\\sup_{0\\le s\\le t}L_s$. For a candidate reserve $u$ and a distortion funct"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15667",
    "domain": "金融",
    "title": "Scalable Pontryagin-Guided Adjoint-to-Control Recovery for Constrained Dynamic Portfolio Choice",
    "url": "https://arxiv.org/abs/2608.15667",
    "source": "Jaegi Jeon, Jeonggyu Huh, Hyeng Keun Koo, Byung Hwa Lim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.15667v2 Announce Type: replace Abstract: We study continuous-time multi-asset portfolio choice and consumption under smooth pointwise constraints, including state-dependent feasible sets. T"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.09773",
    "domain": "金融",
    "title": "Global universality via discrete-time signatures",
    "url": "https://arxiv.org/abs/2603.09773",
    "source": "Mihriban Ceylan, David J. Pr\\\"omel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2603.09773v2 Announce Type: replace-cross Abstract: We establish global universal approximation theorems for non-anticipative and general path-dependent functionals on spaces of piecewise linear"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.23955",
    "domain": "金融",
    "title": "From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems",
    "url": "https://arxiv.org/abs/2605.23955",
    "source": "Ruizhe Zhou, Xiaoyang Liu, Gaoyuan Du, Yi Zheng, Shouxi Ren, Deepayan Chakrabarti, Dengdu Jiang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2605.23955v4 Announce Type: replace-cross Abstract: Deploying machine learning in regulated financial environments -- credit risk, fraud detection, and anti-money laundering -- exposes critical "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17808",
    "domain": "金融",
    "title": "Self-Consistent Adjoint Policy Iteration for Constrained Dynamic Portfolio Choice",
    "url": "https://arxiv.org/abs/2608.17808",
    "source": "Jeonggyu Huh, Yeoneung Kim, Seungwon Jeong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T04:00:00+00:00",
    "summary": "arXiv:2608.17808v2 Announce Type: replace-cross Abstract: We develop simulation-based policy iteration for continuous-time portfolio choice with predictable returns and convex constraints. Each outer "
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
    "id": "hn:49414279",
    "domain": "金融",
    "title": "Tesla discontinues its Solar Roof tiles, not economically viable",
    "url": "https://electrek.co/2026/08/20/tesla-discontinues-solar-roof-panels-only/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-24T01:21:56+00:00",
    "summary": ""
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
  }
]
```
