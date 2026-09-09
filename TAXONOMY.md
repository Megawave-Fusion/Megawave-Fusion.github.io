# 分类与标签规则

## 图片主线的落地

| 原始思路 | 知识库归属 |
| --- | --- |
| 原理 | 01-fundamentals |
| 装置及不同约束路线 | 02-devices；包含托卡马克、FRC、磁镜、仿星器等 |
| ICRH、ECRH 等辅助加热 | 03-heating-current-drive 下各系统独立目录 |
| 腔体材料 | 04-chamber-materials |

手写装置标签以通用路线名称展开，不将模糊字迹当作已确认的专有装置名称。

## 一篇条目一个主归属

波传播的一般理论放基础物理；ICRH 特有的耦合和吸收放 ICRH；某台装置的 ICRH 配置放装置档案并链接系统页。材料的通用物性放材料库；天线特有热负荷分析放对应加热系统。

## 元数据

推荐字段：`title`、`category`、`tags`、`status`、`evidence_type`、`owner`、`updated`、`device`、`system`、`sources`。

- status：draft / in-review / reviewed / archived。reviewed 需记录实际审核人和日期。
- evidence_type：reference-summary / analytical / simulation / experiment / engineering-test / hypothesis。
- device：tokamak / spherical-tokamak / stellarator / frc / mirror / rfp / spheromak / icf / mif / z-pinch / general。
- system：icrh / ecrh / nbi / lhcd / ebw / helicon / general。

来源类型和审核状态相互独立；仿真结果不会因为审核通过而变成实验证据。正文中的设计目标、数值预测和实测值分别标明。
