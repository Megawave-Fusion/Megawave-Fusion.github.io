# 聚变物理总览

本页按粒子、统计、波动、流体、燃烧和排热组织七个专题。各模型共用 SI、守恒边界与测量口径；先判断无量纲排序，再与可观测量比较。

| 建议顺序 | 专题 | 核心问题 |
| --- | --- | --- |
| 起点 | [等离子体基本概念](等离子体基本概念/README.md) | 温度能量、分布函数、准中性、屏蔽与集体尺度 |
| 粒子 | [单粒子运动](单粒子运动/README.md) | 回旋、漂移、磁矩、磁镜与绝热不变量 |
| 统计 | [动理学与碰撞](动理学与碰撞/README.md) | Vlasov、速度矩、闭合、碰撞与弛豫 |
| 集体扰动 | [等离子体波](等离子体波/README.md) | 色散、偏振、截止、共振和阻尼 |
| 宏观体系 | [流体与磁流体力学](流体与磁流体力学/README.md) | 双流体、MHD、磁通、平衡、能量与重联 |
| 燃烧 | [聚变反应与燃烧](聚变反应与燃烧/README.md) | 反应率、功率平衡、Lawson 条件、自加热与净电 |
| 输运与排热 | [输运与边界](输运与边界/README.md) | 新经典、湍流、台基、SOL、鞘层、脱靶和快粒子 |

复核覆盖范围和已修正问题见[核验记录](../核验记录.md)。除特别说明外采用 SI，温度能量用 $\Theta_s=k_BT_s$，以 eV 给出的温度能量先换算为 J 后代入 SI 公式。

## 聚变反应与能量收支

核反应释放能来自初末态静质量之差。D-T 每次反应约释放 17.6 MeV，其中约 3.5 MeV 由 alpha 携带、14.1 MeV 由中子携带。带电产物与中子有不同的沉积路径，因此聚变总功率、等离子体自加热和可回收工程热量需要分别列账。[NRL Plasma Formulary 2016，热核反应表](https://suli.pppl.gov/2016/course/NRL_FORMULARY_16.pdf)。

对热核 D-T，反应数率密度为 $R=n_Dn_T\langle\sigma v\rangle$。这里 $\sigma$ 是截面，而 $\langle\sigma v\rangle$ 已对速度分布平均；两者单位不同，前者是面积，后者是体积/时间。总功率为 $P_{\rm fus}=\int R E_{DT}\,dV$，必须把密度和温度剖面留在积分内部。束流、非热分布和不同离子温度会改变平均，平均时应使用反应物各自的分布函数。[Fitzpatrick：Nuclear Fusion Reactions](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node6.html)。

核算反应道与产物能量、准中性组分以及同一边界内的输入—储能—损失。相同粒子计数、燃料配比、稀释与剖面积分见[聚变反应与燃烧](聚变反应与燃烧/README.md)。

### 从反应计数到脉冲能量

在均匀体积 $V$ 内维持固定反应物密度与温度，时间 $dt$ 中的反应次数为 $dN=n_Dn_T\langle\sigma v\rangle Vdt$。逐次反应乘以释放能，再积分，得到

$$
N=n_Dn_T\langle\sigma v\rangle V\Delta t,\qquad
E_{\rm fus}=NE_{DT},\qquad P_\alpha=\frac{E_\alpha}{E_{DT}}P_{\rm fus}.
$$

取 $n_D=n_T=5\times10^{19}\,\mathrm{m^{-3}}$、给定反应率系数 $10^{-22}\,\mathrm{m^3s^{-1}}$、$V=10\,\mathrm{m^3}$、$\Delta t=2\,\mathrm s$。先算反应数率 $2.5\times10^{18}\,\mathrm{s^{-1}}$，再以 $17.6\,\mathrm{MeV}=2.81983\times10^{-12}\,\mathrm J$ 换算，得到 $P_{\rm fus}=7.05\,\mathrm{MW}$、$E_{\rm fus}=14.1\,\mathrm{MJ}$、alpha 出生功率 $1.40\,\mathrm{MW}$。维持此例的恒定密度需要补给每秒被消耗的 D、T，各为反应数率。若无补给，就应把 $dn_D/dt=dn_T/dt=-n_Dn_T\langle\sigma v\rangle$ 与功率一起积分。

推导起点见 [Fitzpatrick，核反应式 (1.3)–(1.6)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node6.html)；数值为本条给定参数的计算。

计数与能量守恒可合写为

$$
dN=n_Dn_T\langle\sigma v_r\rangle\,dV\,dt,\qquad
P_{\rm fus}=\int R E_{DT}\,dV,\qquad Q_{\rm nuc}=\Delta m\,c^2.
$$

## 约束与性能指标

![恒定加热与固定损失时间下的热储能解析响应](/assets/diagrams/basic-overview.svg)

*恒定加热与固定损失时间下的热储能解析响应。曲线与示意均按本条所列模型生成。*

磁约束通过粒子轨道和集体平衡限制跨场损失；惯性约束在燃料迅速解体前利用短暂高密度产生足够反应；磁惯性路线则在压缩与磁化之间组合条件。三者分别采用相应的损失模型和约束指标。[装置路线](../装置路线/README.md)进一步说明磁拓扑、驱动和工程代价。

能量约束时间常定义为 $\tau_E=W_{\rm th}/P_{\rm loss}$。若储能正在变化，$P_{\rm loss}=P_{\rm heat}-dW_{\rm th}/dt$；还需说明是否已经包含辐射。粒子约束、快粒子慢化和放电脉宽各描述不同过程。三乘积 $nT\tau_E$ 引用时必须给出密度物种、中心/平均温度、温度单位及是否同一时刻实现，并采用同一放电中相互对应的参数。[Wurzel 与 Hsu：Lawson 综述，§IV 的实验比较方法](https://arxiv.org/html/2105.10954v3)。

若用 $Q_p=P_{\rm fus}/P_{\rm ext}$，须明确 $P_{\rm ext}$ 是被吸收功率、注入边界功率，还是其他定义。电网消耗还涉及源效率与辅机；工程净电又涉及热循环。所谓“盈亏平衡”必须带上系统边界。温度、脉冲长度、增益和净供电共同构成性能评价。

### 由加热阶跃反推约束时间

固定有效损失时间 $\tau$，将零维方程写成 $dW/dt+W/\tau=P_0$。乘积分因子 $e^{t/\tau}$ 后，左端成为 $d(We^{t/\tau})/dt$，积分得

$$
W(t)=P_0\tau+[W(0)-P_0\tau]e^{-t/\tau}.
$$

关断热源且其他条件保持时，$P_0=0$，故 $\ln[W(t)/W(0)]=-t/\tau$。若储能从 12 MJ 在 0.30 s 内降到 8 MJ，得到 $\tau=0.30/\ln(12/8)=0.740\,\mathrm s$。重新施加恒定 10 MW 热源，稳态储能是 $P_0\tau=7.40\,\mathrm{MJ}$，从零储能经过一个 $\tau$ 达到其 63.2%。

这个解也说明拟合时应检查 $\ln W$ 是否随时间近似线性：若损失时间随温度改变，衰减曲线的局部斜率就是 $-1/\tau(W)$。定义依据为 [Fitzpatrick，Lawson Criterion，式 (1.11)–(1.14)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node7.html)；这里进一步给出了其恒系数时间解。

## 平衡与 MHD 稳定性

在静态、各向同性、忽略重力的单流体模型中，力平衡为 $\nabla p=\mathbf J\times\mathbf B$，并满足 $\nabla\cdot\mathbf B=0$ 与准静态 Ampère 定律。点乘磁场得到 $\mathbf B\cdot\nabla p=0$，所以压力沿磁力线不变；在适当嵌套磁面条件下可写为磁通函数。强流动、各向异性快粒子压强或三维磁岛会改变这一简化。

从 $\rho D_t\mathbf u=-\nabla p+\mathbf J\times\mathbf B$ 取静止极限，再点乘 $\mathbf B$，即得沿场压力恒定。比压定义为 $\beta=p/[B^2/(2\mu_0)]$。

稳定性须另给扰动与边界：允许扰动若有负势能变化，可指示理想失稳。电阻、动理学共振和反馈需扩展模型；宏观平衡也不排除微观湍流输运。

[流体与磁流体力学](流体与磁流体力学/README.md)逐项推导磁压力与张力、磁通冻结、Grad–Shafranov 磁通约定及电阻重联，并附原始课程和论文。阅读时应同时检查压力是否包含所有物种、磁场是局域值还是参考值、真空和壁的能量是否计入。无量纲 $\beta=2\mu_0p/B^2$ 是热压与磁压之比；稳定性上限由具体几何和剖面确定。

### 一维平板平衡的逐步求解

取 $\mathbf B=B_z(x)\hat{\mathbf z}$、$p=p(x)$，由 $\nabla\times\mathbf B=\mu_0\mathbf J$ 得 $J_y=-B_z'/\mu_0$。因而 $\mathbf J\times\mathbf B=-B_zB_z'\hat{\mathbf x}/\mu_0$，力平衡化为

$$
\frac{dp}{dx}=-\frac{B_z}{\mu_0}\frac{dB_z}{dx},\qquad
p+\frac{B_z^2}{2\mu_0}=C.
$$

设边缘压力可忽略、边缘磁场 $B_a=2\,\mathrm T$，中心压力 $p_0=0.20\,\mathrm{MPa}$。则 $B_0=\sqrt{B_a^2-2\mu_0p_0}=1.870\,\mathrm T$：中心增加的热压由减小的磁压补偿。用两个位置各自的 $p+B^2/(2\mu_0)$ 可直接核对结果，均为约 $1.592\,\mathrm{MPa}$。

这一构造是直磁场静态平衡；弯曲磁场还会引入磁张力。两者共同来自 Maxwell 应力张量，见 [Fitzpatrick，Magnetic Pressure，式 (8.9)–(8.12)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node105.html)。稳定性分析则从此平衡出发，再求扰动的时间演化。

## 等离子体波与波粒相互作用

线性波分析从规定的平衡分布与 Fourier 约定出发，求介电响应、极化和色散。冷等离子体模型说明截止与共振的位置，热吸收与非热尾部进一步由速度分布响应决定。天线耦合还需结合边界和传播路径计算。

Landau 共振比较波相速度与粒子的平行速度；回旋共振还涉及粒子回旋相位，典型形式为 $\omega-k_\parallel v_\parallel-l\Omega_s=0$。本式中 $\Omega_s=q_sB/m_s$ 为带符号角频率，$l$ 为整数；采用正频率约定的系统页面会另行说明极化与谐波符号。共振条件只是相互作用条件，净吸收或增长还由分布梯度、极化和阻尼决定。

沿轨道相位 $\psi=k_\parallel z+l\vartheta-\omega t$ 满足 $\dot\psi=k_\parallel v_\parallel+l\Omega_s-\omega$；持续相互作用要求 $\dot\psi\simeq0$，$l=0$ 即 Landau 共振。

[等离子体波](等离子体波/README.md)将 Langmuir、离子声、O/X、whistler 与 MHD 分支分开，并核对冷介电、功率与阻尼。[辅助加热](../辅助加热/README.md)再连接波传播、沉积、快粒子慢化和电流驱动。一个完整加热结论应说明发射功率、耦合功率、吸收对象与位置，而不只列发生器频率。

### 从阻尼振子理解吸收的相位

用单个线性模坐标 $x$ 表示受驱响应，取 $\ddot x+2\gamma\dot x+\omega_0^2x=(F_0/m)\cos\omega t$。采用 $x=\Re(Xe^{-i\omega t})$，复振幅法给出 $X=(F_0/m)/(\omega_0^2-\omega^2-2i\gamma\omega)$，速度振幅为 $-i\omega X$。将实力与实速度相乘并平均一个周期，得到

$$
\langle F\dot x\rangle=
\frac{F_0^2\gamma\omega^2/m}
{(\omega_0^2-\omega^2)^2+4\gamma^2\omega^2}
=2m\gamma\langle\dot x^2\rangle.
$$

右端是阻尼耗散，直接闭合驱动功率预算。取归一化 $m=F_0=\omega_0=1$、$\gamma=0.1$：在 $\omega=1$ 时平均吸收为 2.5；在 $\omega=0.8$ 时为 0.412。响应幅值、力与速度的相位共同决定做功。这里的 $\gamma$ 表示给定线性阻尼；具体等离子体的阻尼应从分布函数与介电响应求出。线性响应与周期平均功率的处理见 [Fitzpatrick，Dielectric constant of a collisional plasma，式 (1201)–(1205)](https://farside.ph.utexas.edu/teaching/em/lectures/node103.html)。

## 输运、边界与快粒子

跨磁面粒子、热与动量输运决定核心剖面如何响应源与损失。碰撞输运的局域闭合有自己的自由程条件；磁场几何带来的新经典输运、微不稳定性的湍流通量和中性粒子过程应分开建模，再组合为统一预算。有效扩散系数是对特定问题的描述，未必能移植到另一种扰动或几何。

在偏滤器构型中，核心损失经分离面进入 SOL，沿开放磁力线到达靶面。平行导热、鞘层加速、辐射、中性粒子和靶材响应共同决定局部负荷。边缘适量辐射可以帮助排热，核心杂质却可能损害反应率；优化时联合控制核心污染与边缘辐射分配。

[输运与边界](输运与边界/README.md)新增守恒、香蕉轨道、自举电流、湍流相位、台基、两点模型、鞘层与脱靶的连续讲解。快粒子部分同时讨论轨道与 Alfvén 共振，区分再分布、真正逸出和热背景沉积。这样才能把[加热](../辅助加热/README.md)、[诊断](../诊断控制/README.md)与[材料负荷](../腔体材料/README.md)放到同一个物理问题中。

### 把核心损失接到边界热流

考虑静态区域，输入的热功率为 $P_h$，区域内辐射为 $P_r$，则流出边界的导热与粒子能流之和为 $P_{\rm sep}=P_h-P_r$。若把流出功率中的比例 $f_t$ 分配给一个靶区，且该区面热流为 $q(s)=q_0e^{-s/\lambda_q}$、环向长度为 $L_t$，积分得到

$$
f_tP_{\rm sep}=L_t\int_0^\infty q_0e^{-s/\lambda_q}ds
=L_tq_0\lambda_q.
$$

取 $P_h=12\,\mathrm{MW}$、$P_r=4\,\mathrm{MW}$、$f_t=0.6$、$L_t=8\,\mathrm m$、靶面坐标中的衰减宽度 $\lambda_q=0.03\,\mathrm m$，可得峰值 $q_0=20\,\mathrm{MW\,m^{-2}}$。若在相同总功率下展宽到 0.06 m，峰值减半。这里指数剖面是明确指定的积分模型；功率分配、靶面宽度和磁通膨胀在真实计算中各自输入。

边界守恒与输运建模背景见 [Dudson 等，SD1D 粒子、能量与动量损失研究](https://scientific-publications.ukaea.uk/papers/the-role-of-particle-energy-and-momentum-losses-in-1d-simulations-of-divertor-detachment/)。

## 欧姆加热与自加热

在简化标量电阻 MHD 中，$\mathbf E+\mathbf u\times\mathbf B=\eta\mathbf J$，点乘电流可得

$$
\mathbf J\cdot\mathbf E
=\mathbf u\cdot(\mathbf J\times\mathbf B)+\eta J^2.
$$

左边是场对带电介质的总功率密度，第一项可转为整体机械能，第二项才是此模型中的焦耳热。标量电阻条件下 $P_{\rm Ohm}=\int\eta J^2dV$；若动理学响应、各向异性或强射频电场重要，就需使用相应广义模型。[流体与磁流体力学：能量守恒与欧姆加热](流体与磁流体力学/README.md)。

高温弱耦合 Maxwellian 等离子体的经典电阻率大致随 $T_e^{-3/2}$ 降低（还含有效电荷和 Coulomb 对数），所以给定电流密度下欧姆热会随温度升高减弱。这解释了进入高温工况为何需要辅助加热；低温部分电离阶段还要计入电子—中性粒子碰撞。[动理学与碰撞：经典热流与 Spitzer 电阻](动理学与碰撞/README.md)。

电子摩擦给 $eE\simeq m_e\nu_{ei}u_d$、$J=n_eeu_d$，故 $\eta=m_e\nu_{ei}/(n_ee^2)\propto Z_{\rm eff}\ln\Lambda\,\Theta_e^{-3/2}$。自加热份额由 $P_\alpha\simeq P_{\rm fus}/5$ 与 $P_{\rm ext}=P_{\rm fus}/Q_p$ 得 $f_\alpha\simeq Q_p/(Q_p+5)$。

D-T 自加热由反应产生的 alpha 先形成快粒子分布，再向热背景传能。若近似全部沉积且外部热输入定义一致，自加热份额约为 $Q_p/(Q_p+5)$，所以主导自加热与完全不依赖外部热输入的点火不同。欧姆、射频/束流、alpha 沉积各自有功率通道；内部碰撞传能在物种之间转移，对全系统求和时相消。具体推导见[聚变反应与燃烧](聚变反应与燃烧/README.md)。

### 固定电流和固定电场的两种温度响应

设均匀段长 $\ell$、截面积 $A$，则 $J=I/A$、$R=\eta\ell/A$。由体积积分可依次得到 $P_\Omega=\eta J^2A\ell=I^2R=V^2/R$。固定有效电荷与 Coulomb 对数，经典电阻率采用 $\eta\propto\Theta_e^{-3/2}$ 时，控制变量决定功率的变化方向：固定 $I$ 有 $P_\Omega\propto\Theta_e^{-3/2}$；固定电场或电压则有 $P_\Omega\propto\Theta_e^{3/2}$。

教学输入 $\eta=10^{-7}\,\Omega\mathrm m$、$\ell=10\,\mathrm m$、$A=0.5\,\mathrm{m^2}$、$I=0.5\,\mathrm{MA}$，算得 $R=2\,\mu\Omega$、$V=1\,\mathrm V$、$P_\Omega=0.50\,\mathrm{MW}$。温度升为原来四倍，电阻率降至八分之一：固定电流时功率变为 0.0625 MW；固定电压时电流成为 4 MA、功率为 4 MW。后一结果描述电阻稳态，电感决定电流达到新值所需的时间。[Fitzpatrick，Braginskii Equations，电导率与热力段](https://farside.ph.utexas.edu/teaching/plasma/Plasma/node53.html)给出温度标度；标量 Ohm 模型的完整场能收支见[流体与磁流体力学](流体与磁流体力学/README.md)。

## 温度约定与热能积分的文献换算

七个专题就近给出推导与引用。课程支持基本定律，实验论文支持具体性能，装置计划支持设计目标；实际读取范围见[来源索引](../文献资料/来源索引.json)。

- [Fitzpatrick：核聚变反应在线讲义](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node6.html)：从反应道与反应率进入能量预算；本站其他专题分别链接实际使用的粒子、流体、平衡和稳定性章节。
- [NRL Plasma Formulary 2016（PPPL 课程存档）](https://suli.pppl.gov/2016/course/NRL_FORMULARY_16.pdf)：核对量纲、反应道和常用近似；使用前将原文的 cgs 和 eV 系数转换成所需单位。
- [Wurzel 与 Hsu：Lawson 与增益比较综述](https://arxiv.org/html/2105.10954v3)：阅读增益边界、空间/时间剖面及不同路线的比较方法，不把历史数据当当前纪录。
- [国际原子能机构：聚变技术路线](https://nucleus.iaea.org/sites/connect/FUSEpublic/SitePages/Fusion-Technologies.aspx)：作为机构资料导航。
- [IPP：等离子体加热历史课程入口](https://www.ipp.mpg.de/5436011/09_Plasma_Heating.pdf)：本轮访问受限，保留原入口，不作为新增正文已经读过的证据。

### 阅读实例：把原文的密度和温度约定转成同一套量

读到 $w=3nT$ 时，先辨认原文的 $n$ 和 $T$。在 [Fitzpatrick 的 Lawson 推导，式 (1.10)–(1.12)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node7.html)中，$n=n_e=n_D+n_T$，$T$ 采用能量单位。把电子与两种离子分别展开，就得到

$$
w=\frac32(n_e\Theta_e+n_D\Theta_D+n_T\Theta_T)
\xrightarrow{\Theta_s=\Theta,\ n_D+n_T=n_e}3n_e\Theta.
$$

在各组分共动系，$m_s\langle c_j^2\rangle=\Theta_s$，故 $\int m_sc^2f_s\,d^3c/2=3n_s\Theta_s/2$。先逐物种相加，再用准中性与同温条件合并。

设文献参数为 $n_e=8\times10^{19}\,\mathrm{m^{-3}}$、共同温度 12 keV，则 $w=4.61\times10^5\,\mathrm{J\,m^{-3}}$。在 30 m³ 内储能为 13.84 MJ。阅读记录应写成“电子密度、各组分同温、均匀体积”三个明确条件，并把 $12\,\mathrm{keV}$ 转成 $1.92261\times10^{-15}\,\mathrm J$ 后代入。这样同一篇论文中的反应率、热储能和约束时间就能相互检查。

[返回知识库](../README.md)
