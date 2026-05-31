# Curio 跨设备备份与恢复

> 路径 A：备份+一键恢复，让你换 Mac、电脑送修、出差临时机器都能 30 分钟接管。

## 现状：哪些东西"绑本机"

| 资产 | 位置 | 影响 |
|---|---|---|
| WorkBuddy automation 调度 | `~/.workbuddy/workbuddy.db` | 没它 → 没自动调度，简报不会准时跑 |
| Python venv | `~/.workbuddy/binaries/python/envs/curio_sys/` | 没它 → 抓数据/打分链路跑不了 |
| GitHub PAT | `.gh_pat` | 没它 → 推不到 curio-site 仓库 |
| SMTP 密码 | `.smtp_secret` | 没它 → 邮件发不出去 |
| Cloudflare/Resend Token | `worker/.dev.vars` | 没它 → Worker 重新部署不动（Worker 已部署的话不影响线上） |
| 用户偏好 + 反馈历史 | `profile.yaml` | 没它 → 反馈时间线断档，搜索关键词回到默认 |
| 历史候选/打分/导读 | `topics/` | 没它 → 历史期数丢失，缓存重抓需要时间 |

**用户侧（订阅、网站、邮件投递）已经云端化（Cloudflare + GitHub Pages），只有"生成新一期"这一步绑本机。**

## 备份

```bash
cd ~/WorkBuddy/2026-05-29-15-27-22/content-curator   # 或你的项目根
bash scripts/backup.sh
```

会做这些事：

1. 拷贝 4 个 secret 文件 + `profile.yaml` + `topics/` + 翻译/文章缓存
2. 从 `~/.workbuddy/workbuddy.db` 导出所有 Curio 相关 automation 定义
3. 跑 `pip freeze` 出 `requirements-frozen.txt`
4. 打包 `tar -czf` → `openssl aes-256-cbc` 加密
5. 输出 `~/curio-backup-YYYY-MM-DD-HHMM.tar.gz.enc`

**会让你输入加密密码——记牢，不存盘。** 推荐：在 1Password 里新建条目 `Curio Backup Pwd`，把密码贴进去。

### 把加密文件放哪

按推荐顺序：

1. **iCloud Drive / OneDrive / Google Drive**：把 `.enc` 文件丢进同步盘，自动多端备份。
2. **私有 GitHub 仓库**：建一个 `curio-secrets`（private），把 `.enc` push 上去，commit 多个版本就是历史快照。
3. **U 盘 / 移动硬盘**：物理隔离，最稳但最不方便。

### 备份频率建议

| 时机 | 是否要备份 |
|---|---|
| 加新领域 / 改 profile.yaml | ✅ 立即备 |
| 任何 secret 旋转（PAT 过期、SMTP 改密、CF Token 重置） | ✅ 立即备 |
| 每周一份滚动备份 | ✅ 推荐（automation 可以自动跑 backup.sh） |
| 单纯跑了一期简报 | ❌ 不必（topics/ 历史在 git 里也有） |

## 在新 Mac 上恢复

### 前置（手工）

1. 装好 [WorkBuddy](https://workbuddy.cn)
2. 装 Homebrew → `brew install git openssl`（macOS 一般自带 git）
3. 把 `.tar.gz.enc` 备份文件下载到新机器（从 iCloud / GitHub 私有仓库 / U 盘）
4. 从 1Password 翻出加密密码

### 一键恢复

```bash
# clone 一份脚本（或从备份里拿）
git clone https://github.com/zczxd1118/curio-app.git /tmp/curio-app-bootstrap
cd /tmp/curio-app-bootstrap

# 跑恢复
bash scripts/setup_new_device.sh ~/Downloads/curio-backup-2026-05-31.tar.gz.enc
```

会做这些事：

1. 解密 + 解压备份包
2. clone `curio-app` 到 `~/curio`（可用 `CURIO_PROJECT=...` 改路径）
3. 把 secrets / profile / topics / 缓存落到新项目
4. 创建 `~/.workbuddy/binaries/python/envs/curio_sys/` venv，按 `requirements-frozen.txt` 装包
5. 把 automation 定义灌回 `~/.workbuddy/workbuddy.db`，自动替换路径
6. 跑一次 `build_issue_md` 烟测

恢复完，明早 8:00 daily automation 会自动跑出第一期，跟在原机器上一样。

## 风险提示（必读）

1. **加密密码丢了 = 备份废了**。openssl AES-256 是真加密，无后门。务必 1Password / Keeper 多端存。
2. **Cloudflare / Resend / GitHub PAT 可能过期**。如果备份是 3 个月前的，恢复后要先验 token 还在不在；过期就去对应平台重新生成、再跑一次 backup。
3. **WorkBuddy automation 的 cwds 字段**会自动从旧路径替换为新路径，但如果你给项目路径起了个完全不同的名字，要手动检查 `automations` 表的 `cwds` 字段。
4. **不要把 `.enc` 推到公开仓库**。AES-256 安全性依赖密码强度，弱密码（< 12 位）暴力破解就废。
5. **secret 旋转策略**：建议每 6 个月更换 GitHub PAT 和 Cloudflare Token，每次旋转后立即 backup 一次。

## FAQ

**Q：能不能每天自动备份？**
A：可以。在 WorkBuddy 加一条 automation：每天 23:00 跑 `bash scripts/backup.sh`，输出到 `~/Library/Mobile Documents/com~apple~CloudDocs/CurioBackup/`（iCloud Drive）。但密码会变成 stdin 输入难自动化——折中方案是用 `OPENSSL_PASS=xxx` 环境变量喂密码（备份脚本可以改造支持，需要时再加）。

**Q：恢复后 Worker 还要重新部署吗？**
A：不用。Worker 已经在 Cloudflare 上跑着，本地 `worker/.dev.vars` 只是开发时本地起服务用。线上 Worker 的 secrets 在 Cloudflare 后台。

**Q：备份会包含 `node_modules` / `.venv` 吗？**
A：不会。`node_modules` 通过 `npm install` 重建，venv 通过 `pip install -r requirements-frozen.txt` 重建。这两样占 100MB+，没必要打进备份。

**Q：备份文件大概多大？**
A：估算 5-15 MB（topics/ 占大头，secrets 全部加起来 < 1 KB）。
