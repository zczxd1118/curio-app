"""
Curio 后端 server.py — 让网站真正"能用"

跑：python server.py
然后开 http://localhost:8765/

端点：
  GET  /                      → site/index.html（首页）
  GET  /<path>                → site/<path>（静态资源）
  GET  /api/domains           → 列领域
  POST /api/domains           → 新建领域 {id, name, icon, frequency}
  DELETE /api/domains/<id>    → 删领域
  GET  /api/issues/<domain>   → 该领域往期列表
  POST /api/feedback          → 写反馈 {issue_id, items: [{idx, rating, note}], long_term: {...}}
  GET  /api/feedback/<issue>  → 读已有反馈
  POST /api/site/rebuild      → 触发重 build site（领域改动后）
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml
from flask import Flask, jsonify, request, send_from_directory, abort
from flask_cors import CORS

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
TOPICS = ROOT / "topics"
FEEDBACK_DIR = ROOT / "feedback"
SOURCES_YAML = ROOT / "sources.yaml"

FEEDBACK_DIR.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT))

app = Flask(__name__, static_folder=None)
CORS(app)

# 启动时确保 site/ 已 build（Render 部署后第一次启动用）
def _ensure_site():
    if not (SITE / "index.html").exists():
        try:
            from agent.render_site import build_site
            build_site()
            print("[startup] site built", file=sys.stderr)
        except Exception as e:
            print(f"[startup] build_site failed: {e}", file=sys.stderr)
_ensure_site()


# ---------- 工具 ---------- #
def _load_sources() -> dict:
    if not SOURCES_YAML.exists():
        return {"domains": {}}
    return yaml.safe_load(SOURCES_YAML.read_text(encoding="utf-8")) or {"domains": {}}


def _save_sources(cfg: dict) -> None:
    SOURCES_YAML.write_text(
        yaml.dump(cfg, allow_unicode=True, sort_keys=False, indent=2),
        encoding="utf-8",
    )


def _slug(s: str) -> str:
    s = re.sub(r"[^\w\u4e00-\u9fa5-]+", "-", s.strip().lower())
    return re.sub(r"-+", "-", s).strip("-") or "domain"


def _list_issues_for_domain(did: str, dcfg: dict) -> list[dict]:
    """扫所有该领域可能的 weekly markdown"""
    slugs = [did] + list((dcfg.get("topics") or {}).keys())
    issues: list[dict] = []
    seen = set()
    for slug in slugs:
        for f in TOPICS.glob(f"{slug}.weekly.*.md"):
            if f.name in seen:
                continue
            seen.add(f.name)
            m = re.search(r"\.weekly\.(\d{4}-\d{2}-\d{2})\.md$", f.name)
            if not m:
                continue
            date = m.group(1)
            head = f.read_text(encoding="utf-8").split("\n", 1)[0]
            title = head.lstrip("# ").strip()
            issues.append({
                "id": f"{did}/{date}",
                "date": date,
                "filename": f"{date}.html",
                "title": title,
            })
    issues.sort(key=lambda x: x["date"], reverse=True)
    return issues


# ---------- 静态文件 ---------- #
@app.route("/")
def index():
    return send_from_directory(SITE, "index.html")


@app.route("/<path:p>")
def static_files(p: str):
    # 防穿越
    full = (SITE / p).resolve()
    if not str(full).startswith(str(SITE.resolve())):
        abort(403)
    if full.is_dir():
        idx = full / "index.html"
        if idx.exists():
            return send_from_directory(full, "index.html")
        abort(404)
    if not full.exists():
        abort(404)
    return send_from_directory(full.parent, full.name)


# ---------- API：领域 ---------- #
@app.route("/api/domains", methods=["GET"])
def list_domains_api():
    cfg = _load_sources()
    out = []
    for did, dcfg in (cfg.get("domains") or {}).items():
        issues = _list_issues_for_domain(did, dcfg)
        out.append({
            "id": did,
            "name": dcfg.get("name", did),
            "icon": dcfg.get("icon", "📰"),
            "frequency": dcfg.get("frequency", "weekly"),
            "topic_count": len(dcfg.get("topics") or {}),
            "source_count": sum(
                len(t.get("sources", []) or []) for t in (dcfg.get("topics") or {}).values()
            ),
            "issue_count": len(issues),
            "latest_date": issues[0]["date"] if issues else None,
        })
    return jsonify({"domains": out})


@app.route("/api/domains", methods=["POST"])
def create_domain_api():
    data = request.get_json(force=True, silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return jsonify({"error": "name required"}), 400

    domain_id = (data.get("id") or _slug(name)).strip()
    icon = (data.get("icon") or "📰").strip()
    frequency = data.get("frequency") or "weekly"

    cfg = _load_sources()
    domains = cfg.setdefault("domains", {})
    if domain_id in domains:
        return jsonify({"error": f"domain '{domain_id}' exists"}), 409

    domains[domain_id] = {
        "name": name,
        "icon": icon,
        "frequency": frequency,
        "topics": {},
        "_added_at": datetime.now().isoformat(),
    }
    _save_sources(cfg)

    # 异步 build_site（在后台线程跑，不阻塞响应）
    import threading
    def _bg_build():
        try:
            from agent.render_site import build_site
            build_site()
        except Exception as e:
            print(f"⚠️ rebuild site failed: {e}", file=sys.stderr)
    threading.Thread(target=_bg_build, daemon=True).start()

    return jsonify({
        "ok": True,
        "domain": {"id": domain_id, "name": name, "icon": icon, "frequency": frequency},
        "next_step": f"运行 explore 让 AI 拆子话题：python curator.py explore \"{name}\"",
    })


@app.route("/api/domains/<did>", methods=["DELETE"])
def delete_domain_api(did: str):
    cfg = _load_sources()
    domains = cfg.get("domains") or {}
    if did not in domains:
        return jsonify({"error": "not found"}), 404
    domains.pop(did)
    _save_sources(cfg)
    import threading
    def _bg_build():
        try:
            from agent.render_site import build_site
            build_site()
        except Exception:
            pass
    threading.Thread(target=_bg_build, daemon=True).start()
    return jsonify({"ok": True})


@app.route("/api/issues/<did>", methods=["GET"])
def list_issues_api(did: str):
    cfg = _load_sources()
    dcfg = (cfg.get("domains") or {}).get(did)
    if not dcfg:
        return jsonify({"error": "domain not found"}), 404
    return jsonify({"issues": _list_issues_for_domain(did, dcfg)})


# ---------- API：反馈 ---------- #
@app.route("/api/feedback", methods=["POST"])
def write_feedback_api():
    """
    Body: {
      "issue_id": "ai/2026-05-30",
      "items": [
        {"idx": 1, "title": "Anthropic Series H...", "rating": "useful"|"meh"|"off", "note": ""}
      ],
      "long_term": {
        "more": "...",
        "less": "...",
        "format": "..."
      }
    }
    """
    data = request.get_json(force=True, silent=True) or {}
    issue_id = data.get("issue_id", "")
    if not issue_id:
        return jsonify({"error": "issue_id required"}), 400

    safe_id = issue_id.replace("/", "_").replace("..", "")
    fb_path = FEEDBACK_DIR / f"{safe_id}.json"

    record = {
        "issue_id": issue_id,
        "submitted_at": datetime.now().isoformat(),
        "items": data.get("items", []),
        "long_term": data.get("long_term", {}),
    }
    fb_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 把长期偏好顺手追加到 profile.yaml 的 feedback_timeline
    long_term = data.get("long_term", {}) or {}
    if any(long_term.get(k) for k in ("more", "less", "format")):
        try:
            from pathlib import Path as P
            profile_path = ROOT / "profile.yaml"
            if profile_path.exists():
                pcfg = yaml.safe_load(profile_path.read_text(encoding="utf-8")) or {}
                tl = pcfg.setdefault("feedback_timeline", []) or []
                summary_parts = []
                if long_term.get("more"):
                    summary_parts.append(f"想多看：{long_term['more']}")
                if long_term.get("less"):
                    summary_parts.append(f"想少看：{long_term['less']}")
                if long_term.get("format"):
                    summary_parts.append(f"笔法：{long_term['format']}")
                tl.insert(0, {
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "issue": issue_id,
                    "text": " / ".join(summary_parts),
                    "applied": [],
                })
                profile_path.write_text(
                    yaml.dump(pcfg, allow_unicode=True, sort_keys=False, indent=2),
                    encoding="utf-8",
                )
        except Exception as e:
            print(f"⚠️ profile update failed: {e}", file=sys.stderr)

    return jsonify({"ok": True, "saved_at": str(fb_path)})


@app.route("/api/feedback/<path:issue_id>", methods=["GET"])
def read_feedback_api(issue_id: str):
    safe_id = issue_id.replace("/", "_").replace("..", "")
    fb_path = FEEDBACK_DIR / f"{safe_id}.json"
    if not fb_path.exists():
        return jsonify({"feedback": None})
    return jsonify({"feedback": json.loads(fb_path.read_text(encoding="utf-8"))})


@app.route("/api/site/rebuild", methods=["POST"])
def rebuild_site_api():
    try:
        from agent.render_site import build_site
        build_site()
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------- API：一键生成 ---------- #
# 全局任务状态（M0 单用户够用，无需 Redis）
GENERATION_JOBS: dict[str, dict] = {}


@app.route("/api/generate/<domain_id>", methods=["POST"])
def generate_issue_api(domain_id: str):
    """一键为某领域生成第一份周刊（异步跑）"""
    cfg = _load_sources()
    dcfg = (cfg.get("domains") or {}).get(domain_id)
    if not dcfg:
        return jsonify({"error": "domain not found"}), 404

    domain_name = dcfg.get("name", domain_id)

    # 防重复
    if GENERATION_JOBS.get(domain_id, {}).get("status") == "running":
        return jsonify({"error": "已在生成中", "job": GENERATION_JOBS[domain_id]}), 409

    job = {
        "domain_id": domain_id,
        "domain_name": domain_name,
        "status": "running",
        "step": "queued",
        "progress": 0,
        "started_at": datetime.now().isoformat(),
        "log": [],
    }
    GENERATION_JOBS[domain_id] = job

    import threading
    threading.Thread(target=_run_generation, args=(domain_id, dcfg, job), daemon=True).start()

    return jsonify({"ok": True, "job": job})


@app.route("/api/generate/<domain_id>/status", methods=["GET"])
def generate_status_api(domain_id: str):
    job = GENERATION_JOBS.get(domain_id)
    if not job:
        return jsonify({"job": None})
    return jsonify({"job": job})


def _is_chinese_name(s: str) -> bool:
    import re
    chars = re.findall(r"[\u4e00-\u9fa5]", s or "")
    return len(chars) / max(1, len(s)) > 0.3


def _default_sources_for(domain_name: str) -> list[dict]:
    """根据领域名自动给一组合理信源。
    中文领域：用主题翻译成英文 + HN search + 多条 RSS（量子位、机器之心 RSSHub）
    英文领域：用 HN search 拆 3-4 个独立关键词
    """
    is_zh = _is_chinese_name(domain_name)
    sources: list[dict] = []
    name = domain_name.strip()

    if is_zh:
        # 中文领域：先翻译 name 拿英文关键词
        try:
            from agent.translate import translate
            en_name = translate(name, target="en-US")
        except Exception:
            en_name = name

        # 多个 HN 查询（关键词级，HN 不支持 OR）
        en_words = [w.strip() for w in en_name.split() if len(w.strip()) >= 3]
        for w in en_words[:3]:
            sources.append({
                "name": f"HN · {w}",
                "kind": "hn_search", "query": w,
                "days": 30, "min_points": 30, "lang": "en",
            })

        # 中文 RSS（RSSHub 有的话）
        sources.append({
            "name": "量子位（公众号 via RSSHub）",
            "kind": "rss", "url": "https://rsshub.app/wechat/ranking/all/qbitai",
            "lang": "zh", "optional": True,
        })
        sources.append({
            "name": "机器之心（RSSHub）",
            "kind": "rss", "url": "https://rsshub.app/jiqizhixin/zixun",
            "lang": "zh", "optional": True,
        })
    else:
        # 英文领域：拆几个独立关键词搜 HN
        words = [w.strip() for w in name.split() if len(w.strip()) >= 2]
        for w in words[:3] or [name]:
            sources.append({
                "name": f"HN · {w}",
                "kind": "hn_search", "query": w,
                "days": 30, "min_points": 30, "lang": "en",
            })

    return sources


def _run_generation(domain_id: str, dcfg: dict, job: dict):
    """后台跑：explore → search → enrich（抓全文 + 翻译）→ score（占位）→ write。
    """
    def step(name, msg, pct):
        job["step"] = name
        job["progress"] = pct
        job["log"].append({"t": datetime.now().isoformat(), "msg": msg})

    try:
        from agent.fetch_rss import fetch_one_feed
        from agent.fetch_hackernews import search_hn
        from agent.fetch_article import fetch_article
        from agent.translate import translate, is_chinese
        from agent.render_site import build_site

        domain_name = dcfg.get("name", domain_id)
        topics = dcfg.get("topics") or {}

        step("explore", f"为「{domain_name}」准备搜索源", 10)

        # 如果该领域还没 topics（用户刚 add 的），自动配信源
        if not topics:
            sources = _default_sources_for(domain_name)
            dcfg["topics"] = {"default": {"sources": sources}}
            cfg2 = _load_sources()
            cfg2["domains"][domain_id] = dcfg
            _save_sources(cfg2)
            topics = dcfg["topics"]
            step("explore", f"自动配置了 {len(sources)} 个信源（中文 RSS + 英文 HN）", 15)

        # 抓内容
        step("search", "开始抓全网", 20)
        all_items: dict[str, dict] = {}
        for tid, tcfg in topics.items():
            for src in (tcfg.get("sources") or []):
                kind = src.get("kind")
                name = src.get("name", "?")
                step("search", f"抓 {name}", min(60, job["progress"] + 5))
                try:
                    if kind == "rss":
                        items = fetch_one_feed(src["url"], feed_name=name, lang=src.get("lang", ""), max_items=src.get("max", 30))
                    elif kind == "hn_search":
                        items = search_hn(src["query"], days=src.get("days", 7), min_points=src.get("min_points", 0))
                    else:
                        items = []
                    for it in items:
                        all_items.setdefault(it["id"], it)
                    job["log"].append({"t": datetime.now().isoformat(), "msg": f"  → {name}: {len(items)} 条"})
                except Exception as e:
                    job["log"].append({"t": datetime.now().isoformat(), "msg": f"  ⚠️ {name} 失败: {e}"})

        candidates = list(all_items.values())
        step("search", f"共抓到 {len(candidates)} 条候选", 65)

        # M0 阶段：自动生成一份"占位 digest"——前 5 条按热度做必读
        candidates.sort(key=lambda x: x.get("views") or 0, reverse=True)
        must = candidates[:5]
        ref = candidates[5:11]
        skip = candidates[11:30]

        step("score", "选出 5 条头版", 70)

        # ⭐ 关键升级：对必读条目抓全文 + 翻译
        step("enrich", "抓必读全文 + 翻译", 75)
        for i, m in enumerate(must, 1):
            url = m.get("url", "")
            title = m.get("title", "")[:50]
            # 1. 抓全文
            try:
                if url and not url.startswith("https://news.ycombinator.com"):
                    r = fetch_article(url)
                    if r.get("ok"):
                        m["body"] = (r.get("body") or "")[:1500]
                        job["log"].append({"t": datetime.now().isoformat(), "msg": f"  📄 {i}. 抓到 {len(m['body'])} 字 - {title}"})
            except Exception as e:
                job["log"].append({"t": datetime.now().isoformat(), "msg": f"  ⚠️ {i}. 抓全文失败: {e}"})

            # 2. 翻译标题（英文 → 中文）
            try:
                if not is_chinese(m.get("title", "")):
                    m["title_zh"] = translate(m["title"], target="zh-CN")
                # 翻译 body 的前 800 字
                if m.get("body") and not is_chinese(m["body"][:200]):
                    m["body_zh"] = translate(m["body"][:800], target="zh-CN")
            except Exception as e:
                job["log"].append({"t": datetime.now().isoformat(), "msg": f"  ⚠️ {i}. 翻译失败: {e}"})

            step("enrich", f"已处理 {i}/{len(must)} 必读", 75 + (i * 8) // max(1, len(must)))

        scored = {
            "scored_at": datetime.now().isoformat(),
            "domain": domain_name,
            "intro": f"M0 占位版本：本期从 {len(candidates)} 条候选里按热度自动取 top-5 必读。完整 AI 打分将在 M1 接入 API 后启用。",
            "must_read": [
                {
                    "id": m["id"],
                    "platform": m.get("platform", "?"),
                    "title": m.get("title", ""),
                    "url": m.get("url", ""),
                    "source": (m.get("source") or {}).get("name", ""),
                    "score": {"novelty": 7, "depth": 7, "relevance": 7},
                    "why_recommend": f"按热度排序进入头版（{m.get('platform','?')} · {m.get('views') or 0} 热度）",
                } for m in must
            ],
            "reference": [
                {**{
                    "id": r["id"], "platform": r.get("platform", "?"),
                    "title": r.get("title", ""), "url": r.get("url", ""),
                    "source": (r.get("source") or {}).get("name", ""),
                    "why_recommend": "热度第 6-11 位",
                }} for r in ref
            ],
            "skip": [{"id": s["id"], "title": s.get("title", ""), "skip_reason": "热度未进 top 11"} for s in skip],
            "stats": {
                "candidates_total": len(candidates),
                "must_read_count": len(must),
                "reference_count": len(ref),
                "skip_count_actual": len(candidates) - len(must) - len(ref),
                "skip_count_shown": min(5, len(skip)),
            },
        }

        # 写 candidates / scored
        slug = domain_id
        TOPICS.mkdir(exist_ok=True)
        (TOPICS / f"{slug}.candidates.json").write_text(
            json.dumps({"domain": domain_name, "items": candidates, "total": len(candidates)}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        (TOPICS / f"{slug}.scored.json").write_text(
            json.dumps(scored, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        step("write", "拼装周刊", 85)

        # 生成一份简化的 weekly md（M0 占位，没真 LLM 写报道）
        today = datetime.now().strftime("%Y-%m-%d")
        lines = [
            f"# Curio · {domain_name} 周刊",
            "",
            f"**{today} · 由 Curio 主编从 {len(candidates)} 条候选选出（M0 占位版）**",
            "",
            "---",
            "",
            "## 📰 主编社论",
            "",
            f"这是「{domain_name}」领域的第一份周刊。M0 版本按热度自动选出前 5 条头版，AI 打分 + 主编笔法的报道将在 M1 接入 LLM API 后启用。当前你能看到的是真实抓取的全网内容，足够先验证「这个领域能搜到什么」。",
            "",
            "---",
            "",
            f"## 🗞️ 头版报道（{len(must)} 条）",
            "",
        ]
        for i, m in enumerate(must, 1):
            title_orig = m.get("title", "?")
            title_zh = m.get("title_zh", "")
            body = m.get("body") or m.get("summary", "") or ""
            body_zh = m.get("body_zh", "")

            # 标题：中英对照（如果有翻译）
            if title_zh and title_zh != title_orig:
                title_line = f"### {i}. {title_zh}"
                subtitle_line = f"_原标题：{title_orig}_"
            else:
                title_line = f"### {i}. {title_orig}"
                subtitle_line = ""

            lines += [
                title_line,
                "",
                f"**来源**：{(m.get('source') or {}).get('name','?')} · {m.get('platform','?')} · 热度 {m.get('views') or 0}",
                "",
            ]
            if subtitle_line:
                lines += [subtitle_line, ""]

            # 正文：中文版优先，无翻译则原文
            if body_zh:
                lines += ["**📖 中文摘要**", "", body_zh[:600] + ("..." if len(body_zh) > 600 else ""), ""]
                lines += ["<details><summary>展开英文原文</summary>", "", body[:800] + ("..." if len(body) > 800 else ""), "", "</details>", ""]
            elif body:
                lines += [body[:600] + ("..." if len(body) > 600 else ""), ""]
            else:
                lines += ["_（暂无摘要，请点击下方链接查看原文）_", ""]

            lines += [
                f"📺 [打开原文]({m.get('url', '#')})",
                "",
                "---",
                "",
            ]

        if ref:
            lines += [f"## 📖 参考（{len(ref)} 条）", ""]
            # 参考区也翻译标题（轻量、不抓全文）
            for i, r in enumerate(ref, 1):
                t = r.get("title", "?")
                try:
                    if not is_chinese(t):
                        tz = translate(t, target="zh-CN")
                        if tz and tz != t:
                            t = f"{tz}　_{r.get('title','?')[:50]}_"
                except Exception:
                    pass
                lines += [
                    f"**{i}. {t}**　_{(r.get('source') or {}).get('name','?')} · {r.get('platform','?')}_",
                    f"- [打开]({r.get('url','#')})",
                    "",
                ]
            lines += ["---", ""]

        if skip:
            preview_n = min(5, len(skip))
            lines += [f"## ⏭ 跳过（{len(skip)} 条）", "", f"_展示前 {preview_n} 条_", ""]
            for s in skip[:preview_n]:
                lines.append(f"- **{s.get('title','?')}**　_热度未进 top 11_")
            lines += ["", "---", ""]

        lines += [
            "## 📝 本期反馈",
            "",
            "（用网站底部反馈区填写，下次跑前 Agent 会读这段）",
            "",
            "---",
            "",
            f"_Curio v0.8 (M0 自动生成) · {today}_",
        ]

        out_path = TOPICS / f"{slug}.weekly.{today}.md"
        out_path.write_text("\n".join(lines), encoding="utf-8")
        job["log"].append({"t": datetime.now().isoformat(), "msg": f"  ✅ 周刊写入：{out_path.name}"})

        step("site", "重 build 网站", 95)
        build_site()

        step("done", "✨ 完成！", 100)
        job["status"] = "done"
        job["finished_at"] = datetime.now().isoformat()
        job["issue_url"] = f"/d/{domain_id}/{today}.html"

    except Exception as e:
        import traceback
        job["status"] = "error"
        job["error"] = str(e)
        job["traceback"] = traceback.format_exc()[-500:]
        job["log"].append({"t": datetime.now().isoformat(), "msg": f"❌ {e}"})


# ---------- 健康检查 ---------- #
@app.route("/api/health")
def health():
    return jsonify({"ok": True, "service": "curio", "version": "0.7"})


@app.route("/api/echo", methods=["POST"])
def echo():
    """Debug：原样返回收到的 body"""
    raw = request.get_data(as_text=True)
    return jsonify({
        "method": request.method,
        "ct": request.content_type,
        "cl": request.content_length,
        "raw": raw,
        "raw_len": len(raw),
        "json": request.get_json(force=True, silent=True),
    })


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"🛰️  Curio server: http://localhost:{port}/")
    print(f"   📂 site:    {SITE}")
    print(f"   📨 feedback:{FEEDBACK_DIR}")
    print(f"   🔌 API:     http://localhost:{port}/api/health")
    app.run(host="127.0.0.1", port=port, debug=False)
