# 单粒子运动

单粒子轨道是理解磁约束、漂移、磁镜和波粒共振的起点。本专题先把电磁场视为给定场，研究测试粒子；真实等离子体还必须由所有组分的电荷和电流自洽求场。除特别说明外，采用 SI、非相对论、无碰撞近似；$q$ 始终是带符号电荷，$e>0$ 是元电荷大小，$B=|\mathbf B|$，$\mathbf b=\mathbf B/B$。各漂移公式是满足尺度排序时的导引中心近似；完整轨道由 Lorentz 方程积分得到。

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

因此磁力改变速度方向而不直接改变动能。这不仅对均匀或静态磁场成立；磁力项在任意时刻都与速度正交。不过时变磁场伴随 $\nabla\times\mathbf E=-\partial_t\mathbf B$，感应电场可以做功，磁压缩的能量转移因此通过感应电场实现。[UT Austin：Motion in Uniform Fields，式 (2.1)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node16.html)；[Invariance of Magnetic Moment，式 (2.60)–(2.65)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node20.html)。

若场与时间无关且 $\mathbf E=-\nabla\phi$，则

$$
\frac{d}{dt}(K+q\phi)=0,
\qquad
K_2-K_1=-q(\phi_2-\phi_1).
$$

这一步用到了沿轨道的链式法则：静态势满足 $d\phi/dt=\mathbf v\cdot\nabla\phi=-\mathbf E\cdot\mathbf v$，所以它恰好抵消 $dK/dt$。若仍采用 $\mathbf E=-\nabla\phi$ 而势显含时间，剩下的则是 $d(K+q\phi)/dt=q\partial_t\phi$，不能再套用静态能量常数。

这里 $\phi$ 的单位是 V，$q\phi$ 的单位为 J。电子从低电势走向高电势时，$q=-e$ 使其势能下降、动能增加；单价正离子恰好相反。例如电子跨过 $+100\,\mathrm V$ 的电势增量，获得 $100\,\mathrm{eV}$ 动能。这个符号检查比凭“沿电场方向加速”口头记忆更可靠，因为电子受力与电场相反。[UT Austin：Magnetic Mirrors，式 (2.83)–(2.85)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node23.html)。

本式未包含碰撞、辐射反作用或外加非电磁力；温度变化还需对整个分布取速度矩。对相对论粒子应使用 $d(\gamma m\mathbf v)/dt=q(\mathbf E+\mathbf v\times\mathbf B)$；功率仍为 $q\mathbf E\cdot\mathbf v$，但动能不再等于 $mv^2/2$。轨道数值计算若在 $\mathbf E=0$ 的静态场中出现持续动能漂移，首先应检查积分误差。

这里 $\gamma=(1-v^2/c^2)^{-1/2}$。相对论能量 $\mathcal E=\sqrt{m^2c^4+p^2c^2}$ 满足 $\partial\mathcal E/\partial\mathbf p=\mathbf v$，因而 $d[(\gamma-1)mc^2]/dt=\mathbf v\cdot d\mathbf p/dt=q\mathbf E\cdot\mathbf v$。这说明相对论形式保留的是功率恒等式，而非非相对论的速度平方表达式。

### 平行电场加速的轨道与功核算

令 $\mathbf B=B\hat{\mathbf z}$、$\mathbf E=E_\parallel\hat{\mathbf z}$ 均匀且静态。Lorentz 方程的 $z$ 分量独立积分为 $v_z=v_{z0}+at$、$z-z_0=v_{z0}t+at^2/2$，其中 $a=qE_\parallel/m$；横向分量仍作恒速回旋。沿实际轨道计算电功，得到

$$
W_E=q\int_0^tE_\parallel v_z\,dt
=qE_\parallel\left(v_{z0}t+\frac12at^2\right)
=\frac m2\left[(v_{z0}+at)^2-v_{z0}^2\right].
$$

等式的前一端是力沿位移的积分，后一端是纵向动能增量，二者可用不同方法计算。横向磁力随时间改变方向，始终与横向速度正交。这个分解也说明，轨道越来越长的螺距反映平行加速；回旋周期由静态磁场决定。

**算例。** 单价氘离子初始 $v_{z0}=2.00\times10^4\,\mathrm{m\,s^{-1}}$，在 $E_\parallel=50.0\,\mathrm{V\,m^{-1}}$ 中运动 $2.00\,\mu\mathrm s$。先算 $a=eE_\parallel/m_D=2.39590\times10^9\,\mathrm{m\,s^{-2}}$，再得 $v_z=2.47918\times10^4\,\mathrm{m\,s^{-1}}$、$\Delta z=0.0447918\,\mathrm m$。电功除以 $e$ 是 $50.0\times0.0447918=2.23959\,\mathrm{eV}$。直接以两个速度平方求动能差，得到相同值。改变 $B$ 会改变螺旋半径和周期，而这个平行功结果保持原样。[MIT 第 2 章 §2.1–2.2，式 (2.7)、(2.12)–(2.14)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

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

对第一式求导并代入第二式，得到 $\ddot v_x+\Omega^2v_x=0$；初值 $v_x(0)=v_\perp$、$\dot v_x(0)=0$ 固定余弦解，再由 $v_y=\dot v_x/\Omega$ 得正弦分量。位置积分给圆半径 $v_\perp/|\Omega|$，相位推进 $2\pi$ 给周期；以下轨道、半径和螺距均由这同一组解推出。

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

$\rho$、$\Delta z$ 用 m，$\tau_c$ 用 s。半径采用频率绝对值，保持为非负量。平行分量只使圆轨道变成螺旋线，不直接改变回旋频率；这里的频率独立于速度是非相对论结果。[UT Austin：Motion in Uniform Fields，式 (2.3)、(2.5)–(2.7)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node16.html)。

用给定的垂直动能 $K_\perp=mv_\perp^2/2$ 可改写为 $\rho=\sqrt{2mK_\perp}/(|q|B)$。例如 $B=5\,\mathrm T$、$K_\perp=1\,\mathrm{keV}$ 时，电子半径约 $21.3\,\mu\mathrm m$，氘离子半径约 $1.29\,\mathrm{mm}$。这比较的是单粒子的垂直动能；如果改为 Maxwellian 温度算例，必须说明选择哪一种热速度。相同质量和磁场下，把垂直动能增大四倍会使半径增大两倍。

这里的“固定导引中心”只在无电场且磁场均匀时成立；梯度、曲率、其他力以及电场会让导引中心移动。轨道含围绕导引中心的回旋与慢漂移。对磁零点 $B=0$，回旋表达式本身失去定义；对相对论能量，回旋频率变为 $|q|B/(\gamma m)$，共振条件也需保留该相对论因子。

### 从速度解积分到带初值的空间轨道

取初始位置为原点、初速度 $(v_\perp,0,v_\parallel)$，对已得的速度正弦解再积分，便得到带符号 $\Omega=qB/m$ 的轨道：

$$
x(t)=\frac{v_\perp}{\Omega}\sin\Omega t,\quad
y(t)=\frac{v_\perp}{\Omega}(\cos\Omega t-1),\quad
z(t)=v_\parallel t.
$$

因此 $x^2+[y+v_\perp/\Omega]^2=(v_\perp/\Omega)^2$，导引中心位于 $(0,-v_\perp/\Omega)$。半径取绝对值，中心偏移和转动方向保留电荷符号。对正电荷，初始加速度为 $-\Omega v_\perp\hat{\mathbf y}$，与轨道在原点的弯曲方向一致。一个周期后的纵向位移 $2\pi v_\parallel/|\Omega|$ 就是螺距。

**算例。** 取氘离子 $B=0.80\,\mathrm T$、$v_\perp=2.00\times10^5\,\mathrm{m\,s^{-1}}$、$v_\parallel=1.00\times10^5\,\mathrm{m\,s^{-1}}$。$\Omega=eB/m_D=3.83344\times10^7\,\mathrm{rad\,s^{-1}}$，四分之一周期为 $t_q=\pi/(2\Omega)=40.9762\,\mathrm{ns}$。代入轨道，得到 $(x,y,z)=(5.21725,-5.21725,4.09762)\,\mathrm{mm}$。该点离导引中心仍为 $5.21725\,\mathrm{mm}$；速度为 $(0,-2.00\times10^5,1.00\times10^5)\,\mathrm{m\,s^{-1}}$，速度平方与初值相等。这组坐标和速度可同时检验积分程序的符号、相位与能量。[MIT 第 2 章 §2.1.2，式 (2.8)–(2.11)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

## 均匀电磁场中的 E×B 漂移与力漂移

在均匀、静态且 $B\ne0$ 的场中，分解 $\mathbf E=\mathbf E_\perp+E_\parallel\mathbf b$。沿场运动满足 $m\dot v_\parallel=qE_\parallel$；垂直运动可写成回旋运动叠加匀速漂移

$$
\mathbf v_E=\frac{\mathbf E\times\mathbf B}{B^2}.
$$

它的单位为 $\mathrm{m\,s^{-1}}$。代入可直接验证 $\mathbf E_\perp+\mathbf v_E\times\mathbf B=0$：令 $\mathbf w_\perp=\mathbf v_\perp-\mathbf v_E$ 后，$\mathbf w_\perp$ 满足无电场的回旋方程。电子与离子的 $\mathbf v_E$ 相同，因为电荷在电力和磁力两边抵消；两种粒子的瞬时回旋部分由各自质量和电荷决定。[UT Austin：Motion in Uniform Fields，式 (2.2)–(2.4)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node16.html)。

若 $\mathbf E=E_x\hat{\mathbf x}$、$\mathbf B=B\hat{\mathbf z}$，则 $\mathbf v_E=-(E_x/B)\hat{\mathbf y}$。取 $E_x=10^3\,\mathrm{V\,m^{-1}}$、$B=5\,\mathrm T$，漂移为 $-200\hat{\mathbf y}\,\mathrm{m\,s^{-1}}$，这一方向对正离子和电子一致。均匀静态垂直电场对周期回旋的平均净功为零，因为 $\mathbf E\cdot\mathbf v_E=0$、回旋速度周期平均为零；但瞬时 $q\mathbf E\cdot\mathbf v$ 可以不为零，初始动能也不必恒定。

一个缓慢、近似恒定的额外垂直力 $\mathbf F_\perp$ 产生最低阶力漂移

$$
\mathbf v_F=\frac{\mathbf F\times\mathbf B}{qB^2}.
$$

具体求解是把平均力平衡右叉乘 $\mathbf B$：$\mathbf F_\perp\times\mathbf B+q(\mathbf v_F\times\mathbf B)\times\mathbf B=0$。利用 $\mathbf v_F\cdot\mathbf B=0$，第二项等于 $-qB^2\mathbf v_F$，便得到上式；若有平行力，它应进入平行加速方程，不能通过此式消去。

把 $\mathbf F=q\mathbf E$ 代入便返回 $\mathbf v_E$；若 $\mathbf F$ 与电荷无关，例如重力 $m\mathbf g$，漂移就会随电荷符号改变方向。这个公式可由平均力平衡 $\mathbf F_\perp+q\mathbf v_F\times\mathbf B=0$ 导出；快速共振驱动应直接求时变轨道响应。[MIT OCW：Motion of Charged Particles，§2.2–§2.2.1，式 (2.14)–(2.23)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

取非均匀场的局域 $\mathbf E\times\mathbf B/B^2$ 时，需要场在回旋尺度上平滑；快速变化的电场会产生极化等修正。相同的 $\mathbf v_E$ 对精确准中性的混合物给出 $\mathbf j_E=\rho_q\mathbf v_E\simeq0$，但它仍运输粒子、压力与能量，其输运由相应通量描述。当 $E_\perp/B$ 接近光速时，应采用相对论轨道与场变换。

### 从静止释放后的摆线与周期电功

在 $\mathbf E=E\hat{\mathbf x}$、$\mathbf B=B\hat{\mathbf z}$ 中让正粒子从静止释放。记 $v_E=E/B>0$、$\Omega=qB/m>0$；将 $w_y=v_y+v_E$ 代入运动方程，可得 $\dot v_x=\Omega w_y$、$\dot w_y=-\Omega v_x$，初值为 $(v_x,w_y)=(0,v_E)$。积分给出

$$
v_x=v_E\sin\Omega t,\quad v_y=v_E(\cos\Omega t-1),
$$
$$
x=\frac{v_E}{\Omega}(1-\cos\Omega t),\quad
y=\frac{v_E}{\Omega}\sin\Omega t-v_Et,\quad
K=mv_E^2(1-\cos\Omega t)=qEx.
$$

圆周运动与沿 $-y$ 的匀速平移合成摆线。虽然释放时速度为零，导引中心已经以漂移速度移动，回旋速度恰好抵消其瞬时值；每个整周期回到相同电势。

**算例。** 给定氘离子、$E=2.00\times10^3\,\mathrm{V\,m^{-1}}$、$B=0.40\,\mathrm T$，有 $v_E=5000\,\mathrm{m\,s^{-1}}$、周期 $T_c=3.27810\times10^{-7}\,\mathrm s$。半周期时 $x=2v_E/\Omega=0.521725\,\mathrm{mm}$，动能为 $eEx=1.04345\,\mathrm{eV}$。一周期时 $x=0$、动能回零，$y=-v_ET_c=-1.63905\,\mathrm{mm}$。由终点位移除以周期得到 $-5000\,\mathrm{m\,s^{-1}}$，独立恢复漂移速度；对 $qEv_x$ 积分所得周期净功为零。[MIT 第 2 章 §2.2，均匀交叉场的变换与解](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

## 磁场强度梯度引起的 grad-B 漂移

在磁场随空间缓慢变化时，回旋轨道的强场一侧弯曲更紧，弱场一侧弯曲更松，轨道一周后一般不再闭合。对满足导引中心排序的粒子，定义正的磁矩标量 $\mu=mv_\perp^2/(2B)$，得到最低阶梯度漂移

$$
\mathbf v_{\nabla B}
=\frac{\mu}{qB}\,\mathbf b\times\nabla B
=\frac{mv_\perp^2}{2qB^3}\,\mathbf B\times\nabla B
=\frac{K_\perp}{qB^2}\,\mathbf b\times\nabla B.
$$

$\nabla B$ 的单位是 $\mathrm{T\,m^{-1}}$，$\mu$ 的单位是 $\mathrm{J\,T^{-1}}$，结果是速度。三个表达式等价，尤其要保留最后两式中不同的 $B$ 次数。电子与正离子的方向相反；这与同向的 E×B 漂移形成可检验的区别。[UT Austin：Magnetic Drifts，式 (2.52)、(2.53)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node19.html)；[MIT OCW：Motion of Charged Particles，§2.3，式 (2.36)、(2.37)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

也可把回旋平均后的有效磁镜力写作 $\mathbf F_{\mu}=-\mu\nabla B$。它的垂直部分代入力漂移 $\mathbf F\times\mathbf B/(qB^2)$，恰好给出上式。这里的有效力是回旋平均描述中的量；它已包含完整回旋的平均作用。平行部分 $-\mu\nabla_\parallel B$ 则影响沿场运动。

令 $\mathbf B=B(x)\hat{\mathbf z}$、$dB/dx>0$，则 $\mathbf b\times\nabla B$ 指向 $+y$，正离子向 $+y$ 漂移，电子向 $-y$ 漂移。定义 $L_B=B/|\nabla_\perp B|$，漂移大小为

$$
|\mathbf v_{\nabla B}|=\frac{K_\perp}{|q|B L_B}.
$$

对单价粒子 $K_\perp=1\,\mathrm{keV}$、$B=5\,\mathrm T$、$L_B=0.5\,\mathrm m$，大小为 $400\,\mathrm{m\,s^{-1}}$。相同电荷量和相同垂直动能时，该估算不显含质量；若改为固定速度比较，就会有质量依赖。比较时应固定同一种能量或速度条件。

该式要求 $\rho/L_B\ll1$、背景变化慢于回旋，且这里使用的 $v_\perp$ 是相对于导引中心的回旋速度；显著 E×B 流应先分离。$\nabla B$ 指磁场大小的梯度，由标量 $B$ 求导；只有其垂直于磁场的部分进入漂移。把局部的导引中心漂移乘上密度，只是宏观电流的一项贡献，完整电流还涉及回旋磁化以及分布函数的空间变化。

### 把轨道上的非均匀力作回旋平均

先取正电荷、$B_0>0$，局部取 $\mathbf B=(B_0+Gx)\hat{\mathbf z}$，$G=\partial_xB$、$\rho G/B_0\ll1$。在导引中心附近，用零阶轨道 $x=\rho\sin\Omega t$、$v_y=-v_\perp\sin\Omega t$ 计算一阶磁力修正。它在 $x$ 方向的平均值是

$$
\langle\delta F_x\rangle=qG\langle xv_y\rangle
=-\frac{qG\rho v_\perp}{2}=-\frac{mv_\perp^2G}{2B_0}=-\mu G.
$$

于是平均横向力平衡要求 $qB_0v_{\nabla B,y}-\mu G=0$，得到 $v_{\nabla B,y}=\mu G/(qB_0)=K_\perp G/(qB_0^2)$。这个计算把漂移的方向与粒子在强、弱场半圈的受力差联系起来；$\langle\sin^2\Omega t\rangle=1/2$ 正是系数二的来源。

**算例。** 单价氘离子 $K_\perp=600\,\mathrm{eV}$，局部 $B_0=0.60\,\mathrm T$、$G=0.30\,\mathrm{T\,m^{-1}}$。用焦耳代入或约去 $e$，均得 $v_{\nabla B,y}=600\times0.30/0.60^2=500\,\mathrm{m\,s^{-1}}$，沿 $+y$。回旋半径为 $8.34047\,\mathrm{mm}$，所以 $\rho G/B_0=0.00417023$，满足局部展开条件。相同垂直能量的电子有相反漂移方向；由两者速度差可形成垂直电流。[Fitzpatrick，Guiding Center Motion，式 (2.42)–(2.51) 的回旋平均](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node18.html)。

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

其来源可直接在实验室系写清：沿曲线运动时 $d(v_\parallel\mathbf b)/dt$ 的垂直部分是 $v_\parallel^2(\mathbf b\cdot\nabla)\mathbf b=v_\parallel^2\boldsymbol\kappa$，故最低阶需有 $q\mathbf v_\kappa\times\mathbf B=mv_\parallel^2\boldsymbol\kappa$。两边左叉乘 $\mathbf b$，用 $\mathbf b\times(\mathbf v_\kappa\times\mathbf B)=B\mathbf v_\kappa$，得到上式。曲率正交关系由 $\mathbf b\cdot\boldsymbol\kappa=(\mathbf b\cdot\nabla)(\mathbf b^2)/2=0$ 推出。

由于 $v_\parallel$ 以平方出现，同一种电荷沿同一磁力线正向或反向运动时，其曲率漂移方向相同；改变电荷符号则反向。这是检查符号和理解往返轨道平均漂移的有用方法。[UT Austin：Magnetic Drifts，式 (2.54)–(2.56)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node19.html)。

把平行动能 $K_\parallel=mv_\parallel^2/2$ 代入，得到 $|\mathbf v_\kappa|=2K_\parallel/(|q|BR_c)$。例如单价粒子 $K_\parallel=1\,\mathrm{keV}$、$B=5\,\mathrm T$、$R_c=2\,\mathrm m$ 时，曲率漂移为 $200\,\mathrm{m\,s^{-1}}$。相对梯度漂移，曲率项含 $mv_\parallel^2=2K_\parallel$ 带来的系数二。

以轴对称纯环向真空场 $\mathbf B=B_0R_0\hat{\boldsymbol\phi}/R$ 为例，柱坐标满足 $\hat{\mathbf R}\times\hat{\boldsymbol\phi}=\hat{\mathbf z}$，并有 $\boldsymbol\kappa=-\hat{\mathbf R}/R$、$\nabla B=-(B/R)\hat{\mathbf R}$。于是两种漂移同向叠加为

$$
\mathbf v_{\nabla B}+\mathbf v_\kappa
=\frac{m}{qBR}\left(v_\parallel^2+\frac12v_\perp^2\right)\hat{\mathbf z}.
$$

正离子与电子发生相反的垂直漂移。圆环中这类垂直漂移需要借助磁场扭转、自洽电场和轨道平均来控制，完整约束还取决于轨道宽度。[MIT OCW：Motion of Charged Particles，§2.4–§2.5，式 (2.45)、(2.55)、(2.56)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

上述环向场用于隔离曲率效应；托卡马克的完整轨道还包含极向场。有电流时，$\nabla B/B$ 与 $\boldsymbol\kappa$ 的关系包含电流项；真空场满足 $\nabla\times\mathbf B=0$ 时可得到本段给出的特殊关系。强 E×B 流和时间变化会带来额外惯性贡献，应保留完整的导引中心加速度。

### 在圆柱基矢中合并两种磁漂移

对纯环向场 $\mathbf B=B_0R_0\mathbf e_\phi/R$，必须对空间变化的基矢求导。因为 $(\mathbf b\cdot\nabla)=R^{-1}\partial_\phi$ 且 $\partial_\phi\mathbf e_\phi=-\mathbf e_R$，所以 $\boldsymbol\kappa=-\mathbf e_R/R$；同时 $\nabla B=-(B/R)\mathbf e_R$。用 $\mathbf e_\phi\times\mathbf e_R=-\mathbf e_z$ 分别代入两种漂移，得到

$$
\mathbf v_{\nabla B}=\frac{K_\perp}{qBR}\mathbf e_z,\qquad
\mathbf v_\kappa=\frac{2K_\parallel}{qBR}\mathbf e_z,\qquad
\mathbf v_{\rm mag}=\frac{K_\perp+2K_\parallel}{qBR}\mathbf e_z.
$$

平行速度的正负在平方后消失，因此沿环向正走和反走的同种粒子具有相同竖直磁漂移方向。两种漂移在该几何中相加，电荷符号决定上下分离；这也是纯环向场中需要引入额外磁场扭转的动力学原因。

**算例。** 对单价正离子，取 $K_\perp=400\,\mathrm{eV}$、$K_\parallel=800\,\mathrm{eV}$、$B=1.20\,\mathrm T$、$R=1.50\,\mathrm m$。梯度漂移为 $222.222\,\mathrm{m\,s^{-1}}$，曲率漂移为 $888.889\,\mathrm{m\,s^{-1}}$，总和 $1111.11\,\mathrm{m\,s^{-1}}$ 沿 $+z$。保持这些局部参数 $20.0\,\mu\mathrm s$，导引中心升高 $2.22222\,\mathrm{cm}$。该位移直接由 $\int v_zdt$ 求得，可与完整环向场轨道的回旋平均比较。[MIT 第 2 章 §2.3–2.4，式 (2.40)–(2.48)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

## 磁矩守恒、镜力与绝热压缩

缓变磁场中的第一绝热不变量在最低阶为

$$
\mu=\frac{mv_\perp^2}{2B}=\frac{K_\perp}{B},
\qquad
\frac{d\mu}{dt}\simeq0.
$$

$\mu$ 是正标量，单位 $\mathrm{J\,T^{-1}}$。若画成回旋电流环，其磁偶极矩矢量指向 $-\mathbf b$，即 $\boldsymbol\mu_{\mathrm{orb}}=-\mu\mathbf b$；标量 $\mu$ 与磁偶极矩矢量承担不同的记号作用。这里的 $v_\perp$ 是扣除慢漂移后的回旋速度，整体漂移动能在回旋能之外单独计算。[MIT OCW：Motion of Charged Particles，§2.6–§2.6.1，式 (2.85)–(2.97)，区分标量与电流环矢量](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)；[UT Austin：Invariance of Magnetic Moment，式 (2.60)–(2.70)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node20.html)。

标量大小也可由电流环求出：周期电流大小 $|I|=|q|/\tau_c$，面积为 $\pi\rho^2$，所以 $|I|\pi\rho^2=|q||\Omega|\rho^2/2=mv_\perp^2/(2B)$。正电荷沿负方位角回旋，负电荷沿正方位角回旋但电流反向，两者的偶极矩都指向 $-\mathbf b$。

为避免把磁矩守恒与镜力互相当作前提，可先从满足 $\nabla\cdot\mathbf B=0$ 的轴附近静磁场出发。令 $B_z=B(s)$，近轴径向场为 $B_r=-r\partial_sB/2$；零阶回旋有 $r=\rho$、$v_\phi=-\Omega\rho$。于是平行磁力的回旋平均是 $\langle F_s\rangle=-qv_\phi B_r=-mv_\perp^2\partial_sB/(2B)=-\mu\partial_sB$。结合磁场不做功，$\dot K_\perp=-\dot K_\parallel=\mu v_\parallel\partial_sB=\mu\dot B$，故 $d(K_\perp/B)/dt=0$ 至最低阶；一般缓变导引中心展开给出相同结果。时变均匀场的独立推导见下方感应电功。

在静态、无电场且慢漂移能量可忽略时，总动能 $K_\parallel+\mu B$ 保持不变。沿场坐标记为 $s$，因 $ds/dt=v_\parallel$，对能量求导得到导引中心镜力方程

$$
m\frac{dv_\parallel}{dt}=-\mu\frac{\partial B}{\partial s}.
$$

这个等式由导引中心方程连续延拓至 $v_\parallel=0$ 的反射点。它表明粒子进入更强磁场时，平行动能减小而垂直动能增大；总动能仍不变。镜力对正负电荷都指向弱场方向，虽然相应的横向漂移方向会随电荷改变。

若粒子从 $B_0$ 进入 $2B_0$，并在途中保持磁矩，则 $K_\perp$ 增为原来的两倍；若其初始 $K_\parallel$ 不够提供这部分能量，粒子会先反射，不会真的到达 $2B_0$。例如 $K_{\perp0}=2\,\mathrm{keV}$、$K_{\parallel0}=1\,\mathrm{keV}$ 时，静磁场中的镜点满足 $B_m/B_0=(K_{\perp0}+K_{\parallel0})/K_{\perp0}=1.5$。这是一项仅由守恒量得到的判断，不需要先积分完整螺旋轨道。

若磁场本身缓慢增强，$\mu$ 保持近似不变仍使 $K_\perp=\mu B$ 增加，但现在不应再使用静态无电场的总动能守恒。增加的能量来自感应电场；这是 betatron acceleration 或绝热磁压缩的基本机制。外部场能与粒子能之间的交换，和纯静磁场中两个速度分量之间的能量转换必须分开记账。[MIT OCW：Motion of Charged Particles，§2.6.2、§2.7](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

这里的“绝热”指轨道参数变化慢于相应周期。$\mu$ 在所列缓变排序下近似守恒；快速变化、碰撞、回旋共振和有限回旋半径效应给出相应修正。垂直共振加热通过非绝热波粒作用改变 $\mu$，可在导引中心模型中加入对应的扩散或能量源。

### 感应电场如何实现 betatron 增能

考虑轴附近缓慢增长的均匀轴向场 $B(t)$。半径 $r$ 的固定圆周上，Faraday 定律给 $2\pi rE_\phi=-\pi r^2\dot B$，所以 $E_\phi=-r\dot B/2$。正粒子绕 $+z$ 磁场的回旋速度沿负方位方向，故回旋平均电功为正。以回旋半径 $\rho$ 计算，

$$
\langle q\mathbf E\cdot\mathbf v\rangle
=\frac{|q|\rho v_\perp}{2}\dot B
=\frac{mv_\perp^2}{2B}\dot B=\mu\dot B.
$$

另一方面 $K_\perp=\mu B$，求导给 $\dot K_\perp=\mu\dot B+B\dot\mu$，与电功比较得到最低阶 $\dot\mu=0$。因此垂直速度随 $\sqrt B$ 增长，半径随 $B^{-1/2}$ 缩小，回旋环包围的磁通 $\pi\rho^2B$ 保持。能量来自维持时变场的外部电源，经感应电场传给粒子。

**算例。** 给定初始 $B_0=0.20\,\mathrm T$、$K_{\perp0}=300\,\mathrm{eV}$，场在远长于回旋周期的时间内升至 $0.60\,\mathrm T$。磁矩为 $1500\,\mathrm{eV\,T^{-1}}$，故末态垂直能量为 $900\,\mathrm{eV}$，增加 $600\,\mathrm{eV}$；电功积分 $\int_{B_0}^{B_1}\mu\,dB$ 也给 $600\,\mathrm{eV}$。速度比为 $\sqrt3$，半径比为 $1/\sqrt3=0.577350$，磁通比为 $(1/3)\times3=1$。[MIT 第 2 章 §2.7，式 (2.123)–(2.129)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)；[Fitzpatrick 式 (2.60)–(2.64)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node20.html)。

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

速度空间中沿 $+\mathbf B$ 和 $-\mathbf B$ 各有一个半角 $\alpha_L$ 的损失锥；等号处为理想模型的俘获–通过分界。[MIT OCW：Motion of Charged Particles，§2.6.3–§2.6.4，式 (2.112)–(2.118)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)；[UT Austin：Magnetic Mirrors，式 (2.88)–(2.90)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node23.html)。

例如 $R_m=4$ 时，$\alpha_L=30^\circ$。初始 $\alpha_0=45^\circ$ 的粒子在 $B_m=2B_0$ 处反射；$\alpha_0=20^\circ$ 的粒子所需镜点约为 $8.55B_0$，超过可用最大场，因此不会在端部之前发生纯磁反射。对磁场最小处各向同性的速度方向分布，两端损失锥占立体角比例为

$$
f_{\mathrm{cone}}=\frac{2\,2\pi(1-\cos\alpha_L)}{4\pi}
=1-\sqrt{1-\frac1{R_m}}.
$$

$R_m=4$ 给出约 $13.4\%$。这是初始方向空间的几何比例；稳态损失率和约束时间还由补充、散射、飞行时间与势结构确定。

若存在沿轨道的静电势差，则应使用

$$
\mathcal E=\frac12mv_\parallel^2+\mu B+q\phi,
\qquad
K_\parallel(s)=K_{\parallel0}
-\mu[B(s)-B_0]-q[\phi(s)-\phi_0].
$$

可达区域要求 $K_\parallel(s)\ge0$；真正的有效势垒是沿轨道的 $\mu B+q\phi$。纯磁损失锥还要求累计势能变化 $|q\Delta\phi|$ 相对动能很小，局部电场大小与沿轨道势差应分别比较。[UT Austin：Magnetic Mirrors，式 (2.85)、(2.86)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node23.html)。

实际磁镜中，碰撞或波动可把被俘获粒子散射进损失锥；非对称端部需分别检查两个势垒。整体约束还取决于横向漂移、碰撞散射与宏观及速度空间稳定性。镜比增大缩小理想损失锥，实际约束性能与聚变增益还涉及输运、加热和整体能量平衡。

### 抛物线磁镜中的反弹轨道

用磁轴附近场强剖面 $B(s)=B_0(1+s^2/L^2)$ 作为导引中心模型，$s$ 为沿场弧长，磁矩在一次反弹中守恒。镜力 $m\ddot s=-\mu\,dB/ds$ 化为谐振子：

$$
\ddot s+\omega_b^2s=0,\qquad
\omega_b=\sqrt{\frac{2\mu B_0}{mL^2}},\quad
s(t)=s_{\max}\sin\omega_bt,\quad
s_{\max}=L\sqrt{\frac{K_{\parallel0}}{K_{\perp0}}}.
$$

这里以粒子穿过场最小处为 $t=0$。能量关系 $K_\parallel(s)=K_{\parallel0}-\mu B_0s^2/L^2$ 也给同一个转折点；把 $s=s_{\max}$ 代入场强，得到 $B_m/B_0=1+K_{\parallel0}/K_{\perp0}$。反弹周期由场的曲率控制，而单独给镜比只确定可达场强范围。

**算例。** 氘离子在中央具有 $K_{\perp0}=K_{\parallel0}=1.00\,\mathrm{keV}$，取 $L=0.500\,\mathrm m$，并让磁镜延伸到至少 $B=2B_0$。计算得 $\omega_b=\sqrt{2(1000e)/(m_DL^2)}=6.19147\times10^5\,\mathrm{rad\,s^{-1}}$，周期 $10.1481\,\mu\mathrm s$，转折点为 $s_{\max}=0.500\,\mathrm m$。从中心到上端镜点需四分之一周期，即 $2.53703\,\mu\mathrm s$；此时平行动能全部转为额外垂直动能，总能量保持 $2.00\,\mathrm{keV}$。[MIT 第 2 章 §2.6，式 (2.98)–(2.118)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf)。

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

$L_{\parallel,B}$ 表示沿场遇到的场强或方向变化尺度；还应检查慢漂移穿越背景梯度的速率，以及电场在轨道尺度上的变化。若在一次回旋内粒子经历的显著散射概率不可忽略，碰撞也破坏这一无碰撞平均。这些无量纲比值给出导引中心展开的排序参数。[UT Austin：Guiding Center Motion，式 (2.21)–(2.30)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node18.html)。

第一不变量是 $\mu$。对在两个镜点 $s_1,s_2$ 之间作周期往返运动的被俘获粒子，还可定义第二不变量

$$
J_b=\oint m v_\parallel\,ds
=2\int_{s_1}^{s_2}
\sqrt{2m[\mathcal E-\mu B(s)-q\phi(s)]}\,ds.
$$

被积根号来自上一条的能量守恒 $p_\parallel^2/(2m)=\mathcal E-\mu B-q\phi$，返回段与去程具有相同的正面积。作用量近似守恒还需独立的慢变论证：对一维周期 Hamilton 系统，$\partial J_b/\partial\mathcal E=\oint ds/v_\parallel=\tau_b$；缓慢参数 $a(t)$ 满足 $\partial_aJ_b=-\tau_b\langle\partial_aH\rangle$，而能量的周期平均变化为 $\langle\dot{\mathcal E}\rangle=\langle\partial_aH\rangle\dot a$。将两项代入 $\dot J_b=J_{b,\mathcal E}\dot{\mathcal E}+J_{b,a}\dot a$，最低阶恰好抵消。这要求参数在一周期内变化小，并远离周期发散的分界。

$J_b$ 的单位为 $\mathrm{J\,s}$；在闭合积分中，返回段的 $v_\parallel$ 与有向 $ds$ 同时反号，所以两段相加为正。这里采用慢漂移动能可忽略的静态轨道来定义瞬时往返积分；它在背景变化慢于往返周期 $\tau_b$ 时才可能近似守恒。仅仅 $\tau_{\mathrm{bg}}\gg\tau_c$ 足以支持回旋绝热，却不足以保证往返绝热。[UT Austin：Second Adiabatic Invariant，式 (2.115)–(2.118) 及往返时间条件](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node26.html)。

若慢漂移还形成近似闭合的第三种周期轨道，且背景变化比漂移周期 $\tau_d$ 更慢，可进一步讨论第三绝热不变量；在相应排序下，它与漂移轨道所围磁通 $\Psi_d=\int\mathbf B\cdot d\mathbf S$ 成正比。第三不变量要求粒子漂移轨道近似闭合，需结合磁面几何和实际漂移共同判断。[UT Austin：Third Adiabatic Invariant，式 (2.119)、(2.120)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node27.html)。

其磁通形式来自慢闭合轨道的正则作用量：正则动量含 $q\mathbf A$，导引中心最低阶的慢漂移闭合积分中，磁矢势贡献为 $q\oint\mathbf A\cdot d\boldsymbol\ell=q\int\mathbf B\cdot d\mathbf S=q\Psi_d$（Stokes 定理）。只有当其余正则动量贡献在所用排序下可忽略、且存在该慢周期时，才可把第三作用量写成磁通形式；慢变守恒依据与上述周期作用量相同。

因此常见的理想层次是 $\tau_c\ll\tau_b\ll\tau_d$，但每个守恒量都需要与背景变化时间单独比较。靠近俘获–通过分界时，往返周期可能很长，第二不变量可先失效，而第一不变量仍近似有效。类似地，回旋共振满足粒子沿轨道看到的扰动频率接近回旋频率，即使实验室中的某些背景量缓慢，也可能持续改变磁矩。

**实际使用。** 选择全轨道、导引中心或回旋平均模型前，应列出粒子能量和 pitch angle 范围，再检查整个轨道上而非仅初始点处的尺度比。守恒量可用作数值误差诊断，但只有当物理假设允许它守恒时才有效；在有碰撞、显式加热或时变势的计算中强行“修正”能量为常数，会删掉真实物理。长期轨道计算同时跟踪共振、随机化与损失。

### 用反弹作用量求慢压缩后的平行能量

对上一类谐振镜势，平行运动能量是 $K_{\parallel0}=p_\parallel^2/(2m)+m\omega_b^2s^2/2$。相轨道为椭圆，作用量是该椭圆面积。直接以 $s=s_{\max}\sin\theta$ 积分，得到

$$
J=\oint p_\parallel ds
=4m\omega_bs_{\max}^2\int_0^{\pi/2}\cos^2\theta\,d\theta
=\frac{2\pi K_{\parallel0}}{\omega_b}.
$$

当参数变化时间远大于反弹周期时，$J$ 近似保持。固定 $B_0$ 与磁矩，并缓慢改变镜场尺度 $L$，有 $\omega_b\propto L^{-1}$，从而 $K_{\parallel0}\propto L^{-1}$、$s_{\max}\propto L^{1/2}$。第一不变量约束垂直回旋，第二不变量另约束平行反弹；两者分别对应两个快周期。

**算例。** 初始参数取氘、$K_{\perp0}=K_{\parallel0}=1.00\,\mathrm{keV}$、$L_0=0.500\,\mathrm m$。由 $\omega_{b0}=6.19147\times10^5\,\mathrm{rad\,s^{-1}}$ 得 $J=1.62591\times10^{-21}\,\mathrm{J\,s}$。将 $L$ 缓慢减至 $L_1=L_0(2/3)$，末态 $\omega_b$ 增为 $1.5$ 倍，中央平行动能增至 $1.50\,\mathrm{keV}$，转折距离为 $0.500\sqrt{2/3}=0.408248\,\mathrm m$。代入末态 $2\pi K_\parallel/\omega_b$，仍得同一作用量；增加的 $500\,\mathrm{eV}$ 来自改变磁镜的外部功。[Fitzpatrick，Second Adiabatic Invariant，式 (2.115)–(2.118)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node26.html)。

[返回基础原理](../README.md)
