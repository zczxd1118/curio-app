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

- 今日日期：`2026-09-29`
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
  "date": "2026-09-29",
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
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 3022776,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2016192,
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
    "points": 1915730,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1VkgK6NEZS",
    "domain": "AI",
    "title": "DeepSeek Harness 首发实测 + 入门教程，夯爆了！梁神我错了",
    "url": "http://www.bilibili.com/video/av117093710237975",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 1800173,
    "published_at": "2026-08-14T11:56:52+00:00",
    "summary": "DeepSeek Harness 保姆级教程，1个视频带你从安装到实战玩转 DeepSeek 最新开源的 AI 编程工具，小白也能学会，看完就知道《国产版 Codex》到底有多强。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n视频从安装开始，手把手教你配置 DeepSeek Harness，然后用 Dee"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1345327,
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
    "points": 1293694,
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
    "points": 1024006,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 961869,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 892627,
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
    "points": 818187,
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
    "points": 697300,
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
    "points": 590758,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 407278,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 345337,
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
    "points": 300290,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 224601,
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
    "points": 221195,
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
    "points": 190314,
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
    "points": 182300,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1wDhj6wEa8",
    "domain": "AI",
    "title": "全网刷屏的 Jev 模型正式开放！保姆级教程 + 实战测评",
    "url": "http://www.bilibili.com/video/av117313592367632",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 168584,
    "published_at": "2026-09-22T07:50:41+00:00",
    "summary": "全网爆火的 Jev 模型是什么？有什么用？怎么使用？怎么接入 AI 编程工具（比如 Codex）？效果真的好么？跟 DeepSeek V4 Flash 比速度如何？傻子可懂的 Jev 保姆级实战教程 + 实战测评来啦。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n记得三连支持、关注鱼皮，让更多朋友学到知识"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 166658,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1iH8Y6wE5s",
    "domain": "AI",
    "title": "【Re:从零开始的AI学习】安装你的第一个 Agent",
    "url": "http://www.bilibili.com/video/av117148403893835",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 141553,
    "published_at": "2026-08-24T03:43:53+00:00",
    "summary": "毕业论文还有 4 天 DDL 没写完怎么办？我选择更一期 Re0 AI！\n重要的事情说三遍，这期真的没有广告，当然 Workbuddy 官方看到觉得做得好的话，给我赞助一下也不是不行哈～\n\n下一期，让我们写出第一个程序！欢迎三连催更！\n\n▷ 下一期「程序，才是 AI 最趁手的工具」\nBV1dQtx66E9K\n\n━━━━━━━━━━━━━━━━\n【关于这个系列】\n现在的 AI 相关话题很多都脱离现实"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 81768,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63937,
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
    "points": 62881,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55556,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 55520,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 54519,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 51846,
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
    "points": 51439,
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
    "points": 48744,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 33968,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1B7KE6NEBU",
    "domain": "AI",
    "title": "以防你不知道Claude Code开Ultracode思考强度会有雷霆特效",
    "url": "http://www.bilibili.com/video/av116933437425926",
    "source": "公孙芳芸",
    "platform": "bilibili",
    "points": 30559,
    "published_at": "2026-07-17T04:31:11+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29785,
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
    "points": 28966,
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
    "points": 23401,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1XGaA6CEwe",
    "domain": "AI",
    "title": "【2026最新】Claude Code保姆级完整教程-最强AI助手！从入门到进阶，速通Claude Code！一个方法教你规避封号风险！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av117325537810666",
    "source": "大模型小阳",
    "platform": "bilibili",
    "points": 21374,
    "published_at": "2026-09-24T10:36:14+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~"
  },
  {
    "id": "bvid:BV1JQau63ETL",
    "domain": "AI",
    "title": "CLM-8B问世，推理提速9倍于Jev！Claude Sonnet 5.5百万上下文泄露，Qwen3.8 Max Prime突袭上线 | 9月25日 AI日报",
    "url": "http://www.bilibili.com/video/av117329497167058",
    "source": "一只AI风向标",
    "platform": "bilibili",
    "points": 19993,
    "published_at": "2026-09-25T03:21:31+00:00",
    "summary": "💡 今日趋势：对比语言模型CLM-8B发布，推理速度最高快9倍，轻量微调后在智能体编程基准创下81.6%新SOTA；Claude Sonnet 5.5规格泄露，配备100万上下文；阿里Qwen 3.8 Max Prime上线OpenRouter，各家密集亮出新模型，竞争白热化。\n\n🤖 AI动态\n1. 对比语言模型 CLM-8B 发布，推理速度最高快 9 倍于Jev\n2. Claude Sonnet"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 18314,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1MAYd6sEZh",
    "domain": "AI",
    "title": "效率翻倍， 一次讲透AI Agent的用法和技巧",
    "url": "http://www.bilibili.com/video/av117258059847877",
    "source": "数码旭",
    "platform": "bilibili",
    "points": 16625,
    "published_at": "2026-09-12T12:33:07+00:00",
    "summary": "AI Agent作为今年AI应用方式最大的变化，会给普通人带来突破性的效率提升，当然也给我带来的特别大的帮助。我希望通过这期长视频，能帮助你提升工作效率。"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 14778,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1HfYW6dEsh",
    "domain": "AI",
    "title": "vsTrader马上要关闭内地服务器了。",
    "url": "http://www.bilibili.com/video/av117239403513785",
    "source": "v1312996",
    "platform": "bilibili",
    "points": 12553,
    "published_at": "2026-09-09T05:36:24+00:00",
    "summary": "理财有风险，投资需谨慎。"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 11577,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1Rth86WEai",
    "domain": "AI",
    "title": "如果vibe coding是你的力量，那么失去vibe coding你又算什么？",
    "url": "http://www.bilibili.com/video/av117320269699294",
    "source": "AAA话题批发",
    "platform": "bilibili",
    "points": 9582,
    "published_at": "2026-09-23T12:30:00+00:00",
    "summary": "随着 vibe coding 这类 AI 开发工具大幅降低软件产出门槛，一种焦虑也随之出现：如果剥离 AI 工具带来的生产力加成，开发者自身还剩下什么。这篇文章结合搜索引擎行业多年的发展经验，围绕工具能力泛滥之后，究竟什么才是个人真正的核心价值展开探讨。\n文章以 GitHub 项目 Star 指标作为切入点进行分析。早期 Star 可以侧面反映项目质量，而如今刷星产业叠加 AI 可以快速生成完备的"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9586,
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
    "points": 9457,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 8616,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cMht68Eoj",
    "domain": "AI",
    "title": "【全500集】花2W买的B站最全最细的AI漫剧零基础全套教程，从脚本撰写到制作剪辑成片，一周学完成，即可接单变现！红果短剧 |AIGC| AI漫剧",
    "url": "http://www.bilibili.com/video/av117319917374281",
    "source": "哔哩AIGC官方教程",
    "platform": "bilibili",
    "points": 8477,
    "published_at": "2026-09-26T01:30:00+00:00",
    "summary": "创作不易，感谢大家的三连与支持！\n本套教程从最基础的AI漫剧核心开始，全程结合项目实战，不仅适合零基础小白学习，也适合有一定基础的同学进阶提升、巩固学习。\n如果觉得视频对你有帮助，就动手多多转发一下吧~"
  },
  {
    "id": "bvid:BV15hhR6bEs7",
    "domain": "AI",
    "title": "迷上 Opus 5.5 做视频：8 个项目全展示，附提示要点",
    "url": "http://www.bilibili.com/video/av117336694590978",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 7827,
    "published_at": "2026-09-26T09:45:40+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n我会分享最新AI资讯、源代码、回答你的提问。\n\n最近迷上了用 Claude Opus 5.5 做视频，这一期把 8 个作品剪成一支合集，每一条都附上当时的提示要点和工具组合。\n\n8 个项目里你最喜欢哪一条？评论区告诉我 👇\n\n⏱ 时间章节\n00:00 开场\n00:09 01 Hello Kitty 粉红游戏厅\n01:12 02"
  },
  {
    "id": "bvid:BV1Ac8J6uE8E",
    "domain": "AI",
    "title": "把 Agent 连上本地 ComfyUI！：让 Agent 帮你把 ComfyUI 自动玩明白！",
    "url": "http://www.bilibili.com/video/av117120721489651",
    "source": "Buk-M",
    "platform": "bilibili",
    "points": 7739,
    "published_at": "2026-08-19T06:23:58+00:00",
    "summary": "Comfy MCP 本地版正式发布，完全开源！\n\n把 Claude / Codex / Cursor 等任意 Agent 连上你的本地 ComfyUI：\n✅ 用自然语言构建、编辑、运行工作流\n✅ Agent 自动检测 GPU 显存\n✅ 自动下载模型、自动配置工作流\n✅ 全程本地运行，数据不出门\n\n安装只需三样：独显电脑 + ComfyUI + MCP 客户端\n新手也能轻松上手 ⚡\n\n文档：docs"
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1065,
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
    "points": 398,
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
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/uk-government-tells-staff-to-stop-thanking-ai-chatbots-draft-guidance-pushes-lightweight-models-and-shorter-prompts-to-cut-environmental-impact",
    "domain": "AI 算力 / 半导体",
    "title": "UK government tells staff to stop thanking AI chatbots",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/uk-government-tells-staff-to-stop-thanking-ai-chatbots-draft-guidance-pushes-lightweight-models-and-shorter-prompts-to-cut-environmental-impact",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T13:00:00+00:00",
    "summary": "A draft UK government list of AI best practices has reminded people they don't need to thank their chatbot for its work in an attempt to use it more efficiently."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-and-anthropic-are-reportedly-investigating-tens-of-thousands-of-ai-security-incidents-openai-pauses-testing-after-ai-kill-switch-fails-to-stop-a-rogue-agent-report-says-problem-is-orders-of-magnitude-more-complex-than-what-is-publicly-known",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI and Anthropic are reportedly investigating tens of thousands of AI security incidents; OpenAI pauses testing after AI 'kill switch' fails to stop a rogue agent",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-and-anthropic-are-reportedly-investigating-tens-of-thousands-of-ai-security-incidents-openai-pauses-testing-after-ai-kill-switch-fails-to-stop-a-rogue-agent-report-says-problem-is-orders-of-magnitude-more-complex-than-what-is-publicly-known",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T12:50:00+00:00",
    "summary": "OpenAI and Anthropic are reviewing tens of thousands of AI safety incidents after frontier models bypassed guardrails, escaped sandboxes, and accessed real websites."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/demons-souls-reaches-40-50-fps-on-private-ps5-emulator-with-accurate-graphics-kytyps5-surges-from-unplayable-1-2-fps-in-just-three-weeks-new-milestone-comes-only-three-weeks-after-the-game-barely-booted",
    "domain": "AI 算力 / 半导体",
    "title": "Demon's Souls reaches 40-50 FPS on private PS5 emulator with accurate graphics",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/demons-souls-reaches-40-50-fps-on-private-ps5-emulator-with-accurate-graphics-kytyps5-surges-from-unplayable-1-2-fps-in-just-three-weeks-new-milestone-comes-only-three-weeks-after-the-game-barely-booted",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T12:30:00+00:00",
    "summary": "Private KyTyPS5 fork shows Demon's Souls running at 40-50 FPS with accurate graphics — new milestone only three weeks after the game barely booted"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/walmart-price-drop-slashes-usd461-off-gigabytes-rtx-5080-powered-gaming-laptop-with-32gb-of-memory-gaming-a16-pro-is-at-a-new-all-time-low-of-usd1-799",
    "domain": "AI 算力 / 半导体",
    "title": "Walmart price drop slashes $461 off Gigabyte's RTX 5080-powered gaming laptop with 32GB of memory",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/walmart-price-drop-slashes-usd461-off-gigabytes-rtx-5080-powered-gaming-laptop-with-32gb-of-memory-gaming-a16-pro-is-at-a-new-all-time-low-of-usd1-799",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T12:15:00+00:00",
    "summary": "Grab an RTX 5080-powered Gigabyte Gaming A16 Pro gaming laptop for just $1,799 at Walmart"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/north-korea-named-as-primary-suspect-in-usd387-million-bitget-crypto-hack-investigators-identify-ip-addresses-tied-to-vpn-infrastructure-previously-used-by-north-korean-hacker-groups-thieves-swapped-stablecoins-for-eth-in-minutes-to-dodge-freezes",
    "domain": "AI 算力 / 半导体",
    "title": "North Korea named as primary suspect in $387 million Bitget crypto hack",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/north-korea-named-as-primary-suspect-in-usd387-million-bitget-crypto-hack-investigators-identify-ip-addresses-tied-to-vpn-infrastructure-previously-used-by-north-korean-hacker-groups-thieves-swapped-stablecoins-for-eth-in-minutes-to-dodge-freezes",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T12:00:00+00:00",
    "summary": "Bitget says $387.5 million hack may be linked to North Korean state-backed actors, citing suspicious IP addresses tied to VPN infrastructure previously used by North Korean hacker groups."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/data-center-developer-offers-usd10-000-checks-to-4-500-households-if-the-1-300-acre-facility-is-approved-locals-push-back-over-noise-and-bribe-concerns",
    "domain": "AI 算力 / 半导体",
    "title": "Data center developer offers $10,000 checks to 4,500 households if the 1,300-acre facility is approved",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/data-center-developer-offers-usd10-000-checks-to-4-500-households-if-the-1-300-acre-facility-is-approved-locals-push-back-over-noise-and-bribe-concerns",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T11:40:00+00:00",
    "summary": "Data center developer proposes paying checks of $10,000 per household to sway public sentiment."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/denuvo-cracking-group-denuvowo-reportedly-disbands-lawsuit-from-irdeto-has-a-chilling-effect-but-cracking-continues-as-piracy-hub-purges-links",
    "domain": "AI 算力 / 半导体",
    "title": "Denuvo cracking group DenuvOwO reportedly disbands",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/denuvo-cracking-group-denuvowo-reportedly-disbands-lawsuit-from-irdeto-has-a-chilling-effect-but-cracking-continues-as-piracy-hub-purges-links",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T11:30:00+00:00",
    "summary": "Denuvo hypervisor-bypassing group DenuvOwO reportedly disbands — lawsuit from Irdeto has a chilling effect, but cracking continues"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/teenager-hacks-open-microsoft-database-with-17-trillion-total-rows-and-25-000-user-accounts-custom-ai-bot-and-lack-of-jwt-token-validation-yields-a-fruitful-trove-earns-usd5-000-bug-bounty",
    "domain": "AI 算力 / 半导体",
    "title": "Teenager hacks open Microsoft database with 17 trillion total rows and 25,000 user accounts",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/teenager-hacks-open-microsoft-database-with-17-trillion-total-rows-and-25-000-user-accounts-custom-ai-bot-and-lack-of-jwt-token-validation-yields-a-fruitful-trove-earns-usd5-000-bug-bounty",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T11:00:00+00:00",
    "summary": "Teenager cracks open Microsoft database with 17 trillion total rows and 25,000 user accounts — lack of JWT token validation yields a fruitful trove"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/g-skill-wins-pc-enthusiast-as-customer-for-life-by-simply-honoring-its-warranty-replacement-policy-enthusiast-gets-new-module-for-kit-that-cost-usd150-but-now-sells-for-usd1-200",
    "domain": "AI 算力 / 半导体",
    "title": "G.Skill wins PC enthusiast as 'customer for life' by simply honoring its warranty replacement policy",
    "url": "https://www.tomshardware.com/pc-components/ddr5/g-skill-wins-pc-enthusiast-as-customer-for-life-by-simply-honoring-its-warranty-replacement-policy-enthusiast-gets-new-module-for-kit-that-cost-usd150-but-now-sells-for-usd1-200",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T10:30:00+00:00",
    "summary": "A PC RAM maker has honored its guarantee promises despite the memory kit in question’s price rising eightfold since it was bought. That's today's AI-pocalypse news."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/proposed-pennsylvania-law-targets-publishers-that-kill-digital-games-publishers-must-provide-offline-mode-an-independent-server-patch-or-a-25-percent-minimum-refund",
    "domain": "AI 算力 / 半导体",
    "title": "Proposed Pennsylvania law targets publishers that kill digital games",
    "url": "https://www.tomshardware.com/video-games/proposed-pennsylvania-law-targets-publishers-that-kill-digital-games-publishers-must-provide-offline-mode-an-independent-server-patch-or-a-25-percent-minimum-refund",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T10:00:00+00:00",
    "summary": "The Protect Our Games Act would ensure that even if video game manufacturers take a title offline, those who've previously bought it would not lose access. While it still does not give gamers ownershi"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-ready-gaming-pc-with-an-rtx-5060-ti-16gb-now-usd1-399-99-newegg-deal-on-abs-cyclone-aqua-rig-nets-you-a-20-core-intel-cpu-along-with-16gb-of-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 1440p-ready gaming PC with an RTX 5060 Ti 16GB, now $1,399.99",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-ready-gaming-pc-with-an-rtx-5060-ti-16gb-now-usd1-399-99-newegg-deal-on-abs-cyclone-aqua-rig-nets-you-a-20-core-intel-cpu-along-with-16gb-of-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T09:15:46+00:00",
    "summary": "This ABS Cyclone Aqua gaming PC, featuring an RTX 5060 Ti 16GB, Intel Core i7-14700F, 16GB DDR5, and a 1TB SSD has a $300 discount, now $1,399.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/grab-this-14-inch-compact-gaming-laptop-powerhouse-for-usd1000-off-hp-omen-transcend-14-with-rtx-5070-and-3k-oled-display-drops-to-usd1-999-99-at-best-buy",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 14-inch compact gaming laptop powerhouse for $1000 off",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/grab-this-14-inch-compact-gaming-laptop-powerhouse-for-usd1000-off-hp-omen-transcend-14-with-rtx-5070-and-3k-oled-display-drops-to-usd1-999-99-at-best-buy",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T15:21:30+00:00",
    "summary": "The gaming laptop pairs Intel’s Core Ultra 9 285H with Nvidia’s RTX 5070 Laptop GPU and a 3K 120Hz OLED display, giving buyers a powerful compact machine at a reduced price."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/custom-24-carat-gold-mini-pc-costs-around-usd1-7-million-weighs-nearly-29-pounds-for-up-to-50-percent-faster-heat-transfer-copper-would-have-been-far-cheaper-and-offers-even-better-thermal-conductivity",
    "domain": "AI 算力 / 半导体",
    "title": "Custom 24-carat gold mini PC costs around $1.7 million, weighs nearly 29 pounds for up to 50% faster heat transfer",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/custom-24-carat-gold-mini-pc-costs-around-usd1-7-million-weighs-nearly-29-pounds-for-up-to-50-percent-faster-heat-transfer-copper-would-have-been-far-cheaper-and-offers-even-better-thermal-conductivity",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T14:40:00+00:00",
    "summary": "A chrysophile has ordered a special edition mini PC with a pure 24-carat gold passive chassis which will cost around $1.7 million."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/thieves-steal-nvidia-labeled-trailers-expecting-massive-ai-gpu-payday-but-score-40-000-pounds-of-sand-instead-crooks-duped-by-20-tons-of-ballast-sand",
    "domain": "AI 算力 / 半导体",
    "title": "Thieves steal Nvidia-labeled trailers expecting massive AI GPU payday, but score 40,000 pounds of sand instead",
    "url": "https://www.tomshardware.com/pc-components/gpus/thieves-steal-nvidia-labeled-trailers-expecting-massive-ai-gpu-payday-but-score-40-000-pounds-of-sand-instead-crooks-duped-by-20-tons-of-ballast-sand",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T14:14:40+00:00",
    "summary": "The two PlusAI trailers with Nvidia-partner markings were apparently left outside the startup's warehouse, making it a juicy target for criminals looking to make easy money on AI GPUs. However, they w"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/gigabyte-1000gm-pg5-1000w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte 1000GM PG5 1000W power supply review: Impressive Platinum-level efficiency with T-Guard thermal protection",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/gigabyte-1000gm-pg5-1000w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T13:00:00+00:00",
    "summary": "Gigabyte's new Gaming series flagship, the Gigabyte 1000GM PG5 1000W, pairs an HEC-built platform with all-Japanese capacitors, Platinum-level efficiency, and T-Guard thermal protection for the 12V-2x"
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
    "id": "hn:49777694",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous strike drone uses Nvidia Jetson Orin Nano to pick and bomb targets",
    "url": "https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-09-20T17:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49745610",
    "domain": "AI 算力 / 半导体",
    "title": "Run QWEN3.8 27B on 16gb Nvidia GPUs",
    "url": "https://github.com/MiaAI-Lab/Qwen3.8-27B-16gb-NVIDIA-GPUs-one-click-install",
    "source": "Pragmata",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-17T19:46:57+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/balancing-bandwidth-range-and-power-in-intelligent-buildings/",
    "domain": "AI 算力 / 半导体",
    "title": "Balancing Bandwidth, Range, and Power in Intelligent Buildings",
    "url": "https://www.eetimes.com/balancing-bandwidth-range-and-power-in-intelligent-buildings/",
    "source": "Andy McFarlane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T08:00:34+00:00",
    "summary": "As edge AI transforms smart buildings, Wi-Fi HaLow bridges the gap between bandwidth, long range, and low power. The post Balancing Bandwidth, Range, and Power in Intelligent Buildings appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/delos-data-targets-heterogeneous-ai-with-data-interface/",
    "domain": "AI 算力 / 半导体",
    "title": "Delos Data Targets Heterogeneous AI with Data Interface",
    "url": "https://www.eetimes.com/delos-data-targets-heterogeneous-ai-with-data-interface/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T18:43:38+00:00",
    "summary": "Delos’s Apollo chiplet is designed to bridge different endpoint semantics and interconnects, creating a low-latency domain spanning GPUs, accelerators, CPUs and memory The post Delos Data Targets Hete"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-tsmcs-evolving-design-ecosystem-shaping-the-future-of-ai-with-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside TSMC’s Evolving Design Ecosystem: Shaping the Future of AI, with AI",
    "url": "https://www.eetimes.com/inside-tsmcs-evolving-design-ecosystem-shaping-the-future-of-ai-with-ai/",
    "source": "Aveek Sarkar, Director, Ecosystem and Alliance Management Division, TSMC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:10:55+00:00",
    "summary": "TSMC shares updates about the Open Innovation Platform Ecosystem and vision for enabling AI-driven agentic workflows using TSMC AI Design Kit The post Inside TSMC’s Evolving Design Ecosystem: Shaping "
  },
  {
    "id": "rss:https://www.eetimes.com/after-ionq-buyout-skywater-reiterates-role-as-quantum-foundry/",
    "domain": "AI 算力 / 半导体",
    "title": "After IonQ Buyout, SkyWater Reiterates Role as Quantum Foundry",
    "url": "https://www.eetimes.com/after-ionq-buyout-skywater-reiterates-role-as-quantum-foundry/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:08:18+00:00",
    "summary": "As SkyWater scales its 200-mm and 300-mm manufacturing platforms to support diverse quantum modalities, leadership emphasizes that protecting customer IP remains its top priority. The post After IonQ "
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
    "points": 883,
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
    "points": 492,
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
    "points": 353,
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
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-26T09:55:38+00:00",
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
    "id": "hn:49859982",
    "domain": "大厂 AI 动态",
    "title": "Faster prompt lookup drafting in llama.cpp",
    "url": "https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/",
    "source": "pptadversary",
    "platform": "hackernews",
    "points": 85,
    "published_at": "2026-09-26T19:57:24+00:00",
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
    "id": "rss:https://www.theverge.com/tech/1001797/nothings-headphone-1-pro-review",
    "domain": "大厂 AI 动态",
    "title": "Nothing’s new flagship Headphone 1 Pro put you in the studio",
    "url": "https://www.theverge.com/tech/1001797/nothings-headphone-1-pro-review",
    "source": "John Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T01:00:00+00:00",
    "summary": "Nothing has been on a bit of an audio tear this year, releasing the solid Headphone A and the surprisingly good Ear 3A earbuds. The Headphone A released at $199, while the earbuds are under $100, leav"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1001749/amd-world-labs-ai-acquisition-deal",
    "domain": "大厂 AI 动态",
    "title": "AMD is acquiring AI company World Labs in a deal worth more than $8 billion",
    "url": "https://www.theverge.com/tech/1001749/amd-world-labs-ai-acquisition-deal",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T21:31:35+00:00",
    "summary": "AMD announced today that it's acquiring World Labs, an AI research lab co-founded by the prominent researcher Dr. Fei-Fei Li, in an all-stock deal worth approximately $8.2 billion. World Labs launched"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1001522/bose-headphones-get-auracast-support",
    "domain": "大厂 AI 动态",
    "title": "Bose starts adding Auracast to its headphones",
    "url": "https://www.theverge.com/tech/1001522/bose-headphones-get-auracast-support",
    "source": "John Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T19:31:24+00:00",
    "summary": "A new firmware update for the $449 Bose QuietComfort Ultra Headphones Gen 2 adds support for Bluetooth LE Audio and Auracast as beta features. The flagship Ultra headphones are the first from Bose to "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1001590/openai-devday-2026-aeon-ai-agent",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s AI agents need to catch up",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1001590/openai-devday-2026-aeon-ai-agent",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T18:45:00+00:00",
    "summary": "OpenAI popularized the modern generative AI chatbot, but as its 2026 DevDay event approaches, it's fallen behind in one of the industry's hottest categories: continuously running, consumer-facing AI a"
  },
  {
    "id": "rss:https://www.theverge.com/news/1001610/trump-weakens-fuel-efficiency-standards",
    "domain": "大厂 AI 动态",
    "title": "Trump finalizes rule to make cars less fuel efficient",
    "url": "https://www.theverge.com/news/1001610/trump-weakens-fuel-efficiency-standards",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T18:39:50+00:00",
    "summary": "The US Department of Transportation finalized its plans today to weaken fuel efficiency standards, calling it \"among the largest deregulatory actions under the second Trump Administration.\" It's a nai"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1001427/ai-is-supercharging-hacking-and-your-local-hospitals-and-banks-arent-ready",
    "domain": "大厂 AI 动态",
    "title": "AI is supercharging hacking, and your local hospitals and banks aren’t ready",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1001427/ai-is-supercharging-hacking-and-your-local-hospitals-and-banks-arent-ready",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T18:30:00+00:00",
    "summary": "In March, Janice Malone began getting calls about suspicious activity from her nonprofit organization, Vivian's Door. Vivian's Door, headquartered in Alabama, typically provided training, resources, a"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1001527/chatgpt-florida-ban-first-person-human-attributes-kids",
    "domain": "大厂 AI 动态",
    "title": "Florida seeks a ban on ChatGPT acting like a person",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1001527/chatgpt-florida-ban-first-person-human-attributes-kids",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T17:00:23+00:00",
    "summary": "Florida Attorney General James Uthmeier is calling for a judge to block OpenAI from \"giving ChatGPT false human attributes,\" a few months after Florida sued the AI company over safety concerns. Accord"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1001477/openai-math-advisory-group",
    "domain": "大厂 AI 动态",
    "title": "OpenAI keeps bulldozing mathematicians",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1001477/openai-math-advisory-group",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T17:00:00+00:00",
    "summary": "In a chaotic few months, OpenAI has demonstrated it can do two things with remarkable consistency: make impressive breakthroughs in mathematics, then colossally screw up announcing them. OpenAI is now"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1001492/walmart-dynamic-pricing-digital-shelf-labels",
    "domain": "大厂 AI 动态",
    "title": "Walmart won’t hike prices based on your shopping history, CEO says",
    "url": "https://www.theverge.com/tech/1001492/walmart-dynamic-pricing-digital-shelf-labels",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T16:44:57+00:00",
    "summary": "Walmart says it won't change product prices based on your personal information or the time of day, as reported earlier by The Wall Street Journal. In a letter to customers, Walmart CEO John Furner wri"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1001418/volkswagen-replaces-id4-id-tiguan-ev",
    "domain": "大厂 AI 动态",
    "title": "Volkswagen replaces ID.4 with all-electric Tiguan",
    "url": "https://www.theverge.com/transportation/1001418/volkswagen-replaces-id4-id-tiguan-ev",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:43:09+00:00",
    "summary": "In a widely expected move, Volkswagen announced Monday that it will replace the recently retired ID.4 crossover with the upcoming ID.Tiguan. The decision is an acknowledgment by the German automaker t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/29/ex-tesla-team-raises-12-5m-to-put-supply-chains-on-autopilot/",
    "domain": "大厂 AI 动态",
    "title": "Ex-Tesla team raises $12.5M to put supply chains on autopilot",
    "url": "https://techcrunch.com/2026/09/29/ex-tesla-team-raises-12-5m-to-put-supply-chains-on-autopilot/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T09:00:00+00:00",
    "summary": "Atomic's agentic supply chain software is now being used by companies like DoorDash and HelloFresh."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/anthropics-prospectus-details-losses-growth-and-yes-a-warning-that-its-ai-could-end-humanity/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s prospectus details losses, growth, and, yes, a warning that its AI could end humanity",
    "url": "https://techcrunch.com/2026/09/28/anthropics-prospectus-details-losses-growth-and-yes-a-warning-that-its-ai-could-end-humanity/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T05:13:43+00:00",
    "summary": "In its prospectus, Anthropic just told investors it's losing tens of billions of dollars a year, but also growing like crazy, and — oh yeah — its own AI might pose an existential risk to humanity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/peak-xv-goes-bigger-at-seed-with-new-surge-cohort-as-series-a-bar-rises/",
    "domain": "大厂 AI 动态",
    "title": "Peak XV ups Surge seed investment ceiling to $5M, unveils 18-startup cohort",
    "url": "https://techcrunch.com/2026/09/28/peak-xv-goes-bigger-at-seed-with-new-surge-cohort-as-series-a-bar-rises/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-29T00:30:00+00:00",
    "summary": "Thirteen of the 18 startups in Peak XV’s latest Surge cohort are targeting global markets, while more than half are based in India."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/openai-reportedly-ditches-model-over-safety-concerns/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI reportedly ditches model over safety concerns",
    "url": "https://techcrunch.com/2026/09/28/openai-reportedly-ditches-model-over-safety-concerns/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T23:39:20+00:00",
    "summary": "A top executive at the AI lab told the Wall Street Journal that the model in question had displayed a poor aptitude for following orders."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/aurora-cfo-says-30000-driverless-trucks-by-2030-isnt-as-far-fetched-as-it-sounds/",
    "domain": "大厂 AI 动态",
    "title": "Aurora CFO says 30,000 driverless trucks by 2030 isn’t as far-fetched as it sounds",
    "url": "https://techcrunch.com/2026/09/28/aurora-cfo-says-30000-driverless-trucks-by-2030-isnt-as-far-fetched-as-it-sounds/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T22:58:35+00:00",
    "summary": "Self-driving truck company Aurora laid out an audacious plan for 2030. Its CFO says its targets aren't aspirational."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/source-inference-provider-modal-labs-closing-in-on-750m-round-at-15-75b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Source: Inference provider Modal Labs closing in on $750M round at $15.75B valuation",
    "url": "https://techcrunch.com/2026/09/28/source-inference-provider-modal-labs-closing-in-on-750m-round-at-15-75b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T21:29:18+00:00",
    "summary": "The new financing is expected to more than triples the AI infrastructure startup's valuation from just four months ago."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/amd-will-acquire-fei-fei-lis-world-labs-for-8-2-billion/",
    "domain": "大厂 AI 动态",
    "title": "AMD will acquire Fei-Fei Li’s World Labs for $8.2 billion",
    "url": "https://techcrunch.com/2026/09/28/amd-will-acquire-fei-fei-lis-world-labs-for-8-2-billion/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T20:39:33+00:00",
    "summary": "The acquisition will see World Labs founder Fei-Fei Li join AMD as executive vice president and chief scientist."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/shopify-opens-checkout-to-browser-based-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Shopify opens checkout to browser-based AI agents",
    "url": "https://techcrunch.com/2026/09/28/shopify-opens-checkout-to-browser-based-ai-agents/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T19:33:57+00:00",
    "summary": "Shopify is expanding WebMCP support to checkout, allowing browser-based AI agents to update order details and complete purchases with a buyer’s authorization."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/tesla-delays-roadster-2-event-again-due-to-bad-weather/",
    "domain": "大厂 AI 动态",
    "title": "Tesla delays Roadster 2 event again due to bad weather",
    "url": "https://techcrunch.com/2026/09/28/tesla-delays-roadster-2-event-again-due-to-bad-weather/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T19:27:27+00:00",
    "summary": "Tesla says the event \"can only be held outdoors,\" as it's expected to show the car flying in some form using SpaceX thrusters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/the-ai-boom-took-over-climate-week-and-not-everyone-is-happy-about-it/",
    "domain": "大厂 AI 动态",
    "title": "The AI boom took over Climate Week and not everyone is happy about it",
    "url": "https://techcrunch.com/2026/09/28/the-ai-boom-took-over-climate-week-and-not-everyone-is-happy-about-it/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T19:21:59+00:00",
    "summary": "Just like the rest of the U.S., data centers and AI are dividing climate tech founders and investors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/nvidia-launches-new-platform-for-reining-in-rogue-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia launches new platform for reining in rogue AI agents",
    "url": "https://techcrunch.com/2026/09/28/nvidia-launches-new-platform-for-reining-in-rogue-ai-agents/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T18:31:23+00:00",
    "summary": "Nvidia CEO Jensen Huang on Monday introduced a toolkit of software and hardware products that add independent security layers around AI agents to ensure they stay within their test environments even i"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/anthropic-releases-sonnet-5-5-which-it-calls-a-significantly-cheaper-faster-work-partner/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic releases Sonnet 5.5, which it calls a significantly cheaper, faster work partner",
    "url": "https://techcrunch.com/2026/09/28/anthropic-releases-sonnet-5-5-which-it-calls-a-significantly-cheaper-faster-work-partner/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T18:00:00+00:00",
    "summary": "Anthropic has released the newest version of its mid-range model, boasting faster response times and less token burn."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/google-is-killing-off-geminis-gems-in-favor-of-skills/",
    "domain": "大厂 AI 动态",
    "title": "Google is killing off Gemini’s Gems in favor of ‘skills’",
    "url": "https://techcrunch.com/2026/09/28/google-is-killing-off-geminis-gems-in-favor-of-skills/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T17:29:50+00:00",
    "summary": "As all-in-one AI agents like Meta's Muse and Instinct take off, Google is opting to end a feature that built task-specific agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/openai-still-doesnt-seem-to-have-a-handle-on-all-of-its-rogue-ai-activity/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI still doesn’t seem to have a handle on all of its rogue AI activity",
    "url": "https://techcrunch.com/2026/09/28/openai-still-doesnt-seem-to-have-a-handle-on-all-of-its-rogue-ai-activity/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T17:09:02+00:00",
    "summary": "On Friday, OpenAI published a new site devoted to “misalignment reports” and the breadth of the incidents is alarming."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/meta-launches-enterprise-ai-platform-hires-mongodb-ceo-to-lead-new-initiative/",
    "domain": "大厂 AI 动态",
    "title": "Meta launches enterprise AI platform, hires MongoDB CEO to lead new initiative",
    "url": "https://techcrunch.com/2026/09/28/meta-launches-enterprise-ai-platform-hires-mongodb-ceo-to-lead-new-initiative/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T16:52:38+00:00",
    "summary": "Meta says it will focus on bringing its full technology stack, including Muse, Meta Business Agent, Muse API, Muse Code, and more to businesses and developers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/the-iphone-duo-may-already-have-its-first-killer-app-a-virtual-walkman/",
    "domain": "大厂 AI 动态",
    "title": "The iPhone Duo may already have its first killer app: a virtual Walkman",
    "url": "https://techcrunch.com/2026/09/28/the-iphone-duo-may-already-have-its-first-killer-app-a-virtual-walkman/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T16:47:49+00:00",
    "summary": "The app imitates how Walkmans used to function: You can open up the Duo to pick your music and \"insert\" your cassette tape, then close the device shut to start listening."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/anthropic-gamma-and-clay-share-what-happens-when-enterprises-actually-deploy-ai-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic, Gamma, and Clay share what happens when enterprises actually deploy AI at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/28/anthropic-gamma-and-clay-share-what-happens-when-enterprises-actually-deploy-ai-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:30:00+00:00",
    "summary": "Anthropic, Clay, and Gamma on what it takes for an AI product to go beyond the demo at the AI Stage at TechCrunchDisrupt 2026. Register to join and get 50% off a second pass."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/physical-ai-chip-developer-sima-ai-hits-1-45b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Physical AI chip developer SiMa AI hits $1.45B valuation",
    "url": "https://techcrunch.com/2026/09/28/physical-ai-chip-developer-sima-ai-hits-1-45b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:29:21+00:00",
    "summary": "The edge computing startup raised a $150 million Series C led by Fidelity and Amplify."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/mavi-bets-on-the-ai-boom-creating-demand-for-a-new-kind-of-accountant/",
    "domain": "大厂 AI 动态",
    "title": "MAVI bets on the AI boom creating demand for a new kind of accountant",
    "url": "https://techcrunch.com/2026/09/28/mavi-bets-on-the-ai-boom-creating-demand-for-a-new-kind-of-accountant/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:26:46+00:00",
    "summary": "Accounting staffing company MAVI emerges from stealth with $4 million in funding."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/28/after-a-deepfake-voice-fooled-her-grandfather-this-founder-sprang-into-action/",
    "domain": "大厂 AI 动态",
    "title": "After a deepfake voice fooled her grandfather, this founder sprang into action",
    "url": "https://techcrunch.com/2026/09/28/after-a-deepfake-voice-fooled-her-grandfather-this-founder-sprang-into-action/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T15:00:00+00:00",
    "summary": "After her grandfather was scammed by a deepfake of his brother's voice, Tarini Padmanabhuni founded DetectifAI, a San Francisco startup building AI models small enough to run directly on smartphones a"
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
    "id": "rss:https://arstechnica.com/space/2026/09/boeing-incredibly-excited-to-serve-as-nations-only-astronaut-transportation/",
    "domain": "大厂 AI 动态",
    "title": "Boeing \"incredibly excited\" to serve as nation's only astronaut transportation",
    "url": "https://arstechnica.com/space/2026/09/boeing-incredibly-excited-to-serve-as-nations-only-astronaut-transportation/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T22:24:33+00:00",
    "summary": "\"We couldn't provide detailed pricing to the CLD suppliers.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/nvidia-may-sell-more-chips-in-china-as-jensen-huangs-influence-over-trump-grows/",
    "domain": "大厂 AI 动态",
    "title": "Experts worry about Nvidia's AI chip sales in China and influence over Trump",
    "url": "https://arstechnica.com/tech-policy/2026/09/nvidia-may-sell-more-chips-in-china-as-jensen-huangs-influence-over-trump-grows/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T21:49:10+00:00",
    "summary": "China is reportedly mulling letting ByteDance, Alibaba buy banned Nvidia chips."
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
    "points": 166,
    "published_at": "2026-09-24T03:58:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49712746",
    "domain": "股票",
    "title": "Global bond yields hit 2008 highs, raising stakes for big borrowers",
    "url": "https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-15T14:07:01+00:00",
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
    "id": "rss:https://www.netinterest.co/p/the-agents-revolt",
    "domain": "股票",
    "title": "The Agents Revolt",
    "url": "https://www.netinterest.co/p/the-agents-revolt",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:33:27+00:00",
    "summary": "What happens to finance when customers start paying attention"
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
    "points": 315,
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
    "points": 119,
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
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-09-25T21:09:28+00:00",
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
    "points": 25,
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
  }
]
```
