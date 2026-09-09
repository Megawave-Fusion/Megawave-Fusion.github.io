# 曦融兆波 · 聚变知识库

Megawave-Fusion 组织内部知识库。以“原理 → 装置 → 独立辅助加热系统 → 腔体材料”为主线，补充诊断、仿真、工程、实验和文献。

初版提供可扩展分类、系统专题导读、官方参考入口和记录模板。工程条目中的待填写字段并非已完成设计或验收结论。

## 分类导航

| 类目 | 收录范围 |
| --- | --- |
| [01 原理与基础物理](01-fundamentals/README.md) | 反应、约束、平衡、波与粒子、输运及功率收支 |
| [02 装置与技术路线](02-devices/README.md) | 托卡马克、FRC、磁镜、仿星器及补充路线 |
| [03 辅助加热与电流驱动](03-heating-current-drive/README.md) | 每套系统独立管理，ICRH / ECRH / NBI / LHCD / EBW / Helicon |
| [04 腔体、面向等离子体部件与材料](04-chamber-materials/README.md) | 真空室、第一壁、偏滤器、材料数据和制造工艺 |
| [05 诊断、控制与数据采集](05-diagnostics-control/README.md) | 测量、标定、实时控制、时序及数据质量 |
| [06 仿真、计算与验证](06-simulation/README.md) | 模型、求解器、耦合、基准、不确定性与可复现计算 |
| [07 配套工程系统](07-engineering/README.md) | 磁体、电源、真空、冷却、燃料、屏蔽和维护 |
| [08 实验、测试与运行](08-experiments/README.md) | 试验计划、台架、放电记录、标定、验收与故障复盘 |
| [09 项目、机构与产业资料](09-projects-industry/README.md) | 装置档案、团队、供应链、专利及技术成熟度 |
| [10 文献、课程与术语](10-literature/README.md) | 论文笔记、教材、课程、会议、术语与官方来源 |

## 辅助加热：各系统独立入口

- [ICRH / ICRF：离子回旋加热](03-heating-current-drive/icrh/README.md)
- [ECRH / ECCD：电子回旋加热与电流驱动](03-heating-current-drive/ecrh/README.md)
- [NBI / NBCD：中性束注入与电流驱动](03-heating-current-drive/nbi/README.md)
- [LHCD / LHH：低杂波电流驱动与加热](03-heating-current-drive/lhcd/README.md)
- [EBW：电子伯恩斯坦波加热与电流驱动](03-heating-current-drive/ebw/README.md)
- [Helicon：螺旋波加热与电流驱动](03-heating-current-drive/helicon/README.md)

每个系统均有独立的原理、设备组成、设计计算、控制保护、测试验收、文献与案例页面。跨系统知识通过链接复用。

## 如何使用

1. 从上方分类或 [完整目录](CATALOG.md) 找到条目归属。
2. 复制 [知识条目](templates/knowledge-entry.md)、[论文笔记](templates/paper-note.md)、[装置档案](templates/device-profile.md) 或 [系统规格](templates/system-spec.md) 模板。
3. 填写来源、版本、单位、适用条件和证据状态，通过 Pull Request 更新。
4. 提交前执行 `python3 scripts/check_kb.py` 检查内部链接和目录。

[编写规范](CONTRIBUTING.md) · [分类与标签规则](TAXONOMY.md) · [建设待办](ROADMAP.md) · [术语表](10-literature/glossary.md) · [来源目录](references/README.md)

中文为主要说明语言，保留英文术语、缩写与原文标题。文件路径使用稳定的英文名称，所有内部链接采用相对路径。
