# Curio · AI 算力 / 半导体 · 2026-11-27

> 今日 2 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Nvidia 的治理危机从八卦升级成信用事件——S&P 考虑下调评级、董事会独立性被质疑、对东南亚出货暂停，Jensen Huang 回归 CEO 反而成了风险源；二是 Anthropic 上市后股价跌破 83 美元发行价，1.5T 估值叙事开始松动。AI 资本周期的第一次真实回调，可能就从这两条开始。_

---

## 🌟 今日精选

### 1. Jensen Huang 被董事会重新任命为 Nvidia CEO，治理危机升级为信用事件

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _jaz_

一周之内，Nvidia 董事会把刚离任的 Jensen Huang 重新扶回 CEO 位置，官方公告与 CNBC 报道同步落地。但市场没有把它读成稳定信号：S&P 正在评估下调 Nvidia 信用评级，国会公开批评这是「性格的失败」，董事会独立性遭到质疑。这不是人事新闻，是一家 4 万亿美元公司治理结构的压力测试。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 官方新闻稿确认董事会重新任命 Huang 为总裁、CEO 及董事 | Huang 最初离任的真实原因仍未完整披露，公开信息只有片段 |
| S&P 表示正考虑将 Nvidia 信用评级下调至 AA-，理由含治理与「关键人风险」 | S&P 是否真的下调评级尚未决定，AA- 只是评估方向 |
| 国会多名议员公开批评此次回归，CNBC 报道用词为「outrageous」 | 国会批评是否会转化为听证或立法动作，目前没有时间表 |
| 此前有报道称 Huang 违反公司行为准则，涉及与前 Megaspeed 高管的关系 | 东南亚出货暂停是出口管制收紧还是自查，官方口径模糊 |
| Nvidia 已通知代工伙伴暂停对马来西亚、新加坡、泰国、印尼的服务器出货 | 董事会是否有其他成员因这次反转辞职，尚无消息 |

**📖 主编点评**

你如果关注 AI 基建投资逻辑，这条比任何模型发布都重要：Nvidia 的风险溢价正在从「需求不确定」转向「治理不确定」。短期看 GPU 供给节奏可能因出货暂停而波动，长期看这家公司的估值锚会多一条治理折价。别只看财报数字，盯 S&P 的正式决定和下一份 10-Q 的关联交易披露。

📺 [打开原文](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html)

---

### 4. 华为将在 ISSCC 2027 公布自研 HBM 方案，绕开出口管制的存储瓶颈

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Majeed Ahmad_

EE Times 报道，华为将在明年旧金山的 ISSCC 2027 上披露其定制 HBM 设计细节。这是华为在被切断先进 HBM 供应后，第一次公开给出存储层的替代路径。HBM 是当前 AI 芯片最硬的卡点之一，这条比大多数模型新闻更接近产业底层。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 华为将在 ISSCC 2027 公布定制 HBM 设计细节（EE Times 报道） | 自研 HBM 的良率、带宽和量产时间全部未知，ISSCC 论文不等于量产 |
| 会议时间为明年初，地点旧金山 | 是否依赖国内存储厂（如长鑫）代工，报道未提及 |
| 这是华为首次公开披露自研 HBM 方案 | 性能对标 HBM3 还是 HBM3E 没有信息 |
| 背景是美国对先进 HBM 的对华出口限制持续收紧 | 即便方案可行，生态适配（CUDA 替代）仍是更大瓶颈 |
|  | ISSCC 论文可能只披露架构而非完整工艺细节 |

**📖 主编点评**

你如果做 AI 工程实践，这条提醒你：推理优化的成本模型里，HBM 带宽是比算力更稀缺的变量。国内可获得的硬件在带宽上会长期落后，意味着你的部署方案要更早考虑量化、KV cache 压缩和 batch 策略，而不是等硬件追上来。

---

## 📋 备选阅读

- [Nvidia 同意支付 2.9 亿美元和解 2018 年矿卡销售集体诉讼](https://www.tomshardware.com/tech-industry/big-tech/nvidia-agrees-to-usd290-million-settlement-over-2018-crypto-mining-gpu-sales-ends-eight-year-investor-lawsuit-without-admitting-wrongdoing) —— 八年诉讼收尾，是 Nvidia 信息披露问题的历史注脚，与当前治理危机形成呼应。
  _Jhet Borja_
- [德州撤销 1800+ 数据中心项目冻结，开发商抢在 1 月前拿许可](https://www.tomshardware.com/tech-industry/data-centers/texas-lifts-freeze-on-1-800-data-center-projects-in-greg-abbott-u-turn-companies-rush-for-permits-before-gina-hinojosas-january-arrival) —— AI 基建的电力与土地约束在州级政治里反复摇摆，是算力供给侧的领先指标。
  _Oliver Haslam_
- [用两块 Nvidia DGX Station + vLLM 跑 GLM-5.3，达 607.8 tok/s](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— 有具体吞吐数字和部署配置，符合你要的工程细节，但场景偏企业级。
  _wondersky_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
