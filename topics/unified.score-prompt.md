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

- 今日日期：`2026-08-01`
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
  "date": "2026-08-01",
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
    "points": 1642181,
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
    "points": 1525897,
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
    "points": 1014835,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV12omoB4ExF",
    "domain": "AI",
    "title": "黑马程序员全网最全Coze智能体入门到项目实战全套教程，从AI Agent开发入门到6大AI智能体实战项目，涵盖提示词Prompt、RAG、Bot发布微信公众号",
    "url": "http://www.bilibili.com/video/av115713129843205",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 1010603,
    "published_at": "2025-12-15T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：251215\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 985703,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 446723,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 431111,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 390804,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 383509,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 215014,
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
    "points": 195874,
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
    "points": 178249,
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
    "points": 162866,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 154132,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 149973,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 128042,
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
    "points": 114306,
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
    "points": 92875,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 88146,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1Tv3i6LEX1",
    "domain": "AI",
    "title": "用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍",
    "url": "http://www.bilibili.com/video/av116996217838997",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 76131,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73959,
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
    "points": 68046,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53495,
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
    "points": 47525,
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
    "points": 44800,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 39549,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 38962,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35046,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 34131,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 31024,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1fWixBbEgP",
    "domain": "AI",
    "title": "别再用老方法了！Cocos Creator 3.8 + AI 开发实战：从0构建可商用的登录奖励模块",
    "url": "http://www.bilibili.com/video/av115840888408359",
    "source": "游戏主程进阶之路",
    "platform": "bilibili",
    "points": 25676,
    "published_at": "2026-01-05T05:43:24+00:00",
    "summary": "需 要 源 码 请 【＋O、O、裙】【822】【159】【534】"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 25157,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22676,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 17671,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17658,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17578,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 17480,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "iwenwikii",
    "platform": "bilibili",
    "points": 15758,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV14cZqB8EBY",
    "domain": "AI",
    "title": "AI攻克不了的领域竟然是它？揭秘CNC编程为何让AI束手无策",
    "url": "http://www.bilibili.com/video/av116097411976217",
    "source": "极微视界",
    "platform": "bilibili",
    "points": 15005,
    "published_at": "2026-02-19T12:59:23+00:00",
    "summary": "CNC编程AI化有多难？本视频深度解析为什么AI编程在制造业进展缓慢。\n从材料、刀具、机床到隐性知识，揭秘老师傅的经验为什么无法数字化。\nPowerMill、CloudNC等AI编程软件的真实水平如何？CNC编程师的未来在哪里？\n\n⏱️ 时间轴 Timestamps:\n\n00:00 开篇：AI在CNC领域的困境\n00:20 材料的复杂性：为什么同样是45#钢参数却不同\n01:01 刀具与机床的个体"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 13722,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 10843,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10879,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 9656,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1CU346yEYC",
    "domain": "AI",
    "title": "聊聊Vibe Coding | AI降低了门槛，也降低了成本吗？",
    "url": "http://www.bilibili.com/video/av117008079392929",
    "source": "糖果果的陈同学",
    "platform": "bilibili",
    "points": 8745,
    "published_at": "2026-07-30T08:57:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8082,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 7697,
    "published_at": "2026-06-28T09:05:03+00:00",
    "summary": "企鹅交流群：1038830654"
  },
  {
    "id": "bvid:BV15H37zHE7Q",
    "domain": "AI",
    "title": "开源小智服务器xiaozhi-server自动更新以及最新版本MCP接入点配置保姆教程",
    "url": "http://www.bilibili.com/video/av114794426270759",
    "source": "毕乐labs",
    "platform": "bilibili",
    "points": 7502,
    "published_at": "2025-07-04T10:13:51+00:00",
    "summary": "更新过程中遇到xiaozhi-server无法启动的问题，是因为最新的配置有更新，视频中有展示如何解决。对大家有帮助的话请关注up主~"
  },
  {
    "id": "bvid:BV1tUja6mErW",
    "domain": "AI",
    "title": "安卓最强AI Agent，对标claude code，支持mcp,Agent,skills,支持连接Termux，支持deepseekV4，可用于逆向",
    "url": "http://www.bilibili.com/video/av116771772243496",
    "source": "红温火龙果1",
    "platform": "bilibili",
    "points": 7016,
    "published_at": "2026-06-18T15:19:44+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7010,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 6852,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "hn:49035303",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Microsoft, Meta warn against overregulating open-weight models",
    "url": "https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 659,
    "published_at": "2026-07-24T13:32:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49034868",
    "domain": "AI 算力 / 半导体",
    "title": "Half-Life 2 running natively on HaikuOS",
    "url": "https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18",
    "source": "m0do1",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-07-24T12:53:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122838",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba",
    "url": "https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba",
    "source": "gk1",
    "platform": "hackernews",
    "points": 106,
    "published_at": "2026-07-31T13:24:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49035751",
    "domain": "AI 算力 / 半导体",
    "title": "Open Weights and American AI Leadership [pdf]",
    "url": "https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf",
    "source": "lairv",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-07-24T13:58:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48971128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia DGX Spark as a daily driver",
    "url": "https://daniel.lawrence.lu/blog/2026-07-15-dgx-spark-as-daily-driver/",
    "source": "plun9",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-07-19T19:44:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49071512",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's $750B in Deals Reignite Circular AI Fears",
    "url": "https://www.bloomberg.com/news/articles/2026-07-27/nvidia-s-750-billion-deals-revive-fear-of-ai-circular-financing",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-27T16:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49125140",
    "domain": "AI 算力 / 半导体",
    "title": "Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia",
    "url": "https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-31T16:21:11+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits",
    "url": "https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:48:06+00:00",
    "summary": "AI’s memory wall is turning packaging into architecture as CEA-Leti bets on 3D stacking, chiplets, and cooler power. The post CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits a"
  },
  {
    "id": "rss:https://www.eetimes.com/hybrid-architectures-for-space-missions-frameworks-and-consequence/",
    "domain": "AI 算力 / 半导体",
    "title": "Hybrid Architectures for Space Missions: Frameworks and Consequence",
    "url": "https://www.eetimes.com/hybrid-architectures-for-space-missions-frameworks-and-consequence/",
    "source": "Microchip Technology, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:38:20+00:00",
    "summary": "Join this webinar and explore how Microchip's framework translates architectural intent into component choices that preserve differentiation and margin. The post Hybrid Architectures for Space Mission"
  },
  {
    "id": "rss:https://www.eetimes.com/the-commercial-space-race-powering-the-next-comms-network/",
    "domain": "AI 算力 / 半导体",
    "title": "The Commercial Space Race: Powering the Next Comms Network",
    "url": "https://www.eetimes.com/the-commercial-space-race-powering-the-next-comms-network/",
    "source": "Altera, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T13:34:44+00:00",
    "summary": "Join us to learn how Altera is supporting commercial deployments in orbit today and what's coming next. The post The Commercial Space Race: Powering the Next Comms Network appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/military-ai-agents-under-cyberthreat-the-route-forward/",
    "domain": "AI 算力 / 半导体",
    "title": "Military AI Agents Under Cyberthreat: The Route Forward",
    "url": "https://www.eetimes.com/military-ai-agents-under-cyberthreat-the-route-forward/",
    "source": "Liam Critchley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T07:30:00+00:00",
    "summary": "Rapid military AI adoption brings critical security risks, leaving autonomous battlefield systems vulnerable to cyberattacks. The post Military AI Agents Under Cyberthreat: The Route Forward appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/space-grown-semiconductors-the-next-frontier-for-ai-compute/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Is Compressing Software; Space Is Building the Physical Economy",
    "url": "https://www.eetimes.com/space-grown-semiconductors-the-next-frontier-for-ai-compute/",
    "source": "Zaheer Ali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T21:03:54+00:00",
    "summary": "AI is squeezing software jobs; space and semiconductors are where tech turns physical. The post AI Is Compressing Software; Space Is Building the Physical Economy appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/why-qualcomm-bought-an-open-ai-software-stack/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Qualcomm Bought An Open AI Software Stack",
    "url": "https://www.eetimes.com/why-qualcomm-bought-an-open-ai-software-stack/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:43:40+00:00",
    "summary": "Modular says Qualcomm is committed to keeping Mojo and Max hardware-agnostic as heterogeneous AI infrastructure moves from theory to reality. The post Why Qualcomm Bought An Open AI Software Stack app"
  },
  {
    "id": "rss:https://www.eetimes.com/nidec-positions-precision-reducers-for-cobots-humanoids-and-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "Nidec Positions Precision Reducers for Cobots, Humanoids, and Automation",
    "url": "https://www.eetimes.com/nidec-positions-precision-reducers-for-cobots-humanoids-and-automation/",
    "source": "Nidec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T13:00:00+00:00",
    "summary": "Discover Nidec's gear reducer solutions offering precise gear alignment, and low backlash for smooth, reliable operation under load. The post Nidec Positions Precision Reducers for Cobots, Humanoids, "
  },
  {
    "id": "rss:https://www.eetimes.com/indian-startup-vimag-labs-develops-wirelessly-excited-motor-without-rare-earth-magnets/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Startup Vimag Labs Develops Wirelessly Excited Motor Without Rare-Earth Magnets",
    "url": "https://www.eetimes.com/indian-startup-vimag-labs-develops-wirelessly-excited-motor-without-rare-earth-magnets/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T07:00:00+00:00",
    "summary": "Vimag Labs ditches rare-earth magnets with a wirelessly excited EV motor claiming PMSM-level punch. The post Indian Startup Vimag Labs Develops Wirelessly Excited Motor Without Rare-Earth Magnets appe"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone",
    "domain": "AI 算力 / 半导体",
    "title": "Big tech spends more than $1 trillion on AI infrastructure — additional $745 billion expected to be added to the figure in 2026 alone",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T16:30:34+00:00",
    "summary": "Amazon, Google, Meta, and Microsoft have collectively spent more than $1 trillion on AI investments since the rush started in 2023. However, the big four are planning to spend more on AI CAPEX, with b"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/30-years-of-cpus-at-toms-hardware-looking-back-on-three-decades-of-processors-from-the-pentium-ii-to-ryzen-9-9950x3d2",
    "domain": "AI 算力 / 半导体",
    "title": "30 years of CPUs at Tom’s Hardware — looking back on three decades of processors, from the Pentium II to Ryzen 9 9950X3D2",
    "url": "https://www.tomshardware.com/pc-components/cpus/30-years-of-cpus-at-toms-hardware-looking-back-on-three-decades-of-processors-from-the-pentium-ii-to-ryzen-9-9950x3d2",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:13:36+00:00",
    "summary": "Tom’s Hardware has been covering CPUs for 30 years, and to celebrate, we’re looking back on the last three decades of CPU reviews and how the dynamics between Intel and AMD have shifted in that time."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/toms-hardwares-30th-anniversary-from-dip-switches-and-intel-feuds-to-30-years-of-unbiased-testing",
    "domain": "AI 算力 / 半导体",
    "title": "Tom’s Hardware’s 30th Anniversary — From Intel feuds and DIP switches to 30 years of unbiased testing",
    "url": "https://www.tomshardware.com/pc-components/toms-hardwares-30th-anniversary-from-dip-switches-and-intel-feuds-to-30-years-of-unbiased-testing",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:05:30+00:00",
    "summary": "We take a look back at the history of Tom’s Hardware as we celebrate our 30-year anniversary."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-nearly-doubled-its-inventory-to-11-09-billion-as-memory-costs-ate-its-gross-margin",
    "domain": "AI 算力 / 半导体",
    "title": "Apple CEO Tim Cook says the company is fighting 'a hundred-year flood' on memory pricing — expects to pay even more for memory in September following recent price hikes",
    "url": "https://www.tomshardware.com/tech-industry/apple-nearly-doubled-its-inventory-to-11-09-billion-as-memory-costs-ate-its-gross-margin",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T14:54:55+00:00",
    "summary": "Apple will pay even more for memory in the September quarter than it did in the June quarter, CEO Tim Cook told analysts on the company's earnings call."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/beat-the-ai-price-surge-on-pc-hardware-leverage-newegg-combo-deals-track-amazon-prices-and-shop-refurb-outlets-like-woot",
    "domain": "AI 算力 / 半导体",
    "title": "Beat the AI price surge on PC hardware — leverage Newegg combo deals, track Amazon prices, and shop refurb outlets like Woot",
    "url": "https://www.tomshardware.com/pc-components/beat-the-ai-price-surge-on-pc-hardware-leverage-newegg-combo-deals-track-amazon-prices-and-shop-refurb-outlets-like-woot",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T13:10:00+00:00",
    "summary": "With prices skyrocketing, it’s more important than ever to follow these guidelines to help you find great deals on PC hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Lumentum CEO warns of impending bottleneck on critical material used for silicon photonics — fab and material shortfall already lags 30% below customer needs as co-packaged optics demand skyrockets",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:45:27+00:00",
    "summary": "Lumentum CEO Michael Hurlston told an audience at the RAISE Summit that indium phosphide is heading into a squeeze worse than the one in memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access",
    "domain": "AI 算力 / 半导体",
    "title": "Streaming QR codes at 60 FPS achieves nearly 190 KB/s data rate in phone-to-phone tests — browser-based method requires no app, no networking, no pairing, and no permissions beyond camera access",
    "url": "https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:45:20+00:00",
    "summary": "A developer has created a QR code-driven proof-of-concept data transfer system that shuns any dedicated app requirement and neatly sidesteps mandatory networking, pairing, or giving permissions beyond"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-three-sub-usd400-thunderbolt-5-docking-stations",
    "domain": "AI 算力 / 半导体",
    "title": "Sub-$400 Thunderbolt 5 dock roundup — Keychron and Plugable offer dual HDMI, but UGREEN takes top spot with an M.2 NVMe slot",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-three-sub-usd400-thunderbolt-5-docking-stations",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:40:00+00:00",
    "summary": "All three Thunderbolt 5 docks offer similar performance, but one really stands out with its features."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2",
    "domain": "AI 算力 / 半导体",
    "title": "Valve funding port of Linux RADV Radeon Vulkan driver to Windows — cross-platform effort already runs 'Counter-Strike 2'",
    "url": "https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:25:00+00:00",
    "summary": "Valve funding port of Linux RADV Radeon Vulkan driver to Windows — cross-platform effort already runs Counter-Strike 2"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/setting-up-openclaw-isnt-as-straightforward-as-the-internet-wants-you-to-think-running-local-ai-on-humble-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Setting up OpenClaw isn’t as straightforward as the internet wants you to think – running local AI on humble hardware",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/setting-up-openclaw-isnt-as-straightforward-as-the-internet-wants-you-to-think-running-local-ai-on-humble-hardware",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:20:00+00:00",
    "summary": "How realistic is it to run a local AI model and have it automate tasks for you using hardware that doesn’t cost the Earth? We gave it a shot with a Gorgon Point-powered Mini PC, with mixed results."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/sovol-m1d-3d-printer-is-the-first-open-source-idex-design-with-an-integrated-tool-changer-seven-heads-for-quick-swapping-materials-with-two-fully-independent-nozzles",
    "domain": "AI 算力 / 半导体",
    "title": "New open source printer has 7 toolheads that swap in 5 seconds for fast, zero-waste multi-color 3D printing — Sovol M1D 3D printer is the first open-source IDEX design with an integrated tool-changer",
    "url": "https://www.tomshardware.com/3d-printing/sovol-m1d-3d-printer-is-the-first-open-source-idex-design-with-an-integrated-tool-changer-seven-heads-for-quick-swapping-materials-with-two-fully-independent-nozzles",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:00:00+00:00",
    "summary": "Sovol M1D 3D printer is the first open-source IDEX design with an integrated tool-changer — seven heads for quick-swapping materials with two fully independent nozzles, with 300x300x350mm print volume"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/single-dimm-ddr5-gaming-works-better-than-you-probably-think-amds-3d-v-cache-chips-drop-less-than-3-percent-one-ddr5-dimm-beats-dual-channel-ddr4-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Single-DIMM DDR5 gaming works better than you probably think — one DDR5 DIMM beats dual-channel DDR4 RAM, AMD's 3D V-Cache chips drop less than 3% with single stick",
    "url": "https://www.tomshardware.com/pc-components/ddr5/single-dimm-ddr5-gaming-works-better-than-you-probably-think-amds-3d-v-cache-chips-drop-less-than-3-percent-one-ddr5-dimm-beats-dual-channel-ddr4-ram",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:43:24+00:00",
    "summary": "To avoid rising RAM costs, some PC builders and OEMs have shifted toward using a single DDR5 module for gaming PCs. We test how much of a performance loss that actually represents."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/are-your-motherboards-m-2-heatsinks-making-good-contact-with-your-ssd-we-tested-20-modern-intel-and-amd-motherboards-to-verify",
    "domain": "AI 算力 / 半导体",
    "title": "Your motherboard's M.2 SSD heatsink might be slowing down your SSD — Only 6 of 20 tested boards made full contact",
    "url": "https://www.tomshardware.com/pc-components/motherboards/are-your-motherboards-m-2-heatsinks-making-good-contact-with-your-ssd-we-tested-20-modern-intel-and-amd-motherboards-to-verify",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:43:19+00:00",
    "summary": "We tested 20 motherboards for proper M.2 contact and were surprised at the results – not all make good contact."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-emulation-hits-new-milestone-in-record-time-multiple-3d-games-now-playable-in-kyty-performance-and-support-steadily-improving-with-30-fps-gameplay-possible-today",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 emulation hits new milestone in record time, multiple 3D games now playable in Kyty — Performance and support steadily improving with 30 FPS gameplay possible today",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-emulation-hits-new-milestone-in-record-time-multiple-3d-games-now-playable-in-kyty-performance-and-support-steadily-improving-with-30-fps-gameplay-possible-today",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:40:00+00:00",
    "summary": "The PS5 emulation scene is showing extremely impressive progress, with 3D titles now being playable at around 30 FPS just two weeks after the first 3D titles even became bootable."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-new-radeon-rx-9050-is-roughly-30-percent-slower-than-the-rtx-5050-in-games-early-testing-shows-the-cheapest-8gb-rdna-4-gpu-comfortably-handles-1080p-gaming-but-doesnt-impress",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's new Radeon RX 9050 is roughly 30% slower than the RTX 5050 in games, early testing shows — the cheapest 8GB RDNA 4 GPU comfortably handles 1080p gaming but doesn't impress",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-new-radeon-rx-9050-is-roughly-30-percent-slower-than-the-rtx-5050-in-games-early-testing-shows-the-cheapest-8gb-rdna-4-gpu-comfortably-handles-1080p-gaming-but-doesnt-impress",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:28:54+00:00",
    "summary": "The RX 9050 is slower than the RTX 5050 in every conceivable way except when the latter is constrained in some way. It performs worse in synthetic benchmarks and games but has more efficient power con"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/msi-promises-an-expo-ull-like-boost-for-your-existing-ddr5-high-efficiency-mode-brings-low-latency-tuning-to-older-ram",
    "domain": "AI 算力 / 半导体",
    "title": "MSI promises an EXPO ULL-like boost for your existing DDR5 memory — High-Efficiency Mode brings low-latency tuning to older RAM",
    "url": "https://www.tomshardware.com/pc-components/motherboards/msi-promises-an-expo-ull-like-boost-for-your-existing-ddr5-high-efficiency-mode-brings-low-latency-tuning-to-older-ram",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:20:00+00:00",
    "summary": "A new firmware update for MSI motherboards features High-Efficiency Mode, which offers latency tuning similar to AMD's EXPO ULL on regular memory kits."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd900-on-this-rtx-5070-gaming-pc-from-msi-in-this-limited-time-woot-deal-now-usd1-399-grab-a-huge-saving-on-this-codex-r2-rig-with-a-10-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $900 on this RTX 5070 gaming PC from MSI in this limited-time Woot deal, now $1,399 — grab a huge saving on this Codex R2 rig with a 10-core Intel CPU, 32GB DDR5, and a 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd900-on-this-rtx-5070-gaming-pc-from-msi-in-this-limited-time-woot-deal-now-usd1-399-grab-a-huge-saving-on-this-codex-r2-rig-with-a-10-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:03:17+00:00",
    "summary": "This MSI Codex R2 gaming PC is on sale at Woot for $1,399.99 right now, delivering you a rig with a 10-core Intel Core i5-14400F, Nvidia GeForce RTX 5070, 32GB of DDR5 RAM, and a 1TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsungs-fastest-ssd-is-back-to-prime-day-pricing-only-usd30-difference-between-the-much-faster-gen-5-9100-pro-and-gen-4-990",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's fastest SSD is back to Prime Day pricing — only $30 difference between the much faster Gen 5 9100 Pro and Gen 4 990",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsungs-fastest-ssd-is-back-to-prime-day-pricing-only-usd30-difference-between-the-much-faster-gen-5-9100-pro-and-gen-4-990",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:00:29+00:00",
    "summary": "Returning to Prime Day pricing, Samsung's fastest SSD, the 9100 Pro 2TB, is just $10 more than the previous PCIe generation's champion, the 2TB Samsung 990 Pro SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/modder-der8auer-builds-110cm-3d-printed-chimney-to-passively-cool-ryzen-7-9800x3d-without-fans-radically-simple-pc-mod-cuts-down-cpu-temps-by-19-c-using-the-stack-effect",
    "domain": "AI 算力 / 半导体",
    "title": "Modder der8auer builds 110cm 3D-printed chimney to passively cool Ryzen 7 9800X3D without fans, cuts temps by 19C — radically simple PC mod uses the 'stack effect'",
    "url": "https://www.tomshardware.com/pc-components/cooling/modder-der8auer-builds-110cm-3d-printed-chimney-to-passively-cool-ryzen-7-9800x3d-without-fans-radically-simple-pc-mod-cuts-down-cpu-temps-by-19-c-using-the-stack-effect",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:00:00+00:00",
    "summary": "What if instead of relying on mechanical pressure generated by fans, you could just passively cool your PC using natural convection? That's what der8auer managed to pull off in his new experiment usin"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/qualcomm-powered-robot-collapses-spectacularly-on-stage-during-presentation-prepared-stagehands-rush-to-cloak-and-then-carry-off-stricken-humanoid",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm-powered robot collapses spectacularly on stage during company's keynote — prepared stagehands rush to cloak and then carry off stricken humanoid (updated)",
    "url": "https://www.tomshardware.com/tech-industry/robotics/qualcomm-powered-robot-collapses-spectacularly-on-stage-during-presentation-prepared-stagehands-rush-to-cloak-and-then-carry-off-stricken-humanoid",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T10:40:00+00:00",
    "summary": "A Qualcomm exec suffered from one of the most disastrous tech demos we’ve ever seen live on stage at Computex 2026 this summer when a humanoid robot spectacularly collapsed."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mice/keyboard-giant-keychron-launches-nape-pro-wireless-trackball-mouse-rectangular-form-factor-designed-to-sit-under-spacebar-gives-users-six-customizable-buttons-and-a-control-dial",
    "domain": "AI 算力 / 半导体",
    "title": "Keyboard giant Keychron launches Nape Pro wireless trackball mouse — rectangular form factor designed to sit under spacebar gives users six customizable buttons and a control dial",
    "url": "https://www.tomshardware.com/peripherals/mice/keyboard-giant-keychron-launches-nape-pro-wireless-trackball-mouse-rectangular-form-factor-designed-to-sit-under-spacebar-gives-users-six-customizable-buttons-and-a-control-dial",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T10:25:24+00:00",
    "summary": "The Nape Pro wireless trackball mouse features a rectangular form factor, six customizable buttons, and a control dial. Its unique shape and wireless connectivity let users place it anywhere they like"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/if-you-own-a-3d-printer-you-absolutely-need-to-try-hi3d",
    "domain": "AI 算力 / 半导体",
    "title": "If You Own a 3D Printer, You Absolutely Need to Try Hi3D",
    "url": "https://www.tomshardware.com/3d-printing/if-you-own-a-3d-printer-you-absolutely-need-to-try-hi3d",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T10:20:00+00:00",
    "summary": "Let AI Handle Every Tedious Slicing Step in One Click"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/ambitious-gamer-turns-three-old-subway-menu-signage-pcs-to-gaming-puny-intel-core-i3-machines-can-only-muster-15-fps-running-gta-5-25-fps-on-minecraft",
    "domain": "AI 算力 / 半导体",
    "title": "Ambitious gamer turns fanless Subway menu PCs into gaming rigs — passive Intel Core i3 units manage just 15 fps in GTA V and 25 fps in Minecraft",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/ambitious-gamer-turns-three-old-subway-menu-signage-pcs-to-gaming-puny-intel-core-i3-machines-can-only-muster-15-fps-running-gta-5-25-fps-on-minecraft",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T10:20:00+00:00",
    "summary": "An intrepid TechTuber has tested a trio of passive digital signage mini PCs from the Subway sandwich chain to check if they can be repurposed for gaming fun."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/startup-plans-to-put-nuclear-powered-data-centers-in-the-sea-modular-units-could-be-much-faster-to-deploy-but-questions-about-reliability-and-longevity-remain",
    "domain": "AI 算力 / 半导体",
    "title": "Startup plans to put nuclear-powered data centers in the sea — modular units could be much faster to deploy, but questions about reliability and longevity remain",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/startup-plans-to-put-nuclear-powered-data-centers-in-the-sea-modular-units-could-be-much-faster-to-deploy-but-questions-about-reliability-and-longevity-remain",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T10:00:00+00:00",
    "summary": "Atomarine wants to put data centers on modular barges for ocean-based deployments. The firm says these can be powered by LNG-powered ships and seamlessly swap to ship-based SMRs when they become avail"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-nt-4-0-brought-the-win95-ui-to-servers-30-years-ago-today-milestone-unifying-modern-windows-os-hit-rtm-in-the-pentium-era",
    "domain": "AI 算力 / 半导体",
    "title": "Windows NT 4.0 brought the Win95 UI to servers 30 years ago today — milestone unifying modern Windows OS hit RTM in the Pentium era",
    "url": "https://www.tomshardware.com/software/windows/windows-nt-4-0-brought-the-win95-ui-to-servers-30-years-ago-today-milestone-unifying-modern-windows-os-hit-rtm-in-the-pentium-era",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T09:00:00+00:00",
    "summary": "Microsoft released Windows NT 4.0 to manufacturing partners on this day in 1996."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/shanghai-aishengna-named-as-the-maker-of-chinas-first-domestic-immersion-duv-scanners",
    "domain": "AI 算力 / 半导体",
    "title": "Shanghai Aishengna named as the maker of China's first domestic immersion DUV chipmaking tools — first viable domestic 7nm-capable scanner to be completed by 2038",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/shanghai-aishengna-named-as-the-maker-of-chinas-first-domestic-immersion-duv-scanners",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T16:23:55+00:00",
    "summary": "Aishengna has been named by a single source who declined to be named, and its shareholders, SMEE, and Yuliangsheng didn’t respond to requests for comment."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon accidentally spent $1.8 million using Claude for menial coding task, went 860% over budget —'catastrophically expensive' coding blunders discovered in internal Amazon AI usage metrics",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T16:08:25+00:00",
    "summary": "An internal presentation revealed that a failed AI deployment cost Amazon $1.8 million, while a couple of other projects resulted in hundreds of thousands of extra AI expense. What's worse is that the"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/psa-your-watch-band-may-be-messing-with-your-laptop-magnetic-clasps-can-cause-lid-sensors-to-lock-your-pc",
    "domain": "AI 算力 / 半导体",
    "title": "PSA: Your watch band may be messing with your laptop – magnetic clasps can cause lid sensors to lock your PC",
    "url": "https://www.tomshardware.com/laptops/psa-your-watch-band-may-be-messing-with-your-laptop-magnetic-clasps-can-cause-lid-sensors-to-lock-your-pc",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T15:09:46+00:00",
    "summary": "It’s likely a niche issue, but I discovered recently that my magnetic watch clasp was confusing an Acer laptop into thinking I was closing and opening the lid, causing me to repeatedly get logged out "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/exploring-apple-silicons-local-ai-performance-with-the-mac-studio-and-m4-max-m4-max-beats-gb10-and-strix-halo-in-decode-throughput-but-memory-bandwidth-isnt-everything",
    "domain": "AI 算力 / 半导体",
    "title": "Exploring Apple Silicon’s local AI performance with the Mac Studio and M4 Max — M4 Max beats GB10 and Strix Halo in decode throughput, but memory bandwidth isn't everything",
    "url": "https://www.tomshardware.com/desktops/exploring-apple-silicons-local-ai-performance-with-the-mac-studio-and-m4-max-m4-max-beats-gb10-and-strix-halo-in-decode-throughput-but-memory-bandwidth-isnt-everything",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:52:28+00:00",
    "summary": "Apple Silicon has been a popular choice for local AI exploration thanks to its high memory bandwidth compared to other unified memory platforms. We tested the M4 Max version of Apple's Mac Studio to s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-could-build-more-ai-accelerators-than-nvidia-sells-in-2028-analyst-claims-could-push-the-company-to-use-intel-foundry-to-meet-its-goals",
    "domain": "AI 算力 / 半导体",
    "title": "Google could build more AI accelerators than Nvidia sells in 2028, analyst claims — could push the company to use Intel Foundry to meet its goals",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-could-build-more-ai-accelerators-than-nvidia-sells-in-2028-analyst-claims-could-push-the-company-to-use-intel-foundry-to-meet-its-goals",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:35:50+00:00",
    "summary": "Google eyes to build more TPU AI accelerators in 2028 than Nvidia, if a report by Fubon Research is correct."
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
    "id": "hn:49093429",
    "domain": "AI 算力 / 半导体",
    "title": "Kospi Plunges After Nvidia CEO's Visits Spark 'Huang Curse' Fears",
    "url": "https://www.chosun.com/english/market-money-en/2026/07/29/6FEUZWQT5BG3HMJ3G2RZPHROGM/",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T04:29:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/iot-tech-expo-europe-returns-to-amsterdam-as-industrial-ai-and-edge-intelligence-reshape-connected-industry/",
    "domain": "AI 算力 / 半导体",
    "title": "IoT Tech Expo Europe Returns to Amsterdam as Industrial AI and Edge Intelligence Reshape Connected Industry",
    "url": "https://www.eetimes.com/iot-tech-expo-europe-returns-to-amsterdam-as-industrial-ai-and-edge-intelligence-reshape-connected-industry/",
    "source": "IoT Tech Expo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T00:42:04+00:00",
    "summary": "From autonomous factories and AI-powered robots to connected vehicles and smart cities, organizations are entering a new era where connected systems are expected not only to collect data, but also to "
  },
  {
    "id": "rss:https://www.eetimes.com/dynamic-ai-demands-drive-memory-diversity/",
    "domain": "AI 算力 / 半导体",
    "title": "Dynamic AI Demands Drive Memory Diversity",
    "url": "https://www.eetimes.com/dynamic-ai-demands-drive-memory-diversity/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T18:00:00+00:00",
    "summary": "AI workloads aren't creating new memory categories—they're sharpening the trade-offs between capacity, latency, and power. The post Dynamic AI Demands Drive Memory Diversity appeared first on EE Times"
  },
  {
    "id": "hn:49070311",
    "domain": "AI 算力 / 半导体",
    "title": "Ilya Sutskever's SSI and Nvidia Announce Long-Term Strategic Partnership",
    "url": "https://nvidianews.nvidia.com/news/ilya-sutskevers-safe-superintelligence-inc-and-nvidia-announce-long-term-strategic-partnership",
    "source": "lanakei",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-27T14:33:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 609,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 383,
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
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 197,
    "published_at": "2026-07-27T09:56:37+00:00",
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
    "points": 135,
    "published_at": "2026-07-21T21:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48864507",
    "domain": "大厂 AI 动态",
    "title": "Please don't discontinue Gemini 2.5 Flash",
    "url": "https://discuss.ai.google.dev/t/please-dont-discontinue-gemini-2-5-flash/174246",
    "source": "NickDob",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-07-10T20:00:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096841",
    "domain": "大厂 AI 动态",
    "title": "Google DeepMind dismantles AlphaFold team",
    "url": "https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33",
    "source": "ainch",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-07-29T12:50:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48959297",
    "domain": "大厂 AI 动态",
    "title": "Our Approach to Bioresilience: Isomorphic Labs and Google DeepMind",
    "url": "https://deepmind.google/blog/our-approach-to-bioresilience/",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-07-18T16:02:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/973886/sharge-disk-pro-2-hands-on-switch-2-hdmi-usb-c-dock",
    "domain": "大厂 AI 动态",
    "title": "With Switch 2, iPhone, and laptop tricks, the Sharge Disk Pro 2 is finally a worthy EDC",
    "url": "https://www.theverge.com/gadgets/973886/sharge-disk-pro-2-hands-on-switch-2-hdmi-usb-c-dock",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:09:11+00:00",
    "summary": "Sharge, the company that makes delightful retro Mac-shaped chargers and see-inside batteries, is finally impressing me with a portable SSD. I couldn't recommend the Sharge Disk, Disk Plus, or even the"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/973973/apple-airtag-second-generation-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Apple’s new AirTags are back down to their best price",
    "url": "https://www.theverge.com/gadgets/973973/apple-airtag-second-generation-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:35:45+00:00",
    "summary": "We spotted a great deal on Tile trackers earlier this week that&#8217;s still live, but if you&#8217;re an iPhone owner, we ultimately recommend Apple’s latest AirTag. Right now, you can pick up a fou"
  },
  {
    "id": "rss:https://www.theverge.com/tech/973943/google-earth-ai-image-generation-deepfake-tool",
    "domain": "大厂 AI 动态",
    "title": "Google Earth&#8217;s AI deepfake tool only lasted one day",
    "url": "https://www.theverge.com/tech/973943/google-earth-ai-image-generation-deepfake-tool",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:13:29+00:00",
    "summary": "Google has shut down Google Earth feature it launched Thursday that allowed users to edit satellite images with text prompts using AI. The tool essentially let users create AI deepfakes of the real wo"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/973887/nhtsa-tesla-investigation-suspension",
    "domain": "大厂 AI 动态",
    "title": "The NHTSA is investigating 1.2 million Tesla vehicles over suspension failure reports",
    "url": "https://www.theverge.com/transportation/973887/nhtsa-tesla-investigation-suspension",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T18:33:39+00:00",
    "summary": "The National Highway Traffic Safety Administration (NHTSA) is probing nearly 1.2 million Tesla vehicles after receiving complaints about a suspension failure that could cause \"a loss of vehicle direct"
  },
  {
    "id": "rss:https://www.theverge.com/tech/973889/google-pixel-tag-item-tracker",
    "domain": "大厂 AI 动态",
    "title": "Google might launch a ‘Pixel Tag’",
    "url": "https://www.theverge.com/tech/973889/google-pixel-tag-item-tracker",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T18:27:24+00:00",
    "summary": "Google is seemingly working on an item tracker that might compete with Apple's AirTag. 9to5Google obtained an image of something called a \"Google Pixel Tag\" that has a small oval shape. The publicatio"
  },
  {
    "id": "rss:https://www.theverge.com/tech/973738/robot-vacuum-ban-fewer-choices-higher-prices",
    "domain": "大厂 AI 动态",
    "title": "The ban on robot vacuums won’t make them safer, only worse",
    "url": "https://www.theverge.com/tech/973738/robot-vacuum-ban-fewer-choices-higher-prices",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T17:30:49+00:00",
    "summary": "No other gadget knows as much about your home as a robot vacuum. They map your space, learn your routines, and many now carry a camera and microphone into every room in your house. As AI gives them a "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/973723/tomodachi-life-apple-marshall-stanmore-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Tomodachi Life: Living the Dream is a quirky life sim that’s worth buying at this discount",
    "url": "https://www.theverge.com/gadgets/973723/tomodachi-life-apple-marshall-stanmore-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T17:09:13+00:00",
    "summary": "Looking to start your own island paradise full of Miis based on family, friends, and celebrities, but don’t feel like paying full fare? Woot has Tomodachi Life: Living the Dream for Switch on sale for"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/973764/google-earth-ai-satellite-images",
    "domain": "大厂 AI 动态",
    "title": "Here’s the problem with putting an AI image generator in Google Earth",
    "url": "https://www.theverge.com/ai-artificial-intelligence/973764/google-earth-ai-satellite-images",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T17:05:46+00:00",
    "summary": "A text prompt was all it took to generate reality-warping images using Google Earth's satellite, aerial, and 3D imagery with a now-rolled back AI feature, like these images generated by Digital Diggin"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/973741/ai-music-major-record-labels-charts",
    "domain": "大厂 AI 动态",
    "title": "The major labels propose rules to keep AI slop off the charts",
    "url": "https://www.theverge.com/ai-artificial-intelligence/973741/ai-music-major-record-labels-charts",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T16:36:48+00:00",
    "summary": "Several record labels, including the big three - Universal Music Group, Sony Music, and Warner Music Group - have proposed rules regarding chart eligibility for AI songs. In short, they wouldn't be. T"
  },
  {
    "id": "rss:https://www.theverge.com/tech/973709/new-york-kalshi-lawsuit-illegal-gambling-operation",
    "domain": "大厂 AI 动态",
    "title": "New York sues Kalshi for allegedly running an ‘illegal gambling operation’",
    "url": "https://www.theverge.com/tech/973709/new-york-kalshi-lawsuit-illegal-gambling-operation",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:30:13+00:00",
    "summary": "New York is suing Kalshi over claims the prediction market is running \"an illegal gambling operation.\" In the lawsuit, New York Attorney General Letitia James accuses Kalshi of violating state laws by"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/openai-reportedly-finds-evidence-that-more-of-its-agents-ran-amok/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI reportedly finds evidence that more of its agents ran amok",
    "url": "https://techcrunch.com/2026/07/31/openai-reportedly-finds-evidence-that-more-of-its-agents-ran-amok/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:47:26+00:00",
    "summary": "OpenAI has reportedly found evidence of additional agent misbehavior as it looks into the incident that occurred with Hugging Face."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/rivian-spinoff-also-to-start-delivering-e-bikes-after-months-of-delays/",
    "domain": "大厂 AI 动态",
    "title": "Rivian spinoff Also to start delivering e-bikes after months of delays",
    "url": "https://techcrunch.com/2026/07/31/rivian-spinoff-also-to-start-delivering-e-bikes-after-months-of-delays/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:00:08+00:00",
    "summary": "Also has big plans beyond the TM-B. The startup mostly refers to itself as a \"vehicle\" company and has plans to make four-wheel pedal-assist cargo vehicles for Amazon."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/build-in-public-fail-in-public-what-its-like-to-be-a-founder-under-20-right-now/",
    "domain": "大厂 AI 动态",
    "title": "Silicon Valley loves young founders. Until it doesn’t.",
    "url": "https://techcrunch.com/2026/07/31/build-in-public-fail-in-public-what-its-like-to-be-a-founder-under-20-right-now/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:00:00+00:00",
    "summary": "AI tools have democratized the opportunity to build, shortening the timelines of success and enabling more young people to start successful companies without stepping foot inside a Big Tech company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/india-is-starting-to-pay-for-apps-not-just-download-them/",
    "domain": "大厂 AI 动态",
    "title": "India is starting to pay for apps, not just download them",
    "url": "https://techcrunch.com/2026/07/31/india-is-starting-to-pay-for-apps-not-just-download-them/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T21:07:45+00:00",
    "summary": "India's app market generated a record $345 million in Q2."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/google-nixes-its-earth-ai-feature-one-day-after-launch-amid-criticism-it-would-spread-misinformation/",
    "domain": "大厂 AI 动态",
    "title": "Google nixes its Earth AI feature one day after launch, amid criticism it would spread misinformation",
    "url": "https://techcrunch.com/2026/07/31/google-nixes-its-earth-ai-feature-one-day-after-launch-amid-criticism-it-would-spread-misinformation/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:47:28+00:00",
    "summary": "A tool that allowed anyone to generate fake AI-generated imagery and superimpose it over real Google Earth maps quickly spurred backlash."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/fresh-off-its-wiz-payout-index-ventures-raises-2b-across-three-funds/",
    "domain": "大厂 AI 动态",
    "title": "Fresh off its Wiz payout, Index Ventures raises $2B across three funds",
    "url": "https://techcrunch.com/2026/07/31/fresh-off-its-wiz-payout-index-ventures-raises-2b-across-three-funds/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:39:51+00:00",
    "summary": "The new funding brings Index's total available investing capital to $3.5 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/vc-backed-startups-commit-more-fraud-and-researchers-think-they-know-why/",
    "domain": "大厂 AI 动态",
    "title": "VC-backed startups commit more fraud, and researchers think they know why",
    "url": "https://techcrunch.com/2026/07/31/vc-backed-startups-commit-more-fraud-and-researchers-think-they-know-why/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:00:00+00:00",
    "summary": "New research from the U.K.’s Imperial College and France’s Emlyon Business School mapped out how Silicon Valley founders commit fraud — and the role investors play."
  },
  {
    "id": "rss:https://techcrunch.com/video/sam-altman-isnt-the-only-one-who-wants-to-pump-the-brakes-on-ai/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman isn’t the only one who wants to pump the brakes on AI",
    "url": "https://techcrunch.com/video/sam-altman-isnt-the-only-one-who-wants-to-pump-the-brakes-on-ai/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T17:26:32+00:00",
    "summary": "After years of pushing full speed ahead on AI,&#160;OpenAI CEO&#160;Sam Altman says&#160;maybe it’s&#160;time for the AI industry to “pace” itself. The comments came&#160;just days after one of OpenAI"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/snapchat-no-longer-rewards-fully-ai-generated-spotlight-content/",
    "domain": "大厂 AI 动态",
    "title": "Snapchat no longer rewards fully AI-generated Spotlight content",
    "url": "https://techcrunch.com/2026/07/31/snapchat-no-longer-rewards-fully-ai-generated-spotlight-content/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T16:49:08+00:00",
    "summary": "Snapchat has adjusted its recommendation systems to ensure that only videos created by real people are eligible for Spotlight recommendations, taking a stance against AI slop."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/siri-ai-could-come-with-a-paywall-for-power-users/",
    "domain": "大厂 AI 动态",
    "title": "Siri AI could come with a paywall for power users",
    "url": "https://techcrunch.com/2026/07/31/siri-ai-could-come-with-a-paywall-for-power-users/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T16:08:18+00:00",
    "summary": "Apple CEO Tim Cook envisions users being able to buy more compute for Siri AI via Apple's existing iCloud+ subscriptions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/gm-and-ford-are-talking-less-and-less-about-evs/",
    "domain": "大厂 AI 动态",
    "title": "GM and Ford are talking less and less about EVs",
    "url": "https://techcrunch.com/2026/07/31/gm-and-ford-are-talking-less-and-less-about-evs/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:47:46+00:00",
    "summary": "The leading U.S. automakers are mentioning EVs on their investor calls at pre-pandemic rates, according to new data from TechCrunch and Hudson Labs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/samsung-expects-memory-shortage-to-worsen-through-2027-and-last-until-2028/",
    "domain": "大厂 AI 动态",
    "title": "Samsung expects memory shortage to worsen through 2027 and last until 2028",
    "url": "https://techcrunch.com/2026/07/31/samsung-expects-memory-shortage-to-worsen-through-2027-and-last-until-2028/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:37:58+00:00",
    "summary": "AI data center demand is fueling a multi-year chip shortage, pushing up component costs and retail device prices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/spacex-wont-remove-all-of-xais-unpermitted-turbines-for-another-year/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX won’t remove all of xAI’s unpermitted turbines for another year",
    "url": "https://techcrunch.com/2026/07/31/spacex-wont-remove-all-of-xais-unpermitted-turbines-for-another-year/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:16:17+00:00",
    "summary": "SpaceX is building a new power plant for xAI's Colossus data centers, but it won't remove existing, unpermitted turbines for many more months."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/reddit-is-testing-a-new-way-to-watch-and-listen-to-its-viral-posts/",
    "domain": "大厂 AI 动态",
    "title": "Reddit is testing a new way to watch — and listen to — its viral posts",
    "url": "https://techcrunch.com/2026/07/31/reddit-is-testing-a-new-way-to-watch-and-listen-to-its-viral-posts/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T14:49:21+00:00",
    "summary": "Reddit is developing a new video experience that lets users watch — or simply listen to — its most popular posts, taking inspiration from the viral TikTok videos that pair Reddit stories with gameplay"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/smallest-ai-raises-13m-to-build-ultra-fast-voice-ai-that-sounds-genuinely-human/",
    "domain": "大厂 AI 动态",
    "title": "Smallest.ai raises $13M to build ultra-fast voice AI that sounds genuinely human",
    "url": "https://techcrunch.com/2026/07/31/smallest-ai-raises-13m-to-build-ultra-fast-voice-ai-that-sounds-genuinely-human/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T14:47:11+00:00",
    "summary": "The startup is building voice models designed to make AI phone calls pass the Turing test."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/whatsapp-is-testing-a-new-folder-for-messages-from-large-businesses/",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp is testing a new folder for messages from large businesses",
    "url": "https://techcrunch.com/2026/07/31/whatsapp-is-testing-a-new-folder-for-messages-from-large-businesses/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T14:39:43+00:00",
    "summary": "WhatsApp will automatically move messages from large businesses to a new folder a few hours after you receive them."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/tesla-reportedly-might-sell-its-china-business-ahead-of-a-spacex-merger/",
    "domain": "大厂 AI 动态",
    "title": "Tesla reportedly might sell its China business ahead of a SpaceX merger",
    "url": "https://techcrunch.com/2026/07/31/tesla-reportedly-might-sell-its-china-business-ahead-of-a-spacex-merger/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T13:45:53+00:00",
    "summary": "Tesla had already reportedly prepped for the idea in the event that Beijing invades Taiwan."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/repeat-founder-ryan-williams-raises-10m-seed-for-an-ai-startup-for-private-credit-managers/",
    "domain": "大厂 AI 动态",
    "title": "Repeat founder Ryan Williams raises $10M seed for an AI startup for private credit managers",
    "url": "https://techcrunch.com/2026/07/31/repeat-founder-ryan-williams-raises-10m-seed-for-an-ai-startup-for-private-credit-managers/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:00:00+00:00",
    "summary": "Ellis AI announced Thursday its emergence from stealth with $10 million in seed funding."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says its own AI models breached three companies during security tests",
    "url": "https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T01:06:54+00:00",
    "summary": "After OpenAI's models broke into Hugging Face, Anthropic checked its own history and found three similar incidents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/apple-stockpiles-inventory-as-it-braces-for-significant-supply-constraints/",
    "domain": "大厂 AI 动态",
    "title": "Apple stockpiles inventory as it braces for ‘significant supply constraints’",
    "url": "https://techcrunch.com/2026/07/30/apple-stockpiles-inventory-as-it-braces-for-significant-supply-constraints/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T23:28:05+00:00",
    "summary": "Apple is worried enough about supply shortages that it reported about $11.1 billion in inventory, which is almost double the $5.7 billion it reported last September."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/not-just-neanderthals-ghost-lineage-in-africa-left-its-mark-on-our-dna/",
    "domain": "大厂 AI 动态",
    "title": "Not just Neanderthals: Ghost lineage in Africa left its mark on our DNA",
    "url": "https://arstechnica.com/science/2026/07/not-just-neanderthals-ghost-lineage-in-africa-left-its-mark-on-our-dna/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:17:05+00:00",
    "summary": "Some group with no modern descendants contributed a lot to our genomes."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/doctors-took-a-look-at-mans-painful-shoulder-they-found-the-joint-was-missing/",
    "domain": "大厂 AI 动态",
    "title": "Doctors took a look at man's painful shoulder—they found the joint was missing",
    "url": "https://arstechnica.com/health/2026/07/doctors-took-a-look-at-mans-painful-shoulder-they-found-the-joint-was-missing/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T21:51:52+00:00",
    "summary": "The term \"Milwaukee Shoulder Syndrome\" was coined in 1981, based on cases in four women."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/google-plans-to-exempt-sanctioned-nations-from-android-developer-verification/",
    "domain": "大厂 AI 动态",
    "title": "Google plans to exempt sanctioned nations from Android developer verification",
    "url": "https://arstechnica.com/gadgets/2026/07/google-plans-to-exempt-sanctioned-nations-from-android-developer-verification/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T21:35:56+00:00",
    "summary": "Someone in Cuba or Iran can keep installing APKs with no new restrictions, but devs will suffer."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/reddit-keeps-weird-dmca-lawsuit-against-web-scraper-alive-despite-googles-loss/",
    "domain": "大厂 AI 动态",
    "title": "Reddit keeps its strange DMCA fight over Google search results alive",
    "url": "https://arstechnica.com/tech-policy/2026/07/reddit-keeps-weird-dmca-lawsuit-against-web-scraper-alive-despite-googles-loss/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T21:19:39+00:00",
    "summary": "Reddit advances lawsuit accusing Perplexity AI of conspiring with web scraper."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/likely-illegally-claude-gained-access-to-3-networks-will-anthropic-be-held-to-account/",
    "domain": "大厂 AI 动态",
    "title": "Claude published malicious code to the Internet and attacked 3 real companies",
    "url": "https://arstechnica.com/security/2026/07/likely-illegally-claude-gained-access-to-3-networks-will-anthropic-be-held-to-account/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T20:39:14+00:00",
    "summary": "Had the hacks used conventional methods, someone would likely go to prison."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/google-earth-releases-swiftly-retracts-ai-feature-to-make-fake-satellite-images/",
    "domain": "大厂 AI 动态",
    "title": "Google Earth risked ruin with retracted AI tool for making fake satellite pics",
    "url": "https://arstechnica.com/ai/2026/07/google-earth-releases-swiftly-retracts-ai-feature-to-make-fake-satellite-images/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T20:21:05+00:00",
    "summary": "“What on earth is Google doing?” Misinformation fears spur walk-back of AI tool."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/ai-startup-admits-tattoo-for-interview-stunt-was-reckless/",
    "domain": "大厂 AI 动态",
    "title": "Would you get tattooed just to interview at a 7-days-a-week AI startup?",
    "url": "https://arstechnica.com/culture/2026/07/ai-startup-admits-tattoo-for-interview-stunt-was-reckless/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:04:56+00:00",
    "summary": "LemonLime’s CEO got “carried away” with tattoo gimmick."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/high-school-defends-staying-silent-while-boys-made-ai-nudes-of-59-classmates/",
    "domain": "大厂 AI 动态",
    "title": "High school defends staying silent while boys made AI nudes of 59 classmates",
    "url": "https://arstechnica.com/tech-policy/2026/07/high-school-defends-staying-silent-while-boys-made-ai-nudes-of-59-classmates/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T18:11:55+00:00",
    "summary": "Gaps in laws may help Pennsylvania high school escape AI nudes scandal."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/see-the-heat-an-infrared-imaging-system-that-outputs-in-color/",
    "domain": "大厂 AI 动态",
    "title": "Researchers devise a full-color night vision goggle",
    "url": "https://arstechnica.com/science/2026/07/see-the-heat-an-infrared-imaging-system-that-outputs-in-color/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T17:58:38+00:00",
    "summary": "Wavelength and intensity in the infrared are translated into colors in the visible."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/china-could-supply-ev-manufacturing-boom-with-recycled-evs/",
    "domain": "大厂 AI 动态",
    "title": "China could supply EV manufacturing boom with recycled EVs",
    "url": "https://arstechnica.com/science/2026/07/china-could-supply-ev-manufacturing-boom-with-recycled-evs/",
    "source": "Scott K. Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T17:29:21+00:00",
    "summary": "Look at chemistry of batteries and motors shows big opportunity for recycling."
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 342,
    "published_at": "2026-07-26T12:43:21+00:00",
    "summary": ""
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
    "points": 144,
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
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-07-30T16:00:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49092549",
    "domain": "股票",
    "title": "Chip stocks slide in US and Asia as AI jitters rattle investors",
    "url": "https://www.bbc.com/news/articles/cly8zng43npo",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-29T01:56:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49115139",
    "domain": "股票",
    "title": "Microsoft's $450B Jump Is Biggest in Stock Market History",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/microsoft-eyes-history-with-490-billion-pop-in-market-value",
    "source": "signatoremo",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-30T20:12:40+00:00",
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
    "id": "hn:49087537",
    "domain": "股票",
    "title": "Chip stocks tumble as AI sell-off deepens",
    "url": "https://www.ft.com/content/f8c03b5b-e194-4236-82c3-389b6f5dd7ae",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-28T17:54:01+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3778488",
    "domain": "股票",
    "title": "“债券抛售敲响警钟”！圣路易斯联储主席呼吁“尽早加息”",
    "url": "https://wallstreetcn.com/articles/3778488",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T05:29:22+00:00",
    "summary": "Musalem警示美联储需以加息行动捍卫抗通胀公信力。受30年期美债收益率创07年新高及油价、关税等多重通胀压力推升影响，多位鹰派官员力主尽早加息25基点，并驳斥政策决策“外包”给市场的质疑。"
  },
  {
    "id": "wscn:3778489",
    "domain": "股票",
    "title": "首个单月超10万的新势力出现了",
    "url": "https://wallstreetcn.com/articles/3778489",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T04:58:27+00:00",
    "summary": "利润是下一关。"
  },
  {
    "id": "wscn:3778487",
    "domain": "股票",
    "title": "韩国7月出口增速放缓但强于预期，芯片出口破400亿美元支撑贸易顺差",
    "url": "https://wallstreetcn.com/articles/3778487",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T04:55:04+00:00",
    "summary": "韩国7月出口同比大增62.8%至989亿美元，创历史单月第二高。芯片出口激增178.8%至410亿美元，AI数据中心需求旺盛致存储芯片供不应求。强劲的出口与经济基本面为韩国央行继续收紧货币政策提供支撑，市场预计央行或于8月或10月再度加息，并大幅上调全年经济增长预期。"
  },
  {
    "id": "wscn:3778486",
    "domain": "股票",
    "title": "铠侠拉开“巨额回购”大幕，存储巨头“回购牛市”即将到来？",
    "url": "https://wallstreetcn.com/articles/3778486",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T04:07:29+00:00",
    "summary": "日本NAND巨头铠侠一季度营业利润同比暴增28倍，并宣布最高8000亿日元回购及50%总回报目标，创下行业首例。受AI需求支撑，铠侠盈利大爆发；同时，野村预计韩股巨头也将迎来历史上最大规模回购潮，存储板块正开启以“企业回购”驱动的跨市场估值重塑牛市。"
  },
  {
    "id": "wscn:3778485",
    "domain": "股票",
    "title": "二季度利润率跌至近五年低点，宝马官宣启动人员精简",
    "url": "https://wallstreetcn.com/articles/3778485",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T03:32:26+00:00",
    "summary": "上半年在华交付缩水两成。"
  },
  {
    "id": "wscn:3778484",
    "domain": "股票",
    "title": "Stellantis二季度扭亏为盈，北美市场拉动业绩回暖",
    "url": "https://wallstreetcn.com/articles/3778484",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T03:30:35+00:00",
    "summary": "中国市场仍在调整期。"
  },
  {
    "id": "wscn:3778482",
    "domain": "股票",
    "title": "500亿美元投资都完成，亚马逊持股OpenAI 5%，此前已投Anthropic",
    "url": "https://wallstreetcn.com/articles/3778482",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T03:29:28+00:00",
    "summary": "亚马逊已完成对OpenAI共500亿美元的全额投资，持股约5%。此外，亚马逊还向Anthropic承诺最高330亿美元投资，旨在推动自研Trainium芯片渗透并巩固AWS市场地位。"
  },
  {
    "id": "wscn:3778483",
    "domain": "股票",
    "title": "雷诺上半年营收增9.5%，全球“量减收增”",
    "url": "https://wallstreetcn.com/articles/3778483",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T03:29:10+00:00",
    "summary": "中国角色彻底转向。"
  },
  {
    "id": "wscn:3778478",
    "domain": "股票",
    "title": "美股这个财报季盈利增长“超预期”，科技巨头“资本开支与AI回报”双涨",
    "url": "https://wallstreetcn.com/articles/3778478",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T02:42:44+00:00",
    "summary": "高盛表示，美股二季度财报表现强劲，标普500剔除一次性项目后EPS同比大增26%，AI基础设施贡献约三分之一盈利增长。云巨头云业务增速飙至48%，2027年资本开支预计突破1万亿美元，强劲基本面正为AI行情提供支撑。"
  },
  {
    "id": "wscn:3778480",
    "domain": "股票",
    "title": "对话TCL华星赵军：印刷OLED落地主流消费市场开启规模化",
    "url": "https://wallstreetcn.com/articles/3778480",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T02:28:20+00:00",
    "summary": "印刷OLED正式进入规模商业化新阶段"
  },
  {
    "id": "wscn:3778477",
    "domain": "股票",
    "title": "长鑫LPDDR6迎来关键突破",
    "url": "https://wallstreetcn.com/articles/3778477",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T02:04:47+00:00",
    "summary": "长鑫科技LPDDR6研发验证据称接近尾声，距离量产更进一步。其首款产品设计速率12800 Mbps，颗粒容量16Gb，较前代性能大幅提升。按照时间推算，从LPDDR5发布到LPDDR6向核心客户送样，长鑫在DRAM两个代际的跨越上，只用了不到3年的时间。"
  },
  {
    "id": "wscn:3778474",
    "domain": "股票",
    "title": "“黑色7月”以“两连涨”收尾，“AI交易”见底了吗？",
    "url": "https://wallstreetcn.com/articles/3778474",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T01:57:47+00:00",
    "summary": "多数分析师认为经历动量股的大幅回调以及AI龙头估值有所修复后，轮动最剧烈轮动阶段已过。但同时强调并不意味着精确底部已经确认。摩根大通建议增配质量因子，高盛提示长端利率风险，建议维持高流动性、低复杂度持仓。"
  },
  {
    "id": "wscn:3778476",
    "domain": "股票",
    "title": "“AI股神”致信投资者：遭遇“银行挤兑”，再也不加杠杆了，今年仍涨80%，我们能东山再起",
    "url": "https://wallstreetcn.com/articles/3778476",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T01:33:28+00:00",
    "summary": "Leopold表示，为7月基金资产暴跌67%一事\"承担全部责任\"，并承诺将汲取\"代价惨重的教训\"。其基金将继续运营，不会退出公开股票市场，但今后不会再向银行借款以放大押注。\"我们能够承受损失，并有能力东山再起。\""
  },
  {
    "id": "wscn:3778475",
    "domain": "股票",
    "title": "拯救AI交易？Citadel接盘“AI股神”持仓，投行策略师“终于搞明白大跌原因，现在可以往前看了”",
    "url": "https://wallstreetcn.com/articles/3778475",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T00:45:59+00:00",
    "summary": "Citadel以逾10%折价接盘Situational基金160亿美元股票组合，清除了市场最大的“被迫卖家”，止住AI股连环踩踏并推动中美韩科技股大幅反弹。然而高杠杆与AI资本支出合理性的结构性隐忧依然存在。"
  },
  {
    "id": "wscn:3778473",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年8月1日",
    "url": "https://wallstreetcn.com/articles/3778473",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T23:19:30+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3778379",
    "domain": "股票",
    "title": "AI盈利兑现主导交易，亚马逊涨15%力撑纳指收涨，苹果重挫7%，30年美债收益率涨破5.27%",
    "url": "https://wallstreetcn.com/articles/3778379",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T23:13:04+00:00",
    "summary": "标普涨0.70%，纳指涨1%。中概股指收涨1.47%。亚马逊创2012年以来最大单日涨幅。苹果创2025年4月份以来最大单日跌幅。美光跌5.90%。10年期美债收益率升约6个基点至4.74%，月内飙升逾30个基点，创2005年以来最大七月涨幅。美元兑日元跌1%、跌破158关口。现货黄金跌1.27%。WTI原油涨近1.3%。"
  },
  {
    "id": "wscn:3778472",
    "domain": "股票",
    "title": "Hugging Face并非个案？OpenAI扩大调查、据称发现更多AI智能体“失控”迹象",
    "url": "https://wallstreetcn.com/articles/3778472",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T23:02:13+00:00",
    "summary": "据报道，除了已披露的智能体攻击Hugging Face事件，OpenAI目前还在调查其他的智能体脱离隔离环境案例，这些“失控”事件的影响有限，且没有任何智能体离开OpenAI的网络。OpenAI和Anthropic均传出智能体“失控”后，欧盟委员会称与两家公司展开沟通，认为有必要持续监测高风险AI系统。"
  },
  {
    "id": "wscn:3778471",
    "domain": "股票",
    "title": "新兴市场股市创2008年以来最大单日涨幅，韩股创纪录飙升",
    "url": "https://wallstreetcn.com/articles/3778471",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T23:02:01+00:00",
    "summary": "MSCI新兴市场指数周五上涨6.6%，创2008年以来最佳单日表现，7月跌幅收窄至3.3%；韩国KOSPI综指周五创纪录大涨18%。分析指出，周五反弹或是空头回补，杠杆尚未完全出清，波动可能持续。"
  },
  {
    "id": "wscn:3778470",
    "domain": "股票",
    "title": "报道：OpenAI向美国监管机构演示新一代\"Astra\"AI模型",
    "url": "https://wallstreetcn.com/articles/3778470",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:45:18+00:00",
    "summary": "据The Information报道，OpenAI首席执行官Sam Altman本周亲赴华盛顿，向监管机构预演了一款名为\"Astra\"的全新AI模型系列。模型系列的核心能力在于支持多个AI智能体协同工作，并能够在较长时间跨度内持续执行复杂任务。"
  },
  {
    "id": "wscn:3778469",
    "domain": "股票",
    "title": "AI安全警报！Anthropic、OpenAI接连“越狱”，专家警告国家安全风险",
    "url": "https://wallstreetcn.com/articles/3778469",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:27:03+00:00",
    "summary": "Anthropic旗下Claude模型因隔离失效，在逾14万次网络安全测试中意外接入互联网，真实窃取凭证、植入恶意软件；此前OpenAI的AI代理同样突破沙箱、渗透Hugging Face。多名前政府官员警告，随着自主AI系统攻击能力不断增强，相关威胁正逐步上升至国家安全层面。"
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
    "id": "hn:49081705",
    "domain": "股票",
    "title": "AI sell-off intensifies as investors ditch chip stocks",
    "url": "https://www.theguardian.com/business/2026/jul/28/ai-sell-off-chip-stocks-sk-hynix-samsung",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-28T10:08:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49091512",
    "domain": "股票",
    "title": "Apple becomes second $5T company as investors flee AI stocks",
    "url": "https://www.theguardian.com/technology/2026/jul/28/apple-second-ever-5tn-company-as-investors-flee-ai-stocks",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-28T23:41:59+00:00",
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
    "id": "hn:48974426",
    "domain": "股票",
    "title": "Big tech needs to justify AI spending as investors dump stocks",
    "url": "https://www.bloomberg.com/news/articles/2026-07-19/big-tech-needs-to-justify-ai-spending-as-investors-dump-stocks",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-07-20T04:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012630",
    "domain": "股票",
    "title": "Alphabet Announces Second Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-22T20:04:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49033778",
    "domain": "股票",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
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
    "id": "hn:49012394",
    "domain": "股票",
    "title": "We got California to intervene about OpenAI's corporate switch from nonprofit",
    "url": "https://fortune.com/2026/07/22/openai-foundation-class-n-stock-board-control-ipo/",
    "source": "SLHamlet",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-22T19:46:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48962049",
    "domain": "股票",
    "title": "Elon Musk Runs from Interview at Last Minute as SpaceX Stock Crashed [video]",
    "url": "https://www.youtube.com/shorts/TFpF7ZzHc3w",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-18T20:30:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48996223",
    "domain": "股票",
    "title": "The AI Bubble Is No Ordinary Bubble",
    "url": "https://www.theatlantic.com/ideas/2026/07/ai-economy-stock-market/688004/",
    "source": "gereshes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-21T18:31:36+00:00",
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
    "id": "hn:48787052",
    "domain": "股票",
    "title": "Elon Musk posted twice as often on UK race and immigration as about SpaceX IPO",
    "url": "https://www.theguardian.com/technology/2026/jul/04/elon-musk-uk-race-immigration-spacex-ipo",
    "source": "iamflimflam1",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-07-04T17:18:19+00:00",
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
    "id": "hn:48781228",
    "domain": "股票",
    "title": "After $18B IPO, Bending Spoons founder says success comes from minimizing luck",
    "url": "https://techcrunch.com/2026/07/01/after-18b-ipo-bending-spoons-founder-says-success-comes-from-minimizing-luck/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-03T23:31:08+00:00",
    "summary": ""
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
    "id": "hn:48759634",
    "domain": "金融",
    "title": "PeerTube is a free, decentralized and federated video platform",
    "url": "https://github.com/Chocobozzz/PeerTube",
    "source": "doener",
    "platform": "hackernews",
    "points": 680,
    "published_at": "2026-07-02T11:17:45+00:00",
    "summary": ""
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
    "points": 137,
    "published_at": "2026-07-31T03:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48878126",
    "domain": "金融",
    "title": "Under federal rule, colleges must leave grads better off or lose financial aid",
    "url": "https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans",
    "source": "nradov",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-07-12T04:00:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-25T11:04:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48777266",
    "domain": "金融",
    "title": "International chess federation sanctions Kramnik",
    "url": "https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/",
    "source": "DarkContinent",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-07-03T17:04:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48826703",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://www.economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "nreece",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-08T02:17:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 51,
    "published_at": "2026-07-29T14:13:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-07-28T12:19:54+00:00",
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
    "id": "hn:48783175",
    "domain": "金融",
    "title": "The LLVM Compiler Infrastructure",
    "url": "https://cacm.acm.org/federal-funding-of-academic-research/the-llvm-compiler-infrastructure/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-07-04T06:43:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48884775",
    "domain": "金融",
    "title": "Storm clouds gather over America's financial supremacy",
    "url": "https://www.economist.com/finance-and-economics/2026/07/12/storm-clouds-gather-over-americas-financial-supremacy",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-12T21:04:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48785077",
    "domain": "金融",
    "title": "The Fediverse Is Not the Way Forward",
    "url": "https://trialandfailure.net/the-fediverse-is-not-the-way-forward/",
    "source": "ExMachina73",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-04T12:53:12+00:00",
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
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-07-05T06:40:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49047488",
    "domain": "金融",
    "title": "Stripe in talks to acquire OpenRouter in potential $10B deal, WSJ reports",
    "url": "https://finance.yahoo.com/technology/ai/articles/stripe-talks-acquire-openrouter-potential-215104525.html",
    "source": "nlpnerd",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-25T13:38:45+00:00",
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
    "id": "hn:48880233",
    "domain": "金融",
    "title": "IT administrators are \"fed up\" with Microsoft's \"useless\" apps and Windows 11",
    "url": "https://www.neowin.net/news/it-admins-feel-overwhelmingly-sick-of-microsoft-and-windows-11-garbage-apps-products/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-12T11:22:42+00:00",
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
    "id": "hn:49001708",
    "domain": "金融",
    "title": "Tesla Balance Bike",
    "url": "https://shop.tesla.com/product/balance-bike-for-kids",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-22T04:00:11+00:00",
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
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-07T22:04:18+00:00",
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
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48780128",
    "domain": "金融",
    "title": "AI First: How the Federal Government Is Prioritizing AI over People and Planet",
    "url": "https://stopgreedbuildgreen.climateandcommunity.org/posts/ai-first",
    "source": "eatox",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-03T21:21:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48796110",
    "domain": "金融",
    "title": "Moving back home used to be a sign of failure. Now it shows financial savvy",
    "url": "https://www.wsj.com/lifestyle/relationships/living-with-parents-finances-0c35530c",
    "source": "apparent",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-07-05T17:34:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-09T17:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48824532",
    "domain": "金融",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48852473",
    "domain": "金融",
    "title": "Meta is staring down $1.4T in lawsuit over teen mental health",
    "url": "https://finance.yahoo.com/technology/articles/meta-staring-down-1-4t-173432639.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-09T21:15:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48767569",
    "domain": "金融",
    "title": "Trump Made $1B on Crypto Deals While His Fans Lost a Fortune",
    "url": "https://www.wsj.com/finance/currencies/trump-made-1-billion-on-crypto-deals-while-his-fans-lost-a-fortune-408754c9",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-07-02T21:25:54+00:00",
    "summary": ""
  }
]
```
