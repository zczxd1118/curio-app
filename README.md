# Curio · 趋势雷达

> 你选感兴趣的领域，Curio 每天/每周给你出一份**主编已读过、双语、带主编点评**的简报。
> 主站：[curioradar.fun](https://curioradar.fun/) · API：[api.curioradar.fun](https://api.curioradar.fun/health)

---

## 这是什么

Curio 是一个**信息策展 AI Agent**。你只用一句话告诉它"我关心金融、AI、半导体"，它会替你做四件事：

1. **抓**：从 HackerNews / Stratechery / 知名 RSS / B 站 自动抓全网新内容
2. **筛**：用 Claude 当主编，给每条内容打分（新颖度/深度/相关度），淘汰广告党/标题党
3. **写**：每条头版报道附中文事实摘要 + 80-150 字主编点评，可折叠英文原文
4. **推**：通过邮件按 daily/weekly 节奏送到订阅者邮箱，同时网页公开

订阅者只需要输邮箱+点选领域，剩下的 Agent 全包了。

---

## 谁在用

- **你自己**（产品作者）：每天 8:00 收金融日报、大厂讯息日报；每周一 8:00 收 AI 周刊、半导体周刊
- **公网订阅者**：访问 [curioradar.fun](https://curioradar.fun/) 自助订阅

---

## 系统架构

```
┌────────────────────────────────────────────────────────────────┐
│                  你的 Mac（生成侧，绑本机）                      │
│                                                                │
│  WorkBuddy automation cron                                     │
│       ↓ 每天 8:00 / 每周一 8:00                                 │
│  cli_generate.py prepare → Claude 评分 → prepare_notes →       │
│       Claude 写主编点评 → finalize（build_issue_md → site）     │
│       ↓                                                        │
│  git push curio-site → GitHub Pages → curioradar.fun           │
│       ↓                                                        │
│  worker_sync push_content → Cloudflare KV                      │
│       ↓                                                        │
│  worker /broadcast → Resend 发送订阅者邮件                       │
└────────────────────────────────────────────────────────────────┘
                            ↓                ↓
                     ┌──────────────┐  ┌──────────────┐
                     │ Cloudflare   │  │ GitHub Pages │
                     │ Worker + KV  │  │ curio-site   │
                     │ + Resend     │  │              │
                     └──────────────┘  └──────────────┘
                            ↑                ↑
                     ┌──────────────────────────────┐
                     │       公网用户（任何设备）     │
                     │  · 网页看简报                 │
                     │  · 订阅 / 加领域 / 反馈       │
                     │  · 收邮件                    │
                     └──────────────────────────────┘
```

**关键：** 用户侧（订阅、网页、邮件）100% 跑在云端，不依赖你电脑。只有"生成新一期"必须本机跑。

---

## 项目结构

```
content-curator/
├── README.md                  ← 本文档
├── BACKUP.md                  ← 跨设备备份手册
├── PRD.v0.2-subscribe.md      ← 订阅功能 PRD
│
├── cli_generate.py            ← 主入口：prepare / prepare_notes / finalize
├── curator.py                 ← 老链路：search / score / digest（已被 cli_generate 包装）
├── server.py                  ← 本地反馈服务器（已被 Cloudflare Worker 取代，留作备用）
│
├── sources.yaml               ← 领域 + 信源注册表（哪些 RSS / HN keyword / B站 UID）
├── profile.yaml               ← 你的偏好画像 + feedback_timeline
│
├── agent/                     ← Agent 核心模块
│   ├── build_issue_md.py      ← 统一 daily/weekly md 生成器（含双语+chips）
│   ├── render_site.py         ← markdown → HTML 渲染
│   ├── search_*.py            ← B站 / HN / RSS 抓取器
│   ├── fetch_article.py       ← 全文抓取（trafilatura）
│   ├── fetch_subtitle.py      ← B站字幕抓取
│   ├── ingest_feedback.py     ← GitHub Issue 反馈 → profile.yaml
│   ├── worker_sync.py         ← 与 Cloudflare Worker 通信（订阅/广播/加领域 ingest）
│   ├── notify_email.py        ← 自用邮件通知
│   └── auto_sources.py        ← 加新领域时自动配信源
│
├── prompts/                   ← LLM prompt 模板
│   ├── score_content.md       ← 主编评分（输出含 title_zh / keywords / summary_zh）
│   ├── editor_note.md         ← 主编点评写作
│   ├── write_article.md       ← 报道写作（M2 用，目前未启用）
│   └── write_editorial.md     ← 社论写作
│
├── topics/                    ← 每个领域的中间产物 + 历史期数
│   ├── {slug}.candidates.json     ← 抓回来的原始候选
│   ├── {slug}.scored.json         ← Claude 评分后的必读/参考/跳过
│   ├── {slug}.editor_notes.json   ← Claude 写的主编点评
│   └── {slug}.weekly.YYYY-MM-DD.md ← 最终成品 markdown（daily/weekly 共用此文件名）
│
├── site/                      ← 渲染后的静态网站（独立 git 仓库 → curio-site）
│
├── worker/                    ← Cloudflare Worker
│   ├── src/index.js           ← 8 个 endpoint：health/subscribe/confirm/unsubscribe/domains/admin-*/broadcast
│   ├── wrangler.toml          ← CF 部署配置（routes=api.curioradar.fun/*）
│   └── .dev.vars              ← 本地开发用 secrets（gitignored）
│
└── scripts/                   ← 跨设备备份恢复
    ├── secrets-manifest.txt   ← 绑本机资产清单
    ├── backup.sh              ← 加密备份
    ├── backup_and_push.sh     ← 备份 + 推到 secrets 仓库（推荐日常用）
    └── setup_new_device.sh    ← 新设备一键恢复
```

---

## 快速使用

### 用户视角

直接打开 [curioradar.fun](https://curioradar.fun/)：
- 看每个领域最新简报
- 点右下角订阅按钮：输邮箱 → 选领域 → 选 daily/weekly → 收确认邮件
- 点"加领域"按钮：自动跳转 GitHub Issue，作者批准后下一轮生效
- 看完点底部"有用/一般/偏了"反馈，下次生成会读

### 作者视角（手工触发一次）

```bash
cd /Users/zoezczhou/WorkBuddy/2026-05-29-15-27-22/content-curator
PY=/Users/zoezczhou/.workbuddy/binaries/python/envs/curio_sys/bin/python

# 阶段 1：抓数据 + 出 score prompt
$PY cli_generate.py prepare

# 阶段 2：交给 Claude 写 scored.json（这一步在 WorkBuddy 对话里跑）

# 阶段 2.5：抓正文 + 出主编点评 prompt
$PY cli_generate.py prepare_notes

# 阶段 2.6：交给 Claude 写 editor_notes.json

# 阶段 3：拼装 + 渲染 + push GitHub + 邮件 + worker 群发
$PY cli_generate.py finalize --cadence daily   # 或 --cadence weekly
```

平时不用手动跑——三条 WorkBuddy automation 自动调度：
- `automation-1780211294404` 每天 8:00 daily
- `automation-1780140880021` 每周一 8:00 weekly
- `automation-1780167898607` 每小时检查用户的"立即生成"请求

---

## 跨设备备份与恢复

> **核心问题**：换台 Mac 怎么办？详见 [`BACKUP.md`](BACKUP.md)

### 第一次设置（已完成）

1. 跑 `bash scripts/backup.sh` 出加密备份
2. 密码存到 macOS 锁定备忘录「Curio Backup Pwd」
3. 在 GitHub 建 private 仓库 `zczxd1118/curio-secrets` 存 .enc 文件

### 日常备份（**推荐：一行命令**）

```bash
cd /Users/zoezczhou/WorkBuddy/2026-05-29-15-27-22/content-curator
bash scripts/backup_and_push.sh
```

会自动：
1. 生成新加密备份（要你输密码）
2. 移到 `~/curio-secrets/` 仓库
3. git commit + push 到 GitHub
4. 自动保留最近 12 份，删旧的（避免仓库膨胀）

**什么时候跑：**

| 事件 | 是否要备份 |
|---|---|
| 加新领域 / 改 profile.yaml | ✅ 立即 |
| GitHub PAT / Cloudflare Token 旋转 | ✅ 立即 |
| 每周固定一份滚动备份 | ✅ 推荐 |
| 单纯每天跑了简报 | ❌ 不必（topics/ 历史在 git 里也有） |

### 换设备恢复（30 分钟）

新 Mac 上：

```bash
# 1. 装好 WorkBuddy + 工具
brew install git openssl gh

# 2. 登 GitHub
gh auth login

# 3. clone 两个仓库（公开代码 + private 备份）
git clone https://github.com/zczxd1118/curio-app.git /tmp/bootstrap
gh repo clone zczxd1118/curio-secrets ~/curio-secrets

# 4. 跑恢复（输入备忘录里那个密码）
cd /tmp/bootstrap
bash scripts/setup_new_device.sh ~/curio-secrets/curio-backup-*.tar.gz.enc
```

恢复脚本会：
- 解密备份
- clone curio-app 到 `~/curio`
- 还原 4 个 secret + profile.yaml + topics/ + 缓存
- 创建 venv + 装 37 个 Python 包
- 灌回 3 条 WorkBuddy automation（自动 sed 修路径）
- 跑一次 build 烟测

明早 8:00 起 daily automation 自动跑，跟在原机器上一样。

---

## 主要技术栈

| 层 | 技术 | 备注 |
|---|---|---|
| 调度 | WorkBuddy automation（本地 SQLite cron） | 已绑本机 |
| LLM | Claude（通过 WorkBuddy 调度，不付 API 费） | E 方案 |
| 数据抓取 | trafilatura / feedparser / B站 API / HN API | Python |
| 前端 | 静态 HTML + 原生 JS（无框架） | GitHub Pages |
| API 后端 | Cloudflare Worker + KV | api.curioradar.fun |
| 邮件 | Resend (onboarding@resend.dev) | 100/天免费 |
| 域名 | Cloudflare DNS（curioradar.fun） | API 走 CF proxy，主站走 GitHub Pages |
| 反馈 | GitHub Issues 当数据库（5 类 label） | 不需要后端 |
| 加密备份 | openssl AES-256-CBC + pbkdf2 200k iter | macOS 自带 |

---

## 配置 / Secrets

所有 secret 都不进 git。需要的环境变量和文件：

| 文件 | 内容 | 谁需要 |
|---|---|---|
| `.gh_pat` | GitHub Personal Access Token，权限 `repo` | 推送 curio-site |
| `.smtp_secret` | QQ 邮箱 SMTP 授权码 | 自用通知邮件 |
| `worker/.dev.vars` | `CLOUDFLARE_*` / `RESEND_API_KEY` / `ADMIN_TOKEN` | Worker 部署 + worker_sync |
| `profile.yaml` | identity / signal_preferences / dislikes / feedback_timeline | LLM 评分时读 |

完整清单见 [`scripts/secrets-manifest.txt`](scripts/secrets-manifest.txt)。

---

## 常见任务速查

| 想做 | 命令 |
|---|---|
| 加新领域 | 网页"加领域"按钮 → GitHub Issue → 下次自动 ingest，或手工 `python curator.py add-domain` |
| 调整偏好 | 改 `profile.yaml` 的 `signal_preferences` / `dislikes` |
| 强制立刻跑一次 | 网页"⚡ 立刻生成"按钮（每小时 automation 兜底） |
| 检查 worker 状态 | `curl https://api.curioradar.fun/health` |
| 看订阅者数 | `curl -H "Authorization: Bearer $ADMIN_TOKEN" https://api.curioradar.fun/admin/subscribers` |
| 备份+推送 | `bash scripts/backup_and_push.sh` |
| 改双语模板 | 改 `agent/build_issue_md.py` 里的 `_render_headline_card` |
| 调度时间 | WorkBuddy 主界面找对应 automation 改 RRULE |

---

## 仓库与公网入口

| 项 | 地址 | 可见性 |
|---|---|---|
| 项目代码 | https://github.com/zczxd1118/curio-app | Private |
| 网站源码 | https://github.com/zczxd1118/curio-site | Public |
| 加密备份 | https://github.com/zczxd1118/curio-secrets | **Private** |
| 主站 | https://curioradar.fun/ | 公开 |
| 备用主站 | https://zczxd1118.github.io/curio-site/ | 公开 |
| API | https://api.curioradar.fun/ | 公开（admin 接口需 token） |

---

## 风险与注意事项

1. **加密密码丢了 = 备份永远打不开**。AES-256 无后门。
2. **secrets 仓库必须保持 Private**。误转 Public 会暴露所有 token。
3. **GitHub PAT / Cloudflare Token 有效期**：默认无期限，但建议每 6 个月旋转一次，旋转后立刻 backup。
4. **WorkBuddy automation 在 cron 改 RRULE 时**会立刻生效，不会等到下次启动。
5. **Resend 免费额度 100 邮件/天**：超过会失败，订阅者多到该量级时考虑升级或改自建 SMTP。
6. **Cloudflare Bot Fight Mode**：会拦默认 Python urllib UA。`agent/worker_sync.py` 已加 `User-Agent: curio-bot/1.0` 绕过。

---

## 版本与作者

- 版本：v0.8（2026-05-31）—— 统一 daily/weekly 渲染 + 跨设备备份恢复链路完成
- 作者：周小丁（zczxd1118 / 170665060@qq.com）
- 协作：WorkBuddy + Claude
- 上线：2026-05-29 ~ 2026-05-31（3 天从 demo 到公开 SaaS）
