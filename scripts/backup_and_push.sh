#!/usr/bin/env bash
# Curio 一键备份 + 推送到 GitHub private 仓库
#
# 流程：
#   1. 跑 backup.sh 生成加密备份到 ~/curio-backup-*.tar.gz.enc
#   2. 移动到 ~/curio-secrets/ 本地仓库
#   3. git commit + push 到 GitHub zczxd1118/curio-secrets (PRIVATE)
#
# 用法：
#   bash scripts/backup_and_push.sh
#   或：CURIO_BACKUP_PASS=xxxxx bash scripts/backup_and_push.sh   # 自动化场景免输密码
#
# 前置条件：
#   - 已跑过初次的 curio-secrets 仓库初始化（gh repo create --private --push）
#   - ~/curio-secrets/ 已 clone 或已是工作目录
#   - gh CLI / git 已登录

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SECRETS_DIR="${CURIO_SECRETS_DIR:-$HOME/curio-secrets}"

log() { printf "[%s] %s\n" "$(date +%H:%M:%S)" "$*"; }

# ---------- 0. 检查前置 ----------
log "🔍 检查前置"
if [ ! -d "$SECRETS_DIR/.git" ]; then
  echo "❌ $SECRETS_DIR 还没初始化为 git 仓库。"
  echo "   首次跑：参考 BACKUP.md 走一遍 'gh repo create curio-secrets --private --push' 流程。"
  exit 1
fi
command -v git >/dev/null 2>&1 || { echo "❌ 没装 git"; exit 1; }
log "  ✓ secrets 仓库存在：$SECRETS_DIR"

# ---------- 1. 跑 backup.sh ----------
log "🛰️  1/3 跑 backup.sh 生成加密备份"
# 让 backup.sh 直接输出到 secrets 仓库目录，省一次 mv
CURIO_BACKUP_DIR="$SECRETS_DIR" bash "$ROOT/scripts/backup.sh"

# ---------- 2. 找最新备份 + 清理旧的（可选） ----------
log "📦 2/3 整理 secrets 仓库"
cd "$SECRETS_DIR"

# 找出本次刚生成的 .enc（按时间排序最新一个）
LATEST_ENC=$(ls -t curio-backup-*.tar.gz.enc 2>/dev/null | head -1)
if [ -z "$LATEST_ENC" ]; then
  echo "❌ secrets 仓库里没找到 .enc 文件，备份可能失败"
  exit 1
fi
log "  ✓ 最新备份：$LATEST_ENC"

# 保留最近 N 份（防止仓库无限膨胀），N 默认 12
KEEP_N="${CURIO_BACKUP_KEEP:-12}"
TOTAL=$(ls curio-backup-*.tar.gz.enc 2>/dev/null | wc -l | tr -d ' ')
if [ "$TOTAL" -gt "$KEEP_N" ]; then
  log "  🗑  当前 $TOTAL 份备份，保留最近 $KEEP_N 份，删旧的"
  ls -t curio-backup-*.tar.gz.enc | tail -n +$((KEEP_N + 1)) | while read -r old; do
    rm -f "$old"
    log "    - 删除 $old"
  done
fi

# ---------- 3. commit + push ----------
log "🚀 3/3 push 到 GitHub"
git add -A
if git diff --cached --quiet; then
  log "  （没新变化，跳过 commit）"
else
  COMMIT_MSG="backup $(date +%Y-%m-%d-%H%M)"
  git commit -q -m "$COMMIT_MSG"
  log "  ✓ commit：$COMMIT_MSG"
fi

# push（用项目仓库的 PAT 也行，但 gh login 后已有凭证）
if git push -q 2>&1; then
  log "  ✓ push 成功"
else
  log "  ❌ push 失败（检查网络 / gh 登录态）"
  exit 1
fi

# ---------- 总结 ----------
echo ""
echo "=========================================="
echo "✅ 备份 + 推送 完成"
echo "=========================================="
echo "  本地：$SECRETS_DIR/$LATEST_ENC"
echo "  远端：https://github.com/zczxd1118/curio-secrets"
echo "  当前仓库共有 $(ls curio-backup-*.tar.gz.enc 2>/dev/null | wc -l | tr -d ' ') 份历史备份"
echo ""
echo "  解密密码：macOS 备忘录「Curio Backup Pwd」"
