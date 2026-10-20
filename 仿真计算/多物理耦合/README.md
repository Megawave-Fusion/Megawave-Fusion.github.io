# 多物理耦合与数据接口

围绕状态表达、坐标单位、功率矩与保守映射，逐个建立可核对的模块接口。

## 多物理耦合与数据接口

### IMAS、OMAS 与 OMFIT 的层级

[IMAS Data Dictionary](https://imas-data-dictionary.readthedocs.io/en/latest/intro.html)定义 Interface Data Structures（IDS），规定数据含义、单位和坐标；访问层负责读写这些结构。[ITER 2025 年的开放发布公告](https://www.iter.org/node/20687/release-imas-infrastructure-and-physics-models-open-source)涉及基础设施和逐步发布的物理软件，应逐仓库核对许可及依赖。数据结构、模型接口和运行环境共同组成工作流。

[OMFIT 的 STEP](https://www.omfit.io/modules/mod_STEP.html)通过 OMAS 组织状态，将稳定性、输运、平衡和台基计算按步骤连接并保存历史。其[安装说明](https://omfit.io/install.html)明确指出，OMFIT 本体不包含模块调用的所有外部程序；可访问一个界面，不等于已经获得 EFIT、TRANSP 或其他求解器与数据库。软件目录、实际安装和输入数据是三份需要对应的清单。

| 层级 | 负责的工作 | 接口成功之后仍要检查什么 |
| --- | --- | --- |
| 物理求解器 | 解给定方程、生成通量/源项/平衡等 | 方程项、闭合、守恒、分辨率和模型适用性 |
| IMAS/IDS、OMAS 等数据表达 | 描述物理字段、坐标、版本和读写 | 源程序是否按字段定义填值、坐标变换和归一化是否正确 |
| OMFIT/STEP 等工作流 | 准备输入、调用程序、调度迭代、保存状态 | 模块是否真正启用、收敛条件、失败传播及状态是否过期 |
| HPC/容器/作业系统 | 提供依赖与计算资源 | 二进制、驱动、MPI、随机性与结果可重复程度 |

IMAS-Python 的 [IDS validation](https://imas-python.readthedocs.io/en/latest/validation.html)检查时间模式及坐标维度等一致性。字段形状正确后，仍需另算功率积分、物种收支及方向约定，才能判断两段程序在物理上是否闭合。

### 获取与运行依赖

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| OMFIT / IMAS | [OMFIT](https://omfit.io/install.html)要求用户协议并授予仓库权限；[IMAS](https://www.iter.org/node/20687/release-imas-infrastructure-and-physics-models-open-source)已发布多项开放组件 | OMFIT 不附带所有外部程序；IMAS 许可按各基础设施/物理软件仓库与版本核对 |

## 磁坐标、方向与单位转换

### COCOS、磁通与 CGS/SI

同名径向坐标可能表示几何半径、归一化极向磁通或归一化环向磁通的平方根。例如 $\psi_N=(\psi-\psi_a)/(\psi_b-\psi_a)$ 与 $\rho_{\rm tor}=\sqrt{(\Phi-\Phi_a)/(\Phi_b-\Phi_a)}$ 定义不同，不能只改列名就互换；应由同一个平衡给出映射和体积 $V$。下标 $a,b$ 分别表示磁轴与所选边界。

[COCOS 原论文](https://www.epfl.ch/research/domains/swiss-plasma-center/wp-content/uploads/2018/10/Sauter_COCOS_Tokamak_Coordinate_Conventions.pdf)系统区分磁通是否含 $2\pi$、坐标定向和电流/磁场符号。它们会影响 $q$、$F=RB_\phi$、平行波数和同向/反向电流驱动。接口至少保存输入与输出 COCOS、磁通单位、磁轴/边界取值、环向角正向和电流定义，并对一个已知磁场方向的点做向量检查。

[TGYRO 方程与单位表](https://gafusion.github.io/doc/tgyro/equations.html)是实际例子：部分内部量使用 CGS，而本库工程预算使用 SI。由 $1\,\mathrm{erg}=10^{-7}$ J、$1\,\mathrm{cm^2}=10^{-4}$ m²、$1\,\mathrm{cm^3}=10^{-6}$ m³，有

$$
1\,\frac{\mathrm{erg}}{\mathrm{s\,cm^2}}=10^{-3}\,\mathrm{W\,m^{-2}},\qquad
1\,\frac{\mathrm{erg}}{\mathrm{s\,cm^3}}=0.1\,\mathrm{W\,m^{-3}}.
$$

因此 $2\times10^8\,\mathrm{erg\,s^{-1}\,cm^{-2}}$ 对应 $0.20\,\mathrm{MW\,m^{-2}}$。粒子能量、温度能量和归一化热通量也分别恢复单位；写在图上的“功率”必须明确是体积密度、面积通量、磁面输运通量还是已积分功率。

## 空间重映射与耦合步长
### 空间与时间接口

磁通坐标中的密度必须与正确体积元配套；极向磁通与环向磁通各有自己的坐标变换。保守重映射要求输出网格上的积分与输入预算一致。点值插值看起来平滑，仍可能改变总功率。将二维沉积投影为一维磁面平均会丢失环向和极向结构，应说明这种约化对局部热点或不稳定性是否适用。

耦合时间步需解析被关心的反馈时间尺度。隐式或松弛迭代用于改善数值收敛；可保存各物种能量残差、粒子残差和迭代变化量，检查更细耦合步长下的目标量是否稳定。

### 保守重映射算例

把源网格上的单元平均体热源 $s_i$（W/m³）映射到目标单元 $j$，若各单元内用常数重构，可按交叠体积写成

$$
\widetilde s_j=\frac{1}{\Delta\widetilde V_j}
\sum_i s_i\,\Delta V_{ij}^{\rm overlap}.
$$

对所有目标单元乘体积并求和，若新旧网格覆盖同一计算域，且交叠部分没有重复或遗漏，则 $\sum_j\widetilde s_j\Delta\widetilde V_j=\sum_i s_i\Delta V_i$。这是对控制体积分的直接分配；若物理边界改变，移出域的功率需另列。

用累计体积 $V$ 作坐标，原网格边界为 $(0,1,4)$ m³，平均热源为 $(2,1)$ MW/m³，总功率为 $2\times1+1\times3=5$ MW。新网格为 $(0,2,4)$ m³，第一个单元接收 $2\times1+1\times1=3$ MW，第二个接收 2 MW，得到平均值 $(1.5,1)$ MW/m³，总功率仍为 5 MW。

若对原单元中心 $V=(0.5,2.5)$ 的热源做线性点值插值，并在右端使用常数外延，新中心 $V=(1,3)$ 得到 $(1.75,1)$ MW/m³，积分为 5.5 MW，比原值多 10%。曲线平滑没有保证功率一致。高阶映射还可进一步检验非负性、极值和局部矩；此处的分片常数例子只展示守恒结构。

守恒积分与通量定义可对照 [TGYRO 方程说明](https://gafusion.github.io/doc/tgyro/equations.html)。

### 计算图解

![单元平均源按体积重叠重映射，积分功率均为 5 MW。](/assets/diagrams/sim-coupling.svg)

单元平均源按体积重叠重映射，积分功率均为 5 MW。

## RF、分布与输运的功率闭合

### RF 算子能量矩

射频场给出波粒能量交换和扩散系数；分布函数改变介电响应、碰撞功率和电流；输运改变温度、密度及共振位置。迭代耦合把这些更新传回上游，形成场、分布与剖面之间的反馈。最小接口应写明物种、坐标、体积元、功率单位、归一化、时间窗和损失口径。

用非相对论动能 $m_sv^2/2$ 定义 RF 算子贡献时，可检查

$$
P_{\mathrm{RF}\to s}^{\mathrm{FP}}
=\int dV\int d^3v\,\frac{m_sv^2}{2}\,Q_{\mathrm{RF},s}[f_s].
$$

这一功率矩的推导是对分布演化中的 RF 部分 $\partial_tf_s|_{\rm RF}=Q_{{\rm RF},s}$ 乘单粒子动能，再在相空间积分。速度、位置坐标不随时间变化时，时间导数可移出积分，左边就是该算子造成的动能变化率；若使用扩散算子，还可分部积分把能量变化写成扩散通量做功，必须同时保留或明确令零速度空间边界通量。

它应与同一物种、同一体积内的波吸收功率一致，精度受离散和耦合残差限制；相对论计算需换成相对论动能，动量坐标需换积分测度。快离子吸收进入快粒子库，其对背景的碰撞加热是两个能量库之间的转移。是否把逃逸粒子和边界通量纳入预算也须明确。

[Frank 等 2022 原论文摘要](https://arxiv.org/abs/2207.09011)报告了 TORLH 与 CQL3D 的功率自洽耦合，并指出其所研究的 C-Mod 情形中，全波修正未解释全部实验差异。本次读取摘要，只引用这一方法与结论边界，不据此断言所有 LHCD 场景都可忽略全波效应。

### 从单向源项到反馈迭代

**加热方案与放电剖面。** 先用指定平衡和实测或设计剖面计算 RF/NBI 的分物种源项，传入输运模型；剖面变化后更新波吸收、束出生和碰撞交换，必要时再更新平衡。先固定几何、核对单向功率映射，再增加反馈，能够定位每个接口的误差。用 TORAX/RAPTOR 做优化时，可在少量代表性状态上与所选波、轨道或输运教师模型对照，保存代理调用范围。

## 快粒子与热库的能量交换

### 两个能量库的解析算例

设快粒子能量库为 $W_f$、热等离子体能量库为 $W_t$。将快粒子慢化近似为时间常数 $\tau_f$、热损失近似为 $\tau_E$，则

$$
\dot W_f=P_{\rm inj}-W_f/\tau_f,\qquad
\dot W_t=W_f/\tau_f-W_t/\tau_E.
$$

相加后交换项消去，$\dot W_f+\dot W_t=P_{\rm inj}-W_t/\tau_E$，因而耦合接口的同一份沉积功率在两边分别是损失和增益。对瞬时注入后 $P_{\rm inj}=0$、$W_f(0)=W_0$、$W_t(0)=0$，先解第一个指数衰减，再对第二式用积分因子，得到

$$
W_f=W_0e^{-t/\tau_f},\quad
W_t=W_0\frac{\tau_E}{\tau_E-\tau_f}
\left(e^{-t/\tau_E}-e^{-t/\tau_f}\right).
$$

上述两指数式适用于 $\tau_E\ne\tau_f$。当 $\tau_E=\tau_f=\tau$ 时，积分因子直接给出 $W_t=W_0(t/\tau)e^{-t/\tau}$，也等于两指数式的连续极限；此时热能峰值位于 $t=\tau$。

教学取 $W_0=1.0$ MJ、$\tau_f=0.050$ s、$\tau_E=0.20$ s，$t=0.10$ s 时分别有 0.1353 MJ 和 0.6283 MJ，已损失的热量为 0.2364 MJ，三者相加为初始 1.0 MJ。令 $\dot W_t=0$ 可得热能峰值时刻 $\ln(\tau_E/\tau_f)/(1/\tau_f-1/\tau_E)=0.0924$ s。快粒子向电子和离子的真实慢化分配见 [IAEA《Fusion Physics》§5.1.4，书页 543–545 的能量转移](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)；这里用一阶能量库提取了耦合中必须满足的守恒结构。

[返回仿真计算总览](../README.md)
