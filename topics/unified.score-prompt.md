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

- 今日日期：`2026-10-08`
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
  "date": "2026-10-08",
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
    "points": 3119708,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1938210,
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
    "points": 1371391,
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
    "points": 1317341,
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
    "points": 1110575,
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
    "points": 1092415,
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
    "points": 1078307,
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
    "points": 896203,
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
    "points": 834779,
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
    "points": 706217,
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
    "points": 456732,
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
    "points": 349378,
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
    "points": 309801,
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
    "points": 302176,
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
    "points": 273477,
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
    "points": 231929,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 215598,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 196253,
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
    "points": 182928,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 158727,
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
    "points": 151581,
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
    "points": 130293,
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
    "points": 93921,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 75959,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 72457,
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
    "points": 64474,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 61431,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万圣Dwin",
    "platform": "bilibili",
    "points": 59834,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55775,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 54420,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 54175,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 49012,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 36510,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1GgDpBkEuG",
    "domain": "AI",
    "title": "免费不限速！EasyTier自建服务器全流程",
    "url": "http://www.bilibili.com/video/av116372776491925",
    "source": "科技智趣坊",
    "platform": "bilibili",
    "points": 34701,
    "published_at": "2026-04-09T04:21:55+00:00",
    "summary": "5分钟完整版实操！手把手教你用EasyTier自建服务器，无需公网IP，轻松搞定内网穿透、异地组网。不管是远程办公、NAS访问，还是跨网设备互联、游戏联机，都能一键实现。全程无复杂操作，开源免费、安全稳定，新手也能跟着做一步到位。告别第三方中转延迟，打造专属私人局域网，收藏备用，看完直接上手搭建，解决跨网访问所有难题～"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34478,
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
    "points": 33052,
    "published_at": "2025-02-16T09:02:42+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29810,
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
    "points": 28977,
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
    "points": 23894,
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
    "points": 22806,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Cvpw6iEwS",
    "domain": "AI",
    "title": "【10月Agent大横评】Deepseek用什么AI Agent不烧心，从夯到拉？",
    "url": "http://www.bilibili.com/video/av117393351251135",
    "source": "xx滴热茶",
    "platform": "bilibili",
    "points": 20777,
    "published_at": "2026-10-06T09:56:33+00:00",
    "summary": "Deepseek用什么agent不烧心，从夯到拉？穷鬼实测到底哪个agent和deepseek搭配做的又快又好还省钱？【8个Agent大横评】"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 20120,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 17166,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 16795,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1dogD6aERB",
    "domain": "AI",
    "title": "2026年医学生必看的【AI+医学】最强教程来了（学习路线+完整教程）手把手教你医学方向如何结合AI搞定论文和项目！",
    "url": "http://www.bilibili.com/video/av116968686359676",
    "source": "迪哥AI大讲堂-",
    "platform": "bilibili",
    "points": 16257,
    "published_at": "2026-07-23T17:38:08+00:00",
    "summary": "迪哥给大家准备了医学人工智能学习资料包，可在评论区获取！\n包含：\n1、上百篇医学方向人工智能顶会论文+源码\n2、90+各种疾病医疗数据集\n3、人工智能医学领域经典实战项目\n4、医学生必备的学习路线图"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 13200,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12151,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 11690,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9602,
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
    "points": 9288,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1091,
    "published_at": "2026-09-28T02:05:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 403,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49906100",
    "domain": "AI 算力 / 半导体",
    "title": "OpenDLSS: A Vulkan Reimplementation of Nvidia's DLSS 5 Neural Rendering Network",
    "url": "https://github.com/maanHimself/OpenDLSS-NR",
    "source": "sagacity",
    "platform": "hackernews",
    "points": 278,
    "published_at": "2026-09-30T08:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49926773",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Janus – Go binary that runs GGUF models via Vulkan on AMD/Intel/Nvidia",
    "url": "https://github.com/Vibra-Ingenn/Janus",
    "source": "Maverick617",
    "platform": "hackernews",
    "points": 106,
    "published_at": "2026-10-01T20:36:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49933958",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon seeks to offload $8B of Nvidia chips to investors",
    "url": "https://www.reuters.com/business/retail-consumer/amazon-seeks-offload-8-billion-nvidia-chips-investors-ft-reports-2026-10-02/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-10-02T14:30:32+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/rohm-semiconductor-expands-back-end-chip-manufacturing-outsourcing/",
    "domain": "AI 算力 / 半导体",
    "title": "Rohm Semiconductor Expands Back-End Chip Manufacturing Outsourcing",
    "url": "https://www.eetimes.com/rohm-semiconductor-expands-back-end-chip-manufacturing-outsourcing/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T07:18:51+00:00",
    "summary": "Rohm Semiconductor retains wafer fabrication in-house as it expands its back-end semiconductor operations and R&#038;D footprint in India. The post Rohm Semiconductor Expands Back-End Chip Manufacturi"
  },
  {
    "id": "rss:https://www.eetimes.com/can-ai-be-trusted-synopsys-on-agentic-ai-and-autonomous-engineering/",
    "domain": "AI 算力 / 半导体",
    "title": "Can AI Be Trusted? Synopsys on Agentic AI and Autonomous Engineering",
    "url": "https://www.eetimes.com/can-ai-be-trusted-synopsys-on-agentic-ai-and-autonomous-engineering/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T20:07:11+00:00",
    "summary": "See how Synopsys uses agentic AI to orchestrate trusted EDA tools for precise, explainable chip design, and faster engineering workflows. The post Can AI Be Trusted? Synopsys on Agentic AI and Autonom"
  },
  {
    "id": "rss:https://www.eetimes.com/why-ais-limit-is-power-not-chips-gopi-sirineni-at-ai-infra-summit-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Why AI’s Limit Is Power, Not Chips: Gopi Sirineni at AI Infra Summit 2026",
    "url": "https://www.eetimes.com/why-ais-limit-is-power-not-chips-gopi-sirineni-at-ai-infra-summit-2026/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T19:56:58+00:00",
    "summary": "Gopi Sirineni says AI’s bottleneck is power, not chips, and autonomous rack controllers can boost efficiency up to 30%. The post Why AI&#8217;s Limit Is Power, Not Chips: Gopi Sirineni at AI Infra Sum"
  },
  {
    "id": "rss:https://www.eetimes.com/amds-mark-papermaster-exclusive-video-interview-at-world-summit-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s Mark Papermaster: Exclusive Video Interview at World Summit AI",
    "url": "https://www.eetimes.com/amds-mark-papermaster-exclusive-video-interview-at-world-summit-ai/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:39:00+00:00",
    "summary": "For AMD CTO Mark Papermaster, tailored computing and holistic design are key to delivering AI. The post AMD’s Mark Papermaster: Exclusive Video Interview at World Summit AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/engineering-reliability-power-architectures-for-high-performance-burn-in/",
    "domain": "AI 算力 / 半导体",
    "title": "Engineering Reliability: Power Architectures for High-Performance Burn-In",
    "url": "https://www.eetimes.com/engineering-reliability-power-architectures-for-high-performance-burn-in/",
    "source": "Advanced Energy, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T15:47:11+00:00",
    "summary": "Join this session where our expert will examine key power technologies, design considerations, and best practices that help manufacturers enhance product quality, accelerate qualification, and reduce "
  },
  {
    "id": "rss:https://www.eetimes.com/enhance-power-quality-with-a-gan-based-ac-dc-three-level-vienna-rectifier/",
    "domain": "AI 算力 / 半导体",
    "title": "Enhance Power Quality with a GaN-based AC/DC Three-Level Vienna Rectifier",
    "url": "https://www.eetimes.com/enhance-power-quality-with-a-gan-based-ac-dc-three-level-vienna-rectifier/",
    "source": "Renesas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T14:00:00+00:00",
    "summary": "Data centers have become essential to almost every part of the global economy with the continuing rise in computing demands. Modern data centers, consisting of rows of equipment racks for storing, pro"
  },
  {
    "id": "rss:https://www.eetimes.com/from-electrification-to-architecture-the-next-automotive-era/",
    "domain": "AI 算力 / 半导体",
    "title": "From Electrification to Architecture: The Next Automotive Era",
    "url": "https://www.eetimes.com/from-electrification-to-architecture-the-next-automotive-era/",
    "source": "UTAC Group",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T13:00:00+00:00",
    "summary": "From electrification to software-defined vehicles, automotive innovation is driving new requirements for semiconductor packaging and test. The post From Electrification to Architecture: The Next Autom"
  },
  {
    "id": "rss:https://www.eetimes.com/silicon-labs-adds-iot-developer-platform-tools/",
    "domain": "AI 算力 / 半导体",
    "title": "Silicon Labs Adds IoT Developer Platform Tools",
    "url": "https://www.eetimes.com/silicon-labs-adds-iot-developer-platform-tools/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T11:03:18+00:00",
    "summary": "To meet rising edge AI demands, Silicon Labs connects its development tools with generative AI and enterprise data infrastructure. The post Silicon Labs Adds IoT Developer Platform Tools appeared firs"
  },
  {
    "id": "rss:https://www.eetimes.com/the-ai-boom-has-a-gigawatt-accounting-problem/",
    "domain": "AI 算力 / 半导体",
    "title": "The AI Boom Has a Gigawatt Accounting Problem",
    "url": "https://www.eetimes.com/the-ai-boom-has-a-gigawatt-accounting-problem/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T21:57:47+00:00",
    "summary": "Track energized compute, not gigawatts, as AI data centers face delays in memory, networking, cooling, and power. The post The AI Boom Has a Gigawatt Accounting Problem appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/axelera-ai-data-center-inference-performance-in-the-power-envelope-of-embedded-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Axelera AI: Data Center Inference Performance in the Power Envelope of Embedded Systems",
    "url": "https://www.eetimes.com/axelera-ai-data-center-inference-performance-in-the-power-envelope-of-embedded-systems/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-06T18:03:14+00:00",
    "summary": "Axelera’s Europa brings 629 TOPS inference to 35W edge systems while Voyager cuts toolchain lock-in. The post Axelera AI: Data Center Inference Performance in the Power Envelope of Embedded Systems ap"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/video-editing-graphic-design/solo-developer-rebuilds-adobe-creative-suite-in-rust-using-claude-releases-it-free-to-all-targets-100-percent-parity-in-one-month-despite-piracy-claims-and-safety-warnings",
    "domain": "AI 算力 / 半导体",
    "title": "Solo developer rebuilds Adobe Creative Suite in Rust using Claude, releases it free to all",
    "url": "https://www.tomshardware.com/software/video-editing-graphic-design/solo-developer-rebuilds-adobe-creative-suite-in-rust-using-claude-releases-it-free-to-all-targets-100-percent-parity-in-one-month-despite-piracy-claims-and-safety-warnings",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:00:00+00:00",
    "summary": "Multiple Adobe creative tools were recreated using Claude and made open-source by one person."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/it-pro-says-his-parents-keurig-smart-coffee-maker-sent-1tb-of-data-over-their-wi-fi-in-10-days-it-saturated-an-access-point-on-its-own-but-he-says-most-of-the-traffic-never-left-the-home-network",
    "domain": "AI 算力 / 半导体",
    "title": "IT pro says his parents’ Keurig smart coffee maker sent 1TB of data over their Wi-Fi in 10 days",
    "url": "https://www.tomshardware.com/networking/it-pro-says-his-parents-keurig-smart-coffee-maker-sent-1tb-of-data-over-their-wi-fi-in-10-days-it-saturated-an-access-point-on-its-own-but-he-says-most-of-the-traffic-never-left-the-home-network",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T09:30:00+00:00",
    "summary": "A Keurig K-Supreme SMART coffee maker sent about 1TB over a family’s home Wi-Fi in 10 days, saturating an access point."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/these-are-the-best-prime-day-deals-ive-found-on-tools-i-use-to-maintain-my-pc-from-screwdrivers-to-air-blowers-these-tools-will-keep-your-pc-in-tip-top-shape",
    "domain": "AI 算力 / 半导体",
    "title": "These are the best Prime Day deals I've found on tools I use to maintain my PC",
    "url": "https://www.tomshardware.com/desktops/pc-building/these-are-the-best-prime-day-deals-ive-found-on-tools-i-use-to-maintain-my-pc-from-screwdrivers-to-air-blowers-these-tools-will-keep-your-pc-in-tip-top-shape",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T01:39:00+00:00",
    "summary": "You really do need all of these tools to keep your electronics in good order, and luckily they are all on offer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-is-the-cheapest-4tb-ssd-for-prime-day-at-only-10-cents-per-gigabyte-usd399-teamgroup-g50-evo-is-a-speedy-pcie-4-0-drive-at-cut-throat-pricing",
    "domain": "AI 算力 / 半导体",
    "title": "This is the cheapest 4TB SSD for Prime Day at only 10 cents per gigabyte",
    "url": "https://www.tomshardware.com/pc-components/this-is-the-cheapest-4tb-ssd-for-prime-day-at-only-10-cents-per-gigabyte-usd399-teamgroup-g50-evo-is-a-speedy-pcie-4-0-drive-at-cut-throat-pricing",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T00:00:17+00:00",
    "summary": "Hold the press: TeamGroup G50 EVO 4 TB NVMe drive for $399.99 — speedy PCIe 4.0 unit for only 10 cents a gigabyte"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/elevate-your-steam-deck-and-rog-allys-ssd-storage-for-just-usd0-13-per-gb-rare-discount-brings-wd-black-sn770m-2tb-back-to-near-launch-price",
    "domain": "AI 算力 / 半导体",
    "title": "Elevate your Steam Deck and ROG Ally's SSD storage for just $0.13 per GB",
    "url": "https://www.tomshardware.com/pc-components/ssds/elevate-your-steam-deck-and-rog-allys-ssd-storage-for-just-usd0-13-per-gb-rare-discount-brings-wd-black-sn770m-2tb-back-to-near-launch-price",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T23:35:11+00:00",
    "summary": "The WD Black SN770M 2TB SSD is currently on sale for $259.99, just 8% over the PCIe 4.0's launch price before the storage shortage."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/pre-orders-are-live-on-nvidia-rtx-spark-devices-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptop-starting-at-usd2-599-pricing-and-availability-revealed-on-several-models",
    "domain": "AI 算力 / 半导体",
    "title": "Pre-orders are live on Nvidia RTX Spark devices, secure the Surface Laptop Ultra or other RTX Spark laptops here — starting at $2,599",
    "url": "https://www.tomshardware.com/laptops/pre-orders-are-live-on-nvidia-rtx-spark-devices-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptop-starting-at-usd2-599-pricing-and-availability-revealed-on-several-models",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T22:52:39+00:00",
    "summary": "Pre-orders are live on Nvidia RTX Spark laptops, including the Microsoft Surface Laptop Ultra and devices from HP, Lenovo, Asus, and Dell."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/the-logitech-g29-racing-wheel-and-pedal-set-with-real-force-feedback-is-back-on-sale-with-steep-37-percent-discount-get-a-start-to-a-racing-sim-for-usd190",
    "domain": "AI 算力 / 半导体",
    "title": "The Logitech G29 racing wheel and pedal set is back on sale with steep 37% discount",
    "url": "https://www.tomshardware.com/pc-components/the-logitech-g29-racing-wheel-and-pedal-set-with-real-force-feedback-is-back-on-sale-with-steep-37-percent-discount-get-a-start-to-a-racing-sim-for-usd190",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T21:20:00+00:00",
    "summary": "The Logitech G29 is on a 37% discount during Prime Big Deal Days, dropping its price to just $189.98."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/do-you-need-a-mouse-with-an-8k-polling-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Do you need a mouse with an 8K polling rate?",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/do-you-need-a-mouse-with-an-8k-polling-rate",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T21:10:00+00:00",
    "summary": "A gaming mouse with an 8,000 Hz polling rate sounds awesome and speedy on paper, but let's take a look at what that actually means."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/get-a-great-deal-on-the-original-msi-claw-during-best-buy-clearance-sale-handheld-with-intel-core-ultra-7-155h-and-1tb-ssd-is-just-usd562-usd187-off-list-price",
    "domain": "AI 算力 / 半导体",
    "title": "Sneak a great deal on the original MSI Claw during Best Buy clearance sale",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/get-a-great-deal-on-the-original-msi-claw-during-best-buy-clearance-sale-handheld-with-intel-core-ultra-7-155h-and-1tb-ssd-is-just-usd562-usd187-off-list-price",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T21:00:24+00:00",
    "summary": "The MSI Claw A1M is on a clearance sale at Best Buy right now, knocking $187 off list price for a $562 handheld with 1TB of storage."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-a-steelseries-apex-pro-keyboard-at-up-to-50-percent-off-save-up-to-usd120-on-one-of-the-best-gaming-keyboards-you-can-buy-today",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a SteelSeries Apex Pro keyboard at up to 50% off — save up to $120 on one of the best gaming keyboards you can buy today",
    "url": "https://www.tomshardware.com/pc-components/grab-a-steelseries-apex-pro-keyboard-at-up-to-50-percent-off-save-up-to-usd120-on-one-of-the-best-gaming-keyboards-you-can-buy-today",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T20:50:00+00:00",
    "summary": "SteelSeries put some of its most premium gaming keyboards on sale, allowing you to save cash whether you get a wired or a wireless keyboard."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/deep-clean-your-pc-in-seconds-with-cordless-duster-deals-from-usd19-save-hundreds-on-canned-air-with-unlimited-high-rpm-dusting-power",
    "domain": "AI 算力 / 半导体",
    "title": "Deep clean your PC in seconds with cordless duster deals from $19",
    "url": "https://www.tomshardware.com/peripherals/deep-clean-your-pc-in-seconds-with-cordless-duster-deals-from-usd19-save-hundreds-on-canned-air-with-unlimited-high-rpm-dusting-power",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T20:30:00+00:00",
    "summary": "Amazon Prime Big Deal Days 2026 is the perfect time to pick up an air blower to clean grime and dust from your PC fans, keyboard keys, and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-40-percent-on-hotos-cordless-rotary-toolkit-now-just-usd29-99-great-for-3d-printing-and-other-diy-tasks-get-a-powerful-25-000-rpm-motor-2-000-mah-battery-and-35-accessories-on-the-cheap",
    "domain": "AI 算力 / 半导体",
    "title": "Save 40% on Hoto’s cordless rotary toolkit, now just $29.99 — great for 3D printing and other DIY tasks",
    "url": "https://www.tomshardware.com/pc-components/save-40-percent-on-hotos-cordless-rotary-toolkit-now-just-usd29-99-great-for-3d-printing-and-other-diy-tasks-get-a-powerful-25-000-rpm-motor-2-000-mah-battery-and-35-accessories-on-the-cheap",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T20:10:00+00:00",
    "summary": "Designed for detailed DIY work, sanding, polishing, cutting, and 3D printing, Hoto’s cordless rotary toolkit combines a 25,000 RPM motor with 35 accessories and a built-in LED ring light."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/our-favorite-budget-gaming-chair-just-hit-an-all-time-low-of-usd189-save-usd110-on-the-razer-iskur-v2-x-ergonomic-gaming-chair",
    "domain": "AI 算力 / 半导体",
    "title": "Our favorite budget gaming chair just hit an all-time low of $189",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/our-favorite-budget-gaming-chair-just-hit-an-all-time-low-of-usd189-save-usd110-on-the-razer-iskur-v2-x-ergonomic-gaming-chair",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T19:50:00+00:00",
    "summary": "The Razer Iskur V2 X gaming chair has hit a new all-time-low price of $189.51 on Amazon."
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/some-of-the-best-pc-speakers-and-soundbars-weve-tested-are-on-sale-starting-at-just-usd27-99-save-up-to-36-percent-off-a-new-pair-of-pc-speakers-from-creative-edifier-and-onkyo",
    "domain": "AI 算力 / 半导体",
    "title": "Some of the best PC speakers and soundbars we've tested are on sale starting at just $27.99",
    "url": "https://www.tomshardware.com/speakers/some-of-the-best-pc-speakers-and-soundbars-weve-tested-are-on-sale-starting-at-just-usd27-99-save-up-to-36-percent-off-a-new-pair-of-pc-speakers-from-creative-edifier-and-onkyo",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T19:27:44+00:00",
    "summary": "Some of the best PC speakers we've tested are on sale as part of Amazon's Prime Big Deal Days, including options from Edifier, Creative, and Onkyo."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/microsoft-and-nvidia-launch-surface-laptop-ultra-with-rtx-spark-rtx-spark-preorders-live-now-coinciding-with-major-windows-11-changes-for-agentic-ai",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft and Nvidia launch Surface Laptop Ultra with RTX Spark",
    "url": "https://www.tomshardware.com/laptops/microsoft-and-nvidia-launch-surface-laptop-ultra-with-rtx-spark-rtx-spark-preorders-live-now-coinciding-with-major-windows-11-changes-for-agentic-ai",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:07:54+00:00",
    "summary": "Microsoft's Surface Laptop Ultra is now available for pre-order. The company revealed some new Windows 11 features, a new magnetic USB Type-C port, and that the system will work with \"hundreds\" of vid"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/best-amazon-prime-day-3d-printer-deals-2026-save-on-bambu-lab-prusa-creality-elegoo-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day 3D printer deals 2026",
    "url": "https://www.tomshardware.com/3d-printing/best-amazon-prime-day-3d-printer-deals-2026-save-on-bambu-lab-prusa-creality-elegoo-and-more",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T17:50:23+00:00",
    "summary": "We’ve got our sights set on Amazon's Prime Day sales, and the bargains for some of the best 3D printers are hot!"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/essential-3d-printer-maintenance-tool-deals-save-up-to-30-percent-on-precision-tools-lights-snips-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "30% discounts on essential 3D printer maintenance tools",
    "url": "https://www.tomshardware.com/3d-printing/essential-3d-printer-maintenance-tool-deals-save-up-to-30-percent-on-precision-tools-lights-snips-and-more",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T17:14:13+00:00",
    "summary": "3D printers always need a little maintenance, and with these great tools, you’ll be producing great prints all day long."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/here-are-the-best-oled-gaming-monitor-deals-you-can-snag-for-amazon-big-deal-days-2026-beautiful-monitors-up-to-39-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Here are the best OLED gaming monitor deals you can snag for Amazon Big Deal Days 2026",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/here-are-the-best-oled-gaming-monitor-deals-you-can-snag-for-amazon-big-deal-days-2026-beautiful-monitors-up-to-39-percent-off",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T16:40:12+00:00",
    "summary": "OLED gaming monitors are hot right now, and Prime Big Deal Days is an excellent time to be in the market."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/new-linux-tech-compresses-memory-in-ram-as-ram-for-452x-speedup-new-cram-method-offers-giant-boost-to-compressed-memory-reads",
    "domain": "AI 算力 / 半导体",
    "title": "New Linux tech compresses memory in RAM, as RAM, for 452x speedup",
    "url": "https://www.tomshardware.com/software/linux/new-linux-tech-compresses-memory-in-ram-as-ram-for-452x-speedup-new-cram-method-offers-giant-boost-to-compressed-memory-reads",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T16:20:00+00:00",
    "summary": "The new method allows access using standard memory semantics instead of as a block device, drastically improving performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/upgrade-to-wi-fi-6e-or-wi-fi-7-with-these-stellar-savings-tp-link-wi-fi-6e-and-wi-fi-7-routers-get-big-discounts",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrade to Wi-Fi 6E or Wi-Fi 7 with these stellar savings",
    "url": "https://www.tomshardware.com/networking/routers/upgrade-to-wi-fi-6e-or-wi-fi-7-with-these-stellar-savings-tp-link-wi-fi-6e-and-wi-fi-7-routers-get-big-discounts",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T16:00:06+00:00",
    "summary": "Amazon has some fantastic deals on TP-Link wireless routers, and expect even bigger savings if you're an Amazon Prime Rewards VISA cardholder."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/network-switches/this-usd7-99-tp-link-gigabit-switch-lets-you-cheaply-upgrade-your-home-network-and-its-back-at-its-lowest-ever-price-unmanaged-lan-switch-that-adds-five-high-speed-ethernet-ports-to-your-setup-for-lag-free-gaming-or-streaming",
    "domain": "AI 算力 / 半导体",
    "title": "This $7.99 TP-Link gigabit switch lets you cheaply upgrade your home network, and it's back at its lowest ever price",
    "url": "https://www.tomshardware.com/networking/network-switches/this-usd7-99-tp-link-gigabit-switch-lets-you-cheaply-upgrade-your-home-network-and-its-back-at-its-lowest-ever-price-unmanaged-lan-switch-that-adds-five-high-speed-ethernet-ports-to-your-setup-for-lag-free-gaming-or-streaming",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T15:40:00+00:00",
    "summary": "Upgrade your local network with this $7.99 TP-Link gigabit Ethernet switch with five ports, back down to its lowest ever price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/musk-rejects-rumors-of-tsmc-takeover-of-terafab-intel-reaffirms-14a-node-deal-as-musk-floats-cleanroom-sublease",
    "domain": "AI 算力 / 半导体",
    "title": "Musk rejects rumors of TSMC takeover of Terafab — Intel reaffirms 14A node deal as Musk floats cleanroom 'sublease'",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/musk-rejects-rumors-of-tsmc-takeover-of-terafab-intel-reaffirms-14a-node-deal-as-musk-floats-cleanroom-sublease",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T15:20:00+00:00",
    "summary": "Lip-Bu Tan says Intel will remain a part of Elon Musk's Terafab project as Musk wants TSMC to sublease a part of the facility."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-wi-fi-7-mesh-network-for-a-discounted-usd149-99-tp-link-deco-7-be25-offers-5-012-mbps-speeds-and-coverage-for-150-devices",
    "domain": "AI 算力 / 半导体",
    "title": "Get a Wi-Fi 7 mesh network for a discounted $149.99 — TP-Link Deco 7 BE25 offers 5,012 Mbps speeds and coverage for 150 devices",
    "url": "https://www.tomshardware.com/pc-components/get-a-wi-fi-7-mesh-network-for-a-discounted-usd149-99-tp-link-deco-7-be25-offers-5-012-mbps-speeds-and-coverage-for-150-devices",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T15:10:00+00:00",
    "summary": "TP-Link’s Deco 7 BE25 combines Wi-Fi 7 speeds, wide coverage, 2.5Gbps Ethernet, and support for 150-plus devices in a mesh system that now costs considerably less."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/researcher-ports-doom-to-usd8-000-hasselblad-x2d-100-mp-medium-format-camera-uses-touchscreen-for-directional-control-shutter-button-to-fire-weapon",
    "domain": "AI 算力 / 半导体",
    "title": "Researcher ports Doom to $8,000 Hasselblad X2D",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/researcher-ports-doom-to-usd8-000-hasselblad-x2d-100-mp-medium-format-camera-uses-touchscreen-for-directional-control-shutter-button-to-fire-weapon",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T15:00:00+00:00",
    "summary": "Radium Wang experiments with camera firmware and shares some of their findings on GitHub. You might want to be careful when trying this, though, as you probably don't want to brick your expensive came"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/why-i-upgraded-to-a-4k-oled-pc-gaming-monitor-and-why-you-should-or-shouldnt",
    "domain": "AI 算力 / 半导体",
    "title": "Why I upgraded to a 4K OLED PC gaming monitor",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/why-i-upgraded-to-a-4k-oled-pc-gaming-monitor-and-why-you-should-or-shouldnt",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T14:38:31+00:00",
    "summary": "4K 240Hz OLED monitors now cost under $700. I upgraded from a 1440p IPS and can't go back. Here's why I switched, who should upgrade, and who should wait."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/seagate-and-toshiba-battle-for-tdks-hdd-head-business-a-critical-hard-drive-component-multi-billion-dollar-deal-threatens-sole-independent-supplier-as-shortages-intensify",
    "domain": "AI 算力 / 半导体",
    "title": "Seagate and Toshiba battle for TDK's HDD head business, a critical hard drive component",
    "url": "https://www.tomshardware.com/pc-components/hdds/seagate-and-toshiba-battle-for-tdks-hdd-head-business-a-critical-hard-drive-component-multi-billion-dollar-deal-threatens-sole-independent-supplier-as-shortages-intensify",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T14:20:00+00:00",
    "summary": "Seagate and Toshiba both looking forward to acquiring HDD heads business from TDK, the only remaining independent supplier of magnetic heads."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/the-best-switch-2-accessories-on-sale-now-controllers-cameras-cases-screen-protectors-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "The best Switch 2 accessories on sale now",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/the-best-switch-2-accessories-on-sale-now-controllers-cameras-cases-screen-protectors-and-more",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T13:41:28+00:00",
    "summary": "Upgrade your Nintendo Switch 2 with these essential accessories"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/these-15-under-usd50-gadgets-have-upgraded-my-tech-life-and-theyre-all-on-sale-some-are-even-under-usd25",
    "domain": "AI 算力 / 半导体",
    "title": "These 15 under-$50 gadgets have upgraded my tech life, and they're all on sale",
    "url": "https://www.tomshardware.com/peripherals/these-15-under-usd50-gadgets-have-upgraded-my-tech-life-and-theyre-all-on-sale-some-are-even-under-usd25",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T13:20:03+00:00",
    "summary": "From electric screwdrivers to high-res webcams, these are inexpensive game-changers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/qualcomm-will-license-patents-behind-huaweis-logicfolding-chip-architecture-report-says-the-kirin-9050-pro-already-uses-it-with-a-teardown-showing-its-lower-die-is-mostly-cache-and-i-o",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm will license patents behind Huawei’s LogicFolding chip architecture, report says",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/qualcomm-will-license-patents-behind-huaweis-logicfolding-chip-architecture-report-says-the-kirin-9050-pro-already-uses-it-with-a-teardown-showing-its-lower-die-is-mostly-cache-and-i-o",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T13:00:00+00:00",
    "summary": "Qualcomm will license patents behind Huawei’s LogicFolding, according to one report, as a teardown shows off the Kirin 9050 Pro’s two dies."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/florida-sues-tp-link-for-lying-about-the-safety-of-its-routers-state-claims-that-manufacturer-misrepresented-its-security-and-ties-to-china",
    "domain": "AI 算力 / 半导体",
    "title": "Florida sues TP-Link for ‘lying about the safety of its routers’",
    "url": "https://www.tomshardware.com/networking/routers/florida-sues-tp-link-for-lying-about-the-safety-of-its-routers-state-claims-that-manufacturer-misrepresented-its-security-and-ties-to-china",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T12:40:00+00:00",
    "summary": "Florida and three other states have sued the company on the grounds that it's misleading their citizens about the security of its products and its ties with China."
  },
  {
    "id": "hn:49879032",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says AI distillation is 'competition.'",
    "url": "https://www.cnbc.com/2026/09/28/nvidias-jensen-huang-ai-distillation-china.html",
    "source": "cramer4next",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-28T14:55:34+00:00",
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
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1702,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 886,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 768,
    "published_at": "2026-10-04T19:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 618,
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
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49996713",
    "domain": "大厂 AI 动态",
    "title": "I'm not paying $20 for ChatGPT or Claude because a free local LLM does",
    "url": "https://www.xda-developers.com/im-not-paying-20-for-chatgpt-claude-or-gemini-because-a-free-local-llm-does-everything-i-need/",
    "source": "hsnewman",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-07T18:19:03+00:00",
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
    "id": "hn:49993338",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Apple not letting removal of AI models on macOS 27 is outrageous",
    "url": "https://news.ycombinator.com/item?id=49993338",
    "source": "busymom0",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-10-07T14:26:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49859982",
    "domain": "大厂 AI 动态",
    "title": "Faster prompt lookup drafting in llama.cpp",
    "url": "https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/",
    "source": "pptadversary",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-09-26T19:57:24+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1006837/bmw-ix4-ev-range-price-specs-tesla-china",
    "domain": "大厂 AI 动态",
    "title": "BMW’s iX4 SUV is a 428-mile defensive weapon against China’s EV takeover",
    "url": "https://www.theverge.com/transportation/1006837/bmw-ix4-ev-range-price-specs-tesla-china",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T22:01:00+00:00",
    "summary": "While much of the automotive world sits dumbfounded as China gobbles up all its customers, BMW continues to roll out extremely well-crafted, technologically advanced electric vehicles that impress in "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1007489/teengage-engineering-stop-making-synths",
    "domain": "大厂 AI 动态",
    "title": "Teenage Engineering’s CEO says it’ll stop making synths",
    "url": "https://www.theverge.com/gadgets/1007489/teengage-engineering-stop-making-synths",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T21:19:54+00:00",
    "summary": "Teenage Engineering founder and CEO Jesper Kouthoofd told Highsnobiety that it plans to stop making synths. And yes, that includes the iconic OP-1, which put the company on the map. TE isn't just a mu"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1007409/androids-physical-navigation-buttons-are-back-on-googlebooks-but-not-the-way-you-think",
    "domain": "大厂 AI 动态",
    "title": "Android&#8217;s physical navigation buttons are back on Googlebooks, but not the way you think",
    "url": "https://www.theverge.com/tech/1007409/androids-physical-navigation-buttons-are-back-on-googlebooks-but-not-the-way-you-think",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T20:44:34+00:00",
    "summary": "A common misconception I've seen with Googlebooks is that the Quick Insert and Google logo keys are new. They're not, as they first debuted a couple of years ago on some Chromebooks. But there is some"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1007110/october-prime-day-budget-deals-under-50",
    "domain": "大厂 AI 动态",
    "title": "We found some great October Prime Day deals under $50",
    "url": "https://www.theverge.com/gadgets/1007110/october-prime-day-budget-deals-under-50",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T20:30:00+00:00",
    "summary": "Getting in on the Prime Day action doesn’t have to result in an empty wallet. Just as we found a couple handfuls of goodies that are under $25, there are plenty of deals during Amazon’s October sale t"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1007149/roku-oled-tv-pro-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Roku’s OLED TVs are up to $400 off during Prime Day, starting at $700",
    "url": "https://www.theverge.com/gadgets/1007149/roku-oled-tv-pro-prime-day-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T19:27:39+00:00",
    "summary": "Just over a week ago, we covered a deal at Amazon that knocked around 30 percent off Roku’s new (and first-ever) OLED TVs. The deal expired, but has returned for the final day of October Prime Day. Th"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1007276/openai-chatgpt-intelligent-ui-gpt-6",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT&#8217;s &#8216;Intelligent UI&#8217; update fills its responses with pictures, charts, and buttons",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1007276/openai-chatgpt-intelligent-ui-gpt-6",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T19:10:42+00:00",
    "summary": "OpenAI is launching a new Intelligent UI feature in ChatGPT that allows the chatbot to answer your questions with interactive visuals. The update, which is rolling out to all users alongside GPT-6, gi"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1007040/nvidias-powerful-rtx-spark-laptops-can-cost-up-to-7000",
    "domain": "大厂 AI 动态",
    "title": "The first Nvidia RTX Spark laptops cost up to $7,000",
    "url": "https://www.theverge.com/gadgets/1007040/nvidias-powerful-rtx-spark-laptops-can-cost-up-to-7000",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T19:05:52+00:00",
    "summary": "The first array of laptops powered by Nvidia's new RTX Spark chip are designed to compete with high-end MacBook Pros - and they've got some high-end prices to match. The flagship Surface Laptop Ultra "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1007132/icann-domains-2026-ai-agi",
    "domain": "大厂 AI 动态",
    "title": "It appears .agent and .agi are about to be the hot new domains",
    "url": "https://www.theverge.com/tech/1007132/icann-domains-2026-ai-agi",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:46:16+00:00",
    "summary": "For the first time in years, the Internet Corporation for Assigned Names and Numbers - better known as ICANN - is accepting applications for new top-level domains. These are the suffixes at the end of"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1007147/microsoft-surface-laptop-ultra-windows-event-everything-announced",
    "domain": "大厂 AI 动态",
    "title": "Everything announced at Microsoft&#8217;s Surface Laptop Ultra event",
    "url": "https://www.theverge.com/tech/1007147/microsoft-surface-laptop-ultra-windows-event-everything-announced",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:42:22+00:00",
    "summary": "Microsoft just wrapped up a big Windows and Surface-focused keynote in San Francisco. The biggest announcement was arguably the release details about the Surface Laptop Ultra, its new laptop that&#821"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1007113/microsoft-windows-copilot-ai-control-search-hybrid-intelligence",
    "domain": "大厂 AI 动态",
    "title": "Microsoft is giving Copilot more control over Windows and your files",
    "url": "https://www.theverge.com/tech/1007113/microsoft-windows-copilot-ai-control-search-hybrid-intelligence",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:01:20+00:00",
    "summary": "At today's Windows and Surface event, Microsoft showed off an upgrade to its Copilot AI system that will give it access to local files on your PC and the ability to take actions across the OS. It's pa"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/india-rejects-elon-musks-claim-of-discrimination-over-starlink-launch/",
    "domain": "大厂 AI 动态",
    "title": "India rejects Elon Musk’s claim of discrimination over Starlink launch",
    "url": "https://techcrunch.com/2026/10/07/india-rejects-elon-musks-claim-of-discrimination-over-starlink-launch/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T06:14:11+00:00",
    "summary": "Starlink is still awaiting security clearance before it can seek spectrum and begin commercial services in India."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/robot-data-startup-mecka-ai-nabs-60m-from-sequoia/",
    "domain": "大厂 AI 动态",
    "title": "Robot data startup Mecka AI nabs $60M from Sequoia",
    "url": "https://techcrunch.com/2026/10/07/robot-data-startup-mecka-ai-nabs-60m-from-sequoia/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T23:36:57+00:00",
    "summary": "Mecka AI collects and analyzes human motion data to train humanoid robots and other kinds of robots. The startup pays people to record everyday tasks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/while-vcs-crowd-into-san-francisco-endeavor-catalyst-raises-320m-for-founders-elsewhere/",
    "domain": "大厂 AI 动态",
    "title": "While VCs crowd into San Francisco, Endeavor Catalyst raises $320M for founders ‘elsewhere’",
    "url": "https://techcrunch.com/2026/10/07/while-vcs-crowd-into-san-francisco-endeavor-catalyst-raises-320m-for-founders-elsewhere/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T22:59:16+00:00",
    "summary": "Endeavor Catalyst just raised $320 million to keep backing founders outside Silicon Valley. Half the profits go back to the nonprofit that finds them."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/nous-research-confirms-it-hit-1-5b-valuation-launches-ai-agents-for-business-users/",
    "domain": "大厂 AI 动态",
    "title": "Nous Research confirms it hit $1.5B valuation, launches AI agents for business users",
    "url": "https://techcrunch.com/2026/10/07/nous-research-confirms-it-hit-1-5b-valuation-launches-ai-agents-for-business-users/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T20:48:45+00:00",
    "summary": "The developer of Hermes Agent raised a $90 million Series B."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/microsoft-releases-new-nvidia-chip-ai-pcs-with-revamped-windows-11/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft releases new Nvidia-chip AI PCs with revamped Windows 11",
    "url": "https://techcrunch.com/2026/10/07/microsoft-releases-new-nvidia-chip-ai-pcs-with-revamped-windows-11/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T20:22:37+00:00",
    "summary": "Microsoft revealed the specs and price for its Surface Laptop Ultra, AI PCs that run on Nvidia chips that are designed to run AI models and agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/metas-muse-launches-on-ipad-just-a-month-after-its-mobile-debut/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Muse launches on iPad just a month after its mobile debut",
    "url": "https://techcrunch.com/2026/10/07/metas-muse-launches-on-ipad-just-a-month-after-its-mobile-debut/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:30:57+00:00",
    "summary": "Meta’s AI agent Muse is now available on iPad, just a month after its mobile debut, as the company rapidly expands the assistant’s reach and integrations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/chatgpt-for-teens-keeps-teens-talking-even-during-mental-health-crises/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT for Teens keeps teens talking, even during mental health crises",
    "url": "https://techcrunch.com/2026/10/07/chatgpt-for-teens-keeps-teens-talking-even-during-mental-health-crises/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:15:28+00:00",
    "summary": "ChatGPT’s teen safeguards are meant to protect vulnerable users, but new testing found the chatbot continues encouraging engagement during crises and potentially encourages unhealthy relationships wit"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/x-expands-its-gametime-sports-hub-beyond-the-nfl-starting-with-mlb/",
    "domain": "大厂 AI 动态",
    "title": "X expands its ‘Gametime’ sports hub beyond the NFL, starting with MLB",
    "url": "https://techcrunch.com/2026/10/07/x-expands-its-gametime-sports-hub-beyond-the-nfl-starting-with-mlb/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:10:00+00:00",
    "summary": "X is turning its NFL-focused Gametime feature into a year-round sports destination, starting with MLB and with other professional leagues to follow."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/chatgpt-is-getting-a-lot-more-visual-with-the-launch-of-a-new-interface/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT is getting a lot more visual, with the launch of a new interface",
    "url": "https://techcrunch.com/2026/10/07/chatgpt-is-getting-a-lot-more-visual-with-the-launch-of-a-new-interface/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T18:00:19+00:00",
    "summary": "OpenAI is launching a new user interface that will bring interactive visuals to ChatGPT."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/greenairy-is-building-smart-plant-towers-to-clean-the-air-in-your-office/",
    "domain": "大厂 AI 动态",
    "title": "Greenairy is building smart plant towers to clean the air in your office",
    "url": "https://techcrunch.com/2026/10/07/greenairy-is-building-smart-plant-towers-to-clean-the-air-in-your-office/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T17:30:00+00:00",
    "summary": "As it turns out, the cure for stuffy, chemical-infused office air might be a tower of leafy greenery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/cia-officer-admits-to-creating-fake-top-secret-government-program-to-steal-over-190-million-including-gold-bars/",
    "domain": "大厂 AI 动态",
    "title": "CIA officer admits to creating fake top secret government program to steal over $190M, including gold bars",
    "url": "https://techcrunch.com/2026/10/07/cia-officer-admits-to-creating-fake-top-secret-government-program-to-steal-over-190-million-including-gold-bars/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T17:04:46+00:00",
    "summary": "CIA officer David Rush, who worked on highly sensitive intelligence programs, reached a plea deal with U.S. prosecutors after he was caught siphoning money and gold with a fake government contract."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/meta-rolls-out-new-ai-tools-to-detect-ads-that-secretly-lead-to-child-sexual-abuse-material/",
    "domain": "大厂 AI 动态",
    "title": "Meta rolls out new AI tools to detect ads that secretly lead to child sexual abuse material",
    "url": "https://techcrunch.com/2026/10/07/meta-rolls-out-new-ai-tools-to-detect-ads-that-secretly-lead-to-child-sexual-abuse-material/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T16:53:46+00:00",
    "summary": "Meta launches new AI tools after discovering ads on its platforms that may look normal but direct users to harmful content elsewhere online."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/healthleap-raises-38m-for-its-ai-that-flags-hospital-patients-who-may-need-a-closer-look/",
    "domain": "大厂 AI 动态",
    "title": "Healthleap raises $38M for its AI that flags hospital patients who may need a closer look",
    "url": "https://techcrunch.com/2026/10/07/healthleap-raises-38m-for-its-ai-that-flags-hospital-patients-who-may-need-a-closer-look/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T15:07:08+00:00",
    "summary": "The financing includes an $8M seed round co-led by Sequoia Capital and First Round Capital, and a $30 million Series A led by Hummingbird Ventures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/bloom-raises-3-6m-to-become-the-alibaba-of-american-manufacturing/",
    "domain": "大厂 AI 动态",
    "title": "Bloom raises $3.6M to become the ‘Alibaba’ of American manufacturing",
    "url": "https://techcrunch.com/2026/10/07/bloom-raises-3-6m-to-become-the-alibaba-of-american-manufacturing/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T15:00:00+00:00",
    "summary": "The Detroit startup has widened its scope beyond mobility to help drone and robotics companies find U.S.-based manufacturers, shippers, and more."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/spacex-alumni-nab-100m-to-rethink-shipping-with-autonomous-freight-trains/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX alumni nab $100M to rethink shipping with autonomous freight trains",
    "url": "https://techcrunch.com/2026/10/07/spacex-alumni-nab-100m-to-rethink-shipping-with-autonomous-freight-trains/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T15:00:00+00:00",
    "summary": "Parallel Systems raised $100 million to scale production of its autonomous electric rail vehicle, which can shuttle thousands of pounds of freight up to 500 miles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/tony-fadell-on-why-the-first-wave-of-ai-gadgets-failed-and-what-comes-next/",
    "domain": "大厂 AI 动态",
    "title": "Tony Fadell on why the first wave of AI gadgets failed — and what comes next",
    "url": "https://techcrunch.com/2026/10/07/tony-fadell-on-why-the-first-wave-of-ai-gadgets-failed-and-what-comes-next/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T14:41:38+00:00",
    "summary": "The “father of the iPod” says the first generation of AI gadgets failed to solve real problems — and the next wave will need to earn consumers’ trust."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/google-experiments-with-an-ai-powered-gaming-platform/",
    "domain": "大厂 AI 动态",
    "title": "Google experiments with an AI-powered gaming platform",
    "url": "https://techcrunch.com/2026/10/07/google-experiments-with-an-ai-powered-gaming-platform/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T14:36:23+00:00",
    "summary": "Google Labs is working on a new AI-powered game-creation platform called Playground for users to build browser-based games using simple text prompts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/openais-alexander-embiricos-is-coming-to-techcrunch-disrupt-2026-days-after-the-launch-of-dots/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s Alexander Embiricos is coming to TechCrunch Disrupt 2026 — days after the launch of Dots",
    "url": "https://techcrunch.com/2026/10/07/openais-alexander-embiricos-is-coming-to-techcrunch-disrupt-2026-days-after-the-launch-of-dots/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T14:30:00+00:00",
    "summary": "OpenAI’s Alexander Embiricos is coming to the AI Stage at TechCrunch Disrupt 2026, just days after the launch of Dots. Join this conversation by registering for your pass. Get you pass now to save up "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/get-hands-on-the-full-lineup-of-interactive-roundtables-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Get hands-on: The full lineup of interactive roundtables at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/10/07/get-hands-on-the-full-lineup-of-interactive-roundtables-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T14:15:00+00:00",
    "summary": "From Nvidia and Chime to Obvious Ventures and Anthropic, explore the entire roundtable agenda at TechCrunch Disrupt 2026. Register now to save up to $100 on your pass and get a second pass at 50% off."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/07/6-days-to-techcrunch-disrupt-2026-save-on-your-pass-before-doors-open/",
    "domain": "大厂 AI 动态",
    "title": "6 days to TechCrunch Disrupt 2026: Save on your pass before doors open",
    "url": "https://techcrunch.com/2026/10/07/6-days-to-techcrunch-disrupt-2026-save-on-your-pass-before-doors-open/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T14:00:00+00:00",
    "summary": "In 6 days, 10,000+ people from across the global startup and tech ecosystem will come together at San Francisco’s Moscone West for TechCrunch Disrupt 2026. If you’re planning to be one of them, regist"
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-katie-harbath-about-disrupting-politics-at-facebook/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Katie Harbath About Disrupting Politics at Facebook",
    "url": "https://stratechery.com/2026/an-interview-with-katie-harbath-about-disrupting-politics-at-facebook/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:00:00+00:00",
    "summary": "An interview with former Facebook Head of Global Elections Katie Harbath about her new book Disrupting Politics, and how things change for the company in the 2010s."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-and-lg-the-house-for-everyone-else-agent-standards-and-amazon/",
    "domain": "大厂 AI 动态",
    "title": "Apple and LG, The House For Everyone Else, Agent Standards and Amazon",
    "url": "https://stratechery.com/2026/apple-and-lg-the-house-for-everyone-else-agent-standards-and-amazon/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T10:01:39+00:00",
    "summary": "Apple is taking a smarter approach to the home than I expected, leaning into integration (with partners); then, what Amazon should do about agents."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/microsoft-event-debuts-new-ai-friendly-hardware-and-windows-changes/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft event debuts new AI-friendly hardware and Windows changes",
    "url": "https://arstechnica.com/gadgets/2026/10/microsoft-event-debuts-new-ai-friendly-hardware-and-windows-changes/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T00:00:24+00:00",
    "summary": "Get ready for more AI in your Windows and more AI on the desktop."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/10/software-is-over-bold-ai-developer-takes-aim-at-adobe-with-open-source-clones/",
    "domain": "大厂 AI 动态",
    "title": "“Software is over”: Bold AI developer takes aim at Adobe with open source clones",
    "url": "https://arstechnica.com/ai/2026/10/software-is-over-bold-ai-developer-takes-aim-at-adobe-with-open-source-clones/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-07T21:56:42+00:00",
    "summary": "Opus-built Creative Cloud alternatives are ambitious, free, and nowhere near finished."
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
    "id": "hn:49930086",
    "domain": "股票",
    "title": "US tells France and Germany to release diesel stocks or face US export ban",
    "url": "https://www.reuters.com/business/energy/us-tells-france-germany-release-diesel-stocks-or-face-us-export-ban-sources-say-2026-10-01/",
    "source": "geox",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-10-02T05:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49997175",
    "domain": "股票",
    "title": "The world has nearly burned through its oil stockpile buffer",
    "url": "https://www.reuters.com/business/energy/world-has-nearly-burned-through-its-oil-stockpile-buffer-executives-say-2026-10-06/",
    "source": "geox",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-10-07T18:50:58+00:00",
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 562,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49948254",
    "domain": "金融",
    "title": "Federal judge calls Flock 'indiscriminate mass surveillance'",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 498,
    "published_at": "2026-10-03T22:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824686",
    "domain": "金融",
    "title": "Feds Target AI Critics as \"Foreign Agents\"",
    "url": "https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign",
    "source": "nmeagent",
    "platform": "hackernews",
    "points": 396,
    "published_at": "2026-09-24T00:41:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-28T10:30:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 258,
    "published_at": "2026-10-01T13:05:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 256,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49981063",
    "domain": "金融",
    "title": "Former German spy chief arrested for attempted treason",
    "url": "https://www.reuters.com/business/finance/former-german-spy-chief-detained-suspicion-espionage-treason-bild-reports-2026-10-06/",
    "source": "semiquaver",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-10-06T16:51:50+00:00",
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
    "id": "hn:49904408",
    "domain": "金融",
    "title": "Tesla takes on $30B in credit as it approaches unprofitability",
    "url": "https://electrek.co/2026/09/29/tesla-takes-on-30-billion-in-credit-as-it-approaches-unprofitability/",
    "source": "ciconia",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-30T04:37:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-10-01T01:40:50+00:00",
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
    "id": "rss:https://arxiv.org/abs/2610.08797",
    "domain": "金融",
    "title": "Optimal Transport for Actuarial Science",
    "url": "https://arxiv.org/abs/2610.08797",
    "source": "Arthur Charpentier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08797v1 Announce Type: new Abstract: These lecture notes introduce optimal transport as a mathematical language for actuarial science. They treat losses, premiums, scores, reserves, capital"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08798",
    "domain": "金融",
    "title": "Recursive Copula Aggregation for Market and Credit Portfolios",
    "url": "https://arxiv.org/abs/2610.08798",
    "source": "Luisa Tibiletti, Simone Farinelli, Eric Dal Moro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08798v1 Announce Type: new Abstract: Risk aggregation is a central problem in financial risk management and regulatory capital assessment. While copula-based approaches are widely used due "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08799",
    "domain": "金融",
    "title": "Explicit Finite-Sum Tail Risk Measures for Hierarchical Market--Credit Copula Aggregation",
    "url": "https://arxiv.org/abs/2610.08799",
    "source": "Luisa Tibiletti, Simone Farinelli, Eric Dal Moro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08799v1 Announce Type: new Abstract: Hierarchical copula models are widely used for aggregating market and credit risks across multi-level portfolio structures. Existing approaches often re"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08801",
    "domain": "金融",
    "title": "Approximate Design-Based Intervals for Downsampled Cross-Sectional Market Aggregates: A Randomized Design for Bandwidth-Constrained Financial Data Pipelines",
    "url": "https://arxiv.org/abs/2610.08801",
    "source": "Minmin Zeng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08801v1 Announce Type: new Abstract: Financial institutions routinely downsample cross-sectional options panels to meet bandwidth and cost constraints. The industry default---deterministic "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08803",
    "domain": "金融",
    "title": "Equivalent Behavioural Martingale Measure",
    "url": "https://arxiv.org/abs/2610.08803",
    "source": "G. Charles-Cadogan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08803v1 Announce Type: new Abstract: The paper places the Samuelson--Merton ``util-prob'' construction and preference-based state-price interpretation inside a continuous-time equivalent-ma"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08804",
    "domain": "金融",
    "title": "A Regulator's Career Option: Revolving Doors, Regulatory Signals, and Firm Tail Risk",
    "url": "https://arxiv.org/abs/2610.08804",
    "source": "G. Charles-Cadogan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08804v1 Announce Type: new Abstract: This paper develops a revolving-door model in which a regulator designs policy signals that affect a regulated firm's capital structure while holding an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08806",
    "domain": "金融",
    "title": "Agentic AI Systems and Financial Stability, From Model Risk to Systemic Risk",
    "url": "https://arxiv.org/abs/2610.08806",
    "source": "Sriram Nagaraj, Seung Jung Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08806v1 Announce Type: new Abstract: Financial stability rests on the premise that distress is largely idiosyncratic and therefore diversifiable: when one institution errs, the rest of the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08821",
    "domain": "金融",
    "title": "Two-Regime Risk Measures under Convex Loss",
    "url": "https://arxiv.org/abs/2610.08821",
    "source": "Mihaela-Adriana Nistor, Ionel Popescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08821v1 Announce Type: new Abstract: We study a two-regime summary of a real-valued loss distribution. The two representative levels and the boundary between them are chosen by minimizing a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.08869",
    "domain": "金融",
    "title": "Learned Monotone Recurrent Features in Governed Credit Scoring: The Price of the Frame and the Necessity of Macro Conditioning",
    "url": "https://arxiv.org/abs/2610.08869",
    "source": "Yew Lee Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.08869v1 Announce Type: new Abstract: Regulated credit scoring requires scores monotone non-decreasing in every exposure input. Deployed pipelines -- hand-crafted monotone aggregates feeding"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.09246",
    "domain": "金融",
    "title": "Conditional value-at-risk under reward-penalty mechanism with applications to robust portfolio management",
    "url": "https://arxiv.org/abs/2610.09246",
    "source": "Jun Cai, Tiantian Mao, Zhiqiao Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.09246v1 Announce Type: new Abstract: In this paper, we present robust portfolio selection models by incorporating a reward and penalty mechanism into portfolio management. We assume that th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.09613",
    "domain": "金融",
    "title": "Residual Learning in Empirical Asset Pricing",
    "url": "https://arxiv.org/abs/2610.09613",
    "source": "Dexin Peng, Xiaoyu Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.09613v1 Announce Type: new Abstract: Shallow models are special cases of deep models, and deep models theoretically have the potential to outperform the shallow ones. However, the existing "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.09622",
    "domain": "金融",
    "title": "Robust distortion riskmetrics under Wasserstein ambiguity",
    "url": "https://arxiv.org/abs/2610.09622",
    "source": "Yang Liu, Qiuqi Wang, Yihan Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.09622v1 Announce Type: new Abstract: Risk evaluation under distributional ambiguity is central to decision making in finance, economics, and operations research. Wasserstein balls provide a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10046",
    "domain": "金融",
    "title": "Optimal Investment to Reach a Financial Goal: A Stochastic Control Framework",
    "url": "https://arxiv.org/abs/2610.10046",
    "source": "Gechun Liang, Moris S. Strub, Yuwei Wang, Zhaojun Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10046v1 Announce Type: new Abstract: We develop a framework for an investor who trades until she either reaches a financial goal or an exogenous deadline arrives. Analogous to utility funct"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10053",
    "domain": "金融",
    "title": "On Bonart's interpretation of the Square-Root Impact Law",
    "url": "https://arxiv.org/abs/2610.10053",
    "source": "J. -P. Bouchaud, I. Mastromatteo, B. Toth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10053v1 Announce Type: new Abstract: The square-root impact law (SRIL), $I = Y\\sigma\\sqrt{Q/V}$, bundles two facts that a single mechanism must explain at once: a shape (impact proportional"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10069",
    "domain": "金融",
    "title": "Demand Models for Market-Level Data with Closed-Form Inverses",
    "url": "https://arxiv.org/abs/2610.10069",
    "source": "Julien Monardo, Mogens Fosgerau, Andr\\'e de Palma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10069v1 Announce Type: new Abstract: We introduce a class of demand models for market-level data. The models can be estimated by linear instrumental variables regression while accommodating"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10356",
    "domain": "金融",
    "title": "The addicted predator-prey model: How opioid use disorder shapes productivity and growth-cycle dynamics",
    "url": "https://arxiv.org/abs/2610.10356",
    "source": "Nara Chung, Marwil Davila Fernandez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10356v1 Announce Type: new Abstract: This paper extends Goodwin's (1967) predator-prey growth-cycle model to incorporate the negative impact of Opioid Use Disorder (OUD) on labor productivi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.07006",
    "domain": "金融",
    "title": "STOCK-JEPA: Prior-Anchored Latent Revision Representation Learning in Equity Markets",
    "url": "https://arxiv.org/abs/2610.07006",
    "source": "Yizhi Luo, Jiahe Yi, Jianhui Zhang, Shuo Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.07006v1 Announce Type: cross Abstract: Learning effective representations helps characterize the structure and dynamics of equity markets from financial data with a low signal-to-noise rati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.09654",
    "domain": "金融",
    "title": "DSTNet: Dynamic Spectral Trajectory Network for Causal Multi-Horizon Financial Forecasting",
    "url": "https://arxiv.org/abs/2610.09654",
    "source": "Aashish Bohra, Lokendra Vishwakarm",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.09654v1 Announce Type: cross Abstract: Wavelet-based financial forecasters typically use the transform only to denoise, or reduce it to a single spectral snapshot at the forecast origin, an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10256",
    "domain": "金融",
    "title": "OOM-RL II: Reality Is an Oracle, Not a Debugger Provenance-Constrained Diagnosis in Continually Evolving Agent-Engineered Systems",
    "url": "https://arxiv.org/abs/2610.10256",
    "source": "Kun Liu, Liqun Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10256v1 Announce Type: cross Abstract: Reality may establish that an outcome occurred without identifying which evolving procedure produced it or why. This distinction matters in production"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10407",
    "domain": "金融",
    "title": "SOTA: Stock Options Trading Agents Guided by Option-Implied Return Distributions",
    "url": "https://arxiv.org/abs/2610.10407",
    "source": "Yizhen Xie, Mengyang Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10407v1 Announce Type: cross Abstract: As option markets grow and AI advances, agentic systems for option trading are gaining increasing attention. Language-model-based agents can reason ov"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10476",
    "domain": "金融",
    "title": "From a Hierarchy of Stochastic Differential Equations to a Hierarchy of Generalized Beta Distributions",
    "url": "https://arxiv.org/abs/2610.10476",
    "source": "Siqi Shao, R. A. Serota",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10476v1 Announce Type: cross Abstract: We introduce a mean-reverting stochastic differential equation with a three-component stochastic term and show that it generates a hierarchy of steady"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10506",
    "domain": "金融",
    "title": "Validity Without Ground Truth: What Stated-Preference Economics Offers the Evaluation of Language Models",
    "url": "https://arxiv.org/abs/2610.10506",
    "source": "Daniel Robert Kling Alexander, Catherine Louise Kling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10506v1 Announce Type: cross Abstract: Many of the questions now put to large language models have no correct answer to score against: what a policy is worth, which option a user should cho"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10525",
    "domain": "金融",
    "title": "A Hawkes Microfoundation for Multitype Inverse Gaussian Subordinators",
    "url": "https://arxiv.org/abs/2610.10525",
    "source": "Yingli Wang, Wei Xu, Lingjiong Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2610.10525v1 Announce Type: cross Abstract: We provide an event-level Hawkes microfoundation for a multitype inverse-Gaussian stochastic clock. We show that the event counts and integrated inten"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.08720",
    "domain": "金融",
    "title": "Outsourced Cryptocurrency Wash Trading",
    "url": "https://arxiv.org/abs/2411.08720",
    "source": "Hunter Ng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2411.08720v2 Announce Type: replace Abstract: I show that outsourced cryptocurrency wash trading is shaped by the objective assigned to the outside firm. When hired to manufacture volume, wash t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.25555",
    "domain": "金融",
    "title": "Ownership Networks and Economic Power in the Italian Energy Sector",
    "url": "https://arxiv.org/abs/2605.25555",
    "source": "Andrea Pannone, Francesco Giancaterini, Tiziano Bacaloni, Andrea Bernardini, Alessio Abeltino",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2605.25555v2 Announce Type: replace Abstract: The energy sector is a cornerstone of national strategic autonomy, yet its increasing financialization has transformed ownership structures into com"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30209",
    "domain": "金融",
    "title": "Integrity at Stake: Statistical Detection of Anomalous In-Play Betting in Football",
    "url": "https://arxiv.org/abs/2605.30209",
    "source": "David Winkelmann, Maya Vienken, Christian Deutscher, Roland Langrock",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2605.30209v2 Announce Type: replace Abstract: Match-fixing undermines the integrity of sport by eroding public trust and threatening the financial sustainability of clubs and leagues. The expans"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12493",
    "domain": "金融",
    "title": "Beyond the Skew-Stickiness Ratio: Transport Geometry of Spot-Driven Variance Surface Dynamics",
    "url": "https://arxiv.org/abs/2608.12493",
    "source": "Charlie Che, Pradeepta Das",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2608.12493v2 Announce Type: replace Abstract: The dynamics of an implied volatility surface to movements of the underlying is classically described by separate rules: sticky strike, sticky delta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31959",
    "domain": "金融",
    "title": "Implementability in Insurance Markets with Adverse Selection",
    "url": "https://arxiv.org/abs/2609.31959",
    "source": "Maria Andraos, Mario Ghossoub",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2609.31959v2 Announce Type: replace Abstract: We consider an insurance market with hidden information, where the agent's type is private information and is drawn from an arbitrary type space. We"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.17243",
    "domain": "金融",
    "title": "The Hidden Geometry of Global Aid: How Money Moves Through 10 Million Transactions",
    "url": "https://arxiv.org/abs/2512.17243",
    "source": "Paul X. McCarthy, Xian Gong, Marian-Andrei Rizoiu, Paolo Boldi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T04:00:00+00:00",
    "summary": "arXiv:2512.17243v3 Announce Type: replace-cross Abstract: International aid is usually described as flows between countries, hiding the organisations money passes through. We reconstruct global aid's "
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
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-02T21:28:59+00:00",
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
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
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
  }
]
```
