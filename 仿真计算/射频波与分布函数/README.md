# 射频波与分布函数方法

先掌握射线、准光学、全波和弹跳平均 FP 的区别，再进入各加热系统的具体流程。

## 射线、准光学与全波的选择
### GENRAY、GRAY、TORIC 与 AORSA

射线追踪用几何光学近似计算传播和局部吸收；准光学束追踪还描述有限束宽与衍射；全波求解给定频率、边界和介电响应下的场；Fokker–Planck（FP）求碰撞、波扩散、电场与源汇作用下的分布函数。这几层分别决定传播、场结构、非热尾部和电流。具体应用可对照[离子回旋](../../辅助加热/离子回旋加热/README.md)、[电子回旋](../../辅助加热/电子回旋加热/README.md)与[低杂波](../../辅助加热/低杂波电流驱动/README.md)专题。

| 软件 | 物理层级 | 主要输出 | 模型边界与比较重点 |
| --- | --- | --- | --- |
| [GENRAY](https://www.compxco.com/genray.html) | 几何光学射线，具有 EC、LH、ICRF 等色散/吸收选项 | 射线路径、吸收及线性电流驱动；可向 FP 提供 RF 数据 | 核对色散与吸收模型、初始谱和功率；截止、模转换、干涉与衍射需检查近似是否成立 |
| [GRAY](https://baltig.cnr.it/ectoplasm/gray) | 用复 eikonal 描述 EC 高斯束的准光学传播 | 束传播、衍射、吸收与 EC 电流驱动 | 比单条射线多了束宽/衍射描述，但不等同于三维天线近场全波 |
| [TORIC](https://www-internal.psfc.mit.edu/~jwright/Publications/jcw_icnsp_submittedpaper/node2.html) | 轴对称环形几何、热等离子体有限拉莫尔半径（FLR）全波 | 波场、模式转换和分物种吸收 | “全波”仍有线性响应、几何和 FLR 模型近似，须写明所用版本 |
| [AORSA](https://github.com/ORNL-Fusion/aorsa) | 谱全波，保留离子拉莫尔半径与波长比的所有阶响应 | RF 场、沉积，按配置输出准线性系数 | 所谓所有阶不消除平衡梯度、线性响应和有限分辨率的近似；构建与大矩阵求解也是成本 |

TORIC 的[原始论文](https://doi.org/10.1088/0741-3335/41/1/002)说明其有限拉莫尔半径全波模型；AORSA 作者的[电导率修正说明](https://nstx.pppl.gov/DragNDrop/Science_Groups/core/TSGs/energetic_particles/archive/2011/RF%20Conference%202011/Abstracts/Contributed%20Abstracts/Poster%20Session%20A/A49_Jaeger_E_.pdf)区分 $k_\perp\rho$ 与 $\rho/L_{\rm eq}$ 两种展开参数。选择全波应来自具体的波效应需求，而非把求解器名称当作无近似的保证。

### 获取与运行依赖

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| GENRAY / GRAY | [GENRAY](https://github.com/compxco/genray/blob/master/LICENSE)为 GPL-3.0-or-later；[GRAY](https://baltig.cnr.it/ectoplasm/gray/-/blob/master/LICENSE.md)采用自有用户协议，含非商业研究及修改限制 | 分别核对用途和修改条件，不能由公开仓库推断相同许可 |
| AORSA / TORIC | [AORSA](https://raw.githubusercontent.com/ORNL-Fusion/aorsa/master/LICENSE)所核仓库为 MIT；TORIC 本次未确认独立发行许可 | 核对实际发行方、平台协议和依赖 |

### 计算图解

![传播模型与速度空间分布之间的接口。](/assets/diagrams/sim-rf-models.svg)

传播模型与速度空间分布之间的接口。

## 弹跳平均 Fokker–Planck 与电流

### CQL3D 与 LUKE 的输入输出

| 软件 | 物理层级 | 主要输出 | 模型边界与比较重点 |
| --- | --- | --- | --- |
| [CQL3D](https://www.compxco.com/cql3d.html) | 相对论、弹跳平均的碰撞/准线性 FP；常用两动量维加一径向维 | 非热电子/离子分布、加热、电流驱动和相关诊断量 | 名称中的 3D 不表示三维空间全轨道；RF 扩散和几何须由对应模型或上游求解器提供 |
| [LUKE](https://spcgit.epfl.ch/luke/tutorial.html) | 所引教程为相对论、弹跳平均电子 FP，一空间维加两动量维 | 电子分布、电流驱动与相关响应 | 核对背景、碰撞线性化、波输入、电场和输运；该教程基于 MATLAB |

强非热情形中，场给出准线性扩散，分布改变吸收和介电响应，二者可能需要迭代。比较功率时统一天线/入射面、反射、金属/介质损耗、电子/离子吸收和出域功率。频域复场采用峰值幅度时，周期平均功率密度（W/m³）常写为 $\tfrac12\operatorname{Re}(\mathbf J\cdot\mathbf E^*)$；采用 RMS 幅度时因子相应改变，必须跟随软件约定，例如 [HFSS 的相量说明](https://ansyshelp.ansys.com/public/views/secured/electronics/v261/en/subsystems/HFSS/Content/HFSS/PeakVersusRMSPhasors.htm)。RF—FP 功率矩的核对方法见[多物理耦合](../多物理耦合/README.md)。

### 获取与运行依赖：弹跳平均 Fokker–Planck 与电流

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| CQL3D | [官方许可](https://raw.githubusercontent.com/compxco/cql3d/master/LICENSE)为 GPL-3.0-or-later | 实际发行方、平台协议和依赖分别核对 |
| LUKE | 本次未确认独立发行许可 | 核对实际发行方、平台协议和 MATLAB 等运行依赖 |

[返回仿真计算总览](../README.md)
