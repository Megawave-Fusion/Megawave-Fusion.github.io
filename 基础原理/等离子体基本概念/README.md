# 等离子体基本概念

采用 SI、经典非相对论弱耦合模型。$T_s$ 用 K，$\Theta_s=k_BT_s$ 用 J；准中性、Maxwellian、无碰撞和磁化各需独立的尺度或分布假设。数值均为给定输入的教学计算。

## SI 单位、电子伏特与温度能量

等离子体文献常说“电子温度为 $1\,\mathrm{keV}$”。它表示 $k_B T_e$ 的能量值为 $1\,\mathrm{keV}$，电子的单粒子动能仍按分布函数分布。本知识库保留 $T_s$ 的开尔文单位，并用 $\Theta_s$ 表示温度能量，以减少同一字母在不同教材中的歧义：

$$
\Theta_s=k_B T_s,
\qquad
1\,\mathrm{eV}=1.602176634\times10^{-19}\,\mathrm J,
\qquad
k_B=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}.
$$

$\Theta_s=k_BT_s$ 是定义；SI 固定 $e,k_B$。由电功 $W=q\Delta\phi$，$1\,\mathrm{eV}=e\times1\,\mathrm V$，除以 $k_B$ 即得温度换算。

因此，$\Theta_s=1\,\mathrm{eV}$ 对应 $T_s\simeq1.16045\times10^4\,\mathrm K$，$1\,\mathrm{keV}$ 对应约 $1.16045\times10^7\,\mathrm K$。若记 $T_{s,\mathrm{eV}}=\Theta_s/(1\,\mathrm{eV})$，它是一个数值，例如在 $1\,\mathrm{keV}$ 时等于 $1000$；代入 SI 公式前，须把能量还原为焦耳。[NIST：2022 CODATA 常数表，electron volt 条目](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)；[MIT OCW：Introduction，§1.2.1，式 (1.17)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

常用符号中，$n_s$ 是数密度，单位 $\mathrm{m^{-3}}$；$q_s$ 是带符号的电荷，单位 C；电子有 $q_e=-e$，其中 $e>0$；$m_s$ 的单位是 kg；$\mathbf E$ 用 $\mathrm{V\,m^{-1}}$；$\mathbf B$ 用 T；$\varepsilon_0$ 用 $\mathrm{F\,m^{-1}}$。对 SI Lorentz 力，磁力项是 $q_s\mathbf v\times\mathbf B$，没有额外的 $1/c$。Gaussian-cgs 中的磁力形式为 $q_s\mathbf v\times\mathbf B/c$，换成 SI 时应同时转换场、电荷和单位。

在各向同性的非相对论分布中，每粒子的平均无规则平动能是 $3\Theta_s/2$。例如温度能量 $\Theta_e=1\,\mathrm{keV}$ 的 Maxwellian 电子，其平均热动能为 $1.5\,\mathrm{keV}$；若存在整体流速 $\mathbf u_e$，实验室系平均动能还要加上 $m_eu_e^2/2$。这一步区分了温度与束流定向能量。低温体相与高能尾部共存时，还需分别描述各部分的粒子数与能量分布。[UT Austin：Fundamental Parameters，式 (1.1)–(1.4)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node5.html)。

用 $m v^2/2$ 解释温度要求主要粒子处于非相对论范围；当电子能量不可忽略于 $m_ec^2\simeq511\,\mathrm{keV}$ 时，须改用相对论动量和分布。电子与离子温度分别由各自分布定义；eV 是能量单位；压力用 $n\Theta=nk_BT$ 计算。

### 由速度积分得到温度与定向能量

把 Maxwell 分布写成三个一维高斯的乘积。设 $a=m/(2\Theta)$，由 $\int e^{-av^2}dv=\sqrt{\pi/a}$ 对 $a$ 求导，得到 $\int v^2e^{-av^2}dv=\sqrt\pi/(2a^{3/2})$；两式相除便是 $\langle c_x^2\rangle=\Theta/m$。再将 $\mathbf v=\mathbf u+\mathbf c$ 代入动能，利用 $\langle\mathbf c\rangle=0$，有

$$
\langle K\rangle=\frac{m u^2}{2}
+\frac m2\left(\langle c_x^2\rangle+\langle c_y^2\rangle+\langle c_z^2\rangle\right)
=\frac{m u^2}{2}+\frac32\Theta .
$$

高斯宽度决定热能，中心位置决定流动能；整体变换参考系只改变后者。

**算例。** 已知电子温度能量为 $250\,\mathrm{eV}$、定向动能为每粒子 $75\,\mathrm{eV}$。先换算 $\Theta=250e=4.00544\times10^{-17}\,\mathrm J$，所以 $T=\Theta/k_B=2.90113\times10^6\,\mathrm K$；热动能为 $375\,\mathrm{eV}=6.00816\times10^{-17}\,\mathrm J$。由 $u=\sqrt{2(75e)/m_e}$ 得 $5.13637\times10^6\,\mathrm{m\,s^{-1}}$，实验室系平均动能为 $450\,\mathrm{eV}$。热项和定向项分别占 $5/6$ 与 $1/6$，可分别进入压力与宏观动能账本。积分依据见 [MIT 第 1 章 §1.2.1 的 Boltzmann 因子与 Maxwell 分布](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)，矩的分解见 [Fitzpatrick 式 (4.15)、(4.17)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node47.html)。

## 分布函数、密度、流速与温度的定义

速度分布函数 $f_s(\mathbf x,\mathbf v,t)$ 定义为：$f_s\,d^3x\,d^3v$ 是给定相空间小体积内的平均粒子数。这里采用数密度归一化，$f_s$ 的 SI 单位为 $\mathrm{s^3\,m^{-6}}$；除以 $n_s$ 后才是速度空间概率密度。其前两个速度矩给出密度和流速：

$$
n_s=\int f_s\,d^3v,
\qquad
\mathbf u_s=\frac{1}{n_s}\int\mathbf v f_s\,d^3v,
\qquad
\mathbf c_s=\mathbf v-\mathbf u_s.
$$

令 $\mathbf c_s$ 为相对整体流的无规则速度，则压力张量和标量温度能量为

$$
\mathsf P_s=m_s\int\mathbf c_s\mathbf c_s f_s\,d^3v,
\qquad
p_s=\frac13\operatorname{tr}\mathsf P_s,
\qquad
\Theta_s=\frac{p_s}{n_s}.
$$

$\mathsf P_s$、$p_s$ 的单位是 Pa。以上是矩的定义；只要积分存在，就不必先假定热平衡。它们同时给出无规则动能密度 $w_{s,\mathrm{th}}=\tfrac12\operatorname{tr}\mathsf P_s=\tfrac32n_s\Theta_s$。实验室系动量通量多出 $m_sn_s\mathbf u_s\mathbf u_s$，故测量粒子速度时须先扣除流动，才能由展宽求温度。[UT Austin：Moments of Distribution Function，式 (4.5)、(4.6)、(4.11)–(4.17)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node47.html)。

常见的各向同性 Maxwellian 特例是

$$
f_{Ms}=n_s\left(\frac{m_s}{2\pi\Theta_s}\right)^{3/2}
\exp\!\left[-\frac{m_s|\mathbf v-\mathbf u_s|^2}{2\Theta_s}\right].
$$

三个高斯矩给出归一化 $n_s$、零平均相对速度与 $\langle c_j^2\rangle=\Theta_s/m_s$，故 $p_s=n_s\Theta_s$。单价纯氘 $n_e=n_i=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=\Theta_i=10\,\mathrm{keV}$ 时，每种压力约160 kPa，总热压约320 kPa。 [MIT OCW：Introduction，§1.2.1 的 Maxwell–Boltzmann 分布](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

磁化分布常需要 $p_{\parallel s}$ 与 $p_{\perp s}$，后者对应两个垂直自由度中的每一个方向；此时标量压力为 $(p_{\parallel s}+2p_{\perp s})/3$，三个自由度的权重由迹运算确定。两个不同的非 Maxwellian 分布可以有相同的 $n$、$\mathbf u$ 和温度，却具有不同的共振粒子数、热流和聚变反应率。热流与共振响应还需要更高阶矩或速度分布信息。

### 双温高斯的压力张量

取磁场沿 $z$，令共动系分布为

$$
f=\frac{n}{(2\pi)^{3/2}\sigma_\perp^2\sigma_\parallel}
\exp\!\left[-\frac{c_x^2+c_y^2}{2\sigma_\perp^2}
-\frac{c_z^2}{2\sigma_\parallel^2}\right].
$$

依次对三个速度分量积分，零阶矩给 $n$；奇函数积分给零一阶矩及零非对角二阶矩。对角矩分别给 $P_{xx}=P_{yy}=nm\sigma_\perp^2$、$P_{zz}=nm\sigma_\parallel^2$。于是定义 $\Theta_\perp=m\sigma_\perp^2$、$\Theta_\parallel=m\sigma_\parallel^2$ 后，

$$
p=\frac{n(2\Theta_\perp+\Theta_\parallel)}3,\qquad
w_{\rm th}=n\left(\Theta_\perp+\frac12\Theta_\parallel\right).
$$

系数2计入两个垂直自由度；取迹除以三得到标量温度，方向上的压力力仍用张量分量。

**算例。** 给定 $n=2\times10^{19}\,\mathrm{m^{-3}}$、$\Theta_\perp=300\,\mathrm{eV}$、$\Theta_\parallel=900\,\mathrm{eV}$，将 eV 乘 $e$ 后，$P_\perp=961.31\,\mathrm{Pa}$、$P_\parallel=2883.92\,\mathrm{Pa}$。标量温度能量为 $500\,\mathrm{eV}$，故 $p=1602.18\,\mathrm{Pa}$，热能密度 $w_{\rm th}=2403.26\,\mathrm{J\,m^{-3}}$。相同标量温度的各向同性分布具有相同总热能，而这个例子的沿场动量通量为横场的三倍。[Fitzpatrick，式 (4.11)–(4.16)，共动系压力与能量矩](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node47.html)。

## 准中性、净电荷与有限电场

准中性（quasineutrality）是宏观尺度上正负电荷密度近乎抵消的性质。对电子和多种正离子，

$$
\rho_q=\sum_s q_s n_s
=e\left(\sum_i Z_i n_i-n_e\right),
\qquad
n_e\simeq\sum_i Z_i n_i.
$$

$\rho_q$ 的单位是 $\mathrm{C\,m^{-3}}$；$Z_i$ 是离子的电荷数。对于氘、氚和完全电离氦的混合物，应写 $n_e\simeq n_D+n_T+2n_{\mathrm{He}}$，各组分按电荷数加权。杂质的每个电离态也应分别计入。[UT Austin：What is Plasma?，准中性定义](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node3.html)；[MIT OCW：Introduction，§1.1.2，式 (1.2)–(1.9)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

准中性体等离子体中仍可有有限电场。在静电近似中，Poisson 方程是 $-\nabla^2\phi=\rho_q/\varepsilon_0$。若势变化尺度为 $L$、幅度为 $\phi_*$，由量纲估计得到

$$
\frac{|\rho_q|}{e n_e}
\sim \frac{\varepsilon_0\phi_*}{e n_e L^2}
=\left(\frac{\lambda_{De}}{L}\right)^2
\frac{e\phi_*}{\Theta_e},
\qquad
\lambda_{De}^2=\frac{\varepsilon_0\Theta_e}{n_e e^2}.
$$

若 $e|\phi|/\Theta_e\sim1$、$L\gg\lambda_{De}$，极小电荷差也可支撑有限电场。例：$L=1$ m、$\lambda_{De}=10^{-4}$ m、$e|\phi|/\Theta_e=1$ 时，相对失衡约 $10^{-8}$。

电荷中性和电流中性也是不同条件：$\mathbf j=\sum_s q_s n_s\mathbf u_s$ 还依赖各组分流速。单价等密度电子与离子若流速不同，仍可携带电流。反过来，各组分没有平均流动也不自动保证电荷中性。[UT Austin：Moments of Distribution Function，式 (4.7)、(4.8)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node47.html)。

准中性常用于远离鞘层的低频、大尺度体等离子体；Debye 尺度结构、强双层和专门制备的非中性等离子体需要保留空间电荷。约化模型在最低阶令 $\rho_q=0$，是渐近展开的最低阶关系；更高阶电荷差由场方程决定。准中性约束电荷平衡；快粒子、不同组分温度和各向异性都可以与之共存。

### 用一个电势模直接计算电荷分离

对周期空间中的单一静电模，设 $\phi(x)=\phi_0\cos kx$。连续求一次、两次导数，分别得到场和电荷：

$$
E_x=-\partial_x\phi=k\phi_0\sin kx,\qquad
\rho_q=-\varepsilon_0\partial_x^2\phi
=\varepsilon_0k^2\phi_0\cos kx.
$$

因此 $E$ 与电荷密度在空间相位上相差四分之一周期；电势极大处电场为零而净正电荷最大。以背景电子密度归一化，电荷失衡振幅为
$\delta_q=\varepsilon_0k^2\phi_0/(en_e)=(k\lambda_{De})^2e\phi_0/\Theta_e$。周期内 $\int\rho_qdx=0$，局部电荷分离与整体零净电荷可以同时出现。这给准中性展开提供了比单一长度量级更具体的例子。

**算例。** 取波长 $2.0\,\mathrm{cm}$、$\phi_0=20\,\mathrm V$、$n_e=10^{19}\,\mathrm{m^{-3}}$。先算 $k=2\pi/0.020=314.159\,\mathrm{m^{-1}}$，得到场振幅 $6.2832\times10^3\,\mathrm{V\,m^{-1}}$、电荷振幅 $1.74775\times10^{-5}\,\mathrm{C\,m^{-3}}$。除以 $en_e=1.60218\,\mathrm{C\,m^{-3}}$，相对失衡仅为 $1.09086\times10^{-5}$，即约十一百万分之一。对应的强度梯度由这一微小空间电荷提供；波长减半而势幅保持时，场幅加倍、电荷幅增加四倍。[MIT 第 1 章 §1.1.2，式 (1.2)–(1.5)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

## Debye 屏蔽与多组分屏蔽长度

![线性 Debye 屏蔽的势比与累计包围净电荷](/assets/diagrams/basic-concepts.svg)

*线性 Debye 屏蔽的势比与累计包围净电荷。曲线与示意均按本条所列模型生成。*

Debye 屏蔽描述近热平衡介质对微弱、近静态外加电势的密度重排。对可参与响应的 Maxwellian 组分，取远处电势为零，有

$$
n_s(\phi)=n_{s0}\exp\!\left(-\frac{q_s\phi}{\Theta_s}\right)
\simeq n_{s0}\left(1-\frac{q_s\phi}{\Theta_s}\right),
\qquad |q_s\phi|\ll\Theta_s.
$$

这个指数响应来自静态、等温、无流组分的力平衡 $0=-\nabla(n_s\Theta_s)-q_sn_s\nabla\phi$。除以 $n_s\Theta_s$ 并从远处积分，得到 $\ln(n_s/n_{s0})=-q_s\phi/\Theta_s$；小势条件下再用 $e^x=1+x+O(x^2)$ 线性化。它也等价于对总单粒子能量 $mv^2/2+q_s\phi$ 使用 Boltzmann 因子后积分速度。

在线性化背景满足 $\sum_s q_s n_{s0}=0$ 时，诱导电荷为 $\delta\rho_q=-\phi\sum_s n_{s0}q_s^2/\Theta_s$。代入 Poisson 方程可得

$$
\left(\nabla^2-\lambda_D^{-2}\right)\phi
=-\frac{\rho_{\mathrm{ext}}}{\varepsilon_0},
\qquad
\lambda_D^{-2}=\sum_{s\,\mathrm{responsive}}
\frac{n_{s0}q_s^2}{\varepsilon_0\Theta_s}.
$$

这里 $\rho_{\mathrm{ext}}$ 是外加电荷密度，$\lambda_D$ 的单位是 m。无限均匀介质中，一个弱测试点电荷 $Q$ 在远离其非线性近场处产生

$$
\phi(r)=\frac{Q}{4\pi\varepsilon_0r}\exp(-r/\lambda_D).
$$

点电荷外令 $u=r\phi$，球对称方程变为 $u^{\prime\prime}-u/\lambda_D^2=0$。远处衰减选出 $u=Ae^{-r/\lambda_D}$，原点 Gauss 条件固定 $A=Q/(4\pi\varepsilon_0)$；非线性近场另处理。

指数只修饰原有的 $1/r$ 势；屏蔽势随距离连续衰减。[UT Austin：Debye Shielding，式 (1.11)–(1.15)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node7.html)。

必须区分电子 Debye 长度 $\lambda_{De}=\sqrt{\varepsilon_0\Theta_e/(n_ee^2)}$ 与总静态屏蔽长度。若离子在所考虑的响应过程中近似固定，仅保留电子项；若单价离子与电子均可达到上述 Boltzmann 响应，且密度相等、$\Theta_i=\Theta_e$，则 $\lambda_D=\lambda_{De}/\sqrt2$。一般单价等密度情形有 $\lambda_D^{-2}=\lambda_{De}^{-2}(1+\Theta_e/\Theta_i)$。因此不同教材的 $\sqrt2$ 差异往往来自参与屏蔽的组分不同。[MIT OCW：Introduction，§1.2.3，式 (1.19)–(1.24)，明确采用固定离子密度](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

**算例。** 在 $n_e=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=1\,\mathrm{keV}$ 时，$\lambda_{De}\simeq23.5\,\mu\mathrm m$；等温单价双组分的总长度约为 $16.6\,\mu\mathrm m$。把温度提高四倍，电子屏蔽长度增大两倍；把密度提高四倍，它缩小两倍。该线性静态公式不直接描述强鞘层、束流尾迹、快速振荡或一般磁化非平衡响应；这些情形需要相应的动力学介电响应。时间变化与磁化几何的作用由相应频率、波数和偏振响应决定。

### 屏蔽云中累计包含多少电荷

对线性屏蔽区中的球对称势 $\phi=Qe^{-r/\lambda_D}/(4\pi\varepsilon_0r)$，求导时同时保留 $1/r$ 与指数项。用 Gauss 定律便得到半径 $r$ 内测试电荷与屏蔽云的净和：

$$
E_r=\frac{Qe^{-r/\lambda_D}}{4\pi\varepsilon_0r^2}
\left(1+\frac r{\lambda_D}\right),\qquad
Q_{\rm enc}(r)=4\pi\varepsilon_0r^2E_r
=Qe^{-x}(1+x),\quad x=\frac r{\lambda_D}.
$$

再求导，$dQ_{\rm enc}/dr=-Q\,r e^{-r/\lambda_D}/\lambda_D^2$，等于 $4\pi r^2\rho_{\rm ind}(r)$，可与 $\rho_{\rm ind}=-\varepsilon_0\phi/\lambda_D^2$ 互相验证。对正的测试电荷，屏蔽云的各球壳都贡献负电荷；远处累计趋近 $-Q$。这一推导适用于线性响应区，测试粒子附近的非线性核心另由实际相互作用决定。

**算例。** 给定 $\lambda_D=30\,\mu\mathrm m$，考察 $r=90\,\mu\mathrm m$，即 $x=3$。净包围电荷比例为 $4e^{-3}=0.199148$，累计屏蔽了 $80.0852\%$ 的测试电荷。$r=\lambda_D$ 时净比例为 $2/e=0.735759$；所以从 $30$ 到 $90\,\mu\mathrm m$ 的球壳贡献为 $(0.199148-0.735759)Q=-0.536611Q$。势比真空值的衰减为 $e^{-3}$，而包围电荷的衰减另含因子 $1+x$，这是空间求导带来的可观测差别。[Fitzpatrick，Debye Shielding，式 (1.11)–(1.15)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node7.html)。

## 集体效应、Debye 球粒子数与弱耦合

集体响应由自洽电磁场组织。经典弱耦合近似分别检查系统/屏蔽尺度、屏蔽体积粒子数，以及集体频率/碰撞率，约束空间、统计和时间排序。

以电子 Debye 长度为约定，定义

$$
N_{De}=\frac{4\pi}{3}n_e\lambda_{De}^3,
\qquad
a_e=\left(\frac{3}{4\pi n_e}\right)^{1/3},
\qquad
\Gamma_e=\frac{e^2}{4\pi\varepsilon_0a_e\Theta_e}.
$$

$N_{De}$ 是电子 Debye 球内的平均电子数；$a_e$ 是每粒子平均体积对应的球半径，单位 m；$\Gamma_e$ 是典型库仑势能与温度能量之比，三者中前后两者无量纲。把 $n_e=3/(4\pi a_e^3)$ 代入即可自行核对

$$
\frac{\lambda_{De}}{a_e}=\frac{1}{\sqrt{3\Gamma_e}},
\qquad
N_{De}=(3\Gamma_e)^{-3/2}.
$$

所以在这套单种尺度约定下，$N_{De}\gg1$ 与 $\Gamma_e\ll1$ 相联系。因子 $4\pi/3$ 以及选用单种还是总 Debye 长度会改变数值常数；有的书把“plasma parameter”定义为粒子数，有的定义为其倒数，必须读取定义。[UT Austin：Plasma Parameter，式 (1.16)–(1.20)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node8.html)。

对 $n_e=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=1\,\mathrm{keV}$，得到 $a_e\simeq1.34\times10^{-7}\,\mathrm m$、$\Gamma_e\simeq1.08\times10^{-5}$、$N_{De}\simeq5.44\times10^6$。这里大粒子数意味着屏蔽云可在适当平均意义下用连续密度描述；空间涨落和湍流幅度还取决于分布与驱动。多种高电荷离子可能有不同的耦合强度，应分别计算各组分的耦合参数。

在弱耦合库仑理论中，碰撞率相对等离子体频率常具有 $\nu/\omega_p$ 与 $\ln N_D/N_D$ 同阶的缩放关系，但精确系数、库仑对数和碰撞率定义依赖具体过程。该缩放展示了弱耦合极限中集体响应快于碰撞的时间尺度分离。[UT Austin：Collisions，式 (1.21)–(1.27)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node9.html)。

取 $v_t\sim\sqrt{\Theta_e/m_e}$、$b_0\sim e^2/(4\pi\varepsilon_0\Theta_e)$，小角累积给 $\nu\sim n_ev_tb_0^2\ln\Lambda$。用 $\omega_{pe}\sim v_t/\lambda_{De}$、$b_0\sim1/(n_e\lambda_{De}^2)$，得 $\nu/\omega_{pe}\sim\ln\Lambda/N_D$；这里只保留量级。

弱耦合体系在长时间演化中仍会积累碰撞效应；强耦合物质也可以是等离子体，只是上述 Debye–弱散射描述可能失效。部分电离也是等离子体物理的重要范围：部分电离体系能有集体响应，但须把电子–中性粒子等碰撞纳入时间尺度比较。本页采用聚变热等离子体常见的弱耦合排序。

### 沿压缩路径追踪等离子体参数

把 $\lambda_{De}^2=\varepsilon_0\Theta_e/(n_ee^2)$ 代入 Debye 球粒子数，得

$$
N_{De}=\frac{4\pi}{3}
\left(\frac{\varepsilon_0}{e^2}\right)^{3/2}
\Theta_e^{3/2}n_e^{-1/2},\qquad
d\ln N_{De}=\frac32d\ln\Theta_e-\frac12d\ln n_e.
$$

这个微分式把两种压缩路径区分开。等温压缩满足 $N_{De}\propto n_e^{-1/2}$；各向同性三维单原子气体的绝热压缩满足 $\Theta_e\propto n_e^{2/3}$，因而 $N_{De}\propto n_e^{1/2}$。同时 $\Gamma_e\propto n_e^{1/3}/\Theta_e$，绝热路径上它随 $n_e^{-1/3}$ 下降。密度上升和热运动增强的竞争，决定了耦合程度如何变化。

绝热指数可从本页热能矩核对：固定粒子数 $N$ 的物质元有 $U=3N\Theta/2$、$p=N\Theta/V$，无热交换时 $dU=-p\,dV$ 给 $d\ln\Theta=-(2/3)d\ln V=(2/3)d\ln n$。这说明 $2/3$ 依赖三维各向同性热容；磁化无碰撞各向异性压缩不能自动使用这一路径。

**算例。** 初始 $n_e=10^{19}\,\mathrm{m^{-3}}$、$\Theta_e=200\,\mathrm{eV}$，代入得 $\lambda_{De}=33.2456\,\mu\mathrm m$、$N_{De}=1.53919\times10^6$。密度增至八倍时，等温路径的 Debye 长度缩至原来的 $1/\sqrt8$，球内粒子数为原来的 $1/\sqrt8$；绝热路径温度增至 $800\,\mathrm{eV}$，长度为原来的 $1/\sqrt2$，球内粒子数反而增至 $\sqrt8$ 倍，即 $4.35348\times10^6$。因此报告一个压缩过程时，密度和温度路径共同决定其弱耦合排序。[MIT 第 1 章 §1.3，式 (1.34)–(1.35)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

## 等离子体频率及其恢复力

等离子体频率反映电荷分离引起的静电恢复力。对数密度 $n_s$、质量 $m_s$、电荷 $q_s$ 的组分，定义正的角频率

$$
\omega_{ps}=\sqrt{\frac{n_s q_s^2}{\varepsilon_0m_s}},
\qquad
f_{ps}=\frac{\omega_{ps}}{2\pi}.
$$

$\omega_{ps}$ 的单位为 $\mathrm{rad\,s^{-1}}$，$f_{ps}$ 的单位为 Hz；电荷的正负号不会使 $\omega_{ps}$ 变成负数。多数入门语境中的“等离子体频率”指电子频率 $\omega_{pe}$，但含多种粒子时应显式标注组分。[UT Austin：Plasma Frequency，式 (1.5)、(1.6)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node6.html)。

一个可核对符号的推导是：把均匀电子平板相对于固定离子背景沿 $x$ 方向整体移动微小距离 $\xi$。两侧表面电荷产生 $E_x=n_ee\xi/\varepsilon_0$，因此电子所受力为 $-eE_x$，满足

$$
m_e\ddot\xi=-\frac{n_ee^2}{\varepsilon_0}\xi,
\qquad
\ddot\xi+\omega_{pe}^2\xi=0.
$$

该简化模型忽略压力、碰撞、磁场和边界细节，给出电荷分离恢复力的本征频率。若多个冷组分都能运动，无磁、静电、均匀线性模型给出 $\omega^2=\sum_s\omega_{ps}^2$ 的电荷分离振荡分支。固定离子的电子振荡是其中的近似；低频问题则保留离子动力学。

非零纵向波数下，$n_{s1}=-n_{s0}\partial_x\xi_s$、$E_1=-\sum_sn_{s0}q_s\xi_s/\varepsilon_0$。结合 $m_s\ddot\xi_s=q_sE_1$，得 $\ddot E_1+\sum_s\omega_{ps}^2E_1=0$；不含不产生电荷分离的零频自由度。

数值上，在 $n_e=10^{20}\,\mathrm{m^{-3}}$ 时，$\omega_{pe}\simeq5.64\times10^{11}\,\mathrm{rad\,s^{-1}}$，$f_{pe}\simeq89.8\,\mathrm{GHz}$；等密度单价氘的 $\omega_{pD}\simeq9.31\times10^9\,\mathrm{rad\,s^{-1}}$。频率随 $\sqrt n$ 增长；将密度提高四倍只使频率加倍。若密度以 $\mathrm{cm^{-3}}$ 输入常见工程公式，须先注意 $1\,\mathrm{cm^{-3}}=10^6\,\mathrm{m^{-3}}$，否则频率会相差一千倍。

有限温度可带来波数依赖与动力学阻尼，磁场会改变模态与偏振。无磁冷电子介质中的横向电磁波截止与 $\omega_{pe}$ 相关，磁化后各分支有各自的截止条件。$\omega\ll\omega_{pe}$ 常使电子有能力快速调整，但准中性是否成立还须同时检查 $k\lambda_{De}$、边界、驱动与所选分支。数值计算中按 $\omega=2\pi f$ 转换角频率与普通频率。

### 两种可运动组分的相对振荡与能量

让等密度单价离子与电子平板都能沿 $x$ 运动，位移为 $\xi_i,\xi_e$。定义相对位移 $\Delta=\xi_e-\xi_i$，由表面电荷得到 $E=ne\Delta/\varepsilon_0$。两种粒子的运动方程相减，同时把它们的动量方程相加，得到

$$
\ddot\Delta+\omega_*^2\Delta=0,\qquad
\omega_*^2=\frac{ne^2}{\varepsilon_0}\left(\frac1{m_e}+\frac1{m_i}\right),
\qquad \frac{d^2}{dt^2}(m_e\xi_e+m_i\xi_i)=0.
$$

质心作匀速运动，相对坐标承担振荡。令约化质量 $m_r=m_em_i/(m_e+m_i)$，相对运动的能量密度为
$w=nm_r\dot\Delta^2/2+\varepsilon_0E^2/2$；将方程代入求导，两个功率项恰好抵消。因此在位移最大处能量全在电场中，在穿过平衡位置时全在两组分的相对动能中。

**算例。** 对 $n=10^{18}\,\mathrm{m^{-3}}$ 的电子—氘体系，$\omega_{pe}=5.64146\times10^{10}\,\mathrm{rad\,s^{-1}}$；乘 $\sqrt{1+m_e/m_D}$ 得 $\omega_*=5.64223\times10^{10}\,\mathrm{rad\,s^{-1}}$，增加 $0.0136213\%$。给相对位移振幅 $1.0\,\mu\mathrm m$，最大场能密度为 $n^2e^2\Delta_0^2/(2\varepsilon_0)=1.44958\times10^{-3}\,\mathrm{J\,m^{-3}}$。这一数值也等于最大相对动能密度。[Fitzpatrick，Plasma Frequency，式 (1.5)–(1.6)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node6.html)，这里将其固定背景模型扩展为双组分守恒模型。

## 热速度、惯性长度与尺度表

常用热速度有几种不同的统计定义。本条对各向同性、非相对论 Maxwellian 的相对速度 $\mathbf c=\mathbf v-\mathbf u$，使用

$$
v_{ts}=\sqrt{\frac{2\Theta_s}{m_s}},
\qquad
\sigma_{v_x}=\sqrt{\frac{\Theta_s}{m_s}},
\qquad
v_{\mathrm{rms}}=\sqrt{\frac{3\Theta_s}{m_s}}.
$$

这些速度可统一从归一化速率密度 $g(c)=4\pi c^2[m/(2\pi\Theta)]^{3/2}e^{-mc^2/(2\Theta)}$ 求出：令 $a=m/(2\Theta)$，$d\ln g/dc=2/c-2ac=0$ 给最概然值 $\sqrt{2\Theta/m}$；三个高斯方差相加给 $\langle c^2\rangle=3\Theta/m$；平均速率用 $\int_0^\infty c^3e^{-ac^2}dc=1/(2a^2)$ 得 $\sqrt{8\Theta/(\pi m)}$。

$v_{ts}$ 是三维速率分布 $4\pi c^2f_M(c)$ 的最概然速率；$\sigma_{v_x}$ 是任一笛卡尔分量的标准差；$v_{\mathrm{rms}}=\sqrt{\langle c^2\rangle}$ 是均方根速率，三者单位均为 $\mathrm{m\,s^{-1}}$。此外平均速率是 $\langle c\rangle=\sqrt{8\Theta_s/(\pi m_s)}$。这些区别可由高斯积分或对 $c^2\exp[-mc^2/(2\Theta)]$ 求极值直接检查；引用“thermal velocity”时应把定义一起写出。[UT Austin：Fundamental Parameters，式 (1.3)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node5.html)。

同一组分的 Debye 长度满足精确的定义关系

$$
\lambda_{Ds}=\frac{\sqrt{\Theta_s/m_s}}{\omega_{ps}}
=\frac{v_{ts}}{\sqrt2\,\omega_{ps}},
\qquad
d_s=\frac{c}{\omega_{ps}}.
$$

将 $\omega_{ps}^2=n_sq_s^2/(\varepsilon_0m_s)$ 代回即可检验第一式。惯性长度定义为 $c/\omega_{ps}$；其电磁衰减意义由冷横波 $k^2c^2=\omega^2-\omega_{pe}^2$ 取 $k=i\kappa$ 得到。

$d_s$ 是惯性长度，单位 m，$c$ 是光速。$\lambda_D$ 与 $d_s$ 的比值含热速度相对光速的因子，所对应的物理响应不同。$d_e$ 常称电子趋肤深度的特征尺度；实际电磁场衰减长度还依赖频率、碰撞和磁场，应从所用色散关系求出。例如固定离子、无磁、无碰撞冷电子模型有 $k^2c^2=\omega^2-\omega_{pe}^2$；在 $\omega<\omega_{pe}$ 时，衰减长度为 $c/\sqrt{\omega_{pe}^2-\omega^2}$，只有其低频极限才趋于 $d_e$。[UT Austin：Plasma Frequency，式 (1.7)、(1.8)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node6.html)；[MIT OCW：Electromagnetic Waves，§5.2.1–§5.2.2，式 (5.53)–(5.57)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

以下取纯单价氘，$n_e=n_D=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=\Theta_D=1\,\mathrm{keV}$，回旋半径以 $v_{ts}$ 和 $B=5\,\mathrm T$ 计算：

| 物理量 | 电子 | 氘离子 |
| --- | --- | --- |
| $v_{ts}$ | $1.88\times10^7\,\mathrm{m\,s^{-1}}$ | $3.10\times10^5\,\mathrm{m\,s^{-1}}$ |
| 单种 $\lambda_{Ds}$ | $23.5\,\mu\mathrm m$ | $23.5\,\mu\mathrm m$ |
| $d_s=c/\omega_{ps}$ | $0.531\,\mathrm{mm}$ | $3.22\,\mathrm{cm}$ |
| $\rho_{ts}=v_{ts}/\lvert\Omega_s\rvert$ | $21.3\,\mu\mathrm m$ | $1.29\,\mathrm{mm}$ |

相同温度、相同电荷量和相同数密度下，单种 Debye 长度与质量无关；热速度却随 $m^{-1/2}$ 变化，惯性长度与热回旋半径随 $m^{1/2}$ 变化。这解释了为何电子与离子可能对同一尺度的扰动作出不同响应。总静态 Debye 长度仍需按上一条对可响应组分求和，按逆平方规则组合。

统一输入 $1\,\mathrm{keV}=1.60218\times10^{-16}$ J。电子 $\omega_{pe}=5.64146\times10^{11}$ s⁻¹、$|\Omega_e|=8.79410\times10^{11}$ s⁻¹，代入本条公式即得各行。氘/电子质量比3670.48：速率除以其平方根，惯性长度与热回旋半径乘以其平方根，单种 Debye 长度不变。

应把梯度尺度、波长、轨道宽度和网格尺度分别与物理尺度比较；模型包含的物理与网格对该尺度的分辨能力需要分别确定。高能尾粒子的回旋半径应按实际 $m_sv_\perp/(|q_s|B)$ 计算。把 $v_t$ 的两种定义混用会产生 $\sqrt2$ 误差，而把角频率与普通频率混用会再引入 $2\pi$ 误差。

### 从速度分布求穿过平面的单向通量

速度的不同平均方式直接影响粒子通量。均匀各向同性 Maxwellian 穿过静止平面 $x=0$ 的正向通量为 $\Gamma_+=\int_{v_x>0}v_xf\,d^3v$。先积分 $v_y,v_z$，再令 $a=m/(2\Theta)$，用 $\int_0^\infty v_xe^{-av_x^2}dv_x=1/(2a)$，得到

$$
\Gamma_+=n\sqrt{\frac{\Theta}{2\pi m}}
=\frac{n\bar v}{4},\qquad
\bar v=\sqrt{\frac{8\Theta}{\pi m}}.
$$

积分的权重是穿过面积的法向速度，因此快粒子被采样的概率较大。正向通量非零，而对称分布的净通量 $\int v_xf\,d^3v$ 为零。壁面吸收、势垒和碰撞存在时，可在同一个积分上加入透射率及实际入射分布，保留清楚的速度权重。

**算例。** 给定电子 $n=10^{18}\,\mathrm{m^{-3}}$、$\Theta=20\,\mathrm{eV}=3.20435\times10^{-18}\,\mathrm J$，先求 $\sqrt{\Theta/(2\pi m_e)}=7.48231\times10^5\,\mathrm{m\,s^{-1}}$。乘密度得 $\Gamma_+=7.48231\times10^{23}\,\mathrm{m^{-2}s^{-1}}$，对应单向电子电流密度大小 $e\Gamma_+=1.19880\times10^5\,\mathrm{A\,m^{-2}}$。另一侧方向贡献相反的净电流；若一侧是吸收壁，建立的势场会改变入射分布。此处 $\bar v=2.99292\times10^6\,\mathrm{m\,s^{-1}}$，代回 $n\bar v/4$ 给同一结果。[MIT 第 1 章 §1.2.4，式 (1.25)–(1.28)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

## 磁化、碰撞与模型选择的独立判据

某一粒子种类是否磁化，取决于磁场能否在所研究过程的空间、时间和碰撞尺度上组织其轨道。定义带符号回旋角频率 $\Omega_s=q_sB/m_s$、正回旋频率大小 $|\Omega_s|$、回旋半径 $\rho_s=v_\perp/|\Omega_s|$。对缓变背景，常用的条件是

$$
\frac{\rho_s}{L_B}\ll1,
\qquad
\frac{\omega_{\mathrm{proc}}}{|\Omega_s|}\ll1,
\qquad
\frac{\nu_s}{|\Omega_s|}\ll1.
$$

一次回旋内，场强/方向变化约为 $\rho_s/L_B$、$\omega_{\rm proc}/|\Omega_s|$，散射概率约为 $\nu_s/|\Omega_s|$；沿场还需 $v_\parallel/(|\Omega_s|L_\parallel)\ll1$。这些是远小于一的量级排序，周期因子 $2\pi$ 不改变其含义。

$L_B$ 表示磁场大小及方向的有效变化尺度，$\omega_{\mathrm{proc}}$ 是过程特征角频率，$\nu_s$ 是明确指定的散射或动量弛豫率，单位 $\mathrm{s^{-1}}$。还应检查粒子沿磁力线运动时，一次回旋内遇到的磁场变化是否足够小；平行穿越引起的变化率还需满足 $v_\parallel/(|\Omega_s|L_\parallel)\ll1$。[UT Austin：Magnetized Plasmas，式 (1.29)–(1.33)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node10.html)；[Guiding Center Motion，式 (2.21)、(2.22)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node18.html)。

碰撞性则是另一组比较。若用同一种速度约定定义散射平均自由程 $\lambda_{\mathrm{mfp},s}=v_{ts}/\nu_s$，则 $\lambda_{\mathrm{mfp},s}/L$ 衡量粒子跨越长度 $L$ 时的散射程度，而 $\nu_s\tau$ 衡量时间 $\tau$ 内的累积散射。库仑“碰撞频率”统计许多小角偏转的累计效果；动量交换、偏转、慢化和能量交换频率分别按相应速度矩定义。[UT Austin：Collisions，式 (1.21)–(1.24)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node9.html)。

由定义直接得到 $\rho_{ts}/\lambda_{\mathrm{mfp},s}=\nu_s/|\Omega_s|$。因此可以同时具有 $\rho_s\ll\lambda_{\mathrm{mfp},s}\ll L$：粒子在两次显著散射之间完成很多回旋，但在跨越宏观系统之前仍经历很多散射。这是“磁化而有碰撞”的一致情形。也可以有 $\rho_s\ll L\ll\lambda_{\mathrm{mfp},s}$，即相对于该尺度近似无碰撞的磁化体系。这两种排序分别对应碰撞与近无碰撞的磁化模型。

对于 $B=5\,\mathrm T$，电子 $|\Omega_e|/(2\pi)\simeq140\,\mathrm{GHz}$，氘离子约为 $38.1\,\mathrm{MHz}$。但这个比较只说明电子回旋更快；要判断电子或离子磁化，仍须分别加入速度、梯度、过程频率与碰撞率。$|\Omega_e|/\omega_{pe}$ 比较两种本征频率，而轨道磁化使用前述梯度、过程和碰撞排序。

有限回旋半径、回旋共振、强碰撞和磁零点附近的运动需要超出最低阶导引中心描述。从磁化粒子模型约化到 MHD 时，MHD 还需相应的长波低频排序、闭合与组分约化。准中性、弱耦合、低碰撞和磁化应作为四个独立问题逐项说明，这比仅给体系贴上“热等离子体”标签更能确定一个公式是否可用。

### 由碰撞摩擦方程解出横向输运

采用速度无关摩擦频率 $\nu$ 的示范模型，均匀磁场沿 $z$，横向缓变驱动力密度对应每粒子力 $F_x$。稳态速度分量满足 $m\nu u_x=F_x+qBu_y$、$m\nu u_y=-qBu_x$。消去 $u_y$ 得
$u_x=F_x/[m\nu(1+\Omega^2/\nu^2)]$。若驱动来自定温压力梯度，$F_x=-\Theta\,\partial_xn/n$，乘 $n$ 后便是扩散通量：

$$
\Gamma_x=-D_\perp\partial_xn,\qquad
D_\perp=\frac{\Theta\tau/m}{1+\Omega^2\tau^2},\quad
D_\parallel=\frac{\Theta\tau}{m},\quad \tau=\nu^{-1}.
$$

单位为 $\mathrm{m^2\,s^{-1}}$。同一结果也可由速度相关函数 $\langle v_x(0)v_x(t)\rangle=(\Theta/m)e^{-t/\tau}\cos\Omega t$ 的时间积分获得；后者展示了回旋改变位移累积的机制。模型中的 $\nu$ 是给定摩擦率，完整库仑输运系数则由碰撞算子求得。

**算例。** 取氘离子 $\Theta=10\,\mathrm{eV}$、$B=0.10\,\mathrm T$、$\tau=1.0\,\mu\mathrm s$，得到 $\Omega\tau=4.79179$、$D_\parallel=479.179\,\mathrm{m^2\,s^{-1}}$，$D_\perp=19.9981\,\mathrm{m^2\,s^{-1}}$。横向扩散约为平行扩散的 $4.1734\%$。把磁场再增大两倍，强磁化极限中的横向系数约按 $B^{-2}$ 下降；平行运动方程中没有对应的磁偏转项。[Fitzpatrick，Magnetized Limit，输运系数及 $\Omega\tau$ 排序](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node56.html)。

[返回基础原理](../README.md)
