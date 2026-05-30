#!/usr/bin/env bash
# Curio 一键部署脚本
# 用法：bash deploy.sh <你的 github 用户名>
# 例：bash deploy.sh zoezczhou

set -e

USER="${1:-}"
if [ -z "$USER" ]; then
  echo "用法：bash deploy.sh <你的 github 用户名>"
  echo "例：bash deploy.sh zoezczhou"
  exit 1
fi

REPO="curio-site"
ROOT="$(cd "$(dirname "$0")" && pwd)"
SITE_DIR="$ROOT/site"

echo "🛰️  Curio 部署脚本"
echo "   用户：$USER"
echo "   仓库：$REPO"
echo "   静态目录：$SITE_DIR"
echo

# 1. 重 build site 确保最新
echo "📦 1/5 重新构建 site/..."
cd "$ROOT"
/Users/zoezczhou/.workbuddy/binaries/python/envs/curio_sys/bin/python agent/render_site.py 2>&1 | tail -3

# 2. 进 site/ 目录创建独立 git repo（GitHub Pages 用）
echo
echo "📦 2/5 准备 site/ 作为独立 git 仓库..."
cd "$SITE_DIR"
if [ ! -d .git ]; then
  git init -q
  git checkout -q -b main 2>/dev/null || git checkout -q main
fi
# 确保有 .nojekyll（GitHub Pages 默认不渲染 _ 开头的目录）
touch .nojekyll

# 3. 配 origin
echo "📦 3/5 配置 GitHub remote..."
REMOTE_URL="https://github.com/$USER/$REPO.git"
git remote remove origin 2>/dev/null || true
git remote add origin "$REMOTE_URL"

# 4. commit
echo "📦 4/5 commit..."
git add -A
git commit -q -m "Curio site $(date +%Y-%m-%d-%H%M)" || echo "（无变化）"

# 5. push
echo
echo "📦 5/5 准备 push 到 $REMOTE_URL"
echo
echo "   👉 接下来你需要手动执行（首次推送需登录）："
echo
echo "      cd $SITE_DIR"
echo "      git push -u origin main --force"
echo
echo "   然后去：https://github.com/$USER/$REPO/settings/pages"
echo "   把 Source 设为 'Deploy from a branch' / branch=main / folder=/(root)"
echo "   等 1-2 分钟，访问："
echo
echo "      🌐 https://$USER.github.io/$REPO/"
echo
echo "✅ 准备完成。如果 $REPO 还没创建，先去 https://github.com/new 建空仓库（名字必须叫 $REPO）"
