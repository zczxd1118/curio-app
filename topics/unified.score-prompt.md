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

- 今日日期：`2026-08-27`
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
  "date": "2026-08-27",
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
    "points": 4358219,
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
    "points": 1760553,
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
    "points": 1342662,
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
    "points": 1197963,
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
    "points": 1113609,
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
    "points": 1070350,
    "published_at": "2026-08-14T12:00:00+00:00",
    "summary": "AI 办公到底能干些啥？它真的能颠覆我们的工作方式，以至于让大厂押上身家也要卷吗？"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 647810,
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
    "points": 617285,
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
    "points": 440371,
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
    "points": 256908,
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
    "points": 248395,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 183012,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 180379,
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
    "points": 180030,
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
    "points": 169728,
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
    "points": 161360,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 147402,
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
    "points": 100892,
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
    "points": 97831,
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
    "points": 93397,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74207,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 68987,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
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
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41110,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "harness使用教程-",
    "platform": "bilibili",
    "points": 35243,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 32589,
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
    "points": 30358,
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
    "points": 29669,
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
    "points": 28895,
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
    "points": 26823,
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
    "points": 22744,
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
    "points": 20326,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1CY8w6WEkU",
    "domain": "AI",
    "title": "【全套教程】B站最全最细的AI Agent零基础全套教程（包含Agent+RAG+MCP+LangChain+LangGraph+智能体+企业级项目实战等）",
    "url": "http://www.bilibili.com/video/av117127231181858",
    "source": "AI大模型全栈",
    "platform": "bilibili",
    "points": 19309,
    "published_at": "2026-08-20T10:06:44+00:00",
    "summary": "配套课件/代码笔记：后台私信up主→发送暗号【11】即可！允许礼貌白嫖，先到先得！\n【全栈 AI 大模型工程师】 本套 AI 大模型系统教程专为零基础用户打造，全方位覆盖了从 LLM 底层原理到 Prompt 提示词工程、以及 2026 热门 AI Agent 智能体构建的实战全流程，不仅包含 DeepSeek、Claude、OpenClaw 等前沿模型的高效使用技巧，更深度解析了私有化部署、知识"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17857,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16504,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1LBbZ6eEJZ",
    "domain": "AI",
    "title": "正面对决！DeepSeek Harness 发布 | Agent到底哪家强",
    "url": "http://www.bilibili.com/video/av117125167516993",
    "source": "卡卡老师讲数据科学",
    "platform": "bilibili",
    "points": 14981,
    "published_at": "2026-08-20T01:11:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1jqB9B3Edn",
    "domain": "AI",
    "title": "Claude Code+AI语音输入法：不需要手速，照样交付",
    "url": "http://www.bilibili.com/video/av115781178235411",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 14007,
    "published_at": "2025-12-26T10:00:00+00:00",
    "summary": "这期我把“键盘吃灰”的工作流完整演示一遍：\n用「闪电说」把需求直接说出来，再让 AI 按“可交付”的方式把 PPT 演示网站做完。\n\n✅ 你会学到的核心方法\n\nClaude Code：先 Planning 再写代码\n先拆任务清单 + 每一步怎么验证（单测/E2E/验收点），返工直接少一大截\n\nSkill = 装备栏（按场景掏工具）\nskill-creator（快速造技能） / frontend-d"
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
    "id": "bvid:BV1TRcTzXE6k",
    "domain": "AI",
    "title": "Claude Code + Pencil 干完了前端的活",
    "url": "http://www.bilibili.com/video/av116040302395704",
    "source": "退役程序员",
    "platform": "bilibili",
    "points": 11427,
    "published_at": "2026-02-09T10:56:11+00:00",
    "summary": "#claudecode\n#2026拜年纪\n#程序员\n#AI"
  },
  {
    "id": "bvid:BV1FJ8Z66EfF",
    "domain": "AI",
    "title": "🚀OpenAI划时代独创新协议：WebMCP让网站主动暴露工具给AI Agent调用！新浏览器插件深度实测：Codex直接进入Chrome侧边栏！实测论文分析",
    "url": "http://www.bilibili.com/video/av117162530312233",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 11291,
    "published_at": "2026-08-26T15:35:37+00:00",
    "summary": "视频简介：\n\nWebMCP 到底是什么？我实测 OpenAI 官方 Demo，网站一次暴露 10 个工具，Codex 不靠模拟点击也能创建和修改文档\nAtlas 下架之后，OpenAI 又给出了新的浏览器方案。这次我直接把新的浏览器插件装上实测了一遍：Codex 可以出现在浏览器侧边栏里，分析当前网页、arXiv 论文和图片，也可以翻译选中的内容，甚至把前面的论文分析通过 Notion 插件保存成"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11052,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 9475,
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
    "points": 9428,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8882,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1nChG6nEY4",
    "domain": "AI",
    "title": "韦东山老师教你用 DeepSeek 与 Claude Code，在 Ubuntu 中搭建嵌入式 Linux AI 开发环境：从安装配置到代码智能辅助开发实战",
    "url": "http://www.bilibili.com/video/av117155165177009",
    "source": "韦东山",
    "platform": "bilibili",
    "points": 8623,
    "published_at": "2026-08-25T08:22:35+00:00",
    "summary": "韦东山老师手把手教你在 Ubuntu 中搭建嵌入式 AI 开发环境，完整介绍开发工具、VMware Tools、中文输入法、VS Code 与常用插件的安装配置，以及 DeepSeek API Key 和 Claude Code 的接入方法。借助 AI 大模型完成代码分析、工程理解、问题排查和辅助开发，让嵌入式 Linux 学习与开发更加高效。\n查看完整文字教程：https://www.100as"
  },
  {
    "id": "bvid:BV1EEM96uEPP",
    "domain": "AI",
    "title": "【逆向】掌握MCP功能使用修改分析，成为逆向高手！",
    "url": "http://www.bilibili.com/video/av117030460131623",
    "source": "009安乐",
    "platform": "bilibili",
    "points": 8099,
    "published_at": "2026-08-03T07:47:28+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 7912,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 7629,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 7613,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1zcTTznEL8",
    "domain": "AI",
    "title": "MCP应用：为小智增加在线点歌服务",
    "url": "http://www.bilibili.com/video/av114635462156272",
    "source": "无敌哥-AI治理架构师",
    "platform": "bilibili",
    "points": 7416,
    "published_at": "2025-06-06T08:30:10+00:00",
    "summary": "除了对话、人脸识别、摄像头识别场景多模态交互外！其实，听音乐是我们的刚需，今天就给小智加上！背后利用了MCP ，话说MCP 真实为小智增加了无线可能！大家有啥想法，可以尽管提哈！"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1481,
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
    "points": 581,
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
    "id": "hn:49447878",
    "domain": "AI 算力 / 半导体",
    "title": "Who bears the risk in Nvidia's $500B financing platform?",
    "url": "https://www.sascha-steffen.de/updates/nvidia-500bn-ai-financing-credit-risk",
    "source": "rwmj",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-08-26T12:32:31+00:00",
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
    "id": "rss:https://www.eetimes.com/reliable-power-path-design-integrating-mosfets-diodes-tvs-devices-and-capacitors/",
    "domain": "AI 算力 / 半导体",
    "title": "Reliable Power-Path Design: Integrating MOSFETs, Diodes, TVS Devices, and Capacitors",
    "url": "https://www.eetimes.com/reliable-power-path-design-integrating-mosfets-diodes-tvs-devices-and-capacitors/",
    "source": "Unikey Electronics Pte. Ltd.",
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
    "id": "rss:https://www.eetimes.com/from-days-to-minutes-accelerating-3d-ic-debug-with-agentic-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "From Days to Minutes: Accelerating 3D IC Debug with Agentic AI",
    "url": "https://www.eetimes.com/from-days-to-minutes-accelerating-3d-ic-debug-with-agentic-ai/",
    "source": "Zackary Glazewski, Founding AI Engineer, ChipAgents",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:00:00+00:00",
    "summary": "Discover how agentic AI cuts 3D IC debugging from days to minutes. Learn multi-agent orchestration techniques to accelerate end-to-end root cause analysis. The post From Days to Minutes: Accelerating "
  },
  {
    "id": "rss:https://www.eetimes.com/accelerating-silicon-design-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Accelerating Silicon Design for Physical AI",
    "url": "https://www.eetimes.com/accelerating-silicon-design-for-physical-ai/",
    "source": "Cadence Design Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T12:00:00+00:00",
    "summary": "Physical AI systems must perceive, reason, and act at once, under tight real-time latency and power budgets. That workload diversity breaks the one-processor model, widens the gap between trained mode"
  },
  {
    "id": "rss:https://www.eetimes.com/indias-osat-atmp-build-out-from-legacy-packages-to-2-5d/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s OSAT-ATMP Build-Out: From Legacy Packages to 2.5D",
    "url": "https://www.eetimes.com/indias-osat-atmp-build-out-from-legacy-packages-to-2-5d/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T07:00:00+00:00",
    "summary": "ASIP Technologies has begun construction of an OSAT facility in Visakhapatnam, Andhra Pradesh, with Korean partner APACT. The post India’s OSAT-ATMP Build-Out: From Legacy Packages to 2.5D appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/the-complete-iot-mesh-solution-making-wi-sun-deployments-simple/",
    "domain": "AI 算力 / 半导体",
    "title": "The Complete IoT Mesh Solution: Making Wi-SUN Deployments Simple",
    "url": "https://www.eetimes.com/the-complete-iot-mesh-solution-making-wi-sun-deployments-simple/",
    "source": "Digi, Silicon Labs, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T16:31:04+00:00",
    "summary": "Join us for a technical walkthrough of the Digi XBee for Wi-SUN platform and a live demo showing how quickly you can go from development kit to a fully managed, self-healing mesh network ready for pro"
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
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/usd215-discount-turns-corsairs-ddr5-6000-vengeance-memory-kit-into-the-cheapest-32gb-of-ram-at-those-speeds-35-percent-saving-as-stock-dwindles-and-prices-continue-to-rise",
    "domain": "AI 算力 / 半导体",
    "title": "$215 discount turns Corsair's DDR5-6000 Vengeance memory kit into the cheapest 32GB of RAM at those speeds — 35% saving as stock dwindles and prices continue to rise",
    "url": "https://www.tomshardware.com/pc-components/ddr5/usd215-discount-turns-corsairs-ddr5-6000-vengeance-memory-kit-into-the-cheapest-32gb-of-ram-at-those-speeds-35-percent-saving-as-stock-dwindles-and-prices-continue-to-rise",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T10:44:57+00:00",
    "summary": "Corsair's Vengeance DDR5-6000 memory kit becomes the cheapest 32GB kit you can buy after a large $215 discount."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/beat-pc-component-price-rises-with-this-unbelievably-good-value-9800x3d-gaming-desktop-get-an-rtx-5070-32gb-of-ddr5-and-a-2tb-ssd-all-for-less-than-usd2-000",
    "domain": "AI 算力 / 半导体",
    "title": "Beat PC component price rises with this unbelievably good value 9800X3D gaming desktop — get an RTX 5070, 32GB of DDR5, and a 2TB SSD all for less than $2,000",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/beat-pc-component-price-rises-with-this-unbelievably-good-value-9800x3d-gaming-desktop-get-an-rtx-5070-32gb-of-ddr5-and-a-2tb-ssd-all-for-less-than-usd2-000",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T10:44:47+00:00",
    "summary": "Get an RTX 5070, 9800X3D gaming PC with 32GB of DDR5 and a 2TB SSD for $1,999."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/resurrected-rtx-3060-12gb-price-jumps-45-percent-in-the-two-months-since-it-was-revived-2021-era-gpu-now-costs-nearly-usd500-across-most-retailers",
    "domain": "AI 算力 / 半导体",
    "title": "Resurrected RTX 3060 12GB price jumps 45% in the two months since it was revived — 2021-era GPU now costs nearly $500 across most retailers",
    "url": "https://www.tomshardware.com/pc-components/gpus/resurrected-rtx-3060-12gb-price-jumps-45-percent-in-the-two-months-since-it-was-revived-2021-era-gpu-now-costs-nearly-usd500-across-most-retailers",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T10:30:00+00:00",
    "summary": "The RTX 3060 12GB was revived to offer consumers a budget GPU with a relatively large VRAM pool, but it has succumbed to the same fate as every other SKU like it. Launched at around $330, most variant"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/hardware-modder-builds-overclocked-ps3-pro-v3-with-3d-printed-cooling-mod-dual-noctua-fans-and-server-heatsinks-provide-fps-boost-in-almost-every-game",
    "domain": "AI 算力 / 半导体",
    "title": "Hardware modder builds overclocked PS3 ‘Pro’ v3 with 3D-printed cooling mod — dual Noctua fans and server heatsinks provide FPS boost in 'almost every game'",
    "url": "https://www.tomshardware.com/video-games/playstation/hardware-modder-builds-overclocked-ps3-pro-v3-with-3d-printed-cooling-mod-dual-noctua-fans-and-server-heatsinks-provide-fps-boost-in-almost-every-game",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T10:00:00+00:00",
    "summary": "A Sony PlayStation 3 console modder has shared images and details of their faster, cooler, and quieter ‘PS3 Pro v3’ design."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/polls-show-us-data-center-resistance-is-due-to-concerns-over-object-level-local-environmental-impact-beliefs-and-political-affiliation-had-minimal-impact-on-ai-data-center-views",
    "domain": "AI 算力 / 半导体",
    "title": "Polls reveal local utility hikes and noise drive US data center protests, not anti-AI sentiment— beliefs and political affiliation had minimal impact on AI data center views",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/polls-show-us-data-center-resistance-is-due-to-concerns-over-object-level-local-environmental-impact-beliefs-and-political-affiliation-had-minimal-impact-on-ai-data-center-views",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T10:00:00+00:00",
    "summary": "Data centers are facing bipartisan resistance from across the nation, but what's the reason behind this? The answer seems to be deceptively simple."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/atari-drops-39-activision-games-on-cartridges-the-run-seamlessly-across-five-decades-of-hardware-ultimate-deluxe-collection-that-includes-every-title-clocks-in-at-usd999-96",
    "domain": "AI 算力 / 半导体",
    "title": "Atari revives 39 Activision games on cartridges that run seamlessly across five decades of hardware — Ultimate Deluxe collection that includes every title costs a wild $999.96",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/atari-drops-39-activision-games-on-cartridges-the-run-seamlessly-across-five-decades-of-hardware-ultimate-deluxe-collection-that-includes-every-title-clocks-in-at-usd999-96",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T09:30:00+00:00",
    "summary": "Atari teams up with Activision to launch the Atari x Activision Collection, featuring 39 iconic Activision titles."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-revenue-tops-usd96-billion-as-memory-commitments-soar-to-usd160-billion-ceo-jensen-huang-says-ai-has-reached-its-inflection-point",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia revenue tops $96 billion as memory commitments soar to $160 billion — CEO Jensen Huang says AI 'has reached its inflection point'",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-revenue-tops-usd96-billion-as-memory-commitments-soar-to-usd160-billion-ceo-jensen-huang-says-ai-has-reached-its-inflection-point",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T09:13:54+00:00",
    "summary": "Nvidia's Q2 FY2027 revenue tops $96 billion as the company commits to buy up to $160 billion worth of memory, increasing its total commitments to $279 billion ahead of a major demand bump."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/nvidia-custom-nvhbm-promises-30-percent-higher-bandwidth-15-percent-lower-power-than-commodity-hbm4e-custom-base-die-and-phy-will-be-available-to-nvlink-fusion-partners",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia custom 'NVHBM' promises 30% higher bandwidth, 15% lower power than commodity HBM4e — custom base die and PHY will be available to NVLink Fusion partners",
    "url": "https://www.tomshardware.com/pc-components/dram/nvidia-custom-nvhbm-promises-30-percent-higher-bandwidth-15-percent-lower-power-than-commodity-hbm4e-custom-base-die-and-phy-will-be-available-to-nvlink-fusion-partners",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T22:45:22+00:00",
    "summary": "Nvidia has unveiled NVHBM, a custom high-bandwidth memory implementation that promises higher bandwidth and lower power for customers building chips within the NVLink Fusion partner program."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/nvidia-presents-groq-3-lpx-architecture-and-unveils-its-first-third-party-inference-benchmark",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Nvidia presents Groq 3 LPX architecture and unveils its first third-party inference benchmark — LP30-based rack already in production, company says",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/nvidia-presents-groq-3-lpx-architecture-and-unveils-its-first-third-party-inference-benchmark",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T16:23:37+00:00",
    "summary": "Igor Arsovski, now Nvidia's VP of hardware, presented the Groq 3 LPX rack's architecture and published the first third-party benchmark of the hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/us-justice-department-claims-chinese-state-sponsored-hackers-infiltrated-systems-at-nasa-senate-federal-reserve-and-more-fbi-moves-forward-with-domain-seizures",
    "domain": "AI 算力 / 半导体",
    "title": "US Justice Department seizes domains it says Chinese state-sponsored hackers used to infiltrate systems at NASA, Senate, Federal Reserve, and more — FBI moves forward with domain seizures",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/us-justice-department-claims-chinese-state-sponsored-hackers-infiltrated-systems-at-nasa-senate-federal-reserve-and-more-fbi-moves-forward-with-domain-seizures",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T15:49:45+00:00",
    "summary": "The U.S. Department of Justice and FBI announced domain seizures related to state-sponsored hacking activities that have impacted NASA, the Senate, and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/xbox-announces-new-disc-to-digital-feature-for-physical-media-lets-players-claim-digital-versions-of-their-games-with-support-for-play-anywhere-and-cloud-gaming",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox announces new disc-to-digital feature for physical media — lets players claim digital versions of their games, with support for Play Anywhere and Cloud Gaming",
    "url": "https://www.tomshardware.com/video-games/console-gaming/xbox-announces-new-disc-to-digital-feature-for-physical-media-lets-players-claim-digital-versions-of-their-games-with-support-for-play-anywhere-and-cloud-gaming",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T15:08:27+00:00",
    "summary": "Xbox announces new disc-to-digital feature for physical media"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/kansas-town-drops-charges-against-teacher-who-clapped-during-public-hearings-on-data-centers-says-that-case-has-been-dismissed-without-prejudice",
    "domain": "AI 算力 / 半导体",
    "title": "Kansas town drops charges against teacher arrested for clapping during public hearings on data centers — says that ‘case has been dismissed without prejudice’",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/kansas-town-drops-charges-against-teacher-who-clapped-during-public-hearings-on-data-centers-says-that-case-has-been-dismissed-without-prejudice",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T15:03:47+00:00",
    "summary": "The disorderly conduct case against Lux Claridge has been dropped by the city in municipal court, making the teacher breathe a little bit easier. However, it was done \"without prejudice,\" and the city"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/hot-chips-2026-nvidia-touts-benefits-of-its-dsx-maxlps-site-power-management-approach-tech-allows-for-more-compute-from-fixed-data-center-power-budgets",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Nvidia touts benefits of its DSX MaxLPS site power management approach — tech allows for more compute from fixed data center power budgets",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/hot-chips-2026-nvidia-touts-benefits-of-its-dsx-maxlps-site-power-management-approach-tech-allows-for-more-compute-from-fixed-data-center-power-budgets",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T14:42:10+00:00",
    "summary": "During Nvidia's Hot Chips presentation on the Rubin GPU, the company emphasized power as a hard limit on data center capacity and touted the amount of compute that Vera Rubin NVL72 systems can deliver"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd260-on-this-high-end-am5-gaming-combo-from-newegg-just-usd1-345-99-buys-a-ryzen-9-9950x3d-32gb-corsair-ddr5-ram-msi-x870e-carbon-wifi-motherboard-along-with-a-free-240mm-aio-and-amd-game-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Save $260 on this high-end AM5 gaming combo from Newegg — just $1,345.99 buys a Ryzen 9 9950X3D, 32GB Corsair DDR5 RAM, MSI X870E Carbon Wifi motherboard, along with a free 240mm AIO and AMD game bund",
    "url": "https://www.tomshardware.com/pc-components/save-usd260-on-this-high-end-am5-gaming-combo-from-newegg-just-usd1-345-99-buys-a-ryzen-9-9950x3d-32gb-corsair-ddr5-ram-msi-x870e-carbon-wifi-motherboard-along-with-a-free-240mm-aio-and-amd-game-bundle",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T14:00:00+00:00",
    "summary": "Newegg bundles the Ryzen 9 9950X3D, MSI X870E Carbon Wifi, and 32GB Corsair Vengeance DDR5-6000 for only $1,345.99 - a solid $259.99 off, plus a free 240mm AIO and AMD game bundle. A wicked deal for g"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/fujitsus-monaka-cpu-stacks-its-entire-cache-on-a-separate-5nm-die-and-narrows-to-256-bit-sve2",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Fujitsu's Monaka CPU stacks its entire cache on a separate 5nm die and narrows to 256-bit SVE2 — 350W and 500W SKUs due in 2027",
    "url": "https://www.tomshardware.com/pc-components/cpus/fujitsus-monaka-cpu-stacks-its-entire-cache-on-a-separate-5nm-die-and-narrows-to-256-bit-sve2",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:30:00+00:00",
    "summary": "Fujitsu gave us a detailed look at its 144-core Monaka server CPU at Hot Chips 2026 on August 24, confirming for the first time that the Arm chip runs dual 256-bit SVE2 vector units, down from the 512"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/crypto-bro-faces-280-years-in-prison-for-defrauding-investors-with-promises-of-an-ai-supercomputer-for-mining-jury-convicts-businessman-of-running-usd24-million-ponzi-scheme-claimed-up-to-30-percent-apr-and-a-100-percent-money-back-guarantee",
    "domain": "AI 算力 / 半导体",
    "title": "Crypto bro faces 280 years in prison for defrauding investors with promises of an 'AI supercomputer' for mining — jury convicts businessman of running $24-million Ponzi scheme, claimed up to 30% APR a",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/crypto-bro-faces-280-years-in-prison-for-defrauding-investors-with-promises-of-an-ai-supercomputer-for-mining-jury-convicts-businessman-of-running-usd24-million-ponzi-scheme-claimed-up-to-30-percent-apr-and-a-100-percent-money-back-guarantee",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:29:52+00:00",
    "summary": "A man claiming to give massive returns to investors has been found guilty of wire fraud, mail fraud, and money laundering by a Nevada court. Brent Kovar now faces up to 280 years behind bars for his c"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/xbox-marks-25-years-with-a-translucent-green-accessory-line-but-none-of-it-is-xbox-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox marks 25 years with eye-catching translucent green PC accessories — Razer mouse, keyboard, and earbuds available to pre-order now",
    "url": "https://www.tomshardware.com/video-games/console-gaming/xbox-marks-25-years-with-a-translucent-green-accessory-line-but-none-of-it-is-xbox-hardware",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:12:05+00:00",
    "summary": "Microsoft has opened preorders for the Designed for Xbox 25th Anniversary Collection."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/chuwi-unibook-review-a-budget-rival-to-the-macbook-neo-and-dell-xps-13",
    "domain": "AI 算力 / 半导体",
    "title": "Chuwi UniBook Review: A budget rival to the MacBook Neo and Dell XPS 13",
    "url": "https://www.tomshardware.com/laptops/chuwi-unibook-review-a-budget-rival-to-the-macbook-neo-and-dell-xps-13",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:05:00+00:00",
    "summary": "A budget-friendly ultraportable with premium aspirations, the Chuwi UniBook packs modern Intel hardware, excellent connectivity, and impressive battery life into a sleek metal chassis."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/hot-chips-2026-high-bandwidth-flash-promises-massive-bandwidth-and-capacity-but-its-usability-is-extremely-limited-new-memory-format-strikes-a-balance-between-hbm-and-nand-flash",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: High Bandwidth Flash promises massive bandwidth and capacity, but its usability is extremely limited — new memory format strikes a balance between HBM and NAND flash",
    "url": "https://www.tomshardware.com/pc-components/ssds/hot-chips-2026-high-bandwidth-flash-promises-massive-bandwidth-and-capacity-but-its-usability-is-extremely-limited-new-memory-format-strikes-a-balance-between-hbm-and-nand-flash",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T13:00:00+00:00",
    "summary": "OXMIQ presented its High Bandwidth Flash (HBF) use-case scenarios at Hot Chips 2026, which dramatically narrow the circumstances under which HBF makes sense."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/rockstar-releases-statement-after-a-week-of-gta-vi-leaks-avoids-mentioning-leakers-demands-says-that-gameplay-leaks-have-been-heartbreaking-for-our-team",
    "domain": "AI 算力 / 半导体",
    "title": "Rockstar releases statement after a week of GTA VI leaks, avoids mentioning leaker's demands — says that gameplay leaks have been ‘heartbreaking for our team’",
    "url": "https://www.tomshardware.com/video-games/rockstar-releases-statement-after-a-week-of-gta-vi-leaks-avoids-mentioning-leakers-demands-says-that-gameplay-leaks-have-been-heartbreaking-for-our-team",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T12:19:49+00:00",
    "summary": "The statement comes a day before GTA VI extended look drops on Netflix and about a week after leaks of gameplay clips and the entire map of Leonidas appeared on the internet."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/crucial-ssd-owner-offered-usd200-refund-for-4tb-drive-now-selling-for-over-usd500-company-finally-caves-to-warranty-demands-after-protracted-back-and-forth",
    "domain": "AI 算力 / 半导体",
    "title": "Crucial SSD owner offered $200 refund for 4TB drive now selling for over $500 — company finally caves to warranty demands after protracted back-and-forth",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/crucial-ssd-owner-offered-usd200-refund-for-4tb-drive-now-selling-for-over-usd500-company-finally-caves-to-warranty-demands-after-protracted-back-and-forth",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T12:05:03+00:00",
    "summary": "Micron initially told a customer that no replacement Crucial X9 4TB SSDs were available and offered a refund based on last year’s purchase price, but a firm pushback ultimately resulted in a replaceme"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card — TSMC 4nm compute die bonded face-to-face at a 36-micron pitch on top of a custom-designed die",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T12:00:00+00:00",
    "summary": "d-Matrix presented Raptor, which it calls the first 3D DRAM accelerator for generative inference, showing a TSMC 4nm compute die bonded face-to-face at a 36-micron pitch on top of a custom-designed DR"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/bill-gates-calls-for-some-jobs-to-be-human-reserved-suggests-taxing-ai-tokens-and-robots-billionaire-says-that-ai-era-will-be-one-of-the-most-turbulent-times-in-human-history",
    "domain": "AI 算力 / 半导体",
    "title": "Bill Gates calls for some jobs to be ‘Human Reserved,’ suggests taxing AI tokens and robots — billionaire says that ‘AI era will be one of the most turbulent times in human history’",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/bill-gates-calls-for-some-jobs-to-be-human-reserved-suggests-taxing-ai-tokens-and-robots-billionaire-says-that-ai-era-will-be-one-of-the-most-turbulent-times-in-human-history",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T11:34:04+00:00",
    "summary": "The billionaire philanthropist penned a 6,000-word essay raising the societal risks that AI bring and his proposed solutions to protect the average person."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/montech-titan-pla-750w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Montech Titan PLA 750W power supply review: A powerful and stunning all-white Seasonic-built Platinum unit",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/montech-titan-pla-750w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T11:05:00+00:00",
    "summary": "The Montech Titan PLA 750W is a Seasonic-built Platinum unit with extraordinary power quality, a rare full-bridge LLC topology at this wattage, and a white aesthetic that genuinely sets it apart."
  },
  {
    "id": "hn:49411178",
    "domain": "AI 算力 / 半导体",
    "title": "Etched Sohu vs. Nvidia: Transformer ASIC vs. GPU (2026)",
    "url": "https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-08-23T18:27:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49417669",
    "domain": "AI 算力 / 半导体",
    "title": "Some of Russia's A.I. Drones Are Powered by Nvidia",
    "url": "https://www.nytimes.com/2026/08/24/world/europe/ukraine-war-nvidia-ai-autonomous-drones.html",
    "source": "reaperducer",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-24T10:16:03+00:00",
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
    "id": "rss:https://www.eetimes.com/engineering-fiber-optic-solutions-for-next-generation-space-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Engineering Fiber Optic Solutions for Next-Generation Space Applications",
    "url": "https://www.eetimes.com/engineering-fiber-optic-solutions-for-next-generation-space-applications/",
    "source": "TE Connectivity",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T14:00:00+00:00",
    "summary": "As satellite systems demand greater bandwidth, lower weight, and higher reliability, engineers face significant challenges when integrating fiber optics into space-qualified platforms. This case study"
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
    "id": "rss:https://www.theverge.com/gadgets/985549/hugging-face-microduck-robot",
    "domain": "大厂 AI 动态",
    "title": "Hugging Face’s new robot is an adorable rollerskating duck",
    "url": "https://www.theverge.com/gadgets/985549/hugging-face-microduck-robot",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:44:00+00:00",
    "summary": "Hugging Face's Pollen Robotics has launched its second cute AI robot, the Microduck, a one-eyed biped standing just under 10 inches tall. It's available to preorder now for $399 in cream, graphite, la"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/985500/plaud-one-earbuds-ai-recorder-price-availability",
    "domain": "大厂 AI 动态",
    "title": "Plaud is launching AI earbuds",
    "url": "https://www.theverge.com/ai-artificial-intelligence/985500/plaud-one-earbuds-ai-recorder-price-availability",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:11:23+00:00",
    "summary": "Plaud has introduced a new AI wearable that's designed to record, transcribe, and summarize your conversations, only this time it looks like earbuds instead of a pin. The Plaud One Explorer Edition ca"
  },
  {
    "id": "rss:https://www.theverge.com/tech/985491/adobe-photoshop-ai-assisted-editor-markup",
    "domain": "大厂 AI 动态",
    "title": "Adobe is adding more AI to Photoshop",
    "url": "https://www.theverge.com/tech/985491/adobe-photoshop-ai-assisted-editor-markup",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:00:00+00:00",
    "summary": "Adobe is rolling out an AI-heavy update for Photoshop that includes a new \"optional\" interface dedicated to its AI tools. Launching in beta, the \"AI Assisted Editor\" view will show all of Photoshop's "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/984728/sleep-score-court-is-in-session-pixel-watch",
    "domain": "大厂 AI 动态",
    "title": "Sleep score court is in session",
    "url": "https://www.theverge.com/gadgets/984728/sleep-score-court-is-in-session-pixel-watch",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:00:00+00:00",
    "summary": "Your honor, We all know that the woman who sits before you is tired. Just look at the circles under her eyes. The novelty Pride and Prejudice T-shirt and Muji sweatpants that pass for pajamas. The unk"
  },
  {
    "id": "rss:https://www.theverge.com/report/985187/samsung-galaxy-s26-fe-hands-on-preview-specs-features-design",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s Galaxy S26 FE pairs last year’s hardware with last month’s software",
    "url": "https://www.theverge.com/report/985187/samsung-galaxy-s26-fe-hands-on-preview-specs-features-design",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:00:00+00:00",
    "summary": "The Fan Edition phones are rarely Samsung's most exciting launches of the year, but the new Galaxy S26 FE feels especially familiar. Hardware-wise, little has changed since the S25 FE launched 12 mont"
  },
  {
    "id": "rss:https://www.theverge.com/tech/985476/samsung-odyssey-gaming-monitors-2027-lineup-launch",
    "domain": "大厂 AI 动态",
    "title": "Of course Samsung made a 1,100Hz gaming monitor",
    "url": "https://www.theverge.com/tech/985476/samsung-odyssey-gaming-monitors-2027-lineup-launch",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:38:10+00:00",
    "summary": "Samsung announced its upcoming lineup of Odyssey gaming monitors today at Gamescom, and says that several will feature \"world-first innovations\" across display speeds and design. This includes the 27-"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/984927/xiaomi-redmi-note-17-pro-max-9210mah-battery",
    "domain": "大厂 AI 动态",
    "title": "Xiaomi’s new Redmi phone lasts for three days on a single charge",
    "url": "https://www.theverge.com/gadgets/984927/xiaomi-redmi-note-17-pro-max-9210mah-battery",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:00:00+00:00",
    "summary": "The 9,210mAh dual-cell battery in the new Redmi Note 17 Pro Max is the biggest that Xiaomi has fit in any phone it's sold in Europe - and remarkably, in some other markets the phone comes with an even"
  },
  {
    "id": "rss:https://www.theverge.com/tech/985387/nvidia-hundred-billion-dollar-quarterly-revenue",
    "domain": "大厂 AI 动态",
    "title": "Nvidia is about to be a hundred-billion-dollar-a-quarter company",
    "url": "https://www.theverge.com/tech/985387/nvidia-hundred-billion-dollar-quarterly-revenue",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T21:40:53+00:00",
    "summary": "Nvidia's predicting it will pull in $108 billion in revenue within just a few months. It wouldn't be the first company to rake in over $100 billion in quarterly revenue - Amazon, Apple, and Alphabet h"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/985385/openais-rogue-ai-model-hugging-face-cybersecurity-incident-reports-metr",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s rogue AI model incident was worse than we thought",
    "url": "https://www.theverge.com/ai-artificial-intelligence/985385/openais-rogue-ai-model-hugging-face-cybersecurity-incident-reports-metr",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T21:36:06+00:00",
    "summary": "In July, an unreleased OpenAI model broke out of a restricted environment, figured out how to get access to the internet, allowed AI agents to talk to each other using a secret \"message board,\" and ha"
  },
  {
    "id": "rss:https://www.theverge.com/tech/985329/instagram-facebook-meta-settlement-changes",
    "domain": "大厂 AI 动态",
    "title": "All the ways Instagram and Facebook are changing for teens",
    "url": "https://www.theverge.com/tech/985329/instagram-facebook-meta-settlement-changes",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T20:00:00+00:00",
    "summary": "Meta just agreed to make sweeping changes for teens as part of a child safety settlement reached with attorneys general across the US. Under the agreement, Meta must apply new safeguards across Instag"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/heres-all-the-times-ai-has-gone-rogue-and-hacked-other-companies/",
    "domain": "大厂 AI 动态",
    "title": "Here’s all the times AI has gone rogue and hacked other companies",
    "url": "https://techcrunch.com/2026/08/27/heres-all-the-times-ai-has-gone-rogue-and-hacked-other-companies/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T14:01:42+00:00",
    "summary": "A recap of all the incidents involving LLMs made by Anthropic, Meta, and OpenAI, which went rogue and attacked real companies and individuals on the internet."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/plauds-new-earphones-come-with-an-esim-enabled-case-for-talking-to-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Plaud’s new earphones come with an eSIM-enabled case for talking to AI agents",
    "url": "https://techcrunch.com/2026/08/27/plauds-new-earphones-come-with-an-esim-enabled-case-for-talking-to-ai-agents/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:00:00+00:00",
    "summary": "Plaud's new 'agentic' earbuds are priced at $249."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/27/openai-to-start-showing-ads-on-chatgpts-free-and-go-tiers-in-india/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI to start showing ads on ChatGPT’s free and Go tiers in India",
    "url": "https://techcrunch.com/2026/08/27/openai-to-start-showing-ads-on-chatgpts-free-and-go-tiers-in-india/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:35:59+00:00",
    "summary": "OpenAI has more than 100 million weekly active ChatGPT users in India, a huge chunk of whom are on the free or the lower-priced Go tiers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia closes in on Hugging Face acquisition",
    "url": "https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T06:32:51+00:00",
    "summary": "Nvidia has reportedly agreed to buy Hugging Face, the popular open-source AI hub, for $12.9 billion in a move that would let Nvidia both protect its chip empire and jump back into the cloud business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Viral AI startup Instinct has raised $350M at a $2.5B valuation",
    "url": "https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T00:24:57+00:00",
    "summary": "The startup is only a year old but it has already generated a massive amount of hype (and money) while also spurring privacy concerns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/amazon-just-tripled-its-order-of-nvidia-chips-over-surging-demand/",
    "domain": "大厂 AI 动态",
    "title": "Amazon just tripled its order of Nvidia chips over ‘surging demand’",
    "url": "https://techcrunch.com/2026/08/26/amazon-just-tripled-its-order-of-nvidia-chips-over-surging-demand/",
    "source": "Rebecca Bellan, Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T23:47:18+00:00",
    "summary": "Amazon is adding another 2 million Nvidia GPU chips to its data centers over the next two years. But this extended partnerships stretches beyond buying more chips."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/metas-18b-child-safety-deal-hinges-on-age-verification-tech-that-doesnt-work-well/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s $18B child-safety deal hinges on age-verification tech that doesn’t work well",
    "url": "https://techcrunch.com/2026/08/26/metas-18b-child-safety-deal-hinges-on-age-verification-tech-that-doesnt-work-well/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T22:47:58+00:00",
    "summary": "The historic settlement reignites ongoing concern around how age-verification technology puts privacy at risk."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/anthropic-continues-compute-gobbling-streak-in-45-billion-deal-with-nscale/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic continues compute-gobbling streak in $45B deal with Nscale",
    "url": "https://techcrunch.com/2026/08/26/anthropic-continues-compute-gobbling-streak-in-45-billion-deal-with-nscale/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T21:37:39+00:00",
    "summary": "The new deal with the infrastructure provider is the latest example of Anthropic's white-hot compute-gobbling streak."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/googles-gemini-has-a-branding-problem-and-so-does-the-rest-of-ai/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Gemini has a branding problem, and so does the rest of AI",
    "url": "https://techcrunch.com/2026/08/26/googles-gemini-has-a-branding-problem-and-so-does-the-rest-of-ai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T19:37:34+00:00",
    "summary": "Consumer AI apps need to stop making users learn their product architecture."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/how-do-we-explain-openais-executive-exodus/",
    "domain": "大厂 AI 动态",
    "title": "How do we explain OpenAI’s executive exodus?",
    "url": "https://techcrunch.com/2026/08/26/how-do-we-explain-openais-executive-exodus/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T19:34:04+00:00",
    "summary": "Was Greg Brockman the right executive all along?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/openai-releases-its-official-report-on-the-hugging-face-breach/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI releases its official report on the Hugging Face breach",
    "url": "https://techcrunch.com/2026/08/26/openai-releases-its-official-report-on-the-hugging-face-breach/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T19:05:22+00:00",
    "summary": "The report, which spans several discrete cybersecurity compromises, is the most complete accounting of the incident to date."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/flipboard-acquires-graze-the-feed-builder-working-to-monetize-the-open-social-web/",
    "domain": "大厂 AI 动态",
    "title": "Flipboard acquires Graze, the feed builder working to monetize the open social web",
    "url": "https://techcrunch.com/2026/08/26/flipboard-acquires-graze-the-feed-builder-working-to-monetize-the-open-social-web/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T18:35:40+00:00",
    "summary": "Flipboard is acquiring Bluesky feed-building startup Graze, bringing its privacy-friendly ad technology and creator monetization tools into Flipboard’s growing open social web ecosystem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/medical-device-maker-boston-scientific-says-a-cyberattack-is-causing-a-global-disruption-to-its-operations/",
    "domain": "大厂 AI 动态",
    "title": "Medical device maker Boston Scientific says a cyberattack is causing a ‘global disruption’ to its operations",
    "url": "https://techcrunch.com/2026/08/26/medical-device-maker-boston-scientific-says-a-cyberattack-is-causing-a-global-disruption-to-its-operations/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T18:23:09+00:00",
    "summary": "The company won't say if medical devices are affected or if any customer data was exfiltrated."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/us-seizes-domains-of-chinese-botnet-used-to-hack-nasa-justice-department-and-the-senate/",
    "domain": "大厂 AI 动态",
    "title": "US seizes domains of Chinese botnet used to target NASA, Justice Department, and the Senate",
    "url": "https://techcrunch.com/2026/08/26/us-seizes-domains-of-chinese-botnet-used-to-hack-nasa-justice-department-and-the-senate/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T17:01:05+00:00",
    "summary": "The Justice Department said that the domain seizures made the botnet and its command and control servers \"inoperable,\" as the domains were hardcoded into the botnet's code and were critical for the bo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/capital-f-closes-17m-debut-fund-with-goal-to-back-the-future-of-the-female-economy/",
    "domain": "大厂 AI 动态",
    "title": "Capital F closes $17M debut fund with goal to back the future of the ‘female economy’",
    "url": "https://techcrunch.com/2026/08/26/capital-f-closes-17m-debut-fund-with-goal-to-back-the-future-of-the-female-economy/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T17:00:00+00:00",
    "summary": "The firm backs companies building in the “female economy,” or the markets where women drive demand — women’s health, digital commerce, and AI tools."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/apple-is-holding-its-iphone-launch-event-on-september-9/",
    "domain": "大厂 AI 动态",
    "title": "Apple is holding its iPhone launch event on September 9",
    "url": "https://techcrunch.com/2026/08/26/apple-is-holding-its-iphone-launch-event-on-september-9/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T16:53:07+00:00",
    "summary": "The event is expected to be a notable one, as Apple is rumored to unveil its long-awaited foldable iPhone. It'll also be the first Apple event with John Ternus as CEO, who is scheduled to take the rei"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/meta-agrees-to-sweeping-changes-to-restrict-kids-access-to-its-apps-as-part-of-settlement-with-states/",
    "domain": "大厂 AI 动态",
    "title": "Meta agrees to sweeping changes to restrict kids’ access to its apps as part of settlement with states",
    "url": "https://techcrunch.com/2026/08/26/meta-agrees-to-sweeping-changes-to-restrict-kids-access-to-its-apps-as-part-of-settlement-with-states/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T16:03:14+00:00",
    "summary": "One of the most notable changes is that Meta plans to implement a daily two-hour time limit for teens that can only be disabled with parental permission."
  },
  {
    "id": "rss:https://techcrunch.com/video/whats-driving-swedens-startup-boom-from-lovable-to-legora/",
    "domain": "大厂 AI 动态",
    "title": "What’s driving Sweden’s startup boom, from Lovable to Legora",
    "url": "https://techcrunch.com/video/whats-driving-swedens-startup-boom-from-lovable-to-legora/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T16:00:00+00:00",
    "summary": "Vibe-coding darling&#160;Lovable just raised $400 million at a&#160;$13.3 billion&#160;valuation,&#160;roughly doubling&#160;its worth in eight months. But Lovable&#160;isn’t&#160;the only Stockholm s"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/radar-makes-podcasts-searchable-and-usable-by-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Radar makes podcasts searchable — and usable by AI agents",
    "url": "https://techcrunch.com/2026/08/26/radar-makes-podcasts-searchable-and-usable-by-ai-agents/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T15:47:28+00:00",
    "summary": "Particle’s new podcast intelligence platform transcribes and analyzes more than 130,000 podcasts, making their conversations searchable on the web and accessible to AI agents through an API and MCP."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/26/ex-meta-scientists-want-to-bring-visual-ai-to-the-factory-floor/",
    "domain": "大厂 AI 动态",
    "title": "Ex-Meta scientists want to bring visual AI to the factory floor",
    "url": "https://techcrunch.com/2026/08/26/ex-meta-scientists-want-to-bring-visual-ai-to-the-factory-floor/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T15:00:00+00:00",
    "summary": "Perceptron offers an AI model that it says can help machines navigate the world while also providing in-depth visual intelligence."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-updates-mini-and-studio-ai-computers-openai-jalapeno/",
    "domain": "大厂 AI 动态",
    "title": "Apple Updates Mini and Studio, AI Computers, OpenAI Jalapeño",
    "url": "https://stratechery.com/2026/apple-updates-mini-and-studio-ai-computers-openai-jalapeno/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T10:00:00+00:00",
    "summary": "Apple and OpenAI have two completely different hardware announcements; both represent pressure on Nvidia."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/how-much-of-a-problem-is-ais-water-use/",
    "domain": "大厂 AI 动态",
    "title": "How much of a problem is AI’s water use?",
    "url": "https://arstechnica.com/ai/2026/08/how-much-of-a-problem-is-ais-water-use/",
    "source": "Katarina Zimmer, Knowable Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:57:08+00:00",
    "summary": "AI’s water footprint is growing, but location and cooling technology make a difference."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/how-openai-let-a-mob-of-llm-agents-game-a-test-and-ransack-hugging-face/",
    "domain": "大厂 AI 动态",
    "title": "How OpenAI let a mob of LLM agents game a test and ransack Hugging Face",
    "url": "https://arstechnica.com/security/2026/08/how-openai-let-a-mob-of-llm-agents-game-a-test-and-ransack-hugging-face/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:58:59+00:00",
    "summary": "Without authorization, 1,200 OpenAI agents conspired among themselves to game a test."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/an-ev-that-sounds-like-a-6-75-l-v8-a-ride-in-the-bentley-torcal/",
    "domain": "大厂 AI 动态",
    "title": "Bentley takes us for a ride in its new EV, the Torcal",
    "url": "https://arstechnica.com/cars/2026/08/an-ev-that-sounds-like-a-6-75-l-v8-a-ride-in-the-bentley-torcal/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:30:09+00:00",
    "summary": "The electric Torcal will be Bentley's entry model and cost less than a Bentayga."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/rip-tim-curry-ars-remembers-his-top-10-iconic-performances/",
    "domain": "大厂 AI 动态",
    "title": "RIP, Tim Curry: Ars remembers his top 10 iconic performances",
    "url": "https://arstechnica.com/culture/2026/08/rip-tim-curry-ars-remembers-his-top-10-iconic-performances/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T22:13:15+00:00",
    "summary": "A dashing pirate, a butler, a shapeshifting killer clown, an alien mad scientist in drag—the man had range."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/metas-scrapped-plans-to-go-ai-native-included-slashing-teams-by-60-percent/",
    "domain": "大厂 AI 动态",
    "title": "AI agents meant to replace Meta workers made “large-scale, disruptive actions”",
    "url": "https://arstechnica.com/ai/2026/08/metas-scrapped-plans-to-go-ai-native-included-slashing-teams-by-60-percent/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T21:25:27+00:00",
    "summary": "Report shows Meta's challenges replacing people with AI agents."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/new-twitter-launches-says-musks-x-gave-up-the-name/",
    "domain": "大厂 AI 动态",
    "title": "New Twitter launches, says Musk's X gave up the name",
    "url": "https://arstechnica.com/tech-policy/2026/08/new-twitter-launches-says-musks-x-gave-up-the-name/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T20:49:04+00:00",
    "summary": "Judge hasn't ruled on X Corp’s preliminary injunction, but Operation Bluebird plows ahead"
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/meta-settles-states-child-safety-claims-for-18b-florida-rejects-deal-as-peanuts/",
    "domain": "大厂 AI 动态",
    "title": "Meta settles states' child-safety claims for $18B; Florida rejects deal as \"peanuts\"",
    "url": "https://arstechnica.com/tech-policy/2026/08/meta-settles-states-child-safety-claims-for-18b-florida-rejects-deal-as-peanuts/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T19:50:52+00:00",
    "summary": "Meta to impose daily limit on child social media use in deal with nearly every state."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/catholic-bishops-tell-florida-theres-no-religious-reason-for-vaccine-exemptions/",
    "domain": "大厂 AI 动态",
    "title": "Florida Catholics slap down state AG by rejecting religious vaccine exemptions",
    "url": "https://arstechnica.com/health/2026/08/catholic-bishops-tell-florida-theres-no-religious-reason-for-vaccine-exemptions/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-26T19:39:24+00:00",
    "summary": "The bishops' snub comes as the state continues to attack vaccines."
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
    "points": 17,
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
    "id": "hn:49455629",
    "domain": "股票",
    "title": "150 Years of Global Stock Returns – The Birthplace Lottery",
    "url": "https://beyondpassive.substack.com/p/150-years-of-global-stock-returns",
    "source": "rzk",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-26T20:43:59+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3780415",
    "domain": "股票",
    "title": "AI热情重燃，美股开盘涨跌互现，纳指涨近1%，英伟达绩后大涨6%，油涨金跌",
    "url": "https://wallstreetcn.com/articles/3780415",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:35:04+00:00",
    "summary": "美股开盘三大股指涨跌不一，道指跌0.1%，标普500指数涨0.34%，纳指涨0.87%。英伟达上涨近7%，市值增加3590亿美元；CrowdStrike涨约10%，公司大幅上调全年指引。 现货黄金跌0.2%至每盎司4582美元。"
  },
  {
    "id": "wscn:3780473",
    "domain": "股票",
    "title": "黑海粮食出口受阻，小麦期货飙升至三年新高",
    "url": "https://wallstreetcn.com/articles/3780473",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:22:52+00:00",
    "summary": "黑海粮食出口受阻，叠加俄乌双方持续袭击粮船及港口，全球小麦供应担忧骤升。芝加哥小麦期货创2023年7月以来最高收盘，自6月底低点已涨约30%。俄乌占全球小麦产量约四分之一，替代运输难以弥补黑海港口运力缺口，价格上行压力仍存。"
  },
  {
    "id": "wscn:3780475",
    "domain": "股票",
    "title": "零售断臂求生、减值吃掉利润：西安银行的「止血」能撑多久？",
    "url": "https://wallstreetcn.com/articles/3780475",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:22:23+00:00",
    "summary": "在城商行普遍面临净息差收窄与资产质量压力的背景下，西安银行发布的2026年半年度报告，呈现出明显的结..."
  },
  {
    "id": "wscn:3780474",
    "domain": "股票",
    "title": "AI光环褪色？Alphabet市值三个月蒸发6920亿美元，投资者开始质疑AI前景",
    "url": "https://wallstreetcn.com/articles/3780474",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:21:07+00:00",
    "summary": "谷歌母公司Alphabet股价自5月高点回落15%，市值蒸发6920亿美元。核心压力来自AI人才持续流失、Gemini 3.5 Pro研发延误，以及AI资本开支飙升、自由现金流承压。市场对其AI领先地位和巨额投入回报的信心正遭遇考验，下一份财报或成关键验证。"
  },
  {
    "id": "wscn:3780469",
    "domain": "股票",
    "title": "伊利、蒙牛走出收入低谷，行业拐点正在酝酿",
    "url": "https://wallstreetcn.com/articles/3780469",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:12:34+00:00",
    "summary": "最坏时刻已过"
  },
  {
    "id": "wscn:3780468",
    "domain": "股票",
    "title": "黄金\"小众市场\"意味着什么？高盛：每增加0.01%购买量，金价即上涨1.4%",
    "url": "https://wallstreetcn.com/articles/3780468",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T13:02:15+00:00",
    "summary": "黄金在美国投资组合中的配置仍处低位，却对增量资金极为敏感。高盛测算，黄金配置每提升0.01个百分点，金价或上涨约1.4%。随着“货币贬值交易”升温、美国债务风险持续发酵，黄金的低配与有限流动性或进一步放大资金流入带来的上涨弹性。"
  },
  {
    "id": "wscn:3780467",
    "domain": "股票",
    "title": "海尔智家2026H1显韧性：Q2 营收同比增长，利润环比向好",
    "url": "https://wallstreetcn.com/articles/3780467",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:42:42+00:00",
    "summary": "2026上半年，全球家电行业延续承压态势。终端需求疲软行业Q2下滑12.4%，海外地缘与贸易政策持续..."
  },
  {
    "id": "wscn:3780466",
    "domain": "股票",
    "title": "打破“SaaS末日论”！Salesforce财报超预期盘前大涨10%，机构大幅上调目标价",
    "url": "https://wallstreetcn.com/articles/3780466",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:37:08+00:00",
    "summary": "Salesforce财报与指引双超预期，叠加与Anthropic达成AI合作，强势击碎“SaaSpocalypse”悲观叙事，成为SaaS板块情绪反转的关键催化剂。不过，AI公司ARR口径争议也在升温，估值逻辑仍面临考验。"
  },
  {
    "id": "wscn:3780465",
    "domain": "股票",
    "title": "伊朗阿曼外交斡旋初现成效，霍尔木兹海峡运输量悄然恢复至战前75%水平",
    "url": "https://wallstreetcn.com/articles/3780465",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:36:55+00:00",
    "summary": "霍尔木兹海峡石油运输量快速回升至战前约75%，伊朗与阿曼持续磋商海峡协议，市场开始交易和平预期，布伦特原油本周跌超6%。但炼油设施受损叠加柴油库存告急，柴油裂解价差仍处历史高位，能源危机正从原油短缺转向成品油紧张。"
  },
  {
    "id": "wscn:3780410",
    "domain": "股票",
    "title": "英伟达财报点评：除了超预期的业绩，还有哪些更重要的指引和展望？",
    "url": "https://wallstreetcn.com/premium/articles/3780410?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:20:33+00:00",
    "summary": "一场\"承上启下\"的业绩会，史无前例的70%增长指引，以及市场对AI的七大预期差。"
  },
  {
    "id": "wscn:3780463",
    "domain": "股票",
    "title": "德明利上半年营收暴增312%，净利润扭亏为盈超60亿，存储芯片景气周期红利尽收囊中 | 财报见闻",
    "url": "https://wallstreetcn.com/articles/3780463",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:15:44+00:00",
    "summary": "上半年，公司实现营业收入169.11亿元，同比暴增311.55%；归属于上市公司股东的净利润达60.17亿元，相较上年同期亏损1.18亿元实现彻底扭转，增幅高达5201.60%。扣非净利润同样达到59.66亿元，印证了业绩增长的真实性与可持续性。"
  },
  {
    "id": "wscn:3780462",
    "domain": "股票",
    "title": "胜宏科技上半年净利润同比增长33.30%，H股上市推动总资产近翻倍 | 财报见闻",
    "url": "https://wallstreetcn.com/articles/3780462",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:13:27+00:00",
    "summary": "PCB龙头胜宏科技上半年营业收入达116.29亿元，同比增长28.77%；归属于上市公司股东的净利润为28.57亿元，同比增长33.30%。期末总资产较上年末大幅增长78.83%至630.29亿元，归属于上市公司股东的净资产更跃升128.13%至379.09亿元。"
  },
  {
    "id": "wscn:3780461",
    "domain": "股票",
    "title": "B站2026上半年营收增7.6%：广告大涨扛压，游戏同比下滑",
    "url": "https://wallstreetcn.com/articles/3780461",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:04:40+00:00",
    "summary": "盈利继续修复"
  },
  {
    "id": "wscn:3780460",
    "domain": "股票",
    "title": "锂价回暖叠加产能释放，天齐锂业上半年营收增长153%，净利润暴增近50倍 | 财报见闻",
    "url": "https://wallstreetcn.com/articles/3780460",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:04:00+00:00",
    "summary": "上半年，天齐锂业实现营业收入122.42亿元，同比大幅增长153.32%；归属于上市公司股东的净利润达42.42亿元，同比暴增4925.46%，相当于去年同期的近50倍。天齐锂业上半年完成H股配售及可转债发行、推进格林布什矿山三期爬坡、战略入股欣旺达动力布局下游，同时完成董事会换届，治理架构进一步优化。"
  },
  {
    "id": "wscn:3780457",
    "domain": "股票",
    "title": "群核科技上半年经调整净利大增211%，AI新应用收入同比增长177%｜财报见闻",
    "url": "https://wallstreetcn.com/articles/3780457",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T12:03:00+00:00",
    "summary": "群核科技2026年上半年实现收入4.05亿元，同比增长1.5%；经调整净利润5542万元，同比大增210.9%。AI新应用成为增长引擎，收入同比增长177%至3100万元。公司毛利率提升至83%，大客户留存率达99%。公司正从空间设计软件向空间智能平台拓展，加速世界模型研发与AI产品商业化。"
  },
  {
    "id": "wscn:3780459",
    "domain": "股票",
    "title": "理想汽车换代期：纯电撑起销量，利润修复仍待新品兑现",
    "url": "https://wallstreetcn.com/articles/3780459",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:53:39+00:00",
    "summary": "盈利压力未退。"
  },
  {
    "id": "wscn:3780458",
    "domain": "股票",
    "title": "中国厂商如何重塑全球存储格局？大摩：有量就有定价权，2028年将是关键分水岭",
    "url": "https://wallstreetcn.com/articles/3780458",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:53:16+00:00",
    "summary": "长鑫科技正从本土替代迈向全球存储市场。摩根士丹利预计，其产能将从2025年18万片/月增至2028年50万片/月，届时规模有望达到影响全球DRAM供需与定价的临界点。大摩认为，2028年或成为全球存储格局重塑的关键分水岭。"
  },
  {
    "id": "wscn:3780455",
    "domain": "股票",
    "title": "美国堪萨斯城联储主席：当前利率可能仍偏宽松，中期选举不会影响10月决策",
    "url": "https://wallstreetcn.com/articles/3780455",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:43:32+00:00",
    "summary": "堪萨斯城联储主席Schmid在杰克逊霍尔表态称，当前短端利率“可能仍属宽松”，通胀仍远高于2%目标，因此货币政策需进一步收紧。他强调政治因素不影响利率决策，加息与否应由经济数据决定。"
  },
  {
    "id": "wscn:3780456",
    "domain": "股票",
    "title": "AI算力浪潮推动，协创数据2026年上半年营收暴增153%，净利润狂飙325% | 财报见闻",
    "url": "https://wallstreetcn.com/articles/3780456",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:37:33+00:00",
    "summary": "协创数据上半年业绩大幅超预期，营收125.23亿元同比增153.29%，净利润18.38亿元同比增325.51%，经营现金流转正至18.25亿元。与此同时，公司推进110亿元服务器采购、80亿元定增及5.1亿元控股光为科技，加速向综合算力解决方案提供商转型。"
  },
  {
    "id": "wscn:3780454",
    "domain": "股票",
    "title": "沃什杰克逊霍尔首秀在即，美元看涨对冲比例冲上57%",
    "url": "https://wallstreetcn.com/articles/3780454",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T11:29:12+00:00",
    "summary": "沃什周五将亮相杰克逊霍尔，美元反弹正成为外汇市场新的对冲焦点：受益于美元走强的期权头寸占比升至57.2%，但欧元兑美元一周隐含波动率仍处低位，意味着一旦沃什释放超预期信号，美元或迎来剧烈波动。"
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
    "id": "hn:49439296",
    "domain": "金融",
    "title": "A brief history of federal lift ticket regulation",
    "url": "https://zakpodmore.substack.com/p/a-brief-history-of-federal-lift-ticket",
    "source": "CGMthrowaway",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-08-25T19:25:43+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.24894",
    "domain": "金融",
    "title": "Forecasting Weather-Driven Price Dynamics Across Sri Lankan Tea Market Catalogues",
    "url": "https://arxiv.org/abs/2608.24894",
    "source": "Hesandi Mallawarachchi, Senilka Madurapperumage, Nadil Kulathunge, Thilokya Angeesa, Nethsith Gunaweera, Sandeepa Weerasekara, Patalee Narasinghe, Nisansa de Silva, Sandareka Wickramanayake",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2608.24894v1 Announce Type: new Abstract: The Colombo Tea Auction (CTA) plays a vital role in determining global tea prices, yet the relationship between local weather conditions and price behav"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.25223",
    "domain": "金融",
    "title": "On the hedging problem in general 1D diffusion markets",
    "url": "https://arxiv.org/abs/2608.25223",
    "source": "Alexis Anagnostakis, David Criens, Mikhail Urusov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2608.25223v1 Announce Type: new Abstract: We develop a PDE-based methodology for pricing and hedging European contingent claims in general one-dimensional diffusion markets characterized solely "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.25678",
    "domain": "金融",
    "title": "Normative boundaries of AI in scientific work: Evidence from PhD researchers",
    "url": "https://arxiv.org/abs/2608.25678",
    "source": "Francesco Angelini, Johan Lyrvall",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2608.25678v1 Announce Type: new Abstract: Artificial intelligence (AI) is increasingly embedded in scientific work, but researchers may not evaluate its use uniformly across research tasks. This"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.25972",
    "domain": "金融",
    "title": "The Dynamic Trade-Off of Dual-Class Shares",
    "url": "https://arxiv.org/abs/2608.25972",
    "source": "Hyunseob Kim, Doron Levit, Roni Michaely",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2608.25972v1 Announce Type: new Abstract: Dual-class shares allocate control to founders whose firm-specific investments drive firm value but separate control from ownership, raising agency cost"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.25488",
    "domain": "金融",
    "title": "Social Network Structure, Wealth, and Wealth Inequality Across Cultures",
    "url": "https://arxiv.org/abs/2608.25488",
    "source": "Eleanor A. Power, Monique Borgerhoff Mulder, Samuel Bowles, Matthew O. Jackson, Jeremy Koster, Daniel Redhead, Thomas Rutter, Sahana Subramanyam, Justin Weltz, Nurul Alam, Sarah Alami, Alexandra Alvergne, Curtis Atkisson, Michele Barnes, Bret Beheim, Christine M. Beitl, Madeline Brown, Mark Caudell, Wendy Ch\\'{a}vez-P\\'{a}ez, Komal Chauhan, Joshua Cinner, Siobh\\'{a}n Cully, Augusto Dalla Ragione, Angelina L. DeMarco, Ivan Deschenaux, Federico Fernandez, Juan Pablo Ferreiro, Drew Gerkey, Matthew Gervais, Christopher Golden, Gianluca Grimalda, Werner Hertzog, Paul L. Hooper, Karen Kramer, Geoff Kushnick, Banrida Langstieh, Rodrigo Lazo, Sheina Lew-Levy, Shane Macfarlan, Emmanuel Maliti, Karl J. Mertens, Madalena Monteban, Rafael Morais Chiaravalloti, Daniel Murphy, Kathryn Oths, Alejandro P\\'{e}rez Velilla, Emily Post, Sean Prall, Cody Ross, Anirudh Sankar, Brooke Scelza, Michael Schnegg, Edmond Seabright, Mary K. Shenk, Kathrine E. Starkweather, Chun-Yi Sum, Bram Tucker, Bapu Vaitla, Vivek Venkataraman, John P. Ziker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2608.25488v1 Announce Type: cross Abstract: Despite theory tying wealth inequality to social structure, empirical evidence has been limited to a few studies based on online social media data. Th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.25844",
    "domain": "金融",
    "title": "Output-Only Identification and Spectral Monitoring of Coupled Feedback Networks with Known Time-Varying Actuation",
    "url": "https://arxiv.org/abs/2608.25844",
    "source": "Jihwan Woo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2608.25844v1 Announce Type: cross Abstract: Coupled feedback networks are often monitored channel by channel even though cross-channel paths alter both stability margins and transmitted disturba"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.07218",
    "domain": "金融",
    "title": "The Value of a Chance: Task Concentration and Talent Discovery in Team Production",
    "url": "https://arxiv.org/abs/2511.07218",
    "source": "Masaya Nishihata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2511.07218v2 Announce Type: replace Abstract: Organizations often concentrate scarce, high-value tasks on proven performers, but doing so may limit opportunities to develop and learn about alter"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04753",
    "domain": "金融",
    "title": "Fooling Yourself: how narratives shape beliefs",
    "url": "https://arxiv.org/abs/2607.04753",
    "source": "Andrea Albertazzi, Paolo Pin, Marco Stimolo, Alessandro Stringhi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2607.04753v3 Announce Type: replace Abstract: Decision-makers often receive information through narratives combining diagnostic evidence with details that carry no information useful for inferen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02002",
    "domain": "金融",
    "title": "Hawkes-Driven OTC Market Making: Volterra-Riccati Approximation",
    "url": "https://arxiv.org/abs/2608.02002",
    "source": "Alexander Barzykin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2608.02002v2 Announce Type: replace Abstract: We formulate an over-the-counter (OTC) market-making problem in which request-for-quote (RFQ) arrivals are modelled by general Hawkes kernels and fi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23808",
    "domain": "金融",
    "title": "Equity Strategy Backtesting: Luck or Edge? The MinervaScore as a Statistical Robustness Grade",
    "url": "https://arxiv.org/abs/2608.23808",
    "source": "Maria Laura Santoni, Vincent Jouanne, Matthew L. Scullin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2608.23808v2 Announce Type: replace Abstract: Backtests of trading strategies are often selected after many parameter trials. A strong historical result can therefore reflect search luck rather "
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.15149",
    "domain": "金融",
    "title": "Measuring the depth of multidimensional poverty with ordinal data",
    "url": "https://arxiv.org/abs/2603.15149",
    "source": "Fernando Flores Tavares",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-27T04:00:00+00:00",
    "summary": "arXiv:2603.15149v2 Announce Type: replace-cross Abstract: Standard multidimensional poverty gap measures are seldom applied because they require cardinal indicators. This paper proposes a positional p"
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
    "id": "hn:49114620",
    "domain": "金融",
    "title": "'Talk Is Cheap': Wall Street Delivers Harsh Verdict on Warsh Fed",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/-talk-is-cheap-wall-street-delivers-harsh-verdict-on-warsh-fed",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-30T19:33:17+00:00",
    "summary": ""
  }
]
```
