
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
        📋 Agent 收到时会在 GitHub Issue 评论"已收到，开始跑"，完成时再评论结果链接
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
