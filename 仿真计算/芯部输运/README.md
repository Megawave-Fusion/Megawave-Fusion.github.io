# 芯部输运与剖面演化

分别讨论实验收支、稳态通量匹配、快速时序模型与湍流通量闭合。

## 解释性分析与预测性输运

### TRANSP、ASTRA 与 JINTRAC

芯部输运把三维磁几何约化成磁面平均方程。“1D”一般指径向输运；“1.5D”常指径向输运与二维轴对称平衡联用，具体含义应查软件定义。解释性分析输入实测剖面，反推出满足粒子、能量和动量收支所需的通量；预测性分析给定闭合和源项，再演化未知剖面。同一个平台可以在不同通道分别采用这两种模式，比较前应列清哪些量被实验固定。

| 软件或平台 | 主要求解任务 | 适合怎样使用 | 比较时的关键条件 |
| --- | --- | --- | --- |
| [TRANSP](https://arxiv.org/abs/2406.07781) | 托卡马克粒子、功率、动量收支及电流扩散，包含加热、电流驱动和预测模块 | 有完整诊断和执行器输入的放电分析；结合 NUBEAM 研究快离子与加热收支 | 把解释与预测通道、采用的平衡、加热模块、输运闭合和实验约束逐项列出 |
| [ASTRA](https://w3.pppl.gov/~hammett/work/2009/Astra_ocr.pdf) | 通过模型描述语言和模块组织输运问题，原报告给出一维输运与二维平衡的闭合 | 检验自定义通量/源项假设，组织已有装置模型 | 本表采用 2002 年原报告的框架定义；现代发行版、插件和接口需另核对，不能照抄旧安装要求 |
| [JINTRAC：JETTO/SANCO 与 EDGE2D/EIRENE](https://scientific-publications.ukaea.uk/wp-content/uploads/MILITELLO_ASP_2022_NUCL-_FUSION_62_126033.PDF) | 芯部输运和杂质与 SOL/偏滤器多流体—中性粒子耦合 | 研究芯边界、加料、杂质和排热相互反馈 | 核对接口位置、返流/回收、原子数据、边缘输运系数与实际启用的子模块 |

### 获取与运行依赖

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| TRANSP | [发布页](https://transp.pppl.gov/releases.html)要求签协议，[现行协议文本](https://transp.pppl.gov/files/LicenseAgreement.pdf)区分研究与商业使用 | 按实际发行方的协议与装置数据权限配置工作流 |
| JINTRAC | [UKAEA 公开应用论文](https://scientific-publications.ukaea.uk/wp-content/uploads/UKAEA-CCFE-CP2525.PDF)明确按许可使用 | 具体发行包、子模块与运行依赖分别落实 |
| ASTRA | 本次未确认现代发行许可 | 历史报告不可替代当前条款 |

## 稳态通量匹配与 TGYRO
### 从源项积分确定所需通量

| 软件或平台 | 主要求解任务 | 适合怎样使用 | 比较时的关键条件 |
| --- | --- | --- | --- |
| [TGYRO](https://gafusion.github.io/doc/tgyro/solver.html) | 迭代梯度，使新经典与湍流通量满足稳态源项积分 | 在给定边界温度、密度和源项下求稳态剖面，比较通量闭合 | 官方算法以 $\partial_t=0$ 为目标；稳态通量匹配不能直接解释整个升流、加热、降流时序 |

在固定几何、无旋转功项、且只考虑净热源 $S$ 的简化磁面平均能量方程中，令 $r$ 为有长度单位的径向标签，$V'=dV/dr$，$Q$ 为使总径向输运功率等于 $V'Q$ 的通量定义。稳态下

$$
\frac{1}{V'}\frac{d(V'Q)}{dr}=S,
\qquad
P(r)=V'(r)Q(r)=\int_0^r V'(x)S(x)\,dx,
$$

其中取磁轴处净流出功率为零。积分源项给出所需输运功率，再调整剖面梯度，使选定输运闭合给出的 $Q$ 与之匹配。这是 [TGYRO 稳态求解算法](https://gafusion.github.io/doc/tgyro/solver.html)背后的守恒结构；实际多物种求解还须加入各自的交换和源项。

若在某磁面内净热源积分为 4.0 MW，而离散通量给出 3.8 MW，定义功率残差 $R_P=P_{\rm transport}-P_{\rm source}$，则 $R_P=-0.2$ MW，相对源功率为 $-5\%$。即使温度曲线几次迭代几乎重合，这个预算仍未闭合。源项误差、台基边界误差与求解残差应分别报告；收紧非线性容差只会降低其中一部分。

### 获取与运行依赖：稳态通量匹配与 TGYRO

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| TGYRO | [GACODE 主仓库](https://github.com/gafusion/gacode/blob/master/LICENSE)为 Apache-2.0 | 实际调用的通量模型与数据输入分别配置 |

### 计算图解

![稳态圆柱源积分的解析示意，不是 TGYRO 算例。](/assets/diagrams/sim-transport.svg)

稳态圆柱源积分的解析示意，不是 TGYRO 算例。

## 快速输运与控制模型

### RAPTOR 与 TORAX 的时间轨迹

| 软件或平台 | 主要求解任务 | 适合怎样使用 | 比较时的关键条件 |
| --- | --- | --- | --- |
| [RAPTOR](https://crppwww.epfl.ch/~sauter/raptor/) | 面向快速执行、实时状态估计和非线性优化的径向输运 | 控制器开发、放电轨迹和可观测性研究 | 闭合的简化程度、观测器输入和执行器模型决定可用范围；实时性要在指定硬件与算例上测量 |
| [TORAX](https://arxiv.org/abs/2406.06718) | 基于 Python/JAX 的可微芯部输运，推进离子/电子热、粒子与电流扩散方程 | 快速参数扫描、梯度优化、代理模型与输运方程联用 | 区分给定的几何/源项与在线求解量；自动微分覆盖范围取决于所接模块是否可微 |

TORAX 的具体物理配置可查 [v1.4.3 的模型页](https://torax.readthedocs.io/en/v1.4.3/physics_models.html)及[版本发布记录](https://github.com/google-deepmind/torax/releases)：加热源、台基、旋转和边缘约化模块按版本配置。输入一串 EQDSK 并进行几何插值，与在每个时间步重新求自由边界平衡是两种不同的耦合方式。更换源模型或调用外部程序时，应重新检查导数、求解器配置和计算开销。

### 获取与运行依赖：快速输运与控制模型

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| RAPTOR | [官方页](https://crppwww.epfl.ch/~sauter/raptor/)仍要求签转移/CLA 协议 | 获取申请与团队支持周期计入项目安排 |
| TORAX | [主体仓库](https://github.com/google-deepmind/torax/blob/main/LICENSE)为 Apache-2.0 | 第三方数据另列许可，实际配置与依赖按所用版本核对 |

## 准线性输运与代理模型

### TGLF、QuaLiKiz 与教师模型

输运平台本身不唯一决定湍流预测。相同的输运方程，换用常数扩散、TGLF、QuaLiKiz、非线性 gyrokinetic 通量或神经网络代理，会得到不同的剖面与误差结构。

| 模型 | 怎样得到输运通量 | 相比直接非线性计算省下什么 | 需要保留的模型信息 |
| --- | --- | --- | --- |
| [TGLF](https://gafusion.github.io/doc/tglf.html) | 求解 gyro-Landau-fluid 线性模，配合准线性权重和饱和规则 | 约化速度空间响应，并用饱和规则表示非线性通量水平 | 饱和规则、波数范围、几何、电磁项和 $E\times B$ 剪切选项 |
| [QuaLiKiz](https://arxiv.org/abs/1708.01224) | 约化的准线性 gyrokinetic 模型，输出热、粒子与动量通量 | 用约化模结构和饱和模型，减少直接演化非线性湍流的工作量 | 模型版本、适用的局部参数与几何、碰撞和旋转处理 |
| [QLKNN](https://arxiv.org/abs/2105.01168) 等代理 | 学习已有物理模型的数据映射 | 避免每次调用原模型求解 | 教师模型、训练域、特征归一化、阈值附近误差和域外检测 |
| 非线性 gyrokinetic 通量 | 在指定方程与排序下直接演化湍流并做统计平均 | 保留所解析尺度上的非线性相互作用 | 相空间分辨率、尺寸、碰撞、饱和时间、平均窗和统计误差 |

TGLF 是 gyrofluid 线性响应加通量闭合，QuaLiKiz 是约化 gyrokinetic 准线性模型；二者的相似输出不表示采用同一组方程。代理模型对教师的拟合误差、教师对实验的偏差、输运迭代引入的误差应分别记录。阈值附近一点通量误差可能移动温度梯度；在刚性输运区，通量差异与最终剖面差异也未必成比例。对代理可先做独立参数留出，再在相同边界和源项下比较整段输运轨迹，最后检查独立放电。

### 获取与运行依赖：准线性输运与代理模型

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| TGLF | [GACODE 主仓库](https://github.com/gafusion/gacode/blob/master/LICENSE)为 Apache-2.0 | 模型与数据输入分别配置；更新饱和规则后重跑基准 |
| QuaLiKiz / QLKNN | [QuaLiKiz](https://gitlab.com/qualikiz-group/QuaLiKiz/-/blob/main/LICENSE)为 CeCILL-C；QLKNN 按具体模型的发行包核对 | QLKNN 的代码、权重与训练数据分别核对 |

[返回仿真计算总览](../README.md)
