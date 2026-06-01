// Curio API · Cloudflare Worker
// Endpoints:
//   POST /subscribe          —— 网页订阅入口
//   GET  /confirm?token=xxx  —— 邮件验证链接
//   GET  /unsubscribe?token  —— 退订
//   GET  /domains            —— 当前可订阅的领域
//   POST /broadcast          —— automation 调，按订阅者偏好发邮件（需 ADMIN_TOKEN）
//   POST /admin/sync-domains —— automation 同步 sources.yaml 到 KV
//   POST /admin/push-content —— automation 推送本期内容到 KV
//   POST /add-domain-request —— 网页"加领域"按钮转 GitHub Issue 跳转（前端走，这里收一份记录）
//   GET/POST/DELETE /llm/config —— 网页"设置"弹窗 BYOK（鉴权用 OWNER_PIN，存 LLM key）
//   POST /llm/test           —— 测试 LLM 连接是否通（用 OWNER_PIN）
//   GET  /admin/llm-config   —— CI 拉完整 LLM 配置（用 ADMIN_TOKEN）
//   GET  /                   —— 健康检查 + 简介

const PENDING_TTL_SEC = 60 * 60 * 48; // 48h

// ============== utils ==============

function json(data, status = 200, extraHeaders = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "access-control-allow-origin": "*",
      "access-control-allow-methods": "GET,POST,DELETE,OPTIONS",
      "access-control-allow-headers": "content-type, authorization, x-curio-owner-pin",
      ...extraHeaders,
    },
  });
}

function errorJson(msg, status = 400) {
  return json({ ok: false, error: msg }, status);
}

function isValidEmail(s) {
  return typeof s === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s) && s.length <= 200;
}

function isValidCadence(s) {
  return s === "daily" || s === "weekly";
}

function genToken(len = 32) {
  const bytes = new Uint8Array(len);
  crypto.getRandomValues(bytes);
  return Array.from(bytes).map((b) => b.toString(16).padStart(2, "0")).join("");
}

function htmlPage(title, body) {
  return new Response(
    `<!doctype html><html lang="zh"><head><meta charset="utf-8"><title>${title} · Curio</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", system-ui, sans-serif;
         max-width: 540px; margin: 60px auto; padding: 0 20px; color: #1a1a1c; line-height: 1.6; }
  h1 { font-size: 22px; margin: 0 0 16px; }
  .card { background: #fafaf8; border: 1px solid #e6e4dc; border-radius: 12px; padding: 28px; }
  .btn { display: inline-block; padding: 8px 16px; background: #1a1a1c; color: #fff;
         text-decoration: none; border-radius: 6px; margin-top: 12px; }
  code { background: #f0eee5; padding: 2px 6px; border-radius: 4px; font-size: 13px; }
  .muted { color: #888; font-size: 13px; margin-top: 24px; }
</style>
</head><body><div class="card">${body}</div>
<div class="muted">Curio · 你的私人主编 · zxd 个人项目</div>
</body></html>`,
    { status: 200, headers: { "content-type": "text/html; charset=utf-8" } },
  );
}

// ============== email (Resend) ==============

async function sendEmail(env, { to, subject, html, text }) {
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      "authorization": `Bearer ${env.RESEND_API_KEY}`,
      "content-type": "application/json",
    },
    body: JSON.stringify({
      from: env.FROM_EMAIL,
      to: Array.isArray(to) ? to : [to],
      subject,
      html,
      text,
    }),
  });
  const ok = r.ok;
  const body = await r.text();
  return { ok, status: r.status, body };
}

function confirmEmailHTML(env, { confirmUrl, domains, cadence, meta }) {
  const cadenceText = cadence === "daily" ? "每天中午 12:00" : "每周一中午 12:00";
  // 用中文名展示，meta 缺时回退 slug
  const displayName = (slug) => (meta && meta[slug] && meta[slug].name) || slug;
  const domainList = domains.map((d) => `<li>${displayName(d)}</li>`).join("");
  return `<!doctype html><html><body style="font-family:-apple-system,system-ui,sans-serif;max-width:560px;margin:30px auto;padding:0 20px;color:#1a1a1c;line-height:1.6">
<h2 style="margin:0 0 4px;font-weight:600;letter-spacing:-0.01em">确认订阅 Curio</h2>
<p style="color:#888;font-size:13px;margin:0 0 20px">你的私人主编 · curioradar.fun</p>
<p>你（或者用你邮箱的人）刚刚订阅了 Curio 内容简报。</p>
<table cellpadding="0" cellspacing="0" style="background:#fafaf8;border-left:3px solid #d4af37;padding:14px 18px;margin:18px 0;font-size:14px">
  <tr><td style="padding-right:12px;color:#666;vertical-align:top;white-space:nowrap">订阅领域</td><td><ul style="margin:0;padding-left:18px">${domainList}</ul></td></tr>
  <tr><td style="padding:8px 12px 0 0;color:#666;vertical-align:top;white-space:nowrap">推送频率</td><td style="padding-top:8px">${cadenceText}</td></tr>
</table>
<p>请点击下面按钮完成确认（48 小时内有效）：</p>
<p><a href="${confirmUrl}" style="display:inline-block;padding:11px 24px;background:#1a1a1c;color:#fff;text-decoration:none;border-radius:6px;font-weight:500">确认订阅</a></p>
<p style="font-size:12px;color:#888;margin-top:24px">如果不是你订阅的，忽略本邮件即可，订阅不会生效。</p>
<p style="font-size:12px;color:#888">想立刻退订？<a href="${env.API_BASE}/unsubscribe-by-email" style="color:#888">点这里</a>（无需 token，输入邮箱即可）</p>
<p style="font-size:12px;color:#888;border-top:1px solid #eee;padding-top:12px;margin-top:20px">Curio · zxd 个人项目 · <a href="${env.SITE_BASE}/" style="color:#888">访问网站</a></p>
</body></html>`;
}

// ============== handlers ==============

async function handleSubscribe(req, env) {
  let body;
  try {
    body = await req.json();
  } catch {
    return errorJson("invalid json");
  }
  const { email, domains, cadence } = body || {};
  if (!isValidEmail(email)) return errorJson("invalid email");
  if (!Array.isArray(domains) || domains.length === 0) return errorJson("pick at least one domain");
  if (domains.length > 20) return errorJson("too many domains");
  if (!isValidCadence(cadence)) return errorJson("cadence must be daily or weekly");

  // 校验域是否真存在
  const known = await env.CURIO_KV.get("domains:list", "json");
  if (Array.isArray(known) && known.length > 0) {
    const bad = domains.filter((d) => !known.includes(d));
    if (bad.length > 0) return errorJson("unknown domains: " + bad.join(","));
  }

  const lower = email.trim().toLowerCase();
  const existing = await env.CURIO_KV.get("subscriber:" + lower, "json");
  if (existing) {
    // 已确认订阅者重新提交：直接更新
    const merged = { ...existing, domains, cadence, updated_at: new Date().toISOString() };
    await env.CURIO_KV.put("subscriber:" + lower, JSON.stringify(merged));
    return json({ ok: true, status: "updated", message: "订阅偏好已更新" });
  }

  const token = genToken(24);
  const pending = {
    email: lower,
    domains,
    cadence,
    created_at: new Date().toISOString(),
  };
  await env.CURIO_KV.put("pending:" + token, JSON.stringify(pending), { expirationTtl: PENDING_TTL_SEC });

  const confirmUrl = `${env.API_BASE}/confirm?token=${token}`;
  // 拉 domains:meta 让确认邮件里显示中文名而不是 slug
  const meta = await env.CURIO_KV.get("domains:meta", "json");
  const mail = await sendEmail(env, {
    to: lower,
    subject: "确认订阅 Curio · 你的私人主编",
    html: confirmEmailHTML(env, { confirmUrl, domains, cadence, meta }),
    text: `请点击链接完成订阅确认：${confirmUrl}\n（48 小时内有效）`,
  });
  if (!mail.ok) {
    return errorJson("send confirm email failed: " + mail.body, 502);
  }
  return json({ ok: true, status: "pending", message: "已发送确认邮件，48 小时内点击邮件里的链接完成订阅" });
}

async function handleConfirm(req, env) {
  const url = new URL(req.url);
  const token = url.searchParams.get("token");
  if (!token) return htmlPage("出错了", "<h1>缺少 token</h1>");

  const pending = await env.CURIO_KV.get("pending:" + token, "json");
  if (!pending) return htmlPage("链接已失效", "<h1>链接已过期或已使用</h1><p>请回到网站重新订阅。</p>");

  const unsubToken = genToken(24);
  const sub = {
    email: pending.email,
    domains: pending.domains,
    cadence: pending.cadence,
    confirmed_at: new Date().toISOString(),
    unsub_token: unsubToken,
  };
  await env.CURIO_KV.put("subscriber:" + pending.email, JSON.stringify(sub));
  await env.CURIO_KV.put("unsub:" + unsubToken, pending.email); // 反查
  await env.CURIO_KV.delete("pending:" + token);

  const cadenceText = pending.cadence === "daily" ? "每天中午 12:00" : "每周一中午 12:00";
  return htmlPage(
    "订阅成功",
    `<h1>订阅成功</h1>
     <p>${cadenceText} 你会收到 Curio 简报，覆盖：</p>
     <p>${pending.domains.map((d) => `<code>${d}</code>`).join(" ")}</p>
     <p><a class="btn" href="${env.SITE_BASE}/">回到 Curio</a></p>`,
  );
}

async function handleUnsubscribe(req, env) {
  const url = new URL(req.url);
  const token = url.searchParams.get("token");
  if (!token) return htmlPage("出错了", "<h1>缺少 token</h1>");

  const email = await env.CURIO_KV.get("unsub:" + token);
  if (!email) return htmlPage("链接无效", "<h1>链接无效或已退订</h1>");

  await env.CURIO_KV.delete("subscriber:" + email);
  await env.CURIO_KV.delete("unsub:" + token);
  return htmlPage(
    "已退订",
    `<h1>已退订</h1><p>${email} 已从 Curio 订阅列表移除。</p>
     <p>如果改主意了随时回来：<a class="btn" href="${env.SITE_BASE}/">访问 Curio</a></p>`,
  );
}

// 自助退订：用户只输邮箱，自动找 token 并删除（不需要邮件里的 token）
// 这是为了应对 QQ 等邮箱拦截邮件、用户拿不到 token 的场景
async function handleUnsubscribeByEmail(req, env) {
  const url = new URL(req.url);

  // GET：返回一个简单的 HTML 表单
  if (req.method === "GET") {
    const email = url.searchParams.get("email") || "";
    return htmlPage(
      "退订 Curio",
      `<h1>退订 Curio</h1>
       <p>输入你订阅时用的邮箱即可退订。无需打开任何邮件。</p>
       <form method="POST" action="${env.API_BASE}/unsubscribe-by-email" style="max-width:420px">
         <input type="email" name="email" required value="${email}"
                placeholder="your@email.com"
                style="width:100%;padding:10px;font-size:14px;border:1px solid #ddd;border-radius:6px;margin-bottom:12px">
         <button type="submit" style="width:100%;padding:10px;background:#1a1a1c;color:#fff;border:0;border-radius:6px;cursor:pointer;font-size:14px">退订</button>
       </form>
       <p style="margin-top:24px;font-size:12px;color:#888">如果改主意了随时回来：<a href="${env.SITE_BASE}/">访问 Curio</a></p>`
    );
  }

  // POST：真正退订
  let email = "";
  const ct = req.headers.get("content-type") || "";
  if (ct.includes("application/json")) {
    try { const j = await req.json(); email = j.email || ""; } catch {}
  } else {
    const form = await req.formData();
    email = form.get("email") || "";
  }
  email = String(email || "").trim().toLowerCase();
  if (!isValidEmail(email)) {
    return htmlPage("退订失败", "<h1>邮箱格式不对</h1><p><a href='" + env.API_BASE + "/unsubscribe-by-email'>重试</a></p>");
  }

  const sub = await env.CURIO_KV.get("subscriber:" + email, "json");
  if (!sub) {
    // 也检查是否在 pending（未确认）
    return htmlPage(
      "未订阅",
      `<h1>${email} 没在 Curio 订阅列表里</h1>
       <p>可能从未订阅，或之前已退订。</p>
       <p><a href="${env.SITE_BASE}/">访问 Curio</a></p>`
    );
  }
  await env.CURIO_KV.delete("subscriber:" + email);
  if (sub.unsub_token) await env.CURIO_KV.delete("unsub:" + sub.unsub_token);
  return htmlPage(
    "已退订",
    `<h1>已退订</h1>
     <p>${email} 已从 Curio 订阅列表移除。</p>
     <p>之前订阅了：${(sub.domains || []).join(", ")}（${sub.cadence === "daily" ? "日报" : "周刊"}）</p>
     <p>如果改主意了随时回来：<a href="${env.SITE_BASE}/">访问 Curio</a></p>`
  );
}

async function handleDomains(req, env) {
  const list = await env.CURIO_KV.get("domains:list", "json");
  const meta = await env.CURIO_KV.get("domains:meta", "json");
  return json({
    ok: true,
    domains: Array.isArray(list) ? list : [],
    meta: meta || {},
  });
}

function isAdminAuthed(req, env) {
  const got = req.headers.get("authorization") || "";
  const expected = "Bearer " + (env.ADMIN_TOKEN || "");
  return env.ADMIN_TOKEN && got === expected;
}

// 网页点"⚡ 立刻生成" → Worker 收到 → 转发到本机 Cloudflare Tunnel webhook
// 让本机立即跑 prepare（不用等 hourly automation 轮询）。
//
// 前置条件：
// 1. 本机跑 python local_server.py 起 Flask（监听 8787）
// 2. cloudflared tunnel 把本机暴露成 https://local.curioradar.fun
// 3. wrangler.toml 配 LOCAL_TUNNEL_URL = "https://local.curioradar.fun"
//
// 如果 tunnel 不可达，自动 fallback 到旧路径（GitHub Issue + hourly automation）。
async function handleTriggerGenerate(req, env) {
  let body;
  try { body = await req.json(); } catch { return errorJson("invalid json"); }
  const domainId = body && body.domain_id;
  const issueNum = body && body.issue_num;
  if (!domainId) return errorJson("domain_id required");

  const tunnelUrl = env.LOCAL_TUNNEL_URL;
  if (!tunnelUrl) {
    // 没配 tunnel，告诉前端走 fallback（GitHub Issue 路径）
    return json({
      ok: false,
      fallback: "github_issue",
      message: "本机 webhook 未配置，请走 GitHub Issue（hourly automation 兜底）",
    });
  }

  // 转发到本机 Flask
  try {
    const r = await fetch(`${tunnelUrl}/trigger-generate`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Curio-Token": env.ADMIN_TOKEN,
        "User-Agent": "curio-worker/1.0",
      },
      body: JSON.stringify({ domain_id: domainId, issue_num: issueNum }),
      // CF Worker 默认 30s timeout，足够本机响应
    });
    if (!r.ok) {
      return json({
        ok: false,
        fallback: "github_issue",
        message: `本机响应 ${r.status}，请走 GitHub Issue 兜底`,
      });
    }
    const data = await r.json().catch(() => ({}));
    return json({ ok: true, ...data });
  } catch (e) {
    return json({
      ok: false,
      fallback: "github_issue",
      message: `本机不可达：${e.message}（电脑没开？请走 GitHub Issue）`,
    });
  }
}


async function handleAdminUnsubscribeDomain(req, env) {
  const auth = req.headers.get("authorization") || "";
  if (auth !== `Bearer ${env.ADMIN_TOKEN}`) {
    return errorJson("unauthorized", 401);
  }
  let body;
  try { body = await req.json(); } catch { return errorJson("invalid json"); }
  const domainId = body && body.domain_id;
  if (!domainId) return errorJson("domain_id required");

  // 列出所有订阅者，过滤含该 domain 的，把 domain 从 domains[] 移除
  const list = await env.CURIO_KV.list({ prefix: "subscriber:" });
  let touched = 0;
  let removed = 0;  // 因为只订了这一个域，整条订阅删除的数量
  for (const k of list.keys) {
    const sub = await env.CURIO_KV.get(k.name, "json");
    if (!sub || !Array.isArray(sub.domains)) continue;
    if (!sub.domains.includes(domainId)) continue;
    const newDomains = sub.domains.filter(d => d !== domainId);
    if (newDomains.length === 0) {
      // 用户只订了这一个域，整条订阅删掉
      await env.CURIO_KV.delete(k.name);
      if (sub.unsub_token) await env.CURIO_KV.delete("unsub:" + sub.unsub_token);
      removed++;
    } else {
      sub.domains = newDomains;
      await env.CURIO_KV.put(k.name, JSON.stringify(sub));
    }
    touched++;
  }

  // 同步从 domain meta KV 中删除（让 /domains 返回也少一项）
  const meta = (await env.CURIO_KV.get("domains:meta", "json")) || {};
  if (meta[domainId]) {
    delete meta[domainId];
    await env.CURIO_KV.put("domains:meta", JSON.stringify(meta));
  }
  // 也删该域的内容缓存
  await env.CURIO_KV.delete("content:" + domainId + ":latest");

  return json({ ok: true, count: touched, removed });
}

async function handleAdminSyncDomains(req, env) {
  if (!isAdminAuthed(req, env)) return errorJson("unauthorized", 401);
  let body;
  try { body = await req.json(); } catch { return errorJson("invalid json"); }
  const { domains, meta } = body || {};
  if (!Array.isArray(domains)) return errorJson("domains[] required");
  await env.CURIO_KV.put("domains:list", JSON.stringify(domains));
  if (meta && typeof meta === "object") {
    await env.CURIO_KV.put("domains:meta", JSON.stringify(meta));
  }
  return json({ ok: true, count: domains.length });
}

async function handleAdminPushContent(req, env) {
  if (!isAdminAuthed(req, env)) return errorJson("unauthorized", 401);
  let body;
  try { body = await req.json(); } catch { return errorJson("invalid json"); }
  const { slug, content } = body || {};
  if (!slug || !content) return errorJson("slug + content required");
  await env.CURIO_KV.put("content:" + slug + ":latest", JSON.stringify(content));
  return json({ ok: true });
}


// ============== LLM BYOK ==============
//
// 单用户场景下的简化设计：
//   - OWNER_PIN（wrangler secret put OWNER_PIN）作为前端写 LLM 配置时的鉴权
//   - LLM key 存在 KV（"llm:owner" key），明文存（KV 本身就只有 admin/owner 能读）
//   - GET 不暴露完整 key，只返回 provider/model/key_prefix/key_tail，避免泄漏
//   - score-and-finalize.yml 内部用 ADMIN_TOKEN（不是 OWNER_PIN）拉完整 key

const PROVIDER_DEFAULTS = {
  deepseek: { base_url: "https://api.deepseek.com",                   model: "deepseek-chat" },
  openai:   { base_url: "https://api.openai.com/v1",                  model: "gpt-4o-mini" },
  kimi:     { base_url: "https://api.moonshot.cn/v1",                 model: "moonshot-v1-128k" },
  zhipu:    { base_url: "https://open.bigmodel.cn/api/paas/v4",       model: "glm-4-flash" },
};

function isOwnerAuthed(req, env) {
  const pin = req.headers.get("x-curio-owner-pin") || "";
  return env.OWNER_PIN && pin === env.OWNER_PIN;
}

function maskKey(k) {
  if (!k || typeof k !== "string") return "";
  if (k.length <= 12) return k.slice(0, 2) + "***";
  return k.slice(0, 6) + "..." + k.slice(-4);
}

async function handleLLMGet(req, env) {
  if (!isOwnerAuthed(req, env)) return errorJson("unauthorized (owner pin)", 401);
  const cfg = await env.CURIO_KV.get("llm:owner", "json");
  // 单独存的 scoring_mode（即使没配 api 也可设）
  const mode = (await env.CURIO_KV.get("scoring:mode")) || "local";
  if (!cfg) return json({ ok: true, configured: false, scoring_mode: mode });
  return json({
    ok: true,
    configured: true,
    provider: cfg.provider,
    model: cfg.model,
    base_url: cfg.base_url,
    key_masked: maskKey(cfg.api_key),
    updated_at: cfg.updated_at,
    scoring_mode: mode,
  });
}

async function handleLLMSet(req, env) {
  if (!isOwnerAuthed(req, env)) return errorJson("unauthorized (owner pin)", 401);
  let body;
  try { body = await req.json(); } catch { return errorJson("invalid json"); }

  // 单独保存 scoring_mode（local / api / off），不依赖 api 配置
  const incomingMode = (body.scoring_mode || "").trim();
  if (incomingMode && ["local", "api", "off"].includes(incomingMode)) {
    await env.CURIO_KV.put("scoring:mode", incomingMode);
  }

  // 如果 body 里只想改 mode 而没传 api_key，就只改 mode 直接返回
  const provider = (body.provider || "").toLowerCase();
  const api_key = (body.api_key || "").trim();
  if (!api_key && !provider) {
    const finalMode = (await env.CURIO_KV.get("scoring:mode")) || "local";
    const existing = await env.CURIO_KV.get("llm:owner", "json");
    return json({
      ok: true,
      scoring_mode: finalMode,
      configured: !!existing,
      key_masked: existing ? maskKey(existing.api_key) : "",
    });
  }

  const model = (body.model || "").trim();
  const base_url = (body.base_url || "").trim();
  if (!provider || !PROVIDER_DEFAULTS[provider]) return errorJson("provider must be one of: " + Object.keys(PROVIDER_DEFAULTS).join(","));
  if (!api_key || api_key.length < 10) return errorJson("api_key required (min 10 chars)");

  const finalCfg = {
    provider,
    model: model || PROVIDER_DEFAULTS[provider].model,
    base_url: base_url || PROVIDER_DEFAULTS[provider].base_url,
    api_key,
    updated_at: new Date().toISOString(),
  };
  await env.CURIO_KV.put("llm:owner", JSON.stringify(finalCfg));
  const finalMode = (await env.CURIO_KV.get("scoring:mode")) || "local";
  return json({
    ok: true,
    provider: finalCfg.provider,
    model: finalCfg.model,
    base_url: finalCfg.base_url,
    key_masked: maskKey(finalCfg.api_key),
    scoring_mode: finalMode,
  });
}

async function handleLLMDelete(req, env) {
  if (!isOwnerAuthed(req, env)) return errorJson("unauthorized (owner pin)", 401);
  await env.CURIO_KV.delete("llm:owner");
  return json({ ok: true });
}

async function handleLLMTest(req, env) {
  if (!isOwnerAuthed(req, env)) return errorJson("unauthorized (owner pin)", 401);
  let body;
  try { body = await req.json(); } catch { body = {}; }
  // 允许临时传 api_key/provider/model 测试一组未保存的配置
  let cfg = null;
  if (body.api_key && body.provider) {
    const p = (body.provider || "").toLowerCase();
    if (!PROVIDER_DEFAULTS[p]) return errorJson("provider invalid");
    cfg = {
      provider: p,
      model: body.model || PROVIDER_DEFAULTS[p].model,
      base_url: body.base_url || PROVIDER_DEFAULTS[p].base_url,
      api_key: body.api_key,
    };
  } else {
    cfg = await env.CURIO_KV.get("llm:owner", "json");
    if (!cfg) return errorJson("no llm config and no api_key in body");
  }
  const t0 = Date.now();
  try {
    const r = await fetch(cfg.base_url.replace(/\/$/, "") + "/chat/completions", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "authorization": "Bearer " + cfg.api_key,
        "user-agent": "curio-llm-test/1.0",
      },
      body: JSON.stringify({
        model: cfg.model,
        messages: [
          { role: "system", content: "Reply with one Chinese word only." },
          { role: "user", content: "ping" },
        ],
        max_tokens: 8,
        temperature: 0,
      }),
    });
    const dt = Date.now() - t0;
    const text = await r.text();
    let parsed = null;
    try { parsed = JSON.parse(text); } catch {}
    if (!r.ok) {
      return json({ ok: false, status: r.status, latency_ms: dt, error: text.slice(0, 400) });
    }
    const reply = parsed?.choices?.[0]?.message?.content || "";
    return json({ ok: true, status: r.status, latency_ms: dt, reply: reply.slice(0, 80) });
  } catch (e) {
    return json({ ok: false, error: String(e && e.message || e) });
  }
}

// 给 CI（GitHub Actions）拉完整 LLM 配置用：用 ADMIN_TOKEN 鉴权
async function handleAdminLLMConfig(req, env) {
  if (!isAdminAuthed(req, env)) return errorJson("unauthorized", 401);
  const cfg = await env.CURIO_KV.get("llm:owner", "json");
  const mode = (await env.CURIO_KV.get("scoring:mode")) || "local";
  if (!cfg) {
    // 没配 api_key 也允许 CI 拿到 mode（local 时 CI 应该 skip）
    return json({ ok: true, configured: false, scoring_mode: mode });
  }
  return json({ ok: true, configured: true, scoring_mode: mode, ...cfg });
}

async function handleBroadcast(req, env) {
  if (!isAdminAuthed(req, env)) return errorJson("unauthorized", 401);
  let body;
  try { body = await req.json(); } catch { return errorJson("invalid json"); }
  const { cadence, dry_run } = body || {};
  if (!isValidCadence(cadence)) return errorJson("cadence required (daily|weekly)");

  // 列出所有订阅者
  const list = await env.CURIO_KV.list({ prefix: "subscriber:" });
  let sent = 0, skipped = 0, failed = 0;
  const errors = [];

  // 加载 domains 元数据用来在邮件底部显示中文名
  const domainsMeta = (await env.CURIO_KV.get("domains:meta", "json")) || {};
  const displayName = (slug) => (domainsMeta[slug] && domainsMeta[slug].name) || slug;

  const dateStr = new Date().toISOString().slice(0, 10);
  const force = !!body.force;  // POST 时传 force:true 可绕过去重（手动想强发）

  for (const k of list.keys) {
    const sub = await env.CURIO_KV.get(k.name, "json");
    if (!sub) continue;
    if (sub.cadence !== cadence) { skipped++; continue; }

    // 去重：同一日期 + 同一 cadence 同一邮箱，24h 内只发 1 次（绕过用 force:true）
    const dedupKey = `sent:${sub.email}:${cadence}:${dateStr}`;
    if (!force && !dry_run) {
      const already = await env.CURIO_KV.get(dedupKey);
      if (already) { skipped++; continue; }
    }

    // 拉每个域的内容
    const blocks = [];
    for (const d of sub.domains) {
      const c = await env.CURIO_KV.get("content:" + d + ":latest", "json");
      if (c && c.html) blocks.push(c.html);
    }
    if (blocks.length === 0) { skipped++; continue; }

    const unsubUrl = `${env.API_BASE}/unsubscribe?token=${sub.unsub_token}`;
    const subject = `📰 Curio · ${dateStr} · ${cadence === "daily" ? "今日简报" : "本周简报"}`;
    const html = `<!doctype html><html><body style="font-family:-apple-system,system-ui,sans-serif;max-width:680px;margin:0 auto;padding:24px;color:#1a1a1c;line-height:1.6">
<h1 style="border-bottom:2px solid #d4af37;padding-bottom:8px">📰 Curio · ${dateStr}</h1>
${blocks.join('<hr style="border:none;border-top:1px solid #ddd;margin:32px 0">')}
<hr style="border:none;border-top:1px solid #ddd;margin:32px 0">
<p style="font-size:12px;color:#888">
  你正在订阅 ${sub.domains.map(displayName).join("、")}（${cadence === "daily" ? "日报" : "周刊"}）<br>
  <a href="${unsubUrl}" style="color:#888">退订</a> · <a href="${env.SITE_BASE}/" style="color:#888">访问 Curio 网站</a>
</p>
</body></html>`;

    if (dry_run) { sent++; continue; }
    const r = await sendEmail(env, { to: sub.email, subject, html, text: `查看网页版：${env.SITE_BASE}/` });
    if (r.ok) {
      sent++;
      // 写去重 key（48 小时过期）
      await env.CURIO_KV.put(dedupKey, "1", { expirationTtl: 172800 });
    }
    else { failed++; errors.push({ email: sub.email, error: r.body.slice(0, 200) }); }
  }
  return json({ ok: true, sent, skipped, failed, errors });
}

async function handleRoot(req, env) {
  return htmlPage(
    "Curio API",
    `<h1>Curio API</h1>
     <p>这是 Curio 的后端 API（Cloudflare Workers）。</p>
     <p>访问主站：<a class="btn" href="${env.SITE_BASE}/">${env.SITE_BASE}</a></p>`,
  );
}

// ============== router ==============

export default {
  async fetch(req, env) {
    const url = new URL(req.url);

    // CORS preflight
    if (req.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: {
          "access-control-allow-origin": "*",
          "access-control-allow-methods": "GET,POST,DELETE,OPTIONS",
          "access-control-allow-headers": "content-type, authorization, x-curio-owner-pin",
          "access-control-max-age": "86400",
        },
      });
    }

    try {
      if (url.pathname === "/" || url.pathname === "") {
        return handleRoot(req, env);
      }
      if (url.pathname === "/health") {
        return json({ ok: true, ts: Date.now() });
      }
      if (url.pathname === "/subscribe" && req.method === "POST") {
        return handleSubscribe(req, env);
      }
      if (url.pathname === "/confirm" && req.method === "GET") {
        return handleConfirm(req, env);
      }
      if (url.pathname === "/unsubscribe" && req.method === "GET") {
        return handleUnsubscribe(req, env);
      }
      if (url.pathname === "/unsubscribe-by-email") {
        return handleUnsubscribeByEmail(req, env);
      }
      if (url.pathname === "/domains" && req.method === "GET") {
        return handleDomains(req, env);
      }
      if (url.pathname === "/admin/sync-domains" && req.method === "POST") {
        return handleAdminSyncDomains(req, env);
      }
      if (url.pathname === "/admin/push-content" && req.method === "POST") {
        return handleAdminPushContent(req, env);
      }
      if (url.pathname === "/admin/unsubscribe-domain" && req.method === "POST") {
        return handleAdminUnsubscribeDomain(req, env);
      }
      if (url.pathname === "/broadcast" && req.method === "POST") {
        return handleBroadcast(req, env);
      }
      if (url.pathname === "/trigger-generate" && req.method === "POST") {
        return handleTriggerGenerate(req, env);
      }
      // BYOK · 网页设置弹窗用（鉴权用 OWNER_PIN）
      if (url.pathname === "/llm/config" && req.method === "GET") {
        return handleLLMGet(req, env);
      }
      if (url.pathname === "/llm/config" && req.method === "POST") {
        return handleLLMSet(req, env);
      }
      if (url.pathname === "/llm/config" && req.method === "DELETE") {
        return handleLLMDelete(req, env);
      }
      if (url.pathname === "/llm/test" && req.method === "POST") {
        return handleLLMTest(req, env);
      }
      // 公开端点：只返回当前 scoring_mode（不返回 api_key），用于主页文案动态切换
      if (url.pathname === "/scoring-mode" && req.method === "GET") {
        const mode = (await env.CURIO_KV.get("scoring:mode")) || "local";
        return json({ ok: true, scoring_mode: mode });
      }
      // BYOK · CI 拉完整配置（用 ADMIN_TOKEN）
      if (url.pathname === "/admin/llm-config" && req.method === "GET") {
        return handleAdminLLMConfig(req, env);
      }
      return errorJson("not found: " + url.pathname, 404);
    } catch (e) {
      return errorJson("server error: " + (e && e.message), 500);
    }
  },
};
