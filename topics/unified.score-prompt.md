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

- 今日日期：`2026-08-04`
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
  "date": "2026-08-04",
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
    "points": 1658249,
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
    "points": 1552927,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1308274,
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
    "points": 1039797,
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
    "points": 999661,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 591121,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 474578,
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
    "points": 432786,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 406587,
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
    "points": 220360,
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
    "points": 205548,
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
    "points": 178435,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 157962,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 135129,
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
    "points": 117929,
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
    "points": 92940,
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
    "points": 89813,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74000,
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
    "points": 53582,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 48247,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47549,
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
    "points": 45157,
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
    "points": 39960,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34013,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 31248,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 28355,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25961,
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
    "points": 22681,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1MPMd64EiD",
    "domain": "AI",
    "title": "我Vibe Coding做的游戏，上架Steam了【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117031449925140",
    "source": "Nenly同学",
    "platform": "bilibili",
    "points": 20430,
    "published_at": "2026-08-03T11:57:47+00:00",
    "summary": "三个月前，我对游戏开发一无所知，一行代码都不会写，也没摸过游戏引擎。\n现在，我靠VibeCoding做的游戏已经上架 Steam 了。\n\n游戏名：《群侠传：幸存者》\n抢先体验期间完全免费"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 19896,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 18899,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "iwenwikii",
    "platform": "bilibili",
    "points": 18099,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 17914,
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
    "points": 17668,
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
    "points": 17611,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 17212,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 16510,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1g33j6FEv4",
    "domain": "AI",
    "title": "震撼首发Claude.最新白嫖20X教程！！！",
    "url": "http://www.bilibili.com/video/av116984993810941",
    "source": "千夜Qivq",
    "platform": "bilibili",
    "points": 13350,
    "published_at": "2026-07-26T07:06:50+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 13294,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 12417,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10905,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 9349,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9278,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8845,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1mtGK6hEKC",
    "domain": "AI",
    "title": "Deepseek V4 Flash最新测评！Claude Code版！",
    "url": "http://www.bilibili.com/video/av117015578676037",
    "source": "AI产品狙击手",
    "platform": "bilibili",
    "points": 8158,
    "published_at": "2026-07-31T16:41:51+00:00",
    "summary": "上期完成 DeepSeek V4 Flash 在 Codex 平台测评，本期统一拉满 High 思考深度接入 Claude Code 复测，用全套标准化用例横向对比模型真实表现，基础指令、24 点运算、密码锁逻辑推理全部答对，仅十条顺序句子存在单句通顺度瑕疵；代码生成环节暴露统一痛点，所有大型开发任务耗时动辄数十分钟，判断是新模型上线调用高峰算力拥堵导致，自制桌面操作系统成品完整性不及 Codex"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8162,
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
    "points": 8120,
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
    "points": 7515,
    "published_at": "2025-07-04T10:13:51+00:00",
    "summary": "更新过程中遇到xiaozhi-server无法启动的问题，是因为最新的配置有更新，视频中有展示如何解决。对大家有帮助的话请关注up主~"
  },
  {
    "id": "bvid:BV1gQKf6NEGy",
    "domain": "AI",
    "title": "【Cursor接入第三方api完整教程】免费工具对接，轻松解决cursor限制，超详细超简单，新手小白也能看懂",
    "url": "http://www.bilibili.com/video/av116838746954504",
    "source": "AI续航站_",
    "platform": "bilibili",
    "points": 7251,
    "published_at": "2026-06-30T11:10:15+00:00",
    "summary": "大家还有什么不清楚的地方，有什么想了解的问题，都可以在评论区提出来哦。私信再附上一份详细教学指南（也可到本人主页查看）。制作不易还请大家一键三连+关注，非常感谢🌹🌹🌹"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 7226,
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
    "points": 113,
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
    "id": "rss:https://www.eetimes.com/renesas-tackles-memory-bottleneck-with-mrdimm-update/",
    "domain": "AI 算力 / 半导体",
    "title": "Renesas Tackles Memory Bottleneck with MRDIMM Update",
    "url": "https://www.eetimes.com/renesas-tackles-memory-bottleneck-with-mrdimm-update/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T19:00:00+00:00",
    "summary": "Renesas’s Gen 3 DDR5 MRDIMM attacks AI’s memory choke point with 16,000 MT/s bandwidth and no platform overhaul. The post Renesas Tackles Memory Bottleneck with MRDIMM Update appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/video-interview-chipagents-ceo-on-latest-funding-for-agentic-ai-in-eda/",
    "domain": "AI 算力 / 半导体",
    "title": "Video Interview: ChipAgents CEO on Latest Funding for Agentic AI in EDA",
    "url": "https://www.eetimes.com/video-interview-chipagents-ceo-on-latest-funding-for-agentic-ai-in-eda/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T14:07:19+00:00",
    "summary": "ChipAgents raises $60M as EDA’s AI gold rush heats up, pitching autonomous chip-design agents over tired copilots. The post Video Interview: ChipAgents CEO on Latest Funding for Agentic AI in EDA appe"
  },
  {
    "id": "rss:https://www.eetimes.com/nxp-eying-ambarella-is-it-about-automotive-or-edge-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "NXP Eying Ambarella: Is It About Automotive or Edge AI?",
    "url": "https://www.eetimes.com/nxp-eying-ambarella-is-it-about-automotive-or-edge-ai/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T08:24:34+00:00",
    "summary": "Ambarella has quietly transformed its automotive computer-vision technology to serve edge AI applications. The post NXP Eying Ambarella: Is It About Automotive or Edge AI? appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/new-micron-lawsuit-reignites-fight-over-new-york-fab-complaint-alleges-forever-chemicals-will-flow-into-oneida-river",
    "domain": "AI 算力 / 半导体",
    "title": "New Micron lawsuit reignites fight over New York fab — complaint alleges 'forever chemicals' will flow into Oneida River",
    "url": "https://www.tomshardware.com/pc-components/dram/new-micron-lawsuit-reignites-fight-over-new-york-fab-complaint-alleges-forever-chemicals-will-flow-into-oneida-river",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T18:04:36+00:00",
    "summary": "Micron's New York manufacturing facility is back in the crosshairs of another environmental lawsuit, claiming its wastewater and air permits should be nullified."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/in-a-troubling-sign-nvidia-rtx-50-series-prices-jump-up-to-30-percent-in-south-korea-tsmc-wafer-hikes-and-usd20-gddr7-modules-push-rtx-5090-past-usd5-100",
    "domain": "AI 算力 / 半导体",
    "title": "In a troubling sign, Nvidia RTX 50 series prices jump up to 30% in South Korea — TSMC wafer hikes and $20 GDDR7 modules push RTX 5090 past $5,100",
    "url": "https://www.tomshardware.com/pc-components/gpus/in-a-troubling-sign-nvidia-rtx-50-series-prices-jump-up-to-30-percent-in-south-korea-tsmc-wafer-hikes-and-usd20-gddr7-modules-push-rtx-5090-past-usd5-100",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T16:39:36+00:00",
    "summary": "The latest round of price increases affects the entire RTX 50 lineup, with premium models bearing the brunt of rising production costs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-companies-are-now-racing-to-the-bottom-crashing-token-prices-and-competitive-models-push-companies-to-cut-costs",
    "domain": "AI 算力 / 半导体",
    "title": "AI companies are now racing to the bottom — crashing token prices and competitive models push companies to cut costs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-companies-are-now-racing-to-the-bottom-crashing-token-prices-and-competitive-models-push-companies-to-cut-costs",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T16:26:15+00:00",
    "summary": "All major AI developers are cutting prices to compete with impressive new releases from China. But as they shave margins to remain competitive, the profits they'll need to fulfil investment confidence"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/drone-flyover-reveals-rapid-progress-at-elon-musks-atcf-chip-fab-texas-site-prepares-for-all-in-one-logic-memory-and-packaging-facility",
    "domain": "AI 算力 / 半导体",
    "title": "Drone flyover reveals rapid progress at Elon Musk’s new ATCF chip fab — Texas site prepares for all-in-one logic, memory, and packaging facility",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/drone-flyover-reveals-rapid-progress-at-elon-musks-atcf-chip-fab-texas-site-prepares-for-all-in-one-logic-memory-and-packaging-facility",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T15:50:56+00:00",
    "summary": "July drone flyovers of Elon Musk’s Advanced Technology Chip Fab in Texas appear to confirm progress has 'hit another gear.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/lexar-lists-32gb-ddr5-memory-with-homegrown-chinese-chips-3-999-yuan-usd592-price-undercuts-hopes-for-cheaper-cxmt-powered-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Lexar lists 32GB DDR5 memory with homegrown Chinese chips — 3,999 Yuan ($592) price undercuts hopes for cheaper CXMT-powered RAM",
    "url": "https://www.tomshardware.com/pc-components/ddr5/lexar-lists-32gb-ddr5-memory-with-homegrown-chinese-chips-3-999-yuan-usd592-price-undercuts-hopes-for-cheaper-cxmt-powered-ram",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T14:51:09+00:00",
    "summary": "Lexar's latest Thor RGB kit likely uses CXMT-made DRAM, but its pricing remains comparable to premium DDR5 memory from established brands."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-raises-european-xbox-prices-by-up-to-gbp200-rampocalypse-and-component-shortages-force-major-console-markups",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft raises European Xbox prices by up to £200 — RAMpocalypse and component shortages force major console markups",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-raises-european-xbox-prices-by-up-to-gbp200-rampocalypse-and-component-shortages-force-major-console-markups",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T14:49:11+00:00",
    "summary": "Xbox price increases across the UK and Europe have been revealed, with prices upped by as much as £170 or €200."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/asus-proart-pa32ucdmr-32-inch-4k-professional-oled-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ProArt PA32UCDMR 32-inch 4K professional OLED monitor review: Precision, speed, and flexibility",
    "url": "https://www.tomshardware.com/monitors/asus-proart-pa32ucdmr-32-inch-4k-professional-oled-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T13:00:00+00:00",
    "summary": "Asus delivers professional precision and premium gaming performance with the ProArt PA32UCDMR. It also comes with a slick calibrator and controller combination, and sports an all-metal chassis with el"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/gaming-on-the-4gb-radeon-rx-6500-xt-and-gtx-1650-super-in-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026 — upscaling makes low-end GPUs viable for esports and internet cafes",
    "url": "https://www.tomshardware.com/pc-components/gpus/gaming-on-the-4gb-radeon-rx-6500-xt-and-gtx-1650-super-in-2026",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T12:30:00+00:00",
    "summary": "Practically every graphics card introduced since 2022 has had at least 6GB or 8GB of VRAM, but AMD is bucking that trend in 2026 with the new RX 9050 4GB. We dusted off two older 4GB cards to see if t"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/ai-enthusiast-mods-bios-with-claude-code-ai-defeats-rsa-2048-signature-checks-and-unlocks-55-hidden-settings",
    "domain": "AI 算力 / 半导体",
    "title": "AI enthusiast unlocks and mods BIOS with Claude Code — AI defeats RSA-2048 signature checks and unlocks 55 hidden settings",
    "url": "https://www.tomshardware.com/laptops/ai-enthusiast-mods-bios-with-claude-code-ai-defeats-rsa-2048-signature-checks-and-unlocks-55-hidden-settings",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T11:55:17+00:00",
    "summary": "A Redditor recently unlocked their HP laptop BIOS using Claude Code."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/co-packaged-optics-cpo-foundry-roadmaps-breaking-down-tsmc-intel-samsung-and-globalfoundries-approach-to-next-generation-scale-up-connectivity",
    "domain": "AI 算力 / 半导体",
    "title": "Co-Packaged Optics (CPO) foundry roadmaps — breaking down TSMC, Intel, Samsung, and GlobalFoundries' approach to next-generation scale-up connectivity",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/co-packaged-optics-cpo-foundry-roadmaps-breaking-down-tsmc-intel-samsung-and-globalfoundries-approach-to-next-generation-scale-up-connectivity",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T11:45:50+00:00",
    "summary": "As AI systems outgrow copper interconnects, TSMC, Intel, Samsung Foundry, and GlobalFoundries are pursuing four distinctly different co-packaged optics strategies to bring optical connectivity closer "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/gpu-prices-for-current-gen-nvidia-and-amd-price-increases-why-have-the-prices-not-dropped-and-can-you-still-buy-a-cheap-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "GPU prices keep surging in 2026 — Lack of sale discounts and rising VRAM costs keep current-gen prices sky-high",
    "url": "https://www.tomshardware.com/pc-components/gpus/gpu-prices-for-current-gen-nvidia-and-amd-price-increases-why-have-the-prices-not-dropped-and-can-you-still-buy-a-cheap-gpu",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T11:30:00+00:00",
    "summary": "AI, tariffs, and greed have put pressure on PC builders wanting a new GPU. Can you still get a cheap GPU?"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/arm-yourself-with-a-hall-effect-controller-for-just-usd9-gamesirs-tegenaria-lite-pc-controller-is-50-percent-off-for-a-limited-time",
    "domain": "AI 算力 / 半导体",
    "title": "Arm yourself with a Hall Effect controller for just $9 — GameSir's Tegenaria Lite PC controller is 50% off for a limited time",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/arm-yourself-with-a-hall-effect-controller-for-just-usd9-gamesirs-tegenaria-lite-pc-controller-is-50-percent-off-for-a-limited-time",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T11:00:52+00:00",
    "summary": "Pick up a gaming controller complete with drift-free hall-effect thumbsticks for half the price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/worlds-smallest-gpu-silicon-passes-real-world-testing-240-000-transistor-tinygpu-v2-0-renders-3d-graphics-at-up-to-15-fps-while-v3-0-prepares-for-2026-release",
    "domain": "AI 算力 / 半导体",
    "title": "World’s smallest GPU silicon passes real-world testing — 240,000-transistor TinyGPU v2.0 renders 3D graphics at up to 15 FPS while v3.0 prepares for 2026 release",
    "url": "https://www.tomshardware.com/pc-components/gpus/worlds-smallest-gpu-silicon-passes-real-world-testing-240-000-transistor-tinygpu-v2-0-renders-3d-graphics-at-up-to-15-fps-while-v3-0-prepares-for-2026-release",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T11:00:00+00:00",
    "summary": "The TinyGPU v2.0 'standalone GPU' silicon works, and was demonstrated in a video after it came back from its Tiny Tapeout production run."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/hideo-kojima-unveils-a-death-stranding-2-themed-wireless-cd-player-limited-edition-device-costs-usd160-comes-with-bluetooth-5-3-and-exclusive-artwork",
    "domain": "AI 算力 / 半导体",
    "title": "Hideo Kojima unveils a Death Stranding 2-themed wireless CD player — Limited edition device costs ~$160, comes with Bluetooth 5.3 & exclusive artwork",
    "url": "https://www.tomshardware.com/peripherals/hideo-kojima-unveils-a-death-stranding-2-themed-wireless-cd-player-limited-edition-device-costs-usd160-comes-with-bluetooth-5-3-and-exclusive-artwork",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:30:00+00:00",
    "summary": "Kojima is partnering up with km5 to release a limited-edition version of the CP1 wireless CD player designed to resemble a BB Pod from Death Stranding 2. The nuclear orange aesthetic resembles classic"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-32gb-of-corsair-ddr5-for-an-effective-usd230-right-now-in-this-9950x3d-combo-deal-newegg-ram-bundle-ships-with-16-core-amd-x3d-chip-alongside-an-msi-x870e-board-and-a-free-240mm-cooler-for-usd1-308",
    "domain": "AI 算力 / 半导体",
    "title": "Grab 32GB of Corsair DDR5 for an effective $230 right now in this 9950X3D combo deal —Newegg RAM bundle ships with 16-core AMD X3D chip alongside an MSI X870E board and a free 240mm cooler for $1,308",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-32gb-of-corsair-ddr5-for-an-effective-usd230-right-now-in-this-9950x3d-combo-deal-newegg-ram-bundle-ships-with-16-core-amd-x3d-chip-alongside-an-msi-x870e-board-and-a-free-240mm-cooler-for-usd1-308",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:17:24+00:00",
    "summary": "This Newegg RAM bundles ships with the 16-core AMD Ryzen 9 9950X3D, an MSI MPG X870E keyboard, and 32GB of Corsair Vengeance DDR5 RAM for $1,308.99, making the effective RAM cost just $230."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/ten-years-later-the-iconic-gtx-1080-ti-still-holds-up-in-1080p-gaming-but-not-without-showing-its-age-redux-testing-highlights-the-wonders-of-11gb-vram-and-the-woes-of-time",
    "domain": "AI 算力 / 半导体",
    "title": "Ten years later, the iconic GTX 1080 Ti still holds up in 1080p gaming, but not without showing its age — Redux testing highlights the wonders of 11GB VRAM & the woes of time",
    "url": "https://www.tomshardware.com/pc-components/gpus/ten-years-later-the-iconic-gtx-1080-ti-still-holds-up-in-1080p-gaming-but-not-without-showing-its-age-redux-testing-highlights-the-wonders-of-11gb-vram-and-the-woes-of-time",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:00:00+00:00",
    "summary": "PC Games Hardware has retested the GTX 1080 Ti, along with its GP102 brethren, in a range of new games across multiple resolutions. The results reveal the obvious: the 1080 Ti is still a capable GPU a"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/grab-this-240-hz-qd-oled-gaming-monitor-at-just-usd300-gigabytes-27-inch-go27q24a-is-now-usd150-off-at-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 240 Hz QD-OLED gaming monitor at just $300 — Gigabyte's 27-inch GO27Q24A is now $150 off at Newegg",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/grab-this-240-hz-qd-oled-gaming-monitor-at-just-usd300-gigabytes-27-inch-go27q24a-is-now-usd150-off-at-newegg",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T16:16:41+00:00",
    "summary": "Gigabyte's GO27Q24A delivers a 240Hz QD-OLED panel, HDMI 2.1, and esports-focused features for just $299.99"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/errant-spacex-rocket-stage-set-to-smash-into-the-moon-at-5-400-mph-seven-times-the-speed-of-sound-nasa-and-south-korean-orbiters-prepare-to-track-3-ton-tnt-impact",
    "domain": "AI 算力 / 半导体",
    "title": "Errant SpaceX rocket stage set to smash into the moon at 5,400 mph, seven times the speed of sound — NASA and South Korean orbiters prepare to track 3-ton TNT impact",
    "url": "https://www.tomshardware.com/tech-industry/space/errant-spacex-rocket-stage-set-to-smash-into-the-moon-at-5-400-mph-seven-times-the-speed-of-sound-nasa-and-south-korean-orbiters-prepare-to-track-3-ton-tnt-impact",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T15:44:51+00:00",
    "summary": "A used SpaceX rocket segment used to deliver to lunar probes in 2025 is set to crash on the surface of the moon in the near future. This event will be monitored by two satellites as scientists and res"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/microsoft-paint-used-as-a-monitor-to-run-doom-at-up-to-35-fps-project-released-by-firms-azure-cto-runs-actual-doom-engine-and-loads-real-shareware-doom1-wad",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft Paint used as a 'monitor' to run Doom at up to 35 fps, project released by firm's Azure CTO — runs actual Doom engine and loads real shareware DOOM1.WAD",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/microsoft-paint-used-as-a-monitor-to-run-doom-at-up-to-35-fps-project-released-by-firms-azure-cto-runs-actual-doom-engine-and-loads-real-shareware-doom1-wad",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T14:14:24+00:00",
    "summary": "DoomPaint stands out from the Doom crowd as it has been developed by Microsoft's Azure CTO and because it runs using MS Paint as the viewport for in-game action."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/iran-suspected-of-conducting-cyberattacks-on-us-water-suppliers-in-45-municipalities-small-towns-mostly-targeted-with-utilities-switching-to-manual-control",
    "domain": "AI 算力 / 半导体",
    "title": "Iran suspected of conducting cyberattacks on US water suppliers in 45 municipalities — small towns mostly targeted, with utilities switching to manual control",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/iran-suspected-of-conducting-cyberattacks-on-us-water-suppliers-in-45-municipalities-small-towns-mostly-targeted-with-utilities-switching-to-manual-control",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T13:10:00+00:00",
    "summary": "Several US towns said that their water utilities have suffered from cyberattacks, which are suspected to have originated from Iran. While systems remain running, several have resorted to manual contro"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/commemorative-golden-doom-floppy-disks-go-up-for-pre-order-pair-of-limited-edition-dummy-imitation-gold-plating-disks-and-a-box-are-usd30-at-gamestop",
    "domain": "AI 算力 / 半导体",
    "title": "Commemorative golden Doom floppy disks go up for pre-order — pair of limited edition dummy ‘imitation gold plating’ disks and a box are $30 at GameStop",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/commemorative-golden-doom-floppy-disks-go-up-for-pre-order-pair-of-limited-edition-dummy-imitation-gold-plating-disks-and-a-box-are-usd30-at-gamestop",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T12:45:00+00:00",
    "summary": "GameStop has listed a purely ornamental Doom Floppy Disk Limited Edition Imitation Gold Plated Replica at $29.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's upcoming Zen 6 processors could fix microstutters and improve 1% lows in games — Next-gen CPUs tipped to feature per-core optimizations for thermal and power budgets",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T12:30:00+00:00",
    "summary": "A new report suggests AMD is cooking up a range of per-core optimizations for Zen 6 that might not seem huge on their own, but they could add up to make a world of difference in gaming performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850",
    "domain": "AI 算力 / 半导体",
    "title": "First open-source firmware for AM5 officially launches — Dasharo v0.9.0 brings Coreboot and openSIL to Zen 4 APUs on MSI B850",
    "url": "https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T12:10:00+00:00",
    "summary": "3mdeb has introduced a new open-source firmware for the MSI B850-P WiFi, marking the first time open-source firmware has been introduced to the AM5 platform."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/spacexai-says-it-will-remove-all-69-of-its-unpermitted-turbine-power-generators-but-expects-process-to-take-a-year-trailer-mounted-generators-to-be-replaced-by-1-2gw-power-plant",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceXAI says it will remove all 69 of its unpermitted turbine power generators, but expects process to take a year — trailer-mounted generators to be replaced by 1.2GW power plant",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/spacexai-says-it-will-remove-all-69-of-its-unpermitted-turbine-power-generators-but-expects-process-to-take-a-year-trailer-mounted-generators-to-be-replaced-by-1-2gw-power-plant",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T11:50:00+00:00",
    "summary": "These turbines have been the center of a lawsuit involving permits and pollution. While this is good news for the community, it will still take quite some time before they're fully removed from the pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/rtx-5060-ti-survives-car-crash-after-being-bent-in-half-short-pcb-saves-the-day-single-memory-chip-resolder-restore-full-performance",
    "domain": "AI 算力 / 半导体",
    "title": "RTX 5060 Ti survives car crash after being bent in half — short PCB saves the day, single memory chip resolder restore full performance",
    "url": "https://www.tomshardware.com/pc-components/gpus/rtx-5060-ti-survives-car-crash-after-being-bent-in-half-short-pcb-saves-the-day-single-memory-chip-resolder-restore-full-performance",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T11:30:00+00:00",
    "summary": "What happens when a graphics card gets in a car crash? If you're lucky, the damage is limited to just cosmetic scars that can go away over time with no serious damage under-the-hood."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/gem-mint-signed-1983-steve-jobs-business-card-opens-at-usd70-000-second-signed-card-from-that-era-after-usd180-000-record-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Gem Mint signed 1983 Steve Jobs business card opens at $70,000 — second signed card from that era after $180,000 record sale",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/gem-mint-signed-1983-steve-jobs-business-card-opens-at-usd70-000-second-signed-card-from-that-era-after-usd180-000-record-sale",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T11:00:00+00:00",
    "summary": "This rare business card is currently on RR Auction, with a previous example going for $180,000 just a couple of years ago. It's graded Gem Mint 10, meaning it's as perfect as it can get."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/prolific-team-fortress-2-collector-is-selling-his-in-game-case-arsenal-for-an-estimated-usd100-000-1-7-million-items-collected-over-10-years-are-enough-to-fund-a-house-purchase",
    "domain": "AI 算力 / 半导体",
    "title": "Prolific Team Fortress 2 collector is selling his in-game case arsenal for an estimated $100,000 — 1.7 million items collected over 10 years are enough to fund a house purchase",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/prolific-team-fortress-2-collector-is-selling-his-in-game-case-arsenal-for-an-estimated-usd100-000-1-7-million-items-collected-over-10-years-are-enough-to-fund-a-house-purchase",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T10:30:00+00:00",
    "summary": "One Team Fortress 2 player has amassed a collection of over 1.7 million cases from the game, and after nearly a decade of collecting, he’s selling the collection for an estimated $100,000."
  },
  {
    "id": "hn:49125140",
    "domain": "AI 算力 / 半导体",
    "title": "Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia",
    "url": "https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-31T16:21:11+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/humanoid-manipulation-at-the-edge-of-physical-interaction/",
    "domain": "AI 算力 / 半导体",
    "title": "Humanoid Manipulation at the Edge of Physical Interaction",
    "url": "https://www.eetimes.com/humanoid-manipulation-at-the-edge-of-physical-interaction/",
    "source": "Renesas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:00:00+00:00",
    "summary": "This white paper examines emerging humanoid robot architectures, focusing on how joints and dexterous hands are becoming intelligent, sensor-rich subsystems that require tightly integrated control, co"
  },
  {
    "id": "rss:https://www.eetimes.com/erp-statistics-insights-from-70-manufacturing-case-studies/",
    "domain": "AI 算力 / 半导体",
    "title": "ERP Statistics: Insights From 70 Manufacturing Case Studies",
    "url": "https://www.eetimes.com/erp-statistics-insights-from-70-manufacturing-case-studies/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T13:00:00+00:00",
    "summary": "We analyzed 70 customer case studies to better understand the ERP experiences of small manufacturers. Here’s what electronics manufacturers had to say. The post ERP Statistics: Insights From 70 Manufa"
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti Pushes Stacking Roadmap as AI Runs into Memory and Power Limits",
    "url": "https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:48:06+00:00",
    "summary": "AI’s memory wall is turning packaging into architecture as CEA-Leti bets on 3D stacking, chiplets, and cooler power. The post CEA-Leti Pushes Stacking Roadmap as AI Runs into Memory and Power Limits a"
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
    "id": "rss:https://www.tomshardware.com/tech-industry/dell-founder-shows-how-a-usd100-billion-empire-started-42-years-ago-ceo-says-this-one-page-changed-my-life",
    "domain": "AI 算力 / 半导体",
    "title": "Dell founder shows how a $100 billion empire started 42 years ago — CEO says ‘This one page changed my life’",
    "url": "https://www.tomshardware.com/tech-industry/dell-founder-shows-how-a-usd100-billion-empire-started-42-years-ago-ceo-says-this-one-page-changed-my-life",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T17:06:31+00:00",
    "summary": "Billionaire Michael Dell reminisced about the early days of his company, sharing an early quarterly earnings report that showed the then-startup making nearly $135,000 in just three months. Dell says "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/score-the-ultimate-amd-am4-starter-pack-with-a-six-core-cpu-and-16gb-ram-for-only-usd280-kickstart-your-next-pc-build-with-usd138-in-savings",
    "domain": "AI 算力 / 半导体",
    "title": "Score the ultimate AMD AM4 starter pack with a six-core CPU and 16GB RAM for only $280 — kickstart your next PC build with $138 in savings",
    "url": "https://www.tomshardware.com/pc-components/score-the-ultimate-amd-am4-starter-pack-with-a-six-core-cpu-and-16gb-ram-for-only-usd280-kickstart-your-next-pc-build-with-usd138-in-savings",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:09:27+00:00",
    "summary": "If you've been hesitating to upgrade to a modern platform because of the state of the PC hardware industry, this combo deal might be the one for you."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-vows-to-make-windows-11-fly-on-8gb-ram-amid-memory-shortage-optimizations-to-reduce-os-memory-footprint-have-begun",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft vows to make Windows 11 fly on 8GB RAM amid memory shortage — optimizations to reduce OS memory footprint have begun",
    "url": "https://www.tomshardware.com/software/windows/microsoft-vows-to-make-windows-11-fly-on-8gb-ram-amid-memory-shortage-optimizations-to-reduce-os-memory-footprint-have-begun",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:48:26+00:00",
    "summary": "While the company's minimum OS specifications officially say 4GB, most PC builders know that 16GB is the bare minimum for a smooth experience on Windows 11. However, the memory chip shortage and the r"
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
    "id": "hn:49075171",
    "domain": "AI 算力 / 半导体",
    "title": "Sam Altman says we are in the singularity: 'This is the moment'",
    "url": "https://www.businessinsider.com/sam-altman-openai-the-singularity-agi-prediction-anthropic-nvidia-2026-7",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-27T20:35:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48992221",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "speckx",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-21T13:40:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 619,
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
    "id": "rss:https://www.theverge.com/entertainment/974505/beast-of-reincarnation-review-ps5-xbox",
    "domain": "大厂 AI 动态",
    "title": "The studio behind Pokémon struggles to find its voice in Beast of Reincarnation",
    "url": "https://www.theverge.com/entertainment/974505/beast-of-reincarnation-review-ps5-xbox",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T00:00:00+00:00",
    "summary": "You have to imagine that the team at Game Freak is bursting with ideas. The studio puts out new mainline Pok&#233;mon adventures with a machinelike precision. But every so often it launches a curious "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/974778/google-health-fitbit-data-apple-health-syncing",
    "domain": "大厂 AI 动态",
    "title": "Your Fitbit data can now connect directly to Apple Health",
    "url": "https://www.theverge.com/gadgets/974778/google-health-fitbit-data-apple-health-syncing",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T21:24:23+00:00",
    "summary": "Google is rolling out an update that will finally allow you to connect your Fitbit workouts, steps, vitals, and other data to Apple Health, as reported earlier by 9to5Mac. With Google Health's 5.05 up"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/974583/samsungs-m80f-smart-monitor-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s discounted smart monitor is $349.99, its lowest price yet",
    "url": "https://www.theverge.com/gadgets/974583/samsungs-m80f-smart-monitor-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T21:13:38+00:00",
    "summary": "Samsung makes a variety of TVs and computer monitors, but if want both and you’re limited on space, you might want to consider the M80F. This capable 32-inch 4K panel combines features commonly found "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/974571/eu-ai-act-transparency-labels-rules-deepfakes",
    "domain": "大厂 AI 动态",
    "title": "Europe’s AI labeling and transparency rules are now in effect",
    "url": "https://www.theverge.com/ai-artificial-intelligence/974571/eu-ai-act-transparency-labels-rules-deepfakes",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T17:38:45+00:00",
    "summary": "The European Union has ushered in some additional rules that aim to make it easier for people to identify chatbots and AI deepfakes online. The new transparency obligations under the bloc's landmark A"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/974536/kindle-scribe-2022-refurbished-woot-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The first-gen Kindle Scribe is a big e-reader and digital notebook that’s $150 refurbished",
    "url": "https://www.theverge.com/gadgets/974536/kindle-scribe-2022-refurbished-woot-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T17:17:54+00:00",
    "summary": "The Kindle Scribe is worth considering if you’re heading back to school, as its large 10.2-inch screen can display textbooks and ebooks, or let you jot down handwritten notes during class. Now through"
  },
  {
    "id": "rss:https://www.theverge.com/games/974544/microsoft-xbox-360-games-pc-disc-digital-program",
    "domain": "大厂 AI 动态",
    "title": "Microsoft is bringing Xbox 360 games to PC",
    "url": "https://www.theverge.com/games/974544/microsoft-xbox-360-games-pc-disc-digital-program",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T16:31:35+00:00",
    "summary": "Building on its recently announced plans to bring original Xbox games to PC, Microsoft is also planning to let developers bring their Xbox 360 games to PC as well, according to a leaked document, seen"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/974387/bluesky-toni-schneider-interview-ai-atproto-atmosphere",
    "domain": "大厂 AI 动态",
    "title": "Bluesky’s new CEO wants a big tent, not a bubble",
    "url": "https://www.theverge.com/podcast/974387/bluesky-toni-schneider-interview-ai-atproto-atmosphere",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T15:00:00+00:00",
    "summary": "Today, I’m talking with Toni Schneider, who is the brand new CEO of the social platform Bluesky — he formally took over after a short stint as interim CEO. This is one of my favorite kinds of intervie"
  },
  {
    "id": "rss:https://www.theverge.com/games/974450/palworld-online-mobile-mmo",
    "domain": "大厂 AI 动态",
    "title": "Palworld’s expanding to mobile with a new MMORPG",
    "url": "https://www.theverge.com/games/974450/palworld-online-mobile-mmo",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T14:50:29+00:00",
    "summary": "After its 1.0 launch last month, Palworld is coming to iOS and Android with a new open-world MMORPG launching later this year, Polygon reports. Garena, the developer behind the new game, says in its a"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/974411/spider-man-the-odyssey-imax",
    "domain": "大厂 AI 动态",
    "title": "Spider-Man and The Odyssey are splitting up IMAX screens after a record-breaking weekend",
    "url": "https://www.theverge.com/entertainment/974411/spider-man-the-odyssey-imax",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T14:26:47+00:00",
    "summary": "Spider-Man: Brand New Day is joining The Odyssey in IMAX theaters after both movies led the biggest weekend in box office history. On Monday, IMAX announced that Spider-Man: Brand New Day will be avai"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/974391/samsung-nvme-ssd-2tb-steelseries-arctis-omni-pixel-10a-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s 2TB 9100 Pro SSD is actually somewhat reasonably priced",
    "url": "https://www.theverge.com/gadgets/974391/samsung-nvme-ssd-2tb-steelseries-arctis-omni-pixel-10a-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T14:16:13+00:00",
    "summary": "Next to buying RAM, finding a fast, high-capacity NVMe SSD at a reasonable price has been a challenge during RAMageddon. I don’t want to say it’s getting easier, but one of Samsung’s latest SSDs is ch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/after-killer-quarter-palantir-ceo-alex-karp-calls-ai-industry-marxist/",
    "domain": "大厂 AI 动态",
    "title": "After killer quarter, Palantir CEO Alex Karp calls AI industry ‘Marxist’",
    "url": "https://techcrunch.com/2026/08/03/after-killer-quarter-palantir-ceo-alex-karp-calls-ai-industry-marxist/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T23:19:50+00:00",
    "summary": "After a quarter that delivered $1 billion in profit, Palantir CEO Alex Karp on Monday once again warned that AI frontier labs are too untrustworthy for enterprises."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/snap-ceo-sidesteps-specs-pre-order-questions-on-q2-earnings-call/",
    "domain": "大厂 AI 动态",
    "title": "Snap CEO sidesteps Specs preorder questions on Q2 earnings call",
    "url": "https://techcrunch.com/2026/08/03/snap-ceo-sidesteps-specs-pre-order-questions-on-q2-earnings-call/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T22:10:58+00:00",
    "summary": "When asked about product-market fit, Spiegel said he believes mass-market consumer adoption won't occur until the end of the decade."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/aws-is-helping-vibe-coding-startup-superblocks-and-the-implications-are-big/",
    "domain": "大厂 AI 动态",
    "title": "AWS is helping vibe-coding startup Superblocks, and the implications are big",
    "url": "https://techcrunch.com/2026/08/03/aws-is-helping-vibe-coding-startup-superblocks-and-the-implications-are-big/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T20:00:00+00:00",
    "summary": "AWS now allows vibe-coding tool Superblocks to be embedded into the private clouds of AWS customers. It's another step toward decoupling apps from models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/whos-legally-to-blame-for-anthropic-and-openais-autonomous-ai-hacks-its-complicated/",
    "domain": "大厂 AI 动态",
    "title": "Who’s legally to blame for Anthropic and OpenAI’s autonomous AI hacks? It’s complicated",
    "url": "https://techcrunch.com/2026/08/03/whos-legally-to-blame-for-anthropic-and-openais-autonomous-ai-hacks-its-complicated/",
    "source": "Lorenzo Franceschi-Bicchierai, Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T19:45:35+00:00",
    "summary": "OpenAI and Anthropic admitted that their unreleased AI models escaped their sandboxes and hacked several companies in unprecedented cyberattacks. Who is legally to blame? Should prosecutors charge the"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/designarena-creators-raise-7-9-million-to-bring-taste-to-ai-models/",
    "domain": "大厂 AI 动态",
    "title": "Design Arena creators raise $7.9 million to bring taste to AI models",
    "url": "https://techcrunch.com/2026/08/03/designarena-creators-raise-7-9-million-to-bring-taste-to-ai-models/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T19:28:57+00:00",
    "summary": "Design Arena is used by 5.3 million people around the world, providing critical human evaluations to frontier labs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/influencers-draw-backlash-for-attending-openais-first-luxury-trip/",
    "domain": "大厂 AI 动态",
    "title": "Influencers draw backlash for attending OpenAI’s first luxury trip",
    "url": "https://techcrunch.com/2026/08/03/influencers-draw-backlash-for-attending-openais-first-luxury-trip/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T19:09:56+00:00",
    "summary": "OpenAI’s first-ever influencer brand trip is sparking online backlash as tensions over the use of AI continue."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/apple-challenges-uk-governments-latest-demand-for-icloud-backdoor-report/",
    "domain": "大厂 AI 动态",
    "title": "Apple challenges UK government’s latest demand for iCloud backdoor: report",
    "url": "https://techcrunch.com/2026/08/03/apple-challenges-uk-governments-latest-demand-for-icloud-backdoor-report/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T18:54:09+00:00",
    "summary": "Apple has appealed a new legal demand by the U.K. government, which critics say could threaten the privacy rights of users all over the world."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/apple-finally-fixed-siri-so-why-does-it-feel-anticlimactic/",
    "domain": "大厂 AI 动态",
    "title": "Apple finally fixed Siri. So why does it feel anticlimactic?",
    "url": "https://techcrunch.com/2026/08/03/apple-finally-fixed-siri-so-why-does-it-feel-anticlimactic/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T18:43:43+00:00",
    "summary": "Apple’s long-awaited AI overhaul finally makes Siri the assistant it was always supposed to be. Yet it arrives at a moment when simply being a capable AI assistant no longer feels revolutionary."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/outernet-turns-your-saved-posts-into-real-world-adventures/",
    "domain": "大厂 AI 动态",
    "title": "Outernet turns your saved posts into real-world adventures",
    "url": "https://techcrunch.com/2026/08/03/outernet-turns-your-saved-posts-into-real-world-adventures/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T18:00:24+00:00",
    "summary": "Founded by the creators of viral offline events like San Francisco’s citywide scavenger hunt Pursuit, Outernet's app helps users save places and events they discover online, then nudges them to actual"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/whatsapp-says-it-is-is-fixing-an-issue-that-disabled-several-accounts/",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp says it is fixing an issue that disabled several accounts",
    "url": "https://techcrunch.com/2026/08/03/whatsapp-says-it-is-is-fixing-an-issue-that-disabled-several-accounts/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T17:46:01+00:00",
    "summary": "Meta says it’s restoring access to WhatsApp accounts that were mistakenly flagged and placed “under review” after users reported being unexpectedly locked out of the messaging app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/sequoias-shaun-maguire-leads-1b-round-for-nuclear-startup-valar-atomics/",
    "domain": "大厂 AI 动态",
    "title": "Sequoia’s Shaun Maguire leads $1B round for nuclear startup Valar Atomics",
    "url": "https://techcrunch.com/2026/08/03/sequoias-shaun-maguire-leads-1b-round-for-nuclear-startup-valar-atomics/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T17:16:43+00:00",
    "summary": "Valar Atomics raised $1 billion at a $6 billion valuation after signing a development deal with Nvidia in June."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/base-power-raises-another-1b-to-save-the-grid-using-backyard-batteries/",
    "domain": "大厂 AI 动态",
    "title": "Base Power raises another $1B to save the grid using backyard batteries",
    "url": "https://techcrunch.com/2026/08/03/base-power-raises-another-1b-to-save-the-grid-using-backyard-batteries/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T16:46:57+00:00",
    "summary": "Base Power’s $1 billion round will help the startup ramp production of its home batteries."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/congresss-favorite-ai-tool-chatgpt/",
    "domain": "大厂 AI 动态",
    "title": "Congress’ favorite AI tool? ChatGPT",
    "url": "https://techcrunch.com/2026/08/03/congresss-favorite-ai-tool-chatgpt/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T16:40:55+00:00",
    "summary": "House spending records show OpenAI's ChatGPT dominates paid AI use on Capitol Hill, with congressional offices relying on the chatbot to draft memos, summarize legislation, and assist constituent comm"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/wispr-flow-is-preparing-to-launch-a-meeting-notetaker-updated-terms-suggest/",
    "domain": "大厂 AI 动态",
    "title": "Wispr Flow is preparing to launch a meeting notetaker, updated terms suggest",
    "url": "https://techcrunch.com/2026/08/03/wispr-flow-is-preparing-to-launch-a-meeting-notetaker-updated-terms-suggest/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T16:29:30+00:00",
    "summary": "Wispr Flow's new terms of service indicate it will introduce a notetaker that generates meeting summaries and action items."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/horizon3-hits-2-billion-valuation-with-250m-series-e-as-ai-threats-escalate/",
    "domain": "大厂 AI 动态",
    "title": "Horizon3 hits $2 billion valuation with $250M Series E as AI threats escalate",
    "url": "https://techcrunch.com/2026/08/03/horizon3-hits-2-billion-valuation-with-250m-series-e-as-ai-threats-escalate/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T12:50:46+00:00",
    "summary": "Cybersecurity startup Horizon3 raised $250 million at a $2 billion valuation as companies want continuous, AI-powered security validation instead of annual pen testing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/samsung-bans-smart-tv-apps-that-share-users-internet-connections-with-strangers/",
    "domain": "大厂 AI 动态",
    "title": "Samsung bans smart TV apps that share users’ internet connections with strangers",
    "url": "https://techcrunch.com/2026/08/03/samsung-bans-smart-tv-apps-that-share-users-internet-connections-with-strangers/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T12:10:41+00:00",
    "summary": "New security research offers a rare view inside residential proxy networks, which rely on apps that share a person's internet connection with someone else."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/03/a-marc-benioff-backed-startup-thinks-ai-can-solve-the-ai-deployment-problem/",
    "domain": "大厂 AI 动态",
    "title": "A Marc Benioff-backed startup thinks AI can solve the AI deployment problem",
    "url": "https://techcrunch.com/2026/08/03/a-marc-benioff-backed-startup-thinks-ai-can-solve-the-ai-deployment-problem/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:00:00+00:00",
    "summary": "June emerged from stealth today with a $20 million pre-seed round to make AI adoption simpler."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/02/the-global-memory-shortage-hits-the-macbook-air/",
    "domain": "大厂 AI 动态",
    "title": "The global memory shortage hits the MacBook Air",
    "url": "https://techcrunch.com/2026/08/02/the-global-memory-shortage-hits-the-macbook-air/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T21:33:59+00:00",
    "summary": "The global memory chip shortage appears to be affecting the availability of Apple’s most popular Mac."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/02/sam-altman-and-ais-decel-debate/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman and AI’s decel debate",
    "url": "https://techcrunch.com/2026/08/02/sam-altman-and-ais-decel-debate/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T20:54:22+00:00",
    "summary": "On the latest episode of Equity, we discuss why Sam Altman is calling on the industry to \"pace the rate of AI development.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/02/malaysia-is-reportedly-shutting-down-balaji-srinivasans-network-school/",
    "domain": "大厂 AI 动态",
    "title": "Malaysia is reportedly shutting down Balaji Srinivasan’s Network School",
    "url": "https://techcrunch.com/2026/08/02/malaysia-is-reportedly-shutting-down-balaji-srinivasans-network-school/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T17:05:07+00:00",
    "summary": "Let's see how this \"frontier community for techno-optimists\" is doing ..."
  },
  {
    "id": "rss:https://stratechery.com/2026/meta-earnings-metas-timing-problems-the-financial-tail/",
    "domain": "大厂 AI 动态",
    "title": "Meta Earnings, Meta’s Timing Problems, The Financial Tail",
    "url": "https://stratechery.com/2026/meta-earnings-metas-timing-problems-the-financial-tail/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:00:00+00:00",
    "summary": "Meta's earnings were a bit disappointing; future promises about AI products were more disconcerting."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/ukraines-drones-get-ai-upgrades-for-kamikaze-strikes-future-swarm-attacks/",
    "domain": "大厂 AI 动态",
    "title": "US company’s AI lets Ukraine’s cheap kamikaze drones track targets on their own",
    "url": "https://arstechnica.com/ai/2026/08/ukraines-drones-get-ai-upgrades-for-kamikaze-strikes-future-swarm-attacks/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T22:11:39+00:00",
    "summary": "$100 million deal gives 50,000 Ukrainian drones US-developed AI capabilities."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/research-roundup-6-cool-science-stories-we-almost-missed-5/",
    "domain": "大厂 AI 动态",
    "title": "Research roundup: 6 cool science stories we almost missed",
    "url": "https://arstechnica.com/science/2026/08/research-roundup-6-cool-science-stories-we-almost-missed-5/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T20:13:37+00:00",
    "summary": "Also: Cyborg diving suits for cockroaches, why sleepy sperm whales blow bubbles, Betelgeuse's companion star."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/lego-deploys-hubble-space-telescope-as-detailed-desktop-model/",
    "domain": "大厂 AI 动态",
    "title": "Lego deploys Hubble Space Telescope as detailed desktop model",
    "url": "https://arstechnica.com/space/2026/08/lego-deploys-hubble-space-telescope-as-detailed-desktop-model/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T19:21:16+00:00",
    "summary": "The orbiting observatory in minifigure scale."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/an-ai-supervised-remote-exam-went-so-badly-that-58000-students-must-retake-it/",
    "domain": "大厂 AI 动态",
    "title": "An AI-supervised remote exam went so badly that 58,000 students must retake it",
    "url": "https://arstechnica.com/culture/2026/08/an-ai-supervised-remote-exam-went-so-badly-that-58000-students-must-retake-it/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T19:00:50+00:00",
    "summary": "Top scores increased by 5x."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/2026-volkswagen-jetta-sport-the-cheap-car-isnt-completely-extinct-yet/",
    "domain": "大厂 AI 动态",
    "title": "2026 Volkswagen Jetta Sport: The cheap car isn't completely extinct yet",
    "url": "https://arstechnica.com/cars/2026/08/2026-volkswagen-jetta-sport-the-cheap-car-isnt-completely-extinct-yet/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T16:10:22+00:00",
    "summary": "At $25,305, you won't find many new cars for less. But you get what you pay for."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/spacex-is-set-to-acquire-130000-acres-of-marshland-in-southern-louisiana/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX is set to acquire 130,000 acres of marshland in southern Louisiana",
    "url": "https://arstechnica.com/space/2026/08/spacex-is-set-to-acquire-130000-acres-of-marshland-in-southern-louisiana/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T14:41:46+00:00",
    "summary": "A Louisiana launch site would offer several significant advantages."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/trump-wants-the-power-to-stop-the-public-from-suing-polluters/",
    "domain": "大厂 AI 动态",
    "title": "Trump wants the power to stop the public from suing polluters",
    "url": "https://arstechnica.com/tech-policy/2026/08/trump-wants-the-power-to-stop-the-public-from-suing-polluters/",
    "source": "Sarah J. Morath, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T13:33:56+00:00",
    "summary": "Trump's DOJ says citizens should no longer be able to enforce environmental laws."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/how-headlights-got-brighter-whiter-and-more-blinding-after-dark/",
    "domain": "大厂 AI 动态",
    "title": "How headlights got brighter, whiter, and more blinding after dark",
    "url": "https://arstechnica.com/cars/2026/08/how-headlights-got-brighter-whiter-and-more-blinding-after-dark/",
    "source": "Matthew MacConnell",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T11:00:11+00:00",
    "summary": "Automotive lights are better than they've ever been, but there's a trade-off."
  },
  {
    "id": "rss:https://www.producthunt.com/products/inventory",
    "domain": "大厂 AI 动态",
    "title": "Inventory",
    "url": "https://www.producthunt.com/products/inventory",
    "source": "Neil Shah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T10:51:43+00:00",
    "summary": "Search every AI Agent & IDE Conversation Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/qwen3",
    "domain": "大厂 AI 动态",
    "title": "Qwen3.8-Max",
    "url": "https://www.producthunt.com/products/qwen3",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T03:55:30+00:00",
    "summary": "Qwen’s most capable model for coding and cowork Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mascotai",
    "domain": "大厂 AI 动态",
    "title": "MascotAI",
    "url": "https://www.producthunt.com/products/mascotai",
    "source": "Tahiru Nasuru",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T06:19:32+00:00",
    "summary": "Animated SVG mascot studios for apps that need a personality Discussion | Link"
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
    "points": 155,
    "published_at": "2026-07-31T13:37:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-08-03T06:17:53+00:00",
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
    "id": "hn:49137024",
    "domain": "股票",
    "title": "Oil companies report sky-high profits thanks to wartime crude prices",
    "url": "https://www.npr.org/2026/07/31/nx-s1-5910660/big-oil-earnings-q2-2026",
    "source": "speckx",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-01T18:28:06+00:00",
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
    "id": "wscn:3778355",
    "domain": "股票",
    "title": "超级厄尔尼诺来袭：7000亿美元只是开始，更大冲击或在明年",
    "url": "https://wallstreetcn.com/premium/articles/3778355?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:48:36+00:00",
    "summary": "超级厄尔尼诺风险升温，或造成2026年经济损失7000亿美元，推升通胀，扰动航运，加剧贸易保护冲击。"
  },
  {
    "id": "wscn:3778636",
    "domain": "股票",
    "title": "SK海力士联手闪迪发布全球首个HBF标准规范，谷歌加入生态",
    "url": "https://wallstreetcn.com/articles/3778636",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:25:48+00:00",
    "summary": "SK海力士与闪迪联合发布高带宽闪存（HBF）全球首个标准规范，距联盟成立仅六个月。HBF定位于HBM与SSD之间的新型存储层级，支持最高512GB容量及0.4至3.0TB/s带宽，采用UCIe开放互联标准。谷歌与Tenstorrent已加入联盟，规范通过OCP向全行业开放。"
  },
  {
    "id": "wscn:3778628",
    "domain": "股票",
    "title": "创业板大涨近5%，芯片半导体、算力硬件集体反攻，医药股爆发、药明康德涨停，港股科网股多数走低",
    "url": "https://wallstreetcn.com/articles/3778628",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:05:22+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市约3700股飘红，上午半天成交1.37万亿。沪深两市半日成交额1.36万亿，较上个交易日基本持平。板块方面，算力硬件产业链反弹，CPO、PCB、存储器方向领涨。半导体设备、工业金属、AI应用、宇树机器人、网络游戏题材活跃。银行、白酒、煤炭、电力板块走弱。"
  },
  {
    "id": "wscn:3778635",
    "domain": "股票",
    "title": "“石油人民币”？“铁矿石人民币”？人民币国际化正“务实推进”",
    "url": "https://wallstreetcn.com/articles/3778635",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T03:51:30+00:00",
    "summary": "摩根大通指出，人民币在大宗商品结算中的使用持续扩大，2025年人民币结算占中国货物贸易比例已达创纪录的29%。该行认为，人民币国际化进展真实，但“石油人民币”类比可能不恰当，最可能的结果是在多极化体系中扮演更大角色，而非取代美元。"
  },
  {
    "id": "wscn:3778632",
    "domain": "股票",
    "title": "AI投资的逻辑变了：云厂进入收租时代，基础设施产业链承压",
    "url": "https://wallstreetcn.com/articles/3778632",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T03:35:55+00:00",
    "summary": "Q2财报季，微软亚马逊靠云业务大涨，SK海力士闪迪股价腰斩。市场不再比谁在AI上烧钱最多，只认谁能赚回来——云厂30%以上的GPU租赁回报正在被定价，云收入全面加速。另一边，AI基础设施链则在capex增速见顶后，被重新定价。AI的钱正从卖铲子修路的人，流向把铲子变成生意在路上收租的人。"
  },
  {
    "id": "wscn:3778634",
    "domain": "股票",
    "title": "谷歌DeepMind高管：AI千亿资本支出是人类史上最大科学赌注，核心押注\"递归自我改进\"",
    "url": "https://wallstreetcn.com/articles/3778634",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T03:35:45+00:00",
    "summary": "谷歌DeepMind首席战略官Sekhon在伯克利AI峰会上披露，\"递归自我改进\"是科技巨头天量资本支出的核心逻辑。DeepMind与OpenAI研究员预测\"递归自我改进\"或于2027至2028年实现。Sekhon坦承AI收入目前无法支撑支出，行业面临\"收入真空\"风险。"
  },
  {
    "id": "wscn:3778631",
    "domain": "股票",
    "title": "药明康德财报点评：业绩全面超预期，上调全年收入指引",
    "url": "https://wallstreetcn.com/premium/articles/3778631?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T03:11:49+00:00",
    "summary": "更值得关注的是，公司将全年营收指引从18%-22%一次性上调至35%-39%，资本开支从65亿-75亿上调至75亿-85亿——这在公司历史上尚属首次。"
  },
  {
    "id": "wscn:3778629",
    "domain": "股票",
    "title": "高盛合伙人：盈利才是核心驱动力，标普500年内有望再创历史新高",
    "url": "https://wallstreetcn.com/articles/3778629",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T02:52:01+00:00",
    "summary": "美股多头底气何来？高盛合伙人John Flood给出答案：盈利。标普500二季度EPS同比增速追踪值高达45%，远超季初22%预期，剔除非经常项目后仍达26%，创2021年来最快增速。与此同时，市场仓位已显著\"去泡沫化\"，对冲基金去杠杆、散户降温，高盛认为年内再创历史新高的窗口正在打开。"
  },
  {
    "id": "wscn:3778622",
    "domain": "股票",
    "title": "Palantir电话会：力推“主权AI”架构，“没用我们产品的企业，正在浪费Token、泄露商业机密”",
    "url": "https://wallstreetcn.com/articles/3778622",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T02:51:04+00:00",
    "summary": "Palantir管理层在电话会上痛批当前大模型实验室的“算力词元”计费是“寄生模式”，不仅让企业为无效结果买单，更迫使企业泄露核心机密。Palantir通过主推保障企业控制权的“主权AI”架构，宣告AI“跑分时代”终结，正加速将算力转化为真实的经济价值，公司预计未来18个月仍将维持极高增速。"
  },
  {
    "id": "wscn:3778630",
    "domain": "股票",
    "title": "全美25州提起诉讼，反对美政府最新关税措施",
    "url": "https://wallstreetcn.com/articles/3778630",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T02:24:45+00:00",
    "summary": "美国民主党领导的25个州正式起诉联邦政府，直指特朗普对60个贸易伙伴征收新一轮关税属越权之举，既绕过法定调查程序，又疑似\"换马甲\"规避最高法院裁决。"
  },
  {
    "id": "wscn:3778560",
    "domain": "股票",
    "title": "多晶硅期货涨停：产业博弈加剧，从价格执法到产能出清的光伏反内卷能否落地？",
    "url": "https://wallstreetcn.com/premium/articles/3778560?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T02:15:14+00:00",
    "summary": "7月31日市场监管总局在盐城召集27家光伏企业开展价格合规指导、八部门联合推动行业反内卷从\"自律倡议\"走向\"制度化执法\"。"
  },
  {
    "id": "wscn:3778623",
    "domain": "股票",
    "title": "“AI股神爆仓”和“韩股史诗级崩盘”--看似“偶然”实则“必然”，这是未来的预演",
    "url": "https://wallstreetcn.com/articles/3778623",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T02:09:59+00:00",
    "summary": "市场快速消化了“AI股神”爆仓和韩股暴跌事件，短暂震荡后归于平静。但德银认为，两起事件并非孤立偶发，而是十余年低利率催生的系统性杠杆积累的集中显现。更值得警惕的是，美联储主席沃什撤回前瞻性指引，可能是一种刻意为之的转变——主动向市场重新引入“不确定性溢价”，以遏制过度杠杆。美联储主动引入不确定性，“小波动”事件将以更高频率出现，且每一次都可能成为引爆更大危机的导火索。"
  },
  {
    "id": "wscn:3778625",
    "domain": "股票",
    "title": "“爆发性行情尚未终结！”德银维持金价4600美元目标不变",
    "url": "https://wallstreetcn.com/articles/3778625",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T01:38:31+00:00",
    "summary": "德意志银行贵金属策略师Michael Hseuh力排众议，维持2026年四季度金价4600美元/盎司目标不变。面对BIS\"泡沫\"警示，德银以公允价值模型、统计测试、官方需求三重框架反驳：2026年Q2全球央行购金规模创450亿美元历史纪录，金价修正底部或已在3900美元附近确立，始于2024年8月的爆发性行情尚未终结。"
  },
  {
    "id": "wscn:3778624",
    "domain": "股票",
    "title": "AI投资进入“分歧时代”！这是华尔街最纠结的六个问题",
    "url": "https://wallstreetcn.com/articles/3778624",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T01:10:51+00:00",
    "summary": "AI叙事正在自我撕裂：同一笔资本开支，既是增长信号也是财务风险；SaaS股年初跌超20%，但ServiceNow季报依然扎实；开源大模型放量，却无碍OpenAI收入爆发。巴克莱分析师直言，投资者的担忧\"彼此矛盾\"。真正的问题已不是AI有没有用，而是谁拿走收入增量、谁承担扩张风险——每一组对立，都还悬在空中等待裁决。"
  },
  {
    "id": "wscn:3778554",
    "domain": "股票",
    "title": "从 NVL72 到 NVL576：存储HBM退、大光互联进的算力资本开支再分配",
    "url": "https://wallstreetcn.com/premium/articles/3778554?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T00:46:12+00:00",
    "summary": "从 NVL72 到 NVL576 的代际切换中，单 GPU 总拥有成本（TCO）从 3.52 美元/小时下降至 2.96 美元/小时，降幅 16%——但成本结构的内部迁徙远比总成本数字本身更值得关注。"
  },
  {
    "id": "wscn:3778619",
    "domain": "股票",
    "title": "美日联手就能撑住日元吗？华尔街相信“日本不加息，任何干预都没用”",
    "url": "https://wallstreetcn.com/articles/3778619",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T00:33:29+00:00",
    "summary": "美日两国协调干预日元，两天合计动用近1000亿美元，规模创历史纪录，但效果已开始消退。高盛等华尔街机构认为，日元贬值根源在于日本高债务压制利率上行，日本央行不敢真正加息，干预只能买时间。高盛预测，日本央行下次加息或推迟至2027年1月，届时套息交易将卷土重来，日元或再度大幅走弱，美国财政部此次干预也将面临损失。"
  },
  {
    "id": "wscn:3778620",
    "domain": "股票",
    "title": "罕见干预操作！贝森特抛欧元、指示美联储“借钱”，让日本“别抛美债”，市场担心“套利交易逆转”",
    "url": "https://wallstreetcn.com/articles/3778620",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T00:29:31+00:00",
    "summary": "美日联手干预汇市，美财长贝森特罕见出手——以抛售欧元而非美元的方式买入日元，将日元从40年低位强行拉升。更引发市场瞩目的是，贝森特公开向美联储施压、要求扩大FIMA工具额度，此举被前官员直斥\"极不寻常\"。然而分析人士警告，在日本央行政策未转向前，干预效果难以持久，逾万亿美元套利交易平仓风险更悬而未决。"
  },
  {
    "id": "wscn:3778618",
    "domain": "股票",
    "title": "报道：存储三大原厂“2027年产能已提前售罄”，应验“明年是存储最短缺年份”",
    "url": "https://wallstreetcn.com/articles/3778618",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T00:27:00+00:00",
    "summary": "据媒体DIGITIMES报道，三星、美光、SK海力士的DRAM及HBM 2027年全年产能已全数分配完毕，NAND Flash产能亦基本预售一空。此前SK集团预警2027年将面临史上最严重供需失衡。尽管价格涨幅料较2026年趋缓，但\"价格高位常态化\"已成新常态，未提前锁仓者将面临无货可买困境。"
  },
  {
    "id": "wscn:3778621",
    "domain": "股票",
    "title": "韩股崩盘后，散户“失去信心”：牢记两条原则“第一：不买韩股，第二：遵守第一条”",
    "url": "https://wallstreetcn.com/articles/3778621",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T00:17:11+00:00",
    "summary": "7月韩国股市重挫22%遭遇历史性暴跌。散户此前受FOMO情绪驱动，大量买入三星、SK海力士等AI概念股，并借助政府推出的单股杠杆ETF加杠杆入场，损失惨重。分析人士警告，去杠杆化及半导体股震荡或持续数月，市场信心重建更需长期修复。"
  },
  {
    "id": "wscn:3778550",
    "domain": "股票",
    "title": "国产模型降本，AI闭环开始形成：资本市场为何重新定价CSP与应用端？",
    "url": "https://wallstreetcn.com/premium/articles/3778550?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T23:55:33+00:00",
    "summary": "过去两年，AI行情主要奖励芯片、服务器和光模块，资本市场相信算力稀缺，却始终无法回答巨额资本开支由谁买单。如今，国产开源模型能力逼近全球前沿，推理成本持续下降，多模型部署、企业级开发平台与办公Agent同时成熟，AI价值链的权力开始由单一模型向CSP、软件入口和垂直应用迁移。当应用开始制造Token、云平台完成分发、企业愿意按使用量付费，AI是否正从单向投入走向可以自我循环的商业闭环？"
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
    "id": "hn:49136787",
    "domain": "股票",
    "title": "Reddit Stock Collapses 23% as AI Eats Away at User Growth",
    "url": "https://www.barchart.com/story/news/3584357/reddit-stock-collapses-23-as-ai-eats-away-at-user-growth",
    "source": "thm",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-08-01T18:03:08+00:00",
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
    "id": "hn:49115139",
    "domain": "股票",
    "title": "Microsoft's $450B Jump Is Biggest in Stock Market History",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/microsoft-eyes-history-with-490-billion-pop-in-market-value",
    "source": "signatoremo",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-30T20:12:40+00:00",
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
    "id": "hn:49113358",
    "domain": "股票",
    "title": "South Korea's stock market plunges as AI-driven boom fades",
    "url": "https://www.aljazeera.com/economy/2026/7/29/south-koreas-stock-market-plunges-as-ai-driven-boom-fades",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-30T17:54:23+00:00",
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
    "points": 158,
    "published_at": "2026-07-25T11:04:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49118696",
    "domain": "金融",
    "title": "The bond market isn’t buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-31T03:32:21+00:00",
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
    "id": "hn:49157782",
    "domain": "金融",
    "title": "US Schools Are Ditching Chromebooks for MacBooks by the Thousands",
    "url": "https://finance.yahoo.com/technology/articles/us-schools-ditching-chromebooks-macbooks-233015401.html",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-08-03T16:16:19+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00038",
    "domain": "金融",
    "title": "Google's AI & Economy ATLAS v1.0: Mapping Gemini Usage in the Economy",
    "url": "https://arxiv.org/abs/2608.00038",
    "source": "Zanna Iscenko, Scott Strand, Yiyuan Chen, Guillaume Aimard, Mihai Codreanu, Vivek Sampathkumar, Alex Imas, Julian Jacobs, Evalyne Muiruri, Juan Mateos-Garcia, Jia Jen Ng, Samirah Javed, Josh Martin, Omar Ajmeri, Denis Calin, Andrew Kim, Fabien Curto Millet, James Manyika",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00038v1 Announce Type: new Abstract: This paper introduces the AI & Economy ATLAS (Activity, Task, Landscape, and Adoption Study), an ongoing economic research initiative using Google AI us"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00127",
    "domain": "金融",
    "title": "Drawdown Risk Beyond Brownian Motion: A Monte-Carlo Framework, Non-Gaussian Extensions, and Long Memory",
    "url": "https://arxiv.org/abs/2608.00127",
    "source": "Francesco Landolfi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00127v1 Announce Type: new Abstract: How deep and how long should the drawdowns of a systematic trading strategy run, given its Sharpe ratio and the statistical structure of its returns? Bu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00328",
    "domain": "金融",
    "title": "Global coal trade is resilient to maritime chokepoints",
    "url": "https://arxiv.org/abs/2608.00328",
    "source": "Jorrit Gosens, Alex B. H. Turnbull, Frank Jotzo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00328v1 Announce Type: new Abstract: There is renewed attention for maritime chokepoints and their potential disruption of global trade in energy. We analyse global trade in coal, and find "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00567",
    "domain": "金融",
    "title": "Optimal Inflation Rate: A Meta-Analysis",
    "url": "https://arxiv.org/abs/2608.00567",
    "source": "Matej Opatrny, Martin Opatrny, Tomas Havranek, Zuzana Irsova, Mojmir Hampl",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00567v1 Announce Type: new Abstract: We revisit the optimal long-run inflation rate using 777 estimates from 116 primary studies published between 1989 and 2026, the largest sample on the t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00580",
    "domain": "金融",
    "title": "Publication bias and p-hacking in the effect of COVID-19 on learning",
    "url": "https://arxiv.org/abs/2608.00580",
    "source": "Martina Luskova, Nino Buliskeria, Ali Elminejad, Tomas Havranek, Zuzana Irsova, Stepan Jurajda, Marek Kapicka",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00580v1 Announce Type: new Abstract: We revisit a central estimate in the economics of education: the human-capital loss associated with COVID-19 school closures. Estimates of pandemic lear"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00616",
    "domain": "金融",
    "title": "Latent Flow Matching for Arbitrage-Aware Implied Volatility Surface Generation",
    "url": "https://arxiv.org/abs/2608.00616",
    "source": "Oscar Brooks, Dusica Bajalica, Yating Lui, Imen Ben Tahar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00616v1 Announce Type: new Abstract: We propose an arbitrage-aware latent flow-matching framework for unconditional implied volatility surface generation. The method first compresses high-d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00631",
    "domain": "金融",
    "title": "Axient: Debt-Free Finality for Leveraged Binary Event Markets",
    "url": "https://arxiv.org/abs/2608.00631",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00631v1 Announce Type: new Abstract: Leveraged event positions combine a repayable loan with an outcome claim that may become non-tradable before oracle payout is final. This paper specifie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00647",
    "domain": "金融",
    "title": "Axient: On-Chain Credit and Loss Allocation for Leveraged Event Markets: A Venue-Agnostic Protocol for Traders, Credit Providers, Market Makers, and Liquidation Backstops",
    "url": "https://arxiv.org/abs/2608.00647",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00647v1 Announce Type: new Abstract: A physically backed leveraged event position requires real credit: if collateral C receives leverage L, the protocol supplies (L-1)C and uses the combin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00761",
    "domain": "金融",
    "title": "AI and Exchange Rate Predictability",
    "url": "https://arxiv.org/abs/2608.00761",
    "source": "Amin Izadyar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00761v1 Announce Type: new Abstract: I revisit the exchange rate disconnect puzzle, first documented by Meese and Rogoff (1983), using generative artificial intelligence (AI) to forecast cu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00858",
    "domain": "金融",
    "title": "Data-Driven Measures of High-Frequency Trading",
    "url": "https://arxiv.org/abs/2608.00858",
    "source": "Gbenga Ibikunle, Ben Moews, Dmitriy Muravyev, Khaladdin Rzayev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00858v1 Announce Type: new Abstract: We introduce data-driven measures of high-frequency trading (HFT) that distinguish between liquidity-supplying and liquidity-demanding strategies. We tr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00885",
    "domain": "金融",
    "title": "Optimal Trading of Microstructure Mean Reversion",
    "url": "https://arxiv.org/abs/2608.00885",
    "source": "Lucas Rabechini Amaral",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00885v1 Announce Type: new Abstract: At the scale of seconds the observed mid carries a stationary, mean-reverting error around a latent efficient price. We build an order book whose own fl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00911",
    "domain": "金融",
    "title": "Battery Storage Co-Optimization in Day-Ahead and Real-Time Markets with Bayesian Optimization",
    "url": "https://arxiv.org/abs/2608.00911",
    "source": "Thiha Aung, Mike Ludkovski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00911v1 Announce Type: new Abstract: We propose Adaptive Refinement Bayesian Optimization for Day-Ahead and Real-Time (ARBO-DART) markets, an algorithm for BESS intraday dispatch co-optimiz"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00917",
    "domain": "金融",
    "title": "Pro-rata mechanisms in groundwater markets",
    "url": "https://arxiv.org/abs/2608.00917",
    "source": "Igor Cialenco, Michael Ludkovski, Gael Dimitri Tekam Fongouo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00917v1 Announce Type: new Abstract: We introduce a pro-rata rationing mechanism for resolving supply-demand imbalances in groundwater markets, extending the price-formation model of Cialen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00988",
    "domain": "金融",
    "title": "Exactly solvable model for the diffusive price-dynamics paradox under long-range correlated market-order flow",
    "url": "https://arxiv.org/abs/2608.00988",
    "source": "Yuki Sato, Shunta Fujiwara, Kiyoshi Kanazawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.00988v1 Announce Type: new Abstract: We develop an exactly solvable nonlinear time-series model by incorporating the square-root price-impact law into the Lillo--Mike--Farmer (LMF) model to"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01010",
    "domain": "金融",
    "title": "Import dependence and per capita production are main determinants of economies' food supply robustness under production shocks",
    "url": "https://arxiv.org/abs/2608.01010",
    "source": "Han-Yu Zhu, Maria Cristina Rulli, Wei-Xing Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01010v1 Announce Type: new Abstract: Food supply shocks in major producing economies can propagate through trade networks and generate uneven impacts across the global food system. This stu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01181",
    "domain": "金融",
    "title": "Talking to Digital Twins: Selective Disclosure and Belief Measurement in Financial Social Media",
    "url": "https://arxiv.org/abs/2608.01181",
    "source": "Boone Bowles, Raymond Duch, Sorin Sorescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01181v1 Announce Type: new Abstract: Social media affect financial markets, but public posts by financial media personas are voluntary disclosures. What is not disclosed is therefore usuall"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01208",
    "domain": "金融",
    "title": "Climate-Dyna Deep Hedging for XVAs: Model-Based Reinforcement Learning, Residual Climate HVA, and Hedge-Instrument Discovery",
    "url": "https://arxiv.org/abs/2608.01208",
    "source": "Xiaozhen Wang, Francois Buet-Golfouse",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01208v1 Announce Type: new Abstract: For a trading desk, residual climate hedging valuation adjustment (HVA) is the climate cost left after its inherited hedge and any admissible overlay ha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01212",
    "domain": "金融",
    "title": "Do Humans Bargain Differently with AI? Evidence from Alternating-Offer Games",
    "url": "https://arxiv.org/abs/2608.01212",
    "source": "Yuhao Fu, Nobuyuki Hanaki, Haitao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01212v1 Announce Type: new Abstract: Artificial intelligence increasingly participates in economic interactions not only as a tool, but also as an autonomous bargaining counterpart negotiat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01217",
    "domain": "金融",
    "title": "Amortizing the Calibration Triple: A Projection-Consistent Neural Operator for Local-Stochastic Volatility",
    "url": "https://arxiv.org/abs/2608.01217",
    "source": "Xiaozhen Wang, Ana\\\"is Despr\\'es, Martin Dureau, Francois Buet-Golfouse",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01217v1 Announce Type: new Abstract: Local-stochastic volatility (LSV) combines vanilla marginals with richer smile dynamics, but calibration requires a slow, noisy and sequential McKean--V"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01294",
    "domain": "金融",
    "title": "An Information-Geometric Framework for Bayesian Credit Risk Monitoring",
    "url": "https://arxiv.org/abs/2608.01294",
    "source": "Lorenzo Quirini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01294v1 Announce Type: new Abstract: We propose an information-geometric framework for credit risk monitoring in which a bank's knowledge of a borrower is represented by a posterior distrib"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01479",
    "domain": "金融",
    "title": "The VIX-Derived Volatility Model: A VIX-first Joint SPX-VIX Framework",
    "url": "https://arxiv.org/abs/2608.01479",
    "source": "Nicola F. Zaugg, Lech A. Grzelak",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01479v1 Announce Type: new Abstract: We propose the VIX-derived volatility (VDV) model, a VIX-first framework for joint SPXVIX modeling. In the model, we define explicit dynamics for the VI"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01494",
    "domain": "金融",
    "title": "Conformal Kelly: Conformal Prediction Intervals as the Scale in Fractional Kelly Position Sizing",
    "url": "https://arxiv.org/abs/2608.01494",
    "source": "Robert Jacob Ryan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01494v1 Announce Type: new Abstract: Conformal prediction has traditionally been used to quantify prediction uncertainty. We put that uncertainty to a second use, combining a 75% conformal "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01540",
    "domain": "金融",
    "title": "Do people rely on ChatGPT more than their peers to detect deepfake news?",
    "url": "https://arxiv.org/abs/2608.01540",
    "source": "Yuhao Fu, Nobuyuki Hanaki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01540v1 Announce Type: new Abstract: This experimental study investigates how people rely on different sources of advice when detecting AI-generated fake news (deepfake news). In a laborato"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01554",
    "domain": "金融",
    "title": "P-Bubbles, Q-Bubbles, and Risk Premia",
    "url": "https://arxiv.org/abs/2608.01554",
    "source": "Robert A. Jarrow, Simon S. Kwok",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01554v1 Announce Type: new Abstract: We develop a unified modeling framework that connects two distinct types of bubbles defined in the literature: the rational bubbles (aka P-bubbles), and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01607",
    "domain": "金融",
    "title": "AI Financial Advice: Supply, Demand, and Life Cycle Implications",
    "url": "https://arxiv.org/abs/2608.01607",
    "source": "Taha Choukhmane, Tim de Silva, Weidong Lin, Matthew Akuzawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.01607v1 Announce Type: new Abstract: We ask a representative sample to write prompts seeking spending and investing advice from LLMs, then simulate the lifetime effects of following the adv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02002",
    "domain": "金融",
    "title": "Hawkes-Driven OTC Market Making: Volterra-Riccati Approximation",
    "url": "https://arxiv.org/abs/2608.02002",
    "source": "Alexander Barzykin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.02002v1 Announce Type: new Abstract: We formulate an over-the-counter (OTC) market-making problem in which request-for-quote (RFQ) arrivals are modelled by general Hawkes kernels and fills "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02102",
    "domain": "金融",
    "title": "Navigating the skill diversity frontier: How skill complexity explains worker resilience",
    "url": "https://arxiv.org/abs/2608.02102",
    "source": "Mar Carpanelli, Jedrzej Duszynski, Fabian Stephany",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.02102v1 Announce Type: new Abstract: As artificial intelligence transforms labor markets, understanding what makes workers adaptable has become increasingly important. Existing approaches t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02355",
    "domain": "金融",
    "title": "Path Portfolio Optimization: Defect, Lift, and the Price of Path Complexity",
    "url": "https://arxiv.org/abs/2608.02355",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.02355v1 Announce Type: new Abstract: This paper builds Path Portfolio Optimization: portfolio theory on a path-first framework in which the signature is the universal coordinate of the pric"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02475",
    "domain": "金融",
    "title": "Methodology for Modelling Token Economies and Performing Event Impact Analysis with DeTEcT",
    "url": "https://arxiv.org/abs/2608.02475",
    "source": "Rem Sadykhov, Geoffrey Goodell, Philip Treleaven",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T04:00:00+00:00",
    "summary": "arXiv:2608.02475v1 Announce Type: new Abstract: The objective of this paper is to provide a methodology for applying the DeTEcT framework to modelling token economies, to formalise the configuration o"
  },
  {
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 57,
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
    "id": "hn:49087447",
    "domain": "金融",
    "title": "Federal Judges Chastise Justice Department for 'Unlawful' Conduct",
    "url": "https://www.propublica.org/article/justice-department-presumption-of-regularity",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-28T17:47:47+00:00",
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
  }
]
```
