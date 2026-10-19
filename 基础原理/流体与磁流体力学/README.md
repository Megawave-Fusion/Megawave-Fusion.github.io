# 流体与磁流体力学

本专题把粒子的集体运动连接到宏观平衡、磁场演化和能量守恒。采用 SI 单位；$\rho$ 为质量密度，$\rho_c$ 为电荷密度，$\mathbf u$ 为质心速度，$\mathbf J$ 为电流密度，$p$ 为电子与离子总热压力。电阻率写作 $\eta$，磁扩散率另写 $D_m=\eta/\mu_0$，两者单位不同。

建议先读 [动理学与碰撞](../动理学与碰撞/README.md) 中的矩与闭合，再读本页。下文按长波低频排序连接单流体模型、宏观平衡与磁场演化。

## 从双流体到单流体

对单一电荷数 $Z=1$ 的离子和电子，准中性近似下 $n_e\simeq n_i=n$。定义

$$
\rho=n(m_i+m_e),\qquad
\mathbf u=\frac{m_i\mathbf u_i+m_e\mathbf u_e}{m_i+m_e},\qquad
\mathbf J=en(\mathbf u_i-\mathbf u_e).
$$

所以 $m_e\ll m_i$ 时 $\mathbf u\simeq\mathbf u_i$，但 $\mathbf u_e=\mathbf u_i-\mathbf J/(en)$，电子与离子仍保留承载电流的相对速度。电流恰恰来自两者相对运动。多离子组分应从 $\rho=\sum_s m_sn_s$ 与 $\mathbf J=\sum_s q_sn_s\mathbf u_s$ 重新求和，保留各组分的实际质量和电荷。

对两种动量方程相加，组分间碰撞动量交换抵消。再忽略小的电荷分离力、相对漂移动量通量以及黏性，采用标量总压力 $p=p_e+p_i$，得到 $\rho D_t\mathbf u=-\nabla p+\mathbf J\times\mathbf B$。如果快粒子压力、各向异性应力或多组分漂移显著，就应把相应张量及耦合保留下来。

中间的守恒形式是 $\partial_t(\rho\mathbf u)+\nabla\cdot\sum_sm_sn_s\mathbf u_s\mathbf u_s=-\nabla\cdot(\mathbf P_e+\mathbf P_i)+\rho_c\mathbf E+\mathbf J\times\mathbf B$，其中电力、电流来自逐物种电磁力求和。用下方质心分解，动量通量恰好为 $\rho\mathbf u\mathbf u+n\mu_r\mathbf w\mathbf w$，$\mathbf w=\mathbf u_i-\mathbf u_e$、$\mu_r=m_im_e/(m_i+m_e)$。舍去相对通量、净电荷力并用总质量连续性，才化成所列单流体对流方程；这些是约化假设，不能仅靠准中性自动删除。

这里 $D_t=\partial_t+\mathbf u\cdot\nabla$。常见 MHD 尺度检查包括 $\omega\ll |\Omega_i|$、$k_\perp\rho_i\ll1$、$kd_i\ll1$，其中 $d_i=c/\omega_{pi}$；这些是针对所研究运动的排序，不足以单独证明压力闭合正确。特别是弱碰撞聚变等离子体的平行热流，可能需要动理学闭合。

来源：[Fitzpatrick，MHD Equations，§4.14，式 (4.192)–(4.198)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node59.html)；[Closure in Collisionless Magnetized Plasmas，§4.16](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node61.html)。

### 质心变换怎样拆分流动能

令 $M=m_i+m_e$、$\mathbf w=\mathbf J/(en)$。把质心定义与电流定义作为两个联立方程，先由 $\mathbf u_i-\mathbf u_e=\mathbf w$ 消去电子速度，再得到

$$
\mathbf u_i=\mathbf u+\frac{m_e}{M}\mathbf w,\qquad
\mathbf u_e=\mathbf u-\frac{m_i}{M}\mathbf w.
$$

将它们代入两种粒子的宏观动能，正负交叉项 $nm_im_e\mathbf u\cdot\mathbf w/M$ 相消，留下

$$
\frac n2(m_iu_i^2+m_eu_e^2)
=\frac{\rho u^2}{2}+\frac{n\mu_r w^2}{2},\qquad
\mu_r=\frac{m_im_e}{M}.
$$

第二项是电流携带的相对漂移动能；其系数含约化质量。以 $m_e/m_i$ 为小参数时，它约等于 $m_eJ^2/(2ne^2)$，这说明保留电子惯性的模型为何会出现额外能量项。

**算例。** 取单电离氘 $n=10^{19}\,\mathrm{m^{-3}}$，同向的 $J=10^6\,\mathrm{A\,m^{-2}}$、$u=10^4\,\mathrm{m\,s^{-1}}$。先算 $w=J/(en)=6.24151\times10^5\,\mathrm{m\,s^{-1}}$，再乘质量比，得到 $u_i=1.01700\times10^4$、$u_e=-6.13981\times10^5\,\mathrm{m\,s^{-1}}$。相对漂移动能为 $n\mu_rw^2/2=1.77386\,\mathrm{J\,m^{-3}}$。离子速度接近质心速度，电子沿反向运动承载大部分电流；该分解把两种运动的能量分别列清楚。

推导依据：[Fitzpatrick，§4.14 的质心与电流定义](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node59.html)；[Kimura–Morrison，§II.A–B 的双流体变量与扩展 MHD 能量](https://web2.ph.utexas.edu/~morrison/14_morrison_POP_kimura.pdf)。

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

单原子、非相对论、三维各向同性的绝热理想气体取 $\gamma=5/3$。最后一式结合连续性方程等价于 $D_tp=-\gamma p\nabla\cdot\mathbf u$：压缩使压力升高。若存在源项或明显热流，必须改用能量方程，将加热与热流作为相应源项。

各式的来源分别为：质量方程是各组分数目方程乘质量求和；动量方程是上一条的两流体求和；理想欧姆定律是下条广义欧姆定律在 Hall、压力、惯性和电阻电场均可忽略时的最低阶关系；将其代入 Faraday 定律即得感应方程，$\nabla\cdot\partial_t\mathbf B=0$ 保持初始无散度约束。压力闭合来自内能密度 $w_{\rm th}=p/(\gamma-1)$ 与无热源第一定律 $D_tw_{\rm th}=-(w_{\rm th}+p)\nabla\cdot\mathbf u$；对三维平动 $w_{\rm th}=3p/2$，故 $\gamma=5/3$。安培关系则是 Maxwell 方程在位移电流较小排序下的近似。

这里忽略了位移电流，适用于非相对论、低频的宏观运动；特别要求相关传播速度远小于 $c$。模型仍允许非零电场 $\mathbf E=-\mathbf u\times\mathbf B$。理想导电使随流系电场为零，实验室系则保留运动电场。

有强非麦克斯韦尾部、回旋共振、有限拉莫尔半径或磁场零点时，应重新评估模型。弱碰撞情况下，压力各向异性与平行热流由额外闭合关系描述。

来源：[Fitzpatrick，Magnetohydrodynamic Fluids: Introduction，§8.1，式 (8.1)–(8.6)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node104.html)。

### 把绝热压力方程积分成压缩功

跟随一个质量固定的流体元，其体积满足 $\dot V=V\nabla\cdot\mathbf u$。把它代入压力方程，得到 $dp/p=-\gamma\,dV/V$，积分为 $pV^\gamma=p_0V_0^\gamma$。热内能是 $U=pV/(\gamma-1)$，对它微分可直接看出

$$
dU=\frac{V\,dp+p\,dV}{\gamma-1}
=-p\,dV.
$$

于是压缩过程中外界对流体元做的功为

$$
W_{\rm on}=-\int_{V_0}^{V_1}p_0
 \left(\frac{V_0}{V}\right)^\gamma dV
=\frac{p_1V_1-p_0V_0}{\gamma-1}.
$$

这一计算针对各向同性、无热流及不可逆热源的热压力部分；磁能随形变的变化另由感应方程计算。它也给出温度关系 $\Theta\propto V^{1-\gamma}$，其中 $\Theta=k_BT$。

**算例。** 已知 $\gamma=5/3$，$p_0=2000\,\mathrm{Pa}$、$V_0=10^{-3}\,\mathrm{m^3}$，压缩到 $V_1=V_0/8$。代入得到 $p_1=2000\times8^{5/3}=64000\,\mathrm{Pa}$，温度升至原来的 $8^{2/3}=4$ 倍。初末内能分别为 $U_0=2000\times10^{-3}/(2/3)=3\,\mathrm J$ 和 $U_1=64000\times1.25\times10^{-4}/(2/3)=12\,\mathrm J$。压力积分给出的压缩功为 $9\,\mathrm J$，恰等于热内能增加量，且 $\mathrm{Pa\,m^3}=\mathrm J$。

方程来源：[Fitzpatrick，§8.1，式 (8.1)–(8.6) 的理想 MHD 与绝热闭合](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node104.html)。

## 广义欧姆定律与 Hall 项

从电子动量方程逐项整理欧姆定律。对准中性单电荷离子体系，设电子压力张量为 $\mathbf P_e$，电子所受碰撞动量交换力密度为 $\mathbf R_e$，则代数整理给出

$$
\mathbf E+\mathbf u_i\times\mathbf B
=\frac{\mathbf J\times\mathbf B}{en}
-\frac{\nabla\cdot\mathbf P_e}{en}
-\frac{m_e}{e}(\partial_t+\mathbf u_e\cdot\nabla)\mathbf u_e
+\frac{\mathbf R_e}{en}.
$$

出发式为 $m_en(\partial_t+\mathbf u_e\cdot\nabla)\mathbf u_e=-en(\mathbf E+\mathbf u_e\times\mathbf B)-\nabla\cdot\mathbf P_e+\mathbf R_e$。两边除以 $-en$，再用 $\mathbf u_e=\mathbf u_i-\mathbf J/(en)$，把 $\mathbf u_e\times\mathbf B$ 移到左边，就逐项得到上式的符号。简化碰撞模型给 $\mathbf R_e=-m_en\nu_{ei}(\mathbf u_e-\mathbf u_i)=m_e\nu_{ei}\mathbf J/e$，所以 $\eta=m_e\nu_{ei}/(ne^2)$，即 $\mathbf R_e/(en)=\eta\mathbf J$。

这是以离子速度写出的形式；若改成质心速度并把惯性改写成 $\partial_t\mathbf J$，还会产生对流与密度项，不应只抄一个时间导数。用简化各向同性摩擦 $\mathbf R_e=en\eta\mathbf J$，且 $\mathbf P_e=p_e\mathbf I$，右边分别为 Hall、电子压力、电子惯性和电阻项。真实磁化输运还可能有张量电阻、热力等贡献。

各项单位都是 $\mathrm{V\,m^{-1}}$。Hall 项满足 $\mathbf J\cdot(\mathbf J\times\mathbf B)=0$，因此本身不产生焦耳耗散，却会改变磁场随哪个流体运动。压力项能够在电子内能与场之间转移能量，该交换属于压力功。约化方程时按实际尺度比较各项量级；在电流薄层内，整体很小的非理想项仍可能成为主项。

来源：[Kimura 与 Morrison，On energy conservation in extended magnetohydrodynamics (2014)，§II–III](https://web2.ph.utexas.edu/~morrison/14_morrison_POP_kimura.pdf)；[MIT 22.611J，第 4 章 §4.6，双流体到单流体推导](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/resources/chap4/)。本文电子速度形式直接由电子动量守恒整理，避免混用不同截断模型。

### 从电场量级推导离子惯性长度

取磁场在尺度 $L$ 上转向或改变，安培定律给 $J\sim B/(\mu_0L)$。对横向电流和流动，Hall 电场与对流电场的量级比为

$$
\frac{E_H}{E_{\rm conv}}
\sim\frac{JB/(en)}{UB}
=\frac{B}{\mu_0enLU}.
$$

选择 $U=v_A=B/\sqrt{\mu_0nm_i}$，并在质量密度中取离子主导阶，便有

$$
\frac{E_H}{E_{\rm conv}}\sim\frac{d_i}{L},\qquad
d_i=\sqrt{\frac{m_i}{\mu_0ne^2}}=\frac{c}{\omega_{pi}}.
$$

因此 $d_i$ 直接来自电子与离子速度差对感应电场的贡献。若实际 $U$ 与 $v_A$ 不同，比例还要乘 $v_A/U$；若 $\mathbf J$ 平行于 $\mathbf B$，应使用横向电流分量。这样的比较把尺度和几何都放回欧姆定律。

**算例。** 取氘 $n=10^{19}\,\mathrm{m^{-3}}$、$B=0.5\,\mathrm T$、$L=0.1\,\mathrm m$，流速取 $v_A$。代入得 $d_i=0.101810\,\mathrm m$、$v_A=2.43926\times10^6\,\mathrm{m\,s^{-1}}$，所以 $d_i/L=1.01810$。独立代入电场公式得 $E_H\simeq1.24171\times10^6\,\mathrm{V\,m^{-1}}$、$E_{\rm conv}\simeq1.21963\times10^6\,\mathrm{V\,m^{-1}}$，比值相同。保持其他参数而把 $L$ 增至 $1\,\mathrm m$，比值降为 $0.101810$，展示了薄层对 Hall 项的放大。

来源：[Kimura–Morrison，§II.A，式 (2)–(3)](https://web2.ph.utexas.edu/~morrison/14_morrison_POP_kimura.pdf)；[Fitzpatrick，§4.14 单流体排序](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node59.html)。

## 磁压力、磁张力与等离子体 beta

由安培定律和矢量恒等式，磁力密度可以写成

$$
\mathbf J\times\mathbf B
=-\nabla\frac{B^2}{2\mu_0}
+\frac{(\mathbf B\cdot\nabla)\mathbf B}{\mu_0}.
$$

具体恒等式是 $[(\nabla\times\mathbf B)\times\mathbf B]_i=B_j\partial_jB_i-B_j\partial_iB_j$，后一项为 $-\partial_i(B^2/2)$；再除以 $\mu_0$ 即得上式。将 $\mathbf B=B\mathbf b$ 代入张力项，得到 $(\mathbf B\cdot\nabla)\mathbf B=B(\partial_\parallel B)\mathbf b+B^2\boldsymbol\kappa$；取垂直投影就消去第一项，给出下式。$\beta$ 则按热压力与磁压力之比定义为 $p/[B^2/(2\mu_0)]$。

第一项与磁场强度梯度有关，第二项包含弯曲磁场的张力。取 $\mathbf b=\mathbf B/B$、曲率 $\boldsymbol\kappa=(\mathbf b\cdot\nabla)\mathbf b$，垂直分量是

$$
(\mathbf J\times\mathbf B)_\perp
=-\nabla_\perp\frac{B^2}{2\mu_0}
+\frac{B^2}{\mu_0}\boldsymbol\kappa.
$$

注意曲率张力系数是 $B^2/\mu_0$；$B^2/(2\mu_0)$ 是磁压力和磁能密度。磁张力系数是磁能密度的两倍。恒等式也给出 $\mathbf B\cdot(\mathbf J\times\mathbf B)=0$，磁力本身没有沿磁场分量。

定义局域 $\beta=2\mu_0p/B^2$。假想均匀氘等离子体 $n_e=n_i=10^{20}\,\mathrm{m^{-3}}$，$T_e=T_i=10\,\mathrm{keV}$，$B=5\,\mathrm T$，用 $p=n_ek_BT_e+n_ik_BT_i$ 得 $p\simeq3.204\times10^5\,\mathrm{Pa}$，磁压力约 $9.947\times10^6\,\mathrm{Pa}$，故 $\beta\simeq0.0322$。这里 keV 表示 $k_BT$ 的能量值。平均 beta、极向 beta 与归一化 beta 各有自己的平均或归一化定义。

来源：[Fitzpatrick，Magnetic Pressure，§8.2，式 (8.7)–(8.12)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node105.html)；[Plasma Beta，§1.9](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node11.html)。

### 平板平衡的梯度、安培电流与力

考虑静态平板 $\mathbf B=B_z(x)\mathbf e_z$，磁力线笔直，所以曲率张力为零。安培定律先给 $J_y=-B_z'/\mu_0$，再作叉乘得到 $(\mathbf J\times\mathbf B)_x=-B_zB_z'/\mu_0$。力平衡积分成

$$
\frac{dp}{dx}=-\frac{d}{dx}\frac{B_z^2}{2\mu_0},
\qquad p+\frac{B_z^2}{2\mu_0}=\text{常数}.
$$

给定 $B_z=B_0\sqrt{1-x^2/a^2}$、$|x|<a$，逐步代入可得

$$
p=p_0+\frac{B_0^2x^2}{2\mu_0a^2},\qquad
J_y=\frac{B_0x}{\mu_0a^2\sqrt{1-x^2/a^2}},\qquad
J_yB_z=\frac{B_0^2x}{\mu_0a^2}.
$$

最后一个式子与 $dp/dx$ 一致。在 $x>0$ 一侧，向外增大的热压力由向外减小的磁压力配平；压力力 $-\nabla p$ 指向负 $x$，磁力指向正 $x$。

**算例。** 设 $B_0=1\,\mathrm T$、$a=0.5\,\mathrm m$、$p_0=10^4\,\mathrm{Pa}$，计算 $x=0.15\,\mathrm m$。磁场为 $\sqrt{0.91}=0.953939\,\mathrm T$，压力增量是 $0.09/(2\mu_0)=35809.9\,\mathrm{Pa}$，故 $p=45809.9\,\mathrm{Pa}$。压力梯度为 $0.15/(\mu_0\times0.25)=4.77465\times10^5\,\mathrm{Pa\,m^{-1}}$。用安培电流再乘局部磁场得到同一数值，单位 $\mathrm{A\,m^{-2}T}=\mathrm{N\,m^{-3}}=\mathrm{Pa\,m^{-1}}$。

来源：[Fitzpatrick，§8.2，式 (8.7)–(8.12) 的磁压力与张力分解](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node105.html)。

## 磁通冻结的精确含义

令闭合曲线 $C(t)$ 随局部流体速度 $\mathbf u$ 移动，$S(t)$ 为以它为边界的曲面。法拉第定律与运动曲面的输运公式给出

$$
\frac{d}{dt}\int_{S(t)}\mathbf B\cdot d\mathbf S
=-\oint_{C(t)}(\mathbf E+\mathbf u\times\mathbf B)\cdot d\boldsymbol\ell.
$$

理想欧姆定律使右边为零，故穿过物质回路的磁通守恒；局部磁场可随压缩与拉伸改变。在光滑流动与磁场条件下，这意味着磁力线连接关系随流体保持。粒子仍可沿磁场流动；这里的守恒量属于流体物质回路。

利用 $\nabla\cdot\mathbf B=0$，将感应方程展开并与连续性方程组合，可进一步得到

$$
D_t\left(\frac{\mathbf B}{\rho}\right)
=\left(\frac{\mathbf B}{\rho}\cdot\nabla\right)\mathbf u.
$$

中间代数为 $D_t\mathbf B=(\mathbf B\cdot\nabla)\mathbf u-\mathbf B\nabla\cdot\mathbf u$，而质量方程给 $D_t\rho=-\rho\nabla\cdot\mathbf u$。对商 $\mathbf B/\rho$ 求导时，两项中的压缩贡献恰好抵消。运动曲面公式中的边界项则来自回路扫过的窄带面积；将固定曲面的 $\partial_t\mathbf B=-\nabla\times\mathbf E$ 与该扫掠磁通合并，并用 Stokes 定理，得到上方含 $\mathbf E+\mathbf u\times\mathbf B$ 的环流。

因此磁场可随拉伸和压缩改变。比如均匀各向同性压缩，长度缩放为 $a$，质量守恒给 $\rho\propto a^{-3}$，磁通守恒给 $B\propto a^{-2}\propto\rho^{2/3}$。感应方程中的非理想项给出偏离冻结的磁通变化率。

来源：[Fitzpatrick，Flux Freezing，§8.3，式 (8.13)–(8.21)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node106.html)。

### 各向异性形变的 Cauchy 磁场公式

用初始坐标 $\mathbf a$ 标记流体元，令形变矩阵 $F_{ij}=\partial x_i/\partial a_j$、体积比 $\mathcal J=\det F$。质量守恒给 $\rho=\rho_0/\mathcal J$。对沿坐标轴的均匀拉伸 $F=\operatorname{diag}(a,b,c)$，垂直于 $x$ 的物质面面积放大 $bc$ 倍，所以磁通守恒要求 $B_x=B_{0x}/(bc)$；另两面同理。三式组合为

$$
\mathbf B=\frac{F\mathbf B_0}{\mathcal J},\qquad
\frac{\mathbf B}{\rho}=F\frac{\mathbf B_0}{\rho_0}.
$$

一般光滑形变下，$D_tF=(\nabla\mathbf u)F$，对上式微分便重得 $D_t(\mathbf B/\rho)=(\mathbf B/\rho\cdot\nabla)\mathbf u$。这把积分形式的磁通守恒和局部微分形式接在一起。

**算例。** 已知初始均匀场 $\mathbf B_0=(1,0,1)\,\mathrm T$，三个方向的长度分别乘 $a=1/2,b=1,c=2$。于是 $\mathcal J=1$，密度保持原值，而 $\mathbf B=(0.5,0,2)\,\mathrm T$。垂直 $x$ 的面积乘 $2$，其磁通因子是 $0.5\times2=1$；垂直 $z$ 的面积乘 $0.5$，磁通因子为 $2\times0.5=1$。磁能密度比为 $(0.5^2+2^2)/(1^2+1^2)=2.125$。体积不变的剪伸也能增加磁能，能量来自驱动这种形变的机械功。

来源：[Fitzpatrick，§8.3，式 (8.13)–(8.21) 的随流曲面与磁通守恒](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node106.html)。

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

$R_m$ 使用实际特征流速，$S$ 使用 Alfvén 速度；只有 $U=v_A$ 才相等。$R_m\gg1$ 表示在给定尺度平流占优，更薄尺度上的扩散与重联需以局部尺度重新比较。

这些时间来自感应方程各项的量级：$\partial_tB\sim B/\tau$、平流项 $\sim UB/L$、扩散项 $\sim D_mB/L^2$，故 $\tau_U=L/U$、$\tau_R=L^2/D_m$，两项之比为 $R_m=UL/D_m$。Alfvén 速度可由横向位移的张力方程 $\rho\partial_t^2\boldsymbol\xi_\perp=(B^2/\mu_0)\partial_\parallel^2\boldsymbol\xi_\perp$ 识别，波速平方为 $B^2/(\mu_0\rho)$；用该速度定义 $\tau_A$ 就得到 $S=\tau_R/\tau_A$。

一个可检验解是无流、周期区域内 $B_y(x,t)=B_1\sin(kx)e^{-D_mk^2t}$，其他分量为零。其振幅衰减时间是 $1/(D_mk^2)$；若 $L$ 取波长，则是 $L^2/(4\pi^2D_m)$，其中 $4\pi^2$ 来自明确的空间本征函数。磁能按振幅平方衰减，衰减率多一个因子 2。

来源：[Fitzpatrick，MHD Dynamo Theory，§8.9，式 (8.100)–(8.102)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node112.html)；[Magnetic Reconnection: Introduction，§9.1](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node123.html)。

### 周期扩散解的磁能和焦耳热积分

在上述无流周期扩散问题中，对一个波长取空间平均，$\langle\sin^2kx\rangle=\langle\cos^2kx\rangle=1/2$。由 $J_z=\partial_xB_y/\mu_0$ 得

$$
\langle w_B\rangle=\frac{B_1^2}{4\mu_0}e^{-2D_mk^2t},
\qquad
\langle Q_\eta\rangle=\frac{\eta B_1^2k^2}{2\mu_0^2}e^{-2D_mk^2t}.
$$

将第一式对时间求导，利用 $D_m=\eta/\mu_0$，立即得到 $-\partial_t\langle w_B\rangle=\langle Q_\eta\rangle$。进一步时间积分给 $\int_0^t\langle Q_\eta\rangle dt'=\langle w_B(0)\rangle-\langle w_B(t)\rangle$。这是磁扩散子问题的能量预算；把它用于流体演化时，焦耳热进入内能方程，无流约束也要由所取几何或外部约束维持。

**算例。** 设 $B_1=0.1\,\mathrm T$、波长 $0.2\,\mathrm m$、$\eta=10^{-6}\,\Omega\,\mathrm m$。先算 $k=2\pi/0.2=31.4159\,\mathrm{m^{-1}}$、$D_m=0.795775\,\mathrm{m^2\,s^{-1}}$，故振幅时间 $\tau=1/(D_mk^2)=1.27324\,\mathrm{ms}$。初始平均磁能为 $1989.44\,\mathrm{J\,m^{-3}}$，初始平均热功率为 $3.12500\times10^6\,\mathrm{W\,m^{-3}}$。在 $t=\tau$，磁能剩 $1989.44e^{-2}=269.241\,\mathrm{J\,m^{-3}}$，累计转换的热量是 $1720.20\,\mathrm{J\,m^{-3}}$。

来源：[Fitzpatrick，§8.9，式 (8.100)–(8.102)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node112.html)；[Kimura–Morrison，§III 能量核算](https://web2.ph.utexas.edu/~morrison/14_morrison_POP_kimura.pdf)。

## 静态平衡与 Grad–Shafranov 方程

无流、各向同性、忽略重力时，平衡要求 $\nabla p=\mathbf J\times\mathbf B$。点乘 $\mathbf B$ 得 $\mathbf B\cdot\nabla p=0$：压力沿磁力线恒定。有良好嵌套磁面时，压力可写成磁面函数。

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

推导时先用轴对称与 $\nabla\cdot\mathbf B=0$ 把极向场写成 $\mathbf B_p=\nabla\psi\times\mathbf e_\phi/R$；一般先令 $F=RB_\phi$ 为 $(R,Z)$ 的函数。力平衡的环向分量给 $\mathbf B_p\cdot\nabla F=0$，所以在嵌套磁面上 $F=F(\psi)$；沿场压力平衡同样给 $p=p(\psi)$。随后旋度的极向分量给 $\mathbf J_p=F'\mathbf B_p/\mu_0$，环向分量给上方 $J_\phi$。两个叉乘合并为

$$
\mathbf J\times\mathbf B
=J_\phi\mathbf e_\phi\times\mathbf B_p
+\mathbf J_p\times\frac F R\mathbf e_\phi
=-\frac{\Delta^*\psi+FF'}{\mu_0R^2}\nabla\psi.
$$

令它等于 $\nabla p=p'\nabla\psi$，即得所列 Grad–Shafranov 方程；磁轴等 $\nabla\psi=0$ 处按光滑解连续延拓。这一步同时固定了磁通约定与电流符号。

需要给定压力和电流相关剖面以及边界条件才构成可求解问题。固定边界计算给定等离子体边界；自由边界计算还必须包含外部线圈、真空场和边界确定。改变磁通符号或是否除 $2\pi$，所有导数和电流符号必须一致改变。

方程只检验该模型下的力平衡。稳定性由扰动方程确定，输运损失由输运模型确定。三维仿星器、有流或压力各向异性的系统需要相应推广。

来源：[Fitzpatrick，Grad-Shafranov Equation，§14.3，式 (14.30)–(14.33)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node169.html)；[Xu 与 Fitzpatrick (2019)，§2，式 (1)–(3)，归一化约定](https://farside.ph.utexas.edu/Papers/Xu_2019_Nucl._Fusion_59_064002.pdf)。

### 用多项式构造可逐项验算的平衡

选取轴对称局部解 $\psi=AR^4+CZ^2$。对径向部分先求 $(1/R)\partial_R\psi=4AR^2$，再乘 $R\partial_R$ 得 $8AR^2$；竖直二阶导数给 $2C$。因此

$$
\Delta^*\psi=8AR^2+2C.
$$

让 $p'=-8A/\mu_0$、$FF'=-2C$，右端便逐项匹配，积分得到

$$
p=p_0-\frac{8A}{\mu_0}\psi,\qquad
F^2=F_0^2-4C\psi.
$$

在 $R>0$、$p>0$、$F^2>0$ 的区域选择正根，并用磁场定义重建 $B_R=-2CZ/R$、$B_Z=4AR^2$、$B_\phi=F/R$。这一显式解适合检验求解器的导数、符号与残差；闭合磁面和装置边界由另外的几何条件决定。

**算例。** 取 $A=0.01\,\mathrm{Wb\,m^{-4}}$、$C=0.02\,\mathrm{Wb\,m^{-2}}$、$F_0=0.5\,\mathrm{T\,m}$、$p_0=10^4\,\mathrm{Pa}$，在 $(R,Z)=(1,0.3)\,\mathrm m$。得到 $\psi=0.0118\,\mathrm{Wb}$、$\Delta^*\psi=0.12\,\mathrm{Wb\,m^{-2}}$、$p'=-63661.98\,\mathrm{Pa\,Wb^{-1}}$，故 $J_\phi=-0.12/(\mu_0R)=-95492.97\,\mathrm{A\,m^{-2}}$。磁场为 $(-0.012,\,0.499055,\,0.040)\,\mathrm T$，按 $(R,\phi,Z)$ 排列。把这些导数送回方程左右两边，均得到 $0.12\,\mathrm{Wb\,m^{-2}}$。

来源：[Fitzpatrick，§14.3，式 (14.30)–(14.33)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node169.html)；这里采用本页明确写出的 SI 磁通约定计算。

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

对计算域积分后，能量变化等于通过边界的净能流。这里已忽略非相对论 MHD 排序下较小的电场能；完整 Maxwell 定理还含电场能。

在电阻 MHD 中 $\mathbf E=-\mathbf u\times\mathbf B+\eta\mathbf J$，因此

$$
\mathbf J\cdot\mathbf E=\mathbf u\cdot(\mathbf J\times\mathbf B)+\eta J^2.
$$

右边第一项是场与宏观流动的机械能交换，第二项是非负的焦耳加热（$\eta\ge0$）。相应内能方程为

$$
\partial_t\frac p{\gamma-1}+\nabla\cdot\left(\frac p{\gamma-1}\mathbf u\right)
=-p\nabla\cdot\mathbf u+\eta J^2
$$

（本式未加热流、黏性或其他源）。电阻将磁能转成内能，封闭绝热系统的总能量保持守恒。若模拟只在感应方程加扩散却不给内能补上焦耳热，会破坏这项预算。检查加热模型时还要避免把同一 $\mathbf J\cdot\mathbf E$ 同时算作机械功与全部热源而重复记账。

来源：[Kimura 与 Morrison (2014)，§III，能量守恒与模型截断](https://web2.ph.utexas.edu/~morrison/14_morrison_POP_kimura.pdf)；[MIT 22.615，MHD Theory of Fusion Systems](https://ocw.mit.edu/courses/22-615-mhd-theory-of-fusion-systems-spring-2007/)。上式为本页所列基础方程的直接组合；含电子惯性的扩展模型必须连同其额外能量一起处理。

### 把场功逐项分给动能和内能

用 $\mathbf u$ 点乘动量方程，并借连续性整理成守恒形式，动能密度 $K=\rho u^2/2$ 满足

$$
\partial_tK+\nabla\cdot[(K+p)\mathbf u]
=p\nabla\cdot\mathbf u+\mathbf u\cdot(\mathbf J\times\mathbf B).
$$

热内能方程中的 $-p\nabla\cdot\mathbf u$ 与上式压力功抵消；低频 Poynting 方程为 $\partial_tw_B+\nabla\cdot(\mathbf E\times\mathbf B/\mu_0)=-\mathbf J\cdot\mathbf E$。最后使用三重积恒等式与欧姆定律，场功分解成机械功和 $\eta J^2$，它们又与流体方程的交换项抵消。由此总能量通量可以先写成 $(K+w_{\rm th}+p)\mathbf u+\mathbf E\times\mathbf B/\mu_0$，再按所用欧姆定律展开。

**算例。** 指定 $\mathbf u=(1000,0,0)\,\mathrm{m\,s^{-1}}$、$\mathbf B=(0,0,1)\,\mathrm T$、$\mathbf J=(0,10^4,0)\,\mathrm{A\,m^{-2}}$、$\eta=10^{-7}\,\Omega\,\mathrm m$。先算 $-\mathbf u\times\mathbf B=(0,1000,0)\,\mathrm{V\,m^{-1}}$，加上 $\eta\mathbf J$ 后 $E_y=1000.001\,\mathrm{V\,m^{-1}}$。于是 $\mathbf J\cdot\mathbf E=10000010\,\mathrm{W\,m^{-3}}$，其中 $\mathbf u\cdot(\mathbf J\times\mathbf B)=10^7\,\mathrm{W\,m^{-3}}$ 进入宏观动能，$\eta J^2=10\,\mathrm{W\,m^{-3}}$ 进入热内能。这个局部向量算例展示了场功即使很大，直接电阻热仍可很小。

来源：[Kimura–Morrison，§III.A，式 (13) 起的能量积分与 Hall MHD 核算](https://web2.ph.utexas.edu/~morrison/14_morrison_POP_kimura.pdf)；本段按上述电阻 MHD 方程逐项组合。

## 平衡、线性稳定性与能量原理

平衡满足静态方程，稳定性回答受到扰动后是否增长。对静态理想 MHD 平衡，使用位移 $\boldsymbol\xi$，一阶扰动满足

$$
\delta\mathbf B=\nabla\times(\boldsymbol\xi\times\mathbf B_0),\qquad
\delta p=-\boldsymbol\xi\cdot\nabla p_0-\gamma p_0\nabla\cdot\boldsymbol\xi.
$$

这两式来自把流速扰动写成 $\delta\mathbf u=\partial_t\boldsymbol\xi$：线性感应方程对时间积分给 $\delta\mathbf B$；质量守恒给随流体元变化的 $\Delta\rho=-\rho_0\nabla\cdot\boldsymbol\xi$，绝热关系给 $\Delta p=\gamma p_0\Delta\rho/\rho_0$。再用 Euler 扰动与随体扰动的关系 $\delta p=\Delta p-\boldsymbol\xi\cdot\nabla p_0$，就得到压力式。初始扰动需与这些冻结、绝热约束相容。

将它们代入线性动量方程写为 $\rho_0\partial_t^2\boldsymbol\xi=\mathcal F[\boldsymbol\xi]$。对使力算符自伴的边界条件，定义势能二阶变分

$$
\delta W=-\frac12\int\boldsymbol\xi^*\cdot\mathcal F[\boldsymbol\xi]\,dV.
$$

线性力算符明确为 $\mathcal F[\boldsymbol\xi]=-\nabla\delta p+(\nabla\times\delta\mathbf B)\times\mathbf B_0/\mu_0+\mathbf J_0\times\delta\mathbf B$，来自逐项线性化压力力和 $\mathbf J\times\mathbf B$。在所列边界下积分分部使它自伴；用 $\partial_t\boldsymbol\xi$ 点乘运动方程并积分，得到扰动动能 $\tfrac12\int\rho_0|\partial_t\boldsymbol\xi|^2dV$ 与 $\delta W$ 之和守恒。对正规模代入 $\partial_t^2\boldsymbol\xi=-\omega^2\boldsymbol\xi$，再乘 $\boldsymbol\xi^*$ 积分，就给出下述变分商；其正负号来自这个守恒振子结构。

例如等离子体边界紧贴固定理想导体壁、平衡磁场沿壁面时，要求壁上 $\boldsymbol\xi\cdot\mathbf n=0$，并在域内满足相应正则性条件；这里 $\mathbf n$ 为壁面单位法向。对正规模 $e^{-i\omega t}$，有 $\omega^2\int\rho_0|\boldsymbol\xi|^2dV=2\delta W$。存在允许的负 $\delta W$ 位移意味着理想失稳方向；若对所有非平凡允许扰动严格为正，则在该理想静态框架内具有能量稳定性。零值对应需要进一步分析的中性方向。

自由边界问题的变分泛函还包含真空、表面和壁等相应能量。平衡流可改变算符性质。电阻撕裂、动理学或快粒子驱动失稳也可能在理想 MHD 稳定的状态出现。因此一次平衡求解或一个 beta 数值不构成完整稳定性评估。

来源：[MIT 22.615，Lecture 14，第 4–6 页，自伴性与固定边界](https://ocw.mit.edu/courses/22-615-mhd-theory-of-fusion-systems-spring-2007/cda9ba8f1dd4c9f2f9abecc8d010adae_lecture14.pdf)；[Lecture 16，第 1–5 页，能量原理、表面与真空能量](https://ocw.mit.edu/courses/22-615-mhd-theory-of-fusion-systems-spring-2007/8cdfc4d94a61aa60d91bc02046597130_lecture16.pdf)；[MIT 22.611J，第 4 章 §4.13–4.15](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/resources/chap4/)。

### 用固定端弯曲位移算出 Alfvén 本征频率

取均匀 $\mathbf B_0=B_0\mathbf e_z$、均匀密度，在 $z=0,L$ 固定两端，横向采用周期边界。选不可压缩位移 $\boldsymbol\xi=\xi_0\sin(\pi z/L)\mathbf e_x$，它满足两端位移为零且 $\nabla\cdot\boldsymbol\xi=0$。由感应扰动得 $\delta B_x=B_0\partial_z\xi_x$；均匀平衡下能量只剩磁力线弯曲项。若横截面积为 $A_\perp$，

$$
\delta W=\frac{B_0^2A_\perp}{2\mu_0}
\int_0^L(\partial_z\xi_x)^2dz
=\frac{B_0^2A_\perp\pi^2\xi_0^2}{4\mu_0L},
$$

$$
I=\int\rho\xi^2dV=\frac{\rho A_\perp L\xi_0^2}{2},
\qquad \omega^2=\frac{2\delta W}{I}
=v_A^2\frac{\pi^2}{L^2}.
$$

振幅与横截面积在商中消去；这正是平行波数 $k_\parallel=\pi/L$ 的剪切 Alfvén 模。

**算例。** 给定氘密度 $n=10^{19}\,\mathrm{m^{-3}}$，取离子主导质量密度，$B_0=0.2\,\mathrm T$、$L=10\,\mathrm m$、$A_\perp=0.01\,\mathrm{m^2}$、$\xi_0=10^{-3}\,\mathrm m$。积分得 $\delta W=7.85398\times10^{-5}\,\mathrm J$、$I=1.67179\times10^{-15}\,\mathrm{kg\,m^2}$，故 $\omega=\sqrt{2\delta W/I}=3.06527\times10^5\,\mathrm{s^{-1}}$。独立用 $v_A=9.75706\times10^5\,\mathrm{m\,s^{-1}}$ 乘 $\pi/L$ 得相同结果；这个允许扰动具有正的回复能。

来源：[MIT 22.615 Lecture 16，第 1–3 页的变分商与第 6 页的磁力线弯曲项](https://ocw.mit.edu/courses/22-615-mhd-theory-of-fusion-systems-spring-2007/8cdfc4d94a61aa60d91bc02046597130_lecture16.pdf)。

## 磁重联与 Sweet–Parker 标度

磁重联涉及磁场连接关系变化及能量转换；在光滑理想单流体模型中被磁通冻结约束，故重联区域必须考虑适当的非理想物理。电阻、电子压力张量、电子惯性等项是否重要，应由局部尺度判定。

经典 Sweet–Parker 模型假设二维、稳态、近不可压缩、反平行上游磁场与细长层流电流片。设半长 $L$、半厚 $\delta$，两侧密度相近；只求量级，不追求取决于几何定义的常数。质量守恒与磁张力加速给

$$
v_{\rm in}L\sim v_{\rm out}\delta,\qquad v_{\rm out}\sim v_A.
$$

第一式是单位出平面长度的流入质量率 $\rho v_{\rm in}L$ 与流出质量率 $\rho v_{\rm out}\delta$ 相等；第二式来自出流方向动量量级 $\rho v_{\rm out}^2/L\sim B^2/(\mu_0L)$，即磁张力提供出流动能。稳态二维 Faraday 定律还给 $\partial_xE_z=\partial_yE_z=0$，因此可把同一个 $E_z$ 从理想上游匹配到电阻层；片内安培估计 $J_z\sim B/(\mu_0\delta)$ 才给下一步的电阻场。

上游理想电场 $E\sim v_{\rm in}B$ 与片内电阻电场 $E\sim\eta B/(\mu_0\delta)$ 匹配，推出

$$
\frac\delta L\sim S^{-1/2},\qquad
\frac{v_{\rm in}}{v_A}\sim S^{-1/2},\qquad
\tau_{\rm SP}\sim\tau_A S^{1/2}\sim\sqrt{\tau_A\tau_R}.
$$

大 $S$ 下电流片很薄，整体重联速度相对 $v_A$ 很慢。例如纯标度算例 $S=10^8$ 给 $\delta/L\sim10^{-4}$。但继续减薄可能使离子/电子尺度、Hall 效应或电流片不稳定性变得重要，此时层流电阻模型不再适用。具体装置中的重联演化由局部非理想项、背景几何和电流片稳定性共同确定。

来源：[Fitzpatrick，Sweet-Parker Reconnection，§9.9，式 (9.138)–(9.153)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node131.html)。

### 由质量流率和电场匹配联立求解

把几何量级系数取为一，令 $D_m=\eta/\mu_0$，质量守恒给 $v_{\rm in}=v_A\delta/L$，电场匹配给 $v_{\rm in}=D_m/\delta$。消去流入速度后先求厚度，再回代：

$$
\delta^2=\frac{D_mL}{v_A},\qquad
v_{\rm in}=\sqrt{\frac{D_mv_A}{L}},\qquad
E_z=B\sqrt{\frac{D_mv_A}{L}}.
$$

厚度平方的单位为 $(\mathrm{m^2\,s^{-1}})\mathrm m/(\mathrm{m\,s^{-1}})=\mathrm{m^2}$。同一 $E_z$ 贯穿稳态二维层，这是上下游连接的关键。电阻率降低时，流入速度按 $\sqrt{\eta}$ 降低，片厚也按 $\sqrt{\eta}$ 缩小。

**算例。** 采用给定电阻率的层流教学模型：单电离氘 $n=10^{22}\,\mathrm{m^{-3}}$、$B=0.1\,\mathrm T$、半长 $L=1\,\mathrm m$、$\eta=10^{-4}\,\Omega\,\mathrm m$。由此 $v_A=15427.3\,\mathrm{m\,s^{-1}}$、$D_m=79.5775\,\mathrm{m^2\,s^{-1}}$、$S=193.865$，求得 $\delta=0.0718209\,\mathrm m$ 和 $v_{\rm in}=1108.00\,\mathrm{m\,s^{-1}}$。两种电场分别为 $v_{\rm in}B=110.800\,\mathrm{V\,m^{-1}}$ 与 $\eta B/(\mu_0\delta)=110.800\,\mathrm{V\,m^{-1}}$，质量流率也满足 $v_{\rm in}L=v_A\delta$。离子惯性长度 $d_i=0.00321952\,\mathrm m$，故 $\delta/d_i=22.308$。这里以一致的方程组展示标度计算；给定的 $\eta$ 是模型输入，碰撞输运闭合和层流稳定性可随后独立评估。

来源：[Fitzpatrick，§9.9，式 (9.138)–(9.147) 的电场、流量与动量匹配](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node131.html)。

[返回基础原理](../README.md)
