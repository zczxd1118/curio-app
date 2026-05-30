# Content Curator —— PRD v0.2

> **版本**：v0.2（多 Domain + 反馈闭环 + 个人画像）
> **作者**：周小丁
> **日期**：2026-05-29
> **状态**：M0 设计中
> **更新**：v0.1 → v0.2，吸收"个人雷达"日报模式启发，新增 Profile / Feedback / 频率字段

---

## 一、一句话定位

> **你给一个领域，Agent 自己决定订阅谁、推什么、什么时候推。**

从工具升级到 Agent —— 用户给"目标"（关注的领域），Agent 给"路径"（KOL 列表 + 周报推送）。

---

## 二、目标用户

M0 单机自用，M2 后预留多用户能力。

| 用户类型 | 占比 | 痛点 |
|---|---|---|
| 信息焦虑型 | 50% | 不想刷 B 站/小宇宙，但又怕错过新知 |
| 多领域学习者 | 30% | 同时关注 AI / 投资 / 产品 |
| 创作者 | 20% | 需要素材但不想自己挖 |

代表用户：周小丁（电子信息工程大四 + 搜狗实习），用 vibe coding 跟踪一个新领域。

---

## 三、核心价值（vs 已有方案）

| 方案 | 不足 | content-curator 的差异 |
|---|---|---|
| 张咋啦 Newsletter Skill | 工具，需手动配置 | **Agent 主动决策** |
| Refind / Particle | 闭源、信源固定 | **开源、AI 自选 KOL** |
| content-catcher（自有）| 需手填 channels.yaml | **AI 自动生成** |
| RSS 阅读器 | 只是聚合 | **打分 + 推荐理由** |

差异化关键词：**目标驱动 / Agent 决策 / 可解释 / 复用底座**

---

## 四、产品架构

### 4.1 三层结构

```
┌──────────────────────────────────────┐
│   Web UI（M0 wireframe）             │ ← 用户用的壳
│   极简 Linear/Notion 风、深色        │
├──────────────────────────────────────┤
│   API 层（FastAPI，M1 实现）         │ ← 前后端契约
│   /topics  /kols  /weekly  /agent    │
├──────────────────────────────────────┤
│   Agent 大脑（M0 = WorkBuddy 手动）  │ ← 决策逻辑
│   topic→KOL / 内容打分 / 推荐理由    │
├──────────────────────────────────────┤
│   content-catcher（已有）            │ ← 工具底座
│   抓取 / 转写 / 渲染 / 邮件          │
└──────────────────────────────────────┘
```

### 4.2 部署目标

- **M0**：纯前端 mockup（HTML + Tailwind），数据全 mock，跑得动浏览器就行
- **M1**：FastAPI 后端 + 本地 SQLite，前端调真接口
- **M2**：周报定时任务（cron / APScheduler）
- **M3**：Docker 一键启动；后续可考虑 Vercel + Supabase 上云

---

## 五、核心数据模型（M0 即定义清楚）

四级订阅结构：**Domain → Topic → KOL → Content**
两个独立资产：**Profile（个人画像）** 与 **Feedback（反馈记录）**

```
Profile（个人画像）—— 全局唯一，跨 Domain
├── id              "me"（M0 单用户）
├── identity        "电子信息工程大四 + 搜狗实习生 + AI 重度用户"
├── interests       ["vibe coding", "AI Agent", "美联储动向", ...]
├── dislikes        ["纯流量号", "标题党", "口水内容"]
├── signal_preferences  ["要工程实践细节", "要看到代码/示例", "拒绝玄学"]
├── reading_pace    "工作日 30 分钟，周末 2 小时"
├── updated_at
└── auto_updated_from_feedback  bool   ← M1 反馈闭环开关

Feedback（反馈记录）—— Digest 维度
├── id
├── digest_id
├── content_id      可选，针对单条内容
├── kind            useful / boring / wrong_topic / want_more
├── note            自由文本"这周 XX 有点水，想多看 YY"
└── created_at

Domain（领域）—— 用户聚焦的高层赛道
├── id              "finance" / "ai" / "semiconductor"
├── name            "金融" / "AI" / "半导体"
├── icon            🏦 / 🤖 / 🔬
├── description
├── source          preset / custom（M0 仅 preset）
├── color           tag 配色
├── frequency       daily / weekly                ← Domain 默认推送频率
├── topics          [Topic.id]
├── created_at
└── status          active / paused

Topic（主题）—— Domain 下的具体关注点
├── id              "macro-fed" / "vibe-coding" / "advanced-process"
├── name
├── description
├── domain_id       "finance"
├── subtopics       ["美联储议息", ...]
├── frequency       inherit / daily / weekly      ← 默认继承 Domain
├── kols            [KOL.id]
├── created_at
└── status          active / paused

KOL —— 跨 Domain 复用
├── id              "bilibili-25752587"
├── name            "大牙大-"
├── platform        bilibili / youtube / podcast_rss / xiaoyuzhou
├── platform_id
├── avatar_url
├── recommend_reason
├── style           教程 / 评论 / 访谈 / 资讯
├── trust           1-5
├── id_confidence   high / medium / low
├── lang            zh / en
├── topics          [Topic.id]
└── subscribed      bool

Content（单条内容）
├── id
├── kol_id
├── topic_ids       [Topic.id]
├── domain_ids      [Domain.id]
├── title
├── url
├── published_at
├── duration_sec
├── summary
├── score           必读 / 参考 / 跳过
├── score_detail    {新颖度, 深度, 相关度} (1-10)
└── why_recommend

Digest（推送）—— 兼容日报和周报
├── id              "2026-05-29-ai-daily" / "2026-W22-finance-weekly"
├── frequency       daily / weekly                ← 关键字段
├── scope           domain / topic
├── scope_id        "ai" / "vibe-coding"
├── period          单日或一周
├── must_read       [Content.id]
├── reference       [Content.id]
├── skip            [Content.id]
├── intro           Agent 写的开场白
├── feedback_section_md  反馈区 placeholder（用户填，下次跑读取）
├── feedback_ids    [Feedback.id]                 ← 收回的反馈
├── sent_at
└── opened          bool
```

### 5.1 关键设计决策

1. **Profile 是 Agent 的"灵魂"**：不是简单的偏好开关，而是一段自然语言画像，AI 推 KOL / 打分时全程参考
2. **Feedback 不替换偏好**：反馈是**输入信号**，Profile 是**沉淀状态**。M1 自动从最近 4 周反馈摘要回写到 Profile
3. **Digest 兼容日/周报**：用 `frequency` 字段切换，避免做两套数据结构
4. **Domain 设默认频率，Topic 继承**：金融可设 daily（盘前要快），AI 设 weekly（深度内容）
5. **KOL 跨 Domain 复用**：一个 KOL（如黄仁勋）可同属 AI + 半导体，抓内容只抓一次
6. **预置 vs 自定义 Domain**：M0 锁 3 个 preset；M1 放开自建

---

## 六、信息架构（IA）—— 6 页 + 全局 Domain 切换

### 6.1 全局布局：左侧 Domain 切换栏 + 主体内容

```
┌──┬───────────────────────────────────────────────────┐
│🏦│  ← 左侧 Domain 侧边栏                              │
│🤖│                                                    │
│🔬│  主体内容区（路由内容）                            │
│➕│                                                    │
│  │                                                    │
│👤│  ← 底部：个人画像入口                              │
│⚙ │                                                    │
└──┴───────────────────────────────────────────────────┘
```

切换 Domain 时主体刷新；点底部 👤 进 Profile。

### 6.2 6 页地图

```
┌──────────────────────────────────────────────────────┐
│  / 首页 Dashboard                                     │
│  └─ 当前 Domain Topic 卡片 + 本日/本周精选 + 跨 Domain │
└────┬───────┬───────┬─────────────┬──────────┬────────┘
     │       │       │             │          │
     ▼       ▼       ▼             ▼          ▼
  /explore /topic/:id /kol/:id  /digest/:id  /profile
  探索流   主题看板   KOL 详情    Digest      个人画像
                                  (日/周)     (新增)
```

### 6.3 六页职责

| 页面 | 路径 | 职责 | 关键交互 |
|---|---|---|---|
| **Dashboard** | `/` | 当前 Domain 概览 + 今日/本周精选 + 跨 Domain 提示 | 切 Domain；点 Topic 卡；探索新主题 |
| **Explore** | `/explore` | 输入主题 → AI 推子话题 + KOL → 勾选创建 Topic | Domain 上下文带入；Loading；KOL 候选 |
| **Topic 看板** | `/topic/:topicId` | 一个 Topic 全貌：KOL + 内容流 + Digest 历史 + **频率设置** | Tab 切；管理订阅；切 daily/weekly |
| **KOL 详情** | `/kol/:kolId` | 单 KOL 元信息 + 历史内容 + 多 Domain 归属 | 取消订阅；查看跨 Domain 复用 |
| **Digest（推送）** | `/digest/:digestId` | 一份日报或周报：必读/参考/跳过 + Agent 开场白 + **反馈区** | 跳原链接；填反馈；切粒度 |
| **Profile（个人画像）** | `/profile` | 你是谁、你关心什么、你看不上什么、你的反馈历史 | 编辑画像；查看 AI 摘要的最近反馈 |

### 6.4 用户主旅程（金线）

```
1. 首次打开 → / Dashboard，默认选中第一个 Domain
   └─ 看到当前 Domain Topic 卡片墙

2. 切 🏦 金融 Domain → 看到本日 Digest（金融默认 daily）

3. 加新方向 → /explore?domain=ai
   └─ 输入 "vibe coding" → 让 Agent 思考

4. AI 推 4 子话题 + 7 KOL → 勾 3 个 → 创建 Topic
   └─ 跳转 /topic/vibe-coding，提示"Agent 正在抓本周内容"

5. 看 Digest /digest/2026-W22-ai-vibe-coding
   └─ 末尾反馈区填："想多看 Claude Code 实战，少看抽象方法论"

6. 下次跑前 Agent 读这段反馈 → 调整本次推送

7. 路过 /profile → 看到 AI 已把上面那段反馈摘要到画像里
```

### 6.5 多 Domain × 频率心智

- **每个 Domain 是独立工作区**，独立频率
- **跨 Domain 提示**：Dashboard 顶部偶尔显示"🔬 半导体本周有 5 条必读 →"
- **频率混搭**：金融 daily（盘前要快） / AI weekly（深度） / 半导体 weekly

---

## 七、关键页面字段细节

### 7.1 Dashboard `/`

```
┌──┬──────────────────────────────────────────────┐
│🤖│  AI · Dashboard                       ⚙️     │
│✓ │ ──────────────────────────────────────────── │
│🏦│  🤖 AI · 3 Topics · 12 KOL · 本周 22 条      │
│🔬│                                                │
│➕│  📚 Topics in AI                              │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌──────┐   │
│  │  │vibe    │ │大模型   │ │AI 工程 │ │+新主│   │
│  │  │coding  │ │评测     │ │实践    │ │ 题  │   │
│  │  │5KOL/8 │ │3KOL/6 │ │4KOL/8 │ │     │   │
│  │  └────────┘ └────────┘ └────────┘ └──────┘   │
│  │                                                │
│  │  ✨ 本周必读（3）                              │
│  │  ─ Claude Code 1.0 实战 by 大牙大              │
│  │  ─ Cursor 0.50 vs Windsurf by Matthew          │
│  │  ─ Latent Space 访谈 swyx 谈 vibe coding       │
│  │                                                │
│  │  💡 跨 Domain 提示                            │
│  │  🏦 金融 Domain 本周有 5 条必读 →             │
│  │  🔬 半导体 Domain 本周有 8 条新内容 →         │
│  │                                                │
│  │  📨 最新周报：AI · 2026-W22                    │
│  └──────────────────────────────────────────────┘
└──┴──────────────────────────────────────────────┘
```

字段：
- 左侧 Domain 栏：emoji + 选中态高亮 + 红点提示有未读
- 顶部当前 Domain 标题：`{icon} {name}` + 统计
- Topic 卡片：`name` / `kol_count` / `unread_count`
- 本周必读：当前 Domain 内 score=必读 的前 3 条
- 跨 Domain 提示：仅当其它 Domain 有显著内容时才显示

### 7.2 Explore `/explore?domain={domain}` — **M0 演示重点**

```
┌─────────────────────────────────────────┐
│ ← 返回                                   │
│ 当前 Domain：🤖 AI                       │ ← Domain 上下文
├─────────────────────────────────────────┤
│                                          │
│   在 AI 领域下添加新主题                 │
│   ┌─────────────────────────────────┐   │
│   │ vibe coding                  ↵ │   │ ← 大输入框
│   └─────────────────────────────────┘   │
│   示例：AI Agent / 大模型评测 / MCP      │ ← 示例随 Domain 变
│                                          │
│   [让 Agent 思考 →]                      │
│                                          │
└─────────────────────────────────────────┘

       ↓ 点击后，Loading 3 步 4.5s

┌─────────────────────────────────────────┐
│ ✨ 新主题：vibe coding（隶属 🤖 AI）       │
│                                          │
│ 🧭 子话题（4）                           │
│  • AI 编程助手实战                        │
│  • 自然语言开发流程                        │
│  • Side Project 工作流                    │
│  • Agent 工具构建                          │
│                                          │
│ 👥 推荐 KOL（7）—— 勾选要订阅的           │
│ ┌─ ☑ 大牙大-                  [B站] ★★★★★│
│ │   Claude Code 实战派               ✅   │
│ ├─ ☑ Latent Space         [RSS 播客] ★★★★★│
│ │   AI 工程师最深度访谈            ✅   │
│ ├─ ☐ 张咋啦                  [B站] ★★★★ │
│ │   Newsletter 工作流参考标杆      ❓   │
│ └─ ... (其余 4 条)                       │
│                                          │
│  已选 2/7    [创建主题 →]                │
└─────────────────────────────────────────┘
```

字段细节：
- 输入框：placeholder、最大长度 50、回车提交
- Domain 上下文带入 prompt（"在 AI 领域下推荐 KOL"），AI 推得更精准
- Loading 态：3 步进度，每步 1.5s
- KOL 卡：name / platform 标签 / 信任星 / id_confidence 角标 / 推荐理由
- 底部 sticky 操作栏：「已选 N/M」+「创建主题」按钮

### 7.3 Topic `/topic/:topicId`

```
┌─────────────────────────────────────────┐
│ vibe coding                  [⚙ 管理]   │
│ 4 子话题 · 3 KOL · 22 条内容            │
├─────────────────────────────────────────┤
│ [KOL]  [内容流]  [周报历史]              │ ← Tab
├─────────────────────────────────────────┤
│ (默认 Tab = 内容流)                      │
│                                          │
│ 📅 今天                                  │
│ ─ 必读 ┐ Claude Code 1.0 by 大牙大      │
│         │ 30 分钟 · 因为提到了重大功能 │
│ ─ 参考 ┐ Cursor 测评 by Matthew Berman  │
│                                          │
│ 📅 昨天                                  │
│ ─ 跳过 ┐ AI Daily Brief 5/28           │
│         │ 因为重复昨天讨论过的话题      │
│ ...                                      │
└─────────────────────────────────────────┘
```

### 7.4 KOL 详情 `/kol/:kolId`

简洁卡片 + 该 KOL 在本平台的最新 5 条内容 + "在哪些主题被订阅"。

### 7.5 Digest（推送）`/digest/:digestId`

```
┌─────────────────────────────────────────┐
│ 📨 AI Domain · 周报 2026-W22 [日报↔周报] │
│ 2026 年 5 月 25 日 - 5 月 31 日          │
├─────────────────────────────────────────┤
│ 🤖 Agent 开场（基于你的画像）：          │
│ "本周 vibe coding 圈最大事件是 Claude    │
│  Code 1.0 发布。考虑到你最近反馈想多看   │
│  实战，我把 5 条工程实践放在了必读区。"  │
│                                          │
│ ━━━━━ 必读（3）━━━━━                  │
│ 1. Claude Code 1.0 实战  by 大牙大       │
│    🔗 32:14 / B 站                       │
│    💡 完整演示了 5 个新指令              │
│ ...                                      │
│                                          │
│ ━━━━━ 参考（5）━━━━━                  │
│ ━━━━━ 跳过（14）━━━━━ (折叠)          │
│                                          │
│ ━━━━━ 📝 你的反馈（M1 启用）━━━━━       │
│ 这周整体怎么样？想多看什么 / 少看什么？   │
│ ┌─────────────────────────────────┐    │
│ │ 想多看 Claude Code 实战，少看    │    │
│ │ 抽象方法论...                    │    │
│ └─────────────────────────────────┘    │
│ [提交反馈]                                │
│ Agent 会在下次 Digest 前读这段，并把摘要 │
│ 同步到你的画像                           │
└─────────────────────────────────────────┘
```

字段：
- 顶部右侧切换 daily/weekly 粒度
- Agent 开场白引用 Profile（"考虑到你最近反馈..."）
- 反馈区 M0 静态展示，M1 真生效

### 7.6 Profile（个人画像）`/profile` —— 新增页

```
┌──┬──────────────────────────────────────────────┐
│🤖│  👤 你的画像                          [编辑] │
│🏦│ ──────────────────────────────────────────── │
│🔬│                                                │
│➕│  🎭 身份                                       │
│  │  电子信息工程大四 + 搜狗实习 + AI 重度用户     │
│👤│                                                │
│✓ │  🎯 你关心的                                   │
│⚙ │  vibe coding · AI Agent · 美联储动向 ·         │
│  │  半导体国产替代 · 个股研究                     │
│  │                                                │
│  │  🚫 你看不上的                                 │
│  │  纯流量号 · 标题党 · 口水内容                  │
│  │                                                │
│  │  ⚙️ 你想要的信号                                │
│  │  • 要工程实践细节                              │
│  │  • 要看到代码/示例                              │
│  │  • 拒绝玄学论调                                 │
│  │                                                │
│  │  📚 你的节奏                                   │
│  │  工作日 30 分钟 · 周末 2 小时                  │
│  │                                                │
│  │  🔄 最近反馈摘要（M1 自动从 Digest 反馈摘出）   │
│  │  [05-29] 想多看 Claude Code 实战               │
│  │  [05-22] 半导体太多概念股，想多看技术          │
│  │  [05-15] 美联储口径解读已饱和，少推              │
│  │                                                │
│  │  [Agent 自动更新 ☑]                           │
│  └──────────────────────────────────────────────┘
└──┴──────────────────────────────────────────────┘
```

字段：
- 5 个画像分组：身份 / 关心 / 看不上 / 想要的信号 / 节奏
- 反馈摘要时间线（M1 起填充）
- "Agent 自动更新" 开关：开启后 Agent 从 Feedback 摘要回写画像

---

## 八、M0 边界（不做清单）

| 功能 | 何时做 |
|---|---|
| 账号 / 鉴权 / 多用户 | M2+ |
| 真后端 API | M1 |
| 真实抓取（接 content-catcher）| M1 |
| Topic 编辑 / 删除（M0 只做创建）| M1 |
| 用户自建 Domain（M0 仅 3 预置）| M1 |
| **反馈闭环真生效**（M0 静态画反馈区）| **M1**（提前到 M1）|
| **Profile 编辑生效**（M0 静态展示）| **M1** |
| **Digest 频率字段真生效**（M0 mock 静态展示）| **M1** |
| KOL 反馈学习直接调权重 | M3+ |
| 移动端响应式 | M2 |
| 国际化 | 暂无 |
| 付费 / 配额 | 永远不做 |

---

## 九、M0 mock 数据集

3 预置 Domain × 多 Topic × 多 KOL × 多 Content + 1 份 Profile + 多份 Digest（覆盖日报和周报）。

| Domain | 频率 | Topics | KOL | Content | Digest mock |
|---|---|---|---|---|---|
| 🤖 AI | weekly | vibe coding / 大模型评测 / AI 工程实践 | 12 | 22 | 1 周报 |
| 🏦 金融 | daily | 宏观经济与美联储 / 港美股研究 / A股投资 | 8 | 15 | 2 日报 |
| 🔬 半导体 | weekly | 先进制程 / GPU 算力 / 国产替代 | 6 | 12 | 1 周报 |

Profile mock：身份 + 5 关心 + 3 看不上 + 3 信号偏好 + 节奏 + 3 条反馈摘要时间线。

详细 mock 由 `web/mock-data.js` 提供。

---

## 十、M0 验收标准

1. PRD v0.2 答清楚 5 个核心问题（who / what / why / how / boundary）
2. 6 页 wireframe 在浏览器可点击跳转，hash 路由
3. 左侧 Domain 切换栏可切换 3 个预置 Domain，主体内容刷新
4. 6 页都有可点的入口（Dashboard / Explore / Topic / KOL / Digest / Profile）
5. mock 数据走通"AI Domain 探索 vibe coding → 勾 3 KOL → 看周报 → 写反馈"完整链路
6. Digest 页支持日报/周报切换展示（金融 daily / AI weekly）
7. Profile 页静态展示画像 + 反馈摘要时间线
8. 视觉风格符合极简 Linear/Notion 调性
9. 有空状态 / loading 态 / 已订阅态 三种状态展示

---

## 十一、北极星问题

1. AI 推 KOL 不准时怎么反馈？是否需要"重新推"按钮？
2. 同 KOL 多 Topic 订阅，重复内容怎么去重？
3. Topic 跨 Domain 移动 / 合并 / 拆分？
4. Domain × Topic 数量上限？
5. 频率混搭后，跨 Domain 提示在 Dashboard 怎么不抢戏？
6. Profile 完全自然语言 vs 结构化字段 —— 哪种 AI 更稳定？
7. 反馈摘要回写画像 —— 频率是每条反馈触发，还是每周一次？

---

## 十二、里程碑

| 阶段 | 目标 | 投入 |
|---|---|---|
| **M0** ← 当前 | PRD v0.2 + 6 页 HTML wireframe（可点击）| 今天 3-4h |
| **M1** | FastAPI 后端 + Domain/Topic/KOL CRUD + 接 content-catcher + **反馈闭环 + Profile 真生效 + 频率分桶** | 周末 1-2 天 |
| M2 | Digest 生成 + 邮件 + 定时任务 + 用户自建 Domain | 周末 1 天 |
| M3 | 打磨 + 故事（GitHub README + 小红书）| 周末 1 天 |

---

## 十三、附：CLI 版历史

M0 上半场（CLI demo）已完成，详见 `PRD.cli-v0.md` 与 `curator.py`。
CLI 不会废弃，定位为"Agent 大脑的命令行手动入口"，可与 Web 版并存。
