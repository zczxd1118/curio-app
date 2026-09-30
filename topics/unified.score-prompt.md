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

- 今日日期：`2026-09-30`
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
  "date": "2026-09-30",
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
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2020843,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1918522,
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
    "points": 1348520,
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
    "points": 1297126,
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
    "points": 1033624,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 893040,
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
    "points": 820360,
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
    "points": 698439,
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
    "points": 590893,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 443612,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 412451,
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
    "points": 301326,
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
    "points": 299037,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 227923,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 222721,
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
    "points": 191019,
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
    "points": 182355,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 172883,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1wDhj6wEa8",
    "domain": "AI",
    "title": "全网刷屏的 Jev 模型正式开放！保姆级教程 + 实战测评",
    "url": "http://www.bilibili.com/video/av117313592367632",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 171073,
    "published_at": "2026-09-22T07:50:41+00:00",
    "summary": "全网爆火的 Jev 模型是什么？有什么用？怎么使用？怎么接入 AI 编程工具（比如 Codex）？效果真的好么？跟 DeepSeek V4 Flash 比速度如何？傻子可懂的 Jev 保姆级实战教程 + 实战测评来啦。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n记得三连支持、关注鱼皮，让更多朋友学到知识"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 158086,
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
    "points": 151518,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 145210,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 101073,
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
    "points": 93855,
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
    "points": 82288,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1EMhx6QEXa",
    "domain": "AI",
    "title": "【AI时代的STM32教程】",
    "url": "http://www.bilibili.com/video/av117319145688318",
    "source": "keysking",
    "platform": "bilibili",
    "points": 71238,
    "published_at": "2026-09-23T07:32:51+00:00",
    "summary": "新时代的 STM32 教程，正式开更！🚀\n这次我们从 STM32C5 出发，全面拥抱AI Agent 带来的全新开发方式, 以及 STM32CubeMX2、VS Code的现代化开发生态。\n也特别感谢 @意法半导体中国   对本系列的支持～\nSTM32 正在进入一个新的开发时代，我们也会继续把外设原理和工程实践讲透，同时一起探索 AI 时代更高效的学习方式：把原理学明白，把需求说清楚，再让 AI "
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63941,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 63646,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "domain": "AI",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 60598,
    "published_at": "2025-06-28T02:37:22+00:00",
    "summary": "视频主题&amp;项目背景\n主题： 分享个人如何使用cursor 从0到1开发一个比较大的项目，使用的技术栈是vue+小程序+java\n项目\n一个B2B的订货商城及供应链全流程管理，包含的端有：\n小程序商城端\n供应商端\n仓储物流端\n司机配送端\n销售端\n后台管理系统\n以上小程序端都是使用webview的方式\n核心功能：\n商城的基本功能: 正逆向订单、商品、购物车、优惠券、积分、钱包、充值、工单等\n供"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 56548,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 55968,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 53855,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 51723,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48783,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 42009,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 40940,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34427,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1CmAGegEpa",
    "domain": "AI",
    "title": "使用Cursor实战Java项目（Cursor写Java代码）",
    "url": "http://www.bilibili.com/video/av114012708733672",
    "source": "小道仙97",
    "platform": "bilibili",
    "points": 33022,
    "published_at": "2025-02-16T09:02:42+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30825,
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
    "points": 29788,
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
    "points": 28967,
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
    "points": 27677,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1Kvan6QE39",
    "domain": "AI",
    "title": "【全400集】已经替大家付费了，花1W买的AI漫剧制作全套系统教程，逼自己一个月学完，AI邪术爆涨！允许白嫖AI漫剧制作全教程/AI漫剧零基础入门教程",
    "url": "http://www.bilibili.com/video/av117352515505121",
    "source": "晓墨AI电商",
    "platform": "bilibili",
    "points": 23950,
    "published_at": "2026-09-29T04:54:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23459,
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
    "points": 22800,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XGaA6CEwe",
    "domain": "AI",
    "title": "【2026最新】Claude Code保姆级完整教程-最强AI助手！从入门到进阶，速通Claude Code！一个方法教你规避封号风险！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av117325537810666",
    "source": "大模型小阳",
    "platform": "bilibili",
    "points": 22387,
    "published_at": "2026-09-24T10:36:14+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~"
  },
  {
    "id": "bvid:BV1nChG6nEY4",
    "domain": "AI",
    "title": "韦东山老师教你用 DeepSeek 与 Claude Code，在 Ubuntu 中搭建嵌入式 Linux AI 开发环境：从安装配置到代码智能辅助开发实战",
    "url": "http://www.bilibili.com/video/av117155165177009",
    "source": "韦东山",
    "platform": "bilibili",
    "points": 21020,
    "published_at": "2026-08-25T08:22:35+00:00",
    "summary": "韦东山老师手把手教你在 Ubuntu 中搭建嵌入式 AI 开发环境，完整介绍开发工具、VMware Tools、中文输入法、VS Code 与常用插件的安装配置，以及 DeepSeek API Key 和 Claude Code 的接入方法。借助 AI 大模型完成代码分析、工程理解、问题排查和辅助开发，让嵌入式 Linux 学习与开发更加高效。\n查看完整文字教程：https://www.100as"
  },
  {
    "id": "bvid:BV1soaJ6mEM9",
    "domain": "AI",
    "title": "【吊打付费】已经替大家付费了，花1W买的AI漫剧制作全套系统教程，逼自己一个月学完，AI邪术爆涨！允许白嫖AI漫剧制作全教程/AI漫剧零基础入门教程",
    "url": "http://www.bilibili.com/video/av117353136262143",
    "source": "即梦AI动态漫制作",
    "platform": "bilibili",
    "points": 19773,
    "published_at": "2026-09-29T07:33:15+00:00",
    "summary": "想系统学习AI漫剧的小伙伴看置顶评论~\n持续更新中~课程资料”666“获取~求一键三连【长按点赞】支持！"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 18671,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 18657,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1084,
    "published_at": "2026-09-28T02:05:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 970,
    "published_at": "2026-09-16T11:15:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 401,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-09-24T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49879032",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says AI distillation is 'competition.'",
    "url": "https://www.cnbc.com/2026/09/28/nvidias-jensen-huang-ai-distillation-china.html",
    "source": "cramer4next",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-28T14:55:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 128,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/ai-drives-larger-denser-packaging-raising-new-challenges-for-equipment-makers/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Drives Larger, Denser Packaging, Raising New Challenges for Equipment Makers",
    "url": "https://www.eetimes.com/ai-drives-larger-denser-packaging-raising-new-challenges-for-equipment-makers/",
    "source": "Susan Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T08:55:36+00:00",
    "summary": "At A*STAR’s Innovate Together 2026, industry experts explored packaging, hybrid bonding, optical interconnects, and process control for AI. The post AI Drives Larger, Denser Packaging, Raising New Cha"
  },
  {
    "id": "rss:https://www.eetimes.com/astera-labs-leo-controller-update-targets-memory-constraints/",
    "domain": "AI 算力 / 半导体",
    "title": "Astera Labs’ Leo Controller Update Targets Memory Constraints",
    "url": "https://www.eetimes.com/astera-labs-leo-controller-update-targets-memory-constraints/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T22:00:00+00:00",
    "summary": "Astera Labs pairs Leo memory controllers with Scorpio fabric switches to bring scalable memory closer to AI accelerators. The post Astera Labs’ Leo Controller Update Targets Memory Constraints appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-data-centers-make-power-cooling-critical-to-scaling/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Data Centers Make Power, Cooling Critical to Scaling",
    "url": "https://www.eetimes.com/ai-data-centers-make-power-cooling-critical-to-scaling/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T14:42:45+00:00",
    "summary": "AI is transforming data centers into infrastructure platforms where power, cooling, and semiconductors determine scalability. The post AI Data Centers Make Power, Cooling Critical to Scaling appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/eu-cyber-resilience-act-three-misconceptions-that-put-embedded-products-at-risk/",
    "domain": "AI 算力 / 半导体",
    "title": "EU Cyber Resilience Act: Three Misconceptions That Put Embedded Products at Risk",
    "url": "https://www.eetimes.com/eu-cyber-resilience-act-three-misconceptions-that-put-embedded-products-at-risk/",
    "source": "Florian Drittenthaler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T13:13:52+00:00",
    "summary": "The EU Cyber Resilience Act affects more embedded products than manufacturers may expect, with implications for connectivity, resale, and long-term security support. The post EU Cyber Resilience Act: "
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-details-quantum-ai-developments-in-india/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM Details Quantum, AI Developments in India",
    "url": "https://www.eetimes.com/ibm-details-quantum-ai-developments-in-india/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T07:30:00+00:00",
    "summary": "At SEMICON India 2026, IBM's Rahul Rao details India's role in quantum scaling, Qiskit education, and AI accelerators. The post IBM Details Quantum, AI Developments in India appeared first on EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/why-u-s-europe-cooperation-matters-for-quantum-leadership/",
    "domain": "AI 算力 / 半导体",
    "title": "Why U.S.-Europe Cooperation Matters for Quantum Leadership",
    "url": "https://www.eetimes.com/why-u-s-europe-cooperation-matters-for-quantum-leadership/",
    "source": "Jonathan Felbinger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T19:00:00+00:00",
    "summary": "U.S.-Europe collaboration is critical for global quantum leadership, combining capital and talent to scale against rising competition. The post Why U.S.-Europe Cooperation Matters for Quantum Leadersh"
  },
  {
    "id": "rss:https://www.eetimes.com/calterah-turns-uwb-digital-keys-into-in-cabin-sensors/",
    "domain": "AI 算力 / 半导体",
    "title": "Calterah Turns UWB Digital Keys into In-Cabin Sensors",
    "url": "https://www.eetimes.com/calterah-turns-uwb-digital-keys-into-in-cabin-sensors/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T12:58:32+00:00",
    "summary": "Calterah brings UWB keyless anchors into synchronized networks, delivering enhanced vehicle safety without adding expensive hardware. The post Calterah Turns UWB Digital Keys into In-Cabin Sensors app"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/zotac-denies-warranty-support-to-rtx-3060-owner-in-india-after-just-one-year-despite-offering-three-years-of-coverage-company-says-gpus-2023-import-date-takes-precedence-over-purchase-date",
    "domain": "AI 算力 / 半导体",
    "title": "Zotac denies warranty support to RTX 3060 owner in India after just one year despite offering three years of coverage",
    "url": "https://www.tomshardware.com/pc-components/gpus/zotac-denies-warranty-support-to-rtx-3060-owner-in-india-after-just-one-year-despite-offering-three-years-of-coverage-company-says-gpus-2023-import-date-takes-precedence-over-purchase-date",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T15:17:35+00:00",
    "summary": "The owner of a Zotac RTX 3060 in India was denied warranty coverage just one year after buying the card in 2025, despite Zotac's offer of a three-year standard warranty in the country. The company cla"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/score-the-nintendo-switch-2-at-its-lowest-ever-amazon-uk-price-now-just-gbp354-99-pocket-a-gbp65-discount-on-nintendos-portable-gaming-console-with-a-7-9-inch-1080p-screen-4k-dock-and-magnetic-controllers",
    "domain": "AI 算力 / 半导体",
    "title": "Score the Nintendo Switch 2 at its lowest ever Amazon UK price, now just £354.99",
    "url": "https://www.tomshardware.com/video-games/nintendo/score-the-nintendo-switch-2-at-its-lowest-ever-amazon-uk-price-now-just-gbp354-99-pocket-a-gbp65-discount-on-nintendos-portable-gaming-console-with-a-7-9-inch-1080p-screen-4k-dock-and-magnetic-controllers",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T15:11:18+00:00",
    "summary": "The Nintendo Switch 2 is now at a record low price on Amazon UK at just £354.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/blockchain-assisted-cyberattacks-surge-fivefold-driven-by-iranian-and-north-korean-state-actors-russia-linked-groups-open-weight-llms-are-linked-to-an-increase-in-attacks",
    "domain": "AI 算力 / 半导体",
    "title": "Blockchain-assisted cyberattacks surge fivefold, driven by Iranian and North Korean state actors, Russia-linked groups",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/blockchain-assisted-cyberattacks-surge-fivefold-driven-by-iranian-and-north-korean-state-actors-russia-linked-groups-open-weight-llms-are-linked-to-an-increase-in-attacks",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T14:10:00+00:00",
    "summary": "A new report says blockchain dead-drop attacks have risen 440%, with state-linked and criminal groups using transactions, smart contracts, and even phantom wallets to hide malware payloads and C2 infr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-lists-existential-risks-to-humanity-as-one-of-its-risk-factors-in-ipo-prospectus-80-pages-of-risk-factors-dwarf-business-description-as-firm-eyes-usd2-trillion-debut",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic lists ‘existential risks to humanity’ as one of its risk factors in IPO prospectus",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-lists-existential-risks-to-humanity-as-one-of-its-risk-factors-in-ipo-prospectus-80-pages-of-risk-factors-dwarf-business-description-as-firm-eyes-usd2-trillion-debut",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T13:30:00+00:00",
    "summary": "Anthropic serves a dire warning in its IPO prospectus, saying how a rogue model could lead to the end of humanity and, consequentially, its business. Nevertheless, investors are still hoping for a $2-"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/we-tested-13-power-banks-to-help-you-choose-the-best-one-from-10-25k-mah-and-20-220w",
    "domain": "AI 算力 / 半导体",
    "title": "We tested 13 power banks to help you choose the best one",
    "url": "https://www.tomshardware.com/peripherals/usb/we-tested-13-power-banks-to-help-you-choose-the-best-one-from-10-25k-mah-and-20-220w",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T13:10:00+00:00",
    "summary": "We tested 13 power banks from Anker, Belkin, Baseus, Cuktech, and Sharge, tracking charge times, output, temps, and capacity to see which actually hold up."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/silicon-is-starting-to-design-silicon-how-ai-is-being-used-in-chipmaking-from-eda-tools-to-openais-jalapeno-and-beyond",
    "domain": "AI 算力 / 半导体",
    "title": "Silicon is starting to design silicon — how AI is being used in chipmaking, from EDA tools to OpenAI's Jalapeño and beyond",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/silicon-is-starting-to-design-silicon-how-ai-is-being-used-in-chipmaking-from-eda-tools-to-openais-jalapeno-and-beyond",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T12:40:00+00:00",
    "summary": "How close is AI to designing the very same chips it runs on? We explore how artificial intelligence is being used in modern chip design today."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/save-40-percent-on-a-new-budget-gaming-keyboard-steelseries-apex-3-is-just-usd29-in-woot-deal",
    "domain": "AI 算力 / 半导体",
    "title": "Save 40% on a new budget gaming keyboard",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/save-40-percent-on-a-new-budget-gaming-keyboard-steelseries-apex-3-is-just-usd29-in-woot-deal",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T12:20:00+00:00",
    "summary": "Save 40% on this SteelSeries Apex 3 gaming keyboard at Woot"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-nova-lake-platforms-pass-compliance-at-pci-sig-usb-if-as-launch-looms",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's next-gen Nova Lake platforms pass compliance at USB and PCIe standards bodies as launch looms",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-nova-lake-platforms-pass-compliance-at-pci-sig-usb-if-as-launch-looms",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T12:00:00+00:00",
    "summary": "Intel is prepping Core Ultra 400-series 'Nova Lake' platform launches as CPUs and chipsets pass interoperability and compliance tests with PCI-SIG and USB-IF."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/sony-japan-tries-an-anti-scalper-lottery-system-for-ps5-pro-orders-locks-systems-behind-a-60-hour-playtime-requirement-strict-lottery-system-blocks-scalpers-and-tourists-in-japan-requires-a-domestic-account-to-buy",
    "domain": "AI 算力 / 半导体",
    "title": "Sony Japan tries an anti-scalper lottery system for PS5 Pro orders, locks systems behind a 60-hour playtime requirement",
    "url": "https://www.tomshardware.com/video-games/playstation/sony-japan-tries-an-anti-scalper-lottery-system-for-ps5-pro-orders-locks-systems-behind-a-60-hour-playtime-requirement-strict-lottery-system-blocks-scalpers-and-tourists-in-japan-requires-a-domestic-account-to-buy",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T11:32:05+00:00",
    "summary": "In the face of strong demand and device shortages, Sony has decided to filter PlayStation 5 Pro purchasers in Japan using a lottery system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-drops-an-epyc-usd15-000-256-core-bomb-epyc-9006-zen-6-venice-cpus-get-full-spec-and-pricing-treatment-from-usd700-up-to-usd14-904",
    "domain": "AI 算力 / 半导体",
    "title": "AMD drops an EPYC $15,000, 256-core beast",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-drops-an-epyc-usd15-000-256-core-bomb-epyc-9006-zen-6-venice-cpus-get-full-spec-and-pricing-treatment-from-usd700-up-to-usd14-904",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T11:20:00+00:00",
    "summary": "AMD has shared the full SKU list for its 6th Generation EPYC 9006 (codenamed Venice) series, with 1Ku pricing."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-this-4k-ready-gaming-pc-with-a-7800x3d-and-rtx-5070-for-under-usd2-000-right-now-saving-you-usd170-cyberpowerpc-machine-ships-with-32gb-ddr5-and-a-1tb-ssd-ready-for-high-performance-gameplay",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 4K-ready gaming PC with a 7800X3D and RTX 5070 for under $2,000 right now, saving you $170",
    "url": "https://www.tomshardware.com/pc-components/grab-this-4k-ready-gaming-pc-with-a-7800x3d-and-rtx-5070-for-under-usd2-000-right-now-saving-you-usd170-cyberpowerpc-machine-ships-with-32gb-ddr5-and-a-1tb-ssd-ready-for-high-performance-gameplay",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T11:10:00+00:00",
    "summary": "This powerful CyberPowerPC gaming rig, powered by the AMD Ryzen 7 7800X3D and Nvidia GeForce RTX 5070, alongside a 1TB SSD and 32GB of DDR5 RAM, unlocks 4K gameplay for $1,999.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-patent-outlines-embedding-microleds-directly-into-cpu-package-to-light-up-wording-or-work-as-an-extra-asethic-component-microled-is-embedded-with-die-in-glass-substrate",
    "domain": "AI 算力 / 半导体",
    "title": "Intel patent outlines embedding MicroLEDs directly into CPU package to light up wording or work as an 'extra aesthetic component'",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-patent-outlines-embedding-microleds-directly-into-cpu-package-to-light-up-wording-or-work-as-an-extra-asethic-component-microled-is-embedded-with-die-in-glass-substrate",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T10:50:00+00:00",
    "summary": "A recently published Intel patent reveals a system for embedding MicroLEDs directly into a CPU for diagnostic or aesthetic purposes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/photonics/intel-patent-embeds-microleds-in-chip-packaging-technology-may-enable-embedded-optical-interconnects-through-tgvs",
    "domain": "AI 算力 / 半导体",
    "title": "Intel patent embeds MicroLEDs in chip packaging — technology may enable embedded optical interconnects through TGVs",
    "url": "https://www.tomshardware.com/tech-industry/photonics/intel-patent-embeds-microleds-in-chip-packaging-technology-may-enable-embedded-optical-interconnects-through-tgvs",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T10:30:00+00:00",
    "summary": "Intel has showcased a patent it filed in 2022 to embed MicroLEDs inside chip packaging. The company suggests this could be used for diagnostic testing, customized lighting on chip surfaces, but perhap"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/early-nvidia-advisor-says-hes-owed-usd1-billion-in-stock-due-to-vesting-error-1993-stock-options-amount-to-around-4-5-million-shares-after-splits",
    "domain": "AI 算力 / 半导体",
    "title": "Early Nvidia advisor says he's owed $1 billion in stock due to a 1993 vesting error, but Nvidia rejected settlement",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/early-nvidia-advisor-says-hes-owed-usd1-billion-in-stock-due-to-vesting-error-1993-stock-options-amount-to-around-4-5-million-shares-after-splits",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T10:00:00+00:00",
    "summary": "Former Nvidia advisor Eric Gullichsen says a 1993 stock option grant leaves him owed about $1 billion in stock."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/anthropic-ceo-described-jensen-huang-as-kind-of-trump-like-during-2022-meeting-nvidia-ceo-reportedly-called-anthropic-executive-a-bean-counter-after-google-tpu-comparison",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic CEO described Jensen Huang as 'kind of Trump-like' during 2022 meeting",
    "url": "https://www.tomshardware.com/tech-industry/anthropic-ceo-described-jensen-huang-as-kind-of-trump-like-during-2022-meeting-nvidia-ceo-reportedly-called-anthropic-executive-a-bean-counter-after-google-tpu-comparison",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T09:30:00+00:00",
    "summary": "Author Kevin Roose reports that Nvidia and Anthropic's CEOs didn't like each other much during their first meeting in his new book, The AGI Chronicles."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/early-amd-gorgon-halo-ai-mini-pc-packs-192gb-ram-for-an-eye-watering-usd7-099-super-early-bird-deal-cuts-down-price-of-gmktec-evo-x5-with-ryzen-ai-max-pro-495-by-usd425",
    "domain": "AI 算力 / 半导体",
    "title": "Early AMD 'Gorgon Halo' AI mini-PC packs 192GB RAM for an eye-watering $7,099",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/early-amd-gorgon-halo-ai-mini-pc-packs-192gb-ram-for-an-eye-watering-usd7-099-super-early-bird-deal-cuts-down-price-of-gmktec-evo-x5-with-ryzen-ai-max-pro-495-by-usd425",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T17:20:00+00:00",
    "summary": "GMKtec launches the Evo-X5 Pro, an agentic mini-PC with AMD's Ryzen AI Max+ Pro 495, 192GB of RAM, and a price tag up to $7,099."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/the-netherlands-is-rolling-alternative-nixos-based-software-ecosystem-after-u-s-sanctions-on-icc-took-microsoft-off-the-table-trial-programs-running-now-first-release-expected-at-end-of-2027",
    "domain": "AI 算力 / 半导体",
    "title": "The Netherlands is rolling its own software and services after U.S. sanctions took Microsoft off the table",
    "url": "https://www.tomshardware.com/software/the-netherlands-is-rolling-alternative-nixos-based-software-ecosystem-after-u-s-sanctions-on-icc-took-microsoft-off-the-table-trial-programs-running-now-first-release-expected-at-end-of-2027",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T17:00:51+00:00",
    "summary": "When the U.S. imposed sanctions on the International Criminal Court, it also meant that its chief prosecutor lost access to Microsoft services, forcing the Dutch government to make alternative plans."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/google-confirms-chromeos-phase-out-in-2034-10-year-support-lifetime-cut-short-for-some-devices-company-says-it-will-support-transition-to-googlebook-os",
    "domain": "AI 算力 / 半导体",
    "title": "Google confirms ChromeOS phase out in 2034 — 10-year support lifetime cut short for some devices, company says it will support transition to Googlebook OS",
    "url": "https://www.tomshardware.com/laptops/google-confirms-chromeos-phase-out-in-2034-10-year-support-lifetime-cut-short-for-some-devices-company-says-it-will-support-transition-to-googlebook-os",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T16:38:07+00:00",
    "summary": "Google confirmed ChromeOS updates will phase out in 2034 as the company transitions to Googlebook OS and new laptops."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/synopsys-debuts-autopilot-platform-for-developing-chips-autonomously-using-ai-new-agentengineer-platform-is-poised-for-general-availability-by-the-end-of-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Synopsys debuts Autopilot platform for developing chips autonomously using AI",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/synopsys-debuts-autopilot-platform-for-developing-chips-autonomously-using-ai-new-agentengineer-platform-is-poised-for-general-availability-by-the-end-of-2026",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T16:35:00+00:00",
    "summary": "Synopsys unveiled seven AgentEngineer agents on its new Autopilot platform, with general availability planned for the end of 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/noctua-upgrades-thermal-grizzlys-12v-2x6-power-monitor-cuts-active-noise-to-21-5db-and-runs-passively-up-to-a-300w-gpu-load",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua upgrades Thermal Grizzly's 12V-2x6 power monitor",
    "url": "https://www.tomshardware.com/pc-components/gpus/noctua-upgrades-thermal-grizzlys-12v-2x6-power-monitor-cuts-active-noise-to-21-5db-and-runs-passively-up-to-a-300w-gpu-load",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T16:15:00+00:00",
    "summary": "The Noctua Edition replaces the original WireView Pro II cooling solution with a semi-passive design that can handle up to 300W without active cooling and runs below 2,000 RPM when the fan is needed."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/steam-adds-low-latency-pyrowave-codec-to-remote-play-new-codec-offers-better-game-streaming-on-local-networks-but-costs-5-10-times-more-bandwidth",
    "domain": "AI 算力 / 半导体",
    "title": "Steam adds low-latency Pyrowave codec to Remote Play — new codec offers better game streaming on local networks but costs '5-10 times' more bandwidth",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/steam-adds-low-latency-pyrowave-codec-to-remote-play-new-codec-offers-better-game-streaming-on-local-networks-but-costs-5-10-times-more-bandwidth",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T16:10:32+00:00",
    "summary": "The Pyrowave codec was specifically created for the purpose of game streaming, taking advantage of the large bandwidth and powerful compute available on home networks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-custom-jalapeno-ai-inference-asic-is-for-openais-internal-use-but-company-leaves-the-door-open-to-broader-rollout-firm-says-it-will-have-its-hands-full-with-jalapeno-for-a-good-long-time",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's custom Jalapeno AI inference ASIC is for OpenAI’s internal use, but company leaves the door open to broader rollout",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-custom-jalapeno-ai-inference-asic-is-for-openais-internal-use-but-company-leaves-the-door-open-to-broader-rollout-firm-says-it-will-have-its-hands-full-with-jalapeno-for-a-good-long-time",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:45:00+00:00",
    "summary": "OpenAI has danced with the idea of a broader rollout of its Jalapeño ASIC, but hardware VP Richard Ho tells us the chip is for internal use “first and foremost.”"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-jalapeno-design-interview-transcript-hardware-vp-richard-ho-explains-how-ai-assisted-design-may-shape-the-future-of-inference-asics",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI Jalapeño design interview transcript",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-jalapeno-design-interview-transcript-hardware-vp-richard-ho-explains-how-ai-assisted-design-may-shape-the-future-of-inference-asics",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:30:00+00:00",
    "summary": "We sit down with OpenAI's Hardware boss to talk about its chart-topping Jalapeño inference chip in this unredacted interview transcript."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/get-free-access-to-ai-chip-design-week-on-toms-hardware-premium-sign-up-for-an-account-to-read-all-the-in-depth-reports",
    "domain": "AI 算力 / 半导体",
    "title": "Get free access to AI Chip Design week on Tom's Hardware Premium — sign up for an account to read all the in-depth reports",
    "url": "https://www.tomshardware.com/tech-industry/get-free-access-to-ai-chip-design-week-on-toms-hardware-premium-sign-up-for-an-account-to-read-all-the-in-depth-reports",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:30:00+00:00",
    "summary": "From September 28 to October 2, you can access Tom's Hardware Premium's AI Chip Week special features for free, no payment required."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/you-can-now-play-nintendo-switch-games-on-a-jailbroken-ps5-early-alpha-hits-40-fps-in-lighter-titles-but-chokes-on-zelda",
    "domain": "AI 算力 / 半导体",
    "title": "You can now play Nintendo Switch games on a jailbroken PS5",
    "url": "https://www.tomshardware.com/video-games/console-gaming/you-can-now-play-nintendo-switch-games-on-a-jailbroken-ps5-early-alpha-hits-40-fps-in-lighter-titles-but-chokes-on-zelda",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:20:00+00:00",
    "summary": "An experimental emulator makes it possible to play Nintendo Switch games on a jailbroken PS5, with a variety of games having been tested."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-thunderbolt-5-docks-vectotech-v-core-vs-orico-tb5-thunderbolt-5-dock",
    "domain": "AI 算力 / 半导体",
    "title": "Testing two Thunderbolt 5 docks with M.2 storage — VectoTech V-Core vs Orico TB5",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-thunderbolt-5-docks-vectotech-v-core-vs-orico-tb5-thunderbolt-5-dock",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:00:00+00:00",
    "summary": "While their specs seem similar, one dock truly stands out in performance and features."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/virginia-tech-lab-3d-prints-a-liquid-metal-composite-to-guide-heat-boost-thermal-conductivity-40x-the-nozzle-stretches-gallium-indium-droplets-inside-soft-silicone-can-also-create-self-healing-traces",
    "domain": "AI 算力 / 半导体",
    "title": "Virginia Tech lab 3D prints a liquid metal composite to guide heat, boost thermal conductivity 40x",
    "url": "https://www.tomshardware.com/3d-printing/virginia-tech-lab-3d-prints-a-liquid-metal-composite-to-guide-heat-boost-thermal-conductivity-40x-the-nozzle-stretches-gallium-indium-droplets-inside-soft-silicone-can-also-create-self-healing-traces",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T14:45:00+00:00",
    "summary": "Virginia Tech lab prints gallium-indium liquid metal droplets in silicone that guide heat."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/uk-games-expo-bans-games-and-art-made-mostly-using-ai-ukge-enforces-booth-shutdowns-and-bans-after-deleted-comment-debacle-says-that-the-central-creative-process-must-be-conducted-by-humans",
    "domain": "AI 算力 / 半导体",
    "title": "UK Games Expo bans games and art made mostly using AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/uk-games-expo-bans-games-and-art-made-mostly-using-ai-ukge-enforces-booth-shutdowns-and-bans-after-deleted-comment-debacle-says-that-the-central-creative-process-must-be-conducted-by-humans",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T14:00:00+00:00",
    "summary": "The UK's largest tabletop gaming convention told exhibitors that they cannot show off games and other products mostly created using AI. It only allows the 'use of computerized tools used for spell che"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modders-bring-nvidias-dlss-5-neural-rendering-to-amd-radeon-gpus-latest-build-delivers-74-percent-performance-boost-in-just-24-hours-new-launcher-automates-install-process",
    "domain": "AI 算力 / 半导体",
    "title": "Modders bring Nvidia’s DLSS 5 Neural Rendering to AMD Radeon GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/modders-bring-nvidias-dlss-5-neural-rendering-to-amd-radeon-gpus-latest-build-delivers-74-percent-performance-boost-in-just-24-hours-new-launcher-automates-install-process",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T13:30:00+00:00",
    "summary": "An unofficial project is bringing Nvidia’s DLSS 5 to AMD Radeon GPUs, with early testing showing performance climbing from around 30 FPS to 50 FPS in Cyberpunk 2077 after rapid optimization."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/asrock-x870e-challenger-wifi-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock X870E Challenger Wifi Motherboard Review: A value X870E board packed with features",
    "url": "https://www.tomshardware.com/pc-components/motherboards/asrock-x870e-challenger-wifi-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T13:20:00+00:00",
    "summary": "ASRock’s X870E Challenger Wifi packs a flagship audio codec, robust VRMs, USB4, 5 GbE, and Wi-Fi 7 into an affordable, all-white ATX board. It’s one of the best-equipped AMD options under $230."
  },
  {
    "id": "rss:https://www.eetimes.com/xcena-cuts-data-movement-to-address-memory-bottlenecks/",
    "domain": "AI 算力 / 半导体",
    "title": "Xcena Cuts Data Movement to Address Memory Bottlenecks",
    "url": "https://www.eetimes.com/xcena-cuts-data-movement-to-address-memory-bottlenecks/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T07:30:00+00:00",
    "summary": "Xcena’s MX1 uses CXL to push compute into memory by combining DDR5, SSDs, and RISC-V cores while easing programmability. The post Xcena Cuts Data Movement to Address Memory Bottlenecks appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/full-stack-semiconductor-solutions-for-industry-and-digital-energy-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Full-Stack Semiconductor Solutions for Smart, Secure Industry and Digital Energy",
    "url": "https://www.eetimes.com/full-stack-semiconductor-solutions-for-industry-and-digital-energy-applications/",
    "source": "NSING Technologies Pte. Ltd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T14:00:00+00:00",
    "summary": "NSING Technologies, a Singapore-founded semiconductor company, delivers full-stack chip solutions for industrial automation, AI data centers, and digital energy.The N32-series MCUs (144–600 MHz, Corte"
  },
  {
    "id": "hn:49773511",
    "domain": "AI 算力 / 半导体",
    "title": "Every Nvidia GPU has 10 to 30 RISC-V cores inside it",
    "url": "https://www.xda-developers.com/your-nvidia-gpu-dozens-risc-v-cores-one-took-over-graphics-driver/",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-09-20T07:50:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/huaweis-tau-law-takes-commercial-form/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei’s Tau Law Takes Commercial Form",
    "url": "https://www.eetimes.com/huaweis-tau-law-takes-commercial-form/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:18:57+00:00",
    "summary": "Kirin 9050 Pro rests on the Tau (τ) Scaling Law, marking a major change in chip architecture designed to bypass EUV lithography limits. The post Huawei’s Tau Law Takes Commercial Form appeared first o"
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
    "id": "hn:49346906",
    "domain": "AI 算力 / 半导体",
    "title": "Ask HN: Do you feel comfortable admitting that you use AI?",
    "url": "https://news.ycombinator.com/item?id=49346906",
    "source": "var0xyz",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T15:16:15+00:00",
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
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 885,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 613,
    "published_at": "2026-09-25T18:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 607,
    "published_at": "2026-09-08T14:55:45+00:00",
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
    "id": "hn:49859982",
    "domain": "大厂 AI 动态",
    "title": "Faster prompt lookup drafting in llama.cpp",
    "url": "https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/",
    "source": "pptadversary",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-09-26T19:57:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49697014",
    "domain": "大厂 AI 动态",
    "title": "Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama",
    "url": "https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/",
    "source": "0o_MrPatrick_o0",
    "platform": "hackernews",
    "points": 140,
    "published_at": "2026-09-14T13:59:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829472",
    "domain": "大厂 AI 动态",
    "title": "Fourier Analysis: Drawing Llamas with Circles",
    "url": "https://adekau.github.io/posts/2020/llamas.html",
    "source": "cebert",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-09-24T12:03:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49740330",
    "domain": "大厂 AI 动态",
    "title": "I had Gemini train its own replacement for $9",
    "url": "https://www.petervijeh.com/projects/reddit-ner",
    "source": "p-s-v",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-09-17T13:17:16+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1002505/sam-altman-openai-ipo-devday-ai-safety",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman says OpenAI won’t go public until its models are safe",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1002505/sam-altman-openai-ipo-devday-ai-safety",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T00:19:13+00:00",
    "summary": "For months, people have wondered when OpenAI will go public. CEO Sam Altman says it won't happen until the company can make better promises about model safety, with no firm timeline in sight. \"We inte"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1002468/trump-ai-superintelligence-executive-order-ai",
    "domain": "大厂 AI 动态",
    "title": "Trump orders US government to call AI ‘Super Intelligence’",
    "url": "https://www.theverge.com/policy/1002468/trump-ai-superintelligence-executive-order-ai",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T22:25:45+00:00",
    "summary": "The US executive branch is no longer acknowledging the existence of \"artificial intelligence.\" Going forward, official policy websites, policy documents, and press releases will refer only to \"Super I"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1002173/bmws-revamped-i3-boasts-up-to-468-miles-of-range",
    "domain": "大厂 AI 动态",
    "title": "BMW’s revamped i3 boasts up to 468 miles of range",
    "url": "https://www.theverge.com/transportation/1002173/bmws-revamped-i3-boasts-up-to-468-miles-of-range",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T22:01:00+00:00",
    "summary": "When BMW first announced it was reimagining the i3 as an all-electric four-door sedan built on its Neue Klasse platform, it left out a lot of important details, like battery capacity, range, and price"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1002410/shinyhunters-hacking-suspect-arrested",
    "domain": "大厂 AI 动态",
    "title": "Suspected ShinyHunters leader arrested in the Netherlands",
    "url": "https://www.theverge.com/tech/1002410/shinyhunters-hacking-suspect-arrested",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T21:50:31+00:00",
    "summary": "Dutch police say they arrested a 24-year-old Amsterdam man in connection with ShinyHunters, the hacking group that claimed responsibility for high-profile attacks on Ticketmaster, Rockstar Games, and "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1002448/elon-musk-grokipedia-ai-updating-again",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk&#8217;s AI-powered Grokipedia is updating again",
    "url": "https://www.theverge.com/tech/1002448/elon-musk-grokipedia-ai-updating-again",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T21:49:09+00:00",
    "summary": "Grokipedia, the AI-powered online encyclopedia from SpaceXAI, appears to be updating articles once again after a months-long pause. In August, Lawfare reported that articles on Grokipedia hadn't revie"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1002238/openai-google-anthropic-ai-researchers-safety-interviews",
    "domain": "大厂 AI 动态",
    "title": "AI researchers put out videos saying superintelligence is ‘exactly as dangerous as it sounds’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1002238/openai-google-anthropic-ai-researchers-safety-interviews",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:35:03+00:00",
    "summary": "\"The chance of human extinction is about a coin flip, in my view,\" Geoffrey Irving, a former OpenAI and Google DeepMind employee, said in a new interview. It's one of a dozen interviews with AI resear"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1002087/razer-deathstalker-v2-pro-tkl-witcher-3-remastered-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Razer’s low-latency wireless gaming keyboard is almost half off",
    "url": "https://www.theverge.com/gadgets/1002087/razer-deathstalker-v2-pro-tkl-witcher-3-remastered-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:19:07+00:00",
    "summary": "Woot has the Razer DeathStalker V2 Pro TKL on sale for $130, a significant discount from its usual $219.99 price point. This keyboard is built for competitive gaming, with a low latency 2.4GHz wireles"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches Dots, its Muse competitor",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:15:00+00:00",
    "summary": "OpenAI is responding to Meta's buzzy Muse AI with agentic helpers of its own: Dots. During its DevDay keynote on Tuesday, OpenAI announced that Dots will serve as always-on AI assistants that can \"do "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1002201/openai-sam-altman-openai-devday-protests-ice-data-centers",
    "domain": "大厂 AI 动态",
    "title": "Protesters gather at OpenAI’s DevDay",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1002201/openai-sam-altman-openai-devday-protests-ice-data-centers",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:12:27+00:00",
    "summary": "On Tuesday, OpenAI's annual DevDay event began with protests, flyers, and chants. \"Sam Altman, get off it, put people over profit,\" said a group of protesters marching in a circle in front of a series"
  },
  {
    "id": "rss:https://www.theverge.com/news/1002099/xbox-mythic-achievement-announcement-feature",
    "domain": "大厂 AI 动态",
    "title": "Xbox’s Mythic Achievements are here and they&#8217;re just like PlayStation Platinum trophies",
    "url": "https://www.theverge.com/news/1002099/xbox-mythic-achievement-announcement-feature",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T16:17:01+00:00",
    "summary": "Microsoft is officially announcing its new Xbox Mythic Achievements today, and they're already available for Xbox Insiders to test. Mythic Achievements work a lot like Sony's PlayStation Platinum trop"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/apple-pay-set-to-launch-in-india-with-axis-bank-today-sources-say/",
    "domain": "大厂 AI 动态",
    "title": "Apple Pay finally launches in India after years on the sidelines",
    "url": "https://techcrunch.com/2026/09/29/apple-pay-set-to-launch-in-india-with-axis-bank-today-sources-say/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:08:00+00:00",
    "summary": "Some of India's largest banks are holding off on supporting Apple Pay initially."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/america-gov-gets-really-weird-when-you-ask-it-about-minecraft-but-its-not-a-glitch/",
    "domain": "大厂 AI 动态",
    "title": "America.gov gets really weird when you ask it about Minecraft, but it’s not a glitch",
    "url": "https://techcrunch.com/2026/09/29/america-gov-gets-really-weird-when-you-ask-it-about-minecraft-but-its-not-a-glitch/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T23:30:55+00:00",
    "summary": "For the sake of national security, it's a relief to learn that America.gov is not hallucinating to the point that it's penning lengthy poetry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/the-internet-is-convinced-elon-musks-xai-trolled-openais-dots-launch/",
    "domain": "大厂 AI 动态",
    "title": "The internet is convinced Elon Musk’s xAI trolled OpenAI’s ‘Dots’ launch",
    "url": "https://techcrunch.com/2026/09/29/the-internet-is-convinced-elon-musks-xai-trolled-openais-dots-launch/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T22:20:59+00:00",
    "summary": "Before OpenAI launched its new AI agent, Dots, on Tuesday, Elon Musk's xAI had already acquired the domain name \"dot.com,\" which now redirects to the Grok chatbot download page."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/your-car-and-its-mobile-app-are-probably-handing-over-all-kinds-of-data-to-tech-companies/",
    "domain": "大厂 AI 动态",
    "title": "Your car and its mobile app are probably handing over all kinds of data to tech companies",
    "url": "https://techcrunch.com/2026/09/29/your-car-and-its-mobile-app-are-probably-handing-over-all-kinds-of-data-to-tech-companies/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T22:18:35+00:00",
    "summary": "Researchers at Northeastern University found vehicles and their companion apps regularly shared detailed data with some of the largest tech companies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/a16z-backed-eliseai-raises-350m-doubles-valuation-to-4b/",
    "domain": "大厂 AI 动态",
    "title": "a16z-backed EliseAI raises $350M, doubles valuation to $4B",
    "url": "https://techcrunch.com/2026/09/29/a16z-backed-eliseai-raises-350m-doubles-valuation-to-4b/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T21:51:36+00:00",
    "summary": "EliseAI raises $350M, doubles valuation in a year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/tesla-secures-30b-in-new-credit-lines-as-it-looks-to-scale-cybercab-optimus/",
    "domain": "大厂 AI 动态",
    "title": "Tesla secures $30B in new credit lines as it looks to scale Cybercab, Optimus",
    "url": "https://techcrunch.com/2026/09/29/tesla-secures-30b-in-new-credit-lines-as-it-looks-to-scale-cybercab-optimus/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T21:20:12+00:00",
    "summary": "The company says it won't draw on the new debt facilities this year, as it has already planned at least $25 billion in capital expenditures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/openais-latest-features-take-direct-aim-at-the-app-store-model/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s latest features take direct aim at the app store model",
    "url": "https://techcrunch.com/2026/09/29/openais-latest-features-take-direct-aim-at-the-app-store-model/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T20:15:47+00:00",
    "summary": "OpenAI is building out the pieces of an alternative to the traditional app store model, turning ChatGPT into a place where software can be discovered and used by people and AI agents alike."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/openai-reportedly-in-talks-to-raise-30b-round-at-1-4t-valuation/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI reportedly in talks to raise $30B round at $1.4T valuation",
    "url": "https://techcrunch.com/2026/09/29/openai-reportedly-in-talks-to-raise-30b-round-at-1-4t-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T19:52:37+00:00",
    "summary": "The new round is anticipated to be the company's last before its delayed 2027 public debut."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/more-ways-to-disrupt-new-2026-side-events-from-kotra-wayfounder-enterprise-ireland-safetywing-descope/",
    "domain": "大厂 AI 动态",
    "title": "More Ways to Disrupt: New 2026 Side Events from KOTRA, WayFounder, Enterprise Ireland, SafetyWing + Descope",
    "url": "https://techcrunch.com/2026/09/29/more-ways-to-disrupt-new-2026-side-events-from-kotra-wayfounder-enterprise-ireland-safetywing-descope/",
    "source": "Jean Bradley, TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T18:48:03+00:00",
    "summary": "Disrupt doesn’t end when you leave Moscone West. 👀 Founder dinners, investor meetups, happy hours, workshops, roundtables and more are taking over San Francisco during Disrupt Week. See what’s happeni"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/heres-why-openai-is-absent-from-nvidias-industry-wide-effort-to-end-rogue-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Here’s why OpenAI is absent from Nvidia’s industry-wide effort to end rogue AI agents",
    "url": "https://techcrunch.com/2026/09/29/heres-why-openai-is-absent-from-nvidias-industry-wide-effort-to-end-rogue-ai-agents/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T18:35:00+00:00",
    "summary": "OpenAI isn't a public supporter of Nvidia's Open Agent Safety Platform, but it is privately working with Nvidia, TechCrunch has learned."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/openai-takes-on-microsoft-with-the-launch-of-what-feels-a-whole-lot-like-chatgpts-own-office-suite/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI takes on Microsoft with the launch of what feels a whole lot like ChatGPT’s own office suite",
    "url": "https://techcrunch.com/2026/09/29/openai-takes-on-microsoft-with-the-launch-of-what-feels-a-whole-lot-like-chatgpts-own-office-suite/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:45:51+00:00",
    "summary": "OpenAI's newly announced suite of office features puts it into more direct competition with more traditional software companies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/dutch-police-arrest-shinyhunters-hacker-accused-of-planning-two-murders/",
    "domain": "大厂 AI 动态",
    "title": "Dutch police arrest ShinyHunters hacker accused of planning two murders",
    "url": "https://techcrunch.com/2026/09/29/dutch-police-arrest-shinyhunters-hacker-accused-of-planning-two-murders/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:27:09+00:00",
    "summary": "Dutch police said the hacker, arrested for being part of the ShinyHunters cybercriminal gang, had plans to organize the murder of two people on his laptop."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/ai-powered-app-maker-wabi-pivots-to-a-messaging-experience/",
    "domain": "大厂 AI 动态",
    "title": "AI-powered app maker Wabi pivots to a messaging experience",
    "url": "https://techcrunch.com/2026/09/29/ai-powered-app-maker-wabi-pivots-to-a-messaging-experience/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:20:00+00:00",
    "summary": "Wabi is repositioning its prompt-based app builder as a personal AI agent that can create interfaces on demand, combining chat, apps, and ongoing tasks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches Dots, its bubbly agentic avatar",
    "url": "https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:17:15+00:00",
    "summary": "Dots are meant to operate independent of any specific hardware or interface, pursuing user-defined goals continuously in the background with minimal oversight."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/openai-gives-codex-reusable-cloud-environments-that-work-across-devices/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI gives Codex reusable cloud environments that work across devices",
    "url": "https://techcrunch.com/2026/09/29/openai-gives-codex-reusable-cloud-environments-that-work-across-devices/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:15:00+00:00",
    "summary": "OpenAI is expanding Codex with reusable cloud development environments, a revamped CLI with voice controls, new code review tools, and a security-focused product for scanning repositories and preparin"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/openai-launches-gpt-6-1-sol-says-it-nearly-matches-gpt-6-astra-and-costs-less/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches GPT-6.1 Sol, says it nearly matches GPT-6 Astra and costs less",
    "url": "https://techcrunch.com/2026/09/29/openai-launches-gpt-6-1-sol-says-it-nearly-matches-gpt-6-astra-and-costs-less/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:15:00+00:00",
    "summary": "OpenAI says GPT-6.1 Sol delivers significant improvements over GPT-6 Sol across complex professional tasks, including code writing and debugging, document understanding, and executing multistep busine"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/openai-expands-chatgpts-plugins-with-app-like-interfaces-and-automations/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI expands ChatGPT’s plug-ins with app-like interfaces and automations",
    "url": "https://techcrunch.com/2026/09/29/openai-expands-chatgpts-plugins-with-app-like-interfaces-and-automations/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T17:15:00+00:00",
    "summary": "OpenAI is expanding ChatGPT plug-ins with dedicated sidebar homes, interactive panels, file viewers, improved discovery, and support for automations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/can-a-chatbot-fix-the-government-maze-the-white-house-is-about-to-find-out/",
    "domain": "大厂 AI 动态",
    "title": "Can a chatbot fix the government maze? The White House is about to find out",
    "url": "https://techcrunch.com/2026/09/29/can-a-chatbot-fix-the-government-maze-the-white-house-is-about-to-find-out/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T16:55:56+00:00",
    "summary": "America.gov is intended to simplify the process of navigating government bureaucracy, but large language models are imperfect and remain prone to hallucinations, which could cause new issues."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/instinct-founder-said-more-than-50-of-transactions-on-the-platform-are-travel-related/",
    "domain": "大厂 AI 动态",
    "title": "Instinct founder said more than 50% of transactions on the platform are travel-related",
    "url": "https://techcrunch.com/2026/09/29/instinct-founder-said-more-than-50-of-transactions-on-the-platform-are-travel-related/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T15:12:07+00:00",
    "summary": "Instinct founder said the platform is growing 10% day by day, with transaction volume increasing at a similar rate."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/after-losing-his-voice-to-cancer-this-founder-is-building-glasses-for-voice/",
    "domain": "大厂 AI 动态",
    "title": "After losing his voice to cancer, this founder is building ‘glasses for voice’",
    "url": "https://techcrunch.com/2026/09/29/after-losing-his-voice-to-cancer-this-founder-is-building-glasses-for-voice/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T15:00:00+00:00",
    "summary": "Uhura Bionics, part of the Startup Battlefield 200 at TechCrunch Disrupt, wants to replace flat, robotics voice devices with one that carries emotions."
  },
  {
    "id": "rss:https://stratechery.com/2026/one-more-note-on-agents-meta-connect-meta-enterprise-platform/",
    "domain": "大厂 AI 动态",
    "title": "One More Note on Agents, Meta Connect, Meta Enterprise Platform",
    "url": "https://stratechery.com/2026/one-more-note-on-agents-meta-connect-meta-enterprise-platform/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T10:00:00+00:00",
    "summary": "Meta has the chance to own the consumer agentic space; going for enterprise is a big mistake."
  },
  {
    "id": "rss:https://stratechery.com/2026/apps-agents-and-aggregation/",
    "domain": "大厂 AI 动态",
    "title": "Apps, Agents, and Aggregation",
    "url": "https://stratechery.com/2026/apps-agents-and-aggregation/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T10:25:37+00:00",
    "summary": "Agents are the ultimate Aggregators; they reveal apps as a means, not an ends, and providing them is tech's biggest prize."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/most-powerful-obesity-drug-yet-people-lost-up-to-25-of-weight-in-trial/",
    "domain": "大厂 AI 动态",
    "title": "Most powerful obesity drug yet: People lost up to 25% of weight in trial",
    "url": "https://arstechnica.com/health/2026/09/most-powerful-obesity-drug-yet-people-lost-up-to-25-of-weight-in-trial/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T22:30:37+00:00",
    "summary": "Retatrutide is a triple-hormone obesity drug simulating GLP-1, GIP, and glucagon."
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
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
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-09-08T14:54:57+00:00",
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
    "id": "hn:49816810",
    "domain": "股票",
    "title": "Trump's 1,156 July Stock Trades Involved AI, Big Oil, Weapons-Makers, and More",
    "url": "https://www.commondreams.org/news/donald-trump-stock-trades",
    "source": "cirelli94",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-23T14:33:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49819274",
    "domain": "股票",
    "title": "Morgan Stanley Investment-Bank Deal List Leaked in Email Misfire",
    "url": "https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-investment-bank-deal-124657863.html",
    "source": "wslh",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-09-23T17:08:35+00:00",
    "summary": ""
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
    "id": "hn:49796292",
    "domain": "股票",
    "title": "Smart Ring Maker Oura, Backers Seek $2.2B in US IPO",
    "url": "https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-09-22T02:53:48+00:00",
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 561,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 324,
    "published_at": "2026-09-28T10:30:54+00:00",
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
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 255,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 219,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49904408",
    "domain": "金融",
    "title": "Tesla takes on $30B in credit as it approaches unprofitability",
    "url": "https://electrek.co/2026/09/29/tesla-takes-on-30-billion-in-credit-as-it-approaches-unprofitability/",
    "source": "ciconia",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-30T04:37:37+00:00",
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
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.36177",
    "domain": "金融",
    "title": "A tale of two allocations: Risk capital contributions versus risk contributions in the tail",
    "url": "https://arxiv.org/abs/2609.36177",
    "source": "Nawaf Mohammed, Edward Furman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.36177v1 Announce Type: new Abstract: We compare two natural proportional notions of a risk component's contribution to the aggregate tail risk of a collection of risks: the fraction of aggr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.36257",
    "domain": "金融",
    "title": "When Hedging Changes the Payoff: Option Replication with Price Impact and Execution Costs",
    "url": "https://arxiv.org/abs/2609.36257",
    "source": "David Itkin, Leandro S\\'anchez-Betancourt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.36257v1 Announce Type: new Abstract: Hedging a derivative by trading the underlying asset changes the payoff that the hedging intended to replicate. We study this phenomenon when trading ge"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.36349",
    "domain": "金融",
    "title": "Ranking the wrong places: vulnerability assessment, flood losses and risk sharing in Italy and Europe",
    "url": "https://arxiv.org/abs/2609.36349",
    "source": "Stefano Blando",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.36349v1 Announce Type: new Abstract: Before a flood, governments decide where to invest in protection; after it, how much of the loss to compensate. The European Union informs the first dec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.36405",
    "domain": "金融",
    "title": "Finite-Horizon Reversible Investment under Multi-Factor Dynamics",
    "url": "https://arxiv.org/abs/2609.36405",
    "source": "Junkee Jeon, Takwon Kim, Jinwan Park, A. Max Reppen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.36405v1 Announce Type: new Abstract: We study a finite-horizon reversible investment problem in which a risk-neutral firm adjusts capacity at a proportional purchase cost and a lower salvag"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.36631",
    "domain": "金融",
    "title": "A Spread-Gated Hawkes-Flocking Model for Best Bid and Ask Dynamics, with an Application to Limit Order Placement",
    "url": "https://arxiv.org/abs/2609.36631",
    "source": "Hyoeun Lee, Kiseop Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.36631v1 Announce Type: new Abstract: We study the joint dynamics of the best bid and ask prices with a spread-gated Hawkes-flocking model. The model tracks four types of best-quote movement"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37051",
    "domain": "金融",
    "title": "Beyond the Coast: an Empirical Assessment of the Kaldor-Verdoorn Law in Chinese Provinces",
    "url": "https://arxiv.org/abs/2609.37051",
    "source": "Maria Cristina Barbieri G\\'oes, Saverio Barabuffi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37051v1 Announce Type: new Abstract: This paper investigates spatial productivity convergence across Chinese provinces during structural transformation, examining how a shift in auonomous d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37108",
    "domain": "金融",
    "title": "The Efficient Frontier from a LASSO Solver",
    "url": "https://arxiv.org/abs/2609.37108",
    "source": "Thomas Schmelzer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37108v1 Announce Type: new Abstract: In a recent paper, Schmelzer and Hastie argue that Markowitz's Critical Line Algorithm and the LASSO path trace the same curve. Here we use that identit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37343",
    "domain": "金融",
    "title": "Classification as Search Infrastructure: How Category Creation, Addition and Cleanup Shape Knowledge Retrieval",
    "url": "https://arxiv.org/abs/2609.37343",
    "source": "Kerstin H\\\"otte, Nicol\\`o Barbieri, Su Jung Jee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37343v1 Announce Type: new Abstract: Classification systems shape how searchers find relevant objects. We study how revisions to classification architecture affect retrieval by changing the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37741",
    "domain": "金融",
    "title": "Dyson-Schwinger Effective-Action Methods for Rough Volatility: A Correlation-Response Architecture for Calibration, Exotics and Risk",
    "url": "https://arxiv.org/abs/2609.37741",
    "source": "Fr\\'ed\\'eric Pauquay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37741v1 Announce Type: new Abstract: We develop a non-perturbative framework for stochastic-volatility option pricing organised by the two-particle-irreducible (2PI) effective action and th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37820",
    "domain": "金融",
    "title": "Information Games: Strategic Crowding and Firm Repositioning in Language-Model Space",
    "url": "https://arxiv.org/abs/2609.37820",
    "source": "Marcus Gawronsky, Chun-Sung Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37820v1 Announce Type: new Abstract: Firms follow changing economic opportunities, but rivalry changes their response. We develop ESCAPE, a rational-share game of distribution-valued positi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37872",
    "domain": "金融",
    "title": "A Generalized Langevin Model of Latent Liquidity and Concave Price Impact",
    "url": "https://arxiv.org/abs/2609.37872",
    "source": "Andrey Itkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37872v1 Announce Type: new Abstract: We model market impact as the response to submitted order flow net of counterflow from latent traders, activated when price displacements from the level"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37881",
    "domain": "金融",
    "title": "Global Structure and Local Specifications in Sublinear Valuation",
    "url": "https://arxiv.org/abs/2609.37881",
    "source": "Jongjin Park, David Criens, Hyungbin Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37881v1 Announce Type: new Abstract: This work studies the relationships among sublinear valuation rules, uncertainty structures, and local specifications in a time-homogeneous Markovian fr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37903",
    "domain": "金融",
    "title": "From Intraday Orderbook to Imbalance Price: Understanding Cross-Market Interaction",
    "url": "https://arxiv.org/abs/2609.37903",
    "source": "Runyao Yu, Jochen L. Cremer, Pierre Pinson, Jalal Kazempour, Leo Semmelmann, Takuji Matsumoto, Derek W. Bunn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37903v1 Announce Type: new Abstract: Power systems with increasing variable renewable generation face greater uncertainty in scheduling and balancing. Intraday and balancing electricity mar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37963",
    "domain": "金融",
    "title": "Not All LPs Are Equal: The Active-Passive Gap in Automated Market Maker Liquidity Provision",
    "url": "https://arxiv.org/abs/2609.37963",
    "source": "Agathe Sadeghi, Dingyue Liu, Ciamac Moallemi, Xin Wan, Brian Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37963v1 Announce Type: new Abstract: Liquidity provision in automated market makers is typically analyzed at the pool level, implicitly assuming LP homogeneity. This aggregate view can hide"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.35923",
    "domain": "金融",
    "title": "Transpose-odd operator chirality in co-moving multiplicative processes: exact tail-level structure and a detectability obstruction",
    "url": "https://arxiv.org/abs/2609.35923",
    "source": "Nihat \\c{C}a\\u{g}r{\\i} \\c{C}al{\\i}\\c{s}kan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.35923v1 Announce Type: cross Abstract: We ask whether transposition changes the stationary heavy tail of the co-moving recursion $\\mathbf x_{t+1}=Q_tBQ_t^\\top\\mathbf x_t+Q_t\\boldsymbol\\eta_"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.36061",
    "domain": "金融",
    "title": "Introducing the CZAR Loss: A Tailored Objective Function for Financial Log-Return Predictions",
    "url": "https://arxiv.org/abs/2609.36061",
    "source": "Joel Pfeffer (Allora Foundation), J. M. Diederik Kruijssen (Allora Foundation), Florian Stecker (Allora Foundation), Steven N. Longmore (Allora Foundation, LJMU)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.36061v1 Announce Type: cross Abstract: In quantitative finance, standard regression losses are misaligned with the economics of return prediction. As the conditional mean of financial log-r"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.37957",
    "domain": "金融",
    "title": "Multiscale Reconstruction of Weighted Networks from Coarse-Grained Data",
    "url": "https://arxiv.org/abs/2609.37957",
    "source": "Mattia Marzi, Frank P. Pijpers, Diego Garlaschelli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2609.37957v1 Announce Type: cross Abstract: Network reconstruction from partial information is usually performed at the same resolution level at which constraints are observable. This becomes pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.14839",
    "domain": "金融",
    "title": "Multi-Task Dynamic Pricing in Credit Market with Contextual Information",
    "url": "https://arxiv.org/abs/2410.14839",
    "source": "Adel Javanmard, Jingwei Ji, Renyuan Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2410.14839v5 Announce Type: replace Abstract: We study the dynamic pricing problem faced by a broker seeking to learn prices for a large number of credit market securities, such as corporate bon"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.16162",
    "domain": "金融",
    "title": "Two Margins of Climate Cooperation: Emissions and Coalition Membership under Tipping",
    "url": "https://arxiv.org/abs/2506.16162",
    "source": "Yongyang Cai, Yaofeng Cui, Hongbo Duan, Lei Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2506.16162v2 Announce Type: replace Abstract: We study climate coalition stability with endogenous temperature and stochastic tipping. In our dynamic game, rising temperature widens the emission"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.03916",
    "domain": "金融",
    "title": "Delegation or competition: optimal liquidation across dark and lit pools with information privilege",
    "url": "https://arxiv.org/abs/2509.03916",
    "source": "Thibaut Mastrolia, Hao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2509.03916v2 Announce Type: replace Abstract: We study the optimal liquidation problem in both dark and lit pools for an investor delegating the execution of a large position to a broker, in a c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.17121",
    "domain": "金融",
    "title": "New Demand Economics: Education, Demand Upgrading, and Structural Change",
    "url": "https://arxiv.org/abs/2510.17121",
    "source": "Fenghua Wen, Xieyu Yin, Chufu Wen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2510.17121v2 Announce Type: replace Abstract: Education can change what households buy as well as what workers produce. We study this demand channel in a two-sector growth model. Education shift"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.17954",
    "domain": "金融",
    "title": "A multi-view contrastive learning framework for spatial embeddings in risk modelling",
    "url": "https://arxiv.org/abs/2511.17954",
    "source": "Freek Holvoet, Christopher Blier-Wong, Katrien Antonio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2511.17954v3 Announce Type: replace Abstract: Incorporating spatial information, particularly when related to climate, weather, and demographic factors, is crucial for improving underwriting pre"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.19469",
    "domain": "金融",
    "title": "Big Wins, Small Net Gains: Direct and Spillover Effects of First Industry Entries in Puerto Rico",
    "url": "https://arxiv.org/abs/2511.19469",
    "source": "Jorge A. Arroyo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2511.19469v3 Announce Type: replace Abstract: I study how first sizable industry entries reshape local and neighboring labor markets in Puerto Rico. Using over a decade of quarterly municipality"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.05290",
    "domain": "金融",
    "title": "Multi-Period Martingale Optimal Transport: Classical Theory, Neural Acceleration, and Financial Applications",
    "url": "https://arxiv.org/abs/2601.05290",
    "source": "Sri Sairam Gautam B",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T04:00:00+00:00",
    "summary": "arXiv:2601.05290v3 Announce Type: replace Abstract: This paper develops a computational framework for Multi-Period Martingale Optimal Transport (MMOT), addressing convergence rates, algorithmic effici"
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
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T17:11:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-09-24T08:54:57+00:00",
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
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-08T16:54:03+00:00",
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
    "id": "hn:49762617",
    "domain": "金融",
    "title": "Elon Musk and Tesla Forged a New EV Path",
    "url": "https://spectrum.ieee.org/elon-musk-tesla",
    "source": "vinhnx",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-09-19T02:08:54+00:00",
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
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
    "summary": ""
  }
]
```
