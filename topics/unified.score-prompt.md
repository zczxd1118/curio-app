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

- 今日日期：`2026-08-31`
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
  "date": "2026-08-31",
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
    "points": 1779677,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1292793,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1215974,
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
    "points": 1130983,
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
    "points": 1067990,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 944411,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 864247,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 672537,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 651219,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 649924,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1u5XZBCEoT",
    "domain": "AI",
    "title": "Vibe Coding键盘做出来了！你要吗？",
    "url": "http://www.bilibili.com/video/av116334406932650",
    "source": "GeekLogic",
    "platform": "bilibili",
    "points": 588650,
    "published_at": "2026-04-03T11:00:00+00:00",
    "summary": "你是否发现，从去年起，写代码的方式变了。\n我们不再逐行敲击，而是顺应想法，用自然语言去‘引导’AI。\n代码的实现，变得更像是一种心流的表达。\n最近，我看到一张很有意思的网图——一把所谓的&#x27;Vibe Coding 专用键盘’。\n它像是一个玩笑，又像是一种对未来的隐喻。\n这种‘感觉’如果能被实体化，会是什么样？\n所以，我决定动手，把这个概念变成现实。\n\n本项目所有的代码和建模都已开源：\nht"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 586312,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 404140,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 365902,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 353138,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 335176,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 318933,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 201831,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180313,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 174359,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 164371,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1GDgY6CEbU",
    "domain": "AI",
    "title": "我把百万播放的C盘教程，做成了AI一键清理",
    "url": "http://www.bilibili.com/video/av116973534969868",
    "source": "大老湿gg",
    "platform": "bilibili",
    "points": 158299,
    "published_at": "2026-07-25T10:00:00+00:00",
    "summary": "之前做过一期C盘清理教程，播放量超过100万，但手动操作确实比较麻烦。  \n这次我把整套方法交给了Marvis：先扫描C盘、分析空间占用、判断清理风险，等我确认后再执行。最终C盘可用空间从12.9GB变成117GB，释放了约103GB。  \n清理完成后，我还把这套流程做成了定时任务和一键清理脚本，手机上也能远程调用。技能文档会放在评论区，清理个人文件前记得先确认清单。"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 155174,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 152071,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1vZArzvEHk",
    "domain": "AI",
    "title": "到底什么是vibe coding？",
    "url": "http://www.bilibili.com/video/av116137962504600",
    "source": "阿囤囤-庞滚滚",
    "platform": "bilibili",
    "points": 98098,
    "published_at": "2026-02-26T16:58:34+00:00",
    "summary": "发了不少Vibe Coding的视频，\n现在让我们回到原点：解释什么是Vibe Coding。\n\t\n为了方便大家理解，我大概是这么拆解的：\n\t\n#00:22[时刻]#谁提出的Vibe Coding\n#00:51[时刻]# Vibe Coding 改变了互联网工作流\n#02:36[时刻]# 举例说明如何Vibe Coding\n#04:59[时刻]# Vibe Coding的几个特点\n#05:44[时"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93460,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1oTkuBoEW5",
    "domain": "AI",
    "title": "业余程序员才Vibe Coding",
    "url": "http://www.bilibili.com/video/av115921586751411",
    "source": "晓舟报告",
    "platform": "bilibili",
    "points": 74989,
    "published_at": "2026-01-21T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 56160,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54650,
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
    "points": 47667,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1ASRjBxEVx",
    "domain": "AI",
    "title": "6 小时 Vibe Coding 全记录，做个 Web 版 Typora",
    "url": "http://www.bilibili.com/video/av116503185722308",
    "source": "Koala聊开源",
    "platform": "bilibili",
    "points": 46243,
    "published_at": "2026-05-02T04:56:51+00:00",
    "summary": "在这期视频中，我们带着大家一起体验了 6 小时 Vibe Coding 马拉松，在这个过程中，我们通过 TDD + Harness 方法，逐步完成了一个 Web 版 Typora 的移植。视频从项目目标的明确到技术选型，展示了如何在实践中解决一系列复杂问题，如何用测试驱动约束 Agent 行为，并逐步优化架构。通过多个核心测试的突破，我们最终实现了多个 Typora 语法行为的复刻。"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41227,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "harness使用教程-",
    "platform": "bilibili",
    "points": 37731,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34217,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30418,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28900,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 23050,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1JhVS6GEqm",
    "domain": "AI",
    "title": "第一个VibeCoding尝试，体验很好，做了一个宠物软件",
    "url": "http://www.bilibili.com/video/av116668927836761",
    "source": "GiorgioHan",
    "platform": "bilibili",
    "points": 20632,
    "published_at": "2026-05-31T11:25:58+00:00",
    "summary": "第一个VibeCoding尝试，体验很好，做了一个宠物软件-PaiMlomo，你可以用它制作自己宠物的卡通形象并让它住进手机里，还可以用它记录宠物饮食、疫苗、花销等等，还有遛狗路线记录和养宠社区..还在持续更新，欢迎大家提出建议和需求~"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 20631,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 19221,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17770,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1oXjc6CEWK",
    "domain": "AI",
    "title": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116769742195971",
    "source": "京东架构师诸葛",
    "platform": "bilibili",
    "points": 17519,
    "published_at": "2026-06-18T06:52:48+00:00",
    "summary": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
  },
  {
    "id": "bvid:BV1RHRxBvE6v",
    "domain": "AI",
    "title": "我说 AI 编程就是 Vibe Coding，被面试官鄙视了。。。",
    "url": "http://www.bilibili.com/video/av116527579793335",
    "source": "编程导航",
    "platform": "bilibili",
    "points": 14689,
    "published_at": "2026-05-06T12:25:45+00:00",
    "summary": "别再说 AI 编程就是 Vibe Coding 了！6 种主流模式一次讲清\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n记得三连支持、关注鱼皮，让更多朋友学到知识哦~"
  },
  {
    "id": "bvid:BV1ZBT2ztEwp",
    "domain": "AI",
    "title": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程",
    "url": "http://www.bilibili.com/video/av114642592469769",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 13720,
    "published_at": "2025-06-07T14:53:38+00:00",
    "summary": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程"
  },
  {
    "id": "bvid:BV16wtA6yE6J",
    "domain": "AI",
    "title": "WorkBuddy 60分钟超完整保姆级教程！无论是想入门Agent还是想工作提效，听完秒变大神！完整工作流+实战技巧全揭秘，零基础从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117172714344838",
    "source": "workbuddy使用教程",
    "platform": "bilibili",
    "points": 11871,
    "published_at": "2026-08-28T10:49:12+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 11856,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10912,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9445,
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
    "points": 8977,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 8287,
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
    "points": 1974,
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
    "id": "hn:49497235",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's AI advantage is moving beyond the GPU",
    "url": "https://techcrunch.com/2026/08/29/nvidias-ai-advantage-is-moving-beyond-the-gpu/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-30T09:57:06+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/advanced-cooling-technologies-address-the-automotive-heat-challenge/",
    "domain": "AI 算力 / 半导体",
    "title": "Advanced Cooling Technologies Address the Automotive Heat Challenge",
    "url": "https://www.eetimes.com/advanced-cooling-technologies-address-the-automotive-heat-challenge/",
    "source": "Danny J. Lohan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T07:46:55+00:00",
    "summary": "New cooling technologies are emerging as electric drivetrains, AI processors, and autonomous systems push automotive heat fluxes higher. The post Advanced Cooling Technologies Address the Automotive H"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/man-uses-robot-vacuum-to-covertly-record-his-wifes-affair-wins-divorce-settlement-but-gets-sentenced-to-prison-for-making-an-illegal-recording-husband-lands-behind-bars-after-counter-suit-over-privacy-rights",
    "domain": "AI 算力 / 半导体",
    "title": "Man uses robot vacuum to covertly record his wife's affair, wins divorce settlement but gets sentenced to prison for making an illegal recording — Husband lands behind bars after counter-suit over pri",
    "url": "https://www.tomshardware.com/tech-industry/man-uses-robot-vacuum-to-covertly-record-his-wifes-affair-wins-divorce-settlement-but-gets-sentenced-to-prison-for-making-an-illegal-recording-husband-lands-behind-bars-after-counter-suit-over-privacy-rights",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T09:30:00+00:00",
    "summary": "A Taiwanese man sued his wife for having an affair using recordings from a robot vacuum to prove his case. He won, but got sued by the wife for infringing on her personal privacy and was fined the equ"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/speedy-34-inch-240-hz-ultrawide-oled-monitor-now-usd600-off-lg-ultragear-34gx900a-b-only-usd599-99",
    "domain": "AI 算力 / 半导体",
    "title": "Speedy 34-inch 240 Hz ultrawide OLED monitor now $600 off — LG UltraGear 34GX900A-B only $599.99",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/speedy-34-inch-240-hz-ultrawide-oled-monitor-now-usd600-off-lg-ultragear-34gx900a-b-only-usd599-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T18:08:43+00:00",
    "summary": "The LG UltraGear 34GX900A-B packs a fast 240 Hz OLED panel and 3440 x 1440 resolution into an immersive 800R curved display, now available for 50% off."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/dlss-5-mod-brings-next-gen-tech-to-old-ampere-gpus-but-frame-rates-are-horrible-most-games-tank-to-single-digits-high-end-gpus-can-hit-up-to-40-fps-in-some-cases",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 5 mod brings next-gen tech to old Ampere GPUs, but frame rates are horrible — most games tank to single digits, high-end GPUs can hit up to 40 FPS in some cases",
    "url": "https://www.tomshardware.com/pc-components/gpus/dlss-5-mod-brings-next-gen-tech-to-old-ampere-gpus-but-frame-rates-are-horrible-most-games-tank-to-single-digits-high-end-gpus-can-hit-up-to-40-fps-in-some-cases",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T16:30:30+00:00",
    "summary": "DLSS 5 now runs on Ampere GPUs thanks to a patched DLL, but performance is expectedly poor for the most part. You can get up to 30-40 FPS in edge cases with minimum in-game settings, but newer titles "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/spacex-starts-in-house-turbine-blade-manufacturing-to-boost-gas-powered-generator-output-for-elons-ai-data-centers-new-manufacturing-strategy-cuts-generator-delays-by-18-months",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX starts in-house turbine blade manufacturing to boost gas-powered generator output for Elon's AI data centers — new manufacturing strategy cuts generator delays by 18 months",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/spacex-starts-in-house-turbine-blade-manufacturing-to-boost-gas-powered-generator-output-for-elons-ai-data-centers-new-manufacturing-strategy-cuts-generator-delays-by-18-months",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T14:49:50+00:00",
    "summary": "Turbine blades and vanes are among the most complicated turbine engine parts to build, with processes taking as long as 60 to 90 weeks. Because of this, Musk wants to bring their manufacturing in-hous"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/donkey-kong-64-finally-gets-a-fully-native-pc-port-written-in-c-dk64-rekongpiled-brings-ultrawide-support-uncapped-framerates-and-zero-ai-code",
    "domain": "AI 算力 / 半导体",
    "title": "Donkey Kong 64 finally gets a fully native PC port written in C — DK64 ReKONGpiled brings ultrawide support, uncapped framerates, and zero AI code",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/donkey-kong-64-finally-gets-a-fully-native-pc-port-written-in-c-dk64-rekongpiled-brings-ultrawide-support-uncapped-framerates-and-zero-ai-code",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T14:26:14+00:00",
    "summary": "A team of veteran developers has recompiled Donkey Kong 64 in C, so it runs natively on Windows, Linux, and Mac. The entire project is free, uses no generative AI, but still includes more features tha"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/massive-12tb-steam-leak-reveals-decades-of-unreleased-games-archived-files-include-unseen-half-life-2-episode-3-builds-and-assets",
    "domain": "AI 算力 / 半导体",
    "title": "Massive 12TB Steam leak reveals decades of unreleased games — archived files include unseen Half-Life 2: Episode 3 builds and assets",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/massive-12tb-steam-leak-reveals-decades-of-unreleased-games-archived-files-include-unseen-half-life-2-episode-3-builds-and-assets",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:48:42+00:00",
    "summary": "Early builds of Valve games from 2003 to 2013 have been found in a 12TB archive pulled from the company's old servers. These pre-release versions act like time capsules, preserving the state of the ga"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/at-least-three-exhibitors-got-robbed-at-gamescom-2026-laptops-and-handhelds-with-unfinished-game-builds-stolen-from-locked-cabinets",
    "domain": "AI 算力 / 半导体",
    "title": "At least three exhibitors got robbed at Gamescom 2026 — laptops and handhelds with unfinished game builds stolen from locked cabinets",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/at-least-three-exhibitors-got-robbed-at-gamescom-2026-laptops-and-handhelds-with-unfinished-game-builds-stolen-from-locked-cabinets",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:34:59+00:00",
    "summary": "Several developers, publishers, and studios have had their laptops and handheld consoles stolen at Gamescom 2026. However, the organizers said that it's only responsible for general security, and exhi"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/adata-urban-tapsafe-2tb-review",
    "domain": "AI 算力 / 半导体",
    "title": "Adata Urban Tapsafe 2TB review: Solid-state storage you unlock with your phone",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/adata-urban-tapsafe-2tb-review",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:05:00+00:00",
    "summary": "Adata's Urban Tapsafe portable SSD sports magnetic face plates, a metal mounting clip, the ability to unlock the drive with your phone, and share selective access with others via an app."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/diy-archivists-push-budget-nikons-to-902-000-clicks-to-save-1-800-rare-books-team-trains-neural-net-on-photoshop-edits-to-process-526-000-scans",
    "domain": "AI 算力 / 半导体",
    "title": "DIY archivists push budget Nikons to 902,000 clicks to save 1,800 rare books — team trains neural net on Photoshop edits to process 526,000 scans",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/diy-archivists-push-budget-nikons-to-902-000-clicks-to-save-1-800-rare-books-team-trains-neural-net-on-photoshop-edits-to-process-526-000-scans",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:00:00+00:00",
    "summary": "An epic book preservation effort."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-top-dram-maker-cxmt-sues-pentagon-over-its-blacklisting-argues-chips-are-standard-civilian-jedec-spec-not-defense-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "China's top DRAM maker CXMT sues Pentagon over its blacklisting — argues chips are standard civilian JEDEC spec, not defense hardware",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-top-dram-maker-cxmt-sues-pentagon-over-its-blacklisting-argues-chips-are-standard-civilian-jedec-spec-not-defense-hardware",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T11:30:00+00:00",
    "summary": "Chinese DRAM maker CXMT wants the US Department of Defense to remove it from the list of companies linked to the Chinese military."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/corsair-rm1000e-2026-thermalprotect-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair RM1000e (2026) ThermalProtect power supply review: Temperature-sensing 12V-2x6 cable shuts the GPU down before a connector can melt",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/corsair-rm1000e-2026-thermalprotect-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T11:05:00+00:00",
    "summary": "Corsair's mainstream RMe series returns for 2026 with Platinum-class efficiency, a 500W fanless window, and a temperature-sensing 12V-2x6 cable that shuts the GPU down before a connector can melt."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/poor-liquid-metal-application-almost-destroys-asus-zephyrus-m16-laptop-eats-through-the-processor-lid-paste-replacement-triples-framerates-drops-temps-and-eliminates-hard-crashes",
    "domain": "AI 算力 / 半导体",
    "title": "Poor liquid metal application almost destroys Asus Zephyrus M16 laptop, eats through the processor lid — paste replacement triples framerates, drops temps, and eliminates hard crashes",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/poor-liquid-metal-application-almost-destroys-asus-zephyrus-m16-laptop-eats-through-the-processor-lid-paste-replacement-triples-framerates-drops-temps-and-eliminates-hard-crashes",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T11:00:00+00:00",
    "summary": "A user on Reddit shared their story about how the factory-applied liquid metal on their Asus Zephyrus M16 gaming laptop corroded the heatsink and lid of their CPU. It got so bad that the corrosion was"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modders-solder-power-cables-directly-to-rtx-5090-pcb-to-eliminate-notorious-melting-16-pin-connector-bare-board-galax-hof-card-pulls-600w-under-chiller-cooling",
    "domain": "AI 算力 / 半导体",
    "title": "Modders solder power cables directly to RTX 5090 PCB to eliminate notorious melting 16-pin connector — bare-board Galax HOF card pulls 600W under chiller cooling",
    "url": "https://www.tomshardware.com/pc-components/gpus/modders-solder-power-cables-directly-to-rtx-5090-pcb-to-eliminate-notorious-melting-16-pin-connector-bare-board-galax-hof-card-pulls-600w-under-chiller-cooling",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T10:30:00+00:00",
    "summary": "TecLab, a Brazilian YouTuber, has just shown the most dangerous method of bypassing the 16-pin connector on an RTX 5090 — by soldering wires directly to the card's PCB. In an attempt to save the GPU f"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/us-military-uses-high-energy-lasers-to-shoot-down-three-mexican-cartel-drones-over-the-southern-border-narcos-suspected-of-using-uavs-for-surveillance-and-reconnaissance-to-support-illegal-activities",
    "domain": "AI 算力 / 半导体",
    "title": "US military uses high-energy lasers to shoot down three Mexican cartel drones over the southern border — narcos suspected of using UAVs for surveillance and reconnaissance to support illegal activitie",
    "url": "https://www.tomshardware.com/tech-industry/drones/us-military-uses-high-energy-lasers-to-shoot-down-three-mexican-cartel-drones-over-the-southern-border-narcos-suspected-of-using-uavs-for-surveillance-and-reconnaissance-to-support-illegal-activities",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T10:00:00+00:00",
    "summary": "The US military has successfully deployed a laser defense system on the southern border of the country and shot down alleged Mexican cartel drones. These UAVs are suspected of spotting U.S. law enforc"
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
    "id": "hn:49411178",
    "domain": "AI 算力 / 半导体",
    "title": "Etched Sohu vs. Nvidia: Transformer ASIC vs. GPU (2026)",
    "url": "https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-08-23T18:27:33+00:00",
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
    "id": "hn:49436796",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI claims its new chips can outperform Nvidia processors in tests",
    "url": "https://www.bloomberg.com/news/articles/2026-08-25/openai-claims-its-new-chips-can-outperform-nvidia-processors-in-tests",
    "source": "TravisJamison",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-25T16:35:58+00:00",
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
    "points": 362,
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
    "id": "rss:https://www.theverge.com/entertainment/986564/professor-murder-rides-the-subway-dance-punk-perfection-review",
    "domain": "大厂 AI 动态",
    "title": "Professor Murder Rides the Subway is a forgotten slice of dance punk perfection",
    "url": "https://www.theverge.com/entertainment/986564/professor-murder-rides-the-subway-dance-punk-perfection-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T21:18:59+00:00",
    "summary": "I recently dug out my CDs and started reripping them all. I've found a few forgotten gems in there, but few hit harder for me than the beautifully concise Professor Murder Rides the Subway EP. There w"
  },
  {
    "id": "rss:https://www.theverge.com/games/986552/12tb-steam-leak-half-life-2-episode-3",
    "domain": "大厂 AI 动态",
    "title": "Enormous 12TB Steam leak includes abandoned Half-Life 2: Episode 3 assets",
    "url": "https://www.theverge.com/games/986552/12tb-steam-leak-half-life-2-episode-3",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T19:14:08+00:00",
    "summary": "Over 12 terabytes of data, containing builds of every game uploaded to Steam between 2003 and 2013, has been leaked. We don't know everything in the archives yet because of its massive size. But peopl"
  },
  {
    "id": "rss:https://www.theverge.com/science/986544/nancy-grace-roman-space-telescope-launch",
    "domain": "大厂 AI 动态",
    "title": "The Nancy Grace Roman Space Telescope launches to study dark matter and dark energy",
    "url": "https://www.theverge.com/science/986544/nancy-grace-roman-space-telescope-launch",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T16:36:39+00:00",
    "summary": "After funding struggles and a name change, the Nancy Grace Roman Space Telescope has been successfully launched. It will now make a three-month, one-million-mile journey to its orbit at the second Sun"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/986541/texas-governor-abbott-flock-cameras",
    "domain": "大厂 AI 动态",
    "title": "Texas Governor Abbott blocks funding for more Flock cameras",
    "url": "https://www.theverge.com/ai-artificial-intelligence/986541/texas-governor-abbott-flock-cameras",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T15:35:10+00:00",
    "summary": "As backlash grows over Flock's AI surveillance cameras, Texas Governor Greg Abbott has frozen state spending on them. The move came just ahead of the publication of a Texas Tribune investigation that "
  },
  {
    "id": "rss:https://www.theverge.com/games/986302/chess-poker-expansion-gambit",
    "domain": "大厂 AI 动态",
    "title": "Chess.com launched a poker site, and it’s planning even more classic games",
    "url": "https://www.theverge.com/games/986302/chess-poker-expansion-gambit",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T13:00:00+00:00",
    "summary": "Chess.com has done one thing, and one thing very well, for almost 20 years, but now it's going beyond its domain name. The biggest name in online chess quietly launched its first companion site in bet"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986167/china-humanoid-robot-games-race",
    "domain": "大厂 AI 动态",
    "title": "China’s robots race ahead",
    "url": "https://www.theverge.com/tech/986167/china-humanoid-robot-games-race",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on falling robots and the US-China AI race, follow Robert Hart. The Stepback arrives in our su"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986280/mac-mini-studio-star-wars-zero-company-wyze-camera",
    "domain": "大厂 AI 动态",
    "title": "Two new small, powerful Macs",
    "url": "https://www.theverge.com/tech/986280/mac-mini-studio-star-wars-zero-company-wyze-camera",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 142, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, how is it almost September already, and also you can read all the old"
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
    "title": "Sony Music Publishing and Warner Chappell are suing Anthropic",
    "url": "https://www.theverge.com/ai-artificial-intelligence/986438/sony-music-warner-chappell-anthropic-lawsuit-copyright",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T18:19:53+00:00",
    "summary": "Sony Music Publishing and Warner Chappell have filed suit against Anthropic in the US District Court for the Northern District of California seeking damages for \"tens of thousands\" copyrighted works. "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/30/the-u-s-is-building-barriers-around-drones-and-robots-china-still-has-scale/",
    "domain": "大厂 AI 动态",
    "title": "The U.S. is building barriers around drones and robots, but China has scale to get around them",
    "url": "https://techcrunch.com/2026/08/30/the-u-s-is-building-barriers-around-drones-and-robots-china-still-has-scale/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T02:34:00+00:00",
    "summary": "The U.S. is shutting out more foreign-made drones and robots. China’s scale means the global competition may simply move elsewhere."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/30/grindr-wants-to-be-the-everything-app-for-gay-men-investors-are-still-deciding-whether-it-can-pull-it-off/",
    "domain": "大厂 AI 动态",
    "title": "Grindr wants to be the everything app for gay men; investors are still deciding whether it can pull it off",
    "url": "https://techcrunch.com/2026/08/30/grindr-wants-to-be-the-everything-app-for-gay-men-investors-are-still-deciding-whether-it-can-pull-it-off/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T02:18:57+00:00",
    "summary": "George Arison is done letting Wall Street's \"Grindr discount\" go unchallenged — in a wide-ranging Q&#038;A, the CEO walks us through how AI, a controversial $350-plus EDGE tier, and a bet on healthcar"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/30/liuxs-big-microcar-bets-on-sustainability-to-take-on-chinese-rivals/",
    "domain": "大厂 AI 动态",
    "title": "Liux’s Big microcar bets on sustainability to take on Chinese rivals",
    "url": "https://techcrunch.com/2026/08/30/liuxs-big-microcar-bets-on-sustainability-to-take-on-chinese-rivals/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T18:33:44+00:00",
    "summary": "The Liux Big microcar is made in Spain. The startup thinks it can compete in a crowded market with its tiny electric car built around sustainability."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/30/musks-faster-path-to-more-gas-turbines-comes-with-pollution-problem/",
    "domain": "大厂 AI 动态",
    "title": "Musk’s faster path to more gas turbines comes with pollution problem",
    "url": "https://techcrunch.com/2026/08/30/musks-faster-path-to-more-gas-turbines-comes-with-pollution-problem/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T16:54:25+00:00",
    "summary": "Elon Musk says a secretive new SpaceX foundry will let him cast his own turbine blades and get gas power online 18 months faster than anyone else — but it's a bet on a fuel source that's already trigg"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/30/techcrunch-mobility-the-hidden-human-cost-of-robotaxis/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: The hidden human cost of robotaxis",
    "url": "https://techcrunch.com/2026/08/30/techcrunch-mobility-the-hidden-human-cost-of-robotaxis/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T16:03:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/30/caterpillar-is-bringing-to-ai-deployment-what-it-learned-from-automating-mining/",
    "domain": "大厂 AI 动态",
    "title": "Caterpillar is bringing to AI deployment what it learned from automating mining",
    "url": "https://techcrunch.com/2026/08/30/caterpillar-is-bringing-to-ai-deployment-what-it-learned-from-automating-mining/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T15:00:00+00:00",
    "summary": "Caterpillar has spent decades putting autonomous machines to work at remote mining sites. It's now bringing that experience to AI deployment."
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
    "summary": "The Theragun Sense, which retails for $299, is a wellness-focused massage gun that’s designed for everyday aches, muscle tension, relaxation, and soreness."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/08/a-12tb-steam-teraleak-spills-more-than-a-decade-of-lost-pc-gaming-history/",
    "domain": "大厂 AI 动态",
    "title": "A 12TB Steam “teraleak” spills more than a decade of lost PC gaming history",
    "url": "https://arstechnica.com/gaming/2026/08/a-12tb-steam-teraleak-spills-more-than-a-decade-of-lost-pc-gaming-history/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T21:40:56+00:00",
    "summary": "Cut content from Portal 2, hints of Half Life 2: Episode 3, and so much more."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/why-it-matters-that-president-trump-just-dialed-into-a-nasa-news-conference/",
    "domain": "大厂 AI 动态",
    "title": "Why it matters that President Trump just dialed into a NASA news conference",
    "url": "https://arstechnica.com/space/2026/08/why-it-matters-that-president-trump-just-dialed-into-a-nasa-news-conference/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T17:40:30+00:00",
    "summary": "With just one more major mission upcoming, NASA's science programs need a boost."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/inside-metas-push-to-put-robots-to-work-in-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Inside Meta’s push to put robots to work in data centers",
    "url": "https://arstechnica.com/ai/2026/08/inside-metas-push-to-put-robots-to-work-in-data-centers/",
    "source": "Paresh Dave, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T11:03:47+00:00",
    "summary": "The company is testing robots on tasks that can performed by technicians."
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
    "id": "rss:https://www.producthunt.com/products/teenage-engineering",
    "domain": "大厂 AI 动态",
    "title": "EP–2350 FX–MIC",
    "url": "https://www.producthunt.com/products/teenage-engineering",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:41:46+00:00",
    "summary": "The programmable mic you can squeeze, shake & play Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/orato-speech-coach",
    "domain": "大厂 AI 动态",
    "title": "Orato",
    "url": "https://www.producthunt.com/products/orato-speech-coach",
    "source": "Petros Tepoyan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T17:02:44+00:00",
    "summary": "Practice speaking with AI. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/tether-a-ball-for-boring-meetings",
    "domain": "大厂 AI 动态",
    "title": "Tether",
    "url": "https://www.producthunt.com/products/tether-a-ball-for-boring-meetings",
    "source": "Alex",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T06:37:13+00:00",
    "summary": "A ball for boring meetings to keep you busy Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/omlx",
    "domain": "大厂 AI 动态",
    "title": "oMLX",
    "url": "https://www.producthunt.com/products/omlx",
    "source": "Rabnoor Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T20:17:05+00:00",
    "summary": "Mac LLM server that cuts agent wait times from 90s to 5s Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/superagent-a-home-for-your-ai-agents",
    "domain": "大厂 AI 动态",
    "title": "Superagent",
    "url": "https://www.producthunt.com/products/superagent-a-home-for-your-ai-agents",
    "source": "Worathiti Pung",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T22:27:58+00:00",
    "summary": "Claude Code for the rest of us Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/114027",
    "domain": "大厂 AI 动态",
    "title": "屏幕之外，桌面之上：走过十年，明基探索了一束光的更多可能",
    "url": "https://sspai.com/post/114027",
    "source": "Microhoo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T06:57:03+00:00",
    "summary": "查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/113827",
    "domain": "大厂 AI 动态",
    "title": "全球仅剩三位数的物种，科学家却连一个准数都数不出来",
    "url": "https://sspai.com/post/113827",
    "source": "红树林基金会MCF",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T02:53:32+00:00",
    "summary": "门前大桥下游过勺嘴鹬，快来快来数一数……这究竟怎么数呀？ 查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/114022",
    "domain": "大厂 AI 动态",
    "title": "派早报：GTA 6 引发请假玩游戏热潮",
    "url": "https://sspai.com/post/114022",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T22:59:06+00:00",
    "summary": "GTA 6 引发请假玩游戏热潮Sam Altman 为 OpenAI 高管定制豪华表海信发布 A10 系列墨水屏手机Pixel 11 削减内存安全特性，GrapheneOS 考虑放弃支持「承重」等 Claude 滥用词在 GitHub 蔓延工信部曝光车企监督检查典型案例看看就行的简讯少数派的近期动态你可能错过的好文章查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/113974",
    "domain": "大厂 AI 动态",
    "title": "城市漫步指南 | 佛罗伦萨：来自六月的梦幻艺术夏令营",
    "url": "https://sspai.com/post/113974",
    "source": "程天冲",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T07:00:00+00:00",
    "summary": "我种草佛罗伦萨的理由绝对是世所罕见：因为SEVENTEEN的NanaTour有很大一部分是在佛罗伦萨及其周边拍摄的。从去年夏天看了这个综艺开始，我就一直对这个地方念念不忘，心想夏日的意大利到底是有何种 ...查看全文"
  },
  {
    "id": "hn:49443871",
    "domain": "大厂 AI 动态",
    "title": "Analyzing student votes across AI models for college essay help",
    "url": "https://studyarena.com/blog/chatgpt-vs-claude-vs-gemini-college-essays-2026",
    "source": "pasharayan",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-26T03:23:50+00:00",
    "summary": ""
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
    "id": "wscn:3780702",
    "domain": "股票",
    "title": "沃什鹰派发言提振加息预期，美股期指下跌，美债收益率走低，中东局势升温油价急涨",
    "url": "https://wallstreetcn.com/articles/3780702",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T09:18:57+00:00",
    "summary": "MSCI亚太区股票指数下跌0.7%，韩国KOSPI指数现跌0.1%，此前一度跌至3.6%，本地券商称养老基金买入。布伦特原油上涨2.5%，报每桶90.25美元。黄金跌至约每盎司4437美元。"
  },
  {
    "id": "wscn:3780724",
    "domain": "股票",
    "title": "华为上半年营收同比增长10%至4678亿，净利润234.27亿｜财报见闻",
    "url": "https://wallstreetcn.com/articles/3780724",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T09:17:38+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3780681",
    "domain": "股票",
    "title": "沪指低开高走收涨0.9%，液冷服务器、传媒双线爆发，港股AI大模型股午后大涨、MINIMAX飙升17%",
    "url": "https://wallstreetcn.com/articles/3780681",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T09:04:21+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市约3200股飘红，今日成交2.15万亿。板块方面，AI应用端炒作午后持续升温，浪潮信息、紫光股份、寒武纪拉动服务器板块。煤炭、银行板块稳步攀升，中国银行、中信银行同创新高，邮储银行放量猛攻。地产龙头明显承压，招商蛇口、滨江集团领跌。"
  },
  {
    "id": "wscn:3780723",
    "domain": "股票",
    "title": "星宇股份港股IPO之路：拿就业扶持，解约应届生",
    "url": "https://wallstreetcn.com/articles/3780723",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T09:03:24+00:00",
    "summary": "星星之火，可以燎原"
  },
  {
    "id": "wscn:3780722",
    "domain": "股票",
    "title": "七部门发文推动商品消费：破除汽车限购限制，用好个人消费贷款贴息",
    "url": "https://wallstreetcn.com/articles/3780722",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T09:01:39+00:00",
    "summary": "政策从破除汽车流通限制、完善废旧家电回收、布局充电设施等全链条发力，支撑大宗商品更新换代；同时提升生活日用品消费，满足多元化需求。针对“一老一小”推动银发、婴童产品提质扩容，并培育绿色、智能、健康等十万亿级市场。此外，完善消费品标准体系，加快智能家居互联互通等标准应用，加强内外贸产品标准认证衔接。"
  },
  {
    "id": "wscn:3780549",
    "domain": "股票",
    "title": "高盛的“AI实战”：顶级投行如何探索Agent的产品化",
    "url": "https://wallstreetcn.com/articles/3780549",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T08:35:04+00:00",
    "summary": "金融业不能接受“差不多对”的AI。"
  },
  {
    "id": "wscn:3780715",
    "domain": "股票",
    "title": "软银旗下数据中心SB Energy为锁定OpenAI租户，授予估值55亿美元认股权证",
    "url": "https://wallstreetcn.com/articles/3780715",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T08:32:50+00:00",
    "summary": "SB Energy为换取OpenAI成为租户，授予其约55亿美元认股权证，令后者兼具租户与投资者双重身份，软银、英伟达也深度绑定其中。公司虽手握近9GW算力合同及超4000亿美元订单积压，但数据中心尚未投运。招股书坦言业务对OpenAI存在实质性依赖，这一复杂的利益网络将成为IPO估值的关键变量。"
  },
  {
    "id": "wscn:3780720",
    "domain": "股票",
    "title": "韩日芯片合作升温，SK海力士研究在日本合资建存储芯片厂",
    "url": "https://wallstreetcn.com/articles/3780720",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T08:32:37+00:00",
    "summary": "SK海力士正评估在日本建设半导体工厂，以完善全球产能布局，满足AI带动的存储芯片需求。日本因电力和水资源条件及产业链优势成为潜在选项，公司正考察各地，合作模式未定，可能涉及合资或收购。此举也将深化与索尼、任天堂等客户及东京电子等供应商的合作，分散供应链风险。"
  },
  {
    "id": "wscn:3780711",
    "domain": "股票",
    "title": "为降低HBM成本，SK海力士被曝评估英特尔代工方案",
    "url": "https://wallstreetcn.com/articles/3780711",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T08:31:22+00:00",
    "summary": "受制于高昂代工成本，SK海力士拟引入英特尔代工HBM4E基础芯片，或将打破台积电垄断。此举意在重夺议价权、发力定制化HBM，双方更有望在先进封装领域联手。全球AI芯片供应链洗牌在即。"
  },
  {
    "id": "wscn:3780719",
    "domain": "股票",
    "title": "财政整顿：贝森特能切动哪块蛋糕？",
    "url": "https://wallstreetcn.com/articles/3780719",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T08:05:15+00:00",
    "summary": "财通宏观认为，美国债务问题已形成“利息-赤字-债务”负反馈螺旋，短期财政内生扩张难以逆转。实际可压降的支出仅集中于占比13%的非国防自主性支出，节流对赤字率改善有限。历史表明两党减支多限于此类项目，国防与福利刚性难削。当前全面整顿财政纪律不具备条件，短期美联储扩表或是财政压力的唯一解。"
  },
  {
    "id": "wscn:3780704",
    "domain": "股票",
    "title": "敢为天下先！AI长剧首次上星湖南卫视：全AI影视内容工业化的关键一跃？",
    "url": "https://wallstreetcn.com/premium/articles/3780704?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T07:35:31+00:00",
    "summary": "2026年8月31日，国内首部全AI制作30集长剧《后西游记》登陆湖南卫视黄金档与芒果TV双平台，标志AI内容首次进入主流长内容播出体系，并成为广电\"21条\"后首部\"边制作、边审核、边播出\"的剧集。"
  },
  {
    "id": "wscn:3780714",
    "domain": "股票",
    "title": "博通财报在即，摩根大通坚定看好：市场严重低估AI业务增长，谷歌TPU“失宠”担忧过头",
    "url": "https://wallstreetcn.com/articles/3780714",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T07:26:45+00:00",
    "summary": "市场严重误判博通。小摩最新研报指出，博通手握谷歌五年大单，AI业务潜力被显著低估，预计FY27 AI收入将暴增超1300亿美元。分析师重申580美元目标价，直指57%上涨空间，即将发布的财报或成其价值重估的关键节点。"
  },
  {
    "id": "wscn:3780712",
    "domain": "股票",
    "title": "8月PMI：企稳的能见度",
    "url": "https://wallstreetcn.com/articles/3780712",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T07:24:42+00:00",
    "summary": "国联民生认为，8月制造业PMI回升主要受国内需求回暖带动，新订单指数重返扩张区间，但改善集中于大型企业。供需重回扩张，需求修复先于生产，与订单回补、“六张网”和设备更新需求释放有关。价格指数回升，成本压力抬头，企业利润承压。库存被动去化，补库意愿谨慎。非制造业景气偏弱，需求修复尚未广泛扩散。"
  },
  {
    "id": "wscn:3780713",
    "domain": "股票",
    "title": "工信部：开展人工智能应用服务商培育专项行动",
    "url": "https://wallstreetcn.com/articles/3780713",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T07:14:40+00:00",
    "summary": "探索通过首购首用、风险补偿等模式，加大大模型、智能体、Token等服务采购力度，提升行业用模用智质效。支持服务商加强与国家算力网络枢纽节点、国家算力互联互通节点、中国算力平台等对接。"
  },
  {
    "id": "wscn:3780707",
    "domain": "股票",
    "title": "沃什鹰派讲话推升9月加息概率，科技企业为美债市场融资主体---W35海外宏观脱水",
    "url": "https://wallstreetcn.com/premium/articles/3780707?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T06:36:16+00:00",
    "summary": "沃什在Jackson Hole年会发表鹰派演讲，称美联储对持续65个月的高通胀负有全责，除非确信潜在..."
  },
  {
    "id": "wscn:3780699",
    "domain": "股票",
    "title": "沃什讲话推高加息预期，债券投资者仍不信美联储会行动",
    "url": "https://wallstreetcn.com/articles/3780699",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T06:29:54+00:00",
    "summary": "沃什在杰克逊霍尔重申抗通胀立场后，互换市场将9月加息概率推升至约60%，两年期美债收益率周五创逾两个月最大单日涨幅。但多家机构投资者明确表示不为所动：ABN AMRO、Brandywine、DWS均维持低配长期美债立场，认为“言辞不等于行动”。"
  },
  {
    "id": "wscn:3780706",
    "domain": "股票",
    "title": "港股万亿解禁潮下，药师帮的资本选择",
    "url": "https://wallstreetcn.com/articles/3780706",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T06:17:20+00:00",
    "summary": "2026年的港股，正在迎来一轮股票供给高峰。\n今年以来，港股IPO数量和募资规模均维持高位，上市公司..."
  },
  {
    "id": "wscn:3780705",
    "domain": "股票",
    "title": "华创张瑜：地产新政六个方面可能的影响",
    "url": "https://wallstreetcn.com/articles/3780705",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T06:09:39+00:00",
    "summary": "张瑜认为，地产新政将产生六方面深远影响：地方土地出让收入或短期承压；居民付款延后，交付风险降低；房企去高周转，转向资本金约束的稳健经营；银行存贷时点延后，居民存款活化放缓；地产投资与财政支出节奏迎来变化；房价则受供给放缓与需求变化的双重影响。"
  },
  {
    "id": "wscn:3780703",
    "domain": "股票",
    "title": "营收降、净利增，青农商行少提的减值托住了利润？",
    "url": "https://wallstreetcn.com/articles/3780703",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T05:59:35+00:00",
    "summary": "8月31日，青农商行披露上半年共实现归母净利润21.95亿元、同比增长2.84%；扣非归母净利润22..."
  },
  {
    "id": "wscn:3780701",
    "domain": "股票",
    "title": "存款付息率骤降托底息差，渝农商行对公扩张、零售收缩格局延续",
    "url": "https://wallstreetcn.com/articles/3780701",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T05:35:37+00:00",
    "summary": "渝农商行2026年半年度报告，展现了一家区域性农商行在息差下行周期中的应对路径。\n8月31日，渝农商..."
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
    "id": "rss:https://arxiv.org/abs/2608.27538",
    "domain": "金融",
    "title": "Disaffection at Work: Employee Responses to Job-Related Information",
    "url": "https://arxiv.org/abs/2608.27538",
    "source": "Beatrice Braut, Mariele Macaluso, Vincenzo Mollisi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.27538v1 Announce Type: new Abstract: Quiet quitting reflects a form of worker disaffection that operates along the intensive margin of labor supply rather than through job exit. We study ho"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27575",
    "domain": "金融",
    "title": "Pricing and Calibration of Bitcoin Inverse Options via the Rough Bergomi Model",
    "url": "https://arxiv.org/abs/2608.27575",
    "source": "Riccardo Caruso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.27575v1 Announce Type: new Abstract: Bitcoin inverse options, traded on the Deribit exchange and settled in the underlying cryptocurrency rather than in fiat currency, combine extreme and g"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27598",
    "domain": "金融",
    "title": "Do Customer Disclosures Affect Suppliers' Internal Capital Allocation Decisions?",
    "url": "https://arxiv.org/abs/2608.27598",
    "source": "Sangwook Nam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.27598v1 Announce Type: new Abstract: This study examines whether customer disclosures affect how supplier firms allocate capital across business segments. Customer disclosures can shape sup"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27734",
    "domain": "金融",
    "title": "What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery",
    "url": "https://arxiv.org/abs/2608.27734",
    "source": "Eray Gen\\c{c}ay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.27734v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used to discover trading strategies, and much of the resulting literature shares a methodological weakness"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27980",
    "domain": "金融",
    "title": "The Race for Elite Destinations: Education Competition and Low Fertility in Korea",
    "url": "https://arxiv.org/abs/2608.27980",
    "source": "Dongwoo Kim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.27980v1 Announce Type: new Abstract: South Korea has the world's lowest fertility and an intense education race. Families devote nine percent of lifetime income to education, mostly to priv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.28397",
    "domain": "金融",
    "title": "Market-Informed Valuation of GMMB Riders with Surrender Options under a Heston Stochastic-Local Volatility Model",
    "url": "https://arxiv.org/abs/2608.28397",
    "source": "Ludovic Goudenege, Andrea Molent, Xiao Wei, Antonino Zanette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.28397v1 Announce Type: new Abstract: We develop a market-informed valuation framework for guaranteed minimum maturity benefit (GMMB) riders with rational surrender under the Heston stochast"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.28399",
    "domain": "金融",
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "url": "https://arxiv.org/abs/2608.28399",
    "source": "Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.28399v1 Announce Type: cross Abstract: In financial markets, a sequential policy that reacts systematically to price movements may become predictable to other market participants. This pape"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.25972",
    "domain": "金融",
    "title": "The Dynamic Trade-Off of Dual-Class Shares",
    "url": "https://arxiv.org/abs/2608.25972",
    "source": "Hyunseob Kim, Doron Levit, Roni Michaely",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.25972v2 Announce Type: replace Abstract: Dual-class shares allocate control to founders whose firm-specific investments drive firm value but separate control from ownership, raising agency "
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.05294",
    "domain": "金融",
    "title": "Digital Engagement, Income Disparities, and Job Seeking in the United States since 2010",
    "url": "https://arxiv.org/abs/2511.05294",
    "source": "Shaolong Wu, Yijiang River Dong, Siming He",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2511.05294v3 Announce Type: replace-cross Abstract: Surveys often record how frequently people use the internet without measuring the infrastructures, skills, and support systems that make digit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22697",
    "domain": "金融",
    "title": "Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf",
    "url": "https://arxiv.org/abs/2608.22697",
    "source": "Davood Wadi, Yu Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T04:00:00+00:00",
    "summary": "arXiv:2608.22697v2 Announce Type: replace-cross Abstract: Search rankings are valuable because human attention is scarce and sequential. Higher-placed alternatives are easier to find, so they are exam"
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
    "id": "hn:49414279",
    "domain": "金融",
    "title": "Tesla discontinues its Solar Roof tiles, not economically viable",
    "url": "https://electrek.co/2026/08/20/tesla-discontinues-solar-roof-panels-only/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-08-24T01:21:56+00:00",
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
    "id": "hn:49350858",
    "domain": "金融",
    "title": "AI Is Upending One of Finance's Cushiest Jobs",
    "url": "https://www.bloomberg.com/news/features/2026-06-05/ai-is-upending-traditional-financial-advisor-jobs",
    "source": "theriddlr",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-18T18:59:38+00:00",
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
  }
]
```
