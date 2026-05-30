# content-curator

> 个人 AI 信息策展 Agent —— **你给一个领域，Agent 自己决定订阅谁、推什么**。

## 与 content-catcher 的关系

| | content-catcher（已有）| content-curator（本项目）|
|---|---|---|
| 层级 | Level 1 工具 | **Level 2 Agent** |
| 输入 | URL / mid | **主题关键词** |
| 决策者 | 用户 | **AI** |

content-curator 是 content-catcher 的"大脑"——AI 决定订什么，工具负责抓取和送达。

## M0：人机协作环路

### 一、给一个主题，生成 prompt

```bash
python curator.py topic "vibe coding"
```

脚本会打印一段 prompt。把它复制贴回 WorkBuddy 对话框，AI 会返回结构化 KOL JSON。

### 二、把 AI 输出的 JSON 存盘

把 ```json...``` 代码块内的 JSON 保存到 `raw.json`。

### 三、格式化成 KOL 报告

```bash
python curator.py ingest raw.json --topic "vibe coding"
```

输出到 `topics/vibe-coding.md`，包含：
- 子话题拆解
- 按平台分组的 KOL 卡片（含信任度、推荐理由、ID 置信度）
- 用户勾选区（M1 会读这个勾选写 channels.yaml）

## 路线图

| 阶段 | 目标 | 状态 |
|---|---|---|
| **M0** | 主题 → KOL Markdown 报告（人机协作）| 🚧 进行中 |
| M1 | 勾选 → channels.yaml + 跑订阅 | 待启动 |
| M2 | 内容打分 + 周报"为什么推荐" | 待启动 |
| M3 | 打磨 + 写故事 | 待启动 |

## 项目结构

```
content-curator/
├── PRD.md                     ← 产品文档
├── README.md                  ← 本文件
├── curator.py                 ← M0 CLI 入口
├── prompts/
│   └── topic_to_kols.md       ← Prompt 模板（核心资产）
├── agent/                     ← M1+ Python 模块
└── topics/                    ← 输出的策展报告
    └── vibe-coding.md         ← M0 首次产物
```
