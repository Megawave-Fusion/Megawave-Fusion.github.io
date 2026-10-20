# 边缘输运与偏滤器

把平均排热和中性粒子收支，与三维涨落及局部瞬态分开建模。

## 平均输运与动理学中性粒子
### SOLPS-ITER 与 UEDGE

SOL 和偏滤器需要处理沿场输运、鞘层、原子分子过程、回收、杂质与辐射。平均输运模型通常需要给定横场扩散系数；三维湍流模型解析部分涨落，但仍需选择平行热流、中性粒子和边界闭合。

| 软件 | 等离子体和中性粒子处理 | 典型用途 | 关键差异与输入 |
| --- | --- | --- | --- |
| [SOLPS-ITER](https://solps-tutorials.readthedocs.io/) | 标准工作流为二维轴对称 B2.5 多流体与 EIRENE Monte Carlo 中性粒子耦合 | 偏滤器排热、脱靶、杂质/辐射、回收与抽气 | [横场粒子与热扩散系数](https://solps-tutorials.readthedocs.io/feature_blog/Diffusion_coefficients/)是模型输入；应检查网格、反应库及中性粒子统计 |
| [UEDGE](https://github.com/LLNL/UEDGE) | 二维等离子体及中性气体流体，有限体积与全隐式求解 | 边缘稳态扫描和瞬态输运 | 中性流体闭合与 EIRENE 的动理学中性模型不同；横场反常输运也需设定 |

若目的是给靶板平均热流和中性压力做扫描，可先在平均输运模型中约束上游剖面、回收和辐射；若目的是解释 blob、间歇性负荷或横场输运机制，则需要相应的三维涨落模型与合成诊断。拟合实验得到的 $D_\perp,\chi_e,\chi_i$ 能解释该工况，不自动构成对新工况的预测能力。

### 芯部到靶板的负荷交接

**芯部—偏滤器—壁。** 芯部给出越过分界面的功率与粒子流，边缘模型结合加料、回收和抽气返回上游状态、杂质和辐射；靶面热流再投影到实际 CAD 表面，交给热结构求解。检查闭合面和控制体边界，防止把辐射、回收能量或快粒子损失重复计入。该链可与[腔体材料](../../腔体材料/README.md)及[工程系统](../../工程系统/README.md)的载荷定义联用。

### 获取与运行依赖

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| SOLPS-ITER / EIRENE | [SOLPS-ITER](https://github.com/iterorganization/SOLPS-ITER)已公开、顶层 EUPL-1.1；[安装说明](https://solps-tutorials.readthedocs.io/installing/solps-iter-codebase/)仍要求确认 EIRENE 注册/许可 | [EIRENE](https://www.eirene.de/cgi-bin/eirene/write_temp.cgi?temp_dat=Download/download)列专用 EPL 或 CC BY-NC-ND 条款，不能只看顶层仓库；反应数据也应登记 |
| UEDGE | [官方仓库](https://github.com/LLNL/UEDGE)为 LGPL-2.1 | 核对实际模型、输入数据与运行依赖 |

### 计算图解

选定控制体后，用同一参考面记功率：

$$
P_{\rm in}=P_{\rm target}+P_{\rm radiation}+P_{\rm other}+\frac{dW}{dt}.
$$

$P_{\rm other}$ 汇总穿出其他边界的净能流；荷交换和中性粒子功率需按控制体计入相应项，避免把内部交换重复当损失。

![平均边缘模型与中性粒子模型的数据交接。](/assets/diagrams/sim-edge.svg)

平均边缘模型与中性粒子模型的数据交接。

## 边缘涨落与多物种流体

### BOUT++、Hermes-3 与 SOLEDGE3X

| 软件 | 等离子体和中性粒子处理 | 典型用途 | 关键差异与输入 |
| --- | --- | --- | --- |
| [BOUT++](https://bout-dev.readthedocs.io/en/latest/user_docs/introduction.html) / [Hermes-3](https://hermes3.readthedocs.io/en/latest/) | 曲线坐标流体框架 / 建立其上的多物种边缘模型，可配置维度与稳态、瞬态、湍流任务 | 边缘流体、涨落与模型开发 | 指明具体模型、物种、方程和组件；Hermes-3 的[中性流体闭合](https://hermes3.readthedocs.io/en/latest/equations.html)也须按维度选择 |
| [SOLEDGE3X](https://soledge3x.onrender.com/features/fluid_description/) | 漂移序多流体；所引方程页采用静电固定磁场，可运行平均输运或相应湍流问题 | 边缘输运、回收与壁相互作用 | [中性模型](https://soledge3x.onrender.com/features/neutrals/)可用简化扩散或经 STYX 耦合 EIRENE，不能把两种计算等量齐观 |

三维涨落计算需要说明被解析的时间与波数范围，同时给出平行热流、鞘层、中性粒子和材料边界条件。先在简化几何中核对粒子与能量收支，再增加回收和原子过程。框架中的组件可以分别启停，算例应保存实际启用的方程及输入，而不是只写框架名称。

### 获取与运行依赖：边缘涨落与多物种流体

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| BOUT++ / SOLEDGE3X | [BOUT++](https://bout-dev.readthedocs.io/en/latest/user_docs/introduction.html)为 LGPL-3.0-or-later；[SOLEDGE3X](https://soledge3x.onrender.com/)按需获取 | BOUT++ 的具体应用与模型另查；SOLEDGE3X 未核实标准开源许可，不从论文开放性推断 |

[返回仿真计算总览](../README.md)
