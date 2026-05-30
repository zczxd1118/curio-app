
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
