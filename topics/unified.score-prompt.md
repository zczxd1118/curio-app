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

- 今日日期：`2026-08-25`
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
  "date": "2026-08-25",
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
    "points": 1749165,
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
    "points": 1182050,
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
    "points": 1100745,
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
    "points": 877622,
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
    "points": 630194,
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
    "points": 588891,
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
    "points": 439754,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 272868,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 253066,
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
    "points": 246365,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 179806,
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
    "points": 179718,
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
    "points": 164189,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 164159,
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
    "points": 143645,
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
    "points": 98733,
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
    "points": 93354,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63590,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1c8NFzhEMi",
    "domain": "AI",
    "title": "一个CLI干掉所有MCP工具，省99%的token mcp2cli",
    "url": "http://www.bilibili.com/video/av116204349953548",
    "source": "探索未至之境",
    "platform": "bilibili",
    "points": 58876,
    "published_at": "2026-03-10T10:18:17+00:00",
    "summary": "深度解析GitHub热门项目mcp2cli——一个能把任何MCP服务器或OpenAPI规范变成命令行工具的Python项目。它用&quot;懒发现&quot;机制，把MCP协议的token浪费从数十万降到几千，节省高达99%。整个核心实现只有一个Python文件，却支持三种接入模式、OAuth认证和智能缓存。发布仅一天就获得372颗星，但社区也有激烈争议：CLI真的能取代MCP吗？准确率会不会受影"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54435,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 46817,
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
    "points": 41020,
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
    "points": 39162,
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
    "points": 34180,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "harness使用教程-",
    "platform": "bilibili",
    "points": 33451,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 31625,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV12xbz6fE3C",
    "domain": "AI",
    "title": "新神已至？70美刀DeepSeek额度？支持gpt5.6sol！commandcode是否可以击败opencode？",
    "url": "http://www.bilibili.com/video/av117113758947183",
    "source": "汇木岑",
    "platform": "bilibili",
    "points": 30319,
    "published_at": "2026-08-18T00:51:14+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30317,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1kRW3zmEv8",
    "domain": "AI",
    "title": "【即梦AI】即梦Agent杀疯了！8种玩法带你速通即梦Agent智能体模式，赶紧来学！",
    "url": "http://www.bilibili.com/video/av115229962798190",
    "source": "SD电商教程",
    "platform": "bilibili",
    "points": 30172,
    "published_at": "2025-09-19T08:17:20+00:00",
    "summary": "即梦手册、AI绘画资料、系统学习AIGC请戳：https://www.bilibili.com/read/cv41224312"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29664,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 25005,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22735,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21335,
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
    "points": 20080,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1uLXLYYEzc",
    "domain": "AI",
    "title": "这应该是目前B站讲得最清楚的Dify本地私有化落地方案 企业级工作流+Agent实现教程，存下吧，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av114183400063018",
    "source": "秃头说Java",
    "platform": "bilibili",
    "points": 11627,
    "published_at": "2025-03-18T12:40:43+00:00",
    "summary": "【视频配套籽料+问题解答请看”平论区置顶”自取哦】\n视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
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
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 9895,
    "published_at": "2026-06-28T09:05:03+00:00",
    "summary": "企鹅交流群：1038830654"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8811,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1Dp846TE9i",
    "domain": "AI",
    "title": "2026年B站最细最全的AI Agent开发教程，大模型零基础入门到进阶，一套全解决！Agent、Harness、Skill全讲透!大模型面试必备！",
    "url": "http://www.bilibili.com/video/av117143807006108",
    "source": "ai大模型应用开发实战",
    "platform": "bilibili",
    "points": 8348,
    "published_at": "2026-08-23T08:18:02+00:00",
    "summary": "🎁本期配套资料包合集！包含最大模型新学习路线、实战案例、笔记源码、专业电子书、面试题库以及职业规划指南，需要的小伙伴评自取→https://www.bilibili.com/read/cv43357766/?jump_opus=1"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 7496,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
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
    "points": 6911,
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
    "points": 6698,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 6631,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1vWg36QEqC",
    "domain": "AI",
    "title": "大神们都知道Cursor省钱攻略，8月Cursor官方2.5折订阅教程分享给大家，支持最新Grok 4.6 模型，全功能全模型！",
    "url": "http://www.bilibili.com/video/av117097334049761",
    "source": "dfgvvgkg",
    "platform": "bilibili",
    "points": 6548,
    "published_at": "2026-08-15T03:15:57+00:00",
    "summary": "按照我们整理的实操方案，即可直接享受官方Pro版账单的2.5折结算——官方扣费1美元，您这边只需付0.25美元。换算到常用月付套餐，原价20美元/月的Pro，现在仅需36.5元人民币（对比官方146元）。所有扣款明细都可在官网后台实时查验，技术人做事讲究透明，绝无隐形费用。\n功能层面保持完整，无任何裁剪。账号属官方正版Pro会员，所有模型均为满血调用，模式切换毫无限制，响应逻辑始终稳定在线。我们团"
  },
  {
    "id": "bvid:BV1ebTi6yE7p",
    "domain": "AI",
    "title": "llama.cpp添加网络搜索等MCP工具 本地大模型摆脱过时数据束缚 实时获取最新数据 本地部署网络搜索MCP llama.cpp启动器添加了MCP代理选项",
    "url": "http://www.bilibili.com/video/av116845491329271",
    "source": "hsxbxq",
    "platform": "bilibili",
    "points": 6301,
    "published_at": "2026-07-01T15:49:48+00:00",
    "summary": "llama.cpp也可以添加网络搜索等MCP工具了，自此本地大模型终于可以简单的摆脱过时数据的束缚，实时获取最新数据了，相当于极简版的openclaw或Hermes了。 本期视频介绍了llama.cpp服务器图形化启动器1.4版添加了MCP代理选项，以及如何本地部署网络搜索MCP和添加百度搜索MCP方法。\nopen-webSearch介绍：https://github.com/Aas-ee/ope"
  },
  {
    "id": "bvid:BV1Tz8g6HErC",
    "domain": "AI",
    "title": "【全748集】B站最全最细的AI Agent零基础入门教程，2026最新版，教学通俗易懂，小白适用！普通人也能抓住的AI风口！手把手教会你agent智能体搭建~",
    "url": "http://www.bilibili.com/video/av117115201789701",
    "source": "AI全栈开发",
    "platform": "bilibili",
    "points": 5978,
    "published_at": "2026-08-18T11:27:05+00:00",
    "summary": "【2026最新版AI Agent智能体零基础全套教程 | 配套源码+学习路线+项目案例，看置顶评论自取】\n本套教程专为零基础设计，从Agent原理到独立打造智能体，手把手带你系统掌握AI Agent智能体搭建。\n✅ Agent基础：什么是Agent、三大核心能力（规划/工具/记忆）\n✅ 主流框架：Langchain、LangGraph主流框架\n✅ 多Agent协作：A2A协议、任务编排与调度\n✅ "
  },
  {
    "id": "bvid:BV1Nhba6VESD",
    "domain": "AI",
    "title": "2026最新AI工程化编程课程｜ClaudeCode/Codex Vibe Coding大厂企业级落地实战，程序员进阶AI高效开发必看！",
    "url": "http://www.bilibili.com/video/av117109782744406",
    "source": "图灵程序员诸葛",
    "platform": "bilibili",
    "points": 5860,
    "published_at": "2026-08-17T08:02:31+00:00",
    "summary": "视频配套资料含大模型最新学习路线、实战案例、笔记源码、专业电子书、面试题库及职业规划指南撮这里领取https://www.bilibili.com/read/cv50258483/?jump_opus=1"
  },
  {
    "id": "bvid:BV13cmnBFEP9",
    "domain": "AI",
    "title": "Claude Code教程9：Claude Code与GitHub的高效联动",
    "url": "http://www.bilibili.com/video/av115689541077475",
    "source": "木乐乐的异想世界",
    "platform": "bilibili",
    "points": 5469,
    "published_at": "2025-12-09T12:17:23+00:00",
    "summary": "【Claude Code教程第9集中文翻译】Net Ninja带你解锁Claude Code与GitHub的高效联动！本集聚焦实用核心功能：无需复杂配置，在Claude聊天会话中即可设置GitHub集成——安装后自动创建两个关键GitHub Action：①自动审查拉取请求（PR）并给出精准反馈；②当仓库问题提及Claude时，自动在新功能分支处理该问题。注意：需先安装GitHub CLI（附官方"
  },
  {
    "id": "bvid:BV1jWcvzmEzc",
    "domain": "AI",
    "title": "Houdini干货|houdini自己的AI agent（agent工具推荐分享）",
    "url": "http://www.bilibili.com/video/av116057012505638",
    "source": "tinywang_",
    "platform": "bilibili",
    "points": 5200,
    "published_at": "2026-02-12T09:45:41+00:00",
    "summary": "原作者教程：https://www.bilibili.com/video/BV1pwcbzBEEh/?spm_id_from=333.1387.list.card_archive.click&amp;vd_source=da5aa377b2acefadd001ffd4902eca9b\n\nGithub download：https://github.com/Kazama-Suichiku/Houdi"
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
    "id": "rss:https://www.eetimes.com/nxp-expands-industrial-endpoint-access-with-mcu-topology-discovery/",
    "domain": "AI 算力 / 半导体",
    "title": "NXP Expands Industrial Endpoint Access with MCU Topology Discovery",
    "url": "https://www.eetimes.com/nxp-expands-industrial-endpoint-access-with-mcu-topology-discovery/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:00:00+00:00",
    "summary": "NXP’s MCX A5 identifies and maps connected devices to improve network visibility, turning endpoints into accessible sources of real-time data for analytics, automation, and industrial edge AI. The pos"
  },
  {
    "id": "rss:https://www.eetimes.com/radiation-tolerance-of-tantalum-polymer-capacitors/",
    "domain": "AI 算力 / 半导体",
    "title": "Radiation Tolerance of Tantalum Polymer Capacitors",
    "url": "https://www.eetimes.com/radiation-tolerance-of-tantalum-polymer-capacitors/",
    "source": "Krystof Adamek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T14:00:00+00:00",
    "summary": "Environments rich in ionizing radiation create a particularly difficult functional challenge for electronic components. Spacecraft, nuclear reactors, particle accelerators, and hardened military equip"
  },
  {
    "id": "rss:https://www.eetimes.com/welcome-to-the-era-of-trustworthy-ai-for-ic-signoff-and-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "Welcome to the Era of Trustworthy AI for IC Signoff and Manufacturing",
    "url": "https://www.eetimes.com/welcome-to-the-era-of-trustworthy-ai-for-ic-signoff-and-manufacturing/",
    "source": "Juan Rey, Senior Vice President, General Manager and CTO of the Calibre segment, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:00:00+00:00",
    "summary": "Trust is the key to AI adoption in chip design. See how deterministic EDA engines and explainable AI can accelerate signoff and manufacturing. The post Welcome to the Era of Trustworthy AI for IC Sign"
  },
  {
    "id": "rss:https://www.eetimes.com/hp1800-the-magic-of-single-stage-48v-to-ultra-low-voltage/",
    "domain": "AI 算力 / 半导体",
    "title": "HP1800: The Magic of Single-Stage 48V to Ultra-Low Voltage",
    "url": "https://www.eetimes.com/hp1800-the-magic-of-single-stage-48v-to-ultra-low-voltage/",
    "source": "Hynetek Semiconductor Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:00:00+00:00",
    "summary": "HP1800 PWM phase-doubler turns 1 tri-state PWM input to four 180° interleaved complementary outputs. It enables 90–92% efficient single-stage 48V-to-1V AI PoL conversion (vs ~86% two-stage), cutting P"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-inference-pivot-reaches-rebellions-in-korea/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Inference Pivot Reaches Rebellions in Korea",
    "url": "https://www.eetimes.com/nvidia-inference-pivot-reaches-rebellions-in-korea/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T08:07:18+00:00",
    "summary": "Nvidia is reportedly in talks with Korean inference upstart Rebellions about a technical partnership, investment, or acquisition. The post Nvidia’s Inference Pivot Reaches Rebellions in Korea appeared"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-comes-with-up-to-256-p-cores-1-28-gb-of-last-level-cache-next-gen-18a-p-cpu-also-brings-avx-10-2-and-uses-ucie-s-instead-of-emib",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: Intel Xeon 7 'Diamond Rapids' comes with up to 256 P-cores, 1.28 GB of last-level cache — next-gen 18A-P CPU also brings AVX 10.2 and uses UCIe-S instead of EMIB",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-comes-with-up-to-256-p-cores-1-28-gb-of-last-level-cache-next-gen-18a-p-cpu-also-brings-avx-10-2-and-uses-ucie-s-instead-of-emib",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T21:07:45+00:00",
    "summary": "Intel has pulled back the curtain on its next-gen Diamond Rapids Xeon CPUs, packing up to 256 P-cores and 1.28 TB of last-level cache."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: SK hynix pushes hybrid bonding to HBM5 as AI memory hits 775-micron ceiling — firm extends MR-MUF through Nvidia Rubin",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:55:45+00:00",
    "summary": "The problem, per SK, is that HBM cubes are capped at a total thickness of 775 microns, the standard thickness of a 300mm logic wafer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores",
    "domain": "AI 算力 / 半导体",
    "title": "Hot Chips 2026: IBM's first dual-ISA core natively executes ARM and z/Architecture in the same core; all cores run at 5.7 GHz base frequency — next-gen mainframe AI processor is built on 2nm node with",
    "url": "https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:42:34+00:00",
    "summary": "IBM is vastly expanding softwarte support on its mainframes with its first dual-ISA CPU core that natively supports z/Architecture and ARM instructions."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/lgs-native-1-000-hz-1080p-gaming-monitor-has-a-matching-usd1-000-price-tag-preorders-open-for-the-25-inch-ultragear-25g590b",
    "domain": "AI 算力 / 半导体",
    "title": "LG's native 1,000 Hz 1080p gaming monitor has a matching $1,000 price tag — preorders open for the 25-inch UltraGear 25G590B",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/lgs-native-1-000-hz-1080p-gaming-monitor-has-a-matching-usd1-000-price-tag-preorders-open-for-the-25-inch-ultragear-25g590b",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:21:51+00:00",
    "summary": "The UltraGear 25G590B is the first 1,000 Hz gaming monitor with a native 1080p resolution"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/cooler-master-q300l-v3-microatx-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master Q300L v3 MicroATX case review: Sub-$45 MSRP offers incredible value for MicroATX chassis with included fans",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/cooler-master-q300l-v3-microatx-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:07:15+00:00",
    "summary": "Cooler Master’s Q300L V3 offers more airflow, bigger clearances, and a 20 Gbps USB-C for under $45"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-6000-ram-now-costs-usd400-the-latest-price-hike-puts-diy-pc-building-further-out-of-reach-than-ever-before",
    "domain": "AI 算力 / 半导体",
    "title": "32GB of DDR5 6000 RAM now costs $400 — the latest price hike puts DIY PC building further out of reach than ever before",
    "url": "https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-6000-ram-now-costs-usd400-the-latest-price-hike-puts-diy-pc-building-further-out-of-reach-than-ever-before",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T15:30:42+00:00",
    "summary": "32GB of DDR5 6000 RAM now costs more than $400."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nine-indicted-by-taiwan-over-illegal-export-of-nvidia-b300-gpus-to-china-details-reveal-five-point-strategy-to-exploit-and-avoid-customs-controls",
    "domain": "AI 算力 / 半导体",
    "title": "Nine indicted by Taiwan over illegal export of Nvidia B300 GPUs to China — details reveal five-point strategy to exploit and avoid customs controls",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nine-indicted-by-taiwan-over-illegal-export-of-nvidia-b300-gpus-to-china-details-reveal-five-point-strategy-to-exploit-and-avoid-customs-controls",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T15:09:55+00:00",
    "summary": "A new report claims nine people have been indicted over the illegal smuggling of Nvidia B300 servers to China."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/two-intel-chips-break-amazons-top-10-cpus-for-the-first-time-in-months-core-ultra-7-270k-and-core-i7-14700k-finally-challenge-amd-desktop-dominance",
    "domain": "AI 算力 / 半导体",
    "title": "Two Intel chips break Amazon's top 10 CPUs for the first time in months — Core Ultra 7 270K and Core i7-14700K finally challenge AMD desktop dominance",
    "url": "https://www.tomshardware.com/pc-components/cpus/two-intel-chips-break-amazons-top-10-cpus-for-the-first-time-in-months-core-ultra-7-270k-and-core-i7-14700k-finally-challenge-amd-desktop-dominance",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T14:11:31+00:00",
    "summary": "AMD has dominated the DIY space so thoroughly over the last few years that an Intel chip appearing in the top 10 at all is notable, but it's not really that surprising if you look at the details."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/marvell-sells-cxl-memory-recycling-into-the-worst-dram-shortage-in-years",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell VP pushes for DDR4 recycling for use in CXL memory, amid the worst DRAM shortage in years — company introduces three-tier AI memory infrastructure",
    "url": "https://www.tomshardware.com/pc-components/dram/marvell-sells-cxl-memory-recycling-into-the-worst-dram-shortage-in-years",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:11:37+00:00",
    "summary": "Marvell has introduced a three-tier \"AI memory infrastructure\" portfolio, announced at FMS 2026 in Santa Clara on August 4."
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/asus-rog-gjallar-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Gjallar Review: It looks better than it sounds",
    "url": "https://www.tomshardware.com/speakers/asus-rog-gjallar-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:00:00+00:00",
    "summary": "Asus' first-ever gaming soundbar, the ROG Gjallar, is blocky and uninspired, with decent sound and a completely unnecessary audio control hub with built-in beamforming mics."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/researcgers-find-a-drake-passage-cable-to-antarctica-is-buildable",
    "domain": "AI 算力 / 半导体",
    "title": "Undersea cable to Antarctica through Drake Passage is viable, researchers find — 1,600km route to Chile could spell an end to research data leaving in 'suitcases full of hard drives'",
    "url": "https://www.tomshardware.com/networking/researcgers-find-a-drake-passage-cable-to-antarctica-is-buildable",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T12:03:28+00:00",
    "summary": "Antarctic research data still leaves the continent physically, on hard drives ferried out by ship and plane \"in suitcases full of hard drives.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/asus-zenscreen-oled-mq16fc-portable-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ZenScreen OLED (MQ16FC) portable monitor review: A great all-around performer",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/asus-zenscreen-oled-mq16fc-portable-monitor-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T11:05:00+00:00",
    "summary": "The Asus ZenScreen OLED (MQ16FC) excels on several fronts, including pricing."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/valve-was-founded-30-years-ago-today-changed-pc-gaming-forever-with-half-life-then-steam",
    "domain": "AI 算力 / 半导体",
    "title": "Valve was founded 30 years ago today — changed PC gaming forever with Half-Life, then Steam",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/valve-was-founded-30-years-ago-today-changed-pc-gaming-forever-with-half-life-then-steam",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T10:31:08+00:00",
    "summary": "Today marks Valve’s 30th birthday. The company was founded on August 24, 1996, by Gabe Newell and Mike Harrington, both Microsoft veterans."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/kyoto-university-demonstrates-a-sic-transistor-that-runs-at-600c-using-standard-ion-implantation",
    "domain": "AI 算力 / 半导体",
    "title": "Kyoto University builds transistor that survives 600C temperatures, compatible with standard fabs — Standard ion implantation and bottom-gate design fix leakage and voltage drift",
    "url": "https://www.tomshardware.com/tech-industry/kyoto-university-demonstrates-a-sic-transistor-that-runs-at-600c-using-standard-ion-implantation",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T10:30:00+00:00",
    "summary": "A research team at Kyoto University has built a silicon carbide transistor that operates at 600°C (873 K) using ion implantation."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/huge-usd2-200-discount-makes-this-rtx-5090-gaming-pc-cheaper-than-the-gpus-standalone-price-epic-hp-omen-max-45l-rig-ships-with-64gb-ddr5-and-a-2tb-ssd-for-just-usd4-799",
    "domain": "AI 算力 / 半导体",
    "title": "Huge $2,200 discount makes this RTX 5090 gaming PC cheaper than the GPU's standalone price — epic HP Omen Max 45L rig ships with 64GB DDR5 and a 2TB SSD for just $4,799",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/huge-usd2-200-discount-makes-this-rtx-5090-gaming-pc-cheaper-than-the-gpus-standalone-price-epic-hp-omen-max-45l-rig-ships-with-64gb-ddr5-and-a-2tb-ssd-for-just-usd4-799",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T10:11:23+00:00",
    "summary": "A massive discount means this $4,799 HP Omen Max 45L gaming PC is now cheaper than individually buying the RTX 5090 it uses, thanks to a $2,200 discount."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bring-your-ideas-to-life-with-epic-savings-on-flashforge-3d-printers-flashforge-joins-the-aliexpress-828-mega-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Bring your ideas to life with epic savings on Flashforge 3D printers — Flashforge joins the AliExpress 828 mega-sale",
    "url": "https://www.tomshardware.com/3d-printing/bring-your-ideas-to-life-with-epic-savings-on-flashforge-3d-printers-flashforge-joins-the-aliexpress-828-mega-sale",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T10:05:00+00:00",
    "summary": "AliExpress 828 sale brings unbeatable savings on Flashforge 3D printers and premium accessories."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-takes-down-over-400-github-repositories-for-switch-emulators-in-one-go-relentless-dmca-strikes-tied-to-piracy-concerns-over-illegal-cryptographic-keys",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo takes down over 400 GitHub repositories for Switch emulators in one go — Relentless DMCA strikes tied to piracy concerns over illegal cryptographic keys",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-takes-down-over-400-github-repositories-for-switch-emulators-in-one-go-relentless-dmca-strikes-tied-to-piracy-concerns-over-illegal-cryptographic-keys",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T10:00:00+00:00",
    "summary": "Nintendo is doing Nintendo things again as it goes after 7 different master repos containing Switch emulators, which total out to 401 repos wiped in a single day. Most of these belonged to Yuzu forks,"
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
    "id": "rss:https://www.theverge.com/games/983457/lenovo-bad-legion-go-bios-update-bricked",
    "domain": "大厂 AI 动态",
    "title": "Lenovo confirms Legion Go issues after gamers report bricked devices",
    "url": "https://www.theverge.com/games/983457/lenovo-bad-legion-go-bios-update-bricked",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T23:38:10+00:00",
    "summary": "When a company's software update turns your computer into a useless brick, should fixes be free? Framework, the modular computer startup, apparently thinks so. But it's not clear that computing giant "
  },
  {
    "id": "rss:https://www.theverge.com/tech/983244/3d-printed-guns-hashes-hochul",
    "domain": "大厂 AI 动态",
    "title": "The cat-and-mouse game over 3D-printed guns has begun",
    "url": "https://www.theverge.com/tech/983244/3d-printed-guns-hashes-hochul",
    "source": "Mack DeGeurin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T19:50:00+00:00",
    "summary": "The creator of the world's first 3D-printed gun claims he's developed a way to thwart government-mandated software meant to block 3D printers from making firearms. It's an opening volley in what's sha"
  },
  {
    "id": "rss:https://www.theverge.com/policy/983864/zillow-redfin-ftc-settlement",
    "domain": "大厂 AI 动态",
    "title": "Zillow and Redfin settle FTC antitrust case over their rental listings partnership",
    "url": "https://www.theverge.com/policy/983864/zillow-redfin-ftc-settlement",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T17:01:05+00:00",
    "summary": "The FTC and Zillow have announced a settlement that ends the case alleging that a 2025 \"partnership\" between Zillow and Redfin violated antitrust laws. The FTC had alleged Zillow agreed to pay Redfin "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/983765/robotaxi-waymo-zoox-tesla-rules-pushback-nhtsa",
    "domain": "大厂 AI 动态",
    "title": "Robotaxis are real now — so is the pushback",
    "url": "https://www.theverge.com/transportation/983765/robotaxi-waymo-zoox-tesla-rules-pushback-nhtsa",
    "source": "Rani Molla",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T16:42:37+00:00",
    "summary": "Robotaxis are expanding. So is the fight over the rules governing them. In New York, Gov. Kathy Hochul withdrew a proposal earlier this year that would have opened the door to driverless robotaxis out"
  },
  {
    "id": "rss:https://www.theverge.com/games/983822/the-witcher-4-release-window-gamescom",
    "domain": "大厂 AI 动态",
    "title": "The Witcher 4 developers target a 2028 release",
    "url": "https://www.theverge.com/games/983822/the-witcher-4-release-window-gamescom",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T15:48:53+00:00",
    "summary": "CD Projekt Red is aiming to launch The Witcher 4 sometime in 2028, joint CEO Micha&#322; Nowakowski says in a new video. CD Projekt Red has been working on its next mainline Witcher title for years an"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/983794/espn-disney-plus-bundles-price-increase",
    "domain": "大厂 AI 动态",
    "title": "ESPN streaming plans are getting more expensive",
    "url": "https://www.theverge.com/streaming/983794/espn-disney-plus-bundles-price-increase",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T15:06:24+00:00",
    "summary": "ESPN is hiking the price of its subscription on September 17th, a change that will also impact its bundles with Disney Plus. In a support page spotted earlier by Sports Media Watch, ESPN says its ad-s"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983786/raspberry-pi-cyberdeck-tutorial-price-increases",
    "domain": "大厂 AI 动态",
    "title": "Raspberry Pi shares its official tutorial for making a cyberdeck",
    "url": "https://www.theverge.com/tech/983786/raspberry-pi-cyberdeck-tutorial-price-increases",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T14:49:44+00:00",
    "summary": "Raspberry Pi's head of social, Ashley Whittaker, acknowledged the cyberdeck trend today, saying \"we haven't been able to get away from cyberdecks this year.\" Tiny portable computers made out of things"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/983726/apple-airtags-second-gen-four-pack-elgato-stream-deck-switch-2-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Apple’s four-pack of second-gen AirTags is $20 off",
    "url": "https://www.theverge.com/gadgets/983726/apple-airtags-second-gen-four-pack-elgato-stream-deck-switch-2-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T14:04:04+00:00",
    "summary": "Apple’s four-pack of second-generation AirTags is down to $79 (originally $99) at Amazon and at Target, which is the bundle’s lowest price yet. You can get an AirTag for $24 right now piecemeal, but g"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/982901/gofundme-ceo-tim-cadogan-fundraising-healthcare-medical-expenses",
    "domain": "大厂 AI 动态",
    "title": "How GoFundMe became America’s backup plan",
    "url": "https://www.theverge.com/podcast/982901/gofundme-ceo-tim-cadogan-fundraising-healthcare-medical-expenses",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T14:00:00+00:00",
    "summary": "Today on Decoder, I’m talking with Tim Cadogan, the CEO of GoFundMe. You know GoFundMe — it’s a major fundraising platform where you can donate to help people with everything from medical expenses to "
  },
  {
    "id": "rss:https://www.theverge.com/streaming/983741/netflix-open-app-peacock-fox-one",
    "domain": "大厂 AI 动态",
    "title": "Netflix reportedly considers opening its app to other streamers",
    "url": "https://www.theverge.com/streaming/983741/netflix-open-app-peacock-fox-one",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:47:14+00:00",
    "summary": "Netflix executives have considered making third-party streaming services available within its app, according to a report from The New York Times. The recent discussions reportedly centered around brin"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/indias-airbound-bags-37m-to-take-on-trucks-with-rocket-like-drones/",
    "domain": "大厂 AI 动态",
    "title": "India’s Airbound bags $37M to take on trucks with rocket-like drones",
    "url": "https://techcrunch.com/2026/08/24/indias-airbound-bags-37m-to-take-on-trucks-with-rocket-like-drones/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T03:30:00+00:00",
    "summary": "Airbound's ultra-lightweight approach to drone delivery has attracted backing from Greenoaks, DoorDash, and Silicon Valley investor Lachy Groom."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/situational-awareness-star-ai-hedge-fund-that-nearly-imploded-now-being-probed-by-the-sec/",
    "domain": "大厂 AI 动态",
    "title": "Situational Awareness, star AI hedge fund that nearly imploded, now being probed by the SEC",
    "url": "https://techcrunch.com/2026/08/24/situational-awareness-star-ai-hedge-fund-that-nearly-imploded-now-being-probed-by-the-sec/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T00:23:12+00:00",
    "summary": "The AI hedge fund went from \"the talk of Wall Street\" to \"subject of federal subpoenas\" faster than you can say \"diversify your portfolio.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/oura-is-reportedly-eyeing-a-september-ipo-that-could-value-it-at-more-than-16b/",
    "domain": "大厂 AI 动态",
    "title": "Oura is reportedly eyeing a September IPO that could value it at more than $16B",
    "url": "https://techcrunch.com/2026/08/24/oura-is-reportedly-eyeing-a-september-ipo-that-could-value-it-at-more-than-16b/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T23:05:44+00:00",
    "summary": "We all knew it was coming. The expected valuation may surprise, though."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/trump-bought-spacex-shares-two-weeks-after-blockbuster-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Trump bought SpaceX shares two weeks after blockbuster IPO",
    "url": "https://techcrunch.com/2026/08/24/trump-bought-spacex-shares-two-weeks-after-blockbuster-ipo/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T21:24:17+00:00",
    "summary": "The president bought when the stock was in the mid-$150 range. SpaceX finished trading on Monday back at its IPO price of $135."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/zillow-and-redfin-settle-ftc-antitrust-case/",
    "domain": "大厂 AI 动态",
    "title": "Zillow and Redfin settle FTC antitrust case",
    "url": "https://techcrunch.com/2026/08/24/zillow-and-redfin-settle-ftc-antitrust-case/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T20:45:33+00:00",
    "summary": "Zillow and Redfin reached a settlement with the FTC, which requires Redfin to reenter the rental advertising business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/showcase-your-startup-at-techcrunch-disrupt-2026-and-book-an-exhibit-table-while-theres-still-space/",
    "domain": "大厂 AI 动态",
    "title": "Showcase your startup at TechCrunch Disrupt 2026 and book an exhibit table while there’s still space",
    "url": "https://techcrunch.com/2026/08/24/showcase-your-startup-at-techcrunch-disrupt-2026-and-book-an-exhibit-table-while-theres-still-space/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T20:16:34+00:00",
    "summary": "Make the most of Disrupt's crowds of potential investors and partners by exhibiting your startup from October 13-15."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/alabama-launches-investigation-into-openais-hack-of-hugging-face/",
    "domain": "大厂 AI 动态",
    "title": "Alabama launches investigation into OpenAI’s hack of Hugging Face",
    "url": "https://techcrunch.com/2026/08/24/alabama-launches-investigation-into-openais-hack-of-hugging-face/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T19:58:17+00:00",
    "summary": "Weeks after OpenAI disclosed that one of its cybersecurity models had gone rogue and hacked AI dataset company Hugging Face, Alabama’s attorney general announced an investigation into the incident."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/amazon-hikes-hardware-prices-by-60-percent-blaming-memory-shortage/",
    "domain": "大厂 AI 动态",
    "title": "Amazon hikes hardware prices by 60%, blaming memory shortage",
    "url": "https://techcrunch.com/2026/08/24/amazon-hikes-hardware-prices-by-60-percent-blaming-memory-shortage/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T19:54:50+00:00",
    "summary": "As the memory shortage continues to cause trouble for hardware makers, Amazon says it is now being forced to pass on the costs to its consumers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/amjad-masad-ceo-and-co-founder-of-replit-joins-the-disrupt-stage-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Amjad Masad, CEO and co-founder of Replit, joins the Disrupt Stage at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/24/amjad-masad-ceo-and-co-founder-of-replit-joins-the-disrupt-stage-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T19:54:19+00:00",
    "summary": "At TechCrunch Disrupt 2026, Replit CEO Amjad Masad will share his perspective on the future of programming and Replit's role in developing it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/apply-now-to-host-a-side-event-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Apply now to host a Side Event at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/24/apply-now-to-host-a-side-event-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T19:44:13+00:00",
    "summary": "Apply before September 4 to be a part of the TechCrunch Disrupt community by hosting your own Side Event."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/instincts-powerful-ai-assistant-is-raising-privacy-and-security-concerns/",
    "domain": "大厂 AI 动态",
    "title": "Instinct’s powerful AI assistant is raising privacy and security concerns",
    "url": "https://techcrunch.com/2026/08/24/instincts-powerful-ai-assistant-is-raising-privacy-and-security-concerns/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T18:03:55+00:00",
    "summary": "Early testers are raving about what Instinct can do, but some say the AI assistant’s sweeping access, broad terms and ability to act on users’ behalf come with uncomfortable trade-offs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/valor-point72-back-general-intuition-at-6b-valuation-as-ai-startup-pushes-into-robotics/",
    "domain": "大厂 AI 动态",
    "title": "Valor, Point72 back General Intuition at $6B valuation as AI startup pushes into robotics",
    "url": "https://techcrunch.com/2026/08/24/valor-point72-back-general-intuition-at-6b-valuation-as-ai-startup-pushes-into-robotics/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T15:24:18+00:00",
    "summary": "General Intuition, the startup building a foundation model that trains generalized AI agents how to move through space and time, is in talks to raise at a $6 billion pre-money valuation from new inves"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is building AI agents for everything. Will everyone use them?",
    "url": "https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T15:00:00+00:00",
    "summary": "Inside the frontier lab’s push to bring AI agents from software engineers to the masses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/brake-problems-in-gm-evs-draw-greater-federal-scrutiny/",
    "domain": "大厂 AI 动态",
    "title": "Brake problems in GM EVs draw greater federal scrutiny",
    "url": "https://techcrunch.com/2026/08/24/brake-problems-in-gm-evs-draw-greater-federal-scrutiny/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T14:18:47+00:00",
    "summary": "In one crash, the driver of a 2024 Blazer EV said they had to \"deliberately steer the vehicle into a concrete curb\" to slow it down and avoid a \"catastrophic intersection collision.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/hugging-face-reportedly-in-talks-to-be-acquired-for-13b/",
    "domain": "大厂 AI 动态",
    "title": "Hugging Face reportedly in talks to be acquired for $13B",
    "url": "https://techcrunch.com/2026/08/24/hugging-face-reportedly-in-talks-to-be-acquired-for-13b/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:47:26+00:00",
    "summary": "Hugging Face has reportedly been fielding acquisition offers that would value the company at around $13B. But with the founders' feeling of responsibility to community, doubts arise as to whether a sa"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/24/us-nutrition-startup-berry-street-merges-with-indias-healthify-as-glp-1-trends-upwards/",
    "domain": "大厂 AI 动态",
    "title": "US nutrition startup Berry Street merges with India’s Healthify as GLP-1 trends upwards",
    "url": "https://techcrunch.com/2026/08/24/us-nutrition-startup-berry-street-merges-with-indias-healthify-as-glp-1-trends-upwards/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T13:45:15+00:00",
    "summary": "Berry Street founder Noah Kotlove and Healthify founder Tushar Vashisht will act as co-CEOs of the new entity."
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
    "summary": "The Dutch Data Protection Authority is fining Uber €825 million in the second-largest penalty issued under Europe’s GDPR."
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
    "id": "rss:https://stratechery.com/2026/autonomy-and-innovation/",
    "domain": "大厂 AI 动态",
    "title": "Autonomy and Innovation",
    "url": "https://stratechery.com/2026/autonomy-and-innovation/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T10:00:00+00:00",
    "summary": "Incentives favor offense when it comes to agentic cybersecurity; it's the same dynamic that will limit incumbents and fuel startups in the long run."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/ai-is-hitting-entry-level-jobs-hardest-stanford-study-finds/",
    "domain": "大厂 AI 动态",
    "title": "AI is hitting entry-level jobs hardest, Stanford study finds",
    "url": "https://arstechnica.com/ai/2026/08/ai-is-hitting-entry-level-jobs-hardest-stanford-study-finds/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T21:45:53+00:00",
    "summary": "Young employment in AI-impacted fields down 19% compared to more AI-resistant occupations."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/energy-hungry-ai-data-centers-spur-new-power-transformer-technology/",
    "domain": "大厂 AI 动态",
    "title": "Data centers become \"killer application\" for new power transformer tech",
    "url": "https://arstechnica.com/gadgets/2026/08/energy-hungry-ai-data-centers-spur-new-power-transformer-technology/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T21:32:16+00:00",
    "summary": "Solid-state transformers could also benefit EV charging and someday households."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/rfk-jr-may-upend-how-vaccine-recommendations-are-categorized/",
    "domain": "大厂 AI 动态",
    "title": "RFK Jr. may upend how vaccine recommendations are categorized",
    "url": "https://arstechnica.com/health/2026/08/rfk-jr-may-upend-how-vaccine-recommendations-are-categorized/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T21:04:48+00:00",
    "summary": "There are currently 3 categories. Without reason, RFK Jr. is considering changes."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/ads-and-tracking-infiltrated-tvs-now-theyre-coming-for-monitors/",
    "domain": "大厂 AI 动态",
    "title": "Ads and tracking infiltrated TVs. Now they're coming for monitors.",
    "url": "https://arstechnica.com/gadgets/2026/08/ads-and-tracking-infiltrated-tvs-now-theyre-coming-for-monitors/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T20:17:41+00:00",
    "summary": "Monitor vendors are playing with fire."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/feds-deepen-probe-into-general-motors-brake-failures/",
    "domain": "大厂 AI 动态",
    "title": "GM vehicles under federal scrutiny after hundreds of reports",
    "url": "https://arstechnica.com/cars/2026/08/feds-deepen-probe-into-general-motors-brake-failures/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T19:42:50+00:00",
    "summary": "The eBoost brake-by-wire system is responsible for at least 22 crashes now."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/aliexpress-caught-fingerprinting-visitors-after-sending-inaudible-sounds-to-browsers/",
    "domain": "大厂 AI 动态",
    "title": "Inaudible sounds used to fingerprint browsers catch AliExpress red-handed",
    "url": "https://arstechnica.com/security/2026/08/aliexpress-caught-fingerprinting-visitors-after-sending-inaudible-sounds-to-browsers/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T19:19:21+00:00",
    "summary": "Is the technique outdated? Yes. Is it still creepy? Also yes."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/modern-trade-of-mummified-remains-may-carry-its-own-mummys-curse/",
    "domain": "大厂 AI 动态",
    "title": "Buyer beware: Those mummified remains might carry toxic spores",
    "url": "https://arstechnica.com/science/2026/08/modern-trade-of-mummified-remains-may-carry-its-own-mummys-curse/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-24T16:59:07+00:00",
    "summary": "\"Mummified remains sold online exhibit signs of biodeterioration, yet sellers provide no safety guidance.\""
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
    "id": "wscn:3780216",
    "domain": "股票",
    "title": "字节加入企业办公Agent大战：发布“豆包工作”",
    "url": "https://wallstreetcn.com/articles/3780216",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T03:00:20+00:00",
    "summary": "Agent争夺战进入“四国杀”，腾讯、阿里、百度之后字节正式登场。字节推出“豆包工作”，支持文档、PPT、视频、应用等多类型内容生成与编辑，并可在授权后直接操控电脑和浏览器跨软件完成任务。最大差异点在于与飞书深度打通。"
  },
  {
    "id": "wscn:3780197",
    "domain": "股票",
    "title": "三星、SK海力士加码中国NAND产能，西安、大连工厂投资明年前陆续落地",
    "url": "https://wallstreetcn.com/articles/3780197",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T02:46:52+00:00",
    "summary": "AI服务器需求爆发，韩国存储双雄加速押注中国产线。三星电子将西安工厂升级为280层V9 NAND量产基地，月产能剑指5万片，补充投资订单年底落地；SK海力士同步在大连第二工厂提速扩产，目标月产3万片。"
  },
  {
    "id": "wscn:3780212",
    "domain": "股票",
    "title": "Citadel：算力稀缺仍是AI最大瓶颈，超大规模云厂商或成最终赢家",
    "url": "https://wallstreetcn.com/articles/3780212",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T02:46:44+00:00",
    "summary": "Citadel Securities最新分析揭示AI竞争逻辑：决定胜负的不是模型能力，而是\"已通电、随时可用的算力\"。电网接入与审批周期动辄以年计，算力缺口短期无解；AI智能体的兴起更使单任务算力消耗倍增，需求持续碾压供给。谁掌握物理算力基础设施，谁就同时收割前沿模型与廉价执行层的双重红利——超大规模云厂商，或是这场军备竞赛中风险收益比最确定的赢家。"
  },
  {
    "id": "wscn:3780211",
    "domain": "股票",
    "title": "创业板早盘一度跌2%，半导体产业链集体下挫，农业股拉升，恒科指承压，新能源汽车股调整、小鹏跌超7%",
    "url": "https://wallstreetcn.com/articles/3780211",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T02:32:17+00:00",
    "summary": "早盘农业板块再度走强，金健米业7天5板，登海种业、万向德农6天3板，秋乐种业、康农种业、京粮控股、神农种业跟涨。早盘化工板块异动拉升，六国化工、金煤科技涨停，天禾股份、红四方、亚钾国际、中毅达、金能科技跟涨。"
  },
  {
    "id": "wscn:3780210",
    "domain": "股票",
    "title": "零跑也要造机器人了",
    "url": "https://wallstreetcn.com/articles/3780210",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T01:56:42+00:00",
    "summary": "下半年利润还将回暖。"
  },
  {
    "id": "wscn:3780206",
    "domain": "股票",
    "title": "铁索连舟：美债的赤壁之战",
    "url": "https://wallstreetcn.com/articles/3780206",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T01:45:44+00:00",
    "summary": "财通宏观张伟团队认为，美国通过让日本、欧洲大规模持有美债，将盟友财政与自身深度捆绑——此即\"铁索连舟\"。经济上行时铁索稳固，一旦遭遇全球滞胀，一船起火、众船遭殃。日欧深陷滞胀困境，财政承压、汇率受损，购债能力持续下滑，美债海外需求缺口显现。市场抢跑加速预期自我实现，长端利率快速上行本质是一场挤兑。"
  },
  {
    "id": "wscn:3780204",
    "domain": "股票",
    "title": "黄仁勋不停歇：芯片、数据中心、模型三线并进，英伟达以投资换锁定加固AI霸主地位",
    "url": "https://wallstreetcn.com/articles/3780204",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T01:35:56+00:00",
    "summary": "英伟达正以罕见的行动密度构筑AI护城河：同步领投Perplexity、斥资60亿美元拿下Poolside百名工程师与软件授权、深度布局数据中心电力基础设施。与此同时，旗舰芯片明年涨价17%，将推高吉瓦级数据中心成本逾50亿美元。黄仁勋的算盘清晰——在AI基建爆发前夜，以投资换绑定，以涨价证定价权。"
  },
  {
    "id": "wscn:3780202",
    "domain": "股票",
    "title": "欧元：还能涨多少？",
    "url": "https://wallstreetcn.com/articles/3780202",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T01:35:52+00:00",
    "summary": "欧元上周强势突破1.16关键阻力位，一度冲上1.17，但本周开盘后出现回调。欧美经济预期差走阔、欧央行加息概率高达95%、美元信用担忧升温，三重利多共振推动本轮涨势。然而能源价格居高不下、德国政治风险隐现，短期上破1.18动能不足。"
  },
  {
    "id": "wscn:3780130",
    "domain": "股票",
    "title": "37万亿险资换锚：一条100%重磅监管红线落地，能把多少资金推向红利？",
    "url": "https://wallstreetcn.com/premium/articles/3780130?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T01:34:59+00:00",
    "summary": "《保险公司资产负债管理办法》正式落地，最受市场关注的变化，是人身险净投资收益覆盖率被纳入硬性监管指标，并要求不低于100%。在长端利率下行、存量高收益资产持续到期的背景下，股息红利作为稳定净投资收益来源，其监管价值明显上升。按照不同假设测算，未来数年险资对高股息资产的潜在增配规模可能达到数千亿元至万亿元级，这会不会成为红利资产下一阶段最重要的长期买方力量？"
  },
  {
    "id": "wscn:3780205",
    "domain": "股票",
    "title": "苹果为库克举行告别派对，私人伴侣首度公开亮相，继任者Ternus强调“延续”",
    "url": "https://wallstreetcn.com/articles/3780205",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T01:34:35+00:00",
    "summary": "苹果于上周日在苹果园区为即将卸任的CEO库克举办告别派对，乐队OneRepublic现场演出，约200名苹果员工出席。一向极度低调的库克在致辞中公开提及其伴侣Mike。知情人士预计苹果高层在短期内不会有大的变化，并用一个词来概括这次权力交接：延续（continuity）。"
  },
  {
    "id": "wscn:3780208",
    "domain": "股票",
    "title": "从增收不增利到净利增近五成，石头科技利润开始修复",
    "url": "https://wallstreetcn.com/articles/3780208",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T01:19:39+00:00",
    "summary": "走出高投入阵痛期"
  },
  {
    "id": "wscn:3780207",
    "domain": "股票",
    "title": "新国标产品切换期，爱玛科技上半年收入、利润双位数下降",
    "url": "https://wallstreetcn.com/articles/3780207",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T01:18:13+00:00",
    "summary": "从高增长到业绩回落"
  },
  {
    "id": "wscn:3780198",
    "domain": "股票",
    "title": "不满韩国国内扩产，美国施压要求赴美建厂",
    "url": "https://wallstreetcn.com/articles/3780198",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T00:39:31+00:00",
    "summary": "据报道，韩国执政党官员透露，美方明确要求韩企赴美建内存工厂保供应，湖南半导体超大规模项目宣布后，半导体投资施压明显加剧，指责韩企在美半导体投资计划迟迟未能落地。韩国政府计划于9月某个时间节点公布首批对美投资项目。"
  },
  {
    "id": "wscn:3780195",
    "domain": "股票",
    "title": "高盛对冲基金业务主管：油价比杰克逊霍尔美联储年会重要，英伟达是本周焦点",
    "url": "https://wallstreetcn.com/articles/3780195",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T00:30:39+00:00",
    "summary": "高盛对冲基金主管Privorotsky本周发出警示：油价走势对股市的重要性可能超越杰克逊霍尔年会——压低能源价格或是稳定债市的最短路径。英伟达财报需求虽将\"强劲得离谱\"，但AI融资泡沫、内存成本与估值压缩的三重隐忧已暗流涌动。他建议：做多金融与工业，持有\"标普+黄金\"，债券等待做空时机，半导体则需等盈利追上估值再言突破。"
  },
  {
    "id": "wscn:3780196",
    "domain": "股票",
    "title": "过去三周，投资机构买入黄金期货规模创纪录！",
    "url": "https://wallstreetcn.com/articles/3780196",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T00:27:12+00:00",
    "summary": "过去三周，投机性资金净买入黄金期货222亿美元，创逾十年名义金额最高纪录，净多头仓位处于两年93%分位。美国财政部扩大长债回购后，金价单周涨近6%。高盛与瑞银均看多黄金中长期走势，但同时提示短期仓位过热风险，杰克逊霍尔会议成为最大近期变量。预测市场显示黄金年内触及5000美元概率已超60%。"
  },
  {
    "id": "wscn:3780159",
    "domain": "股票",
    "title": "杠杆泡沫挤出、反弹25%后，韩股吸引力还剩下多少？",
    "url": "https://wallstreetcn.com/premium/articles/3780159?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T00:26:34+00:00",
    "summary": "去杠杆基本完成、估值仍处低位，AI需求向主权AI与多产业扩散，韩股增长逻辑正超越传统存储周期。"
  },
  {
    "id": "wscn:3780194",
    "domain": "股票",
    "title": "英伟达震撼首测Vera Rubin，DeepSeek吞吐暴涨30倍！",
    "url": "https://wallstreetcn.com/articles/3780194",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T00:22:02+00:00",
    "summary": "英伟达首次公布Vera Rubin NVL72片上实测数据，搭配DeepSeek-V4-Pro跑Agent编码任务，较GB300每兆瓦吞吐量最高飙升30倍，Token成本暴降35倍。同日，专为Agent设计的Vera CPU已被SpaceXAI规模化部署，并计划2028年送上太空。Groq加速器全面量产。"
  },
  {
    "id": "wscn:3780190",
    "domain": "股票",
    "title": "特朗普政府拟征10.3万美元H-1B费用，覆盖范围较前令大幅扩展",
    "url": "https://wallstreetcn.com/articles/3780190",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T00:05:44+00:00",
    "summary": "美国国土安全部发布规则草案，拟对所有受年度配额限制的H-1B签证申请征收逾10万美元费用，覆盖范围较特朗普此前行政令大幅扩展，包括已在美境内持有H-1B身份的人员。此举旨在弥补移民审核行政成本。此前行政令因法院裁定违法征税而受阻，新规改以行政法规形式推进，规避法律障碍。"
  },
  {
    "id": "wscn:3780192",
    "domain": "股票",
    "title": "救美债！除了回购，贝森特还有一个大招：美元稳定币",
    "url": "https://wallstreetcn.com/articles/3780192",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-25T00:05:18+00:00",
    "summary": "美国财政部长贝森特推行“国债扭转操作”——增发短期国债、回购长期国债，以压低长端利率。而稳定币是贝森特看好的短期国债需求新来源，美相关法案规定美元稳定币须以93天内到期的国债等资产背书。花旗测算，若稳定币市场达4万亿美元，其持有的短期国债规模到2030年或占全部在外流通短期国债的约四分之一。"
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
    "id": "hn:49415187",
    "domain": "金融",
    "title": "Nearly 3M Teslas recalled in China over hidden door handles",
    "url": "https://www.bbc.com/news/articles/c4g6ggdg030o",
    "source": "chicken-stew",
    "platform": "hackernews",
    "points": 118,
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
