/* =========================================================
   M0 mock data —— 严格对齐 PRD v0.2 数据模型
   3 Domain × 9 Topic × KOL × Content × 1 Profile × Digest
   ========================================================= */

window.MOCK = {
  profile: {
    id: "me",
    identity: "电子信息工程大四 + 搜狗实习生 + AI 重度用户",
    name: "周小丁",
    role: "学生 / 实习产品助理",
    interests: [
      "vibe coding",
      "AI Agent",
      "美联储动向",
      "半导体国产替代",
      "个股研究",
    ],
    dislikes: ["纯流量号", "标题党", "口水内容"],
    signal_preferences: [
      "要工程实践细节",
      "要看到代码 / 示例",
      "拒绝玄学论调",
    ],
    reading_pace: "工作日 30 分钟 · 周末 2 小时",
    auto_updated_from_feedback: true,
    feedback_timeline: [
      { date: "2026-05-29", text: "想多看 Claude Code 实战，少看抽象方法论" },
      { date: "2026-05-22", text: "半导体太多概念股，想多看技术演进" },
      { date: "2026-05-15", text: "美联储口径解读已饱和，少推" },
    ],
  },

  domains: [
    {
      id: "ai", name: "AI", icon: "🤖",
      description: "vibe coding · 大模型 · AI 工程",
      source: "preset", color: "#6e8efb",
      frequency: "weekly",
      topic_ids: ["vibe-coding", "llm-eval", "ai-engineering"],
      kol_count: 12, content_count: 22, unread: 3,
    },
    {
      id: "finance", name: "金融", icon: "🏦",
      description: "宏观 · 股票 · 投资策略",
      source: "preset", color: "#f5b942",
      frequency: "daily",
      topic_ids: ["macro-fed", "hk-us-stocks", "a-stocks"],
      kol_count: 8, content_count: 15, unread: 5,
    },
    {
      id: "semiconductor", name: "半导体", icon: "🔬",
      description: "制程 · GPU · 国产替代",
      source: "preset", color: "#8b5cf6",
      frequency: "weekly",
      topic_ids: ["advanced-process", "gpu-compute", "china-substitute"],
      kol_count: 6, content_count: 12, unread: 2,
    },
  ],

  topics: {
    "vibe-coding": {
      id: "vibe-coding", name: "Vibe Coding", domain_id: "ai",
      description: "AI 编程助手实战与工作流",
      subtopics: ["Claude Code", "Cursor / Windsurf", "Side Project", "Agent 工具"],
      frequency: "inherit", kol_count: 5, content_count: 8,
    },
    "llm-eval": {
      id: "llm-eval", name: "大模型评测", domain_id: "ai",
      description: "新模型对比与基准测试",
      subtopics: ["GPT-5 / Claude 4", "推理评测", "中文场景"],
      frequency: "inherit", kol_count: 3, content_count: 6,
    },
    "ai-engineering": {
      id: "ai-engineering", name: "AI 工程实践", domain_id: "ai",
      description: "RAG / Agent / 部署落地",
      subtopics: ["RAG 优化", "Agent 框架", "推理优化"],
      frequency: "inherit", kol_count: 4, content_count: 8,
    },

    "macro-fed": {
      id: "macro-fed", name: "宏观与美联储", domain_id: "finance",
      description: "议息会议、CPI、就业数据",
      subtopics: ["议息会议", "CPI", "就业数据", "美元指数"],
      frequency: "inherit", kol_count: 3, content_count: 5,
    },
    "hk-us-stocks": {
      id: "hk-us-stocks", name: "港美股研究", domain_id: "finance",
      description: "中概 / 美科技 / 港股",
      subtopics: ["中概", "美科技", "港股"],
      frequency: "inherit", kol_count: 3, content_count: 6,
    },
    "a-stocks": {
      id: "a-stocks", name: "A股投资策略", domain_id: "finance",
      description: "板块轮动 + 个股研究",
      subtopics: ["板块轮动", "个股研究", "题材"],
      frequency: "inherit", kol_count: 2, content_count: 4,
    },

    "advanced-process": {
      id: "advanced-process", name: "先进制程", domain_id: "semiconductor",
      description: "3nm / 2nm / Chiplet",
      subtopics: ["3nm/2nm", "Chiplet", "EUV"],
      frequency: "inherit", kol_count: 2, content_count: 4,
    },
    "gpu-compute": {
      id: "gpu-compute", name: "GPU 与算力", domain_id: "semiconductor",
      description: "Nvidia · AMD · 算力卡",
      subtopics: ["Nvidia", "AMD", "云算力"],
      frequency: "inherit", kol_count: 2, content_count: 5,
    },
    "china-substitute": {
      id: "china-substitute", name: "国产替代", domain_id: "semiconductor",
      description: "国产 GPU / 设备 / 材料",
      subtopics: ["国产 GPU", "设备", "材料"],
      frequency: "inherit", kol_count: 2, content_count: 3,
    },
  },

  // Dashboard 本周精选（按 domain 分组）
  must_read_by_domain: {
    ai: [
      { id: "c-001", title: "Claude Code 1.0 实战：5 个新指令完整演示",
        kol: "大牙大-", platform: "B站", duration: "32:14", topic: "vibe-coding" },
      { id: "c-002", title: "Cursor 0.50 vs Windsurf 1.0 深度对比",
        kol: "Matthew Berman", platform: "YouTube", duration: "18:42", topic: "vibe-coding" },
      { id: "c-003", title: "Latent Space 访谈：swyx 谈 vibe coding 的下一步",
        kol: "Latent Space", platform: "Podcast", duration: "1:12:00", topic: "vibe-coding" },
    ],
    finance: [
      { id: "c-101", title: "5 月 FOMC 会议纪要逐句解读",
        kol: "付鹏", platform: "Podcast", duration: "45:00", topic: "macro-fed" },
      { id: "c-102", title: "Nvidia Q1 财报会议 PCE 数据传导路径",
        kol: "投资者老李", platform: "B站", duration: "22:30", topic: "hk-us-stocks" },
    ],
    semiconductor: [
      { id: "c-201", title: "TSMC 2nm 量产时间表与中芯国际差距",
        kol: "芯东西", platform: "B站", duration: "16:08", topic: "advanced-process" },
      { id: "c-202", title: "黄仁勋 Computex 2026 主旨演讲完整版",
        kol: "Nvidia", platform: "YouTube", duration: "1:30:00", topic: "gpu-compute" },
    ],
  },

  // 跨 Domain 提示
  cross_hints: {
    ai: [
      { domain_id: "finance", text: "金融 Domain 今日有 5 条必读", icon: "🏦" },
      { domain_id: "semiconductor", text: "半导体 Domain 本周有 2 条新内容", icon: "🔬" },
    ],
    finance: [
      { domain_id: "ai", text: "AI Domain 本周有 3 条必读", icon: "🤖" },
    ],
    semiconductor: [
      { domain_id: "ai", text: "AI Domain 本周有 3 条必读", icon: "🤖" },
    ],
  },

  // 最新 Digest 入口
  latest_digest_by_domain: {
    ai: { id: "2026-W22-ai", label: "AI · 周报 2026-W22", period: "5 月 25 日 - 5 月 31 日", frequency: "weekly" },
    finance: { id: "2026-05-29-finance", label: "金融 · 日报 5 月 29 日", period: "今日盘前", frequency: "daily" },
    semiconductor: { id: "2026-W22-semiconductor", label: "半导体 · 周报 2026-W22", period: "5 月 25 日 - 5 月 31 日", frequency: "weekly" },
  },
};
