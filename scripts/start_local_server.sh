#!/usr/bin/env bash
# Curio · 一键启动本机 webhook server + Cloudflare Tunnel
#
# 用法：
#   bash scripts/start_local_server.sh
#
# 这会：
#   1. 启动 Flask（监听 127.0.0.1:8787）
#   2. 启动 cloudflared tunnel（暴露成 https://local.curioradar.fun）
#   3. 两个进程都后台跑，关终端不影响
#   4. 日志写到 .local_server_logs/
#
# 停止：
#   bash scripts/stop_local_server.sh

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PY="/Users/zoezczhou/.workbuddy/binaries/python/envs/curio_sys/bin/python"
LOG_DIR="$ROOT/.local_server_logs"
mkdir -p "$LOG_DIR"

PID_FLASK="$LOG_DIR/flask.pid"
PID_TUNNEL="$LOG_DIR/tunnel.pid"

# 1. 检查 cloudflared 装了没
if ! command -v cloudflared >/dev/null 2>&1; then
    echo "❌ cloudflared 未安装"
    echo ""
    echo "安装方法（任选一个）："
    echo "  brew install cloudflared"
    echo "  或下载：https://github.com/cloudflare/cloudflared/releases"
    exit 1
fi

# 2. 检查是否已有进程在跑
if [ -f "$PID_FLASK" ] && kill -0 "$(cat $PID_FLASK)" 2>/dev/null; then
    echo "⚠️  Flask 已在运行 PID=$(cat $PID_FLASK)"
    echo "   先跑 bash scripts/stop_local_server.sh 停掉再启动"
    exit 1
fi

# 3. 启动 Flask
echo "🛰️  启动 Flask local-server..."
nohup $PY local_server.py > "$LOG_DIR/flask.log" 2>&1 &
echo $! > "$PID_FLASK"
sleep 2

# 检查启动成功
if curl -s -m 3 http://127.0.0.1:8787/health > /dev/null 2>&1; then
    echo "   ✓ Flask 监听 127.0.0.1:8787 (PID $(cat $PID_FLASK))"
else
    echo "   ❌ Flask 启动失败，查看 $LOG_DIR/flask.log"
    exit 1
fi

# 4. 启动 cloudflared tunnel（quick tunnel，URL 不固定）
# 注：完整解决方案是 named tunnel + DNS，但需要 CF account login。
# 这里用 quick tunnel 简单起步，输出的 trycloudflare URL 写到 worker .dev.vars
echo ""
echo "🌐 启动 Cloudflare Tunnel（quick mode）..."
nohup cloudflared tunnel --url http://127.0.0.1:8787 \
    > "$LOG_DIR/tunnel.log" 2>&1 &
echo $! > "$PID_TUNNEL"

echo "   等 cloudflared 给出公网 URL（约 5 秒）..."
sleep 5

# 提取 trycloudflare URL
TUNNEL_URL=$(grep -oE 'https://[^[:space:]]+\.trycloudflare\.com' "$LOG_DIR/tunnel.log" | head -1)
if [ -z "$TUNNEL_URL" ]; then
    echo "   ⚠️ 没拿到 tunnel URL，看日志：tail -30 $LOG_DIR/tunnel.log"
    exit 1
fi

echo "   ✓ Tunnel URL: $TUNNEL_URL (PID $(cat $PID_TUNNEL))"

# 5. 测一下端到端
echo ""
echo "🩺 端到端测试..."
HEALTH=$(curl -s -m 5 "$TUNNEL_URL/health")
if echo "$HEALTH" | grep -q '"ok":true'; then
    echo "   ✓ $TUNNEL_URL/health → $HEALTH"
else
    echo "   ⚠️ tunnel 响应异常: $HEALTH"
fi

# 6. 把 URL 写到 worker .dev.vars + 提示用户重新部署
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✅ 启动完成"
echo ""
echo "下一步：让 Worker 知道 tunnel URL"
echo ""
echo "  1. 编辑 worker/wrangler.toml，在 [vars] 下加："
echo "       LOCAL_TUNNEL_URL = \"$TUNNEL_URL\""
echo ""
echo "  2. 部署 worker："
echo "       cd worker && set -a && source .dev.vars && set +a && \\"
echo "       PATH=\"/Users/zoezczhou/.workbuddy/binaries/node/versions/22.22.2/bin:\$PATH\" \\"
echo "       npx wrangler deploy"
echo ""
echo "之后任何人在 curioradar.fun 点'立刻生成'，Worker 会立即调你这台机器。"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "查看日志："
echo "  tail -f $LOG_DIR/flask.log    # webhook server 收到的请求"
echo "  tail -f $LOG_DIR/tunnel.log   # tunnel 状态"
echo ""
echo "停止：bash scripts/stop_local_server.sh"
