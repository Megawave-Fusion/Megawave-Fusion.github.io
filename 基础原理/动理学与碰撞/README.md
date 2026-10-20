# 动理学与碰撞

采用 SI、非相对论、非简并、弱耦合模型；边界、原子过程和快粒子另述。$T_s$ 用 K，$\theta_s=k_BT_s$ 用 J；eV 数值乘 $e$ 后代入 SI。$e>0$，组分电荷记 $q_s$。

## 非平衡分布的压力张量与热流

沿用[分布函数、密度、流速与温度的定义](../等离子体基本概念/README.md#MF000085)中的 $n_s$、$\mathbf u_s$ 与 $\mathbf c_s=\mathbf v-\mathbf u_s$。本条进一步讨论非平衡分布的二阶和三阶中心矩，连接压力各向异性、热流与双群体混合。

压强张量与热流密度是相对于该物种平均流速的中心矩：

$$
\mathbf P_s=m_s\int\mathbf c_s\mathbf c_s f_s\,d^3v,
\qquad
\mathbf h_s=\frac{m_s}{2}\int c_s^2\mathbf c_s f_s\,d^3v.
$$

$\mathbf c_s\mathbf c_s$ 表示二阶张量，$\mathbf P_s$ 的单位是 Pa，$\mathbf h_s$ 的单位是 $\mathrm{W\,m^{-2}}$。本文用 $\mathbf h_s$ 表示热流，以免与电荷 $q_s$ 混淆。定义 $p_s=\operatorname{tr}\mathbf P_s/3$ 后，随机动能密度恒有 $U_s=3p_s/2$；再定义动力学标量温度 $\theta_s=p_s/n_s$。这些等式来自矩定义，不要求分布已经 Maxwell 化，但一个标量温度通常不足以重建非平衡分布。

例如，两束对向粒子可以满足 $\mathbf u_s=0$，却在束流方向有很大的 $P_{s,\parallel}$。把它们替换成相同 $n_s,T_s$ 的 Maxwell 分布，会抹去双峰结构及其可能激发的波。诊断也只测量一定速度、方向或能量范围内的响应，因此“拟合温度”应注明所用谱线、拟合分布与仪器响应。各物种分别使用自己的 $\mathbf u_s$；若改用混合物质心速度，扩散动能会进入相应矩，应同时转换所有速度矩。

在各物种共动系，$\int\mathbf c_sf_s\,d^3v=0$，故

$$
\frac{m_s}{2}\int v^2f_s\,d^3v
=\frac12m_sn_su_s^2+\frac{m_s}{2}\int c_s^2f_s\,d^3v
=\frac12m_sn_su_s^2+\frac32p_s.
$$

直接把实验室系 $v^2$ 平均称为温度会混入整体流动。

来源：[Fitzpatrick，Moments of Distribution Function，式 (4.5)–(4.18)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node47.html)。上述束流例子是由中心矩定义直接得到的说明。

### 非对称双群体的压力和热流

设同一物种由两个具有相同各向同性温度能量 $\theta$ 的 Maxwell 群体组成，权重为 $1-a,a$，中心速度分别为 $0,U\hat{\mathbf x}$。整体流速为 $u_x=aU$。两个中心相对整体流的偏移为 $-aU$ 与 $(1-a)U$，分别展开中心二阶、三阶矩，得

$$
P_{xx}=n[\theta+ma(1-a)U^2],\quad P_{yy}=P_{zz}=n\theta,
$$
$$
h_x=\frac m2\int c^2c_x f\,d^3v
=\frac{mn}{2}a(1-a)(1-2a)U^3.
$$

热高斯中的奇次中心矩为零；第三矩中含 $\theta$ 的部分正比于各群体偏移的加权和，也为零，所以热流只留下群体偏移的三次方。改变 $a$ 为 $1-a$，二阶展宽保持，热流改变符号；对称双束 $a=1/2$ 的热流为零。

**算例。** 给定氘离子 $n=10^{18}\,\mathrm{m^{-3}}$、$a=0.20$、$U=5.00\times10^5\,\mathrm{m\,s^{-1}}$、$\theta=100\,\mathrm{eV}$。先求 $u_x=1.00\times10^5\,\mathrm{m\,s^{-1}}$，再代入得 $P_{xx}=149.765\,\mathrm{Pa}$、$P_{yy}=P_{zz}=16.0218\,\mathrm{Pa}$，标量温度能量为 $378.253\,\mathrm{eV}$。第三矩给 $h_x=2.00615\times10^7\,\mathrm{W\,m^{-2}}$。各子群原本都没有自身热流，合并后的非对称分布却有热流，这体现了取矩时参考流速的重要性。[Fitzpatrick，式 (4.11)–(4.18)，压力、热流及参考系变换](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node47.html)。

## Vlasov 方程、Boltzmann 方程与电磁自洽

在平均电磁场中，带碰撞和外部源的动力学方程写为

$$
\frac{\partial f_s}{\partial t}
+\mathbf v\cdot\nabla_x f_s
+\frac{q_s}{m_s}(\mathbf E+\mathbf v\times\mathbf B)
 \cdot\nabla_v f_s
=\sum_{s'}C_{ss'}[f_s,f_{s'}]+S_s.
$$

$C_{ss'}$ 描述 $s'$ 对 $s$ 的碰撞作用，$S_s$ 表示注入、反应或其他明确建模的源汇，两者与 $\partial_t f_s$ 同单位。左侧分别是局地变化、空间输运和速度空间加速。令碰撞与源都为零，便得到 Vlasov 方程；沿平均场特征轨道满足 $df_s/dt=0$。这一结论描述沿轨道的相空间密度守恒；对速度积分后，空间密度、温度和波幅仍随相空间形变演化。

“无碰撞”指所研究的时间及长度尺度上碰撞项可忽略。无碰撞近似仍保留粒子的集体相互作用：粒子通过电荷密度和电流产生场，场又改变粒子轨道。自洽源为

$$
\rho_q=\sum_s q_s\int f_s\,d^3v,\qquad
\mathbf J=\sum_s q_s\int\mathbf v f_s\,d^3v.
$$

完整电磁模型应同时求解 $\nabla\cdot\mathbf E=\rho_q/\varepsilon_0$、$\nabla\cdot\mathbf B=0$、$\partial_t\mathbf B=-\nabla\times\mathbf E$ 及 $\nabla\times\mathbf B=\mu_0\mathbf J+\mu_0\varepsilon_0\partial_t\mathbf E$。若只给定一个外部场而不让粒子反作用于场，得到的是试验粒子模型。若在低频条件下采用准中性或静电近似，必须说明删去哪些场方程、由何种关系确定电场，使电荷密度与势函数始终满足场约束。

Boltzmann 碰撞项以散射前后的分布乘积之差统计增益与损失，常用于二体散射和给定微分截面的模型。对长程 Coulomb 力，裸的散射积分在小偏转处需要集体屏蔽处理；库仑碰撞率因此具有速度依赖，并与集体屏蔽共同进入算子。Vlasov、Boltzmann、Landau 是不同近似层次的具体方程名称，使用时应同时给出场模型、碰撞算子、边界和源项。

自洽场还给出一个可直接核查的约束：将各物种连续性方程乘电荷并求和，应得到 $\partial_t\rho_q+\nabla\cdot\mathbf J=0$。这与对 Ampère–Maxwell 方程取散度的结果一致。引入反应源后，所有带电产物与反应物的电荷源总和仍应抵消；只添加电子或只添加离子的源而不说明外部电荷通量，会破坏这条关系和场约束。

来源：[Fitzpatrick，Collision Operator，式 (3.1)–(3.9)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node31.html)；[Boltzmann Collision Operator](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node33.html)。

### 自由流动的精确解与相混合

先取无力、无碰撞的一维输运方程 $\partial_tf+v\partial_xf=0$。其特征线满足 $x=x_0+vt$、$v=v_0$，沿线 $df/dt=0$，因此初值 $f(x,v,0)=F(v)[1+\epsilon\cos kx]$ 演化为
$f(x,v,t)=F(v)[1+\epsilon\cos k(x-vt)]$。令 $F$ 为标准差 $\sigma$、积分为 $n_0$ 的零均值高斯。用高斯的 Fourier 积分消去速度，得到

$$
n(x,t)=n_0\left[1+\epsilon e^{-(k\sigma t)^2/2}\cos kx\right],
$$
$$
nu=n_0\epsilon k\sigma^2t\,e^{-(k\sigma t)^2/2}\sin kx.
$$

对第二式求 $x$ 导数，正好抵消第一式的时间导数。空间密度起伏变弱时，速度空间中的相位条纹变细；完整 $f$ 仍沿特征线保持。这个无场子问题可直接作为输运程序的精确基准；带电组分自洽响应时再同时求解场方程。

**算例。** 取 $\epsilon=0.10$、$k=10\,\mathrm{m^{-1}}$、$\sigma=10^4\,\mathrm{m\,s^{-1}}$、$t=10\,\mu\mathrm s$，则 $k\sigma t=1$，密度相对振幅为 $0.10e^{-1/2}=0.0606531$。在 $kx=\pi/2$ 处，密度等于 $n_0$，流速为 $0.10\sigma e^{-1/2}=606.531\,\mathrm{m\,s^{-1}}$。对任意整周期空间积分，总粒子数和总动能保持初值；可同时检查数值耗散与守恒。[Fitzpatrick，Collision Operator，式 (3.4)–(3.9) 的相空间输运](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node31.html)。

## Maxwell 平衡、高能尾部与非平衡混合

局地漂移 Maxwell 分布写为

$$
f_{Ms}=n_s\left(\frac{m_s}{2\pi\theta_s}\right)^{3/2}
\exp\!\left[-\frac{m_s|\mathbf v-\mathbf u_s|^2}{2\theta_s}\right].
$$

固定粒子数、总动量和总动能，极大化 $-\sum_s\int f_s\ln f_s\,d^3v$，得 $\ln f_s=A_s+\boldsymbol\beta\cdot m_s\mathbf v-\gamma m_sv^2/2$。配方、归一化即为共同 $\mathbf u=\boldsymbol\beta/\gamma$、$\theta=1/\gamma$ 的 Maxwell 平衡；各物种不同温度的局地 Maxwellian 仍可交换热量。

指数必须无量纲，因此这里放入的是以 J 计的 $\theta_s$。在该物种共动系中，三个速度分量独立且方差均为 $\theta_s/m_s$，从而 $\mathbf P_s=n_s\theta_s\mathbf I$、$\mathbf h_s=0$。零热流来自关于 $\mathbf c_s$ 的奇函数积分；它不排除实验室系存在由流动携带的能量通量。采用 $v_{ts}=\sqrt{2\theta_s/m_s}$ 时，指数是 $-c_s^2/v_{ts}^2$；若采用一维标准差 $\sqrt{\theta_s/m_s}$ 作为“热速度”，所有相关系数都要一致调整。

各向同性仅要求共动系中的分布只依赖 $c_s$，不要求其径向形状是高斯。例如两个不同温度、相同流速的 Maxwell 分布之和仍然各向同性，其速率分布保留两个温度尺度。反过来，磁化等离子体常用的双温 Maxwell 模型可有 $T_\parallel\ne T_\perp$，其压强张量为

$$
\mathbf P_s=p_{s,\perp}(\mathbf I-\mathbf b\mathbf b)
+p_{s,\parallel}\mathbf b\mathbf b,
\qquad \mathbf b=\mathbf B/|\mathbf B|.
$$

对应标量温度满足 $3\theta_s=\theta_{s,\parallel}+2\theta_{s,\perp}$。这只是陀螺对称模型；若存在明显回旋相位依赖，还需非陀螺压强分量。

自碰撞热化与电子—离子同温是不同时间尺度。无源、均匀、封闭弹性碰撞体系的最终平衡要求共同流速和温度；有空间梯度时，输运仍可生成非 Maxwell 修正。

一个具体反例是相同密度的冷、热组分混合。它们具有同一平均流速时，混合物的标量热能等于两者热能的平均值，但高能尾部仍由较热组分主导。聚变反应率、电流驱动响应和高能损失涉及特定速度权重；这些量还取决于分布在有关能量范围内的形状。报告“已热化”时，应说明检查的是各向同性、低阶矩还是整个分布。

来源：[Fitzpatrick，Boltzmann H-Theorem](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node40.html)；[Collision Operator for Maxwellian Distributions](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node41.html)。各向同性混合分布的反例和双温标量关系直接由矩定义检验。

### 高能尾部的粒子份额和能量份额

定义 $v_t=\sqrt{2\theta/m}$、$x=v/v_t$，把三维 Maxwell 分布对球面角积分，归一化速率概率密度为 $g(x)=4x^2e^{-x^2}/\sqrt\pi$。要计算 $v>av_t$ 的粒子份额，对 $x^2e^{-x^2}$ 分部积分，得到

$$
F_N(a)=\operatorname{erfc}(a)+\frac{2a}{\sqrt\pi}e^{-a^2}.
$$

能量加权还需乘 $x^2$。利用积分递推
$\int_a^\infty x^ne^{-x^2}dx=\tfrac12a^{n-1}e^{-a^2}+\tfrac{n-1}{2}\int_a^\infty x^{n-2}e^{-x^2}dx$，并用总均方速率 $\langle x^2\rangle=3/2$ 归一化，得到

$$
F_E(a)=\operatorname{erfc}(a)
+\frac{2a+4a^3/3}{\sqrt\pi}e^{-a^2}.
$$

**算例。** 选门槛 $v=2v_t$，等价于单粒子动能大于 $4\theta$。将 $a=2$ 代入，尾部粒子份额 $F_N=0.0460117$，却携带 $F_E=0.156236$ 的总动能。若全体平均动能为 $3\theta/2$，尾部每粒子的平均动能便是 $(F_E/F_N)(3\theta/2)=5.09334\theta$。例如 $\theta=100\,\mathrm{eV}$，超过 $400\,\mathrm{eV}$ 的 $4.60\%$ 粒子平均具有约 $509.3\,\mathrm{eV}$。因此需要按速率、通量或能量分别加权同一分布。[Fitzpatrick，Maxwellian 定义与高斯积分，式 (3.145)–(3.152)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node41.html)。

## 从动理学推导连续性、动量和内能方程

先考虑无源、只含守恒弹性碰撞的系统，并假设分布在速度无穷远充分衰减，使积分分部的边界项消失。因为 Lorentz 加速度满足 $\nabla_v\cdot\mathbf a_s=0$，对动力学方程直接积分便得到

$$
\partial_t n_s+\nabla\cdot(n_s\mathbf u_s)=0.
$$

其原因是速度空间加速不会创造粒子，且 $\int C_{ss'}d^3v=0$。电离、复合和聚变反应会改变物种数目，加入它们后右侧必须恢复相应源汇。

再乘以 $m_s\mathbf v$ 并积分，将二阶矩分解为 $m_sn_s\mathbf u_s\mathbf u_s+\mathbf P_s$，借助连续性方程得到

$$
m_sn_s(\partial_t+\mathbf u_s\cdot\nabla)\mathbf u_s
=q_sn_s(\mathbf E+\mathbf u_s\times\mathbf B)
-\nabla\cdot\mathbf P_s+\mathbf R_s,
\qquad
\mathbf R_s=\sum_{s'}\int m_s\mathbf v C_{ss'}\,d^3v.
$$

$\mathbf R_s$ 是碰撞动量交换率密度，单位 $\mathrm{N\,m^{-3}}$。一般压强力是 $-\nabla\cdot\mathbf P_s$，只有各向同性时才退化为 $-\nabla p_s$。相互碰撞物种的动量交换成对相反，在两种动量方程中分别保留正反作用力。

对随机动能取矩，或由总动能方程减去整体流动能方程，可得

$$
\partial_t U_s+\nabla\cdot(U_s\mathbf u_s+\mathbf h_s)
+\mathbf P_s:\nabla\mathbf u_s=Q_s,
\qquad U_s=\tfrac12\operatorname{tr}\mathbf P_s,
$$

$$
Q_s=\sum_{s'}\int\frac12m_sc_s^2C_{ss'}\,d^3v.
$$

这里 $\mathbf P_s:\nabla\mathbf u_s=\sum_{ij}P_{s,ij}\partial_j u_{s,i}$。压缩时 $\nabla\cdot\mathbf u_s<0$，各向同性压强功使内能上升。磁场对点粒子不做功，因为 $\mathbf v\cdot(\mathbf v\times\mathbf B)=0$；电场输入首先出现在总动能方程，分离流动能后不应再把同一份 $\mathbf J\cdot\mathbf E$ 重复加入内能。

尤其要区分：各物种实验室系碰撞总动能之和守恒，但共动系的 $Q_s$ 之和未必为零，因为相对漂移可转化成热。准确关系为 $\sum_s(Q_s+\mathbf u_s\cdot\mathbf R_s)=0$。这给双流体代码的摩擦加热记账提供了直接检验。

例如令一对物种的摩擦为 $\mathbf R_{ss'}=-\alpha(\mathbf u_s-\mathbf u_{s'})$，$\alpha>0$，另一物种受到相反作用，则两者整体流动能的碰撞变化率为 $-\alpha|\mathbf u_s-\mathbf u_{s'}|^2$。相应内能总增益必须为正的同一数值。两种热源的分配还需碰撞模型；其和先满足上述总能量关系。

来源：[Fitzpatrick，Moments of Kinetic Equation，式 (4.33)–(4.38)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node49.html)；[Moments of Collision Operator，式 (4.19)–(4.32)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node48.html)。

### 分部积分中的边界项与膨胀算例

对动理学方程乘速度矩再积分时，力项的处理决定了守恒式的符号。在 $f$ 于速度无穷远足够快衰减的条件下，

$$
\int a_j\partial_{v_j}f\,d^3v=0,\qquad
\int mv_i a_j\partial_{v_j}f\,d^3v=-mn a_i
$$

（后一式先以速度无关电力说明；Lorentz 项按其速度依赖求导后给相应磁力）。再用
$\int mc_ic_jf\,d^3v=P_{ij}$，内能中的压缩功是 $-\mathsf P:\nabla\mathbf u$。各向同性时成为 $-p\nabla\cdot\mathbf u$，并与连续性方程组合成 $D_t\theta=-(2/3)\theta\nabla\cdot\mathbf u$，适用于无热流、无加热的单原子绝热闭合。

**算例。** 考察一个被外部流场均匀拉伸的物质元，给定 $\mathbf u=(ax,0,0)$、$a=3.00\times10^4\,\mathrm{s^{-1}}$，持续 $10\,\mu\mathrm s$。沿物质轨迹有 $n/n_0=e^{-at}=0.740818$；若采用上述各向同性闭合，$\theta/\theta_0=e^{-2at/3}=0.818731$，所以 $p/p_0=e^{-5at/3}=0.606531$。该元长度同时增加 $e^{0.3}$ 倍，$nV$ 保持。用 $pV^{5/3}$ 再检查，因子 $e^{-0.5}e^{(5/3)0.3}=1$。各向同性来自所选闭合；碰撞很弱且各向异性显著时，可保留压力张量继续求解。[Fitzpatrick，Moments of Kinetic Equation，式 (4.33)–(4.38)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node49.html)。

## 矩层级、闭合、平均自由程与 Knudsen 数

矩层级逐阶耦合：$n,\mathbf u,p$ 的演化还需压力张量与热流，再高阶仍出现新矩。零热流、绝热指数及 Fourier 导热是不同闭合，须分别说明其物理排序。

对应某一种弛豫频率 $\nu_s$，可定义碰撞平均自由程的估计

$$
\lambda_{\mathrm{mfp},s}\sim\frac{v_{ts}}{\nu_s},\qquad
\mathrm{Kn}_s=\frac{\lambda_{\mathrm{mfp},s}}{L}.
$$

这里 $L$ 是所研究变化的空间尺度，须具体写明，例如温度梯度长度 $L_T=|\nabla\ln T_s|^{-1}$，或沿磁场长度 $L_{T\parallel}=|\mathbf b\cdot\nabla\ln T_s|^{-1}$。$\lambda_{\mathrm{mfp}}$ 的单位为 m，Knudsen 数无量纲。在 Coulomb 小角散射中，它表示速度方向或相关矩累计改变的距离，并非粒子两次接触硬球之间的直线路程。若改用能量弛豫率，得到的长度也会改变。

碰撞流体展开通常要求相关的 $\mathrm{Kn}\ll1$，并要求宏观变化频率小于维持局地平衡所需的碰撞频率。仅有 $\rho_s/L\ll1$，其中 $\rho_s$ 是回旋半径，足以支持某些回旋平均近似；平行热流的局域性还由平均自由程决定。磁化程度 $|\Omega_s|/\nu_s$ 与碰撞局域性 $\lambda_{\mathrm{mfp},s}/L_\parallel$ 是不同判据。

例如下面定义的单电荷电子—离子参考频率，在 $n_e=10^{20}\,\mathrm{m^{-3}}$、$T_{e,\mathrm{eV}}=1000$、指定 $\ln\Lambda=15$ 时约为 $1.38\times10^5\,\mathrm{s^{-1}}$。用 $v_{te}=\sqrt{2\theta_e/m_e}\simeq1.88\times10^7\,\mathrm{m\,s^{-1}}$，估得 $v_{te}/\nu_{ei}\simeq136\,\mathrm m$。该教学算例采用同一速度和频率约定，说明米级平行梯度仍需与平均自由程比较。高能尾部的有效自由程还可更长，计算热流应覆盖对能量通量有贡献的速度范围。

网格收敛只保证接近指定闭合方程的解。先检验自由程、频率和边界排序，再分开评估闭合偏差与数值残差。

来源：[Fitzpatrick，Fluid Closure](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node52.html)；[Braginskii Equations，闭合小参数及式 (4.70)–(4.73)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node54.html)。示例数值由本页所列 SI 公式计算。

### 热流闭合的有限响应时间

在一个局部示范模型中，用 BGK 碰撞 $C=-(f-f_M)/\tau$，并让 $f_M$ 与 $f$ 具有相同的密度、流速和温度。由于 Maxwellian 的共动三阶矩为零，碰撞项的热流矩是 $-h/\tau$。把空间梯度驱动的三阶矩记为给定的 $S$，得到

$$
\partial_t h+\frac h\tau=S.
$$

乘积分因子 $e^{t/\tau}$，从初值 $h(0)=0$ 积分，得到 $h(t)=\tau S(1-e^{-t/\tau})$。定义稳态闭合值 $h_F=\tau S$，其瞬时响应只在驱动变化时间远长于 $\tau$ 时适合。若驱动按 $e^{-i\omega t}$ 变化，则 $\widetilde h=\widetilde h_F/(1-i\omega\tau)$，振幅衰减因子为 $(1+\omega^2\tau^2)^{-1/2}$，并产生相位滞后。

**算例。** 取 $\tau=1.00\,\mu\mathrm s$、$h_F=-10.0\,\mathrm{kW\,m^{-2}}$。一倍弛豫时间后，$h=-6.32121\,\mathrm{kW\,m^{-2}}$；三倍后为 $-9.50213\,\mathrm{kW\,m^{-2}}$。若 $\omega\tau=1$，周期响应振幅为稳态幅度的 $1/\sqrt2$，相位按本页时间约定滞后 $\pi/4$。因此空间排序 $\lambda_{\rm mfp}/L$ 和时间排序 $\omega\tau$ 应分别进入闭合判断。这里把梯度驱动固定以突出热流的记忆时间。[Fitzpatrick，Fluid Closure，矩层级与渐近闭合](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node52.html)；[Kunz，§VIII.1，式 (VIII.1.1)–(VIII.1.2)，匹配矩的 BGK 模型](https://www.astro.princeton.edu/~kunz/Site/AST554/AST554_Kunz_Lecture_Notes.pdf)。

## Rutherford 散射与多次小偏转的累积

考虑两粒子在一次遭遇期间可近似不受外磁场和第三方强扰动影响的非相对论 Coulomb 散射。令相对速度大小为 $u=|\mathbf v-\mathbf v'|$，约化质量为 $\mu=m_sm_{s'}/(m_s+m_{s'})$，冲量参数为 $b$。由两体轨道的能量和角动量守恒，偏转角大小 $\chi$ 满足

$$
\tan\frac{\chi}{2}=\frac{b_{90}}{b},\qquad
b_{90}=\frac{|q_sq_{s'}|}{4\pi\varepsilon_0\mu u^2}.
$$

令 $a=q_sq_{s^{\prime}}/(4\pi\varepsilon_0)$、$E_r=\mu u^2/2$、$\ell=\mu ub$。Binet 方程 $y^{\prime\prime}+y=-\mu a/\ell^2$ 给双曲线偏心率 $\mathcal e=\sqrt{1+(b/b_{90})^2}$；渐近线满足 $\sin(\chi/2)=1/\mathcal e$，即得散射角。排斥正碰另由 $E_r=a/r_{\min}$ 给 $r_{\min}=2b_{90}$。

$b_{90}$ 的单位是 m，是相对速度发生 $90^\circ$ 偏转对应的冲量参数；它不等同于所有轨道的最近距离。对排斥势的正碰，最近距离是 $2b_{90}$。当 $b\gg b_{90}$ 时，$\chi\simeq2b_{90}/b$ 很小。异号电荷的轨道弯曲方向改变，但散射角大小由绝对电荷乘积确定。

为了理解小角碰撞为何重要，暂取很重、近静止的散射中心，令轻粒子以速度 $u$ 穿过数密度 $n_{s'}$ 的背景。在 $dt$ 内，冲量参数处于 $[b,b+db]$ 的遭遇数为 $n_{s'}u\,dt\,2\pi b\,db$。随机偏转的均方角增量因而正比于

$$
\frac{d\langle\chi^2\rangle}{dt}
\simeq8\pi n_{s'}u b_{90}^2
\int_{b_{\min}}^{b_{\max}}\frac{db}{b}.
$$

这给出 $n_{s'}u^{-3}\ln\Lambda$ 的速度标度；不同速度矩对应的精确系数由完整碰撞积分给出。推导中假定独立、随机、小角偏转；大累计角通过角扩散方程描述。对质量相近的两物种，还必须区分相对速度偏转和各自实验室速度变化。

每个对数 $b$ 区间贡献相近：远距离作用虽弱，遭遇数却多。直线碰撞轨道还要求一次主导遭遇内回旋弯曲可忽略；极强磁化下须重新检查轨道与碰撞核。

还可用 $b_{90}\propto u^{-2}$ 检查速度标度：把相对速度增大一倍，特定偏转角对应的面积尺度变为原来的十六分之一，而单位时间穿过的长度只增加一倍，因此散射率的量级减为原来的八分之一。这里保持背景密度与 Coulomb 对数不变，仅用于理解高速极限；把它外推到速度低于背景热速度的区域，会遗漏背景粒子的运动。

来源：[Fitzpatrick，Two-Body Coulomb Collisions，式 (3.38)–(3.64)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node35.html)；[MIT 22.611J，Collisions in Plasmas，§3.3.4 Random Walk in Angle](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/5617c594de835f49cd769a58ba156ce2_chap3.pdf)。

### 从冲量参数映射到微分散射截面

令 $b_{90}=|q_1q_2|/(4\pi\varepsilon_0m_rg^2)$，其中 $g$ 为无穷远相对速率、$m_r$ 为约化质量。Rutherford 轨道给出 $b=b_{90}\cot(\chi/2)$，$\chi$ 取偏转角大小。入射粒子落在环带 $b$ 到 $b+db$ 的面积为 $d\sigma=2\pi b|db|$，轴对称散射环的立体角为 $d\Omega=2\pi\sin\chi\,d\chi$。两者相除并求导得到

$$
\frac{d\sigma}{d\Omega}
=\frac{b}{\sin\chi}\left|\frac{db}{d\chi}\right|
=\frac{b_{90}^2}{4\sin^4(\chi/2)},\qquad
\sigma(\chi>\chi_0)=\pi b_{90}^2\cot^2(\chi_0/2).
$$

微分截面单位为 $\mathrm{m^2\,sr^{-1}}$，积分截面为 $\mathrm{m^2}$。后式也可直接由 $b<b_{90}\cot(\chi_0/2)$ 对应的入射圆盘面积取得，构成独立的几何核对。

**算例。** 电子与氘核的相对速率取 $g=3.00\times10^6\,\mathrm{m\,s^{-1}}$，使用约化质量得 $b_{90}=2.81481\times10^{-11}\,\mathrm m$。若 $b=2b_{90}$，则 $\chi=2\arctan(1/2)=53.1301^\circ$。所有偏转大于此角的截面为 $\pi(2b_{90})^2=9.95653\times10^{-21}\,\mathrm{m^2}$。把微分截面乘 $2\pi\sin\chi$ 并从该角积分到 $\pi$，得到相同值。[Fitzpatrick，Two-Body Coulomb Collisions，式 (3.64)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node35.html)；[Rutherford Scattering Cross-Section，式 (3.65)–(3.70)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node36.html)。

## Coulomb 对数、屏蔽和短程截断

小角累积中的冲量参数积分产生自然对数

$$
\ln\Lambda=\int_{b_{\min}}^{b_{\max}}\frac{db}{b}
=\ln\!\left(\frac{b_{\max}}{b_{\min}}\right).
$$

它记录了弱偏转近似中可积累贡献的长短距离范围之比。经典弱耦合、近热平衡的基本估计采用屏蔽长度作为大尺度截断；若各组分均能作静态热响应，可写

$$
\lambda_D^{-2}=\sum_s\frac{n_sq_s^2}{\varepsilon_0\theta_s},
\qquad b_{\max}\sim\lambda_D.
$$

对运动试验粒子、强温差或有显著动力学响应的背景，哪些物种能够参与屏蔽与其响应时间有关，应按可响应物种与动态介电函数确定截断。若粒子在系统中停留时间很短、系统尺寸不足或强磁场修改相遇过程，大尺度估计也需检查。

短距离一端，$b\lesssim b_{90}$ 时小角展开不再适用；若量子衍射长度更大，则应把它纳入下限。只作主对数精度估计时，常写

$$
b_{\min}\sim\max\!\left(b_{90},\frac{\hbar}{\mu u}\right).
$$

其中第二项是按约化 de Broglie 长度定义的量级，某些约定含额外的 $1/2$。这些常数改变对数内的有限项，若要报出精确碰撞系数，必须统一采用同一来源的完整定义。电子简并、Pauli 阻塞和强耦合状态分别需要相应量子统计或相关理论。

相对动量 $p=\mu u$ 给量子长度 $\hbar/(\mu u)$。主对数下限取它与经典强偏转尺度中较大者，不能据此确定有限常数。屏蔽上限由可响应组分的密度响应和 Poisson 方程求得。 [等离子体基本概念](../等离子体基本概念/README.md)。

需要 $b_{\max}\gg b_{\min}$、通常还要求 $\ln\Lambda\gg1$，才能把主对数贡献作为受控近似。若算出 $\ln\Lambda$ 接近零或为负，应该首先判断模型和参数是否越出适用范围，并改用适合相应相关强度的描述。许多手册中“常数减去对数”的经验公式默认密度单位为 $\mathrm{cm^{-3}}$、温度单位为 eV；把 SI 密度直接代入会造成很大偏差。本页保留带量纲的基本尺度，避免省略这些单位约定。

例如，将某个截断尺度改成原来的两倍，只使 $\ln\Lambda$ 改变 $\ln2$。若原值是十五，对由主对数控制的系数造成约百分之五的变化。对数内的有限常数及数值有效位数应与算子的近似阶数相配。它不说明所有碰撞误差都只有百分之五；强耦合、非热分布等失效机制可能完全改变模型。

来源：[Fitzpatrick，Coulomb Logarithm，式 (3.114)–(3.122) 及其单位说明](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node39.html)；[MIT 22.616，Collisions and Transport Theory I，Debye cutoff 讨论](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/923ea57a2611e1f05af813f1919354eb_collisionstrans1.pdf)。

### 对数区间为何同等贡献

小角轨道的偏转 $\chi\simeq2b_{90}/b$，每单位时间的入射环带粒子数正比于 $ng\,2\pi b\,db$。于是累计角方差的贡献为 $d\langle\chi^2\rangle/dt\propto b^{-2}b\,db=db/b$。对上下截断积分得到 $\ln(b_{\max}/b_{\min})$。用 $z=\ln b$ 换元后，每个等宽 $z$ 区间贡献相同；若把总贡献平分，分界应满足

$$
\ln\frac{b_*}{b_{\min}}=\ln\frac{b_{\max}}{b_*},
\qquad b_*=\sqrt{b_{\min}b_{\max}}.
$$

这说明中间尺度取几何平均，与线性距离中点相差很大。该主对数分析需同时指定速度、参与屏蔽的组分及短程约定。

**算例。** 取电子动能 $100\,\mathrm{eV}$、$g=\sqrt{2(100e)/m_e}$，给定背景 $n_e=10^{19}\,\mathrm{m^{-3}}$、$\theta_e=100\,\mathrm{eV}$，选电子屏蔽尺度 $b_{\max}=\lambda_{De}=2.35082\times10^{-5}\,\mathrm m$。本例用 $b_{\min}=\max[b_{90},\hbar/(2m_eg)]$：两项分别为 $7.19982\times10^{-12}$ 与 $9.75959\times10^{-12}\,\mathrm m$，因此量子项占优。得到 $\ln\Lambda=14.6946$，半贡献尺度 $b_*=1.51469\times10^{-8}\,\mathrm m$。对 $db/b$ 在两段分别积分，各为 $7.34730$。这里采用指定速度的截断算例，热平均系数还需对分布积分。[Fitzpatrick，Coulomb Logarithm，式 (3.114)–(3.118) 及其后 conventional definition](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node39.html)。

## 偏转、慢化、动量和能量频率不能互换

“碰撞频率”需要同时注明试验粒子、背景物种、所取矩及速度平均。偏转频率描述方向随机化；慢化频率描述平均速度或动量衰减；能量弛豫率描述能量变化；物种温度交换率描述两个分布之间的热交换。它们受不同速度权重和质量比控制，通常只在特定极限下有简单关系。Coulomb 偏转时间统计的是许多弱作用累积至显著方向变化的时间。

一个可明确复用的定义是：两个相近流速的 Maxwell 物种间，以

$$
\mathbf R_{ss'}=-m_sn_s\nu_{ss'}^{(u)}
(\mathbf u_s-\mathbf u_{s'})
$$

定义动量交换频率 $\nu_{ss'}^{(u)}$。其单位为 $\mathrm{s^{-1}}$；由反作用相等相反，必须满足 $m_sn_s\nu_{ss'}^{(u)}=m_{s'}n_{s'}\nu_{s's}^{(u)}$。在单电荷准中性等离子体中，故有 $\nu_{ie}^{(u)}=(m_e/m_i)\nu_{ei}^{(u)}$。交换的是同一份动量，质量大的离子平均流速改变得较慢。

在离子热速度远小于电子热速度、相对漂移足够小的 Maxwell 情形，常用电子—离子参考动量频率为

$$
\nu_{ei}^{(u)}=
\frac{4\sqrt{2\pi}}{3}
\frac{n_i Z^2 e^4\ln\Lambda}
{(4\pi\varepsilon_0)^2\sqrt{m_e}\,\theta_e^{3/2}},
\qquad q_i=Ze.
$$

上述数值系数可以从前面的角扩散复算。固定重离子背景时，单电子偶极角矩的衰减率是 $\nu_D(v)=\tfrac12d\langle\chi^2\rangle/dt=4\pi n_i[Ze^2/(4\pi\varepsilon_0m_e)]^2\ln\Lambda/v^3$。电子 Maxwellian 相对离子有小漂移 $\mathbf w$ 时，$f_e\simeq f_{e0}[1+m_e\mathbf v\cdot\mathbf w/\theta_e]$；取动量矩，角平均 $v_iv_j\to v^2\delta_{ij}/3$，得到

$$
\nu_{ei}^{(u)}=\frac{m_e}{3n_e\theta_e}
\int\nu_D(v)v^2f_{e0}\,d^3v,\qquad
\frac1{n_e}\int\frac{f_{e0}}v\,d^3v
=\sqrt{\frac2\pi}\sqrt{\frac{m_e}{\theta_e}}.
$$

后一积分先对球面角积分，再用 $\int_0^\infty ve^{-m_ev^2/(2\theta_e)}dv=\theta_e/m_e$。代入前式，$4\pi\sqrt{2/\pi}/3=4\sqrt{2\pi}/3$，即得到所列参考频率。它对漂移 Maxwellian 取矩；电场持续驱动下的实际速度畸变仍需解 Spitzer 问题。

这一约定使 $Z=1$、$n_i=n_e$ 时与下引教材的 $1/\tau_e$ 一致。这个频率对应给定分布的小漂移展开；试验电子散射率保留速度依赖，Spitzer 电导则由整体线性化分布响应给出。电子—电子碰撞改变单电子运动方向、恢复分布形状，同时守恒电子总动量；电流摩擦率则由电子与其他组分的动量交换及分布响应确定。

比较文献中的系数时，应先核对热速度定义、$\nu$ 对应的弛豫对象、是否对 Maxwell 分布平均、离子电荷数及 Coulomb 对数。只比较名称“electron collision frequency”可能把不同问题的答案错误地并在一起。

频率是偏离平衡后的响应系数：已共流时净摩擦仍为零，已同温时净热交换仍为零。记录频率时，同时记录流速差、温差或相应分布梯度。

来源：[Fitzpatrick，Collision Times，定义 (3.184)、显式式 (3.188)、(3.190)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node43.html)；[MIT 22.611J，Collisions in Plasmas，§3.3.5、§3.4.5](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/5617c594de835f49cd769a58ba156ce2_chap3.pdf)。本文的反向频率关系由动量守恒单独推得。

### 角向本征函数给出不同矩的衰减率

固定速率 $v$，令 $\xi=v_\parallel/v$，采用轴对称俯仰角扩散
$C[f]=(\nu/2)\partial_\xi[(1-\xi^2)\partial_\xi f]$。将分布展开为 Legendre 多项式 $f=\sum_\ell a_\ell(t)P_\ell(\xi)$。利用 Legendre 微分方程，逐项得到

$$
\frac{da_\ell}{dt}=-\frac{\nu}{2}\ell(\ell+1)a_\ell,\qquad
a_\ell(t)=a_\ell(0)e^{-\nu\ell(\ell+1)t/2}.
$$

$\ell=0$ 是角积分粒子数，保持；$\ell=1$ 对应平均平行速度，按 $\nu$ 衰减；$\ell=2$ 对应压力各向异性，按 $3\nu$ 衰减。速率固定，所以该角向模型保持每粒子能量。频率差异在同一个算子内已出现，来自所观测的角矩不同。

**算例。** 给定 $\nu=10^5\,\mathrm{s^{-1}}$，初始在各向同性背景上加入小的 $P_1$ 与 $P_2$ 分量。经过 $10\,\mu\mathrm s$，一阶系数变为原来的 $e^{-1}=0.367879$，二阶系数变为 $e^{-3}=0.0497871$。例如初始归一化系数分别为 $0.10$ 与 $0.05$，末态分别为 $0.0367879$ 与 $0.00248935$。对数斜率给 $\nu$ 和 $3\nu$，而能量矩的变化为零。这可用于分别测试碰撞模块的角向各向同性化、流动弛豫及能量账本。[Kunz，§VIII.4，式 (VIII.4.4)–(VIII.4.6)，PDF 第 111–112 页](https://www.astro.princeton.edu/~kunz/Site/AST554/AST554_Kunz_Lecture_Notes.pdf)。

## 电子—离子温度交换为什么较慢

![无外源、固定交换系数的电子—离子双温弛豫](/assets/diagrams/basic-kinetic.svg)

*无外源、固定交换系数的电子—离子双温弛豫。曲线与示意均按本条所列模型生成。*

电子撞上很重的离子时，运动方向可以明显变化，速率却只发生很小改变。极限 $m_i\to\infty$ 中，静止离子产生的 Coulomb 场只改变电子轨道方向，不向离子传递有限动能。有限质量修正带来约 $m_e/m_i$ 的热交换尺度，因此电子—离子温度交换比电子偏转慢一个与质量比有关的尺度。

考虑单电荷等离子体，$n_e=n_i=n$，两物种近 Maxwell 分布、平均相对漂移可忽略，且 $\theta_e/m_e\gg\theta_i/m_i$。用上一条的 $\nu_{ei}^{(u)}$ 约定，离子获得的热功率密度在该质量比近似下为

$$
Q_i=3\frac{m_e}{m_i}n\nu_{ei}^{(u)}
(\theta_e-\theta_i),\qquad Q_e=-Q_i.
$$

质量比与系数可从弹性二体碰撞的能量转移求出。令 $M=m_e+m_i$、$\mu=m_em_i/M$，相对速度为 $\mathbf w=\mathbf v_e-\mathbf v_i$，质心速度为 $\mathbf V=(m_e\mathbf v_e+m_i\mathbf v_i)/M$。碰撞保持 $V,w$ 的大小，单次电子能量变化为 $\Delta K_e=\mu\mathbf V\cdot\Delta\mathbf w$。两个无漂移 Maxwellian 给相对高斯方差 $s^2=\theta_e/m_e+\theta_i/m_i$，并有条件平均 $\langle\mathbf V\mid\mathbf w\rangle=(\theta_e-\theta_i)\mathbf w/(Ms^2)$。将角扩散的平均偏转 $\langle\Delta\mathbf w\rangle/dt=-4\pi n_i[e^2/(4\pi\varepsilon_0\mu)]^2\ln\Lambda\,\mathbf w/w^3$ 代入，再用 $\langle1/w\rangle=\sqrt{2/\pi}/s$，便得

$$
Q_i=\frac{4\sqrt{2\pi}\,n_en_i e^4\ln\Lambda}
{(4\pi\varepsilon_0)^2m_em_i(\theta_e/m_e+\theta_i/m_i)^{3/2}}
(\theta_e-\theta_i).
$$

以上热平均采用单电荷、共同 Coulomb 对数；取 $n_e=n_i=n$、$\theta_e/m_e\gg\theta_i/m_i$，系数化为 $3(m_e/m_i)n\nu_{ei}^{(u)}$。质量比来自离子反冲，温差决定净传热方向。

$Q_i$ 单位为 $\mathrm{W\,m^{-3}}$；当 $T_e>T_i$ 时离子被加热，符号正确。这个反对称关系适用于此处忽略相对漂移的热交换。若存在相对漂移，摩擦耗散还会增加随机热能，必须按总能量预算补上，两种内能源的和包含摩擦产生的热。

在均匀、无源、密度固定的示例中，使用每物种 $U_s=3n\theta_s/2$，得到

$$
\frac{d\theta_e}{dt}=-2\frac{m_e}{m_i}\nu_{ei}^{(u)}
(\theta_e-\theta_i),\qquad
\frac{d\theta_i}{dt}=+2\frac{m_e}{m_i}\nu_{ei}^{(u)}
(\theta_e-\theta_i).
$$

若把 $\nu_{ei}^{(u)}$ 在平衡附近视为常数，两者同时变化时，温差以 $4(m_e/m_i)\nu_{ei}^{(u)}$ 衰减；若离子温度由外部热浴固定，电子对热浴的衰减率则为 $2(m_e/m_i)\nu_{ei}^{(u)}$。这说明所谓“平衡时间”即使讨论同一物理过程，也要交代是跟踪温差、单物种温度，还是固定背景。离平衡很远时 $\nu\propto\theta_e^{-3/2}$ 随温度变化，不应把整个过程套成单一指数。

电子加热向离子传递的份额由温差、交换时间与损失共同确定。评估聚变燃料升温，应比较电子—离子交换、外部加热、辐射和约束损失的时间尺度；电子内部热化与电子—离子温度平衡对应不同时间尺度。本条给出的是热 Maxwell 背景间的交换，不用于任意高能离子或电子束的慢化分配。

无源等密度模型保持 $\theta_e+\theta_i$，并使差温趋零，因此共同温度为初始两温的算术平均。这两项是交换模块的守恒与符号检查。

来源：[Fitzpatrick，Unmagnetized Limit，式 (4.82)、(4.86)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node55.html)；[MIT 22.611J，Collisions in Plasmas，§3.5.4 Energy Equilibration](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/5617c594de835f49cd769a58ba156ce2_chap3.pdf)。两个不同衰减率由本条能量方程相减得到。

### 两温度方程的共同温度与差模

对无外热源、固定密度的两组分，令传递给离子的功率密度为 $H=(3/2)n_e\alpha(\theta_e-\theta_i)$，其中 $\alpha$ 在本例内取常数。电子与离子内能方程分别给
$\dot\theta_e=-\alpha(\theta_e-\theta_i)$、
$\dot\theta_i=(n_e/n_i)\alpha(\theta_e-\theta_i)$。将它们按密度加权相加，以及直接相减，得到

$$
\bar\theta=\frac{n_e\theta_e+n_i\theta_i}{n_e+n_i}=\text{常数},\quad
\Delta\theta(t)=\Delta\theta(0)e^{-\alpha(1+n_e/n_i)t}.
$$

因此真正的差温衰减时间是 $\tau_\Delta=[\alpha(1+n_e/n_i)]^{-1}$。重建各温度时，$\theta_e=\bar\theta+[n_i/(n_e+n_i)]\Delta\theta$，离子取相反的 $n_e$ 权重。这些权重直接来自总热能守恒。

**算例。** 单价等密度体系初始 $\theta_e=10.0\,\mathrm{keV}$、$\theta_i=1.0\,\mathrm{keV}$，给定固定模型系数 $\alpha=50.0\,\mathrm{s^{-1}}$。共同温度为 $5.50\,\mathrm{keV}$，差模时间为 $10.0\,\mathrm{ms}$。一倍差模时间后，差温为 $9e^{-1}=3.31091\,\mathrm{keV}$，故电子为 $7.15546\,\mathrm{keV}$、离子为 $3.84454\,\mathrm{keV}$；两温之和仍为 $11.0\,\mathrm{keV}$。真实库仑交换系数随温度变化，可在同一守恒方程中更新 $\alpha$ 并数值积分。[Fitzpatrick，Collision Times，式 (3.184)–(3.186)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node43.html)。

## Fokker–Planck、Landau 算子与守恒检验

许多小速度增量的累计效应可表示成速度空间的漂移与扩散。固定背景时，一般 Fokker–Planck 形式为

$$
C[f]=-\frac{\partial}{\partial v_i}(A_i f)
+\frac12\frac{\partial^2}{\partial v_i\partial v_j}(D_{ij}f),
$$

粗粒化转移积分对 $\Delta\mathbf v$ 展开：零阶与损失项抵消，一阶给 $-\partial_{v_i}(A_if)$，二阶给 $\tfrac12\partial_{v_i}\partial_{v_j}(D_{ij}f)$。截断要求更高增量矩可忽略；少量大角事件主导时不适用。

其中采用重复指标求和，$A_i=\langle\Delta v_i\rangle/\Delta t$、$D_{ij}=\langle\Delta v_i\Delta v_j\rangle/\Delta t$ 是相对于微观相关时间足够长、相对于宏观弛豫时间足够短的粗粒化系数。$A_i$ 单位为 $\mathrm{m\,s^{-2}}$，$D_{ij}$ 单位为 $\mathrm{m^2\,s^{-3}}$；扩散张量应为半正定。只保留扩散而删掉与背景热平衡相容的漂移，通常不会得到正确 Maxwell 平衡。

在弱耦合、主对数、小角 Coulomb 近似下，Landau 算子可用下列明确的 SI 约定表示：

$$
C_{ss'}=K_{ss'}\frac{\partial}{\partial v_i}
\int d^3v'\,U_{ij}(\mathbf w)
\left[f_{s'}(\mathbf v')\frac{\partial f_s(\mathbf v)}{\partial v_j}
-\frac{m_s}{m_{s'}}f_s(\mathbf v)
\frac{\partial f_{s'}(\mathbf v')}{\partial v'_j}\right],
$$

$$
\mathbf w=\mathbf v-\mathbf v',\qquad
U_{ij}(\mathbf w)=\frac{w^2\delta_{ij}-w_iw_j}{w^3},
\qquad
K_{ss'}=2\pi\left(\frac{q_sq_{s'}}{4\pi\varepsilon_0m_s}\right)^2\ln\Lambda_{ss'}.
$$

核与系数也来自 Rutherford 小角冲量：一次遭遇的横向增量大小为 $|\Delta\mathbf v_{s\perp}|=2|q_sq_{s'}|/(4\pi\varepsilon_0m_sb w)$。对冲量方向作方位角平均，每个横向分量分到总平方的一半；再乘遭遇率 $w\,2\pi b\,db\,f_{s'}d^3v'$ 并积分 $db/b$，得到 $D_{ij}=2K_{ss'}\int U_{ij}f_{s'}d^3v'$。有限反冲和平均慢化给漂移系数 $A_i=K_{ss'}(1+m_s/m_{s'})\int U_{ij}\partial_{v'_j}f_{s'}d^3v'$；将它和 $D_{ij}$ 代入 Fokker–Planck 式，用 $\partial_{v_j}\int U_{ij}f_{s'}d^3v'=\int U_{ij}\partial_{v'_j}f_{s'}d^3v'$，便合并成上述 Landau 的通量形式。这里的积分分部仍要求速度边界项消失。

物种对必须采用对称一致的 $\ln\Lambda_{ss'}=\ln\Lambda_{s's}$，此处视为给定局地参数；若擅自给两个方向使用不同的对数，可能破坏成对守恒。该算子对给定背景是线性的，对全部自洽分布则是双线性的，其扩散张量随速度与背景分布变化。

守恒的核心是 $U_{ij}w_j=0$：核只作用在相对速度的横向方向。速度积分分部并交换粒子标签，可检验每个物种粒子数守恒，以及一对物种的总动量、总动能守恒。共同流速、共同温度 Maxwell 分布代入括号后，其速度导数组合与 $\mathbf w$ 成正比，因此被 $\mathbf U$ 消去。这是无需求解方程就能完成的平衡核对。

令 $\mathbf g_s=\nabla_v\ln f_s/m_s$、$G_{ss^{\prime}}=m_s^2K_{ss^{\prime}}=m_{s^{\prime}}^2K_{s^{\prime} s}$。交换物种标签后，成对动量矩相消，能量矩含 $\mathbf w\cdot\mathsf U=0$；共同 Maxwellian 又有 $\mathbf g_s-\mathbf g_{s^{\prime}}=-\mathbf w/\theta$，故碰撞通量为零。

完整算子还满足适当边界条件下的 H 定理，即碰撞使熵不减。数值实现应分别检查粒子数、成对动量、成对能量、分布非负性及 Maxwell 平衡残差。只演化试验粒子而固定背景，试验物种自身会失去动量和能量；守恒必须包括背景收到的份额，或在线性化模型中保留补偿性的场粒子项。离散算子的守恒性质应由上述速度矩积分直接核查。

H 定理同样可直接分部积分：令 $H=\sum_s\int f_s\ln f_s\,d^3v$，并把物种对交换对称化，得到

$$
\left.\frac{dH}{dt}\right|_C
=-\frac12\sum_{ss'}G_{ss'}\iint f_sf_{s'}
(\mathbf g_s-\mathbf g_{s'})\cdot\mathsf U(\mathbf w)
\cdot(\mathbf g_s-\mathbf g_{s'})\,d^3v\,d^3v'\le0.
$$

不等号来自 $\mathbf a\cdot\mathsf U\cdot\mathbf a=[a^2-(\mathbf a\cdot\widehat{\mathbf w})^2]/w\ge0$；物理熵是 $-k_BH$ 加常数。这里要求正分布、对称的成对对数及零边界通量，正是守恒推导所用的条件。

熵单调性指碰撞贡献或封闭系统整体。开放域需另列源和边界熵流；速度域截断也会流失粒子与能量，应与碰撞离散误差分别核算。

来源：[Fitzpatrick，Landau Collision Operator，式 (3.87)–(3.94)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node37.html)；[Collisional Conservation Laws](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node34.html)；[MIT 22.616，Collisions and Transport Theory II，Collision Operator: Summary](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/3277350d3d1b252bad754cdf65dcf6da_collisionstrans2.pdf)。

### 漂移—扩散算子的可解析矩测试

一维 Lenard–Bernstein 示范算子取
$C=\nu\partial_v(vf+\sigma_b^2\partial_vf)$，$\nu,\sigma_b$ 固定；它描述粒子向给定静止热浴弛豫。对算子分别积分 $1,v,v^2$，速度边界通量为零，分部积分给

$$
\dot n=0,\qquad \frac{d\langle v\rangle}{dt}=-\nu\langle v\rangle,\qquad
\frac{d\langle v^2\rangle}{dt}=-2\nu(\langle v^2\rangle-\sigma_b^2).
$$

因此 $u=u_0e^{-\nu t}$，方差
$\sigma^2=\sigma_b^2+(\sigma_0^2-\sigma_b^2)e^{-2\nu t}$。固定热浴吸收粒子的动量与能量，若把热浴也作为动力学物种求解，就要把这些交换量以相反符号加入背景方程。完整自碰撞 Landau 算子则在物种内部保持相应总动量和能量。

**算例。** 用速度单位 $\sigma_b$，设初始高斯均值 $u_0=2\sigma_b$、方差 $4\sigma_b^2$。在 $t=1/\nu$，均值为 $0.735759\sigma_b$，方差为 $1.40601\sigma_b^2$，二阶原始矩为 $1.94735\sigma_b^2$。后者由方差加均值平方恢复，亦可由 $1+(8-1)e^{-2}$ 直接求得。数值程序可同时测试总粒子数、均值和方差；若只检查归一化，就会漏掉漂移项与扩散项的相对系数错误。[Kunz，§VIII.2，式 (VIII.2.1)–(VIII.2.2)，PDF 第 107 页](https://www.astro.princeton.edu/~kunz/Site/AST554/AST554_Kunz_Lecture_Notes.pdf)。

## 经典热流与 Spitzer 电阻的适用条件

近局地 Maxwell 分布的微小畸变承载热流和电流。在弱耦合、完全电离、非相对论、局地碰撞输运且驱动足够小的情形，沿磁场的纯导热部分可写成

$$
h_{e\parallel}^{(T)}=-\kappa_{e\parallel}^{(\theta)}\nabla_\parallel\theta_e,
\qquad
\kappa_{e\parallel}^{(\theta)}\sim
\frac{n_e\theta_e}{m_e\nu_e},
\qquad \nabla_\parallel=\mathbf b\cdot\nabla.
$$

$h_{e\parallel}^{(T)}$ 是热流的标量平行分量，$\kappa^{(\theta)}$ 的单位为 $\mathrm{m^{-1}\,s^{-1}}$。若用以 K 计的温度梯度，热导率则为 $\kappa^{(T)}=k_{\mathrm B}\kappa^{(\theta)}$，单位 $\mathrm{W\,m^{-1}\,K^{-1}}$。量级估计来自粒子在一个自由程内采样的温差乘以其能量输运通量。电子热流还可能含电流耦合项，总热流还需保留相应热电耦合贡献。

同样，从简化电子动量平衡 $-en_e\mathbf E+\mathbf R_{ei}=0$ 和 $\mathbf J\simeq-en_e(\mathbf u_e-\mathbf u_i)$ 可得到参考电阻率 $\eta\sim m_e\nu_{ei}/(n_ee^2)$，单位 $\Omega\,\mathrm m$。完整 Spitzer 电阻需解线性化碰撞方程，包含电子—电子碰撞对分布形状的影响，其数值系数由线性化速度响应确定。在给定电荷组成且忽略对数缓变时，$\eta\propto\theta_e^{-3/2}$；温度越高，经典电阻通常越小。

“沿场电阻”只描述广义 Ohm 定律中的电阻项。存在压强梯度、电子惯性、流动、Hall 项和热电力时，应在广义欧姆定律中分别保留相应项。多电荷离子还引入 $Z_{\mathrm{eff}}=\sum_i n_iZ_i^2/n_e$，但精确系数也依赖碰撞模型，应采用一致的多离子碰撞系数。

在强磁化而仍满足局地碰撞闭合的经典极限，平行导热量级随 $1/\nu$ 增大，垂直扩散量级则为 $\rho_e^2\nu$；这是两种不同的步长与随机化机制。托卡马克的实测径向热输运还可能由轨道几何与湍流主导。若热流携带粒子的自由程接近温度梯度长度，Spitzer–Härm 局地闭合会失效；采用限流器只是额外模型选择，必须说明限流定义和验证范围。

来源：[Fitzpatrick，Unmagnetized Limit，热流与电导式 (4.84)、(4.87)–(4.94)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node55.html)；[Magnetized Limit，式 (4.95)–(4.106)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node56.html)；[MIT 22.616，Collisions and Transport Theory II: Electrical Conductivity—Spitzer Problem](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/3277350d3d1b252bad754cdf65dcf6da_collisionstrans2.pdf)。

### 一个可手算的动理学热流闭合

为看清热流系数的来源，取定压、无平均流的局部 Maxwellian，温度能量沿 $x$ 缓慢变化。用常碰撞时间 BGK 的一阶展开 $f_1=-\tau v_x\partial_xf_M$。由于定压意味着 $n\theta$ 恒定，

$$
\partial_xf_M=f_M\left(\frac{mv^2}{2\theta}-\frac52\right)
\frac{\partial_x\theta}{\theta}.
$$

该修正的一阶速度矩为零，因 $\langle v_x^2v^2\rangle=5(\theta/m)^2$。求热流还用到 $\langle v_x^2v^4\rangle=35(\theta/m)^3$，由此

$$
h_x=\frac m2\int v^2v_xf_1d^3v
=-\frac52\frac{n\theta\tau}{m}\partial_x\theta.
$$

这些四阶、六阶矩可由三个独立高斯的偶数矩逐项相乘得到。真实 Spitzer–Härm 系数采用速度相关的库仑算子；这个常 $\tau$ 模型保留了从分布修正到热流的计算链。

一维高斯偶数矩 $\langle v_x^{2r}\rangle=(2r-1)!!(\theta/m)^r$ 给出四阶系数5、六阶系数35；代入热流积分即得 $5/2$，同一四阶矩保证 $\int v_xf_1d^3v=0$。

**算例。** 电子 $n=10^{18}\,\mathrm{m^{-3}}$、$\theta=20.0\,\mathrm{eV}$、$\tau=0.100\,\mu\mathrm s$，给定梯度 $2.00\,\mathrm{eV\,m^{-1}}$。把两处 eV 各乘一次 $e$，得 $h_x=-2.81794\times10^5\,\mathrm{W\,m^{-2}}$，沿降温方向。梯度长度为 $10\,\mathrm m$；用 $\sqrt{2\theta/m_e}\tau\approx0.265\,\mathrm m$，Knudsen 数约为 $0.0265$，与一阶局地展开相容。[Kunz，§VIII.1 的 BGK 算子](https://www.astro.princeton.edu/~kunz/Site/AST554/AST554_Kunz_Lecture_Notes.pdf)；[Fitzpatrick，Unmagnetized Limit，热流本构与输运系数](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node55.html)。

## 集体屏蔽、Balescu–Lenard 与多体碰撞的区别

在微观层面，粒子电荷和分布都有涨落。将精确的离散粒子描述分成平均部分与涨落部分，平均加速度项包含形如 $\langle\delta\mathbf E\cdot\nabla_v\delta f_s\rangle$ 的相关项。Vlasov 近似保留平均场作用；碰撞理论则对相应相关项作有条件的近似。长程 Coulomb 系统的碰撞来自许多远程小偏转及集体屏蔽的共同作用。

Debye 屏蔽由许多粒子的响应形成，使用屏蔽截断的 Landau 模型已含有这类集体信息。Balescu–Lenard 理论进一步在弱耦合相关展开中保留背景的动态介电响应；在通常的均匀、稳定、无磁静电推导里，碰撞核带有 $|\varepsilon(\mathbf k,\mathbf k\cdot\mathbf v)|^{-2}$ 这样的屏蔽因子。$\mathbf k$ 是波矢，$\varepsilon$ 是该背景的无量纲纵向介电函数。这里给出因子的结构，而不将它当作可脱离其余积分核单独使用的完整算子。[Princeton，Kunz：AST554 Lecture Notes，§IV.5，式 (IV.5.1)–(IV.5.4)，原文将介电函数记为 $D$](https://www.astro.princeton.edu/~kunz/Site/AST554/AST554_Kunz_Lecture_Notes.pdf)。

集体响应使大冲量参数贡献收敛；短程大角散射仍需与近碰撞描述匹配。经典 Balescu–Lenard 采用弱耦合、稳定背景与相应轨道假设。主对数极限下，它与适当截断的 Landau 描述相容。若要求对数之外的精度，则必须同时处理屏蔽、近碰撞和相应近似的匹配。

集体屏蔽进入二粒子相关闭合的介电函数；真正三体反应或不可约三粒子相关则需另给反应通道、守恒律与统计假设，不能按“参与屏蔽粒子多”归为三体碰撞。

新增碰撞项须交代相关层级、已扣除的二体/集体贡献、退化极限及粒子数—动量—能量守恒；未明确时列为待核实模型。

来源：[Fitzpatrick，Collision Operator，平均与涨落相关](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node31.html)；[MIT 22.616，Collisions and Transport Theory I，Debye cutoff 后关于 Balescu–Lenard 的讨论](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/923ea57a2611e1f05af813f1919354eb_collisionstrans1.pdf)。

### 介电屏蔽如何使长波积分收敛

Balescu–Lenard 核中典型的径向波数积分含 $dk/[k|\epsilon(k,\omega)|^2]$。为单独展示静态屏蔽，取 $\epsilon(k,0)=1+k_D^2/k^2$，并保持一个给定短程上限 $k_{\max}$。以下令 $y=k/k_D$、$K=k_{\max}/k_D$。

这里 $k_D=1/\lambda_D$；静态介电式由 $\delta\rho=-\varepsilon_0k_D^2\phi$ 和 Fourier Poisson 方程 $\varepsilon_0k^2\phi=\rho_{\rm ext}+\delta\rho$ 联立得到，即 $\phi=\rho_{\rm ext}/[\varepsilon_0k^2\epsilon(k,0)]$。场的线性响应带一个 $1/\epsilon$，场相关或扩散率涉及场乘其复共轭，故带 $1/|\epsilon|^2$。以下积分仅保留这一静态径向结构，未替代完整动态共振核。

$$
I(K)=\int_0^K\frac{dy}{y}\left(\frac{y^2}{1+y^2}\right)^2
=\int_0^K\frac{y^3}{(1+y^2)^2}dy
=\frac12\left[\ln(1+K^2)+\frac1{1+K^2}-1\right].
$$

积分最后一步用 $u=1+y^2$ 换元。小 $y$ 时被积函数正比于 $y^3$，长波端自然收敛；大 $K$ 时 $I=\ln K-1/2+O(K^{-2})$，仍保留短尺度对数。这把介质的极化响应与人工截断的主对数做了明确比较，动态核中还要保留共振频率依赖。

**算例。** 选 $k_{\max}=100k_D$，平滑屏蔽积分为 $I=4.10527018$；把屏蔽替换成从 $k_D$ 开始的锐截断，则给 $\int_1^{100}dy/y=\ln100=4.60517019$。二者差为 $0.49990001$，已经接近渐近常数 $1/2$。直接对 $y^3/(1+y^2)^2$ 数值积分可检验原函数及上下限；这个示范比较的是同一给定短程上限下的屏蔽处理方式。[Kunz，§IV.5，式 (IV.5.1)–(IV.5.6)，PDF 第 60–61 页](https://www.astro.princeton.edu/~kunz/Site/AST554/AST554_Kunz_Lecture_Notes.pdf)。

[返回基础原理](../README.md)
