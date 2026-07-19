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

- 今日日期：`2026-07-19`
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
  "date": "2026-07-19",
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
    "points": 1545284,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV12omoB4ExF",
    "domain": "AI",
    "title": "黑马程序员全网最全Coze智能体入门到项目实战全套教程，从AI Agent开发入门到6大AI智能体实战项目，涵盖提示词Prompt、RAG、Bot发布微信公众号",
    "url": "http://www.bilibili.com/video/av115713129843205",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 975869,
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
    "points": 911967,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 898101,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 540967,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 489361,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 408024,
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
    "points": 385141,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 291650,
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
    "points": 248966,
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
    "points": 192689,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV17Ejt6QE9Y",
    "domain": "AI",
    "title": "一旦被Claude判定&quot;危险&quot;，你之后说的每句话都会被动手脚——实测曝光",
    "url": "http://www.bilibili.com/video/av116787609863495",
    "source": "YJFGL",
    "platform": "bilibili",
    "points": 178378,
    "published_at": "2026-06-21T10:26:28+00:00",
    "summary": "续上一条视频。这次我测出了更具体的触发机制：\n当对话中**某一条消息被系统分类器判定为&quot;潜在存在危害&quot;**之后，从那条消息开始，之后所有的 user 消息后面都会被持续注入一段隐藏文本。\n也就是说，这不是无差别的全程注入，而是一旦被系统标记，就会进入一种&quot;持续追加提醒&quot;的状态，并且这个状态会一直保持到对话结束，用户完全不知情、也无法解除。\n这意味着：\n你某一"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 177392,
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
    "points": 161951,
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
    "points": 159946,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 140982,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 130868,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV1JbfLBREQH",
    "domain": "AI",
    "title": "震撼首发！我用AI做了一集瑞克和莫蒂！！",
    "url": "http://www.bilibili.com/video/av116104827506918",
    "source": "路边的小石zi",
    "platform": "bilibili",
    "points": 103029,
    "published_at": "2026-02-20T20:32:46+00:00",
    "summary": "震撼首发！我用AI做了一集瑞克和莫蒂！！用时5个小时，知道啥是更震撼的么，这集的剧本，台词，场景，分镜也是AI设计的，而且SD2.0做这种风格几乎完全没有违和感"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 95325,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 92830,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92604,
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
    "points": 73784,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 54107,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53151,
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
    "points": 47414,
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
    "points": 43251,
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
    "points": 38553,
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
    "points": 34964,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 28203,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27947,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV11DjT6uEhc",
    "domain": "AI",
    "title": "【端侧AI】嵌入式AI教程（基于RK3588）",
    "url": "http://www.bilibili.com/video/av116757511542670",
    "source": "Coder-Dawn",
    "platform": "bilibili",
    "points": 27870,
    "published_at": "2026-06-16T02:57:32+00:00",
    "summary": "从零到一入门级嵌入式AI课程！\n从环境搭建---&gt;模型训练---&gt;模型转换---&gt;模型部署全流程!\n\n视频全部公开免费，资料加入知识库获得(资料费9.9，需要的可滴滴)！"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 27352,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25397,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1mhKv68EPQ",
    "domain": "AI",
    "title": "豆包真能干活了！【豆包Agent入门教程】",
    "url": "http://www.bilibili.com/video/av116944258728161",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 24799,
    "published_at": "2026-07-19T03:00:00+00:00",
    "summary": "这个视频让你的豆包技能噌噌上涨，还有“秋芝AI科普skill”帮你答疑～\n感谢朋友们的三连+关注~"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22633,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1pkK56aEVG",
    "domain": "AI",
    "title": "GPT-5.6在Claude Code中表现远超Codex | Theo - t3․gg",
    "url": "http://www.bilibili.com/video/av116929612221157",
    "source": "浮生千山路w",
    "platform": "bilibili",
    "points": 18648,
    "published_at": "2026-07-16T12:29:37+00:00",
    "summary": "来源：https://www.youtube.com/watch?v=Noo0NWD0gHU\n原标题：gpt 5.6 is way better in Claude Code\n频道：Theo - t3․gg\n发布时间：2026-07-16\n\n内容简介：\n作者使用GPT-5.6 Sol版本在Claude Code中进行编程，发现其表现相较于Codex有显著提升，体验令人震惊。视频由Coderabbi"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 18632,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15353,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 15324,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 15042,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 14711,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV1toLuzFEwN",
    "domain": "AI",
    "title": "Udemy高分付费Cursor 课程：使用 Cursor Vibe Coding 进行全栈开发 | 中英字幕 | 口袋资源网",
    "url": "http://www.bilibili.com/video/av114374358343630",
    "source": "疯狂滴小黑",
    "platform": "bilibili",
    "points": 11185,
    "published_at": "2025-04-21T05:50:41+00:00",
    "summary": "🎨 课程名称：Cursor Course: FullStack development with Cursor Vibe Coding\n👨‍🎓 讲师：Eden Marco\n✨ 持续更新课程连接：https://www.koudaizy.com/tutorials/cursor-ai-ide/\n------------------\n\n描述\n免责声明：这不是初学者课程，需要软件工程经验！\n\n***英语"
  },
  {
    "id": "bvid:BV1w9Nc69EXP",
    "domain": "AI",
    "title": "[电赛AIskill]写0行代码/纯agent速通2024年电赛H题——思路&amp;代码分享",
    "url": "http://www.bilibili.com/video/av116900721922369",
    "source": "3545D",
    "platform": "bilibili",
    "points": 10229,
    "published_at": "2026-07-11T09:56:10+00:00",
    "summary": "使用mspm0-skill速通2024年电赛h题教程/思路，视频内使用的是codex桌面端（现在叫ChatGPT桌面端），天猛星开发板+ccs环境编译+OpenOCD/DAPLink烧录，视频内skill支持各种开发板/工具链/Agent/烧录器/IDE等，详见https://github.com/mc3545dada/mspm0-skill，感兴趣的欢迎交流/Issue/PR/star等，谢谢a"
  },
  {
    "id": "bvid:BV1e1Ne6ME9D",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116922700074278",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 8663,
    "published_at": "2026-07-15T07:04:07+00:00",
    "summary": "我重新上传了，希望没有耽误大家学习！\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1ymNv6REs2",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent智能体零基础全套教程，2026最新版，从入门到实战！包含所有干货！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116922347686666",
    "source": "Agent智能体搭建-",
    "platform": "bilibili",
    "points": 8411,
    "published_at": "2026-07-15T05:35:41+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 7906,
    "published_at": "2026-07-10T09:04:48+00:00",
    "summary": "【代码已整理】\n无论你是从零开始开发项目，还是对现有代码进行现代化改造，本课程都能为你提供一套严谨的工作流程，让你按自己的方式构建软件。"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 7761,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1CRKn6mECd",
    "domain": "AI",
    "title": "2026吃透B站最全最细Vibe Coding零基础教程，手把手带你vibecoding实战，Codex+Claude Code+Hermes Agent",
    "url": "http://www.bilibili.com/video/av116934125360761",
    "source": "老溤识途_",
    "platform": "bilibili",
    "points": 7137,
    "published_at": "2026-07-17T07:35:01+00:00",
    "summary": "从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7001,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1aA6uBCEcv",
    "domain": "AI",
    "title": "快速上手｜在OpenCode中接入MCP",
    "url": "http://www.bilibili.com/video/av115965627013763",
    "source": "MiniMax_稀宇极智",
    "platform": "bilibili",
    "points": 6958,
    "published_at": "2026-01-27T06:27:45+00:00",
    "summary": "本视频中，我们将演示如何在OpenCode接入MCP，使MiniMax模型具备网络检索和图片理解的能力。帮助开发者在编码过程中快速获取信息和理解图片内容。\n\n解锁 MiniMax 专属福利，Coding Plan 立享 88 折！\nhttps://platform.minimaxi.com/subscribe/coding-plan?code=1c8FaUGpJ8&amp;source=link"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 370,
    "published_at": "2026-07-11T17:21:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48903715",
    "domain": "AI 算力 / 半导体",
    "title": "Alternative(s) to run CUDA on non-Nvidia hardware",
    "url": "https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/",
    "source": "alok-g",
    "platform": "hackernews",
    "points": 142,
    "published_at": "2026-07-14T08:24:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48597201",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung demonstrates 3D stacked FETs with triple nanosheet channels at 42nm",
    "url": "https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/",
    "source": "its_ajseven",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-06-19T11:03:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/",
    "domain": "AI 算力 / 半导体",
    "title": "New Material Beats Copper’s Thermal Conductivity",
    "url": "https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:00:00+00:00",
    "summary": "Meet θ-TaN, a metal that moves heat nearly 3× better than copper—and could upend chip cooling layers. The post New Material Beats Copper’s Thermal Conductivity appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/asml-raises-outlook-plans-more-euv-capacity/",
    "domain": "AI 算力 / 半导体",
    "title": "ASML Raises Outlook, Plans More EUV Capacity",
    "url": "https://www.eetimes.com/asml-raises-outlook-plans-more-euv-capacity/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:00:00+00:00",
    "summary": "ASML raised its full-year outlook as AI demand prompted plans to expand lithography capacity through at least 2028. The post ASML Raises Outlook, Plans More EUV Capacity appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/gta-3-and-vice-city-are-now-playable-inside-san-andreas-a-mod-lets-you-revisit-liberty-city-and-vice-city-without-leaving-san-andreas",
    "domain": "AI 算力 / 半导体",
    "title": "GTA 3 and Vice City are now playable inside San Andreas — a mod lets you revisit Liberty City and Vice City without leaving San Andreas",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/gta-3-and-vice-city-are-now-playable-inside-san-andreas-a-mod-lets-you-revisit-liberty-city-and-vice-city-without-leaving-san-andreas",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:48:22+00:00",
    "summary": "A GTA modder has embedded GTA 3 and Vice City within San Andreas, even nesting Vice City within GTA 3, with all three games continuing to run simultaneously."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-new-ryzen-7-7700x3d-plummets-to-usd279-days-after-launch-the-x3d-chip-rules-the-mid-range-at-its-discounted-price",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s new Ryzen 7 7700X3D plummets to $279 days after launch — the X3D chip rules the mid-range at its discounted price",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-new-ryzen-7-7700x3d-plummets-to-usd279-days-after-launch-the-x3d-chip-rules-the-mid-range-at-its-discounted-price",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:40:13+00:00",
    "summary": "The Ryzen 7 7700X3D has suddenly become a solid value thanks to a $50 promo code, knocking its price down from $329 to just $279 on Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/strapping-11-fans-and-a-360mm-aio-to-an-rtx-3080-sounds-crazy-until-you-see-the-30-c-temp-drop-modded-gpu-delivered-less-than-5-fps-uplift",
    "domain": "AI 算力 / 半导体",
    "title": "Strapping 11 fans and a 360mm AIO to an RTX 3080 sounds crazy until you see the 30°C temp drop — modded GPU delivered less than 5 FPS uplift at turbojet noise levels",
    "url": "https://www.tomshardware.com/pc-components/cooling/strapping-11-fans-and-a-360mm-aio-to-an-rtx-3080-sounds-crazy-until-you-see-the-30-c-temp-drop-modded-gpu-delivered-less-than-5-fps-uplift",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:22:49+00:00",
    "summary": "TrashBench recently decided to test whether adding more and more fans to a powerful GPU would improve its performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/jurassic-park-packed-usd4-million-of-legit-1993-computer-hardware-a-software-engineer-detailed-every-single-piece-of-hardware-in-the-film",
    "domain": "AI 算力 / 半导体",
    "title": "Jurassic Park packed $4 million of legit 1993 computer hardware — a software engineer detailed every single piece of hardware in the film",
    "url": "https://www.tomshardware.com/desktops/jurassic-park-packed-usd4-million-of-legit-1993-computer-hardware-a-software-engineer-detailed-every-single-piece-of-hardware-in-the-film",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:12:53+00:00",
    "summary": "Google software engineer Fabien Sanglard meticulously listed the computer hardware and software used in the first Jurassic Park film. He even added details for each device, turning the film into somet"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/grab-amds-ryzen-7-5800x3d-10th-anniversary-cpu-with-motherboard-and-16gb-ram-for-just-usd529-save-over-usd100-on-this-epic-amd-gaming-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Grab AMD’s Ryzen 7 5800X3D 10th Anniversary CPU with motherboard and 16GB RAM for just $529 — save over $100 on this epic AMD gaming bundle",
    "url": "https://www.tomshardware.com/pc-components/cpus/grab-amds-ryzen-7-5800x3d-10th-anniversary-cpu-with-motherboard-and-16gb-ram-for-just-usd529-save-over-usd100-on-this-epic-amd-gaming-bundle",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T15:19:27+00:00",
    "summary": "Newegg has a great combo bundle on sale with over $100 in savings for the fastest DDR4 gaming system you can build today. It pairs a Ryzen 7 5800X3D with 16GB of CL16 DDR4-3200 RAM and an Asus TUF Gam"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-50-super-gpus-are-reportedly-ready-but-stuck-in-limbo-due-to-excessive-gddr7-pricing-3gb-gddr7-module-costs-triple-the-price-of-2gb",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 50 Super GPUs are reportedly ready, but stuck in limbo due to excessive GDDR7 pricing — 3GB GDDR7 module costs triple the price of 2GB",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-50-super-gpus-are-reportedly-ready-but-stuck-in-limbo-due-to-excessive-gddr7-pricing-3gb-gddr7-module-costs-triple-the-price-of-2gb",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T13:45:42+00:00",
    "summary": "The 3GB GDDR7 chips that the RTX 50 Super GPUs will use reportedly cost twice to thrice as much as the 2GB chips found on vanilla RTX 50-series graphics cards. This would likely push the retail price "
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/nvidia-ceo-jensen-huangs-trademark-leather-jacket-raises-nearly-usd1-million-at-charity-auction-bidding-makes-usd60-000-valuation-look-like-pocket-change",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang’s trademark leather jacket raises nearly $1 Million at charity auction — bidding makes $60,000 valuation look like pocket change",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/nvidia-ceo-jensen-huangs-trademark-leather-jacket-raises-nearly-usd1-million-at-charity-auction-bidding-makes-usd60-000-valuation-look-like-pocket-change",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T13:22:12+00:00",
    "summary": "‘The Jensen Jacket’ achieved a hammer price of $960,000 this weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/security-engineer-ports-password-cracker-hashcat-to-gameboy-advance-16-8-mhz-chip-can-perform-a-meager-727-hashes-a-second-30-million-times-slower-than-a-modern-rig",
    "domain": "AI 算力 / 半导体",
    "title": "Security engineer ports password cracker hashcat to Gameboy Advance — 16.8 MHz chip can perform a meager 727 hashes a second, 30 million times slower than a modern rig",
    "url": "https://www.tomshardware.com/video-games/nintendo/security-engineer-ports-password-cracker-hashcat-to-gameboy-advance-16-8-mhz-chip-can-perform-a-meager-727-hashes-a-second-30-million-times-slower-than-a-modern-rig",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:30:00+00:00",
    "summary": "Gameboy Advance port of hashcat allows for advanced password cracking in meager hardware — so long as you're willing to wait"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/agi-ai828-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "AGI AI828 SSD Review: A near-last resort for those on a budget",
    "url": "https://www.tomshardware.com/pc-components/ssds/agi-ai828-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:10:00+00:00",
    "summary": "The AGI AI828 is a budget drive with subpar performance and power efficiency. This makes it a last resort, although in the current market, it might be good enough for some."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/korean-outfit-hosting-1-44mb-game-development-contest-to-honor-the-floppy-disk-entrants-must-confine-entire-fileset-including-resources-engine-and-library-to-miniscule-storage-format",
    "domain": "AI 算力 / 半导体",
    "title": "Korean outfit hosting 1.44MB game development contest to honor the floppy disk — entrants must confine entire fileset, including resources, engine, and library, to miniscule storage format",
    "url": "https://www.tomshardware.com/software/korean-outfit-hosting-1-44mb-game-development-contest-to-honor-the-floppy-disk-entrants-must-confine-entire-fileset-including-resources-engine-and-library-to-miniscule-storage-format",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:00:00+00:00",
    "summary": "There’s a new 'open to everyone' floppy disk-size game development competition with cash prizes for the best three submissions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/autonomous-micro-drone-achieves-first-air-to-air-insect-kill-on-the-way-towards-completely-eradicating-mosquitoes-40-gram-unit-uses-car-parking-sensors-can-eliminate-insects-at-up-to-26-feet",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous micro-drone achieves first air-to-air insect kill on the way 'towards completely eradicating mosquitoes' — 40-gram unit uses car parking sensors, can eliminate insects at up to 26 feet",
    "url": "https://www.tomshardware.com/tech-industry/drones/autonomous-micro-drone-achieves-first-air-to-air-insect-kill-on-the-way-towards-completely-eradicating-mosquitoes-40-gram-unit-uses-car-parking-sensors-can-eliminate-insects-at-up-to-26-feet",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T09:00:00+00:00",
    "summary": "A micro-drone designed to locate and eradicate mosquitoes has passed an important milestone with its first recorded air-to-air kill."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asmls-planned-low-na-euv-machine-price-hikes-reportedly-frustrate-tsmc-lithography-machine-maker-comes-knocking-to-make-bank-on-tsmcs-profitable-fabs-potentially-costing-the-taiwanese-chipmaker-billions",
    "domain": "AI 算力 / 半导体",
    "title": "ASML's planned Low-NA EUV machine price hikes reportedly frustrate TSMC — lithography machine maker comes knocking to make bank on TSMC's profitable fabs, potentially costing the Taiwanese chipmaker b",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asmls-planned-low-na-euv-machine-price-hikes-reportedly-frustrate-tsmc-lithography-machine-maker-comes-knocking-to-make-bank-on-tsmcs-profitable-fabs-potentially-costing-the-taiwanese-chipmaker-billions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:57:16+00:00",
    "summary": "ASML says that the increased productivity of its Low-NA EUV tools gives it an option to increase the prices of these scanners in the future. The move may have a drastic effect on TSMC's future expansi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC confirms significant yield and performance improvements in A14 update — strong interest from AI/HPC and smartphone customers",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:30:26+00:00",
    "summary": "TSMC's A14 process technology progresses faster than N2 at this stage of development as developers of both client and AI/HPC plan to use it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fbi-arrests-florida-man-in-steam-malware-investigaton-after-tracing-stolen-bitcoin-to-uber-eats-gift-cards",
    "domain": "AI 算力 / 半导体",
    "title": "Florida man arrested after allegedly stealing $220,000 in crypto using malware hidden in Steam Games — 8,000 devices infected",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fbi-arrests-florida-man-in-steam-malware-investigaton-after-tracing-stolen-bitcoin-to-uber-eats-gift-cards",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:43:21+00:00",
    "summary": "Federal agents arrested 21-year-old Zyaire Dontaevious Zamarion Wilkins of North Lauderdale, Florida, on Tuesday."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/best-back-to-school-tech-deals-on-laptops-and-essential-tech-save-on-new-semester-essentials-now",
    "domain": "AI 算力 / 半导体",
    "title": "Best Back to School tech deals on laptops and essential tech — save on new semester essentials now",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/best-back-to-school-tech-deals-on-laptops-and-essential-tech-save-on-new-semester-essentials-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:29:45+00:00",
    "summary": "Grab savings on the best back-to-school tech deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/gamestop-ceo-says-sonys-decision-to-go-disc-less-is-totally-irrelevant-claims-software-including-physical-discs-accounts-for-only-12-percent-of-the-companys-business",
    "domain": "AI 算力 / 半导体",
    "title": "GameStop CEO says Sony's decision to go disc-less is 'totally irrelevant' — claims software, including physical discs, accounts for only 12% of the company's business",
    "url": "https://www.tomshardware.com/video-games/console-gaming/gamestop-ceo-says-sonys-decision-to-go-disc-less-is-totally-irrelevant-claims-software-including-physical-discs-accounts-for-only-12-percent-of-the-companys-business",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T13:51:39+00:00",
    "summary": "GameStop CEO Ryan Cohen says Sony’s physical game exit is irrelevant to the company's business, amid a $56 billion eBay takeover, as collectibles now drive growth."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security",
    "domain": "AI 算力 / 半导体",
    "title": "Lawmakers want US government to ban memory chips from China, even in allied supply chains — citing 'unacceptable risk' to national, economic, and supply chain security",
    "url": "https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T13:05:44+00:00",
    "summary": "U.S. lawmakers demand Commerce Secretary Howard Lutnick to ban imports of memory chips from China to the U.S., ask allies to do the same."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/ai-data-centers-must-produce-as-much-power-as-they-use-australia-pm-says-new-national-ai-framework-will-also-ensure-water-efficiency-and-protect-intellectual-property-rights",
    "domain": "AI 算力 / 半导体",
    "title": "AI data centers must produce as much power as they use, Australia PM says — new national AI framework will also ensure water efficiency and protect intellectual property rights",
    "url": "https://www.tomshardware.com/tech-industry/policy/ai-data-centers-must-produce-as-much-power-as-they-use-australia-pm-says-new-national-ai-framework-will-also-ensure-water-efficiency-and-protect-intellectual-property-rights",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T12:16:03+00:00",
    "summary": "Australian Prime Minister Anthony Albanese announced the \"Australian Standards for A.I.,\" which will serve as a national framework for data center developments related to AI. The government plans to s"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-nova-lake-leak-points-to-core-ultra-series-400-branding-staggered-release-next-year-hotly-anticipated-flagship-52-core-desktop-cpu-might-not-arrive-until-late-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Nova Lake leak points to Core Ultra Series 400 branding, staggered release next year — hotly anticipated flagship 52-core desktop CPU might not arrive until late 2027",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-nova-lake-leak-points-to-core-ultra-series-400-branding-staggered-release-next-year-hotly-anticipated-flagship-52-core-desktop-cpu-might-not-arrive-until-late-2027",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T12:08:13+00:00",
    "summary": "Intel's upcoming Nova Lake desktop processors continue to gather momentum, with fresh reports hinting at Core Ultra Series 400 branding and a phased launch timeline."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3",
    "domain": "AI 算力 / 半导体",
    "title": "China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena benchmark— Moonshot AI delivers largest open-weight AI model ever, as China works around U.S. compute limits",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:32:01+00:00",
    "summary": "Beijing-based Moonshot AI has released Kimi K3, a 2.8 trillion parameter model that the company describes in its technical blog as the world's first open 3T-class system."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/score-usd1-100-off-this-oled-gaming-laptop-with-rtx-5070-ti-the-ultimate-back-to-school-powerhouse-also-features-a-24-core-ultra-9-290hx-32gb-of-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Score $1,100 off this OLED gaming laptop with RTX 5070 Ti, the ultimate Back to School powerhouse — also features a 24-core Ultra 9 290HX, 32GB of RAM, and a 1TB SSD",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/score-usd1-100-off-this-oled-gaming-laptop-with-rtx-5070-ti-the-ultimate-back-to-school-powerhouse-also-features-a-24-core-ultra-9-290hx-32gb-of-ram-and-a-1tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:24:25+00:00",
    "summary": "Get $1,100 off this HP Omen Max laptop with OLED display, Ultra 9 290HX, 32GB of RAM, and RTX 5070 Ti."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/get-amds-new-ryzen-7-7700x3d-with-16gb-of-ram-and-a-motherboard-for-just-usd450-save-31-percent-on-a-b650m-micro-atx-and-g-skill-ddr5-for-an-epic-small-build",
    "domain": "AI 算力 / 半导体",
    "title": "Get AMD’s new Ryzen 7 7700X3D with 16GB of RAM and a motherboard for just $450 — save 31% on a B650M Micro ATX and G.Skill DDR5 for an epic small build",
    "url": "https://www.tomshardware.com/laptops/get-amds-new-ryzen-7-7700x3d-with-16gb-of-ram-and-a-motherboard-for-just-usd450-save-31-percent-on-a-b650m-micro-atx-and-g-skill-ddr5-for-an-epic-small-build",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:22:31+00:00",
    "summary": "Save over 31% on the price of this Newegg 7700X3D bundle. CPU, motherboard, and RAM combo is just $450 after discounts."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/msi-mag-z890-tomahawk-wifi-ii-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "MSI MAG Z890 Tomahawk Wifi II motherboard review: Loses features from the original, but shaves a few dollars off the price",
    "url": "https://www.tomshardware.com/pc-components/motherboards/msi-mag-z890-tomahawk-wifi-ii-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:10:00+00:00",
    "summary": "SI’s Z890 Tomahawk Wifi II trims a couple of connectivity features, but at its sub-$200 price, it’s still a reasonably equipped budget Z890 board."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-looks-to-increase-prices-of-its-low-na-euv-tools-beyond-existing-productivity-based-model-company-wants-to-capture-the-value-of-all-the-advantages-its-tools-offer-not-just-wafer-throughput-improvements",
    "domain": "AI 算力 / 半导体",
    "title": "ASML looks to increase prices of its Low-NA EUV tools beyond existing productivity-based model — company wants to capture the value of all the advantages its tools offer, not just wafer throughput imp",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-looks-to-increase-prices-of-its-low-na-euv-tools-beyond-existing-productivity-based-model-company-wants-to-capture-the-value-of-all-the-advantages-its-tools-offer-not-just-wafer-throughput-improvements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T10:30:00+00:00",
    "summary": "ASML's comments point to intentions to increase prices, though the company is expected to maintain its value-based approach to price setting. Yet, TSMC is reportedly unhappy about the potential plan."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/mario-kart-wii-recompiled-for-pc-using-ai-with-4k-potential-and-uncapped-frame-rates-first-static-recompilation-of-a-wii-game-supports-over-200-tracks-thanks-to-retro-rewind-compatibility",
    "domain": "AI 算力 / 半导体",
    "title": "Mario Kart Wii recompiled for PC using AI, with 4K potential and uncapped frame rates — 'first static recompilation of a Wii game' supports over 200 tracks thanks to Retro Rewind compatibility",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/mario-kart-wii-recompiled-for-pc-using-ai-with-4k-potential-and-uncapped-frame-rates-first-static-recompilation-of-a-wii-game-supports-over-200-tracks-thanks-to-retro-rewind-compatibility",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T10:00:33+00:00",
    "summary": "Mario Kart Wiicompiled, a claimed 'first static recompilation of a Wii game,' is scheduled to be released in August."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/shark-robot-vacuum-flaw-lets-one-stolen-certificate-run-root-commands-on-others-in-the-same-aws-region",
    "domain": "AI 算力 / 半导体",
    "title": "Robot vacuum flaw lets one stolen certificate run root commands on other Shark robovacs in the same AWS region — unpatched flaw exposes live camera feeds, stored home maps, and Wi-Fi credentials",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/shark-robot-vacuum-flaw-lets-one-stolen-certificate-run-root-commands-on-others-in-the-same-aws-region",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T10:00:00+00:00",
    "summary": "The problem is an over-permissive AWS IoT policy."
  },
  {
    "id": "rss:https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Boosts 2026 Expansion Budget, Adds $100B to U.S. Investment",
    "url": "https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T05:55:59+00:00",
    "summary": "TSMC is raising its 2026 capital budget to $64 billion and adding $100 billion to its U.S. investment for AI. The post TSMC Boosts 2026 Expansion Budget, Adds $100B to U.S. Investment appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-data-centers-push-silicon-photonics-toward-300-mm-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Data Centers Push Silicon Photonics Toward 300-mm Scale",
    "url": "https://www.eetimes.com/ai-data-centers-push-silicon-photonics-toward-300-mm-scale/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T14:00:00+00:00",
    "summary": "AI data centers are torching copper’s reign as ST pushes 300-mm silicon photonics for faster, denser optical links. The post AI Data Centers Push Silicon Photonics Toward 300-mm Scale appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/india-adds-pieces-to-strengthen-its-electronics-supply-chain-puzzle/",
    "domain": "AI 算力 / 半导体",
    "title": "India Adds Pieces to Strengthen Its Electronics Supply Chain Puzzle",
    "url": "https://www.eetimes.com/india-adds-pieces-to-strengthen-its-electronics-supply-chain-puzzle/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T07:00:00+00:00",
    "summary": "India races to own more of its electronics value chain, from OSATs to PCBs, but imported materials still hold the leash. The post India Adds Pieces to Strengthen Its Electronics Supply Chain Puzzle ap"
  },
  {
    "id": "rss:https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/",
    "domain": "AI 算力 / 半导体",
    "title": "How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots",
    "url": "https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:06:44+00:00",
    "summary": "Nidec tackles the brutal gearbox tradeoffs behind humanoid robots, from zero backlash to lighter integrated actuators. The post How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots appea"
  },
  {
    "id": "rss:https://www.eetimes.com/tyl-semi-de-risks-chiplets-with-new-business-model/",
    "domain": "AI 算力 / 半导体",
    "title": "TYLsemi De-Risks Chiplets With New Business Model",
    "url": "https://www.eetimes.com/tyl-semi-de-risks-chiplets-with-new-business-model/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:00:00+00:00",
    "summary": "Startup TYLsemi wants to address the gap between ASIC houses and design services, taking on the risk of developing large chiplet-based chips for AI infrastructure customers. The post TYLsemi De-Risks "
  },
  {
    "id": "rss:https://www.eetimes.com/why-tl3228-is-the-go-to-standard-chip-powering-true-8k-wireless-gaming-peripherals/",
    "domain": "AI 算力 / 半导体",
    "title": "Why TL3228 Is the Go-To Standard Chip Powering True 8K Wireless Gaming Peripherals",
    "url": "https://www.eetimes.com/why-tl3228-is-the-go-to-standard-chip-powering-true-8k-wireless-gaming-peripherals/",
    "source": "Telink",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:00:00+00:00",
    "summary": "The TL3228 integrates a dual-core RISC-V processor consisting of a high-performance D25F core and an energy-efficient N22 core. The post Why TL3228 Is the Go-To Standard Chip Powering True 8K Wireless"
  },
  {
    "id": "rss:https://www.eetimes.com/massive-stock-full-chain-service-your-global-semiconductor-partner/",
    "domain": "AI 算力 / 半导体",
    "title": "Massive Stock, Full-Chain Service — Your Global Semiconductor Partner",
    "url": "https://www.eetimes.com/massive-stock-full-chain-service-your-global-semiconductor-partner/",
    "source": "NEW IDEAS INDUSTRIAL CO., LIMITED",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:00:00+00:00",
    "summary": "Discover how New Ideas Industrial can stabilize your semiconductor supply chain for AI, storage, and UAV applications. The post Massive Stock, Full-Chain Service — Your Global Semiconductor Partner ap"
  },
  {
    "id": "rss:https://www.eetimes.com/after-magdeburg-intel-builds-on-ireland-existing-strength/",
    "domain": "AI 算力 / 半导体",
    "title": "After Magdeburg, Intel Builds on Ireland’s Existing Strength",
    "url": "https://www.eetimes.com/after-magdeburg-intel-builds-on-ireland-existing-strength/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:24:18+00:00",
    "summary": "Leixlip cannot replace Magdeburg, but it shows the value of expanding where fabs, demand, and ecosystems already exist. The post After Magdeburg, Intel Builds on Ireland’s Existing Strength appeared f"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linus-torvalds-rebukes-anti-ai-stances-in-the-linux-kernel-code-review-process-says-linux-is-not-one-of-those-anti-ai-projects-creator-embraces-ai-as-just-a-tool-and-clearly-a-useful-one",
    "domain": "AI 算力 / 半导体",
    "title": "Linus Torvalds rebukes anti-AI stances in the Linux kernel code review process, says 'Linux is not one of those anti-AI projects' — creator embraces AI as just a tool and 'clearly a useful one'",
    "url": "https://www.tomshardware.com/software/linux/linus-torvalds-rebukes-anti-ai-stances-in-the-linux-kernel-code-review-process-says-linux-is-not-one-of-those-anti-ai-projects-creator-embraces-ai-as-just-a-tool-and-clearly-a-useful-one",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:59:13+00:00",
    "summary": "Linus Torvalds, Linux's creator and kernel manager, has seemingly taken an accepting stance of AI-assisted tooling."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/quantum-computing/neural-atom-quantum-computing-roadmap-how-laser-cooled-trapped-atoms-could-pave-the-path-beyond-physical-qubit-counts",
    "domain": "AI 算力 / 半导体",
    "title": "Neural atom quantum computing roadmap — how laser-cooled trapped atoms could pave the path beyond physical qubit counts",
    "url": "https://www.tomshardware.com/tech-industry/quantum-computing/neural-atom-quantum-computing-roadmap-how-laser-cooled-trapped-atoms-could-pave-the-path-beyond-physical-qubit-counts",
    "source": "Francisco Pires",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:52:54+00:00",
    "summary": "Neural Atom Quantum Computing is a rapidly accelerating part of the Quantum puzzle. Featuring software-defined configurable arrays, qubits can be physically moved mid-computation, and this roadmap hig"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-is-exclusive-to-newegg-in-north-america-usd329-cpu-wont-be-available-at-other-vendors-until-at-least-q4",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 7700X3D is exclusive to Newegg in North America — $329 CPU won't be available at other vendors until at least Q4",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-is-exclusive-to-newegg-in-north-america-usd329-cpu-wont-be-available-at-other-vendors-until-at-least-q4",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:47:21+00:00",
    "summary": "AMD's newest CPU, the Ryzen 7 7700X3D, costs $329 and is available exclusively at Newegg in Canada and the United States till the end of Q3 2026. It's a great gaming performer but there are better opt"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tower-semiconductor-revives-shuttered-panasonic-era-fab-in-3-billion-japan-photonics-expansion",
    "domain": "AI 算力 / 半导体",
    "title": "Tower Semiconductor revives shuttered Panasonic-era fab in $3 billion Japan photonics expansion — METI-backed plan targets $3.6 billion revenue by 2028",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tower-semiconductor-revives-shuttered-panasonic-era-fab-in-3-billion-japan-photonics-expansion",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:39:09+00:00",
    "summary": "Tower Semiconductor has announced a dual-track expansion of its 300mm silicon photonics, silicon germanium, and advanced packaging operations in Japan"
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
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-09T13:29:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48734960",
    "domain": "AI 算力 / 半导体",
    "title": "Etched has officially come out of stealth",
    "url": "https://www.bloomberg.com/news/articles/2026-06-30/ai-chip-startup-etched-says-jane-street-tsmc-linked-vc-invested",
    "source": "seventeen29",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-30T16:21:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48601996",
    "domain": "AI 算力 / 半导体",
    "title": "ASML denies US Government report that EUV chipmaking tool was shipped to China",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-denies-us-government-report-that-its-euv-chipmaking-tool-was-shipped-to-china-says-rumors-are-inaccurate-and-damaging-to-our-reputation",
    "source": "srameshc",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-19T19:03:30+00:00",
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
    "id": "rss:https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck",
    "url": "https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-08T09:54:57+00:00",
    "summary": "Compute is the lifeblood of AI. He who controls the spice controls the universe the compute will control the production of tokens and reap the benefits of AI. Without compute you do not have a seat at"
  },
  {
    "id": "hn:48936451",
    "domain": "大厂 AI 动态",
    "title": "NotebookLM is now Gemini Notebook",
    "url": "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 368,
    "published_at": "2026-07-16T16:08:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48735444",
    "domain": "大厂 AI 动态",
    "title": "Nano Banana 2 Lite",
    "url": "https://deepmind.google/models/gemini-image/flash-lite/",
    "source": "minimaxir",
    "platform": "hackernews",
    "points": 435,
    "published_at": "2026-06-30T16:48:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 364,
    "published_at": "2026-07-15T18:40:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756602",
    "domain": "大厂 AI 动态",
    "title": "Kimi K2.7 Code is generally available in GitHub Copilot",
    "url": "https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/",
    "source": "unliftedq",
    "platform": "hackernews",
    "points": 417,
    "published_at": "2026-07-02T04:32:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48662999",
    "domain": "大厂 AI 动态",
    "title": "Computer use in Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 242,
    "published_at": "2026-06-24T17:21:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48959297",
    "domain": "大厂 AI 动态",
    "title": "Our Approach to Bioresilience: Isomorphic Labs and Google DeepMind",
    "url": "https://deepmind.google/blog/our-approach-to-bioresilience/",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 77,
    "published_at": "2026-07-18T16:02:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48707103",
    "domain": "大厂 AI 动态",
    "title": "Google limits Meta's use of its Gemini AI models",
    "url": "https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-06-28T13:30:06+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/967630/dave-eggers-openai-chatgpt-silencing-an-entire-generation",
    "domain": "大厂 AI 动态",
    "title": "Dave Eggers told OpenAI staff that ChatGPT was ‘silencing an entire generation’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/967630/dave-eggers-openai-chatgpt-silencing-an-entire-generation",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T20:54:42+00:00",
    "summary": "Last year, Sam Altman invited author Dave Eggers to give a talk to around 200 OpenAI staffers. The man has written countless novels, screenplays, pieces of journalism, started McSweeney's, and founded"
  },
  {
    "id": "rss:https://www.theverge.com/tech/967612/google-pixel-11a-tensor-g6-leak",
    "domain": "大厂 AI 动态",
    "title": "Google might not kneecap the Pixel 11a with an old processor",
    "url": "https://www.theverge.com/tech/967612/google-pixel-11a-tensor-g6-leak",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T18:25:08+00:00",
    "summary": "Mystic Leaks suggests that the Pixel 11a will return to featuring a flagship-grade processor with the Tensor G6. Rather than the Tensor G5 found in the Pixel 10 and 10 Pro, the Pixel 10a shipped with "
  },
  {
    "id": "rss:https://www.theverge.com/design/967606/google-open-source-3d-emoji",
    "domain": "大厂 AI 动态",
    "title": "Google is open-sourcing its 3D emoji",
    "url": "https://www.theverge.com/design/967606/google-open-source-3d-emoji",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T16:40:55+00:00",
    "summary": "Now, if you want to, you can use Google's 3D emoji in your own creations. The company shared some details about how it went about designing the little pictograms and why, as part of World Emoji Day on"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/967311/gopro-max2-360-degree-action-cam-accessory-bundle-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "GoPro&#8217;s discounted Max 2 bundle includes $100 worth of accessories",
    "url": "https://www.theverge.com/gadgets/967311/gopro-max2-360-degree-action-cam-accessory-bundle-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T15:00:00+00:00",
    "summary": "A 360-degree camera is a great way to ensure you capture every bit of the action, but prices tend to be on the high end for models worth your attention. That’s why it’s notable that the GoPro Max 2 ac"
  },
  {
    "id": "rss:https://www.theverge.com/report/967583/guardian-carter-sherman-podcast-interview",
    "domain": "大厂 AI 动态",
    "title": "The Guardian’s Carter Sherman fondly remembers being terrified by Ocarina of Time",
    "url": "https://www.theverge.com/report/967583/guardian-carter-sherman-podcast-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T14:30:00+00:00",
    "summary": "Carter Sherman has been covering sex, gender, and the complex personal and national politics that accompany them for years. She was a senior reporter for Vice and has written for Elle, Ms. magazine, a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/967183/best-facial-recognition-smart-locks-review",
    "domain": "大厂 AI 动态",
    "title": "Surprise! Facial recognition smart locks are actually good",
    "url": "https://www.theverge.com/tech/967183/best-facial-recognition-smart-locks-review",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T14:00:00+00:00",
    "summary": "Hands-free unlocking is the future of smart locks. The best smart home tech removes friction, and having your door unlock for you as you walk up is as frictionless as it gets - no passcodes to remembe"
  },
  {
    "id": "rss:https://www.theverge.com/tech/966788/sony-bravia-9-ii-tv-review",
    "domain": "大厂 AI 动态",
    "title": "Sony’s flagship RGB LED TV is incredible",
    "url": "https://www.theverge.com/tech/966788/sony-bravia-9-ii-tv-review",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T12:30:00+00:00",
    "summary": "The Sony Bravia 9 II is the most anticipated new TV in years. It's an amazing RGB LED TV. I watched Dungeons &#38; Dragons: Honor Among Thieves on the new Bravia with my son, who has been getting into"
  },
  {
    "id": "rss:https://www.theverge.com/games/961152/denshattack-review",
    "domain": "大厂 AI 动态",
    "title": "More games should be on rails (literally)",
    "url": "https://www.theverge.com/games/961152/denshattack-review",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T12:00:00+00:00",
    "summary": "It's been a good few weeks for games on rails. Nintendo's Star Fox remake wisely kept the tightly scripted, action-packed levels from Star Fox 64 largely the same, and they're still fun to fly through"
  },
  {
    "id": "rss:https://www.theverge.com/tech/967544/best-apps-gadgets-reading-installer",
    "domain": "大厂 AI 动态",
    "title": "The apps, gadgets, and tools every reader needs",
    "url": "https://www.theverge.com/tech/967544/best-apps-gadgets-reading-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 136, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, hope your neighborhood isn't as smoky as mine, and also you can read "
  },
  {
    "id": "rss:https://www.theverge.com/tech/966964/emtb-riders-are-not-cheaters",
    "domain": "大厂 AI 动态",
    "title": "Fine, electric mountain bikes don’t suck",
    "url": "https://www.theverge.com/tech/966964/emtb-riders-are-not-cheaters",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T07:00:00+00:00",
    "summary": "Cheater, I'd grumble between huffs as yet another e-bike rider casually skittered past me on a steep ascent. It's this purist attitude that, for years, has left me blind to one simple fact: electric m"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/waymo-appears-to-pause-san-francisco-service-amidst-power-outage/",
    "domain": "大厂 AI 动态",
    "title": "Waymo says San Francisco service has resumed after one-hour pause",
    "url": "https://techcrunch.com/2026/07/18/waymo-appears-to-pause-san-francisco-service-amidst-power-outage/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T19:30:23+00:00",
    "summary": "This isn’t the first time power outages have caused issues for Waymo."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/kimi-threat-or-menace/",
    "domain": "大厂 AI 动态",
    "title": "Kimi: Threat or menace?",
    "url": "https://techcrunch.com/2026/07/18/kimi-threat-or-menace/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T18:51:07+00:00",
    "summary": "Chinese company Moonshot AI released a new version of its Kimi model this week, prompting concern about \"full AI communism.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/all-the-evs-that-were-discontinued-or-killed-off-in-the-u-s-this-year/",
    "domain": "大厂 AI 动态",
    "title": "All the EVs that were discontinued or killed off in the U.S. this year",
    "url": "https://techcrunch.com/2026/07/18/all-the-evs-that-were-discontinued-or-killed-off-in-the-u-s-this-year/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T16:30:00+00:00",
    "summary": "Th Honda Prologue will no longer be sold in the U.S., joining a growing list of EV models to exit the market this year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/federal-employees-can-download-tiktok-on-their-work-phones-again/",
    "domain": "大厂 AI 动态",
    "title": "Federal employees can download TikTok on their work phones again",
    "url": "https://techcrunch.com/2026/07/18/federal-employees-can-download-tiktok-on-their-work-phones-again/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T15:54:24+00:00",
    "summary": "The Department of Justice says that federal employees can now download TikTok on their government devices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/a-600-mile-road-trip-and-data-proves-ev-charging-doesnt-suck-anymore/",
    "domain": "大厂 AI 动态",
    "title": "A 600-mile road trip (and data) proves EV charging doesn’t suck anymore",
    "url": "https://techcrunch.com/2026/07/18/a-600-mile-road-trip-and-data-proves-ev-charging-doesnt-suck-anymore/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T14:32:00+00:00",
    "summary": "A recent road trip in an EV revealed just how much faster and more reliable DC Fast charging has become in the U.S."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/neil-rimer-thinks-the-ai-money-is-coming-back-out/",
    "domain": "大厂 AI 动态",
    "title": "Neil Rimer thinks the AI money is coming back out",
    "url": "https://techcrunch.com/2026/07/17/neil-rimer-thinks-the-ai-money-is-coming-back-out/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T04:47:25+00:00",
    "summary": "Neil Rimer, the venture capitalist who co-founded Index Ventures, predicts the historic wealth AI is generating in Silicon Valley will have to be redistributed, voluntarily or involuntarily."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/applications-close-in-48-hours-heres-everything-australian-founders-need-to-know-about-stripe-x-startup-battlefield/",
    "domain": "大厂 AI 动态",
    "title": "Applications close in 48 hours — here’s everything Australian founders need to know about Stripe x Startup Battlefield",
    "url": "https://techcrunch.com/2026/07/17/applications-close-in-48-hours-heres-everything-australian-founders-need-to-know-about-stripe-x-startup-battlefield/",
    "source": "Isabelle Johannessen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T23:08:00+00:00",
    "summary": "The window is almost shut. On August 19, eight startups will take the stage at Stripe Tour Sydney in front of investors, global press, and the Australian tech community. One startup walks away with au"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/vertu-wants-executives-to-pay-6880-for-an-ai-agent-heres-how-it-actually-performs/",
    "domain": "大厂 AI 动态",
    "title": "Vertu wants executives to pay $6,880 for an AI agent — here’s how it actually performs",
    "url": "https://techcrunch.com/2026/07/17/vertu-wants-executives-to-pay-6880-for-an-ai-agent-heres-how-it-actually-performs/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T22:55:09+00:00",
    "summary": "From AI workflows to battery life and security, here's what it's really like to live with Vertu's luxury foldable every day."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/",
    "domain": "大厂 AI 动态",
    "title": "Databricks hits $188B valuation, extending its run as AI’s favorite second act",
    "url": "https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T22:12:56+00:00",
    "summary": "Databricks has remade its image into an AI company and has published research on the cost savings of open weight AI models for coding."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/the-zoom-hack-that-says-dont-record-me/",
    "domain": "大厂 AI 动态",
    "title": "The Zoom hack that says, ‘Don’t record me’",
    "url": "https://techcrunch.com/2026/07/17/the-zoom-hack-that-says-dont-record-me/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T21:20:47+00:00",
    "summary": "If every meeting, watercooler conversation, and date gets transcribed and summarized, who's actually reading any of it?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/agility-robotics-plants-its-flag-in-teslas-backyard/",
    "domain": "大厂 AI 动态",
    "title": "Agility Robotics plants its flag in Tesla’s backyard",
    "url": "https://techcrunch.com/2026/07/17/agility-robotics-plants-its-flag-in-teslas-backyard/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T20:19:49+00:00",
    "summary": "Agility is opening a new training center for its Digit robots in Fremont, California."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/ai-driven-memory-crunch-jolts-indias-smartphone-market/",
    "domain": "大厂 AI 动态",
    "title": "AI-driven memory crunch jolts India’s smartphone market",
    "url": "https://techcrunch.com/2026/07/17/ai-driven-memory-crunch-jolts-indias-smartphone-market/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T20:09:27+00:00",
    "summary": "India's smartphone slowdown highlights how the AI boom is reshaping consumer electronics, from pricing and demand to corporate strategy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/",
    "domain": "大厂 AI 动态",
    "title": "Apple and Google ordered to purge ‘nudify’ apps from App Stores",
    "url": "https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:49:53+00:00",
    "summary": "In letters sent to Apple and Google, San Francisco City Attorney David Chiu said that both companies have long been aware that they are hosting apps in violation of state law."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/nuclear-startup-valar-atomics-in-talks-to-raise-new-funding-at-6b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Nuclear startup Valar Atomics in talks to raise new funding at $6B valuation",
    "url": "https://techcrunch.com/2026/07/17/nuclear-startup-valar-atomics-in-talks-to-raise-new-funding-at-6b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:22:00+00:00",
    "summary": "The potential deal highlights a growing trend of complex, multi-stage funding rounds that mask true entry prices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/i-replaced-my-space-heater-and-ceiling-fan-with-one-dyson-appliance/",
    "domain": "大厂 AI 动态",
    "title": "I replaced my space heater and ceiling fan with one Dyson appliance",
    "url": "https://techcrunch.com/2026/07/17/i-replaced-my-space-heater-and-ceiling-fan-with-one-dyson-appliance/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T18:00:17+00:00",
    "summary": "Designed for year-round comfort, the Dyson Hot+Cool HF1 combines quiet operation and simple controls with Dyson's signature bladeless design."
  },
  {
    "id": "rss:https://techcrunch.com/video/how-apples-big-lawsuit-could-disrupt-openais-ipo-plans/",
    "domain": "大厂 AI 动态",
    "title": "How Apple’s big lawsuit could disrupt OpenAI’s IPO plans",
    "url": "https://techcrunch.com/video/how-apples-big-lawsuit-could-disrupt-openais-ipo-plans/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T17:45:46+00:00",
    "summary": "Apple&#160;filed a trade secrets&#160;lawsuit against OpenAI&#160;last Friday, and&#160;it&#8217;s&#160;not messing around. The complaint alleges a pattern of misconduct reaching all the way up to Ope"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/fbi-arrests-man-accused-of-using-steam-games-to-drain-victims-crypto-wallets/",
    "domain": "大厂 AI 动态",
    "title": "FBI arrests man accused of using Steam games to drain victims’ crypto wallets",
    "url": "https://techcrunch.com/2026/07/17/fbi-arrests-man-accused-of-using-steam-games-to-drain-victims-crypto-wallets/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:18:09+00:00",
    "summary": "Prosecutors accused 21-year-old student Zyaire Wilkins of publishing on Steam several fake video games that contained malware, infecting thousands of victims, and stealing crypto from some of them."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/parents-want-safer-phones-for-kids-these-companies-are-answering-the-call/",
    "domain": "大厂 AI 动态",
    "title": "Parents want safer phones for kids. These companies are answering the call.",
    "url": "https://techcrunch.com/2026/07/17/parents-want-safer-phones-for-kids-these-companies-are-answering-the-call/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:12:46+00:00",
    "summary": "As parents look for alternatives to unrestricted smartphones, a growing number of companies are building phones designed specifically for kids, from feature-limited mobile devices to minimalist home p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/amazon-fixing-bug-that-billed-some-aws-customers-billions-of-dollars/",
    "domain": "大厂 AI 动态",
    "title": "Amazon fixing bug that billed some AWS customers billions of dollars",
    "url": "https://techcrunch.com/2026/07/17/amazon-fixing-bug-that-billed-some-aws-customers-billions-of-dollars/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:29:21+00:00",
    "summary": "Some Amazon customers logged on Friday to a surprise bill estimate claiming that they owed the tech and cloud giant billions in fees."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/",
    "domain": "大厂 AI 动态",
    "title": "Patreon stops asking AI bots not to scrape — and starts blocking them",
    "url": "https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:21:17+00:00",
    "summary": "Patreon is strengthening its defenses against AI scraping by working with Cloudflare to block bots that train AI models on creators’ content without permission. The move marks a shift away from relyin"
  },
  {
    "id": "rss:https://stratechery.com/2026/mainframes-and-main-characters/",
    "domain": "大厂 AI 动态",
    "title": "2026.29: Mainframes and Main Characters",
    "url": "https://stratechery.com/2026/mainframes-and-main-characters/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of July 13, 2026, including the end of the mainframe, the continuing adventures of OpenAI, and answering the question, \"Is Netflix Washed?\"."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/will-ai-fix-prior-authorization-or-make-it-worse/",
    "domain": "大厂 AI 动态",
    "title": "Will AI fix prior authorization—or make it worse?",
    "url": "https://arstechnica.com/ai/2026/07/will-ai-fix-prior-authorization-or-make-it-worse/",
    "source": "Joshua Cohen, Undark Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:18:25+00:00",
    "summary": "The government is piloting a program that uses AI for insurance-coverage decisions."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/google-backed-satellites-for-wildfire-detection-launch-as-smoke-chokes-us-canada/",
    "domain": "大厂 AI 动态",
    "title": "Google-backed satellites for wildfire detection launch as smoke chokes US, Canada",
    "url": "https://arstechnica.com/space/2026/07/google-backed-satellites-for-wildfire-detection-launch-as-smoke-chokes-us-canada/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:50:18+00:00",
    "summary": "The FireSat program can spot wildfires that other satellites miss."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/the-pentagons-space-development-agency-hasnt-moved-as-fast-as-anyone-would-like/",
    "domain": "大厂 AI 动态",
    "title": "The Pentagon's Space Development Agency hasn't moved as fast as anyone would like",
    "url": "https://arstechnica.com/space/2026/07/the-pentagons-space-development-agency-hasnt-moved-as-fast-as-anyone-would-like/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:19:42+00:00",
    "summary": "\"Missiles are being launched at the joint force every single day in [Operation] Epic Fury.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/hegseth-wants-a-high-t-military-doctors-call-it-a-clinical-minefield/",
    "domain": "大厂 AI 动态",
    "title": "Hegseth wants a \"High-T\" military; doctors call it a clinical minefield",
    "url": "https://arstechnica.com/health/2026/07/hegseth-wants-a-high-t-military-doctors-call-it-a-clinical-minefield/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T18:53:11+00:00",
    "summary": "\"We're turning the clock back on rational healthcare.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/taco-bell-iceburg-lettuce-identified-as-source-of-cyclosporiasis-in-5-states/",
    "domain": "大厂 AI 动态",
    "title": "Taco Bell iceberg lettuce identified as source of cyclosporiasis in 5 states",
    "url": "https://arstechnica.com/health/2026/07/taco-bell-iceburg-lettuce-identified-as-source-of-cyclosporiasis-in-5-states/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T18:45:23+00:00",
    "summary": "Don't eat Taco Bell lettuce in Indiana, Kentucky, Michigan, Ohio, or West Virginia."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/troubling-new-details-emerge-on-diabetes-ouster-controversy/",
    "domain": "大厂 AI 动态",
    "title": "Troubling new details emerge on diabetes ouster controversy",
    "url": "https://arstechnica.com/science/2026/07/troubling-new-details-emerge-on-diabetes-ouster-controversy/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T17:08:05+00:00",
    "summary": "American Diabetes Association blocked publication of op-ed articles so the authors posted them as a preprint."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/will-russias-answer-to-the-falcon-9-rocket-ever-take-flight/",
    "domain": "大厂 AI 动态",
    "title": "Will Russia's answer to the Falcon 9 rocket ever take flight?",
    "url": "https://arstechnica.com/space/2026/07/will-russias-answer-to-the-falcon-9-rocket-ever-take-flight/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:42:19+00:00",
    "summary": "Grasshopper-like tests could begin in 2028."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/fubo-hikes-prices-by-15-after-restoring-some-nbcu-channels-lost-in-november/",
    "domain": "大厂 AI 动态",
    "title": "Fubo hikes prices by $15 after restoring some NBCU channels lost in November",
    "url": "https://arstechnica.com/gadgets/2026/07/fubo-hikes-prices-by-15-after-restoring-some-nbcu-channels-lost-in-november/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:24:21+00:00",
    "summary": "Fubo subscribers still don't have Versant channels."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/apple-google-must-stop-profiting-off-ai-nudify-apps-san-francisco-ag-says/",
    "domain": "大厂 AI 动态",
    "title": "San Francisco orders Apple, Google to remove nudify apps from app stores",
    "url": "https://arstechnica.com/tech-policy/2026/07/apple-google-must-stop-profiting-off-ai-nudify-apps-san-francisco-ag-says/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:10:05+00:00",
    "summary": "Official estimates Google and Apple likely made millions in nudify app fees."
  },
  {
    "id": "rss:https://arstechnica.com/staff/2026/07/ars-is-looking-for-a-senior-technology-reporter-and-you-might-be-it/",
    "domain": "大厂 AI 动态",
    "title": "Ars is looking for a senior technology reporter, and you might be it!",
    "url": "https://arstechnica.com/staff/2026/07/ars-is-looking-for-a-senior-technology-reporter-and-you-might-be-it/",
    "source": "Lee Hutchinson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:52:28+00:00",
    "summary": "Desktops, laptops, phones, CPUs, GPUs, NAS—if you know this stuff, come work for us!"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/national-academies-climate-attribution-is-maturing-but-still-has-limits/",
    "domain": "大厂 AI 动态",
    "title": "The report oil companies are worried about: Climate attribution science",
    "url": "https://arstechnica.com/science/2026/07/national-academies-climate-attribution-is-maturing-but-still-has-limits/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:30:10+00:00",
    "summary": "New report says our ability to tie weather damages to climate change is improving."
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 312,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48948435",
    "domain": "股票",
    "title": "Short sellers notch $8.7B profit as SpaceX shares dip to IPO price",
    "url": "https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 166,
    "published_at": "2026-07-17T15:17:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48678873",
    "domain": "股票",
    "title": "OpenAI leans toward waiting until next year for IPO",
    "url": "https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-06-25T20:36:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-07-17T18:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48946872",
    "domain": "股票",
    "title": "US Corporate Insiders Are Selling Stocks at a Near Record Pace",
    "url": "https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace",
    "source": "pimienta",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-17T13:00:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 80,
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
    "points": 50,
    "published_at": "2026-07-18T15:26:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48947500",
    "domain": "股票",
    "title": "A.I. Is Running on Borrowed Money",
    "url": "https://www.nytimes.com/2026/07/17/business/ai-spending-oracle-stocks-bonds.html",
    "source": "ripe",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-17T14:01:11+00:00",
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
    "id": "wscn:3777343",
    "domain": "股票",
    "title": "关于杠杆新规、估值和外资最新走向，这是华尔街对韩股的最新看法",
    "url": "https://wallstreetcn.com/articles/3777343",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T04:10:54+00:00",
    "summary": "暴跌25%砸出20年大底！韩股KOSPI估值跌穿08年金融危机谷底。高盛与瑞银齐发声：极端错杀下风险收益比已转正。随着杠杆ETF风险出清、外资悄然进场抄底。"
  },
  {
    "id": "wscn:3777090",
    "domain": "股票",
    "title": "房地产夏季展望：一线租金连涨4月，结构性拐点是否触底信号？",
    "url": "https://wallstreetcn.com/premium/articles/3777090?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T03:33:35+00:00",
    "summary": "北京、上海、深圳住宅租金连续四个月环比上涨，一线城市上半年租金累计上涨0.60%，终结了连续两年的调整态势。"
  },
  {
    "id": "wscn:3777339",
    "domain": "股票",
    "title": "DeepSeek V4「满血版」曝光了！最快明天发布",
    "url": "https://wallstreetcn.com/articles/3777339",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T03:05:42+00:00",
    "summary": "最快明日！DeepSeek V4满血版即将发布。新版性能直追GPT-5.6，并首度引入“峰谷计费”。凭借仅巨头七分之一的极致低价，“价格屠夫”将再掀震撼市场的“DeepSeek时刻”！"
  },
  {
    "id": "wscn:3777336",
    "domain": "股票",
    "title": "数据中心成本暴增！甲骨文又暴雷？",
    "url": "https://wallstreetcn.com/articles/3777336",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T02:49:08+00:00",
    "summary": "甲骨文在新墨西哥州165亿美元AI数据中心因环保审批受阻，被迫将自建天然气电厂改为燃料电池，成本骤增数十亿美元。同时，威斯康星州项目因输电成本分摊和信用评级相关监管裁决，额外增加逾1亿美元支出。近期标普下调其评级，凸显科技巨头在AI基础设施建设中普遍面临环保、水资源、社区许可等隐性成本挑战。"
  },
  {
    "id": "wscn:3777329",
    "domain": "股票",
    "title": "美军对伊朗发动新一轮空袭，约旦美军基地5天遭4袭，美军两人死亡，伊朗最高领袖强调将给美国留下“刻骨铭心的教训”",
    "url": "https://wallstreetcn.com/articles/3777329",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T02:35:23+00:00",
    "summary": "据美国方面消息，伊朗在过去5天内对位于约旦的美军基地发动4次袭击，造成美军两人死亡、数十人受伤，并有多架直升机受损。伊朗最高领袖穆杰塔巴·哈梅内伊18日发表声明称，美方屡次违背其与伊朗总统签署的谅解备忘录，证明美国总统的签字“毫无价值且无效”。"
  },
  {
    "id": "wscn:3777171",
    "domain": "股票",
    "title": "下周重磅日程：欧央行利率决议；谷歌、特斯拉、IBM、英特尔与宁德时代财报",
    "url": "https://wallstreetcn.com/articles/3777171",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T02:10:06+00:00",
    "summary": "财报方面，谷歌、特斯拉、英特尔、IBM、德州仪器及宁德时代集中放榜，AMD举办AI大会，CEO苏姿丰发表演讲。货币政策方面，欧洲央行利率决议来袭，市场预期按兵不动。地缘政治方面，继续关注美伊局势，伯纳姆有望正式接任英国首相。此外，7月国内重磅会议、长鑫科技或上市、DeepSeek V4正式版、世界杯决赛等亦值得关注。"
  },
  {
    "id": "wscn:3777332",
    "domain": "股票",
    "title": "AI算力需求提振光器件景气度，天孚通信上半年净利润预增25%—45%｜财报见闻",
    "url": "https://wallstreetcn.com/articles/3777332",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T02:00:50+00:00",
    "summary": "天孚通信预计2026年上半年净利润11.24亿至13.04亿元，同比增长25%至45%。受益于全球AI与数据中心建设带动高速光器件需求增长，公司持续进行自动化升级以提升盈利能力。但汇兑损失使财务费用同比上升，对利润造成一定拖累。"
  },
  {
    "id": "wscn:3777331",
    "domain": "股票",
    "title": "10天借出10%股份！空头猛扑SpaceX",
    "url": "https://wallstreetcn.com/articles/3777331",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T01:48:01+00:00",
    "summary": "SpaceX股价已跌破发行价，较盘中高点下跌约40%。做空压力急剧攀升，空头借出比例10天内骤升10个百分点，空头累计获利约40亿美元。此外，约9亿股解禁将至加剧抛压，债券收益率向垃圾级靠拢，市场对其股债两端的风险重新定价。"
  },
  {
    "id": "wscn:3777325",
    "domain": "股票",
    "title": "WAIC智能体手机潮涌调研：荣耀、阶跃、中兴各有什么筹码？",
    "url": "https://wallstreetcn.com/articles/3777325",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T01:21:30+00:00",
    "summary": "谁能成为最后的赢家还充满未知数"
  },
  {
    "id": "wscn:3777330",
    "domain": "股票",
    "title": "史上跌速最快、跌幅最大的科技股抛售潮接近尾声了吗？高盛对市场“残酷轮动”的反思",
    "url": "https://wallstreetcn.com/articles/3777330",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T01:14:29+00:00",
    "summary": "高盛合伙人Mark Wilson指出，本轮抛售已持续17个交易日，美股动量因子从峰值回撤28%，TMT动量因子跌幅更达40%，创历史最快最深回撤纪录。根源在于仓位拥挤与杠杆集中，而非基本面恶化。他认为平仓过程\"接近尾声\"，但短期缺乏反转催化剂，且估值仍高、市场结构风险犹存，轮动后的新方向需等待夏季财报消化后方能明朗。"
  },
  {
    "id": "wscn:3774897",
    "domain": "股票",
    "title": "【今天13点会议预告】听徐小庆分享股债汇市场最新洞察，推演下半年配置逻辑",
    "url": "https://wallstreetcn.com/articles/3774897",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T01:05:00+00:00",
    "summary": "7月19日徐小庆主讲Alpha线上闭门私享会：展望2026下半年大类资产配置风向，哪些资产最值得关注？"
  },
  {
    "id": "wscn:3777328",
    "domain": "股票",
    "title": "AI手机告别功能竞赛，荣耀开始重构操作系统",
    "url": "https://wallstreetcn.com/articles/3777328",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T15:43:31+00:00",
    "summary": "AI手机的竞争正在越过功能叠加阶段。\n 7月18日，在2026世界人工智能大会期间，荣耀发布Agen..."
  },
  {
    "id": "wscn:3777326",
    "domain": "股票",
    "title": "蔚来芯片子公司神玑首次独立参展WAIC，瞄准汽车之外AI市场",
    "url": "https://wallstreetcn.com/articles/3777326",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T14:01:18+00:00",
    "summary": "蔚来的芯片业务，开始走出汽车。\n7月17日，在2026世界人工智能大会（WAIC）上，蔚来芯片子公司..."
  },
  {
    "id": "wscn:3777317",
    "domain": "股票",
    "title": "加息周期真的回来了吗？",
    "url": "https://wallstreetcn.com/articles/3777317",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:55:14+00:00",
    "summary": "分析认为，本周市场惊心动魄。短端利率斜率趋缓，更像政策微调而非加息周期；长端利率却暗藏上行动力，财政赤字阴影难散。FOMC按兵不动是基本假设，但霍尔木兹海峡持续升级若叠加通胀压力，加息25bp绝非空谈——坏事连着坏事，概率往往比看起来高得多。"
  },
  {
    "id": "wscn:3777113",
    "domain": "股票",
    "title": "4.3% 增速天秤再回摆：K型分化背后，消费何时接棒？",
    "url": "https://wallstreetcn.com/premium/articles/3777113?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T08:55:29+00:00",
    "summary": "二季度经济增速放缓但结构分化延续，出口与高技术制造托底，消费修复待政策加力后逐步接棒。"
  },
  {
    "id": "wscn:3777307",
    "domain": "股票",
    "title": "上游订单爆表、下游不计代价！“大空头”查诺斯：AI这笔账为什么算不过来",
    "url": "https://wallstreetcn.com/articles/3777307",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T08:47:17+00:00",
    "summary": "查诺斯表示，超大云厂商正基于短期现货定价进行长达二十年的资产决策，大量GPU设备因堆积仓库、归入在建工程而推迟折旧计提，掩盖了技术贬值和利润虚高。云厂商增量资本回报率已由40%腰斩至20%，未来若跌破10%，巨头管理层将被迫减速，从而引爆整个AI生态。"
  },
  {
    "id": "wscn:3777301",
    "domain": "股票",
    "title": "阿里云WAIC论坛： “AI爆发不靠一两颗芯片”、SaaS将转向“按结果付费”、模型不再是唯一核心",
    "url": "https://wallstreetcn.com/articles/3777301",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T08:39:43+00:00",
    "summary": "阿里云WAIC论坛释放信号：智能体正成为云计算的“第一用户”，企业对AI的需求将从模型调用转向可量化的业务结果。李飞飞提出AI SaaS或将走向“按结果付费”，Mark Collier则称“模型不再是唯一核心”。阿里云同步展示了面向智能体的算力、缓存、数据库、沙箱、安全及团队协作能力，物流、开源研发等场景已披露效率改善数据。"
  },
  {
    "id": "wscn:3776376",
    "domain": "股票",
    "title": "当“大投行”撞上“硬科技”：中国券商正复制海外巨头的超级进化",
    "url": "https://wallstreetcn.com/premium/articles/3776376?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T06:13:03+00:00",
    "summary": "尽管“看天吃饭”的周期属性不会消失，但头部券商比以往任何时点都有可能“掌握自己的命运”。"
  },
  {
    "id": "wscn:3777291",
    "domain": "股票",
    "title": "高盛点评Kimi K3：中国开源模型“智能”达到全球普及关键点，高端模型竞争激烈",
    "url": "https://wallstreetcn.com/articles/3777291",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T05:11:08+00:00",
    "summary": "高盛表示，Kimi K3以2.8万亿参数横空出世，将API定价拉升至每百万token 2.3美元，创中国模型定价新高，标志着国内AI公司正式从\"价格战\"迈向\"定价权\"争夺。然而硬币另一面，智谱单日暴跌28%、MiniMax跌16%，揭示出高端编程赛道竞争白热化下，市场对AI模型公司护城河可持续性的深层焦虑。"
  },
  {
    "id": "wscn:3777289",
    "domain": "股票",
    "title": "AI牛市结束了吗？市场充满疑虑",
    "url": "https://wallstreetcn.com/articles/3777289",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T03:46:45+00:00",
    "summary": "科技巨头业绩亮眼、资本开支计划积极，股价却有所下滑——这一诡异背离正令华尔街陷入困惑。野村证券警告，AI繁荣终结已从三种情景演变为四重路径交织，成本收益平衡愈发模糊。半导体重挫、软件逆涨的板块分化暗示资金悄然重定价，而债券市场迄今未现降息押注，意味着AI终结的定价远未完成。"
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
    "id": "hn:48907665",
    "domain": "股票",
    "title": "IBM is on pace for its worst day ever",
    "url": "https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever",
    "source": "1970-01-01",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-07-14T14:39:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48612095",
    "domain": "股票",
    "title": "Show HN: My Windows XP portfolio with working Game Boy and iPod",
    "url": "https://mitchivin.com/",
    "source": "mitchivin",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-06-20T19:18:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48634931",
    "domain": "股票",
    "title": "SpaceX Drops 14% in One Day, Price Now Below IPO Launch",
    "url": "https://finance.yahoo.com/quote/SPCX/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-06-22T19:33:55+00:00",
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
    "id": "hn:48905958",
    "domain": "股票",
    "title": "IBM shares down 23% as clients spend more on hardware and memory chips",
    "url": "https://www.cnbc.com/2026/07/14/ibm-warns-second-quarter-earnings-fell-short-of-expectations.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-14T12:44:17+00:00",
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
    "id": "hn:48598558",
    "domain": "股票",
    "title": "The average SpaceX buyer post-IPO is almost under water after two-day slide",
    "url": "https://www.cnbc.com/2026/06/18/the-average-spacex-buyer-post-ipo-is-almost-under-water-after-two-day-slide.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-06-19T13:48:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48824532",
    "domain": "股票",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48853145",
    "domain": "股票",
    "title": "California universities stockpiling AR-15s, grenades and submachine guns",
    "url": "https://www.theguardian.com/us-news/2026/jul/09/california-universities-military-equipment",
    "source": "sizzle",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-09T22:20:12+00:00",
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
    "id": "hn:48717469",
    "domain": "金融",
    "title": "The CEO of Mullvad is the main financer of the Swedish Örebro party",
    "url": "https://det.social/@lostgen/116820546568940358",
    "source": "Risse",
    "platform": "hackernews",
    "points": 695,
    "published_at": "2026-06-29T10:45:51+00:00",
    "summary": ""
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
    "id": "hn:48634585",
    "domain": "金融",
    "title": "Canada plans 'nuclear renaissance' with up to 10 reactors built by 2040",
    "url": "https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509",
    "source": "geox",
    "platform": "hackernews",
    "points": 593,
    "published_at": "2026-06-22T19:06:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 491,
    "published_at": "2026-07-15T03:32:45+00:00",
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
    "id": "hn:48647444",
    "domain": "金融",
    "title": "Digital euro clears key hurdle as EU seeks to break free from U.S. credit cards",
    "url": "https://finance.yahoo.com/markets/currencies/articles/ecb-secures-key-parliamentary-backing-102718449.html",
    "source": "madars",
    "platform": "hackernews",
    "points": 232,
    "published_at": "2026-06-23T16:27:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673787",
    "domain": "金融",
    "title": "Federal agents track down woman, demand she remove Instagram post about ICE",
    "url": "https://www.syracuse.com/news/2026/06/federal-agents-track-down-syracuse-woman-demand-she-remove-instagram-post-about-ice.html",
    "source": "coloneltcb",
    "platform": "hackernews",
    "points": 217,
    "published_at": "2026-06-25T14:16:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48892638",
    "domain": "金融",
    "title": "Benchmarking 15 “E-Waste” GPUs with Modern Workloads",
    "url": "https://esologic.com/benchmarking-tesla-gpus/",
    "source": "eso_logic",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-07-13T13:48:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48703613",
    "domain": "金融",
    "title": "Feds Killed Polestar and Spared Volvo",
    "url": "https://www.thedrive.com/news/feds-killed-polestar-and-spared-volvo-that-should-terrify-you",
    "source": "mraniki",
    "platform": "hackernews",
    "points": 175,
    "published_at": "2026-06-28T01:55:21+00:00",
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
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-07-18T00:28:46+00:00",
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
    "id": "hn:48653311",
    "domain": "金融",
    "title": "Prairieland defendants sentenced today to prison terms ranging from 30-100 years",
    "url": "https://prairielanddefendants.com/press-release/eight-federal-prairieland-defendants-sentenced-today-to-prison-terms-ranging-from-30-100-years-for-common-protest-activity/",
    "source": "panic",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-06-23T23:54:00+00:00",
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
    "id": "hn:48735748",
    "domain": "金融",
    "title": "Supreme Court takes sledgehammer to federal regulatory structure",
    "url": "https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure",
    "source": "marojejian",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-06-30T17:05:58+00:00",
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
    "id": "hn:48734220",
    "domain": "金融",
    "title": "Supreme Court strikes down limits on party spending in federal elections",
    "url": "https://apnews.com/article/supreme-court-campaign-finance-party-spending-ohio-91e49ee112197ae1210a9abfa46986ed",
    "source": "khriss",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-06-30T15:34:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756848",
    "domain": "金融",
    "title": "He sent a harsh email to ICE's top official. Federal agents tracked him down",
    "url": "https://www.npr.org/2026/07/01/nx-s1-5874124/dhs-tracks-ice-critic",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-07-02T05:20:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48609233",
    "domain": "金融",
    "title": "Big Tech is borrowing like never before",
    "url": "https://startupfortune.com/big-tech-is-borrowing-like-never-before-and-the-fed-just-made-that-a-lot-more-expensive/",
    "source": "krupan",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-06-20T13:49:15+00:00",
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
    "id": "hn:48678494",
    "domain": "金融",
    "title": "Feds deny Polestar authorization to sell cars in US from model year 2027",
    "url": "https://arstechnica.com/cars/2026/06/feds-deny-polestar-authorization-to-sell-cars-in-us-from-model-year-2027/",
    "source": "Quinner",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-06-25T20:00:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48754128",
    "domain": "金融",
    "title": "US feds are actively hiring \"person who decides which models to ban\"",
    "url": "https://www.usajobs.gov/job/856265200",
    "source": "arm32",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-07-01T22:45:41+00:00",
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
    "id": "hn:48723371",
    "domain": "金融",
    "title": "Feds Tracked Down an Anti-ICE Dad in NYC Hotel, but How?",
    "url": "https://gizmodo.com/federal-agents-reportedly-tracked-down-an-anti-ice-dad-in-a-new-york-hotel-its-not-clear-how-2000778714",
    "source": "ripe",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-06-29T18:42:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673197",
    "domain": "金融",
    "title": "Federating Clusters for Zero-Downtime Kubernetes",
    "url": "https://linkerd.io/2026/06/24/federating-clusters-for-zero-downtime-kubernetes/index.html",
    "source": "PagCatOli",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-06-25T13:37:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48613112",
    "domain": "金融",
    "title": "Dallas Fed: 30% of housing cost increase driven by unauthorized immigration [pdf]",
    "url": "https://www.dallasfed.org/~/media/documents/research/papers/2026/wp2607.pdf",
    "source": "silexia",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-20T21:25:10+00:00",
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
    "id": "hn:48677039",
    "domain": "金融",
    "title": "The AI Data-Center Boom Is Sparking a Third Wave of Inflation",
    "url": "https://www.wsj.com/economy/the-data-center-boom-is-sparking-a-third-wave-of-inflation-926adc6e",
    "source": "gmays",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-25T17:58:44+00:00",
    "summary": ""
  }
]
```
