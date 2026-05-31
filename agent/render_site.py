"""
render_site.py — 把 topics/*.weekly.*.md 渲染成静态网站（v0.7：可交互）

输出：
  site/
  ├── index.html              首页（领域卡片 + 添加 modal + 跨领域 Top N + 最新各期）
  ├── d/<domain>/index.html   领域往期列表
  ├── d/<domain>/<date>.html  单期周刊（含可点反馈区）
  ├── styles.css              共享样式
  └── app.js                  前端交互（调 server.py API）
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import markdown as mdlib
import yaml

ROOT = Path(__file__).resolve().parent.parent
TOPICS = ROOT / "topics"
SITE = ROOT / "site"
PROFILE = ROOT / "profile.yaml"
SOURCES = ROOT / "sources.yaml"


# ============================================================================
# CSS
# ============================================================================
CSS = r"""
:root {
  /* 默认深色（报纸夜读模式） */
  --bg: #0a0a0b;
  --bg-soft: #111114;
  --bg-elev: #17171b;
  --line: #26262c;
  --text: #ededed;
  --text-soft: #a8a8af;
  --text-mute: #6e6e76;
  --accent: #d4af37;
  --accent-soft: #b8941f;
  --link: #6e8efb;
  --green: #5cb85c;
  --red: #d9534f;
  --serif: 'Source Serif Pro', 'Noto Serif SC', Georgia, 'Songti SC', serif;
  --sans:  'Inter', 'PingFang SC', system-ui, sans-serif;
  --mono:  'JetBrains Mono', 'SF Mono', Menlo, monospace;
  --shadow: 0 4px 24px rgba(0,0,0,0.45);
}
html[data-theme="light"] {
  --bg: #fbfbfa;
  --bg-soft: #f4f3ee;
  --bg-elev: #ebe9e2;
  --line: #d8d6cf;
  --text: #1a1a1c;
  --text-soft: #4a4a52;
  --text-mute: #888893;
  --accent: #b8941f;
  --accent-soft: #9a7a16;
  --link: #3b5bdb;
  --shadow: 0 4px 16px rgba(60,60,70,0.08);
}
html { transition: color 0.3s ease, background 0.3s ease; }
html[data-theme="light"] .nav { background: rgba(251,251,250,0.92) !important; }
* { box-sizing: border-box; }
html, body { background: var(--bg); color: var(--text); margin: 0; padding: 0; }
body {
  font-family: var(--serif);
  font-size: 17px;
  line-height: 1.72;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

/* Nav */
.nav { position: sticky; top: 0; z-index: 50; background: rgba(10,10,11,0.92); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }
.nav-inner { max-width: 1080px; margin: 0 auto; padding: 14px 24px; display: flex; align-items: center; gap: 24px; font-family: var(--sans); font-size: 13px; }
.brand { font-family: var(--serif); font-size: 18px; font-weight: 600; letter-spacing: 0.02em; color: var(--text); text-decoration: none; }
.brand .dot { color: var(--accent); }
.nav .author { color: var(--text-mute); margin-left: 4px; }
.nav-links { display: flex; gap: 16px; margin-left: auto; align-items: center; flex-wrap: wrap; }
.nav-links a { color: var(--text-soft); text-decoration: none; padding: 4px 10px; border-radius: 4px; transition: all 0.15s; }
.nav-links a:hover { color: var(--text); background: var(--bg-elev); }
.nav-links a.active { color: var(--accent); }

/* Main */
main { max-width: 720px; margin: 0 auto; padding: 48px 24px 96px; }
.hero { border-bottom: 2px solid var(--accent); padding-bottom: 32px; margin-bottom: 40px; }
.hero .kicker { font-family: var(--sans); font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--accent); margin-bottom: 14px; }
.hero h1 { font-family: var(--serif); font-weight: 700; font-size: 38px; line-height: 1.18; margin: 0 0 16px; letter-spacing: -0.01em; }
.hero .meta { font-family: var(--sans); font-size: 13px; color: var(--text-mute); }

/* Markdown content */
.content h2 { font-family: var(--serif); font-weight: 600; font-size: 24px; margin: 56px 0 16px; padding-bottom: 8px; border-bottom: 1px solid var(--line); letter-spacing: -0.005em; }
.content h3 { font-family: var(--serif); font-weight: 600; font-size: 19px; margin: 32px 0 8px; }
.content p { margin: 0 0 18px; }
.content a { color: var(--link); text-decoration: none; border-bottom: 1px solid transparent; }
.content a:hover { border-bottom-color: var(--link); }
.content em { color: var(--text-soft); font-style: normal; font-size: 14px; }
.content strong { color: var(--text); font-weight: 600; }
.content blockquote { margin: 20px 0; padding: 14px 20px; border-left: 3px solid var(--accent); background: var(--bg-soft); font-style: italic; color: var(--text-soft); }
.content blockquote p:last-child { margin-bottom: 0; }
.content code { font-family: var(--mono); font-size: 14px; background: var(--bg-elev); padding: 2px 6px; border-radius: 3px; color: var(--accent); }
.content pre { background: var(--bg-elev); padding: 14px; border-radius: 6px; overflow-x: auto; border: 1px solid var(--line); }
.content ul, .content ol { padding-left: 22px; margin: 0 0 18px; }
.content li { margin-bottom: 6px; }
.content table { width: 100%; border-collapse: collapse; margin: 20px 0; font-family: var(--sans); font-size: 14px; }
.content th { background: var(--bg-elev); text-align: left; padding: 10px 12px; font-weight: 600; color: var(--text-soft); font-size: 12px; letter-spacing: 0.04em; text-transform: uppercase; border-bottom: 1px solid var(--accent-soft); }
.content td { padding: 12px; border-bottom: 1px solid var(--line); vertical-align: top; }
.content tr:hover td { background: var(--bg-soft); }
.content hr { border: none; height: 1px; background: var(--line); margin: 40px 0; }
.content details { background: var(--bg-soft); padding: 12px 16px; border-radius: 6px; border: 1px solid var(--line); margin: 16px 0; }
.content summary { cursor: pointer; color: var(--text-soft); font-family: var(--sans); font-size: 13px; }

/* 互动反馈区 */
.feedback { margin-top: 80px; padding: 32px; background: var(--bg-soft); border-radius: 8px; border: 1px solid var(--line); }
.feedback h2 { margin-top: 0; border: none; padding: 0; }
.feedback .desc { font-family: var(--sans); font-size: 13px; color: var(--text-mute); margin: 8px 0 24px; }
.fb-item { padding: 16px 0; border-bottom: 1px solid var(--line); }
.fb-item:last-of-type { border-bottom: none; }
.fb-item .fb-title { font-family: var(--serif); font-size: 15px; margin-bottom: 10px; color: var(--text); }
.fb-item .fb-title .num { display: inline-block; min-width: 28px; color: var(--accent); font-weight: 600; }
.fb-buttons { display: flex; gap: 8px; margin-bottom: 8px; flex-wrap: wrap; }
.fb-btn { font-family: var(--sans); font-size: 12px; padding: 6px 14px; border-radius: 999px; border: 1px solid var(--line); background: transparent; color: var(--text-soft); cursor: pointer; transition: all 0.15s; }
.fb-btn:hover { border-color: var(--text-soft); color: var(--text); }
.fb-btn.active { color: var(--bg); font-weight: 600; }
.fb-btn[data-rating="useful"].active { background: var(--green); border-color: var(--green); }
.fb-btn[data-rating="meh"].active    { background: var(--text-mute); border-color: var(--text-mute); color: #fff; }
.fb-btn[data-rating="off"].active    { background: var(--red); border-color: var(--red); }
.fb-note { width: 100%; min-height: 32px; background: var(--bg); border: 1px solid var(--line); color: var(--text); padding: 8px 10px; font-family: var(--sans); font-size: 13px; border-radius: 4px; resize: vertical; }
.fb-note:focus { outline: none; border-color: var(--accent-soft); }
.long-term { margin-top: 24px; padding-top: 20px; border-top: 1px dashed var(--line); }
.long-term label { display: block; font-family: var(--sans); font-size: 12px; color: var(--text-soft); letter-spacing: 0.05em; margin-top: 14px; margin-bottom: 6px; }
.long-term input { width: 100%; background: var(--bg); border: 1px solid var(--line); color: var(--text); padding: 10px 12px; font-family: var(--sans); font-size: 14px; border-radius: 4px; }
.long-term input:focus { outline: none; border-color: var(--accent-soft); }
.fb-submit { margin-top: 24px; display: flex; gap: 12px; align-items: center; }
.btn-primary { font-family: var(--sans); font-size: 14px; font-weight: 500; padding: 10px 24px; border-radius: 6px; cursor: pointer; background: var(--accent); color: var(--bg); border: none; transition: all 0.15s; }
.btn-primary:hover { background: var(--accent-soft); }
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }
.fb-status { font-family: var(--sans); font-size: 13px; color: var(--text-mute); }
.fb-status.success { color: var(--green); }
.fb-status.error { color: var(--red); }

/* 首页 */
.domain-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin: 32px 0; }
.domain-card {
  padding: 28px 24px 24px; background: var(--bg-soft);
  border: 1px solid var(--line); border-radius: 12px;
  text-decoration: none; color: var(--text);
  transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease, box-shadow 0.18s ease;
  position: relative; display: block;
  overflow: hidden; min-height: 168px;
}
.domain-card::before {
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent), transparent);
  transform: scaleX(0); transform-origin: left;
  transition: transform 0.3s ease;
}
.domain-card:hover { border-color: var(--accent-soft); background: var(--bg-elev); transform: translateY(-3px); box-shadow: var(--shadow); }
.domain-card:hover::before { transform: scaleX(1); }
.domain-card .badge {
  width: 44px; height: 44px; border-radius: 10px;
  background: linear-gradient(135deg, rgba(212,175,55,0.18), rgba(212,175,55,0.04));
  border: 1px solid rgba(212,175,55,0.3);
  display: inline-flex; align-items: center; justify-content: center;
  margin-bottom: 16px; color: var(--accent);
  font-family: var(--serif); font-size: 18px; font-weight: 600; letter-spacing: 0.02em;
}
.domain-card .badge svg { width: 20px; height: 20px; stroke: currentColor; fill: none; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
.domain-card .name { font-family: var(--serif); font-size: 19px; font-weight: 600; margin-bottom: 4px; letter-spacing: -0.01em; }
.domain-card .meta { font-family: var(--sans); font-size: 12px; color: var(--text-mute); display: flex; align-items: center; gap: 6px; }
.domain-card .meta .dot { width: 3px; height: 3px; border-radius: 50%; background: var(--text-mute); display: inline-block; }
html[data-theme="light"] .domain-card .badge {
  background: linear-gradient(135deg, rgba(184,148,31,0.12), rgba(184,148,31,0.02));
  border-color: rgba(184,148,31,0.25);
}
.domain-card .del-btn { position: absolute; top: 8px; right: 8px; width: 24px; height: 24px; border-radius: 50%; background: transparent; border: 1px solid var(--line); color: var(--text-mute); font-size: 14px; line-height: 20px; cursor: pointer; opacity: 0; transition: opacity 0.15s; padding: 0; }
.domain-card:hover .del-btn { opacity: 1; }
.domain-card .del-btn:hover { color: var(--red); border-color: var(--red); }
.add-domain {
  border: 1.5px dashed var(--line); background: transparent;
  display: flex; align-items: center; justify-content: center;
  flex-direction: column; color: var(--text-mute); cursor: pointer;
  font-family: var(--sans); font-size: 14px;
  min-height: 168px;
}
.add-domain::before { display: none; }
.add-domain:hover { border-color: var(--accent-soft); color: var(--accent); background: transparent; transform: translateY(-3px); }
.add-domain .plus-icon {
  width: 40px; height: 40px; border-radius: 10px;
  border: 1.5px dashed currentColor;
  display: inline-flex; align-items: center; justify-content: center;
  margin-bottom: 10px; transition: all 0.18s;
}
.add-domain:hover .plus-icon { border-style: solid; }
.add-domain .plus-icon svg { width: 18px; height: 18px; stroke: currentColor; fill: none; stroke-width: 1.6; stroke-linecap: round; }

.issue-list { list-style: none; padding: 0; margin: 0; }
.issue-list li { border-bottom: 1px solid var(--line); }
.issue-list a { color: var(--text); text-decoration: none; }
.issue-list a:hover { color: var(--accent); }
.issue-list .date { font-family: var(--mono); font-size: 13px; color: var(--text-mute); min-width: 100px; }
.issue-list .title { font-family: var(--serif); font-size: 17px; flex: 1; }

/* 领域索引页的 issue-row（升级款，整行可点） */
.issue-row { padding: 0; }
.issue-row .issue-link {
  display: flex; align-items: center; gap: 16px;
  padding: 18px 16px; border-radius: 6px;
  transition: all 0.15s;
}
.issue-row .issue-link:hover {
  background: var(--bg-soft);
  padding-left: 22px;
}
.issue-row .arrow {
  margin-left: auto;
  color: var(--text-mute);
  font-family: var(--mono); font-size: 18px;
  transition: transform 0.15s, color 0.15s;
}
.issue-row .issue-link:hover .arrow { color: var(--accent); transform: translateX(4px); }
.issue-row .issue-link:hover .title { color: var(--accent); }

/* 空状态 */
.empty-state {
  text-align: center; padding: 48px 24px;
  background: var(--bg-soft); border: 1px dashed var(--line);
  border-radius: 8px; margin: 32px 0;
}
.empty-state .empty-icon { font-size: 48px; margin-bottom: 16px; opacity: 0.6; }
.empty-state h3 { font-family: var(--serif); font-size: 22px; margin: 0 0 12px; }
.empty-state p { color: var(--text-soft); font-family: var(--sans); font-size: 14px; margin: 0 0 24px; }
.btn-primary-link {
  display: inline-block; padding: 10px 20px;
  background: var(--accent); color: var(--bg) !important;
  border-radius: 6px; text-decoration: none;
  font-family: var(--sans); font-size: 14px; font-weight: 500;
}
.btn-primary-link:hover { background: var(--accent-soft); }

/* Modal */
.modal-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.7); backdrop-filter: blur(4px); z-index: 100; align-items: center; justify-content: center; }
.modal-overlay.show { display: flex; }
.modal { background: var(--bg-soft); border: 1px solid var(--line); border-radius: 12px; padding: 32px; min-width: 420px; max-width: 90vw; box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
.modal h3 { margin: 0 0 8px; font-family: var(--serif); font-size: 22px; }
.modal p { margin: 0 0 20px; color: var(--text-soft); font-family: var(--sans); font-size: 13px; }
.modal .form-row { margin-bottom: 16px; }
.modal label { display: block; font-family: var(--sans); font-size: 12px; color: var(--text-soft); letter-spacing: 0.05em; margin-bottom: 6px; text-transform: uppercase; }
.modal input, .modal select { width: 100%; padding: 10px 12px; background: var(--bg); border: 1px solid var(--line); color: var(--text); border-radius: 4px; font-family: var(--sans); font-size: 14px; }
.modal input:focus, .modal select:focus { outline: none; border-color: var(--accent-soft); }
.modal .icon-row { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px; }
.modal .icon-pick { width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; background: var(--bg); border: 1px solid var(--line); border-radius: 6px; cursor: pointer; font-size: 18px; transition: all 0.15s; }
.modal .icon-pick:hover { border-color: var(--text-soft); }
.modal .icon-pick.active { border-color: var(--accent); background: var(--bg-elev); transform: scale(1.05); }

/* 领域类型选择器（替代 emoji 图标） */
.modal .type-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 8px; margin-top: 6px; max-height: 220px; overflow-y: auto;
}
.modal .type-pick {
  display: flex; align-items: center; gap: 8px;
  padding: 10px 12px; background: var(--bg-elev);
  border: 1px solid var(--line); border-radius: 8px;
  cursor: pointer; transition: all 0.15s;
  font-family: var(--sans); font-size: 13px; color: var(--text-soft);
}
.modal .type-pick:hover { border-color: var(--accent-soft); color: var(--text); }
.modal .type-pick.active {
  border-color: var(--accent); color: var(--accent);
  background: rgba(212,175,55,0.08);
}
.modal .type-pick .ico {
  width: 18px; height: 18px;
  display: inline-flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.modal .type-pick .ico svg {
  width: 16px; height: 16px;
  stroke: currentColor; fill: none; stroke-width: 1.7;
  stroke-linecap: round; stroke-linejoin: round;
}
.modal .type-pick .lbl { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.modal-actions { display: flex; gap: 12px; justify-content: flex-end; margin-top: 24px; }
.btn-secondary { font-family: var(--sans); font-size: 14px; padding: 10px 20px; border-radius: 6px; cursor: pointer; background: transparent; color: var(--text-soft); border: 1px solid var(--line); }
.btn-secondary:hover { background: var(--bg-elev); color: var(--text); }

/* Toast */
.toast { position: fixed; bottom: 32px; left: 50%; transform: translateX(-50%) translateY(100px); background: var(--bg-elev); border: 1px solid var(--accent-soft); color: var(--text); padding: 12px 20px; border-radius: 6px; font-family: var(--sans); font-size: 14px; z-index: 200; opacity: 0; transition: all 0.3s ease; box-shadow: 0 8px 30px rgba(0,0,0,0.4); }
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
.toast.error { border-color: var(--red); }

.rule-double { border-top: 3px double var(--accent); border-bottom: 1px solid var(--accent-soft); height: 4px; margin: 32px 0; }

footer { text-align: center; padding: 32px; font-family: var(--sans); font-size: 12px; color: var(--text-mute); border-top: 1px solid var(--line); margin-top: 80px; }

/* No-server fallback notice */
.fallback-notice { background: var(--bg-elev); border: 1px dashed var(--accent-soft); padding: 12px 16px; border-radius: 6px; font-family: var(--sans); font-size: 13px; color: var(--text-soft); margin: 24px 0; }
.fallback-notice code { background: var(--bg); padding: 2px 6px; border-radius: 3px; color: var(--accent); font-family: var(--mono); }

/* ===== 一键生成 ===== */
.gen-btn {
  position: absolute; bottom: 12px; right: 12px;
  font-family: var(--sans); font-size: 11px;
  padding: 4px 10px; border-radius: 999px;
  background: var(--accent); color: var(--bg);
  border: none; cursor: pointer; font-weight: 500;
  opacity: 0; transition: opacity 0.15s;
}
.domain-card:hover .gen-btn { opacity: 1; }
.gen-btn:hover { background: var(--accent-soft); }
.gen-btn:disabled { opacity: 0.7; cursor: wait; }

/* 进度条 */
.gen-progress {
  position: fixed; bottom: 0; left: 0; right: 0;
  background: var(--bg-elev); border-top: 1px solid var(--accent-soft);
  z-index: 80; padding: 14px 24px;
  font-family: var(--sans); font-size: 13px;
  display: none; transform: translateY(100%);
  transition: transform 0.25s ease;
}
.gen-progress.show { display: block; transform: translateY(0); }
.gen-progress-bar { height: 4px; background: var(--bg); border-radius: 2px; overflow: hidden; margin: 8px 0; }
.gen-progress-fill { height: 100%; background: var(--accent); width: 0; transition: width 0.4s ease; }
.gen-status { display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.gen-status .domain-label { color: var(--accent); font-weight: 500; }
.gen-status .step-msg { color: var(--text-soft); flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.gen-status .pct { color: var(--text-mute); font-family: var(--mono); }

/* ============== B 阶段 增强：主题切换 / 搜索 / 目录 ============== */

/* 主题切换按钮 */
.theme-toggle {
  background: transparent; border: 1px solid var(--line); color: var(--text-soft);
  width: 34px; height: 34px; border-radius: 8px; cursor: pointer;
  display: inline-flex; align-items: center; justify-content: center;
  transition: all 0.15s; padding: 0;
}
.theme-toggle:hover { color: var(--text); background: var(--bg-elev); border-color: var(--accent-soft); }
.theme-toggle svg { width: 16px; height: 16px; stroke: currentColor; fill: none; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
.theme-toggle .icon-sun { display: none; }
html[data-theme="light"] .theme-toggle .icon-sun { display: inline-flex; }
html[data-theme="light"] .theme-toggle .icon-moon { display: none; }
html[data-theme="light"] .theme-toggle .icon-moon-default { display: none; }

/* 订阅按钮 */
.subscribe-btn {
  background: var(--accent); border: 1px solid var(--accent); color: #0a0a0b;
  font-family: var(--sans); font-size: 13px; font-weight: 600; cursor: pointer;
  padding: 7px 14px; border-radius: 8px; transition: all 0.15s;
  display: inline-flex; align-items: center; gap: 6px; height: 34px;
}
.subscribe-btn:hover { background: var(--accent-soft); border-color: var(--accent-soft); color: #0a0a0b; transform: translateY(-1px); }
.subscribe-btn svg { width: 14px; height: 14px; stroke: currentColor; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
@media (max-width: 720px) { .subscribe-btn .sub-label { display: none; } }

/* 订阅 modal 复用 add-domain modal 样式，但加 checkbox / radio 视觉 */
.sub-domain-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
  max-height: 240px; overflow-y: auto; padding: 4px;
}
.sub-domain-pick {
  display: flex; align-items: center; gap: 8px; padding: 8px 10px;
  border: 1px solid var(--line); border-radius: 6px; cursor: pointer;
  transition: all 0.15s; background: var(--bg-elev); user-select: none;
  font-family: var(--sans); font-size: 13px; color: var(--text);
}
.sub-domain-pick:hover { border-color: var(--accent-soft); }
.sub-domain-pick.active { border-color: var(--accent); background: rgba(212,175,55,0.08); color: var(--accent); }
.sub-domain-pick .icon { font-size: 16px; }
.sub-cadence-row { display: flex; gap: 12px; margin-top: 4px; }
.sub-cadence-pick {
  flex: 1; padding: 12px; border: 1px solid var(--line); border-radius: 6px;
  cursor: pointer; transition: all 0.15s; text-align: center;
  font-family: var(--sans); color: var(--text);
}
.sub-cadence-pick:hover { border-color: var(--accent-soft); }
.sub-cadence-pick.active { border-color: var(--accent); background: rgba(212,175,55,0.08); color: var(--accent); }
.sub-cadence-pick .label { font-weight: 600; font-size: 14px; }
.sub-cadence-pick .meta { font-size: 11px; color: var(--text-mute); margin-top: 4px; }
.sub-cadence-pick.active .meta { color: var(--accent-soft); }

/* 旧 emoji 模式遗留（已废弃但避免 CSS 冲突）*/

/* 搜索框 */
.search-wrap { position: relative; }
.search-input {
  background: var(--bg-elev); border: 1px solid var(--line); color: var(--text);
  font-family: var(--sans); font-size: 13px; height: 34px;
  padding: 0 12px 0 32px; border-radius: 8px; width: 200px;
  transition: all 0.15s;
}
.search-input::placeholder { color: var(--text-mute); }
.search-input:focus { outline: none; border-color: var(--accent-soft); width: 260px; background: var(--bg-soft); }
.search-icon {
  position: absolute; left: 10px; top: 50%; transform: translateY(-50%);
  color: var(--text-mute); pointer-events: none;
  width: 14px; height: 14px;
  display: inline-flex; align-items: center; justify-content: center;
}
.search-icon svg { width: 14px; height: 14px; stroke: currentColor; fill: none; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
.search-results {
  position: absolute; top: calc(100% + 8px); right: 0; min-width: 360px; max-width: 440px;
  background: var(--bg-soft); border: 1px solid var(--line); border-radius: 8px;
  box-shadow: var(--shadow); padding: 8px; max-height: 480px; overflow-y: auto;
  display: none; z-index: 100;
}
.search-results.show { display: block; }
.search-result-item {
  display: block; padding: 10px 12px; border-radius: 6px;
  color: var(--text); text-decoration: none; cursor: pointer;
  border-bottom: 1px solid var(--line);
}
.search-result-item:last-child { border-bottom: none; }
.search-result-item:hover { background: var(--bg-elev); }
.search-result-item .sr-title { font-weight: 600; font-size: 14px; line-height: 1.4; margin-bottom: 4px; }
.search-result-item .sr-meta { font-family: var(--sans); font-size: 11px; color: var(--text-mute); display: flex; gap: 10px; }
.search-result-item .sr-meta .domain-tag { color: var(--accent); }
.search-results .empty { padding: 20px; text-align: center; color: var(--text-mute); font-family: var(--sans); font-size: 13px; }
.search-results mark { background: var(--accent-soft); color: var(--bg); padding: 0 2px; border-radius: 2px; }

/* 文章页右侧 TOC */
.toc {
  position: fixed; top: 80px; right: 24px; width: 200px;
  font-family: var(--sans); font-size: 12px;
  max-height: calc(100vh - 120px); overflow-y: auto;
  display: none;   /* 仅大屏显示 */
  z-index: 10;
  padding-left: 12px; border-left: 1px solid var(--line);
}
@media (min-width: 1240px) { .toc.has-items { display: block; } }
.toc-title { color: var(--text-mute); text-transform: uppercase; letter-spacing: 0.1em; font-size: 10px; margin-bottom: 8px; font-weight: 600; }
.toc a {
  display: block; padding: 4px 8px; color: var(--text-soft);
  text-decoration: none; line-height: 1.4; border-left: 2px solid transparent;
  margin-left: -10px; padding-left: 8px;
  transition: all 0.15s;
}
.toc a:hover { color: var(--text); }
.toc a.active { color: var(--accent); border-left-color: var(--accent); }
.toc a.lvl-3 { padding-left: 20px; font-size: 11px; }

@media (max-width: 720px) {
  .search-input, .search-input:focus { width: 120px; }
  .search-results { min-width: 280px; right: -60px; }
}
"""


# ============================================================================
# 前端 JS
# ============================================================================
APP_JS = r"""
// ===== 工具 =====
const API_BASE = '';  // 同源 → 用相对路径（本地 server 模式）
const WORKER_API = (window.CURIO_API_BASE || '').replace(/\/$/, '');  // 公网 Worker API
const GH_REPO = window.CURIO_GH_REPO || 'zczxd1118/curio-app';

function $(s, root=document) { return root.querySelector(s); }
function $$(s, root=document) { return Array.from(root.querySelectorAll(s)); }

// 调 Worker API（支持公网订阅 / 加领域）
async function workerApi(path, opts={}) {
  if (!WORKER_API) throw new Error('Worker API 未配置');
  const r = await fetch(WORKER_API + path, {
    headers: {'Content-Type': 'application/json'},
    ...opts,
  });
  const data = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(data.error || `HTTP ${r.status}`);
  return data;
}

function toast(msg, isError=false) {
  let t = $('.toast') || (() => {
    const el = document.createElement('div');
    el.className = 'toast';
    document.body.appendChild(el);
    return el;
  })();
  t.textContent = msg;
  t.classList.toggle('error', isError);
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2400);
}

async function api(path, opts={}) {
  const r = await fetch(API_BASE + path, {
    headers: {'Content-Type': 'application/json'},
    ...opts,
  });
  if (!r.ok) {
    const data = await r.json().catch(() => ({}));
    throw new Error(data.error || `HTTP ${r.status}`);
  }
  return r.json();
}

// 真实的"是否有可用后端"：仅当 /api/health 返回 ok 时为 true
// 通过 fetch 探测后写到 window.__CURIO_HAS_BACKEND（DOMContentLoaded 阶段设置）
function isServerMode() {
  return window.__CURIO_HAS_BACKEND === true;
}

// ===== 添加领域弹窗 =====
const ICONS = ['🤖','🏦','🔬','📈','🧬','⚛️','🎮','📚','🎨','🚀','🌍','💊','🏛️','🎬','⚖️','🔋'];

// 领域类型 → SVG icon（与后端 _SVG_ICONS 一致）
const DOMAIN_TYPES = [
  {key: 'ai',           label: 'AI / 科技',     svg: '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="2" x2="9" y2="4"/><line x1="15" y1="2" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="22"/><line x1="15" y1="20" x2="15" y2="22"/><line x1="20" y1="9" x2="22" y2="9"/><line x1="20" y1="15" x2="22" y2="15"/><line x1="2" y1="9" x2="4" y2="9"/><line x1="2" y1="15" x2="4" y2="15"/></svg>'},
  {key: 'finance',      label: '金融 / 投资',   svg: '<svg viewBox="0 0 24 24"><polyline points="3 17 9 11 13 15 21 7"/><polyline points="14 7 21 7 21 14"/></svg>'},
  {key: 'semiconductor',label: '半导体 / 芯片', svg: '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="1"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>'},
  {key: 'bigtech',      label: '大厂 / 公司',   svg: '<svg viewBox="0 0 24 24"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v8h4"/><path d="M18 9h2a2 2 0 0 1 2 2v11h-4"/><line x1="10" y1="6" x2="14" y2="6"/><line x1="10" y1="10" x2="14" y2="10"/><line x1="10" y1="14" x2="14" y2="14"/></svg>'},
  {key: 'biotech',      label: '生物 / 医疗',   svg: '<svg viewBox="0 0 24 24"><path d="M9 2v6"/><path d="M15 2v6"/><path d="M3 8h18"/><path d="M5 8v8a4 4 0 0 0 4 4h6a4 4 0 0 0 4-4V8"/><circle cx="9" cy="14" r="1"/><circle cx="15" cy="16" r="1"/><circle cx="12" cy="11" r="1"/></svg>'},
  {key: 'quantum',      label: '量子 / 物理',   svg: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="4" ry="10"/></svg>'},
  {key: 'blockchain',   label: '区块链 / 加密', svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>'},
  {key: 'ev',           label: '电动 / 汽车',   svg: '<svg viewBox="0 0 24 24"><path d="M14 16H9m10 0h3v-3.15a1 1 0 0 0-.84-.99L16 11l-2.7-3.6a1 1 0 0 0-.8-.4H5.24a2 2 0 0 0-1.8 1.1l-.8 1.63A6 6 0 0 0 2 12.42V16h2"/><circle cx="6.5" cy="16.5" r="2.5"/><circle cx="16.5" cy="16.5" r="2.5"/></svg>'},
  {key: 'game',         label: '游戏 / 娱乐',   svg: '<svg viewBox="0 0 24 24"><line x1="6" y1="11" x2="10" y2="11"/><line x1="8" y1="9" x2="8" y2="13"/><line x1="15" y1="12" x2="15.01" y2="12"/><line x1="18" y1="10" x2="18.01" y2="10"/><path d="M17.32 5H6.68a4 4 0 0 0-3.978 3.59c-.006.052-.01.101-.017.152C2.604 9.416 2 14.456 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.414-1.414A2 2 0 0 1 9.828 16h4.344a2 2 0 0 1 1.414.586L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.545-.604-6.584-.685-7.258"/></svg>'},
  {key: 'music',        label: '音乐 / 文娱',   svg: '<svg viewBox="0 0 24 24"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>'},
  {key: 'default',      label: '其他',          svg: '<svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h7"/></svg>'},
];

function openAddDomainModal() {
  // 静态模式：跳到 GitHub Issue（让用户提交"想加什么领域"，Agent 下次跑前 ingest）
  if (!isServerMode()) {
    openAddDomainViaIssue();
    return;
  }

  let modal = $('.modal-overlay');
  if (!modal) {
    modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
      <div class="modal">
        <h3>添加新领域</h3>
        <p>填一个你想长期关注的领域。Curio 会替你从全网找有价值的内容。</p>
        <div class="form-row">
          <label>领域名（中文）</label>
          <input type="text" id="d-name" placeholder="例：生物科技 / 量子计算 / 摄影 / 中医" autofocus>
        </div>
        <div class="form-row">
          <label>领域 ID（自动生成，可改）</label>
          <input type="text" id="d-id" placeholder="biotech">
        </div>
        <div class="form-row">
          <label>图标</label>
          <div class="icon-row" id="d-icons">
            ${ICONS.map((i, idx) => `<div class="icon-pick ${idx===0?'active':''}" data-icon="${i}">${i}</div>`).join('')}
          </div>
        </div>
        <div class="form-row">
          <label>推送频率</label>
          <select id="d-freq">
            <option value="weekly">每周一次（深度内容）</option>
            <option value="daily">每天一次（突发新闻类）</option>
          </select>
        </div>
        <div class="modal-actions">
          <button class="btn-secondary" id="d-cancel">取消</button>
          <button class="btn-primary" id="d-save">添加</button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    // 自动 slug
    const $name = $('#d-name', modal), $id = $('#d-id', modal);
    $name.addEventListener('input', () => {
      const v = $name.value.trim();
      $id.value = v.toLowerCase().replace(/[^\w\u4e00-\u9fa5]+/g, '-').replace(/-+/g,'-').replace(/^-|-$/g,'');
    });

    // icon picker
    $$('#d-icons .icon-pick', modal).forEach(p => {
      p.addEventListener('click', () => {
        $$('#d-icons .icon-pick', modal).forEach(x => x.classList.remove('active'));
        p.classList.add('active');
      });
    });

    // 关闭
    $('#d-cancel', modal).addEventListener('click', () => modal.classList.remove('show'));
    modal.addEventListener('click', e => { if (e.target === modal) modal.classList.remove('show'); });

    // 保存
    $('#d-save', modal).addEventListener('click', async () => {
      const name = $('#d-name', modal).value.trim();
      const id = $('#d-id', modal).value.trim();
      const icon = $('#d-icons .icon-pick.active', modal)?.dataset.icon || '📰';
      const freq = $('#d-freq', modal).value;
      if (!name) { toast('请填领域名', true); return; }

      const btn = $('#d-save', modal);
      btn.disabled = true; btn.textContent = '创建中...';
      try {
        const r = await api('/api/domains', {
          method: 'POST',
          body: JSON.stringify({name, id, icon, frequency: freq}),
        });
        toast('✅ 已添加 ' + icon + ' ' + name);
        modal.classList.remove('show');
        // 刷新页面以显示新领域
        setTimeout(() => location.reload(), 800);
      } catch (e) {
        toast('❌ ' + e.message, true);
        btn.disabled = false; btn.textContent = '添加';
      }
    });
  }
  modal.classList.add('show');
  setTimeout(() => $('#d-name', modal)?.focus(), 50);
}

// 静态模式：通过 GitHub Issue 申请加领域
function openAddDomainViaIssue() {
  let modal = $('.modal-overlay.add-issue');
  if (!modal) {
    modal = document.createElement('div');
    modal.className = 'modal-overlay add-issue';
    modal.innerHTML = `
      <div class="modal">
        <h3>申请新增领域</h3>
        <p>填好后会跳到 GitHub 提交一条 Issue，Agent 下次跑前会自动读取并加入新领域。</p>
        <div class="form-row">
          <label>领域名（中文）</label>
          <input type="text" id="ai-name" placeholder="例：生物科技 / 量子计算 / 摄影" autofocus>
        </div>
        <div class="form-row">
          <label>领域类型</label>
          <div class="type-grid" id="ai-types">
            ${DOMAIN_TYPES.map((t, idx) => `<div class="type-pick ${idx===0?'active':''}" data-key="${t.key}" title="${t.label}"><span class="ico">${t.svg}</span><span class="lbl">${t.label}</span></div>`).join('')}
          </div>
        </div>
        <div class="form-row">
          <label>推送频率</label>
          <select id="ai-freq">
            <option value="weekly">每周一次（深度内容）</option>
            <option value="daily">每天一次（突发新闻）</option>
          </select>
        </div>
        <div class="form-row">
          <label>关键词 / 信源建议（可选，1-3 行）</label>
          <textarea id="ai-keywords" placeholder="例：CRISPR、合成生物学、Nature Biotech RSS"
            style="width:100%;min-height:60px;background:var(--bg-elev);border:1px solid var(--line);color:var(--text);padding:8px;border-radius:4px;font-family:var(--sans);font-size:13px"></textarea>
        </div>
        <div class="modal-actions">
          <button class="btn-secondary" id="ai-cancel">取消</button>
          <button class="btn-primary" id="ai-go">跳转 GitHub 提交</button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);
    $$('#ai-types .type-pick', modal).forEach(p => {
      p.addEventListener('click', () => {
        $$('#ai-types .type-pick', modal).forEach(x => x.classList.remove('active'));
        p.classList.add('active');
      });
    });
    $('#ai-cancel', modal).addEventListener('click', () => modal.classList.remove('show'));
    modal.addEventListener('click', e => { if (e.target === modal) modal.classList.remove('show'); });
    $('#ai-go', modal).addEventListener('click', () => {
      const name = $('#ai-name', modal).value.trim();
      if (!name) { toast('请填领域名', true); return; }
      const typeKey = $('#ai-types .type-pick.active', modal)?.dataset.key || 'default';
      const freq = $('#ai-freq', modal).value;
      const kw = $('#ai-keywords', modal).value.trim();
      const lines = [
        '<!-- Curio 加领域申请 · 自动生成 -->',
        '```yaml',
        'type: add-domain',
        'name: ' + JSON.stringify(name),
        'icon_type: ' + typeKey,
        'frequency: ' + freq,
      ];
      if (kw) {
        lines.push('keywords_or_sources: |');
        kw.split('\n').forEach(line => lines.push('  ' + line));
      }
      lines.push('```');
      lines.push('');
      lines.push('Agent 下次跑前会读取这条 Issue 并自动加入 sources.yaml，然后关闭。');
      const title = encodeURIComponent('[curio-add-domain] ' + name);
      const body = encodeURIComponent(lines.join('\n'));
      const url = 'https://github.com/' + GH_REPO + '/issues/new?labels=curio-add-domain&title=' + title + '&body=' + body;
      window.open(url, '_blank');
      modal.classList.remove('show');
      toast('✅ 已打开 GitHub 提交页');
    });
  }
  modal.classList.add('show');
  setTimeout(() => $('#ai-name', modal)?.focus(), 50);
}

// 静态模式：通过 GitHub Issue 触发立刻生成
function openGenerateViaIssue(domainId, domainName) {
  // 简单 cooldown 检查（localStorage，软限）
  const key = 'curio:gen:' + domainId;
  const last = parseInt(localStorage.getItem(key) || '0', 10);
  const now = Date.now();
  const cooldownMs = 6 * 60 * 60 * 1000; // 6 小时
  if (now - last < cooldownMs) {
    const remain = Math.ceil((cooldownMs - (now - last)) / 1000 / 60);
    if (!confirm(`你刚才已经触发过「${domainName}」的生成，建议等 ${remain} 分钟再试。\n\n仍要继续吗？`)) return;
  }

  let modal = $('.modal-overlay.gen-issue');
  if (modal) modal.remove();
  modal = document.createElement('div');
  modal.className = 'modal-overlay gen-issue';
  modal.innerHTML = `
    <div class="modal" style="max-width:480px">
      <h3>⚡ 立刻生成「${domainName}」</h3>
      <p>提交后会在 GitHub 上自动开一个 Issue，Curio Agent 每小时检查一次，看到后会立刻为你重跑（抓取 → 打分 → 中文摘要 → 主编点评 → 邮件通知）。</p>
      <p style="background:var(--bg-elev);padding:10px 12px;border-left:3px solid var(--accent);font-size:13px;color:var(--text-soft);margin:12px 0;">
        ⏱️ <strong>预计等待：最长 60 分钟</strong>（Agent 调度间隔 1 小时）<br>
        📨 留下邮箱跑完会发一封通知<br>
        📋 你可以在 GitHub Issue 里实时看 Agent 运行状态
      </p>
      <div class="form-row">
        <label>邮箱（可选，跑完了通知你）</label>
        <input type="email" id="gen-email" placeholder="you@example.com" autocomplete="email">
      </div>
      <div class="form-row">
        <label>留言（可选，告诉 Agent 你想看什么）</label>
        <textarea id="gen-note" placeholder="例：本期想多看一些 AI 硬件的"
          style="width:100%;min-height:60px;background:var(--bg-elev);border:1px solid var(--line);color:var(--text);padding:8px;border-radius:4px;font-family:var(--sans);font-size:13px"></textarea>
      </div>
      <p style="font-size:12px;color:var(--text-mute)">注：Agent 跑生成有冷却限制（同一领域 6 小时内一次），高峰期会排队。</p>
      <div class="modal-actions">
        <button class="btn-secondary" id="gen-cancel">取消</button>
        <button class="btn-primary" id="gen-go">提交并跳转 GitHub</button>
      </div>
    </div>
  `;
  document.body.appendChild(modal);
  $('#gen-cancel', modal).addEventListener('click', () => modal.classList.remove('show'));
  modal.addEventListener('click', e => { if (e.target === modal) modal.classList.remove('show'); });
  $('#gen-go', modal).addEventListener('click', () => {
    const email = $('#gen-email', modal).value.trim();
    const note = $('#gen-note', modal).value.trim();
    const lines = [
      '<!-- Curio 生成请求 · 自动生成 -->',
      '```yaml',
      'type: generate',
      'domain_id: ' + domainId,
      'domain_name: ' + JSON.stringify(domainName),
      'requested_at: ' + new Date().toISOString(),
    ];
    if (email) lines.push('notify_email: ' + JSON.stringify(email));
    if (note) lines.push('note: ' + JSON.stringify(note));
    lines.push('```');
    lines.push('');
    lines.push('Agent 看到后会立刻重跑这个领域。完成后会评论本 Issue 并关闭。');
    const title = encodeURIComponent('[curio-generate] ' + domainName);
    const body = encodeURIComponent(lines.join('\n'));
    const url = 'https://github.com/' + GH_REPO + '/issues/new?labels=curio-generate&title=' + title + '&body=' + body;
    window.open(url, '_blank');
    localStorage.setItem(key, String(now));
    modal.classList.remove('show');
    toast('✅ 已打开 GitHub 提交页，Agent 会在下次触发时拉到');
  });
  modal.classList.add('show');
}

// 订阅 modal：邮箱 + 选域 + 选日报/周刊
async function openSubscribeModal() {
  let modal = $('.modal-overlay.subscribe');
  if (!modal) {
    modal = document.createElement('div');
    modal.className = 'modal-overlay subscribe';
    modal.innerHTML = `
      <div class="modal" style="max-width:520px">
        <h3>📨 订阅 Curio 简报</h3>
        <p>留下邮箱，Curio 会按你的偏好把每期内容发到邮箱。我们不会把邮箱用于其他用途。</p>
        <div class="form-row">
          <label>邮箱</label>
          <input type="email" id="sub-email" placeholder="you@example.com" autocomplete="email" autofocus>
        </div>
        <div class="form-row">
          <label>关注哪些领域（多选）</label>
          <div class="sub-domain-grid" id="sub-domains"><div class="sub-domain-pick">加载中...</div></div>
        </div>
        <div class="form-row">
          <label>推送频率</label>
          <div class="sub-cadence-row">
            <div class="sub-cadence-pick active" data-cadence="weekly">
              <div class="label">📅 周刊</div>
              <div class="meta">每周一早 8:00</div>
            </div>
            <div class="sub-cadence-pick" data-cadence="daily">
              <div class="label">☀️ 日报</div>
              <div class="meta">每天早 8:00</div>
            </div>
          </div>
        </div>
        <div class="modal-actions">
          <button class="btn-secondary" id="sub-cancel">取消</button>
          <button class="btn-primary" id="sub-go">订阅</button>
        </div>
        <div id="sub-status" style="margin-top:12px;font-family:var(--sans);font-size:13px;color:var(--text-soft);min-height:20px"></div>
      </div>
    `;
    document.body.appendChild(modal);

    // 加载领域列表（先用本地 nav 派生，再异步从 worker 拉以保证最新）
    const grid = $('#sub-domains', modal);
    const localDomains = [];
    $$('.nav-links a').forEach(a => {
      const text = a.textContent.trim();
      const href = a.getAttribute('href') || '';
      const m = href.match(/d\/([^/]+)\//);
      if (m) {
        const parts = text.split(' ');
        localDomains.push({id: m[1], icon: parts[0] || '📰', name: parts.slice(1).join(' ') || m[1]});
      }
    });
    const renderDomains = (list) => {
      if (!list.length) { grid.innerHTML = '<div class="sub-domain-pick">暂无领域</div>'; return; }
      grid.innerHTML = list.map(d => `
        <div class="sub-domain-pick" data-id="${d.id}">
          <span class="icon">${d.icon || '📰'}</span><span>${d.name}</span>
        </div>`).join('');
      $$('.sub-domain-pick', grid).forEach(p => {
        p.addEventListener('click', () => p.classList.toggle('active'));
      });
    };
    renderDomains(localDomains);
    if (WORKER_API) {
      workerApi('/domains').then(d => {
        if (Array.isArray(d.domains) && d.domains.length && d.meta) {
          const list = d.domains.map(id => ({id, icon: d.meta[id]?.icon || '📰', name: d.meta[id]?.name || id}));
          renderDomains(list);
        }
      }).catch(() => {});
    }

    // cadence
    $$('.sub-cadence-pick', modal).forEach(p => {
      p.addEventListener('click', () => {
        $$('.sub-cadence-pick', modal).forEach(x => x.classList.remove('active'));
        p.classList.add('active');
      });
    });

    $('#sub-cancel', modal).addEventListener('click', () => modal.classList.remove('show'));
    modal.addEventListener('click', e => { if (e.target === modal) modal.classList.remove('show'); });

    $('#sub-go', modal).addEventListener('click', async () => {
      const email = $('#sub-email', modal).value.trim();
      if (!email || !/.+@.+\..+/.test(email)) { toast('邮箱格式不对', true); return; }
      const picked = $$('.sub-domain-pick.active', grid).map(p => p.dataset.id);
      if (!picked.length) { toast('至少选一个领域', true); return; }
      const cadence = $('.sub-cadence-pick.active', modal)?.dataset.cadence || 'weekly';

      const status = $('#sub-status', modal);
      const btn = $('#sub-go', modal);
      btn.disabled = true; btn.textContent = '提交中...';
      status.textContent = '';
      try {
        if (!WORKER_API) throw new Error('Worker API 未配置');
        const r = await workerApi('/subscribe', {
          method: 'POST',
          body: JSON.stringify({email, domains: picked, cadence}),
        });
        status.style.color = '#5cb85c';
        status.textContent = '✅ ' + (r.message || '已发送确认邮件，请查收');
        toast('✅ 已发送确认邮件，请查收');
        setTimeout(() => modal.classList.remove('show'), 2400);
      } catch (e) {
        status.style.color = '#d9534f';
        status.textContent = '❌ ' + e.message;
        // worker 不可达时给个 GitHub Issue 兜底
        if (/HTTP|fetch|Worker/i.test(e.message)) {
          status.innerHTML += ' <a href="#" id="sub-fallback" style="color:var(--accent)">改用 GitHub 提交</a>';
          $('#sub-fallback', modal)?.addEventListener('click', ev => {
            ev.preventDefault();
            const lines = [
              '<!-- Curio 订阅请求 · 自动生成 -->',
              '```yaml',
              'type: subscribe',
              'email: ' + JSON.stringify(email),
              'domains: ' + JSON.stringify(picked),
              'cadence: ' + cadence,
              '```',
            ];
            const url = 'https://github.com/' + GH_REPO + '/issues/new?labels=curio-subscribe&title=' +
              encodeURIComponent('[curio-subscribe] ' + email) + '&body=' + encodeURIComponent(lines.join('\n'));
            window.open(url, '_blank');
          });
        }
      } finally {
        btn.disabled = false; btn.textContent = '订阅';
      }
    });
  }
  modal.classList.add('show');
  setTimeout(() => $('#sub-email', modal)?.focus(), 50);
}

async function deleteDomain(domainId, domainName) {
  if (!confirm(`确定要删除领域「${domainName}」吗？\n\n· 不会再生成新简报\n· 历史期数保留可访问\n· 订阅者会自动从该领域退订\n\n你将被引导到 GitHub 提交一个删除请求 Issue。Agent 在下次触发时（最长 60 分钟内）执行。`)) return;

  // 静态站走 GitHub Issue 链路（和加领域/立即生成对齐）
  const lines = [];
  lines.push('<!-- Curio 删除领域请求 · 自动生成 -->');
  lines.push('');
  lines.push('type: delete-domain');
  lines.push('domain_id: ' + domainId);
  lines.push('domain_name: ' + domainName);
  lines.push('requested_at: ' + new Date().toISOString());
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('确认删除：');
  lines.push('- [ ] 我确认不再需要该领域的简报');
  lines.push('');
  lines.push('Agent 看到后会：');
  lines.push('1. 从 sources.yaml 移除该领域配置');
  lines.push('2. 把所有订阅者从该领域中退订（其他领域订阅保留）');
  lines.push('3. 历史 markdown 不删，仍可通过直接 URL 访问');
  lines.push('4. 完成后评论本 Issue 并关闭');

  const title = encodeURIComponent('[curio-delete-domain] ' + domainName);
  const body = encodeURIComponent(lines.join('\n'));
  const url = 'https://github.com/' + GH_REPO + '/issues/new?labels=curio-delete-domain&title=' + title + '&body=' + body;
  window.open(url, '_blank');
  toast('✅ 已打开 GitHub 删除申请页', false);
}

// ===== 一键生成 =====
function ensureProgressBar() {
  let bar = $('.gen-progress');
  if (!bar) {
    bar = document.createElement('div');
    bar.className = 'gen-progress';
    bar.innerHTML = `
      <div class="gen-status">
        <span class="domain-label"></span>
        <span class="step-msg">准备中...</span>
        <span class="pct">0%</span>
      </div>
      <div class="gen-progress-bar"><div class="gen-progress-fill"></div></div>
    `;
    document.body.appendChild(bar);
  }
  return bar;
}

async function generateIssue(domainId, domainName) {
  // 静态模式：跳 GitHub Issue 让 automation 拉到立刻生成
  if (!isServerMode()) {
    openGenerateViaIssue(domainId, domainName);
    return;
  }
  const btn = document.querySelector(`.gen-btn[data-domain-id="${domainId}"]`);
  if (btn) { btn.disabled = true; btn.textContent = '生成中...'; }

  const bar = ensureProgressBar();
  bar.classList.add('show');
  $('.domain-label', bar).textContent = `🛰️ ${domainName}`;
  $('.step-msg', bar).textContent = '启动中...';
  $('.pct', bar).textContent = '0%';
  $('.gen-progress-fill', bar).style.width = '0%';

  try {
    await api('/api/generate/' + encodeURIComponent(domainId), {method: 'POST'});
  } catch (e) {
    if (!String(e.message).includes('已在生成中')) {
      toast('❌ ' + e.message, true);
      bar.classList.remove('show');
      if (btn) { btn.disabled = false; btn.textContent = '一键生成'; }
      return;
    }
  }

  // 轮询状态
  const poll = async () => {
    try {
      const r = await api('/api/generate/' + encodeURIComponent(domainId) + '/status');
      const job = r.job;
      if (!job) return;
      $('.step-msg', bar).textContent = job.log && job.log.length
        ? job.log[job.log.length - 1].msg
        : job.step;
      $('.pct', bar).textContent = (job.progress || 0) + '%';
      $('.gen-progress-fill', bar).style.width = (job.progress || 0) + '%';

      if (job.status === 'done') {
        $('.step-msg', bar).textContent = '✨ 完成！正在跳转...';
        toast('✅ 已生成 ' + domainName + ' 周刊');
        // issue_url 是绝对路径 /d/<id>/<date>.html，转成相对 origin
        const target = (job.issue_url || '/').replace(/^\/+/, '/');
        setTimeout(() => {
          window.location.assign(target);
        }, 1200);
        return;
      }
      if (job.status === 'error') {
        $('.step-msg', bar).textContent = '❌ ' + (job.error || '失败');
        toast('生成失败：' + job.error, true);
        if (btn) { btn.disabled = false; btn.textContent = '一键生成'; }
        setTimeout(() => bar.classList.remove('show'), 4000);
        return;
      }
      setTimeout(poll, 1500);
    } catch (e) {
      console.error(e);
      setTimeout(poll, 2000);
    }
  };
  setTimeout(poll, 800);
}

// ===== 反馈区 =====
function initFeedback() {
  const fb = $('.feedback');
  if (!fb) return;
  const issueId = fb.dataset.issueId;
  if (!issueId) return;

  // 评分按钮
  $$('.fb-btn', fb).forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.fb-item');
      $$('.fb-btn', item).forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  // 加载已有反馈
  if (isServerMode()) {
    api('/api/feedback/' + encodeURIComponent(issueId)).then(r => {
      if (!r.feedback) return;
      const data = r.feedback;
      (data.items || []).forEach(it => {
        const item = $$('.fb-item', fb).find(el => el.dataset.idx == it.idx);
        if (!item) return;
        const btn = $(`.fb-btn[data-rating="${it.rating}"]`, item);
        if (btn) btn.classList.add('active');
        const note = $('.fb-note', item);
        if (note && it.note) note.value = it.note;
      });
      if (data.long_term) {
        ['more','less','format'].forEach(k => {
          const el = $(`#lt-${k}`);
          if (el && data.long_term[k]) el.value = data.long_term[k];
        });
      }
      $('.fb-status', fb).textContent = '已加载上次反馈（提交可覆盖）';
    }).catch(() => {});
  }

  // 提交（双模式：本地 server 走 API，公网静态站点走 GitHub Issue 跳转）
  const submitBtn = $('.fb-submit-btn', fb);
  if (!submitBtn) return;
  submitBtn.addEventListener('click', async () => {
    const items = $$('.fb-item', fb).map(item => {
      const active = $('.fb-btn.active', item);
      return {
        idx: parseInt(item.dataset.idx),
        title: item.dataset.title || '',
        rating: active ? active.dataset.rating : null,
        note: $('.fb-note', item)?.value.trim() || '',
      };
    }).filter(it => it.rating || it.note);

    const long_term = {
      more: $('#lt-more')?.value.trim() || '',
      less: $('#lt-less')?.value.trim() || '',
      format: $('#lt-format')?.value.trim() || '',
    };

    if (items.length === 0 && !long_term.more && !long_term.less && !long_term.format) {
      toast('反馈是空的，至少给一条评分或填长期偏好', true);
      return;
    }

    submitBtn.disabled = true;
    const status = $('.fb-status', fb);
    status.className = 'fb-status';

    if (isServerMode()) {
      // 本地 server 模式：走 API
      status.textContent = '提交中...';
      try {
        await api('/api/feedback', {
          method: 'POST',
          body: JSON.stringify({issue_id: issueId, items, long_term}),
        });
        status.className = 'fb-status success';
        status.textContent = '✅ 已保存。下次跑前 Agent 会读这段。';
        toast('反馈已保存');
      } catch (e) {
        status.className = 'fb-status error';
        status.textContent = '❌ ' + e.message;
      } finally {
        submitBtn.disabled = false;
      }
    } else {
      // 静态站点模式：拼 GitHub Issue 跳转链接
      const REPO = 'zczxd1118/curio-app';
      const lines = [];
      lines.push('<!-- Curio 反馈 · 自动生成 · 不要修改这一行 -->');
      lines.push('```yaml');
      lines.push('issue_id: ' + issueId);
      lines.push('submitted_at: ' + new Date().toISOString());
      lines.push('items:');
      items.forEach(it => {
        lines.push('  - idx: ' + it.idx);
        lines.push('    title: ' + JSON.stringify(it.title));
        if (it.rating) lines.push('    rating: ' + it.rating);
        if (it.note) lines.push('    note: ' + JSON.stringify(it.note));
      });
      lines.push('long_term:');
      ['more','less','format'].forEach(k => {
        if (long_term[k]) lines.push('  ' + k + ': ' + JSON.stringify(long_term[k]));
      });
      lines.push('```');
      lines.push('');
      lines.push('---');
      lines.push('');
      lines.push('提交后 Agent 会在下次跑生成时读取这条反馈，并自动 close 本 Issue。');
      const body = encodeURIComponent(lines.join('\n'));
      const title = encodeURIComponent('[curio-feedback] ' + issueId);
      const url = 'https://github.com/' + REPO + '/issues/new?labels=curio-feedback&title=' + title + '&body=' + body;
      window.open(url, '_blank');
      status.className = 'fb-status success';
      status.textContent = '✅ 已打开 GitHub 提交页，登录后点 "Submit new issue" 即可。';
      submitBtn.disabled = false;
    }
  });
}

// ===== B 阶段 增强：主题切换 / 搜索 / 目录 =====

// 主题切换（深/浅色），localStorage 持久化
function initTheme() {
  const saved = localStorage.getItem('curio-theme');
  const sysLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;
  const theme = saved || (sysLight ? 'light' : 'dark');
  document.documentElement.setAttribute('data-theme', theme);
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;
  btn.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
    const next = cur === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('curio-theme', next);
  });
}

// 文章页右侧目录（TOC）
function initTOC() {
  const tocEl = document.getElementById('curio-toc');
  const listEl = document.getElementById('curio-toc-list');
  if (!tocEl || !listEl) return;
  const main = document.querySelector('main');
  if (!main) return;
  const heads = $$('h2, h3', main).filter(h => h.closest('.feedback') === null);
  if (heads.length < 2) return;   // 太少不展示
  let html = '';
  heads.forEach((h, i) => {
    if (!h.id) h.id = 'toc-' + i;
    const text = (h.textContent || '').trim();
    const lvl = h.tagName === 'H3' ? 'lvl-3' : 'lvl-2';
    html += `<a href="#${h.id}" class="${lvl}" data-toc-target="${h.id}">${text}</a>`;
  });
  listEl.innerHTML = html;
  tocEl.classList.add('has-items');

  // 滚动同步高亮
  const tocLinks = $$('a', listEl);
  const onScroll = () => {
    let active = null;
    for (const h of heads) {
      if (h.getBoundingClientRect().top < 120) active = h.id;
      else break;
    }
    tocLinks.forEach(a => a.classList.toggle('active', a.dataset.tocTarget === active));
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// 客户端搜索：把所有期刊 must_read 标题做成索引
let __SEARCH_INDEX = null;
async function loadSearchIndex() {
  if (__SEARCH_INDEX) return __SEARCH_INDEX;
  try {
    const root = window.CURIO_REL_ROOT || '';
    const r = await fetch(root + 'search-index.json');
    if (!r.ok) throw new Error();
    __SEARCH_INDEX = await r.json();
  } catch (e) {
    __SEARCH_INDEX = [];
  }
  return __SEARCH_INDEX;
}

function highlight(text, q) {
  if (!q) return text;
  const re = new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
  return text.replace(re, '<mark>$1</mark>');
}

function searchItems(q, items) {
  if (!q) return [];
  const ql = q.toLowerCase();
  const scored = [];
  for (const it of items) {
    const hay = (it.title + ' ' + (it.why || '') + ' ' + (it.domain || '')).toLowerCase();
    const idx = hay.indexOf(ql);
    if (idx >= 0) scored.push({ ...it, _score: -idx });
  }
  scored.sort((a, b) => b._score - a._score);
  return scored.slice(0, 12);
}

function initSearch() {
  const input = document.getElementById('curio-search');
  const box = document.getElementById('curio-search-results');
  if (!input || !box) return;

  const root = window.CURIO_REL_ROOT || '';
  let timer = null;

  const render = (results, q) => {
    if (!results.length) {
      box.innerHTML = '<div class="empty">没找到 "' + q + '" 相关内容</div>';
      box.classList.add('show');
      return;
    }
    box.innerHTML = results.map(r => {
      const url = r.url || (r.issue_path ? root + r.issue_path : '#');
      const title = highlight(r.title, q);
      const why = r.why ? highlight(r.why.slice(0, 80), q) : '';
      const domain = r.domain ? `<span class="domain-tag">${r.domain_icon || ''} ${r.domain}</span>` : '';
      const platform = r.platform ? `<span>${r.platform}</span>` : '';
      return `<a class="search-result-item" href="${url}"${r.url ? ' target="_blank" rel="noopener"' : ''}>
        <div class="sr-title">${title}</div>
        <div class="sr-meta">${domain}${platform}${why ? '<span>' + why + '</span>' : ''}</div>
      </a>`;
    }).join('');
    box.classList.add('show');
  };

  input.addEventListener('input', () => {
    clearTimeout(timer);
    const q = input.value.trim();
    if (!q) { box.classList.remove('show'); return; }
    timer = setTimeout(async () => {
      const idx = await loadSearchIndex();
      render(searchItems(q, idx), q);
    }, 120);
  });

  input.addEventListener('focus', () => {
    if (input.value.trim()) box.classList.add('show');
  });

  document.addEventListener('click', e => {
    if (!e.target.closest('.search-wrap')) box.classList.remove('show');
  });

  // ⌘K / Ctrl+K 聚焦
  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      input.focus();
      input.select();
    } else if (e.key === 'Escape') {
      box.classList.remove('show');
      input.blur();
    }
  });
}

// ===== 启动 =====
document.addEventListener('DOMContentLoaded', () => {
  // B 阶段：主题/搜索/目录
  initTheme();
  initTOC();
  initSearch();

  // 添加领域按钮（点击）
  const addBtn = $('.add-domain');
  if (addBtn) addBtn.addEventListener('click', openAddDomainModal);

  // 订阅按钮
  const subBtn = $('#subscribe-btn');
  if (subBtn) subBtn.addEventListener('click', openSubscribeModal);

  // 删除领域按钮
  $$('.del-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      e.preventDefault(); e.stopPropagation();
      deleteDomain(btn.dataset.domainId, btn.dataset.domainName);
    });
  });

  // 一键生成按钮
  $$('.gen-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      e.preventDefault(); e.stopPropagation();
      generateIssue(btn.dataset.domainId, btn.dataset.domainName);
    });
  });

  // 默认假设无后端（公网 GitHub Pages 永远走这条路径）
  window.__CURIO_HAS_BACKEND = false;
  applyStaticMode();
  initFeedback();

  // 异步探测后端（仅本地开发时会成功）
  fetch('/api/health').then(r => {
    if (!r.ok) throw new Error('no api');
    return r.json().catch(() => ({}));
  }).then(() => {
    // 真有后端：切到 server 模式，重置 UI
    window.__CURIO_HAS_BACKEND = true;
    applyServerMode();
  }).catch(() => {
    // 保持静态模式（已默认应用，无需再操作）
  });
});

// 静态模式：删除按钮 + ⚡生成按钮 + 加领域按钮 都走 GitHub Issue 链路
function applyStaticMode() {
  $$('.del-btn').forEach(b => {
    b.dataset.staticMode = '1';
    b.title = '通过 GitHub Issue 删除该领域';
  });
  $$('.gen-btn').forEach(b => {
    b.dataset.staticMode = '1';
    b.textContent = '⚡ 立刻生成';
    b.title = '点击通过 GitHub Issue 触发立刻生成（用户公开自助）';
  });
  const addBtn = $('.add-domain');
  if (addBtn) {
    addBtn.title = '点击通过 GitHub Issue 申请新增领域';
  }
  $$('.feedback').forEach(fb => {
    const submit = $('.fb-submit-btn', fb);
    if (submit) submit.textContent = '提交反馈到 GitHub';
    const desc = $('.desc', fb);
    if (desc) desc.textContent = '点击下方按钮，会跳转到 GitHub 预填好的 Issue 页面，登录确认即可。Agent 下次跑前会自动读取并关闭。';
  });
}

// 本地 server 模式：恢复按钮可见，反馈区走 API
function applyServerMode() {
  $$('.gen-btn, .del-btn').forEach(b => b.style.display = '');
  const addBtn = $('.add-domain');
  if (addBtn) {
    addBtn.style.opacity = '';
    addBtn.style.cursor = '';
    addBtn.title = '';
  }
  $$('.feedback').forEach(fb => {
    const submit = $('.fb-submit-btn', fb);
    if (submit) submit.textContent = '提交反馈';
  });
}
"""


# ============================================================================
# 渲染器
# ============================================================================
def _slug_for_path(s: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^\w\u4e00-\u9fa5]+", "-", s.strip().lower())).strip("-")


# Lucide SVG 图标库（替代 emoji，单色 + 跨平台一致）
_SVG_ICONS = {
    "ai":           '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="2" x2="9" y2="4"/><line x1="15" y1="2" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="22"/><line x1="15" y1="20" x2="15" y2="22"/><line x1="20" y1="9" x2="22" y2="9"/><line x1="20" y1="15" x2="22" y2="15"/><line x1="2" y1="9" x2="4" y2="9"/><line x1="2" y1="15" x2="4" y2="15"/></svg>',
    "robot":        '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="2" x2="9" y2="4"/><line x1="15" y1="2" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="22"/><line x1="15" y1="20" x2="15" y2="22"/><line x1="20" y1="9" x2="22" y2="9"/><line x1="20" y1="15" x2="22" y2="15"/><line x1="2" y1="9" x2="4" y2="9"/><line x1="2" y1="15" x2="4" y2="15"/></svg>',
    "finance":      '<svg viewBox="0 0 24 24"><polyline points="3 17 9 11 13 15 21 7"/><polyline points="14 7 21 7 21 14"/></svg>',
    "bank":         '<svg viewBox="0 0 24 24"><path d="M3 21h18"/><path d="M3 10h18"/><path d="M5 6l7-3 7 3"/><line x1="4" y1="10" x2="4" y2="21"/><line x1="20" y1="10" x2="20" y2="21"/><line x1="8" y1="14" x2="8" y2="17"/><line x1="12" y1="14" x2="12" y2="17"/><line x1="16" y1="14" x2="16" y2="17"/></svg>',
    "semiconductor":'<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="1"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>',
    "chip":         '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="1"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/></svg>',
    "bigtech":      '<svg viewBox="0 0 24 24"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v8h4"/><path d="M18 9h2a2 2 0 0 1 2 2v11h-4"/><line x1="10" y1="6" x2="14" y2="6"/><line x1="10" y1="10" x2="14" y2="10"/><line x1="10" y1="14" x2="14" y2="14"/><line x1="10" y1="18" x2="14" y2="18"/></svg>',
    "building":     '<svg viewBox="0 0 24 24"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v8h4"/><path d="M18 9h2a2 2 0 0 1 2 2v11h-4"/><line x1="10" y1="6" x2="14" y2="6"/><line x1="10" y1="10" x2="14" y2="10"/><line x1="10" y1="14" x2="14" y2="14"/></svg>',
    "biotech":      '<svg viewBox="0 0 24 24"><path d="M9 2v6"/><path d="M15 2v6"/><path d="M3 8h18"/><path d="M5 8v8a4 4 0 0 0 4 4h6a4 4 0 0 0 4-4V8"/><circle cx="9" cy="14" r="1"/><circle cx="15" cy="16" r="1"/><circle cx="12" cy="11" r="1"/></svg>',
    "quantum":      '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="4" ry="10"/></svg>',
    "blockchain":   '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><line x1="10" y1="6.5" x2="14" y2="6.5"/><line x1="10" y1="17.5" x2="14" y2="17.5"/><line x1="6.5" y1="10" x2="6.5" y2="14"/><line x1="17.5" y1="10" x2="17.5" y2="14"/></svg>',
    "music":        '<svg viewBox="0 0 24 24"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>',
    "ev":           '<svg viewBox="0 0 24 24"><path d="M14 16H9m10 0h3v-3.15a1 1 0 0 0-.84-.99L16 11l-2.7-3.6a1 1 0 0 0-.8-.4H5.24a2 2 0 0 0-1.8 1.1l-.8 1.63A6 6 0 0 0 2 12.42V16h2"/><circle cx="6.5" cy="16.5" r="2.5"/><circle cx="16.5" cy="16.5" r="2.5"/></svg>',
    "game":         '<svg viewBox="0 0 24 24"><line x1="6" y1="11" x2="10" y2="11"/><line x1="8" y1="9" x2="8" y2="13"/><line x1="15" y1="12" x2="15.01" y2="12"/><line x1="18" y1="10" x2="18.01" y2="10"/><path d="M17.32 5H6.68a4 4 0 0 0-3.978 3.59c-.006.052-.01.101-.017.152C2.604 9.416 2 14.456 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.414-1.414A2 2 0 0 1 9.828 16h4.344a2 2 0 0 1 1.414.586L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.545-.604-6.584-.685-7.258"/></svg>',
    "auto":         '<svg viewBox="0 0 24 24"><path d="M14 16H9m10 0h3v-3.15a1 1 0 0 0-.84-.99L16 11l-2.7-3.6a1 1 0 0 0-.8-.4H5.24a2 2 0 0 0-1.8 1.1l-.8 1.63A6 6 0 0 0 2 12.42V16h2"/><circle cx="6.5" cy="16.5" r="2.5"/><circle cx="16.5" cy="16.5" r="2.5"/></svg>',
    "default":      '<svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h7"/></svg>',
}

# 旧 emoji → SVG icon key
_EMOJI_TO_ICON = {
    "🤖": "ai", "🧠": "ai",
    "🏦": "finance", "💰": "finance", "📈": "finance",
    "🔬": "semiconductor", "⚛️": "quantum",
    "🏛️": "bigtech", "🏢": "building",
    "🧬": "biotech",
    "🎮": "game",
    "🎨": "default", "📚": "default",
    "🎵": "music", "🎶": "music",
    "🚗": "auto", "⚡": "ev",
    "🌍": "default", "💊": "biotech",
    "📰": "default", "📊": "finance",
    "📉": "finance", "💼": "finance",
}


def _domain_svg(icon_or_id: str, domain_name: str = "", icon_type: str = "") -> str:
    """根据领域 icon (emoji)、icon_type (svg key) 或 id 返回 SVG 图标 HTML"""
    # 最优先：明确指定的 icon_type
    if icon_type and icon_type in _SVG_ICONS:
        return _SVG_ICONS[icon_type]
    if not icon_or_id:
        icon_or_id = ""
    # 优先用 emoji 映射
    key = _EMOJI_TO_ICON.get(icon_or_id)
    if key and key in _SVG_ICONS:
        return _SVG_ICONS[key]
    # 用 domain id 关键词匹配
    lookup = (icon_or_id + " " + domain_name).lower()
    for k in ["ai", "finance", "bank", "semiconductor", "chip", "bigtech", "building",
             "biotech", "quantum", "blockchain", "music", "ev", "auto", "game"]:
        if k in lookup:
            return _SVG_ICONS[k]
    # 中文关键词
    for zh, k in [("金融", "finance"), ("半导体", "semiconductor"), ("芯片", "semiconductor"),
                  ("大厂", "bigtech"), ("互联网", "bigtech"), ("公司", "building"),
                  ("生物", "biotech"), ("量子", "quantum"), ("区块", "blockchain"),
                  ("加密", "blockchain"), ("游戏", "game"), ("音乐", "music"),
                  ("电动", "ev"), ("汽车", "auto"), ("AI", "ai"), ("ai", "ai")]:
        if zh in (icon_or_id + domain_name):
            return _SVG_ICONS[k]
    # fallback：首字母
    first = (domain_name or icon_or_id or "·").strip()[:1].upper()
    return f'<span style="font-family:var(--serif);font-size:18px;font-weight:600">{first}</span>'


def _read_must_titles(domain_id: str, date: str) -> list[dict]:
    """从 scored.json 读必读标题列表，给反馈区用"""
    # 优先用 topic_id 文件名，再用 domain_id
    candidates = [
        TOPICS / f"{domain_id}.scored.json",
        TOPICS / "vibe-coding.scored.json",  # M0 ai 域占位
    ]
    # 也试所有 *.scored.json
    for f in TOPICS.glob("*.scored.json"):
        if f not in candidates:
            candidates.append(f)
    for p in candidates:
        if p.exists():
            try:
                d = json.loads(p.read_text(encoding="utf-8"))
                must = d.get("must_read", []) or []
                return [{"title": m.get("title", ""), "id": m.get("id", "")} for m in must]
            except Exception:
                continue
    return []


def _load_editor_notes_map(domain_id: str) -> dict:
    """读 {slug}.editor_notes.json + {slug}.scored.json，返回 enriched map：
    { id: {note, title_zh, keywords} } 以及 __title:xxx → 同样 dict 反查
    """
    out = {}
    # 1. 先读 editor_notes（主编点评）
    for f in TOPICS.glob("*.editor_notes.json"):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for it in (data.get("notes") or data.get("items") or []):
            iid = it.get("id")
            entry = {"note": it.get("note", "") or "", "title_zh": "", "keywords": []}
            if iid:
                out[iid] = entry
            t = (it.get("title") or "")[:50]
            if t:
                out["__title:" + t.lower()] = entry
    # 2. 再读 scored.json 拿 title_zh + keywords，并合并进 entry
    for f in TOPICS.glob("*.scored.json"):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for tier in ("must_read", "reference"):
            for it in data.get(tier, []) or []:
                iid = it.get("id")
                title_zh = it.get("title_zh") or ""
                keywords = it.get("keywords") or []
                t_en = (it.get("title") or "")[:50]
                # 找已有 entry 或新建
                entry = None
                if iid and iid in out:
                    entry = out[iid]
                elif t_en:
                    key = "__title:" + t_en.lower()
                    if key in out:
                        entry = out[key]
                if entry is None:
                    entry = {"note": "", "title_zh": title_zh, "keywords": keywords}
                    if iid:
                        out[iid] = entry
                    if t_en:
                        out["__title:" + t_en.lower()] = entry
                else:
                    if title_zh and not entry.get("title_zh"):
                        entry["title_zh"] = title_zh
                    if keywords and not entry.get("keywords"):
                        entry["keywords"] = keywords
                    # 关键修复：把 entry 注册到 scored.json 里的长标题 key 下
                    # （editor_notes 里 title 可能是简短版，weekly md 里反查用的是长版）
                    if t_en:
                        out["__title:" + t_en.lower()] = entry
    return out


def _patch_md_with_editor_notes(body_md: str, editor_notes: dict) -> str:
    """把 markdown 里的"📖 中文摘要"段替换成 LLM 写的导读（按标题前缀匹配）

    ⚠️ 新版（build_issue_md 出的 md）已经同时包含 chips、中文摘要、主编点评 —— 这种情况
    不要再做替换，否则会把中文摘要抹掉。检测方法：md 里同时存在 chips 行（🏷️）和"主编点评"。
    """
    if not editor_notes:
        return body_md
    if "🏷️" in body_md and "**📖 主编点评**" in body_md:
        # 已是统一模板出的新版 md，结构完整，跳过 patch
        return body_md

    def replace_block(match):
        # match.group(1) 是 "### N. 标题"
        # match.group(2) 是中间内容（含烂翻译）
        # match.group(3) 是后续内容（"<details>展开英文..." 或 "📺 [打开原文]"）
        header = match.group(1)
        # 提取标题用来反查
        title_match = re.search(r"###\s+\d+\.\s+(.+)", header)
        if not title_match:
            return match.group(0)
        title_text = title_match.group(1).strip()
        # 用标题前 50 字符 lower 反查
        key = "__title:" + title_text[:50].lower()
        note = editor_notes.get(key, "")
        if not note:
            # 没找到导读，保留原 block
            return match.group(0)
        # 替换：保留头 + 用 LLM note + 保留 details/打开原文
        return f"{header}\n\n**📖 主编点评**\n\n{note}\n\n{match.group(3)}"

    # 匹配模式：### N. 标题 ... **📖 中文摘要** ... <details>...</details>  或  📺 [打开原文]
    pattern = re.compile(
        r"(###\s+\d+\.\s+[^\n]+)"          # 标题行
        r".*?\*\*📖 中文摘要\*\*\s*\n\n"     # "中文摘要"前导
        r".*?"                              # 烂翻译内容
        r"(?=<details|📺 \[打开原文\])"      # 直到 <details> 或 打开原文
        r"(.*?)"                            # 不消费的占位
        r"(<details.*?</details>|📺 \[打开原文\][^\n]*)",  # 后续
        re.DOTALL,
    )
    # 切割每条报道（### 1. ... ### 2. ...）
    chunks = re.split(r"(?=^###\s+\d+\.)", body_md, flags=re.MULTILINE)
    out = []
    for chunk in chunks:
        m = re.match(r"^###\s+\d+\.\s+(.+?)\n", chunk)
        if not m:
            out.append(chunk)
            continue
        title_text = m.group(1).strip()
        # 优先用英文原标题反查
        orig_match = re.search(r"_原标题：(.+?)_", chunk)
        candidates = []
        if orig_match:
            orig = orig_match.group(1).strip()
            candidates.append("__title:" + orig[:50].lower())
        candidates.append("__title:" + title_text[:50].lower())

        entry = None
        for k in candidates:
            if k in editor_notes:
                v = editor_notes[k]
                # 兼容老格式（直接 string）和新格式（dict）
                if isinstance(v, dict):
                    entry = v
                else:
                    entry = {"note": v, "title_zh": "", "keywords": []}
                break
        if not entry or not entry.get("note"):
            out.append(chunk)
            continue

        note = entry.get("note", "")
        title_zh = entry.get("title_zh", "")
        keywords = entry.get("keywords") or []

        # 1. 改写第一行的标题（### N. xxx）：如果有 title_zh 就用中文标题
        if title_zh:
            chunk = re.sub(
                r"^(###\s+\d+\.\s+).+?\n",
                lambda mm: f"{mm.group(1)}{title_zh}\n",
                chunk, count=1, flags=re.MULTILINE
            )

        # 2. 把 "**📖 中文摘要**" 段替换成 keywords + 主编点评
        chips = ""
        if keywords:
            kw_html = " · ".join(f"`{k}`" for k in keywords[:5])
            chips = f"\n🏷️ {kw_html}\n\n"

        zh_pattern = re.compile(
            r"\*\*📖 中文摘要\*\*\s*\n\n.*?(?=<details|📺 \[打开原文\])",
            re.DOTALL,
        )
        replacement = f"{chips}**📖 主编点评**\n\n{note}\n\n"
        new_chunk, n = zh_pattern.subn(replacement, chunk, count=1)

        # 如果 weekly md 已经是新版没有"中文摘要"段（直接是"主编点评"），单独把 chips 插到主编点评前
        if n == 0 and "**📖 主编点评**" in new_chunk and chips:
            new_chunk = new_chunk.replace("**📖 主编点评**", chips.strip() + "\n\n**📖 主编点评**", 1)
        elif n == 0:
            new_chunk = chunk

        out.append(new_chunk)
    return "".join(out)


def render_issue(md_path: Path, domain_id: str, domain_name: str, domain_icon: str) -> str:
    md_text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^#\s+(.+?)$", md_text, re.MULTILINE)
    title = m.group(1).strip() if m else domain_name
    m2 = re.search(r"^\*\*(.+?)\*\*$", md_text, re.MULTILINE)
    meta = m2.group(1).strip() if m2 else ""

    body_md = re.sub(r"^#\s+.+?\n", "", md_text, count=1)
    body_md = re.sub(r"^\*\*.+?\*\*\n", "", body_md, count=1)

    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", md_path.name)
    issue_date = date_match.group(1) if date_match else ""
    issue_id = f"{domain_id}/{issue_date}"

    # 用 editor_notes.json 替换烂的 MyMemory 翻译
    editor_notes = _load_editor_notes_map(domain_id)
    if editor_notes:
        body_md = _patch_md_with_editor_notes(body_md, editor_notes)

    # 砍掉 markdown 里的反馈区（要换成可交互版）
    body_md = re.sub(r"## 📝[^\n]*\n.*?(?=^---\s*$|\Z)", "", body_md, flags=re.DOTALL | re.MULTILINE)

    html_body = mdlib.markdown(
        body_md,
        extensions=["tables", "fenced_code", "attr_list", "md_in_html"],
    )

    # 从 scored.json 取必读列表生成反馈区
    must_items = _read_must_titles(domain_id, issue_date)
    fb_items_html = ""
    for i, m_item in enumerate(must_items, 1):
        title_short = (m_item.get("title", "") or "?")[:80]
        fb_items_html += f'''
        <div class="fb-item" data-idx="{i}" data-title="{title_short}">
          <div class="fb-title"><span class="num">{i}.</span> {title_short}</div>
          <div class="fb-buttons">
            <button class="fb-btn" data-rating="useful">👍 有用</button>
            <button class="fb-btn" data-rating="meh">😐 一般</button>
            <button class="fb-btn" data-rating="off">👎 偏了</button>
          </div>
          <textarea class="fb-note" placeholder="备注（可选）：哪里好 / 哪里不对..."></textarea>
        </div>'''

    fb_html = f'''
    <div class="feedback" data-issue-id="{issue_id}">
      <h2>📝 本期反馈</h2>
      <p class="desc">下次 Agent 跑前会读这段，用来调整搜索关键词、打分倾向。</p>

      <div class="fallback-notice" style="display:none">
        反馈需要后端支持。运行 <code>python server.py</code>，然后用 <code>http://localhost:8765/</code> 打开本页。
      </div>

      {fb_items_html}

      <div class="long-term">
        <label>最近更关注</label>
        <input type="text" id="lt-more" placeholder="如：AI Agent 实战 / 半导体先进制程 / 美股期权策略">

        <label>最近不太关注</label>
        <input type="text" id="lt-less" placeholder="如：纯产品更新 / 概念股炒作">

        <label>报道笔法（这是新尝试，重点反馈）</label>
        <input type="text" id="lt-format" placeholder="如：二栏太多 / 时间线很好 / 想看更多引述">
      </div>

      <div class="fb-submit">
        <button class="btn-primary fb-submit-btn">提交反馈</button>
        <span class="fb-status">未提交</span>
      </div>
    </div>'''

    return _page_template(
        page_title=f"{title} · Curio",
        nav_active=domain_id,
        depth=2,
        body=f'''
<div class="hero">
  <div class="kicker">{domain_icon} {domain_name} · {issue_date}</div>
  <h1>{title}</h1>
  <div class="meta">{meta}</div>
</div>
<div class="content">
{html_body}
</div>
{fb_html}
''',
    )


def render_domain_index(domain_id: str, domain_name: str, domain_icon: str, issues: list[dict]) -> str:
    if issues:
        issue_items = "\n".join(
            f'<li class="issue-row"><a class="issue-link" href="{i["filename"]}">'
            f'<span class="date">{i["date"]}</span>'
            f'<span class="title">{i["title"]}</span>'
            f'<span class="arrow">→</span>'
            f'</a></li>'
            for i in issues
        )
        list_html = f'<ul class="issue-list">{issue_items}</ul>'
    else:
        domain_svg_html = _domain_svg(domain_icon, domain_name)
        list_html = f'''
        <div class="empty-state">
          <div class="empty-icon-svg" style="width:48px;height:48px;margin:0 auto 16px;color:var(--text-mute);display:flex;align-items:center;justify-content:center;border:1px solid var(--line);border-radius:12px">
            <span style="display:inline-flex;width:24px;height:24px">{domain_svg_html}</span>
          </div>
          <h3>这个领域还没有任何一期</h3>
          <p>点首页该领域卡片上的「一键生成」按钮，让 Curio 替你跑全网搜索 + 选必读 + 拼周刊。</p>
          <a class="btn-primary-link" href="../../index.html">回首页一键生成 →</a>
        </div>'''

    domain_kicker_svg = _domain_svg(domain_icon, domain_name)
    body = f"""
<div class="hero">
  <div class="kicker"><span style="display:inline-flex;width:14px;height:14px;vertical-align:-2px;margin-right:6px;color:var(--accent)">{domain_kicker_svg}</span>领域</div>
  <h1>{domain_name}</h1>
  <div class="meta">共 {len(issues)} 期</div>
</div>
{list_html}
"""
    return _page_template(
        page_title=f"{domain_name} · Curio",
        nav_active=domain_id,
        depth=2,
        body=body,
    )


def render_home(domains: list[dict], latest_issues: list[dict], top_n_cross: list[dict]) -> str:
    cards = []
    for d in domains:
        latest_str = d.get("latest_date") or "—"
        # 一键生成按钮：当领域有期数时显示"再跑一次"，没期数时显示"一键生成"
        gen_label = "再跑一次" if d["issue_count"] > 0 else "一键生成"
        icon_svg = _domain_svg(d.get("icon", ""), d.get("name", ""), d.get("icon_type", ""))
        cards.append(f'''
<a class="domain-card" href="d/{d['id']}/index.html">
  <button class="del-btn" data-domain-id="{d['id']}" data-domain-name="{d['name']}" title="删除">×</button>
  <div class="badge">{icon_svg}</div>
  <div class="name">{d['name']}</div>
  <div class="meta"><span>{d['issue_count']} 期</span><span class="dot"></span><span>最新 {latest_str}</span></div>
  <button class="gen-btn" data-domain-id="{d['id']}" data-domain-name="{d['name']}">{gen_label}</button>
</a>''')
    cards.append('''
<div class="domain-card add-domain">
  <div class="plus-icon">
    <svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
  </div>
  <div>添加新领域</div>
</div>''')

    # 跨领域 Top N
    top_n_html = ""
    if top_n_cross:
        rows = "\n".join(
            f'<tr><td style="width:32px;text-align:center;color:var(--text-mute);font-family:var(--mono);font-size:12px">{i+1:02d}</td>'
            f'<td><a href="d/{t["domain_id"]}/{t["filename"]}">{t["headline"][:80]}</a></td>'
            f'<td style="font-family:var(--mono);color:var(--text-mute);font-size:12px">{t["date"]}</td></tr>'
            for i, t in enumerate(top_n_cross)
        )
        top_n_html = f'''
<div class="top-n" style="border:1px solid var(--accent-soft);border-radius:8px;overflow:hidden;margin:32px 0;">
  <div style="background:linear-gradient(90deg,var(--bg-elev),transparent);padding:14px 18px;border-bottom:1px solid var(--line);">
    <span style="font-family:var(--sans);font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:var(--accent);">今日跨领域头条</span>
  </div>
  <table style="width:100%;border-collapse:collapse;font-family:var(--sans);font-size:14px;margin:0;">
    <thead>
      <tr><th style="background:var(--bg-elev);text-align:center;padding:10px 14px;font-weight:600;color:var(--text-soft);font-size:11px;letter-spacing:0.04em;text-transform:uppercase;border-bottom:1px solid var(--line);width:40px">#</th>
      <th style="background:var(--bg-elev);text-align:left;padding:10px 14px;font-weight:600;color:var(--text-soft);font-size:11px;letter-spacing:0.04em;text-transform:uppercase;border-bottom:1px solid var(--line);">头条</th>
      <th style="background:var(--bg-elev);text-align:left;padding:10px 14px;font-weight:600;color:var(--text-soft);font-size:11px;letter-spacing:0.04em;text-transform:uppercase;border-bottom:1px solid var(--line);width:100px">日期</th></tr>
    </thead>
    <tbody>{rows}</tbody>
  </table>
</div>'''

    if latest_issues:
        issue_items = "\n".join(
            f'<li><span class="date">{i["date"]}</span>'
            f'<span class="title"><a href="d/{i["domain_id"]}/{i["filename"]}">{i["title"]}</a></span></li>'
            for i in latest_issues
        )
        latest_html = f"""
<h2>最新各期</h2>
<ul class="issue-list">{issue_items}</ul>"""
    else:
        latest_html = ""

    body = f"""
<div class="hero">
  <div class="kicker">你的私人主编</div>
  <h1>Curio</h1>
  <div class="meta">每周一早上 8:00 自动从全网为你抓取并写成一份私人报纸。</div>
</div>

<h2>你的领域</h2>
<div class="domain-grid">{''.join(cards)}</div>

{top_n_html}

<div class="rule-double"></div>

{latest_html}
"""
    return _page_template(page_title="Curio · 你的私人主编", nav_active="home", depth=0, body=body)


def _page_template(page_title: str, nav_active: str, depth: int, body: str) -> str:
    """depth: 0=root (index.html), 1=d/<x>/index.html, 2=d/<x>/<y>.html"""
    rel_root = "../" * depth if depth > 0 else ""
    # 加时间戳作为 cache buster，避免浏览器使用旧版 JS/CSS
    cache_v = datetime.now().strftime("%Y%m%d%H%M%S")
    css_href = f"{rel_root}styles.css?v={cache_v}"
    js_href = f"{rel_root}app.js?v={cache_v}"

    nav_links = [f'<a href="{rel_root}index.html"' + (' class="active"' if nav_active == "home" else "") + '>首页</a>']
    if SOURCES.exists():
        cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}
        for did, dcfg in (cfg.get("domains") or {}).items():
            cls = ' class="active"' if nav_active == did else ""
            name = dcfg.get("name", did)
            href = f"{rel_root}d/{did}/index.html"
            nav_links.append(f'<a href="{href}"{cls}>{name}</a>')
    nav_html = "".join(nav_links)
    brand_href = f"{rel_root}index.html"

    # API base：用自有域名（Cloudflare proxy），不能用 *.workers.dev（国内 GFW 投毒）
    api_base = os.environ.get("CURIO_API_BASE", "https://api.curioradar.fun")

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<link rel="stylesheet" href="{css_href}">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@400;600;700&family=Inter:wght@400;500;600&family=Noto+Serif+SC:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a class="brand" href="{brand_href}">Curio<span class="dot">.</span></a>
    <div class="nav-links">{nav_html}</div>
    <div class="search-wrap">
      <span class="search-icon">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="20" y1="20" x2="16.65" y2="16.65"/></svg>
      </span>
      <input type="text" class="search-input" id="curio-search" placeholder="搜索  ⌘K" autocomplete="off">
      <div class="search-results" id="curio-search-results"></div>
    </div>
    <button class="subscribe-btn" id="subscribe-btn" title="订阅 Curio 邮件简报">
      <svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      <span class="sub-label">订阅</span>
    </button>
    <button class="theme-toggle" id="theme-toggle" title="切换主题（深/浅色）">
      <span class="icon-moon-default" style="display:inline-flex">
        <svg viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      </span>
      <span class="icon-sun">
        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
      </span>
    </button>
  </div>
</nav>

<aside class="toc" id="curio-toc">
  <div class="toc-title">本期目录</div>
  <div id="curio-toc-list"></div>
</aside>

<main>
{body}
</main>

<footer>
  Curio v0.9 · {datetime.now().strftime('%Y-%m-%d')} · 由你和 AI 共同策展 · <a href="https://github.com/zczxd1118/curio-app" target="_blank" rel="noopener" style="color:inherit;opacity:0.6">zxd</a>
</footer>

<script>
window.CURIO_REL_ROOT = "{rel_root}";
window.CURIO_API_BASE = "{api_base}";
window.CURIO_GH_REPO = "zczxd1118/curio-app";
</script>
<script src="{js_href}"></script>
</body>
</html>
"""


def _extract_top_headline(domain_id: str) -> str:
    """从【该 domain 的】scored.json 拿 must_read[0].title。

    匹配规则（按优先级）：
      1. {domain_id}.scored.json
      2. {topic_id}.scored.json（domain.topics 字典的某个 key）
      3. {domain.name slugify}.scored.json（中文名 → 中文 slug 文件）
    """
    # 1. 直接按 domain_id
    direct = TOPICS / f"{domain_id}.scored.json"
    candidates = [direct]
    # 2. 按 sources.yaml 找 topic_ids 和中文 slug
    try:
        cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}
        dcfg = (cfg.get("domains") or {}).get(domain_id) or {}
        for topic_id in (dcfg.get("topics") or {}):
            candidates.append(TOPICS / f"{topic_id}.scored.json")
        # 中文名 slugify（curator.py:slugify 等价）
        name = dcfg.get("name", "")
        if name:
            zh_slug = re.sub(r"[^\w\u4e00-\u9fa5]+", "-", name.lower()).strip("-")
            if zh_slug:
                candidates.append(TOPICS / f"{zh_slug}.scored.json")
    except Exception:
        pass

    for f in candidates:
        if f.exists():
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
                must = d.get("must_read", [])
                if must:
                    return (must[0].get("title", "") or "")[:80]
            except Exception:
                continue
    return ""


# ============================================================================
# 入口
# ============================================================================
def build_site():
    SITE.mkdir(exist_ok=True)
    (SITE / "styles.css").write_text(CSS, encoding="utf-8")
    (SITE / "app.js").write_text(APP_JS, encoding="utf-8")

    if not SOURCES.exists():
        print("❌ sources.yaml 不存在", file=sys.stderr)
        return 1
    cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}
    domains_cfg = cfg.get("domains") or {}

    domains_meta = []
    all_latest = []
    cross_top_n = []

    for did, dcfg in domains_cfg.items():
        domain_name = dcfg.get("name", did)
        domain_icon = dcfg.get("icon", "📰")

        slugs = [did] + list((dcfg.get("topics") or {}).keys())
        issues = []
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
                first_line = f.read_text(encoding="utf-8").split("\n", 1)[0]
                title = first_line.lstrip("# ").strip()
                issues.append({"date": date, "filename": f"{date}.html", "title": title, "src": f})

        issues.sort(key=lambda x: x["date"], reverse=True)

        # 总要建 d/<did>/ 目录（即使没期数也要有 index.html）
        domain_dir = SITE / "d" / did
        domain_dir.mkdir(parents=True, exist_ok=True)

        for i in issues:
            html = render_issue(i["src"], did, domain_name, domain_icon)
            (domain_dir / i["filename"]).write_text(html, encoding="utf-8")

        idx_html = render_domain_index(did, domain_name, domain_icon, issues)
        (domain_dir / "index.html").write_text(idx_html, encoding="utf-8")

        domains_meta.append({
            "id": did, "name": domain_name, "icon": domain_icon,
            "icon_type": dcfg.get("icon_type", ""),
            "issue_count": len(issues), "latest_date": issues[0]["date"] if issues else None,
        })

        if issues:
            all_latest.append({**issues[0], "domain_id": did, "icon": domain_icon})
            # 取该领域最新期的头条
            headline = _extract_top_headline(did)
            if headline:
                cross_top_n.append({
                    "domain_id": did, "icon": domain_icon,
                    "headline": headline, "filename": issues[0]["filename"],
                    "date": issues[0]["date"],
                })

    all_latest.sort(key=lambda x: x["date"], reverse=True)
    cross_top_n.sort(key=lambda x: x["date"], reverse=True)

    home_html = render_home(domains_meta, all_latest[:8], cross_top_n[:4])
    (SITE / "index.html").write_text(home_html, encoding="utf-8")

    # B 阶段：写客户端搜索索引（扫所有 scored.json 取必读+参考）
    search_idx = []
    for f in TOPICS.glob("*.scored.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        slug = f.stem.replace(".scored", "")
        # 反查 domain_id（slug 可能是中文）
        domain_id = slug
        domain_icon = "📰"
        domain_name = d.get("domain") or slug
        for did, dcfg in domains_cfg.items():
            if dcfg.get("name") == domain_name or did == slug:
                domain_id = did
                domain_icon = dcfg.get("icon", "📰")
                break
        for tier_key, tier_label in [("must_read", "必读"), ("reference", "参考")]:
            for it in (d.get(tier_key) or []):
                search_idx.append({
                    "title": (it.get("title") or "")[:160],
                    "url": it.get("url") or "",
                    "platform": it.get("platform") or "",
                    "tier": tier_label,
                    "why": (it.get("why_recommend") or "")[:160],
                    "domain": domain_name,
                    "domain_icon": domain_icon,
                    "issue_path": f"d/{domain_id}/index.html",
                })
    # 也把每期文章本身收录（按 domain index 跳转）
    for d in all_latest:
        search_idx.append({
            "title": d.get("title") or "",
            "url": "",
            "platform": "",
            "tier": "期刊",
            "why": d.get("date") or "",
            "domain": next((dm["name"] for dm in domains_meta if dm["id"] == d.get("domain_id")), ""),
            "domain_icon": d.get("icon", "📰"),
            "issue_path": f"d/{d.get('domain_id')}/{d.get('filename')}",
        })
    (SITE / "search-index.json").write_text(
        json.dumps(search_idx, ensure_ascii=False), encoding="utf-8"
    )

    # GitHub Pages 自定义域名（让 zczxd1118.github.io/curio-site → curioradar.fun）
    (SITE / "CNAME").write_text("curioradar.fun\n", encoding="utf-8")

    print(f"✅ Site built at: {SITE}")
    print(f"   领域：{len(domains_meta)} 个")
    print(f"   总期数：{sum(d['issue_count'] for d in domains_meta)}")
    print(f"   跨领域头条：{len(cross_top_n)} 条")
    print(f"   搜索索引：{len(search_idx)} 条")
    return 0


if __name__ == "__main__":
    sys.exit(build_site())
