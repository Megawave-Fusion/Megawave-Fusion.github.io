# 陀螺动理学与湍流

按扰动排序、径向范围和分布离散方式选择模型，再比较线性模与非线性通量。

## 扰动、全分布与局部全局模型
### 三个互相独立的模型维度

这组软件要沿三个独立维度比较。采用 $\delta f$ 时，在相应扰动排序下把分布分成背景与主要演化的小扰动；full-$f$ 演化总分布；局部 flux-tube 在小径向区域采用给定平衡量与梯度，全局模型保留径向剖面变化；Eulerian 在相空间网格上演化分布，PIC 用带权标记采样分布。全局模型可以采用 $\delta f$，PIC 也可以是 gyrokinetic PIC。full-$f$ 不取消 gyrokinetic 排序；采用长波近似时也仍受其约束。

回旋平均通常将分布的相空间从三位置、三速度降到三位置、两速度，但成本仍由空间、平行速度、磁矩/垂直能量、物种和时间共同决定。局部线性扫描、全局非线性饱和与电子/离子多尺度研究对应的计算量相差很大；仅按软件名称给出“几核几小时”缺少物理依据。报告预算时应给出目标量误差随自由度和统计时间的变化。

模型定义参见 [GENE 方法论文](https://www.genecode.org/PAPERS_2/JPCS_012011.pdf)与 [GTC 方法说明](https://sun.ps.uci.edu/people/zlin/bib/wong24.pdf)。

### 计算图解

![分别选择分布排序、径向范围和离散方式。](/assets/diagrams/sim-gyrokinetic.svg)

分别选择分布排序、径向范围和离散方式。

## 网格陀螺动理学软件

### GENE、GS2 与 CGYRO

| 软件 | 主要方程与表示 | 合适的研究任务 | 选择时应区分的点 |
| --- | --- | --- | --- |
| [GENE](https://genecode.org/details.html) | Eulerian 五维 gyrokinetic，经典表述为 $\delta f$，有局部与全局模式 | 线性微稳定性、非线性离子/电子尺度湍流、径向非局域效应 | 电磁项、碰撞、物种和托卡马克/仿星器几何按输入配置；global 不等同于 full-$f$ |
| [GS2](https://gyrokinetics.gitlab.io/gs2/) | 沿场线的局部 flux-tube、扰动分布网格 gyrokinetic | 给定磁面附近的增长率、模结构、饱和通量与共同基准 | 对照动理学/绝热电子、碰撞和几何；局部计算不直接给出整半径剖面演化 |
| [CGYRO](https://gafusion.github.io/doc/cgyro.html) | Eulerian、径向谱表示，当前官方说明包括 global-spectral 方案 | 碰撞、电磁、多尺度湍流和径向剖面变化研究 | 旧的“仅局部”概述已不完整；局部/全局算法与径向处理依实际版本和设置 |

GENE 的 $\delta f$、local/global 定义可查[方法论文](https://www.genecode.org/PAPERS_2/JPCS_012011.pdf)；CGYRO 的全局算法由官方[参考文献表中的 2025 年论文](https://gafusion.github.io/doc/zreferences.html)支持，比较时应记录实现版本。Gkeyll 的[简单 GK 鞘层例子](https://gkeyll.readthedocs.io/en/latest/quickstart.html)展示了长波静电 full-$f$ 的边界问题，但该例不含完整电离、复合和辐射，不能直接当作反应堆偏滤器模型。

### 获取与运行依赖

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| GENE / GS2 | [GENE](https://www.genecode.org/license.html)按个人学术申请，限制再分发，非学术另议；[GS2](https://bitbucket.org/gyrokinetics/gs2/raw/master/LICENCE)为 MIT | 电子模型、几何接口、编译库与输入基准分别配置；两个项目的许可条件分别核对 |
| CGYRO | [GACODE 主仓库](https://github.com/gafusion/gacode/blob/master/LICENSE)为 Apache-2.0 | 实际模型与数据输入分别配置 |

## 粒子与连续分布的全局动理学

### GTC 与 Gkeyll 的模型边界

| 软件 | 主要方程与表示 | 合适的研究任务 | 选择时应区分的点 |
| --- | --- | --- | --- |
| [GTC](https://sun.ps.uci.edu/people/zlin/bib/wong24.pdf) | 全局环形 gyrokinetic PIC，可用 $\delta f$ 或 full-$f$，有混合电子等模型 | 全局湍流、快粒子与 Alfvén 模相关研究 | 选定电子与电磁模型，并扫描标记数、随机性和数值噪声；PIC 不表示逐圈解析完整回旋运动 |
| [Gkeyll](https://gkeyll.readthedocs.io/en/latest/) | 当前公开 GK 模块为 full-$f$、长波极限、模态间断 Galerkin 分布网格，静电 GK-Poisson | 非 Maxwellian 分布、开场线与鞘层相关动理学问题 | 与其 Vlasov-Maxwell 模块、历史论文中的电磁扩展分开；实际可用功能以所选模块为准 |

GTC 的粒子标记和 Gkeyll 的分布网格带来不同的误差来源；比较时先统一电子模型、碰撞、场方程及边界。保留 full-f 并不取消所采用的低频或长波排序。Gkeyll 的[鞘层教学例](https://gkeyll.readthedocs.io/en/latest/quickstart.html)还需与包含电离、复合和辐射的实际边缘模型区分。

### 获取与运行依赖：粒子与连续分布的全局动理学

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| GTC | [官方入口](https://sun.ps.uci.edu/gtc/)列 BSD-3-Clause | 电子模型、几何接口、编译库与输入基准分别配置 |
| Gkeyll | [主仓库](https://github.com/gkeyllorg/gkeyll)为 MIT | 按 core/moments/vlasov/gyrokinetic 等实际模块及依赖构建 |

[返回仿真计算总览](../README.md)
