# Curio 本机 Webhook Server（方案 A：点击立即触发）

让 [curioradar.fun](https://curioradar.fun/) 上点"⚡ 立刻生成"按钮的人**5-10 分钟内**看到结果，
而不是等 hourly automation 轮询（最坏 1 小时）。

## 工作原理

```
用户点"⚡ 立刻生成"
   ↓
网页 JS fetch https://api.curioradar.fun/trigger-generate
   ↓
Cloudflare Worker 收到请求
   ↓
转发到 https://*.trycloudflare.com/trigger-generate（Cloudflare Tunnel）
   ↓
Tunnel 把请求路由到本机 http://127.0.0.1:8787（Flask）
   ↓
Flask 后台跑 ingest_generate + process_pending（5-10 分钟）
   ↓
issue 评论"✅ 已生成" + 邮件通知
```

## 前置：装 cloudflared（一次性）

```bash
brew install cloudflared
```

## 日常使用

### 启动（电脑开机 / 想"开门营业"时跑一次）

```bash
cd /Users/zoezczhou/WorkBuddy/2026-05-29-15-27-22/content-curator
bash scripts/start_local_server.sh
```

会输出类似：
```
🛰️  启动 Flask local-server...
   ✓ Flask 监听 127.0.0.1:8787
🌐 启动 Cloudflare Tunnel（quick mode）...
   ✓ Tunnel URL: https://lazy-fox-1234.trycloudflare.com
🩺 端到端测试...
   ✓ /health → {"ok":true,...}
```

**关键**：把脚本输出里那个 `https://xxxxx.trycloudflare.com` 复制下来，加到 `worker/wrangler.toml`：

```toml
[vars]
LOCAL_TUNNEL_URL = "https://lazy-fox-1234.trycloudflare.com"
```

然后部署 worker：

```bash
cd worker
set -a && source .dev.vars && set +a
PATH="/Users/zoezczhou/.workbuddy/binaries/node/versions/22.22.2/bin:$PATH" \
  npx wrangler deploy
```

部署后任何人在 curioradar.fun 点"立刻生成" → 直接调你这台机器。

### 停止（电脑关机前 / 不想被打扰时跑）

```bash
bash scripts/stop_local_server.sh
```

### 查看日志

```bash
# Flask 收到的请求 + 跑 prepare 的输出
tail -f .local_server_logs/flask.log

# 每次触发的具体执行日志
ls .local_server_logs/run_*.log
tail -f .local_server_logs/run_2026-05-31_*.log

# Tunnel 状态
tail -f .local_server_logs/tunnel.log
```

## 限制

### Quick Tunnel URL 每次重启会变

`cloudflared tunnel --url` 模式给的是临时 URL（`*.trycloudflare.com`），重启后 URL 会变。
每次重启 server 都需要：
1. 复制新 URL
2. 改 `wrangler.toml`
3. redeploy worker

如果嫌麻烦，可以升级到 **Named Tunnel**：URL 固定，但需要 Cloudflare 账号绑定 + DNS 配置。

### Flask 是 dev server

`flask run` 是开发服务器，单线程、无优雅重启、性能不高，但对 Curio 这种**低 QPS 场景完全够**（每天 < 100 次触发）。

如果以后量大了再换 gunicorn / uwsgi。

### 必须本机开着

如果你电脑关了 / 睡眠了，tunnel 断开，Worker 转发会失败 → **自动 fallback 到 GitHub Issue 路径**，hourly automation 兜底（最长 1 小时延迟）。这是预期行为：本机开 = 即时；关 = 慢路径。

## 故障排查

### "本机不可达"

1. 检查 Flask 在跑：`curl http://127.0.0.1:8787/health` 应返回 `{"ok":true}`
2. 检查 Tunnel 在跑：`curl https://your-tunnel-url.trycloudflare.com/health`
3. 检查 wrangler.toml 的 `LOCAL_TUNNEL_URL` 跟当前 tunnel URL 一致
4. 检查 `pgrep -f cloudflared` 有进程

### "401 unauthorized"

Worker 端 `ADMIN_TOKEN` 跟本机 `worker/.dev.vars` 里的 `ADMIN_TOKEN` 必须一致。

### 触发了但没出新简报

1. 看 `.local_server_logs/run_*.log` 最新一份
2. 看 `_run_plan.json` 是否生成了
3. WorkBuddy 自动跑 score/notes/finalize（这部分仍依赖 hourly automation 接力，本机 server 只跑 prepare）

## 长期思考

**当前架构**：Worker → Tunnel → 本机 Flask → 跑 prepare → 等 WorkBuddy 跑 Claude 接力

**可能的演进**：

| 方案 | 优点 | 代价 |
|---|---|---|
| 当前 | 免费、不付 LLM API | 本机必须开 |
| Anthropic API + GitHub Actions | 24/7 不依赖本机 | 月费 $20-50 |
| 商用 LLM（DeepSeek 等） | 中间方案 | 月费 $5-20 |
