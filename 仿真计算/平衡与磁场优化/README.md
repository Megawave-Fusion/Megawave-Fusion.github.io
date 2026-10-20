# 平衡与磁场优化

先区分轴对称重建、三维平衡与线圈优化，再准备输运和稳定性所需的几何。

## 轴对称平衡与实验重建
### 诊断约束与自由边界

平衡重建是反问题：给定有限且带误差的诊断，寻找满足力平衡并与测量相容的电流和压力分布。设计平衡通常是正问题：给定线圈和剖面，求磁面及边界。轴对称托卡马克与三维仿星器的几何和假设不同，软件选择也不同。

| 软件 | 方程与表示 | 主要输入和输出 | 选型差异 |
| --- | --- | --- | --- |
| [EFIT / EFIT-AI](https://gafusion.github.io/OMFIT-source/modules/mod_EFIT.html) | 二维轴对称 Grad–Shafranov 平衡，可结合诊断约束重建 | 磁测量、MSE、压力/电流约束和机器几何 → 磁通、边界、$q$ 与 g/a 等文件 | 适合实验平衡与下游输入；内部电流剖面的可信度依赖诊断覆盖、参数化与拟合权重 |
| [FreeGS](https://github.com/freegs-plasma/freegs/blob/master/README.md) | Python 自由边界 GS，Picard 迭代与多重网格 | 线圈、剖面、形状约束 → 稳态磁通、X 点及线圈电流 | 适合磁形状设计、教学和自定义约束；稳态线圈解不包含完整控制电路时间演化 |
| [FreeGSNKE](https://github.com/FusionComputingLab/freegsnke) | 轴对称 GS 平衡与主动/被动导体电路演化 | 初态、线圈电压和剖面参数 → 形状及线圈/被动结构/等离子体总电流轨迹 | 可研究动态平衡和控制；当前采用 FreeGS4E 后端，所核 README 仍将电流扩散与输运耦合列为后续计划 |

FreeGSNKE 的[静态平衡比较论文摘要](https://arxiv.org/abs/2407.12432)描述了在一致 MAST-U 几何、导体电流和剖面条件下与 Fiesta、EFIT++ 的核对；本章仅据摘要引用这一比较范围。静态平衡的一致性证据不能直接转移成动态壁载荷的精度结论。

### 获取与运行依赖

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| EFIT-AI | [官方许可页](https://efit-ai.gitlab.io/efit/license.html)列 BSD-2-Clause，同时附用户协议与邮件申请流程 | 该页另列分发、研究与发表要求，目标发行版按团队提供的完整条款确认；机器与诊断配置另备 |
| FreeGS / FreeGSNKE | 公开；[FreeGS](https://github.com/freegs-plasma/freegs/blob/master/LICENSE)、[FreeGSNKE](https://raw.githubusercontent.com/FusionComputingLab/freegsnke/main/LICENSE)均为 LGPL v3 | 平衡后端、机器几何、线圈数据和装置数据库接口 |

### 计算图解

加权重建可用下式理解（目标函数示意，实际残差及正则项依实现）：

$$
\mathcal J=\sum_j\left[\frac{\mathcal H_j(\psi)-y_j}{\sigma_j}\right]^2+\lambda\mathcal R(\psi).
$$

$y_j$ 为测量、$\mathcal H_j$ 为前向观测、$\sigma_j$ 为误差尺度；正则权重 $\lambda$ 改变拟合与平滑之间的权衡。

![重建约束、设计变量与下游磁几何的职责。](/assets/diagrams/sim-equilibrium.svg)

重建约束、设计变量与下游磁几何的职责。

## 三维平衡与嵌套磁面

### VMEC 与 DESC 的平衡精度

| 软件 | 方程与表示 | 主要输入和输出 | 选型差异 |
| --- | --- | --- | --- |
| [VMEC / VMEC2000](https://princetonuniversity.github.io/STELLOPT/VMEC.html) | 在嵌套磁面假设下求三维理想 MHD 平衡；固定或自由边界 | 边界、压力、旋转变换或电流、磁通及外线圈场 → wout 等几何与剖面 | 适合仿星器几何和已有下游工具链；扫描径向与角向分辨率，检查力残差和近轴导数 |
| [DESC](https://desc-docs.readthedocs.io/en/stable/) | 三维嵌套磁面、伪谱离散、力残差优化和自动微分 | 边界与剖面 → 平衡、派生量和优化结果，可输出 VMEC 相关格式 | 适合梯度设计及平衡/线圈优化；JAX 编译、谱阶及目标函数会影响成本 |

VMEC 和 DESC 都用嵌套磁面表示，磁岛和随机区不能直接从这一表示中产生。[DESC 与 VMEC 的原始比较论文](https://doi.org/10.1017/S0022377823000272)用共同的力平衡误差和具体案例讨论收敛，说明应比较达到同一误差目标的成本。优化还要检查线圈间距、曲率、工程载荷、快粒子约束和扰动敏感性；只降低一个准对称指标，不能替代这些约束。

### 获取与运行依赖：三维平衡与嵌套磁面

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| VMEC2000 | 所核 [VMEC2000 仓库](https://raw.githubusercontent.com/hiddenSymmetries/VMEC2000/master/LICENSE)为 MIT | 此结论限定 hiddenSymmetries/VMEC2000 发行版；外接求解器及 MPI/HDF5 等运行依赖另查 |
| DESC | 所核 [DESC 仓库](https://raw.githubusercontent.com/PlasmaControl/DESC/master/LICENSE)为 MIT | 外接求解器及 JAX 等运行依赖另查 |

## 线圈与多指标优化

### SIMSOPT 的变量、目标与后端

| 软件 | 方程与表示 | 主要输入和输出 | 选型差异 |
| --- | --- | --- | --- |
| [SIMSOPT](https://simsopt.readthedocs.io/latest/mhd.html) | 组织线圈/表面、磁场、目标函数及外部物理求解器的优化框架 | 设计自由度和约束 → 线圈/边界方案及求解历史 | 适合组合多种指标；VMEC、SPEC 等后端需另装，成本取决于调用次数与求导方式 |

优化中把边界 Fourier 系数、线圈曲线和电流作为不同的设计变量，明确哪些固定、哪些变化。每次目标函数评估应留下对应的平衡版本；比较两个方案时，除目标值外同时查看约束违反量与扰动敏感性。所接求解器、求导方法和容差属于优化配置。参见 [SIMSOPT MHD 接口](https://simsopt.readthedocs.io/latest/mhd.html)。

### 获取与运行依赖：线圈与多指标优化

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| SIMSOPT | 所核 [SIMSOPT 仓库](https://raw.githubusercontent.com/hiddenSymmetries/simsopt/master/LICENSE)为 MIT | 外接求解器及 MPI/HDF5 等运行依赖另查 |

[返回仿真计算总览](../README.md)
