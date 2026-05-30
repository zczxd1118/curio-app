/* =========================================================
   Curio · wireframe app
   ========================================================= */

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

const state = { currentDomain: "ai" };

// ---------- Sidebar ----------
function renderSidebar() {
  const items = MOCK.domains
    .map(
      (d) => `
      <button class="sb-item ${
        d.id === state.currentDomain && location.hash !== "#/profile"
          ? "active"
          : ""
      }" data-domain="${d.id}" title="${d.name}">
        ${icon(d.id)}
        ${d.unread ? '<span class="dot"></span>' : ""}
      </button>`
    )
    .join("");

  const sidebar = $(".sidebar");
  sidebar.innerHTML = `
    <div class="sb-logo" title="Curio">C</div>
    ${items}
    <button class="sb-item" data-action="new-domain" title="新建 Domain">
      ${icon("plus")}
    </button>
    <div class="sb-spacer"></div>
    <div class="sb-divider"></div>
    <button class="sb-item ${
      location.hash === "#/profile" ? "active" : ""
    }" data-action="profile" title="个人画像">
      ${icon("user")}
    </button>
    <button class="sb-item" data-action="settings" title="设置">
      ${icon("settings")}
    </button>
  `;

  $$(".sb-item[data-domain]", sidebar).forEach((el) =>
    el.addEventListener("click", () => {
      state.currentDomain = el.dataset.domain;
      if (location.hash === "#/profile" || location.hash === "") {
        location.hash = "#/";
      } else {
        renderRoute();
      }
      renderSidebar();
    })
  );
  $('.sb-item[data-action="profile"]', sidebar).addEventListener("click", () => {
    location.hash = "#/profile";
  });
}

// ---------- Pages ----------
function pageDashboard() {
  const d = MOCK.domains.find((x) => x.id === state.currentDomain);

  const topicCards = d.topic_ids
    .map((tid) => {
      const t = MOCK.topics[tid];
      return `
      <a class="card topic-card" href="#/topic/${t.id}">
        <div class="tc-head">
          <div class="tc-icon">${icon("hash")}</div>
          <div class="tc-name">${t.name}</div>
        </div>
        <div class="tc-stats">
          <span><b>${t.kol_count}</b> KOL</span>
          <span class="sep">·</span>
          <span><b>${t.content_count}</b> 条</span>
        </div>
      </a>`;
    })
    .join("");

  const mustRead = (MOCK.must_read_by_domain[d.id] || [])
    .map(
      (c) => `
      <div class="list-row">
        <span class="tag must">必读</span>
        <div>
          <div class="row-title">${c.title}</div>
          <div class="row-meta">
            ${c.kol}<span class="sep">·</span>${c.platform}<span class="sep">·</span>${c.duration}
          </div>
        </div>
        <span class="row-arrow">${icon("chevronRight")}</span>
      </div>`
    )
    .join("");

  const hints = (MOCK.cross_hints[d.id] || [])
    .map((h) => {
      return `
      <div class="hint-item" data-domain="${h.domain_id}">
        <div class="left">
          <div class="domain-glyph">${icon(h.domain_id)}</div>
          <span>${h.text}</span>
        </div>
        <span class="arrow">${icon("arrowRight")}</span>
      </div>`;
    })
    .join("");

  const digest = MOCK.latest_digest_by_domain[d.id];
  const freqLabel = d.frequency === "daily" ? "Daily" : "Weekly";
  const freqLabelZh = d.frequency === "daily" ? "每日" : "每周";

  return `
    <header class="page-header">
      <div>
        <h1 class="page-title">
          <span class="pt-icon">${icon(d.id)}</span>
          ${d.name}
        </h1>
        <div class="page-meta">
          ${d.topic_ids.length} Topics
          <span class="sep">·</span>
          ${d.kol_count} KOL
          <span class="sep">·</span>
          ${d.content_count} 条内容
          <span class="sep">·</span>
          ${freqLabel} 推送
        </div>
      </div>
      <div class="page-tools">
        <button class="btn ghost">${icon("clock")} 频率</button>
        <a class="btn primary" href="#/explore">${icon("plus")} 新主题</a>
      </div>
    </header>

    <section class="section">
      <div class="section-head">
        <h3 class="section-title">Topics</h3>
        <span class="section-count">${d.topic_ids.length}</span>
      </div>
      <div class="card-grid">
        ${topicCards}
        <a class="card new-topic-card" href="#/explore">
          <span class="row">${icon("plus")} 探索新主题</span>
        </a>
      </div>
    </section>

    <section class="section">
      <div class="section-head">
        <h3 class="section-title">${freqLabelZh}必读</h3>
        <span class="section-count">${(MOCK.must_read_by_domain[d.id] || []).length}</span>
        <span class="spacer"></span>
        <a class="more" href="#">查看全部 ${icon("chevronRight")}</a>
      </div>
      <div class="list">${mustRead}</div>
    </section>

    ${
      hints
        ? `<section class="section">
        <div class="section-head">
          <h3 class="section-title">其它领域</h3>
        </div>
        <div class="cross-hint">${hints}</div>
      </section>`
        : ""
    }

    ${
      digest
        ? `<section class="section">
        <div class="section-head">
          <h3 class="section-title">最新推送</h3>
        </div>
        <a class="digest-banner" href="#/digest/${digest.id}">
          <div class="left">
            <div class="lead">${digest.label}</div>
            <div class="sub">${digest.period}</div>
          </div>
          <div class="right">
            打开 ${icon("arrowRight")}
          </div>
        </a>
      </section>`
        : ""
    }
  `;
}

function pageProfile() {
  const p = MOCK.profile;
  const interests = p.interests.map((t) => `<span class="tg">${t}</span>`).join("");
  const dislikes = p.dislikes.map((t) => `<span class="tg">${t}</span>`).join("");
  const signals = p.signal_preferences.map((t) => `<span class="tg">${t}</span>`).join("");
  const fb = p.feedback_timeline
    .map(
      (f) => `
      <div class="fb-item">
        <div class="fb-date">${f.date}</div>
        <div class="fb-text">${f.text}</div>
      </div>`
    )
    .join("");

  return `
    <header class="page-header">
      <div>
        <h1 class="page-title">
          <span class="pt-icon">${icon("user")}</span>
          画像
        </h1>
        <div class="page-meta">Agent 帮你筛选信息时的参照系</div>
      </div>
      <div class="page-tools">
        <button class="btn ghost">${icon("edit")} 编辑</button>
      </div>
    </header>

    <div class="identity-card">
      <div class="updated"><span class="pulse"></span>实时同步</div>
      <div class="label">Identity</div>
      <h2 class="name">${p.name}</h2>
      <div class="role">${p.identity}</div>
    </div>

    <div class="profile-grid">
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div class="profile-card">
          <h3>${icon("target")} 关心</h3>
          <div class="tag-cloud">${interests}</div>
        </div>
        <div class="profile-card">
          <h3>${icon("ban")} 看不上</h3>
          <div class="tag-cloud dislikes">${dislikes}</div>
        </div>
        <div class="profile-card">
          <h3>${icon("signal")} 想要的信号</h3>
          <div class="tag-cloud signals">${signals}</div>
        </div>
        <div class="profile-card">
          <h3>${icon("clock")} 节奏</h3>
          <div class="body">${p.reading_pace}</div>
        </div>
      </div>

      <div>
        <div class="profile-card" style="height: 100%;">
          <h3>${icon("refresh")} 反馈摘要</h3>
          <div class="body muted" style="font-size:12px;margin-bottom:14px">
            Agent 从你的 Digest 反馈区自动提取，影响下一次推送
          </div>
          <div class="fb-timeline">${fb}</div>
          <div class="toggle-row">
            <span>Agent 自动从反馈更新画像</span>
            <span class="toggle"></span>
          </div>
        </div>
      </div>
    </div>
  `;
}

function pagePlaceholder(name) {
  return `
    <header class="page-header">
      <div>
        <h1 class="page-title">${name}</h1>
        <div class="page-meta">M0 第二批待画</div>
      </div>
      <div class="page-tools">
        <a class="btn ghost" href="#/">← Dashboard</a>
      </div>
    </header>
    <div class="profile-card" style="margin-top:48px;padding:64px;text-align:center;border-style:dashed;">
      <div style="font-size:32px;color:var(--fg-4);margin-bottom:12px;">🚧</div>
      <p class="muted" style="font-size:13px;margin:0">${name} 待补</p>
    </div>
  `;
}

// ---------- Router ----------
function renderRoute() {
  const hash = location.hash || "#/";
  const main = $(".main");
  let html;

  if (hash === "#/" || hash === "") html = pageDashboard();
  else if (hash === "#/profile") html = pageProfile();
  else if (hash === "#/explore") html = pagePlaceholder("Explore");
  else if (hash.startsWith("#/topic/")) html = pagePlaceholder("Topic 看板");
  else if (hash.startsWith("#/kol/")) html = pagePlaceholder("KOL 详情");
  else if (hash.startsWith("#/digest/")) html = pagePlaceholder("Digest");
  else html = pagePlaceholder("404");

  main.innerHTML = html;
  renderSidebar();

  $$(".hint-item[data-domain]", main).forEach((el) =>
    el.addEventListener("click", () => {
      state.currentDomain = el.dataset.domain;
      location.hash = "#/";
    })
  );

  window.scrollTo(0, 0);
}

window.addEventListener("hashchange", renderRoute);
window.addEventListener("DOMContentLoaded", () => {
  renderSidebar();
  renderRoute();
});
