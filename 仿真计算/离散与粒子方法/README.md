# 数值离散与粒子方法

用离散守恒和稳定性条件理解网格方法；用宏粒子循环理解通用 PIC 的统计与时间尺度。

## 有限差分、有限体积与守恒步
### 控制体与公共面通量

有限差分近似网格点上的导数；有限体积对控制体积分，用单元面通量更新体平均量。若内部公共面的通量在相邻单元取同值反号，总和中会相消，这正是离散守恒的重要结构。高阶重构、复杂边界或插值仍可能破坏正性、稳定性或整体守恒，需要单独测试。BOUT++ 官方将自身描述为曲线坐标下的结构化有限差分/体积框架，物理方程由模型指定；示例含流体与湍流模型。参见 [BOUT++ Introduction](https://bout-dev.readthedocs.io/en/stable/user_docs/introduction.html) 和 [Physics models](https://bout-dev.readthedocs.io/en/latest/user_docs/physics_models.html)。每套方程实现都可分别建立解析解和守恒测试。

### 迎风更新与 CFL 算例

考虑常速 $v>0$ 的一维输运 $\partial_tu+\partial_x(vu)=0$。对宽度 $\Delta x$ 的单元积分，单元平均量的变化等于左端流入减右端流出。取迎风界面通量 $F_{i+1/2}=vu_i^n$，用显式时间积分得到

$$
u_i^{n+1}=u_i^n-\nu(u_i^n-u_{i-1}^n)
=(1-\nu)u_i^n+\nu u_{i-1}^n,\qquad
\nu=\frac{v\Delta t}{\Delta x}.
$$

当 $0\leq\nu\leq1$，更新值是两个旧值的凸组合，故保留非负性并保持在相邻值范围内。周期边界下对所有单元求和，通量相邻抵消，总量严格守恒。教学取四单元初值 $(0,1,2,1)$、$\Delta x=0.10$ m、$v=2.0$ m/s、$\Delta t=0.025$ s，$\nu=0.5$，更新为 $(0.5,0.5,1.5,1.5)$；以任意一致的密度单位计，积分总量均为 $0.4$。将时间步增至 $\nu=1.2$ 时，第二单元变为 $-0.2$，凸组合条件随之失效。[Clawpack《Advection》的 Conservation of mass 与 Riemann problem 两节](https://www.clawpack.org/riemann_book/html/Advection.html)给出守恒形式及迎风信息来源；以上离散步由这两个性质直接构造。

### 计算图解

![从连续方程到离散误差的检验链。](/assets/diagrams/sim-numerics.svg)

从连续方程到离散误差的检验链。

## 通用电磁 PIC 的软件与采样

### 完整快速动理学的求解范围

完整 Vlasov–Maxwell PIC 保留快速电磁和粒子动力学，适合激光—等离子体、局部不稳定性或特定动理学机制。它与磁约束长期输运所用的回旋平均模型在解析尺度上不同；将电子快速尺度一直积分到宏观放电时间通常带来巨大的成本。

| 软件 | 本次核对的定位 | 选择依据 |
| --- | --- | --- |
| [Smilei](https://smileipic.github.io/Smilei/) | 通用相对论 PIC，官方算法说明宏粒子、网格 Maxwell 与 PIC 循环 | 适合需要完整快速动理学的课题，核对维度、碰撞、边界及粒子诊断 |
| [WarpX](https://warpx.readthedocs.io/en/latest/) | 通用 PIC，提供不同电磁、静电及混合场路径，并有网格加密和 CPU/GPU 运行能力 | 按具体算法、网格层级、硬件和版本做基准；具有聚变反应模块不等于具备整次托卡马克放电模型 |
| [EPOCH](https://github.com/epochpic/epoch) | 提供一、二、三维实现的等离子体 PIC 软件 | 可作为快速动理学问题的候选；本次只核对公开仓库定位与许可，具体扩展模块需继续阅读对应手册 |

### 宏粒子、网格与推进循环

PIC 用带权宏粒子表示分布，并在网格上求场。一个循环包含粒子处场插值、粒子推进、电荷/电流沉积和场更新。宏粒子代表具有给定统计权重的粒子群；统计噪声、网格加热、时间步误差和边界处理都影响结论。应分别扫描网格、时间步、每格粒子数和随机种子；显式电磁算法还需满足其稳定性约束。上述算法路径已核对 [Smilei 5.1 PIC algorithms](https://smileipic.github.io/Smilei/Understand/algorithms.html) 的 Quasi-particles、Time and space discretization 与 PIC loop，稳定条件由所选时间推进和场求解算法确定。

### 获取与运行依赖

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| Smilei / WarpX / EPOCH | [Smilei](https://smileipic.github.io/Smilei/Overview/licence.html)为 CeCILL-B；[WarpX](https://github.com/BLAST-WarpX/warpx)为 BSD-3-Clause-LBNL；[EPOCH](https://github.com/epochpic/epoch)为 GPL-3.0 | 对照实际求解器与加速器后端、物理模块和输入数据 |

[返回仿真计算总览](../README.md)
