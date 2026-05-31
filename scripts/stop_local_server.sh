#!/usr/bin/env bash
# 停止 Curio 本机 webhook server + Cloudflare Tunnel

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$ROOT/.local_server_logs"
PID_FLASK="$LOG_DIR/flask.pid"
PID_TUNNEL="$LOG_DIR/tunnel.pid"

stop() {
    local name="$1" pidfile="$2"
    if [ -f "$pidfile" ]; then
        local pid=$(cat "$pidfile")
        if kill -0 "$pid" 2>/dev/null; then
            kill "$pid" 2>/dev/null
            echo "  ✓ $name (PID $pid) 已停止"
        else
            echo "  · $name PID $pid 已不在运行"
        fi
        rm -f "$pidfile"
    else
        echo "  · $name 没在跑（无 pid 文件）"
    fi
}

echo "🛑 停止 Curio local-server..."
stop "Flask" "$PID_FLASK"
stop "Tunnel" "$PID_TUNNEL"

# 兜底：杀所有 cloudflared 和 local_server.py 进程
pkill -f "cloudflared tunnel --url http://127.0.0.1:8787" 2>/dev/null && echo "  ✓ 兜底杀 cloudflared" || true
pkill -f "python.*local_server.py" 2>/dev/null && echo "  ✓ 兜底杀 local_server.py" || true

echo "✅ 已停止"
