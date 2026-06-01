"""
agent/worker_sync.py

把生成端（本机）和 Cloudflare Worker (curio-api) 之间的数据通起来：

1. sync_domains  —— 把 sources.yaml 的领域信息推到 KV (domains:list / domains:meta)
2. push_content  —— 把每期 weekly/daily 的 must_read 拼成 HTML 块推到 KV (content:{slug}:latest)
3. broadcast     —— 调 worker /broadcast，让 worker 按订阅者偏好群发 (Resend 实际发邮件)
4. ingest_subscribe_issues —— 兜底：拉 GitHub label=curio-subscribe 的 Issue，转成 /subscribe 调用
5. ingest_add_domain_issues —— 拉 label=curio-add-domain 的 Issue，加入 sources.yaml

环境变量：
- CURIO_API_BASE     公网 worker 地址（默认 https://curio-api.zczxd1118.workers.dev，绑域名后改）
- CURIO_ADMIN_TOKEN  admin endpoint 鉴权（与 worker 注入的 ADMIN_TOKEN 一致）

CLI:
    python -m agent.worker_sync sync_domains
    python -m agent.worker_sync push_content
    python -m agent.worker_sync broadcast --cadence weekly [--dry-run]
    python -m agent.worker_sync ingest_subscribe
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Any, Optional

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.yaml"
TOPICS = ROOT / "topics"
WORKER_DEV_VARS = ROOT / "worker" / ".dev.vars"


# ============== utils ==============

def _load_dev_vars() -> dict:
    out = {}
    if WORKER_DEV_VARS.exists():
        for line in WORKER_DEV_VARS.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip()
    return out


def _env() -> dict:
    """合并 os.environ 和 .dev.vars，os.environ 优先"""
    base = _load_dev_vars()
    base.update({k: v for k, v in os.environ.items() if k.startswith("CURIO_") or k in ("ADMIN_TOKEN",)})
    return base


def _api_base() -> str:
    env = _env()
    return env.get("CURIO_API_BASE", "https://curio-api.zczxd1118.workers.dev").rstrip("/")


def _admin_token() -> str:
    env = _env()
    tok = env.get("CURIO_ADMIN_TOKEN") or env.get("ADMIN_TOKEN") or ""
    if not tok:
        raise RuntimeError(
            "未配置 ADMIN_TOKEN：请在 worker/.dev.vars 写 ADMIN_TOKEN=xxx 或设环境变量 CURIO_ADMIN_TOKEN"
        )
    return tok


def _http(method: str, path: str, body: Optional[dict] = None,
          admin: bool = False, timeout: int = 20) -> tuple[int, dict]:
    url = _api_base() + path
    data = None
    headers = {
        "Content-Type": "application/json",
        # Cloudflare 的 Bot Fight Mode 会拦 Python urllib 默认 UA，伪装成 curl
        "User-Agent": "curio-bot/1.0 (+https://github.com/zczxd1118/curio-app)",
    }
    if admin:
        headers["Authorization"] = "Bearer " + _admin_token()
    if body is not None:
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            payload = json.loads(e.read().decode("utf-8"))
        except Exception:
            payload = {"error": str(e)}
        return e.code, payload
    except Exception as e:
        return 0, {"error": "network: " + str(e)}


def _log(msg: str):
    print(msg, flush=True)


# ============== 1. sync_domains ==============

def sync_domains() -> int:
    if not SOURCES.exists():
        _log("❌ 找不到 sources.yaml")
        return 1
    cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}
    domains = cfg.get("domains") or {}
    if not isinstance(domains, dict):
        _log("❌ sources.yaml domains 不是 dict 格式")
        return 1

    ids = list(domains.keys())
    meta = {}
    for did, dcfg in domains.items():
        if not isinstance(dcfg, dict):
            continue
        meta[did] = {
            "name": dcfg.get("name", did),
            "icon": dcfg.get("icon", "📰"),
            "frequency": dcfg.get("frequency", "weekly"),
        }

    _log(f"🛰️  推送 {len(ids)} 个领域到 worker KV: {ids}")
    code, body = _http("POST", "/admin/sync-domains",
                       body={"domains": ids, "meta": meta}, admin=True)
    if code != 200:
        _log(f"❌ 失败: HTTP {code}: {body}")
        return 1
    _log(f"✅ {body}")
    return 0


# ============== 2. push_content ==============

def _scored_to_html_block(scored: dict, domain_name: str, domain_icon: str) -> str:
    """把 scored.json 的 must_read 拼成一段邮件可读 HTML（老格式，兼容用）"""
    must = scored.get("must_read") or []
    if not must:
        return ""
    items_html = []
    for it in must:
        title = (it.get("title") or "").replace("<", "&lt;").replace(">", "&gt;")
        url = it.get("url") or ""
        why = (it.get("why_recommend") or "").replace("<", "&lt;").replace(">", "&gt;")
        platform = it.get("platform") or ""
        items_html.append(
            f"""<li style="margin-bottom:14px">
              <a href="{url}" style="color:#1a1a1c;font-weight:600;font-size:15px;text-decoration:none">{title}</a>
              <span style="color:#888;font-size:11px;margin-left:6px">{platform}</span>
              <div style="color:#555;font-size:13px;margin-top:4px">{why}</div>
            </li>"""
        )
    return f"""<section style="margin-bottom:32px">
      <h2 style="font-size:18px;border-bottom:1px solid #ddd;padding-bottom:6px;margin-bottom:12px">
        {domain_icon} {domain_name}
      </h2>
      <ul style="list-style:none;padding:0;margin:0">{''.join(items_html)}</ul>
    </section>"""


def _unified_to_html_blocks(scored: dict, domain_to_slug: dict, domains_cfg: dict) -> dict[str, str]:
    """unified.scored.json → 每域一个 HTML 块（按域分组，复用 worker broadcast 链路）

    Returns: {slug: html_block}
    """
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(ROOT))
    try:
        from agent.build_radar_md import _render_headline_html, _fuzzy_match_domain
    except Exception:
        return {}

    headlines = scored.get("headlines") or []
    shortlist = scored.get("shortlist") or []

    # 按 slug 分组
    by_slug_h: dict[str, list] = {}
    by_slug_s: dict[str, list] = {}

    def resolve_slug(domain_text: str) -> str | None:
        """中文/英文 domain → slug"""
        if not domain_text:
            return None
        # 直接命中
        if domain_text in domain_to_slug:
            return domain_to_slug[domain_text]
        if domain_text in domains_cfg:
            return domain_text
        # fuzzy
        for slug in domains_cfg:
            if _fuzzy_match_domain(domain_text, slug):
                return slug
        return None

    for h in headlines:
        slug = resolve_slug(h.get("domain", ""))
        if slug:
            by_slug_h.setdefault(slug, []).append(h)

    for s in shortlist:
        slug = resolve_slug(s.get("domain", ""))
        if slug:
            by_slug_s.setdefault(slug, []).append(s)

    # 渲染每域 HTML
    out = {}
    for slug in set(by_slug_h.keys()) | set(by_slug_s.keys()):
        dcfg = domains_cfg.get(slug, {}) or {}
        domain_name = dcfg.get("name") or slug

        parts = [f'<section style="margin-bottom:36px">']
        parts.append(
            f'<h2 style="font-size:20px;border-bottom:2px solid #d4af37;padding-bottom:6px;margin-bottom:14px">'
            f'🌟 {domain_name}</h2>'
        )

        # 头条
        for h in by_slug_h.get(slug, []):
            parts.append(_render_headline_html(h))

        # 备选
        sl = by_slug_s.get(slug, [])
        if sl:
            parts.append('<div style="margin-top:18px"><strong style="color:#666;font-size:14px">📋 备选阅读</strong><ul style="padding-left:20px;color:#444;font-size:13px;margin-top:8px">')
            for it in sl:
                title = (it.get("title") or "").replace("<", "&lt;").replace(">", "&gt;")
                url = it.get("url") or ""
                one_liner = (it.get("one_liner") or "").replace("<", "&lt;").replace(">", "&gt;")
                if url:
                    parts.append(f'<li style="margin-bottom:6px"><a href="{url}" style="color:#1a1a1c">{title}</a>'
                                 + (f' —— <span style="color:#666">{one_liner}</span>' if one_liner else "") + "</li>")
                else:
                    parts.append(f'<li style="margin-bottom:6px">{title}'
                                 + (f' —— <span style="color:#666">{one_liner}</span>' if one_liner else "") + "</li>")
            parts.append("</ul></div>")

        parts.append("</section>")
        out[slug] = "\n".join(parts)

    return out


def push_content() -> int:
    if not SOURCES.exists():
        _log("❌ 找不到 sources.yaml")
        return 1
    cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}
    domains_cfg = cfg.get("domains") or {}

    # 优先：如果有 unified.scored.json，按 unified 模式拆分推送
    unified_path = TOPICS / "unified.scored.json"
    if unified_path.exists():
        try:
            scored = json.loads(unified_path.read_text(encoding="utf-8"))
            mtime_age_min = (time.time() - unified_path.stat().st_mtime) / 60
            if mtime_age_min < 120:  # 2 小时内的才用
                _log(f"📤 push_content: unified 模式（unified.scored.json 是 {mtime_age_min:.0f} 分钟前生成）")
                # 构建 name → slug 反查
                name_to_slug = {}
                for slug, dcfg in domains_cfg.items():
                    name_to_slug[(dcfg or {}).get("name", slug)] = slug
                    name_to_slug[slug] = slug

                blocks = _unified_to_html_blocks(scored, name_to_slug, domains_cfg)
                pushed = skipped = 0
                for slug, html in blocks.items():
                    dcfg = domains_cfg.get(slug, {}) or {}
                    body_payload = {
                        "slug": slug,
                        "content": {
                            "html": html,
                            "domain": dcfg.get("name", slug),
                            "must_count": 1,
                            "generated_at": time.strftime("%Y-%m-%d %H:%M"),
                        },
                    }
                    code, resp = _http("POST", "/admin/push-content", body=body_payload, admin=True)
                    if code == 200:
                        _log(f"  ✅ {slug} ({dcfg.get('name', slug)}): pushed (unified)")
                        pushed += 1
                    else:
                        _log(f"  ❌ {slug}: HTTP {code}: {resp}")
                        skipped += 1
                _log(f"\n📊 unified 推送完成：{pushed} 成功 / {skipped} 跳过")
                if pushed > 0:
                    return 0
                # 0 个推送 = unified 没匹配到任何域，fall through 到老逻辑
                _log("  ⚠️ unified 模式没匹配到任何域，fallback 到老 *.scored.json 模式")
        except Exception as e:
            _log(f"⚠️ unified 模式失败: {e}，fallback 到老 *.scored.json 模式")

    # 老模式：扫 *.scored.json 单独推
    # 反查 slug → domain_id（多路径）
    name_to_id = {}
    topic_to_id = {}
    zh_slug_to_id = {}
    import re as _re
    for did, dcfg in domains_cfg.items():
        if not isinstance(dcfg, dict):
            continue
        name_to_id[dcfg.get("name", did)] = did
        for tid in (dcfg.get("topics") or {}):
            topic_to_id[tid] = did
        # 中文名 slugify (例如 "金融" → "金融", "大厂讯息" → "大厂讯息")
        zh = _re.sub(r"[^\w\u4e00-\u9fa5]+", "-", dcfg.get("name", "").lower()).strip("-")
        if zh:
            zh_slug_to_id[zh] = did

    pushed = 0
    skipped = 0
    seen_domain_ids = set()
    for f in TOPICS.glob("*.scored.json"):
        slug = f.stem.replace(".scored", "")
        try:
            scored = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            _log(f"  跳过 {f.name}: {e}")
            skipped += 1
            continue

        # 反查 domain_id：优先 slug 直接是 domain_id，再 topic_id 反查，再 name 反查，再中文 slug
        domain_name = scored.get("domain") or slug
        if slug in domains_cfg:
            domain_id = slug
        elif slug in topic_to_id:
            domain_id = topic_to_id[slug]
        elif domain_name in name_to_id:
            domain_id = name_to_id[domain_name]
        elif slug in zh_slug_to_id:
            domain_id = zh_slug_to_id[slug]
        else:
            domain_id = slug
        dcfg = domains_cfg.get(domain_id) or {}
        domain_icon = dcfg.get("icon", "📰")
        # 优先用 sources.yaml 里的 name（中文/正式名）而不是 scored.json 里随手写的 "vibe coding"
        if dcfg.get("name"):
            domain_name = dcfg["name"]

        # 同一 domain_id 多个文件时去重，避免后到的 scored 覆盖（但日志要警告）
        if domain_id in seen_domain_ids:
            _log(f"  ⚠️ {domain_id} 已被推过（来自更早的 scored.json），跳过 {f.name}")
            skipped += 1
            continue
        seen_domain_ids.add(domain_id)

        html = _scored_to_html_block(scored, domain_name, domain_icon)
        if not html:
            _log(f"  {domain_id}: must_read 为空，跳过")
            skipped += 1
            continue

        body_payload = {
            "slug": domain_id,
            "content": {
                "html": html,
                "domain": domain_name,
                "must_count": len(scored.get("must_read") or []),
                "generated_at": time.strftime("%Y-%m-%d %H:%M"),
            },
        }
        code, resp = _http("POST", "/admin/push-content", body=body_payload, admin=True)
        if code == 200:
            _log(f"  ✅ {domain_id} ({domain_name}): pushed")
            pushed += 1
        else:
            _log(f"  ❌ {domain_id}: HTTP {code}: {resp}")
            skipped += 1

    _log(f"\n📊 推送完成：{pushed} 成功 / {skipped} 跳过")
    return 0 if pushed > 0 else 1


# ============== 3. broadcast ==============

def broadcast(cadence: str, dry_run: bool = False) -> int:
    if cadence not in ("daily", "weekly"):
        _log("❌ cadence 必须是 daily 或 weekly")
        return 1
    _log(f"📢 触发 {cadence} 广播 (dry_run={dry_run})")
    code, body = _http("POST", "/broadcast",
                       body={"cadence": cadence, "dry_run": dry_run},
                       admin=True, timeout=120)
    if code != 200:
        _log(f"❌ HTTP {code}: {body}")
        return 1
    _log(f"✅ sent={body.get('sent')} skipped={body.get('skipped')} failed={body.get('failed')}")
    if body.get("errors"):
        for e in body["errors"]:
            _log(f"   error: {e}")
    return 0


# ============== 4. ingest GitHub Issue 兜底（订阅 / 加领域）==============

def _gh_api(path: str, method: str = "GET", body: Optional[dict] = None) -> Any:
    """读 GitHub Token 的优先级（兼容本地 + CI）：
       1. GH_TOKEN 环境变量（GitHub Actions 自动注入）
       2. GITHUB_TOKEN 环境变量（保险）
       3. .gh_pat 文件（本地开发用）
    """
    pat = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not pat:
        pat_file = ROOT / ".gh_pat"
        if not pat_file.exists():
            raise RuntimeError("找不到 GitHub token：未设 GH_TOKEN env，也没有 .gh_pat 文件")
        pat = pat_file.read_text(encoding="utf-8").strip()
    url = "https://api.github.com" + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": "Bearer " + pat,
        "Accept": "application/vnd.github+json",
        "User-Agent": "curio-bot",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())


def _list_open_issues(label: str, repo: str = "zczxd1118/curio-app"):
    return _gh_api(f"/repos/{repo}/issues?state=open&labels={label}&per_page=50")


def _close_issue(num: int, comment: str, label_add: str = "curio-ingested",
                 repo: str = "zczxd1118/curio-app"):
    if comment:
        _gh_api(f"/repos/{repo}/issues/{num}/comments", "POST", {"body": comment})
    if label_add:
        _gh_api(f"/repos/{repo}/issues/{num}/labels", "POST", {"labels": [label_add]})
    _gh_api(f"/repos/{repo}/issues/{num}", "PATCH", {"state": "closed"})


def _parse_yaml_block(body: str) -> dict:
    """提取 ```yaml ... ``` 段；如果没有，尝试解析裸的 'key: value' 行（兼容前端发的格式）"""
    import re
    body = body or ""
    # 1. 优先 ```yaml ... ``` 段
    m = re.search(r"```yaml\s*\n(.+?)\n```", body, re.DOTALL)
    if m:
        try:
            return yaml.safe_load(m.group(1)) or {}
        except Exception:
            pass
    # 2. fallback：扫所有行，提取 "type: xxx" / "domain_id: xxx" 这种 key: value
    out: dict = {}
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("<!--") or line.startswith("---"):
            continue
        m2 = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(.+?)$", line)
        if m2:
            key, val = m2.group(1), m2.group(2).strip()
            if val and val != "none":
                out[key] = val
    return out


def ingest_subscribe_issues() -> int:
    """处理 [curio-subscribe] Issue：转成 /subscribe 调用"""
    try:
        issues = _list_open_issues("curio-subscribe")
    except Exception as e:
        _log(f"❌ 拉取 Issue 失败：{e}")
        return 1

    if not issues:
        _log("（没有待处理的订阅 Issue）")
        return 0

    ok = fail = 0
    for issue in issues:
        num = issue["number"]
        body = issue.get("body") or ""
        data = _parse_yaml_block(body)
        email = (data.get("email") or "").strip()
        domains = data.get("domains") or []
        cadence = (data.get("cadence") or "weekly").strip()

        if not email or not domains:
            _log(f"  #{num}: 缺 email 或 domains，跳过")
            fail += 1
            continue

        code, resp = _http("POST", "/subscribe",
                           body={"email": email, "domains": domains, "cadence": cadence})
        if code == 200:
            _log(f"  ✅ #{num} {email} → {resp.get('status')}")
            try:
                _close_issue(num, comment=f"已转 worker：{resp.get('message','')}", label_add="curio-ingested")
            except Exception as e:
                _log(f"     close 失败: {e}")
            ok += 1
        else:
            _log(f"  ❌ #{num}: HTTP {code}: {resp}")
            fail += 1

    _log(f"\n📊 ingest 完成：{ok} 成功 / {fail} 失败")
    return 0


def ingest_generate_issues() -> int:
    """处理 [curio-generate] Issue：把请求列表写到 .pending_generate.json，
    实际跑生成由 cli_generate 决定（防止 ingest 阶段就阻塞太久）。
    """
    try:
        issues = _list_open_issues("curio-generate")
    except Exception as e:
        _log(f"❌ 拉取 Issue 失败：{e}")
        return 1
    if not issues:
        _log("（没有待处理的生成 Issue）")
        # 清空 pending 文件
        out = ROOT / ".pending_generate.json"
        if out.exists():
            out.write_text(json.dumps({"updated_at": time.strftime("%Y-%m-%d %H:%M"), "pending": []},
                                      ensure_ascii=False, indent=2), encoding="utf-8")
        return 0

    # 同一领域去重
    seen_domain = set()
    pending = []
    for issue in issues:
        num = issue["number"]
        body = issue.get("body") or ""
        data = _parse_yaml_block(body)
        domain_id = (data.get("domain_id") or "").strip()
        if not domain_id:
            _log(f"  #{num}: 缺 domain_id，跳过")
            continue
        if domain_id in seen_domain:
            _log(f"  #{num}: 同一领域已排队，合并")
            try:
                _close_issue(num, comment="已合并到先前的同领域请求中。",
                             label_add="curio-ingested")
            except Exception:
                pass
            continue
        seen_domain.add(domain_id)
        pending.append({
            "issue": num,
            "domain_id": domain_id,
            "domain_name": data.get("domain_name") or domain_id,
            "notify_email": data.get("notify_email"),
            "note": data.get("note"),
        })
        _log(f"  📥 #{num}: 排队 {domain_id}")

        # 给用户一条"Agent 已收到，开始跑了"评论（按 mode 区分文案）
        try:
            domain_name = data.get("domain_name") or domain_id
            note = (data.get("note") or "").strip()
            note_part = f"\n\n你的留言：> {note}" if note else ""

            # 拉当前 scoring_mode 决定文案
            mode = "local"
            try:
                import urllib.request as _urlreq
                req = _urlreq.Request("https://api.curioradar.fun/scoring-mode")
                with _urlreq.urlopen(req, timeout=5) as r:
                    mode = (json.loads(r.read().decode()).get("scoring_mode") or "local")
            except Exception:
                pass

            if mode == "api":
                flow_text = "抓取候选 → DeepSeek API 评分 → 中文摘要 → 渲染网站 → 邮件通知"
                eta_text = "**预计 5-7 分钟**（CI 全云端跑）"
            elif mode == "off":
                flow_text = "⏸ 当前模式为「暂停」"
                eta_text = "**未启用** —— 请去 ⚙️ 设置切换到「API」或「本地」"
            else:
                flow_text = "抓取候选 → Claude 评分（本地 WorkBuddy）→ 中文摘要 → 渲染网站 → 邮件通知"
                eta_text = "**预计 5-65 分钟**（等本地 hourly automation 跑）"

            _gh_api(
                f"/repos/zczxd1118/curio-app/issues/{num}/comments",
                "POST",
                {"body": (
                    f"🤖 **Curio Agent 已收到请求**\n\n"
                    f"开始为「{domain_name}」（id=`{domain_id}`）抓取最新内容。{note_part}\n\n"
                    f"评分模式：`{mode}`\n"
                    f"流程：{flow_text}\n"
                    f"⏱ {eta_text}\n\n"
                    f"完成后会再评论一条带访问链接，并自动关闭本 Issue。"
                )},
            )
        except Exception as e:
            _log(f"     ⚠️ 评论失败：{e}（继续处理）")

    out = ROOT / ".pending_generate.json"
    out.write_text(json.dumps({"updated_at": time.strftime("%Y-%m-%d %H:%M"),
                                "pending": pending}, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    _log(f"\n📝 写入 {out}")
    _log(f"📊 ingest_generate 完成：{len(pending)} 个待处理领域")
    return 0


def close_generate_issue(issue_num: int, success: bool = True, message: str = "",
                         domain_id: str = None, verify: bool = True):
    """生成跑完后调用，关闭对应 Issue。

    verify=True 时会校验产出文件是否真的更新（today 这一期 md 文件存在且 mtime 在 1 小时内）——
    避免出现"Agent 评论已生成但实际啥也没做"的虚假承诺。失败时不关 issue，只评论提示重试。
    """
    import time as _time

    # Step 1: 真实性校验
    if success and verify and domain_id:
        today = _time.strftime("%Y-%m-%d")
        md_path = ROOT / "topics" / f"{domain_id}.weekly.{today}.md"
        if not md_path.exists():
            success = False
            message = f"未找到产出文件 topics/{domain_id}.weekly.{today}.md（生成链路实际未跑通）"
        else:
            mtime = md_path.stat().st_mtime
            age_min = (_time.time() - mtime) / 60
            if age_min > 60:
                success = False
                message = f"产出文件 {md_path.name} 过期 {age_min:.0f} 分钟（不是本次生成）"

    # Step 2: 根据真实性决定关 / 不关
    try:
        if success:
            comment = "✅ 已生成，访问 https://curioradar.fun/ 查看。"
            _close_issue(issue_num, comment=comment, label_add="curio-ingested")
        else:
            comment = (
                f"⚠️ 本次未完整生成新内容：{message}\n\n"
                f"Issue 暂保持 open，下个整点 Agent 会重试。如反复失败请反馈给作者。"
            )
            try:
                _gh_api(
                    f"/repos/zczxd1118/curio-app/issues/{issue_num}/comments",
                    "POST",
                    {"body": comment},
                )
                _log(f"  #{issue_num} 标记失败但保持 open（待重试）")
            except Exception as e:
                _log(f"comment failed issue {issue_num}: {e}")
    except Exception as e:
        _log(f"close issue {issue_num} 失败: {e}")


def ingest_add_domain_issues() -> int:
    """处理 [curio-add-domain] Issue：加入 sources.yaml"""
    try:
        issues = _list_open_issues("curio-add-domain")
    except Exception as e:
        _log(f"❌ 拉取 Issue 失败：{e}")
        return 1
    if not issues:
        _log("（没有待处理的加领域 Issue）")
        return 0

    cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}
    domains_cfg = cfg.setdefault("domains", {})

    ok = fail = 0
    for issue in issues:
        num = issue["number"]
        body = issue.get("body") or ""
        data = _parse_yaml_block(body)
        name = (data.get("name") or "").strip()
        if not name:
            _log(f"  #{num}: 缺 name，跳过")
            fail += 1
            continue
        icon = data.get("icon") or "📰"
        # 新版前端用 icon_type（svg key），保留 icon 兼容旧版
        icon_type = data.get("icon_type") or ""
        freq = data.get("frequency") or "weekly"
        # 生成 slug：英文直接用，中文优先映射到英文关键词
        import re
        slug = re.sub(r"[^a-z0-9-]+", "-", name.lower()).strip("-")
        if not slug:
            # 中文名 → 用 auto_sources 的 ZH_EN_HINTS 反查英文
            try:
                from agent.auto_sources import ZH_EN_HINTS, _translate_safe
                en_words = _translate_safe(name)
                if en_words and en_words[0] != name:
                    slug = re.sub(r"[^a-z0-9-]+", "-", "-".join(en_words[:2]).lower()).strip("-")
            except Exception:
                pass
        if not slug:
            slug = f"domain-{num}"
        if slug in domains_cfg:
            _log(f"  #{num}: {slug} 已存在，跳过")
            try:
                _close_issue(num, comment=f"领域 {slug} 已存在", label_add="curio-ingested")
            except Exception:
                pass
            continue
        # 自动配信源
        try:
            from agent.auto_sources import default_topics_for
            topics = default_topics_for(name)
        except Exception as e:
            _log(f"  #{num}: 默认信源生成失败 ({e})，topics 留空")
            topics = {}

        domain_entry = {
            "name": name,
            "icon": icon,
            "frequency": freq,
            "topics": topics,
        }
        if icon_type:
            domain_entry["icon_type"] = icon_type  # 优先用 icon_type，render_site 渲染时识别
        domains_cfg[slug] = domain_entry
        ok += 1
        src_count = sum(len(t.get("sources") or []) for t in topics.values()) if isinstance(topics, dict) else 0

        # 同时写一个最小 explore.json，让下次 prepare 能直接 search
        try:
            from agent.auto_sources import _translate_safe, is_chinese_name
            keywords = _translate_safe(name) if is_chinese_name(name) else [w for w in name.split() if w]
            explore_path = TOPICS / f"{slug}.explore.json"
            if not explore_path.exists():
                explore_path.write_text(json.dumps({
                    "domain": name,
                    "domain_id": slug,
                    "frequency": freq,
                    "topics": list(topics.keys()) if isinstance(topics, dict) else [],
                    "keywords": keywords[:6],
                    "_note": "auto-generated by ingest_add_domain",
                }, ensure_ascii=False, indent=2), encoding="utf-8")
                _log(f"     → topics/{slug}.explore.json")
        except Exception as e:
            _log(f"     explore.json 生成失败: {e}")
        try:
            _close_issue(num, comment=f"已加入领域 {slug}（{name}），自动配置 {src_count} 个信源，下次跑生效", label_add="curio-ingested")
        except Exception as e:
            _log(f"     close 失败: {e}")

    if ok > 0:
        SOURCES.write_text(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False), encoding="utf-8")
        _log(f"\n📝 已加入 {ok} 个领域到 sources.yaml")
    _log(f"\n📊 ingest_add_domain 完成：{ok} 成功 / {fail} 失败")
    return 0


def ingest_delete_domain_issues() -> int:
    """处理 [curio-delete-domain] Issue：从 sources.yaml 删除该领域，订阅者从该领域退订。

    流程：
    1. 拉所有 label=curio-delete-domain 的 open issue
    2. 解析 yaml block 取 domain_id
    3. sources.yaml 删除该 domain
    4. 调 worker /admin/unsubscribe-domain 把所有订阅了该 domain 的用户从该 domain 退订
       （worker 端实现见 worker/src/index.js）
    5. close issue 加 curio-ingested label
    """
    try:
        issues = _list_open_issues("curio-delete-domain")
    except Exception as e:
        _log(f"❌ 拉取 Issue 失败：{e}")
        return 1
    if not issues:
        _log("（没有待处理的删领域 Issue）")
        return 0

    cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}
    domains_cfg = cfg.setdefault("domains", {})

    ok = fail = 0
    for issue in issues:
        num = issue["number"]
        body = issue.get("body") or ""
        data = _parse_yaml_block(body)
        domain_id = (data.get("domain_id") or "").strip()
        if not domain_id:
            _log(f"  #{num}: 缺 domain_id，跳过")
            fail += 1
            try:
                _close_issue(num, comment="缺 domain_id，无法处理", label_add="curio-ingested")
            except Exception:
                pass
            continue

        if domain_id not in domains_cfg:
            _log(f"  #{num}: {domain_id} 不在 sources.yaml，已忽略")
            try:
                _close_issue(num, comment=f"领域 {domain_id} 不存在或已被删除", label_add="curio-ingested")
            except Exception:
                pass
            continue

        domain_name = domains_cfg[domain_id].get("name", domain_id)
        del domains_cfg[domain_id]
        ok += 1
        _log(f"  #{num}: 已从 sources.yaml 删除 {domain_id} ({domain_name})")

        # 让 worker 把订阅者从这个 domain 退订
        try:
            status, resp = _http("POST", "/admin/unsubscribe-domain",
                                 body={"domain_id": domain_id}, admin=True)
            unsubbed = resp.get("count", 0)
            removed = resp.get("removed", 0)
            _log(f"     → worker 退订 {unsubbed} 个订阅者（其中 {removed} 个整条删除）")
        except Exception as e:
            _log(f"     ⚠️ 通知 worker 退订失败: {e}（可手动跑 /admin/unsubscribe-domain）")

        try:
            _close_issue(num,
                comment=f"已删除领域「{domain_name}」（id={domain_id}）。\n\n- sources.yaml 已移除\n- 订阅者已从该领域退订（其他领域订阅保留）\n- 历史 markdown 文件保留，可通过直接 URL 访问",
                label_add="curio-ingested")
        except Exception as e:
            _log(f"     close 失败: {e}")

    if ok > 0:
        SOURCES.write_text(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False), encoding="utf-8")
        _log(f"\n📝 已删除 {ok} 个领域")
    _log(f"\n📊 ingest_delete_domain 完成：{ok} 成功 / {fail} 失败")
    return 0


# ============== CLI ==============

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("sync_domains", help="把 sources.yaml 的领域同步到 worker KV")
    sub.add_parser("push_content", help="把所有 scored.json 转 HTML 块推到 worker KV")
    bcast = sub.add_parser("broadcast", help="触发 worker 按订阅者偏好群发邮件")
    bcast.add_argument("--cadence", required=True, choices=["daily", "weekly"])
    bcast.add_argument("--dry-run", action="store_true")
    sub.add_parser("ingest_subscribe", help="拉 GitHub [curio-subscribe] Issue 兜底")
    sub.add_parser("ingest_add_domain", help="拉 GitHub [curio-add-domain] Issue 加入 sources.yaml")
    sub.add_parser("ingest_delete_domain", help="拉 GitHub [curio-delete-domain] Issue 删除领域")
    sub.add_parser("ingest_generate", help="拉 GitHub [curio-generate] Issue 写到 .pending_generate.json")

    args = p.parse_args()

    if args.cmd == "sync_domains":
        sys.exit(sync_domains())
    if args.cmd == "push_content":
        sys.exit(push_content())
    if args.cmd == "broadcast":
        sys.exit(broadcast(args.cadence, args.dry_run))
    if args.cmd == "ingest_subscribe":
        sys.exit(ingest_subscribe_issues())
    if args.cmd == "ingest_add_domain":
        sys.exit(ingest_add_domain_issues())
    if args.cmd == "ingest_delete_domain":
        sys.exit(ingest_delete_domain_issues())
    if args.cmd == "ingest_generate":
        sys.exit(ingest_generate_issues())


if __name__ == "__main__":
    main()
