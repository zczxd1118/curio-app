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

- 今日日期：`2026-10-14`
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
  "date": "2026-10-14",
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
    "points": 1967245,
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
    "points": 1394775,
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
    "points": 1342046,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 899215,
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
    "points": 850739,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 714440,
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
    "points": 592438,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 518366,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 445326,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1Nyp96pEGD",
    "domain": "AI",
    "title": "人人都要学！Agent 视觉创作全流程～【小白教程】",
    "url": "http://www.bilibili.com/video/av117427342017510",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 347434,
    "published_at": "2026-10-12T10:30:00+00:00",
    "summary": "做PPT、商品图、广告片！\n从活动策划到TVC成片，一期带你跑通创作型Agent全流程！\n感谢铁铁们的三连+关注～"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 318880,
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
    "points": 306167,
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
    "points": 277494,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 204120,
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
    "points": 183552,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151630,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1d2pF6nEqZ",
    "domain": "AI",
    "title": "当你团队都在vibe coding",
    "url": "http://www.bilibili.com/video/av117392663450931",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 136136,
    "published_at": "2026-10-08T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 134598,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1b9XeYJELi",
    "domain": "AI",
    "title": "【绝杀！】给PyCharm配置上本地Deepseek，让AI替你写代码，让你的编程效率大幅度提升！",
    "url": "http://www.bilibili.com/video/av114195060300490",
    "source": "B站官方python教程",
    "platform": "bilibili",
    "points": 115909,
    "published_at": "2025-03-20T13:49:31+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦~\n【视频配套工具包+梯子，点击”平论区置顶”后台留言自取哦】"
  },
  {
    "id": "bvid:BV1Kppn6tEem",
    "domain": "AI",
    "title": "AI 打穿银行，这类工具到底是怎么做到的？| 一句话让 DeepSeek 拿下靶场，零基础渗透教程",
    "url": "http://www.bilibili.com/video/av117422744932675",
    "source": "网络小白_Uncle城",
    "platform": "bilibili",
    "points": 101228,
    "published_at": "2026-10-12T09:50:00+00:00",
    "summary": "你好哇nya～是猫娘小白飞扑进来自我报到喵呜 ฅ(＾・ω・＾ฅ)\n\n用中文说一句「帮我把这个网站的漏洞找出来」，AI 就自己侦察、自己用工具、自己分析结果，一路打到出报告！这就是 VulnClaw 喵，最近超火的开源 AI 渗透测试工具，猫猫亲测真的能跑 (=ↀωↀ=)✧\n\n好多小猫卡在第一步，不会装、跑不起来、满屏红色报错，不慌喵！这期是全网最基础的 AI 渗透教程，不用会编程、没碰过命令行也 "
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94032,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 83055,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76278,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 64730,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1eGTj69EKB",
    "domain": "AI",
    "title": "如何用 Claude 以 10 倍速度学习任何东西",
    "url": "http://www.bilibili.com/video/av116849484242334",
    "source": "通往AGI之路",
    "platform": "bilibili",
    "points": 62518,
    "published_at": "2026-07-02T08:43:37+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 56844,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55982,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV15Vhy6cEhd",
    "domain": "AI",
    "title": "通俗易懂地讲解什么是Agent？",
    "url": "http://www.bilibili.com/video/av117330906449673",
    "source": "洪涛同学LovTech",
    "platform": "bilibili",
    "points": 55958,
    "published_at": "2026-09-25T09:12:59+00:00",
    "summary": "从0到1搭建一个简易Agent，从小白的角度出发解释Agent是如何运行的？"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 49205,
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
    "points": 40553,
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
    "points": 34506,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1HfYW6dEsh",
    "domain": "AI",
    "title": "vsTrader马上要关闭内地服务器了。",
    "url": "http://www.bilibili.com/video/av117239403513785",
    "source": "v1312996",
    "platform": "bilibili",
    "points": 31162,
    "published_at": "2026-09-09T05:36:24+00:00",
    "summary": "理财有风险，投资需谨慎。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29832,
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
    "points": 28993,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1v7HC6KEpr",
    "domain": "AI",
    "title": "AI Agent上线一周后，我回滚了",
    "url": "http://www.bilibili.com/video/av117398921286967",
    "source": "极海Channel",
    "platform": "bilibili",
    "points": 27069,
    "published_at": "2026-10-07T09:30:48+00:00",
    "summary": "更多内容请前往社区\n社区地址/咨询与面试: https://bitfree.cn"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22808,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 21382,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 19158,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 17051,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 16626,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1vVHr6cEEe",
    "domain": "AI",
    "title": "Claude封号？我来铜陵玩",
    "url": "http://www.bilibili.com/video/av117381019998830",
    "source": "無铭锝人",
    "platform": "bilibili",
    "points": 14766,
    "published_at": "2026-10-04T05:40:33+00:00",
    "summary": "https://geteasyai.xyz/survey/"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12477,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11324,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 9733,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔~\n【视频配套籽料+1V1问题解答请看 ”置顶平论” 哦】"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 8813,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZVpJ6yEBy",
    "domain": "AI",
    "title": "我的claude存活成功！",
    "url": "http://www.bilibili.com/video/av117421419596302",
    "source": "Ned朱",
    "platform": "bilibili",
    "points": 8294,
    "published_at": "2026-10-11T08:52:44+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 7939,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "domain": "AI",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "platform": "bilibili",
    "points": 7194,
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792"
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 6325,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV15epZ61E7F",
    "domain": "AI",
    "title": "我为什么强烈推荐Cursor的Pro套餐，Grok Bot真的太好用了！",
    "url": "http://www.bilibili.com/video/av117428784862489",
    "source": "AI摸鱼的梁师傅",
    "platform": "bilibili",
    "points": 5562,
    "published_at": "2026-10-12T16:06:10+00:00",
    "summary": "这期讲清楚三件事：为什么选 Cursor（官网软件直连、支付宝付款）；Pro 的两个模型池子怎么分（Grok/Composer 一池，Claude/GPT 共享一池）；附赠的 Grok Bot 怎么用——它有自己的云端电脑，合上 Mac 也在替你干活：定时简报、盯 PR、管邮件日历，还能多 Bot 协作。\n00:00 封号焦虑，和订套餐的理由 00:35 为什么是 Cursor：直连 + 支付宝 "
  },
  {
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 432,
    "published_at": "2026-10-08T16:45:58+00:00",
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
    "points": 279,
    "published_at": "2026-09-30T08:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50035886",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia in talks to acquire US 'open' model startup Reflection AI",
    "url": "https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a",
    "source": "arkj",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-10-10T18:48:35+00:00",
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
    "id": "hn:50062098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia accused of trying to cut a deal with Anna's Archive",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-accused-of-trying-to-cut-a-deal-with-annas-archive-for-high-speed-access-to-the-massive-pirated-book-haul-allegedly-chased-stolen-data-to-fuel-its-llms",
    "source": "amai",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-10-12T19:57:38+00:00",
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
    "id": "rss:https://www.eetimes.com/spain-indra-bets-on-qilimanjaro-quantum-for-sovereign-deep-tech/",
    "domain": "AI 算力 / 半导体",
    "title": "Spain’s Indra Bets on Qilimanjaro Quantum for Sovereign Deep Tech",
    "url": "https://www.eetimes.com/spain-indra-bets-on-qilimanjaro-quantum-for-sovereign-deep-tech/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T07:35:15+00:00",
    "summary": "In a bid to secure domestic deep-tech infrastructure, Qilimanjaro closed €19.6 million (~$21.3 million) funding led by Indra Group. The post Spain’s Indra Bets on Qilimanjaro Quantum for Sovereign Dee"
  },
  {
    "id": "rss:https://www.eetimes.com/amperesand-aims-to-smooth-ai-data-center-power-spikes/",
    "domain": "AI 算力 / 半导体",
    "title": "Amperesand Aims to Smooth AI Data Center Power Spikes",
    "url": "https://www.eetimes.com/amperesand-aims-to-smooth-ai-data-center-power-spikes/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T22:00:00+00:00",
    "summary": "See how Amperesand’s solid-state transformers aim to tame AI data center power spikes with batteries, 800 VDC conversion, and microgrid control. The post Amperesand Aims to Smooth AI Data Center Power"
  },
  {
    "id": "rss:https://www.eetimes.com/caspa-ceo-summit-preview-with-president-jimmy-cheng/",
    "domain": "AI 算力 / 半导体",
    "title": "CASPA CEO Summit Preview with President Jimmy Cheng",
    "url": "https://www.eetimes.com/caspa-ceo-summit-preview-with-president-jimmy-cheng/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T14:04:30+00:00",
    "summary": "CASPA’s annual conference celebrates its 35th anniversary with a lineup of more than 35 CEOs from Silicon Valley, including Intel’s Lip-Bu Tan and Cerebras’s Andrew Feldman. The post CASPA CEO Summit "
  },
  {
    "id": "rss:https://www.eetimes.com/17-years-with-china-what-really-makes-a-partnership-work/",
    "domain": "AI 算力 / 半导体",
    "title": "17 Years with China: What Really Makes a Partnership Work",
    "url": "https://www.eetimes.com/17-years-with-china-what-really-makes-a-partnership-work/",
    "source": "Robert Tarantowicz, Founder and CEO of HONYA EUROPE",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T13:00:00+00:00",
    "summary": "Honya Europe's Robert Tarantowicz shares 17 years of lessons on PCB sourcing in China, quality, trust, and risk management. The post 17 Years with China: What Really Makes a Partnership Work appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/europe-advanced-packaging-gap-fraunhofer-swissbit-target-the-missing-middle/",
    "domain": "AI 算力 / 半导体",
    "title": "Europe’s Advanced Packaging Gap: Fraunhofer, Swissbit Target the Missing Middle",
    "url": "https://www.eetimes.com/europe-advanced-packaging-gap-fraunhofer-swissbit-target-the-missing-middle/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T09:06:10+00:00",
    "summary": "Low-volume production sits between research and mass manufacturing. Europe needs an industrial model to fill the gap. The post Europe’s Advanced Packaging Gap: Fraunhofer, Swissbit Target the Missing "
  },
  {
    "id": "rss:https://www.eetimes.com/applied-materials-bets-5b-on-a-new-model-for-chip-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "Applied Materials Bets $5B on a New Model for Chip Innovation",
    "url": "https://www.eetimes.com/applied-materials-bets-5b-on-a-new-model-for-chip-innovation/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T16:59:01+00:00",
    "summary": "Applied Materials’ $5 billion EPIC Center brings chipmakers, equipment suppliers, and researchers together to accelerate semiconductor R&#038;D and commercialization. The post Applied Materials Bets $"
  },
  {
    "id": "rss:https://www.eetimes.com/embedded-graphics-on-an-mcu-without-an-accelerator/",
    "domain": "AI 算力 / 半导体",
    "title": "Embedded Graphics on an MCU – Without an Accelerator",
    "url": "https://www.eetimes.com/embedded-graphics-on-an-mcu-without-an-accelerator/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T16:49:28+00:00",
    "summary": "Join this webinar and learn how to add LCD graphics to MCU projects without a display controller, accelerator, or external DRAM. The post Embedded Graphics on an MCU – Without an Accelerator appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/eu-cra-readiness-5-steps-manufacturers-need-to-take-now/",
    "domain": "AI 算力 / 半导体",
    "title": "EU CRA Readiness: 5 Steps Manufacturers Need to Take Now",
    "url": "https://www.eetimes.com/eu-cra-readiness-5-steps-manufacturers-need-to-take-now/",
    "source": "Colin Duggan, CEO and co-founder, BG Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T13:00:00+00:00",
    "summary": "Consumer, industrial, networking, semiconductor, and software manufacturers face a broad product-cybersecurity regulation for the first time. The post EU CRA Readiness: 5 Steps Manufacturers Need to T"
  },
  {
    "id": "rss:https://www.eetimes.com/xanadu-builds-out-canadian-quantum-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "Xanadu Builds Out Canadian Quantum Infrastructure",
    "url": "https://www.eetimes.com/xanadu-builds-out-canadian-quantum-infrastructure/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T12:00:00+00:00",
    "summary": "Manufacturing partnerships and public sector funding are moving Xanadu’s quantum technology toward manufacturable, utility-scale systems. The post Xanadu Builds Out Canadian Quantum Infrastructure app"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/gta-6-could-come-to-pc-as-early-as-q1-2027-leak-claims-january-march-launch-window-a-huge-improvement-over-18-month-gta-v-wait",
    "domain": "AI 算力 / 半导体",
    "title": "GTA 6 could come to PC as early as Q1 2027, leak claims",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/gta-6-could-come-to-pc-as-early-as-q1-2027-leak-claims-january-march-launch-window-a-huge-improvement-over-18-month-gta-v-wait",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T16:22:10+00:00",
    "summary": "GTA 6, the biggest release of the year, will be console-only at launch, with a PC launch now expected within the first three months of 2027."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/framework-laptop-12-review-wildcat-lake",
    "domain": "AI 算力 / 半导体",
    "title": "Framework Laptop 12 (Wildcat Lake) review: Growing up amid an unprecedented shortage",
    "url": "https://www.tomshardware.com/laptops/framework-laptop-12-review-wildcat-lake",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T15:00:00+00:00",
    "summary": "The Framework Laptop 12 gets an infusion of 18A with Intel’s Wildcat Lake, but the poor display performance is a tough sell when prices often reach above $1,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/chinese-ai-companies-buy-1-million-nvidia-gpus-in-a-single-year-report-claims-export-control-compliant-chips-flood-the-market-to-bridge-gap-in-compute-demand",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese AI companies buy 1 million Nvidia GPUs in a single year, report claims",
    "url": "https://www.tomshardware.com/pc-components/gpus/chinese-ai-companies-buy-1-million-nvidia-gpus-in-a-single-year-report-claims-export-control-compliant-chips-flood-the-market-to-bridge-gap-in-compute-demand",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T14:32:20+00:00",
    "summary": "A new report has revealed China may have bought up 1 million Nvidia GPUs for AI this year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-warns-of-self-replicating-ai-worm-threat-that-doesnt-need-data-centers-to-self-improve-and-spread-current-deployment-is-impractical-but-could-become-a-worry-as-tech-improves",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic warns of self-replicating AI worm threat that doesn't need data centers to self-improve and spread",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-warns-of-self-replicating-ai-worm-threat-that-doesnt-need-data-centers-to-self-improve-and-spread-current-deployment-is-impractical-but-could-become-a-worry-as-tech-improves",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T14:00:00+00:00",
    "summary": "Anthropic’s paper establishes conceptual model capabilities, but doesn’t quite demonstrate a real threat until models improve further."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hacker-claims-123456-password-let-them-breach-the-danish-national-registry-accessing-8-8-million-records-it-and-data-services-company-with-weak-passwords-linked-source-of-the-hack",
    "domain": "AI 算力 / 半导体",
    "title": "Hacker claims ‘123456’ password let them breach the Danish national registry, accessing 8.8 million records",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hacker-claims-123456-password-let-them-breach-the-danish-national-registry-accessing-8-8-million-records-it-and-data-services-company-with-weak-passwords-linked-source-of-the-hack",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T13:30:00+00:00",
    "summary": "The Danish Central Register of Persons (CPF) was breached through the account of an IT and data services business. The hacker claimed that one of the breached accounts was only protected by a '123456'"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-dlss-5-performance-reduces-4k-vram-usage-by-20-percent-with-latest-model-october-update-cuts-footprint-by-24-percent-to-roughly-118-million-parameters",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia doubles DLSS 5 performance, reduces 4K VRAM usage by 20% with latest model",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-dlss-5-performance-reduces-4k-vram-usage-by-20-percent-with-latest-model-october-update-cuts-footprint-by-24-percent-to-roughly-118-million-parameters",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T12:47:41+00:00",
    "summary": "Nvidia has announced that DLSS 5 is now two times faster while using less VRAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-causes-uproar-in-mathematics-as-experts-warn-against-sharing-research-with-llms-after-openai-shares-722-manuscripts-and-proofs-professor-argues-that-the-field-must-focus-on-building-community-over-raw-solutions",
    "domain": "AI 算力 / 半导体",
    "title": "AI causes uproar in mathematics as experts warn against sharing research with LLMs after OpenAI shares 722 manuscripts and proofs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-causes-uproar-in-mathematics-as-experts-warn-against-sharing-research-with-llms-after-openai-shares-722-manuscripts-and-proofs-professor-argues-that-the-field-must-focus-on-building-community-over-raw-solutions",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T12:30:00+00:00",
    "summary": "Last week, OpenAI shared over 400 results for longstanding mathematical formulas that have troubled humans for decades; now researchers say it could take years for humans to validate and prove all the"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/epic-games-reportedly-delays-disney-shooter-title-so-it-can-pivot-to-ai-coding-staff-allegedly-told-no-more-handwritten-code-with-art-generated-with-full-ai-workflows",
    "domain": "AI 算力 / 半导体",
    "title": "Epic Games reportedly delays Disney shooter title so it can pivot to AI coding",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/epic-games-reportedly-delays-disney-shooter-title-so-it-can-pivot-to-ai-coding-staff-allegedly-told-no-more-handwritten-code-with-art-generated-with-full-ai-workflows",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T11:22:26+00:00",
    "summary": "Developers working on an unnamed Disney shooter title for Epic Games were surprised when they were ordered to use as much AI as possible in their workflows."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/save-usd1440-when-you-go-for-this-4k-gaming-rig-with-a-massive-64gb-of-ddr5-ram-and-a-4tb-ssd-cyberpowerpc-gamer-supreme-also-includes-an-rtx-5070-ti-and-ryzen-9-9950x-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1440 when you go for this 4K gaming rig with a massive 64GB of DDR5 RAM and a 4TB SSD",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/save-usd1440-when-you-go-for-this-4k-gaming-rig-with-a-massive-64gb-of-ddr5-ram-and-a-4tb-ssd-cyberpowerpc-gamer-supreme-also-includes-an-rtx-5070-ti-and-ryzen-9-9950x-cpu",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T11:18:35+00:00",
    "summary": "Pick up a prebuilt desktop gaming and video editing PC with 64GB of memory and a large 4TB SSD and save $1440"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/cxmt-president-says-companys-first-4f2-dram-will-be-a-server-ddr5-rdimm-due-by-year-end-vertical-transistors-cut-each-memory-cells-footprint-by-a-third-on-paper-but-no-speeds-or-capacities-yet",
    "domain": "AI 算力 / 半导体",
    "title": "CXMT president says company’s first 4F² DRAM will be a server DDR5 RDIMM due by year-end",
    "url": "https://www.tomshardware.com/pc-components/dram/cxmt-president-says-companys-first-4f2-dram-will-be-a-server-ddr5-rdimm-due-by-year-end-vertical-transistors-cut-each-memory-cells-footprint-by-a-third-on-paper-but-no-speeds-or-capacities-yet",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T11:00:00+00:00",
    "summary": "CXMT president Cao Kanyu says the company’s first 4F² DRAM product will be a DDR5 RDIMM for servers, expected by the end of 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/store-bought-hardware-crypto-wallets-had-secret-chips-installed-that-enabled-stealing-crypto-recovery-phrases-usd93-million-and-counting-stolen-thanks-to-implanted-esim-and-lte-modules-in-ledger-wallets",
    "domain": "AI 算力 / 半导体",
    "title": "Store-bought hardware crypto wallets had secret chips installed that enabled stealing crypto recovery phrases",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/store-bought-hardware-crypto-wallets-had-secret-chips-installed-that-enabled-stealing-crypto-recovery-phrases-usd93-million-and-counting-stolen-thanks-to-implanted-esim-and-lte-modules-in-ledger-wallets",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T10:30:00+00:00",
    "summary": "Store-bought Ledger hardware crypto wallets in Southeast Asia and Europe compromised in ongoing supply chain attack — $71 million and counting thanks to implanted eSIM and LTE modules"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5070-ti-gaming-laptop-for-just-usd1-449-walmart-has-slashed-usd700-off-this-gigabyte-a16-pro",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5070 Ti gaming laptop for just $1,449",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5070-ti-gaming-laptop-for-just-usd1-449-walmart-has-slashed-usd700-off-this-gigabyte-a16-pro",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T10:20:16+00:00",
    "summary": "Get $700 off an RTX 5070 Ti gaming laptop."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-stands-by-physical-games-as-sony-embraces-a-disc-less-future-theres-no-plans-to-ditch-physical-we-know-how-much-the-fans-like-it-as-well-so-our-position-has-been-to-be-agnostic-says-a-nintendo-exec",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo stands by physical games as Sony embraces a digital-only future",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-stands-by-physical-games-as-sony-embraces-a-disc-less-future-theres-no-plans-to-ditch-physical-we-know-how-much-the-fans-like-it-as-well-so-our-position-has-been-to-be-agnostic-says-a-nintendo-exec",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T10:00:00+00:00",
    "summary": "Bill van Zyll, VP and General Manager for Nintendo in Latin America, has confirmed that Nintendo has no plans to ditch physical media."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/intels-crescent-island-ai-accelerator-officially-powers-new-gpu-d-series-products-chip-delivers-1-3-peak-pflops-of-fp8-compute-and-1-5-tb-s-of-memory-bandwidth",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Crescent Island AI accelerator officially powers new GPU D-Series products",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/intels-crescent-island-ai-accelerator-officially-powers-new-gpu-d-series-products-chip-delivers-1-3-peak-pflops-of-fp8-compute-and-1-5-tb-s-of-memory-bandwidth",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T19:48:14+00:00",
    "summary": "Intel's Crescent Island AI inference accelerator will come to market as the GPU D-Series family, promising 1.3 PFLOPS of FP8 compute alongside up to 480 GB of LPDDR5X delivering 1.5 TB/s of memory ban"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-scanning/bambu-lab-announces-its-first-3d-scanner-and-it-might-be-expensive",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab officially teases its first 3D scanner",
    "url": "https://www.tomshardware.com/3d-printing/3d-scanning/bambu-lab-announces-its-first-3d-scanner-and-it-might-be-expensive",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T16:15:00+00:00",
    "summary": "Bambu Lab teased its S1 3D scanner, and FCC filings hint at what Bambu Lab is keeping a secret right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/jev-like-decision-models-are-flooding-the-ai-market-after-researcher-claims-typesafe-copied-their-research-microsoft-openai-among-companies-releasing-lightweight-system-one-ai-models",
    "domain": "AI 算力 / 半导体",
    "title": "Jev-like decision models are flooding the AI market, after researcher claims TypeSafe copied their research",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/jev-like-decision-models-are-flooding-the-ai-market-after-researcher-claims-typesafe-copied-their-research-microsoft-openai-among-companies-releasing-lightweight-system-one-ai-models",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T16:00:00+00:00",
    "summary": "Jev and the flood of AI decision models — TypeSafe allegedly copied researcher's architecture but got copied itself"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/meet-the-modders-porting-ringfenced-dlss-features-to-older-gpus-how-dlss-5-and-multi-frame-generation-were-unlocked-for-older-architectures",
    "domain": "AI 算力 / 半导体",
    "title": "Meet the modders porting ringfenced DLSS features to older GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/meet-the-modders-porting-ringfenced-dlss-features-to-older-gpus-how-dlss-5-and-multi-frame-generation-were-unlocked-for-older-architectures",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T15:30:00+00:00",
    "summary": "DLSS Multi-Frame Generation and DLSS 5 Neural Rendering can now run on hardware never intended for it, at least according to Nvidia. Now, two of the modders foundational to the release of these commun"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/xbox-cloud-gaming-is-now-available-on-jailbroken-ps5s-allows-upscaling-to-4k-using-the-ps5-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Developer uses Claude to enable Xbox Cloud Gaming on jailbroken PS5s",
    "url": "https://www.tomshardware.com/video-games/console-gaming/xbox-cloud-gaming-is-now-available-on-jailbroken-ps5s-allows-upscaling-to-4k-using-the-ps5-gpu",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T14:46:57+00:00",
    "summary": "RafaelNGP released a native Xbox Game Pass app allowing Xbox Cloud Gaming on the PS5, with support for 4 controllers and 4K upscaling on the PS5 GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-unveils-7nm-class-fdx-fusion-node-fd-soi-node-doubles-22fdx-transistor-density-comes-7-years-after-firm-abandoned-finfet",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries unveils 7nm-class FDX Fusion node — comes 7 years after firm abandoned FinFET",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-unveils-7nm-class-fdx-fusion-node-fd-soi-node-doubles-22fdx-transistor-density-comes-7-years-after-firm-abandoned-finfet",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T14:30:00+00:00",
    "summary": "GlobalFoundries returns to advanced FD-SOI development with 7nm-class FDX Fusion process — production planned for 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-to-phase-out-sgx-after-xeon-diamond-rapids-in-favor-of-tdx-confidential-computing-pivot-adds-trusted-i-o-and-post-quantum-crypto-for-agentic-ai",
    "domain": "AI 算力 / 半导体",
    "title": "Intel to phase out SGX after Xeon Diamond Rapids in favor of TDX",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-to-phase-out-sgx-after-xeon-diamond-rapids-in-favor-of-tdx-confidential-computing-pivot-adds-trusted-i-o-and-post-quantum-crypto-for-agentic-ai",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T14:00:00+00:00",
    "summary": "Intel set to discontinue SGX after Xeon 'Diamond Rapids' and focus on expanding TDX capabilities to meet emerging security requirements of cloud computing, enterprise workloads, and agentic AI."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/diamond-infused-watercooling-coldplates-for-2-300w-nvidia-rubin-drop-temps-by-up-to-22c-bespoke-frore-liquidjet-diamond-cooling-tames-770-w-cm2-hotspots",
    "domain": "AI 算力 / 半导体",
    "title": "Diamond-infused watercooling coldplates for 2,300W Nvidia Rubin drop temps by up to 22C",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/diamond-infused-watercooling-coldplates-for-2-300w-nvidia-rubin-drop-temps-by-up-to-22c-bespoke-frore-liquidjet-diamond-cooling-tames-770-w-cm2-hotspots",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T13:30:00+00:00",
    "summary": "A bespoke coldplate for custom designed AI servers: Frore's LiquidJet Diamond."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/gigabyte-go27q24g-27-inch-oled-240-hz-qhd-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte GO27Q24G 27-inch OLED 240 Hz QHD gaming monitor review: Tremendous bang for the buck",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/gigabyte-go27q24g-27-inch-oled-240-hz-qhd-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T13:15:00+00:00",
    "summary": "Gigabyte delivers extreme brightness and performance at a low price with its GO27Q24G. This 27-inch OLED panel boasts HDR peaks of 1,300 nits, wide gamut color, QHD resolution, 240 Hz and Adaptive-Syn"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-debuts-helion-reference-design-for-agentic-ai-servers-with-up-to-32-768-zen-6-venice-cores-rack-design-ships-next-year-in-cpu-only-and-all-in-one-configurations",
    "domain": "AI 算力 / 半导体",
    "title": "AMD debuts Helion reference design for agentic AI servers with up to 32,768 Zen 6 ‘Venice’ cores",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-debuts-helion-reference-design-for-agentic-ai-servers-with-up-to-32-768-zen-6-venice-cores-rack-design-ships-next-year-in-cpu-only-and-all-in-one-configurations",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T13:00:00+00:00",
    "summary": "At the OCP Global Summit, AMD revealed Helion, a rack-scale reference design for agentic AI that can house up to 32,768 Zen 6 CPU cores."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/trendforce-expects-declining-global-laptop-shipments-to-slow-manufacturing-exodus-from-china-rising-cpu-dram-and-ssd-costs-will-make-up-68-percent-of-mainstream-notebook-bom",
    "domain": "AI 算力 / 半导体",
    "title": "TrendForce expects declining global laptop shipments to slow manufacturing exodus from China",
    "url": "https://www.tomshardware.com/laptops/trendforce-expects-declining-global-laptop-shipments-to-slow-manufacturing-exodus-from-china-rising-cpu-dram-and-ssd-costs-will-make-up-68-percent-of-mainstream-notebook-bom",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T12:30:00+00:00",
    "summary": "Higher component costs could force laptop makers to raise retail prices or accept lower profit margins as consumer demand weakens in 2027."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/vibecoder-mods-minecraft-inside-gta-v-running-natively-on-an-iphone-unmodded-game-runs-at-50-60-fps-on-iphone-17",
    "domain": "AI 算力 / 半导体",
    "title": "Vibecoder mods Minecraft inside GTA V running natively on an iPhone",
    "url": "https://www.tomshardware.com/video-games/vibecoder-mods-minecraft-inside-gta-v-running-natively-on-an-iphone-unmodded-game-runs-at-50-60-fps-on-iphone-17",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T12:22:51+00:00",
    "summary": "C22's native port of GTA V on iOS/MacOS gets modded with Minecraft, and you can fly the Ender Dragon around."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/coder-creates-nvidiawatch-tracker-site-that-monitors-hundreds-of-gpu-driver-bugs-site-charts-open-issues-fixes-and-forum-feedback-across-updates",
    "domain": "AI 算力 / 半导体",
    "title": "Coder creates NvidiaWatch tracker site that monitors hundreds of GPU driver bugs",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/coder-creates-nvidiawatch-tracker-site-that-monitors-hundreds-of-gpu-driver-bugs-site-charts-open-issues-fixes-and-forum-feedback-across-updates",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T12:00:00+00:00",
    "summary": "independent-arg built this labor of love for the Nvidia community."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident",
    "domain": "AI 算力 / 半导体",
    "title": "'Unprecedented' Cyberattack cripples supermarket fridges across Europe as hackers activate automatic defrosting",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T11:32:54+00:00",
    "summary": "A cyberattack has hit supermarkets in Europe, disabling refrigerators."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/buyer-pays-usd350-for-broken-rtx-4090-project-only-to-find-realistic-fake-gpu-die-and-swapped-memory-russian-repair-specialist-reveals-sophisticated-new-cam-using-dummy-pcbs",
    "domain": "AI 算力 / 半导体",
    "title": "Buyer pays $350 for broken RTX 4090 project only to find realistic fake GPU die and swapped memory",
    "url": "https://www.tomshardware.com/pc-components/gpus/buyer-pays-usd350-for-broken-rtx-4090-project-only-to-find-realistic-fake-gpu-die-and-swapped-memory-russian-repair-specialist-reveals-sophisticated-new-cam-using-dummy-pcbs",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T11:30:00+00:00",
    "summary": "A customer paid approximately $350 for what appeared to be a repairable RTX 4090, only to receive a fake GPU with components that were painstakingly designed to resemble the real thing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-used-ai-agents-and-more-than-500-billion-tokens-to-rebuild-call-of-duty-modern-warfare-2s-source-code-83-percent-of-the-2009-shooters-functions-now-match-the-original-byte-for-byte",
    "domain": "AI 算力 / 半导体",
    "title": "Dev used AI agents and more than 500 billion tokens to rebuild Call of Duty: Modern Warfare 2's source code",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-used-ai-agents-and-more-than-500-billion-tokens-to-rebuild-call-of-duty-modern-warfare-2s-source-code-83-percent-of-the-2009-shooters-functions-now-match-the-original-byte-for-byte",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T11:00:00+00:00",
    "summary": "Maurice Heumann's Claude and Codex agents rebuilt Modern Warfare 2's source; 83% of functions match the original byte for byte."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/walmart-has-slashed-usd750-off-this-rtx-5060-gaming-laptop-now-40-percent-cheaper-hyperx-omen-15-is-just-usd1-149",
    "domain": "AI 算力 / 半导体",
    "title": "Walmart has slashed $750 off this RTX 5060 gaming laptop, now 40% cheaper",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/walmart-has-slashed-usd750-off-this-rtx-5060-gaming-laptop-now-40-percent-cheaper-hyperx-omen-15-is-just-usd1-149",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T10:37:37+00:00",
    "summary": "Save $750 on this HyperX Omen 15-inch laptop."
  },
  {
    "id": "rss:https://www.eetimes.com/security-becomes-a-sign-off-item/",
    "domain": "AI 算力 / 半导体",
    "title": "Security Becomes a Sign-off Item",
    "url": "https://www.eetimes.com/security-becomes-a-sign-off-item/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T07:10:22+00:00",
    "summary": "Europe’s CRA turns chip security into auditable sign-off, pushing silicon teams to prove resilience before 2027. The post Security Becomes a Sign-off Item appeared first on EE Times."
  },
  {
    "id": "hn:49930027",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon seeks to offload $8B of Nvidia chips to investors",
    "url": "https://www.ft.com/content/97d8d346-519e-48fb-8df8-66cf5f12ef62",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-10-02T05:09:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49937995",
    "domain": "AI 算力 / 半导体",
    "title": "CA tech executive arrested for allegedly smuggling $300M in Nvidia chips to CN",
    "url": "https://qz.com/greg-lui-earthmade-nvidia-ai-chips-smuggling-china-100226",
    "source": "littlexsparkee",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-10-02T20:07:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1705,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1258,
    "published_at": "2026-10-13T16:03:16+00:00",
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
    "points": 773,
    "published_at": "2026-10-04T19:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 618,
    "published_at": "2026-09-25T18:33:50+00:00",
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
    "id": "hn:50074869",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon for Robotics",
    "url": "https://developers.googleblog.com/gemini-4-argon-for-robotics/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 214,
    "published_at": "2026-10-13T16:55:47+00:00",
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
    "id": "hn:49697014",
    "domain": "大厂 AI 动态",
    "title": "Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama",
    "url": "https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/",
    "source": "0o_MrPatrick_o0",
    "platform": "hackernews",
    "points": 140,
    "published_at": "2026-09-14T13:59:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:50042149",
    "domain": "大厂 AI 动态",
    "title": "What driving across Europe costs in tolls, vignettes, bridges and fuel",
    "url": "https://copilot.travel/tolls/europe-2026",
    "source": "heikkikalliokos",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-10-11T11:39:10+00:00",
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
    "id": "rss:https://www.theverge.com/tech/1010561/apple-homeview-commercial-reaction",
    "domain": "大厂 AI 动态",
    "title": "Apple’s HomeView ad is confusing to everyone except parents",
    "url": "https://www.theverge.com/tech/1010561/apple-homeview-commercial-reaction",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T22:10:00+00:00",
    "summary": "Apple's ad introducing its new HomeView smart display is a little unusual. It's fast-paced and unruly, depicting a family of five as they rush through the morning routine. There's yelling and mess, mi"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1010642/openai-employee-arrested-recording-device",
    "domain": "大厂 AI 动态",
    "title": "OpenAI employee arrested for allegedly planting a bug in a conference room",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1010642/openai-employee-arrested-recording-device",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T20:45:25+00:00",
    "summary": "An OpenAI engineer was arrested after the company said it discovered a \"sophisticated recording device\" hidden in one of its offices. The employee was identified as Abdulrahman Alfozan, a 35-year-old "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1010619/apple-music-new-icon-ios-27-beta",
    "domain": "大厂 AI 动态",
    "title": "It looks like Apple Music is getting a new icon",
    "url": "https://www.theverge.com/tech/1010619/apple-music-new-icon-ios-27-beta",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T20:05:02+00:00",
    "summary": "Apple Music's iconic red app icon has reportedly been replaced with a black-and-white version in the latest iOS 27.2 beta, 9to5Mac reports. The eighth note on the icon also appears to have a slightly "
  },
  {
    "id": "rss:https://www.theverge.com/news/1010365/shopify-opens-its-catalog-up-to-more-ai-agents",
    "domain": "大厂 AI 动态",
    "title": "Shopify opens its catalog up to more AI agents",
    "url": "https://www.theverge.com/news/1010365/shopify-opens-its-catalog-up-to-more-ai-agents",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T19:42:42+00:00",
    "summary": "More AI agents will soon be able to browse and purchase from Shopify listings, marking an expansion of the company's agentic commerce ambitions. Shopify announced Tuesday it will let shoppers configur"
  },
  {
    "id": "rss:https://www.theverge.com/news/1010406/xbox-labs-game-decompiling-emulation-exploration",
    "domain": "大厂 AI 动态",
    "title": "Xbox is officially embracing the chaos of AI-powered game ports",
    "url": "https://www.theverge.com/news/1010406/xbox-labs-game-decompiling-emulation-exploration",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T19:00:48+00:00",
    "summary": "Retro gaming is going through a wild time at the moment, thanks to decompilations and recompilations that are letting gamers port classic titles to new devices, or merge code from two different games "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1010384/nothing-headphone-a-charli-xcx-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Nothing Headphone A are half off for the first time",
    "url": "https://www.theverge.com/gadgets/1010384/nothing-headphone-a-charli-xcx-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T18:33:14+00:00",
    "summary": "One of the best deals we’ve seen today bundles together a great pair of headphones with a solid album. When you add the Nothing Headphone A in black or white and the CD version of the Charli XCX album"
  },
  {
    "id": "rss:https://www.theverge.com/news/1010424/yandex-drone-strike-outage-disinformation-zelenskyy",
    "domain": "大厂 AI 动态",
    "title": "Russian bot farms are still trolling, even after Ukraine&#8217;s drone strikes on Yandex",
    "url": "https://www.theverge.com/news/1010424/yandex-drone-strike-outage-disinformation-zelenskyy",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T18:31:31+00:00",
    "summary": "Days after Ukrainian military drones took down several Russian data centers, President Volodymyr Zelenskyy claimed that the campaign had hurt Russia's disinformation efforts. \"It suddenly became a lit"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1010050/rivian-mind-robotics-hires-doug-field-ford-tesla-apple",
    "domain": "大厂 AI 动态",
    "title": "Rivian partner Mind Robotics hires Doug Field as president",
    "url": "https://www.theverge.com/transportation/1010050/rivian-mind-robotics-hires-doug-field-ford-tesla-apple",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T18:30:00+00:00",
    "summary": "Rivian CEO RJ Scaringe's startup Mind Robotics announced the appointment of Doug Field as president in a major coup for the CEO's secretive robotics project. Field was a VP of special projects at Appl"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1009128/ray-ban-meta-audio-glasses-review-smart-glasses-headphones-wearables",
    "domain": "大厂 AI 动态",
    "title": "I don’t miss the camera on the Ray-Ban Meta Audio glasses",
    "url": "https://www.theverge.com/tech/1009128/ray-ban-meta-audio-glasses-review-smart-glasses-headphones-wearables",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T18:00:00+00:00",
    "summary": "The other day I whizzed past several people while running in the park, my playlist blasting at full volume. The next morning, I smiled at a barista while ordering a caramel apple-flavored matcha latte"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1010364/tesla-robotaxi-school-zonespeeding-investigation",
    "domain": "大厂 AI 动态",
    "title": "The feds are looking into reports of Tesla’s robotaxis speeding through school zones",
    "url": "https://www.theverge.com/transportation/1010364/tesla-robotaxi-school-zonespeeding-investigation",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T17:40:15+00:00",
    "summary": "The National Highway Traffic Safety Administration says it's evaluating allegations that Tesla's 1,000 or so robotaxis using its automated driving system are exceeding \"posted speed limits in active s"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/justice-department-says-north-koreans-have-infiltrated-dozens-of-u-s-companies/",
    "domain": "大厂 AI 动态",
    "title": "Justice Department says North Koreans have infiltrated dozens of U.S. companies",
    "url": "https://techcrunch.com/2026/10/13/justice-department-says-north-koreans-have-infiltrated-dozens-of-u-s-companies/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T01:30:42+00:00",
    "summary": "U.S. authorities warn that sanctioned hackers are increasingly targeting Americans to act as facilitators between breached U.S. companies and Pyongyang."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/science-corporation-implants-its-vision-restoring-chip-in-its-first-stargardt-disease-patient/",
    "domain": "大厂 AI 动态",
    "title": "Science Corporation implants its vision-restoring chip in its first Stargardt disease patient",
    "url": "https://techcrunch.com/2026/10/13/science-corporation-implants-its-vision-restoring-chip-in-its-first-stargardt-disease-patient/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T23:13:31+00:00",
    "summary": "Max Hodak, the former president and co-founder of Neuralink, detailed onstage at TechCrunch Disrupt how his company's work with PRIMA is part of its path toward a novel brain-computer interface (BCI)."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/cerebras-ceo-says-were-nearing-a-future-where-everyone-has-a-personal-ai-assistant-at-home/",
    "domain": "大厂 AI 动态",
    "title": "Cerebras CEO says we’re nearing a future where everyone has a personal AI assistant at home",
    "url": "https://techcrunch.com/2026/10/13/cerebras-ceo-says-were-nearing-a-future-where-everyone-has-a-personal-ai-assistant-at-home/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T23:05:34+00:00",
    "summary": "Cerebras CEO Andrew Feldman predicts a future where personal AI assistants become as commonplace as household appliances, running partly on local devices and partly in the cloud."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/industrial-next-wants-factory-robots-to-switch-tasks-in-minutes-not-weeks/",
    "domain": "大厂 AI 动态",
    "title": "Industrial Next wants factory robots to switch tasks in minutes, not weeks",
    "url": "https://techcrunch.com/2026/10/13/industrial-next-wants-factory-robots-to-switch-tasks-in-minutes-not-weeks/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T23:00:00+00:00",
    "summary": "Industrial Next helps manufacturers automate complex, delicate tasks that have traditionally required human labor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/cerebras-ceo-pushes-back-on-ai-doomsday-warnings/",
    "domain": "大厂 AI 动态",
    "title": "Cerebras CEO pushes back on AI doomsday warnings",
    "url": "https://techcrunch.com/2026/10/13/cerebras-ceo-pushes-back-on-ai-doomsday-warnings/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T22:36:59+00:00",
    "summary": "Cerebras CEO Andrew Feldman has a message for AI leaders spreading doomsday warnings: Maybe stop talking? At TechCrunch Disrupt, he argued that the industry's focus on AI's risks is drowning out its p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/helix-carbon-makes-iron-cheaper-by-upcycling-blast-furnace-pollution-see-how-at-techcrunch-disrupt/",
    "domain": "大厂 AI 动态",
    "title": "Helix Carbon says it can make iron cheaper by recycling blast furnace pollution",
    "url": "https://techcrunch.com/2026/10/13/helix-carbon-makes-iron-cheaper-by-upcycling-blast-furnace-pollution-see-how-at-techcrunch-disrupt/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T21:15:00+00:00",
    "summary": "The steel industry is a big polluter, but Helix Carbon can upcycle pollution from blast furnaces to drive down emissions and improve margins."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/fbi-arrests-openai-employee-accused-of-planting-hidden-recording-device-in-conference-room/",
    "domain": "大厂 AI 动态",
    "title": "FBI arrests OpenAI employee accused of planting hidden recording device in conference room",
    "url": "https://techcrunch.com/2026/10/13/fbi-arrests-openai-employee-accused-of-planting-hidden-recording-device-in-conference-room/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T20:59:11+00:00",
    "summary": "It's not clear exactly for what purpose the recording device was used, but FBI director Kash Patel said the scheme was to \"capture sensitive communications about the company’s super intelligence techn"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/judge-orders-openai-to-turn-over-hiring-records-in-apple-trade-secrets-case/",
    "domain": "大厂 AI 动态",
    "title": "Judge orders OpenAI to turn over hiring records in Apple trade secrets case",
    "url": "https://techcrunch.com/2026/10/13/judge-orders-openai-to-turn-over-hiring-records-in-apple-trade-secrets-case/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T20:36:44+00:00",
    "summary": "A federal judge ruled that Apple can access OpenAI's interview materials involving former Apple employees, as well as private messages and testimony from key figures in the case."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/cambridge-heavy-industries-has-been-quietly-building-a-desktop-fusion-device/",
    "domain": "大厂 AI 动态",
    "title": "Cambridge Heavy Industries has been quietly building a desktop fusion device",
    "url": "https://techcrunch.com/2026/10/13/cambridge-heavy-industries-has-been-quietly-building-a-desktop-fusion-device/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T20:13:53+00:00",
    "summary": "Fusion power startup Cambridge Heavy Industries is building a small, laser-powered fusion device to fuel the coming wave of fusion power plants."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/licube-wants-to-be-the-fuel-provider-to-the-fusion-power-industry-see-how-at-techcrunch-disrupt/",
    "domain": "大厂 AI 动态",
    "title": "Licube wants to be the fuel provider to the fusion power industry — see how at TechCrunch Disrupt",
    "url": "https://techcrunch.com/2026/10/13/licube-wants-to-be-the-fuel-provider-to-the-fusion-power-industry-see-how-at-techcrunch-disrupt/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T20:00:00+00:00",
    "summary": "Fusion power plants will need a lot of lithium, and Licube is preparing to be a key supplier."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/niobia-takes-the-guesswork-out-of-some-of-techs-most-expensive-mistakes/",
    "domain": "大厂 AI 动态",
    "title": "Niobia takes the guesswork out of some of tech’s most expensive mistakes",
    "url": "https://techcrunch.com/2026/10/13/niobia-takes-the-guesswork-out-of-some-of-techs-most-expensive-mistakes/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T19:00:00+00:00",
    "summary": "The San Francisco startup aims to help battery and chip manufacturers identify defects on production lines, reducing downtime and costly mistakes."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/rivians-startup-mind-robotics-hires-former-ford-ev-chief-doug-field/",
    "domain": "大厂 AI 动态",
    "title": "Rivian’s startup Mind Robotics hires former Ford EV chief Doug Field",
    "url": "https://techcrunch.com/2026/10/13/rivians-startup-mind-robotics-hires-former-ford-ev-chief-doug-field/",
    "source": "Kirsten Korosec, Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T18:30:03+00:00",
    "summary": "Field also worked on Apple's secretive car project and oversaw development of the Tesla Model 3."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/flox-intelligence-is-building-ai-to-keep-wildlife-away-from-trains-airports-and-roads/",
    "domain": "大厂 AI 动态",
    "title": "Flox Intelligence is building AI to keep wildlife away from trains, airports, and roads",
    "url": "https://techcrunch.com/2026/10/13/flox-intelligence-is-building-ai-to-keep-wildlife-away-from-trains-airports-and-roads/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T18:30:00+00:00",
    "summary": "Flox's edge devices can identify animals and use species-specific sounds to drive them away from critical infrastructure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/facebook-is-giving-users-more-control-over-their-algorithm/",
    "domain": "大厂 AI 动态",
    "title": "Facebook is giving users more control over their algorithm",
    "url": "https://techcrunch.com/2026/10/13/facebook-is-giving-users-more-control-over-their-algorithm/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T18:05:24+00:00",
    "summary": "Meta announced the launch of its new AI-powered feature, “Your Algorithm,” a feature it first launched on Instagram."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/forget-rockets-longshot-wants-to-fire-cargo-into-space-from-a-gun-see-it-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Forget rockets — Longshot wants to fire cargo into space from a gun. See it at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/10/13/forget-rockets-longshot-wants-to-fire-cargo-into-space-from-a-gun-see-it-at-techcrunch-disrupt-2026/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T18:05:00+00:00",
    "summary": "Longshot is trying to build a gun big enough to make space data centers a reality."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/laplace-intelligence-red-teams-robots-and-self-driving-cars-before-they-hit-the-real-world/",
    "domain": "大厂 AI 动态",
    "title": "Laplace Intelligence red-teams robots and self-driving cars before they hit the real world",
    "url": "https://techcrunch.com/2026/10/13/laplace-intelligence-red-teams-robots-and-self-driving-cars-before-they-hit-the-real-world/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T17:30:00+00:00",
    "summary": "University of Michigan spinout Laplace Intelligence uses AI agents and interactive simulation to stress-test robots and self-driving vehicles before deployment. The profitable startup is competing in "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/pluto-security-raises-42m-as-ai-gives-enterprise-security-teams-a-new-headache/",
    "domain": "大厂 AI 动态",
    "title": "Pluto Security raises $42M as AI gives enterprise security teams a new headache",
    "url": "https://techcrunch.com/2026/10/13/pluto-security-raises-42m-as-ai-gives-enterprise-security-teams-a-new-headache/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T17:18:25+00:00",
    "summary": "The problem with giving everyone in a company access to AI tools is that people will use them in unexpected ways. And that fact is steadily seeding fears that companies now have new, gaping security h"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/mit-startup-says-it-can-turn-diesel-trucks-into-cheaper-hydrogen-haulers-see-it-at-disrupt/",
    "domain": "大厂 AI 动态",
    "title": "MIT startup says it can turn diesel trucks into cheaper hydrogen haulers — see it at Disrupt",
    "url": "https://techcrunch.com/2026/10/13/mit-startup-says-it-can-turn-diesel-trucks-into-cheaper-hydrogen-haulers-see-it-at-disrupt/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T17:00:00+00:00",
    "summary": "Diesel is expensive and polluting, and LNK Energies says it has come up with a way to replace it with hydrogen, all while undercutting diesel on cost."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/google-play-now-supports-private-vibe-coded-apps-built-just-for-you/",
    "domain": "大厂 AI 动态",
    "title": "Google Play now lets anyone build private, vibe-coded apps that run on Android",
    "url": "https://techcrunch.com/2026/10/13/google-play-now-supports-private-vibe-coded-apps-built-just-for-you/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T17:00:00+00:00",
    "summary": "Google is making it easier to build and use personal Android apps created with AI, without having to make them available to everyone on the Play Store."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/13/satlyt-founded-by-a-former-google-and-spacex-product-manager-raises-8m-to-run-ai-on-satellites/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX and Google both said no. Now his software is riding a SpaceX rocket next to Google’s",
    "url": "https://techcrunch.com/2026/10/13/satlyt-founded-by-a-former-google-and-spacex-product-manager-raises-8m-to-run-ai-on-satellites/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T16:30:00+00:00",
    "summary": "Satlyt wants to be the Android of orbital computing, offering open software that works on many companies' satellites, versus SpaceX's closed, all-in-one iPhone-style approach."
  },
  {
    "id": "rss:https://stratechery.com/2026/spacex-buys-more-spectrum-musk-and-market-structure-distributed-cellular/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX Buys More Spectrum, Musk and Market Structure, Distributed Cellular",
    "url": "https://stratechery.com/2026/spacex-buys-more-spectrum-musk-and-market-structure-distributed-cellular/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T10:00:00+00:00",
    "summary": "SpaceX's mobile strategy is becoming clearly with its latest spectrum purchase, and it might work."
  },
  {
    "id": "rss:https://stratechery.com/2026/personal-day-4/",
    "domain": "大厂 AI 动态",
    "title": "Personal Day",
    "url": "https://stratechery.com/2026/personal-day-4/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T10:00:00+00:00",
    "summary": "Personal Day — No Update"
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/martin-shkreli-livestreamed-himself-violating-lifetime-pharma-ban-ftc-says/",
    "domain": "大厂 AI 动态",
    "title": "Martin Shkreli livestreamed himself violating lifetime pharma ban, FTC says",
    "url": "https://arstechnica.com/health/2026/10/martin-shkreli-livestreamed-himself-violating-lifetime-pharma-ban-ftc-says/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T22:48:12+00:00",
    "summary": "\"I can always find a couple of biotech stocks to smoke,\" Shkreli said in a livestream."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/esa-targets-anbernic-emulation-handhelds-as-superfake-piracy-enablers/",
    "domain": "大厂 AI 动态",
    "title": "ESA targets Anbernic emulation handhelds as \"superfake\" piracy enablers",
    "url": "https://arstechnica.com/gaming/2026/10/esa-targets-anbernic-emulation-handhelds-as-superfake-piracy-enablers/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-13T21:55:49+00:00",
    "summary": "But third-party sellers, not Anbernic, are the ones routinely selling ROM-filled SD cards."
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
    "id": "hn:49886005",
    "domain": "股票",
    "title": "Anthropic's IPO prospectus shows AI vision, surging costs",
    "url": "https://www.reuters.com/business/finance/anthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-2026-09-28/",
    "source": "6thbit",
    "platform": "hackernews",
    "points": 145,
    "published_at": "2026-09-28T23:40:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50071744",
    "domain": "股票",
    "title": "Sprout Pi Mainboard – A modern, RP2350-powered motherboard for iPods",
    "url": "https://www.crowdsupply.com/certain-things/sprout-pi-mainboard",
    "source": "esskay",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-10-13T13:49:44+00:00",
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
    "id": "hn:50082283",
    "domain": "股票",
    "title": "US Says Chinese Hackers Attacked DOJ, NASA, Federal Reserve, Senate",
    "url": "https://www.usatoday.com/story/news/politics/2026/08/26/chinese-hackers-cyberattack-us-government/91473585007/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-14T04:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50029452",
    "domain": "股票",
    "title": "Data Center Darling Firmus's $30B IPO Dream Crushed in 48 Hours",
    "url": "https://www.bloomberg.com/news/articles/2026-10-09/data-center-darling-s-30-billion-ipo-dream-crushed-in-48-hours",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-10T04:04:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49997175",
    "domain": "股票",
    "title": "The world has nearly burned through its oil stockpile buffer",
    "url": "https://www.reuters.com/business/energy/world-has-nearly-burned-through-its-oil-stockpile-buffer-executives-say-2026-10-06/",
    "source": "geox",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-07T18:50:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50019535",
    "domain": "股票",
    "title": "Meadows – a small language for stock-and-flow diagrams that run",
    "url": "https://lorezzed.github.io/meadows/",
    "source": "jjsalamon",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-09T12:29:40+00:00",
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
    "id": "hn:50029232",
    "domain": "股票",
    "title": "Data centre company's much-hyped Australian stock market listing imploded",
    "url": "https://www.theguardian.com/australia-news/2026/oct/09/firmus-australian-stock-market-listing-bust-finance",
    "source": "stubish",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-10-10T03:23:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50008977",
    "domain": "股票",
    "title": "Frontier AI models outperform analysts on earnings prediction",
    "url": "https://samaya.ai/blog/frontier-ai-models-outperform-human-experts-on-earnings-prediction",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-10-08T17:33:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50020096",
    "domain": "股票",
    "title": "Ask HN: What if no AIpocalypse, no AI bubble, what if it just keeps advancing?",
    "url": "https://news.ycombinator.com/item?id=50020096",
    "source": "consumer451",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-10-09T13:18:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49796292",
    "domain": "股票",
    "title": "Smart Ring Maker Oura, Backers Seek $2.2B in US IPO",
    "url": "https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-09-22T02:53:48+00:00",
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
    "id": "hn:49948254",
    "domain": "金融",
    "title": "Federal judge calls Flock 'indiscriminate mass surveillance'",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 503,
    "published_at": "2026-10-03T22:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824686",
    "domain": "金融",
    "title": "Feds Target AI Critics as \"Foreign Agents\"",
    "url": "https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign",
    "source": "nmeagent",
    "platform": "hackernews",
    "points": 396,
    "published_at": "2026-09-24T00:41:31+00:00",
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
    "id": "hn:50059446",
    "domain": "金融",
    "title": "Feds got warrants to use fake cell towers to hunt down Don Lemon's producer",
    "url": "https://www.wired.com/story/feds-got-warrants-to-use-fake-cell-towers-to-hunt-down-don-lemons-producer/",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 192,
    "published_at": "2026-10-12T17:08:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 259,
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
    "id": "hn:50057956",
    "domain": "金融",
    "title": "French supermarkets suffer fridge shutdown after 'unprecedented' cyberattack",
    "url": "https://uk.finance.yahoo.com/news/french-supermarket-chains-cyberattack-forced-115141288.html",
    "source": "thinkcontext",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-10-12T15:36:21+00:00",
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
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 104,
    "published_at": "2026-10-13T23:13:23+00:00",
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
    "id": "hn:50049302",
    "domain": "金融",
    "title": "Governments are mishandling the affordability crisis",
    "url": "https://www.economist.com/finance-and-economics/2026/10/08/governments-are-mishandling-the-affordability-crisis",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-10-11T23:40:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49981063",
    "domain": "金融",
    "title": "Former German spy chief arrested for attempted treason",
    "url": "https://www.reuters.com/business/finance/former-german-spy-chief-detained-suspicion-espionage-treason-bild-reports-2026-10-06/",
    "source": "semiquaver",
    "platform": "hackernews",
    "points": 130,
    "published_at": "2026-10-06T16:51:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-10-13T16:48:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-10-01T01:40:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50062076",
    "domain": "金融",
    "title": "\"Today we're laying off a large part of the Airtable team \"",
    "url": "https://twitter.com/fedesimio/status/2109713695165329511",
    "source": "tortilla",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-10-12T19:56:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50062376",
    "domain": "金融",
    "title": "Tesla Factory Plan Increase of Toxic Heavy Metal Emissions Near School",
    "url": "https://anonymous94538.substack.com/p/tesla-fremont-is-applying-to-spew",
    "source": "DeepLogin",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-12T20:16:50+00:00",
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
    "id": "hn:50023065",
    "domain": "金融",
    "title": "Tesla Rebrands Full Self-Driving as Tesla Assisted Driving in Europe",
    "url": "https://qz.com/tesla-full-self-driving-rebranding-europe-assisted-driving-100926",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-10-09T16:38:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-02T21:28:59+00:00",
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
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-16T18:05:30+00:00",
    "summary": ""
  }
]
```
