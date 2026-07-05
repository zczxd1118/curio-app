# Curio · AI 算力 / 半导体 · 2026-07-05

> 今日 2 条头条 + 3 条备选

_今日核心信号：阿里因后门风险全面禁用Claude Code，国内AI工具链面临信任危机；OpenAI Scaling Law被曝基础bug，全球算力配置可能长期错配。两条新闻叠加，提示AI工程实践需要更审慎的评估框架。_

---

## 🌟 今日精选

### 3. DRAM价格暴涨成AI算力瓶颈，技术路线被迫转向分层内存架构

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _华尔街见闻_

DRAM价格持续攀升，根源在于HBM挤占产能。AMD、Apple、Marvell等厂商已开始转向AI调度冷数据至闪存、模型常驻NAND等分层策略，纯DRAM堆砌时代正在结束。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DRAM价格因HBM产能挤占持续上涨，PC内存一天三个价 | 分层内存架构能否完全替代DRAM堆砌尚不确定 |
| AMD推出AI调度方案将冷数据迁移至闪存 | 闪迪HBF新架构的成熟度与量产时间未知 |
| Apple将部分模型参数常驻NAND以降低DRAM需求 | HBM4的出货节奏可能缓解部分压力 |
| Marvell发布硬件压缩方案扩容内存带宽 | 消费者端涨价趋势至少持续到2027年 |

**📖 主编点评**

如果你在部署AI应用或做推理优化，需要重新评估内存预算。可以考虑使用量化、模型剪枝等技术减少DRAM占用，或者关注支持闪存直存的推理框架。

📺 [打开原文](https://wallstreetcn.com/articles/3776211)

---

### 4. SK海力士宣布7130亿美元国内投资计划，并筹备纳斯达克上市

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _EE Times_

SK海力士计划投资7130亿美元（约合713B韩元）扩大韩国本土半导体制造产能，同时正在筹备纳斯达克上市。这是韩国存储芯片史上最大规模投资，旨在巩固HBM市场领导地位。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| SK海力士宣布7130亿美元国内投资计划 | 投资落地时间表尚未公布，可能分5-10年完成 |
| 投资将用于扩建HBM和先进DRAM产能 | 纳斯达克上市估值和具体时间未定 |
| 公司正在筹备纳斯达克上市 | 对全球DRAM供需格局的影响需观察 |
| 韩国政府将提供税收优惠和补贴支持 | 三星和美光可能跟进类似投资计划 |

**📖 主编点评**

存储芯片产能扩张对AI算力成本有长期利好，但短期涨价压力仍在。关注SK海力士美股上市后的融资用途，可能影响HBM4的研发进度。

📺 [打开原文](https://www.eetimes.com/sk-hynix-plans-713b-domestic-investment/)

---

## 📋 备选阅读

- [Intel 18A wafer-to-wafer yield issues fixed](https://www.tomshardware.com/tech-industry/semiconductors/intel-18a-wafer-to-wafer-yield-issues-fixed-report-claims-says-production-up-to-15-000-wafers-per-month-at-both-sites) —— Intel 18A良率问题修复，月产能达1.5万片，对先进制程竞争有影响但用户关注度较低。
  _Tom's Hardware_
- [美光日本90亿美元扩建项目开工，预计2028年出货HBM](https://wallstreetcn.com/articles/3776210) —— 美光93亿美元扩建广岛工厂，日本政府补贴5000亿日元，HBM产能竞赛加剧。
  _华尔街见闻_
- [SK hynix, Samsung, Micron面临第三起DRAM价格操纵诉讼](https://www.tomshardware.com/pc-components/dram/samsung-sk-hynix-and-micron-face-a-third-dram-price-fixing-lawsuit) —— 17名原告在加州北区法院起诉三大存储厂商，HBM分配可能成为新焦点。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
