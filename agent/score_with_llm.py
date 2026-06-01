"""
agent/score_with_llm.py

读 topics/unified.score-prompt.md → 调 LLM API → 写 topics/unified.scored.json

设计要点：
- 同一份 prompt 文件给 Claude（本地链路 A）和 LLM API（CI 链路 B），输出 schema 一致
- 默认走 DeepSeek（最便宜、JSON mode 稳），但留了 BYOK 接口可切 OpenAI / Kimi
- 失败 fail-fast：CI 上写不出 scored.json 就退出非 0，工作流直接红
- 不打印 API key（只打前 8 字符）
- 校验输出 JSON 必含 headlines + shortlist，否则报错

环境变量（两套二选一）：

  ## 方式 1（推荐 · BYOK）：从 Curio Worker 拉配置
  CURIO_API_BASE       默认 https://api.curioradar.fun
  CURIO_ADMIN_TOKEN    worker admin token（CI Secret）
  → 自动读取用户在网页"设置"里配的 LLM 配置

  ## 方式 2：环境变量直接给
  LLM_PROVIDER         deepseek（默认） / openai / kimi / zhipu
  DEEPSEEK_API_KEY     DeepSeek key
  OPENAI_API_KEY       OpenAI key（可选）
  MOONSHOT_API_KEY     Kimi key（可选）
  ZHIPU_API_KEY        智谱 key（可选）
  LLM_MODEL            覆盖默认模型名（可选）
  LLM_BASE_URL         覆盖默认 base url（可选，BYOK 用）
"""

from __future__ import annotations
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = ROOT / "topics"
PROMPT_FILE = TOPICS / "unified.score-prompt.md"
SCORED_FILE = TOPICS / "unified.scored.json"


# 各家 provider 默认配置
PROVIDERS = {
    "deepseek": {
        "base_url": "https://api.deepseek.com",
        "model": "deepseek-chat",
        "key_env": "DEEPSEEK_API_KEY",
    },
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o-mini",
        "key_env": "OPENAI_API_KEY",
    },
    "kimi": {
        "base_url": "https://api.moonshot.cn/v1",
        "model": "moonshot-v1-128k",
        "key_env": "MOONSHOT_API_KEY",
    },
    "zhipu": {
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
        "model": "glm-4-flash",
        "key_env": "ZHIPU_API_KEY",
    },
}


def _log(msg: str) -> None:
    print(f"[score_with_llm] {msg}", flush=True)


def _fetch_from_worker() -> dict | None:
    """方式 1：从 Curio Worker /admin/llm-config 拉用户在网页里配的 BYOK"""
    admin_token = os.environ.get("CURIO_ADMIN_TOKEN") or ""
    if not admin_token:
        return None
    base = os.environ.get("CURIO_API_BASE", "https://api.curioradar.fun").rstrip("/")
    url = base + "/admin/llm-config"
    req = urllib.request.Request(
        url,
        method="GET",
        headers={
            "Authorization": "Bearer " + admin_token,
            "User-Agent": "curio-score-bot/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode("utf-8"))
        if not data.get("ok") or not data.get("api_key"):
            _log(f"⚠️ worker 返回无配置：{data}")
            return None
        _log(f"✓ 从 worker 拉到 BYOK：provider={data.get('provider')} model={data.get('model')}")
        return {
            "name": data.get("provider"),
            "model": data.get("model"),
            "base_url": data.get("base_url"),
            "api_key": data.get("api_key"),
        }
    except urllib.error.HTTPError as e:
        if e.code == 404:
            _log("⚠️ worker 上还没配 LLM（404），回退到环境变量")
            return None
        body = e.read().decode("utf-8", errors="replace")
        _log(f"⚠️ worker /admin/llm-config 失败 {e.code}: {body[:200]}")
        return None
    except Exception as e:
        _log(f"⚠️ 连 worker 失败：{e}")
        return None


def _resolve_provider() -> dict:
    # 优先方式 1：worker BYOK
    via_worker = _fetch_from_worker()
    if via_worker and via_worker.get("api_key"):
        return via_worker

    # 方式 2：环境变量
    name = os.environ.get("LLM_PROVIDER", "deepseek").lower()
    if name not in PROVIDERS:
        raise SystemExit(f"❌ 未知 LLM_PROVIDER={name}（合法值：{list(PROVIDERS)}）")
    cfg = dict(PROVIDERS[name])
    cfg["name"] = name
    cfg["base_url"] = os.environ.get("LLM_BASE_URL") or cfg["base_url"]
    cfg["model"] = os.environ.get("LLM_MODEL") or cfg["model"]
    api_key = os.environ.get(cfg["key_env"]) or ""
    if not api_key:
        raise SystemExit(
            f"❌ 既没配 worker BYOK（需 CURIO_ADMIN_TOKEN），也没设 {cfg['key_env']}，无法调用 {name}"
        )
    cfg["api_key"] = api_key
    return cfg


def _call_chat(cfg: dict, prompt: str) -> str:
    """调 OpenAI 兼容 chat completions，返回 content 字符串"""
    url = cfg["base_url"].rstrip("/") + "/chat/completions"
    payload = {
        "model": cfg["model"],
        "messages": [
            {"role": "system",
             "content": "你是一个严格按 JSON schema 输出的资深主编。只返回 JSON，禁止 markdown 包裹、禁止额外文字。"},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.4,
        "response_format": {"type": "json_object"},
        "max_tokens": 8000,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cfg['api_key']}",
        "User-Agent": "curio-score-bot/1.0",
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST", headers=headers)
    _log(f"→ POST {url}  model={cfg['model']}  prompt={len(prompt)} chars")
    t0 = time.time()
    try:
        # 评分 prompt 大 + reasoning 慢，给 5 分钟
        with urllib.request.urlopen(req, timeout=300) as r:
            body = r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"❌ HTTP {e.code}: {body[:500]}")
    except urllib.error.URLError as e:
        raise SystemExit(f"❌ URLError: {e}")
    dt = time.time() - t0
    obj = json.loads(body)
    content = (obj.get("choices") or [{}])[0].get("message", {}).get("content") or ""
    usage = obj.get("usage") or {}
    _log(f"← {dt:.1f}s  prompt_tokens={usage.get('prompt_tokens')} "
         f"completion_tokens={usage.get('completion_tokens')}")
    if not content.strip():
        raise SystemExit(f"❌ LLM 返回空内容：{body[:500]}")
    return content


def _validate_scored(obj: dict) -> None:
    if not isinstance(obj, dict):
        raise SystemExit(f"❌ scored.json 不是 dict：{type(obj)}")
    if "headlines" not in obj or not isinstance(obj["headlines"], list):
        raise SystemExit("❌ scored.json 缺 headlines（应为 list）")
    if len(obj["headlines"]) < 3:
        raise SystemExit(f"❌ headlines 数量太少：{len(obj['headlines'])} < 3")
    if "shortlist" not in obj or not isinstance(obj["shortlist"], list):
        raise SystemExit("❌ scored.json 缺 shortlist（应为 list）")
    required = {"rank", "domain", "title", "lead"}
    for i, h in enumerate(obj["headlines"]):
        miss = required - set(h.keys())
        if miss:
            raise SystemExit(f"❌ headlines[{i}] 缺字段：{miss}")
    _log(f"✓ schema OK  headlines={len(obj['headlines'])}  shortlist={len(obj['shortlist'])}")


def main() -> int:
    if not PROMPT_FILE.exists():
        raise SystemExit(f"❌ {PROMPT_FILE} 不存在 —— 先跑 prepare_unified")
    prompt = PROMPT_FILE.read_text(encoding="utf-8")
    _log(f"prompt 文件：{PROMPT_FILE}（{len(prompt) // 1024}K 字符 ≈ {len(prompt) // 4} token）")

    cfg = _resolve_provider()
    _log(f"provider={cfg['name']}  model={cfg['model']}  key={cfg['api_key'][:8]}...")

    content = _call_chat(cfg, prompt)

    # DeepSeek json_object 模式偶尔会包 markdown ``` 块，剥一层
    s = content.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[-1]
        if s.endswith("```"):
            s = s.rsplit("```", 1)[0]
        s = s.strip()
        if s.lower().startswith("json"):
            s = s[4:].strip()

    try:
        scored = json.loads(s)
    except json.JSONDecodeError as e:
        # 调试用：把原始 content 落盘以便人工 review
        debug = TOPICS / f"unified.scored.raw.{int(time.time())}.txt"
        debug.write_text(content, encoding="utf-8")
        raise SystemExit(f"❌ 返回不是合法 JSON：{e}\n  原始 content 已写入：{debug}")

    _validate_scored(scored)

    # 保留原 _meta（如果之前已存在），加上本次评分元信息
    scored.setdefault("_meta", {})
    scored["_meta"].update({
        "scored_by": f"{cfg['name']}/{cfg['model']}",
        "scored_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    })

    SCORED_FILE.write_text(
        json.dumps(scored, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    _log(f"✅ 已写 {SCORED_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
