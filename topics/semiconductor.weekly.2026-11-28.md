# Curio · AI 算力 / 半导体 · 2026-11-28

> 今日 1 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Nvidia 董事会把黄仁勋请回 CEO 位子，但 SEC 会计调查、国会质疑、S&P 警告董事会独立性、东南亚出货暂停同时压上来，这件事已经从人事八卦变成治理与出口管制的双重风险；二是 Anthropic IPO 定价 $83、估值 $1.5T 后迅速跌破发行价，AI 资产的定价逻辑正在被重新校准。对做 Agent 的你来说，工具层今天没有大新闻，但 Claude Code 桌面端整合、Gemini 4 系列迭代仍在推进。_

---

## 🌟 今日精选

### 1. Nvidia 董事会请回黄仁勋任 CEO，但 SEC 会计调查、国会质疑与东南亚出货暂停同时压顶

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _jaz_

11 月 23 日 Nvidia 董事会宣布恢复黄仁勋总裁兼 CEO 及董事身份，结束了此前数周的权力真空。但这不是一个干净的回归：SEC 正在查潜在会计问题，S&P 警告董事会独立性可能受损，国会直接称这是'性格的失败'，同时公司已要求代工伙伴暂停对马来西亚、新加坡、泰国、印尼的服务器出货。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 11 月 23 日 Nvidia 董事会正式恢复黄仁勋 CEO 与董事职务，官方新闻稿已发布 | SEC 会计调查最终是否升级为正式指控，目前无时间表 |
| SEC 调查正在审查潜在会计问题，多家媒体援引消息人士 | 董事会此次反转是否触发更多机构投资者诉讼或代理权之争 |
| S&P 公开警告 Nvidia 董事会可能已失去独立性 | 东南亚出货暂停是短期合规动作还是长期区域策略收缩，公司未说明 |
| Nvidia 已要求制造伙伴暂停对马来西亚、新加坡、泰国、印尼的服务器出货 | 黄仁勋回归后对华出口政策立场会更强硬还是更务实，尚无公开表态 |
| 此前有报道称超过 1.5GW 受禁 GPU 被走私至中国，被视为黄离职的潜在诱因 | Polymarket 上两个可疑账户在事件中获利超 $34 万，是否涉及内幕交易仍在调查 |
| Nvidia 停止披露新加坡销售额，同期营收达 $104B |  |

**📖 主编点评**

这条不是让你去炒 Nvidia，而是提醒你：AI 算力的供给端正在被地缘政治和公司治理同时扰动。如果你在做需要调用海外模型的 Agent 项目，应该开始假设'API 供给可能因政策突然收紧'，把模型接入层做成可切换的（Claude / Gemini / DeepSeek 多路 fallback），而不是硬绑一家。

📺 [打开原文](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html)

---

## 📋 备选阅读

- [Huawei's Next Big AI Move: HBM Workaround](https://www.eetimes.com/huawei-next-big-ai-move-hbm-workaround/) —— 华为将在 ISSCC 2027 公布自研 HBM 方案，绕开出口管制的存储瓶颈，是国产算力链的关键变量。
  _Majeed Ahmad / EE Times_
- [Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— NVIDIA 官方博客给出跨两台 DGX 跑 GLM-5.3 的 vLLM 配置，607.8 tok/s，是少见的带具体参数的推理优化实操。
  _NVIDIA Developer Blog_
- [Penguin Revives Retired DDR4 for AI Servers](https://www.eetimes.com/penguin-revives-retired-ddr4-for-ai-servers/) —— 企业级开始回收退役 DDR4 用于 AI 服务器扩容，内存成本压力下的务实选择，硬件侧的小信号。
  _Gary Hilson / EE Times_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
