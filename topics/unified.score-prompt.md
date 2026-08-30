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

- 今日日期：`2026-08-30`
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
  "date": "2026-08-30",
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
    "points": 4380984,
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
    "points": 1773723,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1rv7A6oEeP",
    "domain": "AI",
    "title": "2026版LangChain教程，langchain快速入门， Agent智能体rag项目实战",
    "url": "http://www.bilibili.com/video/av116792827579053",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1590716,
    "published_at": "2026-06-23T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】LangChain学习一套通，从入门到三大综合项目实战"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1210282,
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
    "points": 1125879,
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
    "points": 1075260,
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
    "points": 863461,
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
    "points": 663182,
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
    "points": 639205,
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
    "points": 440823,
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
    "points": 259904,
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
    "points": 250110,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV139bD6gEa8",
    "domain": "AI",
    "title": "Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一期视频精通",
    "url": "http://www.bilibili.com/video/av117104095268420",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 201132,
    "published_at": "2026-08-16T07:53:45+00:00",
    "summary": "Pi是近期热度超高的AI Agent。用四个字形容那就是大道至简。 Pi只有四个默认工具，（读文件，写文件，改文件，运行命令），系统提示词也仅仅只有一千Token。极致的精简带来了极致效率提升，在多项权威基准测试里，Pi 的代码质量，工作速度，成本等方面多方面超过主流Agent Codex和Claude Code。 Pi还有极其开放的插件生态，可以自己编写插件扩展Pi的能力。"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 194997,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1i9Z8YhEja",
    "domain": "AI",
    "title": "学 AI，看这个视频就够了！最全程序员 AI 指南：AI核心概念、实用AI工具、AI编程技巧、AI开发技术",
    "url": "http://www.bilibili.com/video/av114262957626976",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 187856,
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
    "points": 180243,
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
    "points": 164330,
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
    "points": 150534,
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
    "points": 102975,
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
    "points": 93439,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 91312,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1Jm8b6ZEwT",
    "domain": "AI",
    "title": "有了AI反而更累了？我的Coding Skill分享",
    "url": "http://www.bilibili.com/video/av117144293476060",
    "source": "一只甜药",
    "platform": "bilibili",
    "points": 81192,
    "published_at": "2026-08-23T10:49:33+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1myM96nETU",
    "domain": "AI",
    "title": "AI 赛博女友！本地部署教程，无需 API、完全免费，8G显存就能跑！实时语音聊天，几乎零延迟，太上头了！| 零度解说",
    "url": "http://www.bilibili.com/video/av117032322339286",
    "source": "零度解说",
    "platform": "bilibili",
    "points": 62575,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "AI 赛博女友一键安装包下载：https://www.freedidi.com/24984.html"
  },
  {
    "id": "bvid:BV1Y6uC6TE1m",
    "domain": "AI",
    "title": "疯狂Vibe Coding一周，我烧了近100亿Token，做了5个项目！",
    "url": "http://www.bilibili.com/video/av117080321957877",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 46431,
    "published_at": "2026-08-12T03:12:41+00:00",
    "summary": "项目地址：\nlocal-ops — 本地服务指挥台（零依赖 Python + 原生前端）：https://github.com/laogou717/local-ops\nmd-wechat — 公众号排版工具：https://github.com/laogou717/md-wechat\ndaydream-room — 白日梦陈列室：https://github.com/laogou717/daydr"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 43886,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39367,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 32652,
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
    "points": 30401,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1Ug3d6AEFp",
    "domain": "AI",
    "title": "2026最火的三个AI Agent，普通人该用哪个",
    "url": "http://www.bilibili.com/video/av117026701973009",
    "source": "厚深AI",
    "platform": "bilibili",
    "points": 21535,
    "published_at": "2026-08-04T11:00:00+00:00",
    "summary": "#aiagent #codex #claudecode #openclaw"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 20530,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 9727,
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
    "points": 9441,
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
    "points": 8958,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1EEM96uEPP",
    "domain": "AI",
    "title": "【逆向】掌握MCP功能使用修改分析，成为逆向高手！",
    "url": "http://www.bilibili.com/video/av117030460131623",
    "source": "009安乐",
    "platform": "bilibili",
    "points": 8419,
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
    "points": 8196,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1Y1bv68Eq9",
    "domain": "AI",
    "title": "DeepSeek Harness 多 Agent 协作插件开源！一条指令拉起 Agent Teams",
    "url": "http://www.bilibili.com/video/av117111879898943",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 7884,
    "published_at": "2026-08-18T10:30:00+00:00",
    "summary": "这期分享我在 DeepSeek Harness 内测期间开发的开源插件 `dsh-agent-teams`。\n\n当你明确指定使用 Agent Teams 后，插件会自动完成：\n\n- 创建队长与多个成员 Agent；\n- 分析任务并生成依赖 DAG；\n- 无依赖任务并行执行；\n- 通过共享任务池原子领取任务，避免成员冲突；\n- 通过本地数据协议完成队长、成员之间的通信与状态同步；\n- 为不同成员配置"
  },
  {
    "id": "bvid:BV1RxLg6FEkx",
    "domain": "AI",
    "title": "AI编程利器cursor+codex，草图变代码实现屏显",
    "url": "http://www.bilibili.com/video/av116583162774844",
    "source": "郭天祥老师",
    "platform": "bilibili",
    "points": 7598,
    "published_at": "2026-05-16T07:53:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uA4YeNEFd",
    "domain": "AI",
    "title": "CocosCreator+Cursor零代码AI游戏开始演示",
    "url": "http://www.bilibili.com/video/av113113684840361",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 7341,
    "published_at": "2024-09-10T14:33:00+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV18XDHYyExy",
    "domain": "AI",
    "title": "Cofounder：AI全栈程序员+项目经理，可平替Cursor+v0、Cline的AI全栈构建工具，通过一句话需求即可生成带有界面、前端、后端、数据库的网站",
    "url": "http://www.bilibili.com/video/av113424382103786",
    "source": "AIGCLINK",
    "platform": "bilibili",
    "points": 7140,
    "published_at": "2024-11-04T11:21:06+00:00",
    "summary": "Cofounder：AI全栈程序员+项目经理，可平替Cursor+v0、Cline的AI全栈构建工具，通过一句话需求即可生成带有界面、前端、后端、数据库的网站"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6940,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 6788,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6715,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1ebTi6yE7p",
    "domain": "AI",
    "title": "llama.cpp添加网络搜索等MCP工具 本地大模型摆脱过时数据束缚 实时获取最新数据 本地部署网络搜索MCP llama.cpp启动器添加了MCP代理选项",
    "url": "http://www.bilibili.com/video/av116845491329271",
    "source": "hsxbxq",
    "platform": "bilibili",
    "points": 6532,
    "published_at": "2026-07-01T15:49:48+00:00",
    "summary": "llama.cpp也可以添加网络搜索等MCP工具了，自此本地大模型终于可以简单的摆脱过时数据的束缚，实时获取最新数据了，相当于极简版的openclaw或Hermes了。 本期视频介绍了llama.cpp服务器图形化启动器1.4版添加了MCP代理选项，以及如何本地部署网络搜索MCP和添加百度搜索MCP方法。\nopen-webSearch介绍：https://github.com/Aas-ee/ope"
  },
  {
    "id": "bvid:BV1zL2hBiEJy",
    "domain": "AI",
    "title": "通过Vibe Coding和AI掌握现代SQL与PostgreSQL（中文语音）",
    "url": "http://www.bilibili.com/video/av115658872392546",
    "source": "明文传输不",
    "platform": "bilibili",
    "points": 5972,
    "published_at": "2026-01-11T04:10:00+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1n9g36wEiZ",
    "domain": "AI",
    "title": "5分钟教会你，什么是agent？",
    "url": "http://www.bilibili.com/video/av117097082392253",
    "source": "开聊",
    "platform": "bilibili",
    "points": 5876,
    "published_at": "2026-08-15T02:12:34+00:00",
    "summary": "呵呵，多评论。"
  },
  {
    "id": "bvid:BV1QfjJ6HECp",
    "domain": "AI",
    "title": "嵌入式神级 MCP 服务器推荐！【Zephyr 101】SP01-2",
    "url": "http://www.bilibili.com/video/av116781754621441",
    "source": "MC-ALL",
    "platform": "bilibili",
    "points": 4420,
    "published_at": "2026-06-20T12:00:00+00:00",
    "summary": "大家好，我是 Ellis\n这里没有 PPT，没有废话\n这是一个基于 STM32F411 的 Zephyr 实战系列\n嵌入式神级 MCP 服务器推荐！"
  },
  {
    "id": "bvid:BV1sM6xB5EEE",
    "domain": "AI",
    "title": "基于LabVIEW的AI Agent智能体实现教程",
    "url": "http://www.bilibili.com/video/av115993393238477",
    "source": "三易电子工作室",
    "platform": "bilibili",
    "points": 4284,
    "published_at": "2026-02-01T04:12:23+00:00",
    "summary": "基于LabVIEW的AI Agent智能体实现教程，made by 三易电子工作室。"
  },
  {
    "id": "bvid:BV1anhG6KEYc",
    "domain": "AI",
    "title": "3分钟搞定Claude桌面版安装+汉化+自由接入大模型",
    "url": "http://www.bilibili.com/video/av117155483944854",
    "source": "大海资源",
    "platform": "bilibili",
    "points": 4135,
    "published_at": "2026-08-25T09:44:19+00:00",
    "summary": "Claude命令版安装教程：https://www.bilibili.com/video/BV1iTbX6JEyy/\ncodex安装教程：https://www.bilibili.com/video/BV1PkGg6BEBz/\n桌面版文字教程：https://www.dhzyw.com/archives/11528.html"
  },
  {
    "id": "bvid:BV1oC4m6aErY",
    "domain": "AI",
    "title": "耗时2个月，全新AI操作系统：DX-OS，内置无限画布/图片分层/ComfyUI/Skills/MCP/Agent/AI漫剧等多功能，使用教程随后更",
    "url": "http://www.bilibili.com/video/av117179961839871",
    "source": "wuli大雄oO",
    "platform": "bilibili",
    "points": 3952,
    "published_at": "2026-08-29T17:29:51+00:00",
    "summary": "免费下载地址：www.dx-os.com"
  },
  {
    "id": "bvid:BV1Ac8J6uE8E",
    "domain": "AI",
    "title": "把 Agent 连上本地 ComfyUI！：让 Agent 帮你把 ComfyUI 自动玩明白！",
    "url": "http://www.bilibili.com/video/av117120721489651",
    "source": "Buk-M",
    "platform": "bilibili",
    "points": 3897,
    "published_at": "2026-08-19T06:23:58+00:00",
    "summary": "Comfy MCP 本地版正式发布，完全开源！\n\n把 Claude / Codex / Cursor 等任意 Agent 连上你的本地 ComfyUI：\n✅ 用自然语言构建、编辑、运行工作流\n✅ Agent 自动检测 GPU 显存\n✅ 自动下载模型、自动配置工作流\n✅ 全程本地运行，数据不出门\n\n安装只需三样：独显电脑 + ComfyUI + MCP 客户端\n新手也能轻松上手 ⚡\n\n文档：docs"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1967,
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
    "points": 111,
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
    "id": "hn:49447878",
    "domain": "AI 算力 / 半导体",
    "title": "Who bears the risk in Nvidia's $500B financing platform?",
    "url": "https://www.sascha-steffen.de/updates/nvidia-500bn-ai-financing-credit-risk",
    "source": "rwmj",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-26T12:32:31+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/googles-marvell-deal-shows-custom-silicon-spreading-beyond-the-tpu/",
    "domain": "AI 算力 / 半导体",
    "title": "Google’s Marvell Deal Shows Custom Silicon Spreading Beyond the TPU",
    "url": "https://www.eetimes.com/googles-marvell-deal-shows-custom-silicon-spreading-beyond-the-tpu/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T21:59:13+00:00",
    "summary": "Google’s expanded relationship with Marvell suggests that memory, networking, storage, and data movement are candidates for specialization too. The post Google’s Marvell Deal Shows Custom Silicon Spre"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt",
    "domain": "AI 算力 / 半导体",
    "title": "California lawmakers unanimously pass Linux exemption from age-verification law — software distributed under the GPL, MIT, BSD, and Apache licenses are exempt",
    "url": "https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T15:57:13+00:00",
    "summary": "California’s legislature has passed Assembly Bill 1856, exempting open-source operating systems from the State’s Digital Age Assurance Act months before the law is due to take effect on January 1, 202"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/usb-flash-drives/magnetic-core-memory-usb-drive-transfers-files-in-sneakernet-first-text-and-image-files-get-moved-between-pcs-via-hugely-constrained-archaic-memory-tech",
    "domain": "AI 算力 / 半导体",
    "title": "Magnetic core memory USB drive transfers files in sneakernet first — text and image files get moved between PCs via hugely constrained archaic memory tech",
    "url": "https://www.tomshardware.com/pc-components/usb-flash-drives/magnetic-core-memory-usb-drive-transfers-files-in-sneakernet-first-text-and-image-files-get-moved-between-pcs-via-hugely-constrained-archaic-memory-tech",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T15:14:44+00:00",
    "summary": "A dinner plate-sized magnetic core memory homebrew USB device has been used to transfer a text file from one PC to another for the first time."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/get-a-32-inch-samsung-odyssey-g55c-curved-gaming-monitor-for-usd199-1440p-165-hz-screen-is-39-percent-off-at-amazon-for-a-limited-time",
    "domain": "AI 算力 / 半导体",
    "title": "Get a 32-inch Samsung Odyssey G55C curved gaming monitor for $199 — 1440p 165 Hz screen is 39% off at Amazon for a limited time",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/get-a-32-inch-samsung-odyssey-g55c-curved-gaming-monitor-for-usd199-1440p-165-hz-screen-is-39-percent-off-at-amazon-for-a-limited-time",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T14:20:00+00:00",
    "summary": "The Samsung Odyssey G55C is a 32-inch curved gaming monitor with a 1440p QHD resolution and 1ms response time. It's currently on sale at just $199.99, saving you $130 off its $329.99 MSRP."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/startup-raises-usd7-million-to-build-backpack-portable-8-8-ounce-drone-interceptors-mara-claims-20x-cost-advantage-over-other-interceptors-priced-one-for-one-against-attack-drones",
    "domain": "AI 算力 / 半导体",
    "title": "Startup raises $7 million to build backpack-portable 8.8-ounce drone interceptors — Mara claims 20x cost advantage over other interceptors, priced one-for-one against attack drones",
    "url": "https://www.tomshardware.com/tech-industry/drones/startup-raises-usd7-million-to-build-backpack-portable-8-8-ounce-drone-interceptors-mara-claims-20x-cost-advantage-over-other-interceptors-priced-one-for-one-against-attack-drones",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T14:16:20+00:00",
    "summary": "San Francisco defense startup Mara has secured $7 million in a pre-seed round to produce what it calls Spike, a portable counter-drone system housed inside a backpack."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/site-provides-instructions-to-get-up-to-usd175-back-for-your-pre-installed-windows-11-license-new-portal-provides-legal-forms-but-warns-buyers-not-to-wipe-storage-first",
    "domain": "AI 算力 / 半导体",
    "title": "Get up to $175 back for your pre-installed Windows 11 license — new portal provides legal forms, but warns buyers not to wipe storage first",
    "url": "https://www.tomshardware.com/software/windows/site-provides-instructions-to-get-up-to-usd175-back-for-your-pre-installed-windows-11-license-new-portal-provides-legal-forms-but-warns-buyers-not-to-wipe-storage-first",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T11:39:30+00:00",
    "summary": "The Refund4Freedom site was put together by the Italian Linux Society and the Free Software Foundation Europe to help address the unfairness of unwanted OS bundling."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/grand-theft-auto-6-will-run-at-only-30-fps-on-consoles-at-launch-no-performance-mode-promised-even-the-souped-up-ps5-pro-might-not-get-60-fps-support",
    "domain": "AI 算力 / 半导体",
    "title": "Grand Theft Auto 6 will run at only 30 FPS on consoles at launch, no performance mode promised — even the souped-up PS5 Pro might not get 60 FPS support",
    "url": "https://www.tomshardware.com/video-games/grand-theft-auto-6-will-run-at-only-30-fps-on-consoles-at-launch-no-performance-mode-promised-even-the-souped-up-ps5-pro-might-not-get-60-fps-support",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T11:30:00+00:00",
    "summary": "GTA 6 is currently running at 30 FPS at Rockstar internally with no confirmation on a 60 FPS mode being available at launch, or even later."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/deco-gear-dg49oled240-49-inch-32-9-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Deco Gear DG49OLED240 49-inch 32:9 OLED gaming monitor review: Two 27-inch QHD screens without the dividing line",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/deco-gear-dg49oled240-49-inch-32-9-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T11:05:00+00:00",
    "summary": "You can replace two 27-inch QHD monitors with one Deco Gear DG49OLED240. This 49-inch 32:9 QD-OLED panel has an 1800R curve, 240 Hz, 5120x1440 pixels, HDR10, DisplayHDR 400, wide gamut color, and Adap"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/microsoft-backed-ai-data-center-faces-multiple-complaints-from-community-issues-range-from-unpermitted-gas-turbines-to-illegal-construction-and-noise-pollution",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft-backed AI data center faces backlash over alleged unpermitted gas turbines and 1.5M-gallon LNG tank — groups' issues with $19.4B facility range from illegal construction to noise pollution",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/microsoft-backed-ai-data-center-faces-multiple-complaints-from-community-issues-range-from-unpermitted-gas-turbines-to-illegal-construction-and-noise-pollution",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T11:00:00+00:00",
    "summary": "The community surrounding the DataOne data center in Vineland, New Jersey, are complaining about the Microsoft-linked project. The company's deployment of several unpermitted gas turbines is just one "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/gta-6-leaker-cyberleek-cashes-out-roughly-250000-hours-before-rockstars-official-reveal",
    "domain": "AI 算力 / 半导体",
    "title": "GTA 6 leaker cashes out in $250,000 crypto rug pull just hours before Rockstar's official reveal — memecoin crashes as Cyberleek's 'anti-corporate' campaign ends in a payday",
    "url": "https://www.tomshardware.com/video-games/console-gaming/gta-6-leaker-cyberleek-cashes-out-roughly-250000-hours-before-rockstars-official-reveal",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T10:30:00+00:00",
    "summary": "The person or group behind nine days of Grand Theft Auto VI gameplay leaks cashed out of the $CYBERLEEK memecoin on Thursday, hours before Rockstar's Extended Look premiered on Netflix."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/us-navy-launches-missiles-from-its-first-drone-sailboat-saildrone-surveyor-launches-dual-jagm-missiles-carrier-strike-group-tests-armed-usv-and-electronic-warfare",
    "domain": "AI 算力 / 半导体",
    "title": "US Navy launches missiles from its first drone sailboat — Saildrone Surveyor launches dual JAGM missiles, carrier strike group tests armed USV and electronic warfare",
    "url": "https://www.tomshardware.com/tech-industry/drones/us-navy-launches-missiles-from-its-first-drone-sailboat-saildrone-surveyor-launches-dual-jagm-missiles-carrier-strike-group-tests-armed-usv-and-electronic-warfare",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T10:00:00+00:00",
    "summary": "The U.S. Navy successfully tested a sail-powered autonomous drone in live-fire exercises in the Pacific."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr4/msi-brings-ddr4-back-to-gaming-laptops-amidst-dram-crisis-katana-15-hx-c14-available-with-up-to-core-i9-14900hx-and-rtx-5070",
    "domain": "AI 算力 / 半导体",
    "title": "MSI brings DDR4 back to gaming laptops amidst DRAM crisis — Katana 15 HX C14 available with up to Core i9-14900HX and RTX 5070",
    "url": "https://www.tomshardware.com/pc-components/ddr4/msi-brings-ddr4-back-to-gaming-laptops-amidst-dram-crisis-katana-15-hx-c14-available-with-up-to-core-i9-14900hx-and-rtx-5070",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:55:43+00:00",
    "summary": "With 32GB DDR4 SO-DIMM memory kits costing roughly half as much as comparable DDR5 kits, MSI’s new Katana 15 HX C14 could help reduce the impact of soaring memory prices."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/new-us-export-controls-reportedly-target-chinese-access-to-remote-ai-servers-trump-admins-cut-down-ai-diffusion-rule-could-be-shared-with-industry-as-soon-as-september",
    "domain": "AI 算力 / 半导体",
    "title": "New US export controls reportedly target Chinese access to remote AI servers — Trump admin's cut-down AI diffusion rule could be shared with industry as soon as September",
    "url": "https://www.tomshardware.com/tech-industry/policy/new-us-export-controls-reportedly-target-chinese-access-to-remote-ai-servers-trump-admins-cut-down-ai-diffusion-rule-could-be-shared-with-industry-as-soon-as-september",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:47:46+00:00",
    "summary": "The Trump administration is reportedly drafting a rule to close a loophole around remote access to advanced AI compute, and it could be shared with trade groups as early as September."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-gears-up-its-influence-in-washington-forming-pac-tells-employees-that-decisions-congress-makes-over-the-coming-years-could-have-substantial-consequences-for-the-ai-industry-according-to-report",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia gears up its influence in Washington, forming PAC — tells employees that decisions Congress makes over the coming years could have substantial consequences for the AI industry, according to rep",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-gears-up-its-influence-in-washington-forming-pac-tells-employees-that-decisions-congress-makes-over-the-coming-years-could-have-substantial-consequences-for-the-ai-industry-according-to-report",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:19:27+00:00",
    "summary": "Nvidia establishes its employees federal political action committee (PAC) to fund politicians whose positions are favorable to Nvidia's interests."
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
    "points": 361,
    "published_at": "2026-08-27T18:03:42+00:00",
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
    "id": "rss:https://www.theverge.com/entertainment/986461/hike-appalachian-trail-pixel-art-a-trail-tale",
    "domain": "大厂 AI 动态",
    "title": "Vicariously hike the Appalachian in the gorgeous A Trail Tale",
    "url": "https://www.theverge.com/entertainment/986461/hike-appalachian-trail-pixel-art-a-trail-tale",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T20:59:26+00:00",
    "summary": "I used to be an avid hiker and would try to go backpacking a few times a year. I always dreamed of thru-hiking the Appalachian Trail, but life kind of got in the way. (Turns out jobs, wives, and child"
  },
  {
    "id": "rss:https://www.theverge.com/policy/986456/milo-yiannopoulos-deported-ice",
    "domain": "大厂 AI 动态",
    "title": "Alt-right troll Milo Yiannopoulos has been deported",
    "url": "https://www.theverge.com/policy/986456/milo-yiannopoulos-deported-ice",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T19:49:59+00:00",
    "summary": "Alt-right troll Milo Yiannopoulos was arrested by ICE on Thursday, and today the Department of Homeland Security confirmed to Reuters and the Washington Post that he had been deported to the UK. Yiann"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/986438/sony-music-warner-chappell-anthropic-lawsuit-copyright",
    "domain": "大厂 AI 动态",
    "title": "Sony Music and Warner Chappell are suing Anthropic",
    "url": "https://www.theverge.com/ai-artificial-intelligence/986438/sony-music-warner-chappell-anthropic-lawsuit-copyright",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T18:19:53+00:00",
    "summary": "Sony Music and Warner Chappell have filed suit against Anthropic in the US District Court for the Northern District of California seeking damages for \"tens of thousands\" copyrighted works. The compani"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/986427/distraction-free-writing-gadget-byok-scripts-extensions",
    "domain": "大厂 AI 动态",
    "title": "Distraction-free writing gadget BYOK is adding custom extensions",
    "url": "https://www.theverge.com/gadgets/986427/distraction-free-writing-gadget-byok-scripts-extensions",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T16:01:13+00:00",
    "summary": "BYOK is a no-frills, single-purpose gadget that 90 percent of people will find absolutely frivolous. But for those who spend a significant chunk of their lives putting words to virtual paper, there is"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/983448/welcome-to-night-vale-cocreator-joseph-fink-learned-storytelling-from-grim-fandango",
    "domain": "大厂 AI 动态",
    "title": "Welcome to Night Vale cocreator Joseph Fink learned storytelling from Grim Fandango",
    "url": "https://www.theverge.com/entertainment/983448/welcome-to-night-vale-cocreator-joseph-fink-learned-storytelling-from-grim-fandango",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T15:00:00+00:00",
    "summary": "Joseph Fink is the cocreator and cowriter of Welcome to Night Vale, arguably the most important fiction podcast ever. He's also the creator of the noir podcast Unlicensed and Alice Isn't Dead, which t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986033/samsung-galaxy-z-flip-8-review",
    "domain": "大厂 AI 动态",
    "title": "The Galaxy Z Flip 8 is at its best when there’s friction",
    "url": "https://www.theverge.com/tech/986033/samsung-galaxy-z-flip-8-review",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T13:00:00+00:00",
    "summary": "What do you want from a flip phone when it's closed? A simple interface, perhaps notifications and a widget or two, for handling the basics? Or a fully fledged Android experience shrunk down for the F"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/985866/h4rris-nihil-young-edm-suno-ai",
    "domain": "大厂 AI 动态",
    "title": "Musicians-turned-detectives are hunting for AI grifters",
    "url": "https://www.theverge.com/entertainment/985866/h4rris-nihil-young-edm-suno-ai",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T12:00:00+00:00",
    "summary": "As audio-focused generative tools and platforms have gotten more sophisticated, the internet has become increasingly filled with AI-generated music whose melodies and vocals are algorithmically derive"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986364/google-search-ai-overviews-auto-expand",
    "domain": "大厂 AI 动态",
    "title": "Google further buries search results under AI mode",
    "url": "https://www.theverge.com/tech/986364/google-search-ai-overviews-auto-expand",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T22:48:11+00:00",
    "summary": "Google is now automatically expanding its AI search summaries at the top of the results page for some searches, as reported by Search Engine Roundtable. The change, when it kicks in, pushes the typica"
  },
  {
    "id": "rss:https://www.theverge.com/games/986337/xbox-ceo-asha-sharma-project-helix-family-of-devices",
    "domain": "大厂 AI 动态",
    "title": "Xbox CEO calls Project Helix a ‘family of devices’",
    "url": "https://www.theverge.com/games/986337/xbox-ceo-asha-sharma-project-helix-family-of-devices",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T22:03:13+00:00",
    "summary": "According to Xbox CEO Asha Sharma, Project Helix, which she announced in March as a codename for Microsoft's \"next generation console\" - phrasing that seemingly implied a singular device - will actual"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/985741/tcl-qm7l-belkin-thunderbolt-dock-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Save hundreds on a TCL mini-LED TV with quantum dots and high refresh rate",
    "url": "https://www.theverge.com/gadgets/985741/tcl-qm7l-belkin-thunderbolt-dock-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:03:07+00:00",
    "summary": "Amazon and Best Buy have the TCL QM7L mini-LED TV on sale for as low as $797.99 for the 55-inch model, a $200 discount from the usual price. We spotted scaling discounts on larger sizes as well, altho"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/29/sony-music-warner-sue-anthropic-alleging-a-brazen-campaign-of-intellectual-property-theft/",
    "domain": "大厂 AI 动态",
    "title": "Sony Music, Warner sue Anthropic, alleging a “brazen campaign” of intellectual property theft",
    "url": "https://techcrunch.com/2026/08/29/sony-music-warner-sue-anthropic-alleging-a-brazen-campaign-of-intellectual-property-theft/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T18:41:59+00:00",
    "summary": "This latest lawsuit is particularly broad and homes in on accusations of illegal piracy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/29/at-techbbq-europes-ai-conversations-kept-coming-back-to-whos-actually-in-control/",
    "domain": "大厂 AI 动态",
    "title": "At TechBBQ, Europe’s AI conversations kept coming back to: Who’s actually in control?",
    "url": "https://techcrunch.com/2026/08/29/at-techbbq-europes-ai-conversations-kept-coming-back-to-whos-actually-in-control/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T17:51:10+00:00",
    "summary": "Investors, founders, and operators from across Europe arrived for the annual Nordic TechBBQ conference to talk about how humans can have agency over AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/29/were-not-doing-30-bets-a-year-vijay-pande-on-betting-small-after-running-4-billion-at-a16z/",
    "domain": "大厂 AI 动态",
    "title": "“We’re not doing 30 bets a year”: Vijay Pande on betting small after running $4 billion at a16z",
    "url": "https://techcrunch.com/2026/08/29/were-not-doing-30-bets-a-year-vijay-pande-on-betting-small-after-running-4-billion-at-a16z/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T17:36:47+00:00",
    "summary": "Vijay Pande — who left a16z's roughly $4 billion biotech practice last year to start the much smaller, AI-native VZVC — talks about why biology is finally shifting from a \"discovery\" science to an \"en"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/29/hollywood-celebs-are-getting-into-microdrama-apps/",
    "domain": "大厂 AI 动态",
    "title": "Hollywood celebs are getting into microdrama apps",
    "url": "https://techcrunch.com/2026/08/29/hollywood-celebs-are-getting-into-microdrama-apps/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T16:10:00+00:00",
    "summary": "Several Hollywood celebs are ditching the massive eight-figure checks and exotic movie sets for a rising format: microdramas."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/29/the-theragun-sense-makes-everyday-recovery-surprisingly-easy/",
    "domain": "大厂 AI 动态",
    "title": "The Theragun Sense makes everyday recovery surprisingly easy",
    "url": "https://techcrunch.com/2026/08/29/the-theragun-sense-makes-everyday-recovery-surprisingly-easy/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T14:00:00+00:00",
    "summary": "As my 20s are set to come to an end later this year, I’ve officially reached the age where sleeping in the wrong position or stretching just a little too far can cause aches and pains. I’ve always bee"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/29/nvidias-ai-advantage-is-moving-beyond-the-gpu/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia’s AI advantage is moving beyond the GPU",
    "url": "https://techcrunch.com/2026/08/29/nvidias-ai-advantage-is-moving-beyond-the-gpu/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T13:00:00+00:00",
    "summary": "The new generation of data center systems is increasing efficiency with smarter traffic control instead of just more processor cycles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/chinese-automakers-are-following-teslas-bet-that-robots-are-the-next-big-profit-machine/",
    "domain": "大厂 AI 动态",
    "title": "Chinese automakers are following Tesla’s bet that robots are the next big profit machine",
    "url": "https://techcrunch.com/2026/08/28/chinese-automakers-are-following-teslas-bet-that-robots-are-the-next-big-profit-machine/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T23:24:27+00:00",
    "summary": "Technical progress has encouraged a new batch of companies to jump in on the promise of profits from humanoid robots. And they're all Chinese automakers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/is-the-best-way-to-watch-a-movie-on-a-pair-of-sunglasses/",
    "domain": "大厂 AI 动态",
    "title": "Is the best way to watch a movie on a pair of sunglasses?",
    "url": "https://techcrunch.com/2026/08/28/is-the-best-way-to-watch-a-movie-on-a-pair-of-sunglasses/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T22:42:48+00:00",
    "summary": "Are XREAL's smart glasses the way of the future for home entertainment?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/neocloud-lambda-secures-1b-in-debt-to-buy-more-chips/",
    "domain": "大厂 AI 动态",
    "title": "Neocloud Lambda secures $1B in debt to buy more chips",
    "url": "https://techcrunch.com/2026/08/28/neocloud-lambda-secures-1b-in-debt-to-buy-more-chips/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T20:24:11+00:00",
    "summary": "Neocloud Lambda has raised $1B in private debt to buy Nvidia AI chips and lease them to Microsoft. It's the latest in a string of loans, underscoring the high cost of the AI boom."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/an-anthropic-researcher-just-gave-us-a-peek-at-self-improving-ai/",
    "domain": "大厂 AI 动态",
    "title": "An Anthropic researcher just gave us a peek at self-improving AI",
    "url": "https://techcrunch.com/2026/08/28/an-anthropic-researcher-just-gave-us-a-peek-at-self-improving-ai/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T19:30:38+00:00",
    "summary": "Given 10 benchmarks for specific misaligned behaviors, the automated systems were able to improve performance on every single one without degrading overall performance."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/braves-browser-one-ups-chrome-with-its-new-support-for-email-aliases/",
    "domain": "大厂 AI 动态",
    "title": "Brave’s browser one-ups Chrome with its new support for email aliases",
    "url": "https://techcrunch.com/2026/08/28/braves-browser-one-ups-chrome-with-its-new-support-for-email-aliases/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T18:50:00+00:00",
    "summary": "The feature, announced this week, allows Brave's users to sign up for websites and other online services without having to share their personal email addresses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/open-weight-ai-companies-are-the-valleys-hottest-acquisition-targets/",
    "domain": "大厂 AI 动态",
    "title": "Open-weight AI companies are the Valley’s hottest acquisition targets",
    "url": "https://techcrunch.com/2026/08/28/open-weight-ai-companies-are-the-valleys-hottest-acquisition-targets/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T18:19:40+00:00",
    "summary": "There's a lot of capital pouring into the business of giving models away."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/how-sweden-built-one-of-europes-hottest-startup-ecosystems/",
    "domain": "大厂 AI 动态",
    "title": "How Sweden built one of Europe’s hottest startup ecosystems",
    "url": "https://techcrunch.com/2026/08/28/how-sweden-built-one-of-europes-hottest-startup-ecosystems/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:09:05+00:00",
    "summary": "Sophia Bendz, general partner at Cherry Ventures, stopped by Equity to break down the latest in the Swedish tech ecosystem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/more-americans-oppose-police-license-plate-cameras-than-support-them-survey/",
    "domain": "大厂 AI 动态",
    "title": "More Americans oppose police license plate cameras than support them: survey",
    "url": "https://techcrunch.com/2026/08/28/more-americans-oppose-police-license-plate-cameras-than-support-them-survey/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:57:58+00:00",
    "summary": "The backlash against license plate readers comes amid a wave of police abuses of surveillance cameras."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/28/friend-focused-photo-sharing-app-retro-snags-21m/",
    "domain": "大厂 AI 动态",
    "title": "Friend-focused photo-sharing app Retro snags $21M",
    "url": "https://techcrunch.com/2026/08/28/friend-focused-photo-sharing-app-retro-snags-21m/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:35:03+00:00",
    "summary": "Retro, a friend-focused photo-sharing app built by former Instagram employees, has raised more than $21 million in Series A funding."
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
    "title": "Anthropic gets its first court win over the Pentagon’s supply-chain risk label",
    "url": "https://techcrunch.com/2026/08/28/anthropic-gets-its-first-court-win-over-the-pentagons-supply-chain-risk-label/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T12:46:12+00:00",
    "summary": "A federal judge ruled the Trump administration illegally labeled Anthropic a supply-chain risk, handing the AI company a victory as its second Pentagon lawsuit continues in Washington."
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
    "id": "rss:https://stratechery.com/2026/internet-hype-and-real-world-change/",
    "domain": "大厂 AI 动态",
    "title": "2026.35: Internet Hype and Real World Change",
    "url": "https://stratechery.com/2026/internet-hype-and-real-world-change/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of August 24, 2026 including the breaker's advantage, the new battle for HDMI1, and how data center discourse ends."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/i-asked-100-companies-for-my-data-some-deleted-it-instead/",
    "domain": "大厂 AI 动态",
    "title": "I asked 100 companies for my data. Some deleted it instead.",
    "url": "https://arstechnica.com/tech-policy/2026/08/i-asked-100-companies-for-my-data-some-deleted-it-instead/",
    "source": "Reece Rodgers, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T10:50:31+00:00",
    "summary": "Testing 100 companies found privacy requests often led to confusion and dead ends."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/kalshi-cant-evade-nevada-gambling-laws-by-calling-bets-swaps-court-rules/",
    "domain": "大厂 AI 动态",
    "title": "Court rules Kalshi sports bets aren't \"swaps,\" just gambling with a different name",
    "url": "https://arstechnica.com/tech-policy/2026/08/kalshi-cant-evade-nevada-gambling-laws-by-calling-bets-swaps-court-rules/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T22:14:52+00:00",
    "summary": "Kalshi can't evade Nevada gambling laws by calling bets \"swaps,\" judges rule."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/cities-terminate-flock-contracts-at-record-pace-in-august/",
    "domain": "大厂 AI 动态",
    "title": "Cities terminate Flock contracts at record pace in August",
    "url": "https://arstechnica.com/tech-policy/2026/08/cities-terminate-flock-contracts-at-record-pace-in-august/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T21:33:54+00:00",
    "summary": "Cancellations have accelerated."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/rfk-jr-has-lied-to-the-senate-lawmakers-call-for-criminal-probe-ouster/",
    "domain": "大厂 AI 动态",
    "title": "\"RFK Jr. has lied to the Senate\": Lawmakers call for criminal probe, ouster",
    "url": "https://arstechnica.com/health/2026/08/rfk-jr-has-lied-to-the-senate-lawmakers-call-for-criminal-probe-ouster/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T21:17:38+00:00",
    "summary": "RFK Jr. went to Samoa to spread vaccine fears. The measles outbreak after killed 83."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/trump-blacklisting-of-woke-anthropic-deemed-illegal-by-federal-judge/",
    "domain": "大厂 AI 动态",
    "title": "Trump blacklisting of \"woke\" Anthropic deemed illegal by federal judge",
    "url": "https://arstechnica.com/tech-policy/2026/08/trump-blacklisting-of-woke-anthropic-deemed-illegal-by-federal-judge/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T18:07:55+00:00",
    "summary": "Anthropic refused to support lethal autonomous warfare and mass surveillance."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/trump-calls-for-creation-of-a-space-academy-to-train-future-nasa-leaders/",
    "domain": "大厂 AI 动态",
    "title": "Here's what we know about the \"space academy\" Trump just announced",
    "url": "https://arstechnica.com/space/2026/08/trump-calls-for-creation-of-a-space-academy-to-train-future-nasa-leaders/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:36:30+00:00",
    "summary": "\"It's called the US Space Academy. That's a big deal.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/apple-one-and-apple-tv-subscription-prices-increase-by-up-to-20-percent/",
    "domain": "大厂 AI 动态",
    "title": "Apple One and Apple TV subscription prices increase by up to 20 percent",
    "url": "https://arstechnica.com/gadgets/2026/08/apple-one-and-apple-tv-subscription-prices-increase-by-up-to-20-percent/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T17:23:53+00:00",
    "summary": "Annual Apple TV subscriptions get the biggest bump."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/our-10-favorite-scenes-from-t2-judgment-day/",
    "domain": "大厂 AI 动态",
    "title": "Our 10 favorite scenes from T2: Judgment Day",
    "url": "https://arstechnica.com/culture/2026/08/our-10-favorite-scenes-from-t2-judgment-day/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T16:44:47+00:00",
    "summary": "James Cameron's 1991 sci-fi blockbuster returns to theaters this weekend for its 35th anniversary."
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
    "id": "wscn:3778839",
    "domain": "股票",
    "title": "支付行业拐点已至：跨境业务加速，AI支付兑现，行业有望重估",
    "url": "https://wallstreetcn.com/premium/articles/3778839?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T08:53:09+00:00",
    "summary": "2026年上半年，支付行业经历了过去三年未见的拐点性变化：银行卡消费在连续7个季度同比负增长后首次转正，支付牌照存量从峰值271张锐减至不足180张且不再新发。"
  },
  {
    "id": "wscn:3780660",
    "domain": "股票",
    "title": "如何应对快速轮动的行情",
    "url": "https://wallstreetcn.com/articles/3780660",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T08:47:09+00:00",
    "summary": "中信证券表示，在行情快速轮动的阶段，赢家大部分是“低估值系”策略。贸易摩擦步入高发期，汇兑损益的影响也在放大，制约了行情的宽度。打破僵局需要新的变化，近期的AI进展强化了算力需求快速增长的既有趋势，但不足以改变远期商业化叙事，若后续看到类似RSI、防蒸馏等可能的新变化出现则有望打开远期估值空间。"
  },
  {
    "id": "wscn:3780656",
    "domain": "股票",
    "title": "顶尖风投a16z：顶尖人才涌向AI基建，基础设施设计将“推倒重来”",
    "url": "https://wallstreetcn.com/articles/3780656",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T08:39:15+00:00",
    "summary": "a16z核心合伙人认为，随着巨头明年CapEx预估迈向1万亿美元，GPU和存储等核心硬件订单已排至2028年。由于现有计算架构逼近物理极限，机架功率激增数十倍，数据中心的芯片、电力（转向800V直流电）和液冷系统正面临“推倒重来”的全面重构。顶尖创业者涌入硬件的比例已从不足5%跃升至20%至30%以上。"
  },
  {
    "id": "wscn:3780658",
    "domain": "股票",
    "title": "驶入迷雾，静待下一个催化",
    "url": "https://wallstreetcn.com/articles/3780658",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T08:38:03+00:00",
    "summary": "国金证券表示，沃什的偏鹰派表态可能会让此前的宽松交易阶段性受阻，但需要指出的是由于利率上行的内生性力量仍偏弱，本轮紧缩交易可能只需要消化前期宽松预期的部分，而非新一轮紧缩的开始。当前科技产业向上斜率已不能与3月相比，紧缩预期之下也难以独善其身。内需方面，房地产政策的信号意义大于实质，短期交易锐度可能不够。市场未来一个阶段可能进入混沌状态，以防御思维为主，静待下一个催化。"
  },
  {
    "id": "wscn:3780655",
    "domain": "股票",
    "title": "盈利为何这么强？",
    "url": "https://wallstreetcn.com/articles/3780655",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T08:19:25+00:00",
    "summary": "兴业证券认为，盈利取代估值成破局关键。全A盈利超预期双位数高增，中报更验证重磅信号：“科技制造反哺地产消费”的新经济正循环正在跑通。紧抓AI链、出口链与内需反转三大景气主线，抢占基本面全面修复红利。"
  },
  {
    "id": "wscn:3780654",
    "domain": "股票",
    "title": "250年历史复盘：AI资本开支泡沫离破裂还有多远",
    "url": "https://wallstreetcn.com/articles/3780654",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T07:33:59+00:00",
    "summary": "历史“25法则”表明，技术支出达经济产出25%前极少崩盘。目前AI投入远未触及红线，这场狂欢远比想象中持久。美股上行空间依然巨大，请继续跟着AI的节奏起舞！"
  },
  {
    "id": "wscn:3780653",
    "domain": "股票",
    "title": "内存成本飙升，已超越一颗顶级SoC的价格",
    "url": "https://wallstreetcn.com/articles/3780653",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T07:01:54+00:00",
    "summary": "AI正将内存重塑为半导体核心，2026年规模预计达8373亿美元。巨头掷千亿提前抢单，手机存储成本狂飙340%反超顶配SoC。但狂欢之下周期魔咒未解，AI仅拉长并放大了繁荣，投资者须高度警惕未来天量产能兑现后的过剩反噬。"
  },
  {
    "id": "wscn:3780651",
    "domain": "股票",
    "title": "美银Hartnett：逆向投资者正静待两大信号，随时准备转向避险模式",
    "url": "https://wallstreetcn.com/articles/3780651",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T05:53:49+00:00",
    "summary": "Hartnett警告，美伊冲突的潜在妥协，以及即将到来的美国中期选举，将成为触发市场潜在转变的核心信号：任何地缘政治的突然降温或美国中期选举中政治权力的意外更迭，都可能迅速打破当前支撑风险资产无领导力上涨的脆弱共识。在上述两大信号触发之前，他认为市场将延续无领涨板块的\"磨高\"格局。"
  },
  {
    "id": "wscn:3780650",
    "domain": "股票",
    "title": "八月惊涛：贝森特出手干预，政策底牌悄然揭开",
    "url": "https://wallstreetcn.com/articles/3780650",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T05:37:13+00:00",
    "summary": "美财长干预债汇市场，亮明“宁可货币贬值也不容债市崩溃”以托底名义增长的底牌，黄金与比特币等资产重回焦点。同时，AI叙事加速从“建设期”向“应用期”切换。当前市场呈现罕见分化，AI狂欢与非AI资产下跌并行，资金正激烈博弈真正的受益者。"
  },
  {
    "id": "wscn:3780649",
    "domain": "股票",
    "title": "克鲁格曼：沃什“没说的”比“说了的”更重要",
    "url": "https://wallstreetcn.com/articles/3780649",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T03:48:27+00:00",
    "summary": "\"我们得到了一位正常的美联储主席。\"克鲁格曼认为，沃什未暗示降息、未提缩表且放弃替代通胀指标，展现出未迎合政治压力的传统鹰派立场。最大矛盾在于：沃什强调短期利率是核心工具、反对非常规政策，而财政部贝森特同期推进的长债购买计划实质上正是量化宽松。"
  },
  {
    "id": "wscn:3780647",
    "domain": "股票",
    "title": "原油\"回来了\"，成品油\"回不来\"，全球炼油缺口正在扩大",
    "url": "https://wallstreetcn.com/articles/3780647",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T02:51:23+00:00",
    "summary": "高盛称，全球成品油出口同比下降约600万桶/日，波斯湾与俄罗斯贡献四分之三降幅。与原油可绕道不同，受损炼厂无法搬移，波斯湾成品油出口仅恢复战前40%。高盛预计全球炼厂开工率至2027年下半年才能恢复，据此将2027年柴油利润率预期上调逾一倍。"
  },
  {
    "id": "wscn:3780646",
    "domain": "股票",
    "title": "马斯克解决发电瓶颈！SpaceX要自产“燃气轮机叶片”",
    "url": "https://wallstreetcn.com/articles/3780646",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T02:29:10+00:00",
    "summary": "据报道，SpaceX正在德克萨斯州Bastrop筹建铸造厂，自产燃气轮机叶片与导叶，马斯克在社交平台上亲自确认该计划，并称可将涡轮机上线时间提前最多18个月。大摩称，该铸造厂同时兼顾Raptor火箭发动机铸件需求，实现航天与AI业务成本共摊。"
  },
  {
    "id": "wscn:3780645",
    "domain": "股票",
    "title": "OpenAI新王Astra首测曝光，前端不存在了？",
    "url": "https://wallstreetcn.com/articles/3780645",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T02:19:42+00:00",
    "summary": "前端要被OpenAI端了？新模型Astra内测曝光，零样本直出复杂3D网页！凭借多智能体与自纠错等核心技术，彻底实现“想法碾压执行”。传Astra将于9月初发布，以极高性价比正面硬刚Fable 5.1，AI编程新王之战一触即发！"
  },
  {
    "id": "wscn:3780536",
    "domain": "股票",
    "title": "北交所累跌25%成今年最弱市场，拐点会从哪里出现？",
    "url": "https://wallstreetcn.com/premium/articles/3780536?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T01:51:05+00:00",
    "summary": "2026年以来，北证50显著跑输主要宽基指数，背后既包含2025年小盘成长估值扩张后的均值回归，也反映出IPO明显提速与二级市场流动性收缩之间的供需错位。经过连续调整，北证A股相对创业板、科创板重新形成估值折价，低估值公司占比明显提高，而板块盈利和新增上市公司质量并未出现同步恶化。与此同时，公募与指数化资金虽在扩容，绝对规模仍不足以改变市场定价。随着北交所从“资产扩容”逐渐进入“工具完善”阶段，当"
  },
  {
    "id": "wscn:3780644",
    "domain": "股票",
    "title": "强制“5天模拟交易”！为了“降温”杠杆ETF，韩国“花样百出”",
    "url": "https://wallstreetcn.com/articles/3780644",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T01:42:13+00:00",
    "summary": "模拟交易仅支持PC端、每日至少1小时的繁琐要求令韩国散户望而却步。韩国监管层通过提高保证金门槛、强制完成5天模拟交易等组合措施，压制单股杠杆ETF热潮。相关ETF资产规模已从114亿美元骤降至50亿美元，8月净流出规模约达10亿美元，且交易额跌至峰值4%。"
  },
  {
    "id": "wscn:3780643",
    "domain": "股票",
    "title": "中选之后，“特朗普交易”要反噬了？",
    "url": "https://wallstreetcn.com/articles/3780643",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T01:27:00+00:00",
    "summary": "特朗普政府以股权换补贴的\"入股\"策略曾推动英特尔、MP Materials等个股大幅飙升，但涨势多为短暂爆发后迅速回落。随着中期选举临近，民主党若夺回国会，将启动国会听证调查，重创相关企业股价与品牌；与此同时，股东诉讼正质疑《芯片法案》授权合法性，一旦胜诉将动摇整个持股组合。"
  },
  {
    "id": "wscn:3780528",
    "domain": "股票",
    "title": "下周重磅日程：中国PMI与美国非农，G20会议，特斯拉Cybercab，博通、智谱财报",
    "url": "https://wallstreetcn.com/articles/3780528",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T01:06:19+00:00",
    "summary": "中国PMI与美国非农先后出炉，后者作为9月FOMC前最后一份就业报告将直接定价降息节奏；沃勒就通胀前景发言，重要性或超沃什杰克逊霍尔表态。财报层面，博通、智谱相继公布，A/H股中报季收官。事件层面，特斯拉Cybercab发布、黄仁勋与马斯克等出席G20科技部长会议、贝森特或在G20警告各国配合对伊经济制裁、电子元器件涨价潮延续，苹果CEO交接、Shein港股上市同步落地。"
  },
  {
    "id": "wscn:3780642",
    "domain": "股票",
    "title": "杰克逊霍尔大会结束了，除了沃什“放鹰”，还有这些要点",
    "url": "https://wallstreetcn.com/articles/3780642",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T00:56:16+00:00",
    "summary": "欧洲央行官员同步释放鹰派信号，倾向9月加息；英国央行行长贝利则态度温和，暗示暂观其变。此外，特朗普再度施压解雇美联储理事库克，政治干预阴影未散。拉加德、植田和男及鲍威尔均缺席本届会议。会议害聚焦代币化等金融创新挑战。"
  },
  {
    "id": "wscn:3780640",
    "domain": "股票",
    "title": "现房销售制时代到来",
    "url": "https://wallstreetcn.com/articles/3780640",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T00:44:04+00:00",
    "summary": "告别“图纸买房”。三部门发文推行商品房现房销售。政策拒绝一刀切，新项目优先现售并首创“定金制”。此举将从根本上防范烂尾风险、破解新房去化困局；更将重塑房企资金链，倒逼房地产行业加速洗牌与高质量发展。"
  },
  {
    "id": "wscn:3780639",
    "domain": "股票",
    "title": "不让黄金绑架泰铢：泰国央行限制黄金交易是否真见成效？",
    "url": "https://wallstreetcn.com/premium/articles/3780639?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T00:32:07+00:00",
    "summary": "泰国央行限制黄金交易、鼓励美元结算，但近期金价上涨使泰铢与金价相关性回升，政策效果有限，后续或更严。"
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
    "points": 120,
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
    "id": "hn:49289340",
    "domain": "金融",
    "title": "Hooray for index funds–just don't call them passive",
    "url": "https://www.economist.com/finance-and-economics/2026/08/11/hooray-for-index-funds-just-dont-call-them-passive",
    "source": "thm",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-13T17:37:33+00:00",
    "summary": ""
  }
]
```
