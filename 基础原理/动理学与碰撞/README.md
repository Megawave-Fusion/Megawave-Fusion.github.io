# 动理学与碰撞

动理学以速度分布描述粒子群，碰撞理论解释分布、动量和能量怎样弛豫。本专题采用非相对论、非简并、弱耦合等离子体为默认对象；涉及边界、强耦合、原子过程或快粒子时另行注明限制。各条公式均用 SI 制。温度 $T_s$ 以 K 表示，另记热能 $\theta_s=k_{\mathrm B}T_s$，单位 J；当报出 $T_{s,\mathrm{eV}}$ 时，含义是 $\theta_s=T_{s,\mathrm{eV}}\times1.602176634\times10^{-19}\,\mathrm J$。$e>0$ 是元电荷，物种电荷写成 $q_s$。文中的“核对”指对照公开教材、复核假设和公式，不代表已完成针对所有聚变工况的数值验证。

## 分布函数、速度矩与温度的含义

物种 $s$ 的分布函数 $f_s(\mathbf x,\mathbf v,t)$ 满足：$f_s\,d^3x\,d^3v$ 是相应相空间小体积内的平均粒子数。这里采用粒子数归一化，故 $f_s$ 的 SI 单位为 $\mathrm{s^3\,m^{-6}}$；它不是积分等于一的概率密度。数密度、平均流速及热运动速度定义为

$$
n_s=\int f_s\,d^3v,\qquad
\mathbf u_s=\frac{1}{n_s}\int\mathbf v f_s\,d^3v,\qquad
\mathbf c_s=\mathbf v-\mathbf u_s.
$$

其中 $n_s$ 的单位为 $\mathrm{m^{-3}}$，$\mathbf u_s$ 和 $\mathbf c_s$ 的单位为 $\mathrm{m\,s^{-1}}$。由于 $\int\mathbf c_s f_s\,d^3v=0$，整体平移速度与随机热运动被明确分开。一个速度很大的冷束，可能有很大的定向动能，却不一定有很高的束流自身温度。

压强张量与热流密度是相对于该物种平均流速的中心矩：

$$
\mathbf P_s=m_s\int\mathbf c_s\mathbf c_s f_s\,d^3v,
\qquad
\mathbf h_s=\frac{m_s}{2}\int c_s^2\mathbf c_s f_s\,d^3v.
$$

$\mathbf c_s\mathbf c_s$ 表示二阶张量，$\mathbf P_s$ 的单位是 Pa，$\mathbf h_s$ 的单位是 $\mathrm{W\,m^{-2}}$。本文用 $\mathbf h_s$ 表示热流，以免与电荷 $q_s$ 混淆。定义 $p_s=\operatorname{tr}\mathbf P_s/3$ 后，随机动能密度恒有 $U_s=3p_s/2$；再定义动力学标量温度 $\theta_s=p_s/n_s$。这些等式来自矩定义，不要求分布已经 Maxwell 化，但一个标量温度通常不足以重建非平衡分布。

例如，两束对向粒子可以满足 $\mathbf u_s=0$，却在束流方向有很大的 $P_{s,\parallel}$。把它们替换成相同 $n_s,T_s$ 的 Maxwell 分布，会抹去双峰结构及其可能激发的波。诊断也只测量一定速度、方向或能量范围内的响应，因此“拟合温度”应注明所用谱线、拟合分布与仪器响应。各物种分别使用自己的 $\mathbf u_s$；若改用混合物质心速度，扩散动能会进入相应矩，定义不能混用。

取 $\mathbf v=\mathbf u_s+\mathbf c_s$ 并展开平方，交叉项的积分为零，因此实验室系动能密度严格分解成 $m_sn_su_s^2/2+3p_s/2$。这给数据处理提供了简单核对：若速度分布整体平移，内部温度应保持不变，整体动能则增加。若程序对 $v^2$ 直接平均后称其为温度，就会把旋转、束流或平行流的能量误算成热能。

核对来源：[Fitzpatrick，Moments of Distribution Function，式 (4.5)–(4.18)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node47.html)。上述束流例子是由中心矩定义直接得到的说明。

## Vlasov 方程、Boltzmann 方程与电磁自洽

在平均电磁场中，带碰撞和外部源的动力学方程写为

$$
\frac{\partial f_s}{\partial t}
+\mathbf v\cdot\nabla_x f_s
+\frac{q_s}{m_s}(\mathbf E+\mathbf v\times\mathbf B)
 \cdot\nabla_v f_s
=\sum_{s'}C_{ss'}[f_s,f_{s'}]+S_s.
$$

$C_{ss'}$ 描述 $s'$ 对 $s$ 的碰撞作用，$S_s$ 表示注入、反应或其他明确建模的源汇，两者与 $\partial_t f_s$ 同单位。左侧分别是局地变化、空间输运和速度空间加速。令碰撞与源都为零，便得到 Vlasov 方程；沿平均场特征轨道满足 $df_s/dt=0$。这一结论是相空间密度随轨道守恒，并不意味着空间密度、温度或波幅保持不变。

“无碰撞”指所研究的时间及长度尺度上碰撞项可忽略。它不意味着粒子彼此不作用：粒子通过电荷密度和电流产生场，场又改变粒子轨道。自洽源为

$$
\rho_q=\sum_s q_s\int f_s\,d^3v,\qquad
\mathbf J=\sum_s q_s\int\mathbf v f_s\,d^3v.
$$

完整电磁模型应同时求解 $\nabla\cdot\mathbf E=\rho_q/\varepsilon_0$、$\nabla\cdot\mathbf B=0$、$\partial_t\mathbf B=-\nabla\times\mathbf E$ 及 $\nabla\times\mathbf B=\mu_0\mathbf J+\mu_0\varepsilon_0\partial_t\mathbf E$。若只给定一个外部场而不让粒子反作用于场，得到的是试验粒子模型。若在低频条件下采用准中性或静电近似，必须说明删去哪些场方程、由何种关系确定电场，不能同时任意指定电荷密度和势函数。

Boltzmann 碰撞项以散射前后的分布乘积之差统计增益与损失，常用于二体散射和给定微分截面的模型。对长程 Coulomb 力，裸的散射积分在小偏转处需要集体屏蔽处理；所以“把中性气体的常数碰撞频率塞入方程”不能自动成为准确的聚变等离子体模型。Vlasov、Boltzmann、Landau 是不同近似层次的具体方程名称，使用时应同时给出场模型、碰撞算子、边界和源项。

自洽场还给出一个可直接核查的约束：将各物种连续性方程乘电荷并求和，应得到 $\partial_t\rho_q+\nabla\cdot\mathbf J=0$。这与对 Ampère–Maxwell 方程取散度的结果一致。引入反应源后，所有带电产物与反应物的电荷源总和仍应抵消；只添加电子或只添加离子的源而不说明外部电荷通量，会破坏这条关系和场约束。

核对来源：[Fitzpatrick，Collision Operator，式 (3.1)–(3.9)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node31.html)；[Boltzmann Collision Operator](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node33.html)。

## Maxwell 分布、各向同性与非平衡状态

局地漂移 Maxwell 分布写为

$$
f_{Ms}=n_s\left(\frac{m_s}{2\pi\theta_s}\right)^{3/2}
\exp\!\left[-\frac{m_s|\mathbf v-\mathbf u_s|^2}{2\theta_s}\right].
$$

指数必须无量纲，因此这里放入的是以 J 计的 $\theta_s$。在该物种共动系中，三个速度分量独立且方差均为 $\theta_s/m_s$，从而 $\mathbf P_s=n_s\theta_s\mathbf I$、$\mathbf h_s=0$。零热流来自关于 $\mathbf c_s$ 的奇函数积分；它不排除实验室系存在由流动携带的能量通量。采用 $v_{ts}=\sqrt{2\theta_s/m_s}$ 时，指数是 $-c_s^2/v_{ts}^2$；若采用一维标准差 $\sqrt{\theta_s/m_s}$ 作为“热速度”，所有相关系数都要一致调整。

各向同性仅要求共动系中的分布只依赖 $c_s$，不要求其径向形状是高斯。例如两个不同温度、相同流速的 Maxwell 分布之和仍然各向同性，却通常不等于一个 Maxwell 分布。反过来，磁化等离子体常用的双温 Maxwell 模型可有 $T_\parallel\ne T_\perp$，其压强张量为

$$
\mathbf P_s=p_{s,\perp}(\mathbf I-\mathbf b\mathbf b)
+p_{s,\parallel}\mathbf b\mathbf b,
\qquad \mathbf b=\mathbf B/|\mathbf B|.
$$

对应标量温度满足 $3\theta_s=\theta_{s,\parallel}+2\theta_{s,\perp}$。这只是陀螺对称模型；若存在明显回旋相位依赖，还需非陀螺压强分量。

自碰撞可以使每个物种趋向自身 Maxwell 分布，而电子、离子之间的共同温度建立得更慢。因此 $T_e\ne T_i$ 与各自近 Maxwell 化并不矛盾。对无源、均匀、封闭的弹性碰撞体系，所有相互碰撞物种的共同流速、共同温度 Maxwell 分布才是完整碰撞平衡。若 $n_s,\mathbf u_s,T_s$ 随空间变化，碰撞项在局地可能很小，输运项仍可产生非 Maxwell 修正；局地平衡不等同于整个动力学方程的稳态解。

一个具体反例是相同密度的冷、热组分混合。它们具有同一平均流速时，混合物的标量热能等于两者热能的平均值，但高能尾部仍由较热组分主导。因此相同的密度与二阶矩不能保证相同的聚变反应率、电流驱动响应或高能损失；这些量还取决于分布在有关能量范围内的形状。报告“已热化”时，应说明检查的是各向同性、低阶矩还是整个分布。

核对来源：[Fitzpatrick，Boltzmann H-Theorem](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node40.html)；[Collision Operator for Maxwellian Distributions](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node41.html)。各向同性混合分布的反例和双温标量关系直接由矩定义检验。

## 从动理学推导连续性、动量和内能方程

先考虑无源、只含守恒弹性碰撞的系统，并假设分布在速度无穷远充分衰减，使积分分部的边界项消失。因为 Lorentz 加速度满足 $\nabla_v\cdot\mathbf a_s=0$，对动力学方程直接积分便得到

$$
\partial_t n_s+\nabla\cdot(n_s\mathbf u_s)=0.
$$

其原因是速度空间加速不会创造粒子，且 $\int C_{ss'}d^3v=0$。电离、复合和聚变反应会改变物种数目，加入它们后右侧必须恢复相应源汇，不能把纯弹性结果照搬过去。

再乘以 $m_s\mathbf v$ 并积分，将二阶矩分解为 $m_sn_s\mathbf u_s\mathbf u_s+\mathbf P_s$，借助连续性方程得到

$$
m_sn_s(\partial_t+\mathbf u_s\cdot\nabla)\mathbf u_s
=q_sn_s(\mathbf E+\mathbf u_s\times\mathbf B)
-\nabla\cdot\mathbf P_s+\mathbf R_s,
\qquad
\mathbf R_s=\sum_{s'}\int m_s\mathbf v C_{ss'}\,d^3v.
$$

$\mathbf R_s$ 是碰撞动量交换率密度，单位 $\mathrm{N\,m^{-3}}$。一般压强力是 $-\nabla\cdot\mathbf P_s$，只有各向同性时才退化为 $-\nabla p_s$。相互碰撞物种的动量交换成对相反；不能在电子方程中加入摩擦后，遗漏离子方程的反作用。

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

例如令一对物种的摩擦为 $\mathbf R_{ss'}=-\alpha(\mathbf u_s-\mathbf u_{s'})$，$\alpha>0$，另一物种受到相反作用，则两者整体流动能的碰撞变化率为 $-\alpha|\mathbf u_s-\mathbf u_{s'}|^2$。相应内能总增益必须为正的同一数值。这一代数检查不要求知道热量如何分配给两物种，但足以排除重复加热或遗漏摩擦耗散的记账错误。

核对来源：[Fitzpatrick，Moments of Kinetic Equation，式 (4.33)–(4.38)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node49.html)；[Moments of Collision Operator，式 (4.19)–(4.32)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node48.html)。

## 矩层级、闭合、平均自由程与 Knudsen 数

上述矩方程在其假设范围内是动力学方程的结果，但只求 $n_s,\mathbf u_s,p_s$ 仍不封闭：动量方程需要完整压强张量，内能方程需要热流；继续推导压强张量方程又会出现三阶矩。所谓闭合，是用额外物理假设把高阶矩或碰撞矩表达成已保留变量。直接令热流为零、指定绝热指数、使用 Fourier 热传导，都是不同闭合，不能因为都写成流体方程就当成同一个模型。

对应某一种弛豫频率 $\nu_s$，可定义碰撞平均自由程的估计

$$
\lambda_{\mathrm{mfp},s}\sim\frac{v_{ts}}{\nu_s},\qquad
\mathrm{Kn}_s=\frac{\lambda_{\mathrm{mfp},s}}{L}.
$$

这里 $L$ 是所研究变化的空间尺度，须具体写明，例如温度梯度长度 $L_T=|\nabla\ln T_s|^{-1}$，或沿磁场长度 $L_{T\parallel}=|\mathbf b\cdot\nabla\ln T_s|^{-1}$。$\lambda_{\mathrm{mfp}}$ 的单位为 m，Knudsen 数无量纲。在 Coulomb 小角散射中，它表示速度方向或相关矩累计改变的距离，并非粒子两次接触硬球之间的直线路程。若改用能量弛豫率，得到的长度也会改变。

碰撞流体展开通常要求相关的 $\mathrm{Kn}\ll1$，并要求宏观变化频率小于维持局地平衡所需的碰撞频率。仅有 $\rho_s/L\ll1$，其中 $\rho_s$ 是回旋半径，足以支持某些回旋平均近似，却不保证沿磁场热输运局域。磁化程度 $|\Omega_s|/\nu_s$ 与碰撞局域性 $\lambda_{\mathrm{mfp},s}/L_\parallel$ 是不同判据。

例如下面定义的单电荷电子—离子参考频率，在 $n_e=10^{20}\,\mathrm{m^{-3}}$、$T_{e,\mathrm{eV}}=1000$、指定 $\ln\Lambda=15$ 时约为 $1.38\times10^5\,\mathrm{s^{-1}}$。用 $v_{te}=\sqrt{2\theta_e/m_e}\simeq1.88\times10^7\,\mathrm{m\,s^{-1}}$，估得 $v_{te}/\nu_{ei}\simeq136\,\mathrm m$。这是按同一速度和频率约定算出的示例，不是任一装置的实测值；它说明“存在碰撞”不足以保证米级平行梯度上的局地闭合。高能尾部的有效自由程还可更长，判断热流时不能只检查一个热速度处的数值。

闭合误差与求解误差也应分开。把空间网格加密后，数值结果可能已经收敛到指定流体方程的解，但该解仍可能因非局地热流而偏离动力学结果。验证时应先检查所用小参数，再检查网格、时间步和边界；当两个不同闭合给出不同结果时，不能仅凭哪一个残差更小便认定其物理更准确。

核对来源：[Fitzpatrick，Fluid Closure](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node52.html)；[Braginskii Equations，闭合小参数及式 (4.70)–(4.73)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node54.html)。示例数值由本页所列 SI 公式计算。

## Rutherford 散射与多次小偏转的累积

考虑两粒子在一次遭遇期间可近似不受外磁场和第三方强扰动影响的非相对论 Coulomb 散射。令相对速度大小为 $u=|\mathbf v-\mathbf v'|$，约化质量为 $\mu=m_sm_{s'}/(m_s+m_{s'})$，冲量参数为 $b$。由两体轨道的能量和角动量守恒，偏转角大小 $\chi$ 满足

$$
\tan\frac{\chi}{2}=\frac{b_{90}}{b},\qquad
b_{90}=\frac{|q_sq_{s'}|}{4\pi\varepsilon_0\mu u^2}.
$$

$b_{90}$ 的单位是 m，是相对速度发生 $90^\circ$ 偏转对应的冲量参数；它不等同于所有轨道的最近距离。对排斥势的正碰，最近距离是 $2b_{90}$。当 $b\gg b_{90}$ 时，$\chi\simeq2b_{90}/b$ 很小。异号电荷的轨道弯曲方向改变，但散射角大小由绝对电荷乘积确定。

为了理解小角碰撞为何重要，暂取很重、近静止的散射中心，令轻粒子以速度 $u$ 穿过数密度 $n_{s'}$ 的背景。在 $dt$ 内，冲量参数处于 $[b,b+db]$ 的遭遇数为 $n_{s'}u\,dt\,2\pi b\,db$。随机偏转的均方角增量因而正比于

$$
\frac{d\langle\chi^2\rangle}{dt}
\simeq8\pi n_{s'}u b_{90}^2
\int_{b_{\min}}^{b_{\max}}\frac{db}{b}.
$$

这给出 $n_{s'}u^{-3}\ln\Lambda$ 的速度标度，而不是一个普遍适用于全部碰撞定义的精确频率。推导中假定独立、随机、小角偏转；当累计角已很大，不能继续把单次角相加当作轨道解。对质量相近的两物种，还必须区分相对速度偏转和各自实验室速度变化。

每个对数冲量参数区间贡献相近，远距离的小偏转虽然弱，却因遭遇数多而累积占优。这也是“大角散射很少”与“碰撞能改变分布”能够同时成立的原因。上述直线轨道近似还要求一次主导遭遇的持续时间内回旋弯曲可以忽略；极强磁化导致屏蔽尺度上的轨道明显弯曲时，需要重新检查碰撞核，不能仅把宏观磁场写入运动方程就宣称散射模型仍然成立。

还可用 $b_{90}\propto u^{-2}$ 检查速度标度：把相对速度增大一倍，特定偏转角对应的面积尺度变为原来的十六分之一，而单位时间穿过的长度只增加一倍，因此散射率的量级减为原来的八分之一。这里保持背景密度与 Coulomb 对数不变，仅用于理解高速极限；把它外推到速度低于背景热速度的区域，会遗漏背景粒子的运动。

核对来源：[Fitzpatrick，Two-Body Coulomb Collisions，式 (3.38)–(3.64)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node35.html)；[MIT 22.611J，Collisions in Plasmas，§3.3.4 Random Walk in Angle](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/5617c594de835f49cd769a58ba156ce2_chap3.pdf)。

## Coulomb 对数、屏蔽和短程截断

小角累积中的冲量参数积分产生自然对数

$$
\ln\Lambda=\int_{b_{\min}}^{b_{\max}}\frac{db}{b}
=\ln\!\left(\frac{b_{\max}}{b_{\min}}\right).
$$

它不是任意拟合常数，而是可用近似的长短距离范围之比。经典弱耦合、近热平衡的基本估计采用屏蔽长度作为大尺度截断；若各组分均能作静态热响应，可写

$$
\lambda_D^{-2}=\sum_s\frac{n_sq_s^2}{\varepsilon_0\theta_s},
\qquad b_{\max}\sim\lambda_D.
$$

对运动试验粒子、强温差或有显著动力学响应的背景，哪些物种能够参与屏蔽与其响应时间有关，不能无条件把所有物种都代入静态和式。若粒子在系统中停留时间很短、系统尺寸不足或强磁场修改相遇过程，大尺度估计也需检查。

短距离一端，$b\lesssim b_{90}$ 时小角展开不再适用；若量子衍射长度更大，则应把它纳入下限。只作主对数精度估计时，常写

$$
b_{\min}\sim\max\!\left(b_{90},\frac{\hbar}{\mu u}\right).
$$

其中第二项是按约化 de Broglie 长度定义的量级，某些约定含额外的 $1/2$。这些常数改变对数内的有限项，若要报出精确碰撞系数，必须统一采用同一来源的完整定义，不能任意拼接。量子截断修正也不意味着可以用这一经典算子处理电子简并、Pauli 阻塞或任意强耦合状态。

需要 $b_{\max}\gg b_{\min}$、通常还要求 $\ln\Lambda\gg1$，才能把主对数贡献作为受控近似。若算出 $\ln\Lambda$ 接近零或为负，应该首先判断模型和参数是否越出适用范围，而不是直接将负值塞入扩散系数或随意钳制成一个正数。许多手册中“常数减去对数”的经验公式默认密度单位为 $\mathrm{cm^{-3}}$、温度单位为 eV；把 SI 密度直接代入会造成很大偏差。本页保留带量纲的基本尺度，避免省略这些单位约定。

例如，将某个截断尺度改成原来的两倍，只使 $\ln\Lambda$ 改变 $\ln2$。若原值是十五，对由主对数控制的系数造成约百分之五的变化。这说明保留大量小数并不会自动提高物理精度，也说明对数内的有限常数必须与所采用算子的近似阶数相配。它不说明所有碰撞误差都只有百分之五；强耦合、非热分布等失效机制可能完全改变模型。

核对来源：[Fitzpatrick，Coulomb Logarithm，式 (3.114)–(3.122) 及其单位说明](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node39.html)；[MIT 22.616，Collisions and Transport Theory I，Debye cutoff 讨论](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/923ea57a2611e1f05af813f1919354eb_collisionstrans1.pdf)。

## 偏转、慢化、动量和能量频率不能互换

“碰撞频率”需要同时注明试验粒子、背景物种、所取矩及速度平均。偏转频率描述方向随机化；慢化频率描述平均速度或动量衰减；能量弛豫率描述能量变化；物种温度交换率描述两个分布之间的热交换。它们受不同速度权重和质量比控制，通常只在特定极限下有简单关系。对于 Coulomb 力，尤其不能把一次很弱的近距离或远距离作用都统计成完全失去原方向的“一个碰撞”。

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

这一约定使 $Z=1$、$n_i=n_e$ 时与下引教材的 $1/\tau_e$ 一致。它是特定分布与小漂移展开的频率，不是任意速度试验电子的精确散射率，也不能直接替代 Spitzer 电导的有效响应系数。电子—电子碰撞可以改变单电子运动方向、恢复分布形状，但全部电子之间的内部碰撞不能改变电子总动量；因此不能把 $\nu_{ee}+\nu_{ei}$ 直接当成电流摩擦率。

比较文献中的系数时，应先核对热速度定义、$\nu$ 对应的弛豫对象、是否对 Maxwell 分布平均、离子电荷数及 Coulomb 对数。只比较名称“electron collision frequency”可能把不同问题的答案错误地并在一起。

实际建模还应区分特征频率和实际净交换：两个物种已经共流时，即使 $\nu_{ss'}^{(u)}$ 很大，$\mathbf R_{ss'}$ 仍为零；两物种同温时，热交换系数可以非零而净热交换为零。频率衡量对偏离平衡的响应速度，不能单独解释成当前存在的动量损失或加热功率。输入参数表最好同时记录所乘的流速差、温差或分布梯度。

核对来源：[Fitzpatrick，Collision Times，定义 (3.184)、显式式 (3.188)、(3.190)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node43.html)；[MIT 22.611J，Collisions in Plasmas，§3.3.5、§3.4.5](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/5617c594de835f49cd769a58ba156ce2_chap3.pdf)。本文的反向频率关系由动量守恒单独推得。

## 电子—离子温度交换为什么较慢

电子撞上很重的离子时，运动方向可以明显变化，速率却只发生很小改变。极限 $m_i\to\infty$ 中，静止离子产生的 Coulomb 场只改变电子轨道方向，不向离子传递有限动能。有限质量修正带来约 $m_e/m_i$ 的热交换尺度，因此不能把电子偏转时间直接当成电子—离子温度平衡时间。

考虑单电荷等离子体，$n_e=n_i=n$，两物种近 Maxwell 分布、平均相对漂移可忽略，且 $\theta_e/m_e\gg\theta_i/m_i$。用上一条的 $\nu_{ei}^{(u)}$ 约定，离子获得的热功率密度在该质量比近似下为

$$
Q_i=3\frac{m_e}{m_i}n\nu_{ei}^{(u)}
(\theta_e-\theta_i),\qquad Q_e=-Q_i.
$$

$Q_i$ 单位为 $\mathrm{W\,m^{-3}}$；当 $T_e>T_i$ 时离子被加热，符号正确。这个反对称关系适用于此处忽略相对漂移的热交换。若存在相对漂移，摩擦耗散还会增加随机热能，必须按总能量预算补上，不能仍把全部内能源设为严格相反。

在均匀、无源、密度固定的示例中，使用每物种 $U_s=3n\theta_s/2$，得到

$$
\frac{d\theta_e}{dt}=-2\frac{m_e}{m_i}\nu_{ei}^{(u)}
(\theta_e-\theta_i),\qquad
\frac{d\theta_i}{dt}=+2\frac{m_e}{m_i}\nu_{ei}^{(u)}
(\theta_e-\theta_i).
$$

若把 $\nu_{ei}^{(u)}$ 在平衡附近视为常数，两者同时变化时，温差以 $4(m_e/m_i)\nu_{ei}^{(u)}$ 衰减；若离子温度由外部热浴固定，电子对热浴的衰减率则为 $2(m_e/m_i)\nu_{ei}^{(u)}$。这说明所谓“平衡时间”即使讨论同一物理过程，也要交代是跟踪温差、单物种温度，还是固定背景。离平衡很远时 $\nu\propto\theta_e^{-3/2}$ 随温度变化，不应把整个过程套成单一指数。

电子加热与离子加热因而不能仅按碰撞频率高低相互替换。评估聚变燃料升温，应比较电子—离子交换、外部加热、辐射和约束损失的时间尺度；电子先形成热分布，并不保证离子已经达到相同温度。本条给出的是热 Maxwell 背景间的交换，不用于任意高能离子或电子束的慢化分配。

上述均匀双温模型还有两个简单的不变量检验。在无外部输入时，$\theta_e+\theta_i$ 保持常数；温差则总朝零减小。因此相同粒子数的两物种最终达到初始热能温度的算术平均。若计算得到共同温度高于两者初值的较大者，或温差自行增大，就应首先检查源项符号、热容和单位，而不是把它解释为碰撞产生了额外能量。

核对来源：[Fitzpatrick，Unmagnetized Limit，式 (4.82)、(4.86)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node55.html)；[MIT 22.611J，Collisions in Plasmas，§3.5.4 Energy Equilibration](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/5617c594de835f49cd769a58ba156ce2_chap3.pdf)。两个不同衰减率由本条能量方程相减得到。

## Fokker–Planck、Landau 算子与守恒检验

许多小速度增量的累计效应可表示成速度空间的漂移与扩散。固定背景时，一般 Fokker–Planck 形式为

$$
C[f]=-\frac{\partial}{\partial v_i}(A_i f)
+\frac12\frac{\partial^2}{\partial v_i\partial v_j}(D_{ij}f),
$$

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

物种对必须采用对称一致的 $\ln\Lambda_{ss'}=\ln\Lambda_{s's}$，此处视为给定局地参数；若擅自给两个方向使用不同的对数，可能破坏成对守恒。该算子对给定背景是线性的，对全部自洽分布则是双线性的，并不等于常系数速度扩散。

守恒的核心是 $U_{ij}w_j=0$：核只作用在相对速度的横向方向。速度积分分部并交换粒子标签，可检验每个物种粒子数守恒，以及一对物种的总动量、总动能守恒。共同流速、共同温度 Maxwell 分布代入括号后，其速度导数组合与 $\mathbf w$ 成正比，因此被 $\mathbf U$ 消去。这是无需求解方程就能完成的平衡核对。

完整算子还满足适当边界条件下的 H 定理，即碰撞使熵不减。数值实现应分别检查粒子数、成对动量、成对能量、分布非负性及 Maxwell 平衡残差。只演化试验粒子而固定背景，试验物种自身会失去动量和能量；守恒必须包括背景收到的份额，或在线性化模型中保留补偿性的场粒子项。不能用“算子叫 Landau”替代这些离散验证。

这里的熵单调性是碰撞贡献或封闭系统的整体陈述。若计算区域有粒子流出、外部束流注入或能量抽取，区域内的熵还含边界通量与源项，不能要求每个网格点的熵始终上升。类似地，速度域截断会形成未计入的粒子与能量通量；验证不守恒时，应先区分碰撞离散误差与截断边界损失，逐项列出预算，而不能仅依靠总残差猜测原因。

核对来源：[Fitzpatrick，Landau Collision Operator，式 (3.87)–(3.94)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node37.html)；[Collisional Conservation Laws](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node34.html)；[MIT 22.616，Collisions and Transport Theory II，Collision Operator: Summary](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/3277350d3d1b252bad754cdf65dcf6da_collisionstrans2.pdf)。

## 经典热流与 Spitzer 电阻的适用条件

近局地 Maxwell 分布的微小畸变承载热流和电流。在弱耦合、完全电离、非相对论、局地碰撞输运且驱动足够小的情形，沿磁场的纯导热部分可写成

$$
h_{e\parallel}^{(T)}=-\kappa_{e\parallel}^{(\theta)}\nabla_\parallel\theta_e,
\qquad
\kappa_{e\parallel}^{(\theta)}\sim
\frac{n_e\theta_e}{m_e\nu_e},
\qquad \nabla_\parallel=\mathbf b\cdot\nabla.
$$

$h_{e\parallel}^{(T)}$ 是热流的标量平行分量，$\kappa^{(\theta)}$ 的单位为 $\mathrm{m^{-1}\,s^{-1}}$。若用以 K 计的温度梯度，热导率则为 $\kappa^{(T)}=k_{\mathrm B}\kappa^{(\theta)}$，单位 $\mathrm{W\,m^{-1}\,K^{-1}}$。量级估计来自粒子在一个自由程内采样的温差乘以其能量输运通量。电子热流还可能含电流耦合项，因此总热流不能总用这一纯导热项表示。

同样，从简化电子动量平衡 $-en_e\mathbf E+\mathbf R_{ei}=0$ 和 $\mathbf J\simeq-en_e(\mathbf u_e-\mathbf u_i)$ 可得到参考电阻率 $\eta\sim m_e\nu_{ei}/(n_ee^2)$，单位 $\Omega\,\mathrm m$。完整 Spitzer 电阻需解线性化碰撞方程，包含电子—电子碰撞对分布形状的影响，其数值系数不等于粗略摩擦模型的系数。在给定电荷组成且忽略对数缓变时，$\eta\propto\theta_e^{-3/2}$；温度越高，经典电阻通常越小。

“沿场电阻”只描述广义 Ohm 定律中的电阻项。存在压强梯度、电子惯性、流动、Hall 项和热电力时，不能把完整关系简化为 $\mathbf E=\eta\mathbf J$ 后仍声称保留了全部效应。多电荷离子还引入 $Z_{\mathrm{eff}}=\sum_i n_iZ_i^2/n_e$，但精确系数也依赖碰撞模型，不能仅在纯氢数值式中机械换一个电荷数。

在强磁化而仍满足局地碰撞闭合的经典极限，平行导热量级随 $1/\nu$ 增大，垂直扩散量级则为 $\rho_e^2\nu$；这是两种不同的步长与随机化机制。托卡马克的实测径向热输运还可能由轨道几何与湍流主导。若热流携带粒子的自由程接近温度梯度长度，Spitzer–Härm 局地闭合会失效；采用限流器只是额外模型选择，必须说明限流定义和验证范围。

核对来源：[Fitzpatrick，Unmagnetized Limit，热流与电导式 (4.84)、(4.87)–(4.94)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node55.html)；[Magnetized Limit，式 (4.95)–(4.106)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node56.html)；[MIT 22.616，Collisions and Transport Theory II: Electrical Conductivity—Spitzer Problem](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/3277350d3d1b252bad754cdf65dcf6da_collisionstrans2.pdf)。

## 集体屏蔽、Balescu–Lenard 与多体碰撞的区别

在微观层面，粒子电荷和分布都有涨落。将精确的离散粒子描述分成平均部分与涨落部分，平均加速度项包含形如 $\langle\delta\mathbf E\cdot\nabla_v\delta f_s\rangle$ 的相关项。Vlasov 近似保留平均场作用；碰撞理论则对相应相关项作有条件的近似。因此，把碰撞解释成许多独立硬球式接触并不适合长程 Coulomb 系统。

Debye 屏蔽由许多粒子的响应形成，使用屏蔽截断的 Landau 模型已含有这类集体信息。Balescu–Lenard 理论进一步在弱耦合相关展开中保留背景的动态介电响应；在通常的均匀、稳定、无磁静电推导里，碰撞核带有 $|\varepsilon(\mathbf k,\mathbf k\cdot\mathbf v)|^{-2}$ 这样的屏蔽因子。$\mathbf k$ 是波矢，$\varepsilon$ 是该背景的无量纲纵向介电函数。这里给出因子的结构，而不将它当作可脱离其余积分核单独使用的完整算子。[Princeton，Kunz：AST554 Lecture Notes，§IV.5，式 (IV.5.1)–(IV.5.4)，原文将介电函数记为 $D$](https://www.astro.princeton.edu/~kunz/Site/AST554/AST554_Kunz_Lecture_Notes.pdf)。

集体响应消除了裸长程相互作用在大冲量参数处的不合理贡献，但经典弱偏转形式仍不能正确处理任意短程大角散射；Balescu–Lenard 因而不是自动解决全部截断、强耦合、强磁化和不稳定背景问题的万能方程。主对数极限下，它与适当截断的 Landau 描述相容。若要求对数之外的精度，则必须同时处理屏蔽、近碰撞和相应近似的匹配，不能仅把 $\ln\Lambda$ 调成更复杂的数值。

尤其应区分“集体屏蔽”“二粒子相关”“真正的三体过程”。屏蔽云由很多粒子组成，并不意味着每次有效散射都是三粒子同时近距离相遇；从二粒子相关闭合得到的碰撞算子也不应仅因含介电函数就改名三体碰撞项。真正的三体反应、复合或不可约三粒子相关，需要相应反应通道、守恒关系和统计假设，不能由碰撞核含三个积分变量或密度的某个幂次来判断。

在聚变知识整理中，遇到声称存在新碰撞项的模型，至少应说明它从哪个相关层级导出、减去了哪些已有二体和集体贡献、在哪个参数极限变小，以及是否保持粒子数、动量和能量预算。没有这些信息时，可将其列为待核实模型，而不宜直接并入标准 Landau 理论。本条只建立概念边界，不宣称某个具体高阶碰撞模型已被实验验证。

核对来源：[Fitzpatrick，Collision Operator，平均与涨落相关](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node31.html)；[MIT 22.616，Collisions and Transport Theory I，Debye cutoff 后关于 Balescu–Lenard 的讨论](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/923ea57a2611e1f05af813f1919354eb_collisionstrans1.pdf)。

[返回基础原理](../README.md)
