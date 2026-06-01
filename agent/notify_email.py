#!/usr/bin/env python3
"""
Curio 邮件推送模块

每周一 automation 跑完 finalize 后，自动发一封"本期摘要"到用户邮箱。

读取：
  - .smtp_secret（格式 SMTP_PASS=xxx，单行）
  - profile.yaml（拿收件人 / 是否启用）
  - topics/*.scored.json（拿本期必读列表）

用法：
  python -m agent.notify_email                  # 真发
  python -m agent.notify_email --dry-run        # 只打印不发
  python -m agent.notify_email --force          # 即使 profile.email.enabled=false 也发
"""

from __future__ import annotations
import argparse
import json
import os
import smtplib
import ssl
import sys
import time
from email.message import EmailMessage
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
SECRET_FILE = ROOT / ".smtp_secret"
PROFILE = ROOT / "profile.yaml"
TOPICS = ROOT / "topics"

SITE_URL = "https://curioradar.fun/"

# QQ 邮箱默认配置；profile.yaml 里可覆盖
DEFAULT_SMTP = {
    "host": "smtp.qq.com",
    "port": 465,
    "use_ssl": True,
    # user/from/to 由 profile.yaml 提供
}


# ============================================================
# 凭证 + 配置
# ============================================================

def read_password() -> str:
    pwd = os.getenv("SMTP_PASS")
    if pwd:
        return pwd
    if not SECRET_FILE.exists():
        return ""
    for line in SECRET_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("SMTP_PASS=") and not line.startswith("#"):
            return line.split("=", 1)[1].strip().strip("'\"")
    return ""


def read_email_cfg() -> dict:
    """从 profile.yaml.email 读邮件配置；缺失字段用默认。"""
    import yaml
    cfg = yaml.safe_load(PROFILE.read_text(encoding="utf-8")) or {}
    em = cfg.get("email") or {}
    out = {
        "enabled": em.get("enabled", False),
        "to": em.get("to", ""),
        "user": em.get("user", em.get("to", "")),   # SMTP 登录用户名默认 = to
        "from_name": em.get("from_name", "Curio Bot"),
        "host": em.get("host", DEFAULT_SMTP["host"]),
        "port": em.get("port", DEFAULT_SMTP["port"]),
        "use_ssl": em.get("use_ssl", DEFAULT_SMTP["use_ssl"]),
    }
    return out


# ============================================================
# 收集本期摘要
# ============================================================

def _active_domain_names() -> set:
    """从 sources.yaml 读当前活跃的域名（中文显示名 + 英文 slug 都算）"""
    try:
        import yaml
        cfg = yaml.safe_load((ROOT / "sources.yaml").read_text(encoding="utf-8")) or {}
        names = set()
        for slug, info in (cfg.get("domains") or {}).items():
            names.add(slug)
            n = (info or {}).get("name")
            if n:
                names.add(n)
        return names
    except Exception:
        return set()


def collect_digest() -> dict:
    """优先读 unified.scored.json（当前 unified 模式）；
    fallback 才扫 topics/*.scored.json，并按 sources.yaml 当前域过滤掉历史残骸。
    """
    digest = {"date": time.strftime("%Y-%m-%d"), "domains": []}

    # ===== 优先：unified.scored.json =====
    unified = TOPICS / "unified.scored.json"
    if unified.exists():
        try:
            d = json.loads(unified.read_text(encoding="utf-8"))
        except Exception:
            d = None
        if d and isinstance(d, dict):
            digest["date"] = d.get("date") or digest["date"]
            # 把 headlines + shortlist 按 domain 分组
            by_domain: dict[str, dict] = {}
            for h in (d.get("headlines") or []):
                name = h.get("domain") or "未分类"
                grp = by_domain.setdefault(name, {"name": name, "intro": "", "must_read": []})
                grp["must_read"].append({
                    "title": (h.get("title") or "")[:120],
                    "url": h.get("url") or "",
                    "platform": h.get("source") or h.get("platform") or "",
                    "why": (h.get("implication") or h.get("lead") or "")[:200],
                })
            # intro 整体放到第一个域上（unified 只有一段 intro）
            unified_intro = (d.get("intro") or "")[:300]
            for i, name in enumerate(by_domain):
                if i == 0 and unified_intro:
                    by_domain[name]["intro"] = unified_intro
            digest["domains"] = list(by_domain.values())
            if digest["domains"]:
                return digest

    # ===== fallback：老 4 域分发模式 =====
    active = _active_domain_names()
    for f in sorted(TOPICS.glob("*.scored.json")):
        if f.name == "unified.scored.json":
            continue
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        domain_name = d.get("domain") or f.stem.replace(".scored", "")
        slug_guess = f.stem.replace(".scored", "")
        # 按当前 sources.yaml 域过滤，避免老残骸
        if active and domain_name not in active and slug_guess not in active:
            continue
        must = d.get("must_read", []) or []
        if not must:
            continue
        digest["domains"].append({
            "name": domain_name,
            "intro": (d.get("intro") or "")[:300],
            "must_read": [
                {
                    "title": (m.get("title") or "")[:120],
                    "url": m.get("url") or "",
                    "platform": m.get("platform") or "",
                    "why": (m.get("why_recommend") or "")[:200],
                }
                for m in must[:6]
            ],
        })
    return digest


# ============================================================
# 渲染 Markdown + HTML
# ============================================================

def render_markdown(digest: dict) -> str:
    lines = []
    lines.append(f"# Curio 本期摘要 · {digest['date']}")
    lines.append("")
    lines.append(f"🌐 [打开网页版]({SITE_URL})")
    lines.append("")
    if not digest["domains"]:
        lines.append("> 本期没有领域产出必读内容。可能是周末或源失效，跑一次手动 prepare 看看。")
        return "\n".join(lines)
    for d in digest["domains"]:
        lines.append(f"## {d['name']}")
        lines.append("")
        if d["intro"]:
            lines.append(f"> {d['intro']}")
            lines.append("")
        for i, m in enumerate(d["must_read"], 1):
            plat = f" · `{m['platform']}`" if m["platform"] else ""
            if m["url"]:
                lines.append(f"**{i}. [{m['title']}]({m['url']})**{plat}")
            else:
                lines.append(f"**{i}. {m['title']}**{plat}")
            if m["why"]:
                lines.append(f"   - {m['why']}")
            lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"反馈直接在网页底部点「提交反馈到 GitHub」，下次跑前 Agent 会读取。")
    return "\n".join(lines)


def md_to_simple_html(md: str) -> str:
    """极简 markdown→HTML（避免依赖 markdown 库）"""
    try:
        import markdown as md_lib
        return md_lib.markdown(md, extensions=["tables", "fenced_code"])
    except ImportError:
        return f"<pre style='font-family:ui-monospace,Menlo,monospace;white-space:pre-wrap'>{escape(md)}</pre>"


# ============================================================
# 发送
# ============================================================

def send(cfg: dict, password: str, subject: str, md_body: str, dry_run: bool = False) -> tuple[bool, str]:
    if dry_run:
        print("=== [dry-run] 邮件不会真发 ===")
        print(f"From: {cfg['from_name']} <{cfg['user']}>")
        print(f"To:   {cfg['to']}")
        print(f"Subject: {subject}")
        print("--- body (markdown) ---")
        print(md_body[:1500] + ("\n...(truncated)" if len(md_body) > 1500 else ""))
        return True, "dry-run"

    msg = EmailMessage()
    msg["From"] = f"{cfg['from_name']} <{cfg['user']}>"
    msg["To"] = cfg["to"]
    msg["Subject"] = subject
    msg.set_content(md_body)

    html = md_to_simple_html(md_body)
    msg.add_alternative(
        f"<html><body style='font-family:-apple-system,BlinkMacSystemFont,sans-serif;"
        f"max-width:680px;margin:0 auto;padding:16px;line-height:1.7;color:#222'>"
        f"{html}</body></html>",
        subtype="html"
    )

    try:
        if cfg["use_ssl"]:
            ctx = ssl.create_default_context()
            with smtplib.SMTP_SSL(cfg["host"], cfg["port"], context=ctx, timeout=30) as s:
                s.login(cfg["user"], password)
                s.send_message(msg)
        else:
            with smtplib.SMTP(cfg["host"], cfg["port"], timeout=30) as s:
                s.starttls()
                s.login(cfg["user"], password)
                s.send_message(msg)
        return True, "ok"
    except Exception as e:
        return False, f"SMTP 失败：{e}"


# ============================================================
# 入口
# ============================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="只打印不真发")
    parser.add_argument("--force", action="store_true", help="即使 profile.email.enabled=false 也发")
    args = parser.parse_args()

    cfg = read_email_cfg()
    if not cfg["enabled"] and not args.force:
        print("[notify_email] profile.yaml.email.enabled = false，跳过（用 --force 强发）")
        return 0
    if not cfg["to"]:
        print("[notify_email] profile.yaml.email.to 为空，跳过")
        return 0

    password = read_password()
    if not password and not args.dry_run:
        print("[notify_email] ❌ 没有 SMTP_PASS（.smtp_secret 不存在或格式错误）")
        return 1

    digest = collect_digest()
    md = render_markdown(digest)
    n_domains = len(digest["domains"])
    n_must = sum(len(d["must_read"]) for d in digest["domains"])
    subject = f"📰 Curio · {digest['date']} · {n_domains} 域 · {n_must} 必读"

    print(f"[notify_email] 收件人：{cfg['to']} · 主题：{subject}")
    ok, msg = send(cfg, password, subject, md, dry_run=args.dry_run)
    if ok:
        print(f"  ✅ {msg}")
        return 0
    else:
        print(f"  ❌ {msg}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
