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

- 今日日期：`2026-11-03`
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
  "date": "2026-11-03",
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
    "points": 2073626,
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
    "points": 1464621,
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
    "points": 1425733,
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
    "points": 1410974,
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
    "points": 1158997,
    "published_at": "2026-10-13T00:57:21+00:00",
    "summary": "这次，我把【Re：从零开始的 AI 学习】第一季全 13 期完整连在一起啦！\n新来的朋友或者想要查漏补缺的伙伴，现在可以一口气通关！从 AI 入门与提示词技巧，到 Agent 玩法、主流模型对比与使用成本……跟着走一遍就能彻底搞懂。\n希望这个系列能给你带来哪怕一点点启发，欢迎点赞、投币、收藏一键三连支持！也超级欢迎转发安利给身边的朋友～\n\n【目录】\n00:00 导语\n00:32 AI 这三年发生了"
  },
  {
    "id": "bvid:BV1REx46NEc4",
    "domain": "AI",
    "title": "【全网最全】DeepSeek Harness超详细教程！50分钟吃透DSH，让SuperAgent给你干活！",
    "url": "http://www.bilibili.com/video/av117540671982699",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 1093083,
    "published_at": "2026-11-01T10:22:02+00:00",
    "summary": "DeepSeek Harness超详细教程！\n大家可以速速收藏啦~\n耗时60天制作！感谢大家的三联\n未来还会出其他AI教程，大家可以关注一下~"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 888578,
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
    "points": 740672,
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
    "points": 645655,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 595333,
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
    "points": 426885,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 366760,
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
    "points": 344762,
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
    "points": 320015,
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
    "points": 292352,
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
    "points": 224097,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 188929,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 185637,
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
    "points": 164544,
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
    "points": 161900,
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
    "points": 151744,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 141746,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 99375,
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
    "points": 95042,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94221,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 75036,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74631,
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
    "points": 64100,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1oQYL64EJV",
    "domain": "AI",
    "title": "【SRC漏洞挖掘】2026最适合新手的AI+自动化挖漏洞教程，从环境搭建到漏洞验证，手把手带你挖到第一个SRC漏洞！",
    "url": "http://www.bilibili.com/video/av117251248490748",
    "source": "阿盾聊安全",
    "platform": "bilibili",
    "points": 62853,
    "published_at": "2026-09-11T07:39:16+00:00",
    "summary": "这套 18 节教程带你从零跑通 AI 自动化挖漏洞全流程：环境搭建、Hermes部署、Burp/Nuclei 集成、资产侦察、漏洞发现到报告验证，一套打通。\n适合有 Web 安全基础、想从手动挖洞升级到自动化的同学。\n资料和工具包见评论区，三连不迷路。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56668,
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
    "points": 52805,
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
    "points": 50047,
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
    "points": 49451,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47791,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 42987,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 42247,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1hEVY6jEGT",
    "domain": "AI",
    "title": "最新【Claude pro Max】保姆级充值教程 Claude code国内购买教程 注册+订阅一个视频教会你",
    "url": "http://www.bilibili.com/video/av116657754277772",
    "source": "codex充值",
    "platform": "bilibili",
    "points": 41449,
    "published_at": "2026-05-29T12:07:14+00:00",
    "summary": "aipayok.com"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41152,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 39188,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34631,
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
    "points": 31143,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 31011,
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
    "points": 29923,
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
    "points": 29033,
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
    "points": 26096,
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
    "points": 25373,
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
    "points": 22844,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 18567,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 16774,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 15641,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
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
    "points": 359,
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
    "points": 351,
    "published_at": "2026-10-24T09:58:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50327058",
    "domain": "AI 算力 / 半导体",
    "title": "Seoul Viosys begins production of rare-earth-free white light emitter",
    "url": "https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml",
    "source": "gmays",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-11-01T16:23:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236073",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-25T21:07:38+00:00",
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
    "id": "hn:50348962",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia – open-source auto-ontology",
    "url": "https://github.com/NVIDIA/auto-ontology",
    "source": "campervans",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-11-03T07:04:50+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/marvell-snaps-photonics-chipmaker-lumentum-to-bolster-ai-connectivity/",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell Snaps Photonics Chipmaker Lumentum to Bolster AI Connectivity",
    "url": "https://www.eetimes.com/marvell-snaps-photonics-chipmaker-lumentum-to-bolster-ai-connectivity/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T08:50:21+00:00",
    "summary": "The $115 billion deal aims to create a category leader in AI connectivity by co-designing network processors and lasers for optical transceivers. The post Marvell Snaps Photonics Chipmaker Lumentum to"
  },
  {
    "id": "rss:https://www.eetimes.com/macronix-builds-hardware-security-into-nor-flash-ahead-of-eu-cyber-resilience-act/",
    "domain": "AI 算力 / 半导体",
    "title": "Macronix Builds Hardware Security into NOR Flash Ahead of EU Cyber Resilience Act",
    "url": "https://www.eetimes.com/macronix-builds-hardware-security-into-nor-flash-ahead-of-eu-cyber-resilience-act/",
    "source": "EE Times Taiwan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T05:30:00+00:00",
    "summary": "The European Union's Cyber Resilience Act (CRA), which becomes mandatory in December 2027, is raising the bar for cybersecurity in connected devices. Rather than relying on software patches to address"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-automotive-dms-oms-technology-challenges-power-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Automotive DMS & OMS: Technology, Challenges & Power Solutions",
    "url": "https://www.eetimes.com/inside-automotive-dms-oms-technology-challenges-power-solutions/",
    "source": "Monotlithic Power Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:33:59+00:00",
    "summary": "Join our expert for an in-depth look inside today's DMS and OMS architectures. You'll gain practical insights into camera design, power delivery, and thermal management strategies, while learning how "
  },
  {
    "id": "rss:https://www.eetimes.com/canadas-quantum-sector-sets-sights-on-commercialization/",
    "domain": "AI 算力 / 半导体",
    "title": "Canada’s Quantum Sector Sets Sights on Commercialization",
    "url": "https://www.eetimes.com/canadas-quantum-sector-sets-sights-on-commercialization/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:58:45+00:00",
    "summary": "Defense procurement, patient capital, and shared infrastructure will help Canadian quantum firms scale at home. The post Canada’s Quantum Sector Sets Sights on Commercialization appeared first on EE T"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-to-the-edge-generative-intelligence-for-robotics-and-autonomous-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "AI to the Edge: Generative Intelligence for Robotics and Autonomous Systems",
    "url": "https://www.eetimes.com/ai-to-the-edge-generative-intelligence-for-robotics-and-autonomous-systems/",
    "source": "MediaTek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:29:50+00:00",
    "summary": "Designed for embedded engineers, robotics developers, AI practitioners, and technical leaders, this webinar explores how generative intelligence is helping shape the future of physical AI. The post AI"
  },
  {
    "id": "rss:https://www.eetimes.com/sir-arthur-c-clarke-deserves-a-nobel-prize/",
    "domain": "AI 算力 / 半导体",
    "title": "Sir Arthur C. Clarke Deserves a Nobel Prize",
    "url": "https://www.eetimes.com/sir-arthur-c-clarke-deserves-a-nobel-prize/",
    "source": "Silicon Catalyst LLC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:57:43+00:00",
    "summary": "Ever since the Silicon Catalyst 2023 Semiconductor Industry Forum (“Welcome to our AI Wonderland”), I’ve been convinced that the Nobel Prize committee needs to consider a posthumous award for Sir Arth"
  },
  {
    "id": "rss:https://www.eetimes.com/biwin-to-show-storage-solutions-for-ai-and-the-edge-at-electronica-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "BIWIN to Show Storage Solutions for AI and the Edge at electronica 2026",
    "url": "https://www.eetimes.com/biwin-to-show-storage-solutions-for-ai-and-the-edge-at-electronica-2026/",
    "source": "BIWIN STORAGE TECHNOLOGY CO., LTD.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:00:00+00:00",
    "summary": "Gear up for the AI era. From 122.88 TB enterprise SSDs to integrated embedded memory and Mini SSDs, BIWIN will showcase storage solutions built specifically for a new generation of electronic systems."
  },
  {
    "id": "rss:https://www.eetimes.com/the-power-of-dual-phase-drmos-technology-in-ai-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "The Power of Dual-Phase DrMOS Technology in AI Systems",
    "url": "https://www.eetimes.com/the-power-of-dual-phase-drmos-technology-in-ai-systems/",
    "source": "Monolithic Power Systems, Inc. (MPS)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:00:00+00:00",
    "summary": "Learn how MPS dual-phase DrMOS solution address power density, efficiency, and thermal management challenges in compact AI power systems. The post The Power of Dual-Phase DrMOS Technology in AI System"
  },
  {
    "id": "rss:https://www.eetimes.com/andes-waits-for-market-momentum-for-cuzco-cpu/",
    "domain": "AI 算力 / 半导体",
    "title": "Andes Waits For Market Momentum For Cuzco CPU",
    "url": "https://www.eetimes.com/andes-waits-for-market-momentum-for-cuzco-cpu/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T12:00:00+00:00",
    "summary": "Andes CTO Charlie Su said the company put its high-end RISC-V CPU on the back burner for commercial reasons. The post Andes Waits For Market Momentum For Cuzco CPU appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/jevon-paradox-and-the-silicon-roadmap/",
    "domain": "AI 算力 / 半导体",
    "title": "Jevons’ Paradox and the Silicon Roadmap",
    "url": "https://www.eetimes.com/jevon-paradox-and-the-silicon-roadmap/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T08:58:48+00:00",
    "summary": "Jevons’ paradox may fuel AI demand, but the silicon roadmap could determine which chips retain their value and which become stranded assets. The post Jevons’ Paradox and the Silicon Roadmap appeared f"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-considers-rebranding-data-centers-to-ai-compute-campuses-as-data-center-backlash-intensifies-company-reportedly-sees-2028-presidential-election-becoming-an-ai-issue",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI considers rebranding data centers to 'AI compute campuses\" as data center backlash intensifies",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-considers-rebranding-data-centers-to-ai-compute-campuses-as-data-center-backlash-intensifies-company-reportedly-sees-2028-presidential-election-becoming-an-ai-issue",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:15:31+00:00",
    "summary": "OpenAI expects AI to become a major issue in the 2028 presidential election and is preparing a policy and public relations push after the U.S. midterm elections. The company is also promoting the term"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/tachyum-developer-of-heavily-delayed-universal-prodigy-processor-voluntarily-files-for-bankruptcy-future-of-prodigy-ip-unknown-as-company-begins-bankruptcy-proceedings",
    "domain": "AI 算力 / 半导体",
    "title": "Tachyum, developer of heavily-delayed universal Prodigy processor, voluntarily files for bankruptcy",
    "url": "https://www.tomshardware.com/pc-components/cpus/tachyum-developer-of-heavily-delayed-universal-prodigy-processor-voluntarily-files-for-bankruptcy-future-of-prodigy-ip-unknown-as-company-begins-bankruptcy-proceedings",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:07:21+00:00",
    "summary": "Tachyum files for bankruptcy, the court in Bratislava initiates bankruptcy proceedings."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/putin-demands-russian-data-centers-supply-capacity-to-the-state-in-wake-of-ukraine-drone-attacks-10-percent-capacity-must-be-available-for-state-it-infrastructure-with-24-hours-notice",
    "domain": "AI 算力 / 半导体",
    "title": "Putin demands Russian data centers supply capacity to the state in wake of Ukraine drone attacks",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/putin-demands-russian-data-centers-supply-capacity-to-the-state-in-wake-of-ukraine-drone-attacks-10-percent-capacity-must-be-available-for-state-it-infrastructure-with-24-hours-notice",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:00:32+00:00",
    "summary": "President Putin has told non-state Russian data centers that they must set aside 10% of their total capacity for use by the country's own IT infrastructure."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/creality-k3-review",
    "domain": "AI 算力 / 半导体",
    "title": "Creality K3 Review: It’s a Tool Changer, not a game changer",
    "url": "https://www.tomshardware.com/3d-printing/creality-k3-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T16:40:58+00:00",
    "summary": "Creality’s four-color tool changer is a good one, but is it too late?"
  },
  {
    "id": "rss:https://www.tomshardware.com/raspberry-pi/16gb-raspberry-pi-5-hiked-to-usd385-more-than-triple-its-launch-price-makers-are-already-shifting-to-pico-esp32-for-small-projects-mini-pcs-for-more-ambitious-tasks",
    "domain": "AI 算力 / 半导体",
    "title": "16GB Raspberry Pi 5 hiked to $385, more than triple its launch price",
    "url": "https://www.tomshardware.com/raspberry-pi/16gb-raspberry-pi-5-hiked-to-usd385-more-than-triple-its-launch-price-makers-are-already-shifting-to-pico-esp32-for-small-projects-mini-pcs-for-more-ambitious-tasks",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T16:17:35+00:00",
    "summary": "The Raspberry Pi 16GB has gone up in price by $80 to $385. It now costs more than triple its January 2025 launch price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/america-hates-data-centers-new-database-reveals-more-than-90-percent-of-10-000-public-comments-are-negative-only-21-percent-mention-ai-73-percent-of-meetings-had-no-data-center-supporters-water-is-the-number-one-concern",
    "domain": "AI 算力 / 半导体",
    "title": "'America hates data centers' — New data highlights public sentiment",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/america-hates-data-centers-new-database-reveals-more-than-90-percent-of-10-000-public-comments-are-negative-only-21-percent-mention-ai-73-percent-of-meetings-had-no-data-center-supporters-water-is-the-number-one-concern",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T15:19:12+00:00",
    "summary": "A new website seeks to distill over 10,000 public comments about data centers in the community across more than 410 local governments, and the consensus is that people don't like them one bit."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/gamers-asus-tuf-monitor-blocks-bullet-fired-through-wall-during-call-of-duty-session-says-280hz-monitor-is-the-best-usd280-i-ever-spent",
    "domain": "AI 算力 / 半导体",
    "title": "Gamer's Asus TUF monitor blocks bullet fired through wall during Call of Duty session",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/gamers-asus-tuf-monitor-blocks-bullet-fired-through-wall-during-call-of-duty-session-says-280hz-monitor-is-the-best-usd280-i-ever-spent",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:34:50+00:00",
    "summary": "A Redditor was playing Call of Duty when they heard gunfire outside their home. After hitting the deck, they discovered that their monitor had potentially saved their life."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/apple-finally-has-a-touchscreen-macbook-why-now",
    "domain": "AI 算力 / 半导体",
    "title": "Apple finally has a touchscreen MacBook. Why now?",
    "url": "https://www.tomshardware.com/laptops/macbooks/apple-finally-has-a-touchscreen-macbook-why-now",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:00:00+00:00",
    "summary": "Apple is introducing a touchscreen laptop in the MacBook Pro with a PROLED XDR Display. Here's where it falls in the long timeline of touchscreen laptops."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/nvidia-brev-security-breach-may-have-exposed-ssh-keys-used-to-access-customer-vms-investigation-finds-unauthorized-activity-spanning-16-days-but-no-evidence-of-misuse",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Brev security breach may have exposed SSH keys used to access customer VMs",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/nvidia-brev-security-breach-may-have-exposed-ssh-keys-used-to-access-customer-vms-investigation-finds-unauthorized-activity-spanning-16-days-but-no-evidence-of-misuse",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:00:00+00:00",
    "summary": "Nvidia is investigating a security incident involving its Brev cloud development platform after detecting unauthorized activity between October 4 and October 20. The incident may have exposed SSH keys"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-engineer-successfully-compiles-a-32-bit-risc-v-cpu-in-qwen-3-5-4b-llm-inserted-directly-into-its-weights-built-in-cpu-can-run-processor-arithmetic-operations-code-and-of-course-doom",
    "domain": "AI 算力 / 半导体",
    "title": "AI model gets a 32-bit RISC-V CPU compiled directly into its weights, then runs DOOM on it",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-engineer-successfully-compiles-a-32-bit-risc-v-cpu-in-qwen-3-5-4b-llm-inserted-directly-into-its-weights-built-in-cpu-can-run-processor-arithmetic-operations-code-and-of-course-doom",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T13:30:00+00:00",
    "summary": "Qwenputer is an experimental blend of the stock Qwen 3.5 4B LLM with a 32-bit RISC-V CPU compiled and inserted directly into its weights."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/google-data-center-wins-approval-in-minnesota-after-protests-delay-council-vote-twice-200-acre-project-moves-forward-despite-opposition-from-local-residents-tech-giant-scales-down-project-and-drops-usd80-million-tax-break-request",
    "domain": "AI 算力 / 半导体",
    "title": "Google data center wins approval in Minnesota after protests delay council vote twice",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/google-data-center-wins-approval-in-minnesota-after-protests-delay-council-vote-twice-200-acre-project-moves-forward-despite-opposition-from-local-residents-tech-giant-scales-down-project-and-drops-usd80-million-tax-break-request",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T13:00:00+00:00",
    "summary": "Google’s proposed Hermantown data center has cleared a major approval hurdle after the city council unanimously backed the project on October 30."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/triple-your-nintendo-switch-2s-storage-for-just-usd99-save-usd50-on-this-ultra-fast-512gb-samsung-p9-microsd-card-for-a-limited-time-only",
    "domain": "AI 算力 / 半导体",
    "title": "Triple your Nintendo Switch 2's storage for just $99",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/triple-your-nintendo-switch-2s-storage-for-just-usd99-save-usd50-on-this-ultra-fast-512gb-samsung-p9-microsd-card-for-a-limited-time-only",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T12:54:57+00:00",
    "summary": "A 34% price cut at Amazon means you can get the Samsung P9 512GB microSD Express card for the Nintendo Switch 2 for just $99.99 right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hackers-claim-to-have-stolen-23tb-of-data-from-russian-statistics-body-including-ukraine-war-casualty-figures-russian-federal-state-statistics-service-admits-its-servers-were-hit-by-coordinated-cyberattacks",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers claim to have stolen 23TB of data from Russian statistics body, including Ukraine war casualty figures",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hackers-claim-to-have-stolen-23tb-of-data-from-russian-statistics-body-including-ukraine-war-casualty-figures-russian-federal-state-statistics-service-admits-its-servers-were-hit-by-coordinated-cyberattacks",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T12:41:54+00:00",
    "summary": "Russia's Rosstat admitted that its servers were attacked by hackers but denies data leaks which appear to show as many as 50,000 military deaths per month."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-confirms-new-claude-code-limits-to-prevent-game-cloning-users-report-opus-5-5-is-also-actively-blocking-reverse-engineering-tasks",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic confirms new Claude Code limits to prevent game cloning, users report blocking reverse engineering tasks",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-confirms-new-claude-code-limits-to-prevent-game-cloning-users-report-opus-5-5-is-also-actively-blocking-reverse-engineering-tasks",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T12:30:00+00:00",
    "summary": "Anthropic employee confirms that Claude Code now has orders not to reproduce game IP — company \"iterating to ensure [...] the right balance\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-mocks-openai-ceo-sam-altmans-claim-that-pcs-having-ram-is-terrible-the-people-deserve-to-have-their-ram-too",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk mocks OpenAI CEO Sam Altman's claim that PCs having RAM is terrible",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-mocks-openai-ceo-sam-altmans-claim-that-pcs-having-ram-is-terrible-the-people-deserve-to-have-their-ram-too",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T12:11:21+00:00",
    "summary": "SpaceX CEO Musk posted a meme to X mocking Altman's belief that it's \""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/spacex-loses-bid-to-dismiss-lawsuit-over-xai-data-center-pollution-judge-rules-mississippi-gas-turbines-are-not-exempt-from-the-clean-air-act",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX loses bid to dismiss lawsuit over xAI data center pollution",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/spacex-loses-bid-to-dismiss-lawsuit-over-xai-data-center-pollution-judge-rules-mississippi-gas-turbines-are-not-exempt-from-the-clean-air-act",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T12:00:00+00:00",
    "summary": "SpaceX loses latest legal fight over xAI's gas-powered data centers in Mississippi — court rejects arguments that mobile turbines are exempt from air permits"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-a-usd450-saving-on-this-4k-ready-gaming-pc-with-an-rtx-5070-ti-and-32gb-ddr5-right-now-abs-rig-from-newegg-ships-with-24-core-intel-cpu-and-a-2tb-ssd-for-usd2-549-99",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a $450 saving on this 4K-ready gaming PC with an RTX 5070 Ti and 32GB DDR5 right now",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-a-usd450-saving-on-this-4k-ready-gaming-pc-with-an-rtx-5070-ti-and-32gb-ddr5-right-now-abs-rig-from-newegg-ships-with-24-core-intel-cpu-and-a-2tb-ssd-for-usd2-549-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T11:52:11+00:00",
    "summary": "This ABS Stratos II Aqua gaming PC has dropped to $2,549.99 at Newegg right now, giving you a rig with a 24-core Intel Core i9-14900KF CPU, an Nvidia GeForce RTX 5070 Ti GPU, a 2TB SSD, and 32GB of DD"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/sonys-final-4k-blu-ray-player-listed-as-out-of-stock-in-japan-firm-may-be-preparing-to-abandon-standalone-players-retailers-reportedly-told-not-to-expect-new-stock-of-its-remaining-model",
    "domain": "AI 算力 / 半导体",
    "title": "Sony's final 4K Blu-ray player listed as out of stock in Japan, firm may be preparing to abandon standalone players",
    "url": "https://www.tomshardware.com/video-games/playstation/sonys-final-4k-blu-ray-player-listed-as-out-of-stock-in-japan-firm-may-be-preparing-to-abandon-standalone-players-retailers-reportedly-told-not-to-expect-new-stock-of-its-remaining-model",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T11:30:00+00:00",
    "summary": "Sony may be preparing to abandon the standalone 4K Blu-ray player market after retailers in Japan reportedly stopped expecting new shipments of its final remaining model, the UBP-X700K. The company ha"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/military-explores-commercial-5g-networks-for-enemy-drone-defense-ai-agents-developed-the-system-recently-used-in-battlefield-trials-in-latvia",
    "domain": "AI 算力 / 半导体",
    "title": "Military explores commercial 5G networks for enemy drone defense",
    "url": "https://www.tomshardware.com/networking/military-explores-commercial-5g-networks-for-enemy-drone-defense-ai-agents-developed-the-system-recently-used-in-battlefield-trials-in-latvia",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T11:00:00+00:00",
    "summary": "The military is looking at leveraging commercial 5G networks to sense and track drone incursions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/supermarket-freezers-across-europe-struck-in-second-crippling-cyberattack-hackers-raise-temperatures-to-50-degrees-celsius-in-belgium-and-sweden-destroying-food-stocks",
    "domain": "AI 算力 / 半导体",
    "title": "Supermarket freezers across Europe struck in second crippling cyberattack",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/supermarket-freezers-across-europe-struck-in-second-crippling-cyberattack-hackers-raise-temperatures-to-50-degrees-celsius-in-belgium-and-sweden-destroying-food-stocks",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T10:49:27+00:00",
    "summary": "A second cyberattack has struck supermarket freezers across Europe."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely",
    "domain": "AI 算力 / 半导体",
    "title": "New AI-driven Windows malware feeds stolen data to Claude to rank victims’ assets by value, then deletes itself",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T21:00:00+00:00",
    "summary": "Cisco Talos says the VOLTA infostealer sends stolen victim data to Claude Opus 4.6 to rank assets by monetization value."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/gog-explores-reviving-physical-pc-game-releases-digital-storefront-needs-publisher-approvals-has-to-figure-out-the-logistics-and-legal-challenges",
    "domain": "AI 算力 / 半导体",
    "title": "GOG explores reviving physical PC game releases",
    "url": "https://www.tomshardware.com/video-games/gog-explores-reviving-physical-pc-game-releases-digital-storefront-needs-publisher-approvals-has-to-figure-out-the-logistics-and-legal-challenges",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T18:45:00+00:00",
    "summary": "GOG wants to sell physical games, in contrast to consoles going digital-only, giving gamers more freedom over their games. However, it still has to figure out logistics and publisher permissions."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/snag-a-nintendo-switch-2-for-only-usd469-while-stock-lasts-usd30-off-a-system-thats-not-often-on-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Snag a Nintendo Switch 2 for only $469 while stock lasts — $30 off a system that's not often on sale",
    "url": "https://www.tomshardware.com/pc-components/snag-a-nintendo-switch-2-for-only-usd469-while-stock-lasts-usd30-off-a-system-thats-not-often-on-sale",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T18:09:28+00:00",
    "summary": "Snag a Nintendo Switch 2 for only $469 while stocks last — $30 off a system that's not often on sale"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/lucky-pc-buyer-gets-usd1-200-discount-on-9900x3d-gaming-pc-walmart-honors-usd1-099-shelf-price-on-usd2-299-unit",
    "domain": "AI 算力 / 半导体",
    "title": "Walmart honors massive shelf price mistake, lucky buyer gets two $2,299 CyberPowerPC gaming rigs for $1,099 each",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/lucky-pc-buyer-gets-usd1-200-discount-on-9900x3d-gaming-pc-walmart-honors-usd1-099-shelf-price-on-usd2-299-unit",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:53:45+00:00",
    "summary": "Redditor gets a gaming PC at more than 50% off in a physical Walmart retail store."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/brazilian-lawyers-busted-for-attempting-to-manipulate-courts-ai-with-prompt-injection-hidden-in-filing-courts-ai-flags-hidden-text-that-demanded-superficial-legal-scrutiny-lawyers-fined-usd16-000",
    "domain": "AI 算力 / 半导体",
    "title": "Brazilian lawyers busted for attempting to manipulate court's AI with prompt injection hidden in filing",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/brazilian-lawyers-busted-for-attempting-to-manipulate-courts-ai-with-prompt-injection-hidden-in-filing-courts-ai-flags-hidden-text-that-demanded-superficial-legal-scrutiny-lawyers-fined-usd16-000",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:05:00+00:00",
    "summary": "The lawyers of a plaintiff in a labor case attempted to use prompt injection to influence the court's AI but were caught. They won the case anyway, as the defendant did not respond, making the move to"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/biwin-m560-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Biwin M560 2TB SSD Review: The DRAM-less drive to beat",
    "url": "https://www.tomshardware.com/pc-components/ssds/biwin-m560-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:00:00+00:00",
    "summary": "The Biwin M560 brings SMI’s SM2504XT to retail with top-tier responsiveness and excellent efficiency, though not the fastest post-cache writes."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/anycubic-and-thingiverse-announce-exclusive-3d-printing-partnership-makeronline-platform-to-offer-1-click-multicolor-3mf-models",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic and Thingiverse announce exclusive 3D printing partnership",
    "url": "https://www.tomshardware.com/3d-printing/anycubic-and-thingiverse-announce-exclusive-3d-printing-partnership-makeronline-platform-to-offer-1-click-multicolor-3mf-models",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T15:00:00+00:00",
    "summary": "Thingiverse partners with Anycubic to bring models directly to 3D printers."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-labs-black-friday-sale-cuts-up-to-usd300-on-the-flagship-h2c-printer-and-more-deep-cuts-across-companys-3d-printer-and-filament-lineup",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab's Black Friday sale cuts up to $300 on the flagship H2C printer and more",
    "url": "https://www.tomshardware.com/3d-printing/bambu-labs-black-friday-sale-cuts-up-to-usd300-on-the-flagship-h2c-printer-and-more-deep-cuts-across-companys-3d-printer-and-filament-lineup",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:30:00+00:00",
    "summary": "Strike an early bargain in Bambu Lab's Black Friday sale. Running until December 1st, save up to $300 on their flagship 3D printer."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/sam-altman-travels-to-south-korea-to-meet-samsung-leadership-to-secure-more-ram-for-data-centers-amid-crushing-shortages-openai-ceo-meets-samsung-leadership-to-discuss-future-ai-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "Sam Altman meets with Samsung leadership to secure more RAM for data centers amid crushing shortages",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/sam-altman-travels-to-south-korea-to-meet-samsung-leadership-to-secure-more-ram-for-data-centers-amid-crushing-shortages-openai-ceo-meets-samsung-leadership-to-discuss-future-ai-data-centers",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:21:23+00:00",
    "summary": "OpenAI CEO Sam Altman met with around 50 Samsung executives in South Korea on October 31 to discuss AI's future, business opportunities and the technology's impact on corporate operations. The meeting"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source USB tool unlocks Nvidia's half-speed GPU AI limiter on Windows",
    "url": "https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-01T14:00:00+00:00",
    "summary": "An open-source UEFI tool, nv-uefi-unlocker, lifts Nvidia’s tensor rate cap on RTX 20, 30, and 40-series GPUs under Windows."
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "AI 算力 / 半导体",
    "title": "xAI’s Colossus 2 – First Gigawatt Datacenter In The World, Unique RL Methodology, Capital Raise",
    "url": "https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "source": "AJ Kourabi",
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
    "source": "Ivan Chiam",
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
    "source": "Jeff Koch",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-08T09:54:57+00:00",
    "summary": "Compute is the lifeblood of AI. He who controls the spice controls the universe the compute will control the production of tokens and reap the benefits of AI. Without compute you do not have a seat at"
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
    "points": 1018,
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
    "points": 338,
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
    "id": "rss:https://www.theverge.com/tech/1024915/apple-iphone-duo-supply-chain-constraints",
    "domain": "大厂 AI 动态",
    "title": "Apple is ‘not able to predict’ when it&#8217;ll have enough iPhone Duos to go around",
    "url": "https://www.theverge.com/tech/1024915/apple-iphone-duo-supply-chain-constraints",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T22:56:11+00:00",
    "summary": "Apple CEO John Ternus doesn't have a timeline for when iPhone Duo supply constraints could lift. During an interview with Reuters, Ternus said the company is \"working hard to get it to as many custome"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1024748/apple-q4-2026-iphone-sales-earnings",
    "domain": "大厂 AI 动态",
    "title": "Apple set an iPhone sales record even without a new standard iPhone",
    "url": "https://www.theverge.com/tech/1024748/apple-q4-2026-iphone-sales-earnings",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T22:02:36+00:00",
    "summary": "Apple had a record-breaking quarter for iPhone sales - despite not releasing a standard model during its latest refresh. In its fourth-quarter earnings report released on Monday, Apple says it earned "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1024835/meta-vr-quest-2-pro-os-end-updates",
    "domain": "大厂 AI 动态",
    "title": "Meta will end Quest 2 OS updates in 2027",
    "url": "https://www.theverge.com/tech/1024835/meta-vr-quest-2-pro-os-end-updates",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T21:04:20+00:00",
    "summary": "Meta is planning to release the last OS update for its Quest 2 and Quest Pro VR headsets by March 2027, the company announced today. The last OS update for those devices is planned to be v213, and aft"
  },
  {
    "id": "rss:https://www.theverge.com/1024807/google-botnet-android-tv-shut-down",
    "domain": "大厂 AI 动态",
    "title": "One of Google’s Android partners turned 1.3 million set-top boxes into a botnet",
    "url": "https://www.theverge.com/1024807/google-botnet-android-tv-shut-down",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T20:37:49+00:00",
    "summary": "Google says one of its Android manufacturing partners secretly built a backdoor in 1.3 million devices and turned them into a botnet. The company says it has now dismantled the backdoor and \"cut ties\""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1024616/bmw-level-2-city-driver-assist-2027",
    "domain": "大厂 AI 动态",
    "title": "BMW is taking on Tesla’s FSD with urban driver assist starting in 2027",
    "url": "https://www.theverge.com/transportation/1024616/bmw-level-2-city-driver-assist-2027",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T20:03:52+00:00",
    "summary": "BMW says that it will expand its navigation-guided, partially automated driving capabilities into urban environments starting in 2027, launching first in Germany with other markets to follow. The new "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1024416/apple-watch-ultra-4-ugreen-finetrack-2-bluetooth-tracker-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Apple Watch Ultra 4 is $100 off, matching its best price to date",
    "url": "https://www.theverge.com/gadgets/1024416/apple-watch-ultra-4-ugreen-finetrack-2-bluetooth-tracker-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:24:09+00:00",
    "summary": "The Apple Watch Ultra 4 is the company&#8217;s most capable smartwatch. Whether you intend to put its many tracking features to the test, or you simply want the longest battery life of any Apple Watch"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1024386/ford-customer-driving-data-privacy-promise-data-brokers",
    "domain": "大厂 AI 动态",
    "title": "Ford promises not to sell your driving habits to data brokers",
    "url": "https://www.theverge.com/transportation/1024386/ford-customer-driving-data-privacy-promise-data-brokers",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:05:46+00:00",
    "summary": "Ford vowed to never sell customer driving data to third-party data brokers as part of a new privacy promise aimed at setting the automaker apart from competitors that have faced legal and regulatory b"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1024632/anthropic-claude-ai-video-game-clones",
    "domain": "大厂 AI 动态",
    "title": "Anthropic clamps down on Claude’s AI video game clones",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1024632/anthropic-claude-ai-video-game-clones",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:56:02+00:00",
    "summary": "Anthropic has updated Claude Code's system prompt to prevent the AI tool from being used to re-create existing video games, as reported by Tom's Hardware. Retro gaming is currently being overrun with "
  },
  {
    "id": "rss:https://www.theverge.com/news/1024649/xbox-chief-operating-officer-helen-chiang-depature-comments",
    "domain": "大厂 AI 动态",
    "title": "Xbox&#8217;s former COO has ‘serious concerns’ about her abrupt departure",
    "url": "https://www.theverge.com/news/1024649/xbox-chief-operating-officer-helen-chiang-depature-comments",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:43:24+00:00",
    "summary": "Xbox's former chief operating officer, Helen Chiang, suddenly left Microsoft less than two weeks ago after being promoted into the role in July. I wrote in my Notepad newsletter last week that it seem"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1024604/openai-data-center-grid-protection-program",
    "domain": "大厂 AI 动态",
    "title": "OpenAI pitches data center power plants as a way to protect nearby areas",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1024604/openai-data-center-grid-protection-program",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:01:30+00:00",
    "summary": "In an announcement on Monday, OpenAI says it will pilot its \"Grid Protectors Program\" at an upcoming data center in Effingham County, Georgia, where the company promises to free up to 1,000 megawatts "
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/03/yvonne-bajela-is-bringing-17m-in-fresh-capital-to-europes-startup-scene/",
    "domain": "大厂 AI 动态",
    "title": "Yvonne Bajela is bringing $17M in fresh capital to Europe’s startup scene",
    "url": "https://techcrunch.com/2026/11/03/yvonne-bajela-is-bringing-17m-in-fresh-capital-to-europes-startup-scene/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T08:01:00+00:00",
    "summary": "Evertrue Capital announces $17M debut fund to back early stage AI and fintech."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/apple-watchs-ai-features-for-rewinding-and-recapping-conversations-begin-beta-testing/",
    "domain": "大厂 AI 动态",
    "title": "Apple Watch’s AI features for rewinding and recapping conversations begin beta testing",
    "url": "https://techcrunch.com/2026/11/02/apple-watchs-ai-features-for-rewinding-and-recapping-conversations-begin-beta-testing/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T07:20:00+00:00",
    "summary": "Now in beta: Apple's new Audio Intelligence features can help you remember what someone said or take notes on conversations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/google-takes-dreambeans-to-india-in-bid-to-bring-ai-generated-personal-stories-to-the-masses/",
    "domain": "大厂 AI 动态",
    "title": "Google takes Dreambeans to India in bid to bring AI-generated personal stories to the masses",
    "url": "https://techcrunch.com/2026/11/02/google-takes-dreambeans-to-india-in-bid-to-bring-ai-generated-personal-stories-to-the-masses/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T03:30:00+00:00",
    "summary": "Google's Dreambeans, its latest AI experiment, now supports 13 Indian languages."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/apple-may-try-to-increase-revenue-by-doing-something-with-third-party-ai-apps/",
    "domain": "大厂 AI 动态",
    "title": "Apple may try to increase revenue by doing…something with third-party AI apps",
    "url": "https://techcrunch.com/2026/11/02/apple-may-try-to-increase-revenue-by-doing-something-with-third-party-ai-apps/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T01:49:52+00:00",
    "summary": "Apple hinted at ways that it could spur revenue through third-party \"opportunities\" during its Monday night earnings call."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/ukraines-new-pocket-sized-gadget-turns-russian-drones-cameras-against-them/",
    "domain": "大厂 AI 动态",
    "title": "Ukraine’s new pocket-sized gadget turns Russian drones’ cameras against them",
    "url": "https://techcrunch.com/2026/11/02/ukraines-new-pocket-sized-gadget-turns-russian-drones-cameras-against-them/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T01:12:55+00:00",
    "summary": "A Kyiv startup’s pocket-sized, 10-ounce receiver lets Ukrainian troops watch the video feeds of Russian drones, though Russian moves toward digital video and AI-guided drones that emit no signals coul"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/",
    "domain": "大厂 AI 动态",
    "title": "Y Combinator’s Garry Tan uses AI agents so much, he spends up to $200K a year on tokens",
    "url": "https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T00:35:52+00:00",
    "summary": "Y Combinator Garry Tan has jokingly admitted that he's suffered from \"cyber psychosis” and barely sleeps sometimes because he’s so excited to be working with his AI agents. On a new episode of Walter "
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/hinge-tests-a-cheaper-plan-as-users-become-more-fed-up-paying-for-dating-apps/",
    "domain": "大厂 AI 动态",
    "title": "Hinge tests a cheaper plan as users become more fed up paying for dating apps",
    "url": "https://techcrunch.com/2026/11/02/hinge-tests-a-cheaper-plan-as-users-become-more-fed-up-paying-for-dating-apps/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-03T00:14:51+00:00",
    "summary": "At a time when people are increasingly tired of dating apps, Hinge is testing a cheaper subscription plan."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/apple-says-its-hard-to-predict-when-iphone-duo-constraints-will-improve/",
    "domain": "大厂 AI 动态",
    "title": "Apple says it’s ‘hard to predict’ when iPhone Duo constraints will improve",
    "url": "https://techcrunch.com/2026/11/02/apple-says-its-hard-to-predict-when-iphone-duo-constraints-will-improve/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T23:25:32+00:00",
    "summary": "Apple says iPhone Duo production is ramping up, but it still can't say when supply will catch up with demand as shipping delays stretch into next year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/trajectory-raises-45m-to-make-ai-model-training-accessible-to-nontechnical-experts/",
    "domain": "大厂 AI 动态",
    "title": "Trajectory raises $45M to make AI model training accessible to nontechnical experts",
    "url": "https://techcrunch.com/2026/11/02/trajectory-raises-45m-to-make-ai-model-training-accessible-to-nontechnical-experts/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T23:13:53+00:00",
    "summary": "The one-year-old startup is now valued at $300 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/apples-inventory-surges-154-as-memory-chip-costs-climb/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s inventory surges 154% as memory chip costs climb",
    "url": "https://techcrunch.com/2026/11/02/apples-inventory-surges-154-as-memory-chip-costs-climb/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T23:04:57+00:00",
    "summary": "Apple says unprecedented memory chip costs will continue to rise, raising questions about future device prices as its inventory climbs to $14.5 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic warns that it’s very close to RSI capability, aka self-building AI",
    "url": "https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T22:14:50+00:00",
    "summary": "RSI is the point at which AI grows so good at training itself that it spawns a dramatic acceleration of AI capabilities. To the AI doomers, RSI represents the cataclysm from which there is no return."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/germany-says-lawmakers-iphones-may-have-been-hacked-with-spyware/",
    "domain": "大厂 AI 动态",
    "title": "Germany says lawmakers’ iPhones may have been hacked with spyware",
    "url": "https://techcrunch.com/2026/11/02/germany-says-lawmakers-iphones-may-have-been-hacked-with-spyware/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:45:54+00:00",
    "summary": "German lawmakers and a filmmaker are among the people who received notifications from Apple warning that their phones may have been hacked."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/web-host-squarespace-lays-off-19-of-its-employees/",
    "domain": "大厂 AI 动态",
    "title": "Web host Squarespace lays off 19% of its employees",
    "url": "https://techcrunch.com/2026/11/02/web-host-squarespace-lays-off-19-of-its-employees/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:25:59+00:00",
    "summary": "The website builder said that the job losses are part of a broader restructuring of its organization."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/",
    "domain": "大厂 AI 动态",
    "title": "New York Times and other outlets sue web browser Brave over alleged content scraping",
    "url": "https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:19:17+00:00",
    "summary": "The New York Times is suing privacy-focused web browser company Brave for allegedly scraping the outlet’s copyrighted content and unlawfully distributing it to its own customers, like Anthropic and Pe"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/snap-settles-lawsuit-accusing-platform-of-fueling-teen-depression-and-eating-disorders/",
    "domain": "大厂 AI 动态",
    "title": "Snap settles lawsuit accusing platform of fueling teen depression and eating disorders",
    "url": "https://techcrunch.com/2026/11/02/snap-settles-lawsuit-accusing-platform-of-fueling-teen-depression-and-eating-disorders/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:11:49+00:00",
    "summary": "The plaintiffs said they started using YouTube as young as age 3 and other social media platforms at around age 9 and developed compulsive usage habits that they attributed to features such as autopla"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/in-one-of-the-largest-deals-in-tech-history-marvell-buys-lumentum-for-115b/",
    "domain": "大厂 AI 动态",
    "title": "In one of the largest deals in tech history, Marvell buys Lumentum for $115B",
    "url": "https://techcrunch.com/2026/11/02/in-one-of-the-largest-deals-in-tech-history-marvell-buys-lumentum-for-115b/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T17:54:11+00:00",
    "summary": "Marvell's planned purchase of Lumentum is one of the biggest acquisitions in tech history. And they both have the same strategic investor: Nvidia."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/readwise-takes-on-amazons-kindle-and-goodreads-with-its-new-app-for-book-lovers/",
    "domain": "大厂 AI 动态",
    "title": "Readwise takes on Amazon’s Kindle and Goodreads with its new app for book lovers",
    "url": "https://techcrunch.com/2026/11/02/readwise-takes-on-amazons-kindle-and-goodreads-with-its-new-app-for-book-lovers/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T17:49:41+00:00",
    "summary": "Readwise Books combines an e-book store, reading tracker, detailed reading stats, and AI features in a bid to challenge Amazon's ecosystem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/spacex-reportedly-wants-to-buy-boost-mobile-to-compete-with-att-t-mobile-and-verizon/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX reportedly wants to buy Boost Mobile to compete with AT&T, T-Mobile, and Verizon",
    "url": "https://techcrunch.com/2026/11/02/spacex-reportedly-wants-to-buy-boost-mobile-to-compete-with-att-t-mobile-and-verizon/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T16:44:48+00:00",
    "summary": "SpaceX has been looking for new ways to use its Starlink network, and a tie-up with cellular operator Boost Mobile could give it the terrestrial access it needs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/42ai-comes-out-of-stealth-with-62-5m-and-a-world-model-that-can-predict-human-behavior/",
    "domain": "大厂 AI 动态",
    "title": "42AI comes out of stealth with $62.5M and a world model that can ‘predict human behavior’",
    "url": "https://techcrunch.com/2026/11/02/42ai-comes-out-of-stealth-with-62-5m-and-a-world-model-that-can-predict-human-behavior/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T16:30:00+00:00",
    "summary": "Here's a question straight out of sci-fi: What if AI could predict what you were going to do before you decided to, even in a completely new situation?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/02/elon-musk-throttles-grok-bot-limits-due-to-unsustainably-high-costs/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk throttles Grok Bot limits due to ‘unsustainably high’ costs",
    "url": "https://techcrunch.com/2026/11/02/elon-musk-throttles-grok-bot-limits-due-to-unsustainably-high-costs/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T16:23:21+00:00",
    "summary": "Musk recently referred to Grok Bot as having \"the fastest growth of a product that I've ever seen in my life.\""
  },
  {
    "id": "rss:https://stratechery.com/2026/google-earnings-facebook-deja-vu-the-agent-play/",
    "domain": "大厂 AI 动态",
    "title": "Google Earnings, Facebook Déjà Vu, The Agent Play",
    "url": "https://stratechery.com/2026/google-earnings-facebook-deja-vu-the-agent-play/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T11:00:00+00:00",
    "summary": "Google's earnings miss looks a lot like Facebook's, and that's a credit to Google. The company is being more aggressive than they get credit for."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/at-home-in-space-opens-caps-air-and-space-museum-renovation/",
    "domain": "大厂 AI 动态",
    "title": "\"At Home in Space\" opens, caps Air and Space Museum renovation",
    "url": "https://arstechnica.com/space/2026/11/at-home-in-space-opens-caps-air-and-space-museum-renovation/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T23:30:16+00:00",
    "summary": "The Smithsonian's National Air and Space Museum has all of its \"space\" back open."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/research-roundup-6-cool-science-stories-we-almost-missed-7/",
    "domain": "大厂 AI 动态",
    "title": "Why large dogs age faster than small ones, and other October research highlights",
    "url": "https://arstechnica.com/science/2026/11/research-roundup-6-cool-science-stories-we-almost-missed-7/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T22:54:35+00:00",
    "summary": "Plus invisible tattoos, medieval skeleton gets an ID, trapping a single antimatter particle, and more."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/11/third-person-dies-of-bird-flu-since-virus-started-jumping-to-livestock/",
    "domain": "大厂 AI 动态",
    "title": "Third person dies of bird flu since virus started jumping to livestock",
    "url": "https://arstechnica.com/health/2026/11/third-person-dies-of-bird-flu-since-virus-started-jumping-to-livestock/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T21:21:43+00:00",
    "summary": "The threat is still considered to be low, but the virus continues to spread."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/11/googles-legend-of-zelda-easter-egg-transports-you-back-to-1998/",
    "domain": "大厂 AI 动态",
    "title": "Googling \"Zelda\" today offers a glimpse of how search worked in 1998",
    "url": "https://arstechnica.com/gaming/2026/11/googles-legend-of-zelda-easter-egg-transports-you-back-to-1998/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:52:23+00:00",
    "summary": "\"The flow of time is always cruel.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/most-of-our-measures-of-a-key-cognitive-process-dont-agree/",
    "domain": "大厂 AI 动态",
    "title": "Most of our measures of a key cognitive process don't agree",
    "url": "https://arstechnica.com/science/2026/11/most-of-our-measures-of-a-key-cognitive-process-dont-agree/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T19:13:26+00:00",
    "summary": "A big study with very little beyond negative results still gets published."
  },
  {
    "id": "rss:https://arstechnica.com/apple/2026/11/apples-roaming-home-robot-may-do-facetime-switch-lights-on-and-yell-at-your-cat/",
    "domain": "大厂 AI 动态",
    "title": "Coming in 2027: Apple’s $1,000 home robot for FaceTime and switching on lights",
    "url": "https://arstechnica.com/apple/2026/11/apples-roaming-home-robot-may-do-facetime-switch-lights-on-and-yell-at-your-cat/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:32:21+00:00",
    "summary": "Apple robot backed by CEO John Ternus may have hefty price tag and limited uses."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/11/claudes-new-rules-against-game-cloning-wont-stop-the-ai-copying-boom/",
    "domain": "大厂 AI 动态",
    "title": "Claude’s new rules against game cloning won’t stop the AI copying boom",
    "url": "https://arstechnica.com/ai/2026/11/claudes-new-rules-against-game-cloning-wont-stop-the-ai-copying-boom/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T18:05:31+00:00",
    "summary": "The tsunami of imitators is way bigger than any one model maker can stem."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/11/china-releases-timeline-for-lunar-landing-on-the-moon-targeting-before-2030/",
    "domain": "大厂 AI 动态",
    "title": "China publicly discloses plan for a lunar landing within three years",
    "url": "https://arstechnica.com/space/2026/11/china-releases-timeline-for-lunar-landing-on-the-moon-targeting-before-2030/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T17:09:13+00:00",
    "summary": "The plan does not include a mission similar to Apollo 8 or Artemis II."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/11/f1-in-mexico-city-we-have-a-new-world-champion/",
    "domain": "大厂 AI 动态",
    "title": "F1 in Mexico City: Yet another Ferrari fiasco, but that’s not all",
    "url": "https://arstechnica.com/cars/2026/11/f1-in-mexico-city-we-have-a-new-world-champion/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T15:57:24+00:00",
    "summary": "There was plenty of drama on and off the track for Formula 1 this weekend."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/the-world-has-a-new-plan-to-save-nature-but-it-still-needs-the-money/",
    "domain": "大厂 AI 动态",
    "title": "The world has a new plan to save nature, but it still needs the money",
    "url": "https://arstechnica.com/science/2026/11/the-world-has-a-new-plan-to-save-nature-but-it-still-needs-the-money/",
    "source": "Kenza Bryan, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T14:56:52+00:00",
    "summary": "A new action plan aims to rescue 2030 nature targets as financing remains inadequate."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/11/this-48-e-paper-display-can-be-whatever-you-want-it-to-be/",
    "domain": "大厂 AI 动态",
    "title": "This $48 e-paper display can be whatever you want it to be",
    "url": "https://arstechnica.com/gadgets/2026/11/this-48-e-paper-display-can-be-whatever-you-want-it-to-be/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-02T12:00:07+00:00",
    "summary": "This DIY e-paper display works in two official ecosystems or on your own server."
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
    "points": 210,
    "published_at": "2026-11-03T00:08:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342284",
    "domain": "股票",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 189,
    "published_at": "2026-11-02T19:27:37+00:00",
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
    "id": "hn:50325107",
    "domain": "股票",
    "title": "The question we should all be asking about AI",
    "url": "https://www.cnn.com/2026/10/30/business/ai-stocks-bonds-debt",
    "source": "heresie-dabord",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-01T12:44:36+00:00",
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
    "id": "hn:50348591",
    "domain": "股票",
    "title": "How AI is creating a lopsided US economy",
    "url": "https://www.abc.net.au/news/2026-10-19/ai-stock-market-concentration-data/107261078",
    "source": "gmays",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-11-03T05:58:27+00:00",
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
    "id": "hn:50297025",
    "domain": "股票",
    "title": "Intel stock plunges after posting disappointing Q4 outlook",
    "url": "https://finance.yahoo.com/video/intel-stock-plunges-after-posting-disappointing-q4-outlook-200731652.html",
    "source": "baal80spam",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-29T22:21:29+00:00",
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
    "id": "hn:50239430",
    "domain": "金融",
    "title": "Tesla cancels Cybertruck in Australia and NZ after 7 years of deposits",
    "url": "https://electrek.co/2026/10/23/tesla-cancels-cybertruck-australia-new-zealand/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-10-26T05:13:15+00:00",
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
    "id": "hn:50295332",
    "domain": "金融",
    "title": "Tesla caught altering specs following rear suspension collapse reports",
    "url": "https://carnewschina.com/2026/09/17/tesla-caught-quietly-altering-model-y-l-manual-specs-following-rear-suspension-collapse-reports/",
    "source": "Alien1Being",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-10-29T20:24:13+00:00",
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
    "id": "hn:50159683",
    "domain": "金融",
    "title": "Trump Appointees Asked a Federal Agency to Acquire a Voting Machine and Hack It",
    "url": "https://www.propublica.org/article/cisa-election-security-donald-trump",
    "source": "soundworlds",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-10-20T00:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50152041",
    "domain": "金融",
    "title": "Federal judge rules Flock violated the fourth amendment",
    "url": "https://twitter.com/scotus_wire/status/2106487374624514071",
    "source": "vessenes",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-19T13:14:41+00:00",
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
    "id": "hn:50202423",
    "domain": "金融",
    "title": "Elon Musk pours $366M into midterm Republican campaigns",
    "url": "https://www.cnbc.com/2026/10/22/elon-musk-midterm-election-spacex-tesla.html",
    "source": "Alien1Being",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-10-22T23:17:23+00:00",
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
  }
]
```
