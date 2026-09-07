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

- 今日日期：`2026-09-07`
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
  "date": "2026-09-07",
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
    "points": 1819292,
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
    "points": 1252239,
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
    "points": 1169654,
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
    "points": 1078003,
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
    "points": 735256,
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
    "points": 716056,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 673027,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 587474,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 499435,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 441844,
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
    "points": 407145,
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
    "points": 353738,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 345991,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 280949,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 270789,
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
    "points": 255769,
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
    "points": 180748,
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
    "points": 164643,
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
    "points": 162630,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 139479,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 109982,
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
    "points": 98844,
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
    "points": 93588,
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
    "points": 74301,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54871,
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
    "points": 47683,
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
    "points": 41519,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 40265,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39633,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1ATtE6bEKr",
    "domain": "AI",
    "title": "新Qoder来了，这次不止要做编程！我用它做了一个数字化转型项目！",
    "url": "http://www.bilibili.com/video/av117199255705243",
    "source": "伊江痕",
    "platform": "bilibili",
    "points": 38031,
    "published_at": "2026-09-02T04:00:00+00:00",
    "summary": "这是你的新版Qoder青年大学习！"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 35396,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 35213,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29711,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1FSLgz9EX6",
    "domain": "AI",
    "title": "强烈推荐！这绝对是2025年AI Agent入门天花板教程！AI大佬86集精讲，全篇通俗易懂！让你少走99%弯路！agent实战/agent开发/AI大模型",
    "url": "http://www.bilibili.com/video/av114392762943758",
    "source": "从零学AI_李沐",
    "platform": "bilibili",
    "points": 28236,
    "published_at": "2025-04-24T11:49:09+00:00",
    "summary": "感谢小伙伴们的收看，配套籽料已全部整理。"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 23860,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22763,
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
    "points": 21281,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1N4tH6GE2h",
    "domain": "AI",
    "title": "Anthropic重磅史诗升级！Claude Code 2.0全自动模式深度实测，多智能体协同全自动写完项目！",
    "url": "http://www.bilibili.com/video/av117184256810815",
    "source": "进化中的阿陈",
    "platform": "bilibili",
    "points": 19290,
    "published_at": "2026-08-30T11:39:11+00:00",
    "summary": "程序员彻底被解放了！Anthropic 重磅发布 Claude Code 2.0！新增王炸级 Auto Mode 全自动模式，无需人工确认全自动写完复杂项目；多 Sub-Agents 智能体协同并行开发，原生内置 iOS 模拟器实时调试 App 与无头浏览器测试，配合 Opus 5 简直强到离谱，速看实测！"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 18662,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 17425,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 15990,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV14Utf6QEnB",
    "domain": "AI",
    "title": "Vibe Coding 术语课：别再管所有弹窗都叫「弹窗」了｜前端：弹窗与提示 12 术语网页演示",
    "url": "http://www.bilibili.com/video/av117207627467822",
    "source": "ZTough",
    "platform": "bilibili",
    "points": 15111,
    "published_at": "2026-09-03T14:42:06+00:00",
    "summary": "网页上那些 &quot;突然冒出来的东西&quot; 到底都叫啥？Alert、Toast、Modal、Drawer、Popconfirm、Tooltip…… 这一期把 12 个前端弹窗与提示术语一次讲清，每个都在真实网页里演示给你看，看完就分得清。\nVibe Coding 术语课持续更新，前端开发、UI 组件、网页开发相关术语每周讲解。觉得有用就点赞、投币、收藏，一键三连支持一下，也欢迎评论区告诉"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15060,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1ZBT2ztEwp",
    "domain": "AI",
    "title": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程",
    "url": "http://www.bilibili.com/video/av114642592469769",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 13860,
    "published_at": "2025-06-07T14:53:38+00:00",
    "summary": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程"
  },
  {
    "id": "bvid:BV1oc4m6wEoD",
    "domain": "AI",
    "title": "【江科大】如何用AI全流程开发STM32",
    "url": "http://www.bilibili.com/video/av117180431736152",
    "source": "拉咯比哩",
    "platform": "bilibili",
    "points": 11979,
    "published_at": "2026-08-30T02:00:00+00:00",
    "summary": "江科大老学长带你 FreeRTOS 项目实践 STM32F103 + Cube MX + FreeRTOS + 面向对象 + 项目框架\n这是AI入门篇，前置章节请见之前的视频\n此篇章将从零开始，用AI实现一套简单的系统\n感谢大家支持"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10927,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1dogD6aERB",
    "domain": "AI",
    "title": "2026年医学生必看的【AI+医学】最强教程来了（学习路线+完整教程）手把手教你医学方向如何结合AI搞定论文和项目！",
    "url": "http://www.bilibili.com/video/av116968686359676",
    "source": "迪哥AI大讲堂-",
    "platform": "bilibili",
    "points": 10282,
    "published_at": "2026-07-23T17:38:08+00:00",
    "summary": "迪哥给大家准备了医学人工智能学习资料包，可在评论区获取！\n包含：\n1、上百篇医学方向人工智能顶会论文+源码\n2、90+各种疾病医疗数据集\n3、人工智能医学领域经典实战项目\n4、医学生必备的学习路线图"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 10279,
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
    "points": 9484,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 9149,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1987,
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
    "id": "hn:49548952",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to acquire Hugging Face",
    "url": "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html",
    "source": "tosh",
    "platform": "hackernews",
    "points": 328,
    "published_at": "2026-09-03T12:10:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49567357",
    "domain": "AI 算力 / 半导体",
    "title": "Georgi Gerganov on llama.cpp/ggml future after Nvidia acquisition of HuggingFace",
    "url": "https://twitter.com/ggerganov/status/2095897173376618881",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-04T17:12:22+00:00",
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
    "id": "hn:49594189",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang says 'AGI has arrived' and congratulates OpenAI",
    "url": "https://www.businessinsider.com/nvidia-jensen-huang-agi-openai-astra-ai-2026-9",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-07T05:23:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49557813",
    "domain": "AI 算力 / 半导体",
    "title": "Tell HN: NVIDIA's Acquisition of HuggingFace was for $HuggingFace",
    "url": "https://news.ycombinator.com/item?id=49557813",
    "source": "MontagFTB",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-03T22:08:41+00:00",
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
    "id": "hn:49552375",
    "domain": "AI 算力 / 半导体",
    "title": "Texas Data Center Map: See where data centers are operating or planned",
    "url": "https://www.kxan.com/news/texas/texas-data-center-tracker-see-where-600-projects-are-operating-or-planned-across-state-in-interactive-map/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-09-03T16:10:12+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/kioxias-flash-for-dram-initiative-eyes-ai-workloads/",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia’s Flash-for-DRAM Initiative Eyes AI Workloads",
    "url": "https://www.eetimes.com/kioxias-flash-for-dram-initiative-eyes-ai-workloads/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T08:01:30+00:00",
    "summary": "The CXL-attached memory expansion uses NAND flash optimized for high-speed processing alongside AI compute devices. The post Kioxia&#8217;s Flash-for-DRAM Initiative Eyes AI Workloads appeared first o"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/single-slot-low-profile-75w-rtx-3060-with-no-power-connectors-disappoints-in-tests-gpu-runs-entirely-off-the-pcie-slot-but-offers-severely-crippled-performance-and-frightening-thermals",
    "domain": "AI 算力 / 半导体",
    "title": "Single-slot low-profile 75W RTX 3060 with no power connectors disappoints in tests — GPU runs entirely off the PCIe slot, but offers severely crippled performance and frightening thermals",
    "url": "https://www.tomshardware.com/pc-components/gpus/single-slot-low-profile-75w-rtx-3060-with-no-power-connectors-disappoints-in-tests-gpu-runs-entirely-off-the-pcie-slot-but-offers-severely-crippled-performance-and-frightening-thermals",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T14:58:29+00:00",
    "summary": "If you want to cut your 12GB RTX 3060's performance in half while worsening its thermals, this might be the perfect product for you."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-admits-to-wiki-incident-after-its-agents-were-discovered-using-a-programming-hub-to-communicate-says-more-transparency-is-needed-regarding-misalignments",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI admits to 'wiki incident' after its agents were discovered using a programming hub to communicate — says more transparency is needed regarding misalignments",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-admits-to-wiki-incident-after-its-agents-were-discovered-using-a-programming-hub-to-communicate-says-more-transparency-is-needed-regarding-misalignments",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T14:31:54+00:00",
    "summary": "OpenAI has admitted that its experimental AI agents used an open German programming wiki to communicate."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/fsp-mega-gm-1200w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "FSP Mega GM 1200W power supply review: An in-house FSP platform that quietly overshoots its own Gold label",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/fsp-mega-gm-1200w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T13:57:18+00:00",
    "summary": "The FSP Mega GM 1200W power supply features Platinum-grade efficiency, an all-Japanese capacitor set, and a compact footprint that is rare on a 1200W unit."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/bitcoin-mining-data-center-condemned-after-leaking-3-million-gallons-of-water-and-forcing-school-closures-facility-operated-for-years-under-a-city-stop-work-order",
    "domain": "AI 算力 / 半导体",
    "title": "Bitcoin mining data center condemned after leaking 3 million gallons of water and forcing school closures — facility operated for years under a city stop-work order",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/bitcoin-mining-data-center-condemned-after-leaking-3-million-gallons-of-water-and-forcing-school-closures-facility-operated-for-years-under-a-city-stop-work-order",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T13:44:22+00:00",
    "summary": "A Bitcoin mining data center in El Reno, Oklahoma has been condemned after it leaked 3 million gallons of water."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-pcie-4-0-ssd-falls-to-usd339-99-on-amazon-usd190-discount-makes-high-capacity-storage-more-affordable",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung 990 2TB PCIe 4.0 SSD falls to $339.99 on Amazon — $190 discount makes high-capacity storage more affordable",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-pcie-4-0-ssd-falls-to-usd339-99-on-amazon-usd190-discount-makes-high-capacity-storage-more-affordable",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T13:08:31+00:00",
    "summary": "Samsung's 2TB 990 offers plenty of fast storage for games and is currently $190 cheaper than its regular $529.99 price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/msi-meg-coreliquid-e15-360-aio-review-bold-and-stunning-with-market-leading-performance",
    "domain": "AI 算力 / 半导体",
    "title": "MSI MEG CoreLiquid E15 360 AIO Review: Bold and stunning, with market-leading performance",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/msi-meg-coreliquid-e15-360-aio-review-bold-and-stunning-with-market-leading-performance",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T12:48:03+00:00",
    "summary": "MSI’s MEG CoreLiquid E15 360 AIO is a luxury cooling product, with a stunning 6.7-inch screen and industry-leading thermal performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/sales-of-cd-and-vinyl-music-sees-strong-resurgence-amid-physical-media-backlash-us-sales-of-retro-media-were-up-59-percent-and-18-percent-respectively-in-h1-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Sales of CD and vinyl music sees strong resurgence amid physical media backlash — US sales of ‘retro media’ were up 59% and 18%, respectively, in H1 2026",
    "url": "https://www.tomshardware.com/service-providers/streaming/sales-of-cd-and-vinyl-music-sees-strong-resurgence-amid-physical-media-backlash-us-sales-of-retro-media-were-up-59-percent-and-18-percent-respectively-in-h1-2026",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T12:16:13+00:00",
    "summary": "Music industry physical revenues jumped by 25.9% in H1 2026, 'powered by 17.7% vinyl growth and a 58.6% increase in CDs,' reported the RIAA."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/ps5-emulator-can-now-run-the-console-version-of-gta-v-at-up-to-60-fps-on-pc-but-quickly-crashes-as-tweakers-continue-to-optimize-ps5-emulation-advancing-at-an-astronomical-pace-leading-up-to-gta-vi-launch",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 emulator can now run the console version of GTA V at up to 60 FPS on PC, but quickly crashes as tweakers continue to optimize — PS5 emulation advancing at an astronomical pace leading up to GTA VI",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/ps5-emulator-can-now-run-the-console-version-of-gta-v-at-up-to-60-fps-on-pc-but-quickly-crashes-as-tweakers-continue-to-optimize-ps5-emulation-advancing-at-an-astronomical-pace-leading-up-to-gta-vi-launch",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T11:48:08+00:00",
    "summary": "A spark was lit under the PS5 emulation scene a couple of months ago and instead of fading over time, it seems to be burning brighter than ever. GTA V now runs between 40-60 FPS for a few minutes befo"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/former-old-school-runescape-dev-gets-jail-time-for-stealing-usd400-000-from-players-virtual-gold-stolen-and-sold-on-the-black-market-before-jagex-caught-the-culprit-using-hidden-firewall-tweaks",
    "domain": "AI 算力 / 半导体",
    "title": "Former Old School RuneScape dev gets jail time for stealing $400,000 from players — virtual gold stolen and sold on the black market before Jagex caught the culprit using hidden firewall tweaks",
    "url": "https://www.tomshardware.com/video-games/former-old-school-runescape-dev-gets-jail-time-for-stealing-usd400-000-from-players-virtual-gold-stolen-and-sold-on-the-black-market-before-jagex-caught-the-culprit-using-hidden-firewall-tweaks",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T10:30:00+00:00",
    "summary": "A former Jagex employee stole over $400,000 worth of in-game items and virtual currency from OSRS players and sold them on the black market. He was eventually arrested and sentenced to a three-year pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/this-246tb-ssd-media-server-is-built-for-millionaire-cinephiles-kaleidescapes-newest-home-theater-vault-supports-25-simultaneous-4k-streams-stores-up-to-2-300-4k-cinematic-movies",
    "domain": "AI 算力 / 半导体",
    "title": "This 246TB SSD media server is built for millionaire cinephiles —Kaleidescape's newest home theater vault supports 25 simultaneous 4K streams, stores up to 2,300 4K cinematic movies",
    "url": "https://www.tomshardware.com/pc-components/storage/this-246tb-ssd-media-server-is-built-for-millionaire-cinephiles-kaleidescapes-newest-home-theater-vault-supports-25-simultaneous-4k-streams-stores-up-to-2-300-4k-cinematic-movies",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T10:00:00+00:00",
    "summary": "Kaleidescape, a maker of luxury home theater equipment, has revealed its latest media server, the \"Compact Terra Prime 246TB SSD.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-nearly-50-percent-on-this-awesome-16-inch-oled-laptop-with-a-ryzen-ai-5-430-cpu-and-16gb-ram-hps-macbook-neo-beating-omnibook-x-flip-is-down-to-just-usd699",
    "domain": "AI 算力 / 半导体",
    "title": "Save nearly 50% on this awesome 16-inch OLED laptop with a Ryzen AI 5 430 CPU & 16GB RAM — HP's MacBook Neo-beating OmniBook X Flip is down to just $699",
    "url": "https://www.tomshardware.com/pc-components/save-nearly-50-percent-on-this-awesome-16-inch-oled-laptop-with-a-ryzen-ai-5-430-cpu-and-16gb-ram-hps-macbook-neo-beating-omnibook-x-flip-is-down-to-just-usd699",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T18:51:54+00:00",
    "summary": "If you're looking for a capable machine for everyday tasks and media consumption without breaking the bank, there isn't a better deal out there than this one."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/stripped-down-windows-11-for-ai-developers-demands-64gb-ram-and-insane-250-gb-s-bandwidth-project-zenith-will-debut-on-amds-flagship-ryzen-ai-halo-platform",
    "domain": "AI 算力 / 半导体",
    "title": "Stripped-down Windows 11 for AI developers demands 64GB RAM and insane 250 GB/s bandwidth — Project Zenith will debut on AMD's flagship Ryzen AI Halo platform",
    "url": "https://www.tomshardware.com/software/windows/stripped-down-windows-11-for-ai-developers-demands-64gb-ram-and-insane-250-gb-s-bandwidth-project-zenith-will-debut-on-amds-flagship-ryzen-ai-halo-platform",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T17:18:57+00:00",
    "summary": "Project Zenith is a version of Windows 11 that lets developers work right out of the box. It comes pre-installed with developer tools like Visual Studio Code, GitHub Copilot, and WSL 2+ Ubuntu, among "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/gamescom-apologizes-after-backlash-over-callous-response-to-indie-dev-hardware-thefts-pledges-security-overhaul-and-invites-devs-to-the-roundtable",
    "domain": "AI 算力 / 半导体",
    "title": "Gamescom apologizes after backlash over callous response to indie dev hardware thefts — pledges security overhaul and invites devs to the roundtable",
    "url": "https://www.tomshardware.com/video-games/gamescom-apologizes-after-backlash-over-callous-response-to-indie-dev-hardware-thefts-pledges-security-overhaul-and-invites-devs-to-the-roundtable",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T16:18:54+00:00",
    "summary": "The Gamescom organizers apologized for their initial response and outlined plans to prevent future incidents. They also praised the community for supporting the affected developers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-returns-to-selling-founders-edition-rtx-50-series-gpus-at-msrp-in-person-at-pax-west-verified-priority-access-has-rtx-5090-rtx-5080-and-rtx-5070-at-list-price",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia returns to selling Founder's Edition RTX 50-series GPUs at MSRP in person at PAX West — Verified Priority Access has RTX 5090, RTX 5080, and RTX 5070 at list price",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-returns-to-selling-founders-edition-rtx-50-series-gpus-at-msrp-in-person-at-pax-west-verified-priority-access-has-rtx-5090-rtx-5080-and-rtx-5070-at-list-price",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T15:04:13+00:00",
    "summary": "Nvidia is offering its RTX 5090, RTX 5080, and RTX 5070 Founder's Edition models at MSRP at PAX West."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-reportedly-prepping-ryzen-5-7500-non-f-cpu-with-integrated-graphics-at-double-the-price-six-core-zen-4-chip-rumored-to-share-identical-specs-with-its-f-moniker-cousin",
    "domain": "AI 算力 / 半导体",
    "title": "AMD reportedly prepping Ryzen 5 7500 (non-F) CPU with integrated graphics at double the price — Six-core Zen 4 chip rumored to share identical specs with its F-moniker cousin",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-reportedly-prepping-ryzen-5-7500-non-f-cpu-with-integrated-graphics-at-double-the-price-six-core-zen-4-chip-rumored-to-share-identical-specs-with-its-f-moniker-cousin",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T13:09:23+00:00",
    "summary": "A new report suggests AMD is preparing a non-F version of the Ryzen 5 7500F with integrated graphics. It would cost 230 Euros, or $267, which would put it above even the 7600X3D in terms of pricing, d"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/best-of-ifa-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best of IFA 2026: MacBook Neo competitors, monitors, and wild laptop concepts",
    "url": "https://www.tomshardware.com/tech-industry/best-of-ifa-2026",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T12:05:00+00:00",
    "summary": "This year in Berlin, IFA exhibitors showed off several affordable, colorful new laptops, some wild concept devices, and a surprising number of monitors that run the gamut from budget to high-refresh O"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-on-amds-rdna-4-gpus-rx-9070-xt-only-manages-30-fps-at-1080p-right-now-but-5070-ti-level-performance-is-the-eventual-goal",
    "domain": "AI 算力 / 半导体",
    "title": "Modder gets Nvidia's DLSS 5 working on AMD's RDNA 4 GPUs — RX 9070 XT only manages 30 FPS at 1080p right now, but 5070 Ti-level performance is the eventual goal",
    "url": "https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-on-amds-rdna-4-gpus-rx-9070-xt-only-manages-30-fps-at-1080p-right-now-but-5070-ti-level-performance-is-the-eventual-goal",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T12:00:00+00:00",
    "summary": "If you have an RX 9000 series GPU, you can try out DLSS 5 on your PC right now and absolutely destroy the stable performance you were getting before."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/cloud-gaming/xbox-game-pass-adds-monthly-time-limits-subscribers-and-non-subcribers-can-buy-more-hours-to-keep-gaming",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox Game Pass imposes monthly cloud gaming limits, just 15 hours per month for Ultimate — subscribers and non-subscribers can buy more hours to keep gaming",
    "url": "https://www.tomshardware.com/video-games/cloud-gaming/xbox-game-pass-adds-monthly-time-limits-subscribers-and-non-subcribers-can-buy-more-hours-to-keep-gaming",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:45:00+00:00",
    "summary": "Microsoft has added monthly limits to its Xbox Game Pass cloud gaming service, where subscribers and non-subscribers can purchase extra playtime when they surpass their limits."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dodge-the-rampocalypse-with-20-percent-discounts-on-corsair-ram-hundreds-off-on-32gb-and-64gb-ddr5-6400-kits",
    "domain": "AI 算力 / 半导体",
    "title": "Dodge the RAMpocalypse with 20% discounts on Corsair RAM — hundreds off on 32GB and 64GB DDR5-6400 kits",
    "url": "https://www.tomshardware.com/pc-components/dodge-the-rampocalypse-with-20-percent-discounts-on-corsair-ram-hundreds-off-on-32gb-and-64gb-ddr5-6400-kits",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:30:00+00:00",
    "summary": "Enjoy limited-time discounts of up to 23% on select Corsair DDR5 memory kits."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/worlds-first-fully-transparent-video-game-console-is-on-its-way-to-kickstarter-arduview-handhelds-shell-pcb-and-display-are-all-transparent",
    "domain": "AI 算力 / 半导体",
    "title": "‘World’s first fully transparent video game console’ is on its way to Kickstarter — Arduview handheld’s shell, PCB, and display are all transparent",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/worlds-first-fully-transparent-video-game-console-is-on-its-way-to-kickstarter-arduview-handhelds-shell-pcb-and-display-are-all-transparent",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:12:46+00:00",
    "summary": "The first units of the ‘world’s first fully transparent video game console’ are shipping to founders, and now the Arduview project is on its way to Kickstarter."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/we-tested-dlss-5-in-nba-2k27-with-every-rtx-50-series-gpu-first-official-release-comes-with-a-big-performance-hit-but-almost-every-blackwell-card-can-run-it-at-1080p",
    "domain": "AI 算力 / 半导体",
    "title": "We tested DLSS 5 in NBA 2K27 with every RTX 50-series GPU — first official release comes with a big performance hit, but almost every Blackwell card can run it at 1080p",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/we-tested-dlss-5-in-nba-2k27-with-every-rtx-50-series-gpu-first-official-release-comes-with-a-big-performance-hit-but-almost-every-blackwell-card-can-run-it-at-1080p",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T11:00:00+00:00",
    "summary": "We tested Nvidia's DLSS 5 in NBA 2K27 across every RTX 50-series graphics card at 1080p, 1440p, and 4K to see just how much performance it costs to explore the frontiers of neural rendering."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/taiwan-cracks-down-on-tech-businesses-with-illegal-chinese-ownership-166-investigations-and-at-least-36-convictions-since-2020",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan cracks down on tech businesses with illegal Chinese ownership — 166 investigations and at least 36 convictions since 2020",
    "url": "https://www.tomshardware.com/tech-industry/policy/taiwan-cracks-down-on-tech-businesses-with-illegal-chinese-ownership-166-investigations-and-at-least-36-convictions-since-2020",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T10:40:00+00:00",
    "summary": "Taiwan's top investigative agency has been tracking Chinese businesses operating on the island without proper authority and shutting them down. These companies have been hiring Taiwanese experts to he"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/trump-slaps-up-to-100-percent-tariffs-on-imported-drones-and-critical-components-in-latest-move-against-chinas-proliferation-of-u-s-drone-market-citing-national-security-products-from-allied-nation-face-10-15-percent-rates",
    "domain": "AI 算力 / 半导体",
    "title": "Trump slaps up to 100% tariffs on imported drones and critical components in latest move against China's proliferation of U.S. drone market, citing national security — products from allied nation face",
    "url": "https://www.tomshardware.com/tech-industry/drones/trump-slaps-up-to-100-percent-tariffs-on-imported-drones-and-critical-components-in-latest-move-against-chinas-proliferation-of-u-s-drone-market-citing-national-security-products-from-allied-nation-face-10-15-percent-rates",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T10:20:00+00:00",
    "summary": "The Trump administration has imposed tariffs of up to 100% on imported drones and key components, as Washington intensifies its push to reduce reliance on Chinese drone technology and rebuild a domest"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/japan-to-mass-procure-3d-printed-rocket-powered-drone-interceptor-terra-b1-capable-of-countering-one-way-attack-platforms",
    "domain": "AI 算力 / 半导体",
    "title": "Japan to mass-procure 3D-printed rocket-powered drone interceptor — Terra B1 capable of countering one-way attack platforms",
    "url": "https://www.tomshardware.com/tech-industry/drones/japan-to-mass-procure-3d-printed-rocket-powered-drone-interceptor-terra-b1-capable-of-countering-one-way-attack-platforms",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T10:00:00+00:00",
    "summary": "Japan’s military has decided to mass-procure Terra B1 interceptor drones. These drones are made using 3D printers and are based on the tried and tested A1 model from Terra Drone, which began to be dep"
  },
  {
    "id": "hn:49552616",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Mireye (YC S26) – Infrastructure for Physical World AI Agents",
    "url": "https://news.ycombinator.com/item?id=49552616",
    "source": "anshchokshi",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-03T16:24:13+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/ee-times-magazine-september-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "EE Times Magazine – September 2026",
    "url": "https://www.eetimes.com/ee-times-magazine-september-2026/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T22:40:26+00:00",
    "summary": "The September 2026 edition of EE Times Magazine examines how smarter buildings combine ambient energy harvesting, sensing, AI, and connected systems to improve safety while protecting privacy. The pos"
  },
  {
    "id": "rss:https://www.eetimes.com/when-the-package-becomes-an-electrical-design-variable/",
    "domain": "AI 算力 / 半导体",
    "title": "When the Package Becomes an Electrical Design Variable",
    "url": "https://www.eetimes.com/when-the-package-becomes-an-electrical-design-variable/",
    "source": "Takaki Murata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:50:10+00:00",
    "summary": "AI power integrity now lives inside the package, not just the PCB. Treat chip, package, and board as one PDN. The post When the Package Becomes an Electrical Design Variable appeared first on EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/7-steps-to-take-now-meet-the-eu-cra-9-11-26-reporting-deadline/",
    "domain": "AI 算力 / 半导体",
    "title": "7 Steps to Take Now: Meet the EU CRA 9/11/26 Reporting Deadline",
    "url": "https://www.eetimes.com/7-steps-to-take-now-meet-the-eu-cra-9-11-26-reporting-deadline/",
    "source": "By Colin Duggan, CEO and co-founder, BG Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:31:18+00:00",
    "summary": "Prepare for the EU Cyber Resilience Act's September 2026 reporting deadline; follow these seven steps to ensure compliance and readiness. The post 7 Steps to Take Now: Meet the EU CRA 9/11/26 Reportin"
  },
  {
    "id": "rss:https://www.eetimes.com/techworks-aligns-u-k-semiconductors-under-uksia-umbrella/",
    "domain": "AI 算力 / 半导体",
    "title": "TechWorks Aligns U.K. Semiconductors Under UKSIA Umbrella",
    "url": "https://www.eetimes.com/techworks-aligns-u-k-semiconductors-under-uksia-umbrella/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T13:46:01+00:00",
    "summary": "TechWorks corrals U.K. chip groups under UKSIA as funding surges 65% and 700 execs swarm London. The post TechWorks Aligns U.K. Semiconductors Under UKSIA Umbrella appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/display-developments-challenge-controllers/",
    "domain": "AI 算力 / 半导体",
    "title": "Display Developments Challenge Controllers",
    "url": "https://www.eetimes.com/display-developments-challenge-controllers/",
    "source": "Teng Tang Yang, Senior Division Director of Product Marketing Division, UMC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T13:00:00+00:00",
    "summary": "Discover how AMOLED, micro-OLED and advanced DDIC technologies are transforming displays with higher resolution, lower power and immersive experiences. The post Display Developments Challenge Controll"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/dlss-5-officially-launches-inside-nba-2k27-limited-to-rtx-50-series-gpus-for-now-nvidia-promises-to-bring-neutral-rendering-tech-to-rtx-40-series-soon",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 5 officially launches inside NBA 2K27, limited to RTX 50-series GPUs for now — Nvidia promises to bring neutral rendering tech to RTX 40-series soon",
    "url": "https://www.tomshardware.com/pc-components/gpus/dlss-5-officially-launches-inside-nba-2k27-limited-to-rtx-50-series-gpus-for-now-nvidia-promises-to-bring-neutral-rendering-tech-to-rtx-40-series-soon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:09:31+00:00",
    "summary": "Nvidia's controversial neural-rendering tech, DLSS 5, is now officially available in NBA 2K27, marking the start of a new era for the company. DLSS 5 will also come to RTX 40-series soon after current"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/grab-a-new-3d-printer-for-as-low-as-usd229-right-now-in-crealitys-labor-day-flash-sale-with-up-to-50-percent-off-big-sale-discounts-also-include-resin-and-filament-bundles-along-with-3d-scanners-and-toolkits",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a new 3D printer for as low as $229 right now in Creality's Labor Day flash sale, with up to 50% off —big sale discounts also include resin and filament bundles, along with 3D scanners and toolki",
    "url": "https://www.tomshardware.com/3d-printing/grab-a-new-3d-printer-for-as-low-as-usd229-right-now-in-crealitys-labor-day-flash-sale-with-up-to-50-percent-off-big-sale-discounts-also-include-resin-and-filament-bundles-along-with-3d-scanners-and-toolkits",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:00:00+00:00",
    "summary": "Grab a new 3D printer in Creality's Labor Day flash sale, with discounts on printers and accessories available."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/nas/minisforum-launches-local-ai-solutions-at-ifa-2026-ai-agent-nas-n5-and-ai-mini-workstation-ms-s1-use-amd-ryzen-ai-max-pro-495-processors-designed-to-run-models-locally",
    "domain": "AI 算力 / 半导体",
    "title": "Minisforum launches local AI solutions at IFA 2026 — AI Agent NAS N5 and AI Mini Workstation MS-S1 use AMD Ryzen AI Max+ Pro 495 processors designed to run models locally",
    "url": "https://www.tomshardware.com/pc-components/nas/minisforum-launches-local-ai-solutions-at-ifa-2026-ai-agent-nas-n5-and-ai-mini-workstation-ms-s1-use-amd-ryzen-ai-max-pro-495-processors-designed-to-run-models-locally",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:15:00+00:00",
    "summary": "Minisforum unveiled the NAS N5 Max-P495 and MS-S1 Max-P945 at IFA 2026. The NAS and mini-PC are powered by the AMD Ryzen AI Max+ Pro 495, which can be configured with up to 192GB of unified memory and"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd900-in-the-best-buy-labor-day-sale-on-tech-with-huge-discounts-on-gaming-pcs-laptops-and-monitors-secure-an-upgrade-fast-to-beat-rising-hardware-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to $900 in the Best Buy Labor Day sale on tech, with huge discounts on gaming PCs, laptops and monitors — secure an upgrade fast to beat rising hardware costs",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-usd900-in-the-best-buy-labor-day-sale-on-tech-with-huge-discounts-on-gaming-pcs-laptops-and-monitors-secure-an-upgrade-fast-to-beat-rising-hardware-costs",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:30:00+00:00",
    "summary": "There's a big Labor Day sale over at Best Buy right now, securing you huge discounts on tech, including gaming PCs, handhelds, laptops, and monitors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-faces-pricing-reckoning-as-token-volume-explodes-25-fold-mid-tier-models-deliver-90-percent-of-flagship-capability-at-one-sixth-the-cost",
    "domain": "AI 算力 / 半导体",
    "title": "Frontier AI faces pricing reckoning as token volume explodes 25-fold — mid-tier models deliver 90% of flagship capability at one-sixth the cost",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-faces-pricing-reckoning-as-token-volume-explodes-25-fold-mid-tier-models-deliver-90-percent-of-flagship-capability-at-one-sixth-the-cost",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T15:21:56+00:00",
    "summary": "As frontier AI developers push for cost savings as much as intelligence enhancements, new models push the boundaries of the pareto frontier, with even small advantages crowning new kings."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/nvidia-app-update-fails-to-block-unofficial-dlss-multi-frame-generation-on-rtx-40-series-modders-restore-support-across-multiple-games-within-hours",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia app update fails to block unofficial DLSS multi-frame generation mod on RTX 40 series gaming GPUs — modders restore support across multiple games within hours",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/nvidia-app-update-fails-to-block-unofficial-dlss-multi-frame-generation-on-rtx-40-series-modders-restore-support-across-multiple-games-within-hours",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T14:56:38+00:00",
    "summary": "When NVIDIA launched the GeForce RTX 50 series, a major part of the hype surrounding the new GPU family was its support for DLSS Multi-Frame Generation. This feature was officially locked to the new R"
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
    "id": "rss:https://www.eetimes.com/indias-quantum-journey-goes-beyond-the-qubit/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s Quantum Journey Goes Beyond the Qubit",
    "url": "https://www.eetimes.com/indias-quantum-journey-goes-beyond-the-qubit/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T08:00:47+00:00",
    "summary": "IBM’s Amaravati deployment could accelerate India’s quantum ecosystem as startups develop processors, software, and supporting technologies. The post India’s Quantum Journey Goes Beyond the Qubit appe"
  },
  {
    "id": "rss:https://www.eetimes.com/mercedes-spinout-athos-closes-its-doors/",
    "domain": "AI 算力 / 半导体",
    "title": "Mercedes Spinout Athos Closes Its Doors",
    "url": "https://www.eetimes.com/mercedes-spinout-athos-closes-its-doors/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T17:07:04+00:00",
    "summary": "The startup was unable to secure the financing required to continue commercialising its chiplet-based technology The post Mercedes Spinout Athos Closes Its Doors appeared first on EE Times."
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1157,
    "published_at": "2026-09-02T15:12:40+00:00",
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
    "id": "hn:49331423",
    "domain": "大厂 AI 动态",
    "title": "AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira",
    "url": "https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug",
    "source": "galnagli",
    "platform": "hackernews",
    "points": 424,
    "published_at": "2026-08-17T14:18:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49468818",
    "domain": "大厂 AI 动态",
    "title": "Gemini-3.5-Transcribe",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source": "k9294",
    "platform": "hackernews",
    "points": 363,
    "published_at": "2026-08-27T18:03:42+00:00",
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
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 297,
    "published_at": "2026-08-27T17:06:32+00:00",
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
    "id": "hn:49566788",
    "domain": "大厂 AI 动态",
    "title": "Project HydraFusion: Frontier quality via multi-model orchestration",
    "url": "https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/",
    "source": "qainsights",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-09-04T16:24:50+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/990932/seattle-times-newsday-lawsuit-openai-microsoft",
    "domain": "大厂 AI 动态",
    "title": "Seattle Times and Newsday sue OpenAI and Microsoft for infringement",
    "url": "https://www.theverge.com/ai-artificial-intelligence/990932/seattle-times-newsday-lawsuit-openai-microsoft",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T23:36:04+00:00",
    "summary": "The Seattle Times and Newsday are just the latest plaintiffs to take OpenAI to court, alleging copyright infringement. The two outlets say the company used their journalism as training data for its AI"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990918/amazon-cargo-plane-crashed-miami",
    "domain": "大厂 AI 动态",
    "title": "An Amazon cargo plane crashed at Miami International Airport",
    "url": "https://www.theverge.com/tech/990918/amazon-cargo-plane-crashed-miami",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T20:56:38+00:00",
    "summary": "A plane bearing an Amazon logo overran the runway at Miami International Airport on Sunday during landing, crashing into vehicles and resulting in multiple injuries. The extent of the damage or the se"
  },
  {
    "id": "rss:https://www.theverge.com/science/990906/isar-aerospace-europe-orbital-rocket-launch",
    "domain": "大厂 AI 动态",
    "title": "Europe has its first commercial orbital rocket",
    "url": "https://www.theverge.com/science/990906/isar-aerospace-europe-orbital-rocket-launch",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T19:04:22+00:00",
    "summary": "German company Isar Aerospace has successfully launched Europe's first entirely commercial orbital rocket. It attempted to achieve the feat last March, but that lasted all of 30 seconds before the veh"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990895/boox-picco-tiny-e-reader-november-ifa",
    "domain": "大厂 AI 动态",
    "title": "Boox’s tiny Picco e-reader should land in November",
    "url": "https://www.theverge.com/tech/990895/boox-picco-tiny-e-reader-november-ifa",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T16:28:58+00:00",
    "summary": "Boox teased the Picco, its take on the buzzy Xteink X4 e-reader, back in July, but provided almost no details. Now, thanks to some reporting out of IFA, we've got a bit more info, though sadly still n"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990436/fairphone-6-plus-review",
    "domain": "大厂 AI 动态",
    "title": "The Fairphone 6 Plus is the midrange phone we desperately needed",
    "url": "https://www.theverge.com/tech/990436/fairphone-6-plus-review",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T13:00:00+00:00",
    "summary": "The Fairphone 6 Plus feels like an extremely average midrange Android phone and I couldn't be more thrilled. The mission has always been admirable. Fairphone seeks out ethically sourced materials and "
  },
  {
    "id": "rss:https://www.theverge.com/games/990691/competitive-pokemon-champions-mobile-tournament-accessibility",
    "domain": "大厂 AI 动态",
    "title": "Competitive Pokémon is on phones now, but you still need a Switch to become a champion",
    "url": "https://www.theverge.com/games/990691/competitive-pokemon-champions-mobile-tournament-accessibility",
    "source": "Kallie Plagge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T13:00:00+00:00",
    "summary": "To get started with competitive Pok&#233;mon battles, all you need is your phone. But to compete at the highest level, like at the Pok&#233;mon World Championships, you're going to need a Switch. And "
  },
  {
    "id": "rss:https://www.theverge.com/column/990183/diy-plug-in-solar-us",
    "domain": "大厂 AI 动态",
    "title": "DIY plug-in solar gains momentum in the US",
    "url": "https://www.theverge.com/column/990183/diy-plug-in-solar-us",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on e-bikes, power stations, and how to work anywhere, follow Thomas Ricker. The Stepback arriv"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990873/earth-garden-globe-field-recordings",
    "domain": "大厂 AI 动态",
    "title": "Explore the globe in field recordings",
    "url": "https://www.theverge.com/tech/990873/earth-garden-globe-field-recordings",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T21:31:34+00:00",
    "summary": "I love field recordings. I love making them. I love them when they're incorporated into my ambient music. They're great background noise for working or sleeping. But they're also great for active list"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990868/iphone-handoff-ios-27",
    "domain": "大厂 AI 动态",
    "title": "iPhone Handoff will seamlessly share one number between two phones",
    "url": "https://www.theverge.com/tech/990868/iphone-handoff-ios-27",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T20:53:58+00:00",
    "summary": "When iOS 27 lands later this month, it will have a feature called iPhone Handoff that lets you switch between two phones using the same number. It was briefly mentioned during the WWDC keynote back in"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/990794/cd-sales-are-booming-as-physical-media-continues-its-resurgence",
    "domain": "大厂 AI 动态",
    "title": "CD sales are booming as physical media continues its resurgence",
    "url": "https://www.theverge.com/entertainment/990794/cd-sales-are-booming-as-physical-media-continues-its-resurgence",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T16:49:33+00:00",
    "summary": "According to the Recording Industry Association of America (RIAA), CD sales exploded in the first half of 2026. A new report from the organization says 17.5 million CDs were sold in the first six mont"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/06/phil-schillers-app-store-exit-reportedly-driven-by-wariness-over-future-plans/",
    "domain": "大厂 AI 动态",
    "title": "Phil Schiller’s App Store exit reportedly driven by wariness over future plans",
    "url": "https://techcrunch.com/2026/09/06/phil-schillers-app-store-exit-reportedly-driven-by-wariness-over-future-plans/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T21:41:06+00:00",
    "summary": "Schiller reportedly had reservations about new CEO John Ternus' goal of bringing in more recurring revenue from the App Store."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/",
    "domain": "大厂 AI 动态",
    "title": "Authors push back as publishers and agents make claims on Anthropic settlement",
    "url": "https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T20:47:37+00:00",
    "summary": "Authors say publishers seem to be claiming more than their fair share of settlement payments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/06/travis-kalanicks-atoms-might-be-getting-into-the-robotaxi-business/",
    "domain": "大厂 AI 动态",
    "title": "Travis Kalanick’s Atoms might be getting into the robotaxi business",
    "url": "https://techcrunch.com/2026/09/06/travis-kalanicks-atoms-might-be-getting-into-the-robotaxi-business/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T16:45:00+00:00",
    "summary": "The Uber founder has said that Atoms will allow him to complete \"unfinished business.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/06/techcrunch-mobility-tesla-cybercab-hits-the-road-and-a-snag/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Tesla Cybercab hits the road — and a snag",
    "url": "https://techcrunch.com/2026/09/06/techcrunch-mobility-tesla-cybercab-hits-the-road-and-a-snag/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T16:08:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/seattle-times-and-newsday-are-the-latest-publications-to-sue-openai-and-microsoft/",
    "domain": "大厂 AI 动态",
    "title": "Seattle Times and Newsday are the latest publications to sue OpenAI and Microsoft",
    "url": "https://techcrunch.com/2026/09/05/seattle-times-and-newsday-are-the-latest-publications-to-sue-openai-and-microsoft/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T22:49:55+00:00",
    "summary": "Two more news organizations are suing OpenAI and Microsoft over the supposed use of their journalism to train AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/hikers-rescued-after-using-google-gemini-for-planning/",
    "domain": "大厂 AI 动态",
    "title": "Hikers rescued after using Google Gemini for planning",
    "url": "https://techcrunch.com/2026/09/05/hikers-rescued-after-using-google-gemini-for-planning/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T19:35:24+00:00",
    "summary": "The sheriff’s office said the hikers “were advised by Gemini to bring far less food and water than their group required.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/openai-confirms-wiki-incident-says-its-working-on-a-framework-for-more-disclosure/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI confirms ‘wiki incident,’ says it’s ‘working on a framework’ for more disclosure",
    "url": "https://techcrunch.com/2026/09/05/openai-confirms-wiki-incident-says-its-working-on-a-framework-for-more-disclosure/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T18:05:27+00:00",
    "summary": "OpenAI acknowledged its role in a recently reported incident where AI agents took over a German wiki forum."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/cluckys-new-alarm-app-wakes-you-up-with-a-crowing-rooster/",
    "domain": "大厂 AI 动态",
    "title": "Clucky’s new alarm app wakes you up with a crowing rooster",
    "url": "https://techcrunch.com/2026/09/05/cluckys-new-alarm-app-wakes-you-up-with-a-crowing-rooster/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T17:00:00+00:00",
    "summary": "Clucky's new alarm app has an option where users are woken up to the sound of a rooster. They then complete a mission to turn it off."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/05/oura-is-going-public-but-these-smart-ring-companies-are-coming-for-its-crown/",
    "domain": "大厂 AI 动态",
    "title": "Oura is going public, but these smart ring companies are coming for its crown",
    "url": "https://techcrunch.com/2026/09/05/oura-is-going-public-but-these-smart-ring-companies-are-coming-for-its-crown/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T15:00:00+00:00",
    "summary": "While Oura has largely dominated the smart ring market for years, a growing number of rivals are now racing to dethrone it by trying all sorts of approaches to get an edge over it."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/german-company-becomes-first-in-europe-to-launch-fully-commercial-orbital-rocket/",
    "domain": "大厂 AI 动态",
    "title": "German company becomes first in Europe to launch fully commercial orbital rocket",
    "url": "https://arstechnica.com/space/2026/09/german-company-becomes-first-in-europe-to-launch-fully-commercial-orbital-rocket/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T11:55:26+00:00",
    "summary": "\"We achieved within a few years what had taken the European space industry decades before.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/farmed-salmon-may-not-be-as-nutritious-as-it-once-was-new-research-suggests/",
    "domain": "大厂 AI 动态",
    "title": "Farmed salmon may not be as nutritious as it once was, new research suggests",
    "url": "https://arstechnica.com/science/2026/09/farmed-salmon-may-not-be-as-nutritious-as-it-once-was-new-research-suggests/",
    "source": "Georgina Gustin, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T10:00:35+00:00",
    "summary": "The shift in the fish’s diet is having significant downstream impacts on the environment and climate."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/09/teslas-cybercab-has-been-deployed-and-its-already-under-investigation/",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s Cybercab has been deployed, and it’s already under investigation",
    "url": "https://arstechnica.com/cars/2026/09/teslas-cybercab-has-been-deployed-and-its-already-under-investigation/",
    "source": "Aarian Marshall, WIRED.COM",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T15:17:36+00:00",
    "summary": "The US government is investigating whether the Cybercab meets vehicle safety standards."
  },
  {
    "id": "rss:https://www.producthunt.com/products/tucky",
    "domain": "大厂 AI 动态",
    "title": "Tucky",
    "url": "https://www.producthunt.com/products/tucky",
    "source": "Mehdi Harzallah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T21:09:48+00:00",
    "summary": "Notes docked to your screen edge, with an AI agent inside Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/airuncode",
    "domain": "大厂 AI 动态",
    "title": "Airuncode",
    "url": "https://www.producthunt.com/products/airuncode",
    "source": "GUSTAVO ARRETURETA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T23:16:55+00:00",
    "summary": "Run multiple local coding agents on your machine Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/remind-7",
    "domain": "大厂 AI 动态",
    "title": "Remind",
    "url": "https://www.producthunt.com/products/remind-7",
    "source": "Chris Doyle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T16:10:46+00:00",
    "summary": "Full-screen meeting reminders with AI briefings Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/assist-4",
    "domain": "大厂 AI 动态",
    "title": "Assist",
    "url": "https://www.producthunt.com/products/assist-4",
    "source": "Abhishek Kumar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T10:08:53+00:00",
    "summary": "Voice annotate your Mac, get screenshots + clipboard manager Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/clipnote-2",
    "domain": "大厂 AI 动态",
    "title": "Clipnote",
    "url": "https://www.producthunt.com/products/clipnote-2",
    "source": "Okumura Daichi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T01:55:40+00:00",
    "summary": "Save your AI conversations so they persist after closing tab Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/113877",
    "domain": "大厂 AI 动态",
    "title": "「弯道超车」赛车入门指北 04：全场最快的车，为什么听一辆慢车指挥",
    "url": "https://sspai.com/post/113877",
    "source": "一群小羊说",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T07:00:00+00:00",
    "summary": "一辆远没有 F1 赛车快的车，凭什么让各路豪强乖乖排在后面，甚至左右冠军归属？查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/114103",
    "domain": "大厂 AI 动态",
    "title": "定义了 Apple 10 年的白色产品：iBook G3 Snow 怀旧手记",
    "url": "https://sspai.com/post/114103",
    "source": "随便好啦",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T03:10:02+00:00",
    "summary": "在金属机身成为 Mac 产品线标配的今天，让我们重温这台 2001 年的 iBook G3，找回属于聚碳酸酯时代的风格。查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/114250",
    "domain": "大厂 AI 动态",
    "title": "派早报：微软公布 Project Zenith 计划、F-Droid 拟效仿 Debian 制定生成式 AI 使用政策",
    "url": "https://sspai.com/post/114250",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T00:20:41+00:00",
    "summary": "美国 CD 销量大幅反弹，公安部上线反诈智能助手「国家反诈 AI」等。查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/114076",
    "domain": "大厂 AI 动态",
    "title": "让 Apple Watch 记录的每一趟游泳数据更有意义：即刻游",
    "url": "https://sspai.com/post/114076",
    "source": "ElijahLee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T07:00:00+00:00",
    "summary": "对于使用AppleWatch游泳的人来说，记录一次游泳并不困难。在手表上打开体能训练App，选择开始游泳，结束后就能在Apple健身中看到完整的游泳表现，包括时间、距离、卡路里、配速、心率等数据。但真 ...查看全文"
  },
  {
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "Google WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-09-03T16:06:08+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "XDOF, just three months out of stealth, is in talks for a Series B at a $1.2B valuation",
    "url": "https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:36:14+00:00",
    "summary": "The round is being raised just months after the robot data startup exited from stealth."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/openais-rogue-agents-keep-escaping-with-no-formal-process-to-investigate-them/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s rogue agents keep escaping, with no formal process to investigate them",
    "url": "https://techcrunch.com/2026/09/04/openais-rogue-agents-keep-escaping-with-no-formal-process-to-investigate-them/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T23:15:11+00:00",
    "summary": "OpenAI’s latest agent swarm incident adds urgency to calls for independent investigations as researchers and lawmakers question whether AI labs should control the scope of their own safety reviews."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/ai-compute-provider-nscale-is-looking-for-3-5b-in-pre-ipo-financing/",
    "domain": "大厂 AI 动态",
    "title": "AI compute provider Nscale is looking for $3.5B in pre-IPO financing",
    "url": "https://techcrunch.com/2026/09/04/ai-compute-provider-nscale-is-looking-for-3-5b-in-pre-ipo-financing/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T21:12:11+00:00",
    "summary": "Nscale, which recently struck a $45 billion deal with Anthropic, is in talks to raise additional funds in anticipation of an upcoming IPO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/judge-blocks-x-rival-from-using-twitter-name-but-allows-tweet-for-now/",
    "domain": "大厂 AI 动态",
    "title": "Judge blocks X rival from using Twitter name, but allows ‘Tweet’ for now",
    "url": "https://techcrunch.com/2026/09/04/judge-blocks-x-rival-from-using-twitter-name-but-allows-tweet-for-now/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:52:05+00:00",
    "summary": "A federal judge temporarily barred an X rival from using the Twitter name, but found that X was likely to have abandoned the “Tweet” trademark and bird logo. The startup has since relaunched as Tweet."
  },
  {
    "id": "rss:https://techcrunch.com/video/what-will-apples-john-ternus-era-look-like/",
    "domain": "大厂 AI 动态",
    "title": "What will Apple’s John Ternus era look like?",
    "url": "https://techcrunch.com/video/what-will-apples-john-ternus-era-look-like/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T17:18:00+00:00",
    "summary": "It&#8217;s&#160;officially the Ternus era at Apple.&#160;&#160; Tim Cook stepped down&#160;as CEO this week, handing the company to former hardware chief John Ternus, whose first memo&#160;promised a "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/no-little-kids-allowed-and-other-new-info-about-teslas-cybercab/",
    "domain": "大厂 AI 动态",
    "title": "No little kids allowed, and other new info about Tesla’s Cybercab",
    "url": "https://techcrunch.com/2026/09/04/no-little-kids-allowed-and-other-new-info-about-teslas-cybercab/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:51:23+00:00",
    "summary": "The company says no children under 13 can ride -- even with a parent. That's more restrictive than the Model Y SUVs it's using as robotaxis."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/",
    "domain": "大厂 AI 动态",
    "title": "Another swarm of OpenAI agents reached the open internet without the frontier lab’s knowledge",
    "url": "https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:21:11+00:00",
    "summary": "It's the latest failure of OpenAI's internal monitoring and security systems."
  },
  {
    "id": "wscn:3781223",
    "domain": "股票",
    "title": "高盛力挺中际旭创：1.6T光模块加速放量，今明两年净利润将大超市场预期",
    "url": "https://wallstreetcn.com/articles/3781223",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T08:05:43+00:00",
    "summary": "高盛高呼“买入”力挺中际旭创，看涨空间超200%。核心看好其1.6T光模块加速量产与硅光技术绝对壁垒，其2026/27年净利润预测分别较市场共识高出25%和42%，盈利预期远超市场共识。叠加最高80亿真金白银火速回购，助推市值重返万亿。"
  },
  {
    "id": "wscn:3781226",
    "domain": "股票",
    "title": "中国央行连续22个月扩大黄金储备",
    "url": "https://wallstreetcn.com/articles/3781226",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T08:03:56+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3781224",
    "domain": "股票",
    "title": "工信部：适时启动6G商用，到2030年智能算力规模达9800EFLOPS",
    "url": "https://wallstreetcn.com/articles/3781224",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T07:49:59+00:00",
    "summary": "规划还列出了13个主要指标，包括到2030年，信息通信行业收入达4.1万亿元，信息基础设施累计投资3.8万亿元，电信业务总量年均增速7%，每万人拥有5G（含5G-A）基站数为50个，智能算力规模达9800EFLOPS（每秒百亿亿次浮点运算），5G（含5G-A）用户普及率达95%等。"
  },
  {
    "id": "wscn:3781221",
    "domain": "股票",
    "title": "华为鸿蒙7正式发布，麒麟芯片时隔六年焕新登场",
    "url": "https://wallstreetcn.com/articles/3781221",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T07:47:04+00:00",
    "summary": "华为发布Mate XT 2三折叠手机，搭载最新麒麟9050 Pro芯片。该芯片采用逻辑折叠技术，在单芯片内分层排布逻辑单元并增设垂直互联通道，有效缩短信号传输路径、降低时延、提升性能。这是华为自Mate40系列发布会后，时隔六年再次在旗舰发布会上推出全新麒麟芯片。"
  },
  {
    "id": "wscn:3781204",
    "domain": "股票",
    "title": "CFA圆桌：Agentic AI 如何重塑金融工作流、投资流程与治理",
    "url": "https://wallstreetcn.com/articles/3781204",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T07:30:30+00:00",
    "summary": "CFA协会最新圆桌访谈指出，Agentic AI正通过“skills”和MCP服务器重塑金融工作流，使AI成为交互与执行核心。面对金融数据缺失，生成式模型驱动的“合成数据”正颠覆传统的压力测试与回测。然而，AI并未消除偏见，甚至因训练数据天生带有“损失厌恶”和资产偏好，模型存在严重的西方中心化和偏好美国科技股的倾向。"
  },
  {
    "id": "wscn:3781222",
    "domain": "股票",
    "title": "霍尔木兹海峡通航量降至5月来最低",
    "url": "https://wallstreetcn.com/articles/3781222",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T07:27:15+00:00",
    "summary": "截至本月6日的10天内，霍尔木兹海峡日均仅约10艘商业船舶通航，为5月以来最低。美军近期“摧毁”三艘伊朗油轮，伊朗则打击了3艘美国船只和3艘油轮。美伊海上互袭升级，商业油轮被当作施压工具。自7月6日以来，海峡周边已有27起船舶遭袭事件。伊朗还宣布将在霍尔木兹海峡外设禁区，进入船只将被制裁。"
  },
  {
    "id": "wscn:3781219",
    "domain": "股票",
    "title": "无源光器件的进击：为什么 FAU 价值量会快速膨胀？",
    "url": "https://wallstreetcn.com/premium/articles/3781219?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T07:16:30+00:00",
    "summary": "在 CPO/NPO 等高密度光互联方案推动下，FAU 正经历\"通道数跃升 + 精度收紧 + 定制化创新\"三重升级，单机价值量从 800G 时代的个位数美元级别膨胀至数倍乃至十余倍。"
  },
  {
    "id": "wscn:3781149",
    "domain": "股票",
    "title": "欧洲LNG库存15年来新低：欧亚抢气，谁扛不住这个冬天？",
    "url": "https://wallstreetcn.com/premium/articles/3781149?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T07:06:54+00:00",
    "summary": "霍尔木兹海峡封锁致卡塔尔供应锐减，欧亚抢气加剧，欧洲库存创十五年低点，冬季或破百，美国难补缺。"
  },
  {
    "id": "wscn:3781007",
    "domain": "股票",
    "title": "特朗普再袭伊朗：消耗战还是中期选前最后一搏？",
    "url": "https://wallstreetcn.com/premium/articles/3781007?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T06:55:12+00:00",
    "summary": "特朗普再袭伊朗，能源冲击与中期选举压力叠加，消耗战难以为继，战争终局或成为市场最大预期差。"
  },
  {
    "id": "wscn:3781194",
    "domain": "股票",
    "title": "科技股领涨亚洲，韩股大涨4%，SK海力士涨7%，海峡冲突推动油价上涨，金银下跌",
    "url": "https://wallstreetcn.com/articles/3781194",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T06:10:19+00:00",
    "summary": "韩国首尔综指日内涨幅扩大至4%，SK海力士涨逾7%，三星电子涨逾5%，为MSCI亚太指数的上行贡献最大。布伦特原油上涨1.1%，交投于每桶97美元上方；西德克萨斯中质原油上涨1.2%，报每桶92.53美元。现货黄金日内跌幅达1.0%，报4386.25美元/盎司；现货白银日内跌幅达1.0%，报65.48美元/盎司。"
  },
  {
    "id": "wscn:3781215",
    "domain": "股票",
    "title": "摩尔线程20%跌停！2577万股周一解禁，12月还有1.86亿股待解禁",
    "url": "https://wallstreetcn.com/articles/3781215",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T06:06:48+00:00",
    "summary": "摩尔线程在9月7日解禁2577万股限售股，导致流通盘激增近85%，引发技术性抛售并触及20%跌停。公司回应称，此次波动主要源于流通盘扩容，呼吁投资者\"理性处理、理性看待\"本次解禁带来的股价变化。12月即将迎来的更大规模解禁（约占总股本39.55%）或仍构成短期市场供给侧的主要压力。"
  },
  {
    "id": "wscn:3781214",
    "domain": "股票",
    "title": "黄仁勋：AGI已到来！OpenAI Astra背后是英伟达，40万张GPU即将上线",
    "url": "https://wallstreetcn.com/articles/3781214",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T06:05:58+00:00",
    "summary": "黄仁勋高呼“AGI已来”，OpenAI旗舰模型Astra由超10万张英伟达芯片训练而成。其“40万张GPU即将上线”的重磅预告，更释放出算力需求井喷的强烈信号。"
  },
  {
    "id": "wscn:3781213",
    "domain": "股票",
    "title": "美债才是AI泡沫的“终极杀手”？机构警告：10年期收益率破5%或成引爆点",
    "url": "https://wallstreetcn.com/articles/3781213",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T05:44:28+00:00",
    "summary": "洛克菲勒国际董事长认为，本轮美国债务过剩源于政府而非企业，高企的财政赤字推动10年期美债收益率逼近5%关口。由于AI基建千亿美元级的资金缺口极度依赖外部融资，美债收益率若突破5%将产生严重挤出效应，大幅抬高AI企业的发债与股权融资成本，恐将直接刺破AI泡沫并冲击股市估值。"
  },
  {
    "id": "wscn:3781200",
    "domain": "股票",
    "title": "创业板涨超3%，算力硬件爆发、中际旭创市值重回万亿，摩尔线程上市以来首次跌停，恒科指跌1%，权重科网股多数承压",
    "url": "https://wallstreetcn.com/articles/3781200",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T05:23:29+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市近3000股飘红，上午半天成交1.25万亿。沪深两市半日成交额1.24万亿，较上个交易日放量不足100亿。板块方面，AI应用侧表现突出，深南电路、剑桥科技等收获涨停，“易中天”、源杰科技、胜宏科技、长鑫科技等大涨。农业股继续活跃，餐饮旅游、零售、工业机械板块走强，煤炭、金融、石化、军工板块调整。摩尔线程因解禁原因闪崩跌停。"
  },
  {
    "id": "wscn:3781209",
    "domain": "股票",
    "title": "捷豹路虎启动全球自愿离职计划",
    "url": "https://wallstreetcn.com/articles/3781209",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T05:07:17+00:00",
    "summary": "将盈亏平衡销量降至约30万辆。"
  },
  {
    "id": "wscn:3781216",
    "domain": "股票",
    "title": "一周展望：聚焦美国CPI 美联储9月加息悬念进入倒计时",
    "url": "https://wallstreetcn.com/articles/3781216",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:45:04+00:00",
    "summary": "上周五远超预期的非农报告出炉之后，本周的市场目光将转向更为关键的CPI数据，这是美联储9月15-16..."
  },
  {
    "id": "wscn:3781201",
    "domain": "股票",
    "title": "从Astra到Atlas：AI下一场大革命，可能发生在三维世界",
    "url": "https://wallstreetcn.com/premium/articles/3781201?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:31:54+00:00",
    "summary": "GPT-6 Astra展示了AI从文字、图片和视频进一步走向可编辑三维资产的能力，World Labs Atlas则把这一变化推进到空间理解、世界重建和环境模拟层面。\n随着人工智能从数字世界迈向物理世界，三维数据正在从专业设计素材演变为机器理解现实环境的重要基础设施，空间数据采集、三维重建、仿真训练以及机器人和自动驾驶等行业，可能由此进入新的产业周期。"
  },
  {
    "id": "wscn:3781205",
    "domain": "股票",
    "title": "高盛复盘中国股票二季报：盈利增速创五年新高，增长从“硬科技”扩散到更多行业",
    "url": "https://wallstreetcn.com/articles/3781205",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T03:03:43+00:00",
    "summary": "高盛称，中国上市公司二季度盈利同比劲增24%，创五年新高，A股科创板利润翻倍，AI红利由芯片向多行业扩散；但消费仍疲弱、互联网承压，高盛维持超配A股。二季度表现最强的板块包括：IT（+142%）、保险（+140%）、材料（+78%）、能源（+52%）、券商（+58%）和医药（+20%）。"
  },
  {
    "id": "wscn:3781203",
    "domain": "股票",
    "title": "9月7日正式上市！农银沪深300质量ETF登陆上交所",
    "url": "https://wallstreetcn.com/articles/3781203",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T02:26:25+00:00",
    "summary": "9月7日，农银汇理沪深300质量交易型开放式指数证券投资基金正式在上海证券交易所挂牌上市，基金日常申..."
  },
  {
    "id": "wscn:3781197",
    "domain": "股票",
    "title": "日本疑似抛售美债为创纪录日元干预融资，外汇储备跌破万亿美元",
    "url": "https://wallstreetcn.com/articles/3781197",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T02:24:16+00:00",
    "summary": "日本8月创纪录动用约986亿美元干预汇市，疑似大规模抛售美债套现，令本已承压的美债市场再添供给隐忧。数据显示，日本外汇储备骤降946亿美元，跌破万亿美元大关，美财长贝森特随即宣布翻倍回购长期债券以稳定市场。此外，日本官员暗示未来或启用FIMA回购工具，每日最高可调600亿美元流动性，无需抛债即可干预。"
  },
  {
    "id": "hn:49511824",
    "domain": "股票",
    "title": "Apple Is Suddenly an AI Infra Stock as OpenAI Buys 10k+ Macs",
    "url": "https://247wallst.com/investing/2026/08/31/apple-is-suddenly-an-ai-infrastructure-stock-as-openai-buys-macs-by-the-tens-of-thousands/",
    "source": "prabal97",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-31T16:44:15+00:00",
    "summary": ""
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
    "id": "hn:49323620",
    "domain": "股票",
    "title": "Anthropic IPO valuation hinges on $190-200B 2028 revenue forecast",
    "url": "https://www.reuters.com/business/anthropic-ipo-valuation-hinges-190-200-billion-2028-revenue-forecast-sources-say-2026-08-15/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-16T21:00:25+00:00",
    "summary": ""
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
    "id": "hn:49401229",
    "domain": "股票",
    "title": "Anthropic IPO filing will show AI backlash as a risk factor, sources say",
    "url": "https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-22T16:23:09+00:00",
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
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 108,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-09-07T05:33:25+00:00",
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
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-09-04T13:15:24+00:00",
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
    "id": "rss:https://arxiv.org/abs/2609.04496",
    "domain": "金融",
    "title": "Portfolio Diversification and Concentration under Dependence Uncertainty: A Majorization Approach",
    "url": "https://arxiv.org/abs/2609.04496",
    "source": "Peng Liu, Yang Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2609.04496v1 Announce Type: new Abstract: Modern portfolio theory identifies diversification as the primary tool for risk reduction. However, under model uncertainty, this cornerstone may no lon"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.04569",
    "domain": "金融",
    "title": "Quantum Circuit Learning for Volatility Modeling: Multifractal Analysis of Realized Volatility Time Series",
    "url": "https://arxiv.org/abs/2609.04569",
    "source": "Tetsuya Takaishi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2609.04569v1 Announce Type: new Abstract: Herein, we propose a quantum circuit learning framework for modeling the realized volatility (RV) of Bitcoin and investigate the statistical properties "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.05047",
    "domain": "金融",
    "title": "Gatheral's Conjecture Revisited",
    "url": "https://arxiv.org/abs/2609.05047",
    "source": "Vladimir Lucic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2609.05047v1 Announce Type: new Abstract: We compare the Heston model with $\\rho=-1$ to the one-dimensional local-volatility model calibrated to the same European option prices. We show that, fo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.05115",
    "domain": "金融",
    "title": "Creators Have Difficulty Abandoning Ideas They Generated",
    "url": "https://arxiv.org/abs/2609.05115",
    "source": "Jin Kim, George E. Newman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2609.05115v1 Announce Type: new Abstract: Creativity researchers often distinguish between two stages of the creative process: generation versus selection. While much is known about the psycholo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.05162",
    "domain": "金融",
    "title": "Quantity, Risk, and Return",
    "url": "https://arxiv.org/abs/2609.05162",
    "source": "Yu An, Yinan Su, Chen Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2609.05162v1 Announce Type: new Abstract: We propose a new model of expected stock returns that incorporates quantity information from market trading activities into the factor pricing framework"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.04420",
    "domain": "金融",
    "title": "Optimal Stratified Allocation for Rare-Event Onset Forecasting in Dependent Sequences",
    "url": "https://arxiv.org/abs/2609.04420",
    "source": "Jaskaran Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2609.04420v1 Announce Type: cross Abstract: Let a finite population of n labelled examples carry a class-weighted loss, with pi*n in a rare positive class weighted by N0/N1. We study estimation "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.04712",
    "domain": "金融",
    "title": "Convex Modeling of Price Cross-Impact over Time",
    "url": "https://arxiv.org/abs/2609.04712",
    "source": "Vincent Yinjun-Wang, Madeleine Udell",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2609.04712v1 Announce Type: cross Abstract: Transaction costs can make or break a trading strategy, particularly in relative-value trading of commodity and macro markets, where edges are a few b"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.04917",
    "domain": "金融",
    "title": "Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the Limits of Automated Investing",
    "url": "https://arxiv.org/abs/2609.04917",
    "source": "Linsen Zhu, Mengqing Cai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2609.04917v1 Announce Type: cross Abstract: Artificial intelligence (AI) now supports investment workflows from data and prediction through research, portfolios, execution, and tool use. Technic"
  },
  {
    "id": "rss:https://arxiv.org/abs/1302.4676",
    "domain": "金融",
    "title": "Analysis of multilevel Monte Carlo path simulation using the Milstein discretisation",
    "url": "https://arxiv.org/abs/1302.4676",
    "source": "Michael B. Giles, Kristian Debrabant, Andreas R\\\"o{\\ss}ler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:1302.4676v4 Announce Type: replace Abstract: The multilevel Monte Carlo path simulation method introduced by Giles ({\\it Operations Research}, 56(3):607-617, 2008) exploits strong convergence pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2310.00553",
    "domain": "金融",
    "title": "Robust Asset-Liability Management",
    "url": "https://arxiv.org/abs/2310.00553",
    "source": "Tjeerd de Vries, Alexis Akira Toda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2310.00553v4 Announce Type: replace Abstract: Financial institutions often cannot replicate long-dated liabilities with available bonds, especially when leverage and collateral constraints bind."
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.01211",
    "domain": "金融",
    "title": "Fast and explicit European option pricing under tempered stable processes",
    "url": "https://arxiv.org/abs/2510.01211",
    "source": "Gaetano Agazzotti, Jean-Philippe Aguilar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2510.01211v2 Announce Type: replace Abstract: We provide series expansions for the tempered stable densities and for the price of European-style contracts in the exponential L\\'evy model driven "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00245",
    "domain": "金融",
    "title": "Agent-to-Agent Finance: Blockchain Payments and Trust Infrastructure for Autonomous AI Agents",
    "url": "https://arxiv.org/abs/2607.00245",
    "source": "Hui Gong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2607.00245v2 Announce Type: replace Abstract: Autonomous artificial intelligence (AI) agents are beginning to occupy a position between analytical tools and transacting counterparties. They can "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09951",
    "domain": "金融",
    "title": "Macroeconomic Risks from Maritime Trade Disruptions",
    "url": "https://arxiv.org/abs/2607.09951",
    "source": "Vipin P. Veetil, Fathimath S. Vemmarath",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2607.09951v2 Announce Type: replace Abstract: This paper develops a model of maritime chokepoint closures in which interrupting a shipping passage produces losses that are not measured, or even "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20842",
    "domain": "金融",
    "title": "Rethinking Synthetic Scenario Realism: Compatibility, Not Fidelity, Drives Hedging Performance",
    "url": "https://arxiv.org/abs/2608.20842",
    "source": "Ryuji Hashimoto, Masanori Hirano, Ryota Ozaki, Kentaro Imajo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T04:00:00+00:00",
    "summary": "arXiv:2608.20842v2 Announce Type: replace Abstract: Deep hedging is a data-driven approach to learn hedging strategies. It relies on synthetic price paths generator, as real market data is often limit"
  },
  {
    "id": "hn:49548497",
    "domain": "金融",
    "title": "Mark Cuban: Why US hospitals \"don't know their costs\"",
    "url": "https://www.beckershospitalreview.com/finance/mark-cuban-why-us-hospitals-dont-know-their-costs/",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-09-03T11:07:10+00:00",
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
    "id": "hn:49559666",
    "domain": "金融",
    "title": "Tesla Begins Offering Rides in a Car Without a Steering Wheel",
    "url": "https://www.nytimes.com/2026/09/03/business/tesla-cybercab-robotaxi-rides.html",
    "source": "telotortium",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-04T02:08:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
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
    "id": "hn:49514224",
    "domain": "金融",
    "title": "Monero Inflation Checker – FCMP++",
    "url": "https://www.reddit.com/r/Monero/comments/1w3hcos/monero_inflation_checker_fcmp/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-31T20:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-25T11:27:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49515596",
    "domain": "金融",
    "title": "Congress to vote on denying federal funding to universities that boycott Israel",
    "url": "https://twitter.com/dylanotes/status/2094229210889965634",
    "source": "slowin",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-31T22:24:39+00:00",
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
    "id": "hn:49531107",
    "domain": "金融",
    "title": "A Hedge-Fund Titan's Divorce Is Putting Wall Street's Staggering Wealth on Publi",
    "url": "https://www.wsj.com/personal-finance/a-hedge-fund-titans-divorce-is-putting-wall-streets-staggering-wealth-on-public-view-6c419f4c",
    "source": "kamaraju",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-02T02:41:04+00:00",
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
    "id": "hn:49396088",
    "domain": "金融",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
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
    "id": "hn:49404624",
    "domain": "金融",
    "title": "Jane Street took $15B hit in July tied to Situational Awareness",
    "url": "https://www.reuters.com/business/finance/jane-street-took-15-billion-hit-july-tied-situational-awareness-sources-say-2026-08-14/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-22T22:50:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49350858",
    "domain": "金融",
    "title": "AI Is Upending One of Finance's Cushiest Jobs",
    "url": "https://www.bloomberg.com/news/features/2026-06-05/ai-is-upending-traditional-financial-advisor-jobs",
    "source": "theriddlr",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-18T18:59:38+00:00",
    "summary": ""
  }
]
```
