# 等离子体波与波粒相互作用

本页从均匀无流背景的小振幅理论连接冷/温流体、MHD 与动理学。每个分支均需给出组分、传播方向、偏振、频率排序及闭合；装置可达性和吸收效率另需几何与边界计算。

## 平面波、符号约定与线性化

本页使用 SI 制，物理扰动取复表示的实部：

$$
\delta\mathbf E(\mathbf r,t)
=\operatorname{Re}\!\left[\widetilde{\mathbf E}
e^{i(\mathbf k\cdot\mathbf r-\omega t)}\right],
\qquad \partial_t\mapsto-i\omega,
\qquad \nabla\mapsto i\mathbf k.
$$

波数 $k=2\pi/\lambda$ 的单位为 $\mathrm{m^{-1}}$，角频率 $\omega=2\pi f$ 的单位为 $\mathrm{s^{-1}}$；两式要求相位在一个波长或周期中增加 $2\pi$。如果取实 $\mathbf k$ 和 $\omega=\omega_r+i\gamma$，代回指数得到 $e^{-i\omega_rt}e^{\gamma t}$，因此 $\gamma<0$ 才是时间阻尼。若改为实 $\omega$、沿 $x$ 的复波数 $k=k_r+ik_i$，指数给 $e^{ik_rx}e^{-k_ix}$，故 $k_i>0$ 表示向 $+x$ 的空间衰减。前者属于时间初值问题的频率根，$\gamma$ 的量纲为逆时间；后者属于给定驱动频率的空间边值问题，$k_i$ 的量纲为逆长度。来源：[Fitzpatrick，§5.2，式 (5.1)–(5.5)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node67.html)。

有磁场时取 $\mathbf B_0=B_0\widehat{\mathbf z}$、$B_0>0$，规定带符号回旋角频率与各组分等离子体角频率为

$$
\Omega_s=\frac{q_sB_0}{m_s},\qquad
\omega_{ps}^2=\frac{n_{s0}q_s^2}{\epsilon_0m_s}.
$$

电子的 $q_e=-e$、$\Omega_e<0$，正离子的 $\Omega_i>0$。除特别说明外，温度 $T_s$ 用 K 表示，热能写成 $k_BT_s$；若输入以 eV 表示的数值 $T_{s,\mathrm{eV}}$，须先用 $k_BT_s=T_{s,\mathrm{eV}}\times1.602176634\times10^{-19}\,\mathrm J$ 换算。本文的热速率定义为 $v_{ts}=\sqrt{k_BT_s/m_s}$，与另一些文献的 $\sqrt{2k_BT_s/m_s}$ 相差 $\sqrt2$，代入 Maxwell 分布或 Landau 参数前必须换算。来源：[Fitzpatrick，§5.3，式 (5.16)–(5.19)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)。

线性化指把 $n_s=n_{s0}+n_{s1}$、$\mathbf v_s=\mathbf v_{s1}$ 等代入原方程，只保留一阶小量。例如 $n_{s1}\mathbf E_1$、$\mathbf v_{s1}\times\mathbf B_1$ 是二阶项，但 $\mathbf v_{s1}\times\mathbf B_0$ 是一阶项，必须保留。均匀无流背景使 Fourier 分量彼此独立；有梯度的装置中，局域结果还要求背景变化尺度显著长于局域波长。冷近似忽略的是相应响应中的压力与速度展宽效应，并非声称实际温度等于零；接近共振时，即使温度不高，热效应也可能成为主导修正。来源：[Fitzpatrick，§5.1 Introduction](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node66.html)。

先对齐电荷符号、磁场方向、时间指数和热速率定义，再比较色散与偏振。统一相位因子不改偏振；只共轭一个分量则可改变旋转方向。

### 二阶对流项生成什么频率

以一维速度扰动 $u_1=U\cos(kx-\omega t)$ 为例，时间导数的一阶幅度是 $\omega U$。保留非线性对流项计算，则

$$
u_1\partial_xu_1=-kU^2\cos\vartheta\sin\vartheta
=-\frac{kU^2}{2}\sin2\vartheta,\qquad \vartheta=kx-\omega t.
$$

因此单一基频在二阶产生二倍频、二倍波数的驱动，其相对量级由 $kU/\omega=U/v_{\rm ph}$ 控制。一般两个 Fourier 分量相乘产生 $(k_1+k_2,\omega_1+\omega_2)$，实场还包含差频项。线性化就是在给定幅度排序下舍去这些耦合，再分别求每个分量的响应。

**算例。** 取 $k=20.0\,\mathrm{m^{-1}}$、$U=100\,\mathrm{m\,s^{-1}}$、$\omega=10^5\,\mathrm{rad\,s^{-1}}$。一阶加速度幅度为 $10^7\,\mathrm{m\,s^{-2}}$；二阶对流项幅度为 $kU^2/2=10^5\,\mathrm{m\,s^{-2}}$，占前者 $1\%$，相应排序参数 $kU/\omega=0.0200$。若只研究无力方程 $\partial_tu+u\partial_xu=0$，特征线为 $x=x_0+u_0(x_0)t$；初始正弦波最大负梯度为 $-kU$，特征线首次相交的时间为 $1/(kU)=0.500\,\mathrm{ms}$。这个独立模型展示小非线性项在长时间内的累积。[Fitzpatrick，Plane Waves in Homogeneous Plasmas，线性展开及式 (5.1)–(5.3)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node67.html)。

## 从感应电流到介电张量和色散矩阵

在线性、均匀背景中，用导电率张量表示感应电流：

$$
\widetilde{\mathbf J}
=\boldsymbol\sigma(\omega,\mathbf k)\widetilde{\mathbf E},
\qquad
\boldsymbol\epsilon_r
=\mathbf I+\frac{i\boldsymbol\sigma}{\epsilon_0\omega}.
$$

介电定义来自把感应电流写成极化电流：$\widetilde{\mathbf J}=\partial_t\widetilde{\mathbf P}_{\rm pol}=-i\omega\widetilde{\mathbf P}_{\rm pol}$，所以 $\widetilde{\mathbf D}=\epsilon_0\widetilde{\mathbf E}+\widetilde{\mathbf P}_{\rm pol}=[\epsilon_0\mathbf I+i\boldsymbol\sigma/\omega]\widetilde{\mathbf E}$。这里 $\mathbf P_{\rm pol}$ 是极化密度，与下文冷张量中的标量 $P$ 不同。

$\boldsymbol\epsilon_r$ 是无量纲相对介电张量；绝对介电张量是 $\epsilon_0\boldsymbol\epsilon_r$，量纲分别为 1 与 F/m。这里把等离子体电流全部吸收到材料响应中，外部天线电流则应作为驱动项另列。各向异性意味着电流方向未必与电场方向一致，动力学响应还通常依赖 $\mathbf k$，应保留对应的张量和波数依赖。来源：[MIT 22.611J，第 5 章 §5.1，式 (5.6)–(5.20)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

由 Faraday 方程 $\mathbf k\times\widetilde{\mathbf E}=\omega\widetilde{\mathbf B}$ 消去磁场，得到

$$
\mathbf k\times(\mathbf k\times\widetilde{\mathbf E})
+\frac{\omega^2}{c^2}\boldsymbol\epsilon_r
\widetilde{\mathbf E}=0.
$$

消元的另一半是 Ampère–Maxwell 方程 $i\mathbf k\times\widetilde{\mathbf B}=\mu_0\boldsymbol\sigma\widetilde{\mathbf E}-i\omega\mu_0\epsilon_0\widetilde{\mathbf E}$。把 Faraday 式代入并乘 $\omega/i$，使用 $c^{-2}=\mu_0\epsilon_0$，就得到上式的正号与介电因子；再用 $\mathbf k\times(\mathbf k\times\mathbf E)=\mathbf k(\mathbf k\cdot\mathbf E)-k^2\mathbf E$，得到下面的矩阵。

定义折射率向量 $\mathbf N=c\mathbf k/\omega$，则

$$
\mathbf M\widetilde{\mathbf E}=0,
\qquad
\mathbf M=\boldsymbol\epsilon_r
+\mathbf N\mathbf N-N^2\mathbf I,
\qquad \det\mathbf M=0.
$$

行列式给出允许根，本征矢给偏振。标量介质中，纵向根满足 $\epsilon_r=0$，横向根满足 $N^2=\epsilon_r$；磁化后一般耦合，须回代矩阵求零空间。 [Fitzpatrick，§5.4，式 (5.40)–(5.55)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node69.html)。

还应区分“求自由模”和“求受迫场”：自由模满足齐次方程；给定天线、导体壁和密度剖面时，求的是含源项的边值问题。局域 $\det\mathbf M=0$ 并没有确定天线激发幅度、边界反射或全局功率。一个数值根也要回代矩阵、核查偏振与连续分支，并剔除乘去分母后引入的代数奇点。

设 $\mathbf E_1\simeq-i\mathbf k\phi_1$，由 $\mathbf k\cdot\mathbf D_1=0$ 得 $\mathbf k\cdot\boldsymbol\epsilon_r\cdot\mathbf k=0$。须核对大折射率、近纵向排序及被忽略的横场；偏振耦合区强制删分量可能抹去模转换。

### 复导电率如何变成空间衰减

对无磁冷电子和固定离子，加入给定摩擦率 $\nu>0$。动量方程 $m_e(\nu-i\omega)\widetilde{\mathbf v}=-e\widetilde{\mathbf E}$ 给
$\sigma=\varepsilon_0\omega_{pe}^2/(\nu-i\omega)$。代入介电定义，整理为

$$
\epsilon_r=1-\frac{\omega_{pe}^2}{\omega(\omega+i\nu)},\qquad
N^2=\epsilon_r,\quad k=\frac{\omega}{c}N.
$$

取向 $+x$ 衰减的平方根 $N=N_r+iN_i$，满足 $N_i>0$。把实部、虚部分别比较，得 $N_r^2-N_i^2=\epsilon_r'$、$2N_rN_i=\epsilon_r''$。场因此按 $e^{-k_ix}$ 衰减，而由场平方构成的能流按 $e^{-2k_ix}$ 衰减。选择平方根的符号需要与传播方向及被动耗散条件一致。

**算例。** 令 $\omega=2\omega_{pe}$、$\nu=0.10\omega_{pe}$，则
$\epsilon_r=1-0.25/(1+0.05i)=0.750623+0.0124688i$。开平方得到 $N=0.866415+0.00719564i$。一个真空波长 $\lambda_0=2\pi c/\omega$ 后，场幅比例为 $\exp(-2\pi N_i)=0.955795$，相应能流比例约为 $0.913545$。将复折射率重新平方，恢复原介电值；这是检查时间相位约定和衰减号的直接代数办法。[Fitzpatrick，式 (5.4)–(5.11)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node67.html)；[Collisional Damping，电子摩擦响应](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node83.html)。

## 电子等离子体振荡与 Bohm–Gross 修正

考虑无磁场、均匀、无碰撞电子，离子在电子时间尺度上固定为中和背景。沿 $x$ 的小位移 $\xi$ 产生 $n_{e1}=-n_0\partial_x\xi$，由 Poisson 方程得到对非零波数扰动 $E_1=en_0\xi/\epsilon_0$。电子受力 $m_e\partial_t^2\xi=-eE_1$，所以

$$
\partial_t^2\xi+\omega_{pe}^2\xi=0,
\qquad
\omega_{pe}^2=\frac{n_0e^2}{\epsilon_0m_e}.
$$

恢复力来自微小电荷分离，惯性来自电子质量。冷模型给出 $\omega^2=\omega_{pe}^2$，不依赖 $k$；这时每个 Fourier 分量都以同一频率振荡，群速度为零。电场沿 $\mathbf k$，故该平面纵向模的 $\mathbf B_1=0$；这里“静电波”表示忽略感应磁场的纵向动力学，并非电场不随时间变化。来源：[Fitzpatrick，§5.7 Waves in Unmagnetized Plasmas](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node72.html)。

温电子的平行动量方程多出压力梯度。使用一维无热流压力响应 $p_{e1}=3k_BT_en_{e1}$，与连续性及 Poisson 方程联立，可得

$$
\omega_r^2\simeq\omega_{pe}^2+3k^2v_{te}^2,
\qquad
v_{te}^2=\frac{k_BT_e}{m_e},
\qquad
\lambda_{De}^2=\frac{\epsilon_0k_BT_e}{n_0e^2}.
$$

这就是 Bohm–Gross 色散。系数 $3$ 对应沿传播方向的压力响应，由该方向的无碰撞压力动力学确定。更可靠的解释是：对 Maxwellian 电子的纵向动力学介电函数作高相速度展开，在 $k\lambda_{De}\ll1$、$\omega_r/k\gg v_{te}$ 时得到同样的首个热修正。流体闭合复现了此极限中的实频率，却没有包含共振速度附近的粒子信息。来源：[Fitzpatrick，§7.2，式 (7.23)–(7.29)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node90.html)。

无热流压力矩满足 $D_tp_{xx}+3p_{xx}\partial_xu_x=0$；与连续性联立得 $p_{xx,1}=3k_BT_en_1$。再消去 $n_1,u_1,E_1$，得 Bohm–Gross 实频。系数3属此一维快速压力闭合，适用性由高相速排序核验。

从该近似微分得到 $v_g\simeq3kv_{te}^2/\omega_r$，说明热压力使局部电子振荡能够传播。随着 $k\lambda_{De}$ 增大，相速度逐渐接近热速率，Landau 阻尼和高阶修正的重要性增加，应解完整动力学色散。高频分支上忽略离子的依据是其响应远小于电子响应，体现了该分支的频率排序；研究低频波时必须重新恢复离子运动。

一个不依赖装置参数的检查是取 $k\lambda_{De}=0.1$。由于 $\omega_{pe}\lambda_{De}=v_{te}$，近似式给出 $\omega_r/\omega_{pe}=\sqrt{1.03}\simeq1.0149$、$v_{\mathrm{ph}}/v_{te}\simeq10.149$，热修正较小而相速度显著大于热速率，与所用排序一致。若直接把同一式代到 $k\lambda_{De}=1$，实频率数值仍然能算出，但原来的展开小量已不小，应转向完整色散。这种把计算结果回代假设的检查，应与代数推导同等重视。

严格准中性约化会滤去电荷分离的电子高频振荡。保留哪些方程，取决于目标频率与尺度上的恢复力和惯性；不能一面令电子密度严格等于固定离子密度，一面研究其相对振荡。

### 高相速展开中的三倍热修正从何而来

令 $\sigma_e^2=\Theta_e/m_e$ 为一维热方差。无碰撞、高相速的纵向介电响应可把 $(\omega-kv)^{-1}$ 按 $kv/\omega$ 展开。奇函数积分消失，对分布导数分部积分有
$\int vF_0'dv=-n_0$、
$\int v^3F_0'dv=-3n_0\sigma_e^2$。由此

$$
\epsilon_L\simeq1-\frac{\omega_{pe}^2}{\omega^2}
-\frac{3k^2\sigma_e^2\omega_{pe}^2}{\omega^4}.
$$

设 $\omega^2=\omega_{pe}^2+\delta$，只保留最低阶 $\delta$ 与 $k^2$，得到 $\delta=3k^2\sigma_e^2$。这个系数 3 来自三次速度矩的分部积分，与一维快速压缩的绝热压力响应相对应。再求导可得 $v_g=3k\sigma_e^2/\omega$，和 $v_{\rm ph}=\omega/k$ 有不同的 $k$ 依赖。

**算例。** 取 $k\lambda_{De}=0.150$，利用 $\omega_{pe}\lambda_{De}=\sigma_e$，先得 $\omega/\omega_{pe}=\sqrt{1+3(0.150)^2}=1.03320$。因此 $v_{\rm ph}/\sigma_e=1.03320/0.150=6.88799$，$v_g/\sigma_e=0.450/1.03320=0.435541$。热修正使频率升高约 $3.32\%$；高相速意味着参与共振的粒子位于速度尾部，而群传播远慢于相位推进。代回介电展开式时，剩余项从更高阶 $k^4\lambda_{De}^4$ 开始。[Fitzpatrick，Landau Damping，式 (7.27)–(7.29)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node90.html)。

## 离子声波与电子 Boltzmann 响应

离子声波（ion-acoustic wave）主要由电子压力提供恢复力，由离子提供惯性。先取单价离子、$n_{e0}=n_{i0}=n_0$，无磁场或沿直磁场传播，电子近似等温且平行惯性可忽略。电子力平衡为

$$
0=en_e\partial_x\phi-k_BT_e\partial_xn_e,
\qquad
n_e=n_0\exp\!\left(\frac{e\phi}{k_BT_e}\right),
\qquad
\frac{n_{e1}}{n_0}=\frac{e\phi_1}{k_BT_e}.
$$

正电势吸引电子，因此指数为正号。该 Boltzmann 响应采用沿扰动方向的快速电子调整；跨磁场几何需重新求电子响应。线性式还要求 $|e\phi_1|\ll k_BT_e$。来源：[MIT 22.611J，第 5 章 §5.4.2 Including the Ion Response、§5.9.8](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

冷离子的连续性和动量方程给出

$$
-i\omega n_{i1}+ikn_0u_{i1}=0,
\qquad
-i\omega m_i u_{i1}=-ike\phi_1,
\qquad
\frac{n_{i1}}{n_0}=\frac{k^2e\phi_1}{m_i\omega^2}.
$$

再代入 $k^2\phi_1=e(n_{i1}-n_{e1})/\epsilon_0$，得到

$$
\omega_r^2=\frac{k^2c_s^2}{1+k^2\lambda_{De}^2},
\qquad c_s^2=\frac{k_BT_e}{m_i}.
$$

长波极限 $k\lambda_{De}\ll1$ 下近似准中性，$\omega_r\simeq kc_s$；有限 Debye 长度使电子屏蔽不完全，产生分母修正。保留压力闭合 $p_{i1}=\gamma_i k_BT_i n_{i1}$ 时，相应流体结果为 $\omega^2=k^2\gamma_i k_BT_i/m_i+k^2c_s^2/(1+k^2\lambda_{De}^2)$，其长波声速平方为 $(k_BT_e+\gamma_i k_BT_i)/m_i$。这只是闭合模型的实频率，不提供弱阻尼保证。

有限离子压力给 $(\omega^2-k^2\gamma_i k_BT_i/m_i)n_{i1}=n_0k^2e\phi_1/m_i$；电子与 Poisson 响应给 $n_{i1}=n_0(e\phi_1/k_BT_e)(1+k^2\lambda_{De}^2)$。消去振幅即得温离子修正。

在无漂移 Maxwellian、弱碰撞的经典情形，弱阻尼要求相速度处在 $v_{ti}\ll\omega_r/k\ll v_{te}$ 的窗口内。长波声速代入后，左侧条件要求 $T_e\gg T_i$；当 $T_e$ 与 $T_i$ 接近时，离子共振粒子数量增加，离子 Landau 阻尼通常显著。模式的寿命由动力学阻尼与驱动的共同作用决定。多离子组分、非 Maxwellian、强碰撞、漂移等情形需要重新分析。来源：[Fitzpatrick，§7.5，式 (7.49)–(7.52) 及温度条件讨论](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node93.html)。

准中性与完全没有电场也不同。长波极限中 $n_{i1}$ 与 $n_{e1}$ 的主阶相等，微小差值仍通过 Poisson 方程产生足以维持共同运动的电场；若一开始严格令差值为零并同时强加有限波数 Poisson 方程，反而会错误地消去声波的恢复机制。对有限 $T_i$，冷离子公式形式上在大波数趋近 $\omega_{pi}$，但相速度随之下降，最终可能违反 $v_{\mathrm{ph}}\gg v_{ti}$。这说明一个极限可以是流体公式的数学极限，却未必是原始物理排序允许达到的实验极限。

### 保留 Poisson 方程得到有限 Debye 修正

取冷单价离子、等温 Boltzmann 电子，令扰动按 $e^{i(kx-\omega t)}$ 变化。离子连续性与动量方程给
$\widetilde n_i=n_0k\widetilde u_i/\omega$、
$\widetilde u_i=ek\widetilde\phi/(m_i\omega)$；电子响应为 $\widetilde n_e=n_0e\widetilde\phi/\Theta_e$。代入 $k^2\widetilde\phi=e(\widetilde n_i-\widetilde n_e)/\varepsilon_0$，消去各振幅得到

$$
\omega^2=\frac{k^2c_s^2}{1+k^2\lambda_{De}^2},\quad
c_s^2=\frac{\Theta_e}{m_i},\quad
\frac{\widetilde n_e}{\widetilde n_i}=\frac1{1+k^2\lambda_{De}^2}.
$$

长波时电子、离子密度起伏接近；波长缩短后，有限电荷分离削弱等温声学近似下的恢复关系。求导得 $v_g=c_s(1+k^2\lambda_{De}^2)^{-3/2}$。冷离子与快速电子响应对应 $\sqrt{\Theta_i/m_i}\ll\omega/k\ll\sqrt{\Theta_e/m_e}$ 的排序。

**算例。** 设 $k\lambda_{De}=0.500$、$c_s=10^5\,\mathrm{m\,s^{-1}}$。相速度为 $8.94427\times10^4\,\mathrm{m\,s^{-1}}$，群速度为 $7.15542\times10^4\,\mathrm{m\,s^{-1}}$。离子密度扰动若为背景的 $1.00\%$，电子扰动为 $0.800\%$，净电荷扰动为背景电荷尺度的 $0.200\%$。三种响应由同一线性方程组产生，可同时代回连续性与 Poisson 方程检查。[Fitzpatrick，Ion Acoustic Waves，式 (7.49)–(7.52)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node93.html)。

## 非磁化横电磁波与密度截止

![冷非磁化横波的色散、相速度与群速度](/assets/diagrams/basic-waves.svg)

*冷非磁化横波的色散、相速度与群速度。曲线与示意均按本条所列模型生成。*

在无磁场冷等离子体中，各组分满足 $-i\omega m_s\mathbf v_{s1}=q_s\mathbf E_1$，因而

$$
\boldsymbol\sigma
=\frac{i\epsilon_0}{\omega}\sum_s\omega_{ps}^2\mathbf I,
\qquad
\epsilon_r=1-\frac{\sum_s\omega_{ps}^2}{\omega^2}.
$$

对横向电场 $\mathbf k\cdot\mathbf E_1=0$，色散矩阵化为 $N^2=\epsilon_r$，得到

$$
\omega^2=c^2k^2+\sum_s\omega_{ps}^2
\simeq c^2k^2+\omega_{pe}^2.
$$

最后一步用于电子高频响应占主导的普通电子—离子等离子体；第一式才保留全部冷组分。这个波同时包含电场、磁场和粒子振荡能。与同一等离子体的纵向 Langmuir 模相比，横向根来自 Ampère 方程中的电流及位移电流，纵向根来自电荷分离。来源：[Fitzpatrick，§5.7，横向与纵向分支](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node72.html)。

固定驱动角频率时，电子近似给出的临界密度为

$$
n_{\mathrm{crit}}=\frac{\epsilon_0m_e\omega^2}{e^2}.
$$

若 $n_e<n_{\mathrm{crit}}$，均匀无耗散介质中有实波数；若 $n_e>n_{\mathrm{crit}}$，则

$$
k=i\kappa,\qquad
\kappa=\frac{\sqrt{\omega_{pe}^2-\omega^2}}{c},
\qquad |E(x)|\propto e^{-\kappa x}
$$

是衰逝解。$1/\kappa$ 是这一理想模型的幅度穿透长度，不应直接替代碰撞金属中的趋肤深度。衰逝描述空间振幅变化，局部热耗散则由平均场功确定：在无耗散半无限介质界面，入射功率可主要被反射；有限厚度层还可能发生隧穿，须由两端边界匹配决定。来源：[Fitzpatrick，§6.3 Cutoffs](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node80.html)。

实际磁约束等离子体通常有强磁场，临界密度截止适用于指定的非磁化横向分支或相应 O 模近似，X 模、低频磁化分支和模转换路径应按各自色散计算。ICRF 天线耦合需求磁化介质与边界的完整电磁响应。计算密度截止前先确认使用的是 $f$ 还是 $\omega$，否则临界密度会误差一个 $4\pi^2$ 因子。

$n_{\rm crit}\propto f^2$：频率加倍，临界密度变四倍。传播、反射和沉积分别核算；无耗散介质有感应电流，也不意味着净热吸收。空间衰逝长度与功率沉积长度须分开。

### 截止以下的空间解和衰减长度

无磁、冷、无碰撞介质中的横波满足 $c^2k^2=\omega^2-\omega_{pe}^2$。若给定实驱动频率低于等离子体频率，令 $k=i\kappa$，选择半无限介质内衰减的解。场方程变为

$$
\frac{d^2\widetilde E}{dx^2}-\kappa^2\widetilde E=0,\quad
\kappa=\frac{\sqrt{\omega_{pe}^2-\omega^2}}c,\quad
\widetilde E(x)=E(0)e^{-\kappa x}.
$$

一般解还包含增长的 $e^{+\kappa x}$，半无限被动区域的远处边界条件将其系数置零。有限厚层则由两侧边界共同决定两个系数，可能发生隧穿。纯虚波数本身给空间衰减，均匀无碰撞介质中的局部周期平均吸收为零；在界面问题中能量账通过反射和透射闭合。

**算例。** 给 $n_e=2.00\times10^{18}\,\mathrm{m^{-3}}$，先算 $f_{pe}=12.6977\,\mathrm{GHz}$。驱动频率 $f=10.0\,\mathrm{GHz}$，使用角频率 $\omega=2\pi f$ 代入，得到 $\kappa^{-1}=6.09746\,\mathrm{mm}$。距界面 $1.00\,\mathrm{cm}$ 时，半无限解的幅度比为 $\exp[-0.010/0.00609746]=0.193975$。接近截止时 $\kappa$ 变小，衰减长度增大；远低于截止时长度趋近 $c/\omega_{pe}$。这说明实际趋肤尺度应由指定频率的色散根求得。[MIT 第 5 章 §5.2.1–5.2.2，式 (5.53)–(5.57)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

## 冷磁化响应、圆偏振与 whistler 分支

在均匀、无流、无碰撞的冷多组分等离子体中，由

$$
-i\omega m_s\mathbf v_{s1}
=q_s(\mathbf E_1+\mathbf v_{s1}\times\mathbf B_0)
$$

逐组分求速度并相加，可得

$$
\boldsymbol\epsilon_r=
\begin{pmatrix}S&-iD&0\\iD&S&0\\0&0&P\end{pmatrix},
\quad
R=1-\sum_s\frac{\omega_{ps}^2}{\omega(\omega+\Omega_s)},
\quad
L=1-\sum_s\frac{\omega_{ps}^2}{\omega(\omega-\Omega_s)},
$$

$$
S=\frac{R+L}{2},\qquad D=\frac{R-L}{2},\qquad
P=1-\sum_s\frac{\omega_{ps}^2}{\omega^2}.
$$

中间求逆可用圆分量完成。定义 $v_{s\pm}=v_{sx}\pm iv_{sy}$、$E_\pm=E_x\pm iE_y$，两条横向动量方程相加、相减后分别为 $-i(\omega-\Omega_s)v_{s+}=(q_s/m_s)E_+$、$-i(\omega+\Omega_s)v_{s-}=(q_s/m_s)E_-$。因此 $J_\pm=i\epsilon_0\sum_s\omega_{ps}^2E_\pm/(\omega\mp\Omega_s)$；代入介电定义得到圆基底中的 $L$、$R$，沿场方程直接给 $P$。再变回 $x,y$ 基底即得 $S=(R+L)/2$、$D=(R-L)/2$ 及非对角元 $\mp iD$。对于 $(1,i,0)$，只有 $E_-$ 非零，故它对应 $R$。

这里 $\Omega_e$ 必须取负值。$R,L$ 的名称只在给定时间 convention、坐标和偏振定义后才有确定意义；直接抄写另一资料的 $\pm\Omega_s$ 而不检查时间因子，可能把电子和离子的共振分支对调。来源：[Fitzpatrick，§5.3，式 (5.31)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)。

取 $\mathbf k=k\widehat{\mathbf z}$、$k>0$，两条横向本征模为

$$
N^2=R,\quad \widetilde{\mathbf E}\propto(1,i,0);
\qquad
N^2=L,\quad \widetilde{\mathbf E}\propto(1,-i,0).
$$

为避免观察方向的歧义，直接看 $z=0$：前者实电场为 $(\cos\omega t,\sin\omega t,0)$，后者为 $(\cos\omega t,-\sin\omega t,0)$。这分别与电子、正离子的自由回旋方向一致。因此 $R$ 的电子分母在 $\omega=|\Omega_e|$ 消失，$L$ 的正离子分母在 $\omega=\Omega_i$ 消失。取反向传播时，代数分支仍可相对于固定 $\mathbf B_0$ 定义，但相对于传播方向的“左右旋”叫法需要重新说明。来源：[Fitzpatrick，§5.5，式 (5.56)–(5.60)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node70.html)。

对单价电子—离子等离子体，在 $\Omega_i\ll\omega\ll|\Omega_e|$ 且 $N^2\gg1$ 的平行传播区间，$R$ 分支给出

$$
N^2\simeq\frac{\omega_{pe}^2}{\omega|\Omega_e|},
\qquad
\omega\simeq\frac{|\Omega_e|c^2}{\omega_{pe}^2}k_\parallel^2.
$$

这就是常用 whistler 近似，强色散来自电子受磁场约束的电流响应。应用到螺旋波放电时，有限半径、斜传播、边界条件及碰撞会改变模式。此近似还需远离回旋共振，共振层吸收则需恢复耗散或动力学响应。来源：[Fitzpatrick，§5.9，式 (5.90)–(5.94) 及 whistler 频段](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node74.html)。

写 $\Omega_{ce}=|\Omega_e|$，电子项近似为 $\omega_{pe}^2/(\omega\Omega_{ce})$；仅当 $\Omega_i/\omega\ll1$、$\omega/\Omega_{ce}\ll1$ 且该项远大于1，才可忽略离子与真空项，得到 whistler 二次色散。

冷张量有两个容易实施的极限检查。若令所有 $\omega_{ps}$ 趋于零，$R,L,S,P$ 都趋于一而 $D\to0$，恢复真空 Maxwell 方程；若令 $B_0\to0$，则 $R=L=P$、$D=0$，恢复无磁场标量响应。无磁极限应从完整冷等离子体公式取出；whistler 展开使用 $\omega\ll|\Omega_e|$ 的独立排序。类似地，多离子组分各自贡献一个带其电荷和质量的响应项，各自的回旋极点需分别保留。

### 电子 Hall 响应的二次色散

对平行传播的电子回旋同旋分支，令 $\Omega_{ce}=eB/m_e>0$。在 $\Omega_i\ll\omega\ll\Omega_{ce}$、离子响应较小且折射率平方远大于一的排序下，冷等离子体关系化为
$N^2\simeq\omega_{pe}^2/(\omega\Omega_{ce})$。将 $N=ck/\omega$ 代入并整理，得到

$$
\omega\simeq\Omega_{ce}d_e^2k^2,\quad
v_{\rm ph}\simeq\Omega_{ce}d_e^2k,\quad
v_g\simeq2\Omega_{ce}d_e^2k,\qquad d_e=\frac c{\omega_{pe}}.
$$

群速度为相速度的两倍。固定传播长度时，低频部分的群速度较小，脉冲中的不同频率依次到达，这给 whistler 的频率随时间变化提供了基本解释。将 $\omega$ 提升至接近回旋频率时，应回到原冷色散式保留分母中的 $\Omega_{ce}-\omega$。

**算例。** 取 $B=0.200\,\mathrm T$、$n_e=10^{18}\,\mathrm{m^{-3}}$，得到 $d_e=5.31409\,\mathrm{mm}$。选择 $kd_e=0.100$，则 $k=18.8179\,\mathrm{m^{-1}}$，频率为 $\omega=0.0100\Omega_{ce}=3.51764\times10^8\,\mathrm{rad\,s^{-1}}$，相速度约 $1.86931\times10^7\,\mathrm{m\,s^{-1}}$，群速度约 $3.73861\times10^7\,\mathrm{m\,s^{-1}}$。氘离子回旋频率为 $9.58359\times10^6\,\mathrm{rad\,s^{-1}}$，给出 $\omega/\Omega_D\approx36.7$；保留完整冷响应可进一步量化有限离子项的修正。[Fitzpatrick，Parallel Wave Propagation，whistler 分支](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node74.html)；[MIT 第 5 章平行传播及 whistler 群延迟，式 (5.94)–(5.98)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

## 垂直传播的 O 模、X 模与上混杂频率

令 $\mathbf k=k\widehat{\mathbf x}\perp\mathbf B_0$，冷色散矩阵分成 $z$ 分量和 $x,y$ 子块。普通模（ordinary / O mode）满足

$$
\widetilde{\mathbf E}\parallel\mathbf B_0,
\qquad N^2=P,
\qquad \omega^2\simeq\omega_{pe}^2+c^2k^2.
$$

电场与背景磁场平行，粒子一阶运动不受 $\mathbf v_1\times\mathbf B_0$ 的作用，因此在上述冷、高频近似内与非磁化横波有相同色散。这里电场虽然“平行磁场”，仍然“垂直波矢”，所以它是横向电磁模。两个“平行”必须明确各自参照物。来源：[Fitzpatrick，§5.10，式 (5.97)–(5.98)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node75.html)。

非寻常模（extraordinary / X mode）位于 $x,y$ 子空间，满足

$$
\det\begin{pmatrix}S&-iD\\iD&S-N^2\end{pmatrix}
=S(S-N^2)-D^2=0,
\qquad
N^2=\frac{RL}{S}.
$$

只要相应分母非零，$R=0$ 或 $L=0$ 给出 X 模截止；$S=0$ 且 $RL\ne0$ 给出该冷分支的共振。X 模一般同时含 $E_x$ 和 $E_y$，其偏振由两个分量的耦合决定。由第一行 $SE_x-iDE_y=0$ 可知，在 $S\to0$ 而 $D$ 有限时，归一化偏振趋向以 $E_x$ 为主；这提示热效应和短波动力学的重要性，此处应进一步求热等离子体响应。来源：[Fitzpatrick，§5.4，式 (5.43)、(5.54)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node69.html)。

若在电子频率范围忽略离子响应，

$$
S\simeq1-\frac{\omega_{pe}^2}{\omega^2-\Omega_e^2},
\qquad
\omega_{\mathrm{UH}}^2\simeq\omega_{pe}^2+\Omega_e^2.
$$

上混杂频率（upper hybrid）结合了电子电荷分离恢复力和磁化运动，由两种回复作用共同决定。该简单式限于这里的冷、高频、垂直传播近似；多组分完整 $S=0$ 还含离子项与其他根。接近 $N\to\infty$ 时，冷模型暗示波长越来越短，有限 Larmor 半径和非局域响应随之增强。上混杂层、电子 Bernstein 波和 O–X–B 转换之间存在联系，但转换效率须解带梯度的热等离子体问题，需要场匹配和功率通量计算。来源：[Fitzpatrick，§5.10，式 (5.99)–(5.103)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node75.html)。

极点还须核查分子：若 $RL$ 与 $S$ 同时为零，回到原矩阵取极限。无磁场时 $R=L=S$，故 $RL/S=S$，不产生额外共振。O/X 的简单偏振定义限于垂直传播；斜入射应跟踪本征矢。

### 由二维行列式得到 X 模并计算传播区

取 $\mathbf k=k\hat{\mathbf x}$、$\mathbf B_0=B_0\hat{\mathbf z}$。横向冷色散矩阵的 $x,y$ 块为
$\left(\begin{smallmatrix}S&-iD\\iD&S-N^2\end{smallmatrix}\right)$，非零解要求 $S(S-N^2)-D^2=0$。用 $S^2-D^2=RL$，得到 $N_X^2=RL/S$；独立的 $z$ 分量给 $N_O^2=P$。固定离子时

$$
R=1-\frac{\omega_{pe}^2}{\omega(\omega-\Omega_{ce})},\quad
L=1-\frac{\omega_{pe}^2}{\omega(\omega+\Omega_{ce})},\quad
S=1-\frac{\omega_{pe}^2}{\omega^2-\Omega_{ce}^2}.
$$

令 $S=0$ 得上混杂频率 $\sqrt{\Omega_{ce}^2+\omega_{pe}^2}$；令 $R$ 或 $L$ 为零得到两个正截止频率。计算传播窗口需要同时查看这些根的顺序。

截止根的显式代数是 $R=0\Rightarrow\omega^2-\Omega_{ce}\omega-\omega_{pe}^2=0$，$L=0\Rightarrow\omega^2+\Omega_{ce}\omega-\omega_{pe}^2=0$，所以两个正根为 $[\sqrt{\Omega_{ce}^2+4\omega_{pe}^2}\pm\Omega_{ce}]/2$。把 $\omega_{pe}/\Omega_{ce}=0.600$ 代入，便给下述 $[\sqrt{2.44}\pm1]/2$；上混杂根来自 $\omega^2-\Omega_{ce}^2=\omega_{pe}^2$。

**算例。** 取 $\omega_{pe}=0.600\Omega_{ce}$，考察 $\omega=0.500\Omega_{ce}$。代入得 $R=2.44$、$L=0.52$、$S=1.48$，所以 $N_X^2=0.857297>0$，而 $N_O^2=1-0.36/0.25=-0.44$。同一频率、密度下，X 分支有实波数，O 分支为空间衰减解。两截止点为 $0.281025\Omega_{ce}$、$1.281025\Omega_{ce}$，上混杂点为 $1.16619\Omega_{ce}$；它们共同确定 X 模频谱的分段结构。[Fitzpatrick，冷介电张量式 (5.27)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)；[Perpendicular Wave Propagation](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node75.html)。

## 理想 MHD 的剪切 Alfvén 波与快慢磁声波

考虑均匀、静止、标量压力的理想 MHD 平衡，采用绝热闭合 $p_1=c_M^2\rho_1$，其中

$$
v_A^2=\frac{B_0^2}{\mu_0\rho_0},
\qquad c_M^2=\frac{\Gamma p_0}{\rho_0}.
$$

这里 $\rho_0$ 是总质量密度，$p_0$ 是总热压力，$\Gamma$ 是该闭合的绝热指数；$c_M$ 不应直接与前述冷离子、等温电子模型的 $c_s$ 混为一谈。由连续性、动量、理想感应方程线性化，得到的色散式可分解为

$$
(\omega^2-k_\parallel^2v_A^2)
\left[\omega^4-k^2(v_A^2+c_M^2)\omega^2
+k^2k_\parallel^2v_A^2c_M^2\right]=0.
$$

第一因子给出剪切 Alfvén 波。其速度扰动垂直于 $\mathbf k$ 与 $\mathbf B_0$ 张成的平面，在该均匀模型中 $\mathbf k\cdot\mathbf v_1=0$，所以 $\rho_1=p_1=0$。恢复力是弯曲磁力线的磁张力；单位长度上的惯性由等离子体质量提供。波频率 $\omega=\pm k_\parallel v_A$ 显示完全垂直传播时这一分支退化为零频，应保留平行波数。来源：[Fitzpatrick，§5.8 Low-Frequency Wave Propagation](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node73.html)。

第二因子给出快、慢磁声波。设 $\cos\theta=k_\parallel/k$，则

$$
v_{f,s}^2=\frac12\left[v_A^2+c_M^2
\pm\sqrt{(v_A^2+c_M^2)^2-4v_A^2c_M^2\cos^2\theta}\right],
\qquad \omega^2=k^2v_{f,s}^2.
$$

正号为快分支，负号为慢分支。一般斜传播时它们包含密度、压力和磁压扰动。完全垂直传播给出 $v_f^2=v_A^2+c_M^2$、$v_s=0$；完全平行传播的两个速度是 $v_A$ 与 $c_M$，谁被称为“快”取决于两者大小。这个极限检查能防止把声波分支和磁分支永久贴上错误标签。来源：[Fitzpatrick，§8.4，式 (8.22)–(8.45)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node107.html)。

本条采用非相对论理想 MHD，要求 $v_A,c_M\ll c$，使忽略位移电流及相对论惯性与所用波速公式相容。它适合低频、长尺度描述，通常要求 $\omega\ll|\Omega_i|$、$k\rho_i\ll1$，并且 Hall、电子惯性、电阻与相关动力学修正可忽略；例如 $kd_i\ll1$、$d_i=c/\omega_{pi}$ 是常用的 Hall 小量条件之一。标量绝热压力闭合还需单独论证，尤其碰撞很弱时，压力各向异性、平行热流和 Landau 阻尼仍由各自排序决定。ICRF 频段所谓 fast / slow 分支须从其冷/热介电色散识别，共振层使用保留回旋响应的色散。来源：[MIT 22.611J，第 5 章 §5.6 Simple Example of MHD Dynamics](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

由 $\beta=2\mu_0p_0/B_0^2$ 得 $c_M^2/v_A^2=\Gamma\beta/2$。以上是均匀局域模；环形磁剪切、曲率和剖面造成的连续谱、耦合及全局本征模须另解平衡与边界。

### 对压缩偏振解一个二阶本征问题

令 $\mathbf k$ 位于 $x,z$ 平面，磁场沿 $z$，传播角为 $\theta$。把线性连续性、压力和感应方程消去后，$x,z$ 两个速度分量满足本征问题
$\omega^2\mathbf u=k^2\mathsf A\mathbf u$，其中

$$
\mathsf A=
\begin{pmatrix}
v_A^2+c_M^2\sin^2\theta&c_M^2\sin\theta\cos\theta\\
c_M^2\sin\theta\cos\theta&c_M^2\cos^2\theta
\end{pmatrix}.
$$

消元过程可从三条 Fourier 方程核对：$\rho_1=\rho_0\mathbf k\cdot\mathbf u/\omega$、$p_1=c_M^2\rho_1$，以及 $\mathbf B_1=[\mathbf B_0(\mathbf k\cdot\mathbf u)-(\mathbf k\cdot\mathbf B_0)\mathbf u]/\omega$。将它们代入 $\omega\rho_0\mathbf u=\mathbf k p_1-(\mathbf k\times\mathbf B_1)\times\mathbf B_0/\mu_0$，$x,z$ 分量分别给

$$
\omega^2u_x=(v_A^2k^2+c_M^2k_x^2)u_x+c_M^2k_xk_zu_z,\qquad
\omega^2u_z=c_M^2k_xk_zu_x+c_M^2k_z^2u_z.
$$

令 $k_x=k\sin\theta$、$k_z=k\cos\theta$ 后除以 $k^2$ 即得矩阵。独立 $y$ 分量满足 $\omega^2u_y=v_A^2k_z^2u_y$，与该二阶行列式相乘就是前述完整三模色散；$c_M^2=\Gamma p_0/\rho_0$ 来自 $\delta(p\rho^{-\Gamma})=0$，$v_A^2$ 则是张力系数除以惯性密度。

迹为 $v_A^2+c_M^2$，行列式为 $v_A^2c_M^2\cos^2\theta$。因此两个相速度平方满足
$V^4-(v_A^2+c_M^2)V^2+v_A^2c_M^2\cos^2\theta=0$。独立的 $y$ 偏振给 $V_A=v_A\cos\theta$。利用迹和行列式，可在开平方前先核对快慢根之和与之积。

**算例。** 给定 $v_A=2.00\times10^6\,\mathrm{m\,s^{-1}}$、$c_M=1.00\times10^6\,\mathrm{m\,s^{-1}}$、$\theta=45^\circ$。用 $10^{12}\,\mathrm{m^2\,s^{-2}}$ 作矩阵单位，$\mathsf A=\left(\begin{smallmatrix}4.5&0.5\\0.5&0.5\end{smallmatrix}\right)$，其本征值为 $(5\pm\sqrt{17})/2$。开平方得到快波 $2.13578\times10^6$、慢波 $6.62153\times10^5$、剪切 Alfvén 波 $1.41421\times10^6\,\mathrm{m\,s^{-1}}$。前两者速度平方之积为 $2.00\times10^{24}\,\mathrm{m^4\,s^{-4}}$，符合行列式。[Fitzpatrick，MHD Waves，式 (8.30)–(8.45)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node107.html)。

## 相速度、群速度、截止与共振的区别

相速度描述固定相位的移动；在一个光滑、弱阻尼色散分支上，群速度描述窄带波包包络的一阶传播：

$$
\mathbf v_{\mathrm{ph}}=\frac{\omega_r}{k}\widehat{\mathbf k},
\qquad
\mathbf v_g=\nabla_{\mathbf k}\omega_r.
$$

第一式只是沿波法线选取的相位速度。在各向异性介质中，$\mathbf v_g$ 未必平行 $\mathbf k$；波前法向与能量传播方向需分别求出。在强阻尼、宽频、强非均匀或分支混合区，应直接分析因果脉冲响应与信号前沿。来源：[Fitzpatrick，§6.7 Pulse Propagation](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node84.html)。

例如无磁场冷横波有

$$
v_{\mathrm{ph}}=\frac{\omega}{k}>c,
\qquad
v_g=\frac{c^2k}{\omega}<c,
\qquad v_{\mathrm{ph}}v_g=c^2.
$$

这个乘积关系仅属于此条色散，其他色散有各自的导数关系。相速度超过 $c$ 没有意味着能量或信息超光速，因为单一等相位面不携带独立新信息。对 Bohm–Gross 波和 whistler 波按各自色散求导，会得到不同关系；信号传播还涉及频率导数和因果响应。

邻近 Fourier 模的拍包络相位为 $\Delta k\,x-\Delta\omega\,t$，窄带极限给 $v_g=d\omega/dk$。二阶色散使包络展宽；跨多分支频谱还须分别传播各自偏振。

在固定频率、固定传播方向的简单局域冷模型里，截止通常指一条分支 $N^2\to0$，共振通常指 $N^2\to\infty$。二者一端是长波极限，另一端是短波极限，分别对应不同的波数极限。在分层介质中，沿界面波数守恒，实际法向转折点可以是 $k_x^2\to0$ 而总 $k$ 非零，斜入射的转折条件应从守恒切向波数下的法向色散求出。来源：[Fitzpatrick，§5.6 Cutoff and Resonance](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node71.html)。

用局域色散拼接射线或 WKB 解，还要求波数随位置变化足够缓慢，例如一维条件 $|\partial_x k|/|k|^2\ll1$。截止及共振附近常会破坏这种近似，需使用局域连接解或全波边值解。反射是能量返回原侧，模转换是能量转入另一传播分支，吸收则要求场对粒子作净功；这三者可同时出现，分别按功率通量与粒子作功核算。冷奇点可以指示必须加入的新物理，却不自动给出有限吸收率。来源：[Fitzpatrick，§6.2 WKB Solutions](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node79.html)；[§6.4 Resonances，式 (6.29) 中正则化与边界条件](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node81.html)。

这一小参数来自把 $E=A(x)e^{i\int^xkdx'}$ 代入标量波方程 $E''+k^2E=0$：剩余项为 $A''+2ikA'+ik'A=0$。最低阶忽略 $A''$ 得 $A\propto k^{-1/2}$，而一个局域波长内 $k$ 的相对变化量正比于 $|k'|/|k|^2$；它和更高导数必须足够小才支持渐近展开。矢量各向异性问题还需另外检查偏振变化与分支间耦合。

### 用窄带 Gaussian 波包显示群速度和展宽

令一维波包的谱振幅为 $\exp[-(k-k_0)^2/(2\Delta k^2)]$。在中心波数附近展开
$\omega(k)=\omega_0+v_g\delta k+\tfrac12\omega''\delta k^2$，代入 Fourier 积分后，线性项把包络中心平移到 $x=v_gt$，二次项给出宽度变化：

$$
|A(x,t)|\propto
[1+(\omega''\Delta k^2t)^2]^{-1/4}
\exp\!\left[-\frac{\Delta k^2(x-v_gt)^2}
{2[1+(\omega''\Delta k^2t)^2]}\right].
$$

相位脊仍由 $\omega_0/k_0$ 推进；包络位置由一阶色散导数决定，包络展宽由二阶导数决定。这来自带复系数的 Gaussian 积分，适用于足够窄的谱带和小的三阶色散累计。

将二阶色散代入 Fourier 积分，用 $\int e^{-aq^2+bq}dq=\sqrt{\pi/a}e^{b^2/(4a)}$（$\Re a>0$）配方，得到 $(1+i\omega^{\prime\prime}\Delta k^2t)^{-1/2}$ 与复宽度。取模即得峰值和展宽；各波数只变相位，范数保持。

**算例。** 冷无磁横波取 $ck_0/\omega_{pe}=0.750$，故 $\omega_0=1.25\omega_{pe}$。有 $v_{\rm ph}=(1.25/0.75)c=1.66667c$，$v_g=c^2k_0/\omega_0=0.600c$；二阶导数为
$\omega''=c^2\omega_{pe}^2/\omega_0^3=0.512c^2/\omega_{pe}$。若 $\Delta k=0.0200\omega_{pe}/c$，包络宽度增加到初值 $\sqrt2$ 倍所需时间是 $1/(\omega''\Delta k^2)=4882.81/\omega_{pe}$。此时峰值包络幅度降为 $2^{-1/4}$，空间积分的波包范数保持；快相位推进和较慢包络输运自然同时出现。[MIT 第 5 章 §5.1 的色散、群速度及 §5.2 的横波关系](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

## Landau 共振与无碰撞阻尼

对均匀、无磁场、一维纵向扰动，粒子沿未扰动轨道 $x=x_0+vt$ 看到的波相位变化率为 $kv-\omega_r$。当

$$
\omega_r-kv=0
$$

时，粒子可在较长时间内保持与电场相近的相位，因此发生显著波粒能量交换。这是 Landau 共振的运动学条件。它本身只挑选共振速度，不决定净交换方向；方向还取决于平衡分布和模的能量性质。来源：[Fitzpatrick，§7.3 Physics of Landau Damping](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node91.html)。

为明确符号，取 $k>0$、$\omega_r>0$，令 $F_{s0}(v)$ 是积分掉横向速度后的分布，满足 $\int F_{s0}\,dv=n_{s0}$。线性 Vlasov–Poisson 方程给出

$$
\epsilon_L(\omega,k)
=1-\sum_s\frac{q_s^2}{\epsilon_0m_sk^2}
\int_{\mathcal L}
\frac{\partial_vF_{s0}(v)}{v-\omega/k}\,dv,
\qquad \epsilon_L=0.
$$

中间响应由 $(-i\omega+ikv)F_{s1}-ik(q_s\phi_1/m_s)F_{s0}'=0$ 给 $F_{s1}=(q_s\phi_1/m_s)F_{s0}'/(v-\omega/k)$。将它代入 $\epsilon_0k^2\phi_1=\sum_sq_s\int F_{s1}dv$，除去非零 $\phi_1$，即得所列介电函数。对因果边界 $\omega\to\omega_r+i0^+$，$1/(v-\omega_r/k-i0^+)=\mathcal P[1/(v-\omega_r/k)]+i\pi\delta(v-\omega_r/k)$，所以共振虚部带下式的负号；$\mathcal P$ 表示主值积分。

积分路径 $\mathcal L$ 按因果初值问题规定：从 $\operatorname{Im}\omega>0$ 的良定义积分作解析延拓，极点绕行方向由该解析延拓固定。弱阻尼展开 $\omega=\omega_r+i\gamma$ 后，

$$
\gamma\simeq-
\frac{\epsilon_{L,I}(\omega_r,k)}
{\partial_\omega\epsilon_{L,R}(\omega_r,k)},
\qquad
\epsilon_{L,I}=-\sum_s\frac{\pi q_s^2}{\epsilon_0m_sk^2}
\left.\partial_vF_{s0}\right|_{v=\omega_r/k}.
$$

对于通常的正频电子 Langmuir 分支，$\partial_\omega\epsilon_{L,R}>0$，无漂移 Maxwellian 在正共振速度处斜率为负，因此 $\gamma<0$。若存在束流或速度空间凸起，斜率可改变并提供自由能；此时要重新求整个色散，结合实频、偏振与各组分共振贡献判断稳定性。来源：[Fitzpatrick，§7.2，式 (7.23)–(7.31)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node90.html)。

Maxwellian 计算常使用 $\zeta_s=\omega/(\sqrt2kv_{ts})$ 和等离子体色散函数 $Z(\zeta)$；这里的 $\sqrt2$ 来自本页热速率 convention。即使场振幅衰减，理想 Vlasov 演化的总能量仍守恒：扰动转入越来越精细的速度空间结构，即相混合（phase mixing）。这一过程使宏观场能进入速度空间结构；不可逆热化由碰撞、粗粒化及后续分布演化描述。大振幅粒子俘获或强阻尼下，以上线性小 $\gamma$ 公式也不再充分。来源：[Fitzpatrick，§7.4 Plasma Dispersion Function](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node92.html)；[§7.2，初值解与连续谱讨论](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node90.html)。

局部幅值降低也可来自波包离开、几何扩散、边界、碰撞或数值耗散。识别 Landau 机制须同时检查共振区分布、场—粒子能量交换和边界通量，并分别检验空间、速度分辨率以排除人工复现。

### 从分布斜率求弱阻尼率

对无磁、固定离子的 Maxwellian 电子，取 $k>0$，令 $\sigma_e^2=\Theta_e/m_e$。Landau 处方给介电函数的共振虚部
$\epsilon_i=-\pi\omega_{pe}^2F_0'(\omega_r/k)/(n_0k^2)$。设 $\omega=\omega_r+i\gamma$ 且 $|\gamma|\ll\omega_r$，在实根附近展开 $\epsilon$，虚部平衡给

$$
\gamma=-\frac{\epsilon_i(\omega_r,k)}
{\partial\epsilon_r/\partial\omega}.
$$

高相速时 $\partial_\omega\epsilon_r\simeq2/\omega_{pe}$，把 Gaussian 斜率及 Bohm–Gross 实频代入，得到常用长波渐近式

$$
\frac{\gamma}{\omega_{pe}}\simeq
-\sqrt{\frac\pi8}\,(k\lambda_{De})^{-3}
\exp\!\left[-\frac1{2k^2\lambda_{De}^2}-\frac32\right].
$$

其中指数里的 $3/2$ 来自实频率的温度修正；虽然它对实频是小修正，放进尾部分布指数后仍影响阻尼系数。

由 Maxwellian 斜率 $F_0^{\prime}=-vF_0/\sigma_e^2$ 代入共振虚部，再用 $\partial_\omega\epsilon_r\simeq2/\omega_{pe}$、$\sigma_e=\omega_{pe}\lambda_{De}$，指数化为 $-1/(2k^2\lambda_{De}^2)-3/2$。指数外 $\omega_r/\omega_{pe}$ 在最低阶取1；弱阻尼式来自 $\epsilon_i+\gamma\partial_\omega\epsilon_r=0$。

**算例。** 取 $k\lambda_{De}=0.200$，代入得 $\gamma/\omega_{pe}\simeq-6.51354\times10^{-5}$。若观察 $1000/\omega_{pe}$ 的时间，场振幅比例为 $e^{-0.0651354}\approx0.936941$，二次型波能比例约为 $0.877858$。这是长波渐近值；进一步对完整 Maxwellian 介电函数求复根，可定量评估所舍弃的高阶项，而正负号由共振斜率和时间约定共同确定。[Fitzpatrick，Landau Damping，式 (7.23)–(7.31)，保留实频温度修正](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node90.html)。

用完整 Maxwellian 响应还可继续求解

$$
1+\frac{1+\zeta Z(\zeta)}{k^2\lambda_{De}^2}=0,\qquad
\zeta=\frac{\omega}{\sqrt2 k\sigma_e},\qquad
Z(\zeta)=e^{-\zeta^2}\left(i\sqrt\pi-2\int_0^\zeta e^{s^2}ds\right).
$$

最后一个表达式来自 $Z'=-2(1+\zeta Z)$、$Z(0)=i\sqrt\pi$ 的积分因子解，自动保留 Landau 解析延拓。对同一 $k\lambda_{De}=0.200$ 求复根，得 $\omega/\omega_{pe}=1.06398434-5.51074\times10^{-5}i$。长波阻尼近似的幅值比完整结果大约 $18.2\%$；这个比较给出了本算例中高阶温度响应对指数尾部的实际影响。[Fitzpatrick，Plasma Dispersion Function，式 (7.39)–(7.43)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node92.html)。

$Z$ 的速度积分先在 $\Im\zeta>0$ 定义再因果延拓。代入 Maxwellian 并用 $x/(x-\zeta)=1+\zeta/(x-\zeta)$ 即得介电式；分部积分给 $Z^{\prime}=-2(1+\zeta Z)$，初值 $Z(0)=i\sqrt\pi$ 固定同一因果解。

## 回旋共振、谐波与射频能量通道

磁化粒子的未扰动轨道包含平行运动和周期回旋；把沿轨道的波场展开成回旋谐波后，出现共振分母

$$
\omega-k_\parallel v_\parallel-\ell\Omega_s,
\qquad
\omega_r-k_\parallel v_\parallel=\ell\Omega_s,
\qquad \ell\in\mathbb Z.
$$

这里沿用带符号 $\Omega_s=q_sB_0/m_s$，$\ell$ 是谐波整数，用于编号轨道 Fourier 分量。对正离子、正频率且 Doppler 修正较小时，$\ell=1$ 是基频、$\ell=2$ 是二次谐波；电子的同向回旋共振在该 signed convention 下对应相应负谐波。文献若把电子回旋频率定义为正的幅值，整数或极化符号也会相应改变。来源：[Fitzpatrick，§7.6 Waves in Magnetized Plasmas，式 (7.80)–(7.87)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)。

共振式中的 $k_\parallel v_\parallel$ 是粒子运动引起的 Doppler 位移。有限平行速度分布把理想冷共振拓宽为一段速度空间响应，而 $k_\perp\rho_s$ 通过回旋轨道上的相位变化控制谐波耦合。只有“频率等于回旋频率”仍不够：波必须有正确的偏振分量、能到达相应区域，并与足够多的粒子有效相互作用。非零 $k_\parallel$ 时，不同 $v_\parallel$ 的粒子也可以在不同位置满足同一射频的共振条件。来源：[Fitzpatrick，§7.7，式 (7.98)–(7.101)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node95.html)。

粒子能量方程尤其简单：

$$
\frac{d}{dt}\!\left(\frac12m_sv^2\right)
=q_s\mathbf E\cdot\mathbf v,
\qquad
\mathbf v\cdot(\mathbf v\times\mathbf B)=0.
$$

直接作功的是电场，静磁场通过改变轨道与相位匹配来组织能量交换。对于 ICRH，波能可先进入少数离子或特定谐波共振粒子的非热运动，再经库仑碰撞转移给电子和其他离子，同时也可能发生轨道损失；存在模转换时，还可能通过别的分支或电子吸收通道沉积。因此“射频发生器输出”“天线耦合功率”“某离子吸收”“整体热能增加”是不同环节，各环节分别定义输入、耦合、吸收及储能功率。

最简冷圆偏振模型里的分母趋零，表示稳态线性响应发生奇异；它没有给出有限共振宽度、粒子分布演化和最终热化比例。若研究加热或电流驱动，需要含动力学吸收的全波或射线模型，再将分组分沉积与 Fokker–Planck、输运和能量守恒联系起来。相关工程入口为[离子回旋加热](../../辅助加热/离子回旋加热/README.md)，本条的共振公式不代替该系统的场谱和工况计算。来源：[Fitzpatrick，§7.7 最后两段：冷共振与无碰撞回旋阻尼的有限宽度](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node95.html)。

### 有限轨道半径如何产生谐波权重

粒子回旋使它采样的波相位含 $k_\perp\rho\sin\vartheta$。记 $b=k_\perp\rho$，将这个周期函数作 Fourier 展开，

$$
e^{ib\sin\vartheta}=\sum_{\ell=-\infty}^{\infty}J_\ell(b)e^{i\ell\vartheta},\qquad
J_\ell(b)=\frac1{2\pi}\int_0^{2\pi}
e^{i(b\sin\vartheta-\ell\vartheta)}d\vartheta .
$$

再结合平行位移 $v_\parallel t$ 与 $\vartheta=\Omega t+\vartheta_0$，每一项的时间相位含 $\omega-k_\parallel v_\parallel-\ell\Omega$，由此出现回旋谐波共振。小 $b$ 时级数给 $J_0=1-b^2/4+\cdots$、$J_1=b/2-b^3/16+\cdots$、$J_2=b^2/8+\cdots$。静电相位耦合的强度权重含 $J_\ell^2$；电磁偏振还会引入相邻阶 Bessel 函数组合。

小参数系数可直接从 $e^{ib\sin\vartheta}=\exp[(b/2)e^{i\vartheta}]\exp[-(b/2)e^{-i\vartheta}]$ 的两条 Taylor 级数相乘取得：选择指数次数差为 $\ell\ge0$ 的项，便有 $J_\ell(b)=\sum_{r=0}^{\infty}(-1)^r(b/2)^{2r+\ell}/[r!(r+\ell)!]$。沿未扰动轨道对每项积分时出现 $\int^t e^{-i(\omega-k_\parallel v_\parallel-\ell\Omega)t'}dt'$，非共振时有相应频差分母，共振时相位不再快速抵消。这同时解释谐波条件和小 $k_\perp\rho$ 时高阶耦合受抑制的原因。

**算例。** 给 $k_\perp\rho=0.200$，由级数得到 $J_0=0.990025$、$J_1=0.0995008$、$J_2=0.00498335$。对应第一、第二谐波相位权重约为 $9.90042\times10^{-3}$ 与 $2.48338\times10^{-5}$，后者是前者的 $0.250836\%$。直接对上式的周期积分求 Fourier 系数，可独立检验这些数。因 $|e^{ib\sin\vartheta}|=1$，Parseval 恒等式还给 $\sum_{\ell=-\infty}^\infty J_\ell^2=1$，可作为谐波截断检查。[Fitzpatrick，Waves in Magnetized Plasmas，回旋相位积分与 Bessel 展开](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)。

## 波吸收功率、Hermitian 分解与能量核算

取实的驱动角频率 $\omega>0$，场幅值使用峰值复振幅而非 RMS。一个周期内场对粒子的平均作功密度为

$$
Q=\left\langle\mathbf J\cdot\mathbf E\right\rangle
=\frac12\operatorname{Re}
\left(\widetilde{\mathbf E}^{\dagger}
\boldsymbol\sigma\widetilde{\mathbf E}\right)
=\frac12\widetilde{\mathbf E}^{\dagger}
\boldsymbol\sigma_H\widetilde{\mathbf E},
\qquad
\boldsymbol\sigma_H=\frac{\boldsymbol\sigma+\boldsymbol\sigma^\dagger}{2}.
$$

单位为 $\mathrm{W\,m^{-3}}$，$\dagger$ 表示共轭转置。重要的是导电率的 **Hermitian 部分** 对平均净作功有贡献，反 Hermitian 部分的二次型纯虚，对周期平均功率没有贡献。导电率的 Hermitian 部分与介电张量的反 Hermitian 部分通过因子 $i/(\epsilon_0\omega)$ 对应。该结论是对 $\langle\mathbf J\cdot\mathbf E\rangle$ 的直接代数分解，所用材料关系见 [Fitzpatrick，§5.2，式 (5.6)–(5.8)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node67.html)。

利用本页 $\boldsymbol\epsilon_r=\mathbf I+i\boldsymbol\sigma/(\epsilon_0\omega)$，定义 Hermitian 的损耗矩阵

$$
\boldsymbol\epsilon_{\mathrm{loss}}
=\frac{\boldsymbol\epsilon_r-\boldsymbol\epsilon_r^\dagger}{2i},
\qquad
\boldsymbol\sigma_H=\epsilon_0\omega\boldsymbol\epsilon_{\mathrm{loss}},
\qquad
Q=\frac{\epsilon_0\omega}{2}
\widetilde{\mathbf E}^{\dagger}
\boldsymbol\epsilon_{\mathrm{loss}}\widetilde{\mathbf E}.
$$

严格的反 Hermitian 部分是 $(\boldsymbol\epsilon_r-\boldsymbol\epsilon_r^\dagger)/2=i\boldsymbol\epsilon_{\mathrm{loss}}$；文献常说“介电张量的反 Hermitian 部分决定吸收”，其含义是以上关系，而非对张量每个元素单独取虚部。比如冷无碰撞张量的 $\pm iD$ 元素虽是纯虚，整体张量在实频率且远离奇点时仍为 Hermitian，其有限周期平均耗散为零。来源：[Fitzpatrick，§5.3，式 (5.37)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)。

一个可独立检查的例子是非磁化、具有给定正碰撞频率 $\nu$ 的电子模型：

$$
m_e(\nu-i\omega)\mathbf v_e=-e\mathbf E,
\quad
\sigma=\frac{\epsilon_0\omega_{pe}^2}{\nu-i\omega},
\quad
Q=\frac{\epsilon_0\omega_{pe}^2\nu}
{2(\nu^2+\omega^2)}|\widetilde{\mathbf E}|^2\ge0.
$$

这验证了时间 convention、$1/2$ 因子和吸收符号；它只是简化摩擦模型，并非完整 Coulomb 碰撞算符。主动分布也可能给出负 $Q$，表示粒子向波供能，因而所有模式都“必须正吸收”并非普遍定理。来源：[Fitzpatrick，§6.6 Collisional Damping](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node83.html)。

对非局域响应，应先用实际 $\mathbf J(\mathbf r)$ 与 $\mathbf E(\mathbf r)$ 计算局部作功；纯局域介电矩阵则采用局部响应近似。稳态能量检查应比较穿过边界的 Poynting 通量、体积分 $\int Q\,dV$、天线输入和壁耗散。若需区分电子与各离子吸收，要分解各组分电流 $\mathbf J_s$ 并分别计算 $Q_s$；各组分沉积与后续温度演化也应分别核算。

将 Ampère–Maxwell 与 Faraday 方程分别点乘 $\mathbf E$、$\mathbf B/\mu_0$，得到

$$
\partial_t\!\left(\frac{\varepsilon_0E^2}{2}+\frac{B^2}{2\mu_0}\right)
+\nabla\cdot\left(\frac{\mathbf E\times\mathbf B}{\mu_0}\right)
=-\mathbf J\cdot\mathbf E.
$$

右侧与粒子动能矩的正场功抵消；周期平均给 $-Q$，边界能流仍须保留。

还要区分能量增长率与振幅增长率：若固定模结构的振幅随 $e^{\gamma t}$ 变化，相应二次型能量就随 $e^{2\gamma t}$ 变化。比较动力学根求得的 $\gamma$ 与时域能量拟合斜率时，必须处理这一因子二。波能还包含粒子有序振荡的贡献，由总波能与平均场功共同换算阻尼率；在色散强的等离子体中，这种遗漏可能直接影响数量级。

### 把复振幅结果还原为一个周期的实功

设实际场与电流分别为 $\mathbf E(t)=\Re[\widetilde{\mathbf E}e^{-i\omega t}]$、$\mathbf J(t)=\Re[\boldsymbol\sigma\widetilde{\mathbf E}e^{-i\omega t}]$。把每个实部写成复量及其共轭之和，乘积产生常数项和 $e^{\pm2i\omega t}$ 项。积分一个周期后二倍频项消失，得到

$$
\frac1T\int_0^T\mathbf J(t)\cdot\mathbf E(t)\,dt
=\frac14\left[
\widetilde{\mathbf E}^\dagger\boldsymbol\sigma\widetilde{\mathbf E}
+\widetilde{\mathbf E}^\dagger\boldsymbol\sigma^\dagger\widetilde{\mathbf E}\right]
=\frac12\widetilde{\mathbf E}^\dagger\boldsymbol\sigma_H\widetilde{\mathbf E}.
$$

这个推导同时确定了峰值复振幅对应的 $1/2$ 系数。若改用 RMS 振幅，定义中已经包含 $\sqrt2$，功率表达式相应调整。

**算例。** 给 $\boldsymbol\sigma=\operatorname{diag}(2+3i,1+4i,0)\,\mathrm{S\,m^{-1}}$，$\widetilde{\mathbf E}=(3,4i,0)\,\mathrm{V\,m^{-1}}$。Hermitian 部分为 $\operatorname{diag}(2,1,0)$，所以 $Q=[2(3^2)+1(4^2)]/2=17.0\,\mathrm{W\,m^{-3}}$。实时间表达式中，$E_x=3\cos\omega t$、$E_y=4\sin\omega t$；两个方向分别贡献平均 $9$ 与 $8\,\mathrm{W\,m^{-3}}$，其余交错正弦项周期平均为零。将 $\mathbf J\cdot\mathbf E$ 作时间数值积分，可以独立验证矩阵计算与峰值/RMS 归一化。[Fitzpatrick，式 (5.6)–(5.8) 的线性材料关系](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node67.html)。

[返回基础原理](../README.md)
