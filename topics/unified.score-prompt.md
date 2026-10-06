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

- 今日日期：`2026-10-06`
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
  "date": "2026-10-06",
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
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1931569,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1364576,
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
    "points": 1311076,
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
    "points": 1107977,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1071501,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 895250,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 830303,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 817997,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "AI Agent这两年大家都听麻了，但真到上手，claude、codex这些又是注册、又是命令行，人还没踏进Agent大门，就先被劝退了。这期视频我用0门槛的国产Agent——字节旗下的TraeWork，用六个超真实的案例，手把手带你玩转Agent！完整的文字教程和GitHub神级Skill清单，打包放置顶评论了。教程制作不易，觉得有一点点帮助的话，记得一键三连～"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 703876,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 441340,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 418193,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 307219,
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
    "points": 301176,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 242803,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 229507,
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
    "points": 194481,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 182777,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 128962,
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
    "points": 93911,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 75858,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1jQHr6NEC3",
    "domain": "AI",
    "title": "普通人唯一的出路，就是用上 Claude Code？",
    "url": "http://www.bilibili.com/video/av117380801894316",
    "source": "MaynorAI",
    "platform": "bilibili",
    "points": 62115,
    "published_at": "2026-10-04T04:44:52+00:00",
    "summary": "图源 X @HYhongyu8，你用过 Claude Code 吗？评论区聊聊。"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 60263,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55724,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 54039,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 53646,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48947,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 40310,
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
    "points": 34461,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29803,
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
    "points": 28975,
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
    "points": 27929,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1Zka56QEsv",
    "domain": "AI",
    "title": "为了用上Claude，我被封了10个号｜网络、代充、KYC、苹果美区踩坑全记录",
    "url": "http://www.bilibili.com/video/av117349864708105",
    "source": "一唯光明故",
    "platform": "bilibili",
    "points": 24889,
    "published_at": "2026-09-28T17:34:14+00:00",
    "summary": "重度 AI 用户，工作全靠它：写报告、做 PPT、处理数据、写 Python 跑内网分析、写前端网页。\n为了用上 Claude，前前后后被封了不下 10 个号，这期把我踩过的坑一次讲清楚。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23764,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22804,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1TJh666Eua",
    "domain": "AI",
    "title": "【实战演示】2026唯一需要掌握的AI软件：Codex全流程实操教学",
    "url": "http://www.bilibili.com/video/av117309565831190",
    "source": "立得AI-阿真",
    "platform": "bilibili",
    "points": 20054,
    "published_at": "2026-09-22T03:00:00+00:00",
    "summary": "整理不易，需要知识库的小伙伴，三连后给后台回复“知识库”，看到了会第一时间发你哦"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 19740,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1gFeX6XEy6",
    "domain": "AI",
    "title": "vibe coding焚决",
    "url": "http://www.bilibili.com/video/av117295070316350",
    "source": "码农人帥气质佳",
    "platform": "bilibili",
    "points": 18575,
    "published_at": "2026-09-19T01:20:14+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1PdhR6GEsa",
    "domain": "AI",
    "title": "vibe coding现况",
    "url": "http://www.bilibili.com/video/av117336426158756",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 17460,
    "published_at": "2026-10-04T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 14275,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 12937,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12072,
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
    "points": 9598,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 9529,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 7723,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1uA4YeNEFd",
    "domain": "AI",
    "title": "CocosCreator+Cursor零代码AI游戏开始演示",
    "url": "http://www.bilibili.com/video/av113113684840361",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 7396,
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
    "points": 7112,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1snhi6WE5P",
    "domain": "AI",
    "title": "【Cursor使用教程】史上最强AI编程工具Cursor！Cursor入门到精通保姆级教程！安装搭建/高阶技巧使用/开发小游戏/应用场景案例实战",
    "url": "http://www.bilibili.com/video/av117308156614035",
    "source": "图灵课堂",
    "platform": "bilibili",
    "points": 6943,
    "published_at": "2026-09-21T08:55:13+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n全套AI大模型笔记/学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "domain": "AI",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "platform": "bilibili",
    "points": 6935,
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6847,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1cKfKYgEQ7",
    "domain": "AI",
    "title": "MasterGo MCP初体验",
    "url": "http://www.bilibili.com/video/av114268359891106",
    "source": "MasterGo-莫高设计",
    "platform": "bilibili",
    "points": 6706,
    "published_at": "2025-04-02T12:30:54+00:00",
    "summary": "https://mp.weixin.qq.com/s/bE-ahoZ_njPVE9hXN1dzVw 文内有操作指南 及 MCP 官方社群～"
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1091,
    "published_at": "2026-09-28T02:05:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 403,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49906100",
    "domain": "AI 算力 / 半导体",
    "title": "OpenDLSS: A Vulkan Reimplementation of Nvidia's DLSS 5 Neural Rendering Network",
    "url": "https://github.com/maanHimself/OpenDLSS-NR",
    "source": "sagacity",
    "platform": "hackernews",
    "points": 278,
    "published_at": "2026-09-30T08:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-09-24T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49933958",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon seeks to offload $8B of Nvidia chips to investors",
    "url": "https://www.reuters.com/business/retail-consumer/amazon-seeks-offload-8-billion-nvidia-chips-investors-ft-reports-2026-10-02/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-10-02T14:30:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49926773",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Janus – Go binary that runs GGUF models via Vulkan on AMD/Intel/Nvidia",
    "url": "https://github.com/Vibra-Ingenn/Janus",
    "source": "Maverick617",
    "platform": "hackernews",
    "points": 106,
    "published_at": "2026-10-01T20:36:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49879032",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says AI distillation is 'competition.'",
    "url": "https://www.cnbc.com/2026/09/28/nvidias-jensen-huang-ai-distillation-china.html",
    "source": "cramer4next",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-28T14:55:34+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/kepler-aims-to-launch-energy-saving-replacement-for-hbm-in-2027/",
    "domain": "AI 算力 / 半导体",
    "title": "Kepler Aims to Launch Energy-Saving Replacement for HBM in 2027",
    "url": "https://www.eetimes.com/kepler-aims-to-launch-energy-saving-replacement-for-hbm-in-2027/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T20:00:00+00:00",
    "summary": "Kepler targets 2027 production for 3D ferroelectric memory promising 5–10× better bandwidth per watt than HBM. The post Kepler Aims to Launch Energy-Saving Replacement for HBM in 2027 appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/trusted-ai-why-intelligence-alone-isnt-enough/",
    "domain": "AI 算力 / 半导体",
    "title": "Trusted AI: Why Intelligence Alone Isn’t Enough",
    "url": "https://www.eetimes.com/trusted-ai-why-intelligence-alone-isnt-enough/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T17:48:56+00:00",
    "summary": "See how trusted AI combines intelligence, domain expertise, and deterministic verification to boost confidence in semiconductor design. The post Trusted AI: Why Intelligence Alone Isn’t Enough appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/access-granted-unlocking-building-safety-and-security-controls-with-audio/",
    "domain": "AI 算力 / 半导体",
    "title": "ACCESS GRANTED – Unlocking Building Safety and Security Controls with Audio",
    "url": "https://www.eetimes.com/access-granted-unlocking-building-safety-and-security-controls-with-audio/",
    "source": "Same Sky and Arrow",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T16:08:24+00:00",
    "summary": "This webinar will cover current controls, modern technology selection, application considerations, and tailored audio component choices. The post ACCESS GRANTED – Unlocking Building Safety and Securit"
  },
  {
    "id": "rss:https://www.eetimes.com/gpt-synopsys-combines-ic-design-eda-with-agentic-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "GPT-Synopsys Combines IC Design EDA with Agentic AI",
    "url": "https://www.eetimes.com/gpt-synopsys-combines-ic-design-eda-with-agentic-ai/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T12:00:00+00:00",
    "summary": "Synopsys joins OpenAI for a leap of faith in AI-native IC design by augmenting frontier models with EDA tools. The post GPT-Synopsys Combines IC Design EDA with Agentic AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/electric-car-makers-need-to-appeal-to-the-other-90/",
    "domain": "AI 算力 / 半导体",
    "title": "Electric Car Makers Need to Appeal to the ‘Other 90%’",
    "url": "https://www.eetimes.com/electric-car-makers-need-to-appeal-to-the-other-90/",
    "source": "Charles Murray",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T05:30:55+00:00",
    "summary": "Broader appeal for the electric car is a big challenge. Innovation is still the best solution. The post Electric Car Makers Need to Appeal to the ‘Other 90%’ appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/corsairs-tiny-pc-touchscreen-discounted-in-all-five-colors-now-usd50-off-xeneon-edge-14-5-inch-lcd-touchscreen-hits-usd199-99",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's tiny PC touchscreen discounted in all five colors, now $50 off",
    "url": "https://www.tomshardware.com/pc-components/corsairs-tiny-pc-touchscreen-discounted-in-all-five-colors-now-usd50-off-xeneon-edge-14-5-inch-lcd-touchscreen-hits-usd199-99",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T08:57:01+00:00",
    "summary": "Get 20% off the Corsair Xeneon Edge 14.5-inch LCD Touchscreen."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/amazon-prime-big-deal-days-2026-day-one",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals live",
    "url": "https://www.tomshardware.com/live/news/amazon-prime-big-deal-days-2026-day-one",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T06:50:09+00:00",
    "summary": "Get all the best deals in the October 2026 Amazon Prime Big Deal Days tech event."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/samsung-9100-pro-ssds-slashed-up-to-41-percent-while-supplies-last-huge-price-cuts-hit-all-capacities-from-1tb-to-8tb",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung 9100 Pro SSDs slashed up to 41% while supplies last — huge price cuts hit all capacities from 1TB to 8TB",
    "url": "https://www.tomshardware.com/pc-components/samsung-9100-pro-ssds-slashed-up-to-41-percent-while-supplies-last-huge-price-cuts-hit-all-capacities-from-1tb-to-8tb",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T05:09:30+00:00",
    "summary": "Amazon slashes the prices of Samsung's entire 9100 Pro lineup of PCIe 5.0 SSDs during the Big Deals sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-hdds/get-a-rare-deal-on-the-shuckable-16tb-seagate-expansion-desktop-drive-at-usd0-02-per-gb-save-usd100-on-this-big-drive-ahead-of-prime-big-deal-days",
    "domain": "AI 算力 / 半导体",
    "title": "Get a rare deal on a shuckable 16TB Seagate Expansion Desktop drive at $0.02 per GB",
    "url": "https://www.tomshardware.com/pc-components/external-hdds/get-a-rare-deal-on-the-shuckable-16tb-seagate-expansion-desktop-drive-at-usd0-02-per-gb-save-usd100-on-this-big-drive-ahead-of-prime-big-deal-days",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T01:18:02+00:00",
    "summary": "The Seagate Expansion Desktop 16TB is a surprisingly decent value at $449.99, at least given where high-capacity HDD prices sit broadly right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/these-32gb-ddr5-memory-kits-are-the-cheapest-available-on-the-market-we-found-the-cheapest-one-around-plus-amd-and-intel-tailored-options",
    "domain": "AI 算力 / 半导体",
    "title": "Get into a 32GB DDR5 memory kit for less this Big Deals Day with these picks",
    "url": "https://www.tomshardware.com/pc-components/these-32gb-ddr5-memory-kits-are-the-cheapest-available-on-the-market-we-found-the-cheapest-one-around-plus-amd-and-intel-tailored-options",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T23:29:26+00:00",
    "summary": "DDR5 RAM is still expensive, but some sizeable discounts on 32GB kits this Prime Big Deals Day week make getting 32GB into your build easier than it has been. Check out our picks."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/its-finally-a-good-time-to-buy-a-raptor-lake-cpu-during-prime-big-deals-day-chips-drop-to-all-time-low-prices-as-inventory-seemingly-stabilizes",
    "domain": "AI 算力 / 半导体",
    "title": "It's finally a good time to buy a Raptor Lake CPU during Prime Big Deals Day",
    "url": "https://www.tomshardware.com/pc-components/cpus/its-finally-a-good-time-to-buy-a-raptor-lake-cpu-during-prime-big-deals-day-chips-drop-to-all-time-low-prices-as-inventory-seemingly-stabilizes",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T23:25:04+00:00",
    "summary": "Intel's 14th Gen Raptor Lake Refresh CPUs are finally getting some good discounts after a year of inconsistent pricing, and some of these chips are even dropping to all-time lows."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/nvidia-rtx-5060-ti-gaming-pc-hits-usd999-with-8-core-ryzen-cpu-16gb-ram-and-1tb-pcie-4-0-ssd-usd600-instant-savings-on-a-complete-1080p-powerhouse",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 5060 Ti gaming PC hits $999 with 8-core Ryzen CPU, 16GB RAM, and 1TB PCIe 4.0 SSD — $600 instant savings on a complete 1080p powerhouse",
    "url": "https://www.tomshardware.com/pc-components/nvidia-rtx-5060-ti-gaming-pc-hits-usd999-with-8-core-ryzen-cpu-16gb-ram-and-1tb-pcie-4-0-ssd-usd600-instant-savings-on-a-complete-1080p-powerhouse",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T19:28:28+00:00",
    "summary": "MSI's Codex Z2C is on sale for $999 and comes with a Ryzen 7 8700F and a GeForce RTX 5060 Ti 8GB."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-switch-2-drops-to-gbp354-99-all-time-low-to-defy-the-ai-tax-pocket-gbp65-in-savings-across-these-retailers",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo Switch 2 drops to £354.99 all-time low to defy the AI tax — pocket £65 in savings across these retailers",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-switch-2-drops-to-gbp354-99-all-time-low-to-defy-the-ai-tax-pocket-gbp65-in-savings-across-these-retailers",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T18:13:45+00:00",
    "summary": "The Nintendo Switch 2, typically priced at £419.99, is now available for just £354.99, giving you a great 15% savings!"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/amazons-prime-big-deal-day-sales-have-big-savings-on-macbooks-and-mac-minis-up-to-usd600-in-savings-on-apple-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Snag an Apple MacBook or Mac Mini with these Amazon Prime Big Deal Days deals that can save you up to $600",
    "url": "https://www.tomshardware.com/laptops/macbooks/amazons-prime-big-deal-day-sales-have-big-savings-on-macbooks-and-mac-minis-up-to-usd600-in-savings-on-apple-hardware",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T17:16:38+00:00",
    "summary": "Amazon's Prime Big Deal Days sales event is a great opportunity to pick up a new Apple MacBook or Mac Mini at a discount."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/grab-this-usd79-98-tp-link-wireless-router-with-wi-fi-7-support-at-its-lowest-ever-price-33-percent-discount-on-archer-be3600-delivers-multi-gigabit-speeds-for-lag-free-streaming-and-gaming",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this $79.98 TP-Link wireless router with Wi-Fi 7 support at its lowest ever price",
    "url": "https://www.tomshardware.com/networking/routers/grab-this-usd79-98-tp-link-wireless-router-with-wi-fi-7-support-at-its-lowest-ever-price-33-percent-discount-on-archer-be3600-delivers-multi-gigabit-speeds-for-lag-free-streaming-and-gaming",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T16:15:51+00:00",
    "summary": "This TP-Link Archer BE3600 wireless router is down to a record-low price, now just $79.98 on Amazon ahead of its big sale event."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/ultrabooks-ultraportables/intels-googlebooks-might-not-run-some-android-apps-as-well-as-qualcomms-google-says-this-is-because-android-apps-were-designed-for-arm-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Googlebooks might not run some Android apps as well as Qualcomm's",
    "url": "https://www.tomshardware.com/laptops/ultrabooks-ultraportables/intels-googlebooks-might-not-run-some-android-apps-as-well-as-qualcomms-google-says-this-is-because-android-apps-were-designed-for-arm-chips",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T15:53:44+00:00",
    "summary": "Some Android apps not optimized for x86-64 may have trouble running on Intel Googlebooks."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-attempts-to-get-ahead-of-expected-rtx-spark-launch-with-gorgon-halo-ai-benchmarks-company-says-it-has-shipped-over-half-a-million-agentic-pcs-to-date",
    "domain": "AI 算力 / 半导体",
    "title": "AMD attempts to get ahead of expected RTX Spark launch with Gorgon Halo benchmarks",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-attempts-to-get-ahead-of-expected-rtx-spark-launch-with-gorgon-halo-ai-benchmarks-company-says-it-has-shipped-over-half-a-million-agentic-pcs-to-date",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T15:38:45+00:00",
    "summary": "AMD is getting ahead of an expected RTX Spark launch later this week with a few benchmarks for its flagship Gorgon Halo chip, the Ryzen AI Max+ Pro 495."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/take-usd40-off-the-blistering-ryzen-7-9800x3d-and-get-two-freebies-just-usd429-buys-one-of-the-fastest-gaming-processors-around-with-a-free-msi-240mm-aio-and-a-game",
    "domain": "AI 算力 / 半导体",
    "title": "Take $40 off the blistering Ryzen 7 9800X3D and get two freebies",
    "url": "https://www.tomshardware.com/pc-components/take-usd40-off-the-blistering-ryzen-7-9800x3d-and-get-two-freebies-just-usd429-buys-one-of-the-fastest-gaming-processors-around-with-a-free-msi-240mm-aio-and-a-game",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T13:47:51+00:00",
    "summary": "Get some solid deals on X3D chips from Newegg. Buy a Ryzen 7 9800X3D for only $429 and Newegg throws in a free 240mm AIO and AMD Onimusha game"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/tencent-scores-100-000-offshore-ai-chip-deal-with-oracle-for-usd7-billion-despite-climbing-prices-per-hour-costs-estimated-to-be-43-percent-under-standard-h100-rental-rates",
    "domain": "AI 算力 / 半导体",
    "title": "Tencent scores 100,000 offshore AI chip deal with Oracle for $7 billion despite climbing prices",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/tencent-scores-100-000-offshore-ai-chip-deal-with-oracle-for-usd7-billion-despite-climbing-prices-per-hour-costs-estimated-to-be-43-percent-under-standard-h100-rental-rates",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T13:20:00+00:00",
    "summary": "Tencent is reportedly renting 100,000 AI chips from Oracle data centers in Southeast Asia for about $7 billion over five years."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/32gb-ram-config-hits-top-spot-on-steam-survey-despite-memory-chip-shortage-amd-closing-in-on-intel-at-more-than-48-percent-share",
    "domain": "AI 算力 / 半导体",
    "title": "32GB dethrones 16GB as top RAM capacity in gaming rigs despite memory shortage",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/32gb-ram-config-hits-top-spot-on-steam-survey-despite-memory-chip-shortage-amd-closing-in-on-intel-at-more-than-48-percent-share",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T13:00:00+00:00",
    "summary": "The September 2026 Steam Survey showed a surprising result despite extreme RAM pricing."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/modder-brings-original-xbox-emulation-to-jailbroken-ps5-xpsemu-plays-halo-2-and-forza-as-ps5-emulators-outnumber-its-15-exclusives",
    "domain": "AI 算力 / 半导体",
    "title": "Modder brings original Xbox emulation to jailbroken PS5",
    "url": "https://www.tomshardware.com/video-games/playstation/modder-brings-original-xbox-emulation-to-jailbroken-ps5-xpsemu-plays-halo-2-and-forza-as-ps5-emulators-outnumber-its-15-exclusives",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T12:40:00+00:00",
    "summary": "The original Xbox can now be emulated on the PS5 thanks to a solo developer's port of Xemu, a popular Xbox emulator."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-ends-secret-data-center-pacts-and-pledges-usd1-billion-to-host-towns-aws-promises-30-000-home-efficiency-retrofits-amid-100-proposed-bans",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon ends secret data center pacts and pledges $1 billion to host towns",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-ends-secret-data-center-pacts-and-pledges-usd1-billion-to-host-towns-aws-promises-30-000-home-efficiency-retrofits-amid-100-proposed-bans",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T12:20:00+00:00",
    "summary": "AWS' Data Center Commitment program aims to sweeten the pill for those who live near AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/google-ai-data-center-project-investigated-after-420-football-fields-of-finnish-forest-razed-trees-were-removed-before-a-mandatory-environmental-impact-assessment-say-reports",
    "domain": "AI 算力 / 半导体",
    "title": "Google AI data center project investigated after 420 football fields of Finnish forest demolished",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/google-ai-data-center-project-investigated-after-420-football-fields-of-finnish-forest-razed-trees-were-removed-before-a-mandatory-environmental-impact-assessment-say-reports",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T12:15:37+00:00",
    "summary": "Google’s latest data center construction project in Finland is being investigated after the company representing the search giant reportedly cleared over 300 hectares of forest before obtaining a mand"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/former-openai-safety-employee-says-companys-safety-culture-is-broken-exits-company-after-failed-kill-switch-and-july-huggingface-hack",
    "domain": "AI 算力 / 半导体",
    "title": "Former OpenAI safety employee says company’s safety culture is broken",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/former-openai-safety-employee-says-companys-safety-culture-is-broken-exits-company-after-failed-kill-switch-and-july-huggingface-hack",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T11:50:00+00:00",
    "summary": "David Robinson argues that Silicon Valley lacks the wisdom on how to handle AI safely and urges the industry to seek outside experts to help build a culture that prioritizes it."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/wolverine-ps5-exclusive-ported-to-pc-in-buggy-solo-project-using-ai-source-code-was-taken-from-sony-2023-ransomware-attack",
    "domain": "AI 算力 / 半导体",
    "title": "Wolverine PS5 exclusive ported to PC in buggy solo project using AI",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/wolverine-ps5-exclusive-ported-to-pc-in-buggy-solo-project-using-ai-source-code-was-taken-from-sony-2023-ransomware-attack",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T11:46:28+00:00",
    "summary": "Solo developer gets Wolverine \"working\" on PC thanks to the 2023 source code leak."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/china-stockpiled-343-immersion-duv-tools-for-advanced-chipmaking-report-claims-270-asml-scanners-can-produce-7nm-processors-without-sanctioned-euv-tools",
    "domain": "AI 算力 / 半导体",
    "title": "China stockpiled 343 immersion DUV tools for advanced chipmaking",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/china-stockpiled-343-immersion-duv-tools-for-advanced-chipmaking-report-claims-270-asml-scanners-can-produce-7nm-processors-without-sanctioned-euv-tools",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T11:35:00+00:00",
    "summary": "Centre for Technology & Statecraft (CTS) calls for banning exports of all immersion DUV tools to China, echoes the MATCH Act by U.S. legislators."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-warns-usd68-billion-in-blocked-data-centers-threatens-us-ai-lead-aws-ceo-decries-100-proposed-bans-pledges-usd1b-community-fund",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon warns $68 billion in blocked data centers threatens US AI lead",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-warns-usd68-billion-in-blocked-data-centers-threatens-us-ai-lead-aws-ceo-decries-100-proposed-bans-pledges-usd1b-community-fund",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T11:15:00+00:00",
    "summary": "AWS CEO warns that growing opposition to data centers could undermine U.S. AI leadership, while defending buildouts against concerns over water consumption, electricity costs, pollution, and community"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/russias-zntc-reportedly-completes-development-of-130nm-capable-litho-tool-volume-production-still-years-away",
    "domain": "AI 算力 / 半导体",
    "title": "Russian firm completes country's first 130nm-capable chipmaking tool, trails modern equipment by 25 years",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/russias-zntc-reportedly-completes-development-of-130nm-capable-litho-tool-volume-production-still-years-away",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T10:50:00+00:00",
    "summary": "ZNTC completes development of Russia's first 130nm-capable lithography stepper, which could be used to produce chips sometimes late this decade, or rather early next."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-senate-kills-bill-that-could-potentially-shield-americans-from-skyrocketing-power-bills-due-to-ai-data-centers-opponents-say-bill-is-toothless-and-doesnt-do-enough-to-protect-citizens",
    "domain": "AI 算力 / 半导体",
    "title": "US Senate kills bill that could potentially shield Americans from skyrocketing power bills due to AI data centers",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-senate-kills-bill-that-could-potentially-shield-americans-from-skyrocketing-power-bills-due-to-ai-data-centers-opponents-say-bill-is-toothless-and-doesnt-do-enough-to-protect-citizens",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T10:25:00+00:00",
    "summary": "The U.S. Senate has blocked the Ratepayer Protection Act in a 57-43 vote, killing legislation that would have pushed regulators to consider making data centers pay the incremental grid costs created b"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/customer-sends-two-stick-usd16-000-ddr5-memory-kit-to-repair-shop-soaring-replacement-costs-make-dimm-repairs-viable-technician-revives-dead-module-with-hot-air-reflow-and-new-pmic",
    "domain": "AI 算力 / 半导体",
    "title": "Customer sends two-stick $16,000 DDR5 memory kit to repair shop",
    "url": "https://www.tomshardware.com/pc-components/ddr5/customer-sends-two-stick-usd16-000-ddr5-memory-kit-to-repair-shop-soaring-replacement-costs-make-dimm-repairs-viable-technician-revives-dead-module-with-hot-air-reflow-and-new-pmic",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T10:00:00+00:00",
    "summary": "A YouTube channel best known for its skillful graphics card fixes has published its first DDR5 module repair video after the economics of RAM repair change."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11-was-released-five-years-ago-today-microsoft-promises-latest-update-is-predictable-and-low-disruption",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11 was released five years ago today",
    "url": "https://www.tomshardware.com/software/windows/windows-11-was-released-five-years-ago-today-microsoft-promises-latest-update-is-predictable-and-low-disruption",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T09:51:27+00:00",
    "summary": "Windows 11 was released five years ago, on October 5, 2021. But it feels like it's been around longer as Microsoft’s latest OS has put users through so much pain."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-reports-florida-womans-claude-diary-threat-to-shoot-up-sheriffs-office-felony-charge-follows-its-at-least-the-third-such-conversation-to-reach-police-since-august",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic reports Florida woman’s Claude ‘diary’ threat to shoot up sheriff’s office, felony charge follows",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-reports-florida-womans-claude-diary-threat-to-shoot-up-sheriffs-office-felony-charge-follows-its-at-least-the-third-such-conversation-to-reach-police-since-august",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T09:40:00+00:00",
    "summary": "Anthropic reviewers reported a Florida woman’s Claude threat against the Lee County Sheriff’s Office, leading to a felony charge."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/russias-uncrewed-robot-tank-fails-during-debut-military-display-in-front-of-president-putin-vehicle-repeatedly-lost-control-links-and-eventually-got-stuck-in-the-mud-despite-the-switch-to-a-human-driver",
    "domain": "AI 算力 / 半导体",
    "title": "Russia's uncrewed robot tank fails during debut military display in front of President Putin",
    "url": "https://www.tomshardware.com/tech-industry/russias-uncrewed-robot-tank-fails-during-debut-military-display-in-front-of-president-putin-vehicle-repeatedly-lost-control-links-and-eventually-got-stuck-in-the-mud-despite-the-switch-to-a-human-driver",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T09:20:00+00:00",
    "summary": "Russia’s new Shturm uncrewed assault tank reportedly suffered repeated command-link failures during its Tsentr-2026 debut, forcing organizers to use a human driver before the vehicle eventually got st"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modder-fixes-melting-rtx-5090-power-connectors-with-custom-distributor-dual-8-pin-mod-peaks-at-just-40c-during-a-48-hour-550w-stress-test",
    "domain": "AI 算力 / 半导体",
    "title": "Modder 'fixes' melting RTX 5090 power connectors with custom distributor",
    "url": "https://www.tomshardware.com/pc-components/gpus/modder-fixes-melting-rtx-5090-power-connectors-with-custom-distributor-dual-8-pin-mod-peaks-at-just-40c-during-a-48-hour-550w-stress-test",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T14:50:00+00:00",
    "summary": "Reddit user u/DallasGrave shared a fix for his RTX 5090, one of the best graphics cards, whose 12VHPWR connector was overheating, along with an image of a module screwed onto the back of his GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/robotics-startup-has-real-human-vs-robot-cage-match-california-responds-with-cease-and-desist-order-regulator-threatens-misdemeanor-charges-after-youtuber-fights-three-robotic-humanoids",
    "domain": "AI 算力 / 半导体",
    "title": "Robotics startup has real human vs. robot cage match, California responds with cease-and-desist order",
    "url": "https://www.tomshardware.com/tech-industry/robotics/robotics-startup-has-real-human-vs-robot-cage-match-california-responds-with-cease-and-desist-order-regulator-threatens-misdemeanor-charges-after-youtuber-fights-three-robotic-humanoids",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T14:36:25+00:00",
    "summary": "The California State Athletic Commission intervened when it saw a human facing off with a humanoid robot inside the fighting ring."
  },
  {
    "id": "rss:https://www.eetimes.com/autosens-2026-regulations-drive-automotive-sensing-architectures/",
    "domain": "AI 算力 / 半导体",
    "title": "AutoSens 2026: Regulation Drives Automotive Sensing Architectures",
    "url": "https://www.eetimes.com/autosens-2026-regulations-drive-automotive-sensing-architectures/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T15:58:50+00:00",
    "summary": "At AutoSens Europe, automotive sensing designs reflected tighter safety standards, advances in AI processing, and growing cybersecurity requirements. The post AutoSens 2026: Regulation Drives Automoti"
  },
  {
    "id": "rss:https://www.eetimes.com/continuous-health-monitoring-drives-integrated-wearable-system-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Continuous Health Monitoring Drives Integrated Wearable System Design",
    "url": "https://www.eetimes.com/continuous-health-monitoring-drives-integrated-wearable-system-design/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T11:29:26+00:00",
    "summary": "Analog Devices India’s Praveen Jose said device miniaturization is driving higher performance and quality in smaller form factors. The post Continuous Health Monitoring Drives Integrated Wearable Syst"
  },
  {
    "id": "rss:https://www.eetimes.com/qualcomm-doubles-down-on-agentic-ai-at-snapdragon-summit-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Doubles Down on Agentic AI at Snapdragon Summit 2026",
    "url": "https://www.eetimes.com/qualcomm-doubles-down-on-agentic-ai-at-snapdragon-summit-2026/",
    "source": "Jim McGregor, Francis Sideco",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T17:31:45+00:00",
    "summary": "Qualcomm introduced two distinct Snapdragon 8 Elite Gen 6 SoCs for high-end smartphones as it expands personal agentic AI across mobile, wearables, and PCs. The post Qualcomm Doubles Down on Agentic A"
  },
  {
    "id": "rss:https://www.eetimes.com/edge-computing-and-security-for-access-control-applications-getting-the-best-of-the-two-worlds/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge Computing and Security for Access Control Applications: Getting the Best of the Two Worlds",
    "url": "https://www.eetimes.com/edge-computing-and-security-for-access-control-applications-getting-the-best-of-the-two-worlds/",
    "source": "Arrow Electronics, Microchip",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T14:01:12+00:00",
    "summary": "Join us where attendees will see how on-device processing improves resilience, reduces exposure of sensitive data, counters spoofing, and supports practical deployment across buildings, smart locks, v"
  },
  {
    "id": "rss:https://www.eetimes.com/pcba-test-strategies-how-to-select-the-right-methodology-and-tester/",
    "domain": "AI 算力 / 半导体",
    "title": "PCBA Test Strategies: How to Select the Right Methodology and Tester",
    "url": "https://www.eetimes.com/pcba-test-strategies-how-to-select-the-right-methodology-and-tester/",
    "source": "Francesca Pinto, SPEA Electronic Test Products Copywriter",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "Are you struggling with PCBA defects? Learn how to optimize your PCBA testing strategy by combining In-Circuit Testing (ICT), Functional Testing (FCT with Bed-of-Nails or Flying Probe Testers. The pos"
  },
  {
    "id": "hn:49657991",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a $20B Semiconductor Fab (2024)",
    "url": "https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-11T13:22:01+00:00",
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
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1700,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 886,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 759,
    "published_at": "2026-10-04T19:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 607,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 493,
    "published_at": "2026-09-15T17:38:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 354,
    "published_at": "2026-09-21T17:30:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 331,
    "published_at": "2026-09-23T15:29:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-09-07T20:12:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 186,
    "published_at": "2026-09-16T14:32:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-09-25T14:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829387",
    "domain": "大厂 AI 动态",
    "title": "Hackers influence ChatGPT and Gemini to direct users to scam centers",
    "url": "https://medium.com/@arielsimon/dark-sourcery-how-hackers-manipulate-ai-to-scam-you-88df434d2073",
    "source": "ArielSimon",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-09-24T11:54:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-09-26T09:55:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49942592",
    "domain": "大厂 AI 动态",
    "title": "Gemini ending free use of Flash and Pro models",
    "url": "https://www.reddit.com/r/GeminiAI/comments/1wwalmc/wtf_google_getting_rid_of_free_gemini_flash_and/",
    "source": "rjh29",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-10-03T09:13:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49859982",
    "domain": "大厂 AI 动态",
    "title": "Faster prompt lookup drafting in llama.cpp",
    "url": "https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/",
    "source": "pptadversary",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-09-26T19:57:24+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1004820/this-remote-controlled-wagon-is-silly-but-useful",
    "domain": "大厂 AI 动态",
    "title": "This remote-controlled wagon is silly but so very useful",
    "url": "https://www.theverge.com/tech/1004820/this-remote-controlled-wagon-is-silly-but-useful",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T08:00:00+00:00",
    "summary": "Confession: When BougeRV told me about its remote-controlled wagon with animated lighting, I called it in for a laugh, expecting to eviscerate it in a review. It's ridiculous, to be sure. But the Dune"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1005177/google-gemini-call-for-me-expansion-rumors",
    "domain": "大厂 AI 动态",
    "title": "Gemini Call for Me might tell your mom you&#8217;re running late",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1005177/google-gemini-call-for-me-expansion-rumors",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T23:09:55+00:00",
    "summary": "Google may be expanding its \"Call for Me\" AI feature beyond business calls so you can use it to send messages to friends and family. Android Authority reports finding a \"Gemini Calling\" introductory s"
  },
  {
    "id": "rss:https://www.theverge.com/games/1004869/reverse-engineered-games-all-the-news-on-video-game-decomps-recomps-vr-and-web-and-3d-ports",
    "domain": "大厂 AI 动态",
    "title": "Reverse-engineered games: All the news on video game decomps, recomps, VR and web and 3D ports",
    "url": "https://www.theverge.com/games/1004869/reverse-engineered-games-all-the-news-on-video-game-decomps-recomps-vr-and-web-and-3d-ports",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T21:17:45+00:00",
    "summary": "It&#8217;s a wild time for retro gaming. Thanks to decompilations and recompilations of classic titles, those games are becoming unshackled from their proprietary code and original hardware to be port"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1004926/matic-fcc-ban-waiver-conditional-approval",
    "domain": "大厂 AI 动态",
    "title": "The Matic is the first robovac to get an FCC ban waiver, not that it needs it",
    "url": "https://www.theverge.com/policy/1004926/matic-fcc-ban-waiver-conditional-approval",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T21:15:05+00:00",
    "summary": "The Matic is our favorite robot vacuum and robo-mop, and it's also now the first to escape the FCC's Roomba ban. Well, sort of - because the Matic wasn't banned to begin with. Here's what's actually h"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1005075/nolla-health-acne-ai-prescriptions",
    "domain": "大厂 AI 动态",
    "title": "This startup is issuing AI-generated acne prescriptions",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1005075/nolla-health-acne-ai-prescriptions",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T20:14:57+00:00",
    "summary": "People in Utah can now use AI to get a prescription for acne treatment. On Monday, healthcare startup Nolla Health announced that users in the state can scan their faces using its app, allowing its AI"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1004933/ai-math-openai-breakthrough-solution",
    "domain": "大厂 AI 动态",
    "title": "All the drama around AI&#8217;s takeover of mathematics",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1004933/ai-math-openai-breakthrough-solution",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T19:28:59+00:00",
    "summary": "This past year, OpenAI, Anthropic, and other labs have announced breakthroughs on numerous long-standing mathematical problems, in some cases pushing well beyond what researchers expected current syst"
  },
  {
    "id": "rss:https://www.theverge.com/news/1004929/wikipedia-openai-rogue-bots-wikimedia-foundation-outage",
    "domain": "大厂 AI 动态",
    "title": "Wikipedia operator says OpenAI&#8217;s &#8216;rogue&#8217; bots may be linked to a May outage",
    "url": "https://www.theverge.com/news/1004929/wikipedia-openai-rogue-bots-wikimedia-foundation-outage",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T19:05:19+00:00",
    "summary": "Following many recent disclosures about AI agents accessing third-party websites and services, the Wikimedia Foundation, which hosts Wikipedia, says that it \"can confirm that we have discovered some a"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1004785/hyundai-ceo-china-ev-us-market-share",
    "domain": "大厂 AI 动态",
    "title": "Hyundai CEO says only a ‘level playing field’ can minimize damage from China",
    "url": "https://www.theverge.com/transportation/1004785/hyundai-ceo-china-ev-us-market-share",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T18:41:48+00:00",
    "summary": "There's been a lot of doom and gloom from the auto industry lately when the subject of China comes up. Automaker CEOs, in particular, warn that allowing low-cost, high-tech Chinese electric vehicles t"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1004880/openai-chatgpt-text-watermarks-eu-ai-act",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is adding text watermarking in ChatGPT and Codex",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1004880/openai-chatgpt-text-watermarks-eu-ai-act",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T18:08:39+00:00",
    "summary": "An invisible, machine-readable watermark in text output is rolling out to ChatGPT and Codex, but only for users in the European Union at first. OpenAI says its textGrain watermarking \"matched or excee"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1004827/openai-sam-altman-vanity-fair-interview-pr",
    "domain": "大厂 AI 动态",
    "title": "OpenAI PR tells journalist to ‘move on’ while asking Sam Altman about a ChatGPT user&#8217;s suicide",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1004827/openai-sam-altman-vanity-fair-interview-pr",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T16:55:42+00:00",
    "summary": "An OpenAI publicist tried to change the topic of CEO Sam Altman's interview with Vanity Fair's Mark Guiducci after the editor brought up a ChatGPT user's suicide. When Guiducci confronted Altman about"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/lucid-motors-ev-output-falls-to-lowest-level-in-almost-two-years/",
    "domain": "大厂 AI 动态",
    "title": "Lucid Motors’ EV output falls to lowest level in almost 2 years",
    "url": "https://techcrunch.com/2026/10/05/lucid-motors-ev-output-falls-to-lowest-level-in-almost-two-years/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T21:54:01+00:00",
    "summary": "The company is deliberately limiting production after years of struggling to find mass-market demand for its EVs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI will start watermarking ChatGPT’s text in the EU",
    "url": "https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T20:36:48+00:00",
    "summary": "OpenAI will watermark ChatGPT and Codex text in the EU to comply with the AI Act. Editing can make the invisible marks harder to detect, it says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/etched-fields-funding-offers-at-40b-valuation-sources-say/",
    "domain": "大厂 AI 动态",
    "title": "Etched fields funding offers at $40B+ valuation, sources say",
    "url": "https://techcrunch.com/2026/10/05/etched-fields-funding-offers-at-40b-valuation-sources-say/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T20:24:09+00:00",
    "summary": "Just a couple of months after its last big raise, the AI chip startup is already being plied with investment offers at double or more its current value, sources tell TechCrunch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/after-factorys-public-spat-with-khosla-menlo-proudly-invests/",
    "domain": "大厂 AI 动态",
    "title": "After Factory’s public spat with Khosla, Menlo proudly invests",
    "url": "https://techcrunch.com/2026/10/05/after-factorys-public-spat-with-khosla-menlo-proudly-invests/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T19:38:07+00:00",
    "summary": "Days after Vinod Khosla called Factory a struggling also-ran, Menlo has shown up with a check and a glowing blog post."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/",
    "domain": "大厂 AI 动态",
    "title": "Reflection debuts Beam, an open-weight AI model to rival Chinese models at lower compute cost",
    "url": "https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T19:33:53+00:00",
    "summary": "Reflection is aiming Beam and future models at enterprises and sovereign nations. The pitch is to build “AI factories,” a product that would let institutions build their own customized, local AI syste"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/instinct-brings-its-ai-agent-to-group-chats-even-for-friends-without-an-account/",
    "domain": "大厂 AI 动态",
    "title": "Instinct brings its AI agent to group chats, even for friends without an account",
    "url": "https://techcrunch.com/2026/10/05/instinct-brings-its-ai-agent-to-group-chats-even-for-friends-without-an-account/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T18:54:30+00:00",
    "summary": "Instinct is launching group chats that let friends use its AI agent together for tasks like planning trips, organizing carpools, and coordinating events. The company says personal accounts remain sepa"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/tiktok-rolls-out-an-ai-shopping-assistant-and-one-click-checkout/",
    "domain": "大厂 AI 动态",
    "title": "TikTok rolls out an AI shopping assistant and one-click checkout",
    "url": "https://techcrunch.com/2026/10/05/tiktok-rolls-out-an-ai-shopping-assistant-and-one-click-checkout/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T18:29:00+00:00",
    "summary": "TikTok describes its new Shopping Assistant as a conversational AI agent designed to help users discover and purchase products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/at-19-ghost-founder-raises-11-million-to-build-a-3499-computer-for-your-personal-ai/",
    "domain": "大厂 AI 动态",
    "title": "At 19, founder raises $11M for Ghost, maker of a $3,499 computer for personal AI",
    "url": "https://techcrunch.com/2026/10/05/at-19-ghost-founder-raises-11-million-to-build-a-3499-computer-for-your-personal-ai/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T18:07:07+00:00",
    "summary": "Ghost's first product is Core, a personal computer designed specifically for AI agents that can take actions on a person's behalf."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/hot-girl-hotline-is-like-dear-abby-for-the-ai-era/",
    "domain": "大厂 AI 动态",
    "title": "Hot Girl Hotline is like ‘Dear Abby’ for the AI era",
    "url": "https://techcrunch.com/2026/10/05/hot-girl-hotline-is-like-dear-abby-for-the-ai-era/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T17:29:22+00:00",
    "summary": "Founded by two sisters, Hot Girl Hotline uses AI to give young women personalized dating and relationship advice, with an emphasis on safety and avoiding emotional dependency."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/5-startups-that-caught-vcs-attention-at-the-latest-pearx-demo-day/",
    "domain": "大厂 AI 动态",
    "title": "5 startups that caught VCs’ attention at the latest PearX demo day",
    "url": "https://techcrunch.com/2026/10/05/5-startups-that-caught-vcs-attention-at-the-latest-pearx-demo-day/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T17:26:44+00:00",
    "summary": "TechCrunch attended Pear’s latest demo day and discovered which startups generated the most buzz, from spatial models to chips for local AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/hackerranks-ai-interviewer-offers-a-glimpse-into-what-job-interviews-could-become/",
    "domain": "大厂 AI 动态",
    "title": "HackerRank’s AI interviewer offers a glimpse into what job interviews could become",
    "url": "https://techcrunch.com/2026/10/05/hackerranks-ai-interviewer-offers-a-glimpse-into-what-job-interviews-could-become/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T16:43:35+00:00",
    "summary": "HackerRank’s AI interviewer has already conducted more than 500,000 interviews, with Snowflake, Snorkel, and Capgemini among its early testers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/openai-launches-visual-ads-that-appear-alongside-image-generation-results/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches visual ads that appear alongside image generation results",
    "url": "https://techcrunch.com/2026/10/05/openai-launches-visual-ads-that-appear-alongside-image-generation-results/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T15:14:24+00:00",
    "summary": "The new ads will begin to appear later this month in the U.S. only for now, and will feature products and services from an initial test group of advertisers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/lola-vision-systems-is-trying-to-make-it-easier-to-run-ai-models-on-chips/",
    "domain": "大厂 AI 动态",
    "title": "Lola Vision Systems is trying to make it easier to run AI models on chips",
    "url": "https://techcrunch.com/2026/10/05/lola-vision-systems-is-trying-to-make-it-easier-to-run-ai-models-on-chips/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T15:00:00+00:00",
    "summary": "Lola Vision Systems is one of the Startup Battlefield 200 companies battling it out at TechCrunch Disrupt, taking place October 13-15 in San Francisco."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/open-or-closed-ai-how-founders-are-choosing-what-to-build-on-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Open or closed AI? How founders are choosing what to build on at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/10/05/open-or-closed-ai-how-founders-are-choosing-what-to-build-on-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T15:00:00+00:00",
    "summary": "Learn how founders are choosing between building on open or closed AI at TechCrunch Disrupt 2026. Register now to save up to $100 and get a second pass at 50% off."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/hackers-steal-8-million-citizens-records-from-danish-government-database/",
    "domain": "大厂 AI 动态",
    "title": "Hackers steal 8 million citizens’ records from Danish government database",
    "url": "https://techcrunch.com/2026/10/05/hackers-steal-8-million-citizens-records-from-danish-government-database/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T14:58:42+00:00",
    "summary": "The Danish government said the breach of names, addresses, and state-issued ID numbers affects 8 million people, including people living abroad and the deceased."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/researchers-are-tracking-a-chinese-ai-agent-fleet/",
    "domain": "大厂 AI 动态",
    "title": "Researchers are tracking a Chinese AI ‘agent fleet’",
    "url": "https://techcrunch.com/2026/10/05/researchers-are-tracking-a-chinese-ai-agent-fleet/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T14:35:09+00:00",
    "summary": "Independent researchers discovered an agent swarm that seems to be running on Tencent's infrastructure and targeting Alibaba's map service, Amap."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/meet-the-startup-battlefield-200-judges-wholl-decide-the-winner-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Meet the Startup Battlefield 200 judges who’ll decide the winner at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/10/05/meet-the-startup-battlefield-200-judges-wholl-decide-the-winner-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T14:30:00+00:00",
    "summary": "Meet the final five Startup Battlefield judges who'll decide who wins the pitch competition at TechCrunch Disrupt 2026. Get your pass now to save up to $100, and get a second at 50% off."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/the-final-disrupt-stage-lineup-three-days-of-conversations-you-wont-hear-anywhere-outside-of-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "The final Disrupt Stage lineup: Three days of conversations you won’t hear anywhere outside of TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/10/05/the-final-disrupt-stage-lineup-three-days-of-conversations-you-wont-hear-anywhere-outside-of-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T14:00:00+00:00",
    "summary": "The full TechCrunch Disrupt Stage lineup revealed, featuring Max Hodak, Mark Wahlberg, Benchmark partners, and more. Register now to save up to $100 on your pass and get a second at 50% off."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/05/can-safeworld-convince-people-that-gen-ai-robots-wont-hurt-them/",
    "domain": "大厂 AI 动态",
    "title": "Can Safeworld convince people that GenAI robots won’t hurt them?",
    "url": "https://techcrunch.com/2026/10/05/can-safeworld-convince-people-that-gen-ai-robots-wont-hurt-them/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T12:00:00+00:00",
    "summary": "Safeworld is building digital humans to make sure robots don't hurt the real ones."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/",
    "domain": "大厂 AI 动态",
    "title": "Google froze its open source bug bounty program due to a ‘significant rise’ in AI submissions",
    "url": "https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T20:31:07+00:00",
    "summary": "AI slop seems to be overwhelming bug bounty programs."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-and-a-hackers-future/",
    "domain": "大厂 AI 动态",
    "title": "Apple and a Hacker’s Future",
    "url": "https://stratechery.com/2026/apple-and-a-hackers-future/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T10:00:00+00:00",
    "summary": "I was happy for years in Apple's walled garden; with AI, however, their protections feel like limitations."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/10/vulnerability-in-agents-from-google-and-others-exposes-structural-flaw-in-mcp/",
    "domain": "大厂 AI 动态",
    "title": "MCP for agent-to-agent comms may be the riskiest protocol you've never heard of",
    "url": "https://arstechnica.com/security/2026/10/vulnerability-in-agents-from-google-and-others-exposes-structural-flaw-in-mcp/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T22:26:35+00:00",
    "summary": "Trust gaps in the new protocol spread malicious prompts from one agent to another."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/cable-lobby-to-sue-trump-fcc-over-repeal-of-national-tv-ownership-cap/",
    "domain": "大厂 AI 动态",
    "title": "Cable lobby to sue Trump FCC over repeal of national TV ownership cap",
    "url": "https://arstechnica.com/tech-policy/2026/10/cable-lobby-to-sue-trump-fcc-over-repeal-of-national-tv-ownership-cap/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T20:47:48+00:00",
    "summary": "Cable industry to sue, says FCC can't repeal TV ownership limit set by Congress."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/texas-city-demands-2m-for-public-records-on-flock-usage/",
    "domain": "大厂 AI 动态",
    "title": "Texas city demands $2M for public records on Flock usage",
    "url": "https://arstechnica.com/tech-policy/2026/10/texas-city-demands-2m-for-public-records-on-flock-usage/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T20:31:12+00:00",
    "summary": "Prices of public records tracking cops' use of Flock go up as backlash swells."
  },
  {
    "id": "rss:https://arstechnica.com/apple/2026/10/command-line-tool-quickly-removes-apple-intelligence-from-macos-27/",
    "domain": "大厂 AI 动态",
    "title": "Command-line tool quickly removes Apple Intelligence from macOS 27",
    "url": "https://arstechnica.com/apple/2026/10/command-line-tool-quickly-removes-apple-intelligence-from-macos-27/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T19:14:44+00:00",
    "summary": "The tool can free up over 12GB of storage."
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49826087",
    "domain": "股票",
    "title": "16GB iPod Nano 3G Upgrade",
    "url": "https://tuckerosman.com/projects/16gb-ipod-nano",
    "source": "Ivoah",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-24T03:58:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49930086",
    "domain": "股票",
    "title": "US tells France and Germany to release diesel stocks or face US export ban",
    "url": "https://www.reuters.com/business/energy/us-tells-france-germany-release-diesel-stocks-or-face-us-export-ban-sources-say-2026-10-01/",
    "source": "geox",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-10-02T05:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49791944",
    "domain": "股票",
    "title": "Wall Street is growing skeptical of the data center boom",
    "url": "https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-21T19:14:30+00:00",
    "summary": ""
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
    "id": "hn:49816810",
    "domain": "股票",
    "title": "Trump's 1,156 July Stock Trades Involved AI, Big Oil, Weapons-Makers, and More",
    "url": "https://www.commondreams.org/news/donald-trump-stock-trades",
    "source": "cirelli94",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-23T14:33:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49819274",
    "domain": "股票",
    "title": "Morgan Stanley Investment-Bank Deal List Leaked in Email Misfire",
    "url": "https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-investment-bank-deal-124657863.html",
    "source": "wslh",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-09-23T17:08:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594296",
    "domain": "股票",
    "title": "OpenAI 2025 financials $38.5B loss ahead of IPO",
    "url": "https://qz.com/openai-leaked-financials-losses-revenue-ipo-061626",
    "source": "u1hcw9nx",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-09-07T05:41:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49810905",
    "domain": "股票",
    "title": "In 2025, 49 percent of adults under age 30 lived with a parent [pdf]",
    "url": "https://www.federalreserve.gov/publications/files/2025-report-economic-well-being-us-households-202605.pdf",
    "source": "gscott",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-23T02:26:49+00:00",
    "summary": ""
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
    "id": "hn:49948254",
    "domain": "金融",
    "title": "Federal judge calls Flock 'indiscriminate mass surveillance'",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 495,
    "published_at": "2026-10-03T22:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 562,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-09-07T05:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-28T10:30:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 257,
    "published_at": "2026-10-01T13:05:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 256,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 219,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49904408",
    "domain": "金融",
    "title": "Tesla takes on $30B in credit as it approaches unprofitability",
    "url": "https://electrek.co/2026/09/29/tesla-takes-on-30-billion-in-credit-as-it-approaches-unprofitability/",
    "source": "ciconia",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-30T04:37:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731356",
    "domain": "金融",
    "title": "Fed hikes rates as inflation worries push up bond yields",
    "url": "https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 184,
    "published_at": "2026-09-16T18:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 123,
    "published_at": "2026-10-01T01:40:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-24T16:15:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49600997",
    "domain": "金融",
    "title": "No constitutional right to clean water, federal court finds",
    "url": "https://www.usatoday.com/story/news/nation/2026/09/07/court-constitution-right-clean-water/91649488007/",
    "source": "measurablefunc",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T17:52:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-10-01T02:26:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 126,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-10-02T21:28:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49930690",
    "domain": "金融",
    "title": "Quantitative Finance with OCaml",
    "url": "https://qcaml.com/index.html",
    "source": "leonry",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-02T07:14:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T17:11:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-25T21:09:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-08T16:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-09-24T08:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49625461",
    "domain": "金融",
    "title": "Teen reading slumps to worst this century due to surge in screen time",
    "url": "https://finance.yahoo.com/news/teen-reading-slumps-worst-century-111013754.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-09-09T12:29:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49769668",
    "domain": "金融",
    "title": "OpenAI and Anthropic oversold AI security breaches",
    "url": "https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/",
    "source": "hei-lima",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-19T19:59:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730769",
    "domain": "金融",
    "title": "Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue",
    "url": "https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/",
    "source": "rsingel",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-09-16T18:09:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-16T18:05:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49645186",
    "domain": "金融",
    "title": "Streaming Is Raising Prices Faster Than Cable Ever Did",
    "url": "https://www.hollywoodreporter.com/business/business-news/streaming-inflation-raising-prices-cable-1236691404/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-10T15:15:11+00:00",
    "summary": ""
  }
]
```
