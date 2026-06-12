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

- 今日日期：`2026-06-12`
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
  "date": "2026-06-12",
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
    "points": 1063224,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1onb6zwEkk",
    "domain": "AI",
    "title": "【Ai教程】100集（全）从零开始学illustrator软件基础 (Ai2025新手入门实用版)Ai2025零基础入门教程！！！",
    "url": "http://www.bilibili.com/video/av115025985412548",
    "source": "天才AI设计鲨",
    "platform": "bilibili",
    "points": 1025017,
    "published_at": "2025-08-14T11:00:00+00:00",
    "summary": "设计行业5年 是一名资深设计师~PS学习交流 （南极有什么→ 动物 群 ：211582457）\n你的三连是我最大的动力！！你的三连是我最大的动力！！你的三连是我最大的动力！！"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 659619,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV17sAte3Exh",
    "domain": "AI",
    "title": "AI做高质量PPT从写到讲的全流程拆解，一期给你讲透！【旁门左道PPT】",
    "url": "http://www.bilibili.com/video/av114039887759711",
    "source": "旁门左道PPT",
    "platform": "bilibili",
    "points": 601622,
    "published_at": "2025-02-21T04:08:12+00:00",
    "summary": "更新一期2025年最新的Ai做PPT-全流程实操教程！&lt;不是那种一键生成通用型PPT的--！&gt;这次我帮大家把做PPT从写到说的全流程拆解出来了，极致压榨各种Ai工具在各个环节使劲儿，去帮大家做出有内容有分析长得还可以的PPT，全程高能，记得码住再看~"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 390096,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 370554,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1SQo5BAEBo",
    "domain": "AI",
    "title": "trae使用教程【B站最详细，零基础必看！】trae小白入门到精通traeCN教程traeexceltrae项目实战trae安装教程用教程trae开发小程序",
    "url": "http://www.bilibili.com/video/av116458407336746",
    "source": "trae教程",
    "platform": "bilibili",
    "points": 360785,
    "published_at": "2026-04-24T07:10:58+00:00",
    "summary": "trae使用教程trae小白入门到精通traeCN教程traeexceltrae项目实战trae安装教程用trae开发小程序traecn使用教程"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 277554,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 239444,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VEA8zYE6f",
    "domain": "AI",
    "title": "翻遍整个B站，这绝对是2026讲的最好的提示词工程（Prompt Engineering）教程，全程干货无废话！让你少走99%的弯路！AI大模型|LLM",
    "url": "http://www.bilibili.com/video/av116147491964472",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 188672,
    "published_at": "2026-02-28T09:22:09+00:00",
    "summary": "翻遍整个B站，这绝对是2026讲的最好的提示词工程（Prompt Engineering）教程，全程干货无废话！让你少走99%的弯路！AI大模型|LLM"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174141,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 167719,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 166509,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 154874,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 148096,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 133972,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 117924,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1oj7C6wERJ",
    "domain": "AI",
    "title": "你的下一代生产力，何必是电脑？26年热门AI耳机大横评！",
    "url": "http://www.bilibili.com/video/av116696845126394",
    "source": "知音剑客",
    "platform": "bilibili",
    "points": 66110,
    "published_at": "2026-06-05T10:10:30+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1yXE963ERm",
    "domain": "AI",
    "title": "🚀Claude Fable 5将编程门槛被彻底击穿！史上最强大模型真正碾压GPT 5.5！全面实测：SVG动画、流体模拟、自动化APP测试，零基础也能开发项目",
    "url": "http://www.bilibili.com/video/av116724829525887",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 63296,
    "published_at": "2026-06-10T08:32:28+00:00",
    "summary": "视频简介：\nClaude Fable 5将编程门槛被彻底击穿！史上最强大模型真正碾压GPT 5.5！全面实测：SVG动画、流体模拟、自动化APP测试，这个模型对物理世界的理解太可怕了！零基础也能做出完美App\n\n本期视频详细演示了Anthropic最新发布的Claude Fable 5模型的全方位实测！\n\n测试内容包括：几维鸟vs渡渡鸟土星环赛车SVG动画、复合弓开弓放箭物理模拟、可交互黑洞渲染、"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 59970,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1RrZHYqEvm",
    "domain": "AI",
    "title": "Cursor+Figma MCP，自动生成可编辑设计稿",
    "url": "http://www.bilibili.com/video/av114257538650701",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 51882,
    "published_at": "2025-03-31T14:36:31+00:00",
    "summary": "分享了两种Figma MCP。一种是通过获取Figma API key来实现Cursor和Figma的连接，更侧重精准控制。\n.\n因为大多数 Figma 文件都会非常大，如果你想让Cursor精准链接到文件中的特定元素，一般选择这个MCP会更合适。\n.\n另一种则是通过Figma插件形式，通过channel实现与Cursor的连接，更侧重从0到1的设计元素生成，比较适合没有太多设计基础的用户。\n.\n"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 51426,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV15sNiecEZc",
    "domain": "AI",
    "title": "五款AI聚合客户端，这次不用跑来跑去了",
    "url": "http://www.bilibili.com/video/av113983935747114",
    "source": "果核次元",
    "platform": "bilibili",
    "points": 41828,
    "published_at": "2025-02-11T07:01:27+00:00",
    "summary": "全网AI，一网打尽。只要你配置好，直接无敌"
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 37228,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 35265,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27161,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1HFDSBPE7b",
    "domain": "AI",
    "title": "3分钟教你部署ai我的世界陪玩！",
    "url": "http://www.bilibili.com/video/av116390124067729",
    "source": "我叫非主流_",
    "platform": "bilibili",
    "points": 26127,
    "published_at": "2026-04-12T11:45:00+00:00",
    "summary": "这是上期视频的教程，求求大家给个三连把="
  },
  {
    "id": "bvid:BV17wRQBLEZn",
    "domain": "AI",
    "title": "目前B站最全最新用AI驱动Playwright，不会写代码也能搞定的Web自动化测试，从安装到实战1小时上手",
    "url": "http://www.bilibili.com/video/av116543870535035",
    "source": "web自动化测试",
    "platform": "bilibili",
    "points": 25741,
    "published_at": "2026-05-09T09:24:55+00:00",
    "summary": "视频配套籽料都帮你们整理在这啦：https://www.bilibili.com/opus/972885207239622681\r\n基础学习包，配套课件，PDF电子书籍，问题解答等\r\n记得[热词系列_三连]up持续为你们带来更优质的课程教学！"
  },
  {
    "id": "bvid:BV1woEJ6rEi5",
    "domain": "AI",
    "title": "翻遍整个B站，这绝对是2026讲的最好的AI Agent智能体教程，手把手教你从0基础开始搭建企业级Agent智能体，全程干货无废话，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116703220535567",
    "source": "AI学习课堂",
    "platform": "bilibili",
    "points": 24492,
    "published_at": "2026-06-06T12:49:16+00:00",
    "summary": "【视频配套籽料,学习路线、系统学习，实战项目案例、电子书+问题解答问题解答请看”平论区置顶”自取哦】\n视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 21791,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1mkRtBfED9",
    "domain": "AI",
    "title": "终于实现AI自动剪视频！Claudecode太强大了",
    "url": "http://www.bilibili.com/video/av116528183777029",
    "source": "大厂转型人强哥",
    "platform": "bilibili",
    "points": 20235,
    "published_at": "2026-05-06T14:54:06+00:00",
    "summary": "终于实现了 AI 自动化剪辑，分享下我的内容工作流。这条视频也是 Claudecode 给我剪辑的，14分钟视频2分钟剪辑完毕，正常实习生剪辑需要 90分钟"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 18386,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1jYRRBDExF",
    "domain": "AI",
    "title": "让AI直接操作godot开发游戏，免费开源MCP插件",
    "url": "http://www.bilibili.com/video/av116545648860073",
    "source": "Yurineko73",
    "platform": "bilibili",
    "points": 17359,
    "published_at": "2026-05-10T03:00:00+00:00",
    "summary": "因为想找一个好用的mcp工具，结果发现不是要收费就是不可商用，于是借助ai直接搓了一个出来。\n目前已经发布1.0.1版本，在godot asset library搜索 [godot mcp native]即可下载使用，\n也可以去GitHub上下载完整项目 https://github.com/yurineko73/Godot-MCP-Native\n免费开源，可以随意扩展和修改，如果有需要的功能或遇"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 16252,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1DtEm6PEzw",
    "domain": "AI",
    "title": "【全36集】5分钟入门AI视频制作！AI生成视频零基础入门到精通保姆级教程（2026最新）AI视频制作全流程教学！包含所有干货！七天就能从小白到大神！（附工具）",
    "url": "http://www.bilibili.com/video/av116720115128393",
    "source": "AI视频系统课程",
    "platform": "bilibili",
    "points": 13816,
    "published_at": "2026-06-09T13:04:41+00:00",
    "summary": "一个冷知识:点赞是免费的!\n但是可以让辛苦做视频的UP主开心快乐一整天!!!\n持续更新中~评论区获取课程资料哟~求一键三连~谢谢各位观众老爷！！！！"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13598,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1hEVY6jEGT",
    "domain": "AI",
    "title": "最新【Claude pro Max】保姆级充值教程 Claude code国内购买教程 注册+订阅一个视频教会你",
    "url": "http://www.bilibili.com/video/av116657754277772",
    "source": "小轩AI-",
    "platform": "bilibili",
    "points": 12988,
    "published_at": "2026-05-29T12:07:14+00:00",
    "summary": "aipayok.com"
  },
  {
    "id": "bvid:BV1rCJdzFEQg",
    "domain": "AI",
    "title": "让AI帮你干活：WindowsMCP安装和使用！",
    "url": "http://www.bilibili.com/video/av115242814212549",
    "source": "磊哥聊AI",
    "platform": "bilibili",
    "points": 11838,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
  },
  {
    "id": "bvid:BV1yT8qzMEbd",
    "domain": "AI",
    "title": "基于SpringAI开发Java版mcp服务",
    "url": "http://www.bilibili.com/video/av114942720148945",
    "source": "程序员Cafe",
    "platform": "bilibili",
    "points": 11297,
    "published_at": "2025-07-30T15:05:27+00:00",
    "summary": "如何用Java开发一个mcp服务？如何把已有的spingboot微服务改造成mcp服务呢？如何在mcp客户端调用mcp服务？\n今天来一个保姆级教学"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 11187,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1ZSVG6eE3V",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116662284130312",
    "source": "非六于期",
    "platform": "bilibili",
    "points": 10796,
    "published_at": "2026-05-30T07:13:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1iAEE6ZEDq",
    "domain": "AI",
    "title": "【2026全网最新】2026 全网最优 Claude Code 教程！零基础从入门到精通，AI 编程手把手实战教学",
    "url": "http://www.bilibili.com/video/av116719695697025",
    "source": "阿飞教你学编程",
    "platform": "bilibili",
    "points": 9924,
    "published_at": "2026-06-09T10:40:48+00:00",
    "summary": "视频中的安装文档，整合包，模型，工作流，请查看置顶评论获取。"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 8994,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV17b7664ERM",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116696257924741",
    "source": "AI产品实战",
    "platform": "bilibili",
    "points": 7989,
    "published_at": "2026-06-05T07:19:09+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1Y4Gd6LELX",
    "domain": "AI",
    "title": "极简安装！Claude Code+CC switch 连接 Deepseek",
    "url": "http://www.bilibili.com/video/av116634383550090",
    "source": "水哥澎湃",
    "platform": "bilibili",
    "points": 6933,
    "published_at": "2026-05-25T09:00:14+00:00",
    "summary": "本视频分享Claude Code 极简安装 + 连接 Deepseek的完整方案，解决国内用户使用不稳定、收费高的问题。用 Harness（马鞍缰绳）思路通俗讲解核心价值，让大模型拥有本地执行、记忆、任务编排能力。全程无复杂命令，包含 Claude Code 部署、CC switch 安装、Deepseek API 配置、连接测试，一步到位，新手也能轻松搞定。\n\n\n00:00  1-目标\n00:2"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 6741,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6403,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1FXLJ6YELZ",
    "domain": "AI",
    "title": "Cursor无限薅最强大模型claude4.7，gpt5.5使用方法",
    "url": "http://www.bilibili.com/video/av116590041369141",
    "source": "长青来了奥",
    "platform": "bilibili",
    "points": 6197,
    "published_at": "2026-05-17T13:01:58+00:00",
    "summary": "一键三连吧！在主页\n自动回复私信要1000粉丝呜呜呜呜求帮忙"
  },
  {
    "id": "bvid:BV1rhdgBMEK2",
    "domain": "AI",
    "title": "Claude Code + Figma MCP：传统 UI 开发流程已死？",
    "url": "http://www.bilibili.com/video/av116538183124050",
    "source": "犬哥网站",
    "platform": "bilibili",
    "points": 6163,
    "published_at": "2026-05-08T12:00:00+00:00",
    "summary": "▬▬▬▬▬ 🏆️ 犬哥专业服务 🏆️ ▬▬▬▬▬\n网页设计＆数位行销服务 ➜ https://frankknow.com\nWordPress 优质主机：https://frankknow.com/wordpress-hosting/\n\n▬▬▬▬▬ 🏆️ 精选架站系列 🏆️ ▬▬▬▬▬\n新手自学架站（网域＋主机＋WordPress 架站，一次学会）➜ https://frankknow.com/wp"
  },
  {
    "id": "bvid:BV1f5DvB4Eoa",
    "domain": "AI",
    "title": "AI 直接操控 Cocos Creator！78 个自动化工具一键搞定场景搭建 让 AI 接管你的 Cocos Creator 编辑器 | Link CC MC",
    "url": "http://www.bilibili.com/video/av116362978528338",
    "source": "一个凡人鸭",
    "platform": "bilibili",
    "points": 5449,
    "published_at": "2026-04-07T10:40:52+00:00",
    "summary": "让 AI 直接操控 Cocos Creator 编辑器！\nLink CC MCP 是一款 AI 驱动的 Cocos Creator 编辑器自动化插件，通过 MCP 协议连接 Cursor 等 AI 编辑器，提供 78 个编辑器操作工具。\n你可以用自然语言让 AI：\n✦ 创建节点、搭建 UI 层级\n✦ 添加/修改组件、绑定脚本\n✦ 管理场景、资源、预制体\n✦ 截图查看场景效果\n✦ 批量操作、动画生成"
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 471,
    "published_at": "2026-06-02T22:55:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48352939",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark",
    "url": "https://www.nvidia.com/en-us/products/rtx-spark/",
    "source": "shenli3514",
    "platform": "hackernews",
    "points": 427,
    "published_at": "2026-06-01T05:24:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48424605",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is proposing a beast of a CPU system for Windows PCs",
    "url": "https://twitter.com/lemire/status/2062880075117113739",
    "source": "tosh",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-06-06T12:52:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48355720",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft builds MacBook Pro rival with NVIDIA-powered Surface Laptop Ultra",
    "url": "https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/",
    "source": "jbk",
    "platform": "hackernews",
    "points": 286,
    "published_at": "2026-06-01T12:04:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356654",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Cosmos 3",
    "url": "https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 149,
    "published_at": "2026-06-01T13:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48444451",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia partners with LG robotics to build humanoid robots in South Korea",
    "url": "https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/",
    "source": "spwa4",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-06-08T12:25:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356312",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity",
    "url": "https://news.ycombinator.com/item?id=48356312",
    "source": "ismaeel_bashir",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/rebellions-bets-on-memory-centric-architecture-as-it-weighs-ipo-options/",
    "domain": "AI 算力 / 半导体",
    "title": "Rebellions Bets on Memory-Centric Architecture as it Weighs IPO Options",
    "url": "https://www.eetimes.com/rebellions-bets-on-memory-centric-architecture-as-it-weighs-ipo-options/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T22:00:00+00:00",
    "summary": "Rebellions leverages memory-centric AI chip designs with SK Hynix and Samsung to fuel IPO ambitions. The post Rebellions Bets on Memory-Centric Architecture as it Weighs IPO Options appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/gigadevice-introduces-gd32e512-and-gd32e252-mcus-for-optical-modules/",
    "domain": "AI 算力 / 半导体",
    "title": "GigaDevice Introduces GD32E512 and GD32E252 MCUs for Optical Modules",
    "url": "https://www.eetimes.com/gigadevice-introduces-gd32e512-and-gd32e252-mcus-for-optical-modules/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:00:00+00:00",
    "summary": "GigaDevice has introduced the new GD32E512 and GD32E252 series MCUs specifically designed for optical module applications. The post GigaDevice Introduces GD32E512 and GD32E252 MCUs for Optical Modules"
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-targets-data-centers-edge-ai-space/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Targets Data Centers, Edge AI, Space",
    "url": "https://www.eetimes.com/risc-v-targets-data-centers-edge-ai-space/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T13:24:38+00:00",
    "summary": "\"RISC-V is now,\" said Andrea Gallo, CEO of RISC-V International, during his keynote at this week's RISC-V Summit Europe 2026 in Bologna. The post RISC-V Targets Data Centers, Edge AI, Space appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/logistics-leaders-navigate-cost-and-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "Logistics Leaders Navigate Cost and Automation",
    "url": "https://www.eetimes.com/logistics-leaders-navigate-cost-and-automation/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T08:11:49+00:00",
    "summary": "Gartner's VP analyst David Gonzalez shares strategies for profitability and technology in supply chain management. The post Logistics Leaders Navigate Cost and Automation appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/startup-ricursive-to-create-an-end-to-end-ai-model-for-chip-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Startup Ricursive to Create an End-to-End AI Model for Chip Design",
    "url": "https://www.eetimes.com/startup-ricursive-to-create-an-end-to-end-ai-model-for-chip-design/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:26:51+00:00",
    "summary": "“We are definitely not an EDA company,” Ricursive co-founders told EE Times. The post Startup Ricursive to Create an End-to-End AI Model for Chip Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/massive-ai-storage-demand-creates-a-new-memory-wall/",
    "domain": "AI 算力 / 半导体",
    "title": "Massive AI Storage Demand Creates a New Memory Wall",
    "url": "https://www.eetimes.com/massive-ai-storage-demand-creates-a-new-memory-wall/",
    "source": "Alper Ilkbahar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:22:01+00:00",
    "summary": "As AI models scale to trillions of parameters, conventional memory architectures face mounting capacity and efficiency constraints. The post Massive AI Storage Demand Creates a New Memory Wall appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-driven-memory-shortage-upends-it-budgets/",
    "domain": "AI 算力 / 半导体",
    "title": "AI-Driven Memory Shortage Upends IT Budgets",
    "url": "https://www.eetimes.com/ai-driven-memory-shortage-upends-it-budgets/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T07:47:11+00:00",
    "summary": "IT departments find that purchasing servers and computers has become much more difficult because of surging memory prices and shortages. The post AI-Driven Memory Shortage Upends IT Budgets appeared f"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-bans-china-linked-chatgpt-accounts-that-amplified-us-data-center-electricity-price-backlash",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI bans China-linked ChatGPT accounts that amplified US data center electricity price backlash — used AI-generated cartoons to stoke fears over U.S. data center energy costs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-bans-china-linked-chatgpt-accounts-that-amplified-us-data-center-electricity-price-backlash",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T18:48:34+00:00",
    "summary": "OpenAI says it has banned two clusters of ChatGPT accounts it believes are operating from China, and that used its models for covert influence campaigns targeting U.S. tech and policy debates."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/memory-famine-compels-gpu-vendors-to-re-release-2020-graphics-cards-geforce-rtx-3060-and-geforce-rtx-3050-return-to-asian-market",
    "domain": "AI 算力 / 半导体",
    "title": "Memory famine compels GPU vendors to re-release 2020 graphics cards — GeForce RTX 3060 and GeForce RTX 3050 return to Asian market",
    "url": "https://www.tomshardware.com/pc-components/gpus/memory-famine-compels-gpu-vendors-to-re-release-2020-graphics-cards-geforce-rtx-3060-and-geforce-rtx-3050-return-to-asian-market",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:33:50+00:00",
    "summary": "Graphics card manufacturer Manli adds new GeForce RTX 3060 and GeForce RTX 3050 SKUs to its portfolio."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-cuts-manus-off-from-its-internal-systems-as-china-ordered-breakup-of-2-billion-ai-deal-begins",
    "domain": "AI 算力 / 半导体",
    "title": "After spat with Chinese gov't, Meta cuts AI Manus off from its internal systems and is 'sunsetting' platform, report claims — Beijing-ordered breakup of $2 billion AI deal begins",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-cuts-manus-off-from-its-internal-systems-as-china-ordered-breakup-of-2-billion-ai-deal-begins",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T14:47:26+00:00",
    "summary": "Meta has finished separating its operations from Manus, the Chinese-founded agentic AI startup it acquired for roughly $2 billion in December."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-18-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Blade 18 (2026) review: Coming in fast and hot",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-18-2026-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T12:57:02+00:00",
    "summary": "The Razer Blade 18 is a large gaming rig with an 18-inch dual-mode display and strong performance, but it runs hot and is very expensive."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/watching-the-world-cup-online-shouldnt-risk-your-precious-data-or-cost-you-the-earth-save-money-on-these-vpn-deals-now",
    "domain": "AI 算力 / 半导体",
    "title": "Watching the World Cup online is easier with these VPN deals — deals for watching the FIFA World Cup 2026",
    "url": "https://www.tomshardware.com/software/vpn/watching-the-world-cup-online-shouldnt-risk-your-precious-data-or-cost-you-the-earth-save-money-on-these-vpn-deals-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T12:35:37+00:00",
    "summary": "A choice of VPN subscriptions to cover you over the FIFA World Cup 2026 and beyond. Stay safe online for less."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mice/logi-mobi-fold-portable-mouse-bends-in-half-and-slides-neatly-into-your-pocket-wireless-mouse-has-a-battery-life-that-will-last-up-to-a-month",
    "domain": "AI 算力 / 半导体",
    "title": "Logi Mobi Fold portable mouse bends in half and slides neatly into your pocket — wireless mouse has a month-long battery life",
    "url": "https://www.tomshardware.com/peripherals/mice/logi-mobi-fold-portable-mouse-bends-in-half-and-slides-neatly-into-your-pocket-wireless-mouse-has-a-battery-life-that-will-last-up-to-a-month",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T11:20:00+00:00",
    "summary": "Logitech's new Mobi Fold mouse neatly bends in half and can be easily carried around in a pocket, making it ideal for laptop users on the go, and far less bulky than conventional offerings, while havi"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/gaming-pc-deflects-bullet-shot-through-wall-by-neighbour-saving-owners-life-criminal-negligence-charges-for-culprit-who-claims-firearm-was-accidentally-discharged-by-her-dog",
    "domain": "AI 算力 / 半导体",
    "title": "Gaming PC deflects bullet shot through wall by neighbour, saving owner's life — criminal negligence charges for culprit who claims 'firearm was accidentally discharged by her dog'",
    "url": "https://www.tomshardware.com/desktops/pc-building/gaming-pc-deflects-bullet-shot-through-wall-by-neighbour-saving-owners-life-criminal-negligence-charges-for-culprit-who-claims-firearm-was-accidentally-discharged-by-her-dog",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T11:10:01+00:00",
    "summary": "A Redditor's powerful gaming PC just might have just saved their life after its splintered G.Skill RAM sticks diverted a bullet shot through the wall."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/crushing-shortages-force-biwin-into-usd1-86-billion-nand-deal-for-ssds-multi-year-agreement-locks-in-fixed-pricing-as-spot-market-threatens-to-dry-up",
    "domain": "AI 算力 / 半导体",
    "title": "Crushing shortages force Biwin into $1.86 billion NAND deal for SSDs — multi-year agreement locks in fixed pricing as spot market threatens to dry up",
    "url": "https://www.tomshardware.com/pc-components/ssds/crushing-shortages-force-biwin-into-usd1-86-billion-nand-deal-for-ssds-multi-year-agreement-locks-in-fixed-pricing-as-spot-market-threatens-to-dry-up",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T11:00:00+00:00",
    "summary": "Biwin signs a 24-months supply agreement with an unknown NAND maker to get memory worth $1.86 billion."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-ddr5-for-just-usd280-usd100-less-than-elsewhere-in-this-epic-newegg-combo-deal-save-23-percent-on-this-gaming-pc-parts-bundle-featuring-intels-fastest-gaming-cpu-in-years-along-with-a-z890-motherboard-for-just-usd769-99",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB DDR5 for just $280, $100 less than elsewhere, in this epic Newegg combo deal — save 23% on this gaming PC parts bundle featuring Intel's fastest gaming CPU in years, along with a Z890 motherb",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-ddr5-for-just-usd280-usd100-less-than-elsewhere-in-this-epic-newegg-combo-deal-save-23-percent-on-this-gaming-pc-parts-bundle-featuring-intels-fastest-gaming-cpu-in-years-along-with-a-z890-motherboard-for-just-usd769-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:53:46+00:00",
    "summary": "Save $230 on this fast Intel Core Ultra 7 270K Plus CPU with a Z890 motherboard and 32GB of DDR5-6000 memory, now just $769.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/ai-is-set-to-consume-up-to-600-billion-gallons-of-water-by-2030-rising-energy-consumption-primarily-to-blame-as-data-center-power-demands-rise",
    "domain": "AI 算力 / 半导体",
    "title": "AI is set to consume up to 600 billion gallons of water by 2030 — rising energy consumption primarily to blame as data center power demands rise",
    "url": "https://www.tomshardware.com/tech-industry/ai-is-set-to-consume-up-to-600-billion-gallons-of-water-by-2030-rising-energy-consumption-primarily-to-blame-as-data-center-power-demands-rise",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:32:06+00:00",
    "summary": "Direct cooling data center GPUs uses only a fraction of the water required to keep them running, and with plans for future GPUs and rack systems to be even more power hungry, this problem could make d"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/8tb-sd-cards-are-set-to-ship-shortly-after-a-two-year-delay-mind-blowing-storage-at-possibly-bank-breaking-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Massive 8TB SD cards are set to ship 'shortly' after a two-year delay — mind-blowing storage at possibly bank-breaking prices",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/8tb-sd-cards-are-set-to-ship-shortly-after-a-two-year-delay-mind-blowing-storage-at-possibly-bank-breaking-prices",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:30:00+00:00",
    "summary": "Notebookcheck reports that 8TB SD cards will soon hit the retail market, although an exact launch date and pricing remain a mystery."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/we-tested-20-wall-chargers-from-cheap-to-expensive-to-see-what-we-would-find-from-15-140w-with-screens-and-without",
    "domain": "AI 算力 / 半导体",
    "title": "We tested 20 wall chargers, from cheap to expensive, to find the best — from 15W to 140W, here are the chargers that perform the best without overheating and throttling",
    "url": "https://www.tomshardware.com/peripherals/usb/we-tested-20-wall-chargers-from-cheap-to-expensive-to-see-what-we-would-find-from-15-140w-with-screens-and-without",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:10:00+00:00",
    "summary": "We tested the top 20 chargers on the market across different power segments to find out which models provide the most consistent power and the best charging experience without thermal throttling."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/louis-rossman-threatens-to-take-samsung-to-court-over-dead-4tb-990-pro-ssd-after-ssd-maker-failed-to-replace-the-drive-under-warranty",
    "domain": "AI 算力 / 半导体",
    "title": "Louis Rossmann is suing Samsung after firm offers $330 refund for defective SSD while selling the drives on Amazon for $949 — spat over 4TB 990 Pro SSD is headed to court",
    "url": "https://www.tomshardware.com/pc-components/ssds/louis-rossman-threatens-to-take-samsung-to-court-over-dead-4tb-990-pro-ssd-after-ssd-maker-failed-to-replace-the-drive-under-warranty",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:00:00+00:00",
    "summary": "Right to Repair activist Louis Rossman threatens to sue Samsung after the SSD maker failed to replace his dead 990 Pro 4TB SSD under warranty."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nashville-considers-hyperscale-data-center-ban-as-zoo-dispute-escalates",
    "domain": "AI 算力 / 半导体",
    "title": "Brad Paisley joins fight as zoo's dispute with AI data center escalates, petition tops 330,000 signatures — Nashville weighs sweeping hyperscale ban",
    "url": "https://www.tomshardware.com/tech-industry/nashville-considers-hyperscale-data-center-ban-as-zoo-dispute-escalates",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T09:30:00+00:00",
    "summary": "An ongoing fight over a proposed data center sited just 50 yards from Nashville Zoo has escalated further, with the zoo’s land use attorney filing a zoning appeal to overturn permits already approved."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/chipsets/intels-upcoming-z790-and-z990-flagship-chipsets-will-reportedly-consume-up-to-14w-at-peak-load-courtesy-of-more-pcie-5-0-support-nova-lake-motherboards-may-feature-a-22-percent-smaller-pch-than-z890",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's upcoming Z970 and Z990 flagship chipsets will reportedly consume up to 14W at peak load, courtesy of more PCIe 5.0 support — Nova Lake motherboards may feature a 22% smaller PCH than Z890",
    "url": "https://www.tomshardware.com/pc-components/chipsets/intels-upcoming-z790-and-z990-flagship-chipsets-will-reportedly-consume-up-to-14w-at-peak-load-courtesy-of-more-pcie-5-0-support-nova-lake-motherboards-may-feature-a-22-percent-smaller-pch-than-z890",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:35:19+00:00",
    "summary": "The Z990 PCH for Nova Lake motherboards is apparently 22% smaller than Z890, despite featuring a higher power maximum power draw of up to 14W. The leaked picture of the PCH shows a 11.15 x 6.5mm die a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-fires-back-at-nvidia-claiming-256-core-zen-6-venice-cpu-beats-vera-by-3-3x-in-rack-level-performance-company-shares-first-estimated-epyc-venice-benchmarks",
    "domain": "AI 算力 / 半导体",
    "title": "AMD fires back at Nvidia, claiming 256-core Zen 6 'Venice' CPU beats Vera by 3.3x in rack-level performance — company shares first estimated EPYC Venice benchmarks",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-fires-back-at-nvidia-claiming-256-core-zen-6-venice-cpu-beats-vera-by-3-3x-in-rack-level-performance-company-shares-first-estimated-epyc-venice-benchmarks",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:00:29+00:00",
    "summary": "AMD has shared the first official results for its 256-core EPYC Venice CPU, saying it beats Nvidia's Vera by 3.3x in a rack-level deployment."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/google-reportedly-books-intel-for-more-than-3-million-tpus-in-2028",
    "domain": "AI 算力 / 半导体",
    "title": "Google reportedly books Intel for packaging more than 3 million TPUs in 2028 — SK hynix is testing Intel's EMIB packaging for HBM integration",
    "url": "https://www.tomshardware.com/tech-industry/google-reportedly-books-intel-for-more-than-3-million-tpus-in-2028",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T15:49:41+00:00",
    "summary": "Google has placed an order for Intel to build more than 3 million of its TPUs in 2028 after months of testing Intel's advanced packaging."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-heavy-industries-recruits-greek-shipowner-and-supermicro-to-bring-50mw-floating-ai-data-centers-to-market",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Heavy Industries recruits Greek shipowner and Supermicro to bring 50MW floating AI data centers to market — can be powered by solid oxide fuel cells running on liquefied natural gas",
    "url": "https://www.tomshardware.com/tech-industry/samsung-heavy-industries-recruits-greek-shipowner-and-supermicro-to-bring-50mw-floating-ai-data-centers-to-market",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:42:30+00:00",
    "summary": "Besides Samsung Heavy, Japan’s MOL is also building a 73 MW floating data center with Karpowership for a 2027 deployment."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/valve-to-discontinue-physical-steam-gift-cards-by-the-end-of-2026-due-to-scammers-says-nefarious-actors-continue-to-exploit-them-despite-years-of-restrictions",
    "domain": "AI 算力 / 半导体",
    "title": "Valve to discontinue physical Steam gift cards by the end of 2026 due to scammers — says nefarious actors continue to exploit them despite years of restrictions",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/valve-to-discontinue-physical-steam-gift-cards-by-the-end-of-2026-due-to-scammers-says-nefarious-actors-continue-to-exploit-them-despite-years-of-restrictions",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T13:20:50+00:00",
    "summary": "Physical Steam gift cards will no longer be restocked at retail stores, though digital gifting options and existing cards will remain supported."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/overenthusiastic-gta-6-fan-claims-to-be-monitoring-oxygen-levels-acoustic-noise-from-the-bushes-at-rockstar-north-hq-promises-trailer-3-launch-is-imminent-based-on-heightened-activity",
    "domain": "AI 算力 / 半导体",
    "title": "Overenthusiastic GTA 6 fan claims to be monitoring oxygen levels, acoustic noise from the bushes at Rockstar North HQ — promises trailer 3 launch is imminent based on heightened activity",
    "url": "https://www.tomshardware.com/video-games/console-gaming/overenthusiastic-gta-6-fan-claims-to-be-monitoring-oxygen-levels-acoustic-noise-from-the-bushes-at-rockstar-north-hq-promises-trailer-3-launch-is-imminent-based-on-heightened-activity",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T12:11:06+00:00",
    "summary": "Either a dedicated jokester or a deranged fan has been posting advanced surveillance on Reddit in an attempt to predict the next GTA 6 trailer."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/analyzing-tsmcs-fab-expansion-roadmap-multi-fab-n2-ramp-cowos-soic-and-uncorking-bottlenecks",
    "domain": "AI 算力 / 半导体",
    "title": "Analyzing TSMC's fab expansion roadmap — multi-fab N2 ramp, CoWoS, SoIC, and uncorking bottlenecks",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/analyzing-tsmcs-fab-expansion-roadmap-multi-fab-n2-ramp-cowos-soic-and-uncorking-bottlenecks",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T11:41:11+00:00",
    "summary": "TSMC is executing the largest manufacturing expansion in semiconductor industry history that combines simultaneous multi-fab N2 ramps, AI-driven manufacturing optimizations, and massive CoWoS/SoIC pac"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/grab-an-usd800-saving-on-this-rtx-5070-ti-gaming-laptop-from-hp-with-customizable-specs-and-a-20-core-cpu-base-model-costs-just-usd1-999-for-16-inch-rig-with-16gb-ddr5-with-oled-costing-just-usd60-extra",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an $800 saving on this RTX 5070 Ti gaming laptop from HP with customizable specs and a 20-core CPU — base model costs just $1,999 for 16-inch rig with 16GB DDR5, with OLED costing just $60 extra",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/grab-an-usd800-saving-on-this-rtx-5070-ti-gaming-laptop-from-hp-with-customizable-specs-and-a-20-core-cpu-base-model-costs-just-usd1-999-for-16-inch-rig-with-16gb-ddr5-with-oled-costing-just-usd60-extra",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T11:30:01+00:00",
    "summary": "Save $800 on this customizable RTX 5070 Ti HP Omen Max 16 gaming laptop with 16GB DDR5, 1TB SSD, and a 16-inch display."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/gigabytes-sensational-rtx-5070-ti-aorus-prime-5-gaming-pc-has-had-usd500-slashed-off-the-list-price-at-walmart-32gb-of-ddr5-ram-and-2tb-of-storage-for-just-usd1-999",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte's sensational RTX 5070 Ti Aorus Prime 5 gaming PC has had $500 slashed off the list price at Walmart — 32GB of DDR5 RAM, and 2TB of storage for just $1,999",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/gigabytes-sensational-rtx-5070-ti-aorus-prime-5-gaming-pc-has-had-usd500-slashed-off-the-list-price-at-walmart-32gb-of-ddr5-ram-and-2tb-of-storage-for-just-usd1-999",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T11:09:29+00:00",
    "summary": "A powerful gaming desktop with a 16GB RTX 5070 Ti GPU at its heart, discounted by a massive $500 at Walmart right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips",
    "domain": "AI 算力 / 半导体",
    "title": "China drafts $295 billion plan to build national AI data center grid running on 80% homemade silicon — projected 2028 timeline could run into limits of local chip production",
    "url": "https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T10:00:00+00:00",
    "summary": "China is drafting a plan to spend roughly 2 trillion yuan over five years on a nationwide grid of AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-printed-triaxial-electrospray-nozzles-could-revolutionize-drug-and-self-healing-material-manufacturing-mit-developed-technique-makes-cleanroom-fabrication-optional",
    "domain": "AI 算力 / 半导体",
    "title": "3D-printed nozzles could revolutionize drug and self-healing material manufacturing — MIT-developed triaxial electrospray design makes cleanroom fabrication optional",
    "url": "https://www.tomshardware.com/3d-printing/3d-printed-triaxial-electrospray-nozzles-could-revolutionize-drug-and-self-healing-material-manufacturing-mit-developed-technique-makes-cleanroom-fabrication-optional",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T09:30:00+00:00",
    "summary": "MIT's 3D-printed triaxial electrospray nozzles could revolutionize drug and self-healing material manufacturing. By using a relatively inexpensive resin printing approach, the new nozzle fabrication t"
  },
  {
    "id": "hn:48234574",
    "domain": "AI 算力 / 半导体",
    "title": "How do you build a semiconductor company on something that's free?",
    "url": "https://www.siliconimist.com/p/the-open-source-silicon-business",
    "source": "johncole",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-22T11:49:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48431367",
    "domain": "AI 算力 / 半导体",
    "title": "The Russian who invented semiconductors 25 years before the USA",
    "url": "https://www.semidoped.com/p/til-the-man-who-invented-the-future",
    "source": "johncole",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-06-07T03:00:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48220446",
    "domain": "AI 算力 / 半导体",
    "title": "IBM invented semiconductor manufacturing automation",
    "url": "https://spectrum.ieee.org/semiconductor-fabrication",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-05-21T10:39:48+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/indias-2035-chip-ambitions-focus-on-targeted-design-manufacturing-leadership/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s 2035 Chip Ambitions Focus on Targeted Design, Manufacturing Leadership",
    "url": "https://www.eetimes.com/indias-2035-chip-ambitions-focus-on-targeted-design-manufacturing-leadership/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T22:00:00+00:00",
    "summary": "India maps out a bold $150B chip strategy for 2035—see why this time might be different. The post India’s 2035 Chip Ambitions Focus on Targeted Design, Manufacturing Leadership appeared first on EE Ti"
  },
  {
    "id": "rss:https://www.eetimes.com/efinix-rethinking-the-logic-routing-tradeoff-in-fpgas/",
    "domain": "AI 算力 / 半导体",
    "title": "Rethinking the Logic-Routing Tradeoff in FPGAs",
    "url": "https://www.eetimes.com/efinix-rethinking-the-logic-routing-tradeoff-in-fpgas/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T17:00:00+00:00",
    "summary": "Efinix’ exchangeable logic-and-routing technology aims to cut power and die area while enabling memory integration and greater flexibility for AI edge designs. The post Rethinking the Logic-Routing Tr"
  },
  {
    "id": "rss:https://www.eetimes.com/the-concerning-unchecked-rise-of-e2e-ai-in-physical-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "The Concerning, Unchecked Rise of E2E AI in Physical Applications",
    "url": "https://www.eetimes.com/the-concerning-unchecked-rise-of-e2e-ai-in-physical-applications/",
    "source": "Girish Mhatre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T13:24:48+00:00",
    "summary": "Don’t let the bodies pile up The post The Concerning, Unchecked Rise of E2E AI in Physical Applications appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-fable-5-brings-mythos-to-the-masses-anthropics-next-frontier-model-is-state-of-the-art-on-nearly-all-tested-benchmarks",
    "domain": "AI 算力 / 半导体",
    "title": "Claude Fable 5 brings Mythos to the masses — Anthropic's new frontier model is 'state-of-the-art on nearly all tested benchmarks'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-fable-5-brings-mythos-to-the-masses-anthropics-next-frontier-model-is-state-of-the-art-on-nearly-all-tested-benchmarks",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T20:34:10+00:00",
    "summary": "After first announcing its scarily capable Mythos Preview model back in April, Anthropic is releasing a public version of Mythos, called Fable 5, that it says is \"safe for general use.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/microphones/razer-seiren-v3-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Seiren V3 Pro Review: USB, XLR, and 32-bit float",
    "url": "https://www.tomshardware.com/peripherals/microphones/razer-seiren-v3-pro-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T17:45:00+00:00",
    "summary": "Razer's new Seiren V3 Pro is an end-address mic with both USB-C and XLR connectivity, and it also supports 32-bit float."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-warns-ai-self-improvement-could-end-in-lost-human-control",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic's warning over AI self-improvement has a hidden message — accelerating development requires more compute before companies ever risk losing control of frontier AI models",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-warns-ai-self-improvement-could-end-in-lost-human-control",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T17:03:06+00:00",
    "summary": "The company that just a few weeks ago told us that its Mythos model was much too powerful to be released is now saying that we might need to hit the pause button."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/secretlab-atlas-review",
    "domain": "AI 算力 / 半导体",
    "title": "Secretlab Atlas review: The one you’ve been waiting for",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/secretlab-atlas-review",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T17:00:00+00:00",
    "summary": "Secretlab has unveiled its new Atlas task chair with an emphasis on productivity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-weighs-criminal-ban-on-ai-chip-exports-to-all-of-china-as-us-trade-talks-continue",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan weighs criminal ban on AI chip exports to all of China — stricter measures beyond blacklisted firms would make smuggling servers a crime",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-weighs-criminal-ban-on-ai-chip-exports-to-all-of-china-as-us-trade-talks-continue",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T15:53:39+00:00",
    "summary": "Taiwan is considering far stricter export controls that would restrict AI chip sales to every customer in China."
  },
  {
    "id": "hn:48196570",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
    "source": "spectraldrift",
    "platform": "hackernews",
    "points": 962,
    "published_at": "2026-05-19T17:43:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48450142",
    "domain": "大厂 AI 动态",
    "title": "Apple reveals new AI architecture built around Google Gemini models",
    "url": "https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/",
    "source": "unclefuzzy",
    "platform": "hackernews",
    "points": 732,
    "published_at": "2026-06-08T19:14:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48449084",
    "domain": "大厂 AI 动态",
    "title": "Siri AI",
    "url": "https://www.apple.com/apple-intelligence/",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 675,
    "published_at": "2026-06-08T18:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48192224",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils new accessibility features",
    "url": "https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/",
    "source": "interpol_p",
    "platform": "hackernews",
    "points": 726,
    "published_at": "2026-05-19T12:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48233563",
    "domain": "大厂 AI 动态",
    "title": "Steve Wozniak cheered after telling students they have AI – actual intelligence",
    "url": "https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5",
    "source": "signa11",
    "platform": "hackernews",
    "points": 650,
    "published_at": "2026-05-22T09:04:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196867",
    "domain": "大厂 AI 动态",
    "title": "Gemini CLI will stop working from June 18, 2026",
    "url": "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/",
    "source": "primaprashant",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-05-19T18:03:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196609",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni",
    "url": "https://deepmind.google/models/gemini-omni/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 323,
    "published_at": "2026-05-19T17:46:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48272354",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files",
    "source": "Kneenex",
    "platform": "hackernews",
    "points": 264,
    "published_at": "2026-05-25T21:45:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48297467",
    "domain": "大厂 AI 动态",
    "title": "Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS",
    "url": "https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/",
    "source": "ChrisArchitect",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-27T17:24:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373764",
    "domain": "大厂 AI 动态",
    "title": "GitHub Copilot App",
    "url": "https://github.com/features/preview/github-app",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-06-02T17:58:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48475307",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini Is Down",
    "url": "https://www.techradar.com/news/live/gemini-down-june-2026",
    "source": "axsaucedo",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-10T12:28:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48413924",
    "domain": "大厂 AI 动态",
    "title": "Leak Reveals Microsoft Wants Its AI to Be 'Addictive'",
    "url": "https://kotaku.com/microsoft-ai-scout-addictive-satya-nadella-404-media-copilot-2000702924",
    "source": "thm",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-06-05T15:32:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/948890/siri-wont-be-your-ai-girlfriend",
    "domain": "大厂 AI 动态",
    "title": "Siri won’t be your AI girlfriend",
    "url": "https://www.theverge.com/tech/948890/siri-wont-be-your-ai-girlfriend",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T07:00:31+00:00",
    "summary": "Our early testing has already shown that Siri AI knows when to shut up, and that's very much by design. In an interview with Mostly Human, Apple's Craig Federighi said new Siri won't act all sycophant"
  },
  {
    "id": "rss:https://www.theverge.com/tech/948814/amazon-echo-hub-homescreen-redesign",
    "domain": "大厂 AI 动态",
    "title": "Amazon&#8217;s Echo Hub gets a customizable new look and Ring&#8217;s AI features",
    "url": "https://www.theverge.com/tech/948814/amazon-echo-hub-homescreen-redesign",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T22:06:32+00:00",
    "summary": "Amazon's rolling out a free software update for Echo Hub devices that gives the home screen a much-needed update to the interface it launched with in 2024. It had already added Alex Plus AI support, b"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/948204/logitech-mx-master-3s-mouse-sale-deal",
    "domain": "大厂 AI 动态",
    "title": "Logitech’s awesome MX Master 3S mouse drops to under $100",
    "url": "https://www.theverge.com/gadgets/948204/logitech-mx-master-3s-mouse-sale-deal",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T20:00:00+00:00",
    "summary": "The platform-agnostic Logitech MX Master 3S wireless mouse is discounted to $89.99 at Amazon ($30 off), matching the best price we’ve seen so far this year. While it may look like a somewhat ordinary "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/948459/blink-camera-bundle-aeropress-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Blink’s six-piece outdoor camera kit is a great deal under $200",
    "url": "https://www.theverge.com/gadgets/948459/blink-camera-bundle-aeropress-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T18:04:43+00:00",
    "summary": "You can save on a big set of outdoor security cameras ahead of Prime Day. Amazon has a five-pack of Blink cameras with a video doorbell included that’s marked down to $166.99. The bundle includes a Bl"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/948529/roborock-q10-s5-plus-robot-vacuum-mop-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Roborock&#8217;s Q10 S5 Plus robovac is over half off, matching its best price to date",
    "url": "https://www.theverge.com/gadgets/948529/roborock-q10-s5-plus-robot-vacuum-mop-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T17:42:29+00:00",
    "summary": "Even at full price, the Roborock Q10 S5 Plus offers impressive value, boasting features typically reserved for pricier robovac models at a fraction of the price. That&#8217;s especially true today. It"
  },
  {
    "id": "rss:https://www.theverge.com/tech/948534/amazon-data-centers-water-use",
    "domain": "大厂 AI 动态",
    "title": "Amazon&#8217;s data centers used 2.5 billion gallons of water last year",
    "url": "https://www.theverge.com/tech/948534/amazon-data-centers-water-use",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T17:26:57+00:00",
    "summary": "Just after Seattle enacted a one-year data center moratorium that some of Amazon's own employees pushed for, Amazon shared how much water its data centers use, reportedly for the first time. With conc"
  },
  {
    "id": "rss:https://www.theverge.com/policy/948525/cruz-wyden-jawbone-act-censorship",
    "domain": "大厂 AI 动态",
    "title": "The bill that would let Jimmy Kimmel sue Brendan Carr is here",
    "url": "https://www.theverge.com/policy/948525/cruz-wyden-jawbone-act-censorship",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T17:23:02+00:00",
    "summary": "Under a new bipartisan bill, Americans could sue for damages if a government official illegally tries to coerce a social media, AI, or broadcasting company to remove their post - regardless of whether"
  },
  {
    "id": "rss:https://www.theverge.com/21570383/price-matching-policy-apple-google-microsoft",
    "domain": "大厂 AI 动态",
    "title": "Here are the price-matching policies for Best Buy, GameStop, and others",
    "url": "https://www.theverge.com/21570383/price-matching-policy-apple-google-microsoft",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T17:14:28+00:00",
    "summary": "Nothing is more frustrating than buying a new pair of headphones, an OLED TV, or a laptop just to find out that you could have gotten it for cheaper somewhere else just a few days or weeks later. That"
  },
  {
    "id": "rss:https://www.theverge.com/tech/948451/fisa-702-reauthorization-vote-fails-congress-wiretapping-lapse",
    "domain": "大厂 AI 动态",
    "title": "A warrantless wiretap law is about to expire — but surveillance networks aren’t actually ‘going dark’",
    "url": "https://www.theverge.com/tech/948451/fisa-702-reauthorization-vote-fails-congress-wiretapping-lapse",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:03:38+00:00",
    "summary": "Congress has failed to pass a three-week extension of Section 702 of the Foreign Intelligence Surveillance Act (FISA), with the House voting 218-198 against reauthorizing the controversial warrantless"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/947974/waymo-premier-monthly-membership-perks-priority-cash-back",
    "domain": "大厂 AI 动态",
    "title": "Waymo introduces $30-a-month premium tier for riders who want faster pickups",
    "url": "https://www.theverge.com/transportation/947974/waymo-premier-monthly-membership-perks-priority-cash-back",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:00:00+00:00",
    "summary": "Uber One, meet Waymo Premier. The robotaxi operator announced a new $29.99-a-month premium tier for riders who want a more elevated and exclusive autonomous experience. The invite-only membership serv"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/cheaper-faster-and-culturally-aware-avataars-video-ai-is-built-for-indias-scale/",
    "domain": "大厂 AI 动态",
    "title": "Cheaper, faster, and culturally aware, Avataar’s video AI is built for India’s scale",
    "url": "https://techcrunch.com/2026/06/11/cheaper-faster-and-culturally-aware-avataars-video-ai-is-built-for-indias-scale/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:30:00+00:00",
    "summary": "Avataar AI's distilled video model is priced at $0.005 for every second of generation"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/equal-ai-raises-30m-to-screen-calls-so-indians-dont-have-to/",
    "domain": "大厂 AI 动态",
    "title": "Equal AI raises $30M to screen calls so Indians don’t have to",
    "url": "https://techcrunch.com/2026/06/11/equal-ai-raises-30m-to-screen-calls-so-indians-dont-have-to/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:30:00+00:00",
    "summary": "Equal AI said that its AI-powered call assistant now has over a million monthly active users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/theker-just-raised-85m-to-build-the-factory-robot-that-doesnt-specialize-in-anything/",
    "domain": "大厂 AI 动态",
    "title": "Theker just raised $85M to build the factory robot that doesn’t specialize in anything",
    "url": "https://techcrunch.com/2026/06/11/theker-just-raised-85m-to-build-the-factory-robot-that-doesnt-specialize-in-anything/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T01:48:07+00:00",
    "summary": "Unlike humanoid robots designed around a fixed form — think Boston Dynamics — Theker's machines are built to be reconfigured."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/",
    "domain": "大厂 AI 动态",
    "title": "Jeff Bezos’s Prometheus raises $12B to build an ‘artificial general engineer’ for the physical world",
    "url": "https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T01:04:38+00:00",
    "summary": "The new round values the physical AI startup that aims to automate heavy engineering and drug design at $41 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/spacex-officially-prices-shares-at-135-in-the-largest-ipo-ever/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX officially prices shares at $135 in the largest IPO ever",
    "url": "https://techcrunch.com/2026/06/11/spacex-officially-prices-shares-at-135-in-the-largest-ipo-ever/",
    "source": "Tim Fernholz, Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T20:33:10+00:00",
    "summary": "Wits its official share pricing announcement, SpaceX's IPO has begun."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/oracle-warns-of-security-bug-that-hackers-abused-to-breach-100-companies/",
    "domain": "大厂 AI 动态",
    "title": "Oracle warns of security bug that hackers abused to breach 100+ companies",
    "url": "https://techcrunch.com/2026/06/11/oracle-warns-of-security-bug-that-hackers-abused-to-breach-100-companies/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T20:27:25+00:00",
    "summary": "The tech giant warned of a security flaw that a cybercrime gang said it's exploiting as part of a mass-hacking campaign. Google said it notified more than 100 organizations that had potentially vulner"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/spacex-spv-investors-wont-know-their-true-holdings-until-post-ipo-lock-ups-lift/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX SPV investors won’t know their true holdings until post-IPO lock-ups lift",
    "url": "https://techcrunch.com/2026/06/11/spacex-spv-investors-wont-know-their-true-holdings-until-post-ipo-lock-ups-lift/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T19:58:01+00:00",
    "summary": "After SpaceX makes its public debut, lower-tier SPV investors face hidden fees, lengthy payout delays, and the risk of outright fraud."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/bluesky-launches-group-chats-as-company-shifts-focus-to-community-features/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky launches group chats, as company shifts focus to community features",
    "url": "https://techcrunch.com/2026/06/11/bluesky-launches-group-chats-as-company-shifts-focus-to-community-features/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T19:41:05+00:00",
    "summary": "Bluesky's latest feature is group chats, arriving amid a shift in focus on building features for smaller communities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/metas-edits-app-is-getting-an-ai-assistant-and-a-desktop-version/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Edits app is getting an AI assistant and a desktop version",
    "url": "https://techcrunch.com/2026/06/11/metas-edits-app-is-getting-an-ai-assistant-and-a-desktop-version/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T17:30:00+00:00",
    "summary": "By integrating an AI assistant directly into Edits, Meta is aiming to keep creators engaged on Instagram as it continues to compete with TikTok and YouTube for creators' attention."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/coinbase-debuts-mcp-for-agent-trading/",
    "domain": "大厂 AI 动态",
    "title": "Coinbase’s new tool can help agents trade and pay for premium research",
    "url": "https://techcrunch.com/2026/06/11/coinbase-debuts-mcp-for-agent-trading/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T17:00:00+00:00",
    "summary": "Coinbase's agent can use x402 protocol to get access to data and APIs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/quantum-spaces-military-spac-is-trying-to-catch-spacexs-ipo-wave/",
    "domain": "大厂 AI 动态",
    "title": "Quantum Space’s military SPAC is trying to catch SpaceX’s IPO wave",
    "url": "https://techcrunch.com/2026/06/11/quantum-spaces-military-spac-is-trying-to-catch-spacexs-ipo-wave/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:59:28+00:00",
    "summary": "Quantum Space says SPACs aren't dead as it seeks a $1.2 billion deal to build military spacecraft."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/deezers-new-tool-can-identify-ai-music-from-spotify-apple-music-and-others/",
    "domain": "大厂 AI 动态",
    "title": "Deezer’s new tool can identify AI music from Spotify, Apple Music, and others",
    "url": "https://techcrunch.com/2026/06/11/deezers-new-tool-can-identify-ai-music-from-spotify-apple-music-and-others/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:36:20+00:00",
    "summary": "Deezer introduced a tool that scans playlists from Spotify, Apple Music, and other platforms to identify AI music."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/social-media-ban-children-countries-list/",
    "domain": "大厂 AI 动态",
    "title": "These are the countries moving to ban social media for children",
    "url": "https://techcrunch.com/2026/06/11/social-media-ban-children-countries-list/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:17:50+00:00",
    "summary": "Australia was the first country to issue a ban in late 2025, aiming to reduce the pressures and risks that young users may face on social media, including cyberbullying, social media addiction, and ex"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/waymo-launches-a-loyalty-program-with-10-cash-back-and-free-cancellations/",
    "domain": "大厂 AI 动态",
    "title": "Waymo launches a loyalty program with 10% cash back and free cancellations",
    "url": "https://techcrunch.com/2026/06/11/waymo-launches-a-loyalty-program-with-10-cash-back-and-free-cancellations/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:00:23+00:00",
    "summary": "Members of the program, called \"Waymo Premier,\" will have to pony up $29.99 per month."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/pools-new-app-turns-your-screenshots-into-a-searchable-memory-bank/",
    "domain": "大厂 AI 动态",
    "title": "Pool’s new app turns your screenshots into something useful",
    "url": "https://techcrunch.com/2026/06/11/pools-new-app-turns-your-screenshots-into-a-searchable-memory-bank/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T15:30:00+00:00",
    "summary": "Pool's new app automatically sorts screenshots into personalized collections, tracks down the original links behind saved content, and helps you rediscover products, recipes, travel ideas, and other t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/microsoft-taps-alt-carbon-in-sign-of-indias-growing-rile-in-carbon-removal/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft taps Alt Carbon in sign of India’s growing role in carbon removal",
    "url": "https://techcrunch.com/2026/06/11/microsoft-taps-alt-carbon-in-sign-of-indias-growing-rile-in-carbon-removal/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T15:00:00+00:00",
    "summary": "Alt Carbon said the agreement followed more than a year of scientific review and due diligence, with Microsoft requiring additional verification and data-sharing measures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/doordashs-new-ai-chatbot-lets-you-order-with-prompts-and-photos/",
    "domain": "大厂 AI 动态",
    "title": "DoorDash’s new AI chatbot lets you order with prompts and photos",
    "url": "https://techcrunch.com/2026/06/11/doordashs-new-ai-chatbot-lets-you-order-with-prompts-and-photos/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T14:23:43+00:00",
    "summary": "The new chatbot, called Ask DoorDash, allows users to search the app for what they're looking for in their own words instead of having to scroll through restaurants and stores to build a cart."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/endurance-energy-raises-54m-to-harness-a-massive-untapped-energy-source/",
    "domain": "大厂 AI 动态",
    "title": "Endurance Energy raises $54M to harness a massive untapped energy source",
    "url": "https://techcrunch.com/2026/06/11/endurance-energy-raises-54m-to-harness-a-massive-untapped-energy-source/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T14:00:12+00:00",
    "summary": "SpaceX alumni Andrew Redd is betting the ocean has vast amounts of untapped geothermal energy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/south-korea-hits-coupang-with-400m-fine-for-data-breach-that-affected-millions/",
    "domain": "大厂 AI 动态",
    "title": "South Korea hits Coupang with $400M+ fine for data breach that affected millions",
    "url": "https://techcrunch.com/2026/06/11/south-korea-hits-coupang-with-400m-fine-for-data-breach-that-affected-millions/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T13:18:51+00:00",
    "summary": "South Korean authorities issued the record-breaking fine following a data breach that affected over 30 million customers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/11/anthropic-taps-tcs-to-scale-its-enterprise-ai-deployments/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic taps TCS to scale its enterprise AI deployments",
    "url": "https://techcrunch.com/2026/06/11/anthropic-taps-tcs-to-scale-its-enterprise-ai-deployments/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T11:48:55+00:00",
    "summary": "The partnership will see TCS creating a business unit focused on deploying Anthropic's AI models to its customers."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-ben-bajarin-about-apple-ai-and-compute/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Ben Bajarin About Apple, AI, and Compute",
    "url": "https://stratechery.com/2026/an-interview-with-ben-bajarin-about-apple-ai-and-compute/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T10:00:00+00:00",
    "summary": "An interview with Ben Bajarin about WWDC and the status of the AI compute industry."
  },
  {
    "id": "rss:https://stratechery.com/2026/fable-5-anthropic-alignment-ai-tiers/",
    "domain": "大厂 AI 动态",
    "title": "Fable 5, Anthropic Alignment, AI Tiers",
    "url": "https://stratechery.com/2026/fable-5-anthropic-alignment-ai-tiers/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T10:00:00+00:00",
    "summary": "Fable 5 is the public version of Mythos, and while it is very capable it sets some troubling new precedents."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/ted-cruz-and-ron-wyden-try-to-fight-censorship-with-bipartisan-jawbone-act/",
    "domain": "大厂 AI 动态",
    "title": "Ted Cruz and Ron Wyden try to fight censorship with bipartisan JAWBONE Act",
    "url": "https://arstechnica.com/tech-policy/2026/06/ted-cruz-and-ron-wyden-try-to-fight-censorship-with-bipartisan-jawbone-act/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T19:31:37+00:00",
    "summary": "Cruz/Wyden bill would help Americans sue federal officials over censorship."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/iot-gadget-firm-acurite-delays-forced-app-migration-due-to-new-apps-shortfalls/",
    "domain": "大厂 AI 动态",
    "title": "AcuRite admits new app falls short, delays old app’s May shutdown to fix problems",
    "url": "https://arstechnica.com/gadgets/2026/06/iot-gadget-firm-acurite-delays-forced-app-migration-due-to-new-apps-shortfalls/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T19:08:54+00:00",
    "summary": "The old app \"still needs to be retired,\" AcuRite tells us."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/after-nearly-breaking-nasas-deep-space-network-worked-well-on-artemis-ii/",
    "domain": "大厂 AI 动态",
    "title": "After nearly breaking, NASA's Deep Space Network \"worked well\" on Artemis II",
    "url": "https://arstechnica.com/space/2026/06/after-nearly-breaking-nasas-deep-space-network-worked-well-on-artemis-ii/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T18:34:01+00:00",
    "summary": "\"Some missions are using more than what their paperwork would say.\""
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/whats-so-special-about-a-formula-1-driver-in-the-loop-simulator/",
    "domain": "大厂 AI 动态",
    "title": "F1 teams spend millions on their simulators—what makes them different?",
    "url": "https://arstechnica.com/cars/2026/06/whats-so-special-about-a-formula-1-driver-in-the-loop-simulator/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T18:18:12+00:00",
    "summary": "Latency, bandwidth, and fidelity all matter when you're chasing milliseconds."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/did-iron-age-britons-remove-brains-of-the-dead/",
    "domain": "大厂 AI 动态",
    "title": "Did Iron Age Britons remove brains of the dead?",
    "url": "https://arstechnica.com/science/2026/06/did-iron-age-britons-remove-brains-of-the-dead/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T17:21:53+00:00",
    "summary": "Archaeologists found apparent scrape marks inside a skull; long bones may have been sharpened into tools."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/06/this-cannot-continue-xbox-leaders-lay-out-hard-truths-behind-sagging-brand/",
    "domain": "大厂 AI 动态",
    "title": "\"This cannot continue\": Xbox leaders lay out \"hard truths\" behind sagging brand",
    "url": "https://arstechnica.com/gaming/2026/06/this-cannot-continue-xbox-leaders-lay-out-hard-truths-behind-sagging-brand/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T13:56:30+00:00",
    "summary": "Brutal self-assessment paints a picture of a Microsoft gaming division in crisis."
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 1060,
    "published_at": "2026-06-04T22:48:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48455233",
    "domain": "股票",
    "title": "We Think the SpaceX IPO Is Overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued?content_id=20768396545",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 263,
    "published_at": "2026-06-09T01:56:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48314363",
    "domain": "股票",
    "title": "Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions",
    "url": "https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/",
    "source": "ianrahman",
    "platform": "hackernews",
    "points": 236,
    "published_at": "2026-05-28T19:43:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373909",
    "domain": "股票",
    "title": "Morningstar values SpaceX at $780B, half its IPO target",
    "url": "https://www.reuters.com/business/media-telecom/morningstar-values-spacex-780-billion-half-its-ipo-target-2026-06-02/",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 211,
    "published_at": "2026-06-02T18:09:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210226",
    "domain": "股票",
    "title": "OpenAI Is Preparing to File for an IPO Soon",
    "url": "https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 206,
    "published_at": "2026-05-20T16:24:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48134429",
    "domain": "股票",
    "title": "Sam Altman's Business Dealings Under GOP Scrutiny Ahead of OpenAI's IPO",
    "url": "https://www.wsj.com/tech/ai/sam-altmans-business-dealings-under-gop-scrutiny-ahead-of-openais-ipo-52c1cc4d",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 199,
    "published_at": "2026-05-14T12:27:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48446310",
    "domain": "股票",
    "title": "Italy's Bending Spoons, owner of AOL and Vimeo, files for Nasdaq IPO",
    "url": "https://www.reuters.com/legal/transactional/italys-bending-spoons-files-us-ipo-2026-06-08/",
    "source": "mmarian",
    "platform": "hackernews",
    "points": 123,
    "published_at": "2026-06-08T15:04:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48394034",
    "domain": "股票",
    "title": "The SpaceX IPO will be the theft of the century",
    "url": "https://montanaskeptic.substack.com/p/the-spacex-ipo-will-be-the-theft",
    "source": "400thecat",
    "platform": "hackernews",
    "points": 142,
    "published_at": "2026-06-04T04:52:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48217052",
    "domain": "股票",
    "title": "OpenAI to confidentially file for IPO as soon as Friday",
    "url": "https://www.cnbc.com/2026/05/20/openai-ipo-filing.html",
    "source": "doppp",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-05-21T02:24:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48499349",
    "domain": "股票",
    "title": "StonkRider – Ride any stock chart",
    "url": "https://stonkrider.com/",
    "source": "nreece",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-12T02:58:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48385866",
    "domain": "股票",
    "title": "SpaceX's IPO is a disaster waiting to happen for your pension fund",
    "url": "https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/",
    "source": "anonymousDan",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3774517",
    "domain": "股票",
    "title": "铠侠超越丰田，成为日本市值第一",
    "url": "https://wallstreetcn.com/articles/3774517",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T06:55:41+00:00",
    "summary": "这一跃升源于AI驱动的存储芯片需求爆发——铠侠预计2027财年营业利润将达约7万亿日元，是丰田目标的两倍以上。铠侠仅用一年时间从市值第169位升至第一，标志着日本资本市场重心正从传统制造业向半导体科技转移。"
  },
  {
    "id": "wscn:3774518",
    "domain": "股票",
    "title": "华为推出HarmonyOS 7，宣布鸿蒙智能向Agent架构全面演进",
    "url": "https://wallstreetcn.com/articles/3774518",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T06:54:50+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3774511",
    "domain": "股票",
    "title": "“前路依然坎坷”！高盛首席美股策略师：最近的震荡不是结束，而是更大波动的开始",
    "url": "https://wallstreetcn.com/articles/3774511",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T06:32:27+00:00",
    "summary": "高盛首席美股策略师Ben Snider维持标普500年底8000点目标，但发出明确警告：市场已录得近50年最剧烈反弹，高杠杆交易叠加极度收窄的市场广度，令波动率居高难下；AI基础设施独揽今年标普500半数盈利增长，集中风险持续积聚——近期震荡不过是序章。"
  },
  {
    "id": "wscn:3774503",
    "domain": "股票",
    "title": "美国30年期国债拍卖遇冷：海外需求骤降，交易商被迫接盘",
    "url": "https://wallstreetcn.com/articles/3774503",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T06:10:15+00:00",
    "summary": "美国最新30年期国债拍卖表现疲软，出现1.2个基点尾差。为2025年8月以来最大。间接投标人占比骤降至59.95%，创近期新低，交易商被迫接盘14.74%，创近一年新高。PPI数据强劲及资金流向私募资产，被认为是需求走弱的主因，市场对美国长端国债需求前景的疑虑加深。"
  },
  {
    "id": "wscn:3774502",
    "domain": "股票",
    "title": "AI材料短缺蔓延：英伟达亲自下场抢购HVLP4铜箔，2026年缺口达1500吨",
    "url": "https://wallstreetcn.com/articles/3774502",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T06:01:55+00:00",
    "summary": "AI供应链博弈已蔓延至最上游。继T-glass玻纤布告急后，HVLP4铜箔正成为2026年新瓶颈——预计缺口1500吨，2027年扩至2500吨。英伟达罕见绕过CCL厂商，直接锁定铜箔与玻纤布产能，并向谷歌、AWS、Meta施压协同备货。供需失衡短期难解，少数掌握关键材料产能的供应商坐拥极强议价权。"
  },
  {
    "id": "wscn:3774509",
    "domain": "股票",
    "title": "企业级AI，工程比模型更接近价值",
    "url": "https://wallstreetcn.com/articles/3774509",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T05:59:27+00:00",
    "summary": "Harness对于垂类Agent比模型更重要。"
  },
  {
    "id": "wscn:3774508",
    "domain": "股票",
    "title": "SK海力士、三星、台积电同时被限！华尔街大行限制对冲基金对亚洲芯片股的杠杠押注",
    "url": "https://wallstreetcn.com/articles/3774508",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T05:41:39+00:00",
    "summary": "全球六大顶级投行联手出击——花旗、摩根大通、高盛等机构已将韩国芯片股互换融资利率从年初的SOFR+200bp骤升至接近15%，摩根士丹利更直接关闭新增订单渠道。这场围堵行动的背后，是SK海力士年内三倍涨幅、三星涨逾175%所积聚的巨大回调风险，叠加SpaceX 750亿美元IPO抢占资产负债表空间。"
  },
  {
    "id": "wscn:3774505",
    "domain": "股票",
    "title": "“智能体最后的考试”，Fable 5竟然不敌GPT 5.5",
    "url": "https://wallstreetcn.com/articles/3774505",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T05:38:22+00:00",
    "summary": "UC伯克利发布考查AI真实工作能力的新基准测试ALE。结果显示：此前公认最强的Claude Fable 5通过率（22%）不敌GPT-5.5（24%），且耗费成本是其数倍；在最高难度任务下两者更是双双挂零。这揭示出AI“做题学霸≠干活能手”，目前最强智能体应对真实复杂工作依然拉胯。"
  },
  {
    "id": "wscn:3774506",
    "domain": "股票",
    "title": "影子市场：SpaceX上市首日预期大涨超35%，估值或突破2万亿美元",
    "url": "https://wallstreetcn.com/articles/3774506",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T05:28:36+00:00",
    "summary": "在线券商IG International提供的衍生品将SpaceX市值定价于2.4万亿美元，较每股135美元的IPO发行价及对应的1.77万亿美元估值，隐含涨幅超过35%。分析师将此次IPO前交易定性为该平台\"迄今最受追捧\"，并表示需求之旺盛\"即便估值看起来已然偏高\"亦未见消退。"
  },
  {
    "id": "wscn:3774504",
    "domain": "股票",
    "title": "美股两倍做多中际旭创基金，预计两个月后上市！",
    "url": "https://wallstreetcn.com/articles/3774504",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T05:20:03+00:00",
    "summary": "6月12日早盘，中际旭创一度高开近5%。同时，海外也传来一则利好。近日，美国市场开发了一只两倍做多中际旭创的产品。该产品由ProShares基金运作。该款产品目前仍处于募集阶段，预计两个月后上市。"
  },
  {
    "id": "wscn:3774486",
    "domain": "股票",
    "title": "中金：AI资本开支是美元流动性的“新水源”",
    "url": "https://wallstreetcn.com/articles/3774486",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:08:48+00:00",
    "summary": "中金认为，美元流动性引擎正经历“大切换”：美联储扩表与财政赤字驱动的外生货币时代落幕，AI资本开支驱动的内生货币扩张崛起，成为流动性“新水源”。这将增强经济韧性与通胀粘性，并推动资产分化：依赖放水的资产承压，而AI等先进生产力资产有望乘势而起。"
  },
  {
    "id": "wscn:3774489",
    "domain": "股票",
    "title": "A股三大股指均涨超1%，有色金属掀涨停潮，商业航天爆发，恒指涨逾2%，科网股普涨",
    "url": "https://wallstreetcn.com/articles/3774489",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:07:23+00:00",
    "summary": "盘面上，个股呈现普涨态势，沪深京三市超4500股飘红，上午半天成交2.07万亿。沪深两市半日成交额2.06万亿，较上个交易日放量4656亿。板块方面，金属、航空航天双主线引领市场，石化、非银金融、工程机械板块活跃，紫金矿业、洛阳钼业、万华化学、中航成飞、宏桥控股等核心标的飙升。新易盛明显承压，拖累中际旭创、天孚通信。"
  },
  {
    "id": "wscn:3774499",
    "domain": "股票",
    "title": "报道：美伊就谅解备忘录文本达成共识，仍需最终批准，将延长停火60天",
    "url": "https://wallstreetcn.com/articles/3774499",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T03:53:08+00:00",
    "summary": "报道称美伊就谅解备忘录达成初步协议，协议由卡塔尔与巴基斯坦斡旋，停火延长60天并启动正式核谈判。核问题上，伊朗承诺永不谋求核武，高浓缩铀将在监督下降纯处理。经济层面，海峡重开后伊朗获60天临时制裁豁免，冻结资产处置仍存争议。然而伊朗外交部否认协议已定，最终落地仍存不确定性。"
  },
  {
    "id": "wscn:3774480",
    "domain": "股票",
    "title": "如果SpaceX失败，这个基金就不存在了——Founders Fund 6亿美元豪赌，赢回了500亿",
    "url": "https://wallstreetcn.com/articles/3774480",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T03:38:09+00:00",
    "summary": "Founders Fund前合伙人Brian Singerman在播客中系统阐述其投资哲学：98%的决策取决于创始人实力，核心逻辑是\"以最优价格将最多资金投入最好的公司\"，摒弃分散投资教条。他坦言若SpaceX失败，Founders Fund将不复存在，押注马斯克源于其不可替代的CEO+CTO双重能力。"
  },
  {
    "id": "wscn:3774497",
    "domain": "股票",
    "title": "突发！SK海力士清州工厂再度起火，3600人紧急疏散",
    "url": "https://wallstreetcn.com/articles/3774497",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T03:31:13+00:00",
    "summary": "6月12日上午，SK海力士清州工厂气体室再度起火，约3600名员工紧急疏散，火由现场人员自行扑灭，目前无伤亡、无气体泄漏，但生产设备是否受影响仍在核查。这是11天内同一园区第二次发生气体室火灾。M15与M15X工厂是SK海力士核心芯片产能所在。"
  },
  {
    "id": "wscn:3774496",
    "domain": "股票",
    "title": "BMO上调标普500目标至7850点：强劲盈利撑起牛市逻辑，通胀或成2026年最大变数",
    "url": "https://wallstreetcn.com/articles/3774496",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T03:28:59+00:00",
    "summary": "盈利增速创1980年以来历史罕见水平，BMO上调标普500目标价至7850点，较当前隐含8%涨幅。但首席策略师Trahan发出双面预警：强劲盈利或推动指数提前突破目标，然而今年秋季核心通胀加速或将侵蚀涨幅，届时通胀叙事甚至可能盖过AI热度。"
  },
  {
    "id": "wscn:3774498",
    "domain": "股票",
    "title": "享界G9官宣：以破圈之姿再造增长极",
    "url": "https://wallstreetcn.com/articles/3774498",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T03:02:42+00:00",
    "summary": "6月11日，享界G9正式官宣。\n从公示信息看，享界G9全系标配华为乾崑智驾，车顶搭载华为自研 896..."
  },
  {
    "id": "wscn:3774493",
    "domain": "股票",
    "title": "植田住院，内田救场：下周这场45分钟记者会，可能决定下半年的市场走向",
    "url": "https://wallstreetcn.com/articles/3774493",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T02:54:47+00:00",
    "summary": "2024年8月，日央行一次25基点加息引发全球套利交易平仓潮。22个月后，历史正在复刻：仓位回到踩踏前水平，日央行再度加息25基点——但这次，行长植田和男因病缺席，\"鸽派救火队长\"内田真一将独自面对全球媒体。在百亿空头压顶、套利安全垫腰斩的当下，任何沟通偏差都可能引爆连环踩踏。这45分钟，将是今年全球市场最危险的时刻。"
  },
  {
    "id": "wscn:3774491",
    "domain": "股票",
    "title": "黄金的三重压制：加息预期、央行抛售与IPO热潮",
    "url": "https://wallstreetcn.com/articles/3774491",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T02:37:54+00:00",
    "summary": "黄金正遭遇近十年最惨季度：加息预期逆转推高持金机会成本，土耳其、俄罗斯被迫抛售200亿美元储备加剧供给压力，SpaceX等科技巨头IPO更大举分流投资者资金。三重压力叠加之下，金价跌破4100美元，昔日\"避险王者\"的多头叙事正面临严峻考验。"
  },
  {
    "id": "wscn:3774421",
    "domain": "股票",
    "title": "拥挤交易撞上日本加息：日元套利交易会否再现踩踏？",
    "url": "https://wallstreetcn.com/premium/articles/3774421?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T02:36:07+00:00",
    "summary": "尽管日元套利交易仓位拥挤且日本加息在即，但汇率驱动逻辑未变，踩踏式平仓风险不大。"
  },
  {
    "id": "hn:48452224",
    "domain": "股票",
    "title": "OpenAI Confidentially Files for IPO",
    "url": "https://www.cnbc.com/2026/06/08/openai-confidentially-files-for-ipo-prepping-wall-street-for-ai-debut.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-08T21:16:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48193111",
    "domain": "股票",
    "title": "Anthropic Is Preparing for IPO and We Should Be Worried",
    "url": "https://www.vincentschmalbach.com/anthropic-ipo-developers-should-be-worried-v2/",
    "source": "vincent_s",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-05-19T13:30:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451099",
    "domain": "股票",
    "title": "Why Morningstar believes the SpaceX IPO is overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued",
    "source": "ForHackernews",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-08T20:07:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390053",
    "domain": "股票",
    "title": "Iran war drains US oil stocks to lowest level since 2004",
    "url": "https://www.ft.com/content/d0be73c8-b8d8-4ffd-874e-e97a6ecffef7",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-06-03T21:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48404734",
    "domain": "股票",
    "title": "Fidelity lowers SpaceX IPO entry requirement from $500,000 to just $2,000",
    "url": "https://finance.yahoo.com/markets/stocks/articles/fidelity-cuts-spacex-ipo-eligibility-183319186.html",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-04T21:15:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48231815",
    "domain": "股票",
    "title": "SpaceX not the behemoth everyone thought",
    "url": "https://www.axios.com/2026/05/21/spacex-ipo-musk-ai",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-05-22T04:03:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436328",
    "domain": "股票",
    "title": "Musk's SpaceX IPO Narrative Is a Whole New Level of Bullshit",
    "url": "https://text.tchncs.de/chronik-des-laufenden-wahnsinns/h1elon-musk-has-spouted-his-fair-share-of-bullshit-but-his-latest-claims-about",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-07T16:24:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48419956",
    "domain": "股票",
    "title": "Nasdaq falls 4% and suffers worst day since April 2025 traders flee chip stocks",
    "url": "https://www.cnbc.com/2026/06/04/stock-market-today-live-updates.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-06T00:02:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48391046",
    "domain": "股票",
    "title": "We Uncovered a Hidden Wealth Transfer in the SpaceX IPO. You're Holding the Bag [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "CharlesW",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-03T22:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229528",
    "domain": "股票",
    "title": "The SpaceX IPO It's Worse Than You Think [video]",
    "url": "https://www.youtube.com/watch?v=-X6YzlY_8tM",
    "source": "ZeljkoS",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-05-21T22:19:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48359035",
    "domain": "股票",
    "title": "Anthropic Files to Go Public, Setting Stage for Huge I.P.O.",
    "url": "https://www.nytimes.com/2026/06/01/technology/anthropic-ipo.html",
    "source": "jbegley",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-06-01T16:27:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48382926",
    "domain": "股票",
    "title": "Goldman Sachs CEO says markets in 'greed' mode as AI companies seek billions",
    "url": "https://www.cnbc.com/2026/06/02/goldman-ceo-david-solomon-greed-mode-ai-firms-ipos.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-03T12:08:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48369063",
    "domain": "股票",
    "title": "Elon Musk Laid Out 602 Goals. We Counted How Many He Hit",
    "url": "https://www.nytimes.com/interactive/2026/06/02/technology/elon-musk-promises-spacex-ipo.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-02T11:56:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48354214",
    "domain": "股票",
    "title": "How Not to Buy SpaceX Stock (It's Harder Than You Think)",
    "url": "https://cranberries.medium.com/how-not-to-buy-spacex-stock-its-harder-than-you-think-a37610cb8bd3",
    "source": "clktmr",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-01T08:50:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48343303",
    "domain": "股票",
    "title": "The SpaceX IPO is great for Elon Musk and terrible for you",
    "url": "https://www.theverge.com/ai-artificial-intelligence/940001/elon-musk-spacex-ipo-ai",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-31T05:34:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48383625",
    "domain": "股票",
    "title": "Dell inks $9.7B Pentagon contract after Trump acquires stock",
    "url": "https://www.washingtonpost.com/politics/2026/05/28/dell-inks-97-billion-pentagon-contract-after-trump-acquires-stock-praises-company/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-03T13:19:10+00:00",
    "summary": ""
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
    "id": "hn:48368083",
    "domain": "股票",
    "title": "Ask HN: What is your opinion on index rule changes to accommodate Mega-Cap IPOs?",
    "url": "https://news.ycombinator.com/item?id=48368083",
    "source": "figmert",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-02T09:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390904",
    "domain": "股票",
    "title": "SpaceX Sets Price for $1.77T IPO",
    "url": "https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html",
    "source": "gen220",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-03T22:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48454210",
    "domain": "金融",
    "title": "Federal judge blocks H1B visa $100K fee",
    "url": "https://www.alaskasnewssource.com/2026/06/08/federal-judge-blocks-h1-b-visa-100k-fee/",
    "source": "naturalmovement",
    "platform": "hackernews",
    "points": 190,
    "published_at": "2026-06-09T00:01:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48479537",
    "domain": "金融",
    "title": "Meta steals a tactic from Tesla and builds data centers in tents",
    "url": "https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-06-10T17:18:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48483445",
    "domain": "金融",
    "title": "US President says 'I love the inflation'",
    "url": "https://www.cnbc.com/2026/06/10/trump-inflation-cpi-iran-oil.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-06-10T22:12:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206387",
    "domain": "金融",
    "title": "The quadratic sandwich",
    "url": "https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html",
    "source": "cpp_frog",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-20T12:06:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48476514",
    "domain": "金融",
    "title": "GnuCash is right. It's also why I built my own finance app",
    "url": "https://k-id.app/blog/gnucash-is-right/",
    "source": "tinosar",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-06-10T14:06:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48488805",
    "domain": "金融",
    "title": "Feds will abruptly dismantle system monitoring climate change, oceans",
    "url": "https://www.usatoday.com/story/news/nation/2026/06/11/climate-change-ocean-monitoring-system-dismantled/90378309007/",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T11:12:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:48491301",
    "domain": "金融",
    "title": "Craig Federighi Details Apple's Collaboration with Google for Siri AI in iOS 27",
    "url": "https://9to5mac.com/2026/06/08/craig-federighi-details-apples-collaboration-with-google-for-siri-ai-in-ios-27/",
    "source": "tambourine_man",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-11T15:01:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48360414",
    "domain": "金融",
    "title": "Making Debian or Fedora persistent live images",
    "url": "https://sigwait.org/~alex/blog/2026/05/28/smdBC8.html",
    "source": "henry_flower",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-06-01T18:02:10+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12446",
    "domain": "金融",
    "title": "Temporal Coarse-Graining of Latent Default-Probability Paths Generates Effective Default Correlation",
    "url": "https://arxiv.org/abs/2606.12446",
    "source": "Shintaro Mori",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12446v1 Announce Type: new Abstract: We show that persistent dynamics of a latent default-probability path can generate effective default correlation through temporal coarse-graining. In th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12450",
    "domain": "金融",
    "title": "Forward-Time Black-Scholes Reconstruction via Regularized Legendre Reduction",
    "url": "https://arxiv.org/abs/2606.12450",
    "source": "Phuong M. Nguyen, Matt Nguyen, Loc H. Nguyen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12450v1 Announce Type: new Abstract: We study a forward-time formulation of the Black-Scholes equation with state-dependent volatility. In contrast to the classical terminal-value pricing p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12585",
    "domain": "金融",
    "title": "Revisiting the ABCs of Working with AI: A Replication with Radiologists",
    "url": "https://arxiv.org/abs/2606.12585",
    "source": "Daniel Martin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12585v1 Announce Type: new Abstract: Artificial intelligence (AI) systems increasingly assist human experts, but the consequences of AI assistance on productivity can be heterogeneous. Capl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12612",
    "domain": "金融",
    "title": "The Mathematics of Heuristic Portfolio Optimization (HPO)",
    "url": "https://arxiv.org/abs/2606.12612",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12612v1 Announce Type: new Abstract: Practitioners allocate capital with forecast-light rules such as equal weight, inverse volatility, risk parity, HRP, and return-adjusted HRP (RA-HRP). T"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12717",
    "domain": "金融",
    "title": "In-Family Arbitrage-Free Interpolation of Mixture Densities Across Expirations",
    "url": "https://arxiv.org/abs/2606.12717",
    "source": "Thijs van den Berg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12717v1 Announce Type: new Abstract: Given risk-neutral densities of a tradeable forward, fitted as $N$-component mixtures at a finite set of expiration pillars, we look for a continuous-ti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12872",
    "domain": "金融",
    "title": "Non-Spanning Identification of Scheduled Event Risk in Option Pricing",
    "url": "https://arxiv.org/abs/2606.12872",
    "source": "Tenghan Zhong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12872v1 Announce Type: new Abstract: Short-dated index options make scheduled macro-announcement risk visible in market prices, but identification is nontrivial: a flexible no-event surface"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12893",
    "domain": "金融",
    "title": "Technology Shocks, Relative Performance Measures, and Outcomes: Evidence from Classical Chess",
    "url": "https://arxiv.org/abs/2606.12893",
    "source": "Dan Ben-Moshe, David Genesove",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12893v1 Announce Type: new Abstract: In the fall of 2020, neural-network methods produced a large improvement in chess engines that became freely and widely available. By the end of 2021, t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13314",
    "domain": "金融",
    "title": "The Privilege of Exposure: Caste and Generative AI in India's Graduate Labour Market",
    "url": "https://arxiv.org/abs/2606.13314",
    "source": "Kaibalyapati Mishra",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.13314v1 Announce Type: new Abstract: Who is exposed to generative AI in a developing-country labour market? We map three occupational AI-exposure indices to India's redesigned Periodic Labo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13419",
    "domain": "金融",
    "title": "Realtime price impact detection",
    "url": "https://arxiv.org/abs/2606.13419",
    "source": "Ilija I Zovko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.13419v1 Announce Type: new Abstract: An important question for an algo trader working an order is to understand if their actions are moving the market against them -- i.e., causing market i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13506",
    "domain": "金融",
    "title": "Skill vs Education Types of Labour Mismatch and Their Association with Earnings",
    "url": "https://arxiv.org/abs/2606.13506",
    "source": "Vsevolod Iakovlev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.13506v1 Announce Type: new Abstract: This paper analyses the distinction between educational and skill types of labour mismatch and their association with earnings. Drawing on cross-section"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13618",
    "domain": "金融",
    "title": "A Declining CVaR Glidepath Framework for Target-Date Fund Design with an Application to the Chilean Pension System",
    "url": "https://arxiv.org/abs/2606.13618",
    "source": "Israel Mu\\~noz, Fernando Su\\'arez, Omar Larr\\'e, Arturo Cifuentes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.13618v1 Announce Type: new Abstract: We propose a framework for designing Target-Date Funds (TDFs) around an explicit return objective while controlling risk directly at the portfolio level"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12787",
    "domain": "金融",
    "title": "Orchestrating the Twin Transition in Multinational Corporations: Technology Roadmapping for Green and Digital Global Business Services",
    "url": "https://arxiv.org/abs/2606.12787",
    "source": "Han-Teng Liao, Karen Ang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12787v1 Announce Type: cross Abstract: Global Business Services (GBS) have emerged as a \"living laboratory\" for the Twin Transition of Green and Digital Transformation, as multinational cor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12788",
    "domain": "金融",
    "title": "To Share or Not to Share: Orchestrating Trustworthy Data in Global Value Chains",
    "url": "https://arxiv.org/abs/2606.12788",
    "source": "Han-Teng Liao, Chang-Yi Kao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.12788v1 Announce Type: cross Abstract: As the EU Carbon Border Adjustment Mechanism (CBAM) approaches, the global semiconductor value chain faces growing structural tensions between regulat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13431",
    "domain": "金融",
    "title": "Adaptive rerouting reshapes impacts of maritime chokepoint disruptions",
    "url": "https://arxiv.org/abs/2606.13431",
    "source": "Mitja Devetak, Jasper Verschuur, Peter Klimek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.13431v1 Announce Type: cross Abstract: Maritime chokepoints concentrate shipping traffic. Disruptions to this traffic can have a widespread impact on the global economy. However, the way in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2408.08874",
    "domain": "金融",
    "title": "Hydrogen Development in China and the EU: A Recommended Tian Ji's Horse Racing Strategy",
    "url": "https://arxiv.org/abs/2408.08874",
    "source": "Hong Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2408.08874v2 Announce Type: replace Abstract: The global momentum towards establishing sustainable energy systems has become increasingly prominent. Hydrogen, as a remarkable carbon-free and ren"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.01921",
    "domain": "金融",
    "title": "Multilayer Perceptron Neural Network Models in Asset Pricing: An Empirical Study on Large-Cap US Stocks",
    "url": "https://arxiv.org/abs/2505.01921",
    "source": "Shanyan Lai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2505.01921v3 Announce Type: replace Abstract: In this study, MLP models with dynamic structure are applied to factor models for asset pricing tasks. Concretely, the MLP pyramid model structure w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.23554",
    "domain": "金融",
    "title": "When Clear Skies Cloud Trust: Environmental Cues and the Paradox of Confidence in Government",
    "url": "https://arxiv.org/abs/2509.23554",
    "source": "Xiangzhe Xu, Ran Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2509.23554v2 Announce Type: replace Abstract: Government trust, as a core concept in political economy and public policy research, serves as a fundamental cornerstone of democratic legitimacy an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.22792",
    "domain": "金融",
    "title": "From Arbitrage Removal to Density Extraction: A Model-Free Framework for Short-Dated Options",
    "url": "https://arxiv.org/abs/2605.22792",
    "source": "Aaron Wizman, Gabriel Turinici, Gregory Merran",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2605.22792v3 Announce Type: replace Abstract: We study risk-neutral density extraction from short-dated option chains. As expiry approaches, option premia decline and bid--ask spreads can be lar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.24242",
    "domain": "金融",
    "title": "Explicit Signal-Adaptive Sequential Optimal Execution Quotes",
    "url": "https://arxiv.org/abs/2605.24242",
    "source": "Fenghui Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2605.24242v2 Announce Type: replace Abstract: This paper develops a unified explicit solution theory for optimal execution through sequential limit-order placement in a limit order book. Rather "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.10337",
    "domain": "金融",
    "title": "Optimal exit strategies of CPT gamblers in unfair gambles",
    "url": "https://arxiv.org/abs/2606.10337",
    "source": "Sang Hu, Xun Yu Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.10337v2 Announce Type: replace Abstract: In this paper we study optimal exit strategies of gamblers with cumulative prospect theory (CPT) preferences in games where the expected payoff is s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11238",
    "domain": "金融",
    "title": "Artificial Intelligence in Ship Finance: Applications, Opportunities, and a Case Study in AI-Augmented Loan Origination",
    "url": "https://arxiv.org/abs/2606.11238",
    "source": "Lasse Dierich, Orestis Schinas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.11238v2 Announce Type: replace Abstract: Ship finance is a data-intensive and document-heavy segment of asset-based lending, requiring the integration of financial, technical, contractual, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.25740",
    "domain": "金融",
    "title": "A mathematical study of the excess growth rate",
    "url": "https://arxiv.org/abs/2510.25740",
    "source": "Steven Campbell, Ting-Kam Leonard Wong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2510.25740v2 Announce Type: replace-cross Abstract: The excess growth rate, defined as the gap in Jensen's inequality for the logarithm, is a fundamental functional in portfolio theory. In this "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07489",
    "domain": "金融",
    "title": "How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope",
    "url": "https://arxiv.org/abs/2606.07489",
    "source": "Jeremy Yang, Kate Zyskowski, Noah Yonack, Jerry Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T04:00:00+00:00",
    "summary": "arXiv:2606.07489v2 Announce Type: replace-cross Abstract: Frontier AI systems are bridging the gap between intelligence and utility by shifting from conversational assistants to autonomous agents that"
  },
  {
    "id": "hn:48384810",
    "domain": "金融",
    "title": "Tesla retroactively added 'supervised' to FSD contracts owners signed years ago",
    "url": "https://electrek.co/2026/06/03/tesla-retroactively-modified-fsd-contracts-supervised/",
    "source": "breve",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-06-03T14:43:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451917",
    "domain": "金融",
    "title": "Federal judge rules Trump's $100k fee for H-1B visas unlawful",
    "url": "https://www.theguardian.com/us-news/2026/jun/08/trump-h-1b-visa-fee-invalidated",
    "source": "xpl",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-08T20:57:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48406282",
    "domain": "金融",
    "title": "S&P Global keeps fast index entry rules unchanged as SpaceX listing looms",
    "url": "https://www.reuters.com/business/finance/sp-global-keeps-fast-entry-proposal-unchanged-spacex-listing-looms-2026-06-04/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-06-04T23:55:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48317563",
    "domain": "金融",
    "title": "Microsoft data suggests using AI is more expensive than hiring people",
    "url": "https://finance.yahoo.com/sectors/technology/articles/microsoft-data-suggests-using-ai-225900743.html",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-05-29T00:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48449003",
    "domain": "金融",
    "title": "Half of Americans say they're worse off financially than a year ago",
    "url": "https://www.cbsnews.com/news/americans-worse-off-financially-year-ago-fed-survey/",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-08T18:12:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436542",
    "domain": "金融",
    "title": "Ripping a DVD, a federal crime in 1999, requires $22 and free software in 2026",
    "url": "https://ringmast4r.substack.com/p/in-1999-this-was-a-federal-crime",
    "source": "akkartik",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-07T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48438281",
    "domain": "金融",
    "title": "Boomers are hoarding most of America's wealth and power",
    "url": "https://finance.yahoo.com/economy/articles/golden-years-not-golden-boomers-113000201.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-07T20:35:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210413",
    "domain": "金融",
    "title": "Standard Chartered CEO walks back comment about 'lower-value human capital'",
    "url": "https://www.wsj.com/finance/banking/ceo-walks-back-comment-about-replacing-lower-value-human-capital-with-ai-15bdfc5c",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-05-20T16:38:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48401755",
    "domain": "金融",
    "title": "Fedora 43 Upgrade revealed 20 years old Outlook Security Bug",
    "url": "https://fedoramagazine.org/fedora-43-upgrade-revealed-20-years-old-outlook-security-bug/",
    "source": "thewebguyd",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-04T17:24:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48403461",
    "domain": "金融",
    "title": "Open Letter to President of Russian Federation from President of Ukraine",
    "url": "https://www.president.gov.ua/en/news/vidkritij-list-prezidentu-rosijskoyi-federaciyi-vid-preziden-104769",
    "source": "defly",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-04T19:27:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48371952",
    "domain": "金融",
    "title": "Amazon joins Microsoft in sending message to employees",
    "url": "https://finance.yahoo.com/sectors/technology/articles/amazon-joins-microsoft-sending-shocking-171700630.html",
    "source": "hereticles",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-02T15:58:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377347",
    "domain": "金融",
    "title": "Feds failing in bid to take a supercomputer from a climate research center",
    "url": "https://arstechnica.com/science/2026/06/judge-blocks-part-of-trump-admins-effort-to-hurt-colorado-research-center/",
    "source": "yodon",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-02T22:46:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48328797",
    "domain": "金融",
    "title": "Federal judge orders Trump's name be removed from Kennedy Center",
    "url": "https://www.msn.com/en-us/news/politics/federal-judge-orders-trump-s-name-be-removed-from-kennedy-center/ar-AA24neRw",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-29T20:29:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48327518",
    "domain": "金融",
    "title": "Americans Are Falling Behind on Their $1.25T Credit-Card Bill",
    "url": "https://www.wsj.com/personal-finance/credit/us-credit-card-debt-af5c7c77",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-05-29T18:41:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48349067",
    "domain": "金融",
    "title": "Nearly Half of Home Insurance Claims Result in Zero Payout",
    "url": "https://www.wsj.com/finance/the-home-insurance-coin-flip-nearly-half-of-claims-result-in-zero-payout-4b49acaf",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-05-31T19:45:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48338988",
    "domain": "金融",
    "title": "Driver, 87, dies after Tesla on Autopilot mode crashes into pond",
    "url": "https://www.usatoday.com/story/news/nation/2026/05/29/tesla-on-autopilot-mode-crashes-into-pond-87-year-old-driver-dies/90319482007/",
    "source": "thinkcontext",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-05-30T17:59:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48333813",
    "domain": "金融",
    "title": "Tesla Self-Certifies Level 4 Autonomous Vehicles in Texas",
    "url": "https://www.notateslaapp.com/news/4216/tesla-self-certifies-l4-autonomy-in-texas",
    "source": "frankacter",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-05-30T07:58:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48341005",
    "domain": "金融",
    "title": "Tesla's 'Full Self-Driving' fraud lawsuit gets first hearing in China",
    "url": "https://electrek.co/2026/05/30/tesla-fsd-china-lawsuit-first-hearing-10-owners/",
    "source": "breve",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-30T21:58:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48364392",
    "domain": "金融",
    "title": "How to Silence the Federal Workforce",
    "url": "https://www.theatlantic.com/ideas/2026/06/trumps-intimidation-whistleblowers-nda/687377/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-02T00:38:21+00:00",
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
