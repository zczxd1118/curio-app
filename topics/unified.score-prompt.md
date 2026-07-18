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

- 今日日期：`2026-07-18`
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
  "date": "2026-07-18",
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
    "id": "bvid:BV1ec7M6xEay",
    "domain": "AI",
    "title": "当你是服务器管理员时和朋友玩MC...",
    "url": "http://www.bilibili.com/video/av116794220091990",
    "source": "安坤哒",
    "platform": "bilibili",
    "points": 4133166,
    "published_at": "2026-06-26T11:05:00+00:00",
    "summary": "正在拍下一期！\n免费的点赞和三连均可加快更新速度！\n熬夜五天制作,真的很累呜呜\n\n关注就可以长期观看MC女孩子系列啦！"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1536288,
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
    "points": 980903,
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
    "points": 907312,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 889516,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1aRq6BtE2M",
    "domain": "AI",
    "title": "NeuroSama是如何实现的？AI Vtuber的技术原理分析",
    "url": "http://www.bilibili.com/video/av115752489195045",
    "source": "赤川鹤鸣_Channel",
    "platform": "bilibili",
    "points": 638521,
    "published_at": "2025-12-21T02:00:00+00:00",
    "summary": "相信经常混 V 圈的小伙伴们一定听说过 Neuro-sama，她是一名完全由 AI 驱动的虚拟 Vtuber，在国内外都有很高的知名度。但是，你是否好奇，她究竟使用了哪些技术，我们能不能也手搓出一个 Neuro-sama 呢？\n本期视频，我们从 Neuro-sama 的主要功能出发，由浅入深地分析、探究并实现了由语音识别到大语言模型再到语音合成的主要功能链路，接着对 Live2D 的控制话题进行了"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 537538,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 484584,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 384136,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 378253,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1BFouBYERu",
    "domain": "AI",
    "title": "手把手教你在Claude Code中熟练使用SKILL技能！",
    "url": "http://www.bilibili.com/video/av116453927814340",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 374241,
    "published_at": "2026-04-23T12:09:57+00:00",
    "summary": "本期视频耗时半个月制作，希望大家能够点赞三连加关注，感谢！\n\n内容包括了一下几个方面：\n00:27 Skill简介\n01:39 Skill和Plugin的区别\n02:51 安装他人的Skill\n04:44 手动创建自己的SKill\n07:30 控制Skill的触发行为\n08:01 Skill的查看和管理\n08:20 Skill的停用和删除\n08:55 找优质Skill的三种渠道"
  },
  {
    "id": "bvid:BV1GX9dYWEPw",
    "domain": "AI",
    "title": "我居然能在MC里玩到这么好玩的摸金服务器！",
    "url": "http://www.bilibili.com/video/av114108926068217",
    "source": "物骨",
    "platform": "bilibili",
    "points": 317736,
    "published_at": "2025-03-06T21:00:00+00:00",
    "summary": "视频内容均来自《LRL服务器》\n服务器游玩方式看评论区置顶\n无需正版，不卖数值，爆率嘎嘎高，不会跑路"
  },
  {
    "id": "bvid:BV1Yd5XzdETJ",
    "domain": "AI",
    "title": "当你发现服务的反矿透有bug",
    "url": "http://www.bilibili.com/video/av114380498870146",
    "source": "Minecraft-空月之歌",
    "platform": "bilibili",
    "points": 285524,
    "published_at": "2025-04-22T07:48:34+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 280954,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1XgGi6sEQc",
    "domain": "AI",
    "title": "Claude Code + DeepSeek V4 Pro，大约花了两块钱的token😄ai使用越来越得心应手，token消耗也越来越高了 很享受用ai的过程",
    "url": "http://www.bilibili.com/video/av116623344142234",
    "source": "赵大海Zachary",
    "platform": "bilibili",
    "points": 268616,
    "published_at": "2026-05-23T10:15:11+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 249257,
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
    "points": 241789,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 191156,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 177331,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV17Ejt6QE9Y",
    "domain": "AI",
    "title": "一旦被Claude判定&quot;危险&quot;，你之后说的每句话都会被动手脚——实测曝光",
    "url": "http://www.bilibili.com/video/av116787609863495",
    "source": "YJFGL",
    "platform": "bilibili",
    "points": 177145,
    "published_at": "2026-06-21T10:26:28+00:00",
    "summary": "续上一条视频。这次我测出了更具体的触发机制：\n当对话中**某一条消息被系统分类器判定为&quot;潜在存在危害&quot;**之后，从那条消息开始，之后所有的 user 消息后面都会被持续注入一段隐藏文本。\n也就是说，这不是无差别的全程注入，而是一旦被系统标记，就会进入一种&quot;持续追加提醒&quot;的状态，并且这个状态会一直保持到对话结束，用户完全不知情、也无法解除。\n这意味着：\n你某一"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 161854,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 159918,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 157766,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 150549,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 138108,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 134959,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 130390,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV1EVuqzrEMJ",
    "domain": "AI",
    "title": "【保姆级教程】手把手教你低成本制作AI女友，【一定要看置顶评论】，可随身携带，自由对话",
    "url": "http://www.bilibili.com/video/av114851468812000",
    "source": "往生堂研发",
    "platform": "bilibili",
    "points": 108057,
    "published_at": "2025-07-14T12:03:53+00:00",
    "summary": "文档地址\nhttps://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md?_refluxos=a10#%E6%96%B9%E5%BC%8F%E4%B8%80docker%E5%8F%AA%E8%BF%90%E8%A1%8Cserver"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92596,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 90626,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1QFMG6gE4x",
    "domain": "AI",
    "title": "服主，服务器连不上了。 此时的物理服主",
    "url": "http://www.bilibili.com/video/av116885320438094",
    "source": "hutaoyi-S9",
    "platform": "bilibili",
    "points": 83875,
    "published_at": "2026-07-08T16:35:36+00:00",
    "summary": "不是哥们，啥几把豆腐渣工程，看的我是两眼一黑。\n玛碧的虚接加大功率用电，buff叠满了。\n真78服了"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73776,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 43146,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV111sBzYEvw",
    "domain": "AI",
    "title": "【AI开发板教程】手把手教你搭建属于自己的语音聊天机器人， 使用T5AI开发板，适合高中生/大学生的DIY教程！",
    "url": "http://www.bilibili.com/video/av115421894281245",
    "source": "大白爱模型",
    "platform": "bilibili",
    "points": 42303,
    "published_at": "2025-10-23T05:46:22+00:00",
    "summary": "🎮 你也能轻松搭建属于自己的AI聊天机器人！\n如果你对人工智能、语音识别和机器人开发感兴趣，那么这期视频你一定不能错过！👨‍💻\n本视频将带你从零开始，使用涂鸦智能T5开发板，教你一步步搭建一个基于Doubao的语音聊天机器人。我不仅会介绍硬件的配置，还会带你走完完整的配网、编程与功能实现流程！💡\n🔧 教程亮点：\nT5开发板硬件介绍：了解板卡的基本配置、如何连接传感器、摄像头等外围设备。\nDIY组装"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 40857,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 38474,
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
    "points": 34964,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV19sE461Eqk",
    "domain": "AI",
    "title": "可能是全SL最精致的GOC了",
    "url": "http://www.bilibili.com/video/av116707498727066",
    "source": "SL_耳机盒",
    "platform": "bilibili",
    "points": 34411,
    "published_at": "2026-06-07T06:55:06+00:00",
    "summary": "可能是全SL最精致的GOC了\n欢迎大家来「鸢神祈冬」服务器游玩"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29468,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 27635,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1jYRRBDExF",
    "domain": "AI",
    "title": "让AI直接操作godot开发游戏，免费开源MCP插件",
    "url": "http://www.bilibili.com/video/av116545648860073",
    "source": "Yurineko73",
    "platform": "bilibili",
    "points": 27220,
    "published_at": "2026-05-10T03:00:00+00:00",
    "summary": "因为想找一个好用的mcp工具，结果发现不是要收费就是不可商用，于是借助ai直接搓了一个出来。\n目前已经发布1.0.1版本，在godot asset library搜索 [godot mcp native]即可下载使用，\n也可以去GitHub上下载完整项目 https://github.com/yurineko73/Godot-MCP-Native\n免费开源，可以随意扩展和修改，如果有需要的功能或遇"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25364,
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
    "points": 22631,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1zfiyB7Euw",
    "domain": "AI",
    "title": "《AI+Python》用AI写Python代码做一个软件",
    "url": "http://www.bilibili.com/video/av115854125564263",
    "source": "自然非机械",
    "platform": "bilibili",
    "points": 15969,
    "published_at": "2026-01-07T13:57:39+00:00",
    "summary": "10分钟用AI写Python代码做一个软件"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15322,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1JhNC6zE8X",
    "domain": "AI",
    "title": "GPT 5.6 Sol 操控 Blender 有多强？社区案例、MCP 安装与真实实测",
    "url": "http://www.bilibili.com/video/av116910771473818",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 15227,
    "published_at": "2026-07-13T04:30:26+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\nGPT 5.6 发布后，Sol 与 Blender 的组合开始出现越来越多惊艳案例：从手绘机器人到 3D 打印零件，从零外部素材的建筑场景到写实动物，AI 正在改变 3D 建模的工作方式。\n\n这期视频里，我会先拆解社区中的优秀案例和高质量提示方法，再实际演示如何把 Blende"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 14961,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 14878,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV14a4y1T7Cp",
    "domain": "AI",
    "title": "VS Code + CursorCode 插件，AI 帮你编写、调试代码",
    "url": "http://www.bilibili.com/video/av654787185",
    "source": "马隆工作室",
    "platform": "bilibili",
    "points": 14093,
    "published_at": "2023-04-11T11:48:41+00:00",
    "summary": "免费， VS Code + CursorCode 插件，AI 帮你编写、调试代码"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 14055,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 370,
    "published_at": "2026-07-11T17:21:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48903715",
    "domain": "AI 算力 / 半导体",
    "title": "Alternative(s) to run CUDA on non-Nvidia hardware",
    "url": "https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/",
    "source": "alok-g",
    "platform": "hackernews",
    "points": 142,
    "published_at": "2026-07-14T08:24:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48597201",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung demonstrates 3D stacked FETs with triple nanosheet channels at 42nm",
    "url": "https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/",
    "source": "its_ajseven",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-06-19T11:03:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/",
    "domain": "AI 算力 / 半导体",
    "title": "New Material Beats Copper’s Thermal Conductivity",
    "url": "https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:00:00+00:00",
    "summary": "Meet θ-TaN, a metal that moves heat nearly 3× better than copper—and could upend chip cooling layers. The post New Material Beats Copper’s Thermal Conductivity appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/asml-raises-outlook-plans-more-euv-capacity/",
    "domain": "AI 算力 / 半导体",
    "title": "ASML Raises Outlook, Plans More EUV Capacity",
    "url": "https://www.eetimes.com/asml-raises-outlook-plans-more-euv-capacity/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:00:00+00:00",
    "summary": "ASML raised its full-year outlook as AI demand prompted plans to expand lithography capacity through at least 2028. The post ASML Raises Outlook, Plans More EUV Capacity appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Boosts 2026 Expansion Budget, Adds $100B to U.S. Investment",
    "url": "https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T05:55:59+00:00",
    "summary": "TSMC is raising its 2026 capital budget to $64 billion and adding $100 billion to its U.S. investment for AI. The post TSMC Boosts 2026 Expansion Budget, Adds $100B to U.S. Investment appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-data-centers-push-silicon-photonics-toward-300-mm-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Data Centers Push Silicon Photonics Toward 300-mm Scale",
    "url": "https://www.eetimes.com/ai-data-centers-push-silicon-photonics-toward-300-mm-scale/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T14:00:00+00:00",
    "summary": "AI data centers are torching copper’s reign as ST pushes 300-mm silicon photonics for faster, denser optical links. The post AI Data Centers Push Silicon Photonics Toward 300-mm Scale appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/india-adds-pieces-to-strengthen-its-electronics-supply-chain-puzzle/",
    "domain": "AI 算力 / 半导体",
    "title": "India Adds Pieces to Strengthen Its Electronics Supply Chain Puzzle",
    "url": "https://www.eetimes.com/india-adds-pieces-to-strengthen-its-electronics-supply-chain-puzzle/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T07:00:00+00:00",
    "summary": "India races to own more of its electronics value chain, from OSATs to PCBs, but imported materials still hold the leash. The post India Adds Pieces to Strengthen Its Electronics Supply Chain Puzzle ap"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asmls-planned-low-na-euv-machine-price-hikes-reportedly-frustrate-tsmc-lithography-machine-maker-comes-knocking-to-make-bank-on-tsmcs-profitable-fabs-potentially-costing-the-taiwanese-chipmaker-billions",
    "domain": "AI 算力 / 半导体",
    "title": "ASML's planned Low-NA EUV machine price hikes reportedly frustrate TSMC — lithography machine maker comes knocking to make bank on TSMC's profitable fabs, potentially costing the Taiwanese chipmaker b",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asmls-planned-low-na-euv-machine-price-hikes-reportedly-frustrate-tsmc-lithography-machine-maker-comes-knocking-to-make-bank-on-tsmcs-profitable-fabs-potentially-costing-the-taiwanese-chipmaker-billions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:57:16+00:00",
    "summary": "ASML says that the increased productivity of its Low-NA EUV tools gives it an option to increase the prices of these scanners in the future. The move may have a drastic effect on TSMC's future expansi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC confirms significant yield and performance improvements in A14 update — strong interest from AI/HPC and smartphone customers",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:30:26+00:00",
    "summary": "TSMC's A14 process technology progresses faster than N2 at this stage of development as developers of both client and AI/HPC plan to use it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fbi-arrests-florida-man-in-steam-malware-investigaton-after-tracing-stolen-bitcoin-to-uber-eats-gift-cards",
    "domain": "AI 算力 / 半导体",
    "title": "Florida man arrested after allegedly stealing $220,000 in crypto using malware hidden in Steam Games — 8,000 devices infected",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fbi-arrests-florida-man-in-steam-malware-investigaton-after-tracing-stolen-bitcoin-to-uber-eats-gift-cards",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:43:21+00:00",
    "summary": "Federal agents arrested 21-year-old Zyaire Dontaevious Zamarion Wilkins of North Lauderdale, Florida, on Tuesday."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/best-back-to-school-tech-deals-on-laptops-and-essential-tech-save-on-new-semester-essentials-now",
    "domain": "AI 算力 / 半导体",
    "title": "Best Back to School tech deals on laptops and essential tech — save on new semester essentials now",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/best-back-to-school-tech-deals-on-laptops-and-essential-tech-save-on-new-semester-essentials-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:29:45+00:00",
    "summary": "Grab savings on the best back-to-school tech deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/gamestop-ceo-says-sonys-decision-to-go-disc-less-is-totally-irrelevant-claims-software-including-physical-discs-accounts-for-only-12-percent-of-the-companys-business",
    "domain": "AI 算力 / 半导体",
    "title": "GameStop CEO says Sony's decision to go disc-less is 'totally irrelevant' — claims software, including physical discs, accounts for only 12% of the company's business",
    "url": "https://www.tomshardware.com/video-games/console-gaming/gamestop-ceo-says-sonys-decision-to-go-disc-less-is-totally-irrelevant-claims-software-including-physical-discs-accounts-for-only-12-percent-of-the-companys-business",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T13:51:39+00:00",
    "summary": "GameStop CEO Ryan Cohen says Sony’s physical game exit is irrelevant to the company's business, amid a $56 billion eBay takeover, as collectibles now drive growth."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security",
    "domain": "AI 算力 / 半导体",
    "title": "Lawmakers want US government to ban memory chips from China, even in allied supply chains — citing 'unacceptable risk' to national, economic, and supply chain security",
    "url": "https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T13:05:44+00:00",
    "summary": "U.S. lawmakers demand Commerce Secretary Howard Lutnick to ban imports of memory chips from China to the U.S., ask allies to do the same."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/ai-data-centers-must-produce-as-much-power-as-they-use-australia-pm-says-new-national-ai-framework-will-also-ensure-water-efficiency-and-protect-intellectual-property-rights",
    "domain": "AI 算力 / 半导体",
    "title": "AI data centers must produce as much power as they use, Australia PM says — new national AI framework will also ensure water efficiency and protect intellectual property rights",
    "url": "https://www.tomshardware.com/tech-industry/policy/ai-data-centers-must-produce-as-much-power-as-they-use-australia-pm-says-new-national-ai-framework-will-also-ensure-water-efficiency-and-protect-intellectual-property-rights",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T12:16:03+00:00",
    "summary": "Australian Prime Minister Anthony Albanese announced the \"Australian Standards for A.I.,\" which will serve as a national framework for data center developments related to AI. The government plans to s"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-nova-lake-leak-points-to-core-ultra-series-400-branding-staggered-release-next-year-hotly-anticipated-flagship-52-core-desktop-cpu-might-not-arrive-until-late-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Nova Lake leak points to Core Ultra Series 400 branding, staggered release next year — hotly anticipated flagship 52-core desktop CPU might not arrive until late 2027",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-nova-lake-leak-points-to-core-ultra-series-400-branding-staggered-release-next-year-hotly-anticipated-flagship-52-core-desktop-cpu-might-not-arrive-until-late-2027",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T12:08:13+00:00",
    "summary": "Intel's upcoming Nova Lake desktop processors continue to gather momentum, with fresh reports hinting at Core Ultra Series 400 branding and a phased launch timeline."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3",
    "domain": "AI 算力 / 半导体",
    "title": "China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena benchmark— Moonshot AI delivers largest open-weight AI model ever, as China works around U.S. compute limits",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:32:01+00:00",
    "summary": "Beijing-based Moonshot AI has released Kimi K3, a 2.8 trillion parameter model that the company describes in its technical blog as the world's first open 3T-class system."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/score-usd1-100-off-this-oled-gaming-laptop-with-rtx-5070-ti-the-ultimate-back-to-school-powerhouse-also-features-a-24-core-ultra-9-290hx-32gb-of-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Score $1,100 off this OLED gaming laptop with RTX 5070 Ti, the ultimate Back to School powerhouse — also features a 24-core Ultra 9 290HX, 32GB of RAM, and a 1TB SSD",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/score-usd1-100-off-this-oled-gaming-laptop-with-rtx-5070-ti-the-ultimate-back-to-school-powerhouse-also-features-a-24-core-ultra-9-290hx-32gb-of-ram-and-a-1tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:24:25+00:00",
    "summary": "Get $1,100 off this HP Omen Max laptop with OLED display, Ultra 9 290HX, 32GB of RAM, and RTX 5070 Ti."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/get-amds-new-ryzen-7-7700x3d-with-16gb-of-ram-and-a-motherboard-for-just-usd450-save-31-percent-on-a-b650m-micro-atx-and-g-skill-ddr5-for-an-epic-small-build",
    "domain": "AI 算力 / 半导体",
    "title": "Get AMD’s new Ryzen 7 7700X3D with 16GB of RAM and a motherboard for just $450 — save 31% on a B650M Micro ATX and G.Skill DDR5 for an epic small build",
    "url": "https://www.tomshardware.com/laptops/get-amds-new-ryzen-7-7700x3d-with-16gb-of-ram-and-a-motherboard-for-just-usd450-save-31-percent-on-a-b650m-micro-atx-and-g-skill-ddr5-for-an-epic-small-build",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:22:31+00:00",
    "summary": "Save over 31% on the price of this Newegg 7700X3D bundle. CPU, motherboard, and RAM combo is just $450 after discounts."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/msi-mag-z890-tomahawk-wifi-ii-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "MSI MAG Z890 Tomahawk Wifi II motherboard review: Loses features from the original, but shaves a few dollars off the price",
    "url": "https://www.tomshardware.com/pc-components/motherboards/msi-mag-z890-tomahawk-wifi-ii-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:10:00+00:00",
    "summary": "SI’s Z890 Tomahawk Wifi II trims a couple of connectivity features, but at its sub-$200 price, it’s still a reasonably equipped budget Z890 board."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-looks-to-increase-prices-of-its-low-na-euv-tools-beyond-existing-productivity-based-model-company-wants-to-capture-the-value-of-all-the-advantages-its-tools-offer-not-just-wafer-throughput-improvements",
    "domain": "AI 算力 / 半导体",
    "title": "ASML looks to increase prices of its Low-NA EUV tools beyond existing productivity-based model — company wants to capture the value of all the advantages its tools offer, not just wafer throughput imp",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-looks-to-increase-prices-of-its-low-na-euv-tools-beyond-existing-productivity-based-model-company-wants-to-capture-the-value-of-all-the-advantages-its-tools-offer-not-just-wafer-throughput-improvements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T10:30:00+00:00",
    "summary": "ASML's comments point to intentions to increase prices, though the company is expected to maintain its value-based approach to price setting. Yet, TSMC is reportedly unhappy about the potential plan."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/mario-kart-wii-recompiled-for-pc-using-ai-with-4k-potential-and-uncapped-frame-rates-first-static-recompilation-of-a-wii-game-supports-over-200-tracks-thanks-to-retro-rewind-compatibility",
    "domain": "AI 算力 / 半导体",
    "title": "Mario Kart Wii recompiled for PC using AI, with 4K potential and uncapped frame rates — 'first static recompilation of a Wii game' supports over 200 tracks thanks to Retro Rewind compatibility",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/mario-kart-wii-recompiled-for-pc-using-ai-with-4k-potential-and-uncapped-frame-rates-first-static-recompilation-of-a-wii-game-supports-over-200-tracks-thanks-to-retro-rewind-compatibility",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T10:00:33+00:00",
    "summary": "Mario Kart Wiicompiled, a claimed 'first static recompilation of a Wii game,' is scheduled to be released in August."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/shark-robot-vacuum-flaw-lets-one-stolen-certificate-run-root-commands-on-others-in-the-same-aws-region",
    "domain": "AI 算力 / 半导体",
    "title": "Robot vacuum flaw lets one stolen certificate run root commands on other Shark robovacs in the same AWS region — unpatched flaw exposes live camera feeds, stored home maps, and Wi-Fi credentials",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/shark-robot-vacuum-flaw-lets-one-stolen-certificate-run-root-commands-on-others-in-the-same-aws-region",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T10:00:00+00:00",
    "summary": "The problem is an over-permissive AWS IoT policy."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linus-torvalds-rebukes-anti-ai-stances-in-the-linux-kernel-code-review-process-says-linux-is-not-one-of-those-anti-ai-projects-creator-embraces-ai-as-just-a-tool-and-clearly-a-useful-one",
    "domain": "AI 算力 / 半导体",
    "title": "Linus Torvalds rebukes anti-AI stances in the Linux kernel code review process, says 'Linux is not one of those anti-AI projects' — creator embraces AI as just a tool and 'clearly a useful one'",
    "url": "https://www.tomshardware.com/software/linux/linus-torvalds-rebukes-anti-ai-stances-in-the-linux-kernel-code-review-process-says-linux-is-not-one-of-those-anti-ai-projects-creator-embraces-ai-as-just-a-tool-and-clearly-a-useful-one",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:59:13+00:00",
    "summary": "Linus Torvalds, Linux's creator and kernel manager, has seemingly taken an accepting stance of AI-assisted tooling."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/quantum-computing/neural-atom-quantum-computing-roadmap-how-laser-cooled-trapped-atoms-could-pave-the-path-beyond-physical-qubit-counts",
    "domain": "AI 算力 / 半导体",
    "title": "Neural atom quantum computing roadmap — how laser-cooled trapped atoms could pave the path beyond physical qubit counts",
    "url": "https://www.tomshardware.com/tech-industry/quantum-computing/neural-atom-quantum-computing-roadmap-how-laser-cooled-trapped-atoms-could-pave-the-path-beyond-physical-qubit-counts",
    "source": "Francisco Pires",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:52:54+00:00",
    "summary": "Neural Atom Quantum Computing is a rapidly accelerating part of the Quantum puzzle. Featuring software-defined configurable arrays, qubits can be physically moved mid-computation, and this roadmap hig"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-is-exclusive-to-newegg-in-north-america-usd329-cpu-wont-be-available-at-other-vendors-until-at-least-q4",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 7700X3D is exclusive to Newegg in North America — $329 CPU won't be available at other vendors until at least Q4",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-is-exclusive-to-newegg-in-north-america-usd329-cpu-wont-be-available-at-other-vendors-until-at-least-q4",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:47:21+00:00",
    "summary": "AMD's newest CPU, the Ryzen 7 7700X3D, costs $329 and is available exclusively at Newegg in Canada and the United States till the end of Q3 2026. It's a great gaming performer but there are better opt"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tower-semiconductor-revives-shuttered-panasonic-era-fab-in-3-billion-japan-photonics-expansion",
    "domain": "AI 算力 / 半导体",
    "title": "Tower Semiconductor revives shuttered Panasonic-era fab in $3 billion Japan photonics expansion — METI-backed plan targets $3.6 billion revenue by 2028",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tower-semiconductor-revives-shuttered-panasonic-era-fab-in-3-billion-japan-photonics-expansion",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:39:09+00:00",
    "summary": "Tower Semiconductor has announced a dual-track expansion of its 300mm silicon photonics, silicon germanium, and advanced packaging operations in Japan"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/lenovo-announces-worlds-first-laptop-with-inkjet-printed-oled-the-legion-r9000p-is-equipped-with-a-240-hz-ijp-panel-from-tcl-csot",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo announces world's first laptop with inkjet-printed OLED — the Legion R9000P is equipped with a 240 Hz IJP panel from TCL CSOT",
    "url": "https://www.tomshardware.com/monitors/lenovo-announces-worlds-first-laptop-with-inkjet-printed-oled-the-legion-r9000p-is-equipped-with-a-240-hz-ijp-panel-from-tcl-csot",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:20:36+00:00",
    "summary": "The Lenovo Legion R9000P is the first laptop to be equipped with an IJP OLED from TCL CSOT. This display promises a 240 Hz refresh rate and 99% DCI-P3 coverage for a fraction of the price of tradition"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-and-japans-noetra-consortium-to-build-140mw-rubin-ai-factory-with-27500-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Japan unveil world's first national AI infrastructure — Noetra consortium to build a 140MW Rubin AI factory with 27,500 GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-and-japans-noetra-consortium-to-build-140mw-rubin-ai-factory-with-27500-gpus",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T13:43:58+00:00",
    "summary": "Nvidia today announced that it's working with Japan's Noetra Corp. to build a 140-megawatt AI factory packing 27,500 Rubin GPUs and 13,750 Vera CPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-cpu-review",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 7700X3D review: A slower 7800X3D, but not necessarily a cheaper one",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-cpu-review",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T13:00:00+00:00",
    "summary": "The 7700X3D is a 7800X3D with lower boost clock speeds, but it doesn’t deliver the same value as we’ve seen with previous versions of this segmentation."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musk-spent-estimated-usd1-billion-on-an-energy-company-to-power-xai-filings-reveal-apr-energy-owns-a-fleet-of-trailer-mounted-gas-and-diesel-turbines-capable-of-generating-more-than-1-gigawatt",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk spent estimated $1 billion on an energy company to power xAI, filings reveal — APR Energy owns a fleet of trailer-mounted gas and diesel turbines capable of generating more than 1 gigawatt",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musk-spent-estimated-usd1-billion-on-an-energy-company-to-power-xai-filings-reveal-apr-energy-owns-a-fleet-of-trailer-mounted-gas-and-diesel-turbines-capable-of-generating-more-than-1-gigawatt",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T12:45:17+00:00",
    "summary": "An FTC document revealed that Elon Musk purchased APR Energy, a mobile natural gas and diesel turbine generator provider, for an estimated $1 billion. The deal wasn't announced publicly and was only d"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/tsmc-commits-another-100-billion-to-arizona-for-at-least-four-more-2nm-fabs",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC commits another $100 billion to Arizona for at least four more 2nm fabs — 2026 capex could hit $64 billion following another record quarterly earnings",
    "url": "https://www.tomshardware.com/tech-industry/tsmc-commits-another-100-billion-to-arizona-for-at-least-four-more-2nm-fabs",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T12:10:51+00:00",
    "summary": "TSMC will invest an additional $100 billion in the U.S. to build at least four more chipmaking plants and advanced packaging facilities in Arizona."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/asus-rog-xreal-r1-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Xreal R1 Review: Gaming-focused AR glasses deliver 240 Hz performance and RGB style",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/asus-rog-xreal-r1-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T12:00:00+00:00",
    "summary": "Asus throws in everything but the kitchen sink with the ROG Xreal R1, including a 240 Hz refresh rate and a breakout box for connecting to a PC or console."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-research-founder-edition-indx-launches-limited-1-000-unit-run-of-revolutionary-toolchanger-mod-now-shipping",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa Research Founder Edition INDX launches — limited 1,000-unit run of revolutionary toolchanger mod now shipping",
    "url": "https://www.tomshardware.com/3d-printing/prusa-research-founder-edition-indx-launches-limited-1-000-unit-run-of-revolutionary-toolchanger-mod-now-shipping",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T11:55:55+00:00",
    "summary": "One thousand Prusa CORE One INDX Founder’s Editions have shipped, giving a lucky few first access to Bondtech’s revolutionary toolchanger mod. The Founders Edition is a special limited run, intended f"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/save-usd300-on-the-bambu-lab-p1s-right-now-in-stock-and-back-to-a-record-low-usd399-score-a-huge-discount-on-this-fully-enclosed-easy-to-use-corexy-3d-printer-with-automatic-bed-leveling-and-a-beginner-friendly-setup",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on the Bambu Lab P1S right now, in stock and back to a record-low $399 — score a huge discount on this fully enclosed, easy-to-use CoreXY 3D printer with automatic bed leveling and a beginne",
    "url": "https://www.tomshardware.com/3d-printing/save-usd300-on-the-bambu-lab-p1s-right-now-in-stock-and-back-to-a-record-low-usd399-score-a-huge-discount-on-this-fully-enclosed-easy-to-use-corexy-3d-printer-with-automatic-bed-leveling-and-a-beginner-friendly-setup",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T11:07:16+00:00",
    "summary": "The Bambu Lab P1S 3D printer is on sale for $399.99 right now, back at its record low price."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/keyboards/openais-first-hardware-device-is-an-rgb-macropod-codex-micro-features-13-low-profile-keys-and-a-joystick-for-controlling-ai-coding-agents",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's first hardware device is an RGB macropod — 'Codex Micro' features 13 low-profile keys and a joystick for controlling AI coding agents",
    "url": "https://www.tomshardware.com/peripherals/keyboards/openais-first-hardware-device-is-an-rgb-macropod-codex-micro-features-13-low-profile-keys-and-a-joystick-for-controlling-ai-coding-agents",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T11:00:00+00:00",
    "summary": "OpenAI has launched the \"Codex Micro\" marcopad in collaboration with Work Louder. It uses RGB to provide feedback about your coding agents in Codex, and features various customizable inputs to maximiz"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5080-gaming-laptop-for-just-usd2-199-thanks-to-this-hp-omen-max-deal-save-usd1-500-on-amd-ryzen-9-beast-with-32gb-of-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5080 gaming laptop for just $2,199 thanks to this HP Omen Max deal — save $1,500 on AMD Ryzen 9 beast with 32GB of RAM",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5080-gaming-laptop-for-just-usd2-199-thanks-to-this-hp-omen-max-deal-save-usd1-500-on-amd-ryzen-9-beast-with-32gb-of-ram",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T10:33:11+00:00",
    "summary": "Get $1,500 off this HP Omen Max gaming laptop with AMD Ryzen 9, RTX 5080, and 32GB of RAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/scientists-synchronize-105-000-nano-oscillators-in-just-45-nanoseconds-paving-the-way-for-a-highly-efficient-and-fast-alternative-to-transistors",
    "domain": "AI 算力 / 半导体",
    "title": "Scientists synchronize 105,000 nano-oscillators in just 45 nanoseconds — paving the way for a highly efficient and fast alternative to transistors",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/scientists-synchronize-105-000-nano-oscillators-in-just-45-nanoseconds-paving-the-way-for-a-highly-efficient-and-fast-alternative-to-transistors",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T10:30:00+00:00",
    "summary": "Scientists synchronize 105,000 nano-oscillators in just 45 nanoseconds — paving way for highly efficient and fast alternative to transistors"
  },
  {
    "id": "rss:https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/",
    "domain": "AI 算力 / 半导体",
    "title": "How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots",
    "url": "https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:06:44+00:00",
    "summary": "Nidec tackles the brutal gearbox tradeoffs behind humanoid robots, from zero backlash to lighter integrated actuators. The post How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots appea"
  },
  {
    "id": "rss:https://www.eetimes.com/tyl-semi-de-risks-chiplets-with-new-business-model/",
    "domain": "AI 算力 / 半导体",
    "title": "TYLsemi De-Risks Chiplets With New Business Model",
    "url": "https://www.eetimes.com/tyl-semi-de-risks-chiplets-with-new-business-model/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:00:00+00:00",
    "summary": "Startup TYLsemi wants to address the gap between ASIC houses and design services, taking on the risk of developing large chiplet-based chips for AI infrastructure customers. The post TYLsemi De-Risks "
  },
  {
    "id": "rss:https://www.eetimes.com/why-tl3228-is-the-go-to-standard-chip-powering-true-8k-wireless-gaming-peripherals/",
    "domain": "AI 算力 / 半导体",
    "title": "Why TL3228 Is the Go-To Standard Chip Powering True 8K Wireless Gaming Peripherals",
    "url": "https://www.eetimes.com/why-tl3228-is-the-go-to-standard-chip-powering-true-8k-wireless-gaming-peripherals/",
    "source": "Telink",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:00:00+00:00",
    "summary": "The TL3228 integrates a dual-core RISC-V processor consisting of a high-performance D25F core and an energy-efficient N22 core. The post Why TL3228 Is the Go-To Standard Chip Powering True 8K Wireless"
  },
  {
    "id": "rss:https://www.eetimes.com/massive-stock-full-chain-service-your-global-semiconductor-partner/",
    "domain": "AI 算力 / 半导体",
    "title": "Massive Stock, Full-Chain Service — Your Global Semiconductor Partner",
    "url": "https://www.eetimes.com/massive-stock-full-chain-service-your-global-semiconductor-partner/",
    "source": "NEW IDEAS INDUSTRIAL CO., LIMITED",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:00:00+00:00",
    "summary": "Discover how New Ideas Industrial can stabilize your semiconductor supply chain for AI, storage, and UAV applications. The post Massive Stock, Full-Chain Service — Your Global Semiconductor Partner ap"
  },
  {
    "id": "rss:https://www.eetimes.com/after-magdeburg-intel-builds-on-ireland-existing-strength/",
    "domain": "AI 算力 / 半导体",
    "title": "After Magdeburg, Intel Builds on Ireland’s Existing Strength",
    "url": "https://www.eetimes.com/after-magdeburg-intel-builds-on-ireland-existing-strength/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:24:18+00:00",
    "summary": "Leixlip cannot replace Magdeburg, but it shows the value of expanding where fabs, demand, and ecosystems already exist. The post After Magdeburg, Intel Builds on Ireland’s Existing Strength appeared f"
  },
  {
    "id": "hn:48894277",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-13T15:32:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-09T13:29:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48734960",
    "domain": "AI 算力 / 半导体",
    "title": "Etched has officially come out of stealth",
    "url": "https://www.bloomberg.com/news/articles/2026-06-30/ai-chip-startup-etched-says-jane-street-tsmc-linked-vc-invested",
    "source": "seventeen29",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-30T16:21:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48601996",
    "domain": "AI 算力 / 半导体",
    "title": "ASML denies US Government report that EUV chipmaking tool was shipped to China",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-denies-us-government-report-that-its-euv-chipmaking-tool-was-shipped-to-china-says-rumors-are-inaccurate-and-damaging-to-our-reputation",
    "source": "srameshc",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-19T19:03:30+00:00",
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
    "id": "hn:48936451",
    "domain": "大厂 AI 动态",
    "title": "NotebookLM is now Gemini Notebook",
    "url": "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 364,
    "published_at": "2026-07-16T16:08:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48735444",
    "domain": "大厂 AI 动态",
    "title": "Nano Banana 2 Lite",
    "url": "https://deepmind.google/models/gemini-image/flash-lite/",
    "source": "minimaxir",
    "platform": "hackernews",
    "points": 435,
    "published_at": "2026-06-30T16:48:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 362,
    "published_at": "2026-07-15T18:40:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756602",
    "domain": "大厂 AI 动态",
    "title": "Kimi K2.7 Code is generally available in GitHub Copilot",
    "url": "https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/",
    "source": "unliftedq",
    "platform": "hackernews",
    "points": 417,
    "published_at": "2026-07-02T04:32:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48662999",
    "domain": "大厂 AI 动态",
    "title": "Computer use in Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 242,
    "published_at": "2026-06-24T17:21:34+00:00",
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
    "id": "hn:48707103",
    "domain": "大厂 AI 动态",
    "title": "Google limits Meta's use of its Gemini AI models",
    "url": "https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-06-28T13:30:06+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/science/967563/cyclospora-taylor-farms-taco-bell-iceberg-lettuce",
    "domain": "大厂 AI 动态",
    "title": "Taylor Farms pulls iceberg lettuce from the US market after cyclosporiasis outbreak",
    "url": "https://www.theverge.com/science/967563/cyclospora-taylor-farms-taco-bell-iceberg-lettuce",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T22:09:47+00:00",
    "summary": "Food producer Taylor Farms released a statement on the Cyclospora outbreak Friday, confirming that it's \"voluntarily removing all iceberg lettuce sourced from central Mexico from the US market.\" Reute"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/967512/shark-chillpill-personal-fan-and-cooling-system-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Shark&#8217;s versatile ChillPill cooling system is back to its best price",
    "url": "https://www.theverge.com/gadgets/967512/shark-chillpill-personal-fan-and-cooling-system-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T20:15:54+00:00",
    "summary": "Portable fans are one of the easiest ways to stay cool during the summer, and you don&#8217;t have to spend much to find a decent one. If you&#8217;re looking for something more versatile, though, Sha"
  },
  {
    "id": "rss:https://www.theverge.com/tech/967486/tiktok-ai-likeness-detection-tool",
    "domain": "大厂 AI 动态",
    "title": "TikTok is testing an AI likeness detection tool",
    "url": "https://www.theverge.com/tech/967486/tiktok-ai-likeness-detection-tool",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:34:30+00:00",
    "summary": "TikTok is starting to test an opt-in tool that scans for AI likenesses and lets creators report them to the company, as spotted by social media consultant Matt Navarra. The tool is initially being tes"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/967471/pebble-smartwatch-warranty-repairs-migicovsky-interview",
    "domain": "大厂 AI 动态",
    "title": "Pebble founder Eric Migicovsky says his 30-day warranty is all about trust",
    "url": "https://www.theverge.com/gadgets/967471/pebble-smartwatch-warranty-repairs-migicovsky-interview",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:14:42+00:00",
    "summary": "Pebble founder Eric Migicovsky says buyers of its new e-paper smartwatches should know what they're signing up for and trust Pebble to make things right if they run into issues, despite the short warr"
  },
  {
    "id": "rss:https://www.theverge.com/tech/967379/apple-music-price-increase",
    "domain": "大厂 AI 动态",
    "title": "Apple Music is getting a price hike",
    "url": "https://www.theverge.com/tech/967379/apple-music-price-increase",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T18:14:26+00:00",
    "summary": "Apple Music is more expensive now. In the US, an individual plan now costs $11.99 per month, a $1 bump up from the previous $10.99 price. A family plan now costs $19.99 per month, up from $16.99, and "
  },
  {
    "id": "rss:https://www.theverge.com/podcast/967244/apple-openai-lawsuit-vergecast",
    "domain": "大厂 AI 动态",
    "title": "Apple’s plot to crush OpenAI",
    "url": "https://www.theverge.com/podcast/967244/apple-openai-lawsuit-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T17:41:32+00:00",
    "summary": "Apple is suing OpenAI. The complaint is readable and intense, as these things often are, though many experts seem to think many of the allegations are just the ways things are done. So what does Apple"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/966907/asus-rog-swift-qd-oled-marathon-steam-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Asus’ top-end 4K QD-OLED gaming monitor is $400 off",
    "url": "https://www.theverge.com/gadgets/966907/asus-rog-swift-qd-oled-marathon-steam-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:47:13+00:00",
    "summary": "The Asus ROG Swift 32-inch 4K QD-OLED gaming monitor has almost everything I want in a high-end gaming monitor, most notably a QD-OLED panel for inky black levels and vivid colors that go beyond what’"
  },
  {
    "id": "rss:https://www.theverge.com/tech/967198/samsung-galaxy-z-fold-8-images-specs-leak",
    "domain": "大厂 AI 动态",
    "title": "Samsung&#8217;s redesigned Z Fold 8 with a wide display just leaked",
    "url": "https://www.theverge.com/tech/967198/samsung-galaxy-z-fold-8-images-specs-leak",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:52:50+00:00",
    "summary": "Leaker Evan Blass shared images of Samsung's redesigned Galaxy Z Fold 8 just days before the July 22nd launch event where Samsung is expected to officially announce the phone. The leaked images show a"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/966498/chip-motors-low-speed-ev-remote-park-price",
    "domain": "大厂 AI 动态",
    "title": "Is America ready for this quirky Jeep-looking EV that can park itself?",
    "url": "https://www.theverge.com/transportation/966498/chip-motors-low-speed-ev-remote-park-price",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:48:39+00:00",
    "summary": "Are we living through a small car renaissance? There's the Slate Truck, Amble's dune buggy, and the Fiat Topolino, as well as a whole galaxy of kei cars and trucks from Japan that have their own built"
  },
  {
    "id": "rss:https://www.theverge.com/games/967174/steam-game-malware-cryptostealer-arrest",
    "domain": "大厂 AI 动态",
    "title": "Florida man arrested for allegedly stealing over $200,000 in crypto using Steam game malware",
    "url": "https://www.theverge.com/games/967174/steam-game-malware-cryptostealer-arrest",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:34:35+00:00",
    "summary": "Federal authorities have arrested a Florida man suspected of stealing at least $220,000 in crypto through malware-infected Steam games, as reported earlier by local news outlet Local10. In the complai"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/neil-rimer-thinks-the-ai-money-is-coming-back-out/",
    "domain": "大厂 AI 动态",
    "title": "Neil Rimer thinks the AI money is coming back out",
    "url": "https://techcrunch.com/2026/07/17/neil-rimer-thinks-the-ai-money-is-coming-back-out/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T04:47:25+00:00",
    "summary": "Neil Rimer, the venture capitalist who co-founded Index Ventures, predicts the historic wealth AI is generating in Silicon Valley will have to be redistributed, voluntarily or involuntarily."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/applications-close-in-48-hours-heres-everything-australian-founders-need-to-know-about-stripe-x-startup-battlefield/",
    "domain": "大厂 AI 动态",
    "title": "Applications close in 48 hours — here’s everything Australian founders need to know about Stripe x Startup Battlefield",
    "url": "https://techcrunch.com/2026/07/17/applications-close-in-48-hours-heres-everything-australian-founders-need-to-know-about-stripe-x-startup-battlefield/",
    "source": "Isabelle Johannessen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T23:08:00+00:00",
    "summary": "The window is almost shut. On August 19, eight startups will take the stage at Stripe Tour Sydney in front of investors, global press, and the Australian tech community. One startup walks away with au"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/vertu-wants-executives-to-pay-6880-for-an-ai-agent-heres-how-it-actually-performs/",
    "domain": "大厂 AI 动态",
    "title": "Vertu wants executives to pay $6,880 for an AI agent — here’s how it actually performs",
    "url": "https://techcrunch.com/2026/07/17/vertu-wants-executives-to-pay-6880-for-an-ai-agent-heres-how-it-actually-performs/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T22:55:09+00:00",
    "summary": "From AI workflows to battery life and security, here's what it's really like to live with Vertu's luxury foldable every day."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/",
    "domain": "大厂 AI 动态",
    "title": "Databricks hits $188B valuation, extending its run as AI’s favorite second act",
    "url": "https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T22:12:56+00:00",
    "summary": "Databricks has remade its image into an AI company and has published research on the cost savings of open weight AI models for coding."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/the-zoom-hack-that-says-dont-record-me/",
    "domain": "大厂 AI 动态",
    "title": "The Zoom hack that says, ‘Don’t record me’",
    "url": "https://techcrunch.com/2026/07/17/the-zoom-hack-that-says-dont-record-me/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T21:20:47+00:00",
    "summary": "If every meeting, watercooler conversation, and date gets transcribed and summarized, who's actually reading any of it?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/agility-robotics-plants-its-flag-in-teslas-backyard/",
    "domain": "大厂 AI 动态",
    "title": "Agility Robotics plants its flag in Tesla’s backyard",
    "url": "https://techcrunch.com/2026/07/17/agility-robotics-plants-its-flag-in-teslas-backyard/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T20:19:49+00:00",
    "summary": "Agility is opening a new training center for its Digit robots in Fremont, California."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/ai-driven-memory-crunch-jolts-indias-smartphone-market/",
    "domain": "大厂 AI 动态",
    "title": "AI-driven memory crunch jolts India’s smartphone market",
    "url": "https://techcrunch.com/2026/07/17/ai-driven-memory-crunch-jolts-indias-smartphone-market/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T20:09:27+00:00",
    "summary": "India's smartphone slowdown highlights how the AI boom is reshaping consumer electronics, from pricing and demand to corporate strategy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/",
    "domain": "大厂 AI 动态",
    "title": "Apple and Google ordered to purge ‘nudify’ apps from App Stores",
    "url": "https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:49:53+00:00",
    "summary": "In letters sent to Apple and Google, San Francisco City Attorney David Chiu said that both companies have long been aware that they are hosting apps in violation of state law."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/nuclear-startup-valar-atomics-in-talks-to-raise-new-funding-at-6b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Nuclear startup Valar Atomics in talks to raise new funding at $6B valuation",
    "url": "https://techcrunch.com/2026/07/17/nuclear-startup-valar-atomics-in-talks-to-raise-new-funding-at-6b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:22:00+00:00",
    "summary": "The potential deal highlights a growing trend of complex, multi-stage funding rounds that mask true entry prices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/i-replaced-my-space-heater-and-ceiling-fan-with-one-dyson-appliance/",
    "domain": "大厂 AI 动态",
    "title": "I replaced my space heater and ceiling fan with one Dyson appliance",
    "url": "https://techcrunch.com/2026/07/17/i-replaced-my-space-heater-and-ceiling-fan-with-one-dyson-appliance/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T18:00:17+00:00",
    "summary": "Designed for year-round comfort, the Dyson Hot+Cool HF1 combines quiet operation and simple controls with Dyson's signature bladeless design."
  },
  {
    "id": "rss:https://techcrunch.com/video/how-apples-big-lawsuit-could-disrupt-openais-ipo-plans/",
    "domain": "大厂 AI 动态",
    "title": "How Apple’s big lawsuit could disrupt OpenAI’s IPO plans",
    "url": "https://techcrunch.com/video/how-apples-big-lawsuit-could-disrupt-openais-ipo-plans/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T17:45:46+00:00",
    "summary": "Apple&#160;filed a trade secrets&#160;lawsuit against OpenAI&#160;last Friday, and&#160;it&#8217;s&#160;not messing around. The complaint alleges a pattern of misconduct reaching all the way up to Ope"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/fbi-arrests-man-accused-of-using-steam-games-to-drain-victims-crypto-wallets/",
    "domain": "大厂 AI 动态",
    "title": "FBI arrests man accused of using Steam games to drain victims’ crypto wallets",
    "url": "https://techcrunch.com/2026/07/17/fbi-arrests-man-accused-of-using-steam-games-to-drain-victims-crypto-wallets/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:18:09+00:00",
    "summary": "Prosecutors accused 21-year-old student Zyaire Wilkins of publishing on Steam several fake video games that contained malware, infecting thousands of victims, and stealing crypto from some of them."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/parents-want-safer-phones-for-kids-these-companies-are-answering-the-call/",
    "domain": "大厂 AI 动态",
    "title": "Parents want safer phones for kids. These companies are answering the call.",
    "url": "https://techcrunch.com/2026/07/17/parents-want-safer-phones-for-kids-these-companies-are-answering-the-call/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:12:46+00:00",
    "summary": "As parents look for alternatives to unrestricted smartphones, a growing number of companies are building phones designed specifically for kids, from feature-limited mobile devices to minimalist home p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/amazon-fixing-bug-that-billed-some-aws-customers-billions-of-dollars/",
    "domain": "大厂 AI 动态",
    "title": "Amazon fixing bug that billed some AWS customers billions of dollars",
    "url": "https://techcrunch.com/2026/07/17/amazon-fixing-bug-that-billed-some-aws-customers-billions-of-dollars/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:29:21+00:00",
    "summary": "Some Amazon customers logged on Friday to a surprise bill estimate claiming that they owed the tech and cloud giant billions in fees."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/",
    "domain": "大厂 AI 动态",
    "title": "Patreon stops asking AI bots not to scrape — and starts blocking them",
    "url": "https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:21:17+00:00",
    "summary": "Patreon is strengthening its defenses against AI scraping by working with Cloudflare to block bots that train AI models on creators’ content without permission. The move marks a shift away from relyin"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/remarkables-new-paper-pure-is-good-thats-why-i-wrote-this-review-on-it/",
    "domain": "大厂 AI 动态",
    "title": "reMarkable’s new Paper Pure is good. That’s why I wrote this review on it.",
    "url": "https://techcrunch.com/2026/07/17/remarkables-new-paper-pure-is-good-thats-why-i-wrote-this-review-on-it/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:47:27+00:00",
    "summary": "Remarkable's Paper Pure replaces Remarkable 2, and it is quite good."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/no-product-no-problem-this-disrupt-2026-session-shows-how-to-get-pre-seed-funding-with-conviction-storytelling/",
    "domain": "大厂 AI 动态",
    "title": "No product? No problem. This Disrupt 2026 session shows how to get pre-seed funding with conviction, storytelling",
    "url": "https://techcrunch.com/2026/07/17/no-product-no-problem-this-disrupt-2026-session-shows-how-to-get-pre-seed-funding-with-conviction-storytelling/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:30:00+00:00",
    "summary": "It’s not just you: AI startups are taking in a huge amount of seed funding, and in the process making things harder for anyone looking for funding even at a pre-seed stage. We’ve covered the trend in "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/zoox-issues-software-recall-after-a-robotaxi-got-confused-by-heavy-smoke/",
    "domain": "大厂 AI 动态",
    "title": "Zoox issues software recall after a robotaxi got confused by heavy smoke",
    "url": "https://techcrunch.com/2026/07/17/zoox-issues-software-recall-after-a-robotaxi-got-confused-by-heavy-smoke/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:12:02+00:00",
    "summary": "The recall comes as the top automotive safety regulator in the U.S. has warned AV companies about their vehicles interfering with first responders."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/",
    "domain": "大厂 AI 动态",
    "title": "Why the first GPU financiers are turning to inference chips in a $400 million deal",
    "url": "https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T12:00:00+00:00",
    "summary": "A $400 million chip-backed loan points to the next wave of AI infrastructure deals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/san-francisco-mayor-pushes-for-tougher-rules-after-the-waymo-traffic-fiasco/",
    "domain": "大厂 AI 动态",
    "title": "San Francisco mayor pushes for tougher rules after the Waymo traffic fiasco",
    "url": "https://techcrunch.com/2026/07/16/san-francisco-mayor-pushes-for-tougher-rules-after-the-waymo-traffic-fiasco/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T23:25:22+00:00",
    "summary": "In the wake of a massive hours-long gridlock event, San Francisco mayor Daniel Lurie has told state regulators it's time to put more requirements on robotaxi operators like Waymo."
  },
  {
    "id": "rss:https://stratechery.com/2026/mainframes-and-main-characters/",
    "domain": "大厂 AI 动态",
    "title": "2026.29: Mainframes and Main Characters",
    "url": "https://stratechery.com/2026/mainframes-and-main-characters/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of July 13, 2026, including the end of the mainframe, the continuing adventures of OpenAI, and answering the question, \"Is Netflix Washed?\"."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/google-backed-satellites-for-wildfire-detection-launch-as-smoke-chokes-us-canada/",
    "domain": "大厂 AI 动态",
    "title": "Google-backed satellites for wildfire detection launch as smoke chokes US, Canada",
    "url": "https://arstechnica.com/space/2026/07/google-backed-satellites-for-wildfire-detection-launch-as-smoke-chokes-us-canada/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:50:18+00:00",
    "summary": "The FireSat program can spot wildfires that other satellites miss."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/the-pentagons-space-development-agency-hasnt-moved-as-fast-as-anyone-would-like/",
    "domain": "大厂 AI 动态",
    "title": "The Pentagon's Space Development Agency hasn't moved as fast as anyone would like",
    "url": "https://arstechnica.com/space/2026/07/the-pentagons-space-development-agency-hasnt-moved-as-fast-as-anyone-would-like/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:19:42+00:00",
    "summary": "\"Missiles are being launched at the joint force every single day in [Operation] Epic Fury.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/hegseth-wants-a-high-t-military-doctors-call-it-a-clinical-minefield/",
    "domain": "大厂 AI 动态",
    "title": "Hegseth wants a \"High-T\" military; doctors call it a clinical minefield",
    "url": "https://arstechnica.com/health/2026/07/hegseth-wants-a-high-t-military-doctors-call-it-a-clinical-minefield/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T18:53:11+00:00",
    "summary": "\"We're turning the clock back on rational healthcare.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/taco-bell-iceburg-lettuce-identified-as-source-of-cyclosporiasis-in-5-states/",
    "domain": "大厂 AI 动态",
    "title": "Taco Bell iceberg lettuce identified as source of cyclosporiasis in 5 states",
    "url": "https://arstechnica.com/health/2026/07/taco-bell-iceburg-lettuce-identified-as-source-of-cyclosporiasis-in-5-states/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T18:45:23+00:00",
    "summary": "Don't eat Taco Bell lettuce in Indiana, Kentucky, Michigan, Ohio, or West Virginia."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/troubling-new-details-emerge-on-diabetes-ouster-controversy/",
    "domain": "大厂 AI 动态",
    "title": "Troubling new details emerge on diabetes ouster controversy",
    "url": "https://arstechnica.com/science/2026/07/troubling-new-details-emerge-on-diabetes-ouster-controversy/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T17:08:05+00:00",
    "summary": "American Diabetes Association blocked publication of op-ed articles so the authors posted them as a preprint."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/will-russias-answer-to-the-falcon-9-rocket-ever-take-flight/",
    "domain": "大厂 AI 动态",
    "title": "Will Russia's answer to the Falcon 9 rocket ever take flight?",
    "url": "https://arstechnica.com/space/2026/07/will-russias-answer-to-the-falcon-9-rocket-ever-take-flight/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:42:19+00:00",
    "summary": "Grasshopper-like tests could begin in 2028."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/fubo-hikes-prices-by-15-after-restoring-some-nbcu-channels-lost-in-november/",
    "domain": "大厂 AI 动态",
    "title": "Fubo hikes prices by $15 after restoring some NBCU channels lost in November",
    "url": "https://arstechnica.com/gadgets/2026/07/fubo-hikes-prices-by-15-after-restoring-some-nbcu-channels-lost-in-november/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:24:21+00:00",
    "summary": "Fubo subscribers still don't have Versant channels."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/apple-google-must-stop-profiting-off-ai-nudify-apps-san-francisco-ag-says/",
    "domain": "大厂 AI 动态",
    "title": "San Francisco orders Apple, Google to remove nudify apps from app stores",
    "url": "https://arstechnica.com/tech-policy/2026/07/apple-google-must-stop-profiting-off-ai-nudify-apps-san-francisco-ag-says/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T16:10:05+00:00",
    "summary": "Official estimates Google and Apple likely made millions in nudify app fees."
  },
  {
    "id": "rss:https://arstechnica.com/staff/2026/07/ars-is-looking-for-a-senior-technology-reporter-and-you-might-be-it/",
    "domain": "大厂 AI 动态",
    "title": "Ars is looking for a senior technology reporter, and you might be it!",
    "url": "https://arstechnica.com/staff/2026/07/ars-is-looking-for-a-senior-technology-reporter-and-you-might-be-it/",
    "source": "Lee Hutchinson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:52:28+00:00",
    "summary": "Desktops, laptops, phones, CPUs, GPUs, NAS—if you know this stuff, come work for us!"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/national-academies-climate-attribution-is-maturing-but-still-has-limits/",
    "domain": "大厂 AI 动态",
    "title": "The report oil companies are worried about: Climate attribution science",
    "url": "https://arstechnica.com/science/2026/07/national-academies-climate-attribution-is-maturing-but-still-has-limits/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:30:10+00:00",
    "summary": "New report says our ability to tie weather damages to climate change is improving."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/fcc-took-pricey-gifts-from-paramount-as-the-company-needed-approval-for-deals/",
    "domain": "大厂 AI 动态",
    "title": "FCC took pricey gifts from Paramount as the company needed approval for deals",
    "url": "https://arstechnica.com/tech-policy/2026/07/fcc-took-pricey-gifts-from-paramount-as-the-company-needed-approval-for-deals/",
    "source": "Corey G. Johnson, ProPublica",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:15:55+00:00",
    "summary": "FCC chair has been gifted at least $63,000 worth of tickets by CBS or its parent company."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/2026-lucid-gravity-touring-review-a-strong-act-2/",
    "domain": "大厂 AI 动态",
    "title": "2026 Lucid Gravity Touring review: A strong act 2",
    "url": "https://arstechnica.com/cars/2026/07/2026-lucid-gravity-touring-review-a-strong-act-2/",
    "source": "Jim Resnick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:00:30+00:00",
    "summary": "Quick, comfortable, roomy, and agile for a large electric SUV."
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 312,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48948435",
    "domain": "股票",
    "title": "Short sellers notch $8.7B profit as SpaceX shares dip to IPO price",
    "url": "https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-07-17T15:17:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48678873",
    "domain": "股票",
    "title": "OpenAI leans toward waiting until next year for IPO",
    "url": "https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-06-25T20:36:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 78,
    "published_at": "2026-07-16T18:03:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-07-17T18:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48946872",
    "domain": "股票",
    "title": "US Corporate Insiders Are Selling Stocks at a Near Record Pace",
    "url": "https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace",
    "source": "pimienta",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-07-17T13:00:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48907665",
    "domain": "股票",
    "title": "IBM is on pace for its worst day ever",
    "url": "https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever",
    "source": "1970-01-01",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-07-14T14:39:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48947500",
    "domain": "股票",
    "title": "A.I. Is Running on Borrowed Money",
    "url": "https://www.nytimes.com/2026/07/17/business/ai-spending-oracle-stocks-bonds.html",
    "source": "ripe",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-17T14:01:11+00:00",
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
    "id": "wscn:3777291",
    "domain": "股票",
    "title": "高盛点评Kimi K3：中国开源模型“智能”达到全球普及关键点，高端模型竞争激烈",
    "url": "https://wallstreetcn.com/articles/3777291",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T05:11:08+00:00",
    "summary": "高盛表示，Kimi K3以2.8万亿参数横空出世，将API定价拉升至每百万token 2.3美元，创中国模型定价新高，标志着国内AI公司正式从\"价格战\"迈向\"定价权\"争夺。然而硬币另一面，智谱单日暴跌28%、MiniMax跌16%，揭示出高端编程赛道竞争白热化下，市场对AI模型公司护城河可持续性的深层焦虑。"
  },
  {
    "id": "wscn:3777289",
    "domain": "股票",
    "title": "AI牛市结束了吗？市场充满疑虑",
    "url": "https://wallstreetcn.com/articles/3777289",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T03:46:45+00:00",
    "summary": "科技巨头业绩亮眼、资本开支计划积极，股价却纹丝不动——这一诡异背离正令华尔街陷入困惑。野村证券警告，AI繁荣终结已从三种情景演变为四重路径交织，成本收益平衡愈发模糊。半导体重挫、软件逆涨的板块分化暗示资金悄然重定价，而债券市场迄今未现降息押注，意味着AI终结的定价远未完成。"
  },
  {
    "id": "wscn:3777285",
    "domain": "股票",
    "title": "阿里发布秒悟团队版，打造企业级AI应用创作平台",
    "url": "https://wallstreetcn.com/articles/3777285",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T03:20:21+00:00",
    "summary": "阿里在WAIC发布企业级AI创作平台秒悟团队版（Meoo Team），无需编程基础，用自然语言即可生成应用、网站、小程序并一键部署。上线仅三个月，日活用户已逾万人，超半数为非技术背景。此次团队版升级直击企业痛点——统一账号、灵活额度管控、三级权限治理，让组织级AI协作生产力全面跃升。"
  },
  {
    "id": "wscn:3777284",
    "domain": "股票",
    "title": "存储的“新鬼故事”：美国要抢钱了？",
    "url": "https://wallstreetcn.com/articles/3777284",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T03:09:41+00:00",
    "summary": "美国贸易代表副代表Rick Switzer明确主张，因美企大量采购推动了三星、SK海力士盈利，美方有权分享其利润。中信证券援引日本半导体、中国台湾面板的历史警示：海外企业高利润一旦被美方重新定性，政治介入往往随之而来，关注两大信号：美国科技巨头是否由锁定供给转向公开反对涨价，华盛顿是否将祭出\"垄断\"\"价格操纵\"等理由介入。"
  },
  {
    "id": "wscn:3777282",
    "domain": "股票",
    "title": "十年第七相：伯纳姆是谁？怎破英国困局？",
    "url": "https://wallstreetcn.com/articles/3777282",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T02:23:26+00:00",
    "summary": "英国工党新党首安迪·伯纳姆将于20日入主唐宁街，成为十年来第七位首相。他以大曼彻斯特\"深度放权\"治理经验为底牌，誓将\"曼彻斯特主义\"复制至全国。然而，经济下行、财政赤字、英欧关系、特朗普变数……堆积如山的挑战，能否撑起这位\"北方之声\"？"
  },
  {
    "id": "wscn:3777279",
    "domain": "股票",
    "title": "SpaceX市值已经蒸发了1万亿美元",
    "url": "https://wallstreetcn.com/articles/3777279",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T02:23:13+00:00",
    "summary": "上市仅数周，SpaceX市值已从峰值蒸发逾1万亿美元，股价跌破135美元发行价。旗舰火箭Starship发动机故障引爆抛售，乐观情绪加速消退。尽管华尔街逾八成分析师仍维持买入评级、平均目标价较当前高出90%，但锁定期解除压力与高估值争议持续发酵。"
  },
  {
    "id": "wscn:3777278",
    "domain": "股票",
    "title": "AI风向标！甲骨文债券CDS升至历史新高",
    "url": "https://wallstreetcn.com/articles/3777278",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T02:23:04+00:00",
    "summary": "甲骨文信用违约互换价差飙升至198.23基点，刷新历史纪录，标普随即将其评级下调至仅高于垃圾级一档。自由现金流告负、1170亿美元债券敞口高悬，叠加Kimi K3搅动AI竞争格局，股债两市正同步对这场豪赌AI基础设施的冒险重新定价。"
  },
  {
    "id": "wscn:3777280",
    "domain": "股票",
    "title": "五年来基金业最大创新，“主动股票ETF”究竟给基民带来了什么？",
    "url": "https://wallstreetcn.com/articles/3777280",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T02:10:37+00:00",
    "summary": "距离获批越来越近"
  },
  {
    "id": "wscn:3777277",
    "domain": "股票",
    "title": "美伊战火重燃，对冲基金凶猛加仓原油，速度创十年来最快",
    "url": "https://wallstreetcn.com/articles/3777277",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T01:47:30+00:00",
    "summary": "美伊冲突骤然升级，对冲基金以近十年最快速度狂押布伦特原油上涨——单周净多头激增逾7.5万手，创2016年来最大增幅。霍尔木兹海峡遭袭封堵叠加俄罗斯炼油设施受损，全球燃料供应双重收紧，炼油利润飙至历史高位。"
  },
  {
    "id": "wscn:3777276",
    "domain": "股票",
    "title": "“老登”逆袭！苹果短暂超越英伟达，成为全球最高市值公司",
    "url": "https://wallstreetcn.com/articles/3777276",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T01:22:48+00:00",
    "summary": "当英伟达因AI新模型Kimi K3冲击单日跌约2%，苹果却凭借\"不烧钱的AI逻辑\"悄然反超，短暂夺回全球市值第一。资本支出仅占销售额2.5%、新版Siri亮相、汇丰罕见上调买入评级……多重催化剂叠加，令苹果成为AI浪潮中最意外的避险赢家。"
  },
  {
    "id": "wscn:3777275",
    "domain": "股票",
    "title": "单周重挫10%、连续三周大跌，较高点回撤20%！“AI牛市龙头”经历“史上最大动量抛售之一”",
    "url": "https://wallstreetcn.com/articles/3777275",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T01:10:57+00:00",
    "summary": "费城半导体指数单周暴跌近10%，较6月高点累计回撤逾20%，正式进入技术性熊市。高盛将此定性为\"有记录以来最大规模的动量策略抛售之一\"。主因并非基本面恶化，而是对冲基金集中平仓\"做多半导体、做空云计算商\"这一年内最热配对交易，叠加台积电资本开支预警引发过度投资忧虑，抛售浪潮已席卷全球科技股。"
  },
  {
    "id": "wscn:3777268",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年7月18日",
    "url": "https://wallstreetcn.com/articles/3777268",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T23:19:49+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3777186",
    "domain": "股票",
    "title": "Kimi冲击美科技股，纳指100一度跌2.7%、收盘跌幅收窄，芯片股进入熊市，油价大涨",
    "url": "https://wallstreetcn.com/articles/3777186",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T22:50:26+00:00",
    "summary": "纳指、标普500均跌超1%。费城半导体指数下跌1.6%，较纪录高位累计回落20%，进入熊市区间。苹果涨0.14%、盘中市值一度回到第一。美股存储芯片指数本周跌超17%。当日闪迪跌3.99%，西部数据则涨2.23%。2年期美债收益率走高4基点。现货黄金先跌后涨，较日低点涨1.6%，重回4000美元。WTI原油上涨4.3%。"
  },
  {
    "id": "wscn:3777246",
    "domain": "股票",
    "title": "公开出售内幕消息？特朗普旗下Truth Social向华尔街推出付费API，“毫秒级”投递特朗普推文",
    "url": "https://wallstreetcn.com/articles/3777246",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T22:48:53+00:00",
    "summary": "特朗普旗下媒体公司TMTG宣布将于8月1日推出\"Truth API\"，出售特朗普Truth Social帖文的实时数据流，目标客户群体主要为算法交易机构。TMTG CEO预计该产品将成为\"持续收入来源。\"这一举动同时引发对公职行为变现的法律与伦理质疑。消息公布当日，公司股价一度下跌8.4%。"
  },
  {
    "id": "wscn:3777267",
    "domain": "股票",
    "title": "报道：美国考虑设立独立AI监管机构，对顶级AI模型进行安全审查",
    "url": "https://wallstreetcn.com/articles/3777267",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T22:48:40+00:00",
    "summary": "据媒体报道，美国财政部长贝森特参与制定提案，拟仿照金融业监管局模式，创建一个独立AI监管机构，由行业出资、向SEC负责，允许科技与金融界共同参与安全标准制定。此前硅谷抱怨美国政府限制尖端AI发布的措施缺乏一致性和透明度。"
  },
  {
    "id": "wscn:3777266",
    "domain": "股票",
    "title": "美军连续第七晚空袭伊朗，伊打击美在巴林无人艇、警告进入“全面进攻和摧毁”阶段",
    "url": "https://wallstreetcn.com/articles/3777266",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T21:57:01+00:00",
    "summary": "美军称，于美东时间周五下午对伊朗启动新一轮打击。伊朗军方同日称，利用岸基巡航导弹打击了印度洋一艘美军舰艇；打击并摧毁美军在巴林的无人艇存放基地。伊朗最高领袖军事顾问称，美伊谅解备忘录已名存实亡，若美方未来几天继续袭击，伊朗武装部队将跨越当前“威慑和报复”阶段，进入“全面进攻和摧毁”阶段。"
  },
  {
    "id": "wscn:3777265",
    "domain": "股票",
    "title": "SpaceX身陷股价破发泥潭之际，向五角大楼兜售数十亿美元AI算力",
    "url": "https://wallstreetcn.com/articles/3777265",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T21:56:48+00:00",
    "summary": "据媒体报道，SpaceX正与美国国防部谈判，拟签价值数十亿美元的算力供应协议，或成双方迄今最大商业合作。马斯克的政商关系再次置于舆论焦点之下，部分美国国家安全官员已公开表达对五角大楼过度依赖马斯克旗下服务的担忧。消息发出后，SpaceX股价盘中一度快速反弹，但随后继续下跌，最终收跌5.43%。"
  },
  {
    "id": "wscn:3777263",
    "domain": "股票",
    "title": "美股半导体指数跌入熊市，芯片股溃败时苹果盘中夺回市值第一，AI牛市迎来“换锚”时刻？",
    "url": "https://wallstreetcn.com/articles/3777263",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T21:14:49+00:00",
    "summary": "即便周四台积电交出超预期的财报，也未能阻止全球科技股进一步杀跌。周五，费城半导体指数较6月高位跌去20%；前两日跌超20%的SK海力士美股一度涨近10%，但未被视为整个行业重新走强信号。AI高估值资产被重估，SpaceX收跌超5%、连日跌破发行价，市值一个月蒸发超1万亿美元。"
  },
  {
    "id": "wscn:3777228",
    "domain": "股票",
    "title": "SpaceX市值蒸发超万亿！IPO后星舰首飞推迟，每一秒倒计时都成了\"公开财报\"",
    "url": "https://wallstreetcn.com/articles/3777228",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T21:11:32+00:00",
    "summary": "SpaceX星舰V3测试因发动机点火失败于发射前中止，计划下周初重新发射。这是SpaceX上市以来首次星舰试飞，市场对其技术进展高度敏感。SpaceX股价周五收跌5.43%，对应市值1.63万亿美元，较6月16日上市第三日收盘时2.64万亿美元的峰值已缩水逾1万亿美元。"
  },
  {
    "id": "wscn:3777262",
    "domain": "股票",
    "title": "美伊冲突跨越“民用红线”，霍尔木兹通行量降至三周低点，原油一周涨近16%",
    "url": "https://wallstreetcn.com/articles/3777262",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T20:53:00+00:00",
    "summary": "科威特指伊朗将袭击范围扩大至科威特的电力与海水淡化厂。伊拉克官员称，该国库尔德地区最大天然气田因面临遭袭的威胁而关闭，美军则将空袭目标延伸至距霍尔木兹海峡350英里以外的恰巴哈尔港。据伊朗消息，因未获伊朗许可企图穿越该海峡，一艘船周五遭伊方打击。美军称重启对伊封锁三天内拦截六船。"
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
    "id": "hn:48905958",
    "domain": "股票",
    "title": "IBM shares down 23% as clients spend more on hardware and memory chips",
    "url": "https://www.cnbc.com/2026/07/14/ibm-warns-second-quarter-earnings-fell-short-of-expectations.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-14T12:44:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48612095",
    "domain": "股票",
    "title": "Show HN: My Windows XP portfolio with working Game Boy and iPod",
    "url": "https://mitchivin.com/",
    "source": "mitchivin",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-06-20T19:18:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48634931",
    "domain": "股票",
    "title": "SpaceX Drops 14% in One Day, Price Now Below IPO Launch",
    "url": "https://finance.yahoo.com/quote/SPCX/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-06-22T19:33:55+00:00",
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
    "id": "hn:48787052",
    "domain": "股票",
    "title": "Elon Musk posted twice as often on UK race and immigration as about SpaceX IPO",
    "url": "https://www.theguardian.com/technology/2026/jul/04/elon-musk-uk-race-immigration-spacex-ipo",
    "source": "iamflimflam1",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-07-04T17:18:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48781228",
    "domain": "股票",
    "title": "After $18B IPO, Bending Spoons founder says success comes from minimizing luck",
    "url": "https://techcrunch.com/2026/07/01/after-18b-ipo-bending-spoons-founder-says-success-comes-from-minimizing-luck/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-03T23:31:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48598558",
    "domain": "股票",
    "title": "The average SpaceX buyer post-IPO is almost under water after two-day slide",
    "url": "https://www.cnbc.com/2026/06/18/the-average-spacex-buyer-post-ipo-is-almost-under-water-after-two-day-slide.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-06-19T13:48:28+00:00",
    "summary": ""
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
    "id": "hn:48824532",
    "domain": "股票",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48853145",
    "domain": "股票",
    "title": "California universities stockpiling AR-15s, grenades and submachine guns",
    "url": "https://www.theguardian.com/us-news/2026/jul/09/california-universities-military-equipment",
    "source": "sizzle",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-09T22:20:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48789829",
    "domain": "股票",
    "title": "Ask HN: When will the stock market crash?",
    "url": "https://news.ycombinator.com/item?id=48789829",
    "source": "roschdal",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-04T22:55:26+00:00",
    "summary": ""
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
    "id": "hn:48717469",
    "domain": "金融",
    "title": "The CEO of Mullvad is the main financer of the Swedish Örebro party",
    "url": "https://det.social/@lostgen/116820546568940358",
    "source": "Risse",
    "platform": "hackernews",
    "points": 695,
    "published_at": "2026-06-29T10:45:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48759634",
    "domain": "金融",
    "title": "PeerTube is a free, decentralized and federated video platform",
    "url": "https://github.com/Chocobozzz/PeerTube",
    "source": "doener",
    "platform": "hackernews",
    "points": 680,
    "published_at": "2026-07-02T11:17:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48634585",
    "domain": "金融",
    "title": "Canada plans 'nuclear renaissance' with up to 10 reactors built by 2040",
    "url": "https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509",
    "source": "geox",
    "platform": "hackernews",
    "points": 593,
    "published_at": "2026-06-22T19:06:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 489,
    "published_at": "2026-07-15T03:32:45+00:00",
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
    "id": "hn:48647444",
    "domain": "金融",
    "title": "Digital euro clears key hurdle as EU seeks to break free from U.S. credit cards",
    "url": "https://finance.yahoo.com/markets/currencies/articles/ecb-secures-key-parliamentary-backing-102718449.html",
    "source": "madars",
    "platform": "hackernews",
    "points": 232,
    "published_at": "2026-06-23T16:27:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673787",
    "domain": "金融",
    "title": "Federal agents track down woman, demand she remove Instagram post about ICE",
    "url": "https://www.syracuse.com/news/2026/06/federal-agents-track-down-syracuse-woman-demand-she-remove-instagram-post-about-ice.html",
    "source": "coloneltcb",
    "platform": "hackernews",
    "points": 217,
    "published_at": "2026-06-25T14:16:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48777266",
    "domain": "金融",
    "title": "International chess federation sanctions Kramnik",
    "url": "https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/",
    "source": "DarkContinent",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-07-03T17:04:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48892638",
    "domain": "金融",
    "title": "Benchmarking 15 “E-Waste” GPUs with Modern Workloads",
    "url": "https://esologic.com/benchmarking-tesla-gpus/",
    "source": "eso_logic",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-07-13T13:48:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48703613",
    "domain": "金融",
    "title": "Feds Killed Polestar and Spared Volvo",
    "url": "https://www.thedrive.com/news/feds-killed-polestar-and-spared-volvo-that-should-terrify-you",
    "source": "mraniki",
    "platform": "hackernews",
    "points": 175,
    "published_at": "2026-06-28T01:55:21+00:00",
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
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-07-18T00:28:46+00:00",
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
    "id": "hn:48783175",
    "domain": "金融",
    "title": "The LLVM Compiler Infrastructure",
    "url": "https://cacm.acm.org/federal-funding-of-academic-research/the-llvm-compiler-infrastructure/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-07-04T06:43:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48785077",
    "domain": "金融",
    "title": "The Fediverse Is Not the Way Forward",
    "url": "https://trialandfailure.net/the-fediverse-is-not-the-way-forward/",
    "source": "ExMachina73",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-04T12:53:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48653311",
    "domain": "金融",
    "title": "Prairieland defendants sentenced today to prison terms ranging from 30-100 years",
    "url": "https://prairielanddefendants.com/press-release/eight-federal-prairieland-defendants-sentenced-today-to-prison-terms-ranging-from-30-100-years-for-common-protest-activity/",
    "source": "panic",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-06-23T23:54:00+00:00",
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
    "id": "hn:48735748",
    "domain": "金融",
    "title": "Supreme Court takes sledgehammer to federal regulatory structure",
    "url": "https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure",
    "source": "marojejian",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-06-30T17:05:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-07-05T06:40:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48734220",
    "domain": "金融",
    "title": "Supreme Court strikes down limits on party spending in federal elections",
    "url": "https://apnews.com/article/supreme-court-campaign-finance-party-spending-ohio-91e49ee112197ae1210a9abfa46986ed",
    "source": "khriss",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-06-30T15:34:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756848",
    "domain": "金融",
    "title": "He sent a harsh email to ICE's top official. Federal agents tracked him down",
    "url": "https://www.npr.org/2026/07/01/nx-s1-5874124/dhs-tracks-ice-critic",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-07-02T05:20:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48609233",
    "domain": "金融",
    "title": "Big Tech is borrowing like never before",
    "url": "https://startupfortune.com/big-tech-is-borrowing-like-never-before-and-the-fed-just-made-that-a-lot-more-expensive/",
    "source": "krupan",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-06-20T13:49:15+00:00",
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
    "id": "hn:48678494",
    "domain": "金融",
    "title": "Feds deny Polestar authorization to sell cars in US from model year 2027",
    "url": "https://arstechnica.com/cars/2026/06/feds-deny-polestar-authorization-to-sell-cars-in-us-from-model-year-2027/",
    "source": "Quinner",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-06-25T20:00:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48780128",
    "domain": "金融",
    "title": "AI First: How the Federal Government Is Prioritizing AI over People and Planet",
    "url": "https://stopgreedbuildgreen.climateandcommunity.org/posts/ai-first",
    "source": "eatox",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-03T21:21:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48754128",
    "domain": "金融",
    "title": "US feds are actively hiring \"person who decides which models to ban\"",
    "url": "https://www.usajobs.gov/job/856265200",
    "source": "arm32",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-07-01T22:45:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48796110",
    "domain": "金融",
    "title": "Moving back home used to be a sign of failure. Now it shows financial savvy",
    "url": "https://www.wsj.com/lifestyle/relationships/living-with-parents-finances-0c35530c",
    "source": "apparent",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-07-05T17:34:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48723371",
    "domain": "金融",
    "title": "Feds Tracked Down an Anti-ICE Dad in NYC Hotel, but How?",
    "url": "https://gizmodo.com/federal-agents-reportedly-tracked-down-an-anti-ice-dad-in-a-new-york-hotel-its-not-clear-how-2000778714",
    "source": "ripe",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-06-29T18:42:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-09T17:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673197",
    "domain": "金融",
    "title": "Federating Clusters for Zero-Downtime Kubernetes",
    "url": "https://linkerd.io/2026/06/24/federating-clusters-for-zero-downtime-kubernetes/index.html",
    "source": "PagCatOli",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-06-25T13:37:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48613112",
    "domain": "金融",
    "title": "Dallas Fed: 30% of housing cost increase driven by unauthorized immigration [pdf]",
    "url": "https://www.dallasfed.org/~/media/documents/research/papers/2026/wp2607.pdf",
    "source": "silexia",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-20T21:25:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48677039",
    "domain": "金融",
    "title": "The AI Data-Center Boom Is Sparking a Third Wave of Inflation",
    "url": "https://www.wsj.com/economy/the-data-center-boom-is-sparking-a-third-wave-of-inflation-926adc6e",
    "source": "gmays",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-25T17:58:44+00:00",
    "summary": ""
  }
]
```
