# 单粒子运动

单粒子轨道是理解磁约束、漂移、磁镜和波粒共振的起点。本专题先把电磁场视为给定场，研究测试粒子；真实等离子体还必须由所有组分的电荷和电流自洽求场。除特别说明外，采用 SI、非相对论、无碰撞近似；$q$ 始终是带符号电荷，$e>0$ 是元电荷大小，$B=|\mathbf B|$，$\mathbf b=\mathbf B/B$。各漂移公式是满足尺度排序时的导引中心近似，不是任意电磁场中的精确轨道。

## Lorentz 方程与磁场不做功

对质量 $m$、电荷 $q$ 的非相对论粒子，位置 $\mathbf x$ 和速度 $\mathbf v$ 满足

$$
\frac{d\mathbf x}{dt}=\mathbf v,
\qquad
m\frac{d\mathbf v}{dt}=q\left(\mathbf E+\mathbf v\times\mathbf B\right).
$$

$m$ 用 kg，$q$ 用 C，$\mathbf E$ 用 $\mathrm{V\,m^{-1}}$，$\mathbf B$ 用 T，力的单位为 N。这里没有 Gaussian-cgs 中的 $1/c$。两边点乘 $\mathbf v$，并用 $\mathbf v\cdot(\mathbf v\times\mathbf B)=0$，得到精确的非相对论功率关系

$$
\frac{dK}{dt}=q\mathbf E\cdot\mathbf v,
\qquad K=\frac12mv^2.
$$

因此磁力改变速度方向而不直接改变动能。这不仅对均匀或静态磁场成立；磁力项在任意时刻都与速度正交。不过时变磁场伴随 $\nabla\times\mathbf E=-\partial_t\mathbf B$，感应电场可以做功，故“磁力不做功”不能被误写成“磁压缩绝不加热”。[UT Austin：Motion in Uniform Fields，式 (2.1)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node16.html)；[Invariance of Magnetic Moment，式 (2.60)–(2.65)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node20.html)。

若场与时间无关且 $\mathbf E=-\nabla\phi$，则

$$
\frac{d}{dt}(K+q\phi)=0,
\qquad
K_2-K_1=-q(\phi_2-\phi_1).
$$

这里 $\phi$ 的单位是 V，$q\phi$ 的单位为 J。电子从低电势走向高电势时，$q=-e$ 使其势能下降、动能增加；单价正离子恰好相反。例如电子跨过 $+100\,\mathrm V$ 的电势增量，获得 $100\,\mathrm{eV}$ 动能。这个符号检查比凭“沿电场方向加速”口头记忆更可靠，因为电子受力与电场相反。[UT Austin：Magnetic Mirrors，式 (2.83)–(2.85)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node23.html)。

**适用范围与误区。** 本式未包含碰撞、辐射反作用或外加非电磁力，单个粒子的动能变化也不能直接等同于整个等离子体温度变化。对相对论粒子应使用 $d(\gamma m\mathbf v)/dt=q(\mathbf E+\mathbf v\times\mathbf B)$；功率仍为 $q\mathbf E\cdot\mathbf v$，但动能不再等于 $mv^2/2$。轨道数值计算若在 $\mathbf E=0$ 的静态场中出现持续动能漂移，首先应检查积分误差，而不能把它解释为磁场加热。

## 回旋运动、带符号频率与 Larmor 半径

取均匀静态 $\mathbf B=B\hat{\mathbf z}$、$\mathbf E=0$，Lorentz 方程的分量为

$$
\dot v_x=\Omega v_y,
\qquad
\dot v_y=-\Omega v_x,
\qquad
\dot v_\parallel=0,
\qquad
\Omega=\frac{qB}{m}.
$$

带符号的 $\Omega$ 编码旋转方向，而 $\omega_c=|\Omega|$ 是正的回旋角频率。若初速度取 $v_x(0)=v_\perp$、$v_y(0)=0$，则 $v_x=v_\perp\cos\Omega t$、$v_y=-v_\perp\sin\Omega t$。因此在 $x$ 向右、$y$ 向上的图中，正粒子从 $+x$ 速度转向 $-y$，电子相反；给出坐标比不注明观察方向的“顺时针”说法更清楚。[MIT OCW：Motion of Charged Particles，§2.1，式 (2.8)–(2.11)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

轨道半径、周期和每周期的平行位移为

$$
\rho=\frac{v_\perp}{|\Omega|}
=\frac{mv_\perp}{|q|B},
\qquad
\tau_c=\frac{2\pi}{|\Omega|},
\qquad
\Delta z=v_\parallel\tau_c.
$$

$\rho$、$\Delta z$ 用 m，$\tau_c$ 用 s。半径必须非负，因此不能写成 $v_\perp/\Omega_e$ 后把电子半径当作负数。平行分量只使圆轨道变成螺旋线，不直接改变回旋频率；这里的频率独立于速度是非相对论结果。[UT Austin：Motion in Uniform Fields，式 (2.3)、(2.5)–(2.7)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node16.html)。

用给定的垂直动能 $K_\perp=mv_\perp^2/2$ 可改写为 $\rho=\sqrt{2mK_\perp}/(|q|B)$。例如 $B=5\,\mathrm T$、$K_\perp=1\,\mathrm{keV}$ 时，电子半径约 $21.3\,\mu\mathrm m$，氘离子半径约 $1.29\,\mathrm{mm}$。这比较的是单粒子的垂直动能；如果改为 Maxwellian 温度算例，必须说明选择哪一种热速度。相同质量和磁场下，把垂直动能增大四倍会使半径增大两倍，而不是四倍。

**适用范围与误区。** 这里的“固定导引中心”只在无电场且磁场均匀时成立；梯度、曲率、其他力以及电场会让导引中心移动。带电粒子也并非焊接在某一条数学磁力线上。对磁零点 $B=0$，回旋表达式本身失去定义；对相对论能量，回旋频率变为 $|q|B/(\gamma m)$，不能继续按常数 $|q|B/m$ 计算共振。

## 均匀电磁场中的 E×B 漂移与力漂移

在均匀、静态且 $B\ne0$ 的场中，分解 $\mathbf E=\mathbf E_\perp+E_\parallel\mathbf b$。沿场运动满足 $m\dot v_\parallel=qE_\parallel$；垂直运动可写成回旋运动叠加匀速漂移

$$
\mathbf v_E=\frac{\mathbf E\times\mathbf B}{B^2}.
$$

它的单位为 $\mathrm{m\,s^{-1}}$。代入可直接验证 $\mathbf E_\perp+\mathbf v_E\times\mathbf B=0$：令 $\mathbf w_\perp=\mathbf v_\perp-\mathbf v_E$ 后，$\mathbf w_\perp$ 满足无电场的回旋方程。电子与离子的 $\mathbf v_E$ 相同，因为电荷在电力和磁力两边抵消；这并不意味着两种粒子的瞬时回旋速度相同。[UT Austin：Motion in Uniform Fields，式 (2.2)–(2.4)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node16.html)。

若 $\mathbf E=E_x\hat{\mathbf x}$、$\mathbf B=B\hat{\mathbf z}$，则 $\mathbf v_E=-(E_x/B)\hat{\mathbf y}$。取 $E_x=10^3\,\mathrm{V\,m^{-1}}$、$B=5\,\mathrm T$，漂移为 $-200\hat{\mathbf y}\,\mathrm{m\,s^{-1}}$，这一方向对正离子和电子一致。均匀静态垂直电场对周期回旋的平均净功为零，因为 $\mathbf E\cdot\mathbf v_E=0$、回旋速度周期平均为零；但瞬时 $q\mathbf E\cdot\mathbf v$ 可以不为零，初始动能也不必恒定。

一个缓慢、近似恒定的额外垂直力 $\mathbf F_\perp$ 产生最低阶力漂移

$$
\mathbf v_F=\frac{\mathbf F\times\mathbf B}{qB^2}.
$$

把 $\mathbf F=q\mathbf E$ 代入便返回 $\mathbf v_E$；若 $\mathbf F$ 与电荷无关，例如重力 $m\mathbf g$，漂移就会随电荷符号改变方向。这个公式可由平均力平衡 $\mathbf F_\perp+q\mathbf v_F\times\mathbf B=0$ 导出，但不能无条件套用于快速共振驱动。[MIT OCW：Motion of Charged Particles，§2.2–§2.2.1，式 (2.14)–(2.23)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

**适用范围与误区。** 取非均匀场的局域 $\mathbf E\times\mathbf B/B^2$ 时，需要场在回旋尺度上平滑；快速变化的电场会产生极化等修正。相同的 $\mathbf v_E$ 对精确准中性的混合物给出 $\mathbf j_E=\rho_q\mathbf v_E\simeq0$，但它仍运输粒子、压力与能量，所以“无净漂移电流”不等于“无输运”。如果 $E_\perp/B$ 接近光速，非相对论分解不能用于定量计算。

## 磁场强度梯度引起的 grad-B 漂移

在磁场随空间缓慢变化时，回旋轨道的强场一侧弯曲更紧，弱场一侧弯曲更松，轨道一周后一般不再闭合。对满足导引中心排序的粒子，定义正的磁矩标量 $\mu=mv_\perp^2/(2B)$，得到最低阶梯度漂移

$$
\mathbf v_{\nabla B}
=\frac{\mu}{qB}\,\mathbf b\times\nabla B
=\frac{mv_\perp^2}{2qB^3}\,\mathbf B\times\nabla B
=\frac{K_\perp}{qB^2}\,\mathbf b\times\nabla B.
$$

$\nabla B$ 的单位是 $\mathrm{T\,m^{-1}}$，$\mu$ 的单位是 $\mathrm{J\,T^{-1}}$，结果是速度。三个表达式等价，尤其要保留最后两式中不同的 $B$ 次数。电子与正离子的方向相反；这与同向的 E×B 漂移形成可检验的区别。[UT Austin：Magnetic Drifts，式 (2.52)、(2.53)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node19.html)；[MIT OCW：Motion of Charged Particles，§2.3，式 (2.36)、(2.37)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

也可把回旋平均后的有效磁镜力写作 $\mathbf F_{\mu}=-\mu\nabla B$。它的垂直部分代入力漂移 $\mathbf F\times\mathbf B/(qB^2)$，恰好给出上式。这里的有效力是回旋平均描述中的量，并不是给原始 Lorentz 方程额外添加一项后再同时计算完整回旋；否则会重复计数。平行部分 $-\mu\nabla_\parallel B$ 则影响沿场运动。

令 $\mathbf B=B(x)\hat{\mathbf z}$、$dB/dx>0$，则 $\mathbf b\times\nabla B$ 指向 $+y$，正离子向 $+y$ 漂移，电子向 $-y$ 漂移。定义 $L_B=B/|\nabla_\perp B|$，漂移大小为

$$
|\mathbf v_{\nabla B}|=\frac{K_\perp}{|q|B L_B}.
$$

对单价粒子 $K_\perp=1\,\mathrm{keV}$、$B=5\,\mathrm T$、$L_B=0.5\,\mathrm m$，大小为 $400\,\mathrm{m\,s^{-1}}$。相同电荷量和相同垂直动能时，该估算不显含质量；若改为固定速度比较，就会有质量依赖。这两种比较不能混在一起。

**适用范围与误区。** 该式要求 $\rho/L_B\ll1$、背景变化慢于回旋，且这里使用的 $v_\perp$ 是相对于导引中心的回旋速度；显著 E×B 流应先分离。$\nabla B$ 指磁场大小的梯度，不是整个矢量场的导数；只有其垂直于磁场的部分进入漂移。把局部的导引中心漂移乘上密度，也不自动等于总宏观电流，完整电流还涉及回旋磁化以及分布函数的空间变化。

## 磁力线曲率漂移与环形场的局限

磁力线即使大小不变，也可能改变方向。定义曲率向量

$$
\boldsymbol\kappa=(\mathbf b\cdot\nabla)\mathbf b,
\qquad
\mathbf b\cdot\boldsymbol\kappa=0,
\qquad
R_c=\frac{1}{|\boldsymbol\kappa|}.
$$

$\boldsymbol\kappa$ 指向局部曲率中心，单位 $\mathrm{m^{-1}}$；$R_c$ 是曲率半径，单位 m。沿弯曲磁力线运动的导引中心有与 $v_\parallel^2\boldsymbol\kappa$ 相关的惯性效应。在静态磁场、弱电漂移的最低阶近似下，曲率漂移为

$$
\mathbf v_\kappa
=\frac{mv_\parallel^2}{qB}\,\mathbf b\times\boldsymbol\kappa
=\frac{v_\parallel^2}{\Omega}\,\mathbf b\times\boldsymbol\kappa.
$$

由于 $v_\parallel$ 以平方出现，同一种电荷沿同一磁力线正向或反向运动时，其曲率漂移方向相同；改变电荷符号则反向。这是检查符号和理解往返轨道平均漂移的有用方法。[UT Austin：Magnetic Drifts，式 (2.54)–(2.56)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node19.html)。

把平行动能 $K_\parallel=mv_\parallel^2/2$ 代入，得到 $|\mathbf v_\kappa|=2K_\parallel/(|q|BR_c)$。例如单价粒子 $K_\parallel=1\,\mathrm{keV}$、$B=5\,\mathrm T$、$R_c=2\,\mathrm m$ 时，曲率漂移为 $200\,\mathrm{m\,s^{-1}}$。与梯度漂移比较时，不能忘记这里因 $mv_\parallel^2=2K_\parallel$ 产生的系数二。

以轴对称纯环向真空场 $\mathbf B=B_0R_0\hat{\boldsymbol\phi}/R$ 为例，柱坐标满足 $\hat{\mathbf R}\times\hat{\boldsymbol\phi}=\hat{\mathbf z}$，并有 $\boldsymbol\kappa=-\hat{\mathbf R}/R$、$\nabla B=-(B/R)\hat{\mathbf R}$。于是两种漂移同向叠加为

$$
\mathbf v_{\nabla B}+\mathbf v_\kappa
=\frac{m}{qBR}\left(v_\parallel^2+\frac12v_\perp^2\right)\hat{\mathbf z}.
$$

正离子与电子发生相反的垂直漂移。因此把直磁场弯成没有端点的圆环，并不足以获得良好单粒子约束；还需要考虑磁场扭转、轨道宽度和自洽电场等物理。[MIT OCW：Motion of Charged Particles，§2.4–§2.5，式 (2.45)、(2.55)、(2.56)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

**适用范围与误区。** 上述环向场只是一个指定几何例子，不是实际托卡马克的完整场。一般有等离子体电流的磁场中，$\nabla B/B$ 与 $\boldsymbol\kappa$ 不能直接互换；真空场中的特定关系有其 Maxwell 方程前提。强 E×B 流、时间变化或显著惯性需要保留更一般的导引中心惯性漂移，不能只留下 $v_\parallel^2\boldsymbol\kappa$ 项。

## 磁矩守恒、镜力与绝热压缩

缓变磁场中的第一绝热不变量在最低阶为

$$
\mu=\frac{mv_\perp^2}{2B}=\frac{K_\perp}{B},
\qquad
\frac{d\mu}{dt}\simeq0.
$$

$\mu$ 是正标量，单位 $\mathrm{J\,T^{-1}}$，不是带符号电荷。若画成回旋电流环，其磁偶极矩矢量指向 $-\mathbf b$，即 $\boldsymbol\mu_{\mathrm{orb}}=-\mu\mathbf b$；这与使用正标量 $\mu$ 表示轨道不变量并不矛盾。这里的 $v_\perp$ 是扣除慢漂移后的回旋速度，不能把显著整体垂直流的动能全部计入磁矩。[MIT OCW：Motion of Charged Particles，§2.6–§2.6.1，式 (2.85)–(2.97)，区分标量与电流环矢量](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)；[UT Austin：Invariance of Magnetic Moment，式 (2.60)–(2.70)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node20.html)。

在静态、无电场且慢漂移能量可忽略时，总动能 $K_\parallel+\mu B$ 保持不变。沿场坐标记为 $s$，因 $ds/dt=v_\parallel$，对能量求导得到导引中心镜力方程

$$
m\frac{dv_\parallel}{dt}=-\mu\frac{\partial B}{\partial s}.
$$

这个等式可由导引中心方程直接延拓至反射点，不能在 $v_\parallel=0$ 处依靠除以 $v_\parallel$ 来证明。它表明粒子进入更强磁场时，平行动能减小而垂直动能增大；总动能仍不变。镜力对正负电荷都指向弱场方向，虽然相应的横向漂移方向会随电荷改变。

若粒子从 $B_0$ 进入 $2B_0$，并在途中保持磁矩，则 $K_\perp$ 增为原来的两倍；若其初始 $K_\parallel$ 不够提供这部分能量，粒子会先反射，不会真的到达 $2B_0$。例如 $K_{\perp0}=2\,\mathrm{keV}$、$K_{\parallel0}=1\,\mathrm{keV}$ 时，静磁场中的镜点满足 $B_m/B_0=(K_{\perp0}+K_{\parallel0})/K_{\perp0}=1.5$。这是一项仅由守恒量得到的判断，不需要先积分完整螺旋轨道。

若磁场本身缓慢增强，$\mu$ 保持近似不变仍使 $K_\perp=\mu B$ 增加，但现在不应再使用静态无电场的总动能守恒。增加的能量来自感应电场；这是 betatron acceleration 或绝热磁压缩的基本机制。外部场能与粒子能之间的交换，和纯静磁场中两个速度分量之间的能量转换必须分开记账。[MIT OCW：Motion of Charged Particles，§2.6.2、§2.7](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

**适用范围与误区。** “绝热”在这里意为参数变化慢于相关周期，不是热力学上的绝热壁。$\mu$ 的最低阶表达式不是任意轨道的精确常数；快速变化、碰撞、回旋共振和有限回旋半径效应都可能破坏它。强波加热正可通过打破某些近似不变量改变粒子分布，所以不能在同一模型中一面严格固定 $\mu$，一面无解释地加入垂直共振加热。

## 磁镜反射、镜比与损失锥

考虑静态磁镜，粒子从磁场最小处 $B_0$ 出发，两端最大磁场均为 $B_{\max}$，镜比定义为 $R_m=B_{\max}/B_0>1$。假设单次往返中碰撞可忽略、磁矩近似守恒、静电势差和慢漂移动能可忽略。以初始 pitch angle $\alpha_0$ 表示速度与 $+\mathbf B$ 的夹角，则

$$
K=\frac12m(v_{\parallel0}^2+v_{\perp0}^2),
\qquad
\mu=\frac{K\sin^2\alpha_0}{B_0},
\qquad
B_m=\frac{B_0}{\sin^2\alpha_0}.
$$

镜点 $B_m$ 来自 $v_\parallel=0$ 时的 $K=\mu B_m$。只要 $B_m<B_{\max}$，粒子就在到达端部最大场前反射，因此通常的被俘获条件为

$$
\sin^2\alpha_0>\frac1{R_m},
\qquad
\alpha_L=\arcsin(R_m^{-1/2}).
$$

速度空间中沿 $+\mathbf B$ 和 $-\mathbf B$ 各有一个半角 $\alpha_L$ 的损失锥；等号处为理想模型的俘获–通过分界，不能据此承诺稳健约束。[MIT OCW：Motion of Charged Particles，§2.6.3–§2.6.4，式 (2.112)–(2.118)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)；[UT Austin：Magnetic Mirrors，式 (2.88)–(2.90)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node23.html)。

例如 $R_m=4$ 时，$\alpha_L=30^\circ$。初始 $\alpha_0=45^\circ$ 的粒子在 $B_m=2B_0$ 处反射；$\alpha_0=20^\circ$ 的粒子所需镜点约为 $8.55B_0$，超过可用最大场，因此不会在端部之前发生纯磁反射。对磁场最小处各向同性的速度方向分布，两端损失锥占立体角比例为

$$
f_{\mathrm{cone}}=\frac{2\,2\pi(1-\cos\alpha_L)}{4\pi}
=1-\sqrt{1-\frac1{R_m}}.
$$

$R_m=4$ 给出约 $13.4\%$。这是初始方向空间的几何比例，不是稳态损失率，也不是粒子约束时间；后两者还依赖补充、散射、飞行时间和势结构。

若存在沿轨道的静电势差，则应使用

$$
\mathcal E=\frac12mv_\parallel^2+\mu B+q\phi,
\qquad
K_\parallel(s)=K_{\parallel0}
-\mu[B(s)-B_0]-q[\phi(s)-\phi_0].
$$

可达区域要求 $K_\parallel(s)\ge0$；真正的有效势垒是沿轨道的 $\mu B+q\phi$。仅有局部 $E\ll Bv$ 并不能保证累计势能差 $|q\Delta\phi|$ 远小于动能，因此不能据“弱电场”直接套用纯磁损失锥公式。[UT Austin：Magnetic Mirrors，式 (2.85)、(2.86)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node23.html)。

**适用范围与误区。** 实际磁镜中，碰撞或波动可把被俘获粒子散射进损失锥；非对称端部需分别检查两个势垒。磁镜反射不证明横向漂移轨道稳定，也不证明没有宏观或速度空间不稳定性。镜比增大能缩小理想损失锥，但不能只凭镜比给出实际约束性能或聚变增益。

## 绝热不变量、导引中心排序与失效条件

导引中心方法把快速回旋与慢轨道分离。其核心是粒子一周内遇到的电磁场变化足够小，而不只是固定空间点处的 $\partial_tB$ 小。一个保守的局部检查包括

$$
\frac{\rho|\nabla B|}{B}\ll1,
\qquad
\frac{\rho}{R_c}\ll1,
\qquad
\frac{|v_\parallel|}{|\Omega|L_{\parallel,B}}\ll1,
\qquad
\frac{|\partial_tB|}{|\Omega|B}\ll1.
$$

$L_{\parallel,B}$ 表示沿场遇到的场强或方向变化尺度；还应检查慢漂移穿越背景梯度的速率，以及电场在轨道尺度上的变化。若在一次回旋内粒子经历的显著散射概率不可忽略，碰撞也破坏这一无碰撞平均。以上是不等式量级检查，不是对任意初值给出统一误差界的定理。[UT Austin：Guiding Center Motion，式 (2.21)–(2.30)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node18.html)。

第一不变量是 $\mu$。对在两个镜点 $s_1,s_2$ 之间作周期往返运动的被俘获粒子，还可定义第二不变量

$$
J_b=\oint m v_\parallel\,ds
=2\int_{s_1}^{s_2}
\sqrt{2m[\mathcal E-\mu B(s)-q\phi(s)]}\,ds.
$$

$J_b$ 的单位为 $\mathrm{J\,s}$；在闭合积分中，返回段的 $v_\parallel$ 与有向 $ds$ 同时反号，所以两段相加为正，而不是互相抵消。这里采用慢漂移动能可忽略的静态轨道来定义瞬时往返积分；它在背景变化慢于往返周期 $\tau_b$ 时才可能近似守恒。仅仅 $\tau_{\mathrm{bg}}\gg\tau_c$ 足以支持回旋绝热，却不足以保证往返绝热。[UT Austin：Second Adiabatic Invariant，式 (2.115)–(2.118) 及往返时间条件](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node26.html)。

若慢漂移还形成近似闭合的第三种周期轨道，且背景变化比漂移周期 $\tau_d$ 更慢，可进一步讨论第三绝热不变量；在相应排序下，它与漂移轨道所围磁通 $\Psi_d=\int\mathbf B\cdot d\mathbf S$ 成正比。不是每一种聚变装置轨道都自动具备这种闭合漂移结构；磁面几何闭合也不等价于任意粒子漂移轨道闭合。[UT Austin：Third Adiabatic Invariant，式 (2.119)、(2.120)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node27.html)。

因此常见的理想层次是 $\tau_c\ll\tau_b\ll\tau_d$，但每个守恒量都需要与背景变化时间单独比较。靠近俘获–通过分界时，往返周期可能很长，第二不变量可先失效，而第一不变量仍近似有效。类似地，回旋共振满足粒子沿轨道看到的扰动频率接近回旋频率，即使实验室中的某些背景量缓慢，也可能持续改变磁矩。

**实际使用。** 选择全轨道、导引中心或回旋平均模型前，应列出粒子能量和 pitch angle 范围，再检查整个轨道上而非仅初始点处的尺度比。守恒量可用作数值误差诊断，但只有当物理假设允许它守恒时才有效；在有碰撞、显式加热或时变势的计算中强行“修正”能量为常数，会删掉真实物理。一个局部尺度检查通过，也不保证长期轨道没有共振、随机化或损失。

[返回基础原理](../README.md)
