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
}
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
.domain-card { padding: 24px; background: var(--bg-soft); border: 1px solid var(--line); border-radius: 8px; text-decoration: none; color: var(--text); transition: all 0.15s; position: relative; display: block; }
.domain-card:hover { border-color: var(--accent-soft); background: var(--bg-elev); transform: translateY(-2px); }
.domain-card .icon { font-size: 28px; margin-bottom: 12px; }
.domain-card .name { font-family: var(--serif); font-size: 18px; font-weight: 600; margin-bottom: 6px; }
.domain-card .meta { font-family: var(--sans); font-size: 12px; color: var(--text-mute); }
.domain-card .del-btn { position: absolute; top: 8px; right: 8px; width: 24px; height: 24px; border-radius: 50%; background: transparent; border: 1px solid var(--line); color: var(--text-mute); font-size: 14px; line-height: 20px; cursor: pointer; opacity: 0; transition: opacity 0.15s; padding: 0; }
.domain-card:hover .del-btn { opacity: 1; }
.domain-card .del-btn:hover { color: var(--red); border-color: var(--red); }
.add-domain { border: 2px dashed var(--line); background: transparent; display: flex; align-items: center; justify-content: center; flex-direction: column; color: var(--text-mute); cursor: pointer; font-family: var(--sans); font-size: 14px; padding: 24px; }
.add-domain:hover { border-color: var(--accent-soft); color: var(--accent); }
.add-domain .icon { font-size: 28px; margin-bottom: 8px; color: inherit; }

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
"""


# ============================================================================
# 前端 JS
# ============================================================================
APP_JS = r"""
// ===== 工具 =====
const API_BASE = '';  // 同源 → 用相对路径

function $(s, root=document) { return root.querySelector(s); }
function $$(s, root=document) { return Array.from(root.querySelectorAll(s)); }

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

function isServerMode() {
  // 用 file:// 打开时 location.protocol === 'file:'
  return location.protocol === 'http:' || location.protocol === 'https:';
}

// ===== 添加领域弹窗 =====
const ICONS = ['🤖','🏦','🔬','📈','🧬','⚛️','🎮','📚','🎨','🚀','🌍','💊','🏛️','🎬','⚖️','🔋'];

function openAddDomainModal() {
  if (!isServerMode()) {
    alert('需要先启动后端：\\n\\n  python server.py\\n\\n然后用 http://localhost:8765/ 打开');
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

async function deleteDomain(domainId, domainName) {
  if (!isServerMode()) { alert('需先启动后端'); return; }
  if (!confirm(`确定要删除领域「${domainName}」吗？\\n（往期 markdown 文件不会被删，可手动恢复）`)) return;
  try {
    await api('/api/domains/' + encodeURIComponent(domainId), {method: 'DELETE'});
    toast('已删除 ' + domainName);
    setTimeout(() => location.reload(), 600);
  } catch (e) {
    toast('❌ ' + e.message, true);
  }
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
  if (!isServerMode()) {
    alert('需要先启动后端：python server.py');
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

// ===== 启动 =====
document.addEventListener('DOMContentLoaded', () => {
  // 添加领域按钮
  const addBtn = $('.add-domain');
  if (addBtn) addBtn.addEventListener('click', openAddDomainModal);

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

  // 反馈交互
  initFeedback();

  // 检测是否后端可用（API 健康检查）
  fetch('/api/health').then(r => {
    if (!r.ok) throw new Error('no api');
  }).catch(() => {
    // 静态模式：显示提示 + 隐藏交互按钮
    const notice = document.getElementById('static-mode-notice');
    if (notice) notice.style.display = 'block';
    $$('.gen-btn, .del-btn').forEach(b => b.style.display = 'none');
    const addBtn = $('.add-domain');
    if (addBtn) {
      addBtn.style.opacity = '0.4';
      addBtn.style.cursor = 'not-allowed';
      addBtn.title = '本地启动 server 后可用';
    }
    // 反馈区改成"通过 GitHub Issue 提交"模式
    $$('.feedback').forEach(fb => {
      const submit = $('.fb-submit-btn', fb);
      if (submit) {
        submit.textContent = '提交反馈到 GitHub';
      }
      const desc = $('.desc', fb);
      if (desc) desc.textContent = '点击下方按钮，会跳转到 GitHub 预填好的 Issue 页面，登录确认即可。Agent 下次跑时会自动读取并关闭。';
    });
  });
});
"""


# ============================================================================
# 渲染器
# ============================================================================
def _slug_for_path(s: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^\w\u4e00-\u9fa5]+", "-", s.strip().lower())).strip("-")


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
        list_html = f'''
        <div class="empty-state">
          <div class="empty-icon">{domain_icon}</div>
          <h3>这个领域还没有任何一期</h3>
          <p>点首页该领域卡片上的「一键生成」按钮，让 Curio 替你跑全网搜索 + 选必读 + 拼周刊。</p>
          <a class="btn-primary-link" href="../../index.html">回首页一键生成 →</a>
        </div>'''

    body = f"""
<div class="hero">
  <div class="kicker">{domain_icon} 领域</div>
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
        cards.append(f'''
<a class="domain-card" href="d/{d['id']}/index.html">
  <button class="del-btn" data-domain-id="{d['id']}" data-domain-name="{d['name']}" title="删除">×</button>
  <div class="icon">{d['icon']}</div>
  <div class="name">{d['name']}</div>
  <div class="meta">{d['issue_count']} 期 · 最新 {latest_str}</div>
  <button class="gen-btn" data-domain-id="{d['id']}" data-domain-name="{d['name']}">{gen_label}</button>
</a>''')
    cards.append('''
<div class="domain-card add-domain">
  <div class="icon">+</div>
  <div>添加新领域</div>
</div>''')

    # 跨领域 Top N
    top_n_html = ""
    if top_n_cross:
        rows = "\n".join(
            f'<tr><td style="width:32px;text-align:center">{i+1}</td>'
            f'<td>{t["icon"]} <a href="d/{t["domain_id"]}/{t["filename"]}">{t["headline"][:80]}</a></td>'
            f'<td style="font-family:var(--mono);color:var(--text-mute);font-size:12px">{t["date"]}</td></tr>'
            for i, t in enumerate(top_n_cross)
        )
        top_n_html = f'''
<div class="top-n" style="border:1px solid var(--accent-soft);border-radius:8px;overflow:hidden;margin:32px 0;">
  <div style="background:linear-gradient(90deg,var(--bg-elev),transparent);padding:14px 18px;border-bottom:1px solid var(--line);">
    <span style="font-family:var(--sans);font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:var(--accent);">🛰️ 今日跨领域头条</span>
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
            f'<span class="title">{i["icon"]} <a href="d/{i["domain_id"]}/{i["filename"]}">{i["title"]}</a></span></li>'
            for i in latest_issues
        )
        latest_html = f"""
<h2>最新各期</h2>
<ul class="issue-list">{issue_items}</ul>"""
    else:
        latest_html = ""

    fallback_notice = '''
<div class="fallback-notice" id="static-mode-notice" style="display:none">
  💡 <strong>当前是只读演示版</strong>。添加领域、提交反馈、一键生成等交互需要本地后端。运行 <code>git clone</code> 后 <code>python server.py</code> 即可解锁完整功能。
</div>'''

    body = f"""
<div class="hero">
  <div class="kicker">🛰️ 你的私人主编</div>
  <h1>Curio</h1>
  <div class="meta">用自然语言告诉它你关心什么，它替你从全网找有价值的内容写成报纸送到你眼前。</div>
</div>

{fallback_notice}

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
            icon = dcfg.get("icon", "")
            name = dcfg.get("name", did)
            href = f"{rel_root}d/{did}/index.html"
            nav_links.append(f'<a href="{href}"{cls}>{icon} {name}</a>')
    nav_html = "".join(nav_links)
    brand_href = f"{rel_root}index.html"

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
  </div>
</nav>

<main>
{body}
</main>

<footer>
  Curio v0.8 · {datetime.now().strftime('%Y-%m-%d')} · 由你和 AI 共同策展
</footer>

<script src="{js_href}"></script>
</body>
</html>
"""


def _extract_top_headline(domain_id: str) -> str:
    """从该 domain 的 scored.json 拿 must_read[0].title 的第 1 句"""
    for f in TOPICS.glob("*.scored.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            must = d.get("must_read", [])
            if must:
                title = must[0].get("title", "") or ""
                # 截 50 字
                return title[:80]
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

    print(f"✅ Site built at: {SITE}")
    print(f"   领域：{len(domains_meta)} 个")
    print(f"   总期数：{sum(d['issue_count'] for d in domains_meta)}")
    print(f"   跨领域头条：{len(cross_top_n)} 条")
    return 0


if __name__ == "__main__":
    sys.exit(build_site())
