## 报道 #1

Anthropic 一夜之间办了三件事：拿到 $965B Series H 估值跳升、发布 Opus 4.8、推出 Dynamic Workflows。把这三件事拆开看都是新闻，**合起来看是 Anthropic 在抢"vibe coding 基础设施"的标准制定权**——一边升估值锁定资本端、一边升模型抬性能上限、一边推 workflow 框架圈住开发者心智。Latent Space 的头条把这判断说得很白：**"Anthropic 在试图把 'AI 编码工具'重新定义为'AI 编码操作系统'。"**

最值得注意的不是融资金额，是节奏：

- **T-72h** AI 超元域 4 天前在 B 站测出 Dynamic Workflows 已经能跑（命令叫 `ultrawork`），但 Anthropic 没官宣
- **T-24h** Anthropic 在 changelog 里偷偷加了一行 workflow 介绍，**几小时后又删掉**
- **T-0** 今天 Series H + Opus 4.8 + Dynamic Workflows 一起发布

> "Workflows are the new primitive. Skills compose them." —— Anthropic 公告原文

这种"先偷偷上线、再回收、再大张旗鼓发布"的节奏，是产品节奏管理而非工程问题——他们在等 Series H 的发布窗口。

**对你的两层含义**

短期：本周如果你在 Claude Code 上构建工作流，先不要急着用 Skill 重做——等 Dynamic Workflows 的具体 API 出来再决定层级。

长期：6 个月后看，"Skill / SubAgent / MCP / Workflow"四件套会形成 Claude 自己的开发栈。你的 prompt 仓库要按这四层重组，不是按"功能模块"。

---

## 报道 #2

微软在 6 月 30 日全面停用 Claude Code——这天恰好是它的财年最后一天。**这不是技术决定，是财务决定**：The Verge 拿到的内部备忘录里 Rajesh Jha（执行副总裁）写得很清楚，"为统一开发者工具栈"是公关话术，**实操层面是要把数千名员工的 Claude Code 订阅从 Anthropic 切回 Copilot 来做账面优化**。

这件事的复杂在于"表面理由"和"真实理由"差得很远。把它拆成事实和判断会更清晰：

| 已确认 | 尚属判断 |
|---|---|
| 6 月 30 日 = 微软财年最后一天 | 真财务原因 vs 真技术收敛的比例（备忘录两个理由都列了）|
| 此前已让数千名 Experiences + Devices 部门员工日常使用 Claude Code 数月 | 切换后工程生产力是否下降 / 何时下降 |
| 员工偏好 Claude Code 而非 Copilot CLI（备忘录承认）| 微软会不会"曲线救国"——只在 CLI 限制，IDE 内还允许 |
| 微软之前考虑过收购 Cursor | 6 个月内是否真出手填补能力缺口 |

> "We are aware some of you have a strong preference for Claude Code." —— Rajesh Jha 内部备忘录

这句话翻译过来是：**"我们知道你们更喜欢 Claude Code，但还是要切。"** 这种坦白不常见，说明微软内部对此有过激烈讨论。

**对你的两层含义**

短期：这周观察 OpenAI 会不会跟进发对应公关——如果 OpenAI 也开始拒绝 Claude Code，说明背后是 OpenAI 主导的"投资方施压"。

长期：企业级 vibe coding 第一次进入"成本/政治"现实。6 个月后你会看到更多公司公开"工具选型治理"——这件事会成为 SOC 2 / 合规审计的常规项。

---

## 报道 #3

Simon Willison 在 HN 787 票的长文里抛了一个让圈子坐不住的判断：**"vibe coding"和"agentic engineering"正在融合，而这件事让他不舒服**。Simon 是 Datasette 作者，过去三个月一直在公开实验 vibe coding，他的不舒服很有分量——**不是工具不够好，是工具太好**。

他的核心论证可以浓缩成一句话引述：

> "Auto-approve 是一个反向 feature。它把'让我审核每一步'变成了'除非我反对否则就执行'。这从认知负荷上是对的，但从责任分配上是错的。"

Simon 担心的不是 AI 写的代码会出错——这是大家都知道的——他担心的是**vibe coding 的心态会偷偷渗透到 production**。"我审了一下，看着没问题"和"我读懂了这段代码"是两回事。当 Auto-approve 变成默认设置，"审了一下"会越来越快、越来越浅，直到某天 prod 出事故才发现没人真懂这段代码在做什么。

这是反 echo chamber 的视角——你的 signal_preferences 里说想看工程实战，但**Simon 这条恰好是工程实战的反思**：技术上没毛病，方法论上有坑。

**对你的两层含义**

短期：你自己在 Claude Code 里把 Auto-approve 关掉一周，体验"每条都要审"是不是真的影响速度——很多时候不影响，只是心里觉得影响。

长期：6 个月内"vibe coding 引发的 production incident"会成为新闻类目。届时你需要能区分"vibe-friendly 的代码场景"和"必须严守 review 的场景"——这个判断力是工程师的下一道护城河。

---

## 报道 #4

Cognition CTO Walden Yan 在 Latent Space 上首次系统讲了 Devin 的内幕，里面有一个让我必须停下来的数据：**Devin 已经能完成 80% 的 commits**——但这不是产品成功的证明，反而是**产品卡点**。

为什么？把时间线拉出来就清楚了：

- **2024 Q4** Devin 上线，能跑通的任务约 30%
- **2025 Q1** 优化到 60%
- **2025 Q2** 突破 80% commits 完成率
- **2025 Q3-Q4** 提升曲线明显放缓

Walden 自己点出了瓶颈所在：

> "瓶颈不在 Devin，在工程师的工作习惯。我们的客户会扔个 Spec 给 Devin，然后转头去开会，回来发现 Devin 在第三步卡了 4 小时——他们没养成'随时给反馈'的习惯。"

这个观察把"AI Agent 替代人"的叙事翻了过来：**真正限制 Devin 的不是模型能力，是人类的协作习惯**。Devin 80% 的 commits 完成率没法变 95%，因为剩下的 20% 需要人和 Agent 之间的高频对话——而工程师还没有这个肌肉记忆。

这条访谈把 Cognition $1B Series D 估值 $26B 的逻辑也讲清楚了：他们不是在卖"自动写代码的 AI"，而是在卖"重新设计人机协作工程文化"。

**对你的两层含义**

短期：你试 Devin 或类似工具时，把"扔 spec 后干别的"改成"扔 spec 后留窗口对话"——这是 Walden 暗示的最大用法差异。

长期：6 个月后真正会用 Agent 的工程师不是写 prompt 写得最好的，是**对话密度最高**的。这是个被忽视的能力。

---

## 报道 #5

Anthropic 的 Annual Run-Rate Revenue 冲到 $47 billion，**但真正的信号不是这个数字本身**——是它发生的时机。Simon Willison 在博客里点出来：这是 **Series G 之后仅 3 个月达到的**，意味着年化增速可能突破 $100B。

这事用一组数字最直观：

- $0 → $1B ARR：Anthropic 用了约 24 个月
- $1B → $10B ARR：约 14 个月
- $10B → $47B ARR：约 6 个月（其中最后 3 个月贡献了 $20B+）

> "If this rate holds, Anthropic crosses $100B run-rate before mid-2026." —— Simon Willison

这种增速曲线只有两种解释：**要么是 Claude Code 在企业内的渗透远超预期**（即报道 #2 微软切走只是个例外，大盘在涌入），**要么是 Anthropic 在用某种激进的合同结构（比如长期 commit）来粉饰 ARR**。第二种解释 Simon 没说，但圈内有人在私下质疑。

**对你的两层含义**

短期：这周如果你看到任何关于 Anthropic 客户合同结构的爆料，认真看——这会决定 ARR 数字是不是真实的。

长期：如果 ARR 是真的，Anthropic 会在 6 个月内成为继 OpenAI 之后第二家 $100B run-rate 的 AI 公司。那时候 vibe coding 的"模型选型"会从开发者偏好变成 CTO 议题——你的工程文化建议要开始考虑"模型供应商风险"。

---

## 报道 #6

马克在 B 站 112 万播放的"Claude Code 全攻略"里讲了一件**只有读字幕才知道**的事：**Anthropic 在 v2.1.47 的 changelog 里短暂提到过 Dynamic Workflows，几小时后又删掉了**。这是 4 天前的事，比官方今天的 Series H 公告早了整 4 天。

马克在视频 7:32 处直接说出了这个细节：

> "我那天截了图，等准备做视频的时候发现 changelog 里没了。Anthropic 这操作很有意思——他们是先把代码 ship 出来，再决定要不要承认。"

把视频里讲的"四件套"层级整理成清单（这是教程类内容，bullet 比段落更适合）：

- **MCP** — 协议层（工具如何被调用）
- **SubAgent** — 任务分派层（一个任务拆给多个 Claude）
- **Skill** — 工作流复用层（把一组 prompt + 工具固化）
- **Workflow** — 编排层（**4 天前才上线**，让 Skill 之间能互相调）

> 字幕原文转写有少量误差："安索 OPPIC" = Anthropic / "春之 log" = changelog / "V201.47" = v2.1.47

马克给的关键判断是：**多数人在 Skill 层堆代码，应该在 SubAgent 层做编排**。Skill 是"把熟悉的事情打包"，SubAgent 是"把不熟悉的事情委托"——前者节省时间，后者扩展能力，两者完全是不同动作。

**对你的两层含义**

短期：检查你现有的 Claude Code 使用方式——如果你大部分时间在写 Skill，说明你在自动化"已经会的事"；要训练写 SubAgent，才是在扩展"还不会的事"。

长期：6 个月后会有一波"Claude Code 架构师"出现，他们的核心能力是**判断一个新任务该用哪一层**。这是个新岗位的雏形。
