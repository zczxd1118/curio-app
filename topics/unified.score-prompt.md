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

- 今日日期：`2026-06-08`
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
  "date": "2026-06-08",
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
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1151472,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1onb6zwEkk",
    "domain": "AI",
    "title": "【Ai教程】100集（全）从零开始学illustrator软件基础 (Ai2025新手入门实用版)Ai2025零基础入门教程！！！",
    "url": "http://www.bilibili.com/video/av115025985412548",
    "source": "天才AI设计鲨",
    "platform": "bilibili",
    "points": 1011683,
    "published_at": "2025-08-14T11:00:00+00:00",
    "summary": "设计行业5年 是一名资深设计师~PS学习交流 （南极有什么→ 动物 群 ：211582457）\n你的三连是我最大的动力！！你的三连是我最大的动力！！你的三连是我最大的动力！！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 833488,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 624088,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 368311,
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
    "points": 332648,
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
    "points": 241558,
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
    "points": 236125,
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
    "points": 183041,
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
    "points": 173698,
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
    "points": 153213,
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
    "points": 144822,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 141360,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 132725,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1xcsPzvE2e",
    "domain": "AI",
    "title": "2025illustrator教程|60分钟快速学习AI软件教程|矢量插画",
    "url": "http://www.bilibili.com/video/av115401358838380",
    "source": "illustrator教程AI",
    "platform": "bilibili",
    "points": 132476,
    "published_at": "2025-10-19T14:46:02+00:00",
    "summary": "素材下载：https://lqayiduj0jd.feishu.cn/wiki/Y02Nw66vhiKzbnkWVQRcYoPinqY"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 105670,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1j67k6oENA",
    "domain": "AI",
    "title": "Claude Ultracode 超码 上线 | 操控100个Agent并行开发  保姆级实战教程",
    "url": "http://www.bilibili.com/video/av116697163896598",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 98863,
    "published_at": "2026-06-05T11:05:27+00:00",
    "summary": "Ultracode 功能太好用了，就是Claude Code昨天新出的“超码”功能，如果你Vibe Coding ，那这个技巧一定要掌握。他解决了Claude Code 一次性跑不完大型任务的问题。\n本期视频很长，但看完你的AI Coding能力将超越整个团队。并且把视频内容整理成了文字版，放在评论区，方便你学习使用。视频很干，可以先喝口水润润喉咙。"
  },
  {
    "id": "bvid:BV1nK7r6wEhA",
    "domain": "AI",
    "title": "Anthropic发出警告，AI已经开始自我进化！",
    "url": "http://www.bilibili.com/video/av116696123771860",
    "source": "杜雨说AI",
    "platform": "bilibili",
    "points": 94770,
    "published_at": "2026-06-05T06:44:07+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1GT5xzyE81",
    "domain": "AI",
    "title": "[简幻欢]通过服务器和你的朋友一起玩我的世界整合包？",
    "url": "http://www.bilibili.com/video/av114363537036653",
    "source": "AilaSama",
    "platform": "bilibili",
    "points": 90350,
    "published_at": "2025-04-19T07:53:49+00:00",
    "summary": "简幻欢是国内Minecraft公益开服平台\r\n官网地址：https://simpfun.cn/auth?type=register&amp;code=1462159\r\n我的推荐码为1462159，填入后可额外获得150积分用于开服\r\n视频内容以CurseForge和Modrinth平台的整合包为例，但其他平台的也应该适用，找到对应的客户端和服务端即可安装"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 85404,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1PKBiBzERa",
    "domain": "AI",
    "title": "如何使用 codebuddy 从 0 到 1 完成一个产品，全流程录制，保姆级教学。",
    "url": "http://www.bilibili.com/video/av115785959804794",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 64708,
    "published_at": "2025-12-27T03:00:00+00:00",
    "summary": "本视频将带大家从 0 到 1 使用 CodeBuddy+CloudBase 完成一个点咖啡小程序商城，全部流程实时录制，手把手保姆级教学。视频如下：\n1、 CodeBuddy 介绍\n2、PRD 文档生成\n3、Figma 设计小程序\n4、Figma转小程序\n5、生成数据库\n6、后台系统搭建\n7、小程序后端替换\n8、一键上线"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 62351,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 58100,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 56148,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 50908,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1c8NFzhEMi",
    "domain": "AI",
    "title": "一个CLI干掉所有MCP工具，省99%的token mcp2cli",
    "url": "http://www.bilibili.com/video/av116204349953548",
    "source": "探索未至之境",
    "platform": "bilibili",
    "points": 49235,
    "published_at": "2026-03-10T10:18:17+00:00",
    "summary": "深度解析GitHub热门项目mcp2cli——一个能把任何MCP服务器或OpenAPI规范变成命令行工具的Python项目。它用&quot;懒发现&quot;机制，把MCP协议的token浪费从数十万降到几千，节省高达99%。整个核心实现只有一个Python文件，却支持三种接入模式、OAuth认证和智能缓存。发布仅一天就获得372颗星，但社区也有激烈争议：CLI真的能取代MCP吗？准确率会不会受影"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 42352,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV15sNiecEZc",
    "domain": "AI",
    "title": "五款AI聚合客户端，这次不用跑来跑去了",
    "url": "http://www.bilibili.com/video/av113983935747114",
    "source": "果核次元",
    "platform": "bilibili",
    "points": 41449,
    "published_at": "2025-02-11T07:01:27+00:00",
    "summary": "全网AI，一网打尽。只要你配置好，直接无敌"
  },
  {
    "id": "bvid:BV1o3XrB6E8W",
    "domain": "AI",
    "title": "🦞彻底超越OpenClaw！Claude Code原生支持Computer Use全自动操控电脑实现办公自动化！实测效果远超想象！CC源代码泄露预警！",
    "url": "http://www.bilibili.com/video/av116323736623030",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 36407,
    "published_at": "2026-03-31T12:19:28+00:00",
    "summary": "视频简介：\nClaude Code源码泄露预警！\n重磅更新！Claude Code CLI一键操控你的电脑！自动下棋、自动测试APP、自动写代码，AI Agent终极形态来了！\n本期视频详细演示了Claude Code最新版原生支持的Computer Use功能！这是继Claude桌面应用Cowork和Code之后，Claude Code CLI正式加入Computer Use阵营，标志着Anth"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 34533,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 33658,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 30119,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29591,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1gKZhYWEnK",
    "domain": "AI",
    "title": "【Cline+MCP】王炸组合！告别手动！MCP 自动化工作流，AI 编码更高效！",
    "url": "http://www.bilibili.com/video/av114262555104373",
    "source": "AI大模型全栈",
    "platform": "bilibili",
    "points": 27574,
    "published_at": "2025-04-01T11:53:56+00:00",
    "summary": "【Cline+MCP】王炸组合！告别手动！MCP 自动化工作流，AI 编码更高效！"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27019,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV13HEw6rEDa",
    "domain": "AI",
    "title": "【2026最新】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116691140872014",
    "source": "绕着宇宙飞一圈",
    "platform": "bilibili",
    "points": 26570,
    "published_at": "2026-06-04T09:39:37+00:00",
    "summary": "求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！"
  },
  {
    "id": "bvid:BV1HFDSBPE7b",
    "domain": "AI",
    "title": "3分钟教你部署ai我的世界陪玩！",
    "url": "http://www.bilibili.com/video/av116390124067729",
    "source": "我叫非主流_",
    "platform": "bilibili",
    "points": 24816,
    "published_at": "2026-04-12T11:45:00+00:00",
    "summary": "这是上期视频的教程，求求大家给个三连把="
  },
  {
    "id": "bvid:BV1HaVh6fEhn",
    "domain": "AI",
    "title": "AI编程进阶必修课！Claude Code+Harness AI 工程化实战！电商项目全流程落地，规范开发、代码治理、简历加分一站式吃透",
    "url": "http://www.bilibili.com/video/av116656764421367",
    "source": "图灵程序员诸葛",
    "platform": "bilibili",
    "points": 19810,
    "published_at": "2026-05-29T08:01:23+00:00",
    "summary": "大模型资料看这里聆取https://www.bilibili.com/read/cv49754608/?jump_opus=1"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17257,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1QzuRz2Epz",
    "domain": "AI",
    "title": "【中文】Cursor AI Unity 教程：新手指南，简单易懂 ｜ Nikhil Malankar",
    "url": "http://www.bilibili.com/video/av114879017000489",
    "source": "CursorInsider",
    "platform": "bilibili",
    "points": 17247,
    "published_at": "2025-07-19T13:00:00+00:00",
    "summary": "在本视频中，我将带你逐步完成 Cursor AI 在 Unity 中的完整设置和配置，帮助你利用 AI 驱动的代码辅助功能，加速你的游戏开发流程。无论你是正在构建一个新项目，还是将 AI 集成到现有的 Unity 游戏中，本教程都涵盖了你所需的一切。\n\n🔧 你将学到：\n✔️ 如何在 Unity 中安装和配置 Cursor AI\n✔️ 设置 Cursor AI 扩展以实现无缝开发\n✔️ 使用 AI "
  },
  {
    "id": "bvid:BV1Y2Ex6kEEf",
    "domain": "AI",
    "title": "vibe coding｜监控Claude/Codex实时任务的桌面宠物来啦～你的桌宠还在只会提醒喝水吗？ 【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116707985330558",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 16203,
    "published_at": "2026-06-07T08:58:03+00:00",
    "summary": "vibe coding了个桌面宠物给claude/codex当监工啦\n\n每次用 Claude Code / Codex 写代码，AI 在那闷头跑任务、转圈圈，我不一直盯着就根本不知道到哪了、卡没卡住，干等着很浪费时间，去做别的事吧又很容易错过结果，任务多起来完全没有直观的全局视角！\n\n于是我做了个桌面宠物工具，让它实时&quot;演&quot;出我的 AI 在干啥👇\n🐾 AI思考时 → 写字记笔记"
  },
  {
    "id": "bvid:BV1jYRRBDExF",
    "domain": "AI",
    "title": "让AI直接操作godot开发游戏，免费开源MCP插件",
    "url": "http://www.bilibili.com/video/av116545648860073",
    "source": "Yurineko73",
    "platform": "bilibili",
    "points": 16127,
    "published_at": "2026-05-10T03:00:00+00:00",
    "summary": "因为想找一个好用的mcp工具，结果发现不是要收费就是不可商用，于是借助ai直接搓了一个出来。\n目前已经发布1.0.1版本，在godot asset library搜索 [godot mcp native]即可下载使用，\n也可以去GitHub上下载完整项目 https://github.com/yurineko73/Godot-MCP-Native\n免费开源，可以随意扩展和修改，如果有需要的功能或遇"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 15534,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 14908,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13543,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 12885,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1CbvxBwEah",
    "domain": "AI",
    "title": "真的不用服务器！用Cloudflare Workers+D1轻松搭建网站！",
    "url": "http://www.bilibili.com/video/av115803408045159",
    "source": "软件工程师Tim",
    "platform": "bilibili",
    "points": 11799,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV1rCJdzFEQg",
    "domain": "AI",
    "title": "让AI帮你干活：WindowsMCP安装和使用！",
    "url": "http://www.bilibili.com/video/av115242814212549",
    "source": "磊哥聊AI",
    "platform": "bilibili",
    "points": 11776,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
  },
  {
    "id": "bvid:BV1RtGU6hEDd",
    "domain": "AI",
    "title": "DeepSeek-Reasonix 【保姆级教程】：专为 DeepSeek 打造的 AI 编程 Agent客户端，长会话成本到底能省多少？",
    "url": "http://www.bilibili.com/video/av116647486556383",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 11427,
    "published_at": "2026-05-27T16:33:52+00:00",
    "summary": "本期体验 DeepSeek-Reasonix 这个开源项目，主要看客户端界面、模型模式、会话导入、MCP 配置、记忆与缓存等功能。内容基于个人使用记录，不做夸张结论，适合对 DeepSeek 生态和 AI 编程工具感兴趣的朋友参考。"
  },
  {
    "id": "bvid:BV1HFRgBvEVv",
    "domain": "AI",
    "title": "claude接入小米mimo模型基础教程（无claude安装教程）",
    "url": "http://www.bilibili.com/video/av116499343738499",
    "source": "栉旎",
    "platform": "bilibili",
    "points": 11299,
    "published_at": "2026-05-01T12:37:49+00:00",
    "summary": "claude接入小米mimo模型全流程，"
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 470,
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
    "points": 325,
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
    "id": "hn:48431367",
    "domain": "AI 算力 / 半导体",
    "title": "The Russian who invented semiconductors 25 years before the USA",
    "url": "https://www.semidoped.com/p/til-the-man-who-invented-the-future",
    "source": "johncole",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-06-07T03:00:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356312",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity",
    "url": "https://news.ycombinator.com/item?id=48356312",
    "source": "ismaeel_bashir",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48439316",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei executive credits bans for accelerating domestic chip independence",
    "url": "https://www.techradar.com/pro/huaweis-chairman-officially-thanks-the-us-government-for-enabling-chinas-semiconductor-industry-chain-to-truly-grow",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-07T22:38:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48430986",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC CEO: I envy their 80% gross margins, but I would never do that",
    "url": "https://www.thestreet.com/investing/stocks/tsmc-taiwan-semiconductor-ceo-sends-blunt-message-to-memory-chip-rivals",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-07T01:53:27+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/antenna-first-design-the-rf-shift-iot-cannot-avoid/",
    "domain": "AI 算力 / 半导体",
    "title": "Antenna-First Design: The RF Shift IoT Cannot Avoid",
    "url": "https://www.eetimes.com/antenna-first-design-the-rf-shift-iot-cannot-avoid/",
    "source": "Senior Director of Engineering at Ignion",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T08:00:00+00:00",
    "summary": "Wireless IoT devices are shrinking while adding bands and certification complexity. Antenna integration can't wait until after layout lock. The post Antenna-First Design: The RF Shift IoT Cannot Avoid"
  },
  {
    "id": "rss:https://www.eetimes.com/connectivity-revolution-or-evolution-inside-data-centers/",
    "domain": "AI 算力 / 半导体",
    "title": "Connectivity Revolution or Evolution Inside Data Centers?",
    "url": "https://www.eetimes.com/connectivity-revolution-or-evolution-inside-data-centers/",
    "source": "Teresa Monteiro and Rimlee Deb Roy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:00:00+00:00",
    "summary": "AI transforms intra-data center networking, accelerating optical innovation while extending decades-long evolution in high-performance connectivity. The post Connectivity Revolution or Evolution Insid"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/anycubic-photon-mono-4-dips-below-usd190-saving-you-21-percent-off-its-retail-price-amazon-deal-saves-usd50-on-this-entry-level-resin-3d-printer",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic Photon Mono 4 dips below $190 saving you 21% off its retail price — Amazon deal saves $50 on this entry-level resin 3D printer",
    "url": "https://www.tomshardware.com/pc-components/anycubic-photon-mono-4-dips-below-usd190-saving-you-21-percent-off-its-retail-price-amazon-deal-saves-usd50-on-this-entry-level-resin-3d-printer",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T14:22:50+00:00",
    "summary": "The Anycubic Photon Mono 4 is on-sale at $189.99, giving you a $50 discount and saving you 21% off its retail price."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/msi-gigabyte-debut-new-5k-27-inch-mini-led-monitors-with-2-304-dimming-zones-and-glossy-panel-both-models-double-the-native-180-hz-refresh-rate-to-330-hz-at-1440p",
    "domain": "AI 算力 / 半导体",
    "title": "MSI, Gigabyte debut new 5K 27-inch Mini-LED monitors with 2,304 dimming zones and glossy panel — both models double the native 180 Hz refresh rate to 330 Hz at 1440p",
    "url": "https://www.tomshardware.com/monitors/msi-gigabyte-debut-new-5k-27-inch-mini-led-monitors-with-2-304-dimming-zones-and-glossy-panel-both-models-double-the-native-180-hz-refresh-rate-to-330-hz-at-1440p",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T14:19:42+00:00",
    "summary": "New Mini-LED monitors from MSI and Gigabyte featuring 5K panels with 2,304 dimming zones and glossy coatings have just been announced. These feature dual- and even triple-mode support, along with full"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/ukraines-birds-adapt-to-battlefield-environment-weaving-optical-fiber-nests-for-warmth-canny-feathered-friends-repurpose-scraps-of-this-spun-off-insulator-material",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine’s birds adapt to battlefield environment, weaving nests out of drone fiber-optic cables — resourceful wildlife adapts to miles of littered drone fibers",
    "url": "https://www.tomshardware.com/networking/ukraines-birds-adapt-to-battlefield-environment-weaving-optical-fiber-nests-for-warmth-canny-feathered-friends-repurpose-scraps-of-this-spun-off-insulator-material",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T13:55:53+00:00",
    "summary": "Birds in Donbas have been discovered feathering their nests with optical fiber."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-rdna-5-gaming-gpus-are-coming-late-next-year-according-to-aibs-at-computex-manufacturers-expect-new-team-red-cards-in-the-second-half-of-2027-alongside-nvidia",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's RDNA 5 gaming GPUs are coming late next year, according to AIBs at Computex — manufacturers expect new Team Red cards in the second half of 2027 alongside Nvidia",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-rdna-5-gaming-gpus-are-coming-late-next-year-according-to-aibs-at-computex-manufacturers-expect-new-team-red-cards-in-the-second-half-of-2027-alongside-nvidia",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T13:30:00+00:00",
    "summary": "AIB partners for AMD at the Computex 2026 show floor have said they expect next-gen RDNA 5 gaming GPUs to land sometime in the second half of 2027, or maybe even in early 2028. That launch schedule li"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/asml-beocmes-europes-most-valuable-company-ever-as-analysts-bet-on-higher-euv-output",
    "domain": "AI 算力 / 半导体",
    "title": "ASML becomes Europe's most valuable company ever as analysts bet on higher EUV output — its market cap hit $674 billion this week",
    "url": "https://www.tomshardware.com/tech-industry/asml-beocmes-europes-most-valuable-company-ever-as-analysts-bet-on-higher-euv-output",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T13:05:00+00:00",
    "summary": "ASML closed Wednesday, June 3rd, as the most valuable company in European history, reaching a market cap of $668 billion."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-signs-usd920m-monthly-compute-deal-with-spacex-companys-projected-annual-data-center-revenue-to-exceed-its-combined-proceeds-from-starlink-launch-services-and-ai-in-2025",
    "domain": "AI 算力 / 半导体",
    "title": "Google signs $920M monthly compute deal with SpaceX — company’s projected annual data center revenue to exceed its combined proceeds from Starlink, launch services, and AI in 2025",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-signs-usd920m-monthly-compute-deal-with-spacex-companys-projected-annual-data-center-revenue-to-exceed-its-combined-proceeds-from-starlink-launch-services-and-ai-in-2025",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T12:45:00+00:00",
    "summary": "Google's $920-million-a-month deal with SpaceX will let it secure 110,000 Nvidia GPUs starting October 2026. This is the second data center deal that SpaceX has secured in a matter of weeks, especiall"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/retropad-is-a-full-feature-parity-version-of-notepad-from-xp-in-just-2-749-bytes-x86-assembly-coded-apps-comes-from-windows-legend-dave-w-plummer",
    "domain": "AI 算力 / 半导体",
    "title": "RetroPad is a ‘full-feature-parity version of Notepad from XP’ in just 2,749 bytes — x86 assembly coded apps comes from Windows legend Dave W Plummer",
    "url": "https://www.tomshardware.com/software/windows/retropad-is-a-full-feature-parity-version-of-notepad-from-xp-in-just-2-749-bytes-x86-assembly-coded-apps-comes-from-windows-legend-dave-w-plummer",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T12:20:00+00:00",
    "summary": "A 'full-feature-parity version of Notepad' has been written in x86 assembly and it weighs in at under 3KB."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/russias-rassvet-constellation-loses-its-first-satellite-to-orbital-decay",
    "domain": "AI 算力 / 半导体",
    "title": "Russia’s new ‘Starlink‑Style’ Rassvet fleet loses its first satellite after weeks — Object 4 drops out of orbit but 15 others remain",
    "url": "https://www.tomshardware.com/tech-industry/russias-rassvet-constellation-loses-its-first-satellite-to-orbital-decay",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T12:00:00+00:00",
    "summary": "Object 4, one of 16 satellites in the first operational batch of Russia's Rassvet broadband network, re-entered Earth's atmosphere on approximately June 6th."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/developer-gets-half-life-running-at-30-fps-on-a-2007-nokia-n95",
    "domain": "AI 算力 / 半导体",
    "title": "Developer gets Half-Life running at 30 FPS on a Nokia N95 — proves 2007 phones can just about match 1998 PCs",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/developer-gets-half-life-running-at-30-fps-on-a-2007-nokia-n95",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:33:09+00:00",
    "summary": "Argentine developer Dante Leoncini has gotten the original Half-Life running at 30 FPS on a Nokia N95, the Symbian slider phone that launched in 2007."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/elegoo-jupiter-2-resin-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "Elegoo Jupiter 2 Resin 3D Printer review: The giant returns for round two",
    "url": "https://www.tomshardware.com/3d-printing/elegoo-jupiter-2-resin-3d-printer-review",
    "source": "Matt Farmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:00:00+00:00",
    "summary": "Elegoo’s Jupiter 2 is a resin powerhouse with a large print area and 16K high-quality 3D printing at a reasonable price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-reaches-almost-45-percent-cpu-share-in-the-latest-steam-hardware-survey-for-windows-gaming-pcs-ryzen-is-steadily-gaining-ground-against-intels-legacy-domination",
    "domain": "AI 算力 / 半导体",
    "title": "AMD reaches almost 45% CPU share in the latest Steam Hardware Survey for Windows gaming PCs — Ryzen is steadily gaining ground against Intel's legacy domination",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-reaches-almost-45-percent-cpu-share-in-the-latest-steam-hardware-survey-for-windows-gaming-pcs-ryzen-is-steadily-gaining-ground-against-intels-legacy-domination",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:00:00+00:00",
    "summary": "The latest Steam Hardware Survey is out and it's showing positive signs of growth for AMD, while Intel is unfortunately on a decline. The Red Team posted its best-ever CPU market share numbers in May "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/youtube-slams-1-7-volts-into-6700k-in-an-attempt-to-stop-the-cpu-from-bottlenecking-an-rtx-3080-pushes-gpu-utilization-from-60-percent-to-74-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Ludicrous overclock slams 1.7 volts into 6700K in an attempt to stop CPU from bottlenecking an RTX 3080 — 5.2 GHz on aging four-core pushes GPU utilization from 60% to 74%",
    "url": "https://www.tomshardware.com/pc-components/cpus/youtube-slams-1-7-volts-into-6700k-in-an-attempt-to-stop-the-cpu-from-bottlenecking-an-rtx-3080-pushes-gpu-utilization-from-60-percent-to-74-percent",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:00:00+00:00",
    "summary": "YouTuber challenges himself to alleviate a CPU bottleneck with a Core i7-6700K paired with an RTX 3080 through overclocking."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-adds-igpu-less-mobile-chips-to-core-200h-lineup-raptor-lake-based-core-7-230h-and-core-5-205h-sport-disabled-graphics-for-small-form-factor-desktop-boards",
    "domain": "AI 算力 / 半导体",
    "title": "Intel adds iGPU-less mobile chips to Core 200H lineup — Raptor Lake-based Core 7 230H and Core 5 205H sport disabled graphics for small form factor desktop boards",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-adds-igpu-less-mobile-chips-to-core-200h-lineup-raptor-lake-based-core-7-230h-and-core-5-205h-sport-disabled-graphics-for-small-form-factor-desktop-boards",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T10:00:00+00:00",
    "summary": "Intel introduces two new Raptor Lake CPUs in its Core 200H series lineup featuring disabled integrated graphics chips. The new CPUs are likely geared towards SFF desktops rather than laptops and 2-in-"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/chipsets/amd-b650-expansion-cards-hit-retail-starting-at-usd199-add-four-m-2-pcie-4-0-slots-and-11-usb-ports-to-any-pc-with-a-pcie-slot",
    "domain": "AI 算力 / 半导体",
    "title": "AMD B650 expansion cards hit retail starting at $199 — add four M.2 PCIe 4.0 slots and 11 USB ports to any PC with a PCIe slot",
    "url": "https://www.tomshardware.com/pc-components/chipsets/amd-b650-expansion-cards-hit-retail-starting-at-usd199-add-four-m-2-pcie-4-0-slots-and-11-usb-ports-to-any-pc-with-a-pcie-slot",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T16:29:46+00:00",
    "summary": "A couple of new add-in cards exemplify the trend of slapping AMD's Promontory 21 chipset onto a card for extra I/O expansion."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/creatives-sound-blaster-katana-v2x-can-be-hijacked-over-bluetooth",
    "domain": "AI 算力 / 半导体",
    "title": "Gaming soundbar can be hijacked from over 16 yards away without touch or pairing — the company allegedly refuses to label the blatant security flaw a cybersecurity risk",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/creatives-sound-blaster-katana-v2x-can-be-hijacked-over-bluetooth",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T16:06:19+00:00",
    "summary": "Security researcher Rasmus Moorats has demonstrated that Creative's Sound Blaster Katana V2X gaming soundbar can be hijacked over Bluetooth from up to 16 yards away."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/upgrade-your-pc-with-a-2tb-pcie-4-0-ssd-750w-power-supply-and-240mm-aio-for-usd300-hardware-bundle-saves-you-nearly-usd200",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrade your PC with a 2TB PCIe 4.0 SSD, 750W power supply, and 240mm AIO for $300 — hardware bundle saves you nearly $200",
    "url": "https://www.tomshardware.com/pc-components/upgrade-your-pc-with-a-2tb-pcie-4-0-ssd-750w-power-supply-and-240mm-aio-for-usd300-hardware-bundle-saves-you-nearly-usd200",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T15:33:18+00:00",
    "summary": "Even though power supplies and CPU coolers have remained unaffected by the AI boom, storage costs have skyrocketed, which makes this deal even more lucrative. You're getting a blazing-fast 2TB SSD, a "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/usd6000-semi-truck-gaming-rig-just-got-a-massive-upgrade-cabin-overhaul-includes-new-racing-bucket-seat-pedals-and-other-accessories-to-level-up-their-truck",
    "domain": "AI 算力 / 半导体",
    "title": "$6000 semi-truck gaming rig just got a massive upgrade — cabin overhaul includes new racing bucket seat, pedals, and other accessories to level up their truck",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/usd6000-semi-truck-gaming-rig-just-got-a-massive-upgrade-cabin-overhaul-includes-new-racing-bucket-seat-pedals-and-other-accessories-to-level-up-their-truck",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T15:22:57+00:00",
    "summary": "The trucker worked with Conspit to install a new seat, pedals, and other parts and accessories to level up their already insane semi-truck sim rig."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/the-floppy-disk-patent-was-granted-today-in-1972-when-80kb-took-up-8-inches-and-were-really-floppy",
    "domain": "AI 算力 / 半导体",
    "title": "The Floppy Disk patent was granted today in 1972 — when 80KB took up 8 inches and were really floppy",
    "url": "https://www.tomshardware.com/pc-components/storage/the-floppy-disk-patent-was-granted-today-in-1972-when-80kb-took-up-8-inches-and-were-really-floppy",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T14:45:15+00:00",
    "summary": "The patent application for the floppy disk was granted to two IBM engineers on this day in 1972."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-research-goes-full-spectrum-in-anticipation-of-indx",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa Research goes full spectrum in anticipation of INDX",
    "url": "https://www.tomshardware.com/3d-printing/prusa-research-goes-full-spectrum-in-anticipation-of-indx",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T13:34:49+00:00",
    "summary": "Prusa Research has announced a new open-source ColorMix engine for both PrusaSlicer and its web-based EasyPrint slicer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/gigabyte-z890-aorus-elite-wifi7-plus-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte Z890 Aorus Elite Wifi7 Plus Motherboard Review: Cost-conscious refresh board delivers (almost) all the fixens",
    "url": "https://www.tomshardware.com/pc-components/motherboards/gigabyte-z890-aorus-elite-wifi7-plus-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T13:13:12+00:00",
    "summary": "At under $270, the Gigabyte Z890 Aorus Elite Wifi7 Plus is a worthwhile mainstream motherboard. Fast networking and ample storage options are just two of the highlights of this refreshed Z890 offering"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/lexar-regional-manager-says-that-ram-prices-are-expected-to-double-by-the-end-of-the-year-discounts-and-stabilized-prices-result-from-distributors-getting-rid-of-old-stock-or-sourcing-products-from-other-regions",
    "domain": "AI 算力 / 半导体",
    "title": "Lexar regional manager says that RAM prices are expected to double by the end of the year — 'discounts' and stabilized prices result from distributors getting rid of old stock or sourcing products fro",
    "url": "https://www.tomshardware.com/pc-components/ram/lexar-regional-manager-says-that-ram-prices-are-expected-to-double-by-the-end-of-the-year-discounts-and-stabilized-prices-result-from-distributors-getting-rid-of-old-stock-or-sourcing-products-from-other-regions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T13:00:00+00:00",
    "summary": "Industry insiders say that RAM prices will continue to go up in the next eight to nine months, as the memory chip crisis goes from bad to worse. While retailers make moves to temporarily reduce prices"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/taiwanese-startup-formulav-line-wants-to-break-into-us-market-with-two-new-unique-cases-company-expects-products-to-become-available-on-newegg-later-this-year",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwanese startup FormulaV Line wants to break into US market with two new unique cases — company expects products to become available on Newegg later this year",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/taiwanese-startup-formulav-line-wants-to-break-into-us-market-with-two-new-unique-cases-company-expects-products-to-become-available-on-newegg-later-this-year",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T12:40:00+00:00",
    "summary": "Taiwanese startup FormulaV Line wants to break into the U.S. market with these two new and unique cases. It also showed off a plethora of other components, including PSUs, cooling solutions, and even "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/g-skill-explains-how-amd-expo-ull-unlocks-additional-performance-expanded-profiles-allow-memory-makers-to-include-subtiming-tweaks-for-the-first-time",
    "domain": "AI 算力 / 半导体",
    "title": "G.Skill explains how AMD EXPO ULL unlocks additional performance — expanded profiles allow memory makers to include subtiming tweaks for the first time",
    "url": "https://www.tomshardware.com/pc-components/ram/g-skill-explains-how-amd-expo-ull-unlocks-additional-performance-expanded-profiles-allow-memory-makers-to-include-subtiming-tweaks-for-the-first-time",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T12:20:00+00:00",
    "summary": "AMD's EXPO Ultra Low Latency program, announced at Computex 2026, aims to give users a one-click route to lower memory latencies than its existing EXPO profiles"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-led-team-claims-it-post-trained-deepseeks-1-6-trillion-parameter-models-on-ascend-910c-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei-led team claims it post-trained DeepSeek's 1.6-trillion-parameter model — 1,000 Ascend 910C chips used in training",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-led-team-claims-it-post-trained-deepseeks-1-6-trillion-parameter-models-on-ascend-910c-chips",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T12:00:00+00:00",
    "summary": "A research group that includes Huawei Technologies says it completed full-parameter post-training of DeepSeek's V4-Pro, a 1.6-trillion-parameter model."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/unreleased-rtx-3050-ti-engineering-sample-appears-in-photos-and-benchmarks-the-rtx-3060-alternative-that-never-happened",
    "domain": "AI 算力 / 半导体",
    "title": "Unreleased RTX 3050 Ti engineering sample appears in photos and benchmarks — the RTX 3060 alternative that never happened",
    "url": "https://www.tomshardware.com/pc-components/gpus/unreleased-rtx-3050-ti-engineering-sample-appears-in-photos-and-benchmarks-the-rtx-3060-alternative-that-never-happened",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T11:40:00+00:00",
    "summary": "Hardware leaker shares photographs and benchmarks for Nvidia's GeForce RTX 3050 Ti desktop graphics card that was never released."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/finland-deploys-new-system-to-detect-threats-to-undersea-cables-distributed-acoustic-sensors-measure-vibrations-from-the-seabed-and-informs-the-authorities-and-operators-of-suspicious-activities",
    "domain": "AI 算力 / 半导体",
    "title": "Finland deploys new system to detect threats to undersea cables — distributed acoustic sensors measure vibrations from the seabed and informs the authorities and operators of suspicious activities",
    "url": "https://www.tomshardware.com/tech-industry/finland-deploys-new-system-to-detect-threats-to-undersea-cables-distributed-acoustic-sensors-measure-vibrations-from-the-seabed-and-informs-the-authorities-and-operators-of-suspicious-activities",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T10:30:00+00:00",
    "summary": "Finnish companies and academic institutions, alongside the Finnish Navy and Border Guards, worked together to develop a system that used existing undersea cables to detect potential disturbances on th"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/retro-gaming-enthusiast-attempts-loading-games-to-sega-genesis-from-a-vinyl-record-player-recording-game-data-as-sound-mega-everdrive-pro-and-pi-pico-2-board-not-enough-to-overcome-limitations-of-the-turntable",
    "domain": "AI 算力 / 半导体",
    "title": "Retro gaming enthusiast attempts loading games to Sega Genesis from a vinyl record player, recording game data as sound — Mega EverDrive Pro and Pi Pico 2 board not enough to overcome limitations of t",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/retro-gaming-enthusiast-attempts-loading-games-to-sega-genesis-from-a-vinyl-record-player-recording-game-data-as-sound-mega-everdrive-pro-and-pi-pico-2-board-not-enough-to-overcome-limitations-of-the-turntable",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T10:00:00+00:00",
    "summary": "A quirky tech enthusiast attempted to load Sega Genesis console games through a vinyl record player."
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
    "id": "hn:48398107",
    "domain": "AI 算力 / 半导体",
    "title": "Nemotron 3 Ultra: Open Moe Hybrid Mamba-Transformer for Agentic Reasoning [pdf]",
    "url": "https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf",
    "source": "victormustar",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-04T13:06:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48354967",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces new AI chip for personal computers",
    "url": "https://www.bbc.com/news/articles/crmp9mppvzro",
    "source": "rishikeshs",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-06-01T10:33:25+00:00",
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
    "id": "hn:48291230",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Vera CPU Benchmarks: Olympus Cores Delivering Great Performance",
    "url": "https://www.phoronix.com/review/nvidia-vera-benchmarks",
    "source": "naves",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-05-27T08:15:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48352693",
    "domain": "AI 算力 / 半导体",
    "title": "A powerful new chapter for Windows PCs, accelerated by Nvidia RTX Spark",
    "url": "https://blogs.windows.com/windowsexperience/2026/05/31/introducing-a-powerful-new-chapter-for-windows-pcs-accelerated-by-nvidia-rtx-spark/",
    "source": "WalterSobchak",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-06-01T04:45:20+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/geopolitics-ai-and-jensen-huang-fuel-electronics-rock-and-roll-era/",
    "domain": "AI 算力 / 半导体",
    "title": "Geopolitics, AI, and Jensen Huang Fuel Electronics’ Rock-and-Roll Era",
    "url": "https://www.eetimes.com/geopolitics-ai-and-jensen-huang-fuel-electronics-rock-and-roll-era/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T22:00:00+00:00",
    "summary": "Jensen Huang and AI frenzy steal the show at Computex 2026—dive in to see how Taiwan leads the electronics. The post Geopolitics, AI, and Jensen Huang Fuel Electronics’ Rock-and-Roll Era appeared firs"
  },
  {
    "id": "rss:https://www.eetimes.com/manufacturing-accelerates-in-may-amid-inflation-and-geopolitical-headwinds/",
    "domain": "AI 算力 / 半导体",
    "title": "Manufacturing Accelerates in May Amid Inflation and Geopolitical Headwinds",
    "url": "https://www.eetimes.com/manufacturing-accelerates-in-may-amid-inflation-and-geopolitical-headwinds/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T13:17:36+00:00",
    "summary": "Manufacturing expanded further in May despite Inflation and lower GDP. The post Manufacturing Accelerates in May Amid Inflation and Geopolitical Headwinds appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/chips-act-2-0-puts-demand-at-center-of-europes-semiconductor-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "Chips Act 2.0 Puts Demand at Center of Europe’s Semiconductor Strategy",
    "url": "https://www.eetimes.com/chips-act-2-0-puts-demand-at-center-of-europes-semiconductor-strategy/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T07:00:00+00:00",
    "summary": "Chips Act 2.0 shifts EU focus from factory subsidies to chip design and demand. The post Chips Act 2.0 Puts Demand at Center of Europe’s Semiconductor Strategy appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/netrasemi-brings-up-a2000-ai-chip-begins-customer-evaluation-phase/",
    "domain": "AI 算力 / 半导体",
    "title": "Netrasemi Brings Up A2000 AI Chip, Begins Customer Evaluation Phase",
    "url": "https://www.eetimes.com/netrasemi-brings-up-a2000-ai-chip-begins-customer-evaluation-phase/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T22:00:00+00:00",
    "summary": "Indian startup Netrasemi has launched the A2000 AI chip built on a 12-nm technology node. The post Netrasemi Brings Up A2000 AI Chip, Begins Customer Evaluation Phase appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/computex-2026-are-we-heading-for-the-agentic-pc-era-yet/",
    "domain": "AI 算力 / 半导体",
    "title": "Computex 2026: Are We Heading for the Agentic PC Era Yet?",
    "url": "https://www.eetimes.com/computex-2026-are-we-heading-for-the-agentic-pc-era-yet/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-04T13:59:22+00:00",
    "summary": "In this video interview, explore whether agentic PCs are truly here as Nvidia and Microsoft unveil new tech at Computex 2026. The post Computex 2026: Are We Heading for the Agentic PC Era Yet? appeare"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency",
    "domain": "AI 算力 / 半导体",
    "title": "NSA using Claude Mythos for 'offensive cyber operations,' report claims — says 'half-a-dozen' Anthropic engineers embedded inside the agency",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T16:53:46+00:00",
    "summary": "US National Security Agency reportedly using Mythos for conducting cyber-attacks — report reveals Anthropic engineers inside the NSA"
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
    "id": "hn:48111896",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model",
    "url": "https://github.com/cactus-compute/needle",
    "source": "HenryNdubuaku",
    "platform": "hackernews",
    "points": 776,
    "published_at": "2026-05-12T18:03:11+00:00",
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
    "id": "hn:48111581",
    "domain": "大厂 AI 动态",
    "title": "Reimagining the mouse pointer for the AI era",
    "url": "https://deepmind.google/blog/ai-pointer/",
    "source": "devhouse",
    "platform": "hackernews",
    "points": 252,
    "published_at": "2026-05-12T17:40:13+00:00",
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
    "id": "hn:48080702",
    "domain": "大厂 AI 动态",
    "title": "Gemini API File Search is now multimodal",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 156,
    "published_at": "2026-05-10T03:22:02+00:00",
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
    "id": "hn:48084710",
    "domain": "大厂 AI 动态",
    "title": "Chrome's AI features may be hogging 4GB of your computer storage",
    "url": "https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features",
    "source": "birdculture",
    "platform": "hackernews",
    "points": 117,
    "published_at": "2026-05-10T15:22:46+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/design/945540/nasa-axiom-space-prada-lcvg-spacesuit-moon-artemis",
    "domain": "大厂 AI 动态",
    "title": "NASA will wear high-tech Prada long johns to the Moon",
    "url": "https://www.theverge.com/design/945540/nasa-axiom-space-prada-lcvg-spacesuit-moon-artemis",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T22:16:41+00:00",
    "summary": "We've seen Axiom Space and Prada's collaboration on the Axiom Extravehicular Mobility Unit (AxEMU) spacesuit. Now the company has revealed the Liquid Cooling and Ventilation Garment (LCVG) that astron"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/945445/summer-game-fest-2026-biggest-stories",
    "domain": "大厂 AI 动态",
    "title": "The 7 biggest storylines from Summer Game Fest 2026",
    "url": "https://www.theverge.com/entertainment/945445/summer-game-fest-2026-biggest-stories",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T18:45:33+00:00",
    "summary": "The 2026 edition of Summer Game Fest just wrapped up, and it was surprisingly hectic. The nearly week-long event came at a challenging time for the games industry, and for the most part the big keynot"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/945256/persona-6-teaser",
    "domain": "大厂 AI 动态",
    "title": "Persona 6 exists, and that’s all we know",
    "url": "https://www.theverge.com/entertainment/945256/persona-6-teaser",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T18:00:41+00:00",
    "summary": "This year's Summer Game Fest turned out to be a good one for fans of Japanese RPGs. First, the conclusion of the Final Fantasy VII remake trilogy was announced at SGF Live, and now we have the long-aw"
  },
  {
    "id": "rss:https://www.theverge.com/news/945359/microsoft-xbox-25th-anniversary-console-controller-release-date",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s Xbox 25th anniversary console comes in translucent green",
    "url": "https://www.theverge.com/news/945359/microsoft-xbox-25th-anniversary-console-controller-release-date",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T17:45:48+00:00",
    "summary": "Microsoft has created a special edition Xbox Series X to celebrate 25 years of the console. The Xbox 25th-anniversary console takes design cues from the original Xbox console, with both the console an"
  },
  {
    "id": "rss:https://www.theverge.com/games/939551/minecraft-dungeons-ii-2-release-date-trailer",
    "domain": "大厂 AI 动态",
    "title": "Minecraft Dungeons 2 gets a September release date",
    "url": "https://www.theverge.com/games/939551/minecraft-dungeons-ii-2-release-date-trailer",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T17:45:25+00:00",
    "summary": "Minecraft Dungeons 2, a sequel to Microsoft's dungeon crawler spinoff Minecraft Dungeons, will be released on September 29th. The company originally revealed the game in a brief trailer in March, prom"
  },
  {
    "id": "rss:https://www.theverge.com/games/939536/fable-xbox-games-showcase-2026",
    "domain": "大厂 AI 动态",
    "title": "Fable launches in late February after recent delay",
    "url": "https://www.theverge.com/games/939536/fable-xbox-games-showcase-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T17:14:57+00:00",
    "summary": "Just a few days after pushing Fable out of 2026, Microsoft showed off more footage of Fable, the first new entry in the storied RPG franchise since 2010's Fable III, at its Xbox Games Showcase on Sund"
  },
  {
    "id": "rss:https://www.theverge.com/games/939564/halo-campaign-evolved-xbox-games-showcase-2026",
    "domain": "大厂 AI 动态",
    "title": "Halo: Campaign Evolved arrives July 28th",
    "url": "https://www.theverge.com/games/939564/halo-campaign-evolved-xbox-games-showcase-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T17:14:08+00:00",
    "summary": "As part of its Xbox Games Showcase on Sunday, Microsoft revealed new details about Halo: Campaign Evolved, the upcoming remake of Halo: Combat Evolved's campaign mode. The remake will debut on Xbox Se"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/945269/gears-of-war-e-day-ps5-launch",
    "domain": "大厂 AI 动态",
    "title": "Gears of War: E-Day isn’t coming to the PS5",
    "url": "https://www.theverge.com/entertainment/945269/gears-of-war-e-day-ps5-launch",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T17:08:56+00:00",
    "summary": "Apparently, the \"return of Xbox\" means a retreat from other platforms. At its Xbox Games Showcase today, Microsoft revealed that Gears of War: E-Day - which was previously rumored for a PS5 launch in "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/943285/the-verge-weekend-questionnaire",
    "domain": "大厂 AI 动态",
    "title": "The Verge Weekend Questionnaire",
    "url": "https://www.theverge.com/entertainment/943285/the-verge-weekend-questionnaire",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T17:00:00+00:00",
    "summary": "Have you ever wondered what the most indispensable app is for your favorite musician or how the world&#8217;s tech CEOs stay focused? Well, that&#8217;s the sort of thing we aim to uncover in our Verg"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/944191/xbox-games-showcase-2026-news-trailers",
    "domain": "大厂 AI 动态",
    "title": "Xbox Games Showcase 2026: All the news and trailers",
    "url": "https://www.theverge.com/entertainment/944191/xbox-games-showcase-2026-news-trailers",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T16:40:00+00:00",
    "summary": "The console industry is in a weird place, and both Xbox and PlayStation have a chance to change the narrative a bit with their showcases at Summer Game Fest. Sony did that by focusing on the single-pl"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/07/is-this-the-dawn-of-the-tokenpocalypse/",
    "domain": "大厂 AI 动态",
    "title": "Is this the dawn of the Tokenpocalypse?",
    "url": "https://techcrunch.com/2026/06/07/is-this-the-dawn-of-the-tokenpocalypse/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T20:26:13+00:00",
    "summary": "We're likely to see more price increases as the big AI companies plan to go public."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/07/notion-restores-access-to-anthropic-after-service-disruption/",
    "domain": "大厂 AI 动态",
    "title": "Notion restores access to Anthropic after service disruption",
    "url": "https://techcrunch.com/2026/06/07/notion-restores-access-to-anthropic-after-service-disruption/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T17:56:22+00:00",
    "summary": "Notion's head of product said he was \"astonished\" at “the amount of people RT-ing this.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/07/openai-is-still-working-on-that-super-app/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is still working on that ‘super app’",
    "url": "https://techcrunch.com/2026/06/07/openai-is-still-working-on-that-super-app/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T16:23:22+00:00",
    "summary": "\"Chat is dead\" — at least, according to a senior OpenAI employee."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/07/inside-gms-900m-ev-battery-gamble/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Inside GM’s $900M EV battery gamble",
    "url": "https://techcrunch.com/2026/06/07/inside-gms-900m-ev-battery-gamble/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility — your central hub for news and insights on the future of transportation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/07/the-worst-hacks-and-breaches-of-2026-so-far/",
    "domain": "大厂 AI 动态",
    "title": "Hacked, leaked, and held for ransom: the worst breaches of 2026 so far",
    "url": "https://techcrunch.com/2026/06/07/the-worst-hacks-and-breaches-of-2026-so-far/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T14:00:00+00:00",
    "summary": "From a massive DOGE data breach and the hacking of critical energy and water systems to the hack of an FBI surveillance system, here are the most damaging security incidents and data breaches of 2026."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI unveils Lockdown Mode to protect sensitive data from prompt injection attacks",
    "url": "https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T20:32:24+00:00",
    "summary": "Even with Lockdown Mode, ChatGPT could be still vulnerable to prompt injections, but the goal is to reduce the likelihood that sensitive data gets shared in the process."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/06/what-to-expect-from-wwdc-2026-siris-highly-anticipated-revamp-and-apple-intelligence-updates/",
    "domain": "大厂 AI 动态",
    "title": "What to expect from WWDC 2026: Siri’s highly anticipated revamp and Apple Intelligence updates",
    "url": "https://techcrunch.com/2026/06/06/what-to-expect-from-wwdc-2026-siris-highly-anticipated-revamp-and-apple-intelligence-updates/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T18:13:36+00:00",
    "summary": "Apple's WWDC nears: Here's what you can look forward to."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/06/sriram-krishnan-is-leaving-his-role-as-white-house-ai-advisor/",
    "domain": "大厂 AI 动态",
    "title": "Sriram Krishnan is leaving his role as White House AI advisor",
    "url": "https://techcrunch.com/2026/06/06/sriram-krishnan-is-leaving-his-role-as-white-house-ai-advisor/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T17:42:15+00:00",
    "summary": "Krishnan is reportedly starting a new institution to continue shaping Trump's AI policy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/06/the-trump-administration-might-take-an-equity-stake-in-openai/",
    "domain": "大厂 AI 动态",
    "title": "The Trump administration might take an equity stake in OpenAI",
    "url": "https://techcrunch.com/2026/06/06/the-trump-administration-might-take-an-equity-stake-in-openai/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T16:17:21+00:00",
    "summary": "President Donald Trump said he's discussing deals \"where the American people can benefit from the success of AI.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/06/beyond-instagram-introducing-the-next-generation-of-social-apps/",
    "domain": "大厂 AI 动态",
    "title": "Beyond Instagram: Introducing the next generation of social apps",
    "url": "https://techcrunch.com/2026/06/06/beyond-instagram-introducing-the-next-generation-of-social-apps/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T15:00:00+00:00",
    "summary": "These newer social apps offer alternatives to Big Tech’s feeds, focusing on interests, creativity, and community."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/06/rip-anthony-head-our-10-favorite-moments-of-buffys-giles/",
    "domain": "大厂 AI 动态",
    "title": "RIP Anthony Head: Our 10 favorite moments of Buffy's Giles",
    "url": "https://arstechnica.com/culture/2026/06/rip-anthony-head-our-10-favorite-moments-of-buffys-giles/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T19:34:05+00:00",
    "summary": "Head's true genius—and that of his character, Giles—lay in quietly filling in the gaps in every scene"
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/school-shooting-survivor-sues-ai-gun-detection-firm-after-system-failed-to-spot-weapon/",
    "domain": "大厂 AI 动态",
    "title": "School shooting survivor sues AI gun detection firm after system failed to spot weapon",
    "url": "https://arstechnica.com/tech-policy/2026/06/school-shooting-survivor-sues-ai-gun-detection-firm-after-system-failed-to-spot-weapon/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T11:08:30+00:00",
    "summary": "How accurate does an AI system need to be?"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/scientists-ejected-from-diabetes-conference-for-distributing-journal-reprints/",
    "domain": "大厂 AI 动态",
    "title": "Scientists ejected from diabetes conference for distributing journal reprints",
    "url": "https://arstechnica.com/science/2026/06/scientists-ejected-from-diabetes-conference-for-distributing-journal-reprints/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T20:53:07+00:00",
    "summary": "Those ousted included ADA journal editor-in-chief Steven Kahn and former ADA president Desmond Schatz"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/otzis-mummified-body-is-home-to-ancient-strains-of-yeast-and-bacteria/",
    "domain": "大厂 AI 动态",
    "title": "Some ancient microbes frozen with Ötzi the Iceman are still growing",
    "url": "https://arstechnica.com/science/2026/06/otzis-mummified-body-is-home-to-ancient-strains-of-yeast-and-bacteria/",
    "source": "Kiona N. Smith",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T11:15:51+00:00",
    "summary": "What’s the difference between a person, an artifact, and an ecosystem?"
  },
  {
    "id": "rss:https://www.producthunt.com/products/olo-1st-ai-style-companion-for-guys",
    "domain": "大厂 AI 动态",
    "title": "Olo",
    "url": "https://www.producthunt.com/products/olo-1st-ai-style-companion-for-guys",
    "source": "Vaishnavi Bhade",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T19:38:31+00:00",
    "summary": "Style smarter with the world's first AI companion for guys Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/tamadoggo",
    "domain": "大厂 AI 动态",
    "title": "Tamadoggo",
    "url": "https://www.producthunt.com/products/tamadoggo",
    "source": "Sorin Vasiliu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T16:39:30+00:00",
    "summary": "A living journal for your pet's life, with AI insights Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/vaani-2",
    "domain": "大厂 AI 动态",
    "title": "Vaani",
    "url": "https://www.producthunt.com/products/vaani-2",
    "source": "Rohan Chaubey",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T06:15:39+00:00",
    "summary": "Lip-synced AI dubbing for creators, brands and studios Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/claude-artifact-player",
    "domain": "大厂 AI 动态",
    "title": "Claude Artifact Player",
    "url": "https://www.producthunt.com/products/claude-artifact-player",
    "source": "Mazen ALSAREM",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-07T20:25:19+00:00",
    "summary": "Run Claude artifacts locally Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/the-virtual-os-museum",
    "domain": "大厂 AI 动态",
    "title": "The Virtual OS Museum",
    "url": "https://www.producthunt.com/products/the-virtual-os-museum",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:41:15+00:00",
    "summary": "Relive vintage operating systems right on your desktop Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/ntsc-rs",
    "domain": "大厂 AI 动态",
    "title": "NTSC-RS",
    "url": "https://www.producthunt.com/products/ntsc-rs",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T05:18:36+00:00",
    "summary": "Open-source video emulation of analog TV and VHS artifacts Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/free-job-postings-api",
    "domain": "大厂 AI 动态",
    "title": "Job Postings API",
    "url": "https://www.producthunt.com/products/free-job-postings-api",
    "source": "Sam Crombie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-06T20:32:22+00:00",
    "summary": "View, monitor, and analyze 1.8M+ US jobs Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3844199957236227?f=rss",
    "domain": "大厂 AI 动态",
    "title": "改变全球速度的AI，付款却卡在上一个时代",
    "url": "https://36kr.com/p/3844199957236227?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:30:56+00:00",
    "summary": "2026年，全球平均每小时就有一家新的AI公司诞生。&nbsp; AI行业的竞争已经白热化到如此程度：大模型的参数在卷，推理速度在卷，应用落地的速度在卷，就连融资PPT的故事密度也在卷。一时间，所有人的目光都盯在“前端”——谁的模型更强，谁的产品先跑出来，谁就能在这场军备竞赛里站稳脚跟。 但在这场喧嚣之外，一个被大多数人忽视的问题，正在悄悄侵蚀每一家AI企业的利润：钱，到底能不能顺畅地流动起来？ "
  },
  {
    "id": "rss:https://36kr.com/p/3844006775360002?f=rss",
    "domain": "大厂 AI 动态",
    "title": "产品观察 | 小米创始员工范典创业AI硬件，做了台“无摩擦”的睡眠床头灯",
    "url": "https://36kr.com/p/3844006775360002?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:07:08+00:00",
    "summary": "作者&nbsp;|&nbsp;邱晓芬 编辑&nbsp;|&nbsp;袁斯来 「格物科技」的创始人范典，是当下智能硬件赛道的一个“异类”。 作为喝过小米粥的小米创始员工，范典曾任曾小米物联网平台部总经理、AIoT战略委员会主席。以大厂高管履历拿笔钱，以最短时间做出款硬件上众筹，依托媒体造势，再滚动更多融资是这两年硬件赛道创业很常见的打法。 但范典做第一款产品用了三年。 2024年，智能硬件还是很冷僻"
  },
  {
    "id": "rss:https://36kr.com/p/3841459663030532?f=rss",
    "domain": "大厂 AI 动态",
    "title": "「华超神控」获亿元天使系列融资，加速打造新一代AI超声脑机接口平台 | 36氪首发",
    "url": "https://36kr.com/p/3841459663030532?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T00:30:00+00:00",
    "summary": "文｜胡香赟 编辑｜海若镜 36氪获悉，近日，新一代AI超声脑机公司华超神控（BCI-Sonics）已完成亿元人民币级天使轮系列融资。天使轮融资由经纬创投领投，天使+轮由德联资本、道远资本联合领投，循光资本持续担任独家财务顾问。募集资金将用于推动公司的技术验证与产业化落地。 华超神控于2025年创立，创始人李昕是中国科学院与德国弗劳恩霍夫IGD研究所联合培养生物医学工程博士，曾任GE医疗全球科研中心"
  },
  {
    "id": "rss:https://36kr.com/p/3843764238174729?f=rss",
    "domain": "大厂 AI 动态",
    "title": "8点1氪丨八家上市公司集中公告“补税”；ChatGPT将迎来史上最大幅度升级；高考新增AI监考员，自动截取异常录像",
    "url": "https://36kr.com/p/3843764238174729?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T00:01:39+00:00",
    "summary": "今日热点导览 AI等机器网络请求量首超人类 瑞幸咖啡回应拿铁去冰仅半杯 宗馥莉自有品牌KELLYONE回归 多家低成本航空公司对登机箱登机收费 黄仁勋会见韩国两大游戏商代表共商游戏AI合作方案 TOP3大新闻 八家上市公司集中公告“补税”&nbsp; 6月1日至6日，不到一周内，八家A股上市公司先后披露补缴税款公告。这八家公司合计补缴税款及滞纳金约4亿元。其中，苹果中国最大授权经销商爱施德（002"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3844252140046849?f=rss",
    "domain": "大厂 AI 动态",
    "title": "乘联分会：5月新能源乘用车市场零售95万辆，同比下降7.5%",
    "url": "https://36kr.com/newsflashes/3844252140046849?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T08:15:30+00:00",
    "summary": "36氪获悉，乘联分会公布数据显示，5月新能源乘用车市场零售95.0万辆，同比下降7.5%，环比增长12.4%；1-5月新能源乘用车市场零售369.7万辆，同比下降15.1%。5月常规燃油乘用车零售56万辆，同比下降39%，环比增长5%。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3844251133970949?f=rss",
    "domain": "大厂 AI 动态",
    "title": "乘联分会：5月全国乘用车市场零售151万辆，同比下降22.1%",
    "url": "https://36kr.com/newsflashes/3844251133970949?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T08:14:28+00:00",
    "summary": "36氪获悉，乘联分会公布数据显示，5月1-31日，全国乘用车市场零售151.0万辆，同比下降22.1%，环比增长9.2%；今年以来累计零售709.9万辆，同比下降19.5%。2026年5月国内乘用车市场呈现总量承压、环比走强、结构极致分化的运行态势，整体未实现实质性复苏。本月小幅回暖主要得益于车市“反内卷”成效凸显，车企促销力度趋于稳定，淡化了消费者降价观望预期，叠加北京车展的热度提振，释放了部分"
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 1053,
    "published_at": "2026-06-04T22:48:19+00:00",
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
    "id": "hn:48385866",
    "domain": "股票",
    "title": "SpaceX's IPO is a disaster waiting to happen for your pension fund",
    "url": "https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/",
    "source": "anonymousDan",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436328",
    "domain": "股票",
    "title": "Musk's SpaceX IPO Narrative Is a Whole New Level of Bullshit",
    "url": "https://text.tchncs.de/chronik-des-laufenden-wahnsinns/h1elon-musk-has-spouted-his-fair-share-of-bullshit-but-his-latest-claims-about",
    "source": "doener",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-07T16:24:21+00:00",
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
    "id": "wscn:3774094",
    "domain": "股票",
    "title": "大周期上行的纵深与波折",
    "url": "https://wallstreetcn.com/articles/3774094",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T08:15:16+00:00",
    "summary": "申银万国认为，当前行情接近高位，6-7月或迎快速调整（波折）。但因宏观未恶化、AI趋势未证伪且居民资金有入市空间，大周期上行趋势不改。行情的“纵深”将由科技产业拓展与广泛的基本面改善驱动。预计下半年开启新一轮上涨，看好AI、新消费、出海及战略资源。"
  },
  {
    "id": "wscn:3774102",
    "domain": "股票",
    "title": "大华银行中国迎来新掌门，郑濬接棒行长兼CEO",
    "url": "https://wallstreetcn.com/articles/3774102",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:46:54+00:00",
    "summary": "总部位于新加坡的大华银行中国迎来管理层调整。\n6月8日，大华银行宣布，现任香港分行行政总裁郑濬将出任..."
  },
  {
    "id": "wscn:3774101",
    "domain": "股票",
    "title": "T+1整改正式收官，30余家中小银行暂停货基申购",
    "url": "https://wallstreetcn.com/articles/3774101",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:46:21+00:00",
    "summary": "随着货币基金销售业务T+1资金划转整改过渡期于5月底结束，一轮持续半年的行业调整正式落地。\n近期，多..."
  },
  {
    "id": "wscn:3774099",
    "domain": "股票",
    "title": "从合规条线进入经营班子，杨文化升任光大银行副行长",
    "url": "https://wallstreetcn.com/articles/3774099",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:45:41+00:00",
    "summary": "光大银行管理层再添一员。\n6月5日，光大银行发布公告称，国家金融监督管理总局已于6月2日核准杨文化担..."
  },
  {
    "id": "wscn:3774098",
    "domain": "股票",
    "title": "从中国区负责人到再掌理财子，范华回归贝莱德建信理财",
    "url": "https://wallstreetcn.com/articles/3774098",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:45:04+00:00",
    "summary": "6月5日，国家金融监督管理总局上海监管局发布批复，核准范华担任贝莱德建信理财有限责任公司总经理。\n此..."
  },
  {
    "id": "wscn:3774096",
    "domain": "股票",
    "title": "仓位崩了，故事还在——读懂这轮AI股大跌的底层逻辑",
    "url": "https://wallstreetcn.com/articles/3774096",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:31:09+00:00",
    "summary": "全球科技股暴跌主因是AI芯片板块仓位极度拥挤、杠杆过高，非农成为去杠杆的扳机。抛压集中在前期涨幅最大的个股，是典型的去杠杆而非基本面崩塌。AI需求未见转弱，关键看后续美国CPI、美联储议息及韩股能否止跌，判断这是阶段性出清还是更长调整的开端。"
  },
  {
    "id": "wscn:3774095",
    "domain": "股票",
    "title": "AI芯片股涨势扭曲亚洲基准指数，主动基金陷入“越涨越卖”循环",
    "url": "https://wallstreetcn.com/articles/3774095",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:20:58+00:00",
    "summary": "台积电、三星和SK海力士暴涨使两大旗舰指数退化为个股押注工具，在MSCI亚太（除日本）指数中权重占比近1/3。这导致主动型基金经理触及持仓上限，被迫陷入“越涨越卖”的被动减持循环，也加速了数百亿资金流向无需受此限制的被动型基金。"
  },
  {
    "id": "wscn:3774093",
    "domain": "股票",
    "title": "拥挤、估值、加息预期扰动不断：科技是否仍然值得坚守？",
    "url": "https://wallstreetcn.com/articles/3774093",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:19:12+00:00",
    "summary": "非农数据暴击、半导体指数单日暴跌逾10%，加息恐慌席卷市场——然而广发、东吴等多家机构逆势研判：EPS上修斜率未逆转、AI产业需求持续扩张，历史五大案例均指向同一结论，科技行情的真正\"杀手\"从不是利率，科技风格调整或是最佳布局窗口，四大事件决定下一阶段节奏。"
  },
  {
    "id": "wscn:3774090",
    "domain": "股票",
    "title": "IMF总裁警告：全球经济尚未准备好应对不断累积的冲击",
    "url": "https://wallstreetcn.com/articles/3774090",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:13:58+00:00",
    "summary": "IMF总裁Georgieva罕见发出警告：历经疫情、俄乌冲突、关税动荡后，全球经济仍未做好迎接持续冲击的准备，\"冲击不会消失\"将成新常态。她更直指AI浪潮或重蹈全球化覆辙——繁荣背后，无数社区岗位可能再度被\"掏空\"而无人关注。"
  },
  {
    "id": "wscn:3774082",
    "domain": "股票",
    "title": "SemiAnalysis回应Vera SOCAMM争议：质疑者没去过Computex海力士展台",
    "url": "https://wallstreetcn.com/articles/3774082",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T07:13:27+00:00",
    "summary": "英伟达Vera Rubin平台SOCAMM内存削减至28TB一度引爆市场，美光单日暴跌13%。但SemiAnalysis直指质疑者\"没去Computex的Hynix展台\"——SK Hynix已现场展示192GB SOCAMM2实物。更关键的是：容量下调或非需求降温，而是HBM产能挤出效应的映射。"
  },
  {
    "id": "wscn:3774062",
    "domain": "股票",
    "title": "全球：“殊途同归”的K型分化",
    "url": "https://wallstreetcn.com/articles/3774062",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T06:49:57+00:00",
    "summary": "中金表示，2026年全球市场呈现极致分化——AI科技一枝独秀，消费内需全面落后。这场\"K型分化\"并非偶然，而是中美信用周期共同演绎的结构性宿命：科技分子强劲奔跑，内需分母持续承压。下半年变数聚焦油价与美债利率，高油价利中国防御，低油价利美国内需修复。配置上，美债兼具胜率与赔率，恒生科技赔率突出，科技主线拥挤但趋势未尽。"
  },
  {
    "id": "wscn:3774092",
    "domain": "股票",
    "title": "欧央行本周加息在即，经济学家警告：或在重蹈2011年政策错误",
    "url": "https://wallstreetcn.com/articles/3774092",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T06:47:24+00:00",
    "summary": "欧央行本周料将宣布加息，但这一决定正引发激烈争议。多位经济学家警告，在欧元区经济加速萎缩、美伊和平谈判仍存变数之际，欧央行急于捍卫抗通胀信誉，可能正在重演2011年两度加息后被迫全面逆转的历史悲剧——而那次政策失误，最终将欧元区推入双底衰退的深渊。"
  },
  {
    "id": "wscn:3774089",
    "domain": "股票",
    "title": "科技股下跌不能甩锅给非农数据",
    "url": "https://wallstreetcn.com/articles/3774089",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T06:36:49+00:00",
    "summary": "东吴证券首席经济学家陈李认为，科技股暴跌根源在于流动性与估值问题：板块估值过高、杠杆交易拥挤引发踩踏，叠加巨头密集融资与苛刻的业绩预期。当前AI产业基本面未变，需求仍在扩张。此次调整仅为资金再平衡而非周期顶点，趋势未反转前可逢低吸纳，但需密切警惕市场叙事框架的松动。"
  },
  {
    "id": "wscn:3774091",
    "domain": "股票",
    "title": "下周美联储会议最大悬念：沃什会向特朗普低头，还是向加息靠拢？",
    "url": "https://wallstreetcn.com/articles/3774091",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T06:27:42+00:00",
    "summary": "新任美联储主席沃什首次议息会议即将登场，三大信号或揭示政策转向：删除\"宽松偏向\"措辞、点阵图出现加息预期、通胀风险权重升温。这位曾力倡降息的新主席，能否在鹰派共识与白宫压力间走出独立路线？分析人士警告，最早今夏或现2023年来首次加息。"
  },
  {
    "id": "wscn:3774056",
    "domain": "股票",
    "title": "韩股“过山车”！黄仁勋救场反弹后再跌超7%，油价飙升5%、黄金跌破4300",
    "url": "https://wallstreetcn.com/articles/3774056",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T06:14:25+00:00",
    "summary": "韩国股市周一遭遇暴跌8.2%并触发熔断。尽管盘中黄仁勋抛出芯片采购利好与韩总统李在明“喊话”救场，但由于AI交易退潮且本周美国CPI等大考在即，午后市场信心再度崩溃，韩股再次下跌超7%。现货黄金周一下跌约1%至每盎司4287美元。油价上涨进一步推高通胀预期，令本已因强劲就业数据而趋紧的货币政策前景愈发复杂。"
  },
  {
    "id": "wscn:3774087",
    "domain": "股票",
    "title": "“你应该感到高兴！”黄仁勋力挺AI：暴跌后终于能打折买了",
    "url": "https://wallstreetcn.com/articles/3774087",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T05:57:56+00:00",
    "summary": "全球科技股遭遇抛售，英伟达CEO黄仁勋却在首尔高呼\"现在是打折买入的好时机\"，并断言AI基础设施建设才刚起步，必将复制互联网崛起之路。与此同时，英伟达与SK海力士宣布签署多年协议，联合开发下一代AI内存芯片，消息提振市场情绪，恐慌性抛售势头有所缓和。"
  },
  {
    "id": "wscn:3774080",
    "domain": "股票",
    "title": "英伟达与LG集团宣布共建AI工厂，覆盖机器人、数据中心、自动驾驶",
    "url": "https://wallstreetcn.com/articles/3774080",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T05:56:29+00:00",
    "summary": "英伟达与LG联手建设AI工厂。LG引入GR00T与Cosmos模型研发CLoiD家用机器人、建实体AI数据厂；结合Blackwell GPU推进韩国主权模型EXAONE商业化；并联合开发800V直流储能与液冷模块，打造涵盖车载ADAS到自主制造的统一工作流。"
  },
  {
    "id": "wscn:3774081",
    "domain": "股票",
    "title": "亚洲煤炭价格涨至22个月高位，印尼出口新规收紧供应",
    "url": "https://wallstreetcn.com/articles/3774081",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T05:48:41+00:00",
    "summary": "供应端，印尼新系统导致发货延误，买家转向澳煤填补缺口；需求端，东北亚夏季高温拉升用电负荷，且日本因天然气供应受地缘冲击而加速转向煤电。多重因素促使纽卡斯尔期货创近两年新高，市场呈现供应紧缺态势。"
  },
  {
    "id": "wscn:3774065",
    "domain": "股票",
    "title": "创业板重挫4%，科技股、有色金属集体下跌，机器人逆势活跃，恒科指跌超3%，沪银狂泻10%",
    "url": "https://wallstreetcn.com/articles/3774065",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T05:42:49+00:00",
    "summary": "个股跌多涨少，沪深京三市超4500股飘绿，上午半天成交1.8万亿。沪深两市半日成交额1.77万亿，较上个交易日缩量近1100亿。板块方面，半导体、太空光伏、存储器、工业金属、光刻机、锂电池、AI算力、跨境电商、创新药题材跌幅靠前；大金融、人形机器人概念股走强。"
  },
  {
    "id": "wscn:3773239",
    "domain": "股票",
    "title": "第三代半导体“双雄会”：GaN凭什么在800V高压时代与SiC分庭抗礼？",
    "url": "https://wallstreetcn.com/premium/articles/3773239?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T05:42:00+00:00",
    "summary": "AI的尽头是电力，电力的答案是GaN，800V架构引爆氮化镓第二增长曲线。"
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
    "id": "hn:48419956",
    "domain": "股票",
    "title": "Nasdaq falls 4% and suffers worst day since April 2025 traders flee chip stocks",
    "url": "https://www.cnbc.com/2026/06/04/stock-market-today-live-updates.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-06T00:02:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48281983",
    "domain": "股票",
    "title": "Show HN: A website that tracks every stock trade Congress makes",
    "url": "https://congress.kadoa.com/",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-05-26T16:28:56+00:00",
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
    "id": "hn:48285468",
    "domain": "股票",
    "title": "There are now more ETFs than stocks in the US",
    "url": "https://www.apollo.com/wealth/the-daily-spark/more-etfs-than-stocks",
    "source": "akyuu",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-05-26T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48280561",
    "domain": "股票",
    "title": "Stockholm poised to become leading European geospatial intel player",
    "url": "https://www.intelligenceonline.com/europe-russia/2026/05/26/stockholm-poised-to-become-leading-european-geospatial-intel-player,110772386-eve",
    "source": "alephnerd",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-05-26T14:44:31+00:00",
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
    "id": "hn:48377119",
    "domain": "股票",
    "title": "Short Seller (Andrew Left) Convicted for $21M Stock Market Manipulation Scheme",
    "url": "https://www.justice.gov/opa/pr/activist-short-seller-convicted-21m-stock-market-manipulation-scheme",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-02T22:19:48+00:00",
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
    "id": "hn:48297843",
    "domain": "股票",
    "title": "Steam Deck OLED is back in stock, with a price increase for both models",
    "url": "https://store.steampowered.com/news/group/45479024/view/672869045073085538",
    "source": "no_news_is",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-27T17:50:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48330421",
    "domain": "股票",
    "title": "The record divide between corporate profits and worker pay",
    "url": "https://www.wsj.com/finance/stocks/the-record-divide-between-corporate-profits-and-worker-pay-ea4c75bc",
    "source": "hhs",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-29T22:55:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48088151",
    "domain": "金融",
    "title": "Maryland citizens hit with $2B power grid upgrade for out-of-state AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises",
    "source": "lemonberry",
    "platform": "hackernews",
    "points": 319,
    "published_at": "2026-05-10T21:16:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48108313",
    "domain": "金融",
    "title": "US inflation jumps to 3.8% as energy costs surge from Iran war",
    "url": "https://www.bbc.com/news/articles/c202pgxx89lo",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 260,
    "published_at": "2026-05-12T13:51:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48100152",
    "domain": "金融",
    "title": "590k buyers paid $59M for Trump's gold phone, but not one has shipped",
    "url": "https://finance.yahoo.com/markets/stocks/articles/590-000-buyers-paid-59-223500998.html",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-05-11T20:19:38+00:00",
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
    "id": "hn:48438281",
    "domain": "金融",
    "title": "Boomers are hoarding most of America's wealth and power",
    "url": "https://finance.yahoo.com/economy/articles/golden-years-not-golden-boomers-113000201.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-07T20:35:10+00:00",
    "summary": ""
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
    "id": "rss:https://arxiv.org/abs/2606.06651",
    "domain": "金融",
    "title": "Temporal Dynamics of Development Aid in Africa: Evidence from a Staggered Difference-in-Differences Study of China and World Bank Projects in Africa",
    "url": "https://arxiv.org/abs/2606.06651",
    "source": "Mattias Antar, Adel Daoud, Connor T. Jerzak",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.06651v1 Announce Type: new Abstract: Subnational studies of aid effectiveness often rely on repeated cross-sections or nighttime lights, making it difficult to separate local treatment effe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.06652",
    "domain": "金融",
    "title": "Probabilistic Risk Sensitivity and Loss Aversion in Cumulative Prospect Theory",
    "url": "https://arxiv.org/abs/2606.06652",
    "source": "Symeon Vaidanis, Marios Kountouris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.06652v1 Announce Type: new Abstract: This paper develops a binary-gamble framework for characterizing risk sensitivity and loss aversion in Cumulative Prospect Theory (CPT). The proposed pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.06737",
    "domain": "金融",
    "title": "Fast-excursion limit of the Heston model",
    "url": "https://arxiv.org/abs/2606.06737",
    "source": "Ryan McCrickerd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.06737v1 Announce Type: new Abstract: This article introduces an unconventional model for price processes in finance that emerges from the classical Heston model under Mechkov's fast-reversi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07059",
    "domain": "金融",
    "title": "Diffusive in plain sight: An inconspicuous law of market impact",
    "url": "https://arxiv.org/abs/2606.07059",
    "source": "Julius F. Bonart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.07059v1 Announce Type: new Abstract: Decomposing impact as the difference between realized and counterfactual returns and requiring both to be diffusive yields an identity that restricts ad"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07109",
    "domain": "金融",
    "title": "Museums as Policy Tools: The Behavioral Impact of Cultural Experiences",
    "url": "https://arxiv.org/abs/2606.07109",
    "source": "Paolo Pin, Roberto Rozzi, Alessandro Stringhi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.07109v1 Announce Type: new Abstract: Museums can serve as policy tools when their content is purposefully curated. We designed a framed field experiment at the Santa Maria della Scala museu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07445",
    "domain": "金融",
    "title": "Bubbles vs. Baselines: Token Valuation and Institutional Capital in PoS Networks under EIP-1559",
    "url": "https://arxiv.org/abs/2606.07445",
    "source": "Mikhail Perepelitsa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.07445v1 Announce Type: new Abstract: This paper presents an open-economy macroeconomic equilibrium model for Proof-of-Stake (PoS) networks with fee-burn mechanics (EIP-1559) that formalizes"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05667",
    "domain": "金融",
    "title": "Sustainability by Design in Decentralized Autonomous Organizations: An Empirical Review of Governance, Innovation, and Institutional Design",
    "url": "https://arxiv.org/abs/2606.05667",
    "source": "Yutian Wang, Luyao Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.05667v1 Announce Type: cross Abstract: Recent innovation theories on economics remain largely grounded in assumptions of hierarchical firms and closed organizational boundaries, offering li"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07276",
    "domain": "金融",
    "title": "The Balance Property: The Constrained Case, with a View on Risk Sharing",
    "url": "https://arxiv.org/abs/2606.07276",
    "source": "Mario V. W\\\"uthrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.07276v1 Announce Type: cross Abstract: The balance property is an important property of fitted statistical models deployed for insurance pricing. It guarantees that the total actuarial pric"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07290",
    "domain": "金融",
    "title": "Boundary behaviour of the Volterra square-root process",
    "url": "https://arxiv.org/abs/2606.07290",
    "source": "Martin Friesen, Stefan Gerhold, Kristof Wiedermann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.07290v1 Announce Type: cross Abstract: In this work, we study the boundary behaviour of the Volterra square- root process on $\\mathbb{R}_+$. For regular Volterra kernels, we establish a tim"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07450",
    "domain": "金融",
    "title": "Information Networks of Stock Prices",
    "url": "https://arxiv.org/abs/2606.07450",
    "source": "Muhammad Aldy Hassan, Hokky Situngkir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.07450v1 Announce Type: cross Abstract: The collective movement of stock prices harbors complex interdependencies that are conventionally simplified only through a linear lens. This paper ex"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07489",
    "domain": "金融",
    "title": "How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope",
    "url": "https://arxiv.org/abs/2606.07489",
    "source": "Jeremy Yang, Kate Zyskowski, Noah Yonack, Jerry Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2606.07489v1 Announce Type: cross Abstract: Frontier AI systems are bridging the gap between intelligence and utility by shifting from conversational assistants to autonomous agents that execute"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.07652",
    "domain": "金融",
    "title": "The heterogeneous impact of the EU-Canada agreement with causal machine learning",
    "url": "https://arxiv.org/abs/2407.07652",
    "source": "Lionel Fontagn\\'e, Francesca Micocci, Armando Rungi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2407.07652v5 Announce Type: replace Abstract: This paper introduces a causal machine learning approach to investigate the effects of free trade agreements and applies it to the EU-Canada Compreh"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.13421",
    "domain": "金融",
    "title": "Market Making and Transient Impact in Spot FX",
    "url": "https://arxiv.org/abs/2601.13421",
    "source": "Alexander Barzykin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2601.13421v2 Announce Type: replace Abstract: Dealers in foreign exchange markets provide bid and ask prices to their clients at which they are happy to buy and sell, respectively. To manage ris"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.26076",
    "domain": "金融",
    "title": "The Financialization of Proof-of-Stake: Asymptotic Centralization under Exogenous Risk Premiums",
    "url": "https://arxiv.org/abs/2604.26076",
    "source": "Mikhail Perepelitsa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2604.26076v3 Announce Type: replace Abstract: This paper introduces a heterogeneous macroeconomic model of a Proof-of-Stake (PoS) network to analyze the long-term centralizing effects of externa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.01176",
    "domain": "金融",
    "title": "Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization",
    "url": "https://arxiv.org/abs/2605.01176",
    "source": "Yi Wang, Takashi Hasuike",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2605.01176v3 Announce Type: replace Abstract: Decision-focused learning (DFL) is attractive for portfolio optimization because it trains predictors according to downstream decision quality rathe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.26363",
    "domain": "金融",
    "title": "Multiperiod Groundwater Markets",
    "url": "https://arxiv.org/abs/2605.26363",
    "source": "Igor Cialenco, Michael Ludkovski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T04:00:00+00:00",
    "summary": "arXiv:2605.26363v2 Announce Type: replace Abstract: Motivated by the emergence of local groundwater exchanges, we construct and analyze stochastic models of dynamic groundwater markets. Our primary fo"
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
    "id": "hn:48271942",
    "domain": "金融",
    "title": "Show HN: Fungible – A local personal finance app in the terminal",
    "url": "https://github.com/tomfunk/fungible",
    "source": "tomfunk",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-05-25T21:35:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377419",
    "domain": "金融",
    "title": "FBI charges two NIH researchers with smuggling monkeypox to US from Congo",
    "url": "https://www.justice.gov/usao-edmi/pr/feds-charge-foreign-nationals-working-national-institutes-health-smuggling-monkeypox",
    "source": "delichon",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-02T22:58:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271001",
    "domain": "金融",
    "title": "Stablecoins Are Private Money. That's Why They're a Risk to the Economy",
    "url": "https://www.wsj.com/finance/currencies/stablecoins-are-private-money-thats-why-theyre-a-risk-to-the-economy-d3498171",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-25T20:02:09+00:00",
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
    "id": "hn:48104043",
    "domain": "金融",
    "title": "Arcadia, CA, Mayor Federally Charged with Acting as Illegal Agent of PRC, Pleads",
    "url": "https://www.justice.gov/usao-cdca/pr/arcadia-mayor-federally-charged-acting-illegal-agent-peoples-republic-china",
    "source": "737min",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-05-12T03:59:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48307404",
    "domain": "金融",
    "title": "Why Tesla's AI trainers don't trust its self-driving tech – or its safety stats",
    "url": "https://www.reuters.com/investigations/why-teslas-ai-trainers-dont-trust-its-self-driving-tech-or-its-safety-stats-2026-05-28/",
    "source": "puzzlingcaptcha",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-28T11:21:18+00:00",
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
    "id": "hn:48287165",
    "domain": "金融",
    "title": "Trump administration proposes NDAs for federal workers",
    "url": "https://www.reuters.com/world/us/trump-administration-proposes-non-disclosure-agreements-us-federal-workers-2026-05-26/",
    "source": "SubiculumCode",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-26T22:58:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48199462",
    "domain": "金融",
    "title": "Invisible_playwright: Stealth Firefox that passes every bot detection test",
    "url": "https://github.com/feder-cr/invisible_playwright",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-05-19T20:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48115538",
    "domain": "金融",
    "title": "America is experiencing a productivity miracle",
    "url": "https://www.economist.com/finance-and-economics/2026/05/11/america-is-experiencing-a-productivity-miracle",
    "source": "mackmcconnell",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-12T22:39:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229518",
    "domain": "金融",
    "title": "Show HN: Smithereen – an early-Facebook-style Fediverse server",
    "url": "https://smithereen.software",
    "source": "grishka",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-21T22:18:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48130202",
    "domain": "金融",
    "title": "Federalism for Anti-Fascists",
    "url": "https://medium.com/@carmitage/federalism-for-anti-fascists-e83fb20c6fc2",
    "source": "hkhn",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-05-14T01:49:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48225108",
    "domain": "金融",
    "title": "Jeff Bezos says bottom half of U.S. earners should pay no federal income tax",
    "url": "https://www.cbsnews.com/news/jeff-bezos-zero-federal-income-tax-lower-earners/",
    "source": "johnshades",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-05-21T16:11:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48222708",
    "domain": "金融",
    "title": "Fedora Retiring Its Deepin Desktop Packages",
    "url": "https://www.phoronix.com/news/Fedora-Removing-Deepin",
    "source": "AdmiralAsshat",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-21T14:00:31+00:00",
    "summary": ""
  }
]
```
