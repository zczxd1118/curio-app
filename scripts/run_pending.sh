#!/usr/bin/env bash
# Curio · 立即处理待生成请求
#
# 当用户在网页点了"⚡ 立刻生成"，本机如果开着且不想等 hourly automation，
# 跑这个脚本就立刻处理所有 pending 的 [curio-generate] Issue。
#
# 用法：
#   bash scripts/run_pending.sh
#
# 流程：
#   1. ingest GitHub Issue → 写 .pending_generate.json
#   2. 跑 prepare（仅那些被请求的领域）
#   3. 提示你接手 score / notes / finalize（让 Claude 通过 WorkBuddy 接力）

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PY="/Users/zoezczhou/.workbuddy/binaries/python/envs/curio_sys/bin/python"

if [ ! -x "$PY" ]; then
    echo "❌ Python 环境不存在: $PY"
    exit 1
fi

echo "🛰️  Curio · 立即处理 pending"
echo "   $(date '+%H:%M:%S')"
echo ""

# 拉 issue → 写 .pending_generate.json + 在 issue 评论"已收到"
echo "📥 ingest [curio-generate] issues..."
$PY -m agent.worker_sync ingest_generate

if [ ! -f ".pending_generate.json" ]; then
    echo "（无 pending）"
    exit 0
fi

PENDING_COUNT=$($PY -c "import json; print(len(json.load(open('.pending_generate.json')).get('pending', [])))")

if [ "$PENDING_COUNT" -eq 0 ]; then
    echo "（pending 列表为空）"
    exit 0
fi

echo "   📌 $PENDING_COUNT 个领域待生成"
echo ""

# 跑 process_pending（这会跑 prepare 但只针对那几个领域）
echo "🚀 跑 prepare（仅 pending 领域）..."
$PY cli_generate.py process_pending

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✅ prepare 完成。下一步需要 Claude 接手（WorkBuddy 自动跑或手动）"
echo ""
echo "如果你想现在等下一次 automation（最长 1 小时），就什么都不用做。"
echo ""
echo "如果想立刻跑完整链路：在 WorkBuddy 里手动触发"
echo "  'Curio 用户生成请求处理' automation"
echo "  （它会读 _run_plan.json，让 Claude 写 scored.json → notes → finalize）"
echo "═══════════════════════════════════════════════════════════════"
