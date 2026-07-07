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

- 今日日期：`2026-07-07`
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
  "date": "2026-07-07",
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
    "points": 3623708,
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
    "points": 1441031,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 941152,
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
    "points": 853149,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 847203,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 765164,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 763249,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 726451,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 666268,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 551994,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 499810,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 383863,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1rv7A6oEeP",
    "domain": "AI",
    "title": "2026版LangChain教程，langchain快速入门， Agent智能体rag项目实战",
    "url": "http://www.bilibili.com/video/av116792827579053",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 370183,
    "published_at": "2026-06-23T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】LangChain学习一套通，从入门到三大综合项目实战"
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 339229,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1wpTJ6yEAq",
    "domain": "AI",
    "title": "我教了140万人装ClaudeCode，现在决定暂时卸载它……",
    "url": "http://www.bilibili.com/video/av116851967270281",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 319495,
    "published_at": "2026-07-02T19:16:20+00:00",
    "summary": "拧巴啊……"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 252871,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 176375,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 172328,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 158951,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 151026,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 135859,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 119418,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 99234,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1kiEu65E48",
    "domain": "AI",
    "title": "【AI漫剧】吊打付费！目前B站最全最细的AI漫剧制作零基础到精通教程！2026最新AI视频生成全流程教学！手把手教你从0到1制作AI短片，带你玩转AI影视赛道！",
    "url": "http://www.bilibili.com/video/av116714578647582",
    "source": "AI视频轻松学",
    "platform": "bilibili",
    "points": 97490,
    "published_at": "2026-06-08T13:45:57+00:00",
    "summary": "一个冷知识:点赞是免费的!\n但是可以让辛苦做视频的UP主开心快乐一整天!!!\n持续更新中~评论区获取课程资料哟~求一键三连~谢谢各位观众老爷！！！！"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92435,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1cME46tEwD",
    "domain": "AI",
    "title": "codex制作个人作品集网站教程",
    "url": "http://www.bilibili.com/video/av116707683273242",
    "source": "小羊同学AIGC",
    "platform": "bilibili",
    "points": 84118,
    "published_at": "2026-06-07T11:00:00+00:00",
    "summary": "自己搭建个人网站的一些心得，踩了不少坑，今天总结给大家！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 71997,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 70265,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 62175,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1mKLG6QENF",
    "domain": "AI",
    "title": "我让 Claude 在 立创EDA 自己画了一块 STM32 最小系统板",
    "url": "http://www.bilibili.com/video/av116584404424785",
    "source": "胡昊用AI造硬件",
    "platform": "bilibili",
    "points": 47113,
    "published_at": "2026-05-16T13:08:49+00:00",
    "summary": "跟 Claude 说一句「画一块 STM32 最小系统板」，\n他自己打开立创EDA，放主控、加晶振、加去耦电容、画连线，\n最后给我一张完整的原理图。\n用到的东西\n· AI 客户端：Claude Code\n· EDA：立创EDA 专业版\n· 桥接：扩展物联搜 &quot;run&quot;，装 Run API Gateway\n· 立创官方 easyeda-api skill"
  },
  {
    "id": "bvid:BV1pewJzUEQY",
    "domain": "AI",
    "title": "claude code实现simulink仿真模型的搭建",
    "url": "http://www.bilibili.com/video/av116222217756047",
    "source": "掌上明猪z",
    "platform": "bilibili",
    "points": 46147,
    "published_at": "2026-03-13T14:01:06+00:00",
    "summary": "MCP：https://ww2.mathworks.cn/matlabcentral/fileexchange/183314-matlab-mcp-core-server\nclaude添加MCP：claude mcp add --transport stdio matlab -- &quot;E:\\APP\\MATLAB2025\\matlab-mcp-core-server-win64.exe&qu"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 41704,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV188Tn6ZE3f",
    "domain": "AI",
    "title": "如何在地铁上VibeCoding？",
    "url": "http://www.bilibili.com/video/av116851229071296",
    "source": "子杰Kyro",
    "platform": "bilibili",
    "points": 38121,
    "published_at": "2026-07-02T16:14:15+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 35809,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 25373,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22603,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV15i7K69EN7",
    "domain": "AI",
    "title": "【6.22最新发布】claude桌面版安装教程！一周快速入门claude code保姆级教程！",
    "url": "http://www.bilibili.com/video/av116793196676384",
    "source": "是蒜七丫",
    "platform": "bilibili",
    "points": 20753,
    "published_at": "2026-06-22T10:07:14+00:00",
    "summary": "求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "小狗瑞恩Ryan",
    "platform": "bilibili",
    "points": 17613,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 17620,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1ZHAozLE7b",
    "domain": "AI",
    "title": "【SynthPilot】Claude Code FPGA开发通关教程",
    "url": "http://www.bilibili.com/video/av116164755790661",
    "source": "晓川科研站",
    "platform": "bilibili",
    "points": 15023,
    "published_at": "2026-03-03T10:26:33+00:00",
    "summary": "全网首个AI Agent FPGA开发教程。SynthPilot通过MCP协议打通Vivado全链路，AI自主写码、综合、读报告、改Bug、迭代——真正的Agent模式闭环开发。从零开始，带你见证FPGA开发方式的代际变革。\n获取工具:synthpilot.dev\n晓川交流群:1007696121"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 14875,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 14347,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV14a4y1T7Cp",
    "domain": "AI",
    "title": "VS Code + CursorCode 插件，AI 帮你编写、调试代码",
    "url": "http://www.bilibili.com/video/av654787185",
    "source": "马隆工作室",
    "platform": "bilibili",
    "points": 13967,
    "published_at": "2023-04-11T11:48:41+00:00",
    "summary": "免费， VS Code + CursorCode 插件，AI 帮你编写、调试代码"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 12526,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV191TY6KEHk",
    "domain": "AI",
    "title": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套Agent教程就够了！",
    "url": "http://www.bilibili.com/video/av116843192851440",
    "source": "Agent智能体-",
    "platform": "bilibili",
    "points": 12461,
    "published_at": "2026-07-01T06:09:09+00:00",
    "summary": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套AI Agent教程就够了！"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 12451,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 10479,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1QuTv6BEf7",
    "domain": "AI",
    "title": "vibe coding｜打工人做App全流程分享！含大量提示词和prd～｜【b站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116844484631808",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 10214,
    "published_at": "2026-07-01T11:29:32+00:00",
    "summary": "我用3天 vibe coding出了我的第二个 App～\n总结了上次匆忙开始没有准备好 导致很多次来回调试和推翻重来的血泪经验，这次用AI vibe coding我的宗旨就是和AI打好配合，人工的部分重点放在了各种给AI的需求文档（虽然也是AI写的）～ 全流程AI来实现落地我只做掌控整体节奏、给AI提供素材/PRD和验收，并且验收通过率也是极高的，极大提高了AI开发可用性和我的效率！\n\n全程无代码"
  },
  {
    "id": "bvid:BV1WBTX6kE1B",
    "domain": "AI",
    "title": "【2026版】这绝对是B站唯一将Vibe Coding从入门到实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！拿走不谢，允许白嫖！",
    "url": "http://www.bilibili.com/video/av116871663722218",
    "source": "码士集团-马小雪",
    "platform": "bilibili",
    "points": 9525,
    "published_at": "2026-07-06T06:47:51+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！ 【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV16yVW6qE8V",
    "domain": "AI",
    "title": "小白必看教程：如何用AI跑生信？vscode配置codex给你答案",
    "url": "http://www.bilibili.com/video/av116652704340048",
    "source": "我叫白内涵",
    "platform": "bilibili",
    "points": 9414,
    "published_at": "2026-05-28T14:38:39+00:00",
    "summary": "小白友好，欢迎大佬们指教"
  },
  {
    "id": "rss:https://www.eetimes.com/canadas-ai-ecosystem-needs-more-urgency/",
    "domain": "AI 算力 / 半导体",
    "title": "Canada’s AI Ecosystem Needs More Urgency",
    "url": "https://www.eetimes.com/canadas-ai-ecosystem-needs-more-urgency/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T22:00:00+00:00",
    "summary": "Canada has the AI talent. Now, it’s time to scale its domestic compute and sovereign hardware. The post Canada’s AI Ecosystem Needs More Urgency appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/mips-software-to-silicon-with-risc-v-interview-with-mips-physical-ai-is-agentic-ai-at-the-edge/",
    "domain": "AI 算力 / 半导体",
    "title": "MIPS on the RISC-V Shift: ‘Physical AI Is Agentic AI at the Edge’",
    "url": "https://www.eetimes.com/mips-software-to-silicon-with-risc-v-interview-with-mips-physical-ai-is-agentic-ai-at-the-edge/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T17:00:00+00:00",
    "summary": "MIPS bets RISC-V and ARC AI will power physical AI in cars and factory robots. Watch the interview and learn more. The post MIPS on the RISC-V Shift: &#8216;Physical AI Is Agentic AI at the Edge&#8217"
  },
  {
    "id": "rss:https://www.eetimes.com/voice-is-key-to-physical-ai-development-methods-need-to-catch-up/",
    "domain": "AI 算力 / 半导体",
    "title": "Voice Is Key to Physical AI; Development Methods Need to Catch Up",
    "url": "https://www.eetimes.com/voice-is-key-to-physical-ai-development-methods-need-to-catch-up/",
    "source": "Finnur Pind",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T12:41:56+00:00",
    "summary": "To solve far-field ASR challenges, physical AI needs acoustic reality, prompting engineers to use physics-based simulation. The post Voice Is Key to Physical AI; Development Methods Need to Catch Up a"
  },
  {
    "id": "rss:https://www.eetimes.com/kioxia-all-set-to-raise-the-nand-game-in-ai-ssds/",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia All Set to Raise the NAND Game in AI SSDs",
    "url": "https://www.eetimes.com/kioxia-all-set-to-raise-the-nand-game-in-ai-ssds/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T07:29:33+00:00",
    "summary": "Here is how the Japanese chipmaker is cashing in on NAND flash demand in data center SSDs. The post Kioxia All Set to Raise the NAND Game in AI SSDs appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/breakthrough-cnt-pellicles-deliver-66x-durability-and-sufficient-transmittance/",
    "domain": "AI 算力 / 半导体",
    "title": "Breakthrough CNT Pellicles Deliver 66x Durability and Sufficient Transmittance",
    "url": "https://www.eetimes.com/breakthrough-cnt-pellicles-deliver-66x-durability-and-sufficient-transmittance/",
    "source": "Lintec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T04:00:00+00:00",
    "summary": "Explore the latest breakthrough in CNT pellicles for EUV lithography: durability is up to 66 times higher, with less transmittance loss. The post Breakthrough CNT Pellicles Deliver 66x Durability and "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/china-made-cxmt-memory-now-supports-faster-speeds-on-msis-amd-motherboards-new-bios-adds-ddr5-8200-validation-on-dual-dimm-ddr5-7200-on-quad-dimm-models",
    "domain": "AI 算力 / 半导体",
    "title": "China-made CXMT memory now supports faster speeds on MSI's AMD motherboards — new BIOS adds DDR5-8200 validation on dual-DIMM, DDR5-7200 on quad-DIMM models",
    "url": "https://www.tomshardware.com/pc-components/ddr5/china-made-cxmt-memory-now-supports-faster-speeds-on-msis-amd-motherboards-new-bios-adds-ddr5-8200-validation-on-dual-dimm-ddr5-7200-on-quad-dimm-models",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T16:20:37+00:00",
    "summary": "MSI has officially validated region-bound Chinese RAM using CXMT modules to run at up to 8,200 MT/s on its AM5 motherboards. Models with two RAM slots can handle these high frequencies a bit better th"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-resets-xbox-by-cutting-3-200-jobs-this-year-divesting-five-game-studios-firm-cites-margins-that-are-3-10x-lower-than-comparable-platform-and-publishing-businesses",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft 'resets' Xbox by cutting 3,200 jobs this year, divesting five game studios — firm cites 'margins that are 3-10x lower than comparable platform and publishing businesses'",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-resets-xbox-by-cutting-3-200-jobs-this-year-divesting-five-game-studios-firm-cites-margins-that-are-3-10x-lower-than-comparable-platform-and-publishing-businesses",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:39:52+00:00",
    "summary": "Xbox CEO Asha Sharma announced that Microsoft's gaming division will cut 3,200 jobs throughout FY27 and is spinning out studios but not canceling any games."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/printers/raspberry-pi-powered-open-source-printer-earns-design-award-nomination-but-still-has-no-price-nine-months-after-reveal",
    "domain": "AI 算力 / 半导体",
    "title": "Working prototype of open-source printer that promises user-repairability and no subscriptions appears in first video — DRM-free 'Open Printer' inkjet still has no announced price, ship date, or print",
    "url": "https://www.tomshardware.com/peripherals/printers/raspberry-pi-powered-open-source-printer-earns-design-award-nomination-but-still-has-no-price-nine-months-after-reveal",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:30:17+00:00",
    "summary": "Open Tools, a Paris-based startup, has announced that its Open Printer has been nominated for two French Design Awards."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen AI Halo review: AMD builds a DGX Spark of its own",
    "url": "https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:00:15+00:00",
    "summary": "The Ryzen AI Halo is a turn-key AMD local AI box that’s backed up with first-party software support, handy utilities, and plenty of documentation for local AI explorers. But the performance and applic"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/you-can-now-use-your-sony-headphones-as-a-real-time-head-tracker-for-race-and-flight-simulators-on-pc-several-hundred-games-already-supported-enthusiast-creates-open-source-app-that-translates-live-sensor-data-into-in-game-camera-controls",
    "domain": "AI 算力 / 半导体",
    "title": "You can now use your Sony headphones as a free real-time head tracker for race and flight simulators on PC, several hundred games already supported — enthusiast creates open-source app that translates",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/you-can-now-use-your-sony-headphones-as-a-real-time-head-tracker-for-race-and-flight-simulators-on-pc-several-hundred-games-already-supported-enthusiast-creates-open-source-app-that-translates-live-sensor-data-into-in-game-camera-controls",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T14:36:21+00:00",
    "summary": "A new open-source app called Sony Head Tracker, developed by Nicholas Slattery, reads raw sensor data from Sony headphones and earbuds and converts them into something OpenTrack can understand. From t"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Kyber rack for Rubin Ultra reportedly delayed to 2028, stopgap solution also axed due to customer pushback — Analyst firm SemiAnalysis says PCB midplane problems led to the delay [Updated]",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T13:33:34+00:00",
    "summary": "Nvidia reportedly won't ship its Kyber NVL144 rack until 2028, a delay of more than 12 months."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Intel tout homegrown American chip supply chain prowess as country bolsters local production, but gaps remain — crucial Blackwell packaging steps remain offshore as projects grow in scope a",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T12:51:09+00:00",
    "summary": "America's AI supply chain now starts and ends in the U.S., while its most valuable middle steps remain entirely offshore until at least 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/electric-drone-breaks-world-air-speed-record-at-434-mph-designed-for-anti-aircraft-interceptor-roles-german-firm-convincingly-smashed-the-official-409-mph-record-hopes-to-get-stamp-of-approval-from-guinness-soon",
    "domain": "AI 算力 / 半导体",
    "title": "Electric drone breaks world air speed record at 434 mph, designed for anti-aircraft interceptor roles — German firm convincingly smashed the official 409 mph record, hopes to get stamp of approval fro",
    "url": "https://www.tomshardware.com/tech-industry/drones/electric-drone-breaks-world-air-speed-record-at-434-mph-designed-for-anti-aircraft-interceptor-roles-german-firm-convincingly-smashed-the-official-409-mph-record-hopes-to-get-stamp-of-approval-from-guinness-soon",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T12:39:54+00:00",
    "summary": "Quantum Systems Group reckons it has broken the flight speed record for an electric drone. During internal testing last month the Munich-based firm recorded its Apex Recordhunter drone hitting a top s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinas-huawei-to-enter-south-korean-ai-chip-market-with-new-atlas-superpods-clusters-pack-8-192-ascend-950-accelerators-per-deployment-reportedly-challenges-nvidia-dominance-with-tripled-inference-performance-of-h20-at-one-quarter-the-cost",
    "domain": "AI 算力 / 半导体",
    "title": "China’s Huawei to enter South Korean AI chip market with new Atlas SuperPods, clusters pack 8,192 Ascend 950 accelerators per deployment — reportedly challenges Nvidia dominance with 'tripled inferenc",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinas-huawei-to-enter-south-korean-ai-chip-market-with-new-atlas-superpods-clusters-pack-8-192-ascend-950-accelerators-per-deployment-reportedly-challenges-nvidia-dominance-with-tripled-inference-performance-of-h20-at-one-quarter-the-cost",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T12:31:48+00:00",
    "summary": "Huawei is reportedly preparing to enter South Korea's AI accelerator market with its Ascend 950 chips and Atlas 950 SuperPod, challenging Nvidia through aggressive pricing, amid a broader push to expa"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-massive-usd1-050-saving-on-this-rtx-5090-gaming-pc-thats-just-16-percent-more-than-the-gpus-standalone-price-right-now-epic-discount-secures-you-a-formidable-4k-gaming-rig-with-a-9800x3d-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Score a massive $1,050 saving on this RTX 5090 gaming PC that's just 16% more than the GPU's standalone price right now — epic discount secures you a formidable 4K gaming rig with a 9800X3D, 32GB DDR5",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-massive-usd1-050-saving-on-this-rtx-5090-gaming-pc-thats-just-16-percent-more-than-the-gpus-standalone-price-right-now-epic-discount-secures-you-a-formidable-4k-gaming-rig-with-a-9800x3d-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T11:45:52+00:00",
    "summary": "Save $1,050 on this epic ABS Kaze II Ruby gaming PC, fitted with a 9800X3D, RTX 5090, 32GB DDR5, and 2TB SSD for just $4,749.05 for a limited time only."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/steam-machine-interview-full-transcript-valve-engineers-discuss-usd1-049-pricing-compact-design-component-shortages-and-windows-support",
    "domain": "AI 算力 / 半导体",
    "title": "Steam Machine interview full transcript: Valve engineers discuss $1,049 pricing, compact design, component shortages, and Windows support",
    "url": "https://www.tomshardware.com/video-games/steam-machine-interview-full-transcript-valve-engineers-discuss-usd1-049-pricing-compact-design-component-shortages-and-windows-support",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T11:32:00+00:00",
    "summary": "Valve's Pierre-Loup Griffais and Yazan Aldehayyat talked to Tom's Hardware about the Steam Machine, it's pricing, engineering, and even Windows support."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/wisconsin-residents-file-class-action-lawsuit-against-microsofts-worlds-most-powerful-ai-data-center-due-to-data-center-noise-plaintiffs-also-mention-construction-noise-and-extreme-light-pollution-from-usd7-3-billion-facility",
    "domain": "AI 算力 / 半导体",
    "title": "Wisconsin residents file class-action lawsuit against Microsoft's 'world's most powerful AI data center' due to data center noise — plaintiffs also mention construction noise and extreme light polluti",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/wisconsin-residents-file-class-action-lawsuit-against-microsofts-worlds-most-powerful-ai-data-center-due-to-data-center-noise-plaintiffs-also-mention-construction-noise-and-extreme-light-pollution-from-usd7-3-billion-facility",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T11:00:00+00:00",
    "summary": "Wisconsin residents file class-action lawsuit against Microsoft due to data center noise — plaintiffs also mention construction noise and extreme light pollution"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/bigme-introduces-a-color-e-ink-monitor-that-could-reportedly-hit-60-fps-25-3-inch-display-will-come-with-a-3200-x-1800-resolution-and-support-for-4096-colors",
    "domain": "AI 算力 / 半导体",
    "title": "Bigme introduces a color e-ink monitor that could reportedly hit 60 FPS — 25.3-inch display will come with a 3200 x 1800 resolution and support for 4096 colors",
    "url": "https://www.tomshardware.com/monitors/bigme-introduces-a-color-e-ink-monitor-that-could-reportedly-hit-60-fps-25-3-inch-display-will-come-with-a-3200-x-1800-resolution-and-support-for-4096-colors",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T10:00:00+00:00",
    "summary": "This is the first e-ink monitor that can hit 60 FPS, making it useful in more tasks outside of just reading. While you likely won't be able to play fast-paced games on this display, it should still ma"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-an-rtx-3060-with-12-gb-of-vram-for-just-usd329-99-at-newegg-msi-ventus-2x-oc-model-back-in-stock-with-free-shipping",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 3060 with 12 GB of VRAM for just $329.99 at Newegg — MSI Ventus 2X OC model back in stock with free shipping",
    "url": "https://www.tomshardware.com/pc-components/get-an-rtx-3060-with-12-gb-of-vram-for-just-usd329-99-at-newegg-msi-ventus-2x-oc-model-back-in-stock-with-free-shipping",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T19:08:22+00:00",
    "summary": "Get an RTX 3060 with 12 GB of VRAM for just $329.99 at Newegg — MSI Ventus 2X OC model back in stock with free shipping"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/spacex-vaporizes-260-starlink-satellites-in-six-months-using-earths-atmosphere-new-environmental-concerns-emerge-over-burning-2-700-pound-orbital-data-centers-fcc-seeks-to-exempt-satellites-from-regulations",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX vaporizes 260 Starlink satellites in six months using Earth's atmosphere — new environmental concerns emerge over burning 2,700-pound orbital data centers, FCC seeks to exempt satellites from r",
    "url": "https://www.tomshardware.com/tech-industry/space/spacex-vaporizes-260-starlink-satellites-in-six-months-using-earths-atmosphere-new-environmental-concerns-emerge-over-burning-2-700-pound-orbital-data-centers-fcc-seeks-to-exempt-satellites-from-regulations",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T16:00:00+00:00",
    "summary": "SpaceX retired 260 Starlink satellites in six months, with hundreds more to follow, as debate grows over the atmospheric impact of satellite burn-ups."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/rampocalyse-pricing-prompts-maker-to-construct-his-own-memory-using-ancient-apollo-era-tech-usb-drive-resurrects-hand-threaded-magnetic-core-memory-using-salvaged-russian-computer-parts",
    "domain": "AI 算力 / 半导体",
    "title": "RAMpocalyse pricing prompts maker to construct his own memory using ancient Apollo-era tech — USB drive resurrects hand-threaded magnetic core memory using salvaged Russian computer parts",
    "url": "https://www.tomshardware.com/pc-components/storage/rampocalyse-pricing-prompts-maker-to-construct-his-own-memory-using-ancient-apollo-era-tech-usb-drive-resurrects-hand-threaded-magnetic-core-memory-using-salvaged-russian-computer-parts",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T15:50:00+00:00",
    "summary": "DIYer shows how they made a handsome magnetic core memory USB drive using home CNC and 3D printing equipment. However, it isn't a homebrew answer to the AI-induced memory crisis with only 64 bits of d"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/germanys-1-5-million-project-to-build-the-worlds-largest-game-archive-collapses-after-funding-dries-up",
    "domain": "AI 算力 / 半导体",
    "title": "Germany's massive 60,000-game preservation project collapses after €1.5 million funding dries up — world's largest game archive was entirely publicly available, now abandoned just as Sony kills physic",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/germanys-1-5-million-project-to-build-the-worlds-largest-game-archive-collapses-after-funding-dries-up",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T15:37:27+00:00",
    "summary": "A German effort to assemble the world's largest publicly accessible video game archive is being wound down after roughly €1.5 million in public funding expired."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/reviewer-tests-rtx-4080m-desktop-graphics-card-powered-by-salvaged-laptop-silicon-performs-worse-than-slightly-more-expensive-rx-9070-gre-but-draws-only-100w-in-games",
    "domain": "AI 算力 / 半导体",
    "title": "Reviewer tests 'RTX 4080M' desktop graphics card powered by salvaged laptop silicon — performs worse than slightly more expensive RX 9070 GRE but draws only 100W in games",
    "url": "https://www.tomshardware.com/pc-components/gpus/reviewer-tests-rtx-4080m-desktop-graphics-card-powered-by-salvaged-laptop-silicon-performs-worse-than-slightly-more-expensive-rx-9070-gre-but-draws-only-100w-in-games",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:46:02+00:00",
    "summary": "Turns out, a modded RTX 4080M desktop GPU performs worse than similarly-priced official options. It currently costs roughly $400 in China and compared to the RX 9070 GRE, this custom card loses in eve"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/hannah-montana-linux-gets-modern-remaster-after-nearly-two-decades-sweet-niblets-new-v26-is-built-on-debian-with-a-re-skin-of-kde-plasma",
    "domain": "AI 算力 / 半导体",
    "title": "Hannah Montana Linux gets modern remaster after nearly two decades — ‘Sweet niblets,’ new v26 is built on Debian with a re-skin of KDE Plasma",
    "url": "https://www.tomshardware.com/software/linux/hannah-montana-linux-gets-modern-remaster-after-nearly-two-decades-sweet-niblets-new-v26-is-built-on-debian-with-a-re-skin-of-kde-plasma",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:23:38+00:00",
    "summary": "Say whaaaat? Hannah Montana Linux is back. Basically abandonware since 2009, the distro has returned with a modern kernel and about 18 years worth of patches."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/us-navy-testing-3d-printed-fighter-jet-parts-for-quick-repairs-composite-parts-printed-at-forward-deployed-3d-printers-to-be-flight-tested-on-operational-f-a-18-super-hornets",
    "domain": "AI 算力 / 半导体",
    "title": "US Navy is flight-testing 3D printed fighter jet parts that cut repair times in half — forward-deployed 3D printers generate composite parts, flight testing to begin on operational F/A-18 Super Hornet",
    "url": "https://www.tomshardware.com/3d-printing/us-navy-testing-3d-printed-fighter-jet-parts-for-quick-repairs-composite-parts-printed-at-forward-deployed-3d-printers-to-be-flight-tested-on-operational-f-a-18-super-hornets",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:11:16+00:00",
    "summary": "The US Navy is experimenting with 3D-printed patches for composite parts, allowing forward bases to repair F/A-18 Super Hornets without waiting for replacement parts coming from the tail end of a logi"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/f1-25-2026-season-edition-gpu-benchmarks-from-pole-position-to-the-back-of-the-grid",
    "domain": "AI 算力 / 半导体",
    "title": "F1 25: 2026 Season Edition GPU benchmarks – From Pole Position to the Back of the Grid",
    "url": "https://www.tomshardware.com/pc-components/gpus/f1-25-2026-season-edition-gpu-benchmarks-from-pole-position-to-the-back-of-the-grid",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T14:05:19+00:00",
    "summary": "With a year of updates behind it and a major overhaul now in place, this is the perfect opportunity to revisit F1 25 and see where performance stands in 2026 with a selection of both Nvidia and AMD GP"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/atomic-semi-rebrands-as-fab2-and-shifts-operations-to-texas",
    "domain": "AI 算力 / 半导体",
    "title": "Jim Keller's startup is building a factory to mass-produce small semiconductor fabs —Atomic Semi rebrands as 'Fab2' underlining intended role as a 'fab fab'",
    "url": "https://www.tomshardware.com/tech-industry/atomic-semi-rebrands-as-fab2-and-shifts-operations-to-texas",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:15:00+00:00",
    "summary": "Atomic Semi, the semiconductor tooling startup founded by chip architect Jim Keller and DIY fabrication pioneer Sam Zeloof, has rebranded as Fab2."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-thinkpad-x1-carbon-gen-14-aura-edition-review",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo ThinkPad X1 Carbon Gen 14 Aura Edition review: A masterclass in mobility and usability",
    "url": "https://www.tomshardware.com/laptops/lenovo-thinkpad-x1-carbon-gen-14-aura-edition-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:10:00+00:00",
    "summary": "A sublime ultraportable with world-class quality and OLED visuals, the ThinkPad X1 Carbon Gen 14 excels at everything it does."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows-11-identifier-used-to-track-scattered-spider-perp-after-microsoft-shared-info-with-fbi-19-year-old-us-estonian-hacker-arrested-over-alleged-ties-to-infamous-extortion-group",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11 identifier code used to track Scattered Spider perp after Microsoft shared info with FBI — 19-year-old US-Estonian hacker arrested over alleged ties to infamous extortion group",
    "url": "https://www.tomshardware.com/software/windows-11-identifier-used-to-track-scattered-spider-perp-after-microsoft-shared-info-with-fbi-19-year-old-us-estonian-hacker-arrested-over-alleged-ties-to-infamous-extortion-group",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:55:00+00:00",
    "summary": "Petet Stokes was arrested in Finland and extradited to the U.S. over alleged ties to the Scattered Spider group, with Microsoft helping in the investigation. He's in custody awaiting trial based on a "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-this-rtx-5070-ti-oled-gaming-laptop-at-usd300-off-acer-predator-helios-neo-16s-ai-drops-to-usd1-899-99",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this RTX 5070 Ti OLED gaming laptop at $300 off — Acer Predator Helios Neo 16S AI drops to $1,899.99",
    "url": "https://www.tomshardware.com/pc-components/grab-this-rtx-5070-ti-oled-gaming-laptop-at-usd300-off-acer-predator-helios-neo-16s-ai-drops-to-usd1-899-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:38:55+00:00",
    "summary": "The Acer Predator Helios Neo 16S AI combines an OLED 240 Hz display, Intel's Core Ultra 9 275HX, RTX 5070 Ti graphics, and 32GB of DDR5 memory, all while saving you $300 off its regular price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens",
    "domain": "AI 算力 / 半导体",
    "title": "Alibaba bans Anthropic's Claude Code after an alleged hidden China-detection backdoor is uncovered — employees told to switch to Qoder as the rift between the firms widens",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:20:00+00:00",
    "summary": "Alibaba banned Claude Code after an alleged hidden China-detection code was found, prompting staff to switch to Qoder as its feud with Anthropic deepens."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-command-series-kb7-review",
    "domain": "AI 算力 / 半导体",
    "title": "Turtle Beach Command Series KB7 Review: A keyboard with a touchscreen and a lot of potential",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-command-series-kb7-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:10:00+00:00",
    "summary": "Turtle Beach's new \"Command Series\" KB7 TKL keyboard features a 4.3-inch touchscreen instead of the typical navigation cluster — like a Stream Deck, but as a touchscreen. Unfortunately, it lacks the s"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-disc-drive-purchase-cap-predates-sonys-disc-cutoff",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 Disc Drive purchase cap predates Sony's disc cutoff — 'high demand' order limit has been on the store page since at least March 2025",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-disc-drive-purchase-cap-predates-sonys-disc-cutoff",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:00:00+00:00",
    "summary": "Meanwhile, the largest petition against the disc cutoff sat beyond 74,000 signatures on the morning of July 4th, closing in on its 75,000 goal."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/you-can-now-play-half-life-2-right-inside-your-browser-at-over-100-fps-with-save-states-and-console-support-ingenious-port-recreates-the-entire-game-campaign-using-webgl-2",
    "domain": "AI 算力 / 半导体",
    "title": "You can now play Half-Life 2 right inside your browser at over 100 FPS with save states & console support — Ingenious port recreates the entire game campaign using WebGL 2",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/you-can-now-play-half-life-2-right-inside-your-browser-at-over-100-fps-with-save-states-and-console-support-ingenious-port-recreates-the-entire-game-campaign-using-webgl-2",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T11:40:00+00:00",
    "summary": "An unofficial browser port of Half-Life 2 has popped up online, allowing you to play the original campaign without downloading anything. Developed in just three months by Slqnt and 98006, it even feat"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/fill-your-steam-library-without-spending-a-single-dime-scratch-your-shopping-itch-with-the-steam-summer-sale-simulator",
    "domain": "AI 算力 / 半导体",
    "title": "Fill your Steam library without spending a single dime — scratch your shopping itch with the Steam Summer Sale Simulator",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/fill-your-steam-library-without-spending-a-single-dime-scratch-your-shopping-itch-with-the-steam-summer-sale-simulator",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T11:20:00+00:00",
    "summary": "This website lets you \"buy\" all the Steam games you want without spending anything at all. It was primarily made for the dopamine hit, but the Achievements page is quite engaging, too."
  },
  {
    "id": "rss:https://www.eetimes.com/inside-infineon-e5b-dresden-fab-virtual-fab-cloning-fast-tracked-the-launch/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Infineon’s €5B Dresden Fab: Virtual Fab Cloning Fast-Tracked the Launch",
    "url": "https://www.eetimes.com/inside-infineon-e5b-dresden-fab-virtual-fab-cloning-fast-tracked-the-launch/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:40:05+00:00",
    "summary": "At the opening of its Dresden smart power fab, Infineon’s COO said virtual fab cloning enabled delivery three months ahead of schedule. The post Inside Infineon&#8217;s €5B Dresden Fab: Virtual Fab Cl"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynix-plans-713b-domestic-investment/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix Plans $713B Domestic Investment",
    "url": "https://www.eetimes.com/sk-hynix-plans-713b-domestic-investment/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:57:51+00:00",
    "summary": "SK Hynix is set to invest $713 billion to expand its semiconductor manufacturing capacity in South Korea and plans a Nasdaq listing. The post SK Hynix Plans $713B Domestic Investment appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/spains-semiconductor-landscape-six-stories-from-a-growing-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Spain’s Semiconductor Landscape: Six Stories from a Growing Ecosystem",
    "url": "https://www.eetimes.com/spains-semiconductor-landscape-six-stories-from-a-growing-ecosystem/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T07:10:19+00:00",
    "summary": "EE Times examines the companies, institutes, and policy initiatives positioning Spain within Europe’s next wave of semiconductor innovation. The post Spain’s Semiconductor Landscape: Six Stories from "
  },
  {
    "id": "rss:https://www.eetimes.com/turkey-needs-to-make-its-own-chips-not-just-design-them/",
    "domain": "AI 算力 / 半导体",
    "title": "Turkey Needs to Make Its Own Chips, Not Just Design Them",
    "url": "https://www.eetimes.com/turkey-needs-to-make-its-own-chips-not-just-design-them/",
    "source": "Oğuz Ergin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T12:42:59+00:00",
    "summary": "Turkey has built a strong chip design base, but without domestic manufacturing, its semiconductor sovereignty remains on loan. The post Turkey Needs to Make Its Own Chips, Not Just Design Them appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/opensearch-powers-ai-data-infrastructure-as-agentic-workloads-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "OpenSearch Powers AI Data Infrastructure as Agentic Workloads Scale",
    "url": "https://www.eetimes.com/opensearch-powers-ai-data-infrastructure-as-agentic-workloads-scale/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T07:40:09+00:00",
    "summary": "OpenSearch turns AI’s data deluge into hybrid search, observability, and agent monitoring while avoiding vendor lock-in. The post OpenSearch Powers AI Data Infrastructure as Agentic Workloads Scale ap"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/961895/hoto-pixeldrive-screwdriver-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Hoto&#8217;s PixelDrive screwdriver is down to $60, matching its best price",
    "url": "https://www.theverge.com/gadgets/961895/hoto-pixeldrive-screwdriver-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T20:24:28+00:00",
    "summary": "If your Prime Day purchases included a new desk, TV stand, bookshelf, or other furniture you still haven&#8217;t assembled, Hoto&#8217;s PixelDrive cordless screwdriver can help speed up the process. "
  },
  {
    "id": "rss:https://www.theverge.com/policy/961802/america-250-free-speech",
    "domain": "大厂 AI 动态",
    "title": "America’s greatest idea is still under threat",
    "url": "https://www.theverge.com/policy/961802/america-250-free-speech",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T18:36:33+00:00",
    "summary": "The United States of America recently turned 250 years old. What a spectacle! The fireworks were amazing, and millions of proud people celebrated across the nation - even around the world. France lit "
  },
  {
    "id": "rss:https://www.theverge.com/science/961483/doctor-zachary-rubin-md-interview",
    "domain": "大厂 AI 动态",
    "title": "Five questions for Dr. Rubin, who’s armed with a mic and a bowtie",
    "url": "https://www.theverge.com/science/961483/doctor-zachary-rubin-md-interview",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T17:15:29+00:00",
    "summary": "Bullshit is cheap but truth is expensive. Anyone with half a brain cell can post wild misinformation that goes mega viral, which wastes the time and expertise of highly trained people who feel an obli"
  },
  {
    "id": "rss:https://www.theverge.com/games/961749/xbox-layoffs-compulsion-double-fine-indie",
    "domain": "大厂 AI 动态",
    "title": "Former Xbox studios Double Fine and Compulsion will keep games after going indie",
    "url": "https://www.theverge.com/games/961749/xbox-layoffs-compulsion-double-fine-indie",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T16:22:34+00:00",
    "summary": "Microsoft is spinning off four of its Xbox game studios - Compulsion Games, Double Fine Productions, Ninja Theory, and Undead Labs - as part of the restructuring announced today. However, two that are"
  },
  {
    "id": "rss:https://www.theverge.com/column/961707/smart-glasses-ai-wearables-meta-surveillance-privacy",
    "domain": "大厂 AI 动态",
    "title": "I spy",
    "url": "https://www.theverge.com/column/961707/smart-glasses-ai-wearables-meta-surveillance-privacy",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T16:00:00+00:00",
    "summary": "I've long argued that Hollywood has simultaneously set and ruined our expectations for smart glasses. But after binge-watching two seasons of Netflix's A Man on the Inside, this is perhaps the first t"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/961612/xtra-muse-dji-osmo-pocket-3-ipad-air-magic-mouse-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The DJI Osmo Pocket 3 lookalike is down to $329",
    "url": "https://www.theverge.com/gadgets/961612/xtra-muse-dji-osmo-pocket-3-ipad-air-magic-mouse-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:09:18+00:00",
    "summary": "Initially, I was going to tell you about a good deal happening on the DJI Osmo Pocket 3, which is down from the $500 it’s sold at most of the year to $378 at multiple retailers. But there’s a better d"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/961603/raina-penchansky-ali-berman-dba-uta-influencer-cliff-marketing",
    "domain": "大厂 AI 动态",
    "title": "Inside the big business of the creator economy, with the agents making it happen",
    "url": "https://www.theverge.com/podcast/961603/raina-penchansky-ali-berman-dba-uta-influencer-cliff-marketing",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T14:30:00+00:00",
    "summary": "We’ve got another special episode of Decoder today, recorded at the Cannes Lions advertising festival in the South of France. I’m talking with Ali Berman and Raina Penchansky, who run the Creators div"
  },
  {
    "id": "rss:https://www.theverge.com/games/961632/nintendo-switch-europe-discontinued",
    "domain": "大厂 AI 动态",
    "title": "Nintendo will stop selling the original Switch in Europe next year",
    "url": "https://www.theverge.com/games/961632/nintendo-switch-europe-discontinued",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T14:15:48+00:00",
    "summary": "Nintendo is making a new version of the Switch 2 with a replaceable battery in Europe - but its predecessor has a very different future. As part of an updated FAQ about revisions to Nintendo hardware "
  },
  {
    "id": "rss:https://www.theverge.com/report/960635/partiful-app-event-planning-data-palantir",
    "domain": "大厂 AI 动态",
    "title": "Can Partiful keep the party going?",
    "url": "https://www.theverge.com/report/960635/partiful-app-event-planning-data-palantir",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T14:00:00+00:00",
    "summary": "One hundred dollars will buy you 8 pounds of glitter; 10 Domino's pizzas; 406 miniature disco balls from Temu; or 100 cans of Coors Light. For a friend's birthday party one year, Ayla D'Silva spent $1"
  },
  {
    "id": "rss:https://www.theverge.com/news/961546/xbox-layoffs-studio-sales-2026",
    "domain": "大厂 AI 动态",
    "title": "Microsoft is selling off four Xbox studios as part of significant gaming cuts",
    "url": "https://www.theverge.com/news/961546/xbox-layoffs-studio-sales-2026",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T13:31:24+00:00",
    "summary": "Microsoft is laying off 4,800 employees today, and more than 30 percent of the job losses are in the company's Xbox division. The significant gaming cuts will affect nearly every part of Xbox and also"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/netflix-invented-binge-watching-now-it-may-have-outgrown-it/",
    "domain": "大厂 AI 动态",
    "title": "Netflix invented binge-watching. Now it may have outgrown it.",
    "url": "https://techcrunch.com/2026/07/06/netflix-invented-binge-watching-now-it-may-have-outgrown-it/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T00:47:33+00:00",
    "summary": "A new report suggests Netflix viewers aren’t sticking around for Season 2. The bigger issue may be that binge-watching itself is no longer the advantage it once was."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/",
    "domain": "大厂 AI 动态",
    "title": "The ‘first’ AI-run ransomware attack still needed a human",
    "url": "https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T23:56:14+00:00",
    "summary": "An AI agent carried out the technical execution of a real-world ransomware attack for the first known time, but new details show a human still chose the victim, set up the infrastructure, and supplied"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/us-investors-will-soon-get-access-to-sk-hynix-another-memory-maker-riding-the-ai-boom/",
    "domain": "大厂 AI 动态",
    "title": "US investors will soon get access to SK Hynix, another memory maker riding the AI boom",
    "url": "https://techcrunch.com/2026/07/06/us-investors-will-soon-get-access-to-sk-hynix-another-memory-maker-riding-the-ai-boom/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T23:21:03+00:00",
    "summary": "SK Hynix is experiencing a boom credited to AI. It will ride that to a multibillion-dollar U.S. IPO, expected to take place on Friday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/vercel-ceo-guillermo-rauch-on-the-fight-to-split-off-models-from-agents/",
    "domain": "大厂 AI 动态",
    "title": "Vercel CEO Guillermo Rauch on the fight to split off models from agents",
    "url": "https://techcrunch.com/2026/07/06/vercel-ceo-guillermo-rauch-on-the-fight-to-split-off-models-from-agents/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T19:49:10+00:00",
    "summary": "\"The reality is, when you're optimizing for production, you start looking at a price/performance,\" Guillermo Rauch tells TechCrunch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/you-can-now-customize-siris-pace-and-expressivity-in-the-latest-ios-27-beta/",
    "domain": "大厂 AI 动态",
    "title": "You can now customize Siri’s pace and expressivity in the latest iOS 27 beta",
    "url": "https://techcrunch.com/2026/07/06/you-can-now-customize-siris-pace-and-expressivity-in-the-latest-ios-27-beta/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T19:01:59+00:00",
    "summary": "The update is part of Apple's broader effort to make Siri feel more natural and personal, as it rebuilds the assistant around generative AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/",
    "domain": "大厂 AI 动态",
    "title": "Every major tech layoff in 2026 that has name-checked AI",
    "url": "https://techcrunch.com/2026/07/06/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/",
    "source": "Rebecca Bellan, Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T18:35:00+00:00",
    "summary": "A running look — in reverse chronological order — at the bigger tech companies that have announced significant layoffs this year with AI as a stated factor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/amazon-competitor-bookshop-org-says-kobo-e-reader-support-will-happen-this-year-after-all/",
    "domain": "大厂 AI 动态",
    "title": "Amazon competitor Bookshop.org says Kobo eReader support will happen this year after all",
    "url": "https://techcrunch.com/2026/07/06/amazon-competitor-bookshop-org-says-kobo-e-reader-support-will-happen-this-year-after-all/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T18:12:01+00:00",
    "summary": "Bookship.org seemed to delay this anticipated partnership again, but tells TechCrunch that it has settled business terms and is working on integration."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/",
    "domain": "大厂 AI 动态",
    "title": "If you use Google, you’re training its AI. Here’s how to opt out.",
    "url": "https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T17:04:58+00:00",
    "summary": "Consider this a belated PSA: A recent change to Google’s privacy settings is allowing the company to store more of your data, including media such as “images, files, and audio and video recordings,” t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/apple-brings-back-card-payments-for-apple-account-purchases-in-india-after-a-four-year-hiatus/",
    "domain": "大厂 AI 动态",
    "title": "Apple brings back card payments for Apple Account purchases in India after a four-year hiatus",
    "url": "https://techcrunch.com/2026/07/06/apple-brings-back-card-payments-for-apple-account-purchases-in-india-after-a-four-year-hiatus/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T16:21:03+00:00",
    "summary": "Apple has started a phased rollout of card payments for Apple Account purchases in India after adapting to the country's payments framework."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/microsoft-lays-off-nearly-5000-employees-across-xbox-commercial-sales/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft lays off nearly 5,000 employees across Xbox, commercial sales",
    "url": "https://techcrunch.com/2026/07/06/microsoft-lays-off-nearly-5000-employees-across-xbox-commercial-sales/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:32:43+00:00",
    "summary": "Microsoft cut around 4,800 roles, or 2.1% of its global workforce, on Monday — the latest in a series of layoffs that’s stoking fears of AI replacing jobs. The layoffs will hit Xbox and commercial sal"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/reddit-is-using-llms-to-solve-a-problem-llms-largely-created/",
    "domain": "大厂 AI 动态",
    "title": "Reddit is using LLMs to solve a problem LLMs largely created",
    "url": "https://techcrunch.com/2026/07/06/reddit-is-using-llms-to-solve-a-problem-llms-largely-created/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:22:08+00:00",
    "summary": "In the AI era, platforms have no choice but to fight fire with fire to cull spam."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/canadian-spy-agency-says-it-hacked-drug-traffickers-extremists-and-a-ransomware-gang-last-year/",
    "domain": "大厂 AI 动态",
    "title": "Canadian spy agency says it hacked drug traffickers, extremists, and a ransomware gang last year",
    "url": "https://techcrunch.com/2026/07/06/canadian-spy-agency-says-it-hacked-drug-traffickers-extremists-and-a-ransomware-gang-last-year/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T14:43:59+00:00",
    "summary": "The hacking operations disclosed in a Canadian spy agency's annual report underscores some pressing national security threats facing the country and its top allies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/how-to-reserve-and-change-your-whatsapp-username/",
    "domain": "大厂 AI 动态",
    "title": "How to reserve and change your WhatsApp username",
    "url": "https://techcrunch.com/2026/07/06/how-to-reserve-and-change-your-whatsapp-username/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T14:15:30+00:00",
    "summary": "WhatsApp now lets users reserve usernames ahead of the feature’s full rollout, making it possible to connect without sharing a phone number once usernames go live."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/station-f-ramps-up-as-a-launchpad-for-europes-hottest-ai-startups/",
    "domain": "大厂 AI 动态",
    "title": "Station F ramps up as a launchpad for Europe’s hottest AI startups",
    "url": "https://techcrunch.com/2026/07/06/station-f-ramps-up-as-a-launchpad-for-europes-hottest-ai-startups/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T13:00:00+00:00",
    "summary": "Station F, a Paris-based startup hub founded by French billionaire Xavier Niel, is gearing up for a new edition of its F/ai accelerator program in a bid to strengthen its positioning as a stepping sto"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/",
    "domain": "大厂 AI 动态",
    "title": "Smart glasses maker Even Realities hits $1B valuation with $150M funding led by Meituan, Tencent",
    "url": "https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T09:00:00+00:00",
    "summary": "Even Realities, an ex-Apple team building camera-free smart glasses, raised $150 million from Meituan and Tencent at a $1 billion valuation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/this-humanoid-robotics-company-is-going-public-but-its-ceo-isnt-promising-a-robot-in-your-home-anytime-soon/",
    "domain": "大厂 AI 动态",
    "title": "This humanoid robotics company is going public, but its CEO isn’t promising a robot in your home anytime soon",
    "url": "https://techcrunch.com/2026/07/05/this-humanoid-robotics-company-is-going-public-but-its-ceo-isnt-promising-a-robot-in-your-home-anytime-soon/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T06:05:29+00:00",
    "summary": "While other humanoid startups chase sky-high valuations, Agility Robotics is betting its future on execution — and a SPAC."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/ubers-european-expansion-plans-may-have-hit-a-speed-bump/",
    "domain": "大厂 AI 动态",
    "title": "Uber’s European expansion plans may have hit a speed bump",
    "url": "https://techcrunch.com/2026/07/05/ubers-european-expansion-plans-may-have-hit-a-speed-bump/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T21:35:17+00:00",
    "summary": "Back in February, Uber announced ambitious plans to launch in seven new European markets in 2026 — but now five of those launches are reportedly on hold."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/trump-memecoin-investors-lost-3-8-billion-analysis-finds/",
    "domain": "大厂 AI 动态",
    "title": "Trump memecoin investors lost $3.8 billion, analysis finds",
    "url": "https://techcrunch.com/2026/07/05/trump-memecoin-investors-lost-3-8-billion-analysis-finds/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T20:29:05+00:00",
    "summary": "Nearly 1 million people have lost a total of $3.8 billion after buying President Donald Trump’s $TRUMP memecoin, while Trump made $636 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/",
    "domain": "大厂 AI 动态",
    "title": "Amazon will stop accepting new customers for Mechanical Turk",
    "url": "https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T17:43:36+00:00",
    "summary": "These may be the last days of Amazon’s Mechanical Turk."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/05/5-desk-gadgets-that-can-make-your-workday-better/",
    "domain": "大厂 AI 动态",
    "title": "5 desk gadgets that can make your workday better",
    "url": "https://techcrunch.com/2026/07/05/5-desk-gadgets-that-can-make-your-workday-better/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T15:00:00+00:00",
    "summary": "The right desk gadgets can help you reduce clutter, stay focused, and add a little extra convenience to your day."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/fcc-to-end-biden-era-rule-that-forces-isps-to-list-all-their-fees/",
    "domain": "大厂 AI 动态",
    "title": "FCC to end Biden-era rule that forces ISPs to list all their fees",
    "url": "https://arstechnica.com/tech-policy/2026/07/fcc-to-end-biden-era-rule-that-forces-isps-to-list-all-their-fees/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T21:13:37+00:00",
    "summary": "FCC to let ISPs stop listing all passthrough fees, give single \"up to\" price."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/kremlin-suspected-of-flying-drones-over-europe-using-russian-shadow-fleet/",
    "domain": "大厂 AI 动态",
    "title": "Kremlin suspected of flying drones over Europe using Russian shadow fleet",
    "url": "https://arstechnica.com/gadgets/2026/07/kremlin-suspected-of-flying-drones-over-europe-using-russian-shadow-fleet/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T20:52:42+00:00",
    "summary": "Drone intruders that possibly flew from Russian ships showed Europe isn’t ready."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/whats-the-oldest-americana-flown-in-space/",
    "domain": "大厂 AI 动态",
    "title": "What is the oldest American object ever launched into space?",
    "url": "https://arstechnica.com/space/2026/07/whats-the-oldest-americana-flown-in-space/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T19:57:56+00:00",
    "summary": "From a Revolutionary War flag to the Statue of Liberty..."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/nuclear-regulatory-commission-plans-really-minor-changes-to-safety-regs/",
    "domain": "大厂 AI 动态",
    "title": "NRC is (sort of) getting rid of \"as low as reasonably achievable\" standard",
    "url": "https://arstechnica.com/science/2026/07/nuclear-regulatory-commission-plans-really-minor-changes-to-safety-regs/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T17:48:45+00:00",
    "summary": "Its issues with current nuclear safety standards are termed semantic, not physical."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/katalysts-satellite-rescue-mission-is-now-in-pursuit-of-nasas-swift/",
    "domain": "大厂 AI 动态",
    "title": "Katalyst's satellite rescue mission is now in pursuit of NASA's Swift",
    "url": "https://arstechnica.com/space/2026/07/katalysts-satellite-rescue-mission-is-now-in-pursuit-of-nasas-swift/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T17:14:09+00:00",
    "summary": "It will take several weeks for the Link spacecraft to rendezvous with NASA's Swift observatory."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/",
    "domain": "大厂 AI 动态",
    "title": "Secret Claude tracker shocks users after Anthropic’s anti-surveillance stance",
    "url": "https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T16:44:18+00:00",
    "summary": "Anthropic accused of spying on users; engineer says “experiment” is over."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/the-incredible-shrinking-xbox-five-studios-3200-employees-let-go/",
    "domain": "大厂 AI 动态",
    "title": "The incredible shrinking Xbox: Five studios, 3,200 employees let go",
    "url": "https://arstechnica.com/gaming/2026/07/the-incredible-shrinking-xbox-five-studios-3200-employees-let-go/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T16:01:54+00:00",
    "summary": "Move affects ~20% of the gaming division, which will refocus on its biggest franchises."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/f1-in-britain-automated-software-to-blame-for-crushing-expectations/",
    "domain": "大厂 AI 动态",
    "title": "F1 in Britain: Automated software to blame for crushing expectations",
    "url": "https://arstechnica.com/cars/2026/07/f1-in-britain-automated-software-to-blame-for-crushing-expectations/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:45:55+00:00",
    "summary": "Sometimes races finish behind a safety car, but it's not always satisfying."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/there-were-not-one-but-two-asteroid-encounters-this-weekend/",
    "domain": "大厂 AI 动态",
    "title": "There were not one, but two asteroid encounters this weekend",
    "url": "https://arstechnica.com/space/2026/07/there-were-not-one-but-two-asteroid-encounters-this-weekend/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:15:30+00:00",
    "summary": "The Torifune asteroid turns out to be shaped like a peanut."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/uk-regulator-warns-of-arms-race-to-keep-up-with-ai-use-in-financial-services/",
    "domain": "大厂 AI 动态",
    "title": "UK regulator warns of \"arms race\" to keep up with AI use in financial services",
    "url": "https://arstechnica.com/ai/2026/07/uk-regulator-warns-of-arms-race-to-keep-up-with-ai-use-in-financial-services/",
    "source": "Martin Arnold",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T14:17:42+00:00",
    "summary": "FCA official makes case for greater powers for watchdog as millions use technology for personal finance decisions."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/bentley-teases-its-first-ev-the-torcal/",
    "domain": "大厂 AI 动态",
    "title": "Bentley teases its first EV, the Torcal",
    "url": "https://arstechnica.com/cars/2026/07/bentley-teases-its-first-ev-the-torcal/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T11:30:38+00:00",
    "summary": "The new model will be officially unveiled in late September."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/the-czinger-21c-might-be-the-wildest-car-we-drive-all-year/",
    "domain": "大厂 AI 动态",
    "title": "The Czinger 21C might be the wildest car we drive all year",
    "url": "https://arstechnica.com/cars/2026/07/the-czinger-21c-might-be-the-wildest-car-we-drive-all-year/",
    "source": "Bradley Iger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T11:00:14+00:00",
    "summary": "This hybrid V8 has organic-looking 3D-printed components and shatters lap records."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/chemical-accidents-rise-as-trump-administration-proposes-weakening-safety-rules/",
    "domain": "大厂 AI 动态",
    "title": "Chemical accidents rise as Trump administration proposes weakening safety rules",
    "url": "https://arstechnica.com/science/2026/07/chemical-accidents-rise-as-trump-administration-proposes-weakening-safety-rules/",
    "source": "Liza Gross, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T11:05:22+00:00",
    "summary": "Chemicals from accidents that injured or killed people increased by nearly 50 percent in recent years."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/the-missing-500-million-cosmic-bombardment-melted-earths-first-crust/",
    "domain": "大厂 AI 动态",
    "title": "The missing 500 million: Cosmic bombardment melted Earth's first crust",
    "url": "https://arstechnica.com/science/2026/07/the-missing-500-million-cosmic-bombardment-melted-earths-first-crust/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T10:55:02+00:00",
    "summary": "The heat of the Hadean may have come from impacts as well as the interior."
  },
  {
    "id": "rss:https://www.producthunt.com/products/stanley-studio",
    "domain": "大厂 AI 动态",
    "title": "Stanley Studio",
    "url": "https://www.producthunt.com/products/stanley-studio",
    "source": "Daniel Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T03:37:29+00:00",
    "summary": "The AI video editor you hire that edits like a human Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/meta",
    "domain": "大厂 AI 动态",
    "title": "Astryx",
    "url": "https://www.producthunt.com/products/meta",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T03:52:49+00:00",
    "summary": "A customizable, agent-ready open-source design system Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/codemote-remote-control-for-any-ai",
    "domain": "大厂 AI 动态",
    "title": "CodeMote",
    "url": "https://www.producthunt.com/products/codemote-remote-control-for-any-ai",
    "source": "Salvatore Castellitti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:39:06+00:00",
    "summary": "Claude Code, Codex, any CLI agent. Driven from your iPhone Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mozaik-4",
    "domain": "大厂 AI 动态",
    "title": "Mozaik",
    "url": "https://www.producthunt.com/products/mozaik-4",
    "source": "Miodrag Vilotijević",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T12:31:38+00:00",
    "summary": "TypeScript runtime for self-organizing AI agents Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/nixmac",
    "domain": "大厂 AI 动态",
    "title": "Nixmac",
    "url": "https://www.producthunt.com/products/nixmac",
    "source": "Cooper Maruyama",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T13:33:34+00:00",
    "summary": "Nix-darwin that speaks plain English Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3885061350617350?f=rss",
    "domain": "大厂 AI 动态",
    "title": "\"龙虾\"为什么这么火？OpenClaw登顶GitHub后，AI Agent时代真的来了？",
    "url": "https://36kr.com/p/3885061350617350?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T06:23:00+00:00",
    "summary": "GitHubStar-history 最近Openclaw以25.2万星标，超越Meta的React登顶GitHub开源项目历史第一！ 要知道React是Facebook(现改名Meta）打造的经典前端框架，过去十余年间，互联网上绝大多数我们熟知的网站与App，底层技术架构皆由它构筑。Openclaw官方更是高调发文嘲讽Meta“我们在迭代创新，而你只在办会议”。 这只被全球开发者亲昵称作“龙虾”"
  },
  {
    "id": "wscn:3776363",
    "domain": "股票",
    "title": "如何交易SK海力士美股上市？瑞银：买ADR，抛韩股",
    "url": "https://wallstreetcn.com/articles/3776363",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T06:39:43+00:00",
    "summary": "SK海力士ADR即将登陆美股，瑞银直接喊出\"做多ADR、做空韩股\"的套利策略。逻辑清晰：ADR持仓成本更低、全球准入更广，而换股机制的潜在限制或使溢价长期存在——台积电ADR至今仍较中国台湾本地股溢价16%即为先例。"
  },
  {
    "id": "wscn:3776362",
    "domain": "股票",
    "title": "必和必拓旗下全球最大铜矿扩建获批，总投资规模最高达147亿美元",
    "url": "https://wallstreetcn.com/articles/3776362",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T06:39:02+00:00",
    "summary": "必和必拓旗下智利埃斯孔迪达铜矿获批13亿美元初期扩建工程，为后续高达147亿美元的总升级计划扫清障碍。此举旨在应对矿石品位下滑压力，并满足清洁能源与数据中心的长期铜需求，助力公司实现2030年代中期全球铜产量翻番的目标。"
  },
  {
    "id": "wscn:3776361",
    "domain": "股票",
    "title": "便宜又能打！美国企业越来越爱用中国AI，OpenRouter平台占比一度达到46%",
    "url": "https://wallstreetcn.com/articles/3776361",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T06:23:47+00:00",
    "summary": "中国AI模型正以\"白菜价\"杀入美国企业市场——比Anthropic、OpenAI便宜60%至90%，性能差距却已缩至\"六到九个月\"。开发者平台OpenRouter数据显示，美企使用中国模型的占比从4.5%骤升至峰值46%。创业公司Lindy一键切换DeepSeek，数月省下数百万美元。这场价格驱动的迁移潮，正在重塑全球AI竞争格局。"
  },
  {
    "id": "wscn:3776359",
    "domain": "股票",
    "title": "华尔街分析师警告：美股正形成\"双重泡沫\"，一旦破裂或引发30%-50%暴跌",
    "url": "https://wallstreetcn.com/articles/3776359",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T05:50:45+00:00",
    "summary": "美股AI热潮下暗流涌动。华尔街分析师发出罕见双重警告：当前美股不仅存在价格泡沫，更隐藏着盈利泡沫。若将企业盈利修正至历史正常增速，标普500估值将飙升至67.6倍市盈率，超越美国史上所有资产泡沫峰值。一旦泡沫破裂，股市或暴跌50%。"
  },
  {
    "id": "wscn:3776345",
    "domain": "股票",
    "title": "日本名义工资再次上涨3%，创1992年以来最长期连续增长记录",
    "url": "https://wallstreetcn.com/articles/3776345",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T05:43:15+00:00",
    "summary": "日本名义工资创三十年最长连增纪录，5月同比涨3.2%，实际工资连续五个月正增长——然而家庭支出却连跌六个月，中小企业因劳动力短缺破产数量更创历史新高。工资繁荣与消费萎靡的深层撕裂，12月前再度加息的概率已飙升至88%。"
  },
  {
    "id": "wscn:3776355",
    "domain": "股票",
    "title": "韩股大跌8%再度熔断！三星重挫10%，纳指期货跌1%，日元徘徊于162水平",
    "url": "https://wallstreetcn.com/articles/3776355",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T05:41:37+00:00",
    "summary": "韩国综合股价指数下跌8%，触发临时交易中止机制。SK海力士同日跌幅亦达10%。铠侠股价延续跌势，最新跌幅达12%。MSCI亚太指数整体下跌2%，芯片板块成为重灾区。纳斯达克100指数期货下跌1.1%，显示华尔街周一的反弹势头正在消退，欧洲股市亦指向低开。"
  },
  {
    "id": "wscn:3776347",
    "domain": "股票",
    "title": "停火仅三周即告反转？伊朗导弹攻击霍尔木兹商船",
    "url": "https://wallstreetcn.com/articles/3776347",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T05:41:15+00:00",
    "summary": "停火墨迹未干，导弹已再度划破霍尔木兹海峡夜空。美伊签署谅解备忘录不足三周，伊朗革命卫队即向过往商船发射至少两枚导弹，两艘船只严重受损。根据此前签署的谅解备忘录框架，核问题谈判被安排在后续阶段进行。然而，随着作为前置核心条件的“开放海峡”遭到实质性破坏，后续阶段的谈判或产生变动。"
  },
  {
    "id": "wscn:3776343",
    "domain": "股票",
    "title": "统一战线--沃什的“三步走”，目标是“重启降息”",
    "url": "https://wallstreetcn.com/articles/3776343",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T05:40:35+00:00",
    "summary": "美联储内部分歧严峻，新主席沃什接掌后如何统一战线成下半年最大悬念。中信建投研判其将分三步破局：7月人事布局制衡委员会，三季度以AI生产率革命重塑供给侧政策框架，四季度完成鸽派转向、重启降息交易。流动性改善预期下，美债、黄金、科技叙事渐入佳境，但三季度波动风险不可轻视。"
  },
  {
    "id": "wscn:3776357",
    "domain": "股票",
    "title": "腾讯AI新船票：WorkBuddy登顶生产力工具，从“慢半拍”到“产品之王”蜕变",
    "url": "https://wallstreetcn.com/premium/articles/3776357?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T05:10:00+00:00",
    "summary": "上线3个月的WorkBuddy已经拿下国内效率AI DAU第一、月访问量885万（+831% MoM）、企业版定价涨价仍然供不应求。"
  },
  {
    "id": "wscn:3776288",
    "domain": "股票",
    "title": "奔向165？日元隐形干预新策略能否抵挡贬值趋势？",
    "url": "https://wallstreetcn.com/premium/articles/3776288?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:13:24+00:00",
    "summary": "隐形干预虽可短暂扰动市场、抬升做空成本，但难改基本面压制，日元中长期仍面临继续贬值并逼近165的压力。"
  },
  {
    "id": "wscn:3776344",
    "domain": "股票",
    "title": "沪指跌超1%失守4000点，半导体产业链逆势活跃，恒指、恒科指冲高回落均转跌，芯片股大跌",
    "url": "https://wallstreetcn.com/articles/3776344",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:13:12+00:00",
    "summary": "盘面上，个股呈现普跌态势，沪深京三市超4700股飘绿，上午半天成交1.64万亿。沪深两市半日成交额1.63万亿，较上个交易日缩量5757亿。板块方面，石油化工、海运、医药、餐饮旅游板块跌幅居前，半导体硅片、半导体设备、GPU概念逆势走强。"
  },
  {
    "id": "wscn:3776356",
    "domain": "股票",
    "title": "老铺黄金的“硬奢”考验，还是绕回了金价",
    "url": "https://wallstreetcn.com/articles/3776356",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:01:49+00:00",
    "summary": "黄金的镣铐"
  },
  {
    "id": "wscn:3776331",
    "domain": "股票",
    "title": "这个夏天全球市场焦点：科技巨头财报，暴跌的油价，沃什动向，美国经济基本面",
    "url": "https://wallstreetcn.com/articles/3776331",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T03:58:26+00:00",
    "summary": "摩根大通全球基本面研究联合负责人Stephen Dulake列出十大市场关注焦点，涵盖科技巨头二季报、油价大幅下跌、美联储主席沃什政策走向以及美国经济基本面。研报指出，市场当前正在进行真实的分化定价，主动管理者面临挑战与机遇并存的复杂局面。"
  },
  {
    "id": "wscn:3776352",
    "domain": "股票",
    "title": "宽基退潮，黄金ETF超车，ETF世界资金大战刚刚开始",
    "url": "https://wallstreetcn.com/articles/3776352",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T03:24:27+00:00",
    "summary": "一场涟漪剧烈的变化"
  },
  {
    "id": "wscn:3776349",
    "domain": "股票",
    "title": "MLCC渠道价格持续上涨，有料号涨价超20倍",
    "url": "https://wallstreetcn.com/articles/3776349",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T03:15:02+00:00",
    "summary": "AI算力浪潮下，华强北MLCC涨价狂飙——村田服务器标准料单日涨幅达5%，GPU超高容型号散货溢价超15%且\"按小时报价\"；渠道炒货推高部分料号价格达出厂价25倍。7月起被动元器件进入全品类普涨阶段，深圳华强、商络电子等分销龙头有望量价齐升，坐享产业链红利。"
  },
  {
    "id": "wscn:3776348",
    "domain": "股票",
    "title": "利润暴增19倍、股价却重挫8%：三星完美财报让“买预期卖事实”再度上演？",
    "url": "https://wallstreetcn.com/articles/3776348",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T03:08:29+00:00",
    "summary": "三星初步业绩显示，二季度营业利润同比暴增19倍至89.4万亿韩元，全面超预期，却换来股价单日暴跌8%。“买预期卖事实”的逻辑之外，Meta暗示AI资本支出设上限、亚洲存储加速追赶、代工业务亏损扩大……高光财报背后，存储神话的裂缝正在显现。"
  },
  {
    "id": "wscn:3776338",
    "domain": "股票",
    "title": "中东供给恢复速度快于预期，高盛下调铝价预测",
    "url": "https://wallstreetcn.com/articles/3776338",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T02:58:16+00:00",
    "summary": "高盛将2027年LME铝均价从2950美元/吨下调至2700美元/吨，2026年四季度从3200降至2950美元/吨。核心原因：中东Al Taweelah冶炼厂复产超预期提速，叠加印尼2027年新增约120万吨供给，致2027年全球铝市过剩量扩大至150万吨，库存重建压制铝价。"
  },
  {
    "id": "wscn:3776342",
    "domain": "股票",
    "title": "美银回应“英伟达Kyber机架延迟”：担忧合理，但PCB/CCL/基板需求强劲，视调整为买点",
    "url": "https://wallstreetcn.com/articles/3776342",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T02:55:38+00:00",
    "summary": "英伟达Kyber机架延迟消息重击中国台湾半导体供应链，CCL、PCB等板块单日重挫8-9%。但美银称：此次下跌本质是“供应约束下的需求缩量”而非趋势逆转，高端CCL与ABF基板供不应求格局将延续至2027年底。成本占比低、供给扩产慢，跌出来的才是买点。"
  },
  {
    "id": "wscn:3776350",
    "domain": "股票",
    "title": "中国人民银行行长潘功胜：支持更多优质企业到香港上市和发债，债券通“南向通”年度投资净额度提升至8000亿元",
    "url": "https://wallstreetcn.com/articles/3776350",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T02:51:20+00:00",
    "summary": "潘功胜表示，债券通\"南向通\"年度净额度从5000亿元大幅提升至8000亿元，同时将债券纳入回购支持范围，产品扩展至港币及人民币相关债券并辐射澳门市场。央行还将支持更多优质内地企业赴港上市发债，持续深化粤港澳大湾区金融合作。"
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
    "id": "rss:https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "domain": "股票",
    "title": "The Underwriters of Hormuz",
    "url": "https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-20T16:23:35+00:00",
    "summary": "A post on marine insurance &#8211; by popular demand"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "domain": "股票",
    "title": "🎙️ Market Intelligence in the Age of AI: An Interview with Morningstar CEO, Kunal Kapoor",
    "url": "https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-17T16:30:34+00:00",
    "summary": "Net Interest Extra ep 20"
  },
  {
    "id": "rss:https://www.netinterest.co/p/redemption-day",
    "domain": "股票",
    "title": "Redemption Day",
    "url": "https://www.netinterest.co/p/redemption-day",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-13T18:09:28+00:00",
    "summary": "When the exit is smaller than the entrance"
  },
  {
    "id": "rss:https://www.netinterest.co/p/learning-from-lloyd",
    "domain": "股票",
    "title": "Learning from Lloyd",
    "url": "https://www.netinterest.co/p/learning-from-lloyd",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-06T17:42:54+00:00",
    "summary": "Blankfein, Goldman and the Next Market Reckoning"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "domain": "股票",
    "title": "🎙️ How Credit Markets Shaped a Nation: An Interview with Sarah Quinn",
    "url": "https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-03T16:45:21+00:00",
    "summary": "Net Interest Extra ep 19"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02645",
    "domain": "金融",
    "title": "Dynamic Capabilities for AI-Enabled Exploration: Antecedents, Mechanisms, and Innovation Outcomes",
    "url": "https://arxiv.org/abs/2607.02645",
    "source": "Thabit Atobishi, Saeed Nosratabadi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02645v1 Announce Type: new Abstract: While the operational benefits of Artificial Intelligence (AI) are well-documented, the mechanisms through which firms leverage AI for strategic explora"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02695",
    "domain": "金融",
    "title": "Financial Epiplexity: A Theory of Learnable Market Structure under Bounded Computation",
    "url": "https://arxiv.org/abs/2607.02695",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02695v1 Announce Type: new Abstract: Financial markets are hard to predict, not because price moves are purely random, but because structure is strategic, capacity-constrained, and computat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02785",
    "domain": "金融",
    "title": "Inside the Kin Network: Consanguineous Marriage, Patriarchal Bargaining, and Women's Acceptance of Intimate Partner Violence in Pakistan",
    "url": "https://arxiv.org/abs/2607.02785",
    "source": "Sana Khalil, Angela Warner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02785v1 Announce Type: new Abstract: We investigate the relationship between consanguineous (close-kin) marriage and women's acceptance of intimate partner violence (IPV) in Pakistan. We ar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02791",
    "domain": "金融",
    "title": "Capitalizing Risk and Regulation: Sequential Shocks in Florida's Condominium Market",
    "url": "https://arxiv.org/abs/2607.02791",
    "source": "Shaoming Cheng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02791v1 Announce Type: new Abstract: Housing markets capitalize new information regarding future risks and ownership costs, yet little is known about how markets respond when sequential sho"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02795",
    "domain": "金融",
    "title": "Coordinated Sniper Cohorts on Pump.fun: Detection of 1,012 Persistent Wallet Rings and the Limits of Naive Causal Inference for First-Hour Buyer Flow",
    "url": "https://arxiv.org/abs/2607.02795",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02795v1 Announce Type: new Abstract: We study coordinated buyer behavior on the Solana pump.fun bonding-curve marketplace using 1,578,333 buyer observations from 166,098 token launches betw"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02823",
    "domain": "金融",
    "title": "Pump.fun Graduation Regime Windows: Survival Analysis of 832,941 Token Launches and the Social-Presence Effect",
    "url": "https://arxiv.org/abs/2607.02823",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02823v1 Announce Type: new Abstract: We present a Kaplan-Meier and Cox proportional-hazards survival analysis of 832,941 Solana pump.fun token launches with 24-hour graduation outcomes, obs"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02830",
    "domain": "金融",
    "title": "Outcome-Classified Precision Auditing of Filter Rules in Algorithmic DEX Trading: Evidence from 2,400 Rejection Events",
    "url": "https://arxiv.org/abs/2607.02830",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02830v1 Announce Type: new Abstract: This paper reports a precision audit of a production filter stack against a 13-day window of post-rejection forward-market observations on Solana DEX tr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02892",
    "domain": "金融",
    "title": "Robots and the Public Finance of Disability Insurance",
    "url": "https://arxiv.org/abs/2607.02892",
    "source": "Duha T. Altindag, Reem El Cheikh Taha, John M. Nunley, R. Alan Seals",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02892v1 Announce Type: new Abstract: Automation affects public budgets through wages and the tax base, and also through inflows into social insurance. We estimate the effect of industrial r"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02947",
    "domain": "金融",
    "title": "FOI-O: An NZ-first ontology and verification methods package for Freedom of Information process modelling",
    "url": "https://arxiv.org/abs/2607.02947",
    "source": "Dylan A Mordaunt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02947v1 Announce Type: new Abstract: Public official-information request records contain process signals. They can support research, workflow review, and human-supervised agent help. Yet th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02978",
    "domain": "金融",
    "title": "Urban Reconstruction and Population Redistribution: Evidence from Tokyo after the Great Kanto Earthquake",
    "url": "https://arxiv.org/abs/2607.02978",
    "source": "Kota Ogasawara",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.02978v1 Announce Type: new Abstract: This study examines the impact of the 1923 Great Kanto Earthquake on population distribution within Tokyo City. The earthquake triggered massive fires t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03082",
    "domain": "金融",
    "title": "Portfolio Optimization and Tail-Risk Analytics of Actively Managed ETFs",
    "url": "https://arxiv.org/abs/2607.03082",
    "source": "William W. Lamptey, Nicholas Appiah, Abootaleb Shirvani, Priscilla Ati-Tay, Svetlozar T. Rachev, Frank J. Fabozzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03082v1 Announce Type: new Abstract: This paper examines portfolio optimization and tail-risk analytics for a heterogeneous universe of actively managed investment funds. Using daily Bloomb"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03113",
    "domain": "金融",
    "title": "Rebate versus Matching, Again: How Opt-in Reshapes the Effectiveness of Price-Equivalent Subsidies",
    "url": "https://arxiv.org/abs/2607.03113",
    "source": "Shusaku Sasaki, Takunori Ishihara, Hiroki Kato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03113v1 Announce Type: new Abstract: Traditional theory predicts equivalent effects of matching and rebate subsidies at equal prices, yet experiments favor matching. Refinements narrow this"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03115",
    "domain": "金融",
    "title": "Beyond the Fixed Price: Valuation and Risk of Non-Standard Renewable PPAs",
    "url": "https://arxiv.org/abs/2607.03115",
    "source": "Nicola Bartolini, Silvia Romagnoli, Amia Santini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03115v1 Announce Type: new Abstract: Renewable Power Purchase Agreements have become increasingly important instruments for supporting the energy transition, as they offer revenue stability"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03144",
    "domain": "金融",
    "title": "DSGE as a Structured World Model:Benchmarking Counterfactual Generalization in Economic Worlds",
    "url": "https://arxiv.org/abs/2607.03144",
    "source": "Wenli Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03144v1 Announce Type: new Abstract: Modern world models -- Dreamer, transformer world models (IRIS, Genie), and JEPA / next-latent architectures -- learn dynamics from observed trajectorie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03214",
    "domain": "金融",
    "title": "Resolving the Binding Constraint on Circular Economy: Principal Return Rate as Interest-Free Monetary Architecture",
    "url": "https://arxiv.org/abs/2607.03214",
    "source": "Amir Rashid",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03214v1 Announce Type: new Abstract: Green growth through circular economy is the dominant institutional response to ecological breakdown. Yet its insufficiency is structural: material flow"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03239",
    "domain": "金融",
    "title": "Exact conditional simulation of Point processes: Application to pathwise market impact estimation",
    "url": "https://arxiv.org/abs/2607.03239",
    "source": "Joseph Lecl\\`ere, Youssef Ouazzani Chahdi, Mathieu Rosenbaum, Gr\\'egoire Szymanski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03239v1 Announce Type: new Abstract: Market impact is defined as the difference between the observed price trajectory under a given execution strategy and the counterfactual trajectory that"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03305",
    "domain": "金融",
    "title": "Cash-invariant hull representation of divergence preferences",
    "url": "https://arxiv.org/abs/2607.03305",
    "source": "Ale\\v{s} \\v{C}ern\\'y, Johannes Ruf, Martin Schweizer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03305v1 Announce Type: new Abstract: Uniformly weighted divergence preferences (UWDP) introduced in Maccheroni et al. (2006) are an important class of risk-averse preferences that contain a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03793",
    "domain": "金融",
    "title": "Sectoral contributions to sustainable development in Turkiye: Which sector is more effective?",
    "url": "https://arxiv.org/abs/2607.03793",
    "source": "Emre Akusta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03793v1 Announce Type: new Abstract: Enhancing sustainable development performance requires an assessment of the relative roles of economic sectors in this process. However, comparative emp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03858",
    "domain": "金融",
    "title": "A Spectral Generalisation of the Variance Ratio: Eigenstructure of Long-Horizon Portfolio Covariance and a Multi-Memory Factor Model of U.S. Equity Returns",
    "url": "https://arxiv.org/abs/2607.03858",
    "source": "Anders G Fr{\\o}seth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.03858v1 Announce Type: new Abstract: We propose a multivariate generalisation of the Lo-MacKinlay (1988) variance ratio that decomposes long-horizon equity-return dynamics into separate ret"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04103",
    "domain": "金融",
    "title": "Governing Generative AI Across Financial Institutions: An SR 26-2-Compatible Framework for Generative AI Risk Control",
    "url": "https://arxiv.org/abs/2607.04103",
    "source": "Yiqing Wang, Yixin Kang, Luyun Lin, Siqi Mao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04103v1 Announce Type: new Abstract: The release of SR 26-2 marks a significant modernization of U.S. model risk management by replacing SR 11-7 with a more risk-based and materiality-sensi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04130",
    "domain": "金融",
    "title": "A Gabor--Epps uncertainty principle for traders",
    "url": "https://arxiv.org/abs/2607.04130",
    "source": "Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04130v1 Announce Type: new Abstract: We propose a Gabor--Epps uncertainty principle for practical trading. The key idea is that high-frequency correlation is not observed in clock time alon"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04221",
    "domain": "金融",
    "title": "A Limit Order Market with Uncertain Informed Trading Participation",
    "url": "https://arxiv.org/abs/2607.04221",
    "source": "Umut \\c{C}etin, Mingwei Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04221v1 Announce Type: new Abstract: We study a one period limit order market with informed traders, noise traders, and competitive liquidity suppliers, in which the number of informed trad"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04278",
    "domain": "金融",
    "title": "Deep Learning for Dynamic Programming with Recursive Utility",
    "url": "https://arxiv.org/abs/2607.04278",
    "source": "Xianhua Peng, Wu Guo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04278v1 Announce Type: new Abstract: We propose the first deep learning algorithm, the Certainty Equivalent Learning (CEL) algorithm, for solving high-dimensional discrete-time dynamic prog"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04280",
    "domain": "金融",
    "title": "Order Splitting and Liquidity Replenishment Are Jointly Necessary for the Square-Root Law of Market Impact:",
    "url": "https://arxiv.org/abs/2607.04280",
    "source": "Yang Zhou, Jianwen Chen, Ruipeng Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04280v1 Announce Type: new Abstract: Three quantitative predictions have been advanced for the square-root law (SRL) of market impact, $I/\\sigma_D = c\\,(Q/V_D)^{\\delta}$ with $\\delta\\approx"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04322",
    "domain": "金融",
    "title": "The neglected contributions of Thomas C. Schelling to the economics of climate change",
    "url": "https://arxiv.org/abs/2607.04322",
    "source": "Richard S. J. Tol",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04322v1 Announce Type: new Abstract: The rich have emitted the bulk of greenhouse gases. The poor suffer the bulk of the impacts. Climate change is a transfer from poor to rich. Climate pol"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04345",
    "domain": "金融",
    "title": "Strategic Information Disclosure in Algorithmic Pricing",
    "url": "https://arxiv.org/abs/2607.04345",
    "source": "Chengcheng Wang, Zexin Ye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04345v1 Announce Type: new Abstract: As firms increasingly adopt AI-powered pricing algorithms, a key and urgent policy concern is how to regulate the potential algorithmic collusion. This "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04346",
    "domain": "金融",
    "title": "Preference-fitting Framework: Elicited Utility Function and PHARA Approximation",
    "url": "https://arxiv.org/abs/2607.04346",
    "source": "Rui Dai, Zongxia Liang, Yang Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04346v1 Announce Type: new Abstract: The utility function plays a core role in portfolio selection, but its specific form is typically hard to elicit. We propose a definition of the elicite"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04392",
    "domain": "金融",
    "title": "Adapted Law Invariance and Time-Consistent Dynamic Risk Measures",
    "url": "https://arxiv.org/abs/2607.04392",
    "source": "Mathias Beiglb\\\"ock, Silvana M. Pesenti, Maxime Sylvestre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04392v1 Announce Type: new Abstract: In static risk measurement, law invariance expresses the principle that the risk of a position should depend only on its distribution, and not on the pa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04753",
    "domain": "金融",
    "title": "Fooling Yourself: how narratives shape beliefs",
    "url": "https://arxiv.org/abs/2607.04753",
    "source": "Andrea Albertazzi, Paolo Pin, Marco Stimolo, Alessandro Stringhi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04753v1 Announce Type: new Abstract: Decision-makers usually receive information through narratives that combine diagnostic evidence with nondiagnostic details. In a laboratory experiment, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04781",
    "domain": "金融",
    "title": "Renewing Reliability: Valuation and Credit Risk Adjustments for Renewable Power Purchase Agreements",
    "url": "https://arxiv.org/abs/2607.04781",
    "source": "Nicola Bartolini, Silvia Romagnoli, Amia Santini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T04:00:00+00:00",
    "summary": "arXiv:2607.04781v1 Announce Type: new Abstract: Power Purchase Agreements (PPAs) are bilateral over-the-counter contracts central to renewable energy financing. While their capacity to stabilise reven"
  }
]
```
