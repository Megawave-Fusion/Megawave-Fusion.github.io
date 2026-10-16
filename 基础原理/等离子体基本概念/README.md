# 等离子体基本概念

本专题从单位、分布函数和尺度比较建立等离子体物理的共同语言。以下主要讨论经典、非相对论、弱耦合等离子体；准中性、Maxwellian 分布、无碰撞和磁化都是需要分别检验的近似，不能互相替代。公式采用 SI；温度以 K 表示时写为 $T_s$，温度对应的能量写为 $\Theta_s=k_B T_s$。各条目中的算例是给定参数下的教学计算，不代表某一装置的实测状态。

## SI 单位、电子伏特与温度能量

等离子体文献常说“电子温度为 $1\,\mathrm{keV}$”。它表示 $k_B T_e$ 的能量值为 $1\,\mathrm{keV}$，并不是每个电子都具有相同的 $1\,\mathrm{keV}$ 动能。本知识库保留 $T_s$ 的开尔文单位，并用 $\Theta_s$ 表示温度能量，以减少同一字母在不同教材中的歧义：

$$
\Theta_s=k_B T_s,
\qquad
1\,\mathrm{eV}=1.602176634\times10^{-19}\,\mathrm J,
\qquad
k_B=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}.
$$

因此，$\Theta_s=1\,\mathrm{eV}$ 对应 $T_s\simeq1.16045\times10^4\,\mathrm K$，$1\,\mathrm{keV}$ 对应约 $1.16045\times10^7\,\mathrm K$。若记 $T_{s,\mathrm{eV}}=\Theta_s/(1\,\mathrm{eV})$，它是一个数值，例如在 $1\,\mathrm{keV}$ 时等于 $1000$；代入 SI 公式前，须把能量还原为焦耳。[NIST：2022 CODATA 常数表，electron volt 条目](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)；[MIT OCW：Introduction，§1.2.1，式 (1.17)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

常用符号中，$n_s$ 是数密度，单位 $\mathrm{m^{-3}}$；$q_s$ 是带符号的电荷，单位 C；电子有 $q_e=-e$，其中 $e>0$；$m_s$ 的单位是 kg；$\mathbf E$ 用 $\mathrm{V\,m^{-1}}$；$\mathbf B$ 用 T；$\varepsilon_0$ 用 $\mathrm{F\,m^{-1}}$。对 SI Lorentz 力，磁力项是 $q_s\mathbf v\times\mathbf B$，没有额外的 $1/c$。不能把某些 Gaussian-cgs 手册中的 $q_s\mathbf v\times\mathbf B/c$ 与 SI 的 tesla、coulomb 数值混用。

在各向同性的非相对论分布中，每粒子的平均无规则平动能是 $3\Theta_s/2$。例如温度能量 $\Theta_e=1\,\mathrm{keV}$ 的 Maxwellian 电子，其平均热动能为 $1.5\,\mathrm{keV}$；若存在整体流速 $\mathbf u_e$，实验室系平均动能还要加上 $m_eu_e^2/2$。这一步区分了温度与束流定向能量。低温体相与少量高能尾部共存时，单一温度也不能概括整个分布。[UT Austin：Fundamental Parameters，式 (1.1)–(1.4)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node5.html)。

**适用范围与误区。** 用 $m v^2/2$ 解释温度要求主要粒子处于非相对论范围；当电子能量不可忽略于 $m_ec^2\simeq511\,\mathrm{keV}$ 时，须改用相对论动量和分布。把 $T_e=T_i$ 当作必然结果、把 eV 当作电压单位、或者在 $n k_B T$ 中再次给已经用焦耳表示的 $\Theta$ 乘上 $k_B$，都会产生实质错误。

## 分布函数、密度、流速与温度的定义

速度分布函数 $f_s(\mathbf x,\mathbf v,t)$ 定义为：$f_s\,d^3x\,d^3v$ 是给定相空间小体积内的平均粒子数。这里采用数密度归一化，$f_s$ 的 SI 单位为 $\mathrm{s^3\,m^{-6}}$，不是积分为一的概率密度。其前两个速度矩给出密度和流速：

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

三个独立高斯积分分别给出 $n_s$、零平均相对速度和 $\langle c_{sx}^2\rangle=\Theta_s/m_s$，因此 $\mathsf P_s=n_s\Theta_s\mathsf I$。这个小推导说明 $p=n\Theta$ 中的 $n$ 必须与温度所指的粒子种类相配。电子和离子分别贡献压力；对单价纯氘且 $n_e=n_D=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=\Theta_D=1\,\mathrm{keV}$，每种压力约为 $1.602\times10^4\,\mathrm{Pa}$，总热压约为 $3.204\times10^4\,\mathrm{Pa}$。[MIT OCW：Introduction，§1.2.1 的 Maxwell–Boltzmann 分布](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

**适用范围与误区。** 磁化分布常需要 $p_{\parallel s}$ 与 $p_{\perp s}$，后者对应两个垂直自由度中的每一个方向；此时标量压力为 $(p_{\parallel s}+2p_{\perp s})/3$，不能随意选取一个方向的温度代替。两个不同的非 Maxwellian 分布可以有相同的 $n$、$\mathbf u$ 和温度，却具有不同的共振粒子数、热流和聚变反应率。测得温度并不等于测得完整分布。

## 准中性、净电荷与有限电场

准中性（quasineutrality）是宏观尺度上正负电荷密度近乎抵消的性质。对电子和多种正离子，

$$
\rho_q=\sum_s q_s n_s
=e\left(\sum_i Z_i n_i-n_e\right),
\qquad
n_e\simeq\sum_i Z_i n_i.
$$

$\rho_q$ 的单位是 $\mathrm{C\,m^{-3}}$；$Z_i$ 是离子的电荷数。对于氘、氚和完全电离氦的混合物，应写 $n_e\simeq n_D+n_T+2n_{\mathrm{He}}$，而不是把电子密度等同于总离子密度。杂质的每个电离态也应分别计入。[UT Austin：What is Plasma?，准中性定义](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node3.html)；[MIT OCW：Introduction，§1.1.2，式 (1.2)–(1.9)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

准中性并不要求 $\mathbf E=0$。在静电近似中，Poisson 方程是 $-\nabla^2\phi=\rho_q/\varepsilon_0$。若势变化尺度为 $L$、幅度为 $\phi_*$，由量纲估计得到

$$
\frac{|\rho_q|}{e n_e}
\sim \frac{\varepsilon_0\phi_*}{e n_e L^2}
=\left(\frac{\lambda_{De}}{L}\right)^2
\frac{e\phi_*}{\Theta_e},
\qquad
\lambda_{De}^2=\frac{\varepsilon_0\Theta_e}{n_e e^2}.
$$

该式是基于单一平滑尺度的估算，不是任意电势的严格误差界。当 $e\phi_*/\Theta_e$ 为一量级且 $L\gg\lambda_{De}$ 时，极小的电荷不平衡就足以支撑有限电场。例如 $n_e=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=1\,\mathrm{keV}$、$L=0.1\,\mathrm m$ 给出 $(\lambda_{De}/L)^2\simeq5.53\times10^{-8}$。这一量级说明不能因为密度近乎相等，就删除粒子动力学中的电场。

电荷中性和电流中性也是不同条件：$\mathbf j=\sum_s q_s n_s\mathbf u_s$ 还依赖各组分流速。单价等密度电子与离子若流速不同，仍可携带电流。反过来，各组分没有平均流动也不自动保证电荷中性。[UT Austin：Moments of Distribution Function，式 (4.7)、(4.8)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node47.html)。

**适用范围与误区。** 准中性常用于远离鞘层的低频、大尺度体等离子体；Debye 尺度结构、强双层和专门制备的非中性等离子体需要保留空间电荷。约化模型在最低阶令 $\rho_q=0$，是渐近排序中的近似，并不表示真实系统在所有阶都精确中性。准中性也不等于局域热平衡；快粒子、不同组分温度和各向异性都可以与之共存。

## Debye 屏蔽与多组分屏蔽长度

Debye 屏蔽描述近热平衡介质对微弱、近静态外加电势的密度重排。对可参与响应的 Maxwellian 组分，取远处电势为零，有

$$
n_s(\phi)=n_{s0}\exp\!\left(-\frac{q_s\phi}{\Theta_s}\right)
\simeq n_{s0}\left(1-\frac{q_s\phi}{\Theta_s}\right),
\qquad |q_s\phi|\ll\Theta_s.
$$

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

指数只修饰原有的 $1/r$ 势；屏蔽并不是在 $r=\lambda_D$ 处突然归零。[UT Austin：Debye Shielding，式 (1.11)–(1.15)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node7.html)。

必须区分电子 Debye 长度 $\lambda_{De}=\sqrt{\varepsilon_0\Theta_e/(n_ee^2)}$ 与总静态屏蔽长度。若离子在所考虑的响应过程中近似固定，仅保留电子项；若单价离子与电子均可达到上述 Boltzmann 响应，且密度相等、$\Theta_i=\Theta_e$，则 $\lambda_D=\lambda_{De}/\sqrt2$。一般单价等密度情形有 $\lambda_D^{-2}=\lambda_{De}^{-2}(1+\Theta_e/\Theta_i)$。因此不同教材的 $\sqrt2$ 差异往往来自参与屏蔽的组分不同。[MIT OCW：Introduction，§1.2.3，式 (1.19)–(1.24)，明确采用固定离子密度](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/0d55dc0f7c1c80046ebc862df0e8b314_chap1.pdf)。

**算例与限制。** 在 $n_e=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=1\,\mathrm{keV}$ 时，$\lambda_{De}\simeq23.5\,\mu\mathrm m$；等温单价双组分的总长度约为 $16.6\,\mu\mathrm m$。把温度提高四倍，电子屏蔽长度增大两倍；把密度提高四倍，它缩小两倍。该线性静态公式不直接描述强鞘层、束流尾迹、快速振荡或一般磁化非平衡响应；这些情形需要相应的动力学介电响应。尤其不能据此宣称等离子体会屏蔽所有随时间变化或垂直于磁场的电场。

## 集体效应、Debye 球粒子数与弱耦合

集体效应（collective behavior）是许多粒子通过自洽电磁场共同响应；它与两粒子间的强散射不是同一概念。对典型的经典弱耦合准中性等离子体，常用三类比较来判断所选近似是否适合：系统尺度相对于屏蔽长度、一个屏蔽体积中粒子的数量，以及集体响应频率相对于破坏该响应的碰撞率。它们分别约束空间范围、统计描述和时间演化，不能只检查其中一项。

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

对 $n_e=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=1\,\mathrm{keV}$，得到 $a_e\simeq1.34\times10^{-7}\,\mathrm m$、$\Gamma_e\simeq1.08\times10^{-5}$、$N_{De}\simeq5.44\times10^6$。这里大粒子数意味着屏蔽云可在适当平均意义下用连续密度描述；它不表示空间上没有涨落，也不保证湍流幅度小。多种高电荷离子可能有不同的耦合强度，不能只由电子的 $\Gamma_e$ 就代替所有组分的检查。

在弱耦合库仑理论中，碰撞率相对等离子体频率常具有 $\nu/\omega_p$ 与 $\ln N_D/N_D$ 同阶的缩放关系，但精确系数、库仑对数和碰撞率定义依赖具体过程。这里仅用它说明弱耦合集体响应可以快于碰撞，不能将该缩放外推至 $N_D\lesssim1$ 来计算强耦合体系。[UT Austin：Collisions，式 (1.21)–(1.27)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node9.html)。

**常见误区。** 弱耦合不等于无碰撞，长时间演化仍会积累碰撞效应；强耦合物质也可以是等离子体，只是上述 Debye–弱散射描述可能失效。“等离子体必须完全电离”也不正确：部分电离体系能有集体响应，但须把电子–中性粒子等碰撞纳入时间尺度比较。本文讨论的是聚变热等离子体常用近似，不是以三条不等式排除所有其他等离子体。

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

该简化模型忽略压力、碰撞、磁场和边界细节，说明的是频率的来源；不能用它替代一般色散关系。若多个冷组分都能运动，无磁、静电、均匀线性模型给出 $\omega^2=\sum_s\omega_{ps}^2$ 的电荷分离振荡分支。固定离子的电子振荡是其中的近似，而非声称所有频率都必须大于离子响应频率。

数值上，在 $n_e=10^{20}\,\mathrm{m^{-3}}$ 时，$\omega_{pe}\simeq5.64\times10^{11}\,\mathrm{rad\,s^{-1}}$，$f_{pe}\simeq89.8\,\mathrm{GHz}$；等密度单价氘的 $\omega_{pD}\simeq9.31\times10^9\,\mathrm{rad\,s^{-1}}$。频率随 $\sqrt n$ 增长；将密度提高四倍只使频率加倍。若密度以 $\mathrm{cm^{-3}}$ 输入常见工程公式，须先注意 $1\,\mathrm{cm^{-3}}=10^6\,\mathrm{m^{-3}}$，否则频率会相差一千倍。

**适用范围与误区。** 有限温度可带来波数依赖与动力学阻尼，磁场会改变模态与偏振。无磁冷电子介质中的横向电磁波截止与 $\omega_{pe}$ 相关，不表示所有磁化等离子体的波都在同一频率截止。$\omega\ll\omega_{pe}$ 常使电子有能力快速调整，但准中性是否成立还须同时检查 $k\lambda_{De}$、边界、驱动与所选分支。把 $\omega$ 直接按 Hz 代入或漏掉 $2\pi$ 是常见数值错误。

## 热速度、惯性长度与尺度表

热速度不是只有一种定义。本条对各向同性、非相对论 Maxwellian 的相对速度 $\mathbf c=\mathbf v-\mathbf u$，使用

$$
v_{ts}=\sqrt{\frac{2\Theta_s}{m_s}},
\qquad
\sigma_{v_x}=\sqrt{\frac{\Theta_s}{m_s}},
\qquad
v_{\mathrm{rms}}=\sqrt{\frac{3\Theta_s}{m_s}}.
$$

$v_{ts}$ 是三维速率分布 $4\pi c^2f_M(c)$ 的最概然速率；$\sigma_{v_x}$ 是任一笛卡尔分量的标准差；$v_{\mathrm{rms}}=\sqrt{\langle c^2\rangle}$ 是均方根速率，三者单位均为 $\mathrm{m\,s^{-1}}$。此外平均速率是 $\langle c\rangle=\sqrt{8\Theta_s/(\pi m_s)}$。这些区别可由高斯积分或对 $c^2\exp[-mc^2/(2\Theta)]$ 求极值直接检查；引用“thermal velocity”时应把定义一起写出。[UT Austin：Fundamental Parameters，式 (1.3)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node5.html)。

同一组分的 Debye 长度满足精确的定义关系

$$
\lambda_{Ds}=\frac{\sqrt{\Theta_s/m_s}}{\omega_{ps}}
=\frac{v_{ts}}{\sqrt2\,\omega_{ps}},
\qquad
d_s=\frac{c}{\omega_{ps}}.
$$

$d_s$ 是惯性长度，单位 m，$c$ 是光速。$\lambda_D$ 与 $d_s$ 的比值含热速度相对光速的因子，所对应的物理响应不同。$d_e$ 常称电子趋肤深度的特征尺度；实际电磁场衰减长度还依赖频率、碰撞和磁场，不能在所有驱动下都直接等于 $d_e$。例如固定离子、无磁、无碰撞冷电子模型有 $k^2c^2=\omega^2-\omega_{pe}^2$；在 $\omega<\omega_{pe}$ 时，衰减长度为 $c/\sqrt{\omega_{pe}^2-\omega^2}$，只有其低频极限才趋于 $d_e$。[UT Austin：Plasma Frequency，式 (1.7)、(1.8)](https://farside.ph.utexas.edu/teaching/plasma/lectures/node6.html)；[MIT OCW：Electromagnetic Waves，§5.2.1–§5.2.2，式 (5.53)–(5.57)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

以下取纯单价氘，$n_e=n_D=10^{20}\,\mathrm{m^{-3}}$、$\Theta_e=\Theta_D=1\,\mathrm{keV}$，回旋半径以 $v_{ts}$ 和 $B=5\,\mathrm T$ 计算：

| 物理量 | 电子 | 氘离子 |
| --- | --- | --- |
| $v_{ts}$ | $1.88\times10^7\,\mathrm{m\,s^{-1}}$ | $3.10\times10^5\,\mathrm{m\,s^{-1}}$ |
| 单种 $\lambda_{Ds}$ | $23.5\,\mu\mathrm m$ | $23.5\,\mu\mathrm m$ |
| $d_s=c/\omega_{ps}$ | $0.531\,\mathrm{mm}$ | $3.22\,\mathrm{cm}$ |
| $\rho_{ts}=v_{ts}/\lvert\Omega_s\rvert$ | $21.3\,\mu\mathrm m$ | $1.29\,\mathrm{mm}$ |

相同温度、相同电荷量和相同数密度下，单种 Debye 长度与质量无关；热速度却随 $m^{-1/2}$ 变化，惯性长度与热回旋半径随 $m^{1/2}$ 变化。这解释了为何电子与离子可能对同一尺度的扰动作出不同响应。总静态 Debye 长度仍需按上一条对可响应组分求和，不能把表中两项相加。

**使用方法与误区。** 应把梯度尺度、波长、轨道宽度和网格尺度分别与物理尺度比较；其中网格足够细只说明可能分辨某尺度，不证明所用模型包含该物理。热回旋半径也不能代替高能尾粒子的实际 $m_sv_\perp/(|q_s|B)$。把 $v_t$ 的两种定义混用会产生 $\sqrt2$ 误差，而把角频率与普通频率混用会再引入 $2\pi$ 误差。

## 磁化、碰撞与模型选择的独立判据

某一粒子种类是否磁化，取决于磁场能否在所研究过程的空间、时间和碰撞尺度上组织其轨道。定义带符号回旋角频率 $\Omega_s=q_sB/m_s$、正回旋频率大小 $|\Omega_s|$、回旋半径 $\rho_s=v_\perp/|\Omega_s|$。对缓变背景，常用的条件是

$$
\frac{\rho_s}{L_B}\ll1,
\qquad
\frac{\omega_{\mathrm{proc}}}{|\Omega_s|}\ll1,
\qquad
\frac{\nu_s}{|\Omega_s|}\ll1.
$$

$L_B$ 表示磁场大小及方向的有效变化尺度，$\omega_{\mathrm{proc}}$ 是过程特征角频率，$\nu_s$ 是明确指定的散射或动量弛豫率，单位 $\mathrm{s^{-1}}$。还应检查粒子沿磁力线运动时，一次回旋内遇到的磁场变化是否足够小；仅有垂直方向的 $\rho_s/L_B$ 小并不自动约束任意大的 $v_\parallel$。[UT Austin：Magnetized Plasmas，式 (1.29)–(1.33)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node10.html)；[Guiding Center Motion，式 (2.21)、(2.22)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node18.html)。

碰撞性则是另一组比较。若用同一种速度约定定义散射平均自由程 $\lambda_{\mathrm{mfp},s}=v_{ts}/\nu_s$，则 $\lambda_{\mathrm{mfp},s}/L$ 衡量粒子跨越长度 $L$ 时的散射程度，而 $\nu_s\tau$ 衡量时间 $\tau$ 内的累积散射。库仑“碰撞频率”通常统计许多小角偏转累积的效果，不是相邻两次微观相互作用的倒数；动量交换、偏转、慢化和能量交换频率也不是同一个数。[UT Austin：Collisions，式 (1.21)–(1.24)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node9.html)。

由定义直接得到 $\rho_{ts}/\lambda_{\mathrm{mfp},s}=\nu_s/|\Omega_s|$。因此可以同时具有 $\rho_s\ll\lambda_{\mathrm{mfp},s}\ll L$：粒子在两次显著散射之间完成很多回旋，但在跨越宏观系统之前仍经历很多散射。这是“磁化而有碰撞”的一致情形。也可以有 $\rho_s\ll L\ll\lambda_{\mathrm{mfp},s}$，即相对于该尺度近似无碰撞的磁化体系。两者都不是逻辑矛盾。

对于 $B=5\,\mathrm T$，电子 $|\Omega_e|/(2\pi)\simeq140\,\mathrm{GHz}$，氘离子约为 $38.1\,\mathrm{MHz}$。但这个比较只说明电子回旋更快；要判断电子或离子磁化，仍须分别加入速度、梯度、过程频率与碰撞率。尤其 $|\Omega_e|>\omega_{pe}$ 不是一般磁化条件，它比较的是两种本征频率，不代替前面的三个尺度条件。

**适用范围与误区。** 有限回旋半径、回旋共振、强碰撞和磁零点附近的运动需要超出最低阶导引中心描述。磁化也不自动意味着 MHD 适用；MHD 还需相应的长波低频排序、闭合与组分约化。准中性、弱耦合、低碰撞和磁化应作为四个独立问题逐项说明，这比仅给体系贴上“热等离子体”标签更能确定一个公式是否可用。

[返回基础原理](../README.md)
