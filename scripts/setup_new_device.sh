#!/usr/bin/env bash
# Curio 新设备一键恢复（路径 A）
#
# 在新 Mac 上运行：
#   1. clone curio-app 仓库
#   2. 解开备份包 → secrets/topics/缓存 落到正确位置
#   3. 创建 Python venv → 装依赖
#   4. 注册 WorkBuddy automation
#   5. 烟测一次 build_issue_md
#
# 前置条件（必须先手工搞定）：
#   - 装好 WorkBuddy（automation 调度需要）
#   - 装好 git / openssl（macOS 自带或 brew install openssl）
#   - 浏览器登录 GitHub，clone 时能用 SSH 或临时 PAT
#   - 拿到加密密码（备份时 1Password 里存的那个）
#
# 用法：
#   bash setup_new_device.sh /path/to/curio-backup-2026-05-31.tar.gz.enc
#
# 环境变量（可选）：
#   CURIO_REPO_URL   curio-app 仓库地址（默认 SSH）
#   CURIO_PROJECT    解出来的项目目标路径（默认 ~/curio）

set -euo pipefail

ENC_FILE="${1:-}"
if [ -z "$ENC_FILE" ] || [ ! -f "$ENC_FILE" ]; then
  echo "用法: bash setup_new_device.sh /path/to/curio-backup.tar.gz.enc"
  exit 1
fi

REPO_URL="${CURIO_REPO_URL:-https://github.com/zczxd1118/curio-app.git}"
PROJECT_DIR="${CURIO_PROJECT:-$HOME/curio}"
STAGING="$(mktemp -d -t curio-restore-XXXXXX)"

cleanup() { rm -rf "$STAGING"; }
trap cleanup EXIT

log() { printf "[%s] %s\n" "$(date +%H:%M:%S)" "$*"; }

# ---------- 0. 前置检查 ----------
log "🔍 0/6 前置检查"
command -v git >/dev/null 2>&1 || { echo "❌ 没装 git，brew install git 先"; exit 1; }
command -v /usr/local/bin/openssl >/dev/null 2>&1 || { echo "❌ 没装 openssl，brew install openssl 先"; exit 1; }
[ -d "$HOME/.workbuddy" ] || { echo "❌ 没装 WorkBuddy，先装"; exit 1; }
log "  ✓ git / openssl / WorkBuddy 都在"

# ---------- 1. 解密 + 解压备份 ----------
log "🔓 1/6 解密 + 解压备份"
TAR_FILE="$STAGING/curio-backup.tar.gz"
if [ -n "${CURIO_BACKUP_PASS:-}" ]; then
  /usr/local/bin/openssl enc -aes-256-cbc -d -pbkdf2 -iter 200000 \
    -pass "env:CURIO_BACKUP_PASS" \
    -in "$ENC_FILE" -out "$TAR_FILE"
else
  echo "请输入备份加密密码："
  /usr/local/bin/openssl enc -aes-256-cbc -d -pbkdf2 -iter 200000 \
    -in "$ENC_FILE" -out "$TAR_FILE"
fi

mkdir -p "$STAGING/payload"
tar -xzf "$TAR_FILE" -C "$STAGING/payload"
log "  ✓ 解出到 $STAGING/payload"

# 显示 manifest
if [ -f "$STAGING/payload/MANIFEST.txt" ]; then
  echo "----------- 备份元数据 -----------"
  head -10 "$STAGING/payload/MANIFEST.txt"
  echo "---------------------------------"
fi

# ---------- 2. clone 项目 ----------
log "📥 2/6 clone curio-app 到 $PROJECT_DIR"
if [ -d "$PROJECT_DIR/.git" ]; then
  log "  ⚠️  $PROJECT_DIR 已存在 git 仓库，跳过 clone（如要重新 clone 请先删掉）"
else
  git clone "$REPO_URL" "$PROJECT_DIR"
  log "  ✓ clone 完成"
fi

# ---------- 3. 把 secrets 落回项目 ----------
log "🔑 3/6 还原 secrets / 数据"
PJSRC="$STAGING/payload/project"
restore_file() {
  local src="$1" dst="$2"
  if [ -e "$src" ]; then
    mkdir -p "$(dirname "$dst")"
    if [ -d "$src" ]; then
      cp -R "$src" "$(dirname "$dst")/"
    else
      cp "$src" "$dst"
    fi
    log "  ✓ $(basename "$dst")"
  fi
}

restore_file "$PJSRC/.gh_pat"           "$PROJECT_DIR/.gh_pat"
restore_file "$PJSRC/.smtp_secret"      "$PROJECT_DIR/.smtp_secret"
restore_file "$PJSRC/worker/.dev.vars"  "$PROJECT_DIR/worker/.dev.vars"
restore_file "$PJSRC/profile.yaml"      "$PROJECT_DIR/profile.yaml"
restore_file "$PJSRC/topics"            "$PROJECT_DIR/topics"
restore_file "$PJSRC/.translate_cache"  "$PROJECT_DIR/.translate_cache"
restore_file "$PJSRC/.article_cache"    "$PROJECT_DIR/.article_cache"

# 修权限（secret 文件 600）
chmod 600 "$PROJECT_DIR/.gh_pat" 2>/dev/null || true
chmod 600 "$PROJECT_DIR/.smtp_secret" 2>/dev/null || true
chmod 600 "$PROJECT_DIR/worker/.dev.vars" 2>/dev/null || true

# ---------- 4. 创建 venv + 装依赖 ----------
log "🐍 4/6 创建 Python venv"
VENV_DIR="$HOME/.workbuddy/binaries/python/envs/curio_sys"
PY_BIN="$HOME/.workbuddy/binaries/python/versions/3.13.12/bin/python3"

if [ ! -x "$PY_BIN" ]; then
  # 兜底：用系统 python3
  PY_BIN="$(command -v python3)"
  log "  ⚠️  WorkBuddy managed python 不存在，用系统 python3：$PY_BIN"
fi

if [ ! -d "$VENV_DIR" ]; then
  "$PY_BIN" -m venv "$VENV_DIR"
  log "  ✓ venv 创建：$VENV_DIR"
else
  log "  ⚠️  venv 已存在，复用"
fi

REQ="$STAGING/payload/python/requirements-frozen.txt"
if [ -f "$REQ" ]; then
  "$VENV_DIR/bin/pip" install -q --upgrade pip
  "$VENV_DIR/bin/pip" install -q -r "$REQ"
  log "  ✓ 装了 $(wc -l < "$REQ" | tr -d ' ') 个包"
else
  log "  ⚠️  备份里没 requirements-frozen.txt，跳过 pip install"
fi

# ---------- 5. 注册 WorkBuddy automation ----------
log "⚙️  5/6 注册 WorkBuddy automation"
SQL="$STAGING/payload/workbuddy/automations.sql"
WB_DB="$HOME/.workbuddy/workbuddy.db"
if [ -f "$SQL" ] && [ -f "$WB_DB" ]; then
  # 先备份现有 db
  cp "$WB_DB" "$WB_DB.backup-$(date +%s)"
  # 替换 cwds 字段里的旧路径为新项目路径（备份机器的项目路径未必跟新机器一样）
  OLD_PATH_HINT=$(grep -o '/Users/[^"]*/content-curator' "$SQL" | head -1)
  if [ -n "$OLD_PATH_HINT" ] && [ "$OLD_PATH_HINT" != "$PROJECT_DIR" ]; then
    sed -i.bak "s|$OLD_PATH_HINT|$PROJECT_DIR|g" "$SQL"
    log "  ✓ 替换路径 $OLD_PATH_HINT → $PROJECT_DIR"
  fi
  /usr/bin/sqlite3 "$WB_DB" < "$SQL" 2>&1 | tail -3 || true
  COUNT=$(/usr/bin/sqlite3 "$WB_DB" "SELECT COUNT(*) FROM automations WHERE name LIKE '%urio%';" 2>/dev/null)
  log "  ✓ 当前 db 里有 $COUNT 条 Curio automation"
else
  log "  ⚠️  没有 automations.sql 或 workbuddy.db，跳过"
fi

# ---------- 6. 烟测 ----------
log "🧪 6/6 烟测一遍"
cd "$PROJECT_DIR"
if [ -x "$VENV_DIR/bin/python" ] && [ -f "agent/build_issue_md.py" ]; then
  # 找一个有 scored.json 的领域试 build
  TEST_SLUG=$(ls topics/*.scored.json 2>/dev/null | head -1 | xargs basename 2>/dev/null | sed 's/.scored.json//')
  if [ -n "$TEST_SLUG" ]; then
    "$VENV_DIR/bin/python" -m agent.build_issue_md --slug "$TEST_SLUG" --cadence daily \
      --out /tmp/curio-smoke.md 2>&1 | tail -3
    [ -s /tmp/curio-smoke.md ] && log "  ✓ build_issue_md 烟测通过" || log "  ⚠️  烟测无输出"
    rm -f /tmp/curio-smoke.md
  else
    log "  ⚠️  topics/ 里没 scored.json，跳过 build 烟测"
  fi
fi

echo
echo "=========================================="
echo "✅ Curio 新设备恢复完成"
echo "=========================================="
echo "  项目路径：$PROJECT_DIR"
echo "  venv：    $VENV_DIR"
echo
echo "验证清单（手动跑一遍）："
echo "  1. cd $PROJECT_DIR && cat profile.yaml | head    # 偏好对不对"
echo "  2. ls topics/*.weekly.*.md | tail -3              # 历史期数在不在"
echo "  3. cat .gh_pat | head -c 10                       # PAT 不是空的"
echo "  4. WorkBuddy 主界面看 3 条 automation 是否在"
echo
echo "下一次自动跑：明早 8:00 daily / 周一 8:00 weekly"
