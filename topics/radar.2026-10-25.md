# Curio 趋势雷达 · 2026-10-25

> 你的私人主编 · 今日跨域精选 5 条头条 + 18 条备选

_今天最值得看的两条信号：一是 OpenAI 宣布前沿模型不再吃「活的互联网」数据，训练数据供应链开始主动收缩；二是 AI 资本侧明显降温——Anthropic 估值被传缩水 5000 亿美元、数据中心类 IPO 接连折戟、10 年期美债收益率破 5.3%。算力与半导体侧则是另一条线：中国用 DUV 多重曝光硬撑 5nm 级，代价是良率与成本。_

---

## 🌟 大厂 AI 动态

### 1. OpenAI 停止用「活的互联网」训练前沿模型，理由是「重大风险」

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

OpenAI 公开表示将不再让前沿模型直接抓取实时互联网数据训练，理由是存在「significant risks」。时间点很微妙——几周前自家工程师还公开说这条路走不通。这不是技术细节调整，而是训练数据供应链的一次主动收缩：实时网页既是最大的语料池，也是最大的投毒面和合规雷区。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| OpenAI 官方表态：前沿模型不再以实时互联网数据为训练来源 | 「不再训练」的具体边界未明：是彻底断网，还是仅限前沿模型、是否含 RL 环境 |
| 给出的理由是「significant risks」，未逐条列明具体风险类型 | 是否与近期网页投毒、版权诉讼或监管压力直接相关，官方未确认 |
| 该决定发生在一位 OpenAI 工程师公开质疑该方案可行性数周之后 | 对模型时效性的实际影响要等下一代模型评测才能验证 |
| 此前业界普遍做法是持续抓取实时网页以保持模型时效性 | 其他厂商（Anthropic、Google）是否跟进，目前无信号 |

**📖 主编点评**

你做 content-curator 这类依赖实时抓取的 Agent，这条是反向提醒：上游模型厂商开始不信任开放网页，你自己的数据管道就更该做来源白名单和内容校验。别把「能抓到」当成「能信」。

📺 [打开原文](https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/)

---

## 🌟 股票

### 2. Anthropic 估值被传缩水 5000 亿美元，AI 一级市场定价开始松动

**[股票]** · ⭐⭐⭐⭐⭐ · _Hacker News / The Telegraph_

Telegraph 报道 Anthropic 估值在 IPO 推进过程中大幅回落，规模达 5000 亿美元级别；同期 Reuters 与 WSJ 已披露其 S-1 显示营收高增但算力成本同样飙升。把这条和 Firmus 30 亿美元 IPO 梦碎、韩国数据中心类 IPO 首日暴跌 30% 放在一起看，AI 资产的定价锚正在从「叙事」切回「现金流」。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Telegraph 报道 Anthropic 估值出现 5000 亿美元级别的回落 | 5000 亿这个数字来自单一媒体，尚未获公司或承销方确认 |
| Reuters、WSJ 已报道其 IPO 招股书显示营收快速增长、算力成本高企 | 估值回落是二级市场折价还是新一轮融资定价，报道未说清 |
| Nvidia 支持的数据中心公司 Firmus 撤回 IPO | 是否引发其他 AI 独角兽推迟上市，目前只是市场猜测 |
| 韩国一宗数据中心相关 IPO 上市后暴跌 30%，拖累板块情绪 | Anthropic 官方对估值口径保持沉默 |

**📖 主编点评**

如果你在简历或项目里引用「AI 融资额」当行业背书，现在要更谨慎——一级市场正在重新定价。对你更有用的是 S-1 里那条：营收涨、算力成本也涨，这才是 Agent 产品真实的经济模型参照。

📺 [打开原文](https://www.telegraph.co.uk/business/2026/10/16/anthropic-valuation-ipo-ai-stock-listing/)

---

## 🌟 AI 算力 / 半导体

### 3. 中国用 DUV 多重曝光逼近 5nm 级，代价是更大 die、更低良率、更长工时

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

Tom's Hardware 梳理了中国在无 EUV 条件下把老一代 DUV 光刻推到极限的路径：靠多重曝光做到接近 5nm 级别。结论不是「做不出来」，而是「做得出来但账单越来越贵」——die 面积变大、良率下降、制造周期拉长，三重成本叠加。这是对「卡脖子」叙事的一次量化修正。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 中国厂商通过 DUV 多重曝光实现接近 5nm 级别的工艺 | 「5nm 级」是性能对标还是密度对标，报道口径偏模糊 |
| 代价包括 die 面积增大、良率下降、制造时间延长 | 实际量产良率数字未公开，成本差距难以精确量化 |
| 报道明确指出进一步微缩的成本曲线在恶化 | 这套路线能撑到几代之后，业内无共识 |
| ASML 同期表示 2026 年在欧洲「几乎没卖出任何设备」 | 对国产 AI 芯片实际供货能力的影响仍需观察 |

**📖 主编点评**

你做的是电子信息工程，这条值得存下来当工艺课的活案例：多重曝光的成本结构比「能不能做」更能说明产业现实。面试聊到国产替代时，讲清 trade-off 比喊口号有说服力得多。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/china-can-make-advanced-chips-without-euv-but-the-bill-keeps-growing-duv-multiple-patterning-means-bigger-dies-lower-yields-and-longer-manufacturing-times)

---

### 4. DeepSeek 4.1 Flash 1017：单任务成本再压低，适合 Agent 负载但幻觉率更高

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

DeepSeek 新版本把 cost-per-task 又往下压了一档，明确定位在 agentic workload——便宜、能跑工具调用链。代价写在标题里：相比闭源竞品更容易幻觉。这条对做 Agent 的人是直接的工程取舍题：省钱换准确率，值不值取决于你的任务能不能容忍重试。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek 4.1 Flash 1017 为开放权重模型 | 具体成本数字与幻觉率对比基线未在摘要中给出 |
| 单任务成本进一步下降，主打 agentic 工作负载 | 「适合 agentic」是厂商定位还是第三方实测结论，需看原评测 |
| 评测显示其幻觉率高于闭源竞品 | 在长链路工具调用中的稳定性尚无公开数据 |
| 定位明确偏向低成本、高吞吐的 Agent 场景 | 对国内开发者可及性（API 稳定性、限流）未提及 |

**📖 主编点评**

如果你在 content-curator 里做多步 Agent 编排，可以拿它当「便宜的执行层」——让贵模型做规划、它做批量执行，再用校验步骤兜幻觉。这比单纯换模型更接近真实工程解法。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseeks-latest-ai-model-is-smarter-than-ever-but-its-low-running-costs-come-at-a-price-open-weight-model-is-fit-for-agentic-workloads-but-is-more-prone-to-hallucination-than-proprietary-competitors)

---

## 🌟 金融

### 5. 10 年期美债收益率升破 5.3%，24 年来最高，AI 数据中心融资首当其冲

**[金融]** · ⭐⭐⭐⭐ · _Hacker News / WSJ_

WSJ 报道 10 年期美债收益率突破 5.3%，为 24 年未见水平。Reuters 同期指出，市场抛售与利率上行正在「测试 AI 数据中心交易热潮」。逻辑很直白：数据中心是重资产、长周期、靠杠杆的项目，贴现率一抬，整个 AI 基建的融资模型就要重算。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 10 年期美债收益率升破 5.3%，为约 24 年最高 | 收益率上行是短期波动还是趋势起点，市场分歧明显 |
| Reuters 报道市场抛售与利率上行正在考验 AI 数据中心交易 | 对具体数据中心项目的融资成本影响尚无量化披露 |
| 美国联邦财政赤字一年内增长 12%，接近 2 万亿美元 | AI 资本开支是否因此放缓，目前只有情绪面证据 |
| 数据中心相关股票与 IPO 近期同步走弱 | 与 AI 泡沫论的关系属于解读，非事实 |

**📖 主编点评**

这条和 Anthropic 估值那条是同一件事的两面。你关注 AI 产品动态时，别只看模型发布——融资环境的松紧决定了哪些工具能活到你用上它的那天。选型时优先押有真实收入的工具。

📺 [打开原文](https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f)

---

## 📋 备选池

### AI

- [从 LLM 到 Agent Skill，一期视频打通底层逻辑](http://www.bilibili.com/video/av116227955497963) —— 概念串联做得完整（LLM→Token→Context→Tool→MCP→Agent→Skill），但属综述型，新颖度不够上头条。
  _马克的技术工作坊_
- [一个 CLI 干掉所有 MCP 工具，省 99% token：mcp2cli 深度解析](http://www.bilibili.com/video/av116204349953548) —— 把 MCP server 转成 CLI、用懒发现把 token 从数十万降到几千，工程细节密度高，值得单独看。
  _探索未至之境_
- [Claude Code Agent Teams 上手指南 + 项目实测](http://www.bilibili.com/video/av116037064331269) —— 讲清 Team Lead 拆任务、多 Teammate 并行的架构，正好对上你关心的子 Agent 编排。
  _程序员阿江-Relakkes_
- [Claude Code Hooks 回调 + Agent Teams 零轮询省 token](http://www.bilibili.com/video/av116046157647899) —— Stop Hook 自动回调替代轮询，是能直接抄进项目的具体配置级技巧。
  _AI超元域_
- [用 Claude Skill 做高质量 PPT（附完整教程）](http://www.bilibili.com/video/av116474832361424) —— 从 0 到 1 装 Skill 跑成品，Skill 打包思路可迁移到自己的 Agent 项目。
  _阿西_出海_

### AI 算力 / 半导体

- [Opus 5.5 agents 发现两种室温磁性半导体候选材料](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors) —— 用 Agent 做材料发现的具体案例，495 分讨论，但结论未经实验验证，先观察。
  _Hacker News_
- [ASML：2026 年在欧洲「什么都没卖出去」](https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand) —— 一句话把欧洲半导体产业空心化说透，配合中国 DUV 那条一起看更有意思。
  _Hacker News_
- [泄露视频：中国工厂成规模拆解 RTX 5090 供 AI 服务器](https://www.tomshardware.com/pc-components/gpus/leaked-video-exposes-how-chinese-factories-are-stripping-rtx-5090s-to-fuel-ai-custom-partner-cards-to-nvidia-founders-editions-on-the-chopping-block) —— 消费卡被拆成 AI 算力，是出口管制下的市场扭曲实证，画面感强。
  _Tom's Hardware_
- [GPU-unlock：解锁 Nvidia 30 系卡的 FP/BF16 指令发射率](https://github.com/Zagitta/gpu-unlock) —— 纯工程向的逆向与指令级优化，235 分，适合你这种想看底层的人。
  _Hacker News_
- [Arm 就 Qualcomm 陪审团裁决表态：2 美元赔偿背后的合规测试控制权](https://www.eetimes.com/two-dollars-and-a-test-suite/) —— 赔偿只有 2 美元，真正争的是定制芯片出厂前必须通过的合规测试归谁管。
  _EE Times_

### 大厂 AI 动态

- [Gemini 4 Argon 发布，配套机器人版本与 StarCraft 实测](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) —— 1700+ 分的大发布，但已过去三周多，且摘要信息薄，放备选等评测沉淀。
  _Hacker News_
- [Block 新语音模型可在 MacBook M4 Max 本地运行](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/) —— 本地跑、听感接近真人，端侧语音这条线值得跟，但缺具体参数。
  _TechCrunch_
- [Daytona 估值达 10 亿美元：给每个 Agent 一台云上电脑](https://techcrunch.com/2026/10/23/agent-cloud-startup-daytona-hits-1b-valuation-backed-by-firstmark-and-a-whos-who-of-angels/) —— Agent 沙箱基础设施的融资信号，Stripe、Datadog 创始人跟投，方向值得记。
  _TechCrunch_

### 股票

- [Capital Wars：CoreWeave 与一座数据中心的建造经济学](https://www.netinterest.co/p/capital-wars) —— 把数据中心建设的资本结构拆开算，是理解 AI 基建融资的少有好材料。
  _Net Interest_
- [中国股票成全球 AI 交易回调中最大输家](https://theedgemalaysia.com/node/822195) —— AI 交易全球性回调的侧写，与美债收益率、Anthropic 估值两条互为印证。
  _Hacker News_

### 金融

- [AI 算力是新的石油，需要一个新市场](https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market) —— 把算力当大宗商品定价的框架讨论，思路新颖但偏宏观，适合周末慢读。
  _Hacker News / The Economist_
- [美国下令所有民事机构移除 DeepSeek，含基于其构建的工具](https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/) —— DHS 命令波及「基于 DeepSeek 构建的工具」，对做二次封装的开发者是合规红线。
  _Hacker News_
- [美联储被指悄悄吹大 AI 泡沫，同时抬高你的电费](https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly) —— 把货币政策、数据中心用电与电价绑在一起讲，观点性强，当观点读不当事实读。
  _Hacker News_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
