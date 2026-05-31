# Curio · 大厂讯息 简报

**2026-05-31 · 由 Curio 主编从候选中选出**

---

## 📰 主编社论

本期（2026-05-31）大厂主旋律：Google 全方位收紧——静默下 4GB AI 模型、封锁去 Google 化设备、撤回 on-device 隐私承诺、Antigravity 编辑器闭源。同时 DOJ 对 Apple/Google 发出 10 万人级数据传票。开发者和隐私社区对 Google 的信任在迅速损耗。

---

## 🗞️ 头版报道（6 条）

### 1. Google Chrome silently installs a 4 GB AI model on your device without consent

**来源**：HN · Google · hackernews

_原标题：Google Chrome silently installs a 4 GB AI model on your device without consent_

**📖 主编点评**

Chrome 在用户毫不知情的情况下静默下载 4GB on-device AI 模型，占用磁盘 + 网络。即使是企业管理的设备也照下不误。这是大厂 AI 部署 vs 用户知情权的最新冲突。如果你管理一批 Mac 或在企业 IT 环境里，建议立刻看 chrome://components 看是否已经被默默装了。

📺 [打开原文](https://news.ycombinator.com/item?id=chrome-4gb-ai)

---

### 2. Google broke reCAPTCHA for de-googled Android users

**来源**：HN · Google · hackernews

_原标题：Google broke reCAPTCHA for de-googled Android users_

**📖 主编点评**

用 GrapheneOS / LineageOS 的用户突然发现 reCAPTCHA 在他们设备上不通过。Google 在用'设备可信度'筛选用户——你不用主流 OS 就被认定为风险。如果你关心数字主权和反平台锁定，这是一记警钟：'能访问主流网站'这件事正在被绑定到'使用主流 OS'上。

📺 [打开原文](https://news.ycombinator.com/item?id=recaptcha-degoogled)

---

### 3. DuckDuckGo search saw 28% more visits after Google said people love AI mode

**来源**：HN · 搜索 · hackernews

_原标题：DuckDuckGo search saw 28% more visits after Google said people love AI mode_

**📖 主编点评**

Google 在搜索结果顶部强推 AI Mode 之后，DuckDuckGo 访问量涨了 28%。这是搜索市场份额自 2010 年以来最明显的一次松动。对持仓 GOOGL 或关注搜索广告业务的人，这条不是噪音——它说明 Google 对搜索的控制力第一次出现可量化的裂缝。

📺 [打开原文](https://news.ycombinator.com/item?id=ddg-28)

---

### 4. Google's Antigravity bait and switch

**来源**：HN · Google · hackernews

_原标题：Google's Antigravity bait and switch_

**📖 主编点评**

Google Antigravity（AI 代码编辑器）原本免费开放使用，最近改成付费 + 闭源。开发者社区炸了。这是大厂 AI 工具最常见的剧本：先免费抢用户，后开始收割。如果你在团队里推过 Antigravity，这条说明现在该评估替代方案了——Cursor / Claude Code / Windsurf 都是更稳定的选择。

📺 [打开原文](https://news.ycombinator.com/item?id=antigravity)

---

### 5. U.S. DOJ demands Apple and Google unmask over 100k users of car-tinkering app

**来源**：HN · DOJ · hackernews

_原标题：U.S. DOJ demands Apple and Google unmask over 100k users of car-tinkering app_

**📖 主编点评**

美国司法部要求 Apple 和 Google 上交一个汽车改装 App 的 10 万+ 用户身份。这条是平台-政府数据请求的边界事件——以前都是个案传票，这次是大规模批量。如果你做隐私敏感的 App 或在合规岗位，这条说明'平台拒绝合作'的成本正在快速上升。

📺 [打开原文](https://news.ycombinator.com/item?id=doj-car-app)

---

### 6. Chrome removes claim of On-device AI not sending data to Google Servers

**来源**：HN · Google · hackernews

_原标题：Chrome removes claim of On-device AI not sending data to Google Servers_

**📖 主编点评**

Chrome 悄悄删除了'设备端 AI 不会向 Google 服务器发送数据'的承诺文案。结合上面那条 4GB 模型静默安装看，整套故事是一致的：Google 在为 on-device AI 的数据回流留口子。如果你给企业或政府做合规咨询，这条是 Chrome 在企业环境里需要重新评估的信号。

📺 [打开原文](https://news.ycombinator.com/item?id=chrome-claim)

---

## 📑 参考阅读

- **Googlebook** — Google 内部文化批评长文。
- **Google Cloud Fraud Defence is just WEI repackaged** — Web Environment Integrity 死灰复燃换皮。
- **Google changes its search box** — Google 搜索框 UI 改版，老用户吐槽。
- **Google Declaring War on the Web** — 评论员长文：Google 与开放 Web 的关系恶化。
- **Incident Report: Railway Blocked by Google Cloud** — Railway（PaaS）被 Google Cloud 误封事件后续。
