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

- 今日日期：`2026-10-15`
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
  "date": "2026-10-15",
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
    "points": 1972938,
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
    "points": 1398719,
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
    "points": 1346170,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1187926,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1122467,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 899703,
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
    "points": 853697,
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
    "points": 715831,
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
    "points": 528134,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1Nyp96pEGD",
    "domain": "AI",
    "title": "人人都要学！Agent 视觉创作全流程～【小白教程】",
    "url": "http://www.bilibili.com/video/av117427342017510",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 397373,
    "published_at": "2026-10-12T10:30:00+00:00",
    "summary": "做PPT、商品图、广告片！\n从活动策划到TVC成片，一期带你跑通创作型Agent全流程！\n感谢铁铁们的三连+关注～"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 356318,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 354762,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 320322,
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
    "points": 306866,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 283544,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1Qub56eEYj",
    "domain": "AI",
    "title": "【全30集】“番茄+豆包+即梦+红果”从零开始学AI漫剧制作教程！附全流程操作演示！让零基础也能学会AI漫剧制作技巧！更多AI漫剧变现方法拿走不谢~",
    "url": "http://www.bilibili.com/video/av117234722740875",
    "source": "哔哩学院AI教程",
    "platform": "bilibili",
    "points": 280705,
    "published_at": "2026-09-08T09:44:20+00:00",
    "summary": "本套教程从零开始讲解，手把手教学，无论是新手小白，还是有一定经验的选手，皆可学习~\n配套工具软件 | 素材 | AIGC | 即梦AI | SD2.0等学习路线\n分享给各位还在寻找资料宝子们！一键三联抱走吖\n视频制作不易，同学们觉得对你有帮助的话记得点点关注，一键三连【666】感谢支持！！"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 278160,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 274249,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 205468,
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
    "points": 183653,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 159554,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 148132,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV1d2pF6nEqZ",
    "domain": "AI",
    "title": "当你团队都在vibe coding",
    "url": "http://www.bilibili.com/video/av117392663450931",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 146003,
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
    "points": 135327,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1Am9kBfEMN",
    "domain": "AI",
    "title": "AI智能体赋能课堂教学——技术很简单，难的是想法",
    "url": "http://www.bilibili.com/video/av116482180647922",
    "source": "爱可可-爱生活",
    "platform": "bilibili",
    "points": 102486,
    "published_at": "2026-04-28T11:55:25+00:00",
    "summary": "在AI迅猛发展的今天，课堂正在悄然发生变化。\n但真正的挑战，从来不是“会不会用工具”，而是——我们究竟希望学生学会什么？\n\n本讲座不教软件操作，不演示平台使用，\n而是聚焦一个更关键的问题：\n如何借助AI，让那些我们一直想实现却做不到的教学理想成为现实。\n\n通过真实课堂案例与可落地的方法模型，讲座将带领教师完成一次思维升级：\n从“让AI替你干活”，转向“用AI创造更好的学习体验”\n从“提高效率”，走"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 102169,
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
    "points": 94045,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 90217,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 87947,
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
    "points": 76312,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1713u6XE1D",
    "domain": "AI",
    "title": "Claude Code 完全接管了 Blender，然后创造了这个",
    "url": "http://www.bilibili.com/video/av116980883398142",
    "source": "stefan_3d_ai",
    "platform": "bilibili",
    "points": 68024,
    "published_at": "2026-07-26T11:00:00+00:00",
    "summary": "如果你给一个完全自主的 AI 代理提供对 Blender 的完整终端控制权限，并让它完完全全靠自己独立运行整整一个小时，到底会发生什么可怕的事情？\n\n在这个视频中，我远远超越了简单的代码复制粘贴，结合 Claude Code 和全新发布的官方 Blender MCP 服务器，深入探索了真正的 3D 工作流自动化究竟长什么样。\n\n---\n\n🔹 试用 Tripo AI 并免费获取 500 生成积分：h"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 65311,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV15Vhy6cEhd",
    "domain": "AI",
    "title": "通俗易懂地讲解什么是Agent？",
    "url": "http://www.bilibili.com/video/av117330906449673",
    "source": "洪涛同学LovTech",
    "platform": "bilibili",
    "points": 63216,
    "published_at": "2026-09-25T09:12:59+00:00",
    "summary": "从0到1搭建一个简易Agent，从小白的角度出发解释Agent是如何运行的？"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56018,
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
    "points": 49253,
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
    "points": 40590,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28998,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 24549,
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
    "points": 22808,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SmpD6QEuX",
    "domain": "AI",
    "title": "【Opus5.6】灰测性能前瞻 Claude Opus56 多则测试例「前端 工程」表现速览",
    "url": "http://www.bilibili.com/video/av117424707865238",
    "source": "小小小名不是小明",
    "platform": "bilibili",
    "points": 21880,
    "published_at": "2026-10-11T22:50:10+00:00",
    "summary": "**注意！！** 此视频中所有成果都来自于网页code模式"
  },
  {
    "id": "bvid:BV1nChG6nEY4",
    "domain": "AI",
    "title": "韦东山老师教你用 DeepSeek 与 Claude Code，在 Ubuntu 中搭建嵌入式 Linux AI 开发环境：从安装配置到代码智能辅助开发实战",
    "url": "http://www.bilibili.com/video/av117155165177009",
    "source": "韦东山",
    "platform": "bilibili",
    "points": 21778,
    "published_at": "2026-08-25T08:22:35+00:00",
    "summary": "韦东山老师手把手教你在 Ubuntu 中搭建嵌入式 AI 开发环境，完整介绍开发工具、VMware Tools、中文输入法、VS Code 与常用插件的安装配置，以及 DeepSeek API Key 和 Claude Code 的接入方法。借助 AI 大模型完成代码分析、工程理解、问题排查和辅助开发，让嵌入式 Linux 学习与开发更加高效。\n查看完整文字教程：https://www.100as"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 21617,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1y7Jr66Epx",
    "domain": "AI",
    "title": "DeepSeek土豆服务器又炸了😅😅",
    "url": "http://www.bilibili.com/video/av117442273614674",
    "source": "yi碗米的日常",
    "platform": "bilibili",
    "points": 21264,
    "published_at": "2026-10-15T01:16:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 19225,
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
    "points": 17735,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV15phrzqEzK",
    "domain": "AI",
    "title": "【Claude Code Router】一键直连五大模型",
    "url": "http://www.bilibili.com/video/av115121162553281",
    "source": "她笑中藏泪花",
    "platform": "bilibili",
    "points": 17580,
    "published_at": "2025-08-31T03:09:22+00:00",
    "summary": "Claude Code Router 教程：手把手完成 CCR 配置与 PROXY_URL 代理，一次直连 Gemini、Kimi、DeepSeek、GLM、Qwen，区分 Anthropic 与 OpenAI 端点，并附 /model 切换与报错速查。点击查看。\n博文链接：https://rosetears.cn/archives/61/"
  },
  {
    "id": "bvid:BV1wpJr6MEff",
    "domain": "AI",
    "title": "DeepSeek似乎炸了…？为什么显示的是服务器不可用？有人能解释一下怎么了吗？",
    "url": "http://www.bilibili.com/video/av117442290456464",
    "source": "洛英-更新中",
    "platform": "bilibili",
    "points": 16447,
    "published_at": "2026-10-15T01:21:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 14135,
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
    "points": 12534,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1TtwCehEzG",
    "domain": "AI",
    "title": "cursor新手必会的怎么回退代码 防止改错改乱代码 提高效率开发",
    "url": "http://www.bilibili.com/video/av113855472605087",
    "source": "项目禅",
    "platform": "bilibili",
    "points": 11512,
    "published_at": "2025-01-19T14:29:21+00:00",
    "summary": ""
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
    "id": "hn:50086363",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's first GPU: GeForce 256",
    "url": "https://dfarq.homeip.net/nvidias-first-gpu-geforce-256/",
    "source": "ibobev",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-10-14T12:05:44+00:00",
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
    "id": "hn:50081435",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reportedly Ending the RTX 5090, Reserves GB202 for Workstation GPUs",
    "url": "https://www.techpowerup.com/353578/nvidia-reportedly-ending-the-rtx-5090-reserves-gb202-silicon-for-workstation-gpus",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-10-14T01:52:56+00:00",
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
    "id": "rss:https://www.eetimes.com/grid-modernization-hidden-cost-a-growing-attack-surface-few-are-watching/",
    "domain": "AI 算力 / 半导体",
    "title": "Grid Modernization’s Hidden Cost: A Growing Attack Surface Few Are Watching",
    "url": "https://www.eetimes.com/grid-modernization-hidden-cost-a-growing-attack-surface-few-are-watching/",
    "source": "David Montoya",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T08:00:00+00:00",
    "summary": "Grid modernization is expanding the energy sector’s cyberattack surface, while limited visibility across IT and OT networks leaves connected assets exposed. The post Grid Modernization’s Hidden Cost: "
  },
  {
    "id": "rss:https://www.eetimes.com/benchmark-electronics-thailand-operations-focus-on-high-mix-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "Benchmark Electronics’ Thailand Operations Focus on High-Mix Manufacturing",
    "url": "https://www.eetimes.com/benchmark-electronics-thailand-operations-focus-on-high-mix-manufacturing/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T19:34:54+00:00",
    "summary": "Benchmark Electronics combines engineering expertise, workforce development, and flexible production to expand high-mix electronics manufacturing across Thailand. The post Benchmark Electronics’ Thail"
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-lithography-3d-scaling-puts-new-demands-on-materials/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond Lithography: 3D Scaling Puts New Demands on Materials",
    "url": "https://www.eetimes.com/beyond-lithography-3d-scaling-puts-new-demands-on-materials/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:29:24+00:00",
    "summary": "ASM International shows how building increasingly complex 3D devices requires advances in materials and processes. The post Beyond Lithography: 3D Scaling Puts New Demands on Materials appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/co-packaged-optics-moves-from-promise-to-production-planning/",
    "domain": "AI 算力 / 半导体",
    "title": "Co-Packaged Optics Moves from Promise to Production Planning",
    "url": "https://www.eetimes.com/co-packaged-optics-moves-from-promise-to-production-planning/",
    "source": "Ayar Labs",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T15:41:12+00:00",
    "summary": "At Ayar Labs CPO Summit, Meta, Broadcom, AMD, and others weighed in on readiness for a 2028 co-packaged optics demand surge and the OCI MSA’s role. The post Co-Packaged Optics Moves from Promise to Pr"
  },
  {
    "id": "rss:https://www.eetimes.com/vicfuse-ul-standard-class-series-fuse-holders-quality-reliability-and-industrial-protection/",
    "domain": "AI 算力 / 半导体",
    "title": "VICFUSE UL Standard Class Series Fuse Holders: Quality, Reliability, and Industrial Protection",
    "url": "https://www.eetimes.com/vicfuse-ul-standard-class-series-fuse-holders-quality-reliability-and-industrial-protection/",
    "source": "ALI",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T13:00:00+00:00",
    "summary": "Explore VICFUSE's Class CF fuse line, which offers current-limiting technology and meets Class J performance standards in a compact design. The post VICFUSE UL Standard Class Series Fuse Holders: Qual"
  },
  {
    "id": "rss:https://www.eetimes.com/tie-showcases-taiwans-push-to-deploy-ai-across-industries/",
    "domain": "AI 算力 / 半导体",
    "title": "TIE Showcases Taiwan’s Push to Deploy AI Across Industries",
    "url": "https://www.eetimes.com/tie-showcases-taiwans-push-to-deploy-ai-across-industries/",
    "source": "EE Times Taiwan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T13:00:00+00:00",
    "summary": "Discover how Taiwan Innotech Expo 2026 showcased AI solutions designed to advance industries with practical, real-world impact The post TIE Showcases Taiwan’s Push to Deploy AI Across Industries appea"
  },
  {
    "id": "rss:https://www.eetimes.com/asml-euv-expansion-runs-through-zeiss/",
    "domain": "AI 算力 / 半导体",
    "title": "ASML’s EUV Expansion Runs Through Zeiss",
    "url": "https://www.eetimes.com/asml-euv-expansion-runs-through-zeiss/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T12:49:10+00:00",
    "summary": "ASML’s plans to expand EUV production depend partly on Zeiss’s ability to increase qualified precision-optics output. The post ASML’s EUV Expansion Runs Through Zeiss appeared first on EE Times."
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
    "id": "rss:https://www.tomshardware.com/tech-industry/grace-hopper-celebration-for-women-in-computing-canceled-two-weeks-out-anitab-org-says-registrations-and-sponsorships-fell-short-of-covering-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Grace Hopper Celebration canceled two weeks out as AnitaB.org runs short of funds",
    "url": "https://www.tomshardware.com/tech-industry/grace-hopper-celebration-for-women-in-computing-canceled-two-weeks-out-anitab-org-says-registrations-and-sponsorships-fell-short-of-covering-costs",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:09:38+00:00",
    "summary": "AnitaB.org canceled this month’s Grace Hopper Celebration in Anaheim, saying registrations and sponsorships couldn’t cover its costs."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/gfiber-and-qualcomm-announce-wi-fi-8-gateway-20-gig-customers-to-be-first-to-receive-next-gen-wireless-upgrade",
    "domain": "AI 算力 / 半导体",
    "title": "GFiber and Qualcomm announce Wi-Fi 8 gateway",
    "url": "https://www.tomshardware.com/networking/routers/gfiber-and-qualcomm-announce-wi-fi-8-gateway-20-gig-customers-to-be-first-to-receive-next-gen-wireless-upgrade",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T16:28:03+00:00",
    "summary": "Wi-Fi 8 hasn't been certified by the IEEE yet, but hardware announcements are still ramping up"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/epic-games-vibe-codes-new-launcher-because-programming-is-hard-starts-46-percent-faster-than-steam-preview-is-available-now-but-not-recommended-for-competitive-players",
    "domain": "AI 算力 / 半导体",
    "title": "Epic Games vibe codes new launcher because 'programming is hard,' claims it starts 46% faster than Steam",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/epic-games-vibe-codes-new-launcher-because-programming-is-hard-starts-46-percent-faster-than-steam-preview-is-available-now-but-not-recommended-for-competitive-players",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T15:44:45+00:00",
    "summary": "Epic Games has introduced a redesigned launcher into preview, which the company says it vibe coded because \"programming is hard.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fbi-shuts-down-over-40-north-korean-laptop-farms-used-by-fake-remote-workers-over-200-devices-seized-in-texas-although-no-arrests-were-made-so-far",
    "domain": "AI 算力 / 半导体",
    "title": "FBI shuts down over 40 North Korean laptop farms used by fake remote workers",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fbi-shuts-down-over-40-north-korean-laptop-farms-used-by-fake-remote-workers-over-200-devices-seized-in-texas-although-no-arrests-were-made-so-far",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T14:41:34+00:00",
    "summary": "CrowdStrike has helped the FBI identify these sites, which Pyongyang uses to earn as much as $500 million annually to help fund its nuclear and other weapons programs."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/the-official-toms-hardware-app-is-here-30-years-of-tech-coverage-and-benchmarks-in-your-pocket",
    "domain": "AI 算力 / 半导体",
    "title": "The official Tom’s Hardware app is here — 30 years of tech coverage and benchmarks in your pocket",
    "url": "https://www.tomshardware.com/software/applications/the-official-toms-hardware-app-is-here-30-years-of-tech-coverage-and-benchmarks-in-your-pocket",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T14:10:00+00:00",
    "summary": "Today we’re introducing the Tom's Hardware app, a faster, easier way to access all of our content while on the go."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-place-custom-tiny-cpu-cores-in-its-ssd-controllers-to-ease-arm-load-as-drive-speeds-rocket-each-h-tpu-reportedly-draws-2-5-percent-of-a-cpu-cores-power",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix to place custom tiny CPU cores in its SSD controllers to ease Arm load as drive speeds rocket",
    "url": "https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-place-custom-tiny-cpu-cores-in-its-ssd-controllers-to-ease-arm-load-as-drive-speeds-rocket-each-h-tpu-reportedly-draws-2-5-percent-of-a-cpu-cores-power",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T14:00:00+00:00",
    "summary": "SK hynix detailed H-TPU, tiny in-house cores that offload routine I/O from the Arm CPUs in its next enterprise SSD controllers."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-homebrew-storefront-with-over-1-600-free-ps5-and-ps4-games-taken-down-by-sony-company-plays-piracy-whack-a-mole-as-two-further-repos-spring-up",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 homebrew storefront with over 1,600 free PS5 and PS4 games taken down by Sony",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-homebrew-storefront-with-over-1-600-free-ps5-and-ps4-games-taken-down-by-sony-company-plays-piracy-whack-a-mole-as-two-further-repos-spring-up",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T13:45:22+00:00",
    "summary": "Over 1,600 PS4 and PS5 games have been made free on jailbroken PS5 units thanks to Overdrive. The homebrew was quickly shut down after going viral, but was quickly revived through forks and re-release"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/spacex-limits-starlink-service-for-ukraines-high-speed-military-drones-without-prior-warning-ukrainian-officials-say-limitation-significantly-complicates-logistics-and-drone-operations",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX limits Starlink service for Ukraine’s high-speed military drones without prior warning",
    "url": "https://www.tomshardware.com/tech-industry/drones/spacex-limits-starlink-service-for-ukraines-high-speed-military-drones-without-prior-warning-ukrainian-officials-say-limitation-significantly-complicates-logistics-and-drone-operations",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T13:04:33+00:00",
    "summary": "Ukrainian officials say SpaceX imposed new speed restrictions on military-grade Starlink terminals without warning, disrupting drone and logistics missions and forcing some operations to be canceled"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/analyzing-intels-emib-and-foveros-advanced-packaging-roadmaps-how-intel-plans-to-scale-chips-in-every-direction",
    "domain": "AI 算力 / 半导体",
    "title": "Analyzing Intel's EMIB and Foveros advanced packaging roadmaps",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/analyzing-intels-emib-and-foveros-advanced-packaging-roadmaps-how-intel-plans-to-scale-chips-in-every-direction",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T12:50:00+00:00",
    "summary": "Intel was the first large chipmaker to start using advanced packaging methods in 2017 – 2019. But where are Intel's EMIB and Foveros technologies today and where are they heading?"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-will-reportedly-receive-its-first-euv-tool-from-asml-in-mid-2027-cutting-edge-scanner-could-sit-idle-for-some-time-as-experimental-facility-is-completed",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's Terafab will reportedly receive its first EUV tool from ASML in mid-2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-will-reportedly-receive-its-first-euv-tool-from-asml-in-mid-2027-cutting-edge-scanner-could-sit-idle-for-some-time-as-experimental-facility-is-completed",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T12:30:00+00:00",
    "summary": "Elon Musk may prefer FEL light sources for in-house chip production, but Terafab will start with proven tech from ASML."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/qualcomm-wins-architecture-breach-verdict-against-arm-but-gets-just-usd2-judge-could-still-suspend-royalty-fees-for-five-years",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm wins architecture breach verdict against Arm but gets just $2",
    "url": "https://www.tomshardware.com/pc-components/cpus/qualcomm-wins-architecture-breach-verdict-against-arm-but-gets-just-usd2-judge-could-still-suspend-royalty-fees-for-five-years",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T12:10:00+00:00",
    "summary": "A federal jury sides with Arm on select issues, rules in favor of Qualcomm in other cases. The legal battle set to continue."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/saudi-openai-engineer-arrested-for-allegedly-planting-usd14-recording-device-in-company-office-cheap-microcontroller-was-meant-to-secretly-capture-sensitive-communications-about-the-companys-super-intelligence-technology",
    "domain": "AI 算力 / 半导体",
    "title": "Saudi OpenAI engineer arrested for allegedly planting $14 recording device in company office",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/saudi-openai-engineer-arrested-for-allegedly-planting-usd14-recording-device-in-company-office-cheap-microcontroller-was-meant-to-secretly-capture-sensitive-communications-about-the-companys-super-intelligence-technology",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T11:48:41+00:00",
    "summary": "An OpenAI engineer has been charged with using or endeavoring to use an electronic, mechanical, or other device to intercept oral communications and is facing up to five years in prison plus a $250,00"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/the-imf-highlights-how-a-financial-wipeout-in-the-ai-sector-could-become-a-global-contagion-agency-report-shines-light-on-circular-economics-and-leveraged-loans",
    "domain": "AI 算力 / 半导体",
    "title": "AI sector wipeout risks global financial contagion, IMF report warns",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/the-imf-highlights-how-a-financial-wipeout-in-the-ai-sector-could-become-a-global-contagion-agency-report-shines-light-on-circular-economics-and-leveraged-loans",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T11:35:00+00:00",
    "summary": "The International Monetary Fund has produced a report examining how financing for the global AI buildout could result in contagion should the industry fail to produce its promised profits."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/offset-extortionate-memory-pricing-with-32gb-of-ddr5-6000-ram-for-usd151-with-this-9800x3d-bundle-combo-also-features-an-x870e-mobo-aio-cooler-onimusha-game-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Offset extortionate memory pricing with 32GB of DDR5-6000 RAM for $151 with this 9800X3D bundle",
    "url": "https://www.tomshardware.com/pc-components/offset-extortionate-memory-pricing-with-32gb-of-ddr5-6000-ram-for-usd151-with-this-9800x3d-bundle-combo-also-features-an-x870e-mobo-aio-cooler-onimusha-game-and-a-2tb-ssd",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T11:20:58+00:00",
    "summary": "Offset high memory and storage prices with a combo deal from Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-researchers-turn-idle-macs-into-a-virtual-gpu-cloud-with-minions-researchers-say-the-distributed-scheme-could-scale-globally-and-support-model-training",
    "domain": "AI 算力 / 半导体",
    "title": "Apple researchers turn idle Macs into a virtual GPU cloud with ‘Minions’",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-researchers-turn-idle-macs-into-a-virtual-gpu-cloud-with-minions-researchers-say-the-distributed-scheme-could-scale-globally-and-support-model-training",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T11:15:00+00:00",
    "summary": "Apple researchers describe Minions, an internal system that runs AI inference jobs on idle Apple Silicon Macs when GPUs are scarce."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/ledger-to-review-sales-and-anti-tamper-policies-after-usd93-million-hardware-wallet-supply-chain-attack-rogue-lte-implants-reportedly-stole-users-recovery-phrases",
    "domain": "AI 算力 / 半导体",
    "title": "After a $93 million crypto hardware-wallet supply chain attack, Ledger to review sales and anti-tamper policies",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/ledger-to-review-sales-and-anti-tamper-policies-after-usd93-million-hardware-wallet-supply-chain-attack-rogue-lte-implants-reportedly-stole-users-recovery-phrases",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T10:50:00+00:00",
    "summary": "Ledger is reviewing chain-of-custody practices and anti-tamper protections after modified hardware wallets sold through a third party were allegedly fitted with LTE implants that captured recovery phr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-gpu-prices-spike-in-japan-prices-up-to-41-percent-higher-than-amazon-us-rtx-5060-ti-sees-the-biggest-increase-among-the-rtx-50-series-stack",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia GPU prices spike in Japan; prices up to 41% higher than Amazon US",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-gpu-prices-spike-in-japan-prices-up-to-41-percent-higher-than-amazon-us-rtx-5060-ti-sees-the-biggest-increase-among-the-rtx-50-series-stack",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T10:25:00+00:00",
    "summary": "A Japanese retailer has increased the prices of RTX 50-series GPUs between 12.71% and 41.10%, with the mainstream models bearing the brunt of the price increases."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-6000-ram-now-costs-usd450-ai-induced-shortage-reaches-worst-milestone-yet",
    "domain": "AI 算力 / 半导体",
    "title": "32GB of DDR5 6000 RAM now costs $450",
    "url": "https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-6000-ram-now-costs-usd450-ai-induced-shortage-reaches-worst-milestone-yet",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T10:10:36+00:00",
    "summary": "32GB of DDR5 6000 RAM now costs $450, as supply for consumer DIMMs remains constrained."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/modder-put-dlss-5-4x-multipass-on-1996-quake-looks-worse-than-rtx-modded-quake",
    "domain": "AI 算力 / 半导体",
    "title": "Modder injects leaked DLSS 5 4x Multipass on 1996 Quake",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/modder-put-dlss-5-4x-multipass-on-1996-quake-looks-worse-than-rtx-modded-quake",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T10:00:00+00:00",
    "summary": "Ukrainian modder puts DLSS 5 over the original Quake, and the results are not impressive compared to the RTX Quake mod."
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
    "points": 1447,
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
    "points": 774,
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
    "points": 231,
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
    "id": "rss:https://www.theverge.com/news/1011654/mckinsey-ai-client-interview",
    "domain": "大厂 AI 动态",
    "title": "McKinsey is making job applicants spar with a fake AI client",
    "url": "https://www.theverge.com/news/1011654/mckinsey-ai-client-interview",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T22:53:31+00:00",
    "summary": "Consulting firm McKinsey &#38; Company is going to ask some entry-level candidates to have a 10-minute conversation with an AI simulation of a client as part of the interview process, according to The"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1011431/apple-homeview-smart-display-best-feature",
    "domain": "大厂 AI 动态",
    "title": "The best feature of Apple’s HomeView might be its simplicity",
    "url": "https://www.theverge.com/tech/1011431/apple-homeview-smart-display-best-feature",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T22:00:02+00:00",
    "summary": "I'm just going to come right out and say it. I love the approach Apple has taken with the HomeView. I think it's the shared, always-available household interface that my family might finally use. Is A"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1011500/openai-state-lawsuits-chatgpt-safety",
    "domain": "大厂 AI 动态",
    "title": "Eight states sue OpenAI, saying ChatGPT isn&#8217;t safe for kids",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1011500/openai-state-lawsuits-chatgpt-safety",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T21:11:28+00:00",
    "summary": "OpenAI is facing a new wave of lawsuits from eight US states that accuse the company of harming children and misleading customers about the safety of ChatGPT, as reported earlier by Reuters. The lawsu"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1011487/microsoft-scam-messages-marketplace-takedown",
    "domain": "大厂 AI 动态",
    "title": "Microsoft and Japan took down a cybercrime network behind over a billion scam messages",
    "url": "https://www.theverge.com/tech/1011487/microsoft-scam-messages-marketplace-takedown",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T20:03:43+00:00",
    "summary": "We've all gotten a scam text about a nonexistent parking ticket or a fake package delivery, but hopefully you'll start seeing fewer of them. Microsoft says it helped dismantle a marketplace for scamme"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1011311/the-ai-race-is-back-on",
    "domain": "大厂 AI 动态",
    "title": "The AI race is back on",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1011311/the-ai-race-is-back-on",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T19:06:03+00:00",
    "summary": "Last week, Anthropic and OpenAI looked like they had the AI race to themselves, pulling ahead with increasingly powerful models that left their rivals in the dust. Google seemed hopelessly far behind,"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1011417/new-york-ag-characterai-bankruptcy",
    "domain": "大厂 AI 动态",
    "title": "Now that Character.AI is going bankrupt, what happens to all of its users&#8217; data?",
    "url": "https://www.theverge.com/policy/1011417/new-york-ag-characterai-bankruptcy",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:47:54+00:00",
    "summary": "New York Attorney General Letitia James revealed a years-long multi-state investigation against Character.AI as they now seek to require protections on consumer data sold through its bankruptcy procee"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1011324/apple-tv-4k-missed-features",
    "domain": "大厂 AI 动态",
    "title": "As a TV enthusiast, I was hoping for more from the Apple TV 4K",
    "url": "https://www.theverge.com/tech/1011324/apple-tv-4k-missed-features",
    "source": "John Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:38:59+00:00",
    "summary": "It's been four long years since the last Apple TV 4K was released, and in that time there have been lots of hopes and dreams for features in whatever comes next. A new chip, 4K/120Hz support, audio pa"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1011369/youtube-music-ai-label",
    "domain": "大厂 AI 动态",
    "title": "YouTube sticks new labels on AI-generated songs",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1011369/youtube-music-ai-label",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:22:56+00:00",
    "summary": "YouTube is adding a \"Made with AI\" label to tracks that were \"altered or fully generated\" using AI, with a similar approach to its existing process for applying AI labels to videos. It doesn't sound l"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1010749/google-play-gift-card-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Save up to 20 percent on gift cards for REI, Barnes &#038; Noble, and more",
    "url": "https://www.theverge.com/gadgets/1010749/google-play-gift-card-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:20:55+00:00",
    "summary": "While we cover a lot of deals on specific products, it’s rare that we find worthwhile savings on gift cards that let you save on essentially anything the store sells. However, until October 19th, you "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1011227/apple-homeview-smart-display-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Apple&#8217;s new HomeView smart display is $10 cheaper at Amazon",
    "url": "https://www.theverge.com/gadgets/1011227/apple-homeview-smart-display-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T17:24:42+00:00",
    "summary": "Apple only just announced on Tuesday that its first smart display, the HomeView, will arrive on November 13th, but you can already save a couple bucks on it. Right now, you can buy the display for $28"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/figma-announces-new-features-to-define-how-agents-work-on-its-platform/",
    "domain": "大厂 AI 动态",
    "title": "Figma announces new features to define how agents work on its platform",
    "url": "https://techcrunch.com/2026/10/14/figma-announces-new-features-to-define-how-agents-work-on-its-platform/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:30:00+00:00",
    "summary": "Figma is also releasing its code layers feature in open beta."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/ricursive-intelligence-is-betting-on-ai-designed-chips-to-help-solve-the-compute-crisis/",
    "domain": "大厂 AI 动态",
    "title": "Ricursive Intelligence is betting on AI-designed chips to help solve the compute crisis",
    "url": "https://techcrunch.com/2026/10/14/ricursive-intelligence-is-betting-on-ai-designed-chips-to-help-solve-the-compute-crisis/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T01:01:32+00:00",
    "summary": "The founders detailed how their startup is developing AI that can design chips, learn from each iteration, and improve subsequent designs, all with the goal of automating and accelerating the chip des"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/flock-ceo-defends-surveillance-technology-amid-national-backlash-we-shouldnt-pause-progress/",
    "domain": "大厂 AI 动态",
    "title": "Flock CEO defends surveillance technology amid national backlash: ‘We shouldn’t pause progress’",
    "url": "https://techcrunch.com/2026/10/14/flock-ceo-defends-surveillance-technology-amid-national-backlash-we-shouldnt-pause-progress/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T00:49:31+00:00",
    "summary": "At TechCrunch Disrupt, Flock CEO Garrett Langley defended his company's surveillance technology despite growing privacy concerns, arguing that its crime-fighting benefits outweigh the risks of abuse."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/meet-the-five-companies-competing-in-the-startup-battlefield-finals-at-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Meet the five companies competing in the Startup Battlefield finals at Disrupt 2026",
    "url": "https://techcrunch.com/2026/10/14/meet-the-five-companies-competing-in-the-startup-battlefield-finals-at-disrupt-2026/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T00:30:00+00:00",
    "summary": "It’s time to unveil the five companies that will be competing in the Startup Battlefield finals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/gudea-leverages-ai-to-help-organizations-prevent-social-media-crises-before-they-erupt/",
    "domain": "大厂 AI 动态",
    "title": "Gudea leverages AI to help organizations prevent social media crises before they erupt",
    "url": "https://techcrunch.com/2026/10/14/gudea-leverages-ai-to-help-organizations-prevent-social-media-crises-before-they-erupt/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T00:00:00+00:00",
    "summary": "Every day, conversations unfold across social media and websites around the world. A seemingly insignificant post—whether it involves AI-generated misinformation, hate speech, or a damaging rumor—can "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/intero-biosystems-wants-drugmakers-to-test-on-mini-human-intestines-not-animals/",
    "domain": "大厂 AI 动态",
    "title": "Intero Biosystems wants drugmakers to test on mini human intestines, not animals",
    "url": "https://techcrunch.com/2026/10/14/intero-biosystems-wants-drugmakers-to-test-on-mini-human-intestines-not-animals/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T23:00:00+00:00",
    "summary": "Intero Biosystems is selling lab-grown human intestines to drugmakers as regulators push for alternatives to animal testing, while the startup looks to scale production and expand its organoid technol"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/cedardb-wants-one-database-to-handle-both-transactions-and-analytics-as-ai-agents-raise-the-stakes/",
    "domain": "大厂 AI 动态",
    "title": "CedarDB wants one database to handle both transactions and analytics, as AI agents raise the stakes",
    "url": "https://techcrunch.com/2026/10/14/cedardb-wants-one-database-to-handle-both-transactions-and-analytics-as-ai-agents-raise-the-stakes/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T22:00:00+00:00",
    "summary": "Databases have traditionally been designed either for analytical data or for operational data. But database engine CedarDB supports both, and its approach has gained relevance with the rise of agentic"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/ambanis-jio-seeks-to-raise-3-2b-in-what-could-be-indias-biggest-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Ambani’s Jio seeks to raise $3.2B in what could be India’s biggest IPO",
    "url": "https://techcrunch.com/2026/10/14/ambanis-jio-seeks-to-raise-3-2b-in-what-could-be-indias-biggest-ipo/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T21:48:20+00:00",
    "summary": "Jio plans to use most of its IPO proceeds to repay debt as it expands beyond telecom."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/flock-ceo-says-its-microphones-detect-just-gunshots-its-website-says-different/",
    "domain": "大厂 AI 动态",
    "title": "Flock CEO says its microphones detect ‘just gunshots’ — its website says different",
    "url": "https://techcrunch.com/2026/10/14/flock-ceo-says-its-microphones-detect-just-gunshots-its-website-says-different/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T21:30:33+00:00",
    "summary": "Langley’s comments come amid mounting scrutiny of Flock from privacy advocates, including the ACLU, and members of the public who are concerned about the misuse of its technology."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/colossal-biosciences-announces-new-ai-platform-to-help-accelerate-de-extinction-efforts/",
    "domain": "大厂 AI 动态",
    "title": "Colossal Biosciences announces new AI platform to help accelerate de-extinction efforts",
    "url": "https://techcrunch.com/2026/10/14/colossal-biosciences-announces-new-ai-platform-to-help-accelerate-de-extinction-efforts/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T21:00:00+00:00",
    "summary": "Colossal announced a new AI platform to help accelerate its de-extinction efforts and Peter Diamandis has launched a new fund to back startups who use it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/flock-ceo-we-havent-fired-any-police-departments-as-customers/",
    "domain": "大厂 AI 动态",
    "title": "Flock CEO: We haven’t ‘fired’ any police departments as customers",
    "url": "https://techcrunch.com/2026/10/14/flock-ceo-we-havent-fired-any-police-departments-as-customers/",
    "source": "Zack Whittaker, Amanda Silberling, Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T20:26:25+00:00",
    "summary": "Flock CEO Garrett Langley said that the surveillance company has not canceled contracts of any police department or law enforcement agency, despite reports of abuse."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/electric-vehicle-sales-in-the-u-s-are-showing-signs-of-life/",
    "domain": "大厂 AI 动态",
    "title": "Electric vehicle sales in the US are showing signs of life",
    "url": "https://techcrunch.com/2026/10/14/electric-vehicle-sales-in-the-u-s-are-showing-signs-of-life/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T20:12:07+00:00",
    "summary": "The electric vehicle market in the U.S. has been growing for the last three consecutive quarters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/timeteller-puts-our-internal-clocks-at-the-center-of-personalized-medicine/",
    "domain": "大厂 AI 动态",
    "title": "TimeTeller puts our internal clocks at the center of personalized medicine",
    "url": "https://techcrunch.com/2026/10/14/timeteller-puts-our-internal-clocks-at-the-center-of-personalized-medicine/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T20:00:00+00:00",
    "summary": "German startup TimeTeller has developed a saliva test kit to help anyone understand their circadian rhythm; it aims to reduce side effects from cancer treatments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/ambrosia-energy-will-build-a-10-gwh-factory-in-texas-to-make-batteries-for-off-grid-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Ambrosia Energy will build a 10 GWh factory in Texas to make batteries for off-grid data centers",
    "url": "https://techcrunch.com/2026/10/14/ambrosia-energy-will-build-a-10-gwh-factory-in-texas-to-make-batteries-for-off-grid-data-centers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T19:51:34+00:00",
    "summary": "Startup Ambrosia Energy will build a massive factory to crank out batteries to augment solar panels, creating a round-the-clock clean power plant."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/hiyd-is-a-health-tracker-that-attaches-to-the-watch-you-already-wear/",
    "domain": "大厂 AI 动态",
    "title": "Hiyd is a health tracker that attaches to the watch you already wear",
    "url": "https://techcrunch.com/2026/10/14/hiyd-is-a-health-tracker-that-attaches-to-the-watch-you-already-wear/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T19:00:00+00:00",
    "summary": "Former Apple engineers figured out how to get a biometric sensor to attach to your watch without any magnets or adhesives."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/youtube-music-launches-new-labels-as-ai-generated-music-floods-streaming-platforms/",
    "domain": "大厂 AI 动态",
    "title": "YouTube Music launches new labels as AI-generated music floods streaming platforms",
    "url": "https://techcrunch.com/2026/10/14/youtube-music-launches-new-labels-as-ai-generated-music-floods-streaming-platforms/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:23:46+00:00",
    "summary": "The label will appear on the player page and include songs entirely generated by AI or partially, such as AI involved in composition and vocals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/apate-sends-ai-agents-undercover-to-get-scammed-so-they-can-gather-fraud-intelligence/",
    "domain": "大厂 AI 动态",
    "title": "Apate sends AI agents undercover to get scammed so they can gather fraud intelligence",
    "url": "https://techcrunch.com/2026/10/14/apate-sends-ai-agents-undercover-to-get-scammed-so-they-can-gather-fraud-intelligence/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:00:00+00:00",
    "summary": "Most companies use AI agents to ship products faster or speed up workflows. Apate.ai sends them undercover to get scammed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/mosqitter-is-turning-its-mosquito-traps-into-an-ai-powered-surveillance-network/",
    "domain": "大厂 AI 动态",
    "title": "Mosqitter is turning its mosquito traps into an AI-powered surveillance network",
    "url": "https://techcrunch.com/2026/10/14/mosqitter-is-turning-its-mosquito-traps-into-an-ai-powered-surveillance-network/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T17:00:00+00:00",
    "summary": "Mosqitter is turning its mosquito-trapping hardware into an AI-powered surveillance network designed to identify species, monitor populations, and provide earlier warnings of mosquito-borne disease ri"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/prismm-helps-banks-keep-inherited-money-in-house/",
    "domain": "大厂 AI 动态",
    "title": "Prismm helps banks keep inherited money in-house",
    "url": "https://techcrunch.com/2026/10/14/prismm-helps-banks-keep-inherited-money-in-house/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T16:00:00+00:00",
    "summary": "With Prismm, account holders can give designated family members access to their accounts and documents ahead of time."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/deezer-will-soon-let-you-filter-out-ai-generated-music/",
    "domain": "大厂 AI 动态",
    "title": "Deezer will soon let you filter out AI-generated music",
    "url": "https://techcrunch.com/2026/10/14/deezer-will-soon-let-you-filter-out-ai-generated-music/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T15:16:04+00:00",
    "summary": "Deezer said that the new toggle will be rolled out by the end of the year."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-homeview-the-new-apple-tv-the-app-story/",
    "domain": "大厂 AI 动态",
    "title": "Apple HomeView, The New Apple TV, The App Story",
    "url": "https://stratechery.com/2026/apple-homeview-the-new-apple-tv-the-app-story/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T10:00:00+00:00",
    "summary": "The Apple Homeview is official, and the question is how big is the addressable market for expensive devices based on subpar AI."
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
    "id": "rss:https://arstechnica.com/security/2026/10/fridge-hack-costing-millions-and-sparking-fires-stemmed-from-poor-security/",
    "domain": "大厂 AI 动态",
    "title": "Fridge hack costing millions and sparking fires stemmed from poor security",
    "url": "https://arstechnica.com/security/2026/10/fridge-hack-costing-millions-and-sparking-fires-stemmed-from-poor-security/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T21:35:09+00:00",
    "summary": "Incident hitting 700 supermarkets exploited outdated devices exposed to the Internet."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/programming-is-hard-epic-games-leans-on-vibe-coding-for-its-new-launcher-app/",
    "domain": "大厂 AI 动态",
    "title": "Epic says its new vibe-coded Epic Games Launcher is faster than Steam",
    "url": "https://arstechnica.com/gaming/2026/10/programming-is-hard-epic-games-leans-on-vibe-coding-for-its-new-launcher-app/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T21:15:56+00:00",
    "summary": "But the new \"Preview\" app \"will have some bugs,\" Epic warns."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/nato-may-redeploy-anti-drone-defenses-as-attacks-sink-more-black-sea-shipping/",
    "domain": "大厂 AI 动态",
    "title": "NATO may redeploy anti-drone defenses as attacks sink more Black Sea shipping",
    "url": "https://arstechnica.com/gadgets/2026/10/nato-may-redeploy-anti-drone-defenses-as-attacks-sink-more-black-sea-shipping/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T21:03:11+00:00",
    "summary": "Suspected Russian drones have sunk or damaged 5 ships near Bulgaria and Romania."
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
    "id": "hn:50098423",
    "domain": "股票",
    "title": "Asia chip stocks fall, AI funding worries",
    "url": "https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-15T02:29:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082283",
    "domain": "股票",
    "title": "US Says Chinese Hackers Attacked DOJ, NASA, Federal Reserve, Senate",
    "url": "https://www.usatoday.com/story/news/politics/2026/08/26/chinese-hackers-cyberattack-us-government/91473585007/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 12,
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
    "id": "hn:49914149",
    "domain": "股票",
    "title": "Anthropic's IPO Prospectus Is a Fucking Doozy",
    "url": "https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus",
    "source": "danaris",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-09-30T20:44:19+00:00",
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
    "id": "hn:50059446",
    "domain": "金融",
    "title": "Feds got warrants to use fake cell towers to hunt down Don Lemon's producer",
    "url": "https://www.wired.com/story/feds-got-warrants-to-use-fake-cell-towers-to-hunt-down-don-lemons-producer/",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-10-12T17:08:16+00:00",
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
    "id": "hn:50090662",
    "domain": "金融",
    "title": "Tesla's Robotaxis Blow Through School Zones, NHTSA Petition Alleges",
    "url": "https://www.extremetech.com/cars/teslas-robotaxis-blow-through-school-zones-nhtsa-petition-alleges",
    "source": "speckx",
    "platform": "hackernews",
    "points": 139,
    "published_at": "2026-10-14T16:45:19+00:00",
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
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 117,
    "published_at": "2026-10-13T23:13:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082021",
    "domain": "金融",
    "title": "Strafe: A new open-source, E2E Encrypted, and federated alternative to Discord",
    "url": "https://strafe.chat/",
    "source": "brydencalaway",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-10-14T03:28:00+00:00",
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
    "points": 48,
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
    "id": "hn:50062076",
    "domain": "金融",
    "title": "\"Today we're laying off a large part of the Airtable team \"",
    "url": "https://twitter.com/fedesimio/status/2109713695165329511",
    "source": "tortilla",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-12T19:56:16+00:00",
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
    "id": "rss:https://arxiv.org/abs/2610.18921",
    "domain": "金融",
    "title": "Creative destruction: Human-AI competition in an experimental market",
    "url": "https://arxiv.org/abs/2610.18921",
    "source": "John Conlon, Peter Schwardmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.18921v1 Announce Type: new Abstract: We study two hypotheses for how a human role in production could persist despite growing AI capabilities. Humans might have a durable advantage in taste"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.19045",
    "domain": "金融",
    "title": "Long Term Pediatric Vaccine Tender Scheduling with Quantity Discounts",
    "url": "https://arxiv.org/abs/2610.19045",
    "source": "Nicholas Uhorchak, Ruben Proano, Sandra Eksioglu, Burak Eksioglu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.19045v1 Announce Type: new Abstract: Pediatric vaccine procurement for low- and lower-middle-income countries (LICs and LMICs) requires long-term coordination across heterogeneous vaccine m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.19720",
    "domain": "金融",
    "title": "Which Text Matters: Handling Model Uncertainty in Text-as-Data Regressions, with an Application to Central Bank Communication",
    "url": "https://arxiv.org/abs/2610.19720",
    "source": "Martin Feldkircher, Bernd Prostmaier, Paul Hofmarcher, Pierre Siklos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.19720v1 Announce Type: new Abstract: Social scientists routinely convert text into covariates like topic shares, ideal points or sentiment scores, and insert them into statistical models of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.20000",
    "domain": "金融",
    "title": "Interior smoothness and zero-variance geometry for finite-maturity Heston American puts",
    "url": "https://arxiv.org/abs/2610.20000",
    "source": "Junkee Jeon, Takwon Kim, Jehan Oh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.20000v1 Announce Type: new Abstract: We study finite-maturity American puts in the Heston model without the Feller condition. At positive variance, the exercise boundary is smooth and stric"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.20037",
    "domain": "金融",
    "title": "Data-Driven Dynamic Portfolio Selection with Vine Copula Simulation and Reinforcement Learning",
    "url": "https://arxiv.org/abs/2610.20037",
    "source": "Gabri\\\"el M. J. Gelissen, Fengyi Yuan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.20037v1 Announce Type: new Abstract: We develop a data-driven approach to dynamic portfolio selection that combines vine-copula simulation with reinforcement learning. The investor has cons"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.20366",
    "domain": "金融",
    "title": "Regime Detection in Latent Factor Models -- A Bayesian Decision-Theoretic Approach",
    "url": "https://arxiv.org/abs/2610.20366",
    "source": "Karl Kristian Engelund",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.20366v1 Announce Type: new Abstract: Regime-switching multi-factor models are widely used in quantitative finance, but filtering does not by itself determine when an agent should act on inf"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.34004",
    "domain": "金融",
    "title": "RICE-Alpha: Reliability-Informed Correction with Event Graphs for LLM-Agent Stock Forecasting",
    "url": "https://arxiv.org/abs/2609.34004",
    "source": "Tong Liu, Lanmiao Liu, Xiang Hu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2609.34004v2 Announce Type: cross Abstract: Equity-relevant news evolves through temporally dependent corporate events, making historical information useful only when event continuity, informati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.19254",
    "domain": "金融",
    "title": "Beyond Time Induction: Structured Conditional Neural Solvers for Parametric Stochastic-Volatility Pricing",
    "url": "https://arxiv.org/abs/2610.19254",
    "source": "Jose Miguel Lara Rangel, Mixtli Vazquez Mendoza",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.19254v1 Announce Type: cross Abstract: Physics-informed neural networks provide a flexible framework for learning parametric PDE solution families without labeled data, yet preserving accur"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.19428",
    "domain": "金融",
    "title": "Common Signals, Spurious Cross-Excitation, and Identification in Multivariate Hawkes Processes",
    "url": "https://arxiv.org/abs/2610.19428",
    "source": "Jiwon Jung, Kiseop Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.19428v1 Announce Type: cross Abstract: Multivariate Hawkes models are widely used to measure endogenous interactions in event data, but latent common signals can generate apparent excitatio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.20125",
    "domain": "金融",
    "title": "Auction-based allocation of routes in capacity-constrained networks",
    "url": "https://arxiv.org/abs/2610.20125",
    "source": "Gergely Cs\\'aji, D\\'avid Csercsik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.20125v1 Announce Type: cross Abstract: We study the route-set allocation problem between end nodes in capacity-constrained flow networks with transfer costs. We introduce an origin--destina"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08199",
    "domain": "金融",
    "title": "Volatility in Prediction Markets: A Structural Approach",
    "url": "https://arxiv.org/abs/2607.08199",
    "source": "Weiye Xi, Ciamac C. Moallemi, Mallesh Pai, Shouqiao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2607.08199v3 Announce Type: replace Abstract: Forward-looking volatility forecasts are central inputs to derivatives pricing, market making, risk management, and volatility-linked trading strate"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02014",
    "domain": "金融",
    "title": "Insights on Time-consistent Deep Hedging under Elicitable Dynamic Risk Measures",
    "url": "https://arxiv.org/abs/2609.02014",
    "source": "Shuyi Zhang, Fr\\'ed\\'eric Godin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2609.02014v2 Announce Type: replace Abstract: We study deep hedging where the objective is expressed in terms of a dynamic risk measure, under which sequential decisions are time-consistent. We "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.17989",
    "domain": "金融",
    "title": "Whom Do AI Agents Work For? Role Assignment Induces Sponsorship Bias in LLM Recommenders",
    "url": "https://arxiv.org/abs/2609.17989",
    "source": "Davood Wadi, Yu Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2609.17989v2 Announce Type: replace Abstract: Large language models (LLMs) now serve as conversational shopping assistants on platforms that also sell advertising. These AI agents face a conflic"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27113",
    "domain": "金融",
    "title": "Active Portfolio Management in Concentrated Equity Markets",
    "url": "https://arxiv.org/abs/2609.27113",
    "source": "Brian Ceco, Xiaofei Shi, Ting-Kam Leonard Wong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2609.27113v2 Announce Type: replace Abstract: The equal-weighted portfolio is a passive, rule-based strategy that has historically been difficult to outperform, delivering higher returns than th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28372",
    "domain": "金融",
    "title": "Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer",
    "url": "https://arxiv.org/abs/2609.28372",
    "source": "Davood Wadi, Yu Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2609.28372v2 Announce Type: replace Abstract: Consumers increasingly delegate purchasing decisions to Large Language Models (LLMs) acting as surrogate consumers. Using \"Tool-Lab,\" an adaptation "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37108",
    "domain": "金融",
    "title": "The Efficient Frontier from a LASSO Solver",
    "url": "https://arxiv.org/abs/2609.37108",
    "source": "Thomas Schmelzer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2609.37108v2 Announce Type: replace Abstract: Schmelzer and Hastie prove that Markowitz's Critical Line Algorithm and the LASSO path trace the same curve. This companion note checks that result "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07888",
    "domain": "金融",
    "title": "A Functional Representation of Credit Behavior for Probability of Default Modeling",
    "url": "https://arxiv.org/abs/2610.07888",
    "source": "Jonas Brunholm, Bjarne H{\\o}jgaard, Thomas D. Nielsen, Orimar Sauri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.07888v2 Announce Type: replace Abstract: This paper proposes a framework for modeling probability of default via functional data analysis. By representing a series of credit variables as fu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07985",
    "domain": "金融",
    "title": "A Finite Bid--Ask Spread from Replenishment Displaced from the Quote",
    "url": "https://arxiv.org/abs/2610.07985",
    "source": "Christopher Angstmann, Derick Diana, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.07985v2 Announce Type: replace Abstract: We give a unified analytic account of a finite bid--ask spread in a two-field reaction--diffusion order book. The model retains separate bid and ask"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.21334",
    "domain": "金融",
    "title": "Ideological Bias in LLMs' Economic Causal Reasoning",
    "url": "https://arxiv.org/abs/2604.21334",
    "source": "Donggyu Lee, Hyeok Yun, Jungwon Kim, Junsik Min, Sungwon Park, Sangyoon Park, Jihee Kim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2604.21334v3 Announce Type: replace-cross Abstract: Do large language models (LLMs) exhibit systematic ideological bias when reasoning about economic causal effects? As LLMs are increasingly use"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21534",
    "domain": "金融",
    "title": "Generative AI Availability, Grades, and Student Satisfaction at a Large University",
    "url": "https://arxiv.org/abs/2607.21534",
    "source": "James M. Zumel Dumlao, Meng Wang, Zhonghan Xie, Junyao Hu, Ivan Bar, George Chaney III, Henry Gold, Misha Teplitskiy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2607.21534v3 Announce Type: replace-cross Abstract: The availability of generative AI (GenAI) has raised concerns that college students substitute GenAI for cognitive effort, earning high grades"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22697",
    "domain": "金融",
    "title": "Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf",
    "url": "https://arxiv.org/abs/2608.22697",
    "source": "Davood Wadi, Yu Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2608.22697v5 Announce Type: replace-cross Abstract: When shopping is delegated to AI agents, it is unclear whether the ranking advantage documented for humans persists. Across 7,000 sessions wit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.34474",
    "domain": "金融",
    "title": "Deep kernel hedging",
    "url": "https://arxiv.org/abs/2609.34474",
    "source": "Jean-Loup Dupret, Donatien Hainaut, Edouard Motte",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2609.34474v2 Announce Type: replace-cross Abstract: We introduce a deep kernel hedging framework that combines the flexibility of deep learning with the structural inductive bias of kernel metho"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.14959",
    "domain": "金融",
    "title": "AlphaRLM: Aligning Language Models for Literature-Grounded Symbolic Factor Discovery",
    "url": "https://arxiv.org/abs/2610.14959",
    "source": "Jie Huang, Yuecheng Hong, Yao Chen, Hao Zhong, Linfeng Xiao, Xudong Liu, Hao Xia, Jianxuan Xin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:00:00+00:00",
    "summary": "arXiv:2610.14959v2 Announce Type: replace-cross Abstract: Formulaic alpha mining seeks to discover executable expressions that capture predictive market signals in a vast, noisy search space. Recent L"
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
  }
]
```
