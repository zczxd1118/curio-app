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

    # 0.2 ingest 订阅请求兜底 → worker /subscribe
    log("📥 ingest subscribe requests (GitHub fallback)")
    run([PY, "-m", "agent.worker_sync", "ingest_subscribe"], check=False)

    domains = args.domains or list_active_domains()
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
        cand_path = TOPICS_DIR / f"{d}.candidates.json"
        if not cand_path.exists():
            log(f"  ⚠️ {cand_path.name} 不存在，跳过该领域")
            continue
        log(f"  🎯 generate score prompt")
        run([PY, str(ROOT / "curator.py"), "score", str(cand_path)], check=False)

        # curator.py 用候选里 domain 字段（中文名）作 slug 写文件
        # 我们要从 candidates.json 里读出真正的 slug
        try:
            cand = json.loads(cand_path.read_text(encoding="utf-8"))
            domain_name = cand.get("domain", d)
            # 复制 slugify 逻辑（curator.py:40）
            import re
            slug = re.sub(r"[^\w\u4e00-\u9fa5]+", "-", domain_name.lower()).strip("-")
        except Exception:
            slug = d

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
    """阶段 3：所有 *.scored.json 已就绪 → digest → write-prompts → 等 article 写完后 → assemble → site → push"""
    log("📰 Curio finalize —— 拼装 → 渲染 → push")

    plan_path = TOPICS_DIR / "_run_plan.json"
    if not plan_path.exists():
        log("  ⚠️ 没找到 _run_plan.json，回落到 curator site 直跑（占位算法）")
        run([PY, str(ROOT / "curator.py"), "site"])
    else:
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        # 校验每个领域是否有 scored.json（自动跳过缺的，不阻塞整体）
        for d in plan["domains"]:
            sp = Path(d["expected_scored_file"])
            if not sp.exists():
                log(f"  ⚠️ {sp.name} 缺失，automation 没处理这个领域，跳过")
                continue
            log(f"  ✓ {sp.name} 已就绪")

        # 跑 site（curator.py 的 site 子命令会读所有 *.scored.json 渲染）
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
        log(f"   网址：https://{GH_USER}.github.io/{GH_REPO}/")


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
        log(f"  🌐 https://{GH_USER}.github.io/{GH_REPO}/")
        return True
    except subprocess.CalledProcessError as e:
        log(f"  ❌ push failed: {e}")
        return False


# ============================================================
# 备用：legacy 一键模式（老占位算法，不需要 Claude 介入）
# ============================================================

def cmd_legacy(args):
    """老逻辑：跑 curator site 直接出占位结果"""
    log("📰 legacy mode —— 直接跑 curator site（占位算法）")
    run([PY, str(ROOT / "curator.py"), "site"])
    if not args.no_push:
        publish()


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

    p_leg = sub.add_parser("legacy", help="老逻辑：占位算法直跑+push")
    p_leg.add_argument("--no-push", action="store_true")
    p_leg.set_defaults(func=cmd_legacy)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
