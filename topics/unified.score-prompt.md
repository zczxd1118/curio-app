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

- 今日日期：`2026-10-09`
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
  "date": "2026-10-09",
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
    "points": 1942430,
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
    "points": 1375490,
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
    "points": 1321351,
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
    "points": 1112018,
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
    "points": 1107192,
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
    "points": 1101113,
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
    "points": 896738,
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
    "points": 837535,
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
    "points": 707599,
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
    "points": 591726,
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
    "points": 466442,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 419221,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 387134,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 311259,
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
    "points": 302836,
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
    "points": 274053,
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
    "points": 233360,
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
    "points": 225900,
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
    "points": 197593,
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
    "points": 183031,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 161006,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1nM6dBdER6",
    "domain": "AI",
    "title": "vscode如何使用AI编程",
    "url": "http://www.bilibili.com/video/av115875633960242",
    "source": "波哥的编程课",
    "platform": "bilibili",
    "points": 146640,
    "published_at": "2026-01-11T08:58:44+00:00",
    "summary": "如何在vs code中使用AI进行开发，推荐了国产AI编程助手，包括安装扩展、注册登录、选择模型、生成代码和微调代码等步骤。同时，强调AI编程还有很多复杂方面，欢迎在评论区留言。"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 130969,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1Qcg6zgEhU",
    "domain": "AI",
    "title": "【AI Agent实战】从零开始教你搭建Agent智能体，小白也能学会的保姆级教程！让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av114771105945944",
    "source": "讲AI的小坛",
    "platform": "bilibili",
    "points": 116390,
    "published_at": "2025-06-30T07:26:07+00:00",
    "summary": "【AI Agent实战】从零开始的智能体搭建，小白也能学会的保姆级教程！让你少走99%弯路，最简单易懂的大模型教程"
  },
  {
    "id": "bvid:BV1phaq6bEyQ",
    "domain": "AI",
    "title": "自费实测！这堆 AI Agent，到底哪个值得你用？【Agent大横评】",
    "url": "http://www.bilibili.com/video/av117346291157971",
    "source": "三颗门牙X",
    "platform": "bilibili",
    "points": 107689,
    "published_at": "2026-09-28T11:00:00+00:00",
    "summary": "现在的 AI Agent，一个比一个能吹，到底哪个真能干活？\n这期我自费充了会员，把 Codex、WorkBuddy、DeepSeek Harness、千问办公、豆包工作、Kimi、GLM、MiniMax 拉出来试了一圈。从 PPT、Excel、网页，到动画、3D 看房和交互原型，看看实际效果，也聊聊日常用起来顺不顺手。\n同一个模型，换个 Agent，效果和花费能差多少？模型够强，软件就一定好用？"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 107165,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 101588,
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
    "points": 93928,
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
    "points": 88379,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76015,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 70339,
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
    "points": 61891,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 58317,
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
    "points": 49048,
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
    "points": 46783,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 40370,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34480,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1B7KE6NEBU",
    "domain": "AI",
    "title": "以防你不知道Claude Code开Ultracode思考强度会有雷霆特效",
    "url": "http://www.bilibili.com/video/av116933437425926",
    "source": "公孙芳芸",
    "platform": "bilibili",
    "points": 33149,
    "published_at": "2026-07-17T04:31:11+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30884,
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
    "points": 29814,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1t2HQ6EEaD",
    "domain": "AI",
    "title": "耗时两个月，烧掉100亿Token，我终于把它开源了！",
    "url": "http://www.bilibili.com/video/av117404088670328",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 29331,
    "published_at": "2026-10-08T07:26:36+00:00",
    "summary": "项目地址：\nhttps://github.com/laogou717/dogsc"
  },
  {
    "id": "bvid:BV1Cvpw6iEwS",
    "domain": "AI",
    "title": "【10月Agent大横评】Deepseek用什么AI Agent不烧心，从夯到拉？",
    "url": "http://www.bilibili.com/video/av117393351251135",
    "source": "xx滴热茶",
    "platform": "bilibili",
    "points": 28725,
    "published_at": "2026-10-06T09:56:33+00:00",
    "summary": "Deepseek用什么agent不烧心，从夯到拉？穷鬼实测到底哪个agent和deepseek搭配做的又快又好还省钱？【8个Agent大横评】"
  },
  {
    "id": "bvid:BV1HfYW6dEsh",
    "domain": "AI",
    "title": "vsTrader马上要关闭内地服务器了。",
    "url": "http://www.bilibili.com/video/av117239403513785",
    "source": "v1312996",
    "platform": "bilibili",
    "points": 26470,
    "published_at": "2026-09-09T05:36:24+00:00",
    "summary": "理财有风险，投资需谨慎。"
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
    "id": "bvid:BV1v7HC6KEpr",
    "domain": "AI",
    "title": "AI Agent上线一周后，我回滚了",
    "url": "http://www.bilibili.com/video/av117398921286967",
    "source": "极海Channel",
    "platform": "bilibili",
    "points": 21652,
    "published_at": "2026-10-07T09:30:48+00:00",
    "summary": "更多内容请前往社区\n社区地址/咨询与面试: https://bitfree.cn"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 20333,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1QYHs6VEcu",
    "domain": "AI",
    "title": "【保姆级教程】Claude 顶级防封指南，避开所有封号雷区！",
    "url": "http://www.bilibili.com/video/av117387278029256",
    "source": "SenManx",
    "platform": "bilibili",
    "points": 19016,
    "published_at": "2026-10-05T08:15:30+00:00",
    "summary": "不懂的可以发在评论区，也可以加群互相交流：389763840"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 18829,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV1ZWRrBJEaQ",
    "domain": "AI",
    "title": "我是如何用Claude skills从Excel到数据分析+图表可视化",
    "url": "http://www.bilibili.com/video/av116519862340507",
    "source": "迪迪碎碎念_AI",
    "platform": "bilibili",
    "points": 14103,
    "published_at": "2026-05-05T03:36:14+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 12737,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
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
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 391,
    "published_at": "2026-10-08T16:45:58+00:00",
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
    "points": 279,
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
    "id": "rss:https://www.eetimes.com/physical-ai-needs-a-neuromorphic-path-from-sensor-to-silicon/",
    "domain": "AI 算力 / 半导体",
    "title": "Physical AI Needs a Neuromorphic Path from Sensor to Silicon",
    "url": "https://www.eetimes.com/physical-ai-needs-a-neuromorphic-path-from-sensor-to-silicon/",
    "source": "Xabier Iturbe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T08:39:41+00:00",
    "summary": "Physical AI will be limited in the real world if we keep pretending that physical data comes packaged like the digital world. The post Physical AI Needs a Neuromorphic Path from Sensor to Silicon appe"
  },
  {
    "id": "rss:https://www.eetimes.com/worlds-first-single-chip-multiturn-position-sensor-in-smaller-form-factor/",
    "domain": "AI 算力 / 半导体",
    "title": "Worlds First Single Chip Multiturn Position Sensor in Smaller Form Factor",
    "url": "https://www.eetimes.com/worlds-first-single-chip-multiturn-position-sensor-in-smaller-form-factor/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T08:08:26+00:00",
    "summary": "Join this webinar, where our expert will explore the technology behind the ADMT4000 and how its ability to track multiple rotations and angular movement without power is transforming the design of bot"
  },
  {
    "id": "rss:https://www.eetimes.com/scaling-3d-ic-design-trends-challenges-and-practical-workflows/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling 3D IC design: Trends, Challenges and Practical Workflows",
    "url": "https://www.eetimes.com/scaling-3d-ic-design-trends-challenges-and-practical-workflows/",
    "source": "Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T07:32:29+00:00",
    "summary": "Join us to discover how Siemens Innovator3D IC streamlines 3D IC design from planning to implementation! The post Scaling 3D IC design: Trends, Challenges and Practical Workflows appeared first on EE "
  },
  {
    "id": "rss:https://www.eetimes.com/why-custom-silicon-matters-in-ai-data-centers/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Custom Silicon Matters in AI Data Centers",
    "url": "https://www.eetimes.com/why-custom-silicon-matters-in-ai-data-centers/",
    "source": "Scott Seal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T19:16:44+00:00",
    "summary": "Custom silicon lets AI data centers cut power, latency and data movement while improving economics at scale. The post Why Custom Silicon Matters in AI Data Centers appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/schiederwerk-showcases-novel-power-supply-solutions-for-mission-critical-applications-at-electronica-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "SCHIEDERWERK Showcases Novel Power Supply Solutions for Mission-Critical Applications at electronica 2026",
    "url": "https://www.eetimes.com/schiederwerk-showcases-novel-power-supply-solutions-for-mission-critical-applications-at-electronica-2026/",
    "source": "SCHIEDERWERK",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:23:33+00:00",
    "summary": "Nuremberg / Munich, Germany, 2026 — SCHIEDERWERK GmbH, a specialist in custom power electronics solutions engineered and manufactured in Germany, will showcase its latest platform-based power supplies"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-jetson-to-sima-ai-modalix-mlsoc-migration-guide/",
    "domain": "AI 算力 / 半导体",
    "title": "NVIDIA Jetson to SiMa.ai Modalix MLSoC Migration Guide",
    "url": "https://www.eetimes.com/nvidia-jetson-to-sima-ai-modalix-mlsoc-migration-guide/",
    "source": "SiMa Technologies, Inc.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:00:00+00:00",
    "summary": "This technical guide provides a practical framework for migrating machine learning models and applications from an NVIDIA/CUDA-based environment to the SiMa.ai Physical AI platform. It explains the ke"
  },
  {
    "id": "rss:https://www.eetimes.com/rising-costs-compute-demand-push-adas-toward-modular-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Rising Costs, Compute Demand Push ADAS Toward Modular AI",
    "url": "https://www.eetimes.com/rising-costs-compute-demand-push-adas-toward-modular-ai/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T13:00:00+00:00",
    "summary": "Rising semiconductor costs and computing requirements drive automakers toward modular ADAS AI solutions. The post Rising Costs, Compute Demand Push ADAS Toward Modular AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/breaking-the-ai-infrastructure-power-wall-from-grid-to-xpu/",
    "domain": "AI 算力 / 半导体",
    "title": "Breaking the AI Infrastructure Power Wall: From Grid to xPU",
    "url": "https://www.eetimes.com/breaking-the-ai-infrastructure-power-wall-from-grid-to-xpu/",
    "source": "Navitas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:36:33+00:00",
    "summary": "Register now for our webinar to discover how Navitas 2.0 is revolutionizing AI infrastructure power delivery. The post Breaking the AI Infrastructure Power Wall: From Grid to xPU appeared first on EE "
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
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/arc-raiders-developer-uses-ai-to-detect-cheating-embark-cracks-down-on-cheaters-deploys-harsh-penalties-including-permaban-on-first-time-offenders",
    "domain": "AI 算力 / 半导体",
    "title": "Arc Raiders publisher developing AI anti-cheat stack in escalating war with cheaters",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/arc-raiders-developer-uses-ai-to-detect-cheating-embark-cracks-down-on-cheaters-deploys-harsh-penalties-including-permaban-on-first-time-offenders",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T10:00:00+00:00",
    "summary": "These strict measures are designed to deter players from cheating. Those caught will get a permaban that span accounts and even hardware in the future."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-tried-to-crush-the-megahertz-myth-25-years-ago-today-debuting-its-performance-rating-system-athlon-xp-chips-introduced-the-scheme-which-endured-until-intel-lost-its-clock-speed-advantage-with-pentium-m",
    "domain": "AI 算力 / 半导体",
    "title": "AMD attempted to crush the 'Megahertz myth' with its Performance Rating system on this day 25 years ago",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-tried-to-crush-the-megahertz-myth-25-years-ago-today-debuting-its-performance-rating-system-athlon-xp-chips-introduced-the-scheme-which-endured-until-intel-lost-its-clock-speed-advantage-with-pentium-m",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T09:30:00+00:00",
    "summary": "Today, a quarter of a century ago, AMD launched its AMD Athlon XP processor family and its Performance Rating (PR) naming scheme."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-to-produce-silicon-interposers-for-tsmcs-cowos-in-the-us-five-year-agreement-valued-at-usd2-billion",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries to produce silicon interposers for TSMC's CoWoS in the US — Five-year agreement valued at $2 billion",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-to-produce-silicon-interposers-for-tsmcs-cowos-in-the-us-five-year-agreement-valued-at-usd2-billion",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:23:28+00:00",
    "summary": "GlobalFoundries becomes a part of TSMC's CoWoS supply chain in the U.S.: set to participate in production of leading-edge AI and HPC accelerators without investing in leading-edge process technologies"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/u-s-suspends-green-card-path-for-h-1b-workers-at-microsoft-and-adobe-labor-certification-program-blocked-due-to-alleged-fraud",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. suspends green card path for H-1B workers at Microsoft and Adobe — labor certification program blocked due to alleged fraud",
    "url": "https://www.tomshardware.com/tech-industry/policy/u-s-suspends-green-card-path-for-h-1b-workers-at-microsoft-and-adobe-labor-certification-program-blocked-due-to-alleged-fraud",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T17:26:07+00:00",
    "summary": "U.S. suspends green card path for H-1B workers at Microsoft, Adobe, and IT outsourcing companies — PERM program blocked due to alleged fraud"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/the-atari-800xl-returns-with-a-faithful-but-modern-retro-games-ltd-redesign-classic-8-bit-home-computer-revamp-sports-mechanical-keyboard-and-hdmi-connectivity",
    "domain": "AI 算力 / 半导体",
    "title": "The Atari 800XL returns with a 'faithful' but modern Retro Games Ltd redesign",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/the-atari-800xl-returns-with-a-faithful-but-modern-retro-games-ltd-redesign-classic-8-bit-home-computer-revamp-sports-mechanical-keyboard-and-hdmi-connectivity",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T16:37:20+00:00",
    "summary": "Pre-orders for the Atari-licensed THE 800XL began today. This is a modernized yet claimed to be faithful recreation of the classic 8-bit home computer, popular in the early 1980s."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/department-of-war-dishes-out-usd1-5-billion-loan-commitment-to-boost-semiconductor-supply-chain-wolfspeed-to-focus-on-national-security-applications-as-part-of-30-year-agreement",
    "domain": "AI 算力 / 半导体",
    "title": "Department of War dishes out $1.5 billion loan commitment to boost semiconductor supply chain",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/department-of-war-dishes-out-usd1-5-billion-loan-commitment-to-boost-semiconductor-supply-chain-wolfspeed-to-focus-on-national-security-applications-as-part-of-30-year-agreement",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T16:24:54+00:00",
    "summary": "Wolfspeed has secured a conditional $1.5 billion, 30-year loan commitment from the U.S. Department of War to expand GaN epitaxy and radiation-hardened SiC and GaN technologies for U.S. national securi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/finland-orders-google-to-stop-work-on-two-ai-data-centers-over-alleged-deforestation-company-admits-it-has-fallen-short-of-our-own-high-standards-in-this-instance",
    "domain": "AI 算力 / 半导体",
    "title": "Finland orders Google to stop work on two AI data centers over alleged deforestation",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/finland-orders-google-to-stop-work-on-two-ai-data-centers-over-alleged-deforestation-company-admits-it-has-fallen-short-of-our-own-high-standards-in-this-instance",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T15:52:45+00:00",
    "summary": "Finnish authorities say they cannot conduct a proper environmental assessment after the site has already been changed."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-labs-3d-printing-patent-application-for-a-new-heatbed-design-may-improve-peeling-issues-replacement-costs-could-possibly-rise-as-a-consequence",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab’s 3D printing patent application for a new heatbed design may improve peeling issues",
    "url": "https://www.tomshardware.com/3d-printing/bambu-labs-3d-printing-patent-application-for-a-new-heatbed-design-may-improve-peeling-issues-replacement-costs-could-possibly-rise-as-a-consequence",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:11:49+00:00",
    "summary": "Bambu Lab applied to patent its new heatbed design that might finally solve bed adhesion problems for large prints."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/software-could-be-the-easiest-fix-for-hyperscalers-ai-power-squeeze-researchers-say-data-center-demand-is-expected-to-rival-japans-electricity-usage-by-2030",
    "domain": "AI 算力 / 半导体",
    "title": "Software could be the easiest fix for hyperscalers' AI power squeeze, researchers say",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/software-could-be-the-easiest-fix-for-hyperscalers-ai-power-squeeze-researchers-say-data-center-demand-is-expected-to-rival-japans-electricity-usage-by-2030",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:00:00+00:00",
    "summary": "The industry is spending billions on more efficient chips, cooling, and grid connections. But what about making computers do less work – or doing it at a better time?"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russias-yandex-data-centers-housing-two-top-supercomputers-major-outage-follows-retaliatory-strike",
    "domain": "AI 算力 / 半导体",
    "title": "Ukrainian drones hit Russia's Yandex data centers housing two top supercomputers",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russias-yandex-data-centers-housing-two-top-supercomputers-major-outage-follows-retaliatory-strike",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T13:46:56+00:00",
    "summary": "No more AI training in Russia? Destiny of two Nvidia-powered Russian supercomputers is unknown as drones hit Yandex data center in Sasovo."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/amd-seeks-broader-partnership-with-samsung-as-it-looks-to-secure-memory-supply-samsung-reportedly-hopes-to-turn-its-memory-supply-relationship-with-amd-into-foundry-orders-for-logic-chips",
    "domain": "AI 算力 / 半导体",
    "title": "AMD seeks 'broader partnership' with Samsung as it looks to secure memory supply",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/amd-seeks-broader-partnership-with-samsung-as-it-looks-to-secure-memory-supply-samsung-reportedly-hopes-to-turn-its-memory-supply-relationship-with-amd-into-foundry-orders-for-logic-chips",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:30:00+00:00",
    "summary": "AMD is pursuing a 'broader partnership' with Samsung as memory company wants to tie advanced memory supply to its orders at its foundry unit."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/american-jailed-for-commanding-10-000-bots-to-stream-his-own-ai-generated-songs-and-earn-millions-in-fraudulent-royalty-payments-beating-taylor-swift-is-the-first-person-to-end-up-in-prison-for-ai-assisted-music-streaming-crime",
    "domain": "AI 算力 / 半导体",
    "title": "American jailed for commanding 10,000 bots to stream his own AI-generated songs",
    "url": "https://www.tomshardware.com/service-providers/streaming/american-jailed-for-commanding-10-000-bots-to-stream-his-own-ai-generated-songs-and-earn-millions-in-fraudulent-royalty-payments-beating-taylor-swift-is-the-first-person-to-end-up-in-prison-for-ai-assisted-music-streaming-crime",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:19:45+00:00",
    "summary": "The first-ever criminal case involving AI-assisted music streaming fraud has concluded, with an American citizen facing 18 months behind bars and an $8M fine."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/researcher-develops-method-for-fingerprinting-cheaters-using-counter-strike-mouse-and-keyboard-input-patterns-says-technique-can-be-used-so-bans-follow-users-even-if-they-make-new-accounts",
    "domain": "AI 算力 / 半导体",
    "title": "Researcher develops method for fingerprinting cheaters using Counter-Strike mouse and keyboard input patterns",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/researcher-develops-method-for-fingerprinting-cheaters-using-counter-strike-mouse-and-keyboard-input-patterns-says-technique-can-be-used-so-bans-follow-users-even-if-they-make-new-accounts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:10:58+00:00",
    "summary": "u/Magga_ built a method that identified players by looking at how they use their mouse and keyboard. They can then use this to ensure that bans follow cheaters, even if they make new accounts from ano"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-epyc-verano-ai-host-cpu-will-reportedly-use-a-special-sb1-socket-zen-6-chip-pairs-72-cores-with-a-24-channel-lpddr5x-memory-subsystem",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's EPYC Verano AI host CPU will reportedly use a special SB1 socket",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-epyc-verano-ai-host-cpu-will-reportedly-use-a-special-sb1-socket-zen-6-chip-pairs-72-cores-with-a-24-channel-lpddr5x-memory-subsystem",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T12:00:00+00:00",
    "summary": "Dynatron quietly unveils air cooler for AMD's EPYC 'Verano' CPUs aimed at AI servers."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/spotifast-lets-you-enjoy-spotify-tracks-while-lowering-ram-usage-by-5x-or-more-open-source-app-cuts-ram-usage-down-to-150-mb-and-brings-back-classic-winamp-skins",
    "domain": "AI 算力 / 半导体",
    "title": "Spotifast lets you enjoy Spotify tracks while lowering RAM usage by 5x or more",
    "url": "https://www.tomshardware.com/software/applications/spotifast-lets-you-enjoy-spotify-tracks-while-lowering-ram-usage-by-5x-or-more-open-source-app-cuts-ram-usage-down-to-150-mb-and-brings-back-classic-winamp-skins",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T11:30:00+00:00",
    "summary": "Spotifast lets you enjoy Spotify tracks while lowering RAM usage by 5x or more — alternative client also packs Winamp skins and Milkdrop visualizations."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-allegedly-intercepted-ups-shipped-f-35-parts-after-employee-missed-email-warning-worker-decided-to-divert-through-hong-kong-to-speed-up-delivery",
    "domain": "AI 算力 / 半导体",
    "title": "China allegedly intercepted UPS-shipped F-35 parts after employee missed email warning",
    "url": "https://www.tomshardware.com/tech-industry/china-allegedly-intercepted-ups-shipped-f-35-parts-after-employee-missed-email-warning-worker-decided-to-divert-through-hong-kong-to-speed-up-delivery",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T11:06:12+00:00",
    "summary": "A UPS worker missed an important email about securely routing top-secret F-35 parts so mistakenly opted for a Hong Kong transit for faster shipping."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-reportedly-seeking-usd40-billion-debt-package-for-nvidia-ai-hardware-massive-raise-could-fund-roughly-360-000-vera-rubin-gpus-across-5-000-nvl72-racks",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX reportedly seeking $40 billion debt package for Nvidia AI hardware",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-reportedly-seeking-usd40-billion-debt-package-for-nvidia-ai-hardware-massive-raise-could-fund-roughly-360-000-vera-rubin-gpus-across-5-000-nvl72-racks",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T11:00:00+00:00",
    "summary": "SpaceX reportedly intends to borrow $40 billion to procure 360,000 Nvidia Rubin AI accelerators, infrastructure."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/former-groq-engineers-sue-board-over-usd20-billion-nvidia-deal-saying-it-handed-nvidia-the-lpu-and-the-team-that-built-it-plaintiffs-allege-the-board-kept-billions-from-other-shareholders",
    "domain": "AI 算力 / 半导体",
    "title": "Former Groq engineers sue board over $20 billion Nvidia deal",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/former-groq-engineers-sue-board-over-usd20-billion-nvidia-deal-saying-it-handed-nvidia-the-lpu-and-the-team-that-built-it-plaintiffs-allege-the-board-kept-billions-from-other-shareholders",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T11:00:00+00:00",
    "summary": "Two former Groq engineers sued Groq’s board in Delaware over the Nvidia licensing deal behind the Groq 3 LPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-1080p-gaming-pc-for-less-than-usd1-000-right-now-fitted-with-nvidia-or-amd-gpus-save-up-to-usd350-to-secure-rigs-with-rtx-5060-or-rx-9060-gpus-at-low-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Score a 1080p gaming PC for less than $1,000 right now, fitted with Nvidia or AMD GPUs",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-1080p-gaming-pc-for-less-than-usd1-000-right-now-fitted-with-nvidia-or-amd-gpus-save-up-to-usd350-to-secure-rigs-with-rtx-5060-or-rx-9060-gpus-at-low-prices",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:57:45+00:00",
    "summary": "Two gaming PCs capable of 1080p gameplay have dropped below $1,000, a price that's hard to beat in the current market, thanks to sales at Best Buy and Walmart."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/make-the-jump-to-an-oled-gaming-monitor-and-save-48-percent-lgs-massive-45-inch-ultragear-screen-hits-its-lowest-price",
    "domain": "AI 算力 / 半导体",
    "title": "Make the jump to an OLED gaming monitor and save 48%",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/make-the-jump-to-an-oled-gaming-monitor-and-save-48-percent-lgs-massive-45-inch-ultragear-screen-hits-its-lowest-price",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:46:50+00:00",
    "summary": "Save 48% on the 45-inch LG 45GX900A-B OLED gaming monitor at Amazon."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-indicts-10-for-smuggling-us-military-grade-chips-to-china-parts-routed-to-missile-and-radar-programs-using-forged-taiwan-defense-institute-orders-texas-instruments-and-analog-devices-hardware-passed-off-as-made-in-taiwan",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan indicts 10 for smuggling US military-grade chips to China, parts routed to missile and radar programs using forged Taiwan defense institute orders",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-indicts-10-for-smuggling-us-military-grade-chips-to-china-parts-routed-to-missile-and-radar-programs-using-forged-taiwan-defense-institute-orders-texas-instruments-and-analog-devices-hardware-passed-off-as-made-in-taiwan",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T10:30:00+00:00",
    "summary": "Taiwanese prosecutors indicted 10 company heads over Texas Instruments and Analog Devices chips allegedly resold to China."
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
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1703,
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
    "points": 771,
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
    "id": "hn:49996713",
    "domain": "大厂 AI 动态",
    "title": "I'm not paying $20 for ChatGPT or Claude because a free local LLM does",
    "url": "https://www.xda-developers.com/im-not-paying-20-for-chatgpt-claude-or-gemini-because-a-free-local-llm-does-everything-i-need/",
    "source": "hsnewman",
    "platform": "hackernews",
    "points": 47,
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
    "id": "hn:49993338",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Apple not letting removal of AI models on macOS 27 is outrageous",
    "url": "https://news.ycombinator.com/item?id=49993338",
    "source": "busymom0",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-10-07T14:26:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50000431",
    "domain": "大厂 AI 动态",
    "title": "100 days later: Microsoft still steers Windows and Copilot users to Edge",
    "url": "https://blog.mozilla.org/en/mozilla/over-the-edge-2-100-days-later/",
    "source": "thimabi",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-10-08T00:06:27+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1008604/openai-defends-decision-fire-safety-researchers",
    "domain": "大厂 AI 动态",
    "title": "OpenAI doubles down on decision to fire three AI safety researchers",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1008604/openai-defends-decision-fire-safety-researchers",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T09:48:26+00:00",
    "summary": "OpenAI is standing firm on its decision to fire three safety researchers after an investigation found they committed \"a significant breach of trust.\" In a post on X on Friday, the company said Jasmine"
  },
  {
    "id": "rss:https://www.theverge.com/news/1008581/microsoft-365-family-premium-shared-ai-features-storage-changes",
    "domain": "大厂 AI 动态",
    "title": "Microsoft 365 Family subscribers will finally be able to share AI benefits",
    "url": "https://www.theverge.com/news/1008581/microsoft-365-family-premium-shared-ai-features-storage-changes",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T07:14:32+00:00",
    "summary": "Microsoft bundled its AI-powered Office features into Microsoft 365 Personal and Family subscriptions last year, but it only allowed the primary account holder to access the AI benefits. Now, Microsof"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1008530/us-government-livestream-execution-firing-squad-fort-hood",
    "domain": "大厂 AI 动态",
    "title": "US plans livestream of execution by firing squad",
    "url": "https://www.theverge.com/tech/1008530/us-government-livestream-execution-firing-squad-fort-hood",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T22:32:04+00:00",
    "summary": "The United States' execution of the Fort Hood shooter will be livestreamed, anonymous officials from the Defense Department told the BBC and Associated Press. The planned execution of Nidal Hasan, the"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1008521/anthropic-open-source-oss-scanner",
    "domain": "大厂 AI 动态",
    "title": "Anthropic launches free AI security scans for open-source projects",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1008521/anthropic-open-source-oss-scanner",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T21:53:51+00:00",
    "summary": "Anthropic's offering to help open-source projects track down security vulnerabilities with a new service called OSS Scanner. It says open-source projects that opt-in will get \"thorough, periodic secur"
  },
  {
    "id": "rss:https://www.theverge.com/science/1008467/spacex-announces-plan-to-become-a-major-mobile-carrier",
    "domain": "大厂 AI 动态",
    "title": "SpaceX announces plan to become a ‘major mobile carrier’",
    "url": "https://www.theverge.com/science/1008467/spacex-announces-plan-to-become-a-major-mobile-carrier",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T21:23:31+00:00",
    "summary": "SpaceX has acquired a portfolio of low-band spectrum licenses - a move the company says \"will pave the way\" for its Starlink Mobile service to become a \"major\" US carrier. When the Federal Communicati"
  },
  {
    "id": "rss:https://www.theverge.com/games/1008353/amd-will-bring-fsr-4-to-handhelds-by-the-end-of-2026",
    "domain": "大厂 AI 动态",
    "title": "AMD will bring FSR 4 to handhelds by the end of 2026",
    "url": "https://www.theverge.com/games/1008353/amd-will-bring-fsr-4-to-handhelds-by-the-end-of-2026",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T21:01:18+00:00",
    "summary": "It's already possible to get AMD's framerate-enhancing FSR 4 boost on handhelds as old as the Steam Deck - but in June, AMD reserved the right to disappoint handheld gamers by not officially bringing "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1008422/apple-macbook-pro-touchscreen-ipad-mini-rumor",
    "domain": "大厂 AI 动态",
    "title": "Apple will reportedly debut its first touchscreen MacBook in three weeks",
    "url": "https://www.theverge.com/tech/1008422/apple-macbook-pro-touchscreen-ipad-mini-rumor",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T20:32:21+00:00",
    "summary": "Apple is set to introduce a new MacBook Pro with a touchscreen and an updated iPad Mini \"on or around\" October 27th, Bloomberg reports. If true, that would put the event just two weeks after the Octob"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1008401/california-shut-down-rek-fighting-robot-company-human",
    "domain": "大厂 AI 动态",
    "title": "California is trying to shut down robot vs. human cage matches",
    "url": "https://www.theverge.com/tech/1008401/california-shut-down-rek-fighting-robot-company-human",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T20:06:56+00:00",
    "summary": "The California State Athletic Commission sent a cease-and-desist letter to a startup that hosted a match between a human and a robot last month, as reported by The New York Times. The fight, which too"
  },
  {
    "id": "rss:https://www.theverge.com/report/1008342/folkston-georgia-ice-detention-hunger-strike-video",
    "domain": "大厂 AI 动态",
    "title": "ICE detainees in Georgia used the facility’s video calling software to expose the conditions inside",
    "url": "https://www.theverge.com/report/1008342/folkston-georgia-ice-detention-hunger-strike-video",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T19:45:00+00:00",
    "summary": "Four men detained at an ICE detention center in rural Georgia used the facility's video conferencing software to expose both the conditions inside and President Donald Trump's hostile takeover of the "
  },
  {
    "id": "rss:https://www.theverge.com/news/1008320/microsoft-windows-search-overhaul-windows-11",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s new Windows Search is exactly what Windows 11 needs",
    "url": "https://www.theverge.com/news/1008320/microsoft-windows-search-overhaul-windows-11",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T19:30:21+00:00",
    "summary": "Windows Search has been one of the most frustrating parts of Windows 11, and now Microsoft is addressing this with a significant overhaul. A new redesigned Windows Search is now in testing that is muc"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/president-trump-awards-big-tech-donors-with-nations-highest-science-prizes/",
    "domain": "大厂 AI 动态",
    "title": "President Trump awards Big Tech donors with nation’s highest science prizes",
    "url": "https://techcrunch.com/2026/10/08/president-trump-awards-big-tech-donors-with-nations-highest-science-prizes/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T22:33:59+00:00",
    "summary": "Together, the awardees have donated nearly $6 billion to efforts tied to Trump and his administration."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/pretend-youre-sitting-at-elizabeth-holmes-desk-on-this-weirdly-detailed-website/",
    "domain": "大厂 AI 动态",
    "title": "Pretend you’re sitting at Elizabeth Holmes’ desk on this weirdly detailed website",
    "url": "https://techcrunch.com/2026/10/08/pretend-youre-sitting-at-elizabeth-holmes-desk-on-this-weirdly-detailed-website/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T21:00:00+00:00",
    "summary": "With over a thousand emails, slides, texts, and documents from the United States v. Elizabeth Holmes trial, Extend engineer Bo Lau created a website that simulates what it might have been like to rifl"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/fired-openai-safety-researchers-dispute-misconduct-claims-warn-of-chilling-effect/",
    "domain": "大厂 AI 动态",
    "title": "Fired OpenAI safety researchers dispute misconduct claims, warn of chilling effect",
    "url": "https://techcrunch.com/2026/10/08/fired-openai-safety-researchers-dispute-misconduct-claims-warn-of-chilling-effect/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T20:04:26+00:00",
    "summary": "Three fired OpenAI safety researchers dispute allegations of mishandling sensitive information, warning in an open letter that their dismissals are creating a chilling effect on the company’s AI safet"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/watch-the-trailer-for-the-altruists-netflixs-show-about-the-ftx-scandal/",
    "domain": "大厂 AI 动态",
    "title": "Watch the trailer for ‘The Altruists,’ Netflix’s show about the FTX scandal",
    "url": "https://techcrunch.com/2026/10/08/watch-the-trailer-for-the-altruists-netflixs-show-about-the-ftx-scandal/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:30:00+00:00",
    "summary": "A fictionalized Sam Bankman-Fried is coming to your TV screen on November 19."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/ben-affleck-is-an-ai-nerd-and-the-internet-is-impressed/",
    "domain": "大厂 AI 动态",
    "title": "Ben Affleck is an AI nerd, and the internet is impressed",
    "url": "https://techcrunch.com/2026/10/08/ben-affleck-is-an-ai-nerd-and-the-internet-is-impressed/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:20:32+00:00",
    "summary": "Ben Affleck is going viral for his deep knowledge of AI, from neural networks and transformers to open weights. The actor, who sold his AI filmmaking startup to Netflix earlier this year, is proving h"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/",
    "domain": "大厂 AI 动态",
    "title": "Popular AI leaderboard Arena nearly doubles valuation to $3.1B valuation in 10 months",
    "url": "https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:19:45+00:00",
    "summary": "The company behind the popular LMArena leaderboard has raised $200 million led by Lightspeed and Khosla, and is now measuring AI models on alignment issues such as lying."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/openais-revenue-is-reportedly-20-billion-less-than-previously-projected/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s revenue is reportedly $20 billion less than previously projected",
    "url": "https://techcrunch.com/2026/10/08/openais-revenue-is-reportedly-20-billion-less-than-previously-projected/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:19:42+00:00",
    "summary": "It had previously been reported that the AI lab's annualized revenue was some $70 billion, but a new report claims it's a whole lot less than that."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/",
    "domain": "大厂 AI 动态",
    "title": "Google brings agentic AI to Gemini, starting with businesses",
    "url": "https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:18:00+00:00",
    "summary": "Google is turning Gemini into an AI agent that can plan, execute tasks, and work across business apps and systems. The agent can delegate work to subagents, use multiple AI models, and even gets its o"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic changes usage policy to ban model abuse and election interference",
    "url": "https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:16:24+00:00",
    "summary": "Anthropic's updated usage policy explicitly prohibits users from repeatedly abusing Claude in extreme cases, though ordinary frustration and criticism are still allowed. The new rules also address ele"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/openais-math-solutions-arent-meeting-the-fields-standards-yet/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s math solutions aren’t meeting the field’s standards yet",
    "url": "https://techcrunch.com/2026/10/08/openais-math-solutions-arent-meeting-the-fields-standards-yet/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T18:10:55+00:00",
    "summary": "OpenAI's flood of proofs deviated from the guidelines set by a group of mathematical researchers consulted by the frontier lab."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/a-startup-founder-who-served-time-in-prison-is-looking-to-court-an-untapped-market-ex-cons/",
    "domain": "大厂 AI 动态",
    "title": "A startup founder who served time in prison is looking to court an untapped market: ex-cons",
    "url": "https://techcrunch.com/2026/10/08/a-startup-founder-who-served-time-in-prison-is-looking-to-court-an-untapped-market-ex-cons/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T16:45:00+00:00",
    "summary": "Richard Bronson, a former Stratton Oakmont partner who served time in federal prison for securities violations, has launched Commissary Club, a startup that uses AI to help people leaving prison find "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/naturas-smart-ring-puts-ai-agents-on-your-finger/",
    "domain": "大厂 AI 动态",
    "title": "Natura’s $99 smart ring puts AI agents on your finger",
    "url": "https://techcrunch.com/2026/10/08/naturas-smart-ring-puts-ai-agents-on-your-finger/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T16:00:00+00:00",
    "summary": "Natura’s $99 Interface smart ring lets you summon AI agents with the press of a finger to complete tasks, capture thoughts, and control devices — while doubling as a health tracker."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/goodfire-says-its-new-inside-out-monitors-catch-rogue-ai-agents-at-a-fraction-of-the-cost/",
    "domain": "大厂 AI 动态",
    "title": "Goodfire says its new ‘inside-out’ monitors catch rogue AI agents at a fraction of the cost",
    "url": "https://techcrunch.com/2026/10/08/goodfire-says-its-new-inside-out-monitors-catch-rogue-ai-agents-at-a-fraction-of-the-cost/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T16:00:00+00:00",
    "summary": "Goodfire just launched what it says is a cheaper way to keep AI agents in check: Instead of paying a second AI to read everything an agent does, its monitors peek inside the model while it works and o"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/us-bars-microsoft-adobe-and-major-it-firms-from-green-card-program-for-skilled-foreign-workers/",
    "domain": "大厂 AI 动态",
    "title": "US bars Microsoft, Adobe, and major IT firms from green card program for skilled foreign workers",
    "url": "https://techcrunch.com/2026/10/08/us-bars-microsoft-adobe-and-major-it-firms-from-green-card-program-for-skilled-foreign-workers/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T15:42:26+00:00",
    "summary": "The other firms being suspended from the program include Capgemini, Cognizant, HCL, Infosys, Tata, and Wipro."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/elon-musk-questions-ambanis-influence-as-starlink-india-launch-stalls/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk questions Ambani’s influence as Starlink India launch stalls",
    "url": "https://techcrunch.com/2026/10/08/elon-musk-questions-ambanis-influence-as-starlink-india-launch-stalls/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T15:12:59+00:00",
    "summary": "“Is Ambani the real boss of India?” Elon Musk asked as he questioned why Starlink has yet to launch its satellite internet service in the country."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/new-york-alleges-tiktok-gave-teens-children-a-placebo-safety-feature-instead-of-a-real-one/",
    "domain": "大厂 AI 动态",
    "title": "New York alleges TikTok gave teens, children a placebo safety feature instead of a real one",
    "url": "https://techcrunch.com/2026/10/08/new-york-alleges-tiktok-gave-teens-children-a-placebo-safety-feature-instead-of-a-real-one/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T15:06:17+00:00",
    "summary": "New York’s lawsuit against the company is one of more than two dozen cases brought by states accusing the social media giant of designing its platform to encourage addictive use among children."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/asos-confirms-breach-of-customer-data-after-hackers-send-rogue-app-notification/",
    "domain": "大厂 AI 动态",
    "title": "Asos confirms breach of customer data after hackers send rogue app notification",
    "url": "https://techcrunch.com/2026/10/08/asos-confirms-breach-of-customer-data-after-hackers-send-rogue-app-notification/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T15:01:15+00:00",
    "summary": "The hackers alerted the fashion giant's customers through a push notification that said they had \"fully compromised\" the company's cloud storage."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/hear-from-ambrosia-energy-and-bloom-energy-execs-on-where-the-ai-infrastructure-boom-is-creating-opportunity-at-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Hear from Ambrosia Energy and Bloom Energy execs on where the AI infrastructure boom is creating opportunity at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/10/08/hear-from-ambrosia-energy-and-bloom-energy-execs-on-where-the-ai-infrastructure-boom-is-creating-opportunity-at-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T15:00:00+00:00",
    "summary": "Ambrosia Energy CEO Ben Longmier and Bloom Energy SVP Bill Thayer join the Smart Systems Stage at TechCrunch Disrupt. Register now to save up to $100. Grab a second of the same pass to save 50%."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/spotify-is-getting-more-serious-about-selling-enterprise-software/",
    "domain": "大厂 AI 动态",
    "title": "Spotify is getting more serious about selling enterprise software",
    "url": "https://techcrunch.com/2026/10/08/spotify-is-getting-more-serious-about-selling-enterprise-software/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:34:33+00:00",
    "summary": "The company launched technology.spotify.com, a new site that will make its internal tech available to outsiders."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/08/waymo-locks-in-5b-loan-from-blackstone-pimco-to-fuel-robotaxi-expansion/",
    "domain": "大厂 AI 动态",
    "title": "Waymo locks in $5B loan from Blackstone, PIMCO to fuel robotaxi expansion",
    "url": "https://techcrunch.com/2026/10/08/waymo-locks-in-5b-loan-from-blackstone-pimco-to-fuel-robotaxi-expansion/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:16:56+00:00",
    "summary": "This is the first time the Alphabet-owned company has turned to debt financing."
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
    "id": "rss:https://arstechnica.com/cars/2026/10/volkswagens-replacement-for-the-id-4-crossover-is-here/",
    "domain": "大厂 AI 动态",
    "title": "Volkswagen's replacement for the ID.4 crossover is here",
    "url": "https://arstechnica.com/cars/2026/10/volkswagens-replacement-for-the-id-4-crossover-is-here/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T10:00:59+00:00",
    "summary": "The new EV’s digital cockpit can mimic instrument displays from VWs of old."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/spacex-calls-for-better-coordination-in-orbit-after-near-misses-with-starlink/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX calls for better coordination in orbit after near-misses with Starlink",
    "url": "https://arstechnica.com/space/2026/10/spacex-calls-for-better-coordination-in-orbit-after-near-misses-with-starlink/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T21:37:32+00:00",
    "summary": "\"These led to conjunctions of tens of meters to hundreds of meters. Way too close to comfort.\""
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
    "id": "hn:49997175",
    "domain": "股票",
    "title": "The world has nearly burned through its oil stockpile buffer",
    "url": "https://www.reuters.com/business/energy/world-has-nearly-burned-through-its-oil-stockpile-buffer-executives-say-2026-10-06/",
    "source": "geox",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-10-07T18:50:58+00:00",
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
    "id": "hn:50008977",
    "domain": "股票",
    "title": "Frontier AI models outperform analysts on earnings prediction",
    "url": "https://samaya.ai/blog/frontier-ai-models-outperform-human-experts-on-earnings-prediction",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-10-08T17:33:29+00:00",
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
    "points": 502,
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
    "points": 259,
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
    "id": "hn:49981063",
    "domain": "金融",
    "title": "Former German spy chief arrested for attempted treason",
    "url": "https://www.reuters.com/business/finance/former-german-spy-chief-detained-suspicion-espionage-treason-bild-reports-2026-10-06/",
    "source": "semiquaver",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-10-06T16:51:50+00:00",
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
    "points": 125,
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
    "id": "rss:https://arxiv.org/abs/2610.10606",
    "domain": "金融",
    "title": "The Gendered Impacts of Perceived Skin Tone: Evidence from African American Siblings in 1870-1940",
    "url": "https://arxiv.org/abs/2610.10606",
    "source": "Ran Abramitzky, Jacob Conway, Roy Mill, Luke C. D. Stein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.10606v1 Announce Type: new Abstract: We study differences in economic outcomes by perceived skin tone among African Americans using full-count U.S. decennial census data from the late-19th "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10727",
    "domain": "金融",
    "title": "Deep Learning vs. Statistical Models for Multi-Horizon Price Forecasting of Second-Hand Electronics: A Systematic Benchmark",
    "url": "https://arxiv.org/abs/2610.10727",
    "source": "Mateusz Buczy\\'nski, Micha{\\l} Wo\\'zniak, Konrad Kaczy\\'nski, Anna Wr\\'oblewska, Sebastian Kuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.10727v1 Announce Type: new Abstract: Forecasting resale prices of used electronics is critical for subscription-based platforms where pricing errors translate directly into risk. Unlike str"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.11093",
    "domain": "金融",
    "title": "Risk Ceilings and Development Deadlines: Pacing AI under Uncertain Safety Productivity",
    "url": "https://arxiv.org/abs/2610.11093",
    "source": "Li Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.11093v1 Announce Type: new Abstract: Can a regulator promise both a risk ceiling and a development deadline when safety productivity is unknown? A ceiling below the final model's unprotecte"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.11256",
    "domain": "金融",
    "title": "Who Leads and Who Collects:Algorithmic Collusion in Markets of Heterogeneous Language Models",
    "url": "https://arxiv.org/abs/2610.11256",
    "source": "Jun Yeong Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.11256v1 Announce Type: new Abstract: Evidence that pricing algorithms collude comes from markets in which every seller runs the same algorithm. We ask what happens when they do not. Four la"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.11691",
    "domain": "金融",
    "title": "Diffusive Market Impact: A Consistent Microfoundation",
    "url": "https://arxiv.org/abs/2610.11691",
    "source": "Julius F. Bonart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.11691v1 Announce Type: new Abstract: Structural price diffusivity explains many empirical regularities of market impact including the ``square-root law'' and its crossover to a linear regim"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.11822",
    "domain": "金融",
    "title": "Weighted selection from elliptical distributions: a stochastic representation and an application to portfolio separation",
    "url": "https://arxiv.org/abs/2610.11822",
    "source": "Nils Chr Framstad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.11822v1 Announce Type: new Abstract: We represent (weighted-)selection-elliptical distributions as an affine combination of the $q$ selection variables plus an elliptical term whose directi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.11917",
    "domain": "金融",
    "title": "Multi-period Mean-Expectile Portfolio Optimization under Wasserstein Ambiguity: Reformulation, Degeneracy and the Role of the Ground Metric",
    "url": "https://arxiv.org/abs/2610.11917",
    "source": "Rupendra Yadav, Aparna Mehra",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.11917v1 Announce Type: new Abstract: Expectiles are the only law-invariant risk measures that are both coherent and elicitable. Unlike Conditional Value-at-Risk (CVaR), however, they do not"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.12049",
    "domain": "金融",
    "title": "The Myth of Restrictive Working-Time Agreements: Firms' Working-Time Adjustment after Exit from Collective Bargaining",
    "url": "https://arxiv.org/abs/2610.12049",
    "source": "Vinzenz Pyka, Andr\\'e Rieder",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.12049v1 Announce Type: new Abstract: Employers in Germany argue that collective agreements restrict their flexibility concerning working hours. Using data from the IAB Establishment Panel f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.12186",
    "domain": "金融",
    "title": "Microfinance Competition in the Presence of Moneylenders: Theory and Evidence",
    "url": "https://arxiv.org/abs/2610.12186",
    "source": "Shyamal Chowdhury, Prabal Roy Chowdhury, Joeri Smits",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.12186v1 Announce Type: new Abstract: After decades of microfinance expansion and despite charging higher interest rates, moneylenders continue to exist alongside microfinance institutions ("
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.23002",
    "domain": "金融",
    "title": "Real interest rates, exchange rates and growth in three emerging economies: an exploratory analysis of Brazil, India and Nigeria",
    "url": "https://arxiv.org/abs/2410.23002",
    "source": "Hugo Spring-Ragain (HEIP)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2410.23002v2 Announce Type: replace Abstract: This paper studies the dynamic relationships between real growth, the real lending interest rate and the exchange rate in Brazil, India and Nigeria "
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.06410",
    "domain": "金融",
    "title": "Delphos: A reinforcement learning framework for assisting discrete choice model specification",
    "url": "https://arxiv.org/abs/2506.06410",
    "source": "Gabriel Nova, Stephane Hess, Sander van Cranenburgh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2506.06410v4 Announce Type: replace Abstract: We introduce Delphos, a deep reinforcement learning framework for assisting discrete choice model specification process. Delphos aims to support the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.00190",
    "domain": "金融",
    "title": "Deep reinforcement learning for optimal trading with partial information",
    "url": "https://arxiv.org/abs/2511.00190",
    "source": "Andrea Macr\\`i, Sebastian Jaimungal, Fabrizio Lillo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2511.00190v2 Announce Type: replace Abstract: Reinforcement Learning (RL) has attracted increasing interest in financial applications, including optimal trading and execution. However, the use o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.23825",
    "domain": "金融",
    "title": "Trade Liberalization and Product Innovation: The Dynamic Role of Exporting",
    "url": "https://arxiv.org/abs/2603.23825",
    "source": "Sizhong Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2603.23825v3 Announce Type: replace Abstract: How does trade liberalization affect firms' incentives to innovate? We answer this question using China's WTO accession and a dynamic model of firms"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.12151",
    "domain": "金融",
    "title": "RED-2400: A Public Benchmark of Algorithmically-Rejected Trading Events with Outcome Labels",
    "url": "https://arxiv.org/abs/2605.12151",
    "source": "Arati U. Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2605.12151v3 Announce Type: replace Abstract: RED-2400 is a public benchmark of 6,660 algorithmically-rejected trading events from a live Solana decentralised-exchange filter stack, observed con"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07059",
    "domain": "金融",
    "title": "Diffusive in plain sight: An inconspicuous law of market impact",
    "url": "https://arxiv.org/abs/2606.07059",
    "source": "Julius F. Bonart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2606.07059v4 Announce Type: replace Abstract: Decomposing market impact as the difference between realized and counterfactual returns, and requiring both to be diffusive, yields a structural ide"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08232",
    "domain": "金融",
    "title": "Hour-Aware Adaptive Risk Management for Autonomous Memecoin Trading on Solana DEXs: Evidence, Theory, and Design Lessons from a 15-Day Deployment",
    "url": "https://arxiv.org/abs/2606.08232",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2606.08232v4 Announce Type: replace Abstract: We report a 15-day paper-traded autonomous memecoin trading deployment on Solana decentralised exchanges (DEXs), designed as a controlled measuremen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02830",
    "domain": "金融",
    "title": "Outcome-Classified Precision Auditing of Filter Rules in Algorithmic DEX Trading: Evidence from 2,400 Rejection Events",
    "url": "https://arxiv.org/abs/2607.02830",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2607.02830v2 Announce Type: replace Abstract: This paper reports a precision audit of a production filter stack against a 13-day window of post-rejection forward-market observations on Solana DE"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12587",
    "domain": "金融",
    "title": "DYSANOS Generative Dynamic Smooth Arbitrage-free Non-parametric Option Surfaces",
    "url": "https://arxiv.org/abs/2608.12587",
    "source": "Hans Buehler, Blanka Horvath, Anastasis Kratsios, Magnus Wiese",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2608.12587v2 Announce Type: replace Abstract: This article presents with DYSANOS the first generative market model for smooth SANOS option surfaces for all strikes and expiries which are free of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27727",
    "domain": "金融",
    "title": "Sovereign Grassroots Currencies: A CBDC Architecture for Credit and Monetary Policy (Full Version)",
    "url": "https://arxiv.org/abs/2609.27727",
    "source": "Ehud Shapiro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2609.27727v3 Announce Type: replace Abstract: A Central Bank Digital Currency (CBDC) is central-bank money in digital form, held by the public. Leading designs have two limitations: conversion f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.02814",
    "domain": "金融",
    "title": "Convergence of Markovian Iteration for $Z$-Coupled FBSDEs via Gaussian Smoothing",
    "url": "https://arxiv.org/abs/2504.02814",
    "source": "Zhipeng Huang, Cornelis W. Oosterlee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2504.02814v3 Announce Type: replace-cross Abstract: In this paper, we investigate the Markovian iteration method for coupled forward-backward stochastic differential equations (FBSDEs) with drif"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.10758",
    "domain": "金融",
    "title": "Investing Is Compression",
    "url": "https://arxiv.org/abs/2604.10758",
    "source": "Oscar Stiffelman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2604.10758v5 Announce Type: replace-cross Abstract: In 1956 John Kelly wrote a paper at Bell Labs describing the relationship between gambling and Information Theory. What came to be known as th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07122",
    "domain": "金融",
    "title": "Lambda-quantiles under the microscope",
    "url": "https://arxiv.org/abs/2608.07122",
    "source": "Fabio Bellini, Felix-Benedikt Liebrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2608.07122v2 Announce Type: replace-cross Abstract: We study Lambda-quantiles, a generalisation of classical quantiles in which the constant probability level $\\lambda \\in [0,1]$ is replaced by "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.22697",
    "domain": "金融",
    "title": "Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf",
    "url": "https://arxiv.org/abs/2608.22697",
    "source": "Davood Wadi, Yu Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2608.22697v4 Announce Type: replace-cross Abstract: When shopping is delegated to AI agents, it is unclear whether the ranking advantage documented for humans persists. Across 7,000 sessions wit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.04959",
    "domain": "金融",
    "title": "AlphaPADI: Formulaic Alpha Discovery via Pool-Aware Hierarchical Discrete Diffusion",
    "url": "https://arxiv.org/abs/2610.04959",
    "source": "Yanzheng Jin, Pengyang Shao, Yunshan Ma, Haowen Pan, Naixin Zhai, Chen-Hui Song, Fei Shen, Kenji Kawaguchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.04959v2 Announce Type: replace-cross Abstract: Formulaic alpha discovery seeks symbolic expressions that predict cross-sectional asset returns. In deployment, multiple formulas are combined"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.05196",
    "domain": "金融",
    "title": "Measuring Learned Monotone Temporal Aggregation at Matched Admissibility",
    "url": "https://arxiv.org/abs/2610.05196",
    "source": "Yew Lee Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T04:00:00+00:00",
    "summary": "arXiv:2610.05196v2 Announce Type: replace-cross Abstract: Risk regulation imposes directional constraints on scores; we adopt their strict per-input form -- the score monotone non-decreasing in every "
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
    "id": "hn:49769668",
    "domain": "金融",
    "title": "OpenAI and Anthropic oversold AI security breaches",
    "url": "https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/",
    "source": "hei-lima",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-19T19:59:28+00:00",
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
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-16T18:05:30+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
    "title": "Amazon’s AI Resurgence: AWS & Anthropic’s Multi-Gigawatt Trainium Expansion",
    "url": "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-03T20:55:46+00:00",
    "summary": "Two-and-a-half years ago, we flagged a looming “cloud crisis” at AWS. Today, the evidence has mounted. AWS is the crown jewel of the Amazon empire, generating ~60% of group profits, and dominating the"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "domain": "电子信息与芯片",
    "title": "H100 vs GB200 NVL72 Training Benchmarks – Power, TCO, and Reliability Analysis, Software Improvement Over Time",
    "url": "https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-20T04:56:35+00:00",
    "summary": "Frontier model training has pushed GPUs and AI systems to their absolute limits, making cost, efficiency, power, performance per TCO, and reliability central to the discussion on effective training. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "domain": "电子信息与芯片",
    "title": "GPT-5 Set the Stage for Ad Monetization and the SuperApp",
    "url": "https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "source": "Doug OLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-13T00:27:14+00:00",
    "summary": "To many power users (Pro and Plus), GPT5 was a disappointing release. But with closer inspection, the real release is focused on the vast majority of ChatGPT’s users, which is the 700m+ free userbase "
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "domain": "电子信息与芯片",
    "title": "Scaling the Memory Wall: The Rise and Roadmap of HBM",
    "url": "https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-12T01:16:06+00:00",
    "summary": "The first portion of this report will explain HBM, the manufacturing process, dynamics between vendors, KVCache offload, disaggregated prefill decode, and wide / high-rank EP. The rest of the report w"
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "domain": "电子信息与芯片",
    "title": "Robotics Levels of Autonomy",
    "url": "https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "source": "Reyk Knuhtsen",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-30T17:02:25+00:00",
    "summary": "Robots have powered manufacturing for decades, yet they stayed single-purpose and thrived only in perfect settings. Previous attempts at intelligent machines overpromised and underdelivered. But they "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/21/vlsi2025/",
    "domain": "电子信息与芯片",
    "title": "Intel 18A Details & Cost, Future of DRAM 4F2 vs 3D, Backside Power Adoption (or Not), China’s FlipFET, Digital Twins from Atoms to Fabs, and More",
    "url": "https://semianalysis.com/2025/07/21/vlsi2025/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-21T14:23:37+00:00",
    "summary": "Long time readers will recall that SemiAnalysis covers more than just datacenters and AMD. Today we’re back to semiconductors with a tech-focused roundup of the best from this year’s VLSI conference, "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "domain": "电子信息与芯片",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  }
]
```
