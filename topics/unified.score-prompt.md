# Curio · 趋势雷达 · 跨域 Top 选稿

> 一次跑完整份简报：从所有领域的合并候选池里，选出 4-5 条跨域 Top 头条 + 备选池。
> 每条头条含"已确认 / 尚属判断对照表 + 主编点评"。

---

## 角色

你是 Curio 的**总编辑**——读者把"看全网"的工作交给你，你的责任是：

1. 从今天所有领域的合并候选池里**精选 4-5 条头条**，领域以候选条目的 `domain` 字段为准
2. 每条头条按 **已确认 / 尚属判断对照表形式**写：标题 + 引子段 + 已确认/尚属判断 + 主编点评
3. 列一份"备选池"（10-15 条标题级简单解释）

**展示分组规则（关键）**：
- 输出时按 `domain` 字段标注（用候选条目里给的中文名，例如 "AI / 科技"、"金融"、"半导体"、"大厂讯息"）
- 系统会**按 domain 拆分到每个域单独的页面/邮件**——所以读者看到的是分领域展示
- 你只需要选稿不混淆 domain，不需要在标题里加 `[领域]` 前缀（系统会自动展示域 chip）
- **【硬约束 - 不可违反】每个出现在候选池里的域，必须至少 1 条出现在 headlines 或 shortlist 里**。如某域候选有限/质量一般，宁可降星标准也要选 1 条放 shortlist —— 否则该域邮件/页面会显示"今日 0 条"，是不可接受的产品 bug。

---

## 输入（变量替换）

- 今日日期：`2026-11-09`
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
  "date": "2026-11-09",
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
- **跨域均衡**：在本期候选池实际包含的领域中，头条尽量覆盖至少 3 个域；不足 3 个域时按实际领域数处理。如果某域今天没有"够 4 星"的，可以不选入头条，但仍须遵守上方备选池的领域覆盖约束。
- **新颖度优先**：选今天/本周首发的、有数字的、有未来动作的。避免"已知信息再拼装"。
- **跨平台同事件去重**：同一个事件（如某公司 IPO）在 HN + RSS 都出现，**选英文原版/最深度的源**。
- **反偏好**：保留 0-1 条用户可能不爱看但应该看的（标 `is_diverse: true`，可选）。
- **历史反馈优先**：如果用户最近一次反馈说"想多看 X"，至少 1 条头条契合。

### 备选池（10-15 条）
- 不上头条但仍值得知晓的。
- 每条 30-60 字一句话。
- 按候选条目的 `domain` 自然分组，不预设固定领域列表。

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
    "id": "bvid:BV1REx46NEc4",
    "domain": "AI",
    "title": "【全网最全】DeepSeek Harness超详细教程！50分钟吃透DSH，让SuperAgent给你干活！",
    "url": "http://www.bilibili.com/video/av117540671982699",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 2386339,
    "published_at": "2026-11-01T10:22:02+00:00",
    "summary": "DeepSeek Harness超详细教程！\n大家可以速速收藏啦~\n耗时60天制作！感谢大家的三联\n未来还会出其他AI教程，大家可以关注一下~"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 2098165,
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
    "points": 1480038,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1465615,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 1446174,
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
    "points": 911075,
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
    "points": 895412,
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
    "points": 747686,
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
    "points": 596075,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1tTxd6KEeL",
    "domain": "AI",
    "title": "全网最细！40分钟速通Codex！【GenJi深度教程】",
    "url": "http://www.bilibili.com/video/av117558925596398",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 514775,
    "published_at": "2026-11-05T10:00:00+00:00",
    "summary": "我们花了两个月整理出来了AI工具：Codex从入门到精通的全教程。这里面包含了安装、核心功能介绍、以及可快速上手的实战案例等等 完全免费的公益课程，如果你看完觉得有帮助，麻烦【点赞、投币、收藏】一键三连，就当作这门课的学费啦！做免费课程不容易，先谢谢大家支持！"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 431444,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1kr4h6fExw",
    "domain": "AI",
    "title": "DeepSeek 新出的 Super Agent 是什么？真有用么？",
    "url": "http://www.bilibili.com/video/av117564076202051",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 389688,
    "published_at": "2026-11-05T13:35:56+00:00",
    "summary": "DeepSeek Harness 团队最新开源的 Super-agent 是什么？和传统 Agent 有什么区别？它是怎么工作的？真的能提升 AI 工作的效率么？一期视频带你掌握 Super-agent 智能体，对 AI 小白、AI 编程爱好者、前端和后端程序员、AI 应用开发求职者都有帮助\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 358195,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 350494,
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
    "points": 323637,
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
    "points": 296055,
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
    "points": 229282,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV15XDfBSE2t",
    "domain": "AI",
    "title": "ClaudeCode平替:OpenCode详细使用教程看这一个就够了（内含超详细安装文档+软件安装包）",
    "url": "http://www.bilibili.com/video/av116379604881806",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 202345,
    "published_at": "2026-04-13T09:00:00+00:00",
    "summary": "opencodeopencode使用全攻略opencode教程opencode和claudecodeopencode使用技巧opencode实战opencode coworkopencode安装opencode开发opencode使用教程opencode教程opencode安装教程opencode使用全攻略opencode和claudecodeopencode skillsopencode插件op"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 186231,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 165213,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 106469,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 96665,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 91205,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 77078,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1c8NFzhEMi",
    "domain": "AI",
    "title": "一个CLI干掉所有MCP工具，省99%的token mcp2cli",
    "url": "http://www.bilibili.com/video/av116204349953548",
    "source": "探索未至之境",
    "platform": "bilibili",
    "points": 63667,
    "published_at": "2026-03-10T10:18:17+00:00",
    "summary": "深度解析GitHub热门项目mcp2cli——一个能把任何MCP服务器或OpenAPI规范变成命令行工具的Python项目。它用&quot;懒发现&quot;机制，把MCP协议的token浪费从数十万降到几千，节省高达99%。整个核心实现只有一个Python文件，却支持三种接入模式、OAuth认证和智能缓存。发布仅一天就获得372颗星，但社区也有激烈争议：CLI真的能取代MCP吗？准确率会不会受影"
  },
  {
    "id": "bvid:BV1RrZHYqEvm",
    "domain": "AI",
    "title": "Cursor+Figma MCP，自动生成可编辑设计稿",
    "url": "http://www.bilibili.com/video/av114257538650701",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 52818,
    "published_at": "2025-03-31T14:36:31+00:00",
    "summary": "分享了两种Figma MCP。一种是通过获取Figma API key来实现Cursor和Figma的连接，更侧重精准控制。\n.\n因为大多数 Figma 文件都会非常大，如果你想让Cursor精准链接到文件中的特定元素，一般选择这个MCP会更合适。\n.\n另一种则是通过Figma插件形式，通过channel实现与Cursor的连接，更侧重从0到1的设计元素生成，比较适合没有太多设计基础的用户。\n.\n"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50283,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1EfY76YEwp",
    "domain": "AI",
    "title": "14k Star Claude Code 开源桌面端，能自动操作电脑了！",
    "url": "http://www.bilibili.com/video/av117251936293145",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 49697,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 46888,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1NP546xEUj",
    "domain": "AI",
    "title": "5分钟安装Claudecode并进入deepseek",
    "url": "http://www.bilibili.com/video/av116555396419337",
    "source": "宝藏女嗨沈幼楚",
    "platform": "bilibili",
    "points": 45586,
    "published_at": "2026-05-11T10:11:25+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41303,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 38358,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34667,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1Nu3M6bEXE",
    "domain": "AI",
    "title": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了",
    "url": "http://www.bilibili.com/video/av116979859984479",
    "source": "Agent开发教程",
    "platform": "bilibili",
    "points": 34630,
    "published_at": "2026-07-25T09:34:49+00:00",
    "summary": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了，草履虫都能学会！"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 32496,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29941,
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
    "points": 29050,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 27867,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 27460,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 26513,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 26219,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 25818,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1spTy6DEb4",
    "domain": "AI",
    "title": "Claude code接管科研全流程：cc-kaiti 带你从 0 走到开题报告和答辩 PPT",
    "url": "http://www.bilibili.com/video/av116866278233889",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 25487,
    "published_at": "2026-07-05T07:53:28+00:00",
    "summary": "十二年科研经验加持的课题开题Skill，从零开始到拿到一份完整的开题报告及开题PPT，仅需一天！\n\n本次视频分享的cc-kaiti这个skill文件及配套的资料包，在后台私我“cc开题”获取~"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22853,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 21446,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21175,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1nwKc6pEmi",
    "domain": "AI",
    "title": "手把手教你用Claude Code做投研分析（AI Investing）",
    "url": "http://www.bilibili.com/video/av116938386775380",
    "source": "frank-quant",
    "platform": "bilibili",
    "points": 18695,
    "published_at": "2026-07-18T01:35:16+00:00",
    "summary": "只敲一行命令，就能得到一份带四个视角、交叉验证、明确标注不确定性的深度投研报告——这一期手把手教你怎么做到。\n\n我们实测了 GitHub 上爆火的开源项目 ai-berkshire（一万多 star）：它把巴菲特、芒格、段永平、李录四位大师的价值投资方法，做成了一套能在 Claude Code / Codex 里一条命令调用的 AI 投研工作流，一共 19 个技能。全程以小米集团为例，从安装、跑报"
  },
  {
    "id": "bvid:BV1Vd8i6iEjd",
    "domain": "AI",
    "title": "AI办公实战课，AI助力工作学习效率提升N倍--从提示词、写作到数据分析与 AI 绘画，一课打通",
    "url": "http://www.bilibili.com/video/av117132901815801",
    "source": "1620谷爱凌",
    "platform": "bilibili",
    "points": 16467,
    "published_at": "2026-08-21T10:04:22+00:00",
    "summary": "AI办公实战课，AI助力工作学习效率提升N倍--从提示词、写作到数据分析与 AI 绘画，一课打通"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 16016,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15533,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "hn:50418016",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang's letter to staff about affair",
    "url": "https://nvidianews.nvidia.com/news/a-message-to-our-company",
    "source": "karimf",
    "platform": "hackernews",
    "points": 703,
    "published_at": "2026-11-08T22:20:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362905",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux",
    "url": "https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 617,
    "published_at": "2026-11-04T08:46:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416801",
    "domain": "AI 算力 / 半导体",
    "title": "Statement from Nvidia board of directors",
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "source": "vincentchau",
    "platform": "hackernews",
    "points": 470,
    "published_at": "2026-11-08T20:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50293047",
    "domain": "AI 算力 / 半导体",
    "title": "Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang",
    "url": "https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 370,
    "published_at": "2026-10-29T17:43:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50348962",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia – open-source auto-ontology",
    "url": "https://github.com/NVIDIA/auto-ontology",
    "source": "campervans",
    "platform": "hackernews",
    "points": 291,
    "published_at": "2026-11-03T07:04:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50327058",
    "domain": "AI 算力 / 半导体",
    "title": "Seoul Viosys begins production of rare-earth-free white light emitter",
    "url": "https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml",
    "source": "gmays",
    "platform": "hackernews",
    "points": 195,
    "published_at": "2026-11-01T16:23:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50387738",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Kubernetes Engine (NVKE)",
    "url": "https://github.com/dsx-ai-factory/nvke",
    "source": "gkapur",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-11-06T03:16:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50275128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Transcribe: open ASR for 40 languages",
    "url": "https://huggingface.co/blog/nvidia/nemotron-transcribe-granary",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 134,
    "published_at": "2026-10-28T15:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416679",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Board to Probe Spying Case After CEO Admits Affair",
    "url": "https://www.bloomberg.com/news/articles/2026-11-08/nvidia-board-to-probe-spying-case-after-ceo-jensen-huang-admits-infidelity",
    "source": "specialp",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-11-08T20:14:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416787",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Opens Investigation into Jensen Huang's Relationship with Chinese Spy",
    "url": "https://www.nytimes.com/2026/11/08/technology/nvidia-investigation-jensen-huang-china.html",
    "source": "Aboutplants",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-11-08T20:25:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363861",
    "domain": "AI 算力 / 半导体",
    "title": "RTX 5090 Street Prices Top $9k as Nvidia GPU Costs Climb",
    "url": "https://aroundprague.cz/en/news/us/rtx-5090-street-prices-top-9-000-as-nvidia-gpu-costs-climb",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 78,
    "published_at": "2026-11-04T11:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50415161",
    "domain": "AI 算力 / 半导体",
    "title": "US believes Nvidia's Huang had romantic relationship with alleged Chinese spy",
    "url": "https://www.ft.com/content/a55a2a22-4479-4f93-a445-6147a5c6d790",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-11-08T17:19:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50417283",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia launches investigation into CEO's affair with suspected Chinese spy",
    "url": "https://www.bbc.co.uk/news/articles/c3dxw10rjn9no",
    "source": "haritha-j",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-08T21:09:42+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/",
    "domain": "AI 算力 / 半导体",
    "title": "DeepX Tapes Out Second-Gen Chip, Projects 6.7× Performance Gain With LPDDR5x-PIM",
    "url": "https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T06:47:26+00:00",
    "summary": "DeepX is targeting edge markets including robotics with its second-generation AI accelerator, which can run large LLMs on device in under 5 W. The post DeepX Tapes Out Second-Gen Chip, Projects 6.7× P"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation",
    "domain": "AI 算力 / 半导体",
    "title": "Synaptics sends cease-and-desist order to creator of open-source DisplayLink driver, dares him to publicize its threats",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T11:00:00+00:00",
    "summary": "A hobbyist's effort to make DisplayLink work better on Linux is turning into a legal saga."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/security-researcher-had-to-jailbreak-their-car-just-to-update-the-clock-missing-tomtom-sd-card-locked-settings-menu-custom-linux-exploit-deployed-to-adjust-daylight-saving-time",
    "domain": "AI 算力 / 半导体",
    "title": "Security researcher had to jailbreak their car just to update the clock",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/security-researcher-had-to-jailbreak-their-car-just-to-update-the-clock-missing-tomtom-sd-card-locked-settings-menu-custom-linux-exploit-deployed-to-adjust-daylight-saving-time",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T10:40:00+00:00",
    "summary": "A security researcher has revealed how they managed to update the time on their car infotainment system using reverse engineering techniques."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-32-gb-of-ram-for-just-usd209-99-thanks-to-the-g-skill-ripjaws-v-ddr4-3200-kit-rare-sale-on-a-quality-kit-from-an-enthusiast-brand-with-a-stellar-reputation",
    "domain": "AI 算力 / 半导体",
    "title": "Grab 32 GB of RAM for just $209.99 thanks to the G.Skill Ripjaws V DDR4-3200 kit — rare sale on a quality kit from an enthusiast brand with a stellar reputation",
    "url": "https://www.tomshardware.com/pc-components/grab-32-gb-of-ram-for-just-usd209-99-thanks-to-the-g-skill-ripjaws-v-ddr4-3200-kit-rare-sale-on-a-quality-kit-from-an-enthusiast-brand-with-a-stellar-reputation",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T10:20:00+00:00",
    "summary": "Grab 32 GB of RAM for just $209.99 thanks to the G.Skill Ripjaws V DDR4-3200 kit"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-ceo-jensen-huang-admits-to-having-an-affair-with-suspected-chinese-spy-jensen-apologizes-in-letter-to-staff-company-board-forms-independent-committee-to-investigate",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang admits to having an affair with suspected Chinese spy",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-ceo-jensen-huang-admits-to-having-an-affair-with-suspected-chinese-spy-jensen-apologizes-in-letter-to-staff-company-board-forms-independent-committee-to-investigate",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T21:27:29+00:00",
    "summary": "Nvidia's board of directors is investigating a report about Jensen Huang's alleged affair with a client, claims it is still confident in Jensen and leadership team."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/diamond-foundry-creates-worlds-first-200mm-single-crystal-diamond-wafer-massive-gem-aims-to-solve-ai-chip-cooling-crisis-envisioned-as-a-cooling-material-for-semiconductors",
    "domain": "AI 算力 / 半导体",
    "title": "Diamond Foundry creates world's first 200mm single-crystal diamond wafer",
    "url": "https://www.tomshardware.com/pc-components/cooling/diamond-foundry-creates-worlds-first-200mm-single-crystal-diamond-wafer-massive-gem-aims-to-solve-ai-chip-cooling-crisis-envisioned-as-a-cooling-material-for-semiconductors",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T15:25:00+00:00",
    "summary": "This 200mm single-crystal diamond wafer is designed to efficiently remove heat and prevent hotspots from forming on AI processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/logitech-g502-x-lightspeed-review",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech G502 X Lightspeed Review: No lights, same price",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/logitech-g502-x-lightspeed-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T15:00:00+00:00",
    "summary": "Logitech's G502 X Lightspeed strips the G502 X Plus of its lighting, but retains the $160 price tag."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/japanese-arcades-suffer-week-long-blackout-following-sega-server-hack-bandai-namco-titles-resume-trial-operations-as-sega-games-remain-offline",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese arcades suffer week-long blackout following Sega server hack",
    "url": "https://www.tomshardware.com/video-games/japanese-arcades-suffer-week-long-blackout-following-sega-server-hack-bandai-namco-titles-resume-trial-operations-as-sega-games-remain-offline",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T15:00:00+00:00",
    "summary": "The sensory overload in video game arcades in Japan was eerily absent from some venues this week."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/the-end-of-an-era-as-linux-7-5-purges-the-last-30-year-old-intel-mmx-optimizations-from-pentium-age-open-source-os-retires-ancient-1997-pentium-instructions-to-streamline-code",
    "domain": "AI 算力 / 半导体",
    "title": "The end of an era as Linux 7.5 purges the last 30-year-old Intel MMX optimizations from Pentium age",
    "url": "https://www.tomshardware.com/software/linux/the-end-of-an-era-as-linux-7-5-purges-the-last-30-year-old-intel-mmx-optimizations-from-pentium-age-open-source-os-retires-ancient-1997-pentium-instructions-to-streamline-code",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T14:40:00+00:00",
    "summary": "Linux developers are preparing to make Intel’s ancient MultiMedia eXtensions irrelevant, with the last MMX code now set to be removed from the kernel."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/ukraine-builds-combat-robots-to-hunt-russian-troops-in-underground-gas-pipelines-ugvs-adapted-following-15-kilometer-subterranean-assault",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine builds combat robots to hunt Russian troops in underground gas pipelines",
    "url": "https://www.tomshardware.com/tech-industry/robotics/ukraine-builds-combat-robots-to-hunt-russian-troops-in-underground-gas-pipelines-ugvs-adapted-following-15-kilometer-subterranean-assault",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T14:36:39+00:00",
    "summary": "Ukraine is developing a new class of combat robots designed to operate inside underground gas pipelines."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-released-its-8800-gtx-gpu-20-years-ago-today-celebrates-with-steam-game-homage-interactive-demos-eye-watering-minimum-requirements-include-rtx-4070-32gb-ram-and-30gb-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia released its 8800 GTX GPU 20 years ago today, celebrates with Steam game homage",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-released-its-8800-gtx-gpu-20-years-ago-today-celebrates-with-steam-game-homage-interactive-demos-eye-watering-minimum-requirements-include-rtx-4070-32gb-ram-and-30gb-storage",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T14:20:00+00:00",
    "summary": "On this day in 2006, Nvidia released the legendary GeForce 8800 GTX graphics card and it is celebrating the event with a very demanding (but free) interactive Steam demo."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/open-source-gpu-task-manager-reveals-exactly-whats-eating-your-vram-microsoft-vps-new-gpu-taskman-tool-reveals-every-process-using-your-gpu-how-much-memory-each-uses-and-breaks-down-ai-and-llm-workloads",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source GPU task manager reveals exactly what's eating your VRAM",
    "url": "https://www.tomshardware.com/pc-components/gpus/open-source-gpu-task-manager-reveals-exactly-whats-eating-your-vram-microsoft-vps-new-gpu-taskman-tool-reveals-every-process-using-your-gpu-how-much-memory-each-uses-and-breaks-down-ai-and-llm-workloads",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T13:40:00+00:00",
    "summary": "A new open-source GitHub project called gputaskman has been released by Microsoft VP Scott Hanselman."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/hundreds-arrested-after-microsoft-data-center-protest-turns-violent-stop-dirty-data-centers-coalition-demands-halt-to-ai-data-center-expansion-dutch-police-seize-break-in-tools-suspected-stolen-items-from-construction-site",
    "domain": "AI 算力 / 半导体",
    "title": "Hundreds arrested after Microsoft data center protest turns violent",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/hundreds-arrested-after-microsoft-data-center-protest-turns-violent-stop-dirty-data-centers-coalition-demands-halt-to-ai-data-center-expansion-dutch-police-seize-break-in-tools-suspected-stolen-items-from-construction-site",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T13:20:00+00:00",
    "summary": "It's unclear which group entered the construction site first, but the action led to the arrest of 150 to 200 protesters."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/two-chinese-companies-cleared-to-buy-banned-nvidia-ai-chips-have-empty-offices-and-unknown-addresses-investigation-reveals-businesses-have-ties-to-sanctioned-chinese-military-suppliers",
    "domain": "AI 算力 / 半导体",
    "title": "Two Chinese companies cleared to buy banned Nvidia AI chips have empty offices and unknown addresses",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/two-chinese-companies-cleared-to-buy-banned-nvidia-ai-chips-have-empty-offices-and-unknown-addresses-investigation-reveals-businesses-have-ties-to-sanctioned-chinese-military-suppliers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T13:00:00+00:00",
    "summary": "The offices for New Matrix and Maginfra, both approved to receive H200 chips, appear abandoned, and people in the buildings say they're unfamiliar with the companies or have never seen anyone working "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/pcs-with-64gb-of-ram-plummet-18-percent-as-memory-prices-soar-cpu-z-install-base-data-shows-ddr4-making-a-surprise-comeback",
    "domain": "AI 算力 / 半导体",
    "title": "PC's with 64GB of RAM plummet 18% as memory prices soar",
    "url": "https://www.tomshardware.com/pc-components/ram/pcs-with-64gb-of-ram-plummet-18-percent-as-memory-prices-soar-cpu-z-install-base-data-shows-ddr4-making-a-surprise-comeback",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T12:40:00+00:00",
    "summary": "CPU-Z data reveals PC memory capacity is dropping for the first time ever. Driven by skyrocketing AI DRAM prices, 64GB RAM adoption plummeted 18% YoY."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabber-uses-second-gen-optane-memory-sticks-to-run-a-2-8-trillion-parameter-ai-model-on-cpu-alone-warns-that-optanes-extreme-heat-can-burn-out-nearby-memory-dram-used-blower-fans-to-prevent-melting-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Homelabber uses second-gen Optane memory sticks to run a 2.8-trillion-parameter AI model on CPU alone",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabber-uses-second-gen-optane-memory-sticks-to-run-a-2-8-trillion-parameter-ai-model-on-cpu-alone-warns-that-optanes-extreme-heat-can-burn-out-nearby-memory-dram-used-blower-fans-to-prevent-melting-ram",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T12:20:00+00:00",
    "summary": "A Reddit homelab user ran Moonshot AI’s 2.8-trillion-parameter Kimi K3 CPU-only on Optane PMem 200 at 0.85 tokens/s with a 1-bit quant."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/pocket-sized-ukrainian-receiver-intercepts-russian-strike-drone-video-feeds-up-to-six-miles-away-device-only-slightly-heavier-than-a-smartphone-intercepts-analog-video-signals-sent-to-russian-operators",
    "domain": "AI 算力 / 半导体",
    "title": "Pocket-sized Ukrainian receiver intercepts Russian strike drone video feeds up to six miles away",
    "url": "https://www.tomshardware.com/tech-industry/drones/pocket-sized-ukrainian-receiver-intercepts-russian-strike-drone-video-feeds-up-to-six-miles-away-device-only-slightly-heavier-than-a-smartphone-intercepts-analog-video-signals-sent-to-russian-operators",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T12:00:00+00:00",
    "summary": "The D·Vision SDR can intercept signals from 500 MHz to 8.7 GHz, covering the 4.1-4.5 GHz spectrum that Russian Molniya strike drones use to communicate with their operators."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/wow-forever-launch-used-70-480-cpu-cores-and-251-terabytes-of-ram-3-924-virtual-machines-powered-one-of-world-of-warcrafts-smoothest-launches-ever",
    "domain": "AI 算力 / 半导体",
    "title": "WoW: Forever launch used 70,480 CPU cores and 251 terabytes of RAM",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/wow-forever-launch-used-70-480-cpu-cores-and-251-terabytes-of-ram-3-924-virtual-machines-powered-one-of-world-of-warcrafts-smoothest-launches-ever",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T11:30:00+00:00",
    "summary": "Inside the astonishing hardware behind World of Warcraft: Forever. 251TB of RAM and 70K cores kept millions of players online without a hitch."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/pc-air-duster-motors-power-21-inch-diy-remote-control-plane-at-130-000-rpm-usd23-air-duster-power-styrofoam-a10-warthog-style-rc-plane-hits-the-skies-much-faster-than-expected",
    "domain": "AI 算力 / 半导体",
    "title": "PC air duster motors power 21-inch DIY remote control plane at 130,000 RPM",
    "url": "https://www.tomshardware.com/maker-stem/pc-air-duster-motors-power-21-inch-diy-remote-control-plane-at-130-000-rpm-usd23-air-duster-power-styrofoam-a10-warthog-style-rc-plane-hits-the-skies-much-faster-than-expected",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T11:00:00+00:00",
    "summary": "A remote-control electronics and DIY hobbyist was surprised by a model airplane they built, powered by a pair of PC air duster engines."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-rtx-5060-gaming-pc-costs-less-than-the-steam-machine-grab-the-ibuypower-slate-prebuilt-pc-with-massive-usd500-discount",
    "domain": "AI 算力 / 半导体",
    "title": "This RTX 5060 gaming PC costs less than the Steam Machine",
    "url": "https://www.tomshardware.com/pc-components/this-rtx-5060-gaming-pc-costs-less-than-the-steam-machine-grab-the-ibuypower-slate-prebuilt-pc-with-massive-usd500-discount",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T21:27:30+00:00",
    "summary": "Best Buy knocks $500 off the iBUYPOWER Slate, bringing this RTX 5060-powered gaming desktop down to $899 with a Ryzen 5 processor, 16GB of DDR5 memory, and a 1TB SSD"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-november-7-2026-micron-roadmap-apples-touchscreen-ambitions-globalfoundries-interview-and-much-more",
    "domain": "AI 算力 / 半导体",
    "title": "This week in Tom's Hardware Premium: November 7, 2026",
    "url": "https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-november-7-2026-micron-roadmap-apples-touchscreen-ambitions-globalfoundries-interview-and-much-more",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T15:00:00+00:00",
    "summary": "This week on Tom's Hardware Premium, we've published in-depth interviews, roadmaps, and features you won't want to miss."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-intelligence-believes-jensen-huang-had-romantic-relationship-with-chinese-spy-in-honeypot-operation-spy-suspect-linked-to-company-accused-of-smuggling-usd2-billion-in-ai-chips",
    "domain": "AI 算力 / 半导体",
    "title": "US intelligence believes Jensen Huang had affair with Chinese spy in honeypot operation",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-intelligence-believes-jensen-huang-had-romantic-relationship-with-chinese-spy-in-honeypot-operation-spy-suspect-linked-to-company-accused-of-smuggling-usd2-billion-in-ai-chips",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:47:37+00:00",
    "summary": "U.S. intelligence sources suggest that Nvidia chief Jensen Huang was targeted by Chinese intelligence in a 'honeypot' operation involving Megaspeed executive Alice Huang."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/grab-a-new-elegoo-3d-printer-from-as-little-as-usd159-right-now-thanks-to-black-friday-sale-now-live-early-discounts-mean-you-can-score-up-to-54-percent-off-filament-and-resin-machines-perfect-for-pro-hobbyists-and-beginners",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a new Elegoo 3D printer from as little as $159 right now, thanks to Black Friday sale, now live",
    "url": "https://www.tomshardware.com/3d-printing/grab-a-new-elegoo-3d-printer-from-as-little-as-usd159-right-now-thanks-to-black-friday-sale-now-live-early-discounts-mean-you-can-score-up-to-54-percent-off-filament-and-resin-machines-perfect-for-pro-hobbyists-and-beginners",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:30:00+00:00",
    "summary": "Elegoo's November sale has begun, and you can score savings of up to 54% on a new printer for the entire month, as long as the stock lasts."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/teamgroup-ga-pro-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "TeamGroup GA Pro 2TB SSD Review: A faltering attempt at a mid-range PCIe 5.0 SSD",
    "url": "https://www.tomshardware.com/pc-components/ssds/teamgroup-ga-pro-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:00:00+00:00",
    "summary": "The TeamGroup GA Pro mostly misses. Decent QD8 and steady-state writes can’t make up for weak overall performance, poor efficiency, and high temps."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidias-jensen-huang-officially-called-to-congress-due-to-reports-of-a-chinese-spy-plot-officials-mention-growing-concerns-over-national-security",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang officially called to Congress due to reports of a Chinese spy plot",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidias-jensen-huang-officially-called-to-congress-due-to-reports-of-a-chinese-spy-plot-officials-mention-growing-concerns-over-national-security",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T13:30:00+00:00",
    "summary": "Nvidia's Jensen Huang officially called to Congress due to reports of Chinese plot — officials mention growing concerns over national security"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC denies exploring 3D DRAM at Nvidia's request",
    "url": "https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T13:00:00+00:00",
    "summary": "Nvidia reportedly asks TSMC to produce '3D DRAM' to address memory shortages."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/enthusiast-abandons-self-hosted-microsoft-exchange-after-27-years-moving-mailboxes-to-microsoft-365-replaces-final-on-premises-relay-with-postfix-starttls-and-lets-encrypt-certificates",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast abandons self-hosted Microsoft Exchange after 27 years, moving mailboxes to Microsoft 365",
    "url": "https://www.tomshardware.com/software/enthusiast-abandons-self-hosted-microsoft-exchange-after-27-years-moving-mailboxes-to-microsoft-365-replaces-final-on-premises-relay-with-postfix-starttls-and-lets-encrypt-certificates",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T12:30:00+00:00",
    "summary": "A homelab enthusiast is retiring a Microsoft Exchange installation that began with Exchange 5.5 on Windows NT 4 in 1999. After migrating mailboxes to Microsoft 365, he kept Exchange 2019 running to re"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/new-bluetooth-high-data-throughput-may-finally-satisfy-audiophiles-bluetooth-hdt-offers-a-maximum-bandwidth-of-7-5mbps-allowing-true-lossless-transmission",
    "domain": "AI 算力 / 半导体",
    "title": "New Bluetooth High Data Throughput may finally satisfy audiophiles",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/new-bluetooth-high-data-throughput-may-finally-satisfy-audiophiles-bluetooth-hdt-offers-a-maximum-bandwidth-of-7-5mbps-allowing-true-lossless-transmission",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T12:30:00+00:00",
    "summary": "Bluetooth HDT can offer a maximum bandwidth of 7.5 Mbps, allowing Bluetooth to be used with more sophisticated devices or big lossless audio files."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/ea-producer-found-20-000-archival-media-assets-in-secret-physical-vault-at-its-hq-betacam-vhs-and-d1-tapes-among-6000-assets-digitized-to-remaster-seven-classic-games",
    "domain": "AI 算力 / 半导体",
    "title": "EA producer found 20,000 archival media assets in secret physical vault at its HQ",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/ea-producer-found-20-000-archival-media-assets-in-secret-physical-vault-at-its-hq-betacam-vhs-and-d1-tapes-among-6000-assets-digitized-to-remaster-seven-classic-games",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T11:30:00+00:00",
    "summary": "The discovery of thousands of archival media assets led to the creation of Anniversary Editions of some classic titles."
  },
  {
    "id": "hn:50398513",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang Summoned by Congress over Chinese Espionage Concerns",
    "url": "https://arstechnica.com/tech-policy/2026/11/nvidia-ceo-jensen-huang-summoned-by-congress-over-chinese-espionage-concerns/",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-06T21:04:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50399226",
    "domain": "AI 算力 / 半导体",
    "title": "China’s Top Spy Agency Recruited Woman Who Targeted Jensen Huang",
    "url": "https://www.nytimes.com/2026/11/06/us/politics/chinese-spy-agency-nvidia-jensen-huang.html",
    "source": "jbegley",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-06T22:16:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50372759",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia store pulls RTX 5080 following RTX 5090 removal, prices rise to 2.2X MSRP",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-store-quietly-pulls-the-rtx-5080-following-rtx-5090-removal-street-prices-climb-to-2-2x-over-msrp",
    "source": "akyuu",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-04T23:12:29+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/the-countdown-to-q-day-has-begun/",
    "domain": "AI 算力 / 半导体",
    "title": "The Countdown to Q-Day Has Begun",
    "url": "https://www.eetimes.com/the-countdown-to-q-day-has-begun/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T21:00:00+00:00",
    "summary": "Will a quantum computer break blockchain cryptography in just two years' time? The post The Countdown to Q-Day Has Begun appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/cosmic-at-semicon-europa-2026-advancing-high-complexity-semiconductor-test-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "Cosmic at SEMICON Europa 2026: Advancing High-Complexity Semiconductor Test Solutions",
    "url": "https://www.eetimes.com/cosmic-at-semicon-europa-2026-advancing-high-complexity-semiconductor-test-solutions/",
    "source": "Cosmic Group",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T18:48:20+00:00",
    "summary": "ALTOPASCIO, Italy — Nov. 9, 2026 — Cosmic Group will participate in SEMICON Europa 2026 in Munich, held concurrently with electronica from Nov. 10 to 13, 2026. Cosmic will be located at booth C1255. R"
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-amd-mix-quantum-and-ai-at-u-s-national-lab/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM, AMD Mix Quantum and AI at U.S. National Lab",
    "url": "https://www.eetimes.com/ibm-amd-mix-quantum-and-ai-at-u-s-national-lab/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T14:10:57+00:00",
    "summary": "IBM, AMD, and Oak Ridge launch hybrid quantum-classical system to accelerate quantum-error correction research ahead of 2028. The post IBM, AMD Mix Quantum and AI at U.S. National Lab appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/europe-chip-industry-perfect-storm-or-perfect-timing/",
    "domain": "AI 算力 / 半导体",
    "title": "Europe’s Chip Industry: Perfect Storm or Perfect Timing?",
    "url": "https://www.eetimes.com/europe-chip-industry-perfect-storm-or-perfect-timing/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T09:53:05+00:00",
    "summary": "At SEMICON Europa 2026, Europe’s chip industry will confront a “perfect storm” of geopolitical, technological, and competitive pressures. The post Europe’s Chip Industry: Perfect Storm or Perfect Timi"
  },
  {
    "id": "rss:https://www.eetimes.com/ee-times-magazine-november-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "EE Times Magazine – November 2026",
    "url": "https://www.eetimes.com/ee-times-magazine-november-2026/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-05T22:30:00+00:00",
    "summary": "This edition of EE Times Magazine explores advances in semiconductor manufacturing and packaging, farm autonomy, and Canada’s efforts to commercialize emerging technologies. The post EE Times Magazine"
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1467,
    "published_at": "2026-10-13T16:03:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50261319",
    "domain": "大厂 AI 动态",
    "title": "Genie 4",
    "url": "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1044,
    "published_at": "2026-10-27T16:06:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50276792",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1019,
    "published_at": "2026-10-28T17:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50403097",
    "domain": "大厂 AI 动态",
    "title": "Every Mac comes with an (undocumented) family member classifier",
    "url": "https://8rank.ai/game/apple-intelligence-personal-knowledge-graph",
    "source": "infwhispers",
    "platform": "hackernews",
    "points": 856,
    "published_at": "2026-11-07T09:46:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363461",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)",
    "url": "https://news.ycombinator.com/item?id=50363461",
    "source": "jameslk",
    "platform": "hackernews",
    "points": 734,
    "published_at": "2026-11-04T10:10:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50411961",
    "domain": "大厂 AI 动态",
    "title": "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU",
    "url": "https://github.com/synchopate/llama-modchip",
    "source": "joshcsimmons",
    "platform": "hackernews",
    "points": 429,
    "published_at": "2026-11-08T10:22:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392118",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.2 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 368,
    "published_at": "2026-11-06T13:35:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122431",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console",
    "url": "https://github.com/cobanov/PS5LM",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 375,
    "published_at": "2026-10-16T18:32:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-10-29T12:41:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-10-16T14:18:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074869",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon for Robotics",
    "url": "https://developers.googleblog.com/gemini-4-argon-for-robotics/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 235,
    "published_at": "2026-10-13T16:55:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50355504",
    "domain": "大厂 AI 动态",
    "title": "Google researchers demand freedom to tell the world what they know about AI",
    "url": "https://www.washingtonpost.com/technology/2026/11/03/google-deepmind-staff-protest-lifetime-ban-criticizing-company/",
    "source": "nsagent",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-11-03T17:55:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1029595/full-text-jensen-huang-affair-memo-nvidia",
    "domain": "大厂 AI 动态",
    "title": "Here’s the full text of Jensen Huang’s memo to Nvidia",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1029595/full-text-jensen-huang-affair-memo-nvidia",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T22:54:50+00:00",
    "summary": "On Sunday, Nvidia announced it was launching an investigation into CEO Jensen Huang's relationship with Alice Huang, an AI executive and agent of the Chinese government. In addition to the Board of Di"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1029579/soul-glo-diaspora-problems-hardcore-punk-review",
    "domain": "大厂 AI 动态",
    "title": "Soul Glo’s Diaspora Problems is a hardcore record like no other",
    "url": "https://www.theverge.com/entertainment/1029579/soul-glo-diaspora-problems-hardcore-punk-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T22:37:22+00:00",
    "summary": "Soul Glo has a new record called NA I'M GON GRAB ALLAT coming out in January, and I, for one, can not wait. While two singles have dropped, it's not enough to truly tide me over, so I've been revisiti"
  },
  {
    "id": "rss:https://www.theverge.com/games/1029557/epic-games-launcher-is-coming-to-steamos",
    "domain": "大厂 AI 动态",
    "title": "Epic Games Launcher is coming to SteamOS",
    "url": "https://www.theverge.com/games/1029557/epic-games-launcher-is-coming-to-steamos",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T20:52:05+00:00",
    "summary": "In October, Epic Games said that it was \"investigating\" making Fortnite compatible with Valve's Linux-based SteamOS. At the time, Epic Games Launcher was in preview, but SteamOS was not specifically l"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1029562/nvidia-investigating-jensen-huang-relationship-chinese-spy",
    "domain": "大厂 AI 动态",
    "title": "Nvidia is investigating Jensen Huang’s relationship with an alleged Chinese spy",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1029562/nvidia-investigating-jensen-huang-relationship-chinese-spy",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T20:22:39+00:00",
    "summary": "Nvidia has announced that it is opening an investigation into CEO Jensen Huang and his relationship with Megaspeed executive Alice Huang, who was reportedly recruited by China's Ministry of State Secu"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1029552/apple-siri-ai-agentic",
    "domain": "大厂 AI 动态",
    "title": "Apple is racing to make Siri more agentic",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1029552/apple-siri-ai-agentic",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T19:18:19+00:00",
    "summary": "Bloomberg's Mark Gurman says CEO John Ternus is pressuring AI czar Craig Federighi to accelerate the Siri roadmap and deliver a powerful AI agent that can compete with OpenAI's Dots or Meta's Muse. Wh"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1029533/elvis-eminem-suno-ai-music-clone-lawsuit",
    "domain": "大厂 AI 动态",
    "title": "Elvis and Eminem rights holders are suing Suno",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1029533/elvis-eminem-suno-ai-music-clone-lawsuit",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T17:23:19+00:00",
    "summary": "Suno is facing yet another pair of lawsuits. A group of rights holders of Elvis Presley's music and the publisher of some of Eminem's biggest records are suing the AI music company, claiming it illega"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1029019/apple-macbook-air-13-15-inch-m5-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Apple’s M5 MacBook Air is down to its lowest price since July",
    "url": "https://www.theverge.com/gadgets/1029019/apple-macbook-air-13-15-inch-m5-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T16:00:00+00:00",
    "summary": "The latest 13-inch MacBook Air is currently available for $1,099.99, marking the second time we’ve seen this $200 discount following the company’s hefty price increases over the summer. Although the b"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1029526/chatbots-might-be-coming-to-apples-homeview",
    "domain": "大厂 AI 动态",
    "title": "Chatbots might be coming to Apple’s HomeView",
    "url": "https://www.theverge.com/tech/1029526/chatbots-might-be-coming-to-apples-homeview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T15:00:30+00:00",
    "summary": "Code in the iOS 27.3 beta suggests that Apple could add support for chatbots to its smart home hub. There's a flag listed for a \"Conversational Apps\" category. While there are no details about what ap"
  },
  {
    "id": "rss:https://www.theverge.com/column/1026252/video-media-news-tiktok-pivot",
    "domain": "大厂 AI 动态",
    "title": "There’s no slowing down media’s pivot-to-video 2.0",
    "url": "https://www.theverge.com/column/1026252/video-media-news-tiktok-pivot",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T13:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on the pressures of creating content for the internet, follow Mia Sato. The Stepback arrives i"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1023230/the90-gem-necklace-hands-on-impressions",
    "domain": "大厂 AI 动态",
    "title": "The UV-tracking Gem made me rethink how sunlight affects my health, not just my appearance",
    "url": "https://www.theverge.com/tech/1023230/the90-gem-necklace-hands-on-impressions",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T17:00:00+00:00",
    "summary": "With temperatures rising to the 90s in Los Angeles, avoiding the heat wasn't exactly an option while I was at a relative's outdoor party in August. So I sat beneath a patio umbrella with a powerful fa"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/is-jensen-huangs-job-on-the-line-yales-jeffrey-sonnenfeld-estimates-its-about-a-50-50/",
    "domain": "大厂 AI 动态",
    "title": "Is Jensen Huang’s job on the line? Yale’s Jeffrey Sonnenfeld estimates it’s “about a 50-50”",
    "url": "https://techcrunch.com/2026/11/08/is-jensen-huangs-job-on-the-line-yales-jeffrey-sonnenfeld-estimates-its-about-a-50-50/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:26:29+00:00",
    "summary": "Nvidia’s board is investigating Jensen Huang over his relationship with a suspected Chinese spy, and Yale’s Jeffrey Sonnenfeld thinks it’s roughly a coin flip whether Huang stays on as CEO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/apps-to-distract-you-from-the-endless-cycle-of-doomscrolling/",
    "domain": "大厂 AI 动态",
    "title": "Apps to distract you from the endless cycle of doomscrolling",
    "url": "https://techcrunch.com/2026/11/08/apps-to-distract-you-from-the-endless-cycle-of-doomscrolling/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T22:00:00+00:00",
    "summary": "It's hard to break the cycle of doomscrolling, but there are plenty of apps that can help you spend more time on content that’s engaging and productive."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/nvidia-says-its-investigating-ceo-jensen-huangs-relationship-with-possible-chinese-spy/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia will investigate CEO Jensen Huang’s relationship with possible Chinese spy",
    "url": "https://techcrunch.com/2026/11/08/nvidia-says-its-investigating-ceo-jensen-huangs-relationship-with-possible-chinese-spy/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T21:00:11+00:00",
    "summary": "In a memo to the company, Huang admitted that he had an affair."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/if-snaps-specs-are-still-ridiculously-expensive-theyre-also-a-lot-more-comfortable-than-they-used-to-be/",
    "domain": "大厂 AI 动态",
    "title": "If Snap’s Specs are still ridiculously expensive, they’re also a lot more comfortable than they used to be",
    "url": "https://techcrunch.com/2026/11/08/if-snaps-specs-are-still-ridiculously-expensive-theyre-also-a-lot-more-comfortable-than-they-used-to-be/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T21:00:00+00:00",
    "summary": "Snap's Specs, which have been in development for many years now, are going to market this fall. Will they be a hit with users?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/coordinated-disturbances-haunt-grids-worldwide-heres-how-researchers-solved-the-mystery/",
    "domain": "大厂 AI 动态",
    "title": "Coordinated disturbances haunt grids worldwide. Here’s how researchers solved the mystery.",
    "url": "https://techcrunch.com/2026/11/08/coordinated-disturbances-haunt-grids-worldwide-heres-how-researchers-solved-the-mystery/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T20:30:00+00:00",
    "summary": "Mystery solved: Coordinated power drops have been haunting power grid worldwide, but a team of researchers in Germany found the culprit."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/sequoia-partners-reportedly-blindsided-when-roelof-botha-joined-spacex-board/",
    "domain": "大厂 AI 动态",
    "title": "Sequoia partners reportedly blindsided when Roelof Botha joined SpaceX board",
    "url": "https://techcrunch.com/2026/11/08/sequoia-partners-reportedly-blindsided-when-roelof-botha-joined-spacex-board/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T19:51:30+00:00",
    "summary": "A new report claims Sequoia's recent changes undo the legacy of the firm's former steward."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/snl-has-a-new-impression-of-elon-musk-the-worst-thing-south-africa-has-ever-done/",
    "domain": "大厂 AI 动态",
    "title": "SNL has a new impression of Elon Musk, ‘the worst thing South Africa has ever done’",
    "url": "https://techcrunch.com/2026/11/08/snl-has-a-new-impression-of-elon-musk-the-worst-thing-south-africa-has-ever-done/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T18:00:04+00:00",
    "summary": "SNL seems to have its knives out for tech executives."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/the-ex-secret-service-agent-who-flipped-a-hacker-is-now-raising-a-second-250m-cybersecurity-fund/",
    "domain": "大厂 AI 动态",
    "title": "He arrested a hacker, then spent 18 months clearing his own name. Now he’s a cybersecurity VC.",
    "url": "https://techcrunch.com/2026/11/08/the-ex-secret-service-agent-who-flipped-a-hacker-is-now-raising-a-second-250m-cybersecurity-fund/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T17:30:00+00:00",
    "summary": "Stephen Ward, a former Secret Service agent and Home Depot CISO, is preparing a second fund of roughly $250 million for Brightmind Partners."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/techcrunch-mobility-the-cybertruck-experiment-is-over/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: The Cybertruck experiment is over",
    "url": "https://techcrunch.com/2026/11/08/techcrunch-mobility-the-cybertruck-experiment-is-over/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T17:02:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/08/ninjas-autobarista-is-impressively-versatile-but-one-feature-was-a-dealbreaker-for-me/",
    "domain": "大厂 AI 动态",
    "title": "Ninja’s AutoBarista is impressively versatile, but one feature was a dealbreaker for me",
    "url": "https://techcrunch.com/2026/11/08/ninjas-autobarista-is-impressively-versatile-but-one-feature-was-a-dealbreaker-for-me/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T15:00:00+00:00",
    "summary": "The AutoBarista's \"Grind iQ\" technology allows the machine to analyze your coffee beans to inform how it pulls a shot of espresso."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/after-the-midterms-things-are-looking-rocky-for-elon-musk-and-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "After the midterms, things are looking rocky for Elon Musk and data centers",
    "url": "https://techcrunch.com/2026/11/07/after-the-midterms-things-are-looking-rocky-for-elon-musk-and-data-centers/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T22:07:22+00:00",
    "summary": "On Equity, we unpacked what the midterms mean for the tech industry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/",
    "domain": "大厂 AI 动态",
    "title": "Megaspeed exec was recruited to spy on Nvidia CEO, according to US intelligence memo",
    "url": "https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T21:17:08+00:00",
    "summary": "A memo circulated earlier this year reportedly claimed that China’s Ministry of State Security recruited a female technology executive to spy on Nvidia's CEO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/parents-want-safer-phones-for-kids-these-companies-are-answering-the-call/",
    "domain": "大厂 AI 动态",
    "title": "Parents want safer phones for kids. These companies are answering the call.",
    "url": "https://techcrunch.com/2026/11/07/parents-want-safer-phones-for-kids-these-companies-are-answering-the-call/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T19:00:00+00:00",
    "summary": "As parents look for alternatives to unrestricted smartphones, a growing number of companies are building phones designed specifically for kids, from feature-limited mobile devices to minimalist home p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/binance-cfo-is-leaving-to-pursue-a-new-venture-after-6-3-billion-hack/",
    "domain": "大厂 AI 动态",
    "title": "Binance CFO is leaving to ‘pursue a new venture’ after $6.3 billion hack",
    "url": "https://techcrunch.com/2026/11/07/binance-cfo-is-leaving-to-pursue-a-new-venture-after-6-3-billion-hack/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T17:24:07+00:00",
    "summary": "The announcement comes barely more than a week after hackers stole $6.3 billion worth of cryptocurrency from Binance users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/07/amazons-new-basic-kindle-proves-you-dont-need-all-the-bells-and-whistles/",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s new basic Kindle proves you don’t need all the bells and whistles",
    "url": "https://techcrunch.com/2026/11/07/amazons-new-basic-kindle-proves-you-dont-need-all-the-bells-and-whistles/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T17:18:00+00:00",
    "summary": "Amazon's redesigned basic Kindle costs more than before, but its lighter build and improved display make a compelling case for skipping the pricier models."
  },
  {
    "id": "rss:https://stratechery.com/2026/jensen-huangs-affair-the-culper-report-huangs-righteousness/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang’s Affair, The Culper Report, Huang’s Righteousness",
    "url": "https://stratechery.com/2026/jensen-huangs-affair-the-culper-report-huangs-righteousness/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T11:00:00+00:00",
    "summary": "Nvidia CEO Jensen Huang admitted to an affair with a Chinese spy, and that might not be the end of his troubles. I hope he survives, but his influence will never be the same."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/physicists-listened-to-electrical-noise-to-crack-a-superconductor-mystery/",
    "domain": "大厂 AI 动态",
    "title": "Physicists listened to electrical noise to crack a superconductor mystery",
    "url": "https://arstechnica.com/science/2026/11/physicists-listened-to-electrical-noise-to-crack-a-superconductor-mystery/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T12:15:31+00:00",
    "summary": "Tuning in to electronic noise can tell us whether electrons have paired up or not."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/the-migration-that-transformed-africas-languages-genes-and-cultures/",
    "domain": "大厂 AI 动态",
    "title": "The Bantu expansion changed Africa. Scientists are still tracing how.",
    "url": "https://arstechnica.com/science/2026/11/the-migration-that-transformed-africas-languages-genes-and-cultures/",
    "source": "Katarina Zimmer, Knowable Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T12:15:55+00:00",
    "summary": "Genes and archaeology are revealing how Bantu speakers spread across much of Africa."
  },
  {
    "id": "rss:https://www.producthunt.com/products/higgsfield",
    "domain": "大厂 AI 动态",
    "title": "Higgsfield Miracle",
    "url": "https://www.producthunt.com/products/higgsfield",
    "source": "Rohan Chaubey",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T18:28:56+00:00",
    "summary": "Edit any part of a video without changing the rest Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/clipspal",
    "domain": "大厂 AI 动态",
    "title": "ClipsPal",
    "url": "https://www.producthunt.com/products/clipspal",
    "source": "Dan Kulkov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T13:34:07+00:00",
    "summary": "AI video editor that edits your talking-head videos Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/egoist-ai-passport",
    "domain": "大厂 AI 动态",
    "title": "Egoist AI Passport",
    "url": "https://www.producthunt.com/products/egoist-ai-passport",
    "source": "Erin McGurk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T16:27:33+00:00",
    "summary": "Secure and share your personal data with AI tools. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/skuttr",
    "domain": "大厂 AI 动态",
    "title": "skuttr",
    "url": "https://www.producthunt.com/products/skuttr",
    "source": "Deborah Choi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:14:39+00:00",
    "summary": "Type one sentence, get a Reel from your camera roll Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/github",
    "domain": "大厂 AI 动态",
    "title": "GitHub New PR Overview",
    "url": "https://www.producthunt.com/products/github",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T03:34:44+00:00",
    "summary": "See what's blocking a PR before you scroll Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/cue-voice-keyboard",
    "domain": "大厂 AI 动态",
    "title": "Cue",
    "url": "https://www.producthunt.com/products/cue-voice-keyboard",
    "source": "Ibrahim Hassan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T20:08:44+00:00",
    "summary": "AI meeting notes, prep Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/north-5",
    "domain": "大厂 AI 动态",
    "title": "Nörth",
    "url": "https://www.producthunt.com/products/north-5",
    "source": "Josh Nies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-08T20:16:37+00:00",
    "summary": "Natural, peer-to-peer collaboration for remote work Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/zigzag-browser",
    "domain": "大厂 AI 动态",
    "title": "Zigzag Browser",
    "url": "https://www.producthunt.com/products/zigzag-browser",
    "source": "Zigao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T14:38:06+00:00",
    "summary": "The polished, native Mac browser for life after Arc Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/agent-clan",
    "domain": "大厂 AI 动态",
    "title": "Agent Clan",
    "url": "https://www.producthunt.com/products/agent-clan",
    "source": "鄭策（TSETSE）",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-07T17:52:26+00:00",
    "summary": "Command your Claude Code and Codex agents with gestures Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/118799",
    "domain": "大厂 AI 动态",
    "title": "双十一 | 少数派会员、正版软件、付费栏目限时优惠",
    "url": "https://sspai.com/post/118799",
    "source": "福利派",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T08:24:03+00:00",
    "summary": "多款付费栏目和正版软件上新，以及口碑、质量都非常优秀的现有产品优惠活动，快来看看有没有你需要的吧。查看全文"
  },
  {
    "id": "hn:50381623",
    "domain": "股票",
    "title": "Nasdaq plummets 4% into correction territory",
    "url": "https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 227,
    "published_at": "2026-11-05T17:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50306008",
    "domain": "股票",
    "title": "US tech stocks see sharp falls over AI cost fears",
    "url": "https://www.bbc.co.uk/news/articles/cvwy72e0n72yo",
    "source": "mindracer",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-30T16:13:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50346153",
    "domain": "股票",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 236,
    "published_at": "2026-11-03T00:08:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50051583",
    "domain": "股票",
    "title": "Research Firm Calls Anthropic's IPO 'Unprecedented Test of Investor Gullibity'",
    "url": "https://www.cnbc.com/2026/10/07/anthropic-will-be-most-ridiculous-ipo-of-year-analyst-says.html",
    "source": "m463",
    "platform": "hackernews",
    "points": 244,
    "published_at": "2026-10-12T05:03:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342284",
    "domain": "股票",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-11-02T19:27:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384822",
    "domain": "股票",
    "title": "$2.5T has been wiped from US stocks",
    "url": "https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 164,
    "published_at": "2026-11-05T21:39:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50382179",
    "domain": "股票",
    "title": "Nasdaq Sinks 5% as Investors Retreat from AI Trade After Election",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-05-2026",
    "source": "armcat",
    "platform": "hackernews",
    "points": 163,
    "published_at": "2026-11-05T18:00:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50401029",
    "domain": "股票",
    "title": "The AI sell-off compared to well-known stock market crashes",
    "url": "https://www.kadoa.com/companies/insights/ai-selloff-perspective",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-11-07T02:20:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50151376",
    "domain": "股票",
    "title": "The obscure trust looming over Anthropic's IPO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-private-trust-188f41f7?st=RtdGHg&reflink=desktopwebshare_permalink",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 154,
    "published_at": "2026-10-19T12:06:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386909",
    "domain": "股票",
    "title": "Investors wipe $2.5T off Nasdaq as blue tsunami prompts AI fears",
    "url": "https://www.reuters.com/legal/transactional/ai-data-center-stocks-slip-democratic-sweep-clouds-expansion-plans-2026-11-05/",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-11-06T01:11:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50389401",
    "domain": "股票",
    "title": "Global stocks tumble as AI panic grips markets after Democrats' midterm success",
    "url": "https://www.theguardian.com/business/live/2026/nov/06/global-stocks-tumble-ai-panic-markets-democrats-midterms-success-jobs-oil-dollar-latest-news-updates",
    "source": "drayfield",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-06T07:52:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384382",
    "domain": "股票",
    "title": "Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896",
    "url": "https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-05T20:58:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50280197",
    "domain": "股票",
    "title": "Alphabet Announces Third Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q3/2026q3-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-10-28T20:11:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50362274",
    "domain": "股票",
    "title": "AI stocks slide as Texas governor result raises data center risks",
    "url": "https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html",
    "source": "1659447091",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-11-04T07:00:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385642",
    "domain": "股票",
    "title": "Michael Burry says Anthropic is 'betting its existence' on optimism",
    "url": "https://www.businessinsider.com/michael-burry-anthropic-ipo-outlook-ant-big-short-2026-11",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-11-05T22:49:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386483",
    "domain": "股票",
    "title": "Major Investors Are Skeptical Anthropic IPO Can Achieve $1.5T Valuation",
    "url": "https://www.wsj.com/finance/major-investors-are-skeptical-anthropic-ipo-can-achieve-1-5-trillion-valuation-ca965d8b",
    "source": "sandinmyjoints",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-11-06T00:17:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50352405",
    "domain": "股票",
    "title": "US Hedge Funds Just Sold Every AI Stock They Bought Since 2025",
    "url": "https://finance.yahoo.com/markets/stocks/articles/us-hedge-funds-just-sold-113114644.html",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-03T14:27:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50351712",
    "domain": "股票",
    "title": "Anthropic's IPO Filing Warns It May Be 'Imminently' Close to RSI",
    "url": "https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-03T13:26:43+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "domain": "股票",
    "title": "The Insatiable Demand for Alpha",
    "url": "https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T17:59:24+00:00",
    "summary": "Why a market shakedown could leave the biggest pod shops stronger"
  },
  {
    "id": "hn:50326281",
    "domain": "股票",
    "title": "Ant: Can unprecedented revenue growth outrun irresponsibly large investment",
    "url": "https://leonlins.com/writing/anthropic_ipo",
    "source": "avoidboringppl",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T14:56:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50295611",
    "domain": "股票",
    "title": "Reddit will force everyone to log in",
    "url": "https://www.theverge.com/tech/1022571/reddit-login-requirement-q3-2026-earnings",
    "source": "timpera",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-29T20:43:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:50323575",
    "domain": "股票",
    "title": "We're Living in the Age of the Imperial CEO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-dual-class-stock-founder-control-4c43a56d",
    "source": "pretext",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T08:09:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50251762",
    "domain": "股票",
    "title": "Anthropic Is the Most Ridiculous IPO of 2026 [pdf]",
    "url": "https://www.newconstructs.com/wp-content/uploads/2026/10/Anthropic-Is-The-Most-Ridiculous-IPO-of-2026.pdf",
    "source": "simonebrunozzi",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T22:06:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50243343",
    "domain": "股票",
    "title": "Anthropic rushing IPO before AI bubble bursts",
    "url": "https://nypost.com/2026/10/23/business/wall-street-is-urging-anthropic-openai-to-do-their-ipos-in-a-hurry-heres-why/",
    "source": "nothrowaways",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T13:30:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50167295",
    "domain": "股票",
    "title": "Data center stocks slide as Korea IPO plunges 30%, pressuring tech sentiment",
    "url": "https://www.cnbc.com/2026/10/20/data-center-stocks-slide-as-korea-ipo-plunges-30percent-pressuring-tech-sentiment.html",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-20T14:50:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50142772",
    "domain": "股票",
    "title": "How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill",
    "url": "https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-10-18T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50071744",
    "domain": "股票",
    "title": "Sprout Pi Mainboard – A modern, RP2350-powered motherboard for iPods",
    "url": "https://www.crowdsupply.com/certain-things/sprout-pi-mainboard",
    "source": "esskay",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-13T13:49:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50171533",
    "domain": "股票",
    "title": "Anthropic S-1 Shows Red-Hot Growth, Risks and Computing Costs",
    "url": "https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1",
    "source": "mmmmmbop",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-20T19:34:39+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/follow-the-money-ece",
    "domain": "股票",
    "title": "Follow the Money",
    "url": "https://www.netinterest.co/p/follow-the-money-ece",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:48:55+00:00",
    "summary": "What six years and 300+ posts of Net Interest say about where finance is heading"
  },
  {
    "id": "hn:50082283",
    "domain": "股票",
    "title": "US Says Chinese Hackers Attacked DOJ, NASA, Federal Reserve, Senate",
    "url": "https://www.usatoday.com/story/news/politics/2026/08/26/chinese-hackers-cyberattack-us-government/91473585007/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-10-14T04:09:23+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/capital-wars",
    "domain": "股票",
    "title": "Capital Wars",
    "url": "https://www.netinterest.co/p/capital-wars",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:24:17+00:00",
    "summary": "CoreWeave and the Economics of a Data Center Build"
  },
  {
    "id": "rss:https://www.netinterest.co/p/me-and-my-agents",
    "domain": "股票",
    "title": "Me and My Agents",
    "url": "https://www.netinterest.co/p/me-and-my-agents",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:39:55+00:00",
    "summary": "Unleashing AI Agents on Bank Earnings"
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
    "id": "hn:50391456",
    "domain": "金融",
    "title": "Tesla to wind down Cybertruck production",
    "url": "https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 1155,
    "published_at": "2026-11-06T12:13:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385870",
    "domain": "金融",
    "title": "Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue",
    "url": "https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 521,
    "published_at": "2026-11-05T23:09:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:50154244",
    "domain": "金融",
    "title": "DeepSeek banned from U.S. federal civilian agencies under new DHS order",
    "url": "https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/",
    "source": "cmrdporcupine",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-10-19T16:16:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:50305573",
    "domain": "金融",
    "title": "The federated code forge",
    "url": "https://tangled.org/blog/forge/",
    "source": "zlliang",
    "platform": "hackernews",
    "points": 333,
    "published_at": "2026-10-30T15:44:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50414427",
    "domain": "金融",
    "title": "Tesla Hasn't Had a Successful New Product Launch Since JB Straubel Stepped Down",
    "url": "https://cleantechnica.com/2026/11/07/tesla-hasnt-had-a-successful-new-product-launch-since-jb-straubel-stepped-down-as-cto/",
    "source": "gumby",
    "platform": "hackernews",
    "points": 199,
    "published_at": "2026-11-08T16:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-20T22:21:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-10-17T14:22:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50260526",
    "domain": "金融",
    "title": "A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies",
    "url": "https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-10-27T15:09:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236073",
    "domain": "金融",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50059446",
    "domain": "金融",
    "title": "Feds got warrants to use fake cell towers to hunt down Don Lemon's producer",
    "url": "https://www.wired.com/story/feds-got-warrants-to-use-fake-cell-towers-to-hunt-down-don-lemons-producer/",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 196,
    "published_at": "2026-10-12T17:08:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50190168",
    "domain": "金融",
    "title": "Epic Games Inc v Apple Inc",
    "url": "https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552",
    "source": "Mayzie",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-10-22T01:52:03+00:00",
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
    "id": "hn:50387406",
    "domain": "金融",
    "title": "Tesla and SpaceX lose over $420B in combined market cap in the two days",
    "url": "https://techlaws.pages.dev/tesla-and-spacex-lose-over-420b-in-combined-market-cap-in-the-two-days/",
    "source": "Pepitobombito",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-11-06T02:30:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 122,
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
    "points": 118,
    "published_at": "2026-10-14T03:28:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:50274706",
    "domain": "金融",
    "title": "Tesla Semi catches fire on I-880",
    "url": "https://electrek.co/2026/10/28/tesla-semi-fire-i-880-hayward-no-crash/",
    "source": "metadat",
    "platform": "hackernews",
    "points": 96,
    "published_at": "2026-10-28T14:54:07+00:00",
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
    "id": "hn:50278678",
    "domain": "金融",
    "title": "Show HN: A proof-of-concept formalization of the IRS federal tax forms",
    "url": "https://github.com/emmilco/us-tax-model",
    "source": "RGS1811",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-10-28T18:30:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50394771",
    "domain": "金融",
    "title": "Only 16% of U.S. fast-charging stations meet federal NEVI standards (open data)",
    "url": "https://chargingnear.me/data",
    "source": "parkgraph",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-06T16:45:10+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.08968",
    "domain": "金融",
    "title": "Portfolio-aware scenario transfer of reserve movements: evidence from Lloyd's syndicates",
    "url": "https://arxiv.org/abs/2611.08968",
    "source": "Colin Priest",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.08968v1 Announce Type: new Abstract: A claims-development movement on one portfolio may not transfer directly as a stress to another size. We estimate how to transfer such scenarios between"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.09208",
    "domain": "金融",
    "title": "The Network Adaptive Market Hypothesis: Detection, Attribution, and Network-Mediated Efficiency",
    "url": "https://arxiv.org/abs/2611.09208",
    "source": "Hitesh Kumar Sahu, Avishek Bhandari, Ipsita Parida",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.09208v1 Announce Type: new Abstract: We propose the Network Adaptive Market Hypothesis (NAMH), a novel extension of the adaptive markets framework that conceptualizes market efficiency as a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.09213",
    "domain": "金融",
    "title": "Joint modelling of financial cost and carbon footprint in motor insurance claims: a BINAR(1) decision framework for circular auto parts adoption",
    "url": "https://arxiv.org/abs/2611.09213",
    "source": "Charles Minier (CNP, LSAF), St\\'ephane Loisel (CNAM Paris), Renata Alcoforado (UFPE, ULISBOA)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.09213v1 Announce Type: new Abstract: Motor insurance claims management increasingly faces a dual objective: controlling claim costs while reducing greenhouse-gas emissions associated with v"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.09286",
    "domain": "金融",
    "title": "The End-of-Day Reversal After 2019: A Pre-Registered Test on S&P 500 Stocks Excluding Heavily Traded Names",
    "url": "https://arxiv.org/abs/2611.09286",
    "source": "Alex Vidovich, Zivana Zerjal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.09286v1 Announce Type: new Abstract: Baltussen, Da and Soebhag (2025) document an end-of-day reversal in U.S. stocks through December 2019: intraday losers outperform intraday winners over "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.09337",
    "domain": "金融",
    "title": "Sanctions, Evasion, and Deterrence: Evidence from Speeding Enforcement",
    "url": "https://arxiv.org/abs/2611.09337",
    "source": "Romain Gauriot, Maria Wisniewska",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.09337v1 Announce Type: new Abstract: The design of sanctions plays a central role in shaping reoffending behavior. We study the effects of fixed monetary fines and accumulating penalty poin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.09751",
    "domain": "金融",
    "title": "Drift-invariant kernels for discount curve models",
    "url": "https://arxiv.org/abs/2611.09751",
    "source": "Andreas Celary, Zehra Eksi-Altay, Damir Filipovic, Paul Kr\\\"uhner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.09751v1 Announce Type: new Abstract: Kernel ridge regression estimates the discount curve as the minimizer of a pricing error plus a penalty given by the norm of a reproducing kernel Hilber"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.09834",
    "domain": "金融",
    "title": "The Logic of Factor Portfolios: Boolean Rules, Interactions, and Trading Costs",
    "url": "https://arxiv.org/abs/2611.09834",
    "source": "Ziyao Wang, Svetlozar T. Rachev, Frank J. Fabozzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.09834v1 Announce Type: new Abstract: Investors turn signals into holdings through decision rules: buy the top decile, hold stocks with high momentum and low volatility, exclude stocks that "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.08528",
    "domain": "金融",
    "title": "Price-Volume Correlations Are Always Zero",
    "url": "https://arxiv.org/abs/2611.08528",
    "source": "Victor Olkhov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.08528v1 Announce Type: cross Abstract: We argue that the use of the empirical time series of values, volumes, and prices of consecutive trades made during the averaging interval to calculat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.08701",
    "domain": "金融",
    "title": "Does a Trading Policy Need to Know What It Trades? Microstructure Invariance and Zero-Shot Transfer of Execution Policies",
    "url": "https://arxiv.org/abs/2611.08701",
    "source": "Hieu Tran, Hong Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.08701v1 Announce Type: cross Abstract: Execution algorithms are calibrated asset by asset, because the queues, trade rates and bid-ask spreads they face differ by orders of magnitude across"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.09012",
    "domain": "金融",
    "title": "Towards Robust Reinforcement Learning Market Making: Lessons from Loss Function Experimentation",
    "url": "https://arxiv.org/abs/2611.09012",
    "source": "Siddharth Nand, Bora Guney",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2611.09012v1 Announce Type: cross Abstract: Market makers play a vital role in ensuring efficient trade within financial markets. Recent literature has delved into training market-making systems"
  },
  {
    "id": "rss:https://arxiv.org/abs/2312.17123",
    "domain": "金融",
    "title": "Further Education During Unemployment",
    "url": "https://arxiv.org/abs/2312.17123",
    "source": "Pauline Leung, Zhuan Pei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2312.17123v5 Announce Type: replace Abstract: Evidence on the effectiveness of retraining unemployed U.S. workers primarily comes from evaluations of training programs, a narrow avenue for skill"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.23447",
    "domain": "金融",
    "title": "Systematic Covariance Envelopes from Wasserstein Geometry: Evidence from Language-Model Representations",
    "url": "https://arxiv.org/abs/2410.23447",
    "source": "Marcus Gawronsky, Chun-Sung Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2410.23447v3 Announce Type: replace Abstract: Firm characteristics are commonly represented as fixed vectors, even though evidence about firms' operations arrives as heterogeneous collections of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.18969",
    "domain": "金融",
    "title": "Correlation Ambiguity, Diversification Fragility, and Insurance Pricing",
    "url": "https://arxiv.org/abs/2603.18969",
    "source": "Peiyun Deng, Shunzhi Pang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2603.18969v2 Announce Type: replace Abstract: We study how correlation ambiguity affects insurance supply, investment, and pricing in a competitive market. An insurer jointly chooses underwritin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.09986",
    "domain": "金融",
    "title": "The Long-Only Minimum Variance Portfolio in a One-Factor Market: Theory and Asymptotics",
    "url": "https://arxiv.org/abs/2604.09986",
    "source": "Alec Kercheval, Ololade Sowunmi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2604.09986v2 Announce Type: replace Abstract: We study the long-only minimum variance (LOMV) portfolio, an object of interest going back to Markowitz, and the simplest non-trivial instance of qu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.22884",
    "domain": "金融",
    "title": "Universal Value-at-Risk superadditivity",
    "url": "https://arxiv.org/abs/2606.22884",
    "source": "Yuyu Chen, Liyuan Lin, Ruodu Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2606.22884v2 Announce Type: replace Abstract: Value-at-Risk (VaR) is a standard regulatory risk measure, and its failure of subadditivity is well known. Much less appreciated is that for suffici"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02978",
    "domain": "金融",
    "title": "Urban Reconstruction and Population Redistribution: Evidence from Tokyo after the Great Kanto Earthquake",
    "url": "https://arxiv.org/abs/2607.02978",
    "source": "Kota Ogasawara",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2607.02978v5 Announce Type: replace Abstract: This study examines the impact of the 1923 Great Kanto Earthquake on population distribution within Tokyo City. Using newly digitized census statist"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29669",
    "domain": "金融",
    "title": "Who Are a Firm's Economic Peers? Mapping a Latent Information Field with Language Models",
    "url": "https://arxiv.org/abs/2608.29669",
    "source": "Marcus Gawronsky, Chun-Sung Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2608.29669v3 Announce Type: replace Abstract: Identifying a firm's economic peers matters for benchmarking, risk measurement, and understanding return dependence, yet a diversified firm may have"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29692",
    "domain": "金融",
    "title": "Portfolio Risk Bounds without Cross-Asset Return Covariances: Distributional Fields from Language-Model Representations",
    "url": "https://arxiv.org/abs/2608.29692",
    "source": "Marcus Gawronsky, Chun-Sung Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2608.29692v2 Announce Type: replace Abstract: Portfolio risk assessment ordinarily relies on reliable estimates of cross-asset return covariances, which are difficult to obtain in short, high-di"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.15973",
    "domain": "金融",
    "title": "Shared AI Decision Interfaces and Credit Allocation in a Simulated Lending Market",
    "url": "https://arxiv.org/abs/2610.15973",
    "source": "Victoria Ruojie Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2610.15973v3 Announce Type: replace Abstract: Language-model agents can choose from a shared menu of actions. I ask whether the order of that menu, which carries no payoff-relevant information, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.15079",
    "domain": "金融",
    "title": "Isotonic Quantile Regression Averaging for uncertainty quantification of electricity price forecasts",
    "url": "https://arxiv.org/abs/2507.15079",
    "source": "Arkadiusz Lipiecki, Bartosz Uniejewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2507.15079v2 Announce Type: replace-cross Abstract: Quantifying the uncertainty of forecasting models is essential to assess and mitigate the risks associated with data-driven decisions, especia"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.02064",
    "domain": "金融",
    "title": "Quantitative Universal Approximation for Noisy Quantum Neural Networks",
    "url": "https://arxiv.org/abs/2604.02064",
    "source": "Lukas Gonon, Antoine Jacquier, Marcel Mordarski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-09T05:00:00+00:00",
    "summary": "arXiv:2604.02064v4 Announce Type: replace-cross Abstract: We prove a quantitative universal approximation theorem for noisy quantum neural networks (QNNs), with explicit non-asymptotic error bounds in"
  },
  {
    "id": "hn:50253630",
    "domain": "金融",
    "title": "The 'Buy, Borrow and Die' Wealth Strategy Has Become a $5T Market",
    "url": "https://www.wsj.com/finance/the-buy-borrow-and-die-wealth-strategy-has-become-a-5-trillion-market-d9149a9d",
    "source": "tysone",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-27T01:30:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50291902",
    "domain": "金融",
    "title": "Alphabet heads for a $500B drop in market value, biggest in its history",
    "url": "https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-10-29T16:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50372038",
    "domain": "金融",
    "title": "Harmony: Chat like Discord. Federated like email",
    "url": "https://mony.lol/",
    "source": "FinalDestiny",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-11-04T21:49:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50328462",
    "domain": "金融",
    "title": "US Jobs Pickup May Keep Fed on Track to Hike Rates Again",
    "url": "https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again",
    "source": "frank_clover",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-01T18:51:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50105900",
    "domain": "金融",
    "title": "Market selloff, rising rates test AI data centre deal boom",
    "url": "https://www.reuters.com/business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-10-15T16:17:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50161207",
    "domain": "金融",
    "title": "U.S. Supreme Court to review 1868 federal ban on home distilling of liquor",
    "url": "https://www.staradvertiser.com/2026/10/19/breaking-news/u-s-supreme-court-to-review-1868-federal-ban-on-home-distilling-of-liquor/",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-10-20T04:02:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50156189",
    "domain": "金融",
    "title": "The US orders every civilian agency to rip out DeepSeek, even tools built on it",
    "url": "https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-19T18:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50202671",
    "domain": "金融",
    "title": "AI compute is the new oil–and needs a new market",
    "url": "https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market",
    "source": "ijidak",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-22T23:45:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236506",
    "domain": "金融",
    "title": "F45 (Fedora 45) Final Is No-Go",
    "url": "https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EWDOYT6TOMFY4XPL5MJC2QWCDJBOR6MU/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-25T22:09:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-10-13T16:48:18+00:00",
    "summary": ""
  }
]
```
