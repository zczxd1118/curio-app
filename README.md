# Curio · 趋势雷达

> **AI 信息策展 SaaS** —— 你选感兴趣的领域，Curio 每天/每周给你出一份"主编已读过、双语对照、带主编点评"的简报，邮件直接送到。
>
> 主站：**[curioradar.fun](https://curioradar.fun/)** · API：[api.curioradar.fun](https://api.curioradar.fun/health)
>
> 当前版本：**v0.9（2026-05-31）** · 真正对外开放的 SaaS

---

## 这是什么

Curio 是一个**信息策展 AI Agent**。你只用一句话告诉它"我关心金融、AI、半导体"，它替你做四件事：

1. **抓**：从 HackerNews / Stratechery / 华尔街见闻 / SemiAnalysis / Latent Space / B 站 等 30+ 信源自动抓取最新内容
2. **筛**：用 Claude 当主编打分（新颖度 / 深度 / 相关度），淘汰广告党、标题党、机翻列表
3. **写**：每条头版 = 中文标题 + 关键词 chips + 中文事实摘要 + 主编点评 + 可折叠英文原文
4. **推**：通过邮件按 daily / weekly 节奏送到订阅者邮箱（自有域名 noreply@curioradar.fun，DKIM/SPF 验证）

订阅者只需输邮箱 + 选领域 + 选频率，剩下的 Agent 全包。

---

## 当前线上状态

| 项 | 地址 / 状态 |
|---|---|
| 主站 | https://curioradar.fun（自有域名 + HTTPS Let's Encrypt） |
| API | https://api.curioradar.fun（Cloudflare Worker，全球 CDN，国内可用） |
| 邮件发件人 | `Curio <noreply@curioradar.fun>`（Resend Verified） |
| 4 个内置领域 | 🤖 AI（周刊）· 🏦 金融（日报）· 🔬 半导体（周刊）· 🏛️ 大厂讯息（日报） |
| 已订阅人数 | 1（产品作者，运营中） |
| 历史期数 | 8 期 markdown 已生成 |

试一下：[curioradar.fun](https://curioradar.fun/) 点订阅按钮 → 输你的邮箱 → 选领域 → 1 分钟内收到验证邮件。

---

## 核心架构

```
┌────────────────────────────────────────────────────────────────────────┐
│                     生成侧（绑本机 Mac，每天/每周自动跑）                │
│                                                                        │
│  WorkBuddy automation cron                                             │
│      ├── 每天 12:00 · daily（金融 + 大厂）                               │
│      ├── 每周一 12:00 · weekly（AI + 半导体）                            │
│      └── 每小时 · 用户"立刻生成"请求处理                                  │
│           ↓                                                            │
│  cli_generate.py prepare                                               │
│      ├── 拉 GitHub Issue 反馈 → profile.yaml                            │
│      ├── 30+ 信源抓候选（HN/RSS/华尔街见闻 API/B 站/...）                  │
│      └── 输出 score-prompt.md                                           │
│           ↓                                                            │
│  Claude（通过 WorkBuddy）打分 → scored.json                              │
│           ↓                                                            │
│  cli_generate.py prepare_notes → 写中文主编点评 prompt                    │
│           ↓                                                            │
│  Claude 写 editor_notes.json                                           │
│           ↓                                                            │
│  cli_generate.py finalize                                              │
│      ├── build_issue_md（统一 daily/weekly 模板）                         │
│      ├── render_site → site/                                           │
│      ├── push curio-site → GitHub Pages                                │
│      ├── push_content → Cloudflare KV                                  │
│      └── /broadcast → Resend 群发订阅者                                  │
└────────────────────────────────────────────────────────────────────────┘
                ↓                       ↓
         ┌──────────────────┐   ┌────────────────┐
         │ Cloudflare       │   │ GitHub Pages   │
         │ - Worker (V8)    │   │ curio-site repo│
         │ - KV (订阅/内容)  │   │ → curioradar.fun│
         │ - DNS Resend     │   │                │
         └──────────────────┘   └────────────────┘
                ↑                       ↑
         ┌──────────────────────────────────┐
         │       公网用户（任何设备）         │
         │  · 浏览器看简报                    │
         │  · 订阅 / 加领域 / 删领域 / 立即生成│
         │  · 邮件收日报/周刊                 │
         │  · 一键退订（无需 token）          │
         └──────────────────────────────────┘
```

**关键设计**：用户侧（订阅、网页、邮件）100% 跑在云端不依赖你电脑。只有"生成新一期"必须本机跑（用 WorkBuddy + Claude，不付外部 API 费）。

---

## 项目结构

```
content-curator/
├── README.md                  ← 本文档
├── BACKUP.md                  ← 跨设备备份与恢复手册
├── PRD.v0.2-subscribe.md      ← 订阅功能 PRD
│
├── cli_generate.py            ← 主入口：prepare / prepare_notes / finalize / process_pending
├── curator.py                 ← 老链路（被 cli_generate 包装）：search / score / digest
├── server.py                  ← 本地反馈服务器（已被 Cloudflare Worker 取代，留作备用）
│
├── sources.yaml               ← 30+ 信源注册表（按领域 + topic 组织）
├── profile.yaml               ← 你的偏好画像 + feedback_timeline
│
├── agent/                     ← Agent 核心模块
│   ├── build_issue_md.py      ← 统一 daily/weekly md 生成器（中文标题+chips+双语+主编点评）
│   ├── render_site.py         ← markdown → HTML，含订阅/加领域/删领域/立即生成 UI
│   ├── auto_sources.py        ← 新加领域自动配同等优质信源（9 类领域分类）
│   ├── search_bilibili.py     ← B 站搜索抓取
│   ├── fetch_hackernews.py    ← HN 关键词搜索
│   ├── fetch_rss.py           ← 通用 RSS 抓取
│   ├── fetch_wallstreetcn.py  ← 华尔街见闻 API（自定义 fetcher，含政治敏感词过滤）
│   ├── fetch_article.py       ← trafilatura 全文抓取
│   ├── fetch_subtitle.py      ← B 站字幕抓取
│   ├── ingest_feedback.py     ← GitHub Issue 反馈 → profile.yaml
│   ├── worker_sync.py         ← Worker 通信（订阅/广播/加领域/删领域 ingest）
│   └── notify_email.py        ← 自用邮件通知
│
├── prompts/                   ← LLM prompt 模板
│   ├── score_content.md       ← 主编评分（输出 title_zh / keywords / summary_zh）
│   ├── editor_note.md         ← 主编点评写作
│   ├── write_article.md       ← 报道写作（M2 用）
│   └── write_editorial.md     ← 社论写作
│
├── topics/                    ← 每个领域的中间产物 + 历史期数
│   ├── {slug}.candidates.json     ← 抓回的原始候选
│   ├── {slug}.scored.json         ← Claude 评分结果
│   ├── {slug}.editor_notes.json   ← Claude 写的主编点评
│   └── {slug}.weekly.YYYY-MM-DD.md ← 最终成品（daily/weekly 共用此命名）
│
├── site/                      ← 渲染后的静态网站（独立 git 仓库 → curio-site）
│
├── worker/                    ← Cloudflare Worker
│   ├── src/index.js           ← 10 个 endpoint（health/subscribe/confirm/unsubscribe/
│   │                              unsubscribe-by-email/domains/admin-*/broadcast）
│   ├── wrangler.toml          ← CF 部署配置
│   └── .dev.vars              ← 本地开发用 secrets（gitignored）
│
└── scripts/                   ← 跨设备备份恢复
    ├── secrets-manifest.txt   ← 绑本机资产清单
    ├── backup.sh              ← 加密备份（openssl AES-256-CBC）
    ├── backup_and_push.sh     ← 一键备份 + push private 仓库（推荐日常用）
    └── setup_new_device.sh    ← 新设备一键恢复
```

---

## 用户视角

直接打开 [curioradar.fun](https://curioradar.fun/)：

| 操作 | 入口 |
|---|---|
| **订阅** | 右下角浮窗按钮 → 邮箱 + 多选领域 + 选 daily/weekly → 收确认邮件 → 点确认 |
| **加领域** | 主页"添加新领域"卡片 → GitHub Issue → 1 小时内自动入库 |
| **删领域** | hover 领域卡 → 右上角 ✕ → GitHub Issue → 1 小时内自动删 + 订阅者退订 |
| **立刻生成** | hover 领域卡 → "⚡ 立刻生成" → GitHub Issue → 最长 60 分钟内出新一期 |
| **退订** | 邮件页脚链接 / 直接访问 [api.curioradar.fun/unsubscribe-by-email](https://api.curioradar.fun/unsubscribe-by-email) |
| **反馈** | 简报底部"有用 / 一般 / 偏了" + 备注 → GitHub Issue → 下次生成会读 |

---

## 作者视角（手工触发一次）

```bash
cd /Users/zoezczhou/WorkBuddy/2026-05-29-15-27-22/content-curator
PY=/Users/zoezczhou/.workbuddy/binaries/python/envs/curio_sys/bin/python

# 阶段 1：抓数据 + 出 LLM prompt
$PY cli_generate.py prepare

# 阶段 2：交给 Claude 写 scored.json（在 WorkBuddy 对话里跑）

# 阶段 2.5：抓正文 + 出主编点评 prompt
$PY cli_generate.py prepare_notes

# 阶段 2.6：交给 Claude 写 editor_notes.json

# 阶段 3：拼装 + 渲染 + push GitHub + 邮件 + worker 群发
$PY cli_generate.py finalize --cadence daily   # 或 --cadence weekly
```

平时不用手动跑——**3 条 WorkBuddy automation 自动调度**：

| Automation | 触发 | 用途 |
|---|---|---|
| `automation-1780211294404` | 每天 12:00 | daily（金融 + 大厂讯息） |
| `automation-1780140880021` | 每周一 12:00 | weekly（AI + 半导体） |
| `automation-1780167898607` | 每小时 | 处理用户的"立刻生成"请求 |

---

## 跨设备备份与恢复

详见 [`BACKUP.md`](BACKUP.md)。要点：

### 第一次设置（已完成）
1. `bash scripts/backup.sh` 生成加密备份（密码存 macOS 锁定备忘录）
2. 加密 `.enc` 文件存 [zczxd1118/curio-secrets](https://github.com/zczxd1118/curio-secrets) Private 仓库

### 日常备份（一行）
```bash
bash scripts/backup_and_push.sh
```
自动做：加密备份 → mv 到 `~/curio-secrets/` → git push（自动保留最近 12 份）

### 换设备恢复（30 分钟）
```bash
brew install git openssl gh
gh auth login
git clone https://github.com/zczxd1118/curio-app.git /tmp/bootstrap
gh repo clone zczxd1118/curio-secrets ~/curio-secrets
cd /tmp/bootstrap
bash scripts/setup_new_device.sh ~/curio-secrets/curio-backup-*.tar.gz.enc
```

恢复脚本会：解密 + clone curio-app + 还原 secrets/topics/缓存 + 创 venv + 装包 + 灌回 3 条 WorkBuddy automation + 烟测。

---

## 主要技术栈

| 层 | 技术 | 备注 |
|---|---|---|
| 调度 | WorkBuddy automation（本地 SQLite cron） | 绑本机 |
| LLM | Claude（通过 WorkBuddy 调度） | 不付外部 API 费 |
| 数据抓取 | trafilatura / feedparser / B 站 API / HN API / 自定义 fetcher | Python |
| 前端 | 静态 HTML + 原生 JS（无框架） | GitHub Pages |
| API 后端 | Cloudflare Worker + KV | 全球 CDN |
| 邮件 | Resend（DKIM + SPF Verified） | 100/天免费 |
| 域名 | Cloudflare DNS（curioradar.fun） | 主站 GitHub Pages，API CF Proxy |
| 反馈 | GitHub Issues 当数据库（5 类 label） | 不需后端持久层 |
| 加密备份 | openssl AES-256-CBC + pbkdf2 200k iter | macOS 自带 |

---

## 配置 / Secrets

所有 secret 不进 git。需要的环境变量和文件：

| 文件 | 内容 | 用途 |
|---|---|---|
| `.gh_pat` | GitHub PAT，权限 `repo` | 推送 curio-site / 创建 Issue |
| `.smtp_secret` | QQ 邮箱 SMTP 授权码 | 自用通知邮件 |
| `worker/.dev.vars` | `CLOUDFLARE_*` / `RESEND_API_KEY` / `ADMIN_TOKEN` | Worker 部署 + worker_sync |
| `profile.yaml` | identity / signal_preferences / dislikes / feedback_timeline | LLM 评分时读 |

完整清单 → [`scripts/secrets-manifest.txt`](scripts/secrets-manifest.txt)。

---

## 信源覆盖

**v0.9 升级后 30+ 信源**，按领域分组：

### 金融
- Stratechery（Ben Thompson 深度科技+金融）
- Net Interest（金融行业内部观察）
- 华尔街见闻 API（中文一手财经）
- arXiv q-fin（量化金融论文）
- HN 关键词：Federal Reserve / inflation / Tesla / Apple earnings

### AI
- Latent Space Blog
- Simon Willison's Blog
- AI Engineer Newsletter
- ByteByteGo Newsletter
- Anthropic Engineering
- arXiv cs.CL / cs.LG
- HN 关键词：Claude / GPT-5 / AI agent / Cursor / vibe coding
- B 站：Cursor 0.50 / Claude Code 实战 / vibe coding

### 半导体
- SemiAnalysis（行业首选深度）
- EE Times
- HN 关键词：TSMC / Nvidia / GPU / ASML / AI chip

### 大厂讯息
- The Verge / TechCrunch / Stratechery
- Product Hunt（新产品脉搏）
- 36氪 / 少数派（中文科技媒体）
- HN 关键词：Google / Apple / Microsoft / Meta / Amazon

### 全局
- HN frontpage 200pts+（兜底高热信号）

**新加领域**会通过 `agent/auto_sources.py` 的 9 类领域分类（finance/semiconductor/ai/bigtech/crypto/biotech/energy/space/gaming/general）自动配上同等水平的信源——保证用户加领域享受跟现有 4 个域**一样的待遇**。

---

## 常见任务速查

| 想做 | 命令 / 入口 |
|---|---|
| 加新领域 | 网页"添加新领域"按钮 → GitHub Issue（label=curio-add-domain）|
| 删领域 | hover 卡片 → ✕ → GitHub Issue（label=curio-delete-domain）|
| 强制立刻跑一次 | 网页"⚡ 立刻生成"按钮（每小时 automation 兜底） |
| 调整偏好 | 改 `profile.yaml` 的 signal_preferences / dislikes |
| 检查 worker 状态 | `curl https://api.curioradar.fun/health` |
| 看订阅者数 | （admin token）`curl -H "Authorization: Bearer $ADMIN_TOKEN" https://api.curioradar.fun/admin/...` |
| 备份 + 推送 | `bash scripts/backup_and_push.sh` |
| 改双语模板 | `agent/build_issue_md.py` 的 `_render_headline_card` |
| 加 RSS 信源 | 改 `sources.yaml` |
| 加领域类型映射 | 改 `agent/auto_sources.py` 的 `CATEGORY_KEYWORDS` |
| 改邮件文案 | `worker/src/index.js` 的 `confirmEmailHTML` |
| 改调度时间 | WorkBuddy 主界面 → 找对应 automation → 改 RRULE |
| 重新部署 worker | `cd worker && set -a && source .dev.vars && set +a && PATH=".../node/.../bin:$PATH" npx wrangler deploy` |

---

## 仓库与公网入口

| 项 | 地址 | 可见性 |
|---|---|---|
| 项目代码 | https://github.com/zczxd1118/curio-app | Private |
| 网站源码 | https://github.com/zczxd1118/curio-site | Public |
| 加密备份 | https://github.com/zczxd1118/curio-secrets | **Private**（含 secrets，绝不能 public） |
| 主站 | https://curioradar.fun/ | 公开 |
| 备用主站 | https://zczxd1118.github.io/curio-site/ | 公开（重定向到主站） |
| API | https://api.curioradar.fun/ | 公开（admin endpoint 要 token） |

---

## 风险与注意事项

1. **加密备份密码丢了 = 备份永远打不开**。openssl AES-256 无后门。
2. **secrets 仓库必须 Private**。误转 Public 暴露所有 token。
3. **GitHub PAT / Cloudflare Token 有效期**：建议每 6 个月旋转，旋转后立即 backup 一次。
4. **WorkBuddy automation cron**：改 RRULE 立即生效，不会等到下次启动。
5. **Resend 免费额度 100 邮件/天**：超过会失败，订阅者多到该量级时升级或换自建 SMTP。
6. **Cloudflare Bot Fight Mode**：会拦默认 Python urllib UA。`agent/worker_sync.py` 已加 `User-Agent: curio-bot/1.0` 绕过。
7. **新发件域名需"信誉积累期"**：QQ / 网易等国产邮箱对新域名（< 1 周）拦得激进，可能进垃圾箱甚至静默丢弃。建议初期：
   - QQ 邮箱白名单加 `curioradar.fun`
   - 多发邮件让收件人主动"标记不是垃圾邮件"
   - 1-2 周后信誉建立，进收件箱概率高
8. **workers.dev 国内被墙**：所有面向用户的 fetch 必须用 `api.curioradar.fun` 而不是 `*.workers.dev`（前者走 Cloudflare proxy 国内可用）。

---

## 路线图

### 已完成（v0.9 · 2026-05-31）
- ✅ 4 内置领域 daily/weekly 自动调度
- ✅ Stratechery 风格双语简报（中文标题 + 关键词 chips + 中文摘要 + 主编点评 + 折叠英文原文）
- ✅ 自有域名主站 + API + 邮件发件
- ✅ 用户自助加领域 / 删领域 / 立刻生成 / 退订
- ✅ 30+ 信源（行业专业 + HN 多元 + 中文一手）
- ✅ 跨设备加密备份 + 一键恢复
- ✅ 反馈闭环（GitHub Issue → profile.yaml → 下次生成）

### 计划中（v1.0）
- 🟡 主编自助建议加信源（Claude 评分时建议补什么源 → 自动开 Issue）
- 🟡 用户中心页面（自助查看订阅、改频率、删订阅）
- 🟡 真正的"立刻生成"（< 1 分钟，通过 GitHub Actions repository_dispatch）
- 🟡 List-Unsubscribe HTTP header（提升发件信誉）
- 🟡 加密信源（Doomberg / Kyla 等被墙的 Substack 通过中转）

### 不做（明确不做）
- ❌ 自有 LLM API 调用（坚持 WorkBuddy + Claude，不付外部 API 钱）
- ❌ 用户登录系统（邮箱即身份，不引入注册流程）
- ❌ 移动 App（响应式 Web 已够用）
- ❌ 多人编辑（这是个人产品，不做协作）

---

## 三天开发回顾（5/29 - 5/31）

| 时间 | 里程碑 |
|---|---|
| 5/29 | M0 demo（vibe-coding 单领域，本地 markdown） |
| 5/30 | M1（多领域 + Stratechery 风格周刊 + GitHub Pages） |
| 5/31 上午 | 统一 daily/weekly 渲染模板（双语 + chips） |
| 5/31 下午 | Cloudflare Worker + 自有域名 + Resend + 跨设备备份 |
| 5/31 晚上 | 信源扩容 + auto_sources v0.9 + Resend 域名验证 + 自助退订 |

总计：**3 天从 demo 到完整对外开放 SaaS** 🎉

---

## 版本与作者

- 版本：**v0.9（2026-05-31）**
- 作者：周小丁（zczxd1118 / 170665060@qq.com，深圳腾讯）
- 协作：WorkBuddy + Claude
- 许可：私人项目（不开源给外部）

如果你订到了这个 README，欢迎在 [curioradar.fun](https://curioradar.fun/) 试订一份简报 ☕
