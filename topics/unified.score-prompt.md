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

- 今日日期：`2026-10-30`
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
  "date": "2026-10-30",
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
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 2053832,
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
    "points": 1453047,
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
    "points": 1411167,
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
    "points": 1372243,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1VZWc6dECG",
    "domain": "AI",
    "title": "【Re:从零开始的AI学习】第一季总集篇｜从入门到用好 AI",
    "url": "http://www.bilibili.com/video/av117430848391663",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 1096292,
    "published_at": "2026-10-13T00:57:21+00:00",
    "summary": "这次，我把【Re：从零开始的 AI 学习】第一季全 13 期完整连在一起啦！\n新来的朋友或者想要查漏补缺的伙伴，现在可以一口气通关！从 AI 入门与提示词技巧，到 Agent 玩法、主流模型对比与使用成本……跟着走一遍就能彻底搞懂。\n希望这个系列能给你带来哪怕一点点启发，欢迎点赞、投币、收藏一键三连支持！也超级欢迎转发安利给身边的朋友～\n\n【目录】\n00:00 导语\n00:32 AI 这三年发生了"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 906951,
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
    "points": 883234,
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
    "points": 735947,
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
    "points": 594739,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 426478,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 357602,
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
    "points": 340627,
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
    "points": 317445,
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
    "points": 289813,
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
    "points": 220396,
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
    "points": 185208,
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
    "points": 164028,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 161437,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151718,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 145924,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103408,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 94788,
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
    "points": 93759,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1renJ6VEuZ",
    "domain": "AI",
    "title": "DeepSeekHarness装进手机",
    "url": "http://www.bilibili.com/video/av117467271666305",
    "source": "文大师啵啵",
    "platform": "bilibili",
    "points": 80208,
    "published_at": "2026-10-19T11:14:25+00:00",
    "summary": "如果把 DeepSeek Harness 完整搬进 Android，手机会变成什么？\n\n它不是又一个聊天助手，而是一台随身 AI 工作站：有自己的工作区、Linux 环境、终端、文件管理系统、插件系统，也能通过无障碍或者 Shizuku 操作手机，并通过内置浏览器实现网页自动化。\n\n这个项目叫 DSHBox，让 DeepSeek Harness 运行在手机上。\n\n本视频展示从首页进入、选择工作区、"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 77232,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 73283,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64076,
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
    "points": 56529,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1RrZHYqEvm",
    "domain": "AI",
    "title": "Cursor+Figma MCP，自动生成可编辑设计稿",
    "url": "http://www.bilibili.com/video/av114257538650701",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 52797,
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
    "points": 49871,
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
    "points": 47776,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41054,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 35839,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34619,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 33436,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29898,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 29564,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 29028,
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
    "points": 25808,
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
    "points": 24692,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22833,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21173,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1Kcso6KEsC",
    "domain": "AI",
    "title": "Anthropic 正式发布 Claude 2.0（17 分钟速通）",
    "url": "http://www.bilibili.com/video/av117521445292425",
    "source": "GoldenSpiderAI",
    "platform": "bilibili",
    "points": 18271,
    "published_at": "2026-10-29T00:51:37+00:00",
    "summary": "视频标题\nAnthropic 正式发布 Claude 2.0（17 分钟速通）\n\n原视频链接\nhttps://www.youtube.com/watch?v=yMnFHFf43Qg\n\n原视频发布时间\n2026-10-28\n\n-----\n---\n时间戳\n00:00 - 开场\n00:52 - 为什么非程序员也要用 Claude Code\n01:30 - 功能 1\n03:13 - 免费 PDF 指南：所"
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 18289,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15449,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 13364,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1Y4Gd6LELX",
    "domain": "AI",
    "title": "极简安装！Claude Code+CC switch 连接 Deepseek",
    "url": "http://www.bilibili.com/video/av116634383550090",
    "source": "水哥澎湃",
    "platform": "bilibili",
    "points": 12554,
    "published_at": "2026-05-25T09:00:14+00:00",
    "summary": "本视频分享Claude Code 极简安装 + 连接 Deepseek的完整方案，解决国内用户使用不稳定、收费高的问题。用 Harness（马鞍缰绳）思路通俗讲解核心价值，让大模型拥有本地执行、记忆、任务编排能力。全程无复杂命令，包含 Claude Code 部署、CC switch 安装、Deepseek API 配置、连接测试，一步到位，新手也能轻松搞定。\n\n\n00:00  1-目标\n00:2"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11440,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1rhdgBMEK2",
    "domain": "AI",
    "title": "Claude Code + Figma MCP：传统 UI 开发流程已死？",
    "url": "http://www.bilibili.com/video/av116538183124050",
    "source": "犬哥网站",
    "platform": "bilibili",
    "points": 10789,
    "published_at": "2026-05-08T12:00:00+00:00",
    "summary": "▬▬▬▬▬ 🏆️ 犬哥专业服务 🏆️ ▬▬▬▬▬\n网页设计＆数位行销服务 ➜ https://frankknow.com\nWordPress 优质主机：https://frankknow.com/wordpress-hosting/\n\n▬▬▬▬▬ 🏆️ 精选架站系列 🏆️ ▬▬▬▬▬\n新手自学架站（网域＋主机＋WordPress 架站，一次学会）➜ https://frankknow.com/wp"
  },
  {
    "id": "bvid:BV1ixxM6mE5T",
    "domain": "AI",
    "title": "vibe coding破防瞬间",
    "url": "http://www.bilibili.com/video/av117511798395204",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 10386,
    "published_at": "2026-10-29T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49970667",
    "domain": "AI 算力 / 半导体",
    "title": "Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates",
    "url": "https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors",
    "source": "outlier99",
    "platform": "hackernews",
    "points": 495,
    "published_at": "2026-10-05T21:00:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50293047",
    "domain": "AI 算力 / 半导体",
    "title": "Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang",
    "url": "https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 325,
    "published_at": "2026-10-29T17:43:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50219700",
    "domain": "AI 算力 / 半导体",
    "title": "GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000's cards",
    "url": "https://github.com/Zagitta/gpu-unlock",
    "source": "fragebogen",
    "platform": "hackernews",
    "points": 350,
    "published_at": "2026-10-24T09:58:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236073",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 175,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50247677",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discusses $2k-per-GPU annual fee for software",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform",
    "source": "gscott",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-10-26T17:34:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/infineons-oktobertech-edge-ai-sdvs-and-the-road-to-800-vdc/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon’s OktoberTech: Edge AI, SDVs, and the Road to 800 VDC",
    "url": "https://www.eetimes.com/infineons-oktobertech-edge-ai-sdvs-and-the-road-to-800-vdc/",
    "source": "Aalyia Shaukat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:59:28+00:00",
    "summary": "Explore Infineon’s OktoberTech takeaways on edge AI, SDVs, GaN power, and the shift toward 800 V DC data centers. The post Infineon’s OktoberTech: Edge AI, SDVs, and the Road to 800 VDC appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/samsung-electronics-posts-80b-operating-profit-on-ai-memory-demand/",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Electronics Posts $80B Operating Profit on AI Memory Demand",
    "url": "https://www.eetimes.com/samsung-electronics-posts-80b-operating-profit-on-ai-memory-demand/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:20:34+00:00",
    "summary": "Samsung reported third-quarter operating profit of $80 billion, but rising component prices caused an operating loss in mobile. The post Samsung Electronics Posts $80B Operating Profit on AI Memory De"
  },
  {
    "id": "rss:https://www.eetimes.com/how-vision-and-connectivity-enable-autonomous-agriculture/",
    "domain": "AI 算力 / 半导体",
    "title": "How Vision and Connectivity Enable Autonomous Agriculture",
    "url": "https://www.eetimes.com/how-vision-and-connectivity-enable-autonomous-agriculture/",
    "source": "Analog Devices, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:07:54+00:00",
    "summary": "Join this webinar to explore how Gigabit Multimedia Serial Link (GMSL) technology helps enable the next generation of autonomous agricultural equipment. The post How Vision and Connectivity Enable Aut"
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-power-sequencing-with-greenpak/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Power Sequencing with GreenPAK™",
    "url": "https://www.eetimes.com/smarter-power-sequencing-with-greenpak/",
    "source": "Dima Mymrikov, Sr. Director of GreenPAK Product Marketing, Renesas Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T13:00:00+00:00",
    "summary": "Programmable mixed-signal devices can replace sprawling RC networks and firmware-dependent control with compact, deterministic, and adaptable multi-rail sequencing. The post Smarter Power Sequencing w"
  },
  {
    "id": "rss:https://www.eetimes.com/stmicroelectronics-weighs-developing-more-powerful-mcus-mpus-for-humanoid-robots/",
    "domain": "AI 算力 / 半导体",
    "title": "STMicroelectronics Weighs Developing More Powerful MCUs, MPUs for Humanoid Robots",
    "url": "https://www.eetimes.com/stmicroelectronics-weighs-developing-more-powerful-mcus-mpus-for-humanoid-robots/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:48:02+00:00",
    "summary": "With humanoid robot designs still evolving and volumes low, STMicroelectronics is watching how the market develops before deciding what to build. The post STMicroelectronics Weighs Developing More Pow"
  },
  {
    "id": "rss:https://www.eetimes.com/how-ai-redefines-semiconductor-manufacturing-from-materials-up/",
    "domain": "AI 算力 / 半导体",
    "title": "How AI Redefines Semiconductor Manufacturing, From Materials Up",
    "url": "https://www.eetimes.com/how-ai-redefines-semiconductor-manufacturing-from-materials-up/",
    "source": "Mahiro Tsujino",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T08:30:08+00:00",
    "summary": "AI chip advances depend on more than design, requiring new materials, manufacturing equipment, and packaging technologies to meet rising performance demands. The post How AI Redefines Semiconductor Ma"
  },
  {
    "id": "rss:https://www.eetimes.com/canadian-startup-aims-to-be-quantums-picks-and-shovels/",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian Startup Aims to Be Quantum’s ‘Picks’ and ‘Shovels’",
    "url": "https://www.eetimes.com/canadian-startup-aims-to-be-quantums-picks-and-shovels/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T20:50:32+00:00",
    "summary": "Toronto-based Meissner Technologies uses AI and laboratory testing to discover superconducting materials that could cut cooling costs and help quantum computers scale. The post Canadian Startup Aims t"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynix-reports-record-q3-results-driven-by-ai-memory-surge/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix Reports Record Q3 Results Driven by AI Memory Surge",
    "url": "https://www.eetimes.com/sk-hynix-reports-record-q3-results-driven-by-ai-memory-surge/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T16:43:42+00:00",
    "summary": "Long-term customer contracts and rising chip prices point to a change in how memory manufacturers manage multi-year production capacity and capex. The post SK Hynix Reports Record Q3 Results Driven by"
  },
  {
    "id": "rss:https://www.eetimes.com/secure-safety-and-security-communications/",
    "domain": "AI 算力 / 半导体",
    "title": "Secure Safety and Security Communications",
    "url": "https://www.eetimes.com/secure-safety-and-security-communications/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T14:00:00+00:00",
    "summary": "This whitepaper explores how building safety and security systems can overcome the limitations of legacy RS-485 networks by adopting Single Pair Ethernet (SPE). It examines the growing demands of AI-e"
  },
  {
    "id": "rss:https://www.eetimes.com/full-stack-semiconductor-solutions-for-embodied-ai-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "Full-Stack Semiconductor Solutions for Embodied AI & Robotics",
    "url": "https://www.eetimes.com/full-stack-semiconductor-solutions-for-embodied-ai-robotics/",
    "source": "NSING",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T14:00:00+00:00",
    "summary": "NSING Technologies, a Singapore-founded semiconductor company, presents this whitepaper on its full-stack semiconductor solutions for embodied AI and robotics, built around high-performance MCUs, secu"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/deadly-intel-fab-28-explosion-causes-two-week-shutdown-to-cost-usd600-million-and-severely-disrupt-server-chip-manufacturing-for-six-months-10nm-xeon-shipments-stall-during-largest-shortage-in-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Deadly Intel Fab 28 explosion causes two-week shutdown, to cost $600 million and severely disrupt server chip manufacturing for six months — 10nm Xeon shipments stall during largest shortage in memory",
    "url": "https://www.tomshardware.com/pc-components/cpus/deadly-intel-fab-28-explosion-causes-two-week-shutdown-to-cost-usd600-million-and-severely-disrupt-server-chip-manufacturing-for-six-months-10nm-xeon-shipments-stall-during-largest-shortage-in-memory",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T09:30:00+00:00",
    "summary": "A two-week shutdown of Intel's Fab 28 in Israel will affect server CPU shipments for two consecutive quarters."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-confirms-nova-lake-will-use-advanced-18a-p-node-more-details-at-ces-company-says-its-taking-panther-lake-capacity-offline-to-build-more-granite-rapids-data-center-cpus",
    "domain": "AI 算力 / 半导体",
    "title": "Intel confirms Nova Lake CPUs will use advanced 18A-P node, more details at CES — company says it's taking Panther Lake capacity offline to build more Granite Rapids data center CPUs",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-confirms-nova-lake-will-use-advanced-18a-p-node-more-details-at-ces-company-says-its-taking-panther-lake-capacity-offline-to-build-more-granite-rapids-data-center-cpus",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T21:55:48+00:00",
    "summary": "Intel's next-gen Nova Lake desktop processors will be the first client product to use Intel's enhanced 18A-P node, CEO Lip-Bu Tan confirmed in the company's Q3 2026 earnings call."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacex-buying-out-418-homes-near-flagship-ai-data-center-but-only-if-they-drop-participation-in-lawsuit-report-claims-the-company-is-targeting-an-entire-neighborhood-but-will-only-buy-from-people-who-dont-pursue-noise-pollution-complaints",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's SpaceX buying out 418 homes near flagship AI data center, but only if they drop participation in lawsuit",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacex-buying-out-418-homes-near-flagship-ai-data-center-but-only-if-they-drop-participation-in-lawsuit-report-claims-the-company-is-targeting-an-entire-neighborhood-but-will-only-buy-from-people-who-dont-pursue-noise-pollution-complaints",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T15:40:20+00:00",
    "summary": "The properties will supposedly house SpaceXSI staff while also giving a chance to those who don't want to live near the data center to sell their homes."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ai-demand-triggers-massive-pcb-shortage-for-pc-makers-as-order-books-full-until-2030-lead-times-stretch-to-30-months-as-material-costs-surge-12x",
    "domain": "AI 算力 / 半导体",
    "title": "AI demand triggers massive PCB shortage for PC makers as order books full until 2030",
    "url": "https://www.tomshardware.com/pc-components/ai-demand-triggers-massive-pcb-shortage-for-pc-makers-as-order-books-full-until-2030-lead-times-stretch-to-30-months-as-material-costs-surge-12x",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T15:25:25+00:00",
    "summary": "The AI industry continues to gobble up manufacturing resources that were once dedicated to serving PC, smart device, and gadget makers. Inevitably, the PCB industry has started to feel its effects."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-data-centers-could-wipe-out-15-years-worth-of-progress-in-greenhouse-gas-emissions-report-claims-buildouts-could-emit-as-much-carbon-dioxide-as-all-of-mexico",
    "domain": "AI 算力 / 半导体",
    "title": "US data centers could wipe out 15 years' worth of progress in greenhouse gas emissions, report claims",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-data-centers-could-wipe-out-15-years-worth-of-progress-in-greenhouse-gas-emissions-report-claims-buildouts-could-emit-as-much-carbon-dioxide-as-all-of-mexico",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T14:34:54+00:00",
    "summary": "The Sierra Club, one of the oldest environmental preservation organizations in the U.S., has now put forth an estimate that by 2030, U.S. data center buildouts will be outputting as much carbon dioxid"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-geforce-rtx-5080-prices-hit-usd2-000-costing-more-than-the-rtx-5090-did-at-launch-and-with-limited-stock-available-original-usd999-msrp-long-forgotten-with-prices-now-2-3x-higher",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia GeForce RTX 5080 prices hit $2,000, costing more than the RTX 5090 did at launch and with limited stock available",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-geforce-rtx-5080-prices-hit-usd2-000-costing-more-than-the-rtx-5090-did-at-launch-and-with-limited-stock-available-original-usd999-msrp-long-forgotten-with-prices-now-2-3x-higher",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T14:21:59+00:00",
    "summary": "It costs just as much to buy an Nvidia GeForce RTX 5080 right now as the launch price for the RTX 5090, with prices now at least two times higher for this high spec GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/hyperx-omen-35l-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Omen 35L review: A polished gaming PC for deep pockets",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/hyperx-omen-35l-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T14:00:00+00:00",
    "summary": "Premium styling, quiet operation, and impressive performance elevates the HyperX Omen 35L into competition with the best the market has to offer. But whether it's worth the money depends on which conf"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/nvidia-ceo-jensen-huang-may-have-been-the-target-of-a-spy-plot-through-chinese-intelligence-asset-report-claims-exec-from-firm-under-investigation-for-smuggling-banned-ai-chips-to-china-accused-of-being-a-spy-was-also-feeding-information-to-beijing",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang may have been the target of a spy plot through 'Chinese intelligence asset,' report claims",
    "url": "https://www.tomshardware.com/tech-industry/policy/nvidia-ceo-jensen-huang-may-have-been-the-target-of-a-spy-plot-through-chinese-intelligence-asset-report-claims-exec-from-firm-under-investigation-for-smuggling-banned-ai-chips-to-china-accused-of-being-a-spy-was-also-feeding-information-to-beijing",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T13:04:23+00:00",
    "summary": "Sources say that Alice Huang, a senior executive at an Nvidia cloud partner who has close ties with Jensen Huang, is suspected of passing information to Beijing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/dept-of-justice-reportedly-probes-nvidia-over-usd13-billion-hugging-face-ai-platform-acquisition-concerns-raised-over-competition-in-ai-and-pressure-on-customers",
    "domain": "AI 算力 / 半导体",
    "title": "Dept of Justice reportedly probes Nvidia over $13 billion Hugging Face AI platform acquisition",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/dept-of-justice-reportedly-probes-nvidia-over-usd13-billion-hugging-face-ai-platform-acquisition-concerns-raised-over-competition-in-ai-and-pressure-on-customers",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T12:49:19+00:00",
    "summary": "Nvidia's near $13 billion buyout of Hugging Face has come under scrutiny over concerns that it will impact competition in the AI space."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/tech-whizzs-internet-accessible-synology-nas-gets-bit-by-ransomware-attack-from-18-month-old-remote-code-execution-flaw-security-updates-neglected-in-a-series-of-catastrophic-errors",
    "domain": "AI 算力 / 半导体",
    "title": "Tech whiz's internet-accessible Synology NAS gets bit by ransomware attack from 18-month-old remote code execution flaw",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/tech-whizzs-internet-accessible-synology-nas-gets-bit-by-ransomware-attack-from-18-month-old-remote-code-execution-flaw-security-updates-neglected-in-a-series-of-catastrophic-errors",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T12:41:14+00:00",
    "summary": "Tech whizz' internet-accessible Synology NAS gets bit by transomware attack — security updates 18 months out of date in a series of catastrophic errors"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/our-first-step-at-defining-a-cpu-benchmark-for-agentic-ai-how-we-can-measure-throughput-of-agentic-ai-workloads-without-any-gpu-involved",
    "domain": "AI 算力 / 半导体",
    "title": "Our first step at defining a CPU benchmark for agentic AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/our-first-step-at-defining-a-cpu-benchmark-for-agentic-ai-how-we-can-measure-throughput-of-agentic-ai-workloads-without-any-gpu-involved",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T12:20:00+00:00",
    "summary": "Over the past six months, CPUs have taken center stage as agentic AI workloads evolve. Here’s our first attempt at trying to measure CPU performance when running agentic workloads."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-huge-usd1-250-saving-on-this-alienware-gaming-pc-with-an-rtx-5070-ti-and-32gb-ddr5-right-now-big-newegg-price-drop-means-you-can-grab-this-4k-ready-rig-with-a-24-core-intel-cpu-and-1tb-ssd-for-usd2-599-99",
    "domain": "AI 算力 / 半导体",
    "title": "Score a huge $1,250 saving on this Alienware gaming PC with an RTX 5070 Ti and 32GB DDR5 right now",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-huge-usd1-250-saving-on-this-alienware-gaming-pc-with-an-rtx-5070-ti-and-32gb-ddr5-right-now-big-newegg-price-drop-means-you-can-grab-this-4k-ready-rig-with-a-24-core-intel-cpu-and-1tb-ssd-for-usd2-599-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:55:45+00:00",
    "summary": "You can save $1,250 on this Alienware Aurora gaming PC with an RTX 5070 Ti and 32GB of DDR5 RAM, now priced at just $2,599.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/fujifilm-plans-5x-production-boost-of-100tb-magnetic-storage-tapes-driven-by-ai-usd63-million-injection-is-the-largest-investment-in-tape-for-20-years",
    "domain": "AI 算力 / 半导体",
    "title": "Fujifilm plans 5x production boost of 100TB magnetic storage tapes driven by skyrocketing AI storage demand",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/fujifilm-plans-5x-production-boost-of-100tb-magnetic-storage-tapes-driven-by-ai-usd63-million-injection-is-the-largest-investment-in-tape-for-20-years",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:40:00+00:00",
    "summary": "Fujifilm plans to increase the production of magnetic tape by as much as 5x as it works to meet a newfound demand for AI data center storage."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd234-on-32gb-of-ddr5-ram-with-this-four-item-am5-newegg-bundle-score-g-skill-trident-z5-neox-ram-the-venerable-ryzen-7-9800x3d-processor-gigabyte-x870e-aorus-elite-wifi7-motherboard-and-a-free-240mm-aio-for-only-usd1-069",
    "domain": "AI 算力 / 半导体",
    "title": "Save $234 on 32GB of DDR5 RAM with this 3-item AM5 Newegg bundle",
    "url": "https://www.tomshardware.com/pc-components/save-usd234-on-32gb-of-ddr5-ram-with-this-four-item-am5-newegg-bundle-score-g-skill-trident-z5-neox-ram-the-venerable-ryzen-7-9800x3d-processor-gigabyte-x870e-aorus-elite-wifi7-motherboard-and-a-free-240mm-aio-for-only-usd1-069",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:31:57+00:00",
    "summary": "This Newegg AM5 combo deal is $234 off. Priced at only $1,069, you get a Ryzen7 9800X3D, X870E Aorus Elite Wifi7 board, 32GB of G.Skill DDR5-6000 RAM and a free MSI AIO cooler."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ipo-filing-shows-most-of-its-compute-goes-to-r-and-d-not-serving-customers-company-details-massive-usd800-billion-in-tpu-and-gpu-contracts",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic’s IPO filing shows most of its compute goes to R&D, not serving customers",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ipo-filing-shows-most-of-its-compute-goes-to-r-and-d-not-serving-customers-company-details-massive-usd800-billion-in-tpu-and-gpu-contracts",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:30:00+00:00",
    "summary": "Anthropic’s S-1 splits its $8.9 billion H1 compute bill: most went to R&amp;D, with less than a third estimated to serve Claude customers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fake-ps5-emulators-are-being-used-to-infect-gamers-computers-with-password-scraping-malware-two-well-known-github-repos-including-anyps5-hit",
    "domain": "AI 算力 / 半导体",
    "title": "Fake PS5 emulators are being used to steal gamers' passwords",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fake-ps5-emulators-are-being-used-to-infect-gamers-computers-with-password-scraping-malware-two-well-known-github-repos-including-anyps5-hit",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:20:00+00:00",
    "summary": "Malware disguised as two popular PS5 game emulators, distributed via GitHub, has been identified as stealing passwords from unsuspecting gamers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/secular-humanist-gets-religious-exemption-from-using-ai-argues-that-offloading-his-thinking-to-llms-violates-his-beliefs-american-humanist-association-says-its-the-first-case-of-its-kind",
    "domain": "AI 算力 / 半导体",
    "title": "Man granted first-of-its-kind religious exemption against mandatory AI use at work",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/secular-humanist-gets-religious-exemption-from-using-ai-argues-that-offloading-his-thinking-to-llms-violates-his-beliefs-american-humanist-association-says-its-the-first-case-of-its-kind",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:00:00+00:00",
    "summary": "A research administrator at the University of Kentucky was granted a Title VII exemption, allowing them to not use AI tools as it goes against their moral beliefs."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/github-report-highlights-massive-influx-of-ai-generated-code-sixfold-increase-in-activity-over-one-year-required-extra-4-million-cpu-cores-and-160pb-of-storage",
    "domain": "AI 算力 / 半导体",
    "title": "GitHub says massive influx of AI-generated code required extra 4 million CPU cores and 160 petabytes of storage to manage",
    "url": "https://www.tomshardware.com/software/github-report-highlights-massive-influx-of-ai-generated-code-sixfold-increase-in-activity-over-one-year-required-extra-4-million-cpu-cores-and-160pb-of-storage",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T10:30:00+00:00",
    "summary": "Agentic AI led to a sixfold year-on-year influx of new code at GitHub, leading the company to add 4 million CPU cores and 160PB of storage to its datacenters"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/flock-ignores-minnesota-citys-orders-not-to-reinstall-ai-surveillance-cameras-citizens-complain-after-spotting-two-cameras-despite-the-city-canceling-its-contract",
    "domain": "AI 算力 / 半导体",
    "title": "Flock ignores Minnesota city’s orders not to reinstall AI surveillance cameras",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/flock-ignores-minnesota-citys-orders-not-to-reinstall-ai-surveillance-cameras-citizens-complain-after-spotting-two-cameras-despite-the-city-canceling-its-contract",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T10:00:00+00:00",
    "summary": "Dayton, MN's city council removed Flock cameras and canceled its contract in August, but Flock reinstalled cameras anyway, almost a month after the program's suspension."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/apple-launches-new-macbook-with-touchscreen-and-oled-starts-at-usd2-899",
    "domain": "AI 算力 / 半导体",
    "title": "Apple launches new MacBook Pro with touchscreen and OLED — starts at $2,899",
    "url": "https://www.tomshardware.com/laptops/apple-launches-new-macbook-with-touchscreen-and-oled-starts-at-usd2-899",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:15:39+00:00",
    "summary": "The computer is also lighter and has an updated speaker system."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub",
    "domain": "AI 算力 / 半导体",
    "title": "Malaysia seizes $12 million worth of advanced AI chips hidden inside 30 servers",
    "url": "https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:02:14+00:00",
    "summary": "Malaysian customs seized 30 servers containing more than $12 million worth of advanced AI chips at Kuala Lumpur International Airport, as authorities investigate a suspected smuggling network linked t"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/ai-component-hikes-force-the-worlds-largest-pc-makers-to-return-manufacturing-capacity-to-china-brands-to-seek-lower-production-costs-and-efficiency-in-established-supply-chain",
    "domain": "AI 算力 / 半导体",
    "title": "AI component hikes force the world's largest PC makers to return manufacturing capacity to China",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/ai-component-hikes-force-the-worlds-largest-pc-makers-to-return-manufacturing-capacity-to-china-brands-to-seek-lower-production-costs-and-efficiency-in-established-supply-chain",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:24:16+00:00",
    "summary": "PC manufacturing in China tends to be cheaper because of an established supply chain and workforce. Smaller Chinese suppliers are also winning orders by offering easier access to domestic chip manufac"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-tells-engineers-to-stop-tokenmaxxing-to-look-productive-says-ai-will-be-central-to-software-development-but-usage-is-not-the-goal-new-guidelines-claim",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon tells engineers to stop ‘tokenmaxxing’ to look productive",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-tells-engineers-to-stop-tokenmaxxing-to-look-productive-says-ai-will-be-central-to-software-development-but-usage-is-not-the-goal-new-guidelines-claim",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:13:48+00:00",
    "summary": "Amazon has published new engineering guidelines warning developers and managers against ‘tokenmaxxing,’ arguing that AI usage metrics are ‘deeply flawed’ unless tied to long-term outcomes. The move fo"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/fcc-rebuffs-tp-link-again-as-it-attempts-to-sell-wi-fi-8-gear-in-the-us-fcc-alleges-inaccurate-documentation-and-out-of-spec-power-levels-for-routers",
    "domain": "AI 算力 / 半导体",
    "title": "FCC rebuffs TP-Link again as it attempts to sell Wi-Fi 8 gear in the US",
    "url": "https://www.tomshardware.com/networking/routers/fcc-rebuffs-tp-link-again-as-it-attempts-to-sell-wi-fi-8-gear-in-the-us-fcc-alleges-inaccurate-documentation-and-out-of-spec-power-levels-for-routers",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:07:35+00:00",
    "summary": "TP-Link just can’t seem to catch a break with the FCC, as it’s not under fire for exceeding power limits on its routers"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/corsair-warthog-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair Warthog case review: A rugged, military-themed chassis with plenty of airflow",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/corsair-warthog-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T14:00:00+00:00",
    "summary": "The military-inspired Warthog mid-tower borrows from Corsair’s Vengeance C70 and takes the military aesthetic up a couple of notches. Is the rugged look worth it?"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/us-marines-join-nato-mission-in-the-baltic-sea-to-protect-undersea-cables-from-sabotage-as-russia-continues-to-lurk-around-four-dozen-recon-and-intel-specialists-deployed-to-deter-seabed-threats",
    "domain": "AI 算力 / 半导体",
    "title": "US Marines join NATO mission in the Baltic Sea to protect undersea cables from sabotage as Russia continues to lurk",
    "url": "https://www.tomshardware.com/tech-industry/us-marines-join-nato-mission-in-the-baltic-sea-to-protect-undersea-cables-from-sabotage-as-russia-continues-to-lurk-around-four-dozen-recon-and-intel-specialists-deployed-to-deter-seabed-threats",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T13:24:14+00:00",
    "summary": "50 U.S. marines are joining a NATO mission to help protect and monitor undersea infrastructure in the Baltic Sea."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/sk-hynix-owned-solidigm-is-plotting-a-new-usd45-billion-flash-memory-factory-for-the-us-report-claims-wants-go-ahead-to-export-equipment-for-china-upgrades-in-return",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix-owned Solidigm is plotting a new $45 billion flash memory factory for the US, report claims",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/sk-hynix-owned-solidigm-is-plotting-a-new-usd45-billion-flash-memory-factory-for-the-us-report-claims-wants-go-ahead-to-export-equipment-for-china-upgrades-in-return",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T13:01:21+00:00",
    "summary": "Solidigm, an American subsidiary of SK hynix, is in discussions about potentially investing $45 billion in a new flash chip factory that would be built in the United States."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-hdds/seagates-16tb-external-hdd-falls-to-0-025-cents-per-gb-at-newegg-this-storage-deal-is-usd50-cheaper-than-even-its-prime-day-sale-price",
    "domain": "AI 算力 / 半导体",
    "title": "Seagate's 16TB external HDD falls to 0.025 cents per GB at Newegg",
    "url": "https://www.tomshardware.com/pc-components/external-hdds/seagates-16tb-external-hdd-falls-to-0-025-cents-per-gb-at-newegg-this-storage-deal-is-usd50-cheaper-than-even-its-prime-day-sale-price",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T13:00:00+00:00",
    "summary": "Save $150 on this 16TB Seagate Expansion Desktop External HDD when you make use of this Newegg deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/why-native-pc-ports-of-console-games-are-suddenly-everywhere-reverse-engineer-anything-gives-ai-agents-a-unified-toolkit-and-byte-for-byte-checks-keep-hallucinations-in-line",
    "domain": "AI 算力 / 半导体",
    "title": "Why native PC ports of console games are suddenly everywhere",
    "url": "https://www.tomshardware.com/video-games/why-native-pc-ports-of-console-games-are-suddenly-everywhere-reverse-engineer-anything-gives-ai-agents-a-unified-toolkit-and-byte-for-byte-checks-keep-hallucinations-in-line",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T12:00:00+00:00",
    "summary": "With dozens of titles unofficially ported to PC over the past few months, the big questions are: why is this now possible, and what changed?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-gpu-vendor-palit-denies-its-galax-factory-has-closed-due-to-a-shortage-of-chips-company-says-brand-continues-to-operate-as-usual",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX GPU vendor Palit denies its Galax factory has closed due to a shortage of chips",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-gpu-vendor-palit-denies-its-galax-factory-has-closed-due-to-a-shortage-of-chips-company-says-brand-continues-to-operate-as-usual",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T11:56:26+00:00",
    "summary": "Palit denies news that Galax is going out of production."
  },
  {
    "id": "hn:50128597",
    "domain": "AI 算力 / 半导体",
    "title": "EU negotiates sanctions swap with China to rescue critical ASML supplier",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/eu-negotiates-sanction-swap-with-china-to-rescue-critical-asml-supplier-german-coatings-firm-faces-shutdown-without-chinese-rare-earths",
    "source": "anigbrowl",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-17T06:49:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "AI 算力 / 半导体",
    "title": "xAI’s Colossus 2 – First Gigawatt Datacenter In The World, Unique RL Methodology, Capital Raise",
    "url": "https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-16T17:38:01+00:00",
    "summary": "Much has been written about xAI’s Colossus 1. The Memphis build belongs in the history books: the largest AI training cluster, erected from scratch in 122 days. With roughly 200,000 H100/H200s and ~30"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "domain": "AI 算力 / 半导体",
    "title": "Another Giant Leap: The Rubin CPX Specialized Accelerator & Rack",
    "url": "https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-10T19:57:18+00:00",
    "summary": "Nvidia announced the Rubin CPX, a solution that is specifically designed to be optimized for the prefill phase, with the single-die Rubin CPX heavily emphasizing compute FLOPS over memory bandwidth. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck",
    "url": "https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-08T09:54:57+00:00",
    "summary": "Compute is the lifeblood of AI. He who controls the spice controls the universe the compute will control the production of tokens and reap the benefits of AI. Without compute you do not have a seat at"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s AI Resurgence: AWS & Anthropic’s Multi-Gigawatt Trainium Expansion",
    "url": "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-03T20:55:46+00:00",
    "summary": "Two-and-a-half years ago, we flagged a looming “cloud crisis” at AWS. Today, the evidence has mounted. AWS is the crown jewel of the Amazon empire, generating ~60% of group profits, and dominating the"
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
    "points": 1039,
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
    "points": 1007,
    "published_at": "2026-10-28T17:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 775,
    "published_at": "2026-10-04T19:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 336,
    "published_at": "2026-10-29T12:41:56+00:00",
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
    "id": "hn:50299212",
    "domain": "大厂 AI 动态",
    "title": "AGI Economics: Coordination vs. Competence",
    "url": "https://institute.deepmind.com/essays/the-economics-of-intelligence/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-30T02:36:33+00:00",
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
    "id": "rss:https://www.theverge.com/policy/1022880/wikipedia-openai-new-york-times-copyright",
    "domain": "大厂 AI 动态",
    "title": "Wikipedia’s operator says a bad AI copyright ruling could threaten the open web",
    "url": "https://www.theverge.com/policy/1022880/wikipedia-openai-new-york-times-copyright",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T09:00:00+00:00",
    "summary": "The Wikimedia Foundation is staking out a middle ground in a group of landmark AI copyright cases, pushing courts to legally protect large language models (LLMs) training on copyrighted work - but not"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/1022934/curry-barker-obsession-horror-short-youtube-mama-bear",
    "domain": "大厂 AI 动态",
    "title": "The director of Obsession put a new horror short on YouTube",
    "url": "https://www.theverge.com/streaming/1022934/curry-barker-obsession-horror-short-youtube-mama-bear",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T23:57:18+00:00",
    "summary": "Curry Barker, the director behind the hit horror film Obsession, just published a new horror short on YouTube. The short, titled \"Mama Bear,\" is nearly five minutes long. The video is pretty unnerving"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1022911/intel-wildcat-lake-sold-out-ram-shortage",
    "domain": "大厂 AI 动态",
    "title": "Intel says it&#8217;s selling every affordable laptop chip it can make",
    "url": "https://www.theverge.com/tech/1022911/intel-wildcat-lake-sold-out-ram-shortage",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T23:42:21+00:00",
    "summary": "During Intel's latest earnings call, CEO Lip-Bu Tan said that demand for its budget-focused Wildcat Lake chips \"is outstripping supply.\" According to CFO David Zinsner, the chips are now sold out. Zin"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1022848/reddit-ceo-google-ai-mode-traffic",
    "domain": "大厂 AI 动态",
    "title": "Reddit’s CEO says Google’s AI Mode ‘does not drive traffic’",
    "url": "https://www.theverge.com/tech/1022848/reddit-ceo-google-ai-mode-traffic",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T22:19:32+00:00",
    "summary": "Reddit CEO Steve Huffman said in an earnings call today that Google's AI-powered search modes do not help with traffic to the platform, echoing problems facing other websites and publishers. As part o"
  },
  {
    "id": "rss:https://www.theverge.com/news/1022626/patrick-stewart-star-trek-death",
    "domain": "大厂 AI 动态",
    "title": "Patrick Stewart has died at age 86",
    "url": "https://www.theverge.com/news/1022626/patrick-stewart-star-trek-death",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:10:02+00:00",
    "summary": "Patrick Stewart, best known for his roles in Star Trek and X-Men, has died at age 86. A message posted to Stewart's Instagram account says the actor died in his Los Angeles home on Wednesday \"followin"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1022571/reddit-login-requirement-q3-2026-earnings",
    "domain": "大厂 AI 动态",
    "title": "Reddit will force everyone to log in",
    "url": "https://www.theverge.com/tech/1022571/reddit-login-requirement-q3-2026-earnings",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:07:00+00:00",
    "summary": "Reddit is announcing a huge shift: It's going to start requiring users to log in. Right now, you can browse Reddit without having an account, and the site is generally a great resource for crowdsource"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1022420/rivian-q3-earnings-r2-sales-volkswagen-software",
    "domain": "大厂 AI 动态",
    "title": "Rivian’s R2 is officially its best-selling vehicle",
    "url": "https://www.theverge.com/transportation/1022420/rivian-q3-earnings-r2-sales-volkswagen-software",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:02:00+00:00",
    "summary": "Rivian reported its third quarter earnings of 2026, providing us a closer look at the company's financial health as it ramps up production of its all-important R2 electric vehicle - which is now, for "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1022555/gm-data-privacy-attorneys-general-lawsuit",
    "domain": "大厂 AI 动态",
    "title": "GM to pay $220 million to resolve claims it sold driving habits data",
    "url": "https://www.theverge.com/transportation/1022555/gm-data-privacy-attorneys-general-lawsuit",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T19:19:28+00:00",
    "summary": "General Motors has agreed to pay $220 million to settle claims that it illegally sold driver and location information to data brokers, as reported earlier by Reuters. The agreement, which resolves a c"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1022519/google-gemini-file-editing-documents-pdfs",
    "domain": "大厂 AI 动态",
    "title": "You can generate and edit Google Docs files directly in Gemini chats now",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1022519/google-gemini-file-editing-documents-pdfs",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T18:45:31+00:00",
    "summary": "Now you can generate, preview, and edit PDFs, Google Docs, Google Sheets, slide decks, Markdown files, TXT files, and code directly within Google Gemini. The new file editing capabilities are availabl"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1022440/ikea-varmblixt-smart-lamp-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Ikea&#8217;s colorful donut-shaped smart lamp is $20 off",
    "url": "https://www.theverge.com/gadgets/1022440/ikea-varmblixt-smart-lamp-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T18:18:36+00:00",
    "summary": "With its playful design, versatility, and relatively affordable price, the Ikea Varmblixt quickly became one of my colleague Jennifer Pattison Tuohy’s new favorite smart light products when she tested"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/waymos-next-robotaxi-will-be-a-toyota-bz4x-destined-for-japan-and-the-uk/",
    "domain": "大厂 AI 动态",
    "title": "Waymo taps Toyota to supply robotaxis for Japan and the U.K.",
    "url": "https://techcrunch.com/2026/10/30/waymos-next-robotaxi-will-be-a-toyota-bz4x-destined-for-japan-and-the-uk/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T07:01:00+00:00",
    "summary": "Waymo will begin testing self-driving versions of Toyota's electric bZ4X vehicles in Japan next year as part of a broader partnership with the automaker."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/you-dont-need-to-believe-in-a-god-to-get-a-religious-exemption-from-using-ai-at-work/",
    "domain": "大厂 AI 动态",
    "title": "You don’t need to believe in a god to get a religious exemption from using AI at work",
    "url": "https://techcrunch.com/2026/10/29/you-dont-need-to-believe-in-a-god-to-get-a-religious-exemption-from-using-ai-at-work/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T01:20:48+00:00",
    "summary": "David Durman, a University of Kentucky administrator, recently earned a religious exemption from using AI in the workplace."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/andy-jassy-says-prime-video-is-on-track-to-earn-tens-of-billions-of-dollars/",
    "domain": "大厂 AI 动态",
    "title": "Andy Jassy says Prime Video is on track to earn ‘tens of billions of dollars’",
    "url": "https://techcrunch.com/2026/10/29/andy-jassy-says-prime-video-is-on-track-to-earn-tens-of-billions-of-dollars/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T23:44:56+00:00",
    "summary": "The success of blockbuster hits like \"Project Hail Mary\" and \"Verity\" is only part of the story, Amazon's CEO says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/aws-will-be-a-1t-business-jassy-says-but-first-it-will-spend-big/",
    "domain": "大厂 AI 动态",
    "title": "AWS will be a $1T business, Jassy says — but first, it will spend big",
    "url": "https://techcrunch.com/2026/10/29/aws-will-be-a-1t-business-jassy-says-but-first-it-will-spend-big/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T23:42:22+00:00",
    "summary": "Amazon wants to be the king of AI cloud computing and become the first $1 trillion revenue business. But to do that it will have to continue on its capex spending spree, its CEO said Thursday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/binance-pauses-withdrawals-as-hackers-suspected-of-stealing-billions-in-crypto/",
    "domain": "大厂 AI 动态",
    "title": "Binance pauses withdrawals as hackers suspected of stealing billions in crypto",
    "url": "https://techcrunch.com/2026/10/29/binance-pauses-withdrawals-as-hackers-suspected-of-stealing-billions-in-crypto/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T22:27:23+00:00",
    "summary": "Some estimates say hackers stole billions in crypto from Binance, the world's largest cryptocurrency exchange, during a cyberattack on Thursday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/elon-musk-is-truly-a-genius-says-vladimir-putin/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk is ‘truly a genius,’ says Vladimir Putin",
    "url": "https://techcrunch.com/2026/10/29/elon-musk-is-truly-a-genius-says-vladimir-putin/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T21:51:29+00:00",
    "summary": "Putin said that he and Musk are in \"close contact\" about Rassvet, Russia's Starlink-like satellite connectivity project."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/amazon-reported-booming-cloud-revenue-but-otherwise-missed-expectations/",
    "domain": "大厂 AI 动态",
    "title": "Amazon reported booming cloud revenue but otherwise missed expectations",
    "url": "https://techcrunch.com/2026/10/29/amazon-reported-booming-cloud-revenue-but-otherwise-missed-expectations/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T21:20:47+00:00",
    "summary": "The biggest ouch of the report was its negative free cash flow of $2.4 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/gm-reaches-220m-settlement-over-selling-drivers-private-data/",
    "domain": "大厂 AI 动态",
    "title": "GM reaches $220M settlement over selling drivers’ private data",
    "url": "https://techcrunch.com/2026/10/29/gm-reaches-220m-settlement-over-selling-drivers-private-data/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T21:01:04+00:00",
    "summary": "As part of the settlement, GM must get drivers’ express consent before it collects or shares their driving and location data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/fan-fiction-site-archive-of-our-own-could-be-offline-for-up-to-4-weeks/",
    "domain": "大厂 AI 动态",
    "title": "Fan-fiction site Archive of Our Own (AO3) could be offline for up to 4 weeks after security incident",
    "url": "https://techcrunch.com/2026/10/29/fan-fiction-site-archive-of-our-own-could-be-offline-for-up-to-4-weeks/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:43:56+00:00",
    "summary": "The site has such a passionate user base that, within two hours of the announcement, its status page's posts had garnered millions of views (and much panicked commentary) across social media."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/as-search-traffic-dries-up-reddit-announces-its-shifting-to-a-logged-in-experience/",
    "domain": "大厂 AI 动态",
    "title": "As search traffic dries up, Reddit announces it’s shifting to a logged-in experience",
    "url": "https://techcrunch.com/2026/10/29/as-search-traffic-dries-up-reddit-announces-its-shifting-to-a-logged-in-experience/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:08:31+00:00",
    "summary": "As AI transforms how people find information online, Reddit is rethinking its open-web roots to protect its audience and business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/rivian-expands-joint-venture-with-vw-to-include-ai-assistant/",
    "domain": "大厂 AI 动态",
    "title": "Rivian expands joint venture with VW to include AI assistant",
    "url": "https://techcrunch.com/2026/10/29/rivian-expands-joint-venture-with-vw-to-include-ai-assistant/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:05:47+00:00",
    "summary": "Rivian doesn't disclose if the value of its $5.8 billion joint venture will expand as a result."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/the-r2-suv-is-already-rivians-best-selling-vehicle/",
    "domain": "大厂 AI 动态",
    "title": "The R2 SUV is already Rivian’s best-selling vehicle",
    "url": "https://techcrunch.com/2026/10/29/the-r2-suv-is-already-rivians-best-selling-vehicle/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:02:03+00:00",
    "summary": "Rivian is seeing strong enough sales of the new EV that it improved its guidance to Wall Street for the second time this year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/openai-backed-thrive-holdings-acquires-adt/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI-backed Thrive Holdings acquires ADT",
    "url": "https://techcrunch.com/2026/10/29/openai-backed-thrive-holdings-acquires-adt/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T19:56:19+00:00",
    "summary": "OpenAI-backed Thrive Holdings is buying ADT in a $15.3 billion deal, with plans to bring AI to the home security business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/where-was-my-invite-to-the-wait-what-airbnb-had-a-gala/",
    "domain": "大厂 AI 动态",
    "title": "Where was my invite to the — wait, what? Airbnb had a gala?",
    "url": "https://techcrunch.com/2026/10/29/where-was-my-invite-to-the-wait-what-airbnb-had-a-gala/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T19:17:49+00:00",
    "summary": "Airbnb’s nonprofit held its inaugural gala on Wednesday in Los Angeles, and the internet had one reaction — the *what* gala?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/meta-quietly-launches-an-ai-fashion-app-called-style-sketch/",
    "domain": "大厂 AI 动态",
    "title": "Meta quietly launches an AI fashion app called Style Sketch",
    "url": "https://techcrunch.com/2026/10/29/meta-quietly-launches-an-ai-fashion-app-called-style-sketch/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T19:14:36+00:00",
    "summary": "The app connects to Instagram to build a virtual closet from photos you’ve already shared, or lets you add items manually by snapping a photo, recording a quick video, or uploading images from your ca"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/granola-crunches-up-a-dictation-feature-to-compete-with-wispr/",
    "domain": "大厂 AI 动态",
    "title": "Granola crunches up a dictation feature to compete with Wispr",
    "url": "https://techcrunch.com/2026/10/29/granola-crunches-up-a-dictation-feature-to-compete-with-wispr/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T17:54:38+00:00",
    "summary": "Uno reverse! After Wispr added meeting notes to its dictation app, Granola is adding dictation to its meeting notetaker. The voice AI wars are getting interesting."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/",
    "domain": "大厂 AI 动态",
    "title": "Mistral releases weights for its trillion-parameter AI model, targeting cybersecurity",
    "url": "https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T17:00:00+00:00",
    "summary": "Mistral says its new model can afford organizations a kind of control over its cyber defenses that closed models can't."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/u-s-investigated-chinese-spy-plot-aimed-at-nvidia-ceo/",
    "domain": "大厂 AI 动态",
    "title": "US investigated Chinese spy plot aimed at Nvidia CEO",
    "url": "https://techcrunch.com/2026/10/29/u-s-investigated-chinese-spy-plot-aimed-at-nvidia-ceo/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:42:32+00:00",
    "summary": "A top executive of a Singapore AI cloud company that was accused of illegally selling Nvidia chips to China could also have been a Chinese spy, sources have told the New York Times."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/ex-palantir-execs-launch-dream-with-17m-from-a16z-to-build-ai-world-models-for-construction/",
    "domain": "大厂 AI 动态",
    "title": "Ex-Palantir execs launch Dream with $17M from a16z to build AI world models for construction",
    "url": "https://techcrunch.com/2026/10/29/ex-palantir-execs-launch-dream-with-17m-from-a16z-to-build-ai-world-models-for-construction/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:21:00+00:00",
    "summary": "Dream is grounded in real physics and construction standards. Just as LLMs learn from text, Dream's world model is trained on more than 100 million square feet of building data gathered from permit ar"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/29/superme-raises-20m-for-its-network-of-ai-expert-profiles/",
    "domain": "大厂 AI 动态",
    "title": "SuperMe raises $20M for its network of AI expert profiles",
    "url": "https://techcrunch.com/2026/10/29/superme-raises-20m-for-its-network-of-ai-expert-profiles/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:19:43+00:00",
    "summary": "SuperMe is a network of AI profiles built from the knowledge of real-life experts. When you ask a question, the platform determines which experts are best suited to answer and creates a group chat wit"
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-palantir-cto-shyam-sankar-about-the-ai-religious-war/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Palantir CTO Shyam Sankar About the AI Religious War",
    "url": "https://stratechery.com/2026/an-interview-with-palantir-cto-shyam-sankar-about-the-ai-religious-war/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T10:00:00+00:00",
    "summary": "An interview with Palantir CTO Shyam Sankar about AI diffusion and safety, forward-deployed engineer, and what the battle in tech is actually about."
  },
  {
    "id": "rss:https://stratechery.com/2026/meta-earnings-muse-and-the-frontier-musebook/",
    "domain": "大厂 AI 动态",
    "title": "Meta Earnings, Muse and the Frontier, Musebook",
    "url": "https://stratechery.com/2026/meta-earnings-muse-and-the-frontier-musebook/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T10:06:13+00:00",
    "summary": "Meta's earnings come in the context of Zuckerberg delivering on his promise; if investors believe in Muse they must support Meta's spending on compute."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/reddit-will-require-you-to-log-in-eventually-ceo-confirms/",
    "domain": "大厂 AI 动态",
    "title": "Reddit is moving to “a logged-in-only experience,” CEO says",
    "url": "https://arstechnica.com/gadgets/2026/10/reddit-will-require-you-to-log-in-eventually-ceo-confirms/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T21:47:57+00:00",
    "summary": "Reddit's search traffic \"was down meaningfully\" last quarter."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/windows-11-gets-right-click-menu-improvements-as-pc-revenue-slides/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft fixes a Windows 11 annoyance as PC revenue declines",
    "url": "https://arstechnica.com/gadgets/2026/10/windows-11-gets-right-click-menu-improvements-as-pc-revenue-slides/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:18:49+00:00",
    "summary": "The latest update also brings a cloud recovery option for PCs that won't boot."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/pentagon-ig-refuses-to-investigate-starlink-starshield-slowdown-in-ukraine/",
    "domain": "大厂 AI 动态",
    "title": "Pentagon IG refuses to investigate Starlink/Starshield slowdown in Ukraine",
    "url": "https://arstechnica.com/tech-policy/2026/10/pentagon-ig-refuses-to-investigate-starlink-starshield-slowdown-in-ukraine/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:08:10+00:00",
    "summary": "Inspector general rejected request from Democratic and Republican senators."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/trump-declares-robot-imports-a-national-security-threat/",
    "domain": "大厂 AI 动态",
    "title": "Trump declares robot imports a national security threat",
    "url": "https://arstechnica.com/gadgets/2026/10/trump-declares-robot-imports-a-national-security-threat/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T19:07:53+00:00",
    "summary": "President orders trade talks on foreign-made factory robots, threatens tariffs."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/report-trump-did-nothing-with-intel-that-china-planted-spy-close-to-nvidia-ceo/",
    "domain": "大厂 AI 动态",
    "title": "Trump ignored intel on China’s Nvidia spy to protect company’s stock, report says",
    "url": "https://arstechnica.com/tech-policy/2026/10/report-trump-did-nothing-with-intel-that-china-planted-spy-close-to-nvidia-ceo/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T18:29:12+00:00",
    "summary": "Spy accused of exploiting Trump ties to Huang, funneling secrets to China."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/turning-a-solar-power-system-into-its-own-backup/",
    "domain": "大厂 AI 动态",
    "title": "Turning a solar power system into its own backup",
    "url": "https://arstechnica.com/science/2026/10/turning-a-solar-power-system-into-its-own-backup/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T18:02:26+00:00",
    "summary": "Plant design allows it to run on either stored solar heat or combustion."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/trump-admin-sues-utah-to-save-kalshi-from-the-states-total-ban-on-gambling/",
    "domain": "大厂 AI 动态",
    "title": "Kalshi and its co-founders face felony charges for violating Utah gambling laws",
    "url": "https://arstechnica.com/tech-policy/2026/10/trump-admin-sues-utah-to-save-kalshi-from-the-states-total-ban-on-gambling/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T17:21:33+00:00",
    "summary": "Charges filed as Trump admin tries to save Kalshi from Utah's total ban on gambling."
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
    "id": "hn:50280197",
    "domain": "股票",
    "title": "Alphabet Announces Third Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q3/2026q3-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-10-28T20:11:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50232604",
    "domain": "股票",
    "title": "Microsoft and others tell crypto platform not to tokenize their stocks",
    "url": "https://gizmodo.com/microsoft-mcdonalds-verizon-and-others-tell-crypto-platform-not-to-tokenize-their-stocks-2000830368",
    "source": "gumby",
    "platform": "hackernews",
    "points": 100,
    "published_at": "2026-10-25T15:28:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50162431",
    "domain": "股票",
    "title": "The Secret Life of Circuits is now in stock everywhere",
    "url": "https://blog.coredump.cx/p/the-secret-life-of-circuits-is-now",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-10-20T07:15:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50297025",
    "domain": "股票",
    "title": "Intel stock plunges after posting disappointing Q4 outlook",
    "url": "https://finance.yahoo.com/video/intel-stock-plunges-after-posting-disappointing-q4-outlook-200731652.html",
    "source": "baal80spam",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-29T22:21:29+00:00",
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
    "id": "hn:50265525",
    "domain": "股票",
    "title": "In China, the AI bubble has burst",
    "url": "https://finance.yahoo.com/markets/stocks/articles/analysis-china-ai-bubble-already-120038616.html",
    "source": "smurda",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-27T20:44:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:50254255",
    "domain": "股票",
    "title": "Pentagon orders bases to plan for 90 days without the grid",
    "url": "https://fortune.com/2026/10/26/pentagon-fortress-bases-90-days-off-grid-uk-be-ready-stockpile/",
    "source": "russfink",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-27T03:02:29+00:00",
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
    "id": "hn:50193524",
    "domain": "股票",
    "title": "Chinese stocks turn biggest losers as global AI trade stumbles",
    "url": "https://theedgemalaysia.com/node/822195",
    "source": "miohtama",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-22T10:32:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50210325",
    "domain": "股票",
    "title": "Built a site that teaches investing using the live market as the examples",
    "url": "https://www.stocksightfinance.com",
    "source": "kshitik",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-23T15:07:06+00:00",
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
    "id": "hn:50159963",
    "domain": "股票",
    "title": "Investors temper Anthropic IPO valuation expectations over growth slowdown",
    "url": "https://www.reuters.com/business/finance/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-2026-10-15/",
    "source": "xqcgrek2",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-20T00:49:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122366",
    "domain": "股票",
    "title": "Anthropic's Valuation Collapsed by $500B",
    "url": "https://www.telegraph.co.uk/business/2026/10/16/anthropic-valuation-ipo-ai-stock-listing/",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T18:27:58+00:00",
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
    "id": "hn:50046896",
    "domain": "股票",
    "title": "Nvidia-backed data centre firm Firmus scraps IPO as AI valuation concerns deepen",
    "url": "https://www.bbc.com/news/articles/ck9dzpw4ll8po",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-11T19:26:05+00:00",
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
    "id": "hn:50260526",
    "domain": "金融",
    "title": "A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies",
    "url": "https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 177,
    "published_at": "2026-10-27T15:09:27+00:00",
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
    "id": "hn:50274706",
    "domain": "金融",
    "title": "Tesla Semi catches fire on I-880",
    "url": "https://electrek.co/2026/10/28/tesla-semi-fire-i-880-hayward-no-crash/",
    "source": "metadat",
    "platform": "hackernews",
    "points": 95,
    "published_at": "2026-10-28T14:54:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50278678",
    "domain": "金融",
    "title": "Show HN: A proof-of-concept formalization of the IRS federal tax forms",
    "url": "https://github.com/emmilco/us-tax-model",
    "source": "RGS1811",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-10-28T18:30:53+00:00",
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
    "id": "hn:50291902",
    "domain": "金融",
    "title": "Alphabet heads for a $500B drop in market value, biggest in its history",
    "url": "https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-29T16:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50141295",
    "domain": "金融",
    "title": "Tesla 'Cannot Guarantee' Roadster Reservation Holders Will Ever Get a Car",
    "url": "https://www.thedrive.com/news/tesla-cannot-guarantee-roadster-reservation-holders-will-ever-get-a-car",
    "source": "healsdata",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-10-18T14:16:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50239430",
    "domain": "金融",
    "title": "Tesla cancels Cybertruck in Australia and NZ after 7 years of deposits",
    "url": "https://electrek.co/2026/10/23/tesla-cancels-cybertruck-australia-new-zealand/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-10-26T05:13:15+00:00",
    "summary": ""
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
    "id": "hn:50189801",
    "domain": "金融",
    "title": "Tesla profits drop 43% in Q3",
    "url": "https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/",
    "source": "throw0101a",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-10-22T01:02:23+00:00",
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
    "id": "hn:50118624",
    "domain": "金融",
    "title": "Tesla unveils 'flying' Roadster with SpaceX thrusters [video]",
    "url": "https://www.youtube.com/watch?v=eqOfmtTJD1A",
    "source": "skadamat",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-10-16T14:12:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50194602",
    "domain": "金融",
    "title": "Full Disk Encryption on Fedora with TPM2",
    "url": "https://www.apalrd.net/posts/2026/ent_luks/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-10-22T12:46:40+00:00",
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
    "id": "hn:50122776",
    "domain": "金融",
    "title": "Show HN: Stoke Money – Personal finance app built around a cash flow forecast",
    "url": "https://stoke.money",
    "source": "_wesley",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-16T18:54:47+00:00",
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
