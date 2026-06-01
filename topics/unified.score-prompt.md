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
- **每个域至少 1 条头条**（4-5 条头条要分布在 ≥3 个域，避免某个域读者打开邮件看到空白）

---

## 输入（变量替换）

- 今日日期：`2026-06-01`
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
- **本期用户特别请求**（可能为空）：`想看一些跟ai技术相关的`
- 候选内容池（已合并所有域，每条带 `domain` 字段）：见末尾

---

## 输出格式（严格 JSON）

```json
{
  "date": "2026-06-01",
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

用户在网页"立刻生成"按钮上提交了请求并附了留言：

> **想看一些跟ai技术相关的**

评分时优先考虑这条诉求：让 ≥1 条头条贴合，且在 intro 里提一句"按你的请求侧重 XX"。

---

## 候选池（已合并所有域）

```json
[
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 941751,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 849237,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 745439,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "点赞+评论+关注，AI 会发你详细文档（不关注会导致无法发送私信给你，因为批量发太多给陌生人，会平台限流）"
  },
  {
    "id": "bvid:BV1wuQEBDEN8",
    "domain": "AI",
    "title": "【2026 最新版】｜字节大佬亲授 Claude Code 全栈教程，从入门到精通全覆盖，小白 10 分钟上手，干货无废话，建议收藏！",
    "url": "http://www.bilibili.com/video/av116408209967652",
    "source": "跟着李迟学AI",
    "platform": "bilibili",
    "points": 237404,
    "published_at": "2026-04-15T10:23:31+00:00",
    "summary": "这也是2026B站最新最系统的Claude Code + 自动化工作流教学课程，小白10分钟轻松上手！\n求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~求三连~"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 228943,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1E6CFBMEnk",
    "domain": "AI",
    "title": "【2025最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！cursor教程｜AI 编程",
    "url": "http://www.bilibili.com/video/av115524067463218",
    "source": "诸葛老师本人",
    "platform": "bilibili",
    "points": 191249,
    "published_at": "2025-11-10T06:52:42+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\n‍视频配套笔记、AI大模型笔记代码：https://www.bilibili.com/read/cv43354937/?jump_opus=1"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 158928,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 152345,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 149152,
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
    "points": 139889,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 83236,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 79868,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 62103,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1kJ2LYME9t",
    "domain": "AI",
    "title": "AI code 实战｜一小时用 cursor 发布上线微信小程序项目",
    "url": "http://www.bilibili.com/video/av113267162743660",
    "source": "AIcode扣德哥_Ai编程",
    "platform": "bilibili",
    "points": 61583,
    "published_at": "2024-10-07T17:04:20+00:00",
    "summary": "FAQ ：cursor 如何与微信小程序打通\nhttps://docs.qq.com/doc/DWmhLdXNFdUVZbFdC\n（上线两天收到了10+问题，把主要的解法贴在上面）\n\n用 cursor 完成小程序开发，实战全记录，核心心得——\n做好产品设计。\n提前规划版本和功能，思考实现路径。\n做好技术选型。\n主次分明，先完成核心功能。"
  },
  {
    "id": "bvid:BV1MJXZBgE32",
    "domain": "AI",
    "title": "AI Coding 进阶：从 Vibe/Plan/Spec 到 Harness Engineering 与 Agent Teams",
    "url": "http://www.bilibili.com/video/av116334289491216",
    "source": "Qoder",
    "platform": "bilibili",
    "points": 59559,
    "published_at": "2026-04-02T09:00:33+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1RJPSz4EMW",
    "domain": "AI",
    "title": "（上集）分享一个非常不错的 Claude Code 中转站，不用再花大量时间精力去死磕美区虚拟卡、头疼配置网络环境、焦虑高额美金账单了",
    "url": "http://www.bilibili.com/video/av116198075272768",
    "source": "崔总干货确实多",
    "platform": "bilibili",
    "points": 54470,
    "published_at": "2026-03-09T07:40:57+00:00",
    "summary": "这期视频为大家分享一个近期实测表现不错的 API 直连claude code中转站。\n\n对于经常使用 AI 辅助编程或进行自动化开发、数据分析、文件处理的朋友来说，直接使用claude code官方 API 往往面临网络环境要求严苛、支付门槛高以及封号风险。为了帮助到大家，我测试了国内十多家中转方案，发现目前这个平台在稳定性和计费透明度上比较契合日常开发需求。\n\n💡 核心功能与优势：\n网络与防封："
  },
  {
    "id": "bvid:BV1CDVu6TEnv",
    "domain": "AI",
    "title": "Vibe coding成瘾。一开始觉得很兴奋，但是玩多了就有一种游戏开挂的感觉。像这个小demo古法编程怎么也要写两天，AI来写15分钟搞定了，一开始挺期待的…",
    "url": "http://www.bilibili.com/video/av116661831208897",
    "source": "工科男孙老师",
    "platform": "bilibili",
    "points": 53466,
    "published_at": "2026-05-30T05:23:02+00:00",
    "summary": "Vibe coding成瘾。一开始觉得很兴奋，但是玩多了就有一种游戏开挂的感觉。像这个小demo古法编程怎么也要写两天，AI来写15分钟搞定了，一开始挺期待的，过去没时间玩的东西现在都能很快搞定，但是做完毫无快感。就像是上班后买了大学时心心念念的psp游戏机，但是再也没有借同学的那种快感了。"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 50582,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1y9yyYDEUN",
    "domain": "AI",
    "title": "6个超实用的Cursor小技巧：效率提升200%，免费无限量使用Cursor Pro",
    "url": "http://www.bilibili.com/video/av113365611582948",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 49097,
    "published_at": "2024-10-25T04:10:00+00:00",
    "summary": "海外支付平台WildCard：https://bewildcard.com/i/BYWIND （有折扣）"
  },
  {
    "id": "bvid:BV1fM8JzCErf",
    "domain": "AI",
    "title": "【实用教程】完美解决Cursor地区限制使用claude/gpt问题！",
    "url": "http://www.bilibili.com/video/av114930506340006",
    "source": "洞犀AI大模型讲堂",
    "platform": "bilibili",
    "points": 41078,
    "published_at": "2025-07-28T11:02:31+00:00",
    "summary": "cursor 最近发布了新的模型地区可用性政策，中国地区无法使用Claude/GPT/gemini，如果你遇到类似的问题，可以参考本期教程视频的方法，可以继续使用Claude大模型。"
  },
  {
    "id": "bvid:BV1YojdzzE77",
    "domain": "AI",
    "title": "cursor+claude-4开发前后端项目,全程解读，干货满满",
    "url": "http://www.bilibili.com/video/av114579409469776",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 32579,
    "published_at": "2025-05-27T11:01:30+00:00",
    "summary": "本期视频主题\n零代码使用cursor完成一个前后端分离的小项目\n前端: vue3\n后端: java springboot\n关联知识点：\nCursor 新手教程③： Cursor rules 让 AI 更懂你\ncursor实战系列：0到1开发一个小程序，需求整理、小程序注册备案\n一、前后端开发的两种模式\n二、项目初始化\n三、前后端的协作流程\n四、文档阶段\n五、拆分前后端任务\n六、启动前后端测试"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29184,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1e7VA6vEJU",
    "domain": "AI",
    "title": "【2026最新】绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116640356304890",
    "source": "码士集团-马小安",
    "platform": "bilibili",
    "points": 25462,
    "published_at": "2026-05-26T10:22:46+00:00",
    "summary": "绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！\n配套课件笔记/PPT已备好，另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~"
  },
  {
    "id": "bvid:BV116P7zXEkE",
    "domain": "AI",
    "title": "纯小白教学：用vibecoding做个人网站",
    "url": "http://www.bilibili.com/video/av116160209093711",
    "source": "阿囤囤-庞滚滚",
    "platform": "bilibili",
    "points": 24085,
    "published_at": "2026-03-02T15:11:36+00:00",
    "summary": "不需要🪜哦～"
  },
  {
    "id": "bvid:BV1v8mtBpEwK",
    "domain": "AI",
    "title": "Kiro 上手必看：从Vibe 到 Spec 全攻略！",
    "url": "http://www.bilibili.com/video/av115695564102585",
    "source": "AI编程瓜哥",
    "platform": "bilibili",
    "points": 20453,
    "published_at": "2025-12-10T13:49:11+00:00",
    "summary": "一眼懂，Vibe coding 和Spec Coding，双模式实战。"
  },
  {
    "id": "bvid:BV1JcDSBYE4V",
    "domain": "AI",
    "title": "新版 Cursor 看不到代码了？5 分钟学会新界面所有操作",
    "url": "http://www.bilibili.com/video/av116390174393526",
    "source": "未生AI",
    "platform": "bilibili",
    "points": 19901,
    "published_at": "2026-04-12T05:55:17+00:00",
    "summary": "Cursor 最新版本的界面。只有一个文字输入框。没有代码，没有文件树，没有你以前熟悉的任何东西。\n\n很多人打开之后直接懵了——这怎么用？我的代码呢？这期视频，我就来告诉你，新版 Cursor 到底怎么用。\n\nCursor 的改版，不只是界面变了。\n\n所有 AI 编程工具，以前的形态都是一样的——左边文件树，右边代码，AI 在旁边帮你补全。\n\n这个形态本质上还是：人在主导代码，AI 在辅助人。\n\n"
  },
  {
    "id": "bvid:BV1aNb5z7Eqb",
    "domain": "AI",
    "title": "cursor一键重置机器码不需要重装系统",
    "url": "http://www.bilibili.com/video/av115010617544835",
    "source": "玩转Code",
    "platform": "bilibili",
    "points": 18431,
    "published_at": "2025-08-11T14:35:16+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JfT4zVEa5",
    "domain": "AI",
    "title": "Cursor1.0新特性BugBot自动化代码Code Review使用教程+实测",
    "url": "http://www.bilibili.com/video/av114630882037891",
    "source": "码里奥Ziho",
    "platform": "bilibili",
    "points": 15082,
    "published_at": "2025-06-05T13:05:30+00:00",
    "summary": "Cursor推出了新的1.0版本，本视频对新特性Bugbot做了一个教程+实测\nBugBot可以在Github进行PR (Pull Request) 的时候，通过AI大模型帮助我们进行CR (Code Review)\n本视频用一个例子演示了如何使用Bugbot功能，并且最后给出了实测的结果\n\n感谢支持！！！欢迎三连\n个人公众号 【码里奥】"
  },
  {
    "id": "bvid:BV1ZFc2epE4s",
    "domain": "AI",
    "title": "Cursor+VS2022编译器 准备cursor的c++开发环境",
    "url": "http://www.bilibili.com/video/av113820676655607",
    "source": "新手村养牛人",
    "platform": "bilibili",
    "points": 14040,
    "published_at": "2025-01-13T11:00:14+00:00",
    "summary": "cmake_minimum_required(VERSION 3.23)\nproject(CursorVs2022)\nset(CMAKE_CXX_STANDARD 17)\n\nset(CMAKE_INCLUDE_CURRENT_DIR ON)\nSET(CMAKE_BUILD_TYPE Debug)\nset(CMAKE_AUTOMOC ON)\nset(CMAKE_AUTOUIC ON)\nset(CMA"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 13421,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1cNV56VEBd",
    "domain": "AI",
    "title": "当你装了codex后会发生什么……",
    "url": "http://www.bilibili.com/video/av116663542356559",
    "source": "AIwood爱屋研究室",
    "platform": "bilibili",
    "points": 10762,
    "published_at": "2026-05-30T12:38:28+00:00",
    "summary": "剧情纯属恶搞，如有雷同，算你NB！"
  },
  {
    "id": "bvid:BV1jsV861EVM",
    "domain": "AI",
    "title": "【2026胎教级】Claude Code全栈教程，从入门到精通，搞定所有开发场景，小白10分钟搞定，全程干货无废话，存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116657502687649",
    "source": "程序员黑梦",
    "platform": "bilibili",
    "points": 10749,
    "published_at": "2026-05-29T11:08:50+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10745,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1NYVG6jEKE",
    "domain": "AI",
    "title": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通",
    "url": "http://www.bilibili.com/video/av116662133132089",
    "source": "字节软件测试",
    "platform": "bilibili",
    "points": 10146,
    "published_at": "2026-05-30T06:39:27+00:00",
    "summary": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通"
  },
  {
    "id": "bvid:BV1rgNPenEsL",
    "domain": "AI",
    "title": "cursor0.45 重置方法！",
    "url": "http://www.bilibili.com/video/av113944643571652",
    "source": "想回家的前端开发",
    "platform": "bilibili",
    "points": 10144,
    "published_at": "2025-02-04T08:25:43+00:00",
    "summary": "发视频是因为不想让小白闲鱼。"
  },
  {
    "id": "bvid:BV1RCqPBFEDq",
    "domain": "AI",
    "title": "使用 Claude Code 从零到一开发项目",
    "url": "http://www.bilibili.com/video/av115848605932169",
    "source": "AgenticX",
    "platform": "bilibili",
    "points": 9954,
    "published_at": "2026-01-06T14:33:59+00:00",
    "summary": "我过去启动 Claude Code 项目的方式完全错误：只是简单输入 “claude”，然后毫无规划、毫无准备、毫无系统地自由发挥式提示——这就好比不画蓝图就直接盖房子。\n过去一年中，我用 Claude Code 构建了数十个项目，最终总结出一套简洁的三阶段系统（PSB：Plan-规划、Setup-设置、Build-构建），让每个项目从第一天起就轻松十倍。\n本视频中，我将分享自己每次启动新 Cla"
  },
  {
    "id": "bvid:BV15BGX63E2K",
    "domain": "AI",
    "title": "【5.28最新发布】claude桌面版安装教程！一周快速入门claude code保姆级教程！",
    "url": "http://www.bilibili.com/video/av116651194385987",
    "source": "是蒜七丫",
    "platform": "bilibili",
    "points": 9459,
    "published_at": "2026-05-28T08:19:55+00:00",
    "summary": "求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三"
  },
  {
    "id": "bvid:BV1oNVH6xEWS",
    "domain": "AI",
    "title": "Claude Code 国内直连保姆级教程｜10分钟从入门到精通，原理+安装+实战全覆盖，解锁Vibe Coding编程新范式",
    "url": "http://www.bilibili.com/video/av116667602503393",
    "source": "码士集团-小晨晨晨",
    "platform": "bilibili",
    "points": 8080,
    "published_at": "2026-05-31T06:14:34+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1gwk3Y8Ers",
    "domain": "AI",
    "title": "CURSOR 遇到机器上使用过多的免费账号",
    "url": "http://www.bilibili.com/video/av113663037931907",
    "source": "想回家的前端开发",
    "platform": "bilibili",
    "points": 8062,
    "published_at": "2024-12-16T14:51:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uXLz6NEp6",
    "domain": "AI",
    "title": "Cursor 推出史上最强模型 Composer 2.5，性能直逼Claude Opus 4.7，价格仅为1/10！Cursor 内部几乎全员弃用旧模型！",
    "url": "http://www.bilibili.com/video/av116600929852292",
    "source": "Terminator-AI",
    "platform": "bilibili",
    "points": 5412,
    "published_at": "2026-05-19T11:12:32+00:00",
    "summary": "本视频深度解析Cursor最新发布的Composer 2.5模型，其性能在SWE-Bench Multilingual等权威测试中直逼Claude Opus 4.7，而价格仅为前者的十分之一。\n\n核心亮点包括三大训练创新：使用文本反馈的针对性RL实现局部精准纠偏，合成任务数量达到Composer 2的25倍，以及通过分布式正交化Muon和双网格HSDP实现极限算力压榨——在1T模型上优化器仅需0."
  },
  {
    "id": "bvid:BV1X15y6nE8Z",
    "domain": "AI",
    "title": "cursor无限免费使用最新方法cursor无限续杯cursor使用教程免费",
    "url": "http://www.bilibili.com/video/av116567140540269",
    "source": "开团秒跟cursor",
    "platform": "bilibili",
    "points": 5169,
    "published_at": "2026-05-13T11:59:02+00:00",
    "summary": "最新2026年5月13号 免费Cursor无限续杯保姆级使用教程集成MCP，实现opus4.6/4.7无限使用额度自由，相关工具请到 1030496866 文件夹中自行获取,完全免费，完全免费，离线插件版本,安装即可用，无任何数据收集行为"
  },
  {
    "id": "bvid:BV1caVh6fE6Z",
    "domain": "AI",
    "title": "【2026最新版】绝对是B站讲的最细的Claude Code教程，从国内环境安装出发，项目开发及个人使用总结带你玩转 Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116656764358481",
    "source": "AI大模型_",
    "platform": "bilibili",
    "points": 3709,
    "published_at": "2026-05-29T07:53:39+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV1NHZFBHECg",
    "domain": "AI",
    "title": "Claude Code高阶使用技巧",
    "url": "http://www.bilibili.com/video/av116470856096641",
    "source": "AI视频总结",
    "platform": "bilibili",
    "points": 3741,
    "published_at": "2026-04-26T13:55:57+00:00",
    "summary": "本视频深度解析Claude Code的高阶使用技巧，涵盖指令优化、工作流自动化及多任务并行策略。通过输入优化、终端增强及高级命令组合，助你从简单的指令下达者转变为高效的AI协作专家。"
  },
  {
    "id": "bvid:BV1FXLJ6YELZ",
    "domain": "AI",
    "title": "Cursor无限薅最强大模型claude4.7，gpt5.5使用方法",
    "url": "http://www.bilibili.com/video/av116590041369141",
    "source": "长青来了奥",
    "platform": "bilibili",
    "points": 3679,
    "published_at": "2026-05-17T13:01:58+00:00",
    "summary": "一键三连吧！在主页\n自动回复私信要1000粉丝呜呜呜呜求帮忙"
  },
  {
    "id": "bvid:BV1x6Vt6dEef",
    "domain": "AI",
    "title": "100 小时测试 Claude Code vs Codex（真实结果）",
    "url": "http://www.bilibili.com/video/av116656495925868",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 3424,
    "published_at": "2026-05-29T06:44:49+00:00",
    "summary": "【海外 AI 订阅】\n国内直连，支付宝付款，不用代理，\n一站订阅 ChatGPT / Codex / Claude Code / X\n订阅链接：https://bewild.ai?code=SJZD\n订阅时请填优惠邀请码：SJZD，具体优惠金额以官网为准。\n\n【视频介绍】\n我花了 100 个小时测试 Claude Code 和 Codex，结果真的让我非常意外。\n相同的提示词、相同的项目构建、两个"
  },
  {
    "id": "bvid:BV19DZ4BLE18",
    "domain": "AI",
    "title": "全网最简单解决cursor断网问题",
    "url": "http://www.bilibili.com/video/av116075249272918",
    "source": "门叁皮",
    "platform": "bilibili",
    "points": 3466,
    "published_at": "2026-02-15T15:04:18+00:00",
    "summary": "最简单的cursor断网解决方案"
  },
  {
    "id": "bvid:BV1CTRNBsECb",
    "domain": "AI",
    "title": "基于Claude Code的漏洞赏金自动化：从HackerOne报告到4万美元实战复盘",
    "url": "http://www.bilibili.com/video/av116513218495043",
    "source": "王尼互",
    "platform": "bilibili",
    "points": 3446,
    "published_at": "2026-05-03T23:25:06+00:00",
    "summary": "https://www.youtube.com/watch?v=pRPT_yrgRL0\n本视频系统拆解基于Claude Code构建漏洞赏金自动化流程的核心方法，包括如何利用公开漏洞报告（如HackerOne）生成专属AI技能、设计项目级代理文件（Agent/Memory）以及构建漏洞技能包，实现从资产发现到漏洞挖掘的全链路自动化。\n内容涵盖：\n基于历史漏洞报告定制检测规则与优先级策略（如XSS、"
  },
  {
    "id": "bvid:BV1rbRmBgEto",
    "domain": "AI",
    "title": "手把手教你 Vibe Coding：Codex 几个实用功能，特别适合不懂开发的新人",
    "url": "http://www.bilibili.com/video/av116539827160862",
    "source": "唐师兄Terence",
    "platform": "bilibili",
    "points": 2994,
    "published_at": "2026-05-09T01:00:00+00:00",
    "summary": "codex 下载地址：https://chatgpt.com/codex/"
  },
  {
    "id": "bvid:BV1QbVE6GE9a",
    "domain": "AI",
    "title": "新手也能用Vibe Coding给Hermes搭建可视化办公室~ 动手coding自己做工具~",
    "url": "http://www.bilibili.com/video/av116667099122260",
    "source": "在下李君陌",
    "platform": "bilibili",
    "points": 2668,
    "published_at": "2026-05-31T04:02:32+00:00",
    "summary": "视频中的大模型分别来自\n1.Kimi K2.6&amp; GLM5.1 — 优云智算\nhttps://passport.compshare.cn/register?referral_code=DzKOV5Iik6lG9svK0phShR&amp;ytag=GPU_YY_YX_bl_ljm0531\n2.DeepSeek-V4\nhttps://platform.deepseek.com/"
  },
  {
    "id": "bvid:BV1JUGb6jEny",
    "domain": "AI",
    "title": "90% 的人都没用对 Claude Code，Claude Code 的高阶玩法都在这",
    "url": "http://www.bilibili.com/video/av116618998912532",
    "source": "程序员Shark",
    "platform": "bilibili",
    "points": 2212,
    "published_at": "2026-05-22T15:46:55+00:00",
    "summary": "为了做了精心的翻译和校对，原文：https://www.youtube.com/watch?v=uogzSxOw4LU，再次感谢作者。\n概要：这部分内容真正想讲的，不是 Claude Code 又多了几个新功能，而是怎么把它用成一套顺手的开发工具。很多人一开始只是拿它来聊天，但真想把效率拉起来，重点其实在\n setup、命令、扩展能力和工作流设计。前面先讲了几个特别常用的 command：mode"
  },
  {
    "id": "hn:48198551",
    "domain": "金融",
    "title": "Tesla's lithium refinery discharges 231,000 gallons of polluted wastewater a day",
    "url": "https://www.autonocion.com/us/tesla-lithium-refinery-texas/",
    "source": "atombender",
    "platform": "hackernews",
    "points": 498,
    "published_at": "2026-05-19T19:52:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48165980",
    "domain": "金融",
    "title": "Tesla Solar Roof is on life support as it pivot to panels",
    "url": "https://electrek.co/2026/05/14/tesla-solar-roof-promise-vs-reality-pivot-panels/",
    "source": "celsoazevedo",
    "platform": "hackernews",
    "points": 328,
    "published_at": "2026-05-17T04:09:52+00:00",
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
    "id": "hn:48309986",
    "domain": "金融",
    "title": "Show HN: Ktx – Open-source executable context layer for data agents",
    "url": "https://github.com/Kaelio/ktx",
    "source": "lucamrtl",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-05-28T15:05:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48236770",
    "domain": "金融",
    "title": "Launch HN: Superset (YC P26) – IDE for the agents era",
    "url": "https://github.com/superset-sh/superset",
    "source": "avipeltz",
    "platform": "hackernews",
    "points": 107,
    "published_at": "2026-05-22T14:53:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://stratechery.com/2026/luceing-their-mind/",
    "domain": "金融",
    "title": "2026.22: Luceing Their Mind",
    "url": "https://stratechery.com/2026/luceing-their-mind/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of May 25, 2026, including why everyone hates Luce, how to monetize AI answers, and social mobility in China."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/",
    "domain": "金融",
    "title": "An Interview with Eric Seufert About Models and Ads, and AI’s Upside for Humanity",
    "url": "https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T10:00:00+00:00",
    "summary": "An Interview with Eric Seufert about building models for generative AI, why Meta's foundational models are so important, and why understanding advertising leads to optimism about humanity's future."
  },
  {
    "id": "hn:48160991",
    "domain": "金融",
    "title": "Tesla reveals two Robotaxi crashes involving teleoperators",
    "url": "https://techcrunch.com/2026/05/15/tesla-reveals-two-robotaxi-crashes-involving-teleoperators/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-05-16T15:21:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://stratechery.com/2026/the-spacex-ipo-and-data-centers-in-space/",
    "domain": "金融",
    "title": "The SpaceX IPO and Data Centers in Space",
    "url": "https://stratechery.com/2026/the-spacex-ipo-and-data-centers-in-space/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T10:00:00+00:00",
    "summary": "There isn't a financial model that justifies the SpaceX IPO, but data centers in space are plausible, and that might be enough."
  },
  {
    "id": "rss:https://stratechery.com/2026/nvidia-earnings-the-ai-stack-nvidias-new-reporting/",
    "domain": "金融",
    "title": "Nvidia Earnings, The AI Stack, Nvidia’s New Reporting",
    "url": "https://stratechery.com/2026/nvidia-earnings-the-ai-stack-nvidias-new-reporting/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-26T10:00:00+00:00",
    "summary": "Nvidia is changing its reporting to delineate between hyperscaler sales — where Nvidia is fighting commoditization — and everyone else, where Nvidia runs the whole stack."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-data-center-veto/",
    "domain": "金融",
    "title": "2026.21: The Data Center Veto",
    "url": "https://stratechery.com/2026/the-data-center-veto/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-22T17:12:32+00:00",
    "summary": "The best Stratechery content from the week of May 18, 2026, including data center discontent, agent economics, and slime mold."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-parallel-founder-parag-agarwal-about-valuing-content-on-the-agentic-web/",
    "domain": "金融",
    "title": "An Interview with Parallel Founder Parag Agarwal About Valuing Content on the Agentic Web",
    "url": "https://stratechery.com/2026/an-interview-with-parallel-founder-parag-agarwal-about-valuing-content-on-the-agentic-web/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T10:00:00+00:00",
    "summary": "An interview with Parallel founder Parag Agarwal about valuing content and incentivizing its creation in a world of agents (plus questions about Twitter)."
  },
  {
    "id": "rss:https://stratechery.com/2026/google-i-o-world-models-i-o-spaghetti/",
    "domain": "金融",
    "title": "Google I/O, World Models, I/O Spaghetti",
    "url": "https://stratechery.com/2026/google-i-o-world-models-i-o-spaghetti/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-20T10:00:00+00:00",
    "summary": "Google I/O put AI everywhere, for better and for worse. Meanwhile, is DeepMind aligned with Google's business objectives?"
  },
  {
    "id": "rss:https://stratechery.com/2026/data-center-discontent-understanding-the-opposition-fixing-the-problem/",
    "domain": "金融",
    "title": "Data Center Discontent, Understanding the Opposition, Fixing the Problem",
    "url": "https://stratechery.com/2026/data-center-discontent-understanding-the-opposition-fixing-the-problem/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-18T10:00:00+00:00",
    "summary": "There are understandable reasons for people to oppose data centers; the only solution that will work is simply paying them off."
  },
  {
    "id": "rss:https://stratechery.com/2026/shifting-alliances-in-a-changing-world/",
    "domain": "金融",
    "title": "2026.20: Shifting Alliances in a Changing World",
    "url": "https://stratechery.com/2026/shifting-alliances-in-a-changing-world/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-15T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of May 11, 2026, including a new kind of computing, Elon Musk, and 360 degrees of US-China relations."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-ben-thompson-at-the-moffettnathanson-media-internet-communications-conference/",
    "domain": "金融",
    "title": "An Interview with Ben Thompson at the MoffettNathanson Media, Internet & Communications Conference",
    "url": "https://stratechery.com/2026/an-interview-with-ben-thompson-at-the-moffettnathanson-media-internet-communications-conference/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-14T10:00:00+00:00",
    "summary": "An interview with me about the implications of the compute shortage on Aggregation Theory, consumer AI, and more."
  },
  {
    "id": "hn:48311647",
    "domain": "半导体",
    "title": "Claude Opus 4.8",
    "url": "https://www.anthropic.com/news/claude-opus-4-8",
    "source": "craigmart",
    "platform": "hackernews",
    "points": 1734,
    "published_at": "2026-05-28T16:49:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206768",
    "domain": "半导体",
    "title": "Meta blocks human rights accounts from reaching audiences in Saudi Arabia, UAE",
    "url": "https://www.alqst.org/ar/posts/1190",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 1079,
    "published_at": "2026-05-20T12:43:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:47920074",
    "domain": "半导体",
    "title": "Men who stare at walls",
    "url": "https://www.alexselimov.com/posts/men_who_stare_at_walls/",
    "source": "aselimov3",
    "platform": "hackernews",
    "points": 724,
    "published_at": "2026-04-27T11:08:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48143880",
    "domain": "半导体",
    "title": "Mullvad exit IPs are surprisingly identifying",
    "url": "https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/",
    "source": "RGBCube",
    "platform": "hackernews",
    "points": 613,
    "published_at": "2026-05-15T02:35:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48184402",
    "domain": "半导体",
    "title": "Was my $48K GPU server worth it?",
    "url": "https://rosmine.ai/2026/05/13/was-my-48k-gpu-worth-it/",
    "source": "apwheele",
    "platform": "hackernews",
    "points": 568,
    "published_at": "2026-05-18T19:33:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:48164287",
    "domain": "半导体",
    "title": "Zerostack – A Unix-inspired coding agent written in pure Rust",
    "url": "https://crates.io/crates/zerostack/1.0.0",
    "source": "gidellav",
    "platform": "hackernews",
    "points": 575,
    "published_at": "2026-05-16T22:23:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48191602",
    "domain": "半导体",
    "title": "Show HN: Gaussian Splat of a Strawberry",
    "url": "https://superspl.at/scene/84df8849",
    "source": "danybittel",
    "platform": "hackernews",
    "points": 529,
    "published_at": "2026-05-19T10:38:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48259808",
    "domain": "半导体",
    "title": "Migrating from Go to Rust",
    "url": "https://corrode.dev/learn/migration-guides/go-to-rust/",
    "source": "jabits",
    "platform": "hackernews",
    "points": 477,
    "published_at": "2026-05-24T18:31:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48169874",
    "domain": "半导体",
    "title": "Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep",
    "url": "https://github.com/MinishLab/semble",
    "source": "Bibabomas",
    "platform": "hackernews",
    "points": 445,
    "published_at": "2026-05-17T15:37:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48299220",
    "domain": "半导体",
    "title": "What Apple and Google are doing to push notifications",
    "url": "https://www.jacquescorbytuech.com/writing/what-apple-and-google-are-doing-your-push-notifications",
    "source": "iamacyborg",
    "platform": "hackernews",
    "points": 416,
    "published_at": "2026-05-27T19:24:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:47776035",
    "domain": "半导体",
    "title": "Anna's Archive loses $322M Spotify piracy case without a fight",
    "url": "https://torrentfreak.com/annas-archive-loses-322-million-spotify-piracy-case-without-a-fight/",
    "source": "askl",
    "platform": "hackernews",
    "points": 444,
    "published_at": "2026-04-15T08:05:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48238025",
    "domain": "半导体",
    "title": "U.S. researchers face new restrictions on publishing with foreign collaborators",
    "url": "https://www.science.org/content/article/u-s-researchers-face-new-restrictions-publishing-foreign-collaborators",
    "source": "ceejayoz",
    "platform": "hackernews",
    "points": 419,
    "published_at": "2026-05-22T16:23:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:47827259",
    "domain": "半导体",
    "title": "Stop trying to engineer your way out of listening to people",
    "url": "https://ashley.rolfmore.com/stop-trying-to-engineer-your-way-out-of-listening-to-people/",
    "source": "walterbell",
    "platform": "hackernews",
    "points": 438,
    "published_at": "2026-04-19T20:09:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206340",
    "domain": "半导体",
    "title": "Saying goodbye to asm.js",
    "url": "https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html",
    "source": "eqrion",
    "platform": "hackernews",
    "points": 410,
    "published_at": "2026-05-20T12:01:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:47901064",
    "domain": "半导体",
    "title": "ASML became the chokepoint for cutting-edge chips",
    "url": "https://worksinprogress.co/issue/the-worlds-most-complex-machine/",
    "source": "mellosouls",
    "platform": "hackernews",
    "points": 416,
    "published_at": "2026-04-25T12:47:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:48307231",
    "domain": "半导体",
    "title": "AMD pulls a bait-and-switch on Linux users with Vivado licensing changes",
    "url": "https://itsfoss.com/news/amd-vivado-bait-and-switch-on-linux-users/",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 336,
    "published_at": "2026-05-28T10:56:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48293080",
    "domain": "半导体",
    "title": "Incident with Pull Requests, Issues, Git Operations and API Requests",
    "url": "https://www.githubstatus.com/incidents/xy1tt3hs572m",
    "source": "maxnoe",
    "platform": "hackernews",
    "points": 335,
    "published_at": "2026-05-27T12:15:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48165797",
    "domain": "半导体",
    "title": "I found ultra-pure quantum crystals in an abandoned mine in the Atacama desert",
    "url": "https://medium.com/@breid.at/ultra-pure-quantum-crystals-from-an-abandoned-mine-in-a-mysterious-desert-93cc87d12314",
    "source": "vi_sextus_vi",
    "platform": "hackernews",
    "points": 287,
    "published_at": "2026-05-17T03:25:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48231247",
    "domain": "半导体",
    "title": "Gnutella: A Protocol Outliving the World That Created It",
    "url": "https://rickcarlino.com/notes/p2p/gnutella-explanation.html",
    "source": "rickcarlino",
    "platform": "hackernews",
    "points": 272,
    "published_at": "2026-05-22T02:24:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48221896",
    "domain": "半导体",
    "title": "Show HN: I Dedicated 4 Years to Mastering Offline Password Cracking",
    "url": "https://news.ycombinator.com/item?id=48221896",
    "source": "bojta-lepenye",
    "platform": "hackernews",
    "points": 268,
    "published_at": "2026-05-21T12:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48321076",
    "domain": "半导体",
    "title": "Real-time LLM Inference on Standard GPUs: 3k tokens/s per request",
    "url": "https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/",
    "source": "NicoConstant",
    "platform": "hackernews",
    "points": 204,
    "published_at": "2026-05-29T09:47:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48270111",
    "domain": "半导体",
    "title": "The bootstrapper's EU stack for under €10 per month",
    "url": "https://eualternative.eu/guides/bootstrapper-free-tier-eu-stack/",
    "source": "sparkling",
    "platform": "hackernews",
    "points": 225,
    "published_at": "2026-05-25T18:37:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48266422",
    "domain": "半导体",
    "title": "Microsoft pulls plug on plans for 244-acre data center in Caledonia (2025)",
    "url": "https://www.tmj4.com/news/racine-county/microsoft-pulls-plug-on-plans-for-244-acre-data-center-in-caledonia-after-community-pushback",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-05-25T13:09:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48226038",
    "domain": "半导体",
    "title": "Chewing gum restores dad's taste and smell years after Covid",
    "url": "https://discover.swns.com/2026/05/chewing-gum-restores-dads-taste-and-smell-years-after-covid/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-05-21T17:14:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:47595971",
    "domain": "半导体",
    "title": "My son pleasured himself on Gemini Live. Entire family's Google accounts banned",
    "url": "https://old.reddit.com/r/LegalAdviceUK/comments/1s92fql/my_son_pleasured_himself_in_front_of_gemini_live/",
    "source": "samlinnfer",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-04-01T02:14:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210590",
    "domain": "半导体",
    "title": "Ask HN: Shouldn't Google need to give a public statement about Railway incident?",
    "url": "https://news.ycombinator.com/item?id=48210590",
    "source": "srameshc",
    "platform": "hackernews",
    "points": 180,
    "published_at": "2026-05-20T16:50:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48265056",
    "domain": "半导体",
    "title": "IBM Spins Off the First Pure-Play Quantum Chip Foundry",
    "url": "https://futurumgroup.com/insights/2-billion-chips-act-investment-in-quantum-bets-on-ibms-300mm-superconducting-silicon/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 158,
    "published_at": "2026-05-25T09:43:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:47896163",
    "domain": "半导体",
    "title": "Show HN: I've built a nice home server OS",
    "url": "https://lightwhale.asklandd.dk/",
    "source": "Zta77",
    "platform": "hackernews",
    "points": 194,
    "published_at": "2026-04-24T21:42:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48247005",
    "domain": "半导体",
    "title": "Matrix Multiplications on GPUs Run Faster When Given “Predictable” Data (2024)",
    "url": "https://www.thonking.ai/p/strangely-matrix-multiplications",
    "source": "tosh",
    "platform": "hackernews",
    "points": 172,
    "published_at": "2026-05-23T12:11:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48250980",
    "domain": "半导体",
    "title": "Air France and Airbus found guilty of manslaughter over 2009 plane crash",
    "url": "https://www.bbc.com/news/articles/czd2qmdvmq6o",
    "source": "baal80spam",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-05-23T20:09:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48189539",
    "domain": "半导体",
    "title": "Fender escalates legal campaign against S-style guitars",
    "url": "https://www.guitarworld.com/gear/electric-guitars/fender-cease-and-desist-lsl-instruments",
    "source": "rectang",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-05-19T05:28:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48256108",
    "domain": "半导体",
    "title": "What it takes to transpose a matrix",
    "url": "https://gudok.xyz/transpose/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-05-24T10:30:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48272393",
    "domain": "半导体",
    "title": "Show HN: OpenBrief – Local-first video downloader/summarizer",
    "url": "https://github.com/tantara/openbrief",
    "source": "tantara",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-05-25T21:50:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:48012477",
    "domain": "半导体",
    "title": "Offenders sentenced up to 10 years for spying on TSMC",
    "url": "https://www.taipeitimes.com/News/front/archives/2026/04/28/2003856358",
    "source": "ironyman",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-05-04T18:04:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48265745",
    "domain": "半导体",
    "title": "GPT Guesses Between 1 and 100",
    "url": "https://github.com/exmergo/research-chatgpt-guesses-between-1-and-100",
    "source": "adunk",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-05-25T11:46:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48234574",
    "domain": "半导体",
    "title": "How do you build a semiconductor company on something that's free?",
    "url": "https://www.siliconimist.com/p/the-open-source-silicon-business",
    "source": "johncole",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-22T11:49:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48209105",
    "domain": "半导体",
    "title": "Stable Audio 3",
    "url": "https://arxiv.org/abs/2605.17991",
    "source": "guardienaveugle",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-20T15:10:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48183038",
    "domain": "半导体",
    "title": "Cutting inference cold starts by 40x with LP, FUSE, C/R, and CUDA-checkpoint",
    "url": "https://modal.com/blog/truly-serverless-gpus",
    "source": "charles_irl",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-05-18T17:56:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48327222",
    "domain": "半导体",
    "title": "AI will be used to estimate age of asylum seekers from next year",
    "url": "https://www.bbc.co.uk/news/articles/ce3pe36qe7ro",
    "source": "vylorn",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-05-29T18:23:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:48220446",
    "domain": "半导体",
    "title": "IBM invented semiconductor manufacturing automation",
    "url": "https://spectrum.ieee.org/semiconductor-fabrication",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-05-21T10:39:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48007145",
    "domain": "半导体",
    "title": "ASML's Best Selling Product Isn't What You Think It Is",
    "url": "https://www.siliconimist.com/p/asmls-best-selling-product",
    "source": "johncole",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-05-04T11:08:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48291230",
    "domain": "半导体",
    "title": "Nvidia Vera CPU Benchmarks: Olympus Cores Delivering Great Performance",
    "url": "https://www.phoronix.com/review/nvidia-vera-benchmarks",
    "source": "naves",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-05-27T08:15:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48041316",
    "domain": "半导体",
    "title": "Show HN: PHP-fts – Full-text search engine in pure PHP, no extensions",
    "url": "https://github.com/olivier-ls/php-fts",
    "source": "asmodios",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-05-06T20:28:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48261543",
    "domain": "半导体",
    "title": "San Francisco immigration court shuts down after purge of judges",
    "url": "https://apnews.com/article/san-francisco-immigration-court-closed-asylum-8a0946a7cd4bcc9bd925d075cabef44a",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-05-24T22:12:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:47807609",
    "domain": "半导体",
    "title": "Writing string.h functions using string instructions in asm x86-64 (2025)",
    "url": "https://pmasschelier.github.io/x86_64_strings/",
    "source": "thaisstein",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-04-17T16:22:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48037923",
    "domain": "半导体",
    "title": "Canadian fiddler sues Google after AI Overview claimed he was a sex offender",
    "url": "https://www.theguardian.com/music/2026/may/05/canadian-ashley-macisaac-fiddler-musician-singer-songwriter-sues-google-ai-sex-offender-ntwnfb",
    "source": "LordAtlas",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-05-06T16:12:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48019219",
    "domain": "大厂讯息",
    "title": "Google Chrome silently installs a 4 GB AI model on your device without consent",
    "url": "https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/",
    "source": "john-doe",
    "platform": "hackernews",
    "points": 1755,
    "published_at": "2026-05-05T07:34:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48067119",
    "domain": "大厂讯息",
    "title": "Google broke reCAPTCHA for de-googled Android users",
    "url": "https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users",
    "source": "anonymousiam",
    "platform": "hackernews",
    "points": 1561,
    "published_at": "2026-05-08T18:45:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:47989883",
    "domain": "大厂讯息",
    "title": "VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage",
    "url": "https://github.com/microsoft/vscode/pull/310226",
    "source": "indrora",
    "platform": "hackernews",
    "points": 1513,
    "published_at": "2026-05-02T19:57:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48296649",
    "domain": "大厂讯息",
    "title": "DuckDuckGo search saw 28% more visits after Google said people love AI mode",
    "url": "https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/",
    "source": "HelloUsername",
    "platform": "hackernews",
    "points": 1071,
    "published_at": "2026-05-27T16:28:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48341578",
    "domain": "大厂讯息",
    "title": "Microsoft Office 2019 and 2021 for Mac view-only conversion",
    "url": "https://consumerrights.wiki/w/Microsoft_Office_2019_and_2021_for_Mac_view-only_conversion_(2026)",
    "source": "antipurist",
    "platform": "hackernews",
    "points": 983,
    "published_at": "2026-05-30T23:26:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48111545",
    "domain": "大厂讯息",
    "title": "Googlebook",
    "url": "https://googlebook.google/",
    "source": "tambourine_man",
    "platform": "hackernews",
    "points": 932,
    "published_at": "2026-05-12T17:37:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48222529",
    "domain": "大厂讯息",
    "title": "Google's Antigravity bait and switch",
    "url": "https://www.0xsid.com/blog/antigravity-bait-n-switch",
    "source": "ssiddharth",
    "platform": "hackernews",
    "points": 770,
    "published_at": "2026-05-21T13:50:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48192224",
    "domain": "大厂讯息",
    "title": "Apple unveils new accessibility features",
    "url": "https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/",
    "source": "interpol_p",
    "platform": "hackernews",
    "points": 726,
    "published_at": "2026-05-19T12:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48197370",
    "domain": "大厂讯息",
    "title": "Google changes its search box",
    "url": "https://blog.google/products-and-platforms/products/search/search-io-2026/",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 701,
    "published_at": "2026-05-19T18:34:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:48063199",
    "domain": "大厂讯息",
    "title": "Google Cloud Fraud Defence is just WEI repackaged",
    "url": "https://privatecaptcha.com/blog/google-cloud-fraud-defence-wei/",
    "source": "ribtoks",
    "platform": "hackernews",
    "points": 707,
    "published_at": "2026-05-08T13:56:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48214449",
    "domain": "大厂讯息",
    "title": "Google Declaring War on the Web",
    "url": "https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 637,
    "published_at": "2026-05-20T21:33:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48012735",
    "domain": "大厂讯息",
    "title": "Microsoft Edge stores all passwords in memory in clear text, even when unused",
    "url": "https://twitter.com/L1v1ng0ffTh3L4N/status/2051308329880719730",
    "source": "cft",
    "platform": "hackernews",
    "points": 644,
    "published_at": "2026-05-04T18:22:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48050964",
    "domain": "大厂讯息",
    "title": "Chrome removes claim of On-device Al not sending data to Google Servers",
    "url": "https://old.reddit.com/r/chrome/comments/1t5qayz/chrome_removes_claim_of_ondevice_al_not_sending/",
    "source": "newsoftheday",
    "platform": "hackernews",
    "points": 639,
    "published_at": "2026-05-07T15:56:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48315968",
    "domain": "大厂讯息",
    "title": "GitHub bans security researcher who posted zero-day Windows exploits",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/microsofts-github-bans-security-researcher-who-posted-zero-day-windows-exploits-because-company-ruined-their-life-expert-claims-action-is-vindictive-and-promises-further-retaliation",
    "source": "possibilistic",
    "platform": "hackernews",
    "points": 560,
    "published_at": "2026-05-28T21:45:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48168856",
    "domain": "大厂讯息",
    "title": "Security researcher says Microsoft built a Bitlocker backdoor, releases exploit",
    "url": "https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html",
    "source": "nolok",
    "platform": "hackernews",
    "points": 594,
    "published_at": "2026-05-17T13:42:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48266051",
    "domain": "大厂讯息",
    "title": "Search engines alternatives now that Google isn't Google anymore",
    "url": "https://techcrunch.com/2026/05/21/six-search-engines-worth-trying-now-that-google-isnt-really-google-anymore/",
    "source": "elorant",
    "platform": "hackernews",
    "points": 571,
    "published_at": "2026-05-25T12:27:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48201484",
    "domain": "大厂讯息",
    "title": "Incident Report: Railway Blocked by Google Cloud [resolved]",
    "url": "https://status.railway.com/incident/I23M92U0",
    "source": "aarondf",
    "platform": "hackernews",
    "points": 560,
    "published_at": "2026-05-20T00:23:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48253386",
    "domain": "大厂讯息",
    "title": "Microsoft open-sources “the earliest DOS source code discovered to date”",
    "url": "https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/",
    "source": "DamnInteresting",
    "platform": "hackernews",
    "points": 516,
    "published_at": "2026-05-24T01:21:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210263",
    "domain": "大厂讯息",
    "title": "Apparently Google hates us now",
    "url": "https://twitter.com/pokemoncentral/status/2057123807404638250",
    "source": "zeitg3ist",
    "platform": "hackernews",
    "points": 508,
    "published_at": "2026-05-20T16:27:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48151383",
    "domain": "大厂讯息",
    "title": "U.S. DOJ demands Apple and Google unmask over 100k users of car-tinkering app",
    "url": "https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/",
    "source": "tencentshill",
    "platform": "hackernews",
    "points": 477,
    "published_at": "2026-05-15T17:28:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:48073979",
    "domain": "大厂讯息",
    "title": "A History of IDEs at Google",
    "url": "https://laurent.le-brun.eu/blog/a-history-of-ides-at-google",
    "source": "laurentlb",
    "platform": "hackernews",
    "points": 473,
    "published_at": "2026-05-09T11:14:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48139219",
    "domain": "大厂讯息",
    "title": "First public macOS kernel memory corruption exploit on Apple M5",
    "url": "https://blog.calif.io/p/first-public-kernel-memory-corruption",
    "source": "quadrige",
    "platform": "hackernews",
    "points": 464,
    "published_at": "2026-05-14T18:25:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48215979",
    "domain": "大厂讯息",
    "title": "Show HN: I reverse engineered Apple's video wallpapers",
    "url": "https://github.com/kageroumado/phosphene",
    "source": "kageroumado",
    "platform": "hackernews",
    "points": 427,
    "published_at": "2026-05-20T23:54:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48021561",
    "domain": "大厂讯息",
    "title": "iOS 27 is adding a 'Create a Pass' button to Apple Wallet",
    "url": "https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/",
    "source": "alentodorov",
    "platform": "hackernews",
    "points": 435,
    "published_at": "2026-05-05T12:28:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48039362",
    "domain": "大厂讯息",
    "title": "Google Cloud fraud defense, the next evolution of reCAPTCHA",
    "url": "https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-fraud-defense-the-next-evolution-of-recaptcha/",
    "source": "unforgivenpasta",
    "platform": "hackernews",
    "points": 415,
    "published_at": "2026-05-06T17:59:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48025687",
    "domain": "大厂讯息",
    "title": "IBM didn't want Microsoft to use the Tab key to move between dialog fields",
    "url": "https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298",
    "source": "SeenNotHeard",
    "platform": "hackernews",
    "points": 397,
    "published_at": "2026-05-05T17:28:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48168198",
    "domain": "大厂讯息",
    "title": "Apple Silicon costs more than OpenRouter",
    "url": "https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html",
    "source": "datadrivenangel",
    "platform": "hackernews",
    "points": 355,
    "published_at": "2026-05-17T12:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48205782",
    "domain": "大厂讯息",
    "title": "Google’s AI is being manipulated. The search giant is quietly fighting back",
    "url": "https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results",
    "source": "tigerlily",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-05-20T10:57:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48302822",
    "domain": "大厂讯息",
    "title": "Google employee charged with $1M Polymarket insider trading bet on search term",
    "url": "https://www.cnbc.com/2026/05/27/google-employee-polymarket-insider-trading.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 319,
    "published_at": "2026-05-28T00:49:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48075144",
    "domain": "大厂讯息",
    "title": "GrapheneOS fixes Android VPN leak Google refused to patch",
    "url": "https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/",
    "source": "Georgelemental",
    "platform": "hackernews",
    "points": 355,
    "published_at": "2026-05-09T14:11:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48198291",
    "domain": "大厂讯息",
    "title": "OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool",
    "url": "https://openai.com/index/advancing-content-provenance/",
    "source": "smooke",
    "platform": "hackernews",
    "points": 332,
    "published_at": "2026-05-19T19:34:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48328175",
    "domain": "大厂讯息",
    "title": "Microsoft 0-day feud escalates as researcher threatens another exploit dump",
    "url": "https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 274,
    "published_at": "2026-05-29T19:37:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48253186",
    "domain": "大厂讯息",
    "title": "Scammers are abusing an internal Microsoft account to send spam links",
    "url": "https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/",
    "source": "spike021",
    "platform": "hackernews",
    "points": 304,
    "published_at": "2026-05-24T00:51:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:48238703",
    "domain": "大厂讯息",
    "title": "I built a Git-tracked book production pipeline",
    "url": "https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/",
    "source": "dustin1114",
    "platform": "hackernews",
    "points": 285,
    "published_at": "2026-05-22T17:17:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:48272354",
    "domain": "大厂讯息",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files",
    "source": "Kneenex",
    "platform": "hackernews",
    "points": 264,
    "published_at": "2026-05-25T21:45:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48043964",
    "domain": "大厂讯息",
    "title": "RSS feeds send me more traffic than Google",
    "url": "https://shkspr.mobi/blog/2026/05/rss-feeds-send-me-more-traffic-than-google/",
    "source": "SpyCoder77",
    "platform": "hackernews",
    "points": 297,
    "published_at": "2026-05-07T00:40:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48130519",
    "domain": "大厂讯息",
    "title": "Microsoft BitLocker – YellowKey zero-day exploit",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/microsoft-bitlocker-protected-drives-can-now-be-opened-with-just-some-files-on-a-usb-stick-yellowkey-zero-day-exploit-demonstrates-an-apparent-backdoor",
    "source": "cookiengineer",
    "platform": "hackernews",
    "points": 292,
    "published_at": "2026-05-14T02:45:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48158130",
    "domain": "大厂讯息",
    "title": "Where to buy a non-Apple, non-Google smartphone",
    "url": "https://www.theregister.com/on-prem/2026/05/01/where-to-buy-a-non-apple-non-google-smartphone/5219681",
    "source": "_____k",
    "platform": "hackernews",
    "points": 286,
    "published_at": "2026-05-16T08:34:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48094641",
    "domain": "大厂讯息",
    "title": "Google says criminal hackers used AI to find a major software flaw",
    "url": "https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html",
    "source": "donohoe",
    "platform": "hackernews",
    "points": 244,
    "published_at": "2026-05-11T13:20:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48238351",
    "domain": "大厂讯息",
    "title": "You can no longer Google the word 'disregard'",
    "url": "https://techcrunch.com/2026/05/22/you-can-no-longer-google-the-word-disregard/",
    "source": "coloneltcb",
    "platform": "hackernews",
    "points": 222,
    "published_at": "2026-05-22T16:47:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48066169",
    "domain": "大厂讯息",
    "title": "Apple, Intel have reached preliminary chip-making deal",
    "url": "https://www.reuters.com/business/apple-intel-have-reached-preliminary-chip-making-deal-wsj-reports-2026-05-08/",
    "source": "scrlk",
    "platform": "hackernews",
    "points": 229,
    "published_at": "2026-05-08T17:25:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48230049",
    "domain": "大厂讯息",
    "title": "The IBM-ification of Google?",
    "url": "https://zeroshot.bearblog.dev/google-is-shattering-under-its-own-weight-the-ibm-ification-of-google/",
    "source": "sabatonfan",
    "platform": "hackernews",
    "points": 206,
    "published_at": "2026-05-21T23:30:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:47984522",
    "domain": "大厂讯息",
    "title": "Why are there both TMP and TEMP environment variables? (2015)",
    "url": "https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213",
    "source": "ankitg12",
    "platform": "hackernews",
    "points": 216,
    "published_at": "2026-05-02T08:23:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48273169",
    "domain": "大厂讯息",
    "title": "CVE-2026-28952: Apple macOS 26.5 Kernel Vuln found by Claude",
    "url": "https://support.apple.com/en-us/127115",
    "source": "dragonsenseiguy",
    "platform": "hackernews",
    "points": 172,
    "published_at": "2026-05-25T23:40:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196020",
    "domain": "大厂讯息",
    "title": "Google I/O",
    "url": "https://io.google/2026/",
    "source": "thanhhaimai",
    "platform": "hackernews",
    "points": 186,
    "published_at": "2026-05-19T17:01:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48349487",
    "domain": "大厂讯息",
    "title": "ChatGPT for Google Sheets is vulnerable to data exfiltration and phishing",
    "url": "https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration",
    "source": "hackerBanana",
    "platform": "hackernews",
    "points": 106,
    "published_at": "2026-05-31T20:35:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48097796",
    "domain": "大厂讯息",
    "title": "Microsoft Israel chief leaves amid ethical controversy",
    "url": "https://en.globes.co.il/en/article-microsoft-israel-chief-leaves-amid-ethical-controversy-1001542602",
    "source": "bhouston",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-05-11T17:18:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48275508",
    "domain": "大厂讯息",
    "title": "Ask HN: Is anyone working at least 4 hours daily on an Apple Vision Pro?",
    "url": "https://news.ycombinator.com/item?id=48275508",
    "source": "widenrun",
    "platform": "hackernews",
    "points": 153,
    "published_at": "2026-05-26T05:49:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48225782",
    "domain": "大厂讯息",
    "title": "Improving C# Memory Safety",
    "url": "https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/",
    "source": "soheilpro",
    "platform": "hackernews",
    "points": 165,
    "published_at": "2026-05-21T16:54:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:47995037",
    "domain": "大厂讯息",
    "title": "Show HN: Apple's SHARP running in the browser via ONNX runtime web",
    "url": "https://github.com/bring-shrubbery/ml-sharp-web",
    "source": "bring-shrubbery",
    "platform": "hackernews",
    "points": 185,
    "published_at": "2026-05-03T09:14:56+00:00",
    "summary": ""
  }
]
```
