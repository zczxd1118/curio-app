# Curio · AI 算力 / 半导体 · 2026-11-19

> 今日 2 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Nvidia 在黄仁勋辞职后交出 1158 亿美元季度营收、AI 基建需求没塌，但公司治理与 10-Q 延迟披露成了新的不确定性；二是 Anthropic 以每股 83 美元、1.5 万亿美元估值定价 IPO，同时被信用机构打上高收益垃圾级预期——AI 资本周期第一次被公开定价。对你而言，今天值得读的是「工程细节 + 行业结构」，不是情绪。_

---

## 🌟 今日精选

### 1. Nvidia 临时 CEO 任内首份财报：季度营收 1158 亿美元，AI 基建需求未随人事震荡下滑

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _News Desk_

黄仁勋 11 月 12 日辞职后，Nvidia 由临时 CEO Colette Kress 交出的第一份季报显示营收 1158 亿美元，AI 基础设施需求仍是主要拉动。这条的意义不在数字本身，而在于它回答了「换帅是否伤业务」这个最贵的疑问。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 季度营收 1158 亿美元，由临时 CEO Colette Kress 主持发布 | 1158 亿是否包含渠道提前拉货，需等 10-Q 明细才能判断 |
| 营收与利润增长主要来自 AI 基础设施需求 | 临时 CEO 能否在下一季度维持供应链与客户关系，尚无证据 |
| 黄仁勋已于 11 月 12 日即刻辞任 CEO，董事会表示不打算让其回归 | 董事会拒绝回归的表态是否会在员工请愿压力下松动，仍不明朗 |
| 公司此前未按期提交 10-Q，引发分析师追问 | AI 基建需求是否已见顶，单季数据不足以定论 |
| Kress 在全员会上承诺 12 月前加薪与追加股权以稳定团队 |  |

**📖 主编点评**

你应该把这条当成「AI 资本周期的体检报告」来读，而不是财经八卦。真正要盯的是 10-Q 补交后的应收账款与库存科目——那才是判断这轮算力需求是真实消耗还是渠道囤货的关键。对你的 side project 没有直接影响，但决定了明年 GPU 租赁价格和 API 定价的走向。

📺 [打开原文](https://www.eetimes.com/nvidia-reports-115-8b-in-quarterly-revenue-under-interim-ceo/)

---

### 3. 三张退役 V100 组 1042 美元主机，跑 Qwen 3.6 35B 达 100 tok/s，长上下文反超 5399 美元 Mac Studio

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Shane Downing_

一位 homelab 玩家用三张二手 Tesla V100 搭出总价 1042 美元的机器，跑 Qwen 3.6 35B 达到约 100 tokens/s，在长上下文场景下超过 5399 美元的 M5 Max Mac Studio。这是本周最具体的「推理成本」数据点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 硬件为三张二手 Nvidia Tesla V100，整机成本约 1042 美元 | 100 tok/s 的具体 batch size 与量化精度未在摘要中说明 |
| 模型为 Qwen 3.6 35B，吞吐约 100 tokens/s | 长上下文优势是否在真实 Agent 多轮调用中保持，需实测 |
| 对比对象为 5399 美元的 M5 Max Mac Studio | 二手 V100 的供货与功耗成本未计入总拥有成本 |
| 长上下文场景下该配置表现优于对比机 | 该结果是否可复现，取决于具体推理框架配置 |

**📖 主编点评**

如果你想给自己的 Agent 项目做本地推理兜底，这条给出了一个反直觉的性价比答案：退役卡在长上下文上仍有优势。建议你去翻原帖的推理框架与量化参数，照抄一份配置跑通，这本身就是简历上「推理优化」的实证素材。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts)

---

## 📋 备选阅读

- [Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— Nvidia 官方 vLLM 跨机部署细节，607.8 tok/s 有具体配置，工程价值高但离个人项目较远。
  _wondersky_
- [DDR6 RAM shrinks by 44% while delivering 4X DDR5's baseline bandwidth](https://www.tomshardware.com/pc-components/ram/ddr6-ram-shrinks-by-44-percent-while-delivering-4x-ddr5s-baseline-bandwidth-jedec-previews-12-8-gt-s-modules-with-up-to-1-terabyte-of-capacity-per-slot) —— JEDEC 预览 DDR6：模块从 133mm 缩到 74mm，起步 12.8 GT/s，单槽最高 1TB，是硬件层的长期信号。
  _Zhiye Liu_
- [TSMC Hacked](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm) —— TSMC 向 SEC 提交的网络安全事件声明原文，供应链安全信号，值得扫一眼原文措辞。
  _gmays_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
