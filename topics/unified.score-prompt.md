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

- 今日日期：`2026-08-18`
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
  "date": "2026-08-18",
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
    "points": 1722396,
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
    "points": 1332745,
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
    "points": 1140499,
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
    "points": 1068821,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV12omoB4ExF",
    "domain": "AI",
    "title": "黑马程序员全网最全Coze智能体入门到项目实战全套教程，从AI Agent开发入门到6大AI智能体实战项目，涵盖提示词Prompt、RAG、Bot发布微信公众号",
    "url": "http://www.bilibili.com/video/av115713129843205",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 1045313,
    "published_at": "2025-12-15T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：251215\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV1o4gw6ZExs",
    "domain": "AI",
    "title": "我是怎么用AI干活的？",
    "url": "http://www.bilibili.com/video/av117092535768773",
    "source": "林亦LYi",
    "platform": "bilibili",
    "points": 977001,
    "published_at": "2026-08-14T12:00:00+00:00",
    "summary": "AI 办公到底能干些啥？它真的能颠覆我们的工作方式，以至于让大厂押上身家也要卷吗？"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 875061,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 850835,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1wugF6YEL3",
    "domain": "AI",
    "title": "再见Claude Code！你好DeepSeek Harness！",
    "url": "http://www.bilibili.com/video/av117089415204498",
    "source": "Lau博士的云组会",
    "platform": "bilibili",
    "points": 609967,
    "published_at": "2026-08-13T17:42:16+00:00",
    "summary": "DeepSeek Harness开源了。看完就两个字：牛逼\n本期视频，Lau博士就带着大家一起，解读DeepSeek 亲手做的这个 Harness，到底有什么不一样。"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 585466,
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
    "points": 584445,
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
    "points": 526035,
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
    "points": 437867,
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
    "points": 398305,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 352166,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 267447,
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
    "points": 241709,
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
    "points": 240373,
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
    "points": 179377,
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
    "points": 168601,
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
    "points": 163859,
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
    "points": 134845,
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
    "points": 125455,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 117137,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV139bD6gEa8",
    "domain": "AI",
    "title": "Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一期视频精通",
    "url": "http://www.bilibili.com/video/av117104095268420",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 101490,
    "published_at": "2026-08-16T07:53:45+00:00",
    "summary": "Pi是近期热度超高的AI Agent。用四个字形容那就是大道至简。 Pi只有四个默认工具，（读文件，写文件，改文件，运行命令），系统提示词也仅仅只有一千Token。极致的精简带来了极致效率提升，在多项权威基准测试里，Pi 的代码质量，工作速度，成本等方面多方面超过主流Agent Codex和Claude Code。 Pi还有极其开放的插件生态，可以自己编写插件扩展Pi的能力。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93249,
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
    "points": 91444,
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
    "points": 85943,
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
    "points": 74145,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63542,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54151,
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
    "points": 47628,
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
    "points": 46386,
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
    "points": 44616,
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
    "points": 40698,
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
    "points": 38883,
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
    "points": 35133,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29633,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "harness使用教程-",
    "platform": "bilibili",
    "points": 28536,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 26517,
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
    "points": 22713,
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
    "points": 21881,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 19550,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17720,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1aQMX6oEni",
    "domain": "AI",
    "title": "【Agent面经】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av117030678239428",
    "source": "Agent开发实战",
    "platform": "bilibili",
    "points": 17568,
    "published_at": "2026-08-03T08:50:19+00:00",
    "summary": "【Agent面试100问】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16302,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1DPwGe1Ekf",
    "domain": "AI",
    "title": "Cursor从小白到专家-第15课：如何用Cursor+Dify搭建本地知识库？",
    "url": "http://www.bilibili.com/video/av113836698898908",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 14323,
    "published_at": "2025-01-16T08:55:00+00:00",
    "summary": "在第九课“如何用 cursor + coze 搭建线上知识库”的分享后，有一部分精神股东表示，想要本地知识库的搭建教程。\n.\n有求必应，今天第15课的分享就是“用 cursor + dify 搭建本地知识库”，手把手教会。我们第16课见 ~"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 11618,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 9430,
    "published_at": "2026-06-28T09:05:03+00:00",
    "summary": "企鹅交流群：1038830654"
  },
  {
    "id": "bvid:BV1jV3i68EZS",
    "domain": "AI",
    "title": "2026吃透Java AI Agent+SpringAI Alibaba Agent Framwork+Skill实战全套教程！从0到1掌握智能体开发！",
    "url": "http://www.bilibili.com/video/av116996385605699",
    "source": "程序员北边",
    "platform": "bilibili",
    "points": 9380,
    "published_at": "2026-07-28T09:16:25+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv39693258/"
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
    "points": 245,
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
    "id": "hn:49322519",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX at end of second quarter",
    "url": "https://www.cnbc.com/2026/08/14/nvidia-discloses-21-billion-stake-in-spacex-at-end-of-second-quarter.html",
    "source": "johnbarron",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-08-16T18:40:54+00:00",
    "summary": ""
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
    "id": "rss:https://www.tomshardware.com/tech-industry/pc-partner-warns-of-rising-gpu-prices-and-budget-card-shortages-analyst-suggests-makers-are-hiking-prices-beyond-memory-costs",
    "domain": "AI 算力 / 半导体",
    "title": "PC Partner warns of rising GPU prices and budget card shortages — analyst suggests makers are hiking prices beyond memory costs",
    "url": "https://www.tomshardware.com/tech-industry/pc-partner-warns-of-rising-gpu-prices-and-budget-card-shortages-analyst-suggests-makers-are-hiking-prices-beyond-memory-costs",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T11:00:00+00:00",
    "summary": "PC Partner warns that graphics card prices will rise further in H2 2026 as memory costs climb and supplies tighten and entry-level boards will gain the most. This is how they gain money, says Jon Pedd"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-an-rtx-5090-alienware-pc-for-less-than-the-price-of-the-gpu-alone-usd1-550-discount-means-area-51-is-usd20-cheaper-than-buying-the-card-by-itself",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5090 Alienware PC for less than the price of the GPU alone — $1,550 discount means Area-51 is $20 cheaper than buying the card by itself",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-an-rtx-5090-alienware-pc-for-less-than-the-price-of-the-gpu-alone-usd1-550-discount-means-area-51-is-usd20-cheaper-than-buying-the-card-by-itself",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T10:55:01+00:00",
    "summary": "Get an RTX 5090 Alienware gaming PC for less than the standalone cost of the GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/save-usd60-on-corsairs-impressive-96-percent-gaming-keyboard-with-elgato-stream-deck-integration-the-vanguard-96-rgb-features-pre-lubed-mechanical-switches-sound-dampening-a-color-lcd-screen-and-a-full-size-number-pad",
    "domain": "AI 算力 / 半导体",
    "title": "Save $60 on Corsair's impressive 96% gaming keyboard with Elgato Stream Deck integration — the Vanguard 96 RGB features pre-lubed mechanical switches, sound dampening, a color LCD screen, and a full-s",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/save-usd60-on-corsairs-impressive-96-percent-gaming-keyboard-with-elgato-stream-deck-integration-the-vanguard-96-rgb-features-pre-lubed-mechanical-switches-sound-dampening-a-color-lcd-screen-and-a-full-size-number-pad",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T10:50:50+00:00",
    "summary": "Save $60 on Corsair's impressive Vanguard 96 RGB mechanical gaming keyboard at Best Buy."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/japanese-repair-shop-sells-gddr6-vram-upgrades-for-usd25-per-gb-during-memory-crisis-rtx-2080-ti-modded-to-22gb-for-just-usd282-double-the-vram-creates-a-budget-ai-powerhouse",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese repair shop sells GPU VRAM upgrades for $25 per GB during memory crisis — RTX 2080 Ti modded to 22GB of GDDR6 for just $282, double the VRAM creates a budget AI powerhouse",
    "url": "https://www.tomshardware.com/pc-components/gpus/japanese-repair-shop-sells-gddr6-vram-upgrades-for-usd25-per-gb-during-memory-crisis-rtx-2080-ti-modded-to-22gb-for-just-usd282-double-the-vram-creates-a-budget-ai-powerhouse",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T10:30:00+00:00",
    "summary": "This vendor can upgrade your RTX 2080 Ti to feature 22GB of VRAM for less than $300, converting it into an AI powerhouse without breaking the bank."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/hong-kong-pc-store-accuses-two-senior-staff-of-stealing-stock-to-supply-their-own-online-shop-for-over-a-year",
    "domain": "AI 算力 / 半导体",
    "title": "Senior PC store staff accused of running secret rival shop with stolen inventory — Hong Kong retailer claims substantial losses over year-long scheme",
    "url": "https://www.tomshardware.com/tech-industry/hong-kong-pc-store-accuses-two-senior-staff-of-stealing-stock-to-supply-their-own-online-shop-for-over-a-year",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T10:00:00+00:00",
    "summary": "A PC retailer in Wan Chai's Computer Zone 298 mall in Hong Kong, has accused two of its senior employees of stealing company stock for roughly a year and reselling it."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/desktop-uv-printers-and-wild-custom-builds-take-over-open-sauce-2026-usd1-700-full-color-printers-flash-cured-resin-and-a-rideable-speeder-bike",
    "domain": "AI 算力 / 半导体",
    "title": "Desktop UV printers and wild custom builds take over Open Sauce 2026 — $1,700 full-color printers, flash-cured resin, and a rideable speeder bike",
    "url": "https://www.tomshardware.com/3d-printing/desktop-uv-printers-and-wild-custom-builds-take-over-open-sauce-2026-usd1-700-full-color-printers-flash-cured-resin-and-a-rideable-speeder-bike",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T09:45:00+00:00",
    "summary": "If you want to see the bleeding edge of 3D printing tech, you go to FormNext in Frankfurt, Germany. If you want to see the latest in consumer electronics, you go to CES in Las Vegas. If you want to se"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/air-conditioner-powered-by-a-pc-fan-labeled-a-scam-by-german-consumer-organization-theres-a-reason-this-lookalike-ac-unit-is-far-cheaper-than-its-competitors",
    "domain": "AI 算力 / 半导体",
    "title": "Air conditioner powered by a 'PC fan' labeled a scam by German consumer organization — there's a reason this lookalike AC unit is far cheaper than its competitors",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/air-conditioner-powered-by-a-pc-fan-labeled-a-scam-by-german-consumer-organization-theres-a-reason-this-lookalike-ac-unit-is-far-cheaper-than-its-competitors",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T09:30:00+00:00",
    "summary": "Tear down of a so-called air conditioner from Epicool revealed 'a simple PC fan combined with a small heating element.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-portable-external-cd-dvd-drive-comes-with-a-2-5-inch-sata-and-an-sd-card-slot-for-just-usd26-save-10-percent-on-a-modern-essential-for-keeping-physical-media-alive",
    "domain": "AI 算力 / 半导体",
    "title": "This portable, external CD/DVD drive comes with a 2.5-inch SATA and an SD Card slot for just $26 — Save 10% on a modern essential for keeping physical media alive",
    "url": "https://www.tomshardware.com/pc-components/this-portable-external-cd-dvd-drive-comes-with-a-2-5-inch-sata-and-an-sd-card-slot-for-just-usd26-save-10-percent-on-a-modern-essential-for-keeping-physical-media-alive",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T15:18:31+00:00",
    "summary": "If you have a bunch of old CDs or DVDs lying around and want something quick and simple to access them, this external drive can get the job done for you for less than $30 while offering extra features"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/dude-youre-getting-a-dell-ai-server-rack-dell-recycles-famous-ad-campaign-to-appeal-to-its-new-ai-overlords",
    "domain": "AI 算力 / 半导体",
    "title": "Dell CEO unveils new 'Dude, you’re getting a Dell (AI server rack)' video — PC maker recycles famous PC ad campaign to tout its new AI data center products",
    "url": "https://www.tomshardware.com/tech-industry/dude-youre-getting-a-dell-ai-server-rack-dell-recycles-famous-ad-campaign-to-appeal-to-its-new-ai-overlords",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T14:31:33+00:00",
    "summary": "Dell has created a humorous AI-era update to its iconic early-2000s 'Dude, you’re getting a Dell' series of commercials."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/maker-compresses-a-2-9mb-song-1000-times-with-metas-ai-codec-and-prints-it-on-paper-as-eight-qr-codes",
    "domain": "AI 算力 / 半导体",
    "title": "Maker compresses a 2.9MB song by 1000x and prints it on paper as eight QR codes — 21KB song is two minutes long, requires a neural network for playback",
    "url": "https://www.tomshardware.com/tech-industry/maker-compresses-a-2-9mb-song-1000-times-with-metas-ai-codec-and-prints-it-on-paper-as-eight-qr-codes",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T14:22:36+00:00",
    "summary": "The open-source codec Meta released in 2022 converts a waveform into discrete tokens that a matching decoder turns back into audio."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/ukraine-destroys-tu-95-bomber-using-48000-chinese-drone-clone",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine built a $48,000 long-range drone after covertly snapping Chinese factory photos, clone destroys Russian Tu-95 bomber — attack drone has 2,000 km range, country builds 6,000 flying-wing drones ",
    "url": "https://www.tomshardware.com/tech-industry/drones/ukraine-destroys-tu-95-bomber-using-48000-chinese-drone-clone",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T13:20:00+00:00",
    "summary": "The drone that destroyed a Tupolev Tu-95MS strategic bomber at Russia's Engels-2 air base last month turns out to be the MICH 2000."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/macos-screen-sharing-flaw-exploited-to-root-macs-and-plant-monero-miners",
    "domain": "AI 算力 / 半导体",
    "title": "Critical macOS Screen Sharing flaw gives attackers remote root access — CISA bumps bug to 9.8 severity following active Monero cryptojacking attacks",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/macos-screen-sharing-flaw-exploited-to-root-macs-and-plant-monero-miners",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T13:00:00+00:00",
    "summary": "The Dutch National Cyber Security Centre (NCSC-NL) says that attackers are actively exploiting CVE-2026-65400, an authentication bypass in macOS Screen Sharing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-hybrid-ai-asic-could-integrate-on-package-cpu-cores-for-reinforcement-learning",
    "domain": "AI 算力 / 半导体",
    "title": "Google reportedly taps AMD to design next-generation TPU — hybrid AI ASIC could integrate on-package CPU cores for reinforcement learning",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-hybrid-ai-asic-could-integrate-on-package-cpu-cores-for-reinforcement-learning",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T12:40:00+00:00",
    "summary": "Google may be building a TPU with on-package CPU cores specifically for agentic and reinforced learning workloads, according to a rumor."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-says-it-will-launch-new-core-with-nova-lake-on-desktop-first-not-in-data-center-vp-robert-hallock-hopes-enthusiasts-do-the-math-compared-to-amd",
    "domain": "AI 算力 / 半导体",
    "title": "Intel says it will launch new core with Nova Lake on desktop first, not in data center — VP Robert Hallock hopes enthusiasts ‘do the math’ compared to AMD",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-says-it-will-launch-new-core-with-nova-lake-on-desktop-first-not-in-data-center-vp-robert-hallock-hopes-enthusiasts-do-the-math-compared-to-amd",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T12:10:00+00:00",
    "summary": "Intel’s Robert Hallock says he hopes enthusiasts “do the math” compared to AMD, highlighting that the company’s new core architecture will release in consumer processors before the data center."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-printed-sound-powered-jet-engines-propel-micro-drones-fliers-are-completely-silent-researchers-use-ultrasonic-frequencies-to-drive-12-000-rpm-silent-hovering-fliers",
    "domain": "AI 算力 / 半导体",
    "title": "3D-printed sound-powered jet engines propel micro drones — fliers are completely silent; researchers use ultrasonic frequencies to drive 12,000-RPM silent hovering fliers",
    "url": "https://www.tomshardware.com/3d-printing/3d-printed-sound-powered-jet-engines-propel-micro-drones-fliers-are-completely-silent-researchers-use-ultrasonic-frequencies-to-drive-12-000-rpm-silent-hovering-fliers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:50:00+00:00",
    "summary": "A specially shaped 3D-printed resonator can make air shoot out of its nozzle and provide thrust when it hit with the proper frequency. While the prototypes don't deliver practical levels of thrust yet"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-printing-enthusiast-creates-flock-sock-camera-blind-slip-on-cover-attaches-to-broom-handle-to-make-it-easy-to-put-on-devices-placed-on-traffic-and-streetlights",
    "domain": "AI 算力 / 半导体",
    "title": "3D-printing enthusiast creates ‘Flock Sock’ to blind controversial cameras, shares design — slip-on cover attaches to broom handle to make it easy to put on devices placed on traffic and streetlights",
    "url": "https://www.tomshardware.com/3d-printing/3d-printing-enthusiast-creates-flock-sock-camera-blind-slip-on-cover-attaches-to-broom-handle-to-make-it-easy-to-put-on-devices-placed-on-traffic-and-streetlights",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:30:00+00:00",
    "summary": "SquidInk created a 3D-printing model that would allow anyone to build an easy-to-install \"protective cover\" for Flock cameras. The \"Flock Sock\" slips on these devices in seconds using a broom handle, "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/the-pc-age-began-45-years-ago-with-the-breakthrough-intel-8088-processor-8-bit-bus-fueled-45-years-of-x86-dominance",
    "domain": "AI 算力 / 半导体",
    "title": "The PC age began 45 years ago with the breakthrough Intel 8088 processor — 8-bit bus fueled 45 years of x86 dominance",
    "url": "https://www.tomshardware.com/pc-components/cpus/the-pc-age-began-45-years-ago-with-the-breakthrough-intel-8088-processor-8-bit-bus-fueled-45-years-of-x86-dominance",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:20:00+00:00",
    "summary": "45 years ago, in August 1981, the PC age began in earnest with the launch of the IBM PC Model 5150. At its heart was the Intel 8088 microprocessor."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/modern-oled-tvs-are-just-as-susceptible-to-burn-in-as-older-models-but-theyre-much-brighter-longevity-test-highlights-luminance-headroom-and-efficiency-as-mitigations",
    "domain": "AI 算力 / 半导体",
    "title": "Modern OLEDs are just as vulnerable to burn-in as 2017 panels in 10,000-hour test — twice the brightness and 27% efficiency gains offer crucial headroom",
    "url": "https://www.tomshardware.com/monitors/modern-oled-tvs-are-just-as-susceptible-to-burn-in-as-older-models-but-theyre-much-brighter-longevity-test-highlights-luminance-headroom-and-efficiency-as-mitigations",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:10:00+00:00",
    "summary": "Rtings.com's latest update on their Accelerated Longevity Test shows that modern OLED TVs don't offer a clear advantage over older models in terms of burn-in since both show similar image retention af"
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/xtool-m2-color-craft-laser-and-engraver-review",
    "domain": "AI 算力 / 半导体",
    "title": "xTool M2 color craft laser and engraver review: Improved print head and positioning cameras at a lower price",
    "url": "https://www.tomshardware.com/maker-stem/xtool-m2-color-craft-laser-and-engraver-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T11:05:00+00:00",
    "summary": "The M2 is xTool’s second take on an all-in-one craft tool in a box. It isn’t just an iterative update to the M1 Ultra, the new M2 color craft laser and engraver thoroughly remixes the offering by addi"
  },
  {
    "id": "hn:49306491",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://www.ft.com/content/6f66a76d-0b2d-4301-886c-87ecc046731b",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-15T01:02:55+00:00",
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
    "id": "hn:49248477",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is pulling Wall Street into the AI buildout",
    "url": "https://thenextweb.com/news/nvidia-500-billion-wall-street-ai-infrastructure-funding-package",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-10T19:25:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49279812",
    "domain": "AI 算力 / 半导体",
    "title": "Why space is a terrible place to cool a data center",
    "url": "https://thenewstack.io/spacex-and-nvidias-orbital-ai-datacenter-fantasy/",
    "source": "CrankyBear",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-12T23:08:21+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/",
    "domain": "AI 算力 / 半导体",
    "title": "Smartphone Makers Squeezed by Soaring Chip Costs",
    "url": "https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T18:47:35+00:00",
    "summary": "Chip costs are gutting smartphone margins; expect pricier iPhones and fewer cheap phones. The post Smartphone Makers Squeezed by Soaring Chip Costs appeared first on EE Times."
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
    "points": 866,
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
    "points": 306,
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
    "id": "hn:49335017",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp v0.1.0",
    "url": "https://github.com/ggml-org/llama.cpp/releases/tag/v0.1.0",
    "source": "satvikpendem",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-08-17T17:56:06+00:00",
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
    "id": "rss:https://www.theverge.com/tech/981289/reddit-ai-text-video-posts",
    "domain": "大厂 AI 动态",
    "title": "Reddit’s AI is turning posts into podcasts and short videos",
    "url": "https://www.theverge.com/tech/981289/reddit-ai-text-video-posts",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T23:46:01+00:00",
    "summary": "Reddit is trying out a new way for people to take in content on Reddit: by turning text posts into audio / video content. As part of an experiment, some posts are being adapted into videos that use AI"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/981209/abc-news-searched-livestreamed-show",
    "domain": "大厂 AI 动态",
    "title": "ABC&#8217;s livestreamed news show is powered by trending topics",
    "url": "https://www.theverge.com/streaming/981209/abc-news-searched-livestreamed-show",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T20:59:23+00:00",
    "summary": "ABC News has officially introduced Searched, a livestreamed show that highlights stories people are discussing on social media and searching on the web, as reported earlier by Variety. Though the netw"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/981134/glorious-gmmk-3-mechanical-keyboard-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "This compact Glorious mechanical keyboard is just $35",
    "url": "https://www.theverge.com/gadgets/981134/glorious-gmmk-3-mechanical-keyboard-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T19:27:49+00:00",
    "summary": "Are you curious about custom mechanical keyboards, but don’t want to spend hundreds just to get started without being sure you’ll enjoy the hobby? You can grab the 65-percent Glorious GMMK 3 mechanica"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/981014/dartwords-clippy-word-game",
    "domain": "大厂 AI 动态",
    "title": "Wordle meets Clippy in this new word game",
    "url": "https://www.theverge.com/entertainment/981014/dartwords-clippy-word-game",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T19:03:41+00:00",
    "summary": "Like many of us, Sam Rosenthal plays games like Wordle every day, chasing after good scores and sharing the results with friends and family. But he's also a game designer, the creative director at Bla"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/981105/youtube-video-view-counting-update",
    "domain": "大厂 AI 动态",
    "title": "YouTube is changing how it counts views to give the numbers a boost",
    "url": "https://www.theverge.com/streaming/981105/youtube-video-view-counting-update",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T17:13:03+00:00",
    "summary": "YouTube will soon count a view as soon as a video starts to play, lining up with the system used by Instagram, TikTok, and its Shorts videos. The update will go into effect on August 24th, \"which mean"
  },
  {
    "id": "rss:https://www.theverge.com/games/981054/analogue-pocket-supreme-red-gold-fall-winter-2026-collection",
    "domain": "大厂 AI 动态",
    "title": "The Analogue Pocket gets a Supreme makeover in red or gold",
    "url": "https://www.theverge.com/games/981054/analogue-pocket-supreme-red-gold-fall-winter-2026-collection",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T16:40:32+00:00",
    "summary": "Analogue and Supreme are teaming up to release metallic versions of the Analogue Pocket handheld in red and gold as part of Supreme's fall / winter 2026 collection. Here's how they're described on Sup"
  },
  {
    "id": "rss:https://www.theverge.com/tech/981008/sonos-mobile-ios-iphone-app-live-activities",
    "domain": "大厂 AI 动态",
    "title": "Sonos finally added Live Activities controls for your iPhone lockscreen",
    "url": "https://www.theverge.com/tech/981008/sonos-mobile-ios-iphone-app-live-activities",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T16:38:35+00:00",
    "summary": "Sonos released an update to its mobile app that finally introduces support for iOS' Live Activities, giving iPhone users quick access to playback controls on their lockscreen. The added functionality "
  },
  {
    "id": "rss:https://www.theverge.com/report/980933/trump-border-wall-big-bend-arizona-cottonwood-tree-sit",
    "domain": "大厂 AI 动态",
    "title": "Trump’s dumb border wall",
    "url": "https://www.theverge.com/report/980933/trump-border-wall-big-bend-arizona-cottonwood-tree-sit",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T16:30:00+00:00",
    "summary": "About 22 miles south of the former mining town of Patagonia, Arizona, down a winding, unpaved mountain road that passes cows grazing on open range, stands a cottonwood tree believed to be at least 200"
  },
  {
    "id": "rss:https://www.theverge.com/tech/980977/apple-app-tracking-transparency-settlement-germany",
    "domain": "大厂 AI 动态",
    "title": "Apple ordered to stop scaring iPhone and iPad users away from third-party apps",
    "url": "https://www.theverge.com/tech/980977/apple-app-tracking-transparency-settlement-germany",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T15:10:25+00:00",
    "summary": "Apple's changing its rules for data collection consent prompts after Germany's Federal Cartel Office accused Apple of giving the prompts a design that favored its own apps. Apple's App Tracking Transp"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/980916/wiim-sound-speaker-lite-airpods-max-2-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "WiiM’s capable HomePod-esque smart speaker is almost $50 off",
    "url": "https://www.theverge.com/gadgets/980916/wiim-sound-speaker-lite-airpods-max-2-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T14:35:25+00:00",
    "summary": "The smart speaker market is more or less dominated by major tech companies: Apple, Google, Sonos, and Amazon. But WiiM’s powerful 100W Sound smart speaker is an attractive alternative because it’s not"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s annualized revenue surges to $65B",
    "url": "https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T23:56:26+00:00",
    "summary": "The model maker added $18 billion in annualized revenue in two months."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/ai-automation-startup-relay-shuts-down-staff-joins-googles-chrome-team/",
    "domain": "大厂 AI 动态",
    "title": "AI automation startup Relay shuts down, staff joins Google’s Chrome team",
    "url": "https://techcrunch.com/2026/08/17/ai-automation-startup-relay-shuts-down-staff-joins-googles-chrome-team/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T21:27:05+00:00",
    "summary": "\"We have some really ambitious plans to help you work with AI in Chrome to get things done, and I’ll have more to share soon,\" Jacob Bank, Relay founder and CEO, said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/unprecedented-number-of-apple-users-received-recent-spyware-alert-say-investigators/",
    "domain": "大厂 AI 动态",
    "title": "‘Unprecedented’ number of Apple users received recent spyware alert, say investigators",
    "url": "https://techcrunch.com/2026/08/17/unprecedented-number-of-apple-users-received-recent-spyware-alert-say-investigators/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T20:18:35+00:00",
    "summary": "Cybersecurity experts who investigate spyware attacks say the number of people who received a recent threat notification from Apple is unusually high."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/save-up-to-300-on-your-techcrunch-disrupt-2026-pass-until-august-21/",
    "domain": "大厂 AI 动态",
    "title": "Save up to $300 on your TechCrunch Disrupt 2026 pass until August 21",
    "url": "https://techcrunch.com/2026/08/17/save-up-to-300-on-your-techcrunch-disrupt-2026-pass-until-august-21/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T19:33:51+00:00",
    "summary": "If you’ve been circling around Disrupt, then now’s the best time to lock in your pass and start getting ready to join the rest of the startup community gathering in San Francisco from October 13-15 at"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/spotifys-new-playlist-notes-let-users-and-editors-explain-their-song-picks/",
    "domain": "大厂 AI 动态",
    "title": "Spotify’s new Playlist Notes let users and editors explain their song picks",
    "url": "https://techcrunch.com/2026/08/17/spotifys-new-playlist-notes-let-users-and-editors-explain-their-song-picks/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T19:24:43+00:00",
    "summary": "Spotify launches a new feature that gives users a chance to explain the stories and reasoning behind their favorite music. Editors will be using the feature, too, on top playlists like RapCaviar and o"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/higgsfield-raises-400m-series-b-quadrupling-its-valuation-in-8-months-to-5-4b/",
    "domain": "大厂 AI 动态",
    "title": "Higgsfield raises $400M Series B, quadrupling its valuation in 8 months to $5.4B",
    "url": "https://techcrunch.com/2026/08/17/higgsfield-raises-400m-series-b-quadrupling-its-valuation-in-8-months-to-5-4b/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T19:04:27+00:00",
    "summary": "Higgsfield, founded by former Snap exec Alex Mashrabov, lets users create AI images and videos."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/reddit-begins-testing-a-new-audio-and-video-experience-similar-to-popular-tiktok-videos/",
    "domain": "大厂 AI 动态",
    "title": "Reddit begins testing a new audio and video experience, similar to popular TikTok videos",
    "url": "https://techcrunch.com/2026/08/17/reddit-begins-testing-a-new-audio-and-video-experience-similar-to-popular-tiktok-videos/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T18:42:30+00:00",
    "summary": "Reddit is beginning to test video and audio versions of popular posts, allowing users to watch or listen to Reddit stories instead of just reading them."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/sound-powered-fire-protection-startup-gets-15m-to-snuff-out-fires-before-they-turn-catastrophic/",
    "domain": "大厂 AI 动态",
    "title": "Sound-powered fire protection startup gets $15M to snuff out fires before they turn catastrophic",
    "url": "https://techcrunch.com/2026/08/17/sound-powered-fire-protection-startup-gets-15m-to-snuff-out-fires-before-they-turn-catastrophic/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T18:32:27+00:00",
    "summary": "Sonic Fire Tech raised its new funding to help get its sound-powered fire protection system into everything from commercial kitchens to apartment buildings."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/youtube-will-now-count-a-view-as-soon-as-a-video-starts-playing/",
    "domain": "大厂 AI 动态",
    "title": "YouTube will now count a view as soon as a video starts playing",
    "url": "https://techcrunch.com/2026/08/17/youtube-will-now-count-a-view-as-soon-as-a-video-starts-playing/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T18:09:33+00:00",
    "summary": "The change comes a year after YouTube applied the same approach to counting views on Shorts videos."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/feedly-attributes-weeklong-slowdown-to-bug-not-its-ai-pivot/",
    "domain": "大厂 AI 动态",
    "title": "Feedly attributes weeklong slowdown to bug, not its AI pivot",
    "url": "https://techcrunch.com/2026/08/17/feedly-attributes-weeklong-slowdown-to-bug-not-its-ai-pivot/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T17:10:59+00:00",
    "summary": "Feedly says a bug is behind the performance issues that have made its web app nearly \"unusable\" for some users, while complaints about its mobile apps and customer support are adding to frustrations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/amazon-once-an-online-bookseller-is-destroying-rare-books-to-train-ai-models/",
    "domain": "大厂 AI 动态",
    "title": "Amazon, which started off selling books, is destroying rare texts to train AI",
    "url": "https://techcrunch.com/2026/08/17/amazon-once-an-online-bookseller-is-destroying-rare-books-to-train-ai-models/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T16:38:44+00:00",
    "summary": "Rare books are incredibly valuable for training LLMs, since these models have already trained on whatever's available online."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/groq-raises-350m-to-fuel-its-pivot-from-ai-chips-to-neocloud/",
    "domain": "大厂 AI 动态",
    "title": "Groq raises $350M to fuel its pivot from AI chips to neocloud",
    "url": "https://techcrunch.com/2026/08/17/groq-raises-350m-to-fuel-its-pivot-from-ai-chips-to-neocloud/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T16:15:12+00:00",
    "summary": "Groq raised $350 million at a $3.5 billion valuation as the former AI chipmaker pivots to a neocloud business and expands its Nvidia-powered data center footprint."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/nvidia-investing-1-5b-in-softbank-data-center-developer-behind-openai-project/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia investing $1.5B in SoftBank data center developer behind OpenAI project",
    "url": "https://techcrunch.com/2026/08/17/nvidia-investing-1-5b-in-softbank-data-center-developer-behind-openai-project/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T15:16:24+00:00",
    "summary": "Nvidia's investment in SoftBank's data center developer will guarantee its chips power an OpenAI data center."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/terra-industries-closes-52m-seed-round-to-build-defense-infrastructure-for-the-global-south/",
    "domain": "大厂 AI 动态",
    "title": "Terra Industries closes $52M seed round to build defense infrastructure for the Global South",
    "url": "https://techcrunch.com/2026/08/17/terra-industries-closes-52m-seed-round-to-build-defense-infrastructure-for-the-global-south/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T15:06:07+00:00",
    "summary": "African defense tech company Terra Industries announced an additional $18 million in funding, bringing its seed round to $52 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/wordpress-com-targets-the-next-generation-of-web-creators-with-a-free-student-plan/",
    "domain": "大厂 AI 动态",
    "title": "WordPress.com targets the next generation of web creators with a free student plan",
    "url": "https://techcrunch.com/2026/08/17/wordpress-com-targets-the-next-generation-of-web-creators-with-a-free-student-plan/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T14:56:00+00:00",
    "summary": "WordPress.com Education lets teachers offer their students free domains, plug-in support, and professional website-building tools."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/uber-adds-zipline-drones-to-its-eats-delivery-network/",
    "domain": "大厂 AI 动态",
    "title": "Uber adds Zipline drones to its Eats delivery network",
    "url": "https://techcrunch.com/2026/08/17/uber-adds-zipline-drones-to-its-eats-delivery-network/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T13:18:49+00:00",
    "summary": "Uber is also making investing in Zipline a part of the tie-up."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/wispr-raises-280m-at-2b-valuation-as-it-looks-beyond-dictation/",
    "domain": "大厂 AI 动态",
    "title": "Wispr raises $280M at $2B valuation as it looks beyond dictation",
    "url": "https://techcrunch.com/2026/08/17/wispr-raises-280m-at-2b-valuation-as-it-looks-beyond-dictation/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T13:10:05+00:00",
    "summary": "The funds will allow Wispr to increase its footprint as it ventures into new areas, such as meetings, with its newly released note-taker tool."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/17/crypto-hardware-wallet-owners-face-fresh-security-risks-after-recent-spate-of-personal-data-thefts/",
    "domain": "大厂 AI 动态",
    "title": "Crypto hardware wallet owners face fresh security risks after recent spate of personal data thefts",
    "url": "https://techcrunch.com/2026/08/17/crypto-hardware-wallet-owners-face-fresh-security-risks-after-recent-spate-of-personal-data-thefts/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T13:00:19+00:00",
    "summary": "The hacks at shipping companies used to mail out hardware wallets puts crypto owners at greater risk of real-world attacks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/",
    "domain": "大厂 AI 动态",
    "title": "Stripe will reportedly acquire AI gateway startup OpenRouter for $7B+",
    "url": "https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T20:57:04+00:00",
    "summary": "OpenRouter's CEO recently described the startup as Stripe for AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/16/why-people-arent-buying-mark-zuckerbergs-ai-future/",
    "domain": "大厂 AI 动态",
    "title": "Why people aren’t buying Mark Zuckerberg’s AI future",
    "url": "https://techcrunch.com/2026/08/16/why-people-arent-buying-mark-zuckerbergs-ai-future/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-16T20:32:01+00:00",
    "summary": "On the latest episode of Equity podcast, we discuss why not everyone is buying Zuckerberg’s vision."
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
    "id": "rss:https://arstechnica.com/health/2026/08/us-vaccination-rates-fall-again-as-exemptions-continue-to-rise-cdc-data-shows/",
    "domain": "大厂 AI 动态",
    "title": "US vaccination rates fall again as exemptions continue to rise, CDC data shows",
    "url": "https://arstechnica.com/health/2026/08/us-vaccination-rates-fall-again-as-exemptions-continue-to-rise-cdc-data-shows/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T22:08:47+00:00",
    "summary": "Again, the CDC did not publish a full report and instead simply put the data online."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/former-spacex-engineers-are-building-a-robotic-factory-for-making-steel-parts/",
    "domain": "大厂 AI 动态",
    "title": "Former SpaceX engineers are building a robotic factory for making steel parts",
    "url": "https://arstechnica.com/ai/2026/08/former-spacex-engineers-are-building-a-robotic-factory-for-making-steel-parts/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T21:18:49+00:00",
    "summary": "“We're not necessarily building in a dogmatic fashion towards full autonomy.”"
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/the-moons-shadow-raced-across-the-heart-of-spain-and-i-was-there-to-see-it/",
    "domain": "大厂 AI 动态",
    "title": "The Moon's shadow raced across the heart of Spain, and I was there to see it",
    "url": "https://arstechnica.com/space/2026/08/the-moons-shadow-raced-across-the-heart-of-spain-and-i-was-there-to-see-it/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T20:23:09+00:00",
    "summary": "Here's what it was like watching a total solar eclipse 90 minutes north of Madrid."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/as-wisconsin-cities-flee-flock-its-shared-camera-network-loses-value/",
    "domain": "大厂 AI 动态",
    "title": "As Wisconsin cities flee Flock, its shared camera network loses value",
    "url": "https://arstechnica.com/tech-policy/2026/08/as-wisconsin-cities-flee-flock-its-shared-camera-network-loses-value/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T20:14:23+00:00",
    "summary": "\"Network effect\" can run in reverse."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/supreme-court-rejects-verizon-bid-for-47-million-refund-of-fcc-fine/",
    "domain": "大厂 AI 动态",
    "title": "Supreme Court rejects Verizon bid for $47 million refund of FCC fine",
    "url": "https://arstechnica.com/tech-policy/2026/08/supreme-court-rejects-verizon-bid-for-47-million-refund-of-fcc-fine/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T20:00:20+00:00",
    "summary": "Despite loss, carriers still claim selling device-location data isn't illegal."
  },
  {
    "id": "hn:49335271",
    "domain": "股票",
    "title": "30-year Treasury yield tops 5.31%, the highest in 19 years",
    "url": "https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 50,
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
    "id": "hn:49322233",
    "domain": "股票",
    "title": "AI is not just one bubble, strategist says – but a 'rolling sequence of bubbles'",
    "url": "https://fortune.com/2026/08/16/ai-bubble-sequence-saas-software-stocks-silver-prices-chipmakers/",
    "source": "pessimizer",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-16T18:05:39+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779667",
    "domain": "股票",
    "title": "商业航天夏季展望：一级火热二级寒冰，如何理解剪刀差背后的“叙事重构”？",
    "url": "https://wallstreetcn.com/premium/articles/3779667?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T03:36:35+00:00",
    "summary": "商业航天板块正在经历 2018 年以来最具戏剧性的\"叙事交替\"。二级市场寒意阵阵（板块 PE-TTM 从年初 132.6 倍回落至 94.4 倍、7 月单月 -26.64%），一级市场热火朝天（融资额 151.3 亿元、火箭赛道单笔 50.37 亿元 D+ 轮、垣信卫星启动不低于 50 亿新轮）。"
  },
  {
    "id": "wscn:3779672",
    "domain": "股票",
    "title": "地缘危机打破可再生能源转型幻想，美挪加三国竞相加码化石燃料投资",
    "url": "https://wallstreetcn.com/articles/3779672",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T03:28:32+00:00",
    "summary": "霍尔木兹海峡战云密布，全球能源版图正在重绘。美国页岩油商将资本支出上调近5亿美元，产量有望明年底冲至历史峰值；气候目标倡导大国挪威宣布重启封存近三十年的北海气田；加拿大政策松绑重燃投资信心。能源安全已压倒气候目标，可再生能源转型的节奏面临根本性重估。"
  },
  {
    "id": "wscn:3779664",
    "domain": "股票",
    "title": "铜市供需持续失衡，LME库存单月骤降32%，矿业股迎来新一轮上行机遇",
    "url": "https://wallstreetcn.com/articles/3779664",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T03:19:14+00:00",
    "summary": "LME铜价周一涨至每吨14,396美元，现货升水飙升至2021年以来最高。供应端多重扰动持续施压：智利铜产量同比下降6.7%，Antofagasta下调产量指引，印尼冶炼厂停产。与此同时，市场对美国精炼铜关税预期升温，加剧LME现货紧张。月度交割日临近或进一步放大空头压力，分析师认为矿业股仍具上行空间。"
  },
  {
    "id": "wscn:3779671",
    "domain": "股票",
    "title": "对冲基金连续五日扫货美股，科技板块逼空行情主导年内第二快买入潮",
    "url": "https://wallstreetcn.com/articles/3779671",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T03:10:54+00:00",
    "summary": "高盛Prime Brokerage报告显示，信息技术板块是上周资金净流入规模最大的板块（+1.2个标准差），买盘由多头建仓与空头回补共同驱动，两者比例约为2比1，软件股因Workday并购消息引发大规模空头回补，净配置比例从1.3%升至4.5%。ETF空头头寸上周再度下降3%，月度累计降幅达12%，连续第六周净减少。"
  },
  {
    "id": "wscn:3779656",
    "domain": "股票",
    "title": "AI有多少收入才不是泡沫？",
    "url": "https://wallstreetcn.com/articles/3779656",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T03:10:36+00:00",
    "summary": "AI产业正面临一场万亿级别的自证之战。国金宏观测算显示，2030年前后需近万亿美元收入才能覆盖会计成本，外部融资缺口峰值或在2028年触及7000-8000亿美元。折旧越激进，变现压力越大；而无论哪种情景，年化增速需保持50%以上。沉没成本持续累积，\"1到10\"的担忧正在取代\"0到1\"。"
  },
  {
    "id": "wscn:3779668",
    "domain": "股票",
    "title": "A股三大股指早盘齐跌，半导体硅片活跃，频准激光上市首日暴涨超500%，恒科指跌2%，AI大模型双雄重挫",
    "url": "https://wallstreetcn.com/articles/3779668",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T03:02:54+00:00",
    "summary": "油气概念表现活跃，石化机械直线涨停，海油工程、石化油服、通源石油、山东墨龙、科力股份跟涨。早盘猪肉概念再度活跃，罗牛山2连板，此前天邦食品涨停，大北农、大禹生物、正邦科技、巨星农牧等跟涨。"
  },
  {
    "id": "wscn:3779593",
    "domain": "股票",
    "title": "1.6T突然卡在这颗小芯片上？AI光模块的新瓶颈浮出水面",
    "url": "https://wallstreetcn.com/premium/articles/3779593?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T02:40:21+00:00",
    "summary": "800G仍在放量，1.6T开始爬坡，AI光模块的供给瓶颈却正从激光器进一步扩散到DSP、TIA、Driver等电芯片。AAOI已将DSP和TIA列为800G、1.6T交付的重要运营约束，MACOM则确认200G/lane产品成为数据中心业务增长的重要动力。与此同时，LPO/NPO削弱模块内DSP后，TIA与Driver反而需要承担更多线性放大和信号补偿任务。当量增、规格升级、架构重构与供应趋紧同时"
  },
  {
    "id": "wscn:3779647",
    "domain": "股票",
    "title": "欧央行研究：即便AI达到预期，美国科技股也可能回调，威胁欧元区",
    "url": "https://wallstreetcn.com/articles/3779647",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T02:27:06+00:00",
    "summary": "欧洲央行经济学家发出警告：即便AI最终兑现所有承诺，美国科技股回调仍可能不可避免。核心逻辑在于，技术成功反而会将风险从企业层面扩散至整体经济，推高无法对冲的系统性风险溢价，压制估值。欧元区亦难独善其身，而当前政策应对空间远不及互联网泡沫破裂时充裕。"
  },
  {
    "id": "wscn:3779661",
    "domain": "股票",
    "title": "美对冲基金二季度持仓大曝光：SpaceX获全线押注，Alphabet迎史上最集中加仓潮，英伟达遭减持",
    "url": "https://wallstreetcn.com/articles/3779661",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T02:23:32+00:00",
    "summary": "SpaceX上市首季9家机构抢仓零减持，Alphabet获伯克希尔领衔11家机构加仓；亚马逊则成为本季度最大的多空分歧所在。英伟达与博通遭净减持，AI硬件资金加速流向希捷科技、CoreWeave等存储与算力基础设施。"
  },
  {
    "id": "wscn:3779662",
    "domain": "股票",
    "title": "黄金\"逼空\"进入第二阶段：宏观信号与技术面共振，4500美元成关键阻力",
    "url": "https://wallstreetcn.com/articles/3779662",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T02:20:56+00:00",
    "summary": "分析表示，黄金技术面21日与50日均线看涨交叉确立，宏观面与美联储利率预期及日本超长端利率双重共振回归。中国资金主导本轮涨势，亚洲交易所参与度从个位数跃升至50%，西方多头亦开始回归，黄金资金流入创年内单周新高。4500美元成关键阻力，期权策略或更具性价比。"
  },
  {
    "id": "wscn:3779659",
    "domain": "股票",
    "title": "中国AI基础设施的价值洼地：占全球85%的算力流量，仅10%的市场收入",
    "url": "https://wallstreetcn.com/articles/3779659",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T02:18:48+00:00",
    "summary": "中国AI模型已悄然承载全球85%至89%的智能体与代码生成流量，变现收入占比却仅10%至16%——这正是当前最被低估的套利机会。美国AI算力市值合计1750亿美元，中国同类资产仅约200亿美元，单CoreWeave的市值相当于中国三家头部算力公司的近四倍。万国数据创纪录预订量已率先验证基本面拐点，估值洼地与催化剂正同步浮现。"
  },
  {
    "id": "wscn:3779666",
    "domain": "股票",
    "title": "从技术故事到资本故事：AI建设周期的下一个主战场",
    "url": "https://wallstreetcn.com/articles/3779666",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T02:13:28+00:00",
    "summary": "美国超大规模云厂商大幅上调资本支出计划、公开与私募信贷市场加速介入AI基础设施融资、融资结构快速演进并向价值链更深处延伸——这一切在短短数月内集中发生，速度之快、范围之广、创新之多，超出市场预期。大摩认为，AI正在演变为资本市场故事，理解资本流向的重要性将不亚于理解技术创新本身。"
  },
  {
    "id": "wscn:3779626",
    "domain": "股票",
    "title": "美债供需结构压力向长端集中，供需缺口战略溢价提振铜价，东南亚多国贸易逆差扩张---0817宏观脱水",
    "url": "https://wallstreetcn.com/premium/articles/3779626?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T02:12:22+00:00",
    "summary": "美国财政可持续性风险难以收敛，TCJA、疫情补贴及大美丽法案等扩张政策持续推升美债供给，关税退税、美..."
  },
  {
    "id": "wscn:3779665",
    "domain": "股票",
    "title": "创A股历史纪录！中一签最高爆赚55万，“最贵新股”首日飙涨595%",
    "url": "https://wallstreetcn.com/articles/3779665",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T02:10:27+00:00",
    "summary": "年内最贵新股频准激光（N频准）8月18日登陆科创板，发行价186.88元刷新A股纪录，首日股价暴涨逾595%，中一签最高浮盈高达55.66万元，创新股首日收益历史之最。公司深耕精准激光器赛道，客户覆盖哈佛、MIT及国盾量子等顶尖机构，2025年营收4.18亿元、毛利率稳守67%高位。然而，开盘后市盈率飙至264倍，分析人士警示或已透支未来两三年业绩预期。"
  },
  {
    "id": "wscn:3779663",
    "domain": "股票",
    "title": "“太疯狂了”！韩国散户“从首尔转战华尔街”：买SK海力士ADR、押注三倍杠杆ETF",
    "url": "https://wallstreetcn.com/articles/3779663",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T01:54:17+00:00",
    "summary": "数据显示，韩国散户7月净买入美股约45亿美元。其中8.4亿美元流向SK海力士ADR，尽管溢价约10%。三倍杠杆半导体ETF SOXL位居韩国投资者最爱榜首，杠杆产品占十大买入标的四席。分析人士指出，韩国散户\"换场不换注\"，仍押注AI主题，ADR溢价与杠杆盛行是投机过热信号，或加剧局部市场波动。"
  },
  {
    "id": "wscn:3779660",
    "domain": "股票",
    "title": "海外流动性会出问题么？",
    "url": "https://wallstreetcn.com/articles/3779660",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T01:41:11+00:00",
    "summary": "中金认为，当前海外美元流动性未明显收紧，预计未来维持震荡，不至大幅收缩。三大核心因素中：美联储加息压力缓解；美债三季度供给扰动有限；静态看较难重演日元套息逆转风暴，需紧盯日元汇率。9月是关键节点，若因流动性引发市场回调，反而是更好的买入机会。"
  },
  {
    "id": "wscn:3779643",
    "domain": "股票",
    "title": "技术越成功 回调越必然",
    "url": "https://wallstreetcn.com/premium/articles/3779643?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T00:52:22+00:00",
    "summary": "铁路、无线电、互联网：三次技术都成功了，早期股东都被消灭了"
  },
  {
    "id": "wscn:3779658",
    "domain": "股票",
    "title": "Anthropico和OpenAI会停止向企业出售他们最先进的AI技术吗？",
    "url": "https://wallstreetcn.com/articles/3779658",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T00:51:31+00:00",
    "summary": "因加速布局垂直行业应用，Anthropic与OpenAI正悄然将API客户变成竞争对手——Canva已深陷其中，Harvey、Cursor开始自训模型自救。安全管控、防蒸馏、自营应用三重逻辑叠加，正推动两大AI巨头逐步收紧对外API的开放边界。"
  },
  {
    "id": "wscn:3779652",
    "domain": "股票",
    "title": "AI大战转折点？与管理层会面后，华尔街的感受：腾讯在打“中途岛战役”",
    "url": "https://wallstreetcn.com/articles/3779652",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T00:38:52+00:00",
    "summary": "美银美林将腾讯AI竞争格局比作\"中途岛战役\"——战争未终，但力量对比已悄然转变。报告显示，腾讯大手笔押注算力、加速混元模型迭代、双线推进WorkBuddy与小微落地，尽管折旧压力压缩近期利润，但当前市盈率远未反映其AI期权价值，维持买入评级，目标价780港元，较现价仍有逾77%上行空间。"
  },
  {
    "id": "wscn:3779651",
    "domain": "股票",
    "title": "Cursor一夜“干掉了”GitHub",
    "url": "https://wallstreetcn.com/articles/3779651",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T00:38:02+00:00",
    "summary": "GitHub突发大宕机之际，Cursor顺势推出专为AI Agent设计的代码托管平台Origin。它支持一键镜像并脱离GitHub，凭借堆叠式PR、AI自动解决冲突等功能，彻底颠覆了传统为“人”设计的慢节奏工作流。Cursor的终极猎物已变为GitHub。"
  },
  {
    "id": "hn:49311379",
    "domain": "股票",
    "title": "OpenAI talent exodus raises 'huge red flag' ahead of IPO",
    "url": "https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-08-15T15:25:16+00:00",
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
    "id": "rss:https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "domain": "股票",
    "title": "NEW POD! The Race to Secure a Bank Charter with Adam Shapiro of Klaros Group",
    "url": "https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-31T15:45:44+00:00",
    "summary": "Net Interest Extra ep 21"
  },
  {
    "id": "rss:https://www.netinterest.co/p/revolut-unbound",
    "domain": "股票",
    "title": "Revolut Unbound",
    "url": "https://www.netinterest.co/p/revolut-unbound",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-27T16:20:38+00:00",
    "summary": "The Quest to Build the World&#8217;s First Truly Global Bank"
  },
  {
    "id": "hn:49325159",
    "domain": "金融",
    "title": "The federal keyword lists that canceled billions in research funding",
    "url": "https://www.highereddive.com/news/inside-the-federal-keyword-lists-that-canceled-billions-in-research-funding/826203/",
    "source": "walrus01",
    "platform": "hackernews",
    "points": 278,
    "published_at": "2026-08-17T00:14:10+00:00",
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
    "points": 78,
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
    "id": "rss:https://arxiv.org/abs/2608.13745",
    "domain": "金融",
    "title": "Dynamic Physical Hedging amid Jump Losses, Reconstruction-Price Uncertainty, Population Interactions",
    "url": "https://arxiv.org/abs/2608.13745",
    "source": "Paramahansa Pramanik, Michael Bowdin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.13745v1 Announce Type: new Abstract: We study dynamic physical hedging for insurers exposed jointly to catastrophe losses and stochastic reconstruction costs. Surplus evolves as a controlle"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13775",
    "domain": "金融",
    "title": "Structured Payment in Pawnshop Borrowing: Mandates vs. Choice",
    "url": "https://arxiv.org/abs/2608.13775",
    "source": "Francis J. DiTraglia, Craig McIntosh, Isaac Meza, Joyce Sadka, Enrique Seira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.13775v1 Announce Type: new Abstract: Pawn loans offer borrowers a substantial degree of repayment flexibility in exchange for a harsh penalty in case of default: forfeit of collateral worth"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13871",
    "domain": "金融",
    "title": "Financial Technologies, Labor Markets, and Wage Inequality: Evidence from Instant Payment Systems",
    "url": "https://arxiv.org/abs/2608.13871",
    "source": "Carlos Burga, Jacelly Cespedes, Carlos Parra, Bernardo Ricca",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.13871v1 Announce Type: new Abstract: While technological innovations typically increase wage inequality by favoring skilled workers, we show that instant payment systems instead reduce it. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14141",
    "domain": "金融",
    "title": "Who Owns the Online Media?",
    "url": "https://arxiv.org/abs/2608.14141",
    "source": "Ulrich Matter, Philine Widmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.14141v1 Announce Type: new Abstract: Ownership matters for the media's watchdog role. We map the ownership networks behind thousands of online news outlets in the U.S., Canada, and Europe. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14164",
    "domain": "金融",
    "title": "Science under Threat? A Natural Experiment in Economics",
    "url": "https://arxiv.org/abs/2608.14164",
    "source": "Dominic Rohner, Oliver Vanden Eynde, Philine Widmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.14164v1 Announce Type: new Abstract: Academic freedom has come under growing strain worldwide. To study whether and how academics respond to political pressure, we exploit a natural experim"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14256",
    "domain": "金融",
    "title": "An ergodic theorem for multi-period mutual insurance",
    "url": "https://arxiv.org/abs/2608.14256",
    "source": "John Armstrong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.14256v1 Announce Type: new Abstract: Suppose there are $N$ heterogeneous agents in a market with idiosyncratic risks but no uninsurable systematic risk factors. These agents may agree arbit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14323",
    "domain": "金融",
    "title": "Dependence-Informed Sparse Neural Architecture for Stock Return Prediction",
    "url": "https://arxiv.org/abs/2608.14323",
    "source": "Hongyu Lin, Yulin Chen, Yuanrong Wang, Antonio Briola, Tomaso Aste",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.14323v1 Announce Type: new Abstract: Using neural networks for stock return prediction typically requires choices about depth and hidden-layer width that are difficult to connect to financi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13732",
    "domain": "金融",
    "title": "On the First Hitting Time Problems for Diffusion Processes: Local Time-Space Approach",
    "url": "https://arxiv.org/abs/2608.13732",
    "source": "Jerome Detemple, Yerkin Kitapbayev, Danila Shabalin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.13732v1 Announce Type: cross Abstract: Using the local time-space calculus of Peskir (2005) and the method developed in Mijatovic (2010), we derive a new integral representation for the dis"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13979",
    "domain": "金融",
    "title": "Systemic Risk in Financial Networks Revisited: Debt Dilution as a Backdoor Bail-in",
    "url": "https://arxiv.org/abs/2608.13979",
    "source": "Jason Roderick Donaldson, Giorgia Piacentino, Xiaobo Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.13979v1 Announce Type: cross Abstract: We develop a model of interbank networks with random liquidity shocks. Networks of dilutable debt---e.g., long-term, unsecured---facilitate efficient "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14014",
    "domain": "金融",
    "title": "Buy the Rumor, Sell the News: When Is News Priced In?",
    "url": "https://arxiv.org/abs/2608.14014",
    "source": "Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Sid Ghatak, Arman Khaledian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.14014v1 Announce Type: cross Abstract: Two old market sayings hold that news is already priced in by the time it is published, and that the rumor is bought while the news is sold. Both plac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.14134",
    "domain": "金融",
    "title": "Photonic Quantum Computing vs. Classical Solvers in Constrained Factor Portfolio Optimization",
    "url": "https://arxiv.org/abs/2608.14134",
    "source": "Nirvik Sahoo, Chyng Wen Tee, Paul Robert Griffin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.14134v1 Announce Type: cross Abstract: The authors present a rigorous empirical evaluation of three distinct optimization paradigms for institutional factor portfolio construction: an entro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2108.08097",
    "domain": "金融",
    "title": "Cognitive Ability and Tournament Entry: Evidence from Three Korean Populations",
    "url": "https://arxiv.org/abs/2108.08097",
    "source": "Syngjoo Choi, Byung-Yeon Kim, Jungmin Lee, Sokbae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2108.08097v3 Announce Type: replace Abstract: We compare tournament entry among three Korean groups raised in different institutional environments: South Korea, North Korea, and China. Experimen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.20238",
    "domain": "金融",
    "title": "Large Language Models Polarize Ideologically but Moderate Affectively in Online Political Discourse",
    "url": "https://arxiv.org/abs/2601.20238",
    "source": "Gavin Wang, Srinaath Anbudurai, Oliver Sun, Xitong Li, Lynn Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2601.20238v2 Announce Type: replace Abstract: The emergence of large language models (LLMs) is reshaping how people engage in political discourse online. We examine how the release of ChatGPT al"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02823",
    "domain": "金融",
    "title": "Pump.fun Graduation Regime Windows: Survival Analysis of 832,941 Token Launches and the Social-Presence Effect",
    "url": "https://arxiv.org/abs/2607.02823",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2607.02823v2 Announce Type: replace Abstract: Kaplan-Meier and Cox proportional-hazards survival analysis of 832,941 Solana pump.fun token launches, observed 2026-05-08 to 2026-06-10. Pooled gra"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05802",
    "domain": "金融",
    "title": "Failure Privacy and Safe Collective Expression with Social Assurance Contracts",
    "url": "https://arxiv.org/abs/2607.05802",
    "source": "Matthew Cashman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2607.05802v5 Announce Type: replace Abstract: Controversial views sometimes remain unspoken because they invite retaliation. However, a sufficiently large group could speak safely if only they s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12424",
    "domain": "金融",
    "title": "AI-Driven Multiscenario Interest Rate Forecasting: A Proof of Concept for Banking Asset Management",
    "url": "https://arxiv.org/abs/2608.12424",
    "source": "Ekkehardt Bauer, Dirk Holl\\\"ander, David Scholz, Linus Wolff, Christoph Ostermair, Kyrillus Aiad, Joachim Hasebrook",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2608.12424v2 Announce Type: replace Abstract: This study focuses on developing an AI-supported prototype for multiperspective interest rate forecasting that combines classical econometric models"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.19294",
    "domain": "金融",
    "title": "Duality and Policy Evaluation in Distributionally Robust Bayesian Diffusion Control",
    "url": "https://arxiv.org/abs/2506.19294",
    "source": "Jose Blanchet, Jiayi Cheng, Yuewei Ling, Hao Liu, Yang Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2506.19294v4 Announce Type: replace-cross Abstract: We study diffusion control problems under parameter uncertainty. Controllers based on plug-in estimation can be brittle due to potential distr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.01408",
    "domain": "金融",
    "title": "Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections",
    "url": "https://arxiv.org/abs/2512.01408",
    "source": "Jose Blanchet, Jiayi Cheng, Hao Liu, Yang Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2512.01408v2 Announce Type: replace-cross Abstract: We revisit Merton's continuous-time portfolio selection through a data-driven, distributionally robust lens. Our aim is to tap the benefits of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.23596",
    "domain": "金融",
    "title": "The Nonstationarity-Complexity Tradeoff in Return Prediction",
    "url": "https://arxiv.org/abs/2512.23596",
    "source": "Agostino Capponi, Chengpiao Huang, J. Antonio Sidaoui, Kaizheng Wang, Jiacheng Zou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T04:00:00+00:00",
    "summary": "arXiv:2512.23596v2 Announce Type: replace-cross Abstract: Does more data improve return prediction? In non-stationary financial markets, longer training windows improve prediction of complex models bu"
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
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T20:11:15+00:00",
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
    "id": "hn:49190429",
    "domain": "金融",
    "title": "Data shows just how hard Tesla's Cybertruck has flopped",
    "url": "https://www.msn.com/en-us/autos/general/this-data-shows-just-how-hard-tesla-s-cybertruck-has-actually-flopped/ar-AA29sikQ",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T23:25:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49208461",
    "domain": "金融",
    "title": "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions",
    "url": "https://www.wsj.com/finance/investing/new-intelligence-warns-russia-may-provoke-nato-amid-dwindling-u-s-munitions-68f497c7",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-07T10:52:27+00:00",
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
    "id": "hn:49033778",
    "domain": "金融",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
  }
]
```
