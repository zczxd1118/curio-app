# Curio · AI 算力 / 半导体 · 2026-11-24

> 今日 1 条头条 + 4 条备选

_今天全网只有一个真正的信号：Nvidia 在 Huang 因丑闻辞职 11 天后，被董事会和 Trump 政府联手请回 CEO 位——这不是公司治理事件，是 AI 算力供应链的政治定价。第二条是 Anthropic 的 Claude Ship 把 code review 和 approve 交给 Agent，AI 编程的瓶颈从写代码挪到了合并代码。其余候选池以教程和促销为主，密度偏低。_

---

## 🌟 今日精选

### 1. Nvidia 董事会请回 Huang：11 天罢免再复职，Trump 直接介入董事会会议

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Sally Ward-Foxton_

11 月 12 日 Huang 因与 Megaspeed 高管 Alice Huang 的关系及涉华间谍传闻辞职，董事会启动调查；11 月 23 日董事会宣布复职，Trump 向 CNBC 确认自己打电话给董事会"说服了他们"。同期 SEC 对 Nvidia 会计问题的调查仍在进行，Huang 下周将赴参议院作证。这不是一次人事反复，而是算力供应链被政治直接定价的公开样本。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 11 月 12 日 Huang 辞去 CEO，Reuters 与 BBC 均报道第二段办公室关系使丑闻升级 | 复职能否稳住客户与供应链，还是会让超大规模买家加速自研 ASIC 与二供分散风险，目前无数据 |
| 11 月 23 日 Nvidia 官方新闻稿宣布董事会复任 Huang 为总裁、CEO 及董事 | SEC 会计调查若升级为正式指控，董事会此次决策的合法性会被重新审视 |
| Trump 对 CNBC 称"我跟他们谈了，我说服了他们"，NYT 报道其主导了复职推动 | 参议院听证会是否触发出口管制层面的新立法，尚无草案 |
| Huang 下周将就涉华关系赴参议院公开作证，两党议员已公开批评复职 | 员工内部并非一致欢迎，Tom's Hardware 报道有工程师称"这是最糟的结果" |
| SEC 对 Nvidia 潜在会计问题的调查仍在进行，涉及新加坡销售额停止披露 | Polymarket 上两个账户在复职消息前获利 34 万美元，是否存在信息泄露仍属未证实 |
| Megaspeed 据 TechCrunch 报道接近被列入美国实体黑名单 |  |

**📖 主编点评**

你不需要交易 Nvidia，但需要重估一件事：算力供给的确定性现在挂在政治而非产能上。做 Agent 项目时，把模型和推理供应商做成可切换的一层——这不是过度设计，是当前唯一理性的架构选择。另外这条值得你完整读一遍 EE Times 和 The Verge 的两篇，是很好的"公司治理如何影响技术路线"案例素材。

📺 [打开原文](https://www.eetimes.com/nvidia-board-reinstates-jensen-huang-as-ceo/)

---

## 📋 备选阅读

- [TSMC Hacked](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm) —— TSMC 向 SEC 提交的网络安全事件声明原文，一手材料，值得扫一眼看披露口径。
  _gmays_
- [Shared CXL memory pools come with steep software tax that could stall multi-server scaling](https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26) —— UT Arlington 与 Intel 实测四主机共享 CXL 内存池的同步开销，直接关系到 AI KV cache 能不能跨机扩展。
  _Shane Downing_
- [Japan puts chipmaking labs inside trucks with mobileFab](https://www.tomshardware.com/tech-industry/semiconductors/japan-puts-chipmaking-labs-inside-trucks-with-mobilefab-trucks-pack-30-cm-lithography-gear-to-tackle-a-10-year-semiconductor-engineer-shortage) —— 日本把 30cm 光刻设备装进卡车做巡回教学，应对十年工程师缺口——对电子信息的你是个有意思的产业侧观察。
  _Bruno Ferreira_
- [Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— NVIDIA 官方博客给出跨两台 DGX 跑 GLM-5.3 到 607.8 tok/s 的具体配置，推理优化方向可参考。
  _wondersky_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
