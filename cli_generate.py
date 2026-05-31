#!/usr/bin/env python3
"""
Curio 一键生成脚本 —— 给 WorkBuddy automation 用

按"趋势雷达 V1"流程：
  WorkBuddy（这里）
    ↓ 跑生成
  GitHub（curio-site 仓库）
    ↓ 自动部署
  GitHub Pages（公网 URL）
    ↓ 浏览器
  反馈 json → profile.yaml → 次日读取

E 方案（用 Claude 当 LLM）的多阶段流程：

  阶段 1: prepare    — 抓候选 + 生成所有 prompt 文件，等 Claude 处理
  阶段 2: （automation 自己）读 prompt 文件 → 调用 Claude → 写回结果
  阶段 3: finalize   — 拼装 → 渲染 site → push GitHub

用法：
  python cli_generate.py prepare        # 阶段 1：抓数据 + 输出 prompts
  python cli_generate.py finalize       # 阶段 3：拼装 + 渲染 + push
  python cli_generate.py finalize --no-push   # 阶段 3 但只生成不推送
  python cli_generate.py legacy         # 老逻辑：直接跑 curator site（占位算法）
"""

import argparse
import os
import subprocess
import sys
import time
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY = "/Users/zoezczhou/.workbuddy/binaries/python/envs/curio_sys/bin/python"
SITE_DIR = ROOT / "site"
TOPICS_DIR = ROOT / "topics"
PAT_FILE = ROOT / ".gh_pat"
GH_USER = "zczxd1118"
GH_REPO = "curio-site"


def log(msg: str):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def run(cmd: list, cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess:
    log(f"$ {' '.join(str(c) for c in cmd)}")
    return subprocess.run(cmd, cwd=str(cwd), check=check, text=True)


# ============================================================
# 阶段 1: prepare —— 抓数据 + 生成 prompt 文件给 Claude
# ============================================================

def list_active_domains() -> list:
    """从 sources.yaml 读出活跃领域 ID"""
    import yaml
    cfg = yaml.safe_load((ROOT / "sources.yaml").read_text(encoding="utf-8"))
    domains = cfg.get("domains", {})
    if isinstance(domains, dict):
        return [k for k, v in domains.items()
                if isinstance(v, dict) and v.get("frequency") in ("daily", "weekly")]
    # 兼容 list 形式
    return [d["id"] for d in domains if d.get("frequency") in ("daily", "weekly")]


def cmd_prepare(args):
    """阶段 1：拉反馈 → search → score（生成 prompt）"""
    log("🛰️  Curio prepare —— 抓数据 + 生成 LLM prompts")

    # 0. 先拉 GitHub Issue 反馈，蒸馏到 profile.yaml
    log("📥 ingest feedback from GitHub Issues")
    run([PY, "-m", "agent.ingest_feedback"], check=False)

    # 0.1 ingest 加领域请求 → sources.yaml
    log("📥 ingest add-domain requests")
    run([PY, "-m", "agent.worker_sync", "ingest_add_domain"], check=False)

    # 0.15 ingest 删领域请求 → sources.yaml 删除
    log("📥 ingest delete-domain requests")
    run([PY, "-m", "agent.worker_sync", "ingest_delete_domain"], check=False)

    # 0.2 ingest 订阅请求兜底 → worker /subscribe
    log("📥 ingest subscribe requests (GitHub fallback)")
    run([PY, "-m", "agent.worker_sync", "ingest_subscribe"], check=False)

    # 0.3 ingest 用户立刻生成请求 → 把对应领域加入本次生成队列
    # 这样 daily/weekly 自动跑时会顺手处理掉所有 pending 的"立刻生成"请求
    # （原来是单独 hourly 跑 process_pending，体验是"等下个整点"；
    #  现在 daily 12:00 和 weekly 周一 12:00 跑前都会捎带处理，无额外成本）
    log("📥 ingest curio-generate requests (merge into this run)")
    run([PY, "-m", "agent.worker_sync", "ingest_generate"], check=False)
    pending_file = ROOT / ".pending_generate.json"
    user_requested_domains: list[str] = []
    if pending_file.exists():
        try:
            pending_data = json.loads(pending_file.read_text(encoding="utf-8"))
            user_requested_domains = [p["domain_id"] for p in pending_data.get("pending", [])]
            if user_requested_domains:
                log(f"   📌 用户请求生成的领域：{user_requested_domains}（合并到本次）")
        except Exception as e:
            log(f"   ⚠️ 读 pending 失败: {e}")

    domains = args.domains or list_active_domains()

    # 用户请求的领域如果不在 args.domains 限制范围内，也要带上（除非显式指定 --domains）
    if not args.domains and user_requested_domains:
        for udom in user_requested_domains:
            if udom not in domains:
                domains.append(udom)
                log(f"   ➕ 用户请求 '{udom}' 不在默认列表，临时加入本次")

    log(f"   领域：{domains}")

    plan = {"prepared_at": time.strftime("%Y-%m-%d %H:%M"), "domains": []}

    for d in domains:
        log("")
        log(f"━━━━━━━━━ 处理 {d} ━━━━━━━━━")

        # 1. search（抓候选）—— sources.yaml 里已配源，search 不依赖 explore.json
        # 直接跑 search 默认会扫该领域所有 topic 的源
        log(f"  🔍 search candidates for {d}")
        explore_path = TOPICS_DIR / f"{d}.explore.json"
        if explore_path.exists():
            run([PY, str(ROOT / "curator.py"), "search", str(explore_path)], check=False)
        else:
            log(f"  （没有 explore.json，沿用既有 candidates.json）")

        # 2. score（生成打分 prompt 文件）
        # curator.py 写的文件名是 {domain.name slugify} 而非 {domain_id}
        # 所以同时尝试几个候选路径
        cand_path = TOPICS_DIR / f"{d}.candidates.json"
        if not cand_path.exists():
            # 从 sources.yaml 拿 name，再 slugify
            try:
                import yaml as _yaml
                cfg = _yaml.safe_load((ROOT / "sources.yaml").read_text(encoding="utf-8")) or {}
                dname = ((cfg.get("domains") or {}).get(d) or {}).get("name", d)
                import re as _re
                alt_slug = _re.sub(r"[^\w\u4e00-\u9fa5]+", "-", dname.lower()).strip("-")
                alt_path = TOPICS_DIR / f"{alt_slug}.candidates.json"
                if alt_path.exists():
                    cand_path = alt_path
            except Exception:
                pass
        if not cand_path.exists():
            log(f"  ⚠️ {cand_path.name} 不存在，跳过该领域")
            continue
        log(f"  🎯 generate score prompt")
        run([PY, str(ROOT / "curator.py"), "score", str(cand_path)], check=False)

        # curator.py 现在已优先用英文 domain_id 作 slug（v0.9.1 修复后）
        # 优先 domain_id，兜底从 candidates.json 读 / 兜底 d
        slug = d  # 默认就是英文 domain id
        try:
            cand = json.loads(cand_path.read_text(encoding="utf-8"))
            slug = cand.get("domain_id") or d
            domain_name = cand.get("domain", d)
        except Exception:
            domain_name = d

        score_prompt = TOPICS_DIR / f"{slug}.score-prompt.md"
        scored_file = TOPICS_DIR / f"{slug}.scored.json"
        plan["domains"].append({
            "domain": d,
            "domain_name": domain_name if 'domain_name' in dir() else d,
            "slug": slug,
            "candidates_file": str(cand_path),
            "score_prompt_file": str(score_prompt),
            "expected_scored_file": str(scored_file),
        })

    # 把"待处理清单"写出，automation 读这个
    plan_path = TOPICS_DIR / "_run_plan.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    log("")
    log(f"✅ prepare 完成 → {plan_path}")
    log(f"   等 automation 处理 {len(plan['domains'])} 个领域的 score prompt")


# ============================================================
# 阶段 3: finalize —— 拼装 + 渲染 + push
# ============================================================

def cmd_prepare_notes(args):
    """阶段 2.5：scored.json 已就绪 → 给每条必读生成"中文导读 prompt 文件"，等 Claude 处理"""
    log("📝 prepare_notes —— 给每条必读生成中文导读 prompt")

    import yaml
    profile = yaml.safe_load((ROOT / "profile.yaml").read_text(encoding="utf-8")) or {}
    template = (ROOT / "prompts" / "editor_note.md").read_text(encoding="utf-8")

    # 复用 curator.py 的抓正文 + fill_prompt
    sys.path.insert(0, str(ROOT))
    from curator import _fetch_body_for, fill_prompt, slugify

    plan_path = TOPICS_DIR / "_run_plan.json"
    if not plan_path.exists():
        log("  ❌ 没有 _run_plan.json")
        return

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    notes_plan = {"prepared_at": time.strftime("%Y-%m-%d %H:%M"), "domains": []}

    # 兼容旧 plan：如果 plan["domains"] 里 expected 不存在，扫所有 *.scored.json 兜底
    plan_slugs = {d.get("slug") for d in plan["domains"]}
    plan_by_slug = {d.get("slug"): d for d in plan["domains"]}
    for f in TOPICS_DIR.glob("*.scored.json"):
        slug = f.stem.replace(".scored", "")
        if slug not in plan_slugs:
            plan["domains"].append({
                "domain": slug,
                "slug": slug,
                "expected_scored_file": str(f),
            })

    for d in plan["domains"]:
        scored_path = Path(d.get("expected_scored_file") or (TOPICS_DIR / f"{d.get('slug', d['domain'])}.scored.json"))
        if not scored_path.exists():
            log(f"  ⚠️ {scored_path.name} 不存在，跳过 {d['domain']}")
            continue

        scored = json.loads(scored_path.read_text(encoding="utf-8"))
        must = scored.get("must_read", []) or []
        if not must:
            log(f"  {d['domain']}: must_read 为空，跳过")
            continue

        log(f"  {d['domain']}: {len(must)} 条必读，抓正文 + 出 prompt")
        items = []
        for i, m in enumerate(must, 1):
            # 仅对英文必读写中文导读（中文标题已经是中文，不需要）
            title = (m.get("title") or "")[:200]
            if not title:
                continue
            # 简单判断是否英文为主：有 ASCII 字母且占比高
            ascii_ratio = sum(1 for c in title if c.isascii() and c.isalpha()) / max(len(title), 1)
            is_english = ascii_ratio > 0.4

            log(f"    [{i}/{len(must)}] {title[:50]}... ({'EN' if is_english else 'CN/MIX'})")
            if not is_english:
                # 中文标题就不写导读，render 会直接显示
                items.append({"id": m.get("id"), "title": title, "skip_reason": "中文文章不需导读"})
                continue

            # 抓正文
            try:
                body, kind = _fetch_body_for(m)
            except Exception as e:
                log(f"      抓正文失败: {e}")
                body, kind = "", "fallback"

            prompt = fill_prompt(
                template,
                IDENTITY=profile.get("identity", "").strip(),
                SIGNAL_PREFERENCES=profile.get("signal_preferences", []),
                DISLIKES=profile.get("dislikes", []),
                TITLE=title,
                SOURCE=(m.get("source") or {}).get("name", "") if isinstance(m.get("source"), dict) else (m.get("source") or ""),
                PLATFORM=m.get("platform", ""),
                ID=m.get("id", ""),
                ARTICLE_BODY=body[:2000] if body else "(无法抓取正文)",
            )
            items.append({
                "id": m.get("id"),
                "title": title,
                "url": m.get("url", ""),
                "body_kind": kind,
                "prompt": prompt,
            })

        slug = d.get("slug") or d.get("domain")
        out_path = TOPICS_DIR / f"{slug}.note-prompts.json"
        out_path.write_text(json.dumps({
            "domain": d["domain"], "slug": slug,
            "items": items,
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"    → {out_path.name}（{len([i for i in items if 'prompt' in i])} 条 prompt）")

        notes_plan["domains"].append({
            "domain": d["domain"], "slug": slug,
            "note_prompts_file": str(out_path),
            "expected_notes_file": str(TOPICS_DIR / f"{slug}.editor_notes.json"),
        })

    notes_plan_path = TOPICS_DIR / "_notes_plan.json"
    notes_plan_path.write_text(json.dumps(notes_plan, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"\n✅ prepare_notes 完成 → {notes_plan_path}")
    log(f"   等 automation 处理 {len(notes_plan['domains'])} 个领域的导读 prompt")


def cmd_finalize(args):
    """阶段 3：所有 *.scored.json 已就绪 → 统一 build_issue_md → site → push"""
    log("📰 Curio finalize —— 拼装 → 渲染 → push")

    cadence = args.cadence or "weekly"
    plan_path = TOPICS_DIR / "_run_plan.json"

    # 统一 md 生成：每个有 scored.json 的领域都按 cadence 生成 issue md
    log(f"  📝 build issue md (cadence={cadence}) —— daily 和 weekly 共用模板")
    sys.path.insert(0, str(ROOT))
    try:
        from agent.build_issue_md import build_issue_md, CADENCE_CFG
    except Exception as e:
        log(f"  ❌ 加载 build_issue_md 失败: {e}")
        return

    if plan_path.exists():
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        plan_domains = plan.get("domains", [])
    else:
        # 兜底：扫所有 scored.json
        plan_domains = []
        for f in TOPICS_DIR.glob("*.scored.json"):
            slug = f.stem.replace(".scored", "")
            plan_domains.append({"domain": slug, "slug": slug, "expected_scored_file": str(f)})

    today = time.strftime("%Y-%m-%d")
    built = 0
    for d in plan_domains:
        slug = d.get("slug") or d.get("domain")
        sp = Path(d.get("expected_scored_file") or (TOPICS_DIR / f"{slug}.scored.json"))
        if not sp.exists():
            log(f"  ⚠️ {sp.name} 缺失，跳过")
            continue
        try:
            scored = json.loads(sp.read_text(encoding="utf-8"))
            md = build_issue_md(scored, cadence=cadence, slug=slug, today=today)
            out = TOPICS_DIR / f"{slug}.weekly.{today}.md"
            out.write_text(md, encoding="utf-8")
            log(f"  ✓ {out.name}")
            built += 1
        except Exception as e:
            log(f"  ❌ {slug} build_issue_md 失败: {e}")

    log(f"  📝 已生成 {built} 份 issue md")

    # 跑 site（render_site.py 会扫 *.weekly.*.md 渲染成 HTML）
    log("  🏗️ build site")
    run([PY, str(ROOT / "curator.py"), "site"])

    # 推送
    if not args.no_push:
        publish()
    else:
        log("  --no-push，跳过 push")

    # 邮件通知 - 自用版（profile.yaml.email.enabled 控制是否真发）
    if not args.no_email:
        log("📧 send notification email (self)")
        run([PY, "-m", "agent.notify_email"], check=False)
    else:
        log("  --no-email，跳过邮件")

    # Worker 同步 + 群发订阅者
    if not args.no_worker:
        log("🛰️  sync domains to worker KV")
        run([PY, "-m", "agent.worker_sync", "sync_domains"], check=False)
        log("📦 push content to worker KV")
        run([PY, "-m", "agent.worker_sync", "push_content"], check=False)
        cadence = args.cadence or "weekly"
        log(f"📢 broadcast to {cadence} subscribers")
        run([PY, "-m", "agent.worker_sync", "broadcast", "--cadence", cadence],
            check=False)
    else:
        log("  --no-worker，跳过 worker 同步与广播")

    log("")
    log("✅ finalize 完成")
    if not args.no_push:
        log(f"   网址：https://curioradar.fun/  (备用 https://{GH_USER}.github.io/{GH_REPO}/)")


def publish():
    """推 site/ 到 curio-site 仓库 → GitHub Pages 自动部署"""
    log("🚀 publish → GitHub Pages")

    if not PAT_FILE.exists():
        log("  ❌ .gh_pat 不存在，跳过 push"); return False
    pat = PAT_FILE.read_text().strip()
    if not pat:
        log("  ❌ .gh_pat 为空，跳过 push"); return False
    if not SITE_DIR.exists():
        log("  ❌ site/ 不存在"); return False

    if not (SITE_DIR / ".git").exists():
        run(["git", "init", "-q"], cwd=SITE_DIR)
        run(["git", "checkout", "-q", "-b", "main"], cwd=SITE_DIR, check=False)

    run(["git", "config", "user.email", "curio-bot@local"], cwd=SITE_DIR, check=False)
    run(["git", "config", "user.name", "Curio Bot"], cwd=SITE_DIR, check=False)
    (SITE_DIR / ".nojekyll").touch()

    remote = f"https://{pat}@github.com/{GH_USER}/{GH_REPO}.git"
    run(["git", "remote", "remove", "origin"], cwd=SITE_DIR, check=False)
    run(["git", "remote", "add", "origin", remote], cwd=SITE_DIR)
    run(["git", "add", "-A"], cwd=SITE_DIR)
    msg = f"Curio auto {time.strftime('%Y-%m-%d %H:%M')}"
    cp = subprocess.run(["git", "commit", "-q", "-m", msg], cwd=str(SITE_DIR), text=True)
    if cp.returncode != 0:
        log("  （没新变化）")
    try:
        run(["git", "push", "-u", "origin", "main", "--force"], cwd=SITE_DIR)
        log(f"  ✅ pushed → https://github.com/{GH_USER}/{GH_REPO}")
        log(f"  🌐 https://curioradar.fun/")
        return True
    except subprocess.CalledProcessError as e:
        log(f"  ❌ push failed: {e}")
        return False


# ============================================================
# Unified 模式：合并所有域 → 一份 Top 4-5 头条（借鉴 Starfan）
# ============================================================

def cmd_prepare_unified(args):
    """阶段 1（unified）：跑 prepare → 合并所有域 candidates → 写 unified.score-prompt.md

    与原 prepare 不同：原 prepare 给每域出独立 prompt（4 次 Claude），
    unified 把候选池合并 + 用 unified_radar.md 模板出 1 份 prompt（1 次 Claude）。
    """
    log("🛰️  Curio prepare (unified) — 抓数据 → 合并候选 → 一份大 prompt")

    # 1. 复用原 prepare（抓数据 + 写 each domain candidates.json）
    args.domains = args.domains if hasattr(args, "domains") else None
    cmd_prepare(args)

    # 2. 合并候选池
    log("")
    log("📚 合并所有域候选 → unified.candidates.json")
    plan_path = TOPICS_DIR / "_run_plan.json"
    if not plan_path.exists():
        log("❌ 没找到 _run_plan.json")
        return
    plan = json.loads(plan_path.read_text(encoding="utf-8"))

    all_items = []
    domain_summary = []
    for d in plan.get("domains", []):
        cand_file = Path(d["candidates_file"])
        if not cand_file.exists():
            continue
        try:
            cand = json.loads(cand_file.read_text(encoding="utf-8"))
            for it in cand.get("items", []):
                # 给每条标注它来自哪个域
                it["domain"] = d.get("domain_name") or d.get("domain")
                it["domain_id"] = d.get("slug") or d.get("domain")
                all_items.append(it)
            domain_summary.append(f"{d.get('domain_name')}={len(cand.get('items',[]))}")
        except Exception as e:
            log(f"  ⚠️ 读 {cand_file.name} 失败: {e}")

    log(f"   合并 {len(all_items)} 条（{', '.join(domain_summary)}）")

    # 候选去重：按 url 去重，保留各自最新
    seen_urls = set()
    deduped = []
    for it in all_items:
        url = it.get("url", "")
        if url and url in seen_urls:
            continue
        seen_urls.add(url)
        deduped.append(it)
    log(f"   去重后 {len(deduped)} 条")

    # 写合并候选
    unified_cand = {
        "date": time.strftime("%Y-%m-%d"),
        "total": len(deduped),
        "items": deduped,
    }
    (TOPICS_DIR / "unified.candidates.json").write_text(
        json.dumps(unified_cand, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 3. 生成 unified score prompt
    log("")
    log("📝 生成 unified score prompt")
    template_path = ROOT / "prompts" / "unified_radar.md"
    template = template_path.read_text(encoding="utf-8")

    # 读 profile
    import yaml as _yaml
    profile = {}
    profile_path = ROOT / "profile.yaml"
    if profile_path.exists():
        profile = _yaml.safe_load(profile_path.read_text(encoding="utf-8")) or {}

    # 读 pending note
    user_note = ""
    pending_file = ROOT / ".pending_generate.json"
    if pending_file.exists():
        try:
            pdata = json.loads(pending_file.read_text(encoding="utf-8"))
            notes = [p.get("note") for p in pdata.get("pending", []) if p.get("note")]
            if notes:
                user_note = " / ".join(notes)
        except Exception:
            pass

    user_note_block = ""
    if user_note:
        user_note_block = (
            f"用户在网页\"立刻生成\"按钮上提交了请求并附了留言：\n\n"
            f"> **{user_note}**\n\n"
            f"评分时优先考虑这条诉求：让 ≥1 条头条贴合，且在 intro 里提一句\"按你的请求侧重 XX\"。"
        )

    # 精简候选条目（避免 prompt 过长）
    items_for_prompt = []
    for it in deduped:
        pub = it.get("published_at")
        if pub and not isinstance(pub, (str, type(None))):
            pub = str(pub)  # date/datetime 对象转字符串
        items_for_prompt.append({
            "id": it.get("id"),
            "domain": it.get("domain"),
            "title": it.get("title", "")[:200],
            "url": it.get("url", ""),
            "source": (it.get("source", {}) or {}).get("name", "") if isinstance(it.get("source"), dict) else str(it.get("source", "")),
            "platform": it.get("platform"),
            "points": it.get("views"),
            "published_at": pub,
            "summary": (it.get("summary", "") or "")[:200],
        })

    # 简单变量替换
    today = time.strftime("%Y-%m-%d")
    prompt = template
    prompt = prompt.replace("{{DATE}}", today)
    prompt = prompt.replace("{{IDENTITY}}", str(profile.get("identity", "")).strip())
    prompt = prompt.replace("{{INTERESTS}}", json.dumps(profile.get("interests", []), ensure_ascii=False, default=str))
    prompt = prompt.replace("{{DISLIKES}}", json.dumps(profile.get("dislikes", []), ensure_ascii=False, default=str))
    prompt = prompt.replace("{{SIGNAL_PREFERENCES}}", json.dumps(profile.get("signal_preferences", []), ensure_ascii=False, default=str))
    prompt = prompt.replace("{{READING_PACE}}", str(profile.get("reading_pace", "")).strip())
    prompt = prompt.replace("{{FEEDBACK_TIMELINE}}", json.dumps(profile.get("feedback_timeline", [])[-3:], ensure_ascii=False, default=str))
    prompt = prompt.replace("{{ALREADY_PUSHED_TITLES}}", "[]")
    prompt = prompt.replace("{{USER_NOTE}}", user_note or "无")
    prompt = prompt.replace("{{USER_NOTE_BLOCK}}", user_note_block or "（无）")
    prompt = prompt.replace("{{CANDIDATES_JSON}}",
                            "```json\n" + json.dumps(items_for_prompt, ensure_ascii=False, indent=2, default=str) + "\n```")

    out_path = TOPICS_DIR / "unified.score-prompt.md"
    out_path.write_text(prompt, encoding="utf-8")
    log(f"   ✓ {out_path}")
    log(f"   prompt 体积：{len(prompt) // 1024}K 字符 ≈ {len(prompt) // 4} token")

    # 4. 更新 _run_plan.json 加 unified 段
    plan["unified"] = {
        "score_prompt_file": str(out_path),
        "expected_scored_file": str(TOPICS_DIR / "unified.scored.json"),
        "candidates_count": len(deduped),
    }
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    log("")
    log("✅ unified prepare 完成")
    log(f"   等 Claude 读 {out_path.name} → 写 unified.scored.json")


def cmd_finalize_unified(args):
    """阶段 3（unified）：读 unified.scored.json → 渲染 → push → 邮件"""
    log("📰 Curio finalize (unified) —— 渲染 Top 4-5 头条")

    scored_file = TOPICS_DIR / "unified.scored.json"
    if not scored_file.exists():
        log(f"❌ {scored_file} 不存在（Claude 还没写）")
        return

    sys.path.insert(0, str(ROOT))
    from agent.build_radar_md import build_radar_md

    scored = json.loads(scored_file.read_text(encoding="utf-8"))
    today = scored.get("date") or time.strftime("%Y-%m-%d")
    md = build_radar_md(scored)

    # 写到 site/radar/{date}.html 直接（这是新视图）
    radar_dir = SITE_DIR / "radar"
    radar_dir.mkdir(parents=True, exist_ok=True)
    md_path = TOPICS_DIR / f"radar.{today}.md"
    md_path.write_text(md, encoding="utf-8")
    log(f"   ✓ {md_path}")

    # 渲染整站（同时把新 md 也带上）
    log("  🏗️ build site")
    run([PY, str(ROOT / "curator.py"), "site"], check=False)

    # push site
    if not args.no_push:
        log("  ☁️ push curio-site")
        push_site()

    # 邮件
    if not args.no_email:
        log("  📧 self-notify")
        run([PY, "-m", "agent.notify_email"], check=False)

    # 广播给订阅者
    if not args.no_worker:
        log(f"  📢 broadcast cadence={args.cadence}")
        run([PY, "-m", "agent.worker_sync", "broadcast", "--cadence", args.cadence], check=False)

    log("")
    log("✅ unified finalize 完成")


def push_site():
    """push site/ 到 curio-site 仓库"""
    pat = PAT_FILE.read_text().strip() if PAT_FILE.exists() else ""
    if not pat:
        log("⚠️ 没找到 .gh_pat，跳过 push")
        return
    site = SITE_DIR
    run(["git", "-C", str(site), "add", "-A"], check=False)
    run(["git", "-C", str(site), "commit", "-q", "-m",
         f"radar update {time.strftime('%Y-%m-%d %H:%M')}"], check=False)
    remote = f"https://{GH_USER}:{pat}@github.com/{GH_USER}/{GH_REPO}.git"
    run(["git", "-C", str(site), "push", remote, "main"], check=False)


# ============================================================
# 备用：legacy 一键模式（老占位算法，不需要 Claude 介入）
# ============================================================

def cmd_legacy(args):
    """老逻辑：跑 curator site 直接出占位结果"""
    log("📰 legacy mode —— 直接跑 curator site（占位算法）")
    run([PY, str(ROOT / "curator.py"), "site"])
    if not args.no_push:
        publish()


def cmd_process_pending(args):
    """处理用户通过 [curio-generate] Issue 提交的生成请求

    流程：
    1. 调 worker_sync ingest_generate → 拉 Issue 写 .pending_generate.json
    2. 读 pending → 对每个领域跑 prepare（仅那个 domain）
    3. 退出 → 让 automation 后续阶段（Claude 写 scored）继续接力
       或：用户后续手动跑 finalize 完成
    """
    log("⚡ Curio process_pending — 处理用户的生成请求")

    # 1. ingest 最新 Issue
    log("📥 ingest [curio-generate] issues")
    run([PY, "-m", "agent.worker_sync", "ingest_generate"], check=False)

    pending_file = ROOT / ".pending_generate.json"
    if not pending_file.exists():
        log("（无 pending）")
        return

    try:
        data = json.loads(pending_file.read_text(encoding="utf-8"))
    except Exception as e:
        log(f"❌ 读 pending 失败: {e}")
        return

    pending = data.get("pending") or []
    if not pending:
        log("（pending 列表空）")
        return

    log(f"   {len(pending)} 个待生成领域：{[p.get('domain_id') for p in pending]}")

    # 2. 对每个 domain 跑 prepare
    domain_ids = [p["domain_id"] for p in pending]
    cmd = [PY, str(ROOT / "cli_generate.py"), "prepare", "--domains"] + domain_ids
    log(f"   $ {' '.join(cmd)}")
    run(cmd, check=False)

    log("")
    log("✅ process_pending 完成 prepare 阶段")
    log("   下一步：让 Claude（或 automation）处理 _run_plan.json 里的 score-prompt")
    log("   再跑：cli_generate.py prepare_notes  → finalize")
    log("   完成后请记得调 worker_sync 关掉 Issue：")
    for p in pending:
        log(f"     python -m agent.worker_sync close_issue --num {p['issue']} --success")


# ============================================================
# 入口
# ============================================================

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_prep = sub.add_parser("prepare", help="阶段1：抓数据+生成LLM prompts")
    p_prep.add_argument("--domains", nargs="*", help="只处理指定领域 ID")
    p_prep.set_defaults(func=cmd_prepare)

    p_notes = sub.add_parser("prepare_notes", help="阶段2.5：scored.json 后给必读生成中文导读 prompt")
    p_notes.set_defaults(func=cmd_prepare_notes)

    p_fin = sub.add_parser("finalize", help="阶段3：拼装+渲染+push+邮件+worker群发")
    p_fin.add_argument("--no-push", action="store_true")
    p_fin.add_argument("--no-email", action="store_true", help="跳过自用邮件推送")
    p_fin.add_argument("--no-worker", action="store_true", help="跳过 worker 同步与订阅者群发")
    p_fin.add_argument("--cadence", choices=["daily", "weekly"], default=None,
                       help="本次 broadcast 推送给哪个 cadence 的订阅者（默认 weekly）")
    p_fin.set_defaults(func=cmd_finalize)

    p_proc = sub.add_parser("process_pending", help="处理用户通过 [curio-generate] Issue 提交的请求")
    p_proc.set_defaults(func=cmd_process_pending)

    p_uni = sub.add_parser("prepare_unified",
                           help="阶段1（unified 模式）：合并所有域候选 → 一份 unified.score-prompt.md")
    p_uni.set_defaults(func=cmd_prepare_unified)

    p_unif = sub.add_parser("finalize_unified",
                            help="阶段3（unified 模式）：读 unified.scored.json → radar/{date}.md → site → push → 邮件")
    p_unif.add_argument("--no-push", action="store_true")
    p_unif.add_argument("--no-email", action="store_true")
    p_unif.add_argument("--no-worker", action="store_true")
    p_unif.add_argument("--cadence", choices=["daily", "weekly"], default="daily")
    p_unif.set_defaults(func=cmd_finalize_unified)

    p_leg = sub.add_parser("legacy", help="老逻辑：占位算法直跑+push")
    p_leg.add_argument("--no-push", action="store_true")
    p_leg.set_defaults(func=cmd_legacy)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
