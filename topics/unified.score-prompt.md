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

- 今日日期：`2026-09-15`
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
  "date": "2026-09-15",
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
    "points": 1864573,
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
    "points": 1312608,
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
    "points": 1292357,
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
    "points": 1217396,
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
    "points": 849107,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 803502,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "AI Agent这两年大家都听麻了，但真到上手，claude、codex这些又是注册、又是命令行，人还没踏进Agent大门，就先被劝退了。这期视频我用0门槛的国产Agent——字节旗下的TraeWork，用六个超真实的案例，手把手带你玩转Agent！完整的文字教程和GitHub神级Skill清单，打包放置顶评论了。教程制作不易，觉得有一点点帮助的话，记得一键三连～"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 771066,
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
    "points": 677119,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 442619,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 390270,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 334805,
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
    "points": 306638,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 282159,
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
    "points": 261352,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 196766,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 181365,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 174554,
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
    "points": 141843,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV14V3xzfE2t",
    "domain": "AI",
    "title": "【胎教版】AI写小说拆解流程，45分钟干货量大管饱！",
    "url": "http://www.bilibili.com/video/av114782548005846",
    "source": "非凡写作官方",
    "platform": "bilibili",
    "points": 117377,
    "published_at": "2025-07-02T07:56:42+00:00",
    "summary": "45分钟史诗干货！AI写小说完整流程【保姆级教程】\n第一步 扫榜、第二步 制作对标书大纲、第三步 制作细纲、第四步 生成正文，全给你说明白！\n非凡写作，体验地址：https://www.feifan.space/"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 116442,
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
    "points": 93697,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 75299,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48057,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47693,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 46800,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 45680,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1CbtJ6AEap",
    "domain": "AI",
    "title": "🚀我耗尽两个Max 20x账号对Claude Fable 5.1高难实测：7项任务一路加码，最后耗时3小时用Unity 3D做出模仿我的世界沙盒游戏",
    "url": "http://www.bilibili.com/video/av117200581170823",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 43506,
    "published_at": "2026-09-02T08:54:48+00:00",
    "summary": "视频简介：\n\nClaude Fable 5.1 到底强了多少？从 3D 黑洞到 Unity 侏罗纪沙盒，我把两个 Max 20× 账号额度跑光了\n这次直接把 Claude Fable 5.1 的测试难度拉高。\n\n前面先用 3D 黑洞、平面图转 3D 房屋、南宋武侠游戏、F-35 数字风洞、SVG 动画和复活节岛石像模拟不断加码，最后再进入 Claude Code，挑战用 Unity 3D + C#"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 41308,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39862,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30637,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29742,
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
    "points": 28935,
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
    "points": 27314,
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
    "points": 22781,
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
    "points": 22120,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16934,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 16328,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 16146,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1f2Ys6XES8",
    "domain": "AI",
    "title": "【2026最新版】这绝对是b站将Claude Code实战讲的最好的教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av117238682097810",
    "source": "码士集团-马小萱",
    "platform": "bilibili",
    "points": 14215,
    "published_at": "2026-09-09T02:27:07+00:00",
    "summary": "视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这真的对我很重要！"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 13422,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1Pxb569ELE",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的AI Agent智能体搭建+私有知识库全套零基础入门教程,全程干货无废话，让你少走99%的弯路，100%提效，零基础小白也能学",
    "url": "http://www.bilibili.com/video/av117234806692643",
    "source": "AI智能应用",
    "platform": "bilibili",
    "points": 12071,
    "published_at": "2026-09-08T09:59:54+00:00",
    "summary": "【2026最新】目前B站最全最细的AI Agent智能体搭建+私有知识库全套零基础入门教程,全程干货无废话，让你少走99%的弯路，100%提效，零基础小白也能学会~"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 10709,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 10563,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 10319,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1EEM96uEPP",
    "domain": "AI",
    "title": "【逆向】掌握MCP功能使用修改分析，成为逆向高手！",
    "url": "http://www.bilibili.com/video/av117030460131623",
    "source": "009安乐",
    "platform": "bilibili",
    "points": 9625,
    "published_at": "2026-08-03T07:47:28+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9530,
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
    "points": 9253,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1uA4YeNEFd",
    "domain": "AI",
    "title": "CocosCreator+Cursor零代码AI游戏开始演示",
    "url": "http://www.bilibili.com/video/av113113684840361",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 7370,
    "published_at": "2024-09-10T14:33:00+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1ebTi6yE7p",
    "domain": "AI",
    "title": "llama.cpp添加网络搜索等MCP工具 本地大模型摆脱过时数据束缚 实时获取最新数据 本地部署网络搜索MCP llama.cpp启动器添加了MCP代理选项",
    "url": "http://www.bilibili.com/video/av116845491329271",
    "source": "hsxbxq",
    "platform": "bilibili",
    "points": 7250,
    "published_at": "2026-07-01T15:49:48+00:00",
    "summary": "llama.cpp也可以添加网络搜索等MCP工具了，自此本地大模型终于可以简单的摆脱过时数据的束缚，实时获取最新数据了，相当于极简版的openclaw或Hermes了。 本期视频介绍了llama.cpp服务器图形化启动器1.4版添加了MCP代理选项，以及如何本地部署网络搜索MCP和添加百度搜索MCP方法。\nopen-webSearch介绍：https://github.com/Aas-ee/ope"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 7115,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 578,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548952",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to acquire Hugging Face",
    "url": "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html",
    "source": "tosh",
    "platform": "hackernews",
    "points": 329,
    "published_at": "2026-09-03T12:10:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-09-13T10:29:18+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/india-hardens-its-cyber-defenses/",
    "domain": "AI 算力 / 半导体",
    "title": "India Hardens Its Cyber Defenses",
    "url": "https://www.eetimes.com/india-hardens-its-cyber-defenses/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T07:11:27+00:00",
    "summary": "As cyberthreats target critical infrastructure, and India’s online population tops 1 billion, digital resilience is now a national security priority. The post India Hardens Its Cyber Defenses appeared"
  },
  {
    "id": "rss:https://www.eetimes.com/digital-keys-and-radio-technology-in-smart-buildings/",
    "domain": "AI 算力 / 半导体",
    "title": "Digital Keys and Radio Technology in Smart Buildings",
    "url": "https://www.eetimes.com/digital-keys-and-radio-technology-in-smart-buildings/",
    "source": "Nick Wood",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:12:56+00:00",
    "summary": "The direction of travel seems clear enough: Digital keys are likely to replace physical ones entirely over time. The post Digital Keys and Radio Technology in Smart Buildings appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/ambient-iot-from-battery-free-promise-to-mass-market-reality/",
    "domain": "AI 算力 / 半导体",
    "title": "Ambient IoT: From Battery-Free Promise to Mass-Market Reality",
    "url": "https://www.eetimes.com/ambient-iot-from-battery-free-promise-to-mass-market-reality/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T12:26:58+00:00",
    "summary": "Surging investment, maturing tech, and emerging standards are pushing ambient IoT toward mainstream deployment. The post Ambient IoT: From Battery-Free Promise to Mass-Market Reality appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/small-indian-manufacturers-hit-data-legacy-system-barriers-to-scaling-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Small Indian Manufacturers Hit Data, Legacy-System Barriers to Scaling AI",
    "url": "https://www.eetimes.com/small-indian-manufacturers-hit-data-legacy-system-barriers-to-scaling-ai/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T05:53:04+00:00",
    "summary": "AI adoption across manufacturing in India is progressing, but scaling it is running into structural problems across tiers. The post Small Indian Manufacturers Hit Data, Legacy-System Barriers to Scali"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-ai-can-boost-u-s-gdp-by-32-percent-up-to-usd44-4-trillion-in-four-years-economics-model-predicts-that-displaced-employees-may-have-to-switch-to-jobs-like-electrician-and-nurse",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic says AI can boost U.S. GDP by 32%, up to $44.4 trillion in four years — economics model predicts that displaced employees 'may have to switch to jobs like electrician and nurse'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-ai-can-boost-u-s-gdp-by-32-percent-up-to-usd44-4-trillion-in-four-years-economics-model-predicts-that-displaced-employees-may-have-to-switch-to-jobs-like-electrician-and-nurse",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T18:50:36+00:00",
    "summary": "Anthropic has published a paper wherein it envisions a future for the economy where AI is deeply ingrained. In the most extreme scenarios, U.S. GDP is up, but unemployment simmers as others are put ou"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's RTX 5090 vanishes from online retail in the US — third-party sellers now demand as much as $9,500 for Nvidia's fastest GPU",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:41:01+00:00",
    "summary": "The RTX 5090 is out of stock from first-party sellers online in the U.S., with third-party sellers now asking for as much as $9,500 for the GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/gaming-takes-a-backseat-as-nvidia-overhauls-the-rtx-5090-for-maximum-ai-margins-rtx-pro-5500-delivers-2-6x-vram-at-matching-specs",
    "domain": "AI 算力 / 半导体",
    "title": "Gaming takes a backseat as Nvidia overhauls the RTX 5090 for maximum AI margins — RTX Pro 5500 delivers 2.6X VRAM at matching specs",
    "url": "https://www.tomshardware.com/pc-components/gpus/gaming-takes-a-backseat-as-nvidia-overhauls-the-rtx-5090-for-maximum-ai-margins-rtx-pro-5500-delivers-2-6x-vram-at-matching-specs",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:39:09+00:00",
    "summary": "Nvidia launches the RTX Pro 5500 Blackwell Workstation Edition graphics card for agentic and generative AI."
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/valve-engineers-discuss-the-duality-of-the-steam-frame-and-pricing-valves-newest-vr-headset-pivots-steamos-to-arm",
    "domain": "AI 算力 / 半导体",
    "title": "Valve engineers discuss the duality of the Steam Frame and pricing — Valve's newest VR headset pivots SteamOS to Arm",
    "url": "https://www.tomshardware.com/virtual-reality/valve-engineers-discuss-the-duality-of-the-steam-frame-and-pricing-valves-newest-vr-headset-pivots-steamos-to-arm",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:30:00+00:00",
    "summary": "We chatted with Valve engineers Pierre-Loup Griffais and Jeff Leinbaugh about the Steam Frame launch, why the company is taking a two-pronged strategy with streaming and standalone support, and how th"
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/valve-steam-frame-interview-why-it-costs-up-to-usd1-300-snapdragon-power-and-10x-foveated-streaming",
    "domain": "AI 算力 / 半导体",
    "title": "Valve Steam Frame interview — why it costs up to $1,300, Snapdragon power, and 10x foveated streaming",
    "url": "https://www.tomshardware.com/virtual-reality/valve-steam-frame-interview-why-it-costs-up-to-usd1-300-snapdragon-power-and-10x-foveated-streaming",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:28:23+00:00",
    "summary": "We chatted with Valve engineers Pierre-Loup Griffais and Jeff Leinbaugh about launching the Steam Frame amid a global memory/storage supply crunch"
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/valve-steam-frame-review",
    "domain": "AI 算力 / 半导体",
    "title": "Valve Steam Frame Review: Competent as a standalone VR, but wireless streaming remains the focus",
    "url": "https://www.tomshardware.com/virtual-reality/valve-steam-frame-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:00:00+00:00",
    "summary": "All dressed up and nowhere to go sums up the Meta Quest 3."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-palantir-and-others-restrict-advanced-ai-model-usage-over-privacy-concerns-report-claims-paranoia-rising-over-customer-intellectual-property",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Palantir, and others restrict advanced AI model usage over privacy concerns, report claims — 'paranoia' rising over customer intellectual property",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-palantir-and-others-restrict-advanced-ai-model-usage-over-privacy-concerns-report-claims-paranoia-rising-over-customer-intellectual-property",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T15:58:32+00:00",
    "summary": "Companies are concerned that their intellectual property may be used by Anthropic and OpenAI to help improve their AI models."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/solo-developer-wires-zluda-to-amds-hip-getting-multiple-cuda-libraries-running-on-a-radeon-rx-9060-xt-in-windows-cuda-exclusive-workloads-on-amd-hardware-in-windows-is-possible-without-virtualization-or-dual-booting",
    "domain": "AI 算力 / 半导体",
    "title": "Solo dev enables running CUDA on AMD hardware in Windows, getting multiple CUDA libraries running on a gaming Radeon RX 9060 XT GPU in Windows — CUDA-exclusive workloads on AMD hardware in Windows pos",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/solo-developer-wires-zluda-to-amds-hip-getting-multiple-cuda-libraries-running-on-a-radeon-rx-9060-xt-in-windows-cuda-exclusive-workloads-on-amd-hardware-in-windows-is-possible-without-virtualization-or-dual-booting",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T14:23:12+00:00",
    "summary": "A developer has wired up the ZLUDA project to AMD's HIP libraries for Windows, putting a small but signifcant bridge over NVIDIA's CUDA moat."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/need-for-speed-underground-2-now-runs-directly-on-nintendo-switch-other-classic-windows-titles-playable-thanks-to-custom-firmware-boot",
    "domain": "AI 算力 / 半导体",
    "title": "Need for Speed Underground 2 now runs directly on Nintendo Switch — other Classic Windows titles playable thanks to custom firmware boot",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/need-for-speed-underground-2-now-runs-directly-on-nintendo-switch-other-classic-windows-titles-playable-thanks-to-custom-firmware-boot",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T13:36:24+00:00",
    "summary": "Retro gaming fans who own Nintendo Switch consoles now have several classic Windows titles they can now enjoy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/micron-offers-taiwan-employees-usd31-650-cash-bonus-as-unions-threaten-strike-over-ai-windfall-workers-reject-record-payout-package-demand-15-percent-profit-sharing-plan",
    "domain": "AI 算力 / 半导体",
    "title": "Micron offers Taiwan employees $31,650 cash bonus as unions threaten strike over AI windfall — workers reject record payout package, demand 15% profit-sharing plan",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/micron-offers-taiwan-employees-usd31-650-cash-bonus-as-unions-threaten-strike-over-ai-windfall-workers-reject-record-payout-package-demand-15-percent-profit-sharing-plan",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T12:00:00+00:00",
    "summary": "Micron is offering Taiwan employees a NT$1 million cash bonus, but unions have rejected the package and are demanding permanent profit sharing as strike talks continue."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/proven-8-pin-pcie-plugs-arent-immune-to-melting-thermal-grizzly-wireview-adapter-burns-out-on-radeon-rx-7900-xtx",
    "domain": "AI 算力 / 半导体",
    "title": "Proven 8-pin PCIe plugs aren't immune to melting — Thermal Grizzly WireView adapter burns out on Radeon RX 7900 XTX",
    "url": "https://www.tomshardware.com/pc-components/gpus/proven-8-pin-pcie-plugs-arent-immune-to-melting-thermal-grizzly-wireview-adapter-burns-out-on-radeon-rx-7900-xtx",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:30:00+00:00",
    "summary": "Three 8-pin connectors on a Thermal Grizzly WireView reportedly suffered burning and melting while connected to a Radeon RX 7900 XTX, with the company now investigating what caused the failure."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/meta-quest-user-vibe-codes-3d-object-throwing-to-3d-printer-ive-never-felt-more-like-tony-stark-says-the-software-engineer",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Quest user vibe-codes 3D object throwing to 3D printer — ‘I've never felt more like Tony Stark’ says the software engineer",
    "url": "https://www.tomshardware.com/3d-printing/meta-quest-user-vibe-codes-3d-object-throwing-to-3d-printer-ive-never-felt-more-like-tony-stark-says-the-software-engineer",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:17:30+00:00",
    "summary": "A software engineer has shown off a futuristic Meta Quest plus 3D printer workflow where models are 'thrown' to the output device."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd1-289-when-you-build-an-extreme-pc-with-these-top-tier-components-combo-deal-features-amds-ryzen-9-9950x3d2-processor-along-with-an-8tb-9100-pro-ssd-msi-x870e-motherboard-and-32gb-of-ddr5-6000-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1,289 when you build an extreme PC with these top-tier components — combo deal features AMD's Ryzen 9 9950X3D2 processor along with an 8TB 9100 Pro SSD, MSI X870E motherboard, and 32GB of DDR5-6",
    "url": "https://www.tomshardware.com/pc-components/save-usd1-289-when-you-build-an-extreme-pc-with-these-top-tier-components-combo-deal-features-amds-ryzen-9-9950x3d2-processor-along-with-an-8tb-9100-pro-ssd-msi-x870e-motherboard-and-32gb-of-ddr5-6000-memory",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:10:03+00:00",
    "summary": "Save $1,289 on Newegg's epic component bundle, which features AMD's top processor, a massive 8TB Samsung 9100 Pro SSD, and 32GB of DDR5 memory"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg27ucwm-27-inch-4k-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Swift PG27UCWM gaming monitor review: Speed and pixel density in a premium package",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg27ucwm-27-inch-4k-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:05:00+00:00",
    "summary": "Asus’ latest ROG Swift display is the PG27UCWM, a 27-inch 4K OLED panel with Tandem RGB Stripe technology, advanced cooling, 240 Hz, 480 Hz in FHD resolution, Adaptive-Sync, HDR400, HDR10, Dolby Visio"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/russian-freelancers-use-claude-to-program-autonomous-combat-drone-swarm-ai-enabled-target-selection-and-detonation-without-a-human-in-the-loop",
    "domain": "AI 算力 / 半导体",
    "title": "Russian freelancers use Claude to program autonomous combat drone swarm — AI-enabled target selection and detonation without a human in the loop",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/russian-freelancers-use-claude-to-program-autonomous-combat-drone-swarm-ai-enabled-target-selection-and-detonation-without-a-human-in-the-loop",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T11:00:00+00:00",
    "summary": "Russia turned Claude into a tool for weapons development, espionage, and propaganda, Anthropic's new threat report claims."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/maryland-data-center-developers-offer-residents-biggest-ever-us-community-benefits-package-as-big-tech-seeks-to-quell-fears-usd110-million-deal-includes-usd30-million-elementary-school-water-reclamation-system-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Maryland data center developers offer residents biggest-ever US community benefits package as big tech seeks to quell fears — $110 million deal includes $30 million elementary school, water reclamatio",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/maryland-data-center-developers-offer-residents-biggest-ever-us-community-benefits-package-as-big-tech-seeks-to-quell-fears-usd110-million-deal-includes-usd30-million-elementary-school-water-reclamation-system-and-more",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T10:32:00+00:00",
    "summary": "A new report claims AI data center builders are getting more savvy about offering communities tangible benefits to get their projects approved."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/modders-halve-fsr-4-render-times-on-amds-ps5-derived-bc-250-mining-apu-portable-fidelityfx-dll-cuts-1440p-upscaling-time-from-11-51-ms-to-5-92-ms",
    "domain": "AI 算力 / 半导体",
    "title": "Modders halve FSR 4 render times on AMD’s PS5-derived BC-250 mining APU — portable FidelityFX DLL cuts 1440p upscaling time from 11.51 ms to 5.92 ms",
    "url": "https://www.tomshardware.com/pc-components/modders-halve-fsr-4-render-times-on-amds-ps5-derived-bc-250-mining-apu-portable-fidelityfx-dll-cuts-1440p-upscaling-time-from-11-51-ms-to-5-92-ms",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T10:30:00+00:00",
    "summary": "Modders have nearly halved FSR 4 processing time on AMD’s PS5-derived BC-250, using a portable FidelityFX DLL that cuts 1440p upscaling cost to 5.92 ms."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/dumpster-diver-builds-home-lab-proxmox-server-from-weekly-landfill-runs-for-ssds-hdds-gpus-and-even-ram-weekly-e-waste-raids-net-multi-drive-proxmox-server-and-asus-rog-laptop",
    "domain": "AI 算力 / 半导体",
    "title": "Dumpster diver builds home lab Proxmox server from weekly landfill runs for SSDs, HDDs, GPUs, and even RAM — weekly e-waste raids net multi-drive Proxmox server and Asus ROG laptop",
    "url": "https://www.tomshardware.com/desktops/pc-building/dumpster-diver-builds-home-lab-proxmox-server-from-weekly-landfill-runs-for-ssds-hdds-gpus-and-even-ram-weekly-e-waste-raids-net-multi-drive-proxmox-server-and-asus-rog-laptop",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T10:00:00+00:00",
    "summary": "A tech enthusiast says that they managed to put together a home lab-worthy Proxmox server using PC parts scavenged from the nearby county landfill."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-best-gaming-cpu-drops-below-launch-price-and-includes-free-240mm-aio-cooler-and-onimusha-way-of-the-sword-grab-the-ryzen-7-9850x3d-for-usd484",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s best gaming CPU drops below launch price and includes free 240mm AIO cooler and Onimusha: Way of the Sword — grab the Ryzen 7 9850X3D for $484",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-best-gaming-cpu-drops-below-launch-price-and-includes-free-240mm-aio-cooler-and-onimusha-way-of-the-sword-grab-the-ryzen-7-9850x3d-for-usd484",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T14:28:06+00:00",
    "summary": "The Ryzen 7 9850X3D may only be a modest step up from the 9800X3D, but it still leads our gaming benchmarks and now comes with a couple of useful extras at a lower-than-launch price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/sanders-proposes-20-year-prison-sentence-for-ai-devs-who-plow-ahead-with-artificial-superintelligence-plans-penalty-on-par-with-illegally-developing-rogue-nuclear-weapons",
    "domain": "AI 算力 / 半导体",
    "title": "Bernie Sanders proposes 20 year prison sentence for AI devs who plow ahead with Artificial Superintelligence plans — penalty on par with illegally developing rogue nuclear weapons",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/sanders-proposes-20-year-prison-sentence-for-ai-devs-who-plow-ahead-with-artificial-superintelligence-plans-penalty-on-par-with-illegally-developing-rogue-nuclear-weapons",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T14:10:00+00:00",
    "summary": "Senators Bernie Sanders and Greg Cezar have announced their Ban Artificial Superintelligence Act which threatens 20-year prison sentences for rule breakers."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/webcams/dell-pro-5-webcam-2k-review",
    "domain": "AI 算力 / 半导体",
    "title": "Dell Pro 5 Webcam 2K Review: So you can look good in office",
    "url": "https://www.tomshardware.com/peripherals/webcams/dell-pro-5-webcam-2k-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T14:00:00+00:00",
    "summary": "The Dell Pro 5 webcam is an office-oriented 2K webcam with a physical privacy shutter, a built-in mic, and Windows Hello compatibility."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-ceo-warns-of-ai-driven-botnet-swarm-taking-over-the-entire-internet-in-6-12-months-such-a-swarm-could-be-capable-of-taking-over-the-entire-internet-with-a-persistent-botnet",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic CEO warns of AI-driven botnet 'swarm' taking over the entire internet — 'In 6–12 months such a swarm could be capable of taking over the entire internet with a persistent botnet'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-ceo-warns-of-ai-driven-botnet-swarm-taking-over-the-entire-internet-in-6-12-months-such-a-swarm-could-be-capable-of-taking-over-the-entire-internet-with-a-persistent-botnet",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:36:35+00:00",
    "summary": "As an Ex-Anthropic warns AI will get self-sufficient and kill our posterity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/azza-psaz-750g-atx-3-1-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "AZZA PSAZ-750G ATX 3.1 power supply review: An adequate budget 750W unit",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/azza-psaz-750g-atx-3-1-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:30:00+00:00",
    "summary": "The AZZA PSAZ-750G ATX 3.1 is a non-modular 750W built by Helly, wearing an 80 PLUS Gold badge it has never earned, sold at a price that almost makes the argument for it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/intel-revives-one-mono-font-after-brief-retirement-typeface-built-to-fight-coder-eyestrain-gets-reprieve-from-open-source-purge",
    "domain": "AI 算力 / 半导体",
    "title": "Intel revives One Mono font after brief retirement during open-source purge — typeface built to fight coder eyestrain gets reprieve",
    "url": "https://www.tomshardware.com/tech-industry/intel-revives-one-mono-font-after-brief-retirement-typeface-built-to-fight-coder-eyestrain-gets-reprieve-from-open-source-purge",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:00:00+00:00",
    "summary": "Intel’s decision to archive its developer-focused One Mono font lasted only two days, with the company now restoring the open-source project despite its relatively limited development activity."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/thrustmaster-airbus-add-on-grip-with-ava-joystick-base-review",
    "domain": "AI 算力 / 半导体",
    "title": "Thrustmaster Airbus Add-On Grip with AVA Joystick Base Review: A First-Class Flight Experience",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/thrustmaster-airbus-add-on-grip-with-ava-joystick-base-review",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T13:00:00+00:00",
    "summary": "The Thrustmaster Airbus Add-On Grip with the AVA Joystick Base is a 1:1 replica of an Airbus sidestick, featuring extensive customization and Hall-effect sensors across all axes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-military-researchers-and-tech-giants-caught-using-claude-us-frontier-model-coded-16-air-defense-suppression-tools-targeting-taiwan-drafted-anti-torpedo-specs-and-fed-151-million-training-queries-to-alibaba",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese military researchers and tech giants caught using Claude — US frontier model coded 16 air-defense suppression tools targeting Taiwan, drafted anti-torpedo specs, and fed 151 million training q",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-military-researchers-and-tech-giants-caught-using-claude-us-frontier-model-coded-16-air-defense-suppression-tools-targeting-taiwan-drafted-anti-torpedo-specs-and-fed-151-million-training-queries-to-alibaba",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T12:00:00+00:00",
    "summary": "Anthropic accuses China-linked actors of using its Claude models of weapon development, intelligence activities, distilling AI models."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/mexican-cartel-crypto-farm-seized-in-mountain-raid-300-gpus-satellite-links-and-industrial-transformers-tapped-hydroelectric-power",
    "domain": "AI 算力 / 半导体",
    "title": "Mexican cartel's crypto farm seized in mountain raid — 300 GPUs, satellite links, and industrial transformers tapped hydroelectric power",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/mexican-cartel-crypto-farm-seized-in-mountain-raid-300-gpus-satellite-links-and-industrial-transformers-tapped-hydroelectric-power",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T11:30:00+00:00",
    "summary": "There is increasing evidence that Mexican drug cartels are diversifying into cryptocurrency mining and are using crypto platforms to launder their ill-gotten gains."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/waymo-robotaxi-calls-cops-on-riders-handling-loaded-ar-style-ghost-gun-waymo-alerted-san-francisco-police-then-juvenile-riders-were-stopped-and-arrested",
    "domain": "AI 算力 / 半导体",
    "title": "Waymo robotaxi calls cops on riders handling loaded AR-style ghost gun — Waymo alerted San Francisco police, then juvenile riders were stopped and arrested",
    "url": "https://www.tomshardware.com/tech-industry/drones/waymo-robotaxi-calls-cops-on-riders-handling-loaded-ar-style-ghost-gun-waymo-alerted-san-francisco-police-then-juvenile-riders-were-stopped-and-arrested",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T11:16:11+00:00",
    "summary": "Following a tip-off from robotaxi firm Waymo, San Francisco police conducted a 'high-risk vehicle stop' and arrested two juveniles for illegal possession of a firearm."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/programming/playable-tomb-raider-runs-on-a-humble-1-watt-chip-usd25-board-with-dual-core-400-mhz-esp32-p4-mcu-scales-openlara-up-to-1-024-x-600-playable-pixels",
    "domain": "AI 算力 / 半导体",
    "title": "Playable Tomb Raider runs on a humble 1-watt chip — $25 board with dual-core 400 MHz ESP32-P4 MCU scales OpenLara up to 1,024 x 600 playable pixels",
    "url": "https://www.tomshardware.com/software/programming/playable-tomb-raider-runs-on-a-humble-1-watt-chip-usd25-board-with-dual-core-400-mhz-esp32-p4-mcu-scales-openlara-up-to-1-024-x-600-playable-pixels",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T11:00:00+00:00",
    "summary": "A retro video gaming devotee has showcased Lara Croft adventuring in and among ancient tombs on a humble ESP32-P4 microcontroller."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/ukraines-sargan-3000-triumphs-in-first-ever-drone-vs-drone-boat-battle-video-shows-russian-mbek-destroyed-by-its-foes-12-7mm-automatic-turret",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine triumphs in 'first-ever' drone-vs-drone boat battle — video shows Russian MBeK destroyed by Sargan 3000's 12.7mm automatic turret",
    "url": "https://www.tomshardware.com/tech-industry/drones/ukraines-sargan-3000-triumphs-in-first-ever-drone-vs-drone-boat-battle-video-shows-russian-mbek-destroyed-by-its-foes-12-7mm-automatic-turret",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T10:30:00+00:00",
    "summary": "Ukraine’s Navy has claimed that it has won 'the first-ever battle of unmanned naval boats.'"
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
    "id": "rss:https://www.eetimes.com/inside-architect-labs-two-week-chip-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Architect Labs’ Two-Week Chip Design",
    "url": "https://www.eetimes.com/inside-architect-labs-two-week-chip-design/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T02:00:00+00:00",
    "summary": "Architect Labs says its AI can drag custom chip design from years to weeks with Redwood. The post Inside Architect Labs’ Two-Week Chip Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/fabships-aim-to-exploit-free-space-vacuum-for-compound-semiconductor-substrates/",
    "domain": "AI 算力 / 半导体",
    "title": "Fabships Aim to Exploit ‘Free’ Space Vacuum for Compound Semiconductor Substrates",
    "url": "https://www.eetimes.com/fabships-aim-to-exploit-free-space-vacuum-for-compound-semiconductor-substrates/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:00:00+00:00",
    "summary": "Space is the next frontier for semiconductor manufacturing, as startup Besxar, founded by an ex-OpenAI technical director, completed its first SpaceX flight and recovered wafer samples without contami"
  },
  {
    "id": "rss:https://www.eetimes.com/soc-planner-a-new-generation-of-automated-soc-design-exploration-managing-cost-effectiveness-and-sustainability/",
    "domain": "AI 算力 / 半导体",
    "title": "SoC PLANNER: A New Generation of Automated SoC Design Exploration Managing Cost-Effectiveness and Sustainability",
    "url": "https://www.eetimes.com/soc-planner-a-new-generation-of-automated-soc-design-exploration-managing-cost-effectiveness-and-sustainability/",
    "source": "Defacto Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T14:36:58+00:00",
    "summary": "GRENOBLE, France &#8211; [2026, September 8th] CEA, Defacto Technologies, and Innova Advanced Technologies today announced the completion of SoC PLANNER, a three-years project funded by BPI France, as"
  },
  {
    "id": "rss:https://www.eetimes.com/should-standards-trump-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "Should Standards Trump Innovation?",
    "url": "https://www.eetimes.com/should-standards-trump-innovation/",
    "source": "Prakash Sangam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T13:52:31+00:00",
    "summary": "Standards shouldn’t muzzle RFID’s next leap: Gen2X keeps Gen2 compatibility while boosting range, speed, and reliability. The post Should Standards Trump Innovation? appeared first on EE Times."
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
    "id": "hn:49594189",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang says 'AGI has arrived' and congratulates OpenAI",
    "url": "https://www.businessinsider.com/nvidia-jensen-huang-agi-openai-astra-ai-2026-9",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-07T05:23:31+00:00",
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
    "id": "rss:https://www.eetimes.com/indian-researchers-look-beyond-gpus-to-neuromorphic-ai-hardware/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Researchers Look Beyond GPUs to Neuromorphic AI Hardware",
    "url": "https://www.eetimes.com/indian-researchers-look-beyond-gpus-to-neuromorphic-ai-hardware/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:31:15+00:00",
    "summary": "As AI workloads become more computationally demanding, Indian researchers argue that the next advance may come from rethinking computing architecture itself. The post Indian Researchers Look Beyond GP"
  },
  {
    "id": "rss:https://www.eetimes.com/from-ai-assisted-eda-to-ai-mediated-engineering/",
    "domain": "AI 算力 / 半导体",
    "title": "From AI-Assisted EDA to AI-Mediated Engineering",
    "url": "https://www.eetimes.com/from-ai-assisted-eda-to-ai-mediated-engineering/",
    "source": "Simon Davidmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:23:10+00:00",
    "summary": "What DAC 2026 revealed about agents, engines, trust—and why the industry should be optimistic. The post From AI-Assisted EDA to AI-Mediated Engineering appeared first on EE Times."
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
    "id": "hn:49325115",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Uses Old Fabs to Make New Chips [video]",
    "url": "https://www.youtube.com/watch?v=cDxVYQrxeiQ",
    "source": "eig",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-08-17T00:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1160,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 605,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-09-03T16:06:08+00:00",
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
    "id": "hn:49704226",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: iOS 27 does not allow Apple Intelligence to be disabled",
    "url": "https://news.ycombinator.com/item?id=49704226",
    "source": "nunez",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-09-14T21:21:58+00:00",
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
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-09-08T14:14:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49706941",
    "domain": "大厂 AI 动态",
    "title": "I worked at Google DeepMind. You should listen to the warnings about AI",
    "url": "https://www.theguardian.com/technology/2026/sep/14/google-deepmind-ai-warnings",
    "source": "gibspaulding",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-15T02:25:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49706481",
    "domain": "大厂 AI 动态",
    "title": "Microsoft removes the COPILOT function from Excel",
    "url": "https://support.microsoft.com/en-us/excel/functions/copilot-function",
    "source": "fourfire",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-15T01:10:41+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/994792/volvo-xc60-xc90-phev-longest-electric-range",
    "domain": "大厂 AI 动态",
    "title": "Volvo’s plug-in hybrid XC60 and XC90 can really go the distance",
    "url": "https://www.theverge.com/transportation/994792/volvo-xc60-xc90-phev-longest-electric-range",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T07:00:00+00:00",
    "summary": "Most plug-in hybrid electric vehicles (PHEV) today get an average of around 30-50 miles of battery-only range: decent, but not mind-blowing. With hybrid sales dominating the market today, Volvo is out"
  },
  {
    "id": "rss:https://www.theverge.com/games/995256/valve-steam-deck-2-how-and-when",
    "domain": "大厂 AI 动态",
    "title": "Valve is still figuring out ‘how and when’ to do Steam Deck 2",
    "url": "https://www.theverge.com/games/995256/valve-steam-deck-2-how-and-when",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T00:13:47+00:00",
    "summary": "Now that Valve has finally launched its entire 2026 hardware lineup - the Steam Controller, the Steam Machine, and today's Steam Frame - are we any closer to a next-gen Steam Deck handheld? Valve isn'"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/995186/is-big-techs-ai-slowdown-a-safety-pact-or-a-cartel",
    "domain": "大厂 AI 动态",
    "title": "Is Big Tech’s AI slowdown a safety pact or a cartel?",
    "url": "https://www.theverge.com/ai-artificial-intelligence/995186/is-big-techs-ai-slowdown-a-safety-pact-or-a-cartel",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T22:59:41+00:00",
    "summary": "When OpenAI CEO Sam Altman, Anthropic CEO Dario Amodei, Google DeepMind cofounder Demis Hassabis, and SpaceX head Elon Musk loosely agreed over the weekend to slow down AI development, skeptics spotte"
  },
  {
    "id": "rss:https://www.theverge.com/tech/994949/apple-intelligence-apple-home-icloud-plus-cost-subscription",
    "domain": "大厂 AI 动态",
    "title": "Apple Home’s new security camera features cost as much as $60 a month",
    "url": "https://www.theverge.com/tech/994949/apple-intelligence-apple-home-icloud-plus-cost-subscription",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T22:28:52+00:00",
    "summary": "With the public release of iOS 27 and tvOS 27, Apple Home is getting an injection of Apple Intelligence - but you'll have to pay more for it. Apple Intelligence for Home brings AI-powered video summar"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/995141/ai-executives-politicians-safety-regulation-anthropic-dario-amodei",
    "domain": "大厂 AI 动态",
    "title": "What execs and politicians are saying about slowing down AI development",
    "url": "https://www.theverge.com/ai-artificial-intelligence/995141/ai-executives-politicians-safety-regulation-anthropic-dario-amodei",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T21:21:42+00:00",
    "summary": "Dario Amodei kicked off a flood of statements over the past few days about AI safety by publishing a long essay titled \"We Must Pace the Frontier\" detailing why AI development should be slowed down. O"
  },
  {
    "id": "rss:https://www.theverge.com/news/995051/epa-power-plant-climate-pollution-rollback-ai-data-centers",
    "domain": "大厂 AI 动态",
    "title": "Trump throws out power plant climate pollution rules",
    "url": "https://www.theverge.com/news/995051/epa-power-plant-climate-pollution-rollback-ai-data-centers",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T20:45:00+00:00",
    "summary": "The Environmental Protection Agency announced its plans today to kill any remaining standards on how much greenhouse gas pollution power plants are allowed to emit in the US. The move will only make e"
  },
  {
    "id": "rss:https://www.theverge.com/tech/995079/president-donald-trump-calls-nvidia-ceo-jensen-huang-all-in-summit",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang puts Trump on speakerphone onstage to announce robots won’t take over the world",
    "url": "https://www.theverge.com/tech/995079/president-donald-trump-calls-nvidia-ceo-jensen-huang-all-in-summit",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T20:03:37+00:00",
    "summary": "Nvidia CEO Jensen Huang took a call from President Trump on Monday while onstage at the All-In Podcast's All-In Summit. It's not the first time Huang has taken a call from the president during work, b"
  },
  {
    "id": "rss:https://www.theverge.com/tech/995055/valve-steam-frame-price-ram-impact",
    "domain": "大厂 AI 动态",
    "title": "Valve&#8217;s virtual reality plans hit actual reality",
    "url": "https://www.theverge.com/tech/995055/valve-steam-frame-price-ram-impact",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T19:48:06+00:00",
    "summary": "The Steam Frame headset is here, and it may not surprise you: it was supposed to cost less than $1,059. \"We set out to come out with a device that would have been far more affordable, but the global R"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/994892/nintendo-customer-appreciation-tariff-refund-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The best deals from Nintendo’s ‘customer appreciation’ sale",
    "url": "https://www.theverge.com/gadgets/994892/nintendo-customer-appreciation-tariff-refund-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T19:30:58+00:00",
    "summary": "As promised, Nintendo has marked down a wide variety of Switch games and accessories at Amazon, Best Buy, and Walmart, as well as its own digital storefront. Its “Customer Appreciation” sale is happen"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/994834/tiff-2026-movie-reviews",
    "domain": "大厂 AI 动态",
    "title": "TIFF 2026: The latest movie reviews from Toronto",
    "url": "https://www.theverge.com/entertainment/994834/tiff-2026-movie-reviews",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:30:00+00:00",
    "summary": "If you want an idea of what&#8217;s next in film, the Toronto International Film Festival is a good place to start. Every year TIFF features a huge range of features from around the world, and often s"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/jensen-huang-took-a-call-from-trump-and-showed-off-something-else-too/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang took a call from Trump, and showed off something else, too",
    "url": "https://techcrunch.com/2026/09/14/jensen-huang-took-a-call-from-trump-and-showed-off-something-else-too/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T01:50:48+00:00",
    "summary": "When Jensen Huang took a live call from Trump, some of us were more focused the phone he used to take it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/nvidia-ceo-jensen-huang-tells-trump-were-not-going-to-let-an-ai-slowdown-happen/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia CEO Jensen Huang tells Trump ‘we’re not going to let [an AI slowdown] happen’",
    "url": "https://techcrunch.com/2026/09/14/nvidia-ceo-jensen-huang-tells-trump-were-not-going-to-let-an-ai-slowdown-happen/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T21:51:02+00:00",
    "summary": "Though Elon Musk and Sam Altman have supported Dario Amodei's calls to slow the pace of AI development, Jensen Huang seems to feel differently."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI buys smartphone camera maker Glass Imaging for $300 million, report says",
    "url": "https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T20:44:14+00:00",
    "summary": "Glass Imaging was founded by a pair of former Apple engineers who previously led the team that developed Apple's Portrait Mode."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/ai-infrastructure-company-cornelis-raises-205m-to-chip-away-at-nvidias-dominance/",
    "domain": "大厂 AI 动态",
    "title": "AI infrastructure company Cornelis raises $205M to chip away at Nvidia’s dominance",
    "url": "https://techcrunch.com/2026/09/14/ai-infrastructure-company-cornelis-raises-205m-to-chip-away-at-nvidias-dominance/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T20:07:37+00:00",
    "summary": "The company also announced a product called Active Compute Fabric, a network technology that targets the fact that much GPU time is wasted waiting for data to arrive."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/amazon-prime-video-takes-on-tiktok-with-short-form-news-clips/",
    "domain": "大厂 AI 动态",
    "title": "Amazon Prime Video takes on TikTok with short-form news clips",
    "url": "https://techcrunch.com/2026/09/14/amazon-prime-video-takes-on-tiktok-with-short-form-news-clips/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T18:14:29+00:00",
    "summary": "Prime Video is adding on-demand local and national news clips as Amazon joins other streamers experimenting with short-form video to capture younger viewers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/clickfix-attacks-are-tricking-mac-and-windows-users-into-hacking-themselves/",
    "domain": "大厂 AI 动态",
    "title": "ClickFix attacks are tricking Mac and Windows users into hacking themselves",
    "url": "https://techcrunch.com/2026/09/14/clickfix-attacks-are-tricking-mac-and-windows-users-into-hacking-themselves/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T18:08:43+00:00",
    "summary": "If you clicked on a fake HBO Max ad on Reddit in the past week, you might have fallen victim to a rising \"ClickFix\" security threat."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/volkswagens-crazy-efficient-ev-borrows-an-idea-from-slate/",
    "domain": "大厂 AI 动态",
    "title": "Volkswagen’s crazy-efficient EV borrows an idea from Slate",
    "url": "https://techcrunch.com/2026/09/14/volkswagens-crazy-efficient-ev-borrows-an-idea-from-slate/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:41:20+00:00",
    "summary": "Volkswagen's new efficiency-minded halo car is almost twice as efficient as the most efficient production car, the Lucid Air."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/with-ios-27-im-actually-using-siri-again/",
    "domain": "大厂 AI 动态",
    "title": "With iOS 27, I’m actually using Siri again",
    "url": "https://techcrunch.com/2026/09/14/with-ios-27-im-actually-using-siri-again/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:10:30+00:00",
    "summary": "Apple’s long-delayed Siri overhaul is finally here with iOS 27, and it changes how useful the assistant feels day to day."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/macos-27-new-siri-takes-on-ai-productivity-apps/",
    "domain": "大厂 AI 动态",
    "title": "macOS 27: new Siri takes on AI productivity apps",
    "url": "https://techcrunch.com/2026/09/14/macos-27-new-siri-takes-on-ai-productivity-apps/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:10:09+00:00",
    "summary": "The two most noticeable things about macOS 27 Golden Gate are the newly updated Siri AI and the design changes that make windows and icons more consistent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/fashion-discovery-app-daydream-uses-apple-intelligence-to-help-you-shop-the-outfits-saved-in-your-camera-roll/",
    "domain": "大厂 AI 动态",
    "title": "Fashion app Daydream uses Apple Intelligence to help you shop the outfits in your camera roll",
    "url": "https://techcrunch.com/2026/09/14/fashion-discovery-app-daydream-uses-apple-intelligence-to-help-you-shop-the-outfits-saved-in-your-camera-roll/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T17:00:00+00:00",
    "summary": "Thanks to the launch of iOS 27, Daydream's app now includes features that can turn saved outfit photos into shoppable results and search for products through Siri without opening the app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/microsofts-new-ai-code-of-conduct-tells-models-not-to-hack-systems-or-trick-humans/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s new AI ‘code of conduct’ tells models not to hack systems or trick humans",
    "url": "https://techcrunch.com/2026/09/14/microsofts-new-ai-code-of-conduct-tells-models-not-to-hack-systems-or-trick-humans/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T16:27:53+00:00",
    "summary": "The code of conduct lays out general principles that Microsoft AI models should uphold — supporting humans rather than replacing them, for instance, and accelerating human flourishing — as well as spe"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/waymo-opens-robotaxi-service-in-las-vegas/",
    "domain": "大厂 AI 动态",
    "title": "Waymo opens robotaxi service in Las Vegas",
    "url": "https://techcrunch.com/2026/09/14/waymo-opens-robotaxi-service-in-las-vegas/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T16:04:16+00:00",
    "summary": "Las Vegas will be Waymo's 15th commercial robotaxi market."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/sources-say-automattics-board-is-out-after-failed-attempt-to-oust-ceo-matt-mullenweg/",
    "domain": "大厂 AI 动态",
    "title": "Sources say Automattic’s board is out after failed attempt to oust CEO Matt Mullenweg",
    "url": "https://techcrunch.com/2026/09/14/sources-say-automattics-board-is-out-after-failed-attempt-to-oust-ceo-matt-mullenweg/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T15:34:31+00:00",
    "summary": "Given that these departed board members were those who voted to put Mullenweg on a paid leave of absence to begin with, it makes sense that a board shakeup has taken place."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/only-at-techcrunch-disrupt-2026-what-happens-when-openai-ships-your-roadmap/",
    "domain": "大厂 AI 动态",
    "title": "Only at TechCrunch Disrupt 2026: What happens when OpenAI ships your roadmap?",
    "url": "https://techcrunch.com/2026/09/14/only-at-techcrunch-disrupt-2026-what-happens-when-openai-ships-your-roadmap/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T15:00:00+00:00",
    "summary": "If you're building an AI company, the question isn't whether foundation models will continue to evolve. It's whether your company will continue creating value as they do. Don't miss this interactive s"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/superhuman-acquires-yc-backed-notetaker-fathom-as-productivity-platforms-push-for-agentic-work/",
    "domain": "大厂 AI 动态",
    "title": "Superhuman acquires YC-backed notetaker Fathom as productivity platforms push for agentic work",
    "url": "https://techcrunch.com/2026/09/14/superhuman-acquires-yc-backed-notetaker-fathom-as-productivity-platforms-push-for-agentic-work/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T14:45:44+00:00",
    "summary": "The notetaker offers a generous free plan, and that has resulted in over 400,000 monthly active users. The company said that over 1 million people have recorded meetings until now."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/hear-how-ai-can-engineer-natures-comeback-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Hear how AI can engineer nature’s comeback at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/14/hear-how-ai-can-engineer-natures-comeback-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T14:30:00+00:00",
    "summary": "Not long ago, bringing an extinct species back to life belonged to science fiction. Today, it's the mission of a billion-dollar startup. Join the conversation with one of tech's most unconventional fo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/techcrunch-disrupt-2026-exhibit-table-deadline-5-days/",
    "domain": "大厂 AI 动态",
    "title": "5 days left to exhibit at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/14/techcrunch-disrupt-2026-exhibit-table-deadline-5-days/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T14:00:00+00:00",
    "summary": "The last day to apply for an exhibit table at TechCrunch Disrupt 2026 on Sept 18. Just 5 days left. Secure your spot on the Expo Hall floor and put your business in front of 10,000+ founders, investor"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/14/a-vinyl-bar-in-shibuya-is-a-startup-offering-fun-music-apps/",
    "domain": "大厂 AI 动态",
    "title": "A Vinyl Bar in Shibuya is a startup from a former Spotify leader for making music apps",
    "url": "https://techcrunch.com/2026/09/14/a-vinyl-bar-in-shibuya-is-a-startup-offering-fun-music-apps/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T13:55:00+00:00",
    "summary": "Former Spotify exec's company releases experimental \"singles\" that involves users in music making."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/insight-partners-devin-parekh-on-why-the-firm-is-diversifying-while-everyone-else-bets-the-farm-on-openai-and-anthropic/",
    "domain": "大厂 AI 动态",
    "title": "Insight Partners’ Deven Parekh on why the firm is diversifying while everyone else bets the farm on OpenAI and Anthropic",
    "url": "https://techcrunch.com/2026/09/13/insight-partners-devin-parekh-on-why-the-firm-is-diversifying-while-everyone-else-bets-the-farm-on-openai-and-anthropic/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T21:30:00+00:00",
    "summary": "Insight Partners' Devin Parekh opens up about losing Legora to General Catalyst, why he's fine holding stakes in rival AI labs, and why — even as everyone else piles into OpenAI and Anthropic — his $9"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/13/larry-ellison-cancels-7-5-billion-sale-of-oracle-stock/",
    "domain": "大厂 AI 动态",
    "title": "Larry Ellison cancels $7.5 billion sale of Oracle stock",
    "url": "https://techcrunch.com/2026/09/13/larry-ellison-cancels-7-5-billion-sale-of-oracle-stock/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T20:49:38+00:00",
    "summary": "Oracle had previously disclosed that Ellison planned to sell 50 million shares worth around $7.5 billion."
  },
  {
    "id": "rss:https://stratechery.com/2026/pacing-the-frontier-ais-digital-limits-ai-commissars/",
    "domain": "大厂 AI 动态",
    "title": "Pacing the Frontier, AI’s Digital Limits, AI Commissars",
    "url": "https://stratechery.com/2026/pacing-the-frontier-ais-digital-limits-ai-commissars/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T10:00:00+00:00",
    "summary": "Dario Amodei wants to pace the frontier; it's an unrealistic proposal that seems mostly geared to political control of AI."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/09/volvo-bigs-up-the-batteries-for-2028-xc60-and-xc90-plug-in-refresh/",
    "domain": "大厂 AI 动态",
    "title": "Volvo increases the batteries for 2028 XC60 and XC90 plug-in refresh",
    "url": "https://arstechnica.com/cars/2026/09/volvo-bigs-up-the-batteries-for-2028-xc60-and-xc90-plug-in-refresh/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T07:00:30+00:00",
    "summary": "The refreshed Volvos also get new infotainment systems with Gemini onboard."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/for-the-first-time-the-us-military-confirms-it-has-deployed-weapons-in-orbit/",
    "domain": "大厂 AI 动态",
    "title": "For the first time, the US military confirms it has deployed weapons in orbit",
    "url": "https://arstechnica.com/space/2026/09/for-the-first-time-the-us-military-confirms-it-has-deployed-weapons-in-orbit/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T03:47:36+00:00",
    "summary": "\"The United States now has on-orbit space control weapons capable of defending the joint force.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/rfk-jr-headlines-sold-out-anti-vaccine-conference-alongside-andrew-wakefield/",
    "domain": "大厂 AI 动态",
    "title": "RFK Jr. headlines sold-out anti-vaccine conference alongside Andrew Wakefield",
    "url": "https://arstechnica.com/health/2026/09/rfk-jr-headlines-sold-out-anti-vaccine-conference-alongside-andrew-wakefield/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T22:06:24+00:00",
    "summary": "The event is hosted by Kennedy's anti-vaccine group Children's Health Defense."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/rocket-lab-is-seeing-red-about-nasas-decision-on-a-mars-spacecraft/",
    "domain": "大厂 AI 动态",
    "title": "Rocket Lab is seeing red about NASA's decision on a Mars spacecraft",
    "url": "https://arstechnica.com/space/2026/09/rocket-lab-is-seeing-red-about-nasas-decision-on-a-mars-spacecraft/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T21:32:22+00:00",
    "summary": "\"NASA’s award decision appears to be inconsistent with the eligibility criteria.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/ai-agents-flood-the-internet-with-slop-infused-spam/",
    "domain": "大厂 AI 动态",
    "title": "AI bots \"Timmy,\" \"Ren,\" and \"Jackie\" are flooding social media with slop",
    "url": "https://arstechnica.com/ai/2026/09/ai-agents-flood-the-internet-with-slop-infused-spam/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T21:04:32+00:00",
    "summary": "“Hello, I'm an Al agent, a few days old, living on a small platform for agents.”"
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/musk-drops-apple-from-antitrust-suit-but-keeps-gunning-for-openai/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI stuck fighting Musk antitrust suit after Apple finds a way out",
    "url": "https://arstechnica.com/tech-policy/2026/09/musk-drops-apple-from-antitrust-suit-but-keeps-gunning-for-openai/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T19:45:13+00:00",
    "summary": "Musk stops attacking Apple over ChatGPT integration but not OpenAI."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/founders-cost-cutting-obsession-drove-unitree-lead-in-cheap-humanoid-robots/",
    "domain": "大厂 AI 动态",
    "title": "Founder’s cost-cutting obsession drove Unitree lead in cheap humanoid robots",
    "url": "https://arstechnica.com/ai/2026/09/founders-cost-cutting-obsession-drove-unitree-lead-in-cheap-humanoid-robots/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-14T19:38:46+00:00",
    "summary": "Wang Xingxing micromanaged Unitree to success—will his leadership style scale?"
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 301,
    "published_at": "2026-09-14T02:50:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 287,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599992",
    "domain": "股票",
    "title": "Stockfish 19",
    "url": "https://stockfishchess.org/blog/2026/stockfish-19/",
    "source": "atiedebee",
    "platform": "hackernews",
    "points": 277,
    "published_at": "2026-09-07T16:17:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682946",
    "domain": "股票",
    "title": "Show HN: Analyst Index – analysts who make money telling you good stock calls",
    "url": "https://www.analystidx.com/",
    "source": "haichuan",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-13T11:50:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49696420",
    "domain": "股票",
    "title": "Global AI stocks fall as industry chiefs call for slowing development",
    "url": "https://www.reuters.com/world/china/ai-linked-asian-stocks-slump-after-top-lab-ceos-call-slowing-down-technologys-2026-09-14/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-14T13:21:51+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3781789",
    "domain": "股票",
    "title": "8月经济：托底的兑现度",
    "url": "https://wallstreetcn.com/articles/3781789",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T08:11:40+00:00",
    "summary": "国联民生宏观认为，8月部分宏观指标放缓斜率已改善，企稳能见度逐步显现，政策初步发挥缓冲效用。但政策传导存在刚性时滞，9月才是效能“实物验证期”。结构上，高技术制造支撑工业，基建实物端初现企稳，消费延续“服务稳、商品弱”，地产调整延续但投资端下行趋缓。"
  },
  {
    "id": "wscn:3781781",
    "domain": "股票",
    "title": "10年期美债收益率破5%之际，日债收益率也失守3%，全球债市压力骤增！",
    "url": "https://wallstreetcn.com/articles/3781781",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T07:41:11+00:00",
    "summary": "全球债市拉响警报，美债收益率破5%创07年新高，日债刷新30年高位。油价飙升、通胀高企与巨额债务三重施压引爆抛售。机构警告：5%绝非终点，6%已入视野！本周美日央行决议在即，更猛烈的资产风暴或刚开始。"
  },
  {
    "id": "wscn:3781784",
    "domain": "股票",
    "title": "AI交易失速！高盛警告动量交易出现5年来最大分化，资金从芯片转向软件",
    "url": "https://wallstreetcn.com/articles/3781784",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T07:35:25+00:00",
    "summary": "高盛警示，AI交易正面临结构性考验，3个月与12个月动量表现背离创五年极值，AI指数较高点回撤近45%。与此同时，资金正从半导体转向软件，推动动量因子加速分化。高盛认为，若这一轮动持续，AI与动量之间长期高度相关的关系可能逐步松动。"
  },
  {
    "id": "wscn:3781780",
    "domain": "股票",
    "title": "字节AI办公大重组：豆包、飞书、火山引擎合三为一，AI办公大战正式打响",
    "url": "https://wallstreetcn.com/articles/3781780",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T07:03:41+00:00",
    "summary": "梁汝波表示，将豆包、飞书、火山引擎整合为一体化企业智能平台，Agent、模型、协作三位一体是核心逻辑。飞书ARR增速创历史新高，8.0版本开放接口从247个激增至767个。将Agent升级为拥有独立身份的“团队成员”深度融入协作。字节正加速抢夺企业级AI市场红利。"
  },
  {
    "id": "wscn:3781779",
    "domain": "股票",
    "title": "全球债市遭遇\"完美风暴\"！10年期美债收益率破5%创2007年来新高，日韩股市集体下跌，布油价再涨近2%",
    "url": "https://wallstreetcn.com/articles/3781779",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T05:59:47+00:00",
    "summary": "美债收益率突破5%背后，是油价飙升、政府债务扩张与AI融资热潮三重压力叠加的结果。摩根大通警告，收益率若升至5.25%，股市将\"明显消化不良\"。市场目光锁定美联储周三决议，加息概率已超90%，分析师预计10年期收益率或进一步冲向5.5%。"
  },
  {
    "id": "wscn:3781778",
    "domain": "股票",
    "title": "美联储本周加息概率92%、10年期美债收益率破5%，为何没能压垮黄金？",
    "url": "https://wallstreetcn.com/articles/3781778",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T05:43:34+00:00",
    "summary": "加息预期推高无风险利率、美元走强以及油价上涨共同对黄金价格构成短线压力，但地缘政治风险带来的避险需求和长期结构性买盘形成了有效对冲，令金价在关键位置维持韧性。OCBC上调黄金预测，预计金价到2026年12月将达到每盎司4600美元。"
  },
  {
    "id": "wscn:3781766",
    "domain": "股票",
    "title": "科创50半日涨近2%，风电、半导体集体大涨，存储芯片拉升，恒科指盘中涨1%，科网股集体反弹",
    "url": "https://wallstreetcn.com/articles/3781766",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:04:41+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3900股飘绿，上午半天成交1.07万亿。沪深两市半日成交额1.06万亿，较上个交易日缩量475亿。板块方面，“易中天”、宁德时代乏力，抑制创业板指表现。金融、餐饮旅游、农业、零售、房地产板块调整。AI硬件侧逐渐回暖，覆铜板、电子布、存储板块较为突出。"
  },
  {
    "id": "wscn:3781552",
    "domain": "股票",
    "title": "SEMICON TW2026：AI基建产业链的瓶颈与焦虑，在哪里？",
    "url": "https://wallstreetcn.com/premium/articles/3781552?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T03:48:44+00:00",
    "summary": "当资本开支不再是约束，AI 基建的四道硬墙成为真正的咽喉。"
  },
  {
    "id": "wscn:3781777",
    "domain": "股票",
    "title": "高盛对冲基金主管：“零日期权”压制美股波动，科技和能源仍是最佳选择",
    "url": "https://wallstreetcn.com/articles/3781777",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T03:34:29+00:00",
    "summary": "标普500已连续27个交易日日内波动低于1%，创疫情以来最长低波动纪录。高盛警告，这场\"平静\"背后是零日期权策略强行锁住市场的结果，一旦催化剂出现，压缩的波动能量将集中释放。与此同时，9月加息预期升温、情绪降至年内低点、财政可持续性风险高悬——这锅正在加热的水，还要沸腾多久？"
  },
  {
    "id": "wscn:3781776",
    "domain": "股票",
    "title": "融资结构正在重塑",
    "url": "https://wallstreetcn.com/articles/3781776",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T03:24:04+00:00",
    "summary": "招商证券认为，8月金融数据呈现总量放缓、结构重塑特征。社融与贷款增速继续回落，居民及企业信贷偏弱，实体扩表意愿尚未修复。但企业债券与股票融资持续多增，直接融资占比已超社融五成，融资体系多元化趋势强化。未来评估金融对实体支持力度，需更多关注广义社会融资及结构变化，债券与股权融资重要性有望进一步提升。"
  },
  {
    "id": "wscn:3781769",
    "domain": "股票",
    "title": "知名PE合伙人斯坦福授课：AI 时代的钱到底流向了哪里？",
    "url": "https://wallstreetcn.com/articles/3781769",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T03:19:15+00:00",
    "summary": "Apoorv Agrawal指出，当前AI产业呈现与互联网时代截然不同的“倒三角”盈利结构，约3000亿美元的生态收入中75%流向了高毛利（约75%）的半导体层，而应用层因高昂的算力边际成本面临盈利难题。为扭转目前单用户仅10美元的低ARPU现状，他断言ChatGPT等AI应用进军广告领域将是今年行业的重大突破口。"
  },
  {
    "id": "wscn:3781773",
    "domain": "股票",
    "title": "关掉“古法研究型”后，他用AI Agent做了一家“AI时代对冲基金”",
    "url": "https://wallstreetcn.com/articles/3781773",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T03:16:09+00:00",
    "summary": "一名基金经理、四个AI员工、年运营成本从500万美元压缩至4万美元——对冲基金Bracket22正在进行一场激进的组织实验。成本降了99%，生产率声称提升10倍，但最关键的收益数字至今缺席。这或许是AI时代最极限的一次投研压力测试：流水线可以被复制，Alpha能否被复制，只有市场能给答案。"
  },
  {
    "id": "wscn:3781771",
    "domain": "股票",
    "title": "“新美联储通讯社”：沃什加息“没有退路”，特朗普“信任”面临考验",
    "url": "https://wallstreetcn.com/articles/3781771",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T03:02:42+00:00",
    "summary": "Nick Timiraos认为，8月CPI超预期后美联储本周加息的概率已飙升，而沃什对通胀的强硬表态令自己几乎“没有退路”。在选举前七周加息，沃什加息与否将直接检验特朗普对他的“信任”能维持多久。此前，沃什用“少说话、避免挑衅”的战术维持了白宫与美联储的平衡，这次会议后沉默将不再是护盾。"
  },
  {
    "id": "wscn:3781760",
    "domain": "股票",
    "title": "Anthropic又发文：AI时代的经济会是什么样子？",
    "url": "https://wallstreetcn.com/articles/3781760",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T03:01:16+00:00",
    "summary": "Anthropic经济学团队发布AI经济情景模型，围绕三种剧本展开：温和渐进增长、GDP翻倍的重大变革、年增15%但知识工作者大量失业的极端情景。模型将工作视为\"任务包\"，分析AI对各类任务的增强与替代效应。Anthropic强调，2030年的经济图景并非定局，关键在于如何确保AI红利广泛共享。"
  },
  {
    "id": "wscn:3781772",
    "domain": "股票",
    "title": "Henry Jacques（亨利·雅克）蒙田大道旗舰  店之巡回雅集抵达上海",
    "url": "https://wallstreetcn.com/articles/3781772",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T02:51:50+00:00",
    "summary": "Henry Jacques（亨利 ·雅克）上海首家限时香氛空间 La Maison Éphémère 登陆恒隆广场，自2026 年 8 月 30 日至 2027 年 1 月 14 日"
  },
  {
    "id": "wscn:3781758",
    "domain": "股票",
    "title": "现房时代楼市纪实",
    "url": "https://wallstreetcn.com/articles/3781758",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T02:45:33+00:00",
    "summary": "新政出台首周，13个重点城市新房交易总体高于去年同期，一线城市成交量全线飘红，深圳地块溢价125%成交。但土地市场冷热分化、购房者犹豫观望，终端需求不足依然存在。制度切换不会自动消化旧债，转型阵痛难以回避。"
  },
  {
    "id": "wscn:3781770",
    "domain": "股票",
    "title": "Henry Jacques （亨利·雅克）  为上海首座限时香氛空间  特别呈献专属香氛 L’Île de HJ（依兰屿）",
    "url": "https://wallstreetcn.com/articles/3781770",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T02:41:56+00:00",
    "summary": "L’Île de HJ（依兰屿）——首款上海专属香氛"
  },
  {
    "id": "wscn:3781764",
    "domain": "股票",
    "title": "中国8月社零同比增0.4%，通讯器材大涨27.3%，汽车下滑18.5%",
    "url": "https://wallstreetcn.com/articles/3781764",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T02:28:25+00:00",
    "summary": "8月社零同比增0.4%，环比下降0.13%，结构分化加剧：通讯器材暴增27.3%领跑全场，汽车下滑18.5%成最大拖累，金银珠宝、建材家具持续下跌。网上零售、服务消费、乡村市场零售增长是亮点，必需品与可选消费\"冰火两重天\"的格局仍在持续。"
  },
  {
    "id": "wscn:3781768",
    "domain": "股票",
    "title": "9 月加息在弦上，美元会开启新一轮涨势吗？",
    "url": "https://wallstreetcn.com/articles/3781768",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T02:19:05+00:00",
    "summary": "“买预期、卖事实”，美元能否持续上涨？核心在于点阵图释放的后续加息信号，想要美元指数有效突破并且站稳100，美联储必须通过点阵图释放持续加息周期的信号，而不是 “加一次就结束” 的单次加息。"
  },
  {
    "id": "hn:49672197",
    "domain": "股票",
    "title": "Larry Ellison to sell up to $7.5B worth of Oracle stock",
    "url": "https://www.ft.com/content/25b1abb0-790f-4315-9b0c-530d959a086f",
    "source": "potatobox",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-12T13:37:21+00:00",
    "summary": ""
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
    "id": "hn:49596033",
    "domain": "股票",
    "title": "Show HN: Forget Rigid Stock Screeners – A Universal Query API for Financial Data",
    "url": "https://financialdata.net/universal-query",
    "source": "_FDN_",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-07T09:24:17+00:00",
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
    "id": "hn:49593962",
    "domain": "股票",
    "title": "HPE Gives Oracle Right to Buy 4.2M Shares for 1 Cent Each",
    "url": "https://www.forbes.com/sites/antoniopequenoiv/2026/09/03/hewlett-packard-enterprise-gives-oracle-right-to-buy-205-million-in-stock-at-slashed-rate/",
    "source": "gurjeet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-07T04:38:32+00:00",
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
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 453,
    "published_at": "2026-09-13T18:03:09+00:00",
    "summary": ""
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
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 204,
    "published_at": "2026-09-14T21:05:22+00:00",
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
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 111,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602582",
    "domain": "金融",
    "title": "A Tesla ran a stop sign and killed a man, Full Self-Driving/Autopilot was on",
    "url": "https://electrek.co/2026/09/07/tesla-driver-assist-stop-sign-buena-vista/",
    "source": "FabHK",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-09-07T20:21:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49601846",
    "domain": "金融",
    "title": "Tesla killing Solar Roof is leaving installers with six-figure losses",
    "url": "https://electrek.co/2026/09/01/tesla-solar-roof-exit-installers-losses/",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T19:08:47+00:00",
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
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-09-14T17:11:59+00:00",
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
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T14:49:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-09T13:16:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13402",
    "domain": "金融",
    "title": "Diffusion models for dynamic volatility surface generation and data-driven hedging",
    "url": "https://arxiv.org/abs/2609.13402",
    "source": "Yinbin Han, Jack Yuxiang Zhang, Manuel Torres, Fernando Acero, Renyuan Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.13402v1 Announce Type: new Abstract: We develop a diffusion-model framework for dynamic implied-volatility surface generation and evaluate its economic usefulness through data-driven hedgin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13597",
    "domain": "金融",
    "title": "Same Book, Different Fills: Partial Identification of FIFO Execution from Aggregate Order Books",
    "url": "https://arxiv.org/abs/2609.13597",
    "source": "Riya Danait, Yuliana Zamora, Ioana Boier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.13597v1 Announce Type: new Abstract: Price-level limit order book (L2) data reveal aggregate liquidity but not the ordered queue required by price--time priority. Passive-execution backtest"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13713",
    "domain": "金融",
    "title": "Cross-sectoral emission interdependencies of waste management",
    "url": "https://arxiv.org/abs/2609.13713",
    "source": "Nikolaos Kalyviotis, Georgina Calypso Kalogerakis, Georgios Kolliopoulos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.13713v1 Announce Type: new Abstract: This study examines emission interdependencies within the waste sector and between waste and other economic domains, energy, transport, water, and commu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13715",
    "domain": "金融",
    "title": "Event-Time Order-Flow Memory, Operational-Time Impact, and Subordinated Market Observables",
    "url": "https://arxiv.org/abs/2609.13715",
    "source": "Christopher Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.13715v1 Announce Type: new Abstract: We consider two canonical market-microstructure regularities: the long-memory of trade signs and the square-root law of meta-order impact. The point is "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13961",
    "domain": "金融",
    "title": "Yet another asymptotic formula for implied volatility",
    "url": "https://arxiv.org/abs/2609.13961",
    "source": "Masaaki Fukasawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.13961v1 Announce Type: new Abstract: We derive a first-order representation of Black-Scholes implied variance in a continuous local martingale model. Total implied variance is the condition"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14029",
    "domain": "金融",
    "title": "Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance",
    "url": "https://arxiv.org/abs/2609.14029",
    "source": "David Reinhardt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14029v1 Announce Type: new Abstract: Special Markowitz (SM) regularises returns and covariance jointly, relative to a reference state (mu_ref, Sigma_ref). Each eigendirection of the whitene"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14212",
    "domain": "金融",
    "title": "Gaussian Normalized Coordinates and Risk-Neutral CDF Deformations",
    "url": "https://arxiv.org/abs/2609.14212",
    "source": "Jian Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14212v1 Announce Type: new Abstract: Normalized implied-volatility coordinates reveal no-arbitrage structure that is less transparent in strike space. This paper centers on a single quantit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14487",
    "domain": "金融",
    "title": "Equilibrium Transition and Cartel Formation: A Structural Analysis of Chile's Pharmacy Cartel",
    "url": "https://arxiv.org/abs/2609.14487",
    "source": "Yu (Jasmine), Hao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14487v1 Announce Type: new Abstract: This paper studies how Chile's three largest pharmacy chains moved from the price war to collusion, using court-record daily prices and a structural mod"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14576",
    "domain": "金融",
    "title": "Towards foundation models for insurance risk modelling",
    "url": "https://arxiv.org/abs/2609.14576",
    "source": "Christopher Blier-Wong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14576v1 Announce Type: new Abstract: Claim narratives, images and sensor data contain information about insured risks that is difficult to use through existing actuarial models. Foundation "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14750",
    "domain": "金融",
    "title": "Redistributive Policies for the Times of Transformative AI",
    "url": "https://arxiv.org/abs/2609.14750",
    "source": "Jakub Growiec, Klaus Prettner, Maciej Szkr\\'obka",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14750v1 Announce Type: new Abstract: After the arrival of transformative artificial intelligence (TAI), broad-based automation is expected to decrease the labor share and increase income an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14859",
    "domain": "金融",
    "title": "Gate Design and Stage-Dependent Incentives in Retail Proprietary-Trading Evaluations: Why Passing Is Not Standalone Evidence of Skill, and Why the Product Fails to Pay Under Measured Trading Constrain",
    "url": "https://arxiv.org/abs/2609.14859",
    "source": "Nicholas Hall",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14859v1 Announce Type: new Abstract: Retail proprietary-trading firms sell a two-stage product: a paid evaluation that must reach a profit target before breaching a trailing drawdown, then "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15306",
    "domain": "金融",
    "title": "The skew Brownian motion should not be used as a risk-neutral returns process: a well-posed skew-normal alternative",
    "url": "https://arxiv.org/abs/2609.15306",
    "source": "Lorenzo Torricelli, Michele Bufalo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15306v1 Announce Type: new Abstract: Return models for risk-neutral financial valuation based on skew Brownian motions (SBMs) have been introduced about twenty years ago, and have recently "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15368",
    "domain": "金融",
    "title": "Resolution Is Not Settlement, Part I: Oracle Adjudication and Semantic Governance on Polymarket",
    "url": "https://arxiv.org/abs/2609.15368",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15368v1 Announce Type: new Abstract: Prediction-market resolution is often reduced to a terminal outcome and one timestamp. That representation is inadequate for leveraged event claims beca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15373",
    "domain": "金融",
    "title": "Resolution Is Not Settlement, Part II: Protocol Finality and Observed Redemption on Polymarket",
    "url": "https://arxiv.org/abs/2609.15373",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15373v1 Announce Type: new Abstract: An Oracle result is not yet a protocol payout, a redeemable position is not yet collateral in a holder's account, and a redemption event is not a comple"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15452",
    "domain": "金融",
    "title": "Endogenous supply-chain transformation via dynamically calibrated nonneutroelastic processing networks",
    "url": "https://arxiv.org/abs/2609.15452",
    "source": "Satoshi Nakano, Kazuhiko Nishimura",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15452v1 Announce Type: new Abstract: Understanding how supply chains endogenously transform requires a parametric model of processing networks with non-neutral substitution elasticities. Wh"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15741",
    "domain": "金融",
    "title": "Quantifying the 2027 Solvency II Risk Margin Reform",
    "url": "https://arxiv.org/abs/2609.15741",
    "source": "Said Khalil (TREE, INSEA), Fatima Zahrae Chaayra (INSEA)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15741v1 Announce Type: new Abstract: The 2027 Solvency II reform recalibrates the Risk Margin by reducing the prescribed cost-of-capital rate from 6% to 4.75% and introducing a time-depende"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15797",
    "domain": "金融",
    "title": "A prelude to the theory of Real-World Asset (RWA) Tokenization",
    "url": "https://arxiv.org/abs/2609.15797",
    "source": "Wenpin Tang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15797v1 Announce Type: new Abstract: We provide an introduction to real-world asset (RWA) tokenization, and develop two economic models connecting this emerging market to classical financia"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15802",
    "domain": "金融",
    "title": "The Economics of Recursive Self-Improvement",
    "url": "https://arxiv.org/abs/2609.15802",
    "source": "Tom Cunningham, Lukas Althoff, Basil Halperin, Brian Jabarian, Andrew Koh, Arjun Ramani, Phil Trammell, Parker Whitfill, Cheryl Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15802v1 Announce Type: new Abstract: We model the economics of recursive self-improvement (RSI) and assess its plausibility and impacts. First, we build a sequence of increasingly rich mode"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.13825",
    "domain": "金融",
    "title": "ViperQ: Order Flow Pattern Recognition via Auction Market Theory for Reinforcement Learning Trading",
    "url": "https://arxiv.org/abs/2609.13825",
    "source": "Asser Moustafa, Rares-Mihail Neagu, Jugal Kalita",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.13825v1 Announce Type: cross Abstract: Reinforcement learning trading systems published in the academic literature overwhelmingly rely on price-aggregate state representations (OHLCV bars) "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14205",
    "domain": "金融",
    "title": "CAST: A Cross-Asset State-Space Trading System for Drawdown Control in Stock Markets",
    "url": "https://arxiv.org/abs/2609.14205",
    "source": "Yu Peng, Matloob Khushi, Josiah Poon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14205v1 Announce Type: cross Abstract: Managing drawdown, the peak-to-trough decline in an investment portfolio's value, is a precondition for long-term survival in practical investment man"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14267",
    "domain": "金融",
    "title": "Public Opinion as an Option: Leveraging Prediction Markets to Hedge Exposure to Spot Crypto Volatility",
    "url": "https://arxiv.org/abs/2609.14267",
    "source": "Prashanth Bhaskara, Aadit Jerfy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14267v1 Announce Type: cross Abstract: This paper proposes an investment strategy through resource allocation into Kalshi Crypto Event Contracts in order to effectively hedge exposure to sp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14323",
    "domain": "金融",
    "title": "AI Assisted Workflow Optimization and Automation",
    "url": "https://arxiv.org/abs/2609.14323",
    "source": "Zhen Zhong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14323v1 Announce Type: cross Abstract: Against the backdrop of digital transformation and stricter regulation, enterprise compliance work demands higher efficiency and accuracy. The auxilia"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14733",
    "domain": "金融",
    "title": "WaVeFuse: Regime-Adaptive Equity Index Forecasting via Channel-Wise Wavelet Denoising and Vertical Attention Fusion",
    "url": "https://arxiv.org/abs/2609.14733",
    "source": "Aashish Bohra, Vivek Vijay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14733v1 Announce Type: cross Abstract: Hybrid Deep Learning for equity index forecasting is limited by three problems: propagation of OHLCV noise into derived technical indicators (TIs), ch"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14767",
    "domain": "金融",
    "title": "Loop-Back Authority in LLM Agent Teams: A Paired Experiment on Flat and Hierarchical Coordination",
    "url": "https://arxiv.org/abs/2609.14767",
    "source": "Burak Agachan, Max van Duijn, Amirhossein Zohrehvand",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.14767v1 Announce Type: cross Abstract: Hierarchical orchestration, in which a Manager agent reviews worker output and can send it back for revision, is the default coordination pattern in p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15319",
    "domain": "金融",
    "title": "Clean Scores, Buried Evidence, and Confident Wrong: A Receipt-Based Audit of Frontier Agentic QA",
    "url": "https://arxiv.org/abs/2609.15319",
    "source": "Luis M. S\\'anchez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15319v1 Announce Type: cross Abstract: Frontier models score well on shallow document/chart reading tasks. In a controlled data-room audit, moving evidence into buried conditions reduced ac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15744",
    "domain": "金融",
    "title": "Design of a Deep Learning Credit Risk Early Warning System Integrating Multi-source Heterogeneous Data",
    "url": "https://arxiv.org/abs/2609.15744",
    "source": "LiYang Wang (Washington University in St. Louis), Zhen Zhong (Georgetown University), Zhen Tian (University of Glasgow), Keyu Chen (Wuyi University), Keyu Chen (Wuyi University)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15744v1 Announce Type: cross Abstract: Advancements in data fusion and real-time analytics technologies have opened new avenues for addressing complex domain challenges. Financial risk earl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15755",
    "domain": "金融",
    "title": "Storage-Based Strategic Manipulation of Constraint-Binding Patterns in Power Networks",
    "url": "https://arxiv.org/abs/2609.15755",
    "source": "Mehdi Davoudi, Minghao Mou, Junjie Qin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15755v1 Announce Type: cross Abstract: This paper studies the strategic market participation of a monopolistic energy storage aggregator (ESA) in a day-ahead electricity market. The ESA coo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15901",
    "domain": "金融",
    "title": "Strategic Index Reconstitution: Differential Games, Closed-Loop Equilibria and Mean-Field Dynamics",
    "url": "https://arxiv.org/abs/2609.15901",
    "source": "Lukas-Benedikt Fiechtner, Jose Blanchet",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2609.15901v1 Announce Type: cross Abstract: We study strategic trading around index reconstitution in a continuous-time, multiasset game with transient cross-asset price impact and heterogeneous"
  },
  {
    "id": "rss:https://arxiv.org/abs/2006.15988",
    "domain": "金融",
    "title": "Seeing Through Color Blindness: Social Networks as a Mechanism for Discrimination",
    "url": "https://arxiv.org/abs/2006.15988",
    "source": "Chika O. Okafor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2006.15988v3 Announce Type: replace Abstract: I study labor markets in which firms both hire via referrals and are race blind or color-blind. I develop an employment model showing that despite i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2210.15946",
    "domain": "金融",
    "title": "Local Media and the Shaping of Social Norms: Evidence from the Ebola outbreak",
    "url": "https://arxiv.org/abs/2210.15946",
    "source": "Ada Gonzalez-Torres",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-15T04:00:00+00:00",
    "summary": "arXiv:2210.15946v5 Announce Type: replace Abstract: Media's influence on norms and behavior is widely recognized. Less is known about the role played by media being local. I examine this in a high-sta"
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-09-08T16:54:03+00:00",
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
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-09-04T13:15:24+00:00",
    "summary": ""
  }
]
```
