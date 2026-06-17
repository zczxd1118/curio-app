# Curio · AI · 2026-06-17

> 今日 1 条头条 + 2 条备选

_今日核心信号：SpaceX 上市后即以 60B 美元收购 AI 编程工具 Cursor，标志着 AI 编程赛道进入巨头整合期；同时英伟达 B200 租赁价翻倍、AMD 收购 MEXT 打破内存墙，算力成本结构性上升。你的 content-curator 项目应关注 Cursor 被收购后的生态变化，以及 MCP/Skills 等工具链的工程实践。_

---

## 🌟 今日精选

### 5. 开源免费：用 Cloudflare Tunnel 将本地电脑变成公网服务器，AI Agent 可远程访问

**[AI]** · ⭐⭐⭐⭐ · _小宇Boi_

一个名为 cloudflare-tunnel-skill 的开源项目，让你通过 Cloudflare 的隧道技术将本地电脑暴露为公网服务器，无需公网 IP 或域名。该 Skill 可以直接发给 AI Agent（如 Claude Code），让它自动配置并部署。这意味着你可以让 AI Agent 直接访问你本地的开发环境、数据库或 API，实现远程协作。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 开源项目 cloudflare-tunnel-skill，基于 Cloudflare Tunnel | 安全风险——暴露本地端口可能被恶意利用 |
| 支持临时和长期部署，临时部署随机分配域名 | Cloudflare 的免费额度限制（带宽和请求数） |
| 可直接发给 AI Agent 自动配置 | 与 ngrok、Tailscale 等现有方案的比较 |
| 免费使用，无需服务器 | 对 AI Agent 工作流的实际提升——是否值得增加安全复杂度 |

**📖 主编点评**

这个 Skill 直接解决了你 content-curator 项目的一个痛点：如何让 AI Agent 访问本地资源。建议：1）在项目中集成这个 Skill，让 Agent 可以自动部署隧道并访问本地数据库或文件系统；2）注意安全配置，只暴露必要端口并添加认证；3）结合你的 MCP 实践，让 Agent 通过 MCP 协议安全地调用本地工具。

📺 [打开原文](http://www.bilibili.com/video/av116734778480044)

---

## 📋 备选阅读

- [零基础 Vibe Coding 教程：Claude Code + Codex + Cursor 实战](http://www.bilibili.com/video/av116711944620974) —— 尚硅谷出品的系统化 Vibe Coding 教程，从零开始用自然语言指挥 AI 开发真实项目，适合你的 content-curator 项目参考。
  _尚硅谷_
- [使用 Rust 开发 AI Agent - 简介](http://www.bilibili.com/video/av116724259232762) —— 从零开始用 Rust 搭建 AI Agent，适合想深入底层实现的学习者，但 Rust 学习曲线较陡。
  _软件工艺师_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
