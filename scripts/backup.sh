#!/usr/bin/env bash
# Curio 跨设备备份脚本（路径 A）
#
# 把所有"绑本机"的资产打包成一个加密 .tar.gz.enc 文件：
#   - 4 个 secret 文件（.gh_pat / .smtp_secret / worker/.dev.vars / profile.yaml）
#   - topics/ 历史数据
#   - 翻译/文章缓存
#   - WorkBuddy automation 定义（从 ~/.workbuddy/workbuddy.db 导出）
#   - Python venv 包列表（pip freeze）
#
# 加密：openssl aes-256-cbc，密码用户当场输入（不存盘）
# 输出：~/curio-backup-YYYY-MM-DD.tar.gz.enc
#
# 用法：
#   bash scripts/backup.sh
#   或：CURIO_BACKUP_DIR=~/Documents bash scripts/backup.sh

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TIMESTAMP="$(date +%Y-%m-%d-%H%M)"
BACKUP_DIR="${CURIO_BACKUP_DIR:-$HOME}"
STAGING="$(mktemp -d -t curio-backup-XXXXXX)"
OUT_TAR="$STAGING/curio-backup-$TIMESTAMP.tar.gz"
OUT_ENC="$BACKUP_DIR/curio-backup-$TIMESTAMP.tar.gz.enc"

cleanup() { rm -rf "$STAGING"; }
trap cleanup EXIT

log() { printf "[%s] %s\n" "$(date +%H:%M:%S)" "$*"; }

log "🛰️  Curio backup → $OUT_ENC"
log "    源仓库：$ROOT"

# ---------- 1. 拷贝项目内文件 ----------
mkdir -p "$STAGING/payload/project"
PAYLOAD="$STAGING/payload"

copy_if_exists() {
  local src="$1" dst="$2"
  if [ -e "$src" ] || [ -L "$src" ]; then
    mkdir -p "$(dirname "$dst")"
    # 软链解开成真实文件（.smtp_secret 是 symlink）
    if [ -L "$src" ]; then
      cp -L "$src" "$dst" 2>/dev/null && log "  ✓ $(basename "$src") (deref)"
    elif [ -d "$src" ]; then
      cp -R "$src" "$dst" && log "  ✓ $(basename "$src")/ (dir)"
    else
      cp "$src" "$dst" && log "  ✓ $(basename "$src")"
    fi
  else
    log "  ⚠️  缺失: $src（跳过）"
  fi
}

log "📦 1/5 拷贝项目内文件"
copy_if_exists "$ROOT/.gh_pat"           "$PAYLOAD/project/.gh_pat"
copy_if_exists "$ROOT/.smtp_secret"      "$PAYLOAD/project/.smtp_secret"
copy_if_exists "$ROOT/worker/.dev.vars"  "$PAYLOAD/project/worker/.dev.vars"
copy_if_exists "$ROOT/profile.yaml"      "$PAYLOAD/project/profile.yaml"
copy_if_exists "$ROOT/topics"            "$PAYLOAD/project/topics"
copy_if_exists "$ROOT/.translate_cache"  "$PAYLOAD/project/.translate_cache"
copy_if_exists "$ROOT/.article_cache"    "$PAYLOAD/project/.article_cache"

# ---------- 2. 导出 WorkBuddy automation ----------
log "📦 2/5 导出 WorkBuddy automation 定义"
WB_DB="$HOME/.workbuddy/workbuddy.db"
mkdir -p "$PAYLOAD/workbuddy"
if [ -f "$WB_DB" ]; then
  # 只导 curio 相关的 automation
  /usr/bin/sqlite3 "$WB_DB" \
    ".mode insert automations" \
    "SELECT * FROM automations WHERE name LIKE '%curio%' OR name LIKE '%Curio%' OR prompt LIKE '%curio%' OR prompt LIKE '%Curio%';" \
    > "$PAYLOAD/workbuddy/automations.sql" 2>/dev/null || true
  COUNT=$(grep -c "INSERT INTO" "$PAYLOAD/workbuddy/automations.sql" 2>/dev/null || echo 0)
  log "  ✓ 导出 $COUNT 条 automation 到 automations.sql"
else
  log "  ⚠️  $WB_DB 不存在，跳过"
fi

# ---------- 3. 导出 venv 依赖 ----------
log "📦 3/5 导出 Python 依赖列表"
VENV_PIP="$HOME/.workbuddy/binaries/python/envs/curio_sys/bin/pip"
mkdir -p "$PAYLOAD/python"
if [ -x "$VENV_PIP" ]; then
  "$VENV_PIP" freeze > "$PAYLOAD/python/requirements-frozen.txt" 2>/dev/null
  N=$(wc -l < "$PAYLOAD/python/requirements-frozen.txt" | tr -d ' ')
  log "  ✓ 冻结 $N 个包到 requirements-frozen.txt"
else
  log "  ⚠️  curio_sys venv pip 不存在，跳过"
fi

# ---------- 4. 写元数据 ----------
log "📦 4/5 写备份元数据"
cat > "$PAYLOAD/MANIFEST.txt" <<EOF
Curio Backup
============
created_at:   $(date -u +"%Y-%m-%dT%H:%M:%SZ")
host:         $(hostname)
user:         $USER
project_root: $ROOT
git_commit:   $(cd "$ROOT" && git rev-parse --short HEAD 2>/dev/null || echo "unknown")
git_branch:   $(cd "$ROOT" && git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")

Contents:
$(find "$PAYLOAD" -type f | sed "s|$PAYLOAD/||" | sort)
EOF

# ---------- 5. 打包 + 加密 ----------
log "📦 5/5 打包 + AES-256 加密"
( cd "$STAGING" && tar -czf "$OUT_TAR" -C "$PAYLOAD" . )
RAW_SIZE=$(du -h "$OUT_TAR" | awk '{print $1}')
log "  原始 tar.gz: $RAW_SIZE"

mkdir -p "$BACKUP_DIR"
if [ -n "${CURIO_BACKUP_PASS:-}" ]; then
  log "  使用 CURIO_BACKUP_PASS 环境变量加密（适用于 automation 自动备份）"
  /usr/local/bin/openssl enc -aes-256-cbc -salt -pbkdf2 -iter 200000 \
    -pass "env:CURIO_BACKUP_PASS" \
    -in "$OUT_TAR" -out "$OUT_ENC"
else
  echo
  echo "🔒 请输入备份加密密码（**记牢**，丢了备份就解不开）"
  echo "   建议：在 1Password / Keeper 里新建条目，标题 'Curio Backup Pwd'"
  echo
  /usr/local/bin/openssl enc -aes-256-cbc -salt -pbkdf2 -iter 200000 \
    -in "$OUT_TAR" -out "$OUT_ENC"
fi

ENC_SIZE=$(du -h "$OUT_ENC" | awk '{print $1}')

echo
echo "✅ 备份完成"
echo "   文件：$OUT_ENC"
echo "   大小：$ENC_SIZE"
echo
echo "下一步建议（按推荐顺序）："
echo "  1. 上传到 iCloud Drive / OneDrive / Google Drive 同步盘"
echo "  2. 或 push 到一个私有 GitHub 仓库（curio-secrets，private）"
echo "  3. 在 1Password 里把加密密码存到 'Curio Backup Pwd' 条目"
echo
echo "新设备恢复："
echo "  bash scripts/setup_new_device.sh /path/to/curio-backup-*.tar.gz.enc"
