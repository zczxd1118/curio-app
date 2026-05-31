"""Curio · 本机 webhook server（方案 A：网页点击 → 立即触发）

让 Cloudflare Worker 通过 Cloudflare Tunnel 直接调本机，触发立即生成，
而不是等 hourly automation 轮询。

启动：
    python local_server.py

监听：
    POST /trigger-generate {"domain_id": "...", "issue_num": ...}

鉴权：
    Header X-Curio-Token 必须等于 ADMIN_TOKEN（与 worker .dev.vars 同）
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path
from threading import Thread

from flask import Flask, jsonify, request
from flask_cors import CORS

ROOT = Path(__file__).resolve().parent
PY = "/Users/zoezczhou/.workbuddy/binaries/python/envs/curio_sys/bin/python"
LOG_DIR = ROOT / ".local_server_logs"
LOG_DIR.mkdir(exist_ok=True)


def _admin_token() -> str:
    """从 worker/.dev.vars 读 ADMIN_TOKEN（与 worker 共用）"""
    dev_vars = ROOT / "worker" / ".dev.vars"
    if not dev_vars.exists():
        return ""
    for line in dev_vars.read_text().splitlines():
        if line.startswith("ADMIN_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"')
    return ""


ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN") or _admin_token()
if not ADMIN_TOKEN:
    print("⚠️  ADMIN_TOKEN 没设——任何人都能触发本机！", file=sys.stderr)


app = Flask(__name__)
CORS(app)

# 当前正在跑的任务（防止并发）
_running = {"task": None, "started_at": None}


def _spawn_run_pending(reason: str = "webhook"):
    """后台跑 ingest_generate + prepare 阶段（不阻塞 HTTP 响应）

    Score/Notes/Finalize 必须靠 WorkBuddy automation 接力（Claude 写 prompt 输出），
    本地脚本只能跑前置阶段。但 prepare 完成后会让下一次 hourly 自动接力。
    """
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_path = LOG_DIR / f"run_{timestamp}.log"

    def _runner():
        with open(log_path, "w", encoding="utf-8") as logf:
            logf.write(f"# Curio local-server triggered run · {reason}\n")
            logf.write(f"# started: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            logf.flush()
            try:
                # 1) ingest_generate（拉 issue → .pending_generate.json + comment "已收到"）
                logf.write("\n=== 1) ingest_generate ===\n"); logf.flush()
                p1 = subprocess.run(
                    [PY, "-m", "agent.worker_sync", "ingest_generate"],
                    cwd=str(ROOT), capture_output=True, text=True, timeout=120,
                )
                logf.write(p1.stdout); logf.write(p1.stderr); logf.flush()

                # 2) process_pending（跑 prepare 给被请求的领域）
                logf.write("\n\n=== 2) process_pending ===\n"); logf.flush()
                p2 = subprocess.run(
                    [PY, str(ROOT / "cli_generate.py"), "process_pending"],
                    cwd=str(ROOT), capture_output=True, text=True, timeout=600,
                )
                logf.write(p2.stdout); logf.write(p2.stderr); logf.flush()

                logf.write(f"\n\n# finished: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                logf.write("# 接下来：WorkBuddy automation 在 hourly 间隔会跑 score/notes/finalize\n")
            except subprocess.TimeoutExpired as e:
                logf.write(f"\n[TIMEOUT] {e}\n")
            except Exception as e:
                logf.write(f"\n[ERROR] {e}\n")
            finally:
                _running["task"] = None
                _running["started_at"] = None

    _running["task"] = log_path.name
    _running["started_at"] = time.time()
    t = Thread(target=_runner, daemon=True)
    t.start()
    return log_path.name


@app.route("/health", methods=["GET"])
def health():
    """无鉴权，给 worker / curl 探活用"""
    return jsonify({
        "ok": True,
        "service": "curio-local-server",
        "ts": time.time(),
        "running": _running["task"],
    })


@app.route("/trigger-generate", methods=["POST"])
def trigger_generate():
    """Worker 收到 /trigger-generate → 网页点击 → 这里被调用 → 后台跑 prepare"""
    auth = request.headers.get("X-Curio-Token", "")
    if not ADMIN_TOKEN or auth != ADMIN_TOKEN:
        return jsonify({"ok": False, "error": "unauthorized"}), 401

    if _running["task"]:
        elapsed = int(time.time() - (_running["started_at"] or time.time()))
        return jsonify({
            "ok": True,
            "queued": False,
            "message": f"已有任务在跑（{elapsed} 秒前启动），新请求会被下一轮 ingest 拿到",
            "running": _running["task"],
        })

    body = request.get_json(silent=True) or {}
    reason = f"webhook · domain={body.get('domain_id', '?')} · issue=#{body.get('issue_num', '?')}"

    log_name = _spawn_run_pending(reason=reason)
    return jsonify({
        "ok": True,
        "queued": True,
        "log": log_name,
        "message": "已开始处理，5-10 分钟内 Claude 接力完成生成",
    })


@app.route("/trigger-generate", methods=["GET"])
def trigger_generate_get():
    """简单状态页（不会真触发）"""
    if _running["task"]:
        elapsed = int(time.time() - (_running["started_at"] or time.time()))
        return jsonify({"running": _running["task"], "elapsed_sec": elapsed})
    return jsonify({"running": None, "message": "idle"})


if __name__ == "__main__":
    port = int(os.environ.get("CURIO_LOCAL_PORT", "8787"))
    host = os.environ.get("CURIO_LOCAL_HOST", "127.0.0.1")
    print(f"🛰️  Curio local-server: http://{host}:{port}")
    print(f"   ADMIN_TOKEN: {'<set>' if ADMIN_TOKEN else '<MISSING — server is open!>'}")
    print(f"   logs: {LOG_DIR}")
    app.run(host=host, port=port, debug=False)
