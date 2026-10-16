# 流体与磁流体力学

本专题把粒子的集体运动连接到宏观平衡、磁场演化和能量守恒。采用 SI 单位；$\rho$ 为质量密度，$\rho_c$ 为电荷密度，$\mathbf u$ 为质心速度，$\mathbf J$ 为电流密度，$p$ 为电子与离子总热压力。电阻率写作 $\eta$，磁扩散率另写 $D_m=\eta/\mu_0$，两者单位不同。

建议先读 [动理学与碰撞](../动理学与碰撞/README.md) 中的矩与闭合，再读本页。下文给出具体模型及其条件；“MHD”不代表能自动描述所有碰撞性、频率和尺度下的等离子体。资料与公式复核日期：2026-10-16；领域专家审核仍待完成。

## 从双流体到单流体

对单一电荷数 $Z=1$ 的离子和电子，准中性近似下 $n_e\simeq n_i=n$。定义

$$
\rho=n(m_i+m_e),\qquad
\mathbf u=\frac{m_i\mathbf u_i+m_e\mathbf u_e}{m_i+m_e},\qquad
\mathbf J=en(\mathbf u_i-\mathbf u_e).
$$

所以 $m_e\ll m_i$ 时 $\mathbf u\simeq\mathbf u_i$，但 $\mathbf u_e=\mathbf u_i-\mathbf J/(en)$；单流体不等于电子与离子完全同速。电流恰恰来自两者相对运动。多离子组分应从 $\rho=\sum_s m_sn_s$ 与 $\mathbf J=\sum_s q_sn_s\mathbf u_s$ 重新求和，不能把所有离子当成氢。

对两种动量方程相加，组分间碰撞动量交换抵消。再忽略小的电荷分离力、相对漂移动量通量以及黏性，采用标量总压力 $p=p_e+p_i$，得到 $\rho D_t\mathbf u=-\nabla p+\mathbf J\times\mathbf B$。如果快粒子压力、各向异性应力或多组分漂移显著，就应把相应张量及耦合保留下来。

这里 $D_t=\partial_t+\mathbf u\cdot\nabla$。常见 MHD 尺度检查包括 $\omega\ll |\Omega_i|$、$k_\perp\rho_i\ll1$、$kd_i\ll1$，其中 $d_i=c/\omega_{pi}$；这些是针对所研究运动的排序，不足以单独证明压力闭合正确。特别是弱碰撞聚变等离子体的平行热流，可能需要动理学闭合。

来源：[Fitzpatrick，MHD Equations，§4.14，式 (4.192)–(4.198)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node59.html)；[Closure in Collisionless Magnetized Plasmas，§4.16](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node61.html)。

## 理想 MHD 的方程与适用条件

无外加质量源、无黏性、无热传导、无辐射和不可逆加热，压力各向同性时，常用理想 MHD 为

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf u)=0,
\qquad \rho D_t\mathbf u=-\nabla p+\mathbf J\times\mathbf B,
$$

$$
\mathbf E+\mathbf u\times\mathbf B=0,
\qquad \partial_t\mathbf B=\nabla\times(\mathbf u\times\mathbf B),
\qquad \nabla\cdot\mathbf B=0,
$$

$$
\mu_0\mathbf J=\nabla\times\mathbf B,
\qquad D_t(p\rho^{-\gamma})=0.
$$

单原子、非相对论、三维各向同性的绝热理想气体取 $\gamma=5/3$。最后一式结合连续性方程等价于 $D_tp=-\gamma p\nabla\cdot\mathbf u$：压缩使压力升高。若存在源项或明显热流，必须改用能量方程，不能一边加热一边维持该绝热关系不变。

这里忽略了位移电流，适用于非相对论、低频的宏观运动；特别要求相关传播速度远小于 $c$。模型仍允许非零电场 $\mathbf E=-\mathbf u\times\mathbf B$。理想导电并不意味着实验室系 $\mathbf E=0$，也不意味着所有实际等离子体永远没有电阻效应。

有强非麦克斯韦尾部、回旋共振、有限拉莫尔半径或磁场零点时，应重新评估模型。弱碰撞情况下不能仅凭磁化强就宣布标量绝热闭合成立。

来源：[Fitzpatrick，Magnetohydrodynamic Fluids: Introduction，§8.1，式 (8.1)–(8.6)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node104.html)。

## 广义欧姆定律与 Hall 项

先保留电子动量方程，而不是直接假定理想导电。对准中性单电荷离子体系，设电子压力张量为 $\mathbf P_e$，电子所受碰撞动量交换力密度为 $\mathbf R_e$，则代数整理给出

$$
\mathbf E+\mathbf u_i\times\mathbf B
=\frac{\mathbf J\times\mathbf B}{en}
-\frac{\nabla\cdot\mathbf P_e}{en}
-\frac{m_e}{e}(\partial_t+\mathbf u_e\cdot\nabla)\mathbf u_e
+\frac{\mathbf R_e}{en}.
$$

这是以离子速度写出的形式；若改成质心速度并把惯性改写成 $\partial_t\mathbf J$，还会产生对流与密度项，不应只抄一个时间导数。用简化各向同性摩擦 $\mathbf R_e=en\eta\mathbf J$，且 $\mathbf P_e=p_e\mathbf I$，右边分别为 Hall、电子压力、电子惯性和电阻项。真实磁化输运还可能有张量电阻、热力等贡献。

各项单位都是 $\mathrm{V\,m^{-1}}$。Hall 项满足 $\mathbf J\cdot(\mathbf J\times\mathbf B)=0$，因此本身不产生焦耳耗散，却会改变磁场随哪个流体运动。压力项能够在电子内能与场之间转移能量，不能一律叫作电阻。忽略哪些项要比较其量级，不能仅凭模型名字删项；在电流薄层内，整体很小的非理想项仍可能成为主项。

来源：[Kimura 与 Morrison，On energy conservation in extended magnetohydrodynamics (2014)，§II–III](https://web2.ph.utexas.edu/~morrison/14_morrison_POP_kimura.pdf)；[MIT 22.611J，第 4 章 §4.6，双流体到单流体推导](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/resources/chap4/)。本文电子速度形式直接由电子动量守恒整理，避免混用不同截断模型。

## 磁压力、磁张力与等离子体 beta

由安培定律和矢量恒等式，磁力密度可以写成

$$
\mathbf J\times\mathbf B
=-\nabla\frac{B^2}{2\mu_0}
+\frac{(\mathbf B\cdot\nabla)\mathbf B}{\mu_0}.
$$

第一项与磁场强度梯度有关，第二项包含弯曲磁场的张力。取 $\mathbf b=\mathbf B/B$、曲率 $\boldsymbol\kappa=(\mathbf b\cdot\nabla)\mathbf b$，垂直分量是

$$
(\mathbf J\times\mathbf B)_\perp
=-\nabla_\perp\frac{B^2}{2\mu_0}
+\frac{B^2}{\mu_0}\boldsymbol\kappa.
$$

注意曲率张力系数是 $B^2/\mu_0$；$B^2/(2\mu_0)$ 是磁压力和磁能密度。二者都可出现，不能因名称相近丢掉因子 2。恒等式也给出 $\mathbf B\cdot(\mathbf J\times\mathbf B)=0$，磁力本身没有沿磁场分量。

定义局域 $\beta=2\mu_0p/B^2$。假想均匀氘等离子体 $n_e=n_i=10^{20}\,\mathrm{m^{-3}}$，$T_e=T_i=10\,\mathrm{keV}$，$B=5\,\mathrm T$，用 $p=n_ek_BT_e+n_ik_BT_i$ 得 $p\simeq3.204\times10^5\,\mathrm{Pa}$，磁压力约 $9.947\times10^6\,\mathrm{Pa}$，故 $\beta\simeq0.0322$。这里 keV 表示 $k_BT$ 的能量值。此为量级算例，不是装置测量；平均 beta、极向 beta、归一化 beta 不能与这个局域定义混用。

来源：[Fitzpatrick，Magnetic Pressure，§8.2，式 (8.7)–(8.12)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node105.html)；[Plasma Beta，§1.9](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node11.html)。

## 磁通冻结的精确含义

令闭合曲线 $C(t)$ 随局部流体速度 $\mathbf u$ 移动，$S(t)$ 为以它为边界的曲面。法拉第定律与运动曲面的输运公式给出

$$
\frac{d}{dt}\int_{S(t)}\mathbf B\cdot d\mathbf S
=-\oint_{C(t)}(\mathbf E+\mathbf u\times\mathbf B)\cdot d\boldsymbol\ell.
$$

理想欧姆定律使右边为零，故守恒的是穿过物质回路的磁通，不是任意固定空间点的 $B$。在光滑流动与磁场条件下，这意味着磁力线连接关系随流体保持。粒子仍可沿磁场流动；“冻结”不是每个粒子停在某根几何曲线上，也不是单粒子磁矩守恒的别名。

利用 $\nabla\cdot\mathbf B=0$，将感应方程展开并与连续性方程组合，可进一步得到

$$
D_t\left(\frac{\mathbf B}{\rho}\right)
=\left(\frac{\mathbf B}{\rho}\cdot\nabla\right)\mathbf u.
$$

因此磁场可随拉伸和压缩改变。比如均匀各向同性压缩，长度缩放为 $a$，质量守恒给 $\rho\propto a^{-3}$，磁通守恒给 $B\propto a^{-2}\propto\rho^{2/3}$。若感应方程含显著非理想项，不能继续套用理想冻结结论。

来源：[Fitzpatrick，Flux Freezing，§8.3，式 (8.13)–(8.21)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node106.html)。

## 电阻扩散、磁雷诺数与 Lundquist 数

对标量电阻率 $\eta$，由 $\mathbf E+\mathbf u\times\mathbf B=\eta\mathbf J$ 得

$$
\partial_t\mathbf B=\nabla\times(\mathbf u\times\mathbf B)
-\nabla\times\left(\frac{\eta}{\mu_0}\nabla\times\mathbf B\right).
$$

只有 $\eta$ 空间均匀且 $\nabla\cdot\mathbf B=0$ 时，最后一项才等于 $D_m\nabla^2\mathbf B$。$\eta$ 的单位为 $\Omega\,\mathrm m$，$D_m=\eta/\mu_0$ 为 $\mathrm{m^2\,s^{-1}}$。把电阻率直接放在拉普拉斯项前会造成 SI 量纲错误。

取尺度 $L$ 与流速 $U$，定义

$$
\tau_R=\frac{L^2}{D_m},\quad \tau_U=\frac LU,\quad
R_m=\frac{UL}{D_m},\qquad
v_A=\frac{B}{\sqrt{\mu_0\rho}},\quad
S=\frac{Lv_A}{D_m}=\frac{\tau_R}{\tau_A},\quad \tau_A=\frac L{v_A}.
$$

$R_m$ 使用实际特征流速，$S$ 使用 Alfvén 速度；只有 $U=v_A$ 才相等。$R_m\gg1$ 表示在给定尺度平流占优，不能排除更薄尺度上的扩散或重联。

一个可检验解是无流、周期区域内 $B_y(x,t)=B_1\sin(kx)e^{-D_mk^2t}$，其他分量为零。其振幅衰减时间是 $1/(D_mk^2)$；若 $L$ 取波长，则是 $L^2/(4\pi^2D_m)$，不是精确等于量级估计 $\tau_R$。磁能按振幅平方衰减，衰减率多一个因子 2。

来源：[Fitzpatrick，MHD Dynamo Theory，§8.9，式 (8.100)–(8.102)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node112.html)；[Magnetic Reconnection: Introduction，§9.1](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node123.html)。

## 静态平衡与 Grad–Shafranov 方程

无流、各向同性、忽略重力时，平衡要求 $\nabla p=\mathbf J\times\mathbf B$。点乘 $\mathbf B$ 得 $\mathbf B\cdot\nabla p=0$：压力沿磁力线恒定。有良好嵌套磁面时通常写成磁面函数；这不是任意三维磁场都存在全局磁面的证明。

在轴对称圆柱坐标 $(R,\phi,Z)$ 中，明确采用磁通约定

$$
\mathbf B=\frac{1}{R}\nabla\psi\times\mathbf e_\phi
+\frac{F(\psi)}R\mathbf e_\phi.
$$

$\psi$ 是极向磁通除以 $2\pi$，单位 Wb，$F=RB_\phi$ 的单位为 T m。由此 $B_R=-\partial_Z\psi/R$、$B_Z=\partial_R\psi/R$，安培定律给 $\mu_0J_\phi=-\Delta^*\psi/R$。力平衡化为

$$
\Delta^*\psi=-\mu_0R^2\frac{dp}{d\psi}-F\frac{dF}{d\psi},\qquad
\Delta^*=R\frac{\partial}{\partial R}\left(\frac1R\frac{\partial}{\partial R}\right)+\frac{\partial^2}{\partial Z^2}.
$$

需要给定压力和电流相关剖面以及边界条件才构成可求解问题。固定边界计算给定等离子体边界；自由边界计算还必须包含外部线圈、真空场和边界确定。改变磁通符号或是否除 $2\pi$，所有导数和电流符号必须一致改变。

方程只检验该模型下的力平衡。求得平衡既不证明它稳定，也不确定输运损失。三维仿星器、有流或压力各向异性的系统需要相应推广。

来源：[Fitzpatrick，Grad-Shafranov Equation，§14.3，式 (14.30)–(14.33)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node169.html)；[Xu 与 Fitzpatrick (2019)，§2，式 (1)–(3)，归一化约定](https://farside.ph.utexas.edu/Papers/Xu_2019_Nucl._Fusion_59_064002.pdf)。

## 能量守恒与欧姆加热

理想 MHD 的总能量密度包括宏观动能、内能和磁能：

$$
\mathcal E=\frac12\rho u^2+\frac p{\gamma-1}+\frac{B^2}{2\mu_0}.
$$

在无外源、无耗散的上述模型下，连续性、动量、压力和感应方程相加得到

$$
\partial_t\mathcal E+\nabla\cdot\left[
\left(\mathcal E+p+\frac{B^2}{2\mu_0}\right)\mathbf u
-\frac{\mathbf B(\mathbf u\cdot\mathbf B)}{\mu_0}
\right]=0.
$$

积分后的能量变化取决于边界通量；开放系统中“总能量守恒”不意味着计算域内能量恒定。这里已忽略非相对论 MHD 排序下较小的电场能，不能把此式当成完整 Maxwell 能量定理。

在电阻 MHD 中 $\mathbf E=-\mathbf u\times\mathbf B+\eta\mathbf J$，因此

$$
\mathbf J\cdot\mathbf E=\mathbf u\cdot(\mathbf J\times\mathbf B)+\eta J^2.
$$

右边第一项是场与宏观流动的机械能交换，第二项是非负的焦耳加热（$\eta\ge0$）。相应内能方程为

$$
\partial_t\frac p{\gamma-1}+\nabla\cdot\left(\frac p{\gamma-1}\mathbf u\right)
=-p\nabla\cdot\mathbf u+\eta J^2
$$

（本式未加热流、黏性或其他源）。电阻使磁能转成内能，并不会让封闭绝热系统的总能量凭空消失。若模拟只在感应方程加扩散却不给内能补上焦耳热，会破坏这项预算。检查加热模型时还要避免把同一 $\mathbf J\cdot\mathbf E$ 同时算作机械功与全部热源而重复记账。

来源：[Kimura 与 Morrison (2014)，§III，能量守恒与模型截断](https://web2.ph.utexas.edu/~morrison/14_morrison_POP_kimura.pdf)；[MIT 22.615，MHD Theory of Fusion Systems](https://ocw.mit.edu/courses/22-615-mhd-theory-of-fusion-systems-spring-2007/)。上式为本页所列基础方程的直接组合；含电子惯性的扩展模型必须连同其额外能量一起处理。

## 平衡、线性稳定性与能量原理

平衡满足静态方程，稳定性回答受到扰动后是否增长。对静态理想 MHD 平衡，使用位移 $\boldsymbol\xi$，一阶扰动满足

$$
\delta\mathbf B=\nabla\times(\boldsymbol\xi\times\mathbf B_0),\qquad
\delta p=-\boldsymbol\xi\cdot\nabla p_0-\gamma p_0\nabla\cdot\boldsymbol\xi.
$$

将它们代入线性动量方程写为 $\rho_0\partial_t^2\boldsymbol\xi=\mathcal F[\boldsymbol\xi]$。对使力算符自伴的边界条件，定义势能二阶变分

$$
\delta W=-\frac12\int\boldsymbol\xi^*\cdot\mathcal F[\boldsymbol\xi]\,dV.
$$

例如等离子体边界紧贴固定理想导体壁、平衡磁场沿壁面时，要求壁上 $\boldsymbol\xi\cdot\mathbf n=0$，并在域内满足相应正则性条件；这里 $\mathbf n$ 为壁面单位法向。对正规模 $e^{-i\omega t}$，有 $\omega^2\int\rho_0|\boldsymbol\xi|^2dV=2\delta W$。存在允许的负 $\delta W$ 位移意味着理想失稳方向；若对所有非平凡允许扰动严格为正，则在该理想静态框架内具有能量稳定性。零值需要进一步分析中性模，不能直接判为增长模。

自由边界问题还要计入真空、表面和壁等相应能量，不能只截取等离子体体积分。平衡流可改变算符性质。电阻撕裂、动理学或快粒子驱动失稳也可能在理想 MHD 稳定的状态出现。因此一次平衡求解或一个 beta 数值不构成完整稳定性评估。

来源：[MIT 22.615，Lecture 14，第 4–6 页，自伴性与固定边界](https://ocw.mit.edu/courses/22-615-mhd-theory-of-fusion-systems-spring-2007/cda9ba8f1dd4c9f2f9abecc8d010adae_lecture14.pdf)；[Lecture 16，第 1–5 页，能量原理、表面与真空能量](https://ocw.mit.edu/courses/22-615-mhd-theory-of-fusion-systems-spring-2007/8cdfc4d94a61aa60d91bc02046597130_lecture16.pdf)；[MIT 22.611J，第 4 章 §4.13–4.15](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/resources/chap4/)。

## 磁重联与 Sweet–Parker 标度

磁重联涉及磁场连接关系变化及能量转换；在光滑理想单流体模型中被磁通冻结约束，故重联区域必须考虑适当的非理想物理。电阻、电子压力张量、电子惯性等项是否重要，应由局部尺度判定。

经典 Sweet–Parker 模型假设二维、稳态、近不可压缩、反平行上游磁场与细长层流电流片。设半长 $L$、半厚 $\delta$，两侧密度相近；只求量级，不追求取决于几何定义的常数。质量守恒与磁张力加速给

$$
v_{\rm in}L\sim v_{\rm out}\delta,\qquad v_{\rm out}\sim v_A.
$$

上游理想电场 $E\sim v_{\rm in}B$ 与片内电阻电场 $E\sim\eta B/(\mu_0\delta)$ 匹配，推出

$$
\frac\delta L\sim S^{-1/2},\qquad
\frac{v_{\rm in}}{v_A}\sim S^{-1/2},\qquad
\tau_{\rm SP}\sim\tau_A S^{1/2}\sim\sqrt{\tau_A\tau_R}.
$$

大 $S$ 下电流片很薄，整体重联速度相对 $v_A$ 很慢。例如纯标度算例 $S=10^8$ 给 $\delta/L\sim10^{-4}$。但继续减薄可能使离子/电子尺度、Hall 效应或电流片不稳定性变得重要，此时层流电阻模型不再适用。该推导不是所有重联事件的普适速率，也不能凭它预报具体装置的破裂时间。

来源：[Fitzpatrick，Sweet-Parker Reconnection，§9.9，式 (9.138)–(9.153)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node131.html)。

[返回基础原理](../README.md)
