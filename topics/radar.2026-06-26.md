# Curio 趋势雷达 · 2026-06-26

> 你的私人主编 · 今日跨域精选 5 条头条 + 13 条备选

_今日全球科技市场遭遇剧烈震荡：内存涨价潮引发苹果、微软、Xbox 全线提价，亚洲芯片股暴跌，韩股熔断。与此同时，AI 领域多线并进——OpenAI 的 GPT-5.6 因白宫要求推迟发布，Anthropic 指控阿里大规模蒸馏 Claude，Qualcomm 发布 HBC 近存计算架构。存储超级周期共识空前强烈，但终端需求反噬风险已现。_

---

## 🌟 AI

### 1. Anthropic 指控阿里用 2.5 万假账号、2880 万次对话蒸馏 Claude，要求严惩

**[AI]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Anthropic 公开指控阿里巴巴在 2026 年 4 月至 6 月期间，通过 25,000 个虚假账户与 Claude 进行了 2880 万次交互，系统性地蒸馏模型能力用于训练自家 AI。Anthropic 称此举违反服务条款，且发生在特朗普政府加强对华 AI 技术管控的背景下，要求追究责任。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 追踪到 25,000 个虚假账户，产生 2,880 万次 API 调用 | 阿里是否将蒸馏成果用于其通义千问系列模型尚未确认 |
| 蒸馏活动集中在 2026 年 4 月至 6 月 | 美国政府是否会采取实质性制裁仍不确定 |
| Anthropic 已向美国政府通报此事 | 蒸馏对 Claude 模型性能的具体影响程度未知 |
| 阿里此前曾因类似行为被多家 AI 公司警告 | 阿里可能辩称这是常规的模型评估行为 |

**📖 主编点评**

这是 AI 领域迄今规模最大的模型蒸馏攻击事件。如果你在用 Claude API 做产品，建议关注 Anthropic 是否会加强反爬和速率限制，提前规划备用模型。同时，这起事件可能加速美国对华 AI 技术出口管制升级，影响国内开发者获取前沿模型的渠道。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude)

---

## 🌟 AI 算力 / 半导体

### 2. Qualcomm 发布 HBC 近存计算架构，AI250/AI350 加速器能效比 HBM 高 6 倍

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Qualcomm 在数据中心日上公布了全新的 HBC（Hybrid Bonded Capacitor）近存计算架构，以及基于该架构的 AI250 和 AI350 推理加速器。官方宣称 HBC 的带宽功耗比是 HBM 的 6 倍，容量可达片上 SRAM 的 200 倍，旨在打破 AI 推理的“内存墙”。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| HBC 架构采用混合键合电容技术，实现近存计算 | 实际量产时间和客户导入计划未公布 |
| AI250 和 AI350 两款加速器面向数据中心推理场景 | 与 NVIDIA 和 AMD 现有产品的性能对比数据缺失 |
| 带宽功耗比是 HBM 的 6 倍 | HBC 技术的良率和成本尚未披露 |
| 容量是片上 SRAM 的 200 倍 | Qualcomm 在数据中心领域缺乏生态积累 |

**📖 主编点评**

Qualcomm 这次不是小打小闹——HBC 架构如果落地，可能改变 AI 推理芯片的竞争格局。对做 AI 部署的你来说，这意味着未来可能有更省电、更便宜的推理方案。但 Qualcomm 数据中心执行力存疑，建议保持关注但不要押注，等首批客户测试结果。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-reveals-hbc-near-memory-ai-architecture-ai250-and-ai350-accelerators-touts-6x-higher-bandwidth-per-watt-compared-to-hbm-200x-capacity-compared-to-on-chip-sram)

---

### 5. OpenAI 与 Broadcom 发布推理芯片 Jalapeño，更值得关注的是其芯片设计 AI

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _EE Times_

OpenAI 与 Broadcom 联合发布了名为 Jalapeño 的定制推理加速器，但 EE Times 分析认为，真正有长期影响的是 OpenAI 在芯片设计过程中使用的 AI 自动化工具——它可能改变芯片设计行业本身。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Jalapeño 是 OpenAI 与 Broadcom 合作的定制推理芯片 | Jalapeño 的性能指标尚未公开 |
| 芯片设计过程中使用了 AI 自动化工具 | AI 设计工具的具体能力边界不明确 |
| Jalapeño 针对 LLM 推理场景优化 | 与 NVIDIA 现有产品的性价比对比未知 |
| OpenAI 计划大规模部署该芯片 | 芯片量产时间和成本未披露 |

**📖 主编点评**

OpenAI 造芯片本身不意外，但用 AI 设计芯片这件事值得你关注。如果你做 AI 工程，这意味着未来芯片设计工具可能成为新的 AI 应用方向。短期内，Jalapeño 对普通开发者影响有限，但长期看，AI 驱动的芯片设计可能降低定制芯片门槛。

📺 [打开原文](https://www.eetimes.com/openai-jalapeno-will-be-spicy-but-the-real-sizzle-is-its-chip-design-ai/)

---

## 🌟 大厂 AI 动态

### 3. 白宫要求 OpenAI 推迟 GPT-5.6 发布，仅限合作伙伴内测

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _The Verge_

据 The Information 报道，特朗普政府出于安全顾虑，要求 OpenAI 推迟 GPT-5.6 的公开上线。OpenAI CEO Sam Altman 同意将模型先向有限合作伙伴开放，而非全面发布。这标志着美国政府首次直接干预大模型发布节奏。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 白宫以安全为由要求 OpenAI 推迟 GPT-5.6 公开发布 | 推迟时间长度未公布，可能为数周至数月 |
| OpenAI 同意改为向精选合作伙伴先行开放 | 合作伙伴名单和评估标准未披露 |
| GPT-5.6 是 GPT-5 系列的增量更新版本 | GPT-5.6 的具体能力提升细节尚未公开 |
| 这是美国政府首次直接要求 AI 公司推迟模型发布 | 此举是否会成为未来大模型发布的常态尚不确定 |

**📖 主编点评**

政府介入模型发布节奏是全新信号。如果你依赖 OpenAI 的最新模型做产品，需要为不确定性做好准备——考虑多模型备份方案。同时，这可能会让更多开发者转向开源模型或 Anthropic 等替代方案。

📺 [打开原文](https://www.theverge.com/ai-artificial-intelligence/957372/openai-will-delay-gpt-5-6-after-trump-administration-request)

---

## 🌟 金融

### 4. 内存涨价反噬终端需求：苹果涨价 + OpenAI IPO 推迟引爆亚洲芯片股崩盘

**[金融]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

苹果和微软因存储短缺同日宣布涨价，叠加 OpenAI 考虑推迟 IPO 的消息，周五亚洲科技股遭猛烈抛售。韩股一度重挫近 9% 触发熔断，日经 225 跌约 5%，软银暴跌 14%。市场开始重新评估：内存涨价带来的芯片利润扩张，是否正在以压制终端消费为代价？

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 苹果 Mac/iPad 全线涨价，最高涨幅 $500 | 存储涨价是否已到拐点尚未可知 |
| 微软 Xbox 系列第三次涨价，涨幅 $100-$150 | 终端需求萎缩是否会倒逼芯片降价仍不确定 |
| OpenAI 考虑推迟 IPO | OpenAI IPO 推迟的具体原因和时长未确认 |
| 韩股触发熔断，日经 225 跌 5%，软银跌 14% | 亚洲科技股回调幅度是否过度需观察 |

**📖 主编点评**

存储超级周期正在从利好芯片厂转向压制终端消费。如果你在考虑买新电脑或服务器，现在不是好时机——价格还在涨。对做 AI 项目的你，硬件成本上升可能影响部署预算，建议优先优化模型效率而非堆硬件。

📺 [打开原文](https://wallstreetcn.com/articles/3775589)

---

## 📋 备选池

### AI

- [Stratechery 创始人 Ben Thompson 的 Vibe Coding 实战总结：10 条 takeaways](https://stratechery.com/2026/my-vibe-coding-adventure-the-app-and-the-experience-ten-takeaways/) —— 深度长文，从真实项目出发总结 vibe coding 经验，比教程更有洞察，适合想认真用 AI 编程的你。
  _Stratechery_
- [Patronus AI 获 5000 万美元融资，构建“数字世界”压力测试 AI Agent](https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/) —— Agent 测试赛道升温，如果你在构建 Agent 产品，Patronus 的方案值得参考。
  _TechCrunch_
- [General Intuition 融资 3.2 亿美元，用游戏训练 AI Agent 的直觉](https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/) —— 用游戏数据训练 Agent 是个有趣方向，但估值 23 亿美元偏高，观察后续产品落地。
  _TechCrunch_

### AI 算力 / 半导体

- [IBM 展示 0.7nm 芯片技术，目标 5 年内量产](https://www.eetimes.com/ibm-shows-sub-1-nm-chips-targeting-production-in-5-years/) —— IBM 的 nanostack 晶体管技术令人印象深刻，但量产时间表遥远，短期影响有限。
  _EE Times_
- [Qualcomm 计划为中国市场定制数据中心芯片，规避出口限制](https://www.tomshardware.com/tech-industry/qualcomm-plans-china-specific-data-center-chips-built-to-clear-us-export-limits) —— Dragonfly 系列将推出中国特供版，性能缩水但合规，对国内 AI 算力市场是利好。
  _Tom's Hardware_
- [Micron 签署 1000 亿美元长期供应协议，称存储危机何时结束未知](https://www.tomshardware.com/pc-components/dram/micron-inks-long-term-supply-agreements-worth-usd100-billion-says-it-has-no-idea-when-ram-crisis-will-end) —— 16 份 LTA 锁定 1000 亿美元收入，存储涨价至少持续到 2027 年，买硬件趁早。
  _Tom's Hardware_

### 大厂 AI 动态

- [Notion Mail 关停，转向 AI Agent 处理邮件](https://techcrunch.com/2026/06/25/notion-mail-shuts-down-amid-agent-takeover/) —— Notion 认为用户更想要 AI 代理管理邮箱而非传统邮件客户端，Agent 替代 SaaS 的趋势加速。
  _TechCrunch_
- [Adobe 收购 Topaz Labs，整合 AI 图像增强工具](https://techcrunch.com/2026/06/25/adobe-acquires-image-and-video-enhancement-tool-maker-topaz-labs/) —— Adobe 在 AI 工具上继续买买买，Topaz 的降噪和超分能力将融入全家桶。
  _TechCrunch_
- [Amazon 向印度追加 130 亿美元 AI 基础设施投资](https://techcrunch.com/2026/06/25/amazon-ups-india-bet-with-fresh-13b-ai-infrastructure-investment/) —— AWS 在印度建 AI 数据中心，全球算力布局加速，对出海开发者是利好。
  _TechCrunch_

### 金融

- [美光长协含金量：客户预付 220 亿美元，锁定“史上最赚钱”毛利率](https://wallstreetcn.com/articles/3775569) —— 存储周期被长协熨平，美光从周期股变成长股，但终端涨价风险也在累积。
  _华尔街见闻_
- [联想预警：内存涨价是“新常态”，高价将持续至 2030 年后](https://wallstreetcn.com/articles/3775587) —— 联想认为 DRAM/NAND 价格已结构性上涨，PC 和手机将持续涨价，买数码产品趁早。
  _华尔街见闻_
- [三星和 SK 海力士酝酿赴美上市，以消除“韩国折价”](https://wallstreetcn.com/articles/3775584) —— 韩国半导体双雄寻求美国上市，吸引全球被动资金，对股价是催化剂。
  _华尔街见闻_
- [SpaceX 光环消退，美股航天概念股 6 月跌幅超 50%](https://wallstreetcn.com/articles/3775575) —— 航天泡沫破裂，商业化周期太长撑不起高估值，短期回避。
  _华尔街见闻_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
