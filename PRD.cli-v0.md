# content-curator —— 个人 AI 信息策展 Agent

> **版本**：v0.1
> **作者**：周小丁
> **日期**：2026-05-29
> **状态**：M0 进行中
> **依赖**：content-catcher（工具底座，已完成）

---

## 一句话定位

> **你给一个领域，Agent 自己决定订阅谁、推什么、什么时候推。**

不是工具（你给指令它执行），而是 Agent（你给目标它自主决策）。

---

## M0 决策记录（2026-05-29）

| 项 | 选定方案 |
|---|---|
| 项目路径 | `/Users/zoezczhou/WorkBuddy/2026-05-29-15-27-22/content-curator/` |
| Agent 大脑 | WorkBuddy（人机协作）|
| Demo 形态 | curator.py + 人机协作环路 |
| Prompt 模板位置 | `prompts/topic_to_kols.md` |
| M0 产物 | `topics/vibe-coding.md`（首个真实主题验证）|

### 核心架构（M0）

```
用户：python curator.py topic "vibe coding"
  ↓
脚本：读取 prompts/topic_to_kols.md，注入主题，打印完整 prompt
  ↓
用户：把 prompt 贴到 WorkBuddy 对话框
  ↓
WorkBuddy（大脑）：用 WebSearch + 知识 → 输出结构化 KOL JSON
  ↓
用户：python curator.py ingest <json> --topic "vibe coding"
  ↓
脚本：JSON → 格式化成 topics/vibe-coding.md（含子话题、KOL 卡片、推荐理由）
  ↓
M1：把这份 md 转成 channels.yaml，喂给 content-catcher
```

### 里程碑

| 阶段 | 目标 |
|---|---|
| **M0** ← 当前 | 主题 → KOL Markdown 报告（人机协作环路）|
| M1 | KOL → channels.yaml 自动生成 + 跑订阅 |
| M2 | 内容打分 + 周报"为什么推荐" |
| M3 | 打磨 + 写故事 |

---

## 完整 PRD（参考）

详见 `/Users/zoezczhou/WorkBuddy/2026-05-27-15-46-19/content-curator/PRD.md`，已在新对话延续。
