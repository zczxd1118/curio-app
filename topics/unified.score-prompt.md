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

- 今日日期：`2026-08-05`
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
  "date": "2026-08-05",
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
    "points": 1663558,
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
    "points": 1310506,
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
    "points": 1048831,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1024358,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 1005194,
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
    "points": 594021,
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
    "points": 484442,
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
    "points": 433468,
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
    "points": 415804,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 403224,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 384757,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 256769,
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
    "points": 222163,
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
    "points": 209023,
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
    "points": 178508,
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
    "points": 163889,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 163108,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 137739,
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
    "points": 119266,
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
    "points": 92978,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 53111,
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
    "points": 47554,
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
    "points": 45285,
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
    "points": 40303,
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
    "points": 39866,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35062,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34019,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1kRW3zmEv8",
    "domain": "AI",
    "title": "【即梦AI】即梦Agent杀疯了！8种玩法带你速通即梦Agent智能体模式，赶紧来学！",
    "url": "http://www.bilibili.com/video/av115229962798190",
    "source": "SD电商教程",
    "platform": "bilibili",
    "points": 29961,
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
    "points": 29544,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 27387,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25994,
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
    "points": 22684,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 20146,
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
    "points": 19230,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "codex安装-",
    "platform": "bilibili",
    "points": 19002,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 18938,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 18043,
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
    "points": 17672,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 17396,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 16260,
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
    "points": 13191,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 10544,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 9957,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV138Ng6wEEj",
    "domain": "AI",
    "title": "【2026版】这绝对是B站讲的最好的Vibe Coding企业级项目实战，90分钟速通Claude Code、Codex，Cursor、AI工程化编程实战开发！",
    "url": "http://www.bilibili.com/video/av116905822259723",
    "source": "图灵架构师诸葛",
    "platform": "bilibili",
    "points": 8508,
    "published_at": "2026-07-12T07:30:41+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\n【本视频笔记代码/学习大纲/全套面试真题/系统学习/实战案例等请戳链接获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1mtGK6hEKC",
    "domain": "AI",
    "title": "Deepseek V4 Flash最新测评！Claude Code版！",
    "url": "http://www.bilibili.com/video/av117015578676037",
    "source": "AI产品狙击手",
    "platform": "bilibili",
    "points": 8432,
    "published_at": "2026-07-31T16:41:51+00:00",
    "summary": "上期完成 DeepSeek V4 Flash 在 Codex 平台测评，本期统一拉满 High 思考深度接入 Claude Code 复测，用全套标准化用例横向对比模型真实表现，基础指令、24 点运算、密码锁逻辑推理全部答对，仅十条顺序句子存在单句通顺度瑕疵；代码生成环节暴露统一痛点，所有大型开发任务耗时动辄数十分钟，判断是新模型上线调用高峰算力拥堵导致，自制桌面操作系统成品完整性不及 Codex"
  },
  {
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 8248,
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
    "points": 8197,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 7377,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1aA6uBCEcv",
    "domain": "AI",
    "title": "快速上手｜在OpenCode中接入MCP",
    "url": "http://www.bilibili.com/video/av115965627013763",
    "source": "MiniMax_稀宇极智",
    "platform": "bilibili",
    "points": 7221,
    "published_at": "2026-01-27T06:27:45+00:00",
    "summary": "本视频中，我们将演示如何在OpenCode接入MCP，使MiniMax模型具备网络检索和图片理解的能力。帮助开发者在编码过程中快速获取信息和理解图片内容。\n\n解锁 MiniMax 专属福利，Coding Plan 立享 88 折！\nhttps://platform.minimaxi.com/subscribe/coding-plan?code=1c8FaUGpJ8&amp;source=link"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7014,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
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
    "points": 114,
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
    "id": "hn:49177126",
    "domain": "AI 算力 / 半导体",
    "title": "It looks like 'Big Short' investor Michael Burry nailed bet against chip stocks",
    "url": "https://www.businessinsider.com/big-short-michael-burry-ai-chip-stocks-soxx-nvidia-substack-2026-8",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-05T00:30:23+00:00",
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
    "id": "rss:https://www.eetimes.com/automotive-cybersecurity-ai-attack-surfaces-grow/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Cybersecurity: AI Attack Surfaces Grow",
    "url": "https://www.eetimes.com/automotive-cybersecurity-ai-attack-surfaces-grow/",
    "source": "Egil Juliussen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:00:00+00:00",
    "summary": "AI and software-defined cars turn APIs, servers, and chargers into hacker playgrounds; see why automakers must harden fleets now. The post Automotive Cybersecurity: AI Attack Surfaces Grow appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/jamie-urquhart-1957-2026-friendly-supportive-right-to-the-end/",
    "domain": "AI 算力 / 半导体",
    "title": "Jamie Urquhart (1957-2026): Friendly, Supportive, Right to the End",
    "url": "https://www.eetimes.com/jamie-urquhart-1957-2026-friendly-supportive-right-to-the-end/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:33:32+00:00",
    "summary": "Arm co-founder Jamie Urquhart backed chips, startups, and people to the end—read how his quiet force shaped an industry. The post Jamie Urquhart (1957-2026): Friendly, Supportive, Right to the End app"
  },
  {
    "id": "rss:https://www.eetimes.com/new-space-power-computing-and-thermal-challenges-beyond-earth/",
    "domain": "AI 算力 / 半导体",
    "title": "New Space: Power, Computing and Thermal Challenges Beyond Earth",
    "url": "https://www.eetimes.com/new-space-power-computing-and-thermal-challenges-beyond-earth/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T14:48:24+00:00",
    "summary": "New Space explores the technologies reshaping the commercial space economy. The post New Space: Power, Computing and Thermal Challenges Beyond Earth appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/protecting-military-ai-agents-from-cyberthreats/",
    "domain": "AI 算力 / 半导体",
    "title": "Protecting Military AI Agents From Cyberthreats",
    "url": "https://www.eetimes.com/protecting-military-ai-agents-from-cyberthreats/",
    "source": "Liam Critchley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T07:36:29+00:00",
    "summary": "Military AI faces hackers, poisoned data, and weak rules; lock it down with zero trust, red-teaming, and real governance. The post Protecting Military AI Agents From Cyberthreats appeared first on EE "
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
    "id": "rss:https://www.tomshardware.com/tech-industry/amd-doubles-data-center-revenue-year-over-year-but-gaming-revenue-plunged-by-31-percent-ceo-lisa-su-says-prices-have-weighed-on-consumer-demand-but-is-optimistic-about-client-market",
    "domain": "AI 算力 / 半导体",
    "title": "AMD doubles data center revenue year over year, but gaming revenue plunged by 31% — CEO Lisa Su says prices have 'weighed on' consumer demand but is 'optimistic' about client market",
    "url": "https://www.tomshardware.com/tech-industry/amd-doubles-data-center-revenue-year-over-year-but-gaming-revenue-plunged-by-31-percent-ceo-lisa-su-says-prices-have-weighed-on-consumer-demand-but-is-optimistic-about-client-market",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:03:07+00:00",
    "summary": "AMD reported record revenue in Q2 2026, including doubling its data center business year-over-year, but gaming revenue dived 31%."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/more-gpu-price-hikes-loom-for-asia-as-japanese-distributor-warns-of-new-increases-cfd-sales-signals-20-percent-to-40-percent-higher-prices-on-gigabyte-graphics-card-orders-starting-this-month",
    "domain": "AI 算力 / 半导体",
    "title": "More GPU price hikes loom for Asia as Japanese distributor warns of new increases — CFD Sales signals 20% to 40% higher prices on Gigabyte graphics card orders starting this month",
    "url": "https://www.tomshardware.com/pc-components/gpus/more-gpu-price-hikes-loom-for-asia-as-japanese-distributor-warns-of-new-increases-cfd-sales-signals-20-percent-to-40-percent-higher-prices-on-gigabyte-graphics-card-orders-starting-this-month",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:38:15+00:00",
    "summary": "Japanese technology supplier and distributor confirms that the Gigabyte graphics card will cost between 20% and 40% more due to a new price increase."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-mulling-ban-on-key-chinese-networking-tech-in-data-center-component-crackdown-white-house-wants-to-impose-restrictions-in-2026-china-says-it-will-respond-if-necessary",
    "domain": "AI 算力 / 半导体",
    "title": "US mulling ban on key Chinese networking tech in data center component crackdown — White House wants to impose restrictions in 2026, China says it will respond if necessary",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-mulling-ban-on-key-chinese-networking-tech-in-data-center-component-crackdown-white-house-wants-to-impose-restrictions-in-2026-china-says-it-will-respond-if-necessary",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:54:00+00:00",
    "summary": "Sources say that the FCC is drafting a ban on optical transceivers for data centers. These components, which convert electrical signals into light signals, are said to pose a risk as they can be used "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/texas-slams-on-the-breaks-for-1-800-data-centers-power-grid-requirements-are-five-times-higher-than-peak-record-demand-474-gigawatts-of-power-requests-are-now-subject-to-new-moratorium",
    "domain": "AI 算力 / 半导体",
    "title": "Texas slams on the brakes for 1,800 data centers, power grid requirements are five times higher than peak record demand — 474 gigawatts of power requests are now subject to new moratorium",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/texas-slams-on-the-breaks-for-1-800-data-centers-power-grid-requirements-are-five-times-higher-than-peak-record-demand-474-gigawatts-of-power-requests-are-now-subject-to-new-moratorium",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:48:12+00:00",
    "summary": "Gov. Greg Abbott (R) instructed PUCT and ERCOT to pause all data center applications until they complete an audit on all the information that data center developers must submit. The move reportedly ca"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-demonstrate-the-worlds-highest-density-3d-nand-flash-332-active-layers-and-up-to-4-800-mt-s-interface",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia and Sandisk demonstrate the world's highest-density 3D NAND flash — 332 active layers and up to 4,800 MT/s interface",
    "url": "https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-demonstrate-the-worlds-highest-density-3d-nand-flash-332-active-layers-and-up-to-4-800-mt-s-interface",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:15:42+00:00",
    "summary": "Kioxia and Sandisk introduce BiCS10 3D QLC NAND device with a record areal density of over 37 Gbit/mm^2."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie",
    "domain": "AI 算力 / 半导体",
    "title": "New HBF spec outlines tech that can give GPUs terabytes of extra memory — Sandisk and SK hynix unveil spec with up to 16-Hi NAND stacks, 3 TB/s bandwidth, UCIe",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T14:42:58+00:00",
    "summary": "Sandisk and SK hynix formally introduce HBF specification that promises up to 3 TB/s of bandwidth eventually, though only four companies are currently interested in the technology."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/pc-cooling-outfit-arctic-reverses-tariff-era-price-hikes-after-us-government-refund-lowers-prices-across-lineup-including-coolers-and-case-fans",
    "domain": "AI 算力 / 半导体",
    "title": "PC cooling outfit Arctic reverses tariff-era price hikes after US government refund — lowers prices across lineup, including coolers and case fans",
    "url": "https://www.tomshardware.com/pc-components/cooling/pc-cooling-outfit-arctic-reverses-tariff-era-price-hikes-after-us-government-refund-lowers-prices-across-lineup-including-coolers-and-case-fans",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T13:37:09+00:00",
    "summary": "The company says it is honoring its earlier promise to reverse tariff-driven price increases, becoming one of the first PC hardware vendors to publicly roll back pricing after a major court ruling."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinese-chipmaking-tool-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese chipmaking tool roadmaps examined — Beijing's nascent lithography tools target DUV production at five machines a year, and an EUV prototype with no chips",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinese-chipmaking-tool-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T13:15:00+00:00",
    "summary": "Ultimately, three markers will indicate whether China’s domestic DUV program is a legitimate rival or yet more state-sanctioned hot air."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/at-least-37-people-arrested-in-2026-so-far-for-protesting-against-data-centers-most-taken-into-custody-acted-peacefully-only-broke-petty-rules",
    "domain": "AI 算力 / 半导体",
    "title": "At least 37 people arrested in 2026 so far for protesting against data centers, most for breaking 'petty rules' — most taken into custody acted peacefully",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/at-least-37-people-arrested-in-2026-so-far-for-protesting-against-data-centers-most-taken-into-custody-acted-peacefully-only-broke-petty-rules",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T12:53:03+00:00",
    "summary": "Data center protesters are getting arrested for minor infractions, yet they continue pushing back against these projects. Aside from the arrests, there's also at least 12 instances (probably more) whe"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/lenovo-loq-essentials-15-gen-11-review",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo LOQ Essentials 15 Gen 11 Review: A good display meets a low-power RTX 5060",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/lenovo-loq-essentials-15-gen-11-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "The Lenovo LOQ Essentials 15 Gen 11 pairs an RTX 5060, 144 Hz display, and excellent upgradeability with a comfortable keyboard, but its low-power GPU configuration and outdated CPU leave it strugglin"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/apple-is-getting-this-wrong-says-openai-startup-blasts-iphone-maker-over-lawsuit-alleging-it-stole-confidential-information-through-ex-apple-employees",
    "domain": "AI 算力 / 半导体",
    "title": "‘Apple is getting this wrong,’ says OpenAI — startup blasts iPhone maker over lawsuit alleging it stole confidential information through ex-Apple employees",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/apple-is-getting-this-wrong-says-openai-startup-blasts-iphone-maker-over-lawsuit-alleging-it-stole-confidential-information-through-ex-apple-employees",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T11:52:34+00:00",
    "summary": "OpenAI denies Apple's allegations in a blog post. The company claims that it doesn't have and even doesn't want its rivals trade secrets."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/chinese-ship-spotted-lurking-over-taiwan-us-undersea-cables-research-vessel-seen-loitering-above-the-8-000-mile-pacific-light-cable-network-fiber-optic-system",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese ship spotted lurking over Taiwan-US undersea cables — 'research vessel' seen loitering above the 8,000-mile Pacific Light Cable Network fiber-optic system",
    "url": "https://www.tomshardware.com/networking/chinese-ship-spotted-lurking-over-taiwan-us-undersea-cables-research-vessel-seen-loitering-above-the-8-000-mile-pacific-light-cable-network-fiber-optic-system",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T11:49:18+00:00",
    "summary": "A new video shows Taiwan’s Coast Guard warning a 200-ft long Chinese-flagged research vessel, spotted loitering over a fiber internet cable, to change course."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/desks/grab-a-new-secretlab-sit-to-stand-desk-for-usd699-save-usd50-as-the-magnus-evo-receives-its-first-ever-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a new Secretlab sit-to-stand desk for $699 — Save $50 as the Magnus Evo receives its first-ever discount",
    "url": "https://www.tomshardware.com/peripherals/desks/grab-a-new-secretlab-sit-to-stand-desk-for-usd699-save-usd50-as-the-magnus-evo-receives-its-first-ever-discount",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:37:50+00:00",
    "summary": "Secretlab has finally reduced the price of the Magnus Evo standing desk. In its first-ever discount, you can save $50 on a new sit-to-stand desk."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/16gb-gpus-and-8-core-cpus-officially-become-the-most-popular-configs-on-steam-latest-hardware-survey-shows-modern-gamings-growing-hunger-for-more-resources",
    "domain": "AI 算力 / 半导体",
    "title": "16GB GPUs and 8-core CPUs officially become the most popular configs on Steam — Latest hardware survey shows modern gaming's growing hunger for more resources",
    "url": "https://www.tomshardware.com/pc-components/16gb-gpus-and-8-core-cpus-officially-become-the-most-popular-configs-on-steam-latest-hardware-survey-shows-modern-gamings-growing-hunger-for-more-resources",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:30:00+00:00",
    "summary": "For the first time in Steam history, 8-core CPUs have overtaken 6-core CPUs and GPUs with 16GB of VRAM have overtaken 8GB GPUs. Even though the hardware survey doesn't represent everyone, it still ind"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/three-major-pc-makers-now-using-chinese-memory-to-fight-unprecedented-memory-shortage-report-claims-hp-asus-and-acer-using-small-amounts-of-cxmt-chips-in-limited-number-of-notebooks-for-non-us-market",
    "domain": "AI 算力 / 半导体",
    "title": "Three major PC makers now using Chinese memory to fight 'unprecedented memory shortage,' report claims — HP, Asus, and Acer using 'small amounts' of CXMT chips in limited number of notebooks for non-U",
    "url": "https://www.tomshardware.com/tech-industry/three-major-pc-makers-now-using-chinese-memory-to-fight-unprecedented-memory-shortage-report-claims-hp-asus-and-acer-using-small-amounts-of-cxmt-chips-in-limited-number-of-notebooks-for-non-us-market",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:15:23+00:00",
    "summary": "A new report claims that HP, Asus, and Acer have started to use a small amount of CXMT memory chips in notebooks for non-US markets."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/china-cracks-down-on-copycat-chip-designs-with-new-regulations-and-penalties-new-guidelines-enforce-originality-and-independent-development",
    "domain": "AI 算力 / 半导体",
    "title": "China cracks down on copycat chip designs with new regulations and penalties — new guidelines enforce originality and independent development",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/china-cracks-down-on-copycat-chip-designs-with-new-regulations-and-penalties-new-guidelines-enforce-originality-and-independent-development",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:00:00+00:00",
    "summary": "China tightens legal protections for domestically developed chip layout designs by raising originality requirements and strengthening infringement penalties."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/this-144-piece-toolkit-is-a-must-buy-for-hobbyists-and-pc-builders-for-under-usd40-pocket-a-20-percent-saving-on-this-screwdriver-set-with-two-drivers-120-magnetic-bits-and-22-repair-tools-for-your-projects",
    "domain": "AI 算力 / 半导体",
    "title": "This 144-piece toolkit is a must-buy for hobbyists and PC builders for under $40 — pocket a 20% saving on this screwdriver set with two drivers, 120 magnetic bits, and 22 repair tools for your project",
    "url": "https://www.tomshardware.com/desktops/pc-building/this-144-piece-toolkit-is-a-must-buy-for-hobbyists-and-pc-builders-for-under-usd40-pocket-a-20-percent-saving-on-this-screwdriver-set-with-two-drivers-120-magnetic-bits-and-22-repair-tools-for-your-projects",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T09:43:27+00:00",
    "summary": "Pick up this 144-in-1 repair toolkit from Strebito, with 120 bits and a number of other tools, for less than $40 right now, saving you 20%."
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
    "id": "hn:49025890",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's 256-core Epyc 9996 'Venice' claims up to a 3.4x jump over Intel Xeon",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-23T18:16:54+00:00",
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
    "id": "rss:https://www.theverge.com/entertainment/975297/spider-man-brand-new-day-marvel-sony-xmen-doomsday",
    "domain": "大厂 AI 动态",
    "title": "Don’t screw this up, Marvel",
    "url": "https://www.theverge.com/entertainment/975297/spider-man-brand-new-day-marvel-sony-xmen-doomsday",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T23:20:56+00:00",
    "summary": "In less than a week, Spider-Man: Brand New Day raked in $1 billion worldwide and had the biggest box office opening weekend in Hollywood history. The feature has been a reminder of why Sony is probabl"
  },
  {
    "id": "rss:https://www.theverge.com/tech/975407/signal-linked-devices-sync",
    "domain": "大厂 AI 动态",
    "title": "Now you can securely link multiple phones to one Signal account",
    "url": "https://www.theverge.com/tech/975407/signal-linked-devices-sync",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:02:46+00:00",
    "summary": "You can link more devices with one phone number on Signal now, including an Android phone or iPhone. Signal already supported linking PCs and iPads, but not additional phones. When you link a device o"
  },
  {
    "id": "rss:https://www.theverge.com/tech/975381/amd-q2-2026-earnings-ai-gaming-ryzen",
    "domain": "大厂 AI 动态",
    "title": "AMD&#8217;s data center business is booming while gaming takes a backseat",
    "url": "https://www.theverge.com/tech/975381/amd-q2-2026-earnings-ai-gaming-ryzen",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T20:57:49+00:00",
    "summary": "Driven by demand for AI capacity, AMD's data center revenue more than doubled year-over-year in its latest earnings report, reaching $6.7 billion. That's up from $5.8 billion in Q1, and jumping 107 pe"
  },
  {
    "id": "rss:https://www.theverge.com/science/975335/spacex-made-more-money-as-a-neocloud",
    "domain": "大厂 AI 动态",
    "title": "SpaceX made more revenue as an AI company than a space company",
    "url": "https://www.theverge.com/science/975335/spacex-made-more-money-as-a-neocloud",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T20:47:55+00:00",
    "summary": "SpaceX's AI revenue grew more than three times to $2.6 billion from the year before, mostly because of deals that the company made to provide compute to other AI companies, according to SpaceX's quart"
  },
  {
    "id": "rss:https://www.theverge.com/games/974736/ea-private-company-deal-closed",
    "domain": "大厂 AI 动态",
    "title": "EA is now a private company",
    "url": "https://www.theverge.com/games/974736/ea-private-company-deal-closed",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T20:18:14+00:00",
    "summary": "Electronic Arts has officially become a private company. Last September, EA announced that an investor group led by Saudi Arabia's Public Investment Fund (PIF), Silver Lake, and Affinity Partners woul"
  },
  {
    "id": "rss:https://www.theverge.com/tech/975300/telegram-app-store-takedown-extortion-pavel-durov",
    "domain": "大厂 AI 动态",
    "title": "Telegram CEO says an extortionist planted CSAM in a chat to get it pulled from the App Store",
    "url": "https://www.theverge.com/tech/975300/telegram-app-store-takedown-extortion-pavel-durov",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T19:11:05+00:00",
    "summary": "Telegram CEO Pavel Durov blames an extortionist for planting child sexual abuse material (CSAM) in a public chat to get the app temporarily removed from Apple's App Store on Monday night. \"Apple remov"
  },
  {
    "id": "rss:https://www.theverge.com/tech/975173/openai-influencers-brand-trip-ai-backlash-marketing",
    "domain": "大厂 AI 动态",
    "title": "How an OpenAI influencer trip backfired",
    "url": "https://www.theverge.com/tech/975173/openai-influencers-brand-trip-ai-backlash-marketing",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:46:41+00:00",
    "summary": "The brand trip is a right of passage for influencers. It's a mark of legitimacy that a sponsor wants to invite them on an all-expenses-paid vacation, often with luxurious freebies and activities. Trip"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/975113/lenovo-legion-go-s-steamos-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Lenovo&#8217;s Legion Go S with SteamOS is down to its lowest price ever",
    "url": "https://www.theverge.com/gadgets/975113/lenovo-legion-go-s-steamos-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:35:04+00:00",
    "summary": "Memory and storage prices will be inflated for the foreseeable future, so we’re always happy to find a good deal on capable gaming hardware, like this discount on the Lenovo Legion Go S with a Z2 Go p"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/975180/llm-ai-chatbot-use-not-healthy",
    "domain": "大厂 AI 动态",
    "title": "‘Not healthy’ LLM use is more common than you think",
    "url": "https://www.theverge.com/ai-artificial-intelligence/975180/llm-ai-chatbot-use-not-healthy",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:33:46+00:00",
    "summary": "Hank Green, a popular YouTuber and science communicator, said he is stepping back from production amid intense criticism over his use of AI. Green described his AI usage as \"not healthy,\" but stressed"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/975172/bmw-spider-man-movie-infotainment-ad",
    "domain": "大厂 AI 动态",
    "title": "BMW’s in-car Spider-Man ad is villain behavior",
    "url": "https://www.theverge.com/transportation/975172/bmw-spider-man-movie-infotainment-ad",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:17:14+00:00",
    "summary": "When a premium car brand like BMW says it has a \"special surprise\" in store for drivers, I'd expect something more luxurious than having a movie commercial beamed onto the dashboard. That's exactly wh"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/elon-musk-repeatedly-one-upped-his-execs-on-spacexs-first-earnings-call/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk repeatedly one-upped his execs on SpaceX’s first earnings call",
    "url": "https://techcrunch.com/2026/08/04/elon-musk-repeatedly-one-upped-his-execs-on-spacexs-first-earnings-call/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:30:58+00:00",
    "summary": "Musk kept inflating the already-big promises being made by SpaceX CFO Bret Johnsen and Gwynne Shotwell on the company's first call."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/lucids-turnaround-plan-hinges-on-1-4b-in-cash-savings-robotaxis/",
    "domain": "大厂 AI 动态",
    "title": "Lucid’s turnaround plan hinges on $1.4B in cash savings, robotaxis",
    "url": "https://techcrunch.com/2026/08/04/lucids-turnaround-plan-hinges-on-1-4b-in-cash-savings-robotaxis/",
    "source": "Kirsten Korosec, Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:24:00+00:00",
    "summary": "Lucid's new CEO Silvio Napoli listed four must-win priorities, including the successful launch of its midsize EV, finishing a factory in Saudi Arabia, cutting expenses, and robotaxis."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/how-to-get-the-best-hotel-deals-for-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "How to get the best hotel deals for TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/04/how-to-get-the-best-hotel-deals-for-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:18:30+00:00",
    "summary": "We’ve partnered with hotels around Moscone West during Disrupt, taking place October 13 to 15, to secure the best prices available for attendees."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/spacex-has-bought-329m-worth-of-tesla-megapacks-so-far-this-year/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX has bought $329M worth of Tesla Megapacks so far this year",
    "url": "https://techcrunch.com/2026/08/04/spacex-has-bought-329m-worth-of-tesla-megapacks-so-far-this-year/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T21:07:26+00:00",
    "summary": "The purchase illustrates just how interconnected Elon Musk's universe of companies are."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/spacex-doubles-revenues-on-anthropic-and-google-compute-deals-starlink-growth/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX doubles revenue on Anthropic and Google compute deals, Starlink growth",
    "url": "https://techcrunch.com/2026/08/04/spacex-doubles-revenues-on-anthropic-and-google-compute-deals-starlink-growth/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T20:36:30+00:00",
    "summary": "SpaceX doubled its revenue compared to last year, according to its first quarterly earnings since going public in June."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/android-app-developers-may-be-unwittingly-sharing-their-users-location-data-with-advertisers/",
    "domain": "大厂 AI 动态",
    "title": "Android app developers may be unwittingly sharing their users’ location data with advertisers",
    "url": "https://techcrunch.com/2026/08/04/android-app-developers-may-be-unwittingly-sharing-their-users-location-data-with-advertisers/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T20:26:53+00:00",
    "summary": "New findings by the Electronic Frontier Foundation aim to warn app developers that some of the third-party code they place in their apps may also collect their users' location data when they grant per"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/",
    "domain": "大厂 AI 动态",
    "title": "Open-weight AI models are catching up to the frontier. The safety gap remains.",
    "url": "https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T20:05:26+00:00",
    "summary": "A new SaferAI report finds Z.ai's open-weight GLM-5.2 approaches frontier AI capabilities while lacking key safety mitigations, renewing concerns that powerful open models could outpace governance and"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic signs $10B deal with AI cloud startup Volta",
    "url": "https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T19:48:40+00:00",
    "summary": "Anthropic has been on a cloud partnership spree in recent months, and its latest move is reportedly a $10 billion deal with AI cloud startup Volta."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/meet-wrinkles-an-ai-app-that-uncovers-the-hidden-stories-of-the-places-around-you/",
    "domain": "大厂 AI 动态",
    "title": "Meet Wrinkles, an app that uncovers the hidden stories of the places around you",
    "url": "https://techcrunch.com/2026/08/04/meet-wrinkles-an-ai-app-that-uncovers-the-hidden-stories-of-the-places-around-you/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T19:34:34+00:00",
    "summary": "Wrinkles, available on both iOS and Android, essentially acts as an AI-powered audio tour guide that reveals hidden history and local stories."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/nvidia-doesnt-mess-around-a-week-after-open-ai-industry-group-formed-its-already-showing-progress/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia doesn’t mess around: A week after open AI industry group formed, it’s already showing progress",
    "url": "https://techcrunch.com/2026/08/04/nvidia-doesnt-mess-around-a-week-after-open-ai-industry-group-formed-its-already-showing-progress/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T19:28:49+00:00",
    "summary": "The week-old Open Secure AI Alliance, spearheaded by Nvidia and grown to over 120 companies, already has proposals out for defending against AI agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/waymo-opens-up-robotaxi-service-in-dallas-to-everyone/",
    "domain": "大厂 AI 动态",
    "title": "Waymo opens up robotaxi service in Dallas to everyone",
    "url": "https://techcrunch.com/2026/08/04/waymo-opens-up-robotaxi-service-in-dallas-to-everyone/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:31:01+00:00",
    "summary": "Waymo has dropped the waitlist for its robotaxi service in Dallas, the latest step in the company's bid to scale its self-driving technology across the United States, U.K., and Europe."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/take-an-extra-100-off-your-techcrunch-disrupt-2026-pass-this-week-only/",
    "domain": "大厂 AI 动态",
    "title": "Take an extra $100 off your TechCrunch Disrupt 2026 pass: This week only!",
    "url": "https://techcrunch.com/2026/08/04/take-an-extra-100-off-your-techcrunch-disrupt-2026-pass-this-week-only/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:20:54+00:00",
    "summary": "Starting today, you can take an additional $100 off your founder, investor, or attendee TechCrunch Disrupt 2026 pass, which is a nice bonus on top of our current discounted pricing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/tv-time-co-founder-launches-bingers-to-revive-the-beloved-tv-tracking-app/",
    "domain": "大厂 AI 动态",
    "title": "TV Time co-founder launches Bingers to revive the beloved TV-tracking app",
    "url": "https://techcrunch.com/2026/08/04/tv-time-co-founder-launches-bingers-to-revive-the-beloved-tv-tracking-app/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:05:48+00:00",
    "summary": "Bingers is a new TV and movie tracker that revives the social features fans loved with TV Time, while adding support for importing their viewing history."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/",
    "domain": "大厂 AI 动态",
    "title": "Hackers steal over $130M by exploiting bug in offline hardware wallets",
    "url": "https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:27:59+00:00",
    "summary": "A security vulnerability in the cryptocurrency hardware wallet Coldcard is allowing hackers to drain the crypto from victims’ wallets. The total losses amount to more than $130 million, according to b"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/spotify-adds-merlin-to-its-ai-music-remix-and-covers-effort/",
    "domain": "大厂 AI 动态",
    "title": "Spotify expands AI remix and covers project with Merlin partnership",
    "url": "https://techcrunch.com/2026/08/04/spotify-adds-merlin-to-its-ai-music-remix-and-covers-effort/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T15:50:06+00:00",
    "summary": "Spotify says Merlin, which represents more than 30,000 independent labels and distributors, has joined Universal Music Group in backing its upcoming AI-powered remix and covers product. The paid tool "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/texas-halts-new-data-centers-as-governor-calls-for-audits/",
    "domain": "大厂 AI 动态",
    "title": "Texas halts new data centers as governor calls for audits",
    "url": "https://techcrunch.com/2026/08/04/texas-halts-new-data-centers-as-governor-calls-for-audits/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T15:42:35+00:00",
    "summary": "Tech companies and developers have been scouring the U.S. for places to build data centers, and they’ve been drawn to Texas’ loose regulations and seemingly abundant power supply. But even Texas can b"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/walmart-completes-its-acquisition-of-tv-advertising-company-vibe-co/",
    "domain": "大厂 AI 动态",
    "title": "Walmart completes its acquisition of TV advertising company Vibe.co",
    "url": "https://techcrunch.com/2026/08/04/walmart-completes-its-acquisition-of-tv-advertising-company-vibe-co/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T15:38:22+00:00",
    "summary": "The acquisition, which was announced in June, brings Vibe.co into Walmart Connect, Walmart's connected TV advertising platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/elon-musk-spends-half-his-time-talking-robots-and-ai-on-tesla-earnings-calls/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk spends half his time talking robots and AI on Tesla earnings calls",
    "url": "https://techcrunch.com/2026/08/04/elon-musk-spends-half-his-time-talking-robots-and-ai-on-tesla-earnings-calls/",
    "source": "Sean O'Kane, Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T15:20:06+00:00",
    "summary": "An analysis of the last seven years of Tesla earnings calls shows just how little attention Musk pays to Tesla's car business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/host-a-side-event-during-techcrunch-founder-summit-week-in-boston/",
    "domain": "大厂 AI 动态",
    "title": "Host a Side Event during TechCrunch Founder Summit Week in Boston",
    "url": "https://techcrunch.com/2026/08/04/host-a-side-event-during-techcrunch-founder-summit-week-in-boston/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T15:00:00+00:00",
    "summary": "Want to tap into the energy of 1,100+ startup founders, investors, and tech leaders descending on Boston for the Founder Summit 2026 on June 9? Host your own Side Event during “Founder Summit Week,” h"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/04/apple-says-more-ex-employees-may-have-taken-confidential-data-to-openai/",
    "domain": "大厂 AI 动态",
    "title": "Apple says more ex-employees may have taken confidential data to OpenAI",
    "url": "https://techcrunch.com/2026/08/04/apple-says-more-ex-employees-may-have-taken-confidential-data-to-openai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T14:03:01+00:00",
    "summary": "Apple says its trade secrets investigation into OpenAI has widened. In a new court filing, Apple claims additional former staff may have retained or accessed confidential information."
  },
  {
    "id": "rss:https://stratechery.com/2026/microsoft-earnings-microsoft-vs-meta-the-efficiency-payoff/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Earnings, Microsoft vs. Meta, The Efficiency Payoff",
    "url": "https://stratechery.com/2026/microsoft-earnings-microsoft-vs-meta-the-efficiency-payoff/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T10:00:00+00:00",
    "summary": "Microsoft's earnings were compelling because they showed a clarity of strategy, lower costs, and a tangibility of application. The reason why is scarier."
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
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/senators-demand-crackdown-on-wildfire-prediction-markets/",
    "domain": "大厂 AI 动态",
    "title": "Senators demand crackdown on wildfire \"prediction markets\"",
    "url": "https://arstechnica.com/tech-policy/2026/08/senators-demand-crackdown-on-wildfire-prediction-markets/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T21:52:31+00:00",
    "summary": "Fire experts warn such markets could incentivize arson."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/trump-forced-to-reinstate-broadband-grants-but-court-lets-us-scrap-race-criteria/",
    "domain": "大厂 AI 动态",
    "title": "Trump killed the Digital Equity Act, but US was forced to bring part of it back",
    "url": "https://arstechnica.com/tech-policy/2026/08/trump-forced-to-reinstate-broadband-grants-but-court-lets-us-scrap-race-criteria/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T21:27:05+00:00",
    "summary": "$1.25 billion program restored, but judge ruled race provision unconstitutional."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/texas-halts-data-center-connections-to-power-grid-amid-overwhelming-demand/",
    "domain": "大厂 AI 动态",
    "title": "Texas halts data center connections to power grid amid overwhelming demand",
    "url": "https://arstechnica.com/ai/2026/08/texas-halts-data-center-connections-to-power-grid-amid-overwhelming-demand/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T20:34:28+00:00",
    "summary": "Governor who touted Texas as AI “epicenter” pauses data center grid connections."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/china-is-teslas-cash-cow-but-for-how-much-longer/",
    "domain": "大厂 AI 动态",
    "title": "China is Tesla's cash cow, but for how much longer?",
    "url": "https://arstechnica.com/cars/2026/08/china-is-teslas-cash-cow-but-for-how-much-longer/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:34:48+00:00",
    "summary": "Tesla's Shanghai factory is busier than ever but might be cut loose."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/the-pixel-11s-glow-feature-is-actually-called-hilight-heres-what-it-does/",
    "domain": "大厂 AI 动态",
    "title": "The Pixel 11's \"glow\" feature is actually called HiLight—here's what it does",
    "url": "https://arstechnica.com/gadgets/2026/08/the-pixel-11s-glow-feature-is-actually-called-hilight-heres-what-it-does/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:11:05+00:00",
    "summary": "The camera flash will evolve into a multicolor LED that illuminates when your phone is face down."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/can-trump-fcc-repeal-39-tv-ownership-cap-republican-who-wrote-cap-into-law-says-no/",
    "domain": "大厂 AI 动态",
    "title": "Tom DeLay helped create TV ownership cap—he says Trump FCC has no authority to repeal it",
    "url": "https://arstechnica.com/tech-policy/2026/08/can-trump-fcc-repeal-39-tv-ownership-cap-republican-who-wrote-cap-into-law-says-no/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T15:51:00+00:00",
    "summary": "Congress set ownership limit at 39%, but FCC claims authority to kill the rule."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/trump-admin-aware-of-deaths-in-explosive-diarrhea-outbreak-delays-reporting/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin \"aware\" of deaths in explosive diarrhea outbreak, delays reporting",
    "url": "https://arstechnica.com/health/2026/08/trump-admin-aware-of-deaths-in-explosive-diarrhea-outbreak-delays-reporting/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T15:06:07+00:00",
    "summary": "Federal officials will update the outbreak sometime \"this week,\" a spokesperson said."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/2027-chevrolet-corvette-grand-sport-x-proves-code-is-as-important-as-hardware/",
    "domain": "大厂 AI 动态",
    "title": "2027 Chevrolet Corvette Grand Sport X proves code is as important as hardware",
    "url": "https://arstechnica.com/cars/2026/08/2027-chevrolet-corvette-grand-sport-x-proves-code-is-as-important-as-hardware/",
    "source": "Tim Stevens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T14:45:08+00:00",
    "summary": "Chevy's 721-hp hybrid ups the ante with few compromises, but at a steep cost."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/openai-says-apples-trade-secrets-lawsuit-is-aggressive-and-oddly-personal/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says Apple's trade secrets lawsuit is \"aggressive and oddly personal\"",
    "url": "https://arstechnica.com/tech-policy/2026/08/openai-says-apples-trade-secrets-lawsuit-is-aggressive-and-oddly-personal/",
    "source": "Jamie John, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T13:38:29+00:00",
    "summary": "“We do not have, nor want, any of their trade secrets,” the ChatGPT maker says."
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
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 100,
    "published_at": "2026-08-04T09:27:47+00:00",
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
    "points": 70,
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
    "id": "wscn:3778723",
    "domain": "股票",
    "title": "韩国警方立案调查三星、SK海力士CEO，涉嫌“绩效奖金”方面的背信罪",
    "url": "https://wallstreetcn.com/articles/3778723",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T05:45:34+00:00",
    "summary": "韩国一少数股东团体向警方投诉三星电子与SK海力士CEO，指控其未经股东大会批准将固定比例营业利润与绩效奖金挂钩，涉嫌背信并损害股东利益。目前京畿南部警察厅已立案调查。"
  },
  {
    "id": "wscn:3778724",
    "domain": "股票",
    "title": "长江资管迎新董事长，张波履新",
    "url": "https://wallstreetcn.com/articles/3778724",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T05:21:00+00:00",
    "summary": "从信用业务条线走向资管掌舵人"
  },
  {
    "id": "wscn:3778644",
    "domain": "股票",
    "title": "62.8%！韩国7月出口放缓之后：AI繁荣的结构性红利还是周期性狂欢？",
    "url": "https://wallstreetcn.com/premium/articles/3778644?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:06:33+00:00",
    "summary": "韩国7月半导体出口增速放缓，但AI结构性需求推升价格平台，投资正从周期波动转向结构性定价。"
  },
  {
    "id": "wscn:3778711",
    "domain": "股票",
    "title": "沪指涨超1%，科创50暴涨逾5%，半导体大爆发，“易中天”集体回应美国光模块禁令，港股科网股盘中反弹",
    "url": "https://wallstreetcn.com/articles/3778711",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:03:51+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3900股飘红，上午半天成交1.7万亿，沪深两市半日成交额1.69万亿，较上个交易日放量3290亿。板块方面，半导体、算力硬件产业链延续反弹，PCB、存储器、工业气体方向领涨；多模态AI、智能驾驶、工业金属、太空光伏、固态电池、商业航天概念股活跃。"
  },
  {
    "id": "wscn:3778716",
    "domain": "股票",
    "title": "美元指数又回到100关口，接下来怎么走？",
    "url": "https://wallstreetcn.com/articles/3778716",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T03:36:24+00:00",
    "summary": "日元干预洗盘后，美元指数再度触及100整数关口。头寸中性、利差匹配、加息预期模糊——三重信号均指向同一结论：美元正悬于可上可下的微妙中间态。但7月美国经济数据韧性超预期，叠加美联储急需借杰克逊霍尔年会重塑鹰派公信力，短期美元下行动能或已衰竭。"
  },
  {
    "id": "wscn:3778721",
    "domain": "股票",
    "title": "高盛：超大型科技股垄断格局瓦解，15年市场集中度拐点已现",
    "url": "https://wallstreetcn.com/articles/3778721",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T03:34:30+00:00",
    "summary": "高盛首席全球股票策略师警告：持续逾十五年的美股高度集中格局正迎来结构性拐点。ChatGPT引爆的资本开支竞赛持续侵蚀科技巨头自由现金流，叠加资本成本上升，科技估值优势大幅收窄。与此同时，盈利驱动的\"大扩散\"加速——日本、欧洲、新兴市场强势崛起，工业等传统行业迎来重估。单押美股科技的时代或已终结，多元化配置的真实回报窗口正在开启。"
  },
  {
    "id": "wscn:3778720",
    "domain": "股票",
    "title": "SpaceX的AB面：星链日赚1800万，AI日烧1.7亿",
    "url": "https://wallstreetcn.com/articles/3778720",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T03:25:00+00:00",
    "summary": "SpaceX首份季报呈现极端割裂：营收同比暴增92%至78亿美元，AI单季资本开支却高达158亿，超过英伟达全年研发预算。马斯克正试图在星链的快速盈利、AI的激进扩张与星舰的长期研发这三种截然不同的商业张力中维持平衡。然而，一家公司能否同时打赢这三场战争，市场仍在等待明确的答案。"
  },
  {
    "id": "wscn:3778430",
    "domain": "股票",
    "title": "TaaS：如何理解开源模型Token优化与算力工厂收入分成的新模式？",
    "url": "https://wallstreetcn.com/premium/articles/3778430?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T03:24:59+00:00",
    "summary": "AI算力基础设施的估值逻辑正在发生根本性重构——市场不应继续以\"硬件折旧+租金差价\"的重资产周期股框架为这类公司定价，而应以\"单GPU年化Token收入+客户Token消耗量复合增速\"的SaaS化框架重新审视。"
  },
  {
    "id": "wscn:3778719",
    "domain": "股票",
    "title": "知名科技投资人Gavin Baker谈AI暴跌：市场很恐慌，但基本面很好",
    "url": "https://wallstreetcn.com/articles/3778719",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T03:24:32+00:00",
    "summary": "Gavin Baker表示，7月AI股票下跌40%-60%与实际基本面严重背离——他在硅谷实地调研后，未发现任何负面可量化指标，GPU租金价格反而上涨50%-60%。他认为唯一真实的风险是信用市场收紧，但若超大规模云厂商运营现金流如期加速，债务融资需求将大幅缩减。而监管被其列为最大尾部风险。"
  },
  {
    "id": "wscn:3778714",
    "domain": "股票",
    "title": "亚洲科技股重挫25-30%，市场定价“EPS下调或资本开支削减”！摩根大通预测：恰恰相反",
    "url": "https://wallstreetcn.com/articles/3778714",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T03:06:19+00:00",
    "summary": "摩根大通力排众议，宣布当前是买入亚洲科技股的时机。该行指出，亚洲科技股及费城半导体指数累计下跌25%-30%，但基本面毫无恶化迹象——AI扩展定律完好、超大规模云服务商资本开支2027年将飙至1.49万亿美元、合同积压规模创历史新高，EPS仍将持续上调。市场的悲观定价，或正是最佳买点。"
  },
  {
    "id": "wscn:3778562",
    "domain": "股票",
    "title": "从一颗GPU的“供电阀门”到40亿元市场：DrMOS为何成为AI算力新焦点？",
    "url": "https://wallstreetcn.com/premium/articles/3778562?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T02:56:41+00:00",
    "summary": "DrMOS将驱动器、高侧MOSFET与低侧MOSFET集成在单一封装内，是处理器核心供电系统中负责高频开关、低压转换和大电流输出的关键功率级。随着AI芯片功耗迈向千瓦级，DrMOS需求正在同时受到GPU出货增长、供电相数增加、电流规格升级、成熟制程产能趋紧和国产算力供应链重构的推动。那么，这究竟是一次由缺货涨价驱动的短期行情，还是国产高端模拟芯片从验证迈向规模量产的产业拐点？"
  },
  {
    "id": "wscn:3778717",
    "domain": "股票",
    "title": "马斯克谈存储“供给1年涨20%，需求涨200%，价格当然涨”！高盛韩国交易员：市场定价明年三星亏钱吗？",
    "url": "https://wallstreetcn.com/articles/3778717",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T02:49:07+00:00",
    "summary": "马斯克在SpaceX二季度财报会上直言，存储供给年增约20%，需求年增200%，价格上涨是经济学基本规律。高盛首尔交易员Justin Park随即引用这一逻辑，指出除非市场认为三星2027年将亏损，否则当前股价下行空间有限，核心支撑在于每股净资产（BVPS）。"
  },
  {
    "id": "wscn:3778655",
    "domain": "股票",
    "title": "从极端回撤到阶段反弹，A股科技板块的4个关键信号是什么？",
    "url": "https://wallstreetcn.com/premium/articles/3778655?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T02:07:58+00:00",
    "summary": "7月创业板指、科创50分别下跌23.0%和25.9%，8月4日双创迎来显著反弹，这究竟只是极端跌幅后的技术性回补，还是科技行情重新启动的起点？判断答案不能只看AI产业景气，也不能机械套用“跌多必涨”的历史规律，而应同时回答四个问题：本轮下跌杀的是情绪、估值还是产业逻辑，融资盘与拥挤筹码是否真正出清，历史上的次月反弹能提供多大参考，以及市场能否重新回到由景气度和盈利预期驱动的定价逻辑？"
  },
  {
    "id": "wscn:3778709",
    "domain": "股票",
    "title": "高盛大幅上调中国大模型收入预期，性价比只是起点，能力才是真正的底牌",
    "url": "https://wallstreetcn.com/articles/3778709",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T02:07:21+00:00",
    "summary": "中国大模型正从“性价比叙事”迈向“收入兑现叙事”。高盛上调2026年ARR预期至130亿美元，Agent与编码场景驱动token消费结构性爆发，中国模型已连续14周包揽OpenRouter调用量前五。4到8倍的成本优势叠加能力跃迁，使中国模型从“便宜但凑合”进阶为“足够好且不可不用”。"
  },
  {
    "id": "wscn:3778713",
    "domain": "股票",
    "title": "中国7月RatingDog服务业PMI降至50.4，连续43个月保持扩张，就业、出口新业务均连续三个月增长",
    "url": "https://wallstreetcn.com/articles/3778713",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T02:04:42+00:00",
    "summary": "Yao Yu总结认为，7月服务业整体扩张出现显著放缓，但出口业务韧性、就业持续增长与成本压力缓解提供了积极信号。服务业PMI预计短期内将维持扩张，但恢复速度将高度依赖内需企稳与企业信心的修复进程。"
  },
  {
    "id": "wscn:3778706",
    "domain": "股票",
    "title": "高盛详解韩国存储“8大焦点”：估值、长协、库存、长鑫冲击、回购等",
    "url": "https://wallstreetcn.com/articles/3778706",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T01:54:14+00:00",
    "summary": "高盛报告系统回应市场八大疑虑：HBM价格2027年有望翻倍、长期协议条款向供应商倾斜、行业库存健康、NAND供需不会逆转、股东回报将超预期、ADR溢价短期持续、二季度业绩低于预期属一次性因素、长鑫冲击局限于中国本土市场。高盛认为上述担忧均被市场过度解读，真实供需格局依然支撑存储价格维持高位。"
  },
  {
    "id": "wscn:3778708",
    "domain": "股票",
    "title": "Arista Q2业绩超预期并大幅上调指引，高管直言“需求不是问题，供应是主要瓶颈”",
    "url": "https://wallstreetcn.com/articles/3778708",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T01:46:31+00:00",
    "summary": "Arista Networks二季度单季营收首破30亿美元，同比劲增38%，全年指引大幅上调至126亿美元——相当于2021年全年规模的四倍。AI浪潮不止冲击算力，更全面渗透网络层：scale out、scale across多战场同步爆发，供应链紧张或延续至2028年。"
  },
  {
    "id": "wscn:3778712",
    "domain": "股票",
    "title": "报道：DeepSeek重启融资，投前估值5000亿元",
    "url": "https://wallstreetcn.com/articles/3778712",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T01:32:21+00:00",
    "summary": "据报道，DeepSeek重启了第二轮融资，本轮计划募资500亿元，投前估值约5000亿元，并计划将在8月下旬完成签约。若本轮融资顺利，DeepSeek将在两轮融资中募到超1000亿元的资金。此前DeepSeek暂停第二轮融资，其中一个原因是DeepSeek创始人梁文锋对网上广泛流传的言论感到不满。"
  },
  {
    "id": "wscn:3778710",
    "domain": "股票",
    "title": "Alipay+前支付解决方案总经理Joyce Bo转投万事达卡，执掌亚太核心支付",
    "url": "https://wallstreetcn.com/articles/3778710",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T01:24:31+00:00",
    "summary": "8月3日，全球支付巨头万事达卡宣布，Joyce Bo 已加入公司，出任亚太区核心支付业务执行副总裁。..."
  },
  {
    "id": "wscn:3778705",
    "domain": "股票",
    "title": "美股创出新高！顶住“夏季风暴”的投资者获得回报",
    "url": "https://wallstreetcn.com/articles/3778705",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T00:47:56+00:00",
    "summary": "经历42个交易日震荡后，标普500指数创下年内第25个历史新高，道指、罗素2000同步刷新纪录。此轮反弹由Mag 7领衔，伊朗协议预期推动油价大跌、通胀预期回落提供催化，叠加\"Leopold强制清仓\"打出市场底部、空头大规模回补，坚守仓位的投资者终获回报。"
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
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 266,
    "published_at": "2026-08-04T21:09:39+00:00",
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
    "id": "hn:49173576",
    "domain": "金融",
    "title": "Investors in Situational Awareness deserved to lose their shirts",
    "url": "https://www.economist.com/finance-and-economics/2026/08/04/investors-in-situational-awareness-deserved-to-lose-their-shirts",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-08-04T19:18:35+00:00",
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
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-04T20:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49157782",
    "domain": "金融",
    "title": "US Schools Are Ditching Chromebooks for MacBooks by the Thousands",
    "url": "https://finance.yahoo.com/technology/articles/us-schools-ditching-chromebooks-macbooks-233015401.html",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-08-03T16:16:19+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02666",
    "domain": "金融",
    "title": "Rebuilding Startups: An Empirical Study on Remote Work and Skill Complementarity",
    "url": "https://arxiv.org/abs/2608.02666",
    "source": "Zixi Lei, Xiaomeng Chen, Wen Wen, Andrew Whinston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.02666v1 Announce Type: new Abstract: Remote work is a common practice of workplace flexibility enabled by digital infrastructure, yet its implications for firms' talent composition and orga"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02800",
    "domain": "金融",
    "title": "Raising Rivals' Costs on Hybrid Platforms: The Complementarity of Fees and Self-Preferencing",
    "url": "https://arxiv.org/abs/2608.02800",
    "source": "Maysam Rabbani, Ram Sewak Dubey",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.02800v1 Announce Type: new Abstract: Hybrid platforms disadvantage third-party sellers through the platform fee and self-preferencing, and regulators have worried that constraining either i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02817",
    "domain": "金融",
    "title": "Reviving Micro Real Rigidities: The Importance of Demand Shocks",
    "url": "https://arxiv.org/abs/2608.02817",
    "source": "S. Bora\\u{g}an Aruoba, Eugene Oue, Felipe Saffie, Jonathan L. Willis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.02817v1 Announce Type: new Abstract: We revisit micro real rigidities as a source of monetary non-neutrality in a menu-cost model with variable markups, using firm-level evidence to pin dow"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02854",
    "domain": "金融",
    "title": "Preference robust distortion risk measures",
    "url": "https://arxiv.org/abs/2608.02854",
    "source": "Carole Bernard, Silvana M. Pesenti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.02854v1 Announce Type: new Abstract: We introduce a framework for preference-robust decision making when preferences over risk are modelled through generalised distortion risk measures. Unl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02917",
    "domain": "金融",
    "title": "Mandate without Managers: Automated Market Makers as Verifiable Portfolio Products",
    "url": "https://arxiv.org/abs/2608.02917",
    "source": "Zachary Feinstein, Ionut Florescu, Sean O'Leary",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.02917v1 Announce Type: new Abstract: Automated market makers (AMMs) are typically interpreted and evaluated as decentralized exchanges. Herein, we take the perspective envisioned by Balance"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03153",
    "domain": "金融",
    "title": "Does the Gender Wage Gap Originate at Labor Market Entry? Evidence from South Korea",
    "url": "https://arxiv.org/abs/2608.03153",
    "source": "Dongwoo Kim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03153v1 Announce Type: new Abstract: When in the lifecycle does a large gender wage gap emerge? South Korea has the largest gender pay gap in the OECD, 29%. Among recent college graduates t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03221",
    "domain": "金融",
    "title": "Digital State Capacity",
    "url": "https://arxiv.org/abs/2608.03221",
    "source": "Patrick Healy (Department of Economics, Monash Business School, Monash University, SoDa Laboratories, Monash Business School, Monash University), Simon D. Angus (Department of Economics, Monash Business School, Monash University, SoDa Laboratories, Monash Business School, Monash University), Paul Raschky (Department of Econometrics and Business Statistics, Monash Business School, Monash University, SoDa Laboratories, Monash Business School, Monash University), Klaus Ackermann (Department of Economics, Monash Business School, Monash University, SoDa Laboratories, Monash Business School, Monash University), Nathan Lane (SoDa Laboratories, Monash Business School, Monash University, Department of International Development, London School of Economics and Political Science), Weijia Li (Department of Econometrics and Business Statistics, Monash Business School, Monash University, SoDa Laboratories, Monash Business School, Monash University), Cynthia Huang (SoDa Laboratories, Monash Business School, Monash University, Social Data Science and AI Lab, LMU Munich)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03221v1 Announce Type: new Abstract: Digital State Capacity is the ability of governments to deploy ICT infrastructure and information systems to implement policy. This paper introduces a n"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03466",
    "domain": "金融",
    "title": "A unifying perspective on the collapse to the mean for law-invariant functionals",
    "url": "https://arxiv.org/abs/2608.03466",
    "source": "Felix-Benedikt Liebrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03466v1 Announce Type: new Abstract: We revisit the ``collapse to the mean'' phenomenon, which refers to mild structural conditions, such as local linearity, that force a law-invariant func"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03504",
    "domain": "金融",
    "title": "Stochastic Choice with Advertising",
    "url": "https://arxiv.org/abs/2608.03504",
    "source": "Henrik Petri, Kai Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03504v1 Announce Type: new Abstract: We study how advertised products (e.g., Top Picks, Recommended, Featured) affect consumer choice on digital platforms and retail interfaces by extending"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03570",
    "domain": "金融",
    "title": "Cities and political violence in West Africa",
    "url": "https://arxiv.org/abs/2608.03570",
    "source": "Steven M. Radil, Olivier J. Walther",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03570v1 Announce Type: new Abstract: This paper examines how political violence in West Africa is distributed between urban agglomerations and their surrounding areas using spatially disagg"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03596",
    "domain": "金融",
    "title": "Transnational political violence in African borderlands",
    "url": "https://arxiv.org/abs/2608.03596",
    "source": "David G. Russell, Olivier J. Walther",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03596v1 Announce Type: new Abstract: This paper examines the relationship between borderlands and political violence in Africa. Using spatiotemporal data on conflict events from 1997 to 202"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03703",
    "domain": "金融",
    "title": "Preying on Leveraged ETFs",
    "url": "https://arxiv.org/abs/2608.03703",
    "source": "Yinhong Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03703v1 Announce Type: new Abstract: We argue that the extreme volatility of the Korean market in 2026 was driven by arbitrageurs preying on the closing rebalance of leveraged exchange-trad"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03716",
    "domain": "金融",
    "title": "Synthetic supply networks",
    "url": "https://arxiv.org/abs/2608.03716",
    "source": "Galvin Ng, Luca Mungo, Damien Bertrand, Fran\\c{c}ois Lafond",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03716v1 Announce Type: new Abstract: A good representation of the population of firms and households is essential for large-scale economic models. While there exist good methods to create s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03925",
    "domain": "金融",
    "title": "Option Pricing with Time-Changed Fractional Brownian Motion: A Fractional Variance Gamma Model",
    "url": "https://arxiv.org/abs/2608.03925",
    "source": "Robert Jarrow, Jayen Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03925v1 Announce Type: new Abstract: Fractional Brownian motion (fBm) exhibits attractive features for financial modeling, including long-range dependence, path roughness, and anomalous dif"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02651",
    "domain": "金融",
    "title": "Delegated Monitoring in Public-Private Sector Credit Programs: Underinvestment, Overinvestment, and the Design of Subsidized Lending",
    "url": "https://arxiv.org/abs/2608.02651",
    "source": "G. Charles-Cadogan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.02651v1 Announce Type: cross Abstract: This paper studies public-private partnerships that delegate access-to-credit programs to private equity and venture-capital intermediaries. The publi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.02828",
    "domain": "金融",
    "title": "Proper-score observation-driven filters: local geometry, estimation, and continuous-time limits",
    "url": "https://arxiv.org/abs/2608.02828",
    "source": "Giulia Livieri, Gianluca Palmari",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.02828v1 Announce Type: cross Abstract: Observation-driven filters update a time-varying parameter with the likelihood score, linking the recursion to the logarithmic scoring rule. We replac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03088",
    "domain": "金融",
    "title": "A New Approach to Goodness of Fit for Ergodic Markov Processes",
    "url": "https://arxiv.org/abs/2608.03088",
    "source": "Vance Martin, Yoshihiko Nishiyama, John Stachurski, Yiran Xie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03088v1 Announce Type: cross Abstract: We introduce a new density-based goodness of fit test for ergodic Markov processes. Our test compares the data against the class of models specified i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03616",
    "domain": "金融",
    "title": "Measuring the engine of a liquidation cascade: subcritical branching inside a first-order transition",
    "url": "https://arxiv.org/abs/2608.03616",
    "source": "Ramon Marc Garcia Seuma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.03616v1 Announce Type: cross Abstract: We study seven major crypto-perpetual liquidation cascades (2022-2025), and in the largest of them we can watch the mechanism directly. From the on-ch"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.03285",
    "domain": "金融",
    "title": "The not-so-hidden risks of 'hidden-to-maturity' accounting: on depositor runs and bank resilience",
    "url": "https://arxiv.org/abs/2407.03285",
    "source": "Zachary Feinstein, Grzegorz Halaj, Andreas Sojmark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2407.03285v3 Announce Type: replace Abstract: We introduce a simple model of depositor runs to capture run risks at financial institutions based on their balance sheet composition. Specifically,"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.13763",
    "domain": "金融",
    "title": "Eliciting reference measures of law-invariant functionals",
    "url": "https://arxiv.org/abs/2507.13763",
    "source": "Felix-Benedikt Liebrich, Ruodu Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2507.13763v3 Announce Type: replace Abstract: Law-invariant functionals are central to risk management and assign identical values to random prospects sharing the same distribution under an atom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.04660",
    "domain": "金融",
    "title": "Global Inequalities in Clinical Trials Participation",
    "url": "https://arxiv.org/abs/2601.04660",
    "source": "Wen Lou, Adri\\'an A. D\\'iaz-Faes, Jiangen He, Zhihao Liu, Vincent Larivi\\`ere",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2601.04660v3 Announce Type: replace Abstract: Clinical trials are fundamental to the production of medical evidence and determine who gains access to experimental therapies. Although prior work "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08232",
    "domain": "金融",
    "title": "Hour-Aware Adaptive Risk Management for Autonomous Memecoin Trading on Solana DEXs: Evidence, Theory, and Design Lessons from a 15-Day Deployment",
    "url": "https://arxiv.org/abs/2606.08232",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2606.08232v3 Announce Type: replace Abstract: We report a 15-day paper-traded autonomous memecoin trading deployment on Solana decentralised exchanges (DEXs), designed as a controlled measuremen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02795",
    "domain": "金融",
    "title": "Coordinated Sniper Cohorts on Pump.fun: Detection of 1,012 Persistent Wallet Rings and a Contamination-Adjusted Estimate of Coordination-Specific First-Hour Buyer-Flow Lift",
    "url": "https://arxiv.org/abs/2607.02795",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2607.02795v3 Announce Type: replace Abstract: Motivated by Kyle (1985) informed order flow and the Meiklejohn et al. (2013) wallet-clustering tradition, we ask whether persistent coordinated wal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00328",
    "domain": "金融",
    "title": "Global coal trade is resilient to maritime chokepoints",
    "url": "https://arxiv.org/abs/2608.00328",
    "source": "Jorrit Gosens, Alex B. H. Turnbull, Frank Jotzo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.00328v2 Announce Type: replace Abstract: Maritime chokepoints and their potential disruption of global trade in energy find renewed attention. We analyse global trade in coal, and find that"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00616",
    "domain": "金融",
    "title": "Latent Flow Matching for Arbitrage-Aware Implied Volatility Surface Generation",
    "url": "https://arxiv.org/abs/2608.00616",
    "source": "Oscar Brooks, Dusica Bajalica, Yating Liu, Imen Ben Tahar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.00616v2 Announce Type: replace Abstract: We propose an arbitrage-aware latent flow-matching framework for unconditional implied volatility surface generation. The method first compresses hi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.11257",
    "domain": "金融",
    "title": "Prediction-Enhanced Monte Carlo: A Machine Learning View on Control Variate",
    "url": "https://arxiv.org/abs/2412.11257",
    "source": "Fengpei Li, Haoxian Chen, Jiahe Lin, Arkin Gupta, Xiaowei Tan, Honglei Zhao, Gang Xu, Yuriy Nevmyvaka, Agostino Capponi, Henry Lam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2412.11257v4 Announce Type: replace-cross Abstract: For many complex simulation tasks spanning areas such as healthcare, engineering, and finance, Monte Carlo (MC) methods are invaluable due to "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.01432",
    "domain": "金融",
    "title": "A New Theory of Value for Post-AGI Economics",
    "url": "https://arxiv.org/abs/2608.01432",
    "source": "Keyun Ruan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T04:00:00+00:00",
    "summary": "arXiv:2608.01432v2 Announce Type: replace-cross Abstract: Artificial general intelligence (AGI) may weaken scarcities in labour, expertise, information, and productive capability that underpin establi"
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
  },
  {
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49051055",
    "domain": "金融",
    "title": "Fedora 45 Atomic Desktops Look to Allow for Web-Based Remote Installations",
    "url": "https://www.phoronix.com/news/Fedora-45-Atomic-Remote-Install",
    "source": "nateb2022",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-25T20:10:00+00:00",
    "summary": ""
  }
]
```
