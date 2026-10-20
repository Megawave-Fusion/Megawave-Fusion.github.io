# 低杂波电流驱动（LHCD / LHH）

低杂波电流驱动利用低杂频段的慢波与沿磁场高速运动的电子相互作用。其主要价值是非感应电流和电流剖面控制，但波能否从发射器进入核心、在哪里被吸收，与最终驱动多少电流是不同问题。本页于 2026-10-16 根据公开原论文、机构文档补充，围绕传播与电流响应展开。 对应计算流程见[模拟专题](../../仿真计算/低杂波电流驱动模拟/README.md)。

## 低杂慢波可达性与朗道共振

### 频率范围与朗道共振

在通常的磁化电子、较弱磁化离子条件下，低杂频段位于离子和电子回旋频率之间。单一离子组分、冷等离子体近似下，低杂共振可估为

$$
\omega_{LH}^2\simeq\Omega_i^2+
\frac{\omega_{pi}^2}{1+\omega_{pe}^2/\Omega_e^2}.
$$


这里 $\Omega_s=|q_s|B/m_s$、$\omega_{ps}^2=n_sq_s^2/(\epsilon_0m_s)$，均为角频率，单位 $\mathrm{rad\,s^{-1}}$。加热源工作在这一频段，并不意味着每个波包必须落在局部 $\omega=\omega_{LH}$ 共振层。LHCD 的主要电子吸收机制是平行电场的朗道作用：$\omega-k_\parallel v_\parallel=0$。定义 $N_\parallel=ck_\parallel/\omega$ 后，共振电子满足 $v_\parallel=c/N_\parallel$。[Wallace 等，FNSF 原论文 §2.1](https://library.psfc.mit.edu/catalog/reports/2010/17ja/17ja024/17ja024_full.pdf)

发射谱向一个平行方向偏置，波对相应电子群进行准线性扩散，碰撞和粒子输运则不断松弛该分布，最终形成携带电流的快电子尾。若正负方向对称，吸收可以很强而净电流很小。电流方向按电子负电荷定义，必须说明是电子流向还是常规电流方向。[Wallace 等，CFETR 研究 §1–§2](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)

### 可达性与吸收之间的窗口

一个常用的冷、局部、单离子近似可达性条件是

$$
|N_\parallel|\gtrsim N_{acc}=
\frac{\omega_{pe}}{\Omega_e}
+\sqrt{1+\frac{\omega_{pe}^2}{\Omega_e^2}-\frac{\omega_{pi}^2}{\omega^2}}.
$$


它表示慢波分支在传播途中避免与快波分支合并而失去可达性的一项必要约束；根号内量、频率区间和局部参数需满足该推导的适用条件。边缘耦合与全路径传播随后分别求解。密度升高增加 $\omega_{pe}$，较强磁场增大 $\Omega_e$；所以高场侧发射可能扩大允许的传播窗口，最终沉积位置由沿程折射和阻尼决定。[CFETR 原论文，式 (2) 与 §2](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)

可达性公式来自两个冷波根的分离条件，而非把 $\omega=\omega_{LH}$ 代入共振式。取磁场沿 z，波矢在 x-z 平面；将冷波矩阵的行列式按 $x=N_\perp^2$ 展开，得到 $Sx^2-[RL+SP-(S+P)N_\parallel^2]x+P(R-N_\parallel^2)(L-N_\parallel^2)=0$。这里 S、D、P、R、L 的定义与[冷介电张量](../离子回旋加热/README.md#MF000136)相同，x 的两个根对应该频段的快、慢分支。对 $\Omega_i\ll\omega\ll\Omega_e$ 的高密度近似代入介电分量，在分支合并边界令判别式为零，慢波可达一侧写成 $(|N_\parallel|-a)^2\gtrsim1+a^2-b$，其中 $a=\omega_{pe}/\Omega_e$、$b=\omega_{pi}^2/\omega^2$。选取与慢波连续连接的 $|N_\parallel|\ge a$ 一支并开方，即得到上面的 $N_{acc}$。完整冷波根与热传播路径可继续检验这一约化条件。

较低 $|N_\parallel|$ 选择碰撞较弱的高速电子，但受可达性及尾电子数约束。对非相对论通行电子，$I_e=ev/(2\pi R)$、$P_{\rm drag}\sim m_e\nu v^2$，结合 $\nu\propto n_e/v^3$ 得

$$
\frac IP\propto\frac{v^2}{n_eR}\propto\frac1{n_eR N_\parallel^2}.
$$

此缩放忽略俘获、相对论及有限分布宽度。高 $|N_\parallel|$ 更易在外层提前吸收。 [FNSF 原论文，§2.1](https://library.psfc.mit.edu/catalog/reports/2010/17ja/17ja024/17ja024_full.pdf)。

### 发射谱不等于吸收谱

波沿环形磁场传播时，局部 $k_\parallel$ 由波矢与磁场的投影决定；极向折射、磁剪切和几何变化会使 $N_\parallel$ 上移或下移。轴对称性约束环向模数，却不使整个 $N_\parallel$ 沿射线恒定。边缘密度涨落还可能散射波束。因此模型必须报告吸收处的谱和沉积，将天线谱沿传播更新后用于解释电流效率。[CFETR 原论文，式 (3)–(4) 及 §4](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)

### 由冷介电分量求低杂共振尺度

在 $|\Omega_e|\gg\omega$ 下，把冷介电分量写成 $S\simeq1+\omega_{pe}^2/\Omega_e^2-\omega_{pi}^2/(\omega^2-\Omega_i^2)$。令 S=0，先移项得到 $\omega_{pi}^2/(\omega^2-\Omega_i^2)=1+\omega_{pe}^2/\Omega_e^2$，再取倒数即得到上文的 $\omega_{LH}^2$。在高密度单电荷氢同位素极限，结合准中性有 $\omega_{pi}^2/\omega_{pe}^2=m_e/m_i$，主项进一步趋于 $|\Omega_e|\Omega_i$，显示该频率位于电子与离子回旋尺度之间。[冷介电分量的起点，Fitzpatrick 式 (5.31)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)

### 从可达折射率反求密度窗口

在忽略可达性根式中的离子修正项时，记 $a=\omega_{pe}/\Omega_e$，有 $N_{acc}=a+\sqrt{1+a^2}$。要求给定 $N_\parallel=N>1$ 满足可达性，先移项再平方：$(N-a)^2\ge1+a^2$，整理得 $a\le(N^2-1)/(2N)$。最后用 $\omega_{pe}^2=n_ee^2/(\epsilon_0m_e)$，得到 $n_e\le\epsilon_0B^2[(N^2-1)/(2N)]^2/m_e$。

设 $N=2$、$B=3$ T，则 $a$ 上限为 0.75，局部密度上限约 $4.920\times10^{19}$ m⁻³。若磁场增至 6 T，同一近似窗口扩大四倍；这解释高场侧注入的物理吸引力。另一方面，$v_{res}=c/N$ 在 N=2 时为 0.5c，最低相对论电子动能约 79.05 keV。设计时在每个沿程位置同时画出可达性与电子分布响应，便能把“进入高密度区”和“在希望的位置沉积”这两个要求联系起来。

![局部冷近似下，曲线低于给定发射折射率才满足这一可达性条件。](/assets/diagrams/heat-lh.svg)

局部冷近似下，曲线低于给定发射折射率才满足这一可达性条件。

推导起点与参考位置：[CFETR LHCD scoping study，§2，式 (1)–(4)](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)。

## 波导阵列与平行发射谱

微波放大源将功率送入分配网络；移相器控制相邻波导的相位差，多波导口发射器把这些场组合为有方向性的谱。对于沿平行方向间距为 $d$、相邻相位递增为 $\Delta\phi$ 的理想阵列，按场约定 $\sum_m A_m\exp[i(m\Delta\phi-k_\parallel md)]$，主峰近似满足 $k_\parallel d=\Delta\phi$ 模 $2\pi$。因此主峰 $N_\parallel\simeq c\Delta\phi/(\omega d)$；改变相位会改谱，也会改变电流驱动方向。

有限孔径、幅相误差、栅瓣和互耦共同改变加载后的谱。真空测相位需经等离子体负载修正；窗、隔离负载和水冷按反射及长脉冲热平衡核算。 [CFETR 原论文对主瓣、旁瓣和阵列宽度的说明，§2](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)。

慢波需要近场耦合到等离子体；孔口附近密度过低会形成较宽的倏逝区、加大反射。把发射器移近等离子体有时改善耦合，却增加热流和粒子轰击，运行点应同时满足耦合与部件负荷要求。DIII-D 高场侧研究因此专门测量刮削层密度，并将其输入三维全波耦合模型。[MIT PSFC 2025 年学位论文摘要：高场侧刮削层与 LHCD](https://library.psfc.mit.edu/catalog/reports/2020/25rr/25rr013/abstract.php)

### 有限波导阵列怎样形成平行谱

考虑 M 个等幅口径，间距 d、相邻驱动相位差 $\Delta\phi$。其阵列因子 $A(k)=\sum_{m=0}^{M-1}\exp[im(\Delta\phi-kd)]$ 是几何级数，化为相位因子乘 $\sin(M\psi/2)/\sin(\psi/2)$，其中 $\psi=\Delta\phi-kd$。主瓣位于 $k=\Delta\phi/d$；最近零点满足 $\Delta k=\pm2\pi/(Md)$，所以有限口径必然给出有限谱宽。

取 $f=3.7$ GHz、$d=10$ mm、$\Delta\phi=\pi/2$、M=32，则主瓣 $k_\parallel=157.08$ m⁻¹、$N_\parallel\simeq2.026$，两侧第一零点相距主峰的 $\Delta N$ 约为 0.253。把 M 减为 16，零点距离加倍。相位控制改变谱中心，阵列长度改变谱宽，单元口径与等离子体负载再给阵列因子乘上各自响应。通过直接复数求和与正弦表达式对比，可以检查相位正负号、端口编号和谱归一化。

推导起点与参考位置：[MIT Electromagnetic Fields and Energy，§14.6，反射与阻抗变换](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)；[CFETR LHCD scoping study，§2，式 (1)–(4)](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)。

## LH 沉积计算与电流效率

计算链为发射器全波耦合 → 传播与吸收 → Fokker–Planck 电子分布/电流。射线要求局部波长远小于背景尺度；近场、衍射与涨落需对应波动模型，强快尾需迭代阻尼。

一个独立量级检查是 $N_\parallel=2$ 时 $v_\parallel=0.5c$。若假定电子没有垂直速度，其相对论动能为

$$
E_\parallel^{min}=m_ec^2\left[(1-N_\parallel^{-2})^{-1/2}-1\right]
\simeq79.1\,\mathrm{keV}.
$$


这是满足该平行速度的最小总能量，作用电子仍覆盖完整共振速度区域。用非相对论 $m_ev^2/2$ 会给约 63.9 keV，在这里已有明显差别。高温或强快电子尾计算应采用合适的相对论动理学描述。[CFETR 原论文，§2.1 对相对论 CQL3D 的说明](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)

效率常定义为 $\eta=\bar n_e R_0 I_{CD}/P_{LH}$，SI 单位为 $\mathrm{A\,W^{-1}m^{-2}}$；若把密度改写为 $10^{20}\,\mathrm{m^{-3}}$ 单位，其数值也相应缩放，必须注明。$P_{LH}$ 是源输出、净耦合还是核心吸收功率，会改变效率数值。射线全部最终吸收的理想计算若没有边缘损失，不应与含发射器损耗的实验分母直接比较。

高密度下效率下降并非单一“密度上限”就能解释。边缘碰撞吸收、参数不稳定性、波谱散射和单程吸收不足可共同改变核心沉积。2018 年多装置研究指出较热、较低再循环的边缘有利于减少寄生损失，但其摘要也明确要求更多实验与交叉建模；该趋势应结合各装置的边缘参数检验。[Ding 等，2018 年论文机构摘要](https://research.chalmers.se/en/publication/528652)

为理解可达性与驱动的竞争，可在忽略 $\omega_{pi}^2/\omega^2$ 的进一步近似中令 $a=\omega_{pe}/\Omega_e$，得到 $N_{acc}\simeq a+\sqrt{1+a^2}$。当 $a$ 从 0.5 增至 1，最低可达折射率从约 1.62 增至约 2.41；对应的平行相速度下降。这一局部冷模型与温度剖面、边缘耦合和沿路折射共同构成设计输入。它说明提高密度的同时，往往需要重新优化相位谱或发射位置，保持原谱不变未必仍能实现原沉积目标。[FNSF 原论文的可达性条件](https://library.psfc.mit.edu/catalog/reports/2010/17ja/17ja024/17ja024_full.pdf)

总电流存在参数退化，须同时比较尾电子能谱、空间分布和沉积半径。

### 效率归一化及输入误差传播

定义 $\eta_{CD}=n_eRI_{CD}/P$ 后，逐步解出 $I_{CD}=\eta_{CD}P/(n_eR)$，其量纲为 A。若把 $n_{20}=n_e/10^{20}$，电流用 MA、功率用 MW，则常用数值 $\eta_{20}=n_{20}RI_{MA}/P_{MW}=\eta_{CD}/10^{20}$。对独立小误差作对数微分，可得相对方差是 n、R、I、P 四项相对方差之和。

教学输入 $n_e=3\times10^{19}$ m⁻³、R=2 m、$I_{CD}=100$ kA、P=1 MW，得到 $\eta_{CD}=6\times10^{18}$ A/(W·m²)，即 $\eta_{20}=0.060$。四个量的相对标准不确定度若依次为 5%、1%、10%、3%，合成为 11.62%，故 $\eta_{20}=0.060\pm0.007$。在假定效率和几何保持相同的参数练习中，密度加倍会令电流减半；实际扫描则重新计算传播、吸收与碰撞响应，用测量判断该缩放保持多大范围。

推导起点与参考位置：[CFETR LHCD scoping study，§2，式 (1)–(4)](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)。

## 幅相控制与反射功率测量

单通道跳闸同时改变功率、主副瓣和局部电压；保护按各通道复幅值及网络模型决定降额或撤功率。

反射功率升高可能来自边缘密度变化、位置变化、打火或器件故障，处理时应结合真空、弧光、温度和等离子体信号区分原因。功率源功率扣除反射得到的是某计量面上的净前向功率，其中仍可能包括窗、波导或边缘的损耗，核心加热由后续吸收与热响应确定。边缘耦合控制与设备保护需协同，供气优化同时考虑整体密度、再循环和吸收变化。[MIT PSFC：高场侧刮削层摘要](https://library.psfc.mit.edu/catalog/reports/2020/25rr/25rr013/abstract.php)，[Ding 等机构摘要](https://research.chalmers.se/en/publication/528652)

### 方向耦合器的泄漏如何影响反射功率

令真实反射电压比为 $\Gamma$，方向性为 D dB 的测量通道带有入射波泄漏幅度 $\epsilon=10^{-D/20}$。测得复幅比为 $\Gamma_m=\Gamma+\epsilon e^{i\phi}$，展开模平方得 $|\Gamma_m|^2=|\Gamma|^2+\epsilon^2+2|\Gamma|\epsilon\cos\phi'$，其中 $\phi'$ 是两复幅的相对相位。因此固定泄漏幅度时，反射功率份额在 $(|\Gamma|-\epsilon)^2$ 与 $(|\Gamma|+\epsilon)^2$ 之间变化。若标定只给泄漏幅度的上限，则下界应改为 $[\max(0,|\Gamma|-\epsilon)]^2$。误差在复幅值上叠加，随后才取模平方；功率信号之间的简单相减无法描述未知相位泄漏。

取正向功率 1 MW、真实反射 40 kW，即 $|\Gamma|=0.2$；方向性为 30 dB 时 $\epsilon=0.03162$。不同泄漏相位可使测值位于约 28.35–53.65 kW，而真实驻波比为 $(1+0.2)/(1-0.2)=1.5$。验收可用已知反射负载和相位扫描测出这个误差包络，运行中则把标定后的复数校正用于反射估计。这样设置功率回退逻辑时，可以把负载变化与仪器串扰分别计入判断。

推导起点与参考位置：[MIT Electromagnetic Fields and Energy，§14.6，反射与阻抗变换](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)。

## 环电压响应与非感应电流识别

冷态网络确定复幅值、互耦和参考面；高功率负载试验检查源、窗、传输和热稳定性，等离子体扫描再检验边缘加载。谱计算注明时空相位约定。

硬 X 射线可提供快电子尾的证据，但其辐射强度还依赖能谱、密度、杂质和观测几何，电流反演需要结合电子分布和磁平衡。环电压变化同时包含电阻率变化和磁通扩散；实际 $I_{LH}$ 需要电流平衡、磁平衡/内部磁场约束以及温度密度诊断共同分析。原始时间窗要足够区分波功率快速响应与较慢电流扩散，且应对邻近的无 LH 放电或功率调制进行比较。[MIT PSFC RR-14-01，第 1 章研究动机与诊断方法](https://library.psfc.mit.edu/catalog/reports/2010/14rr/14rr001/14rr001_full.pdf)

验证同时解释耦合功率、快电子谱和电流剖面，避免仅拟合总电流。

### 环电压、电阻率与驱动电流的分离

在固定几何的零维电路模型中，先把总电流分为欧姆部分 $I_{Ohm}=I_p-I_{NI}$，其电阻压降为 $R_pI_{Ohm}$；再把磁通变化的感应压降写为 $d(L_pI_p)/dt$。当等效电感 $L_p$ 固定时，两项相加得 $V_{loop}=R_p(I_p-I_{NI})+L_p\dot I_p$，其中 $R_p$、$L_p$ 分别用 Ω、H。稳态电流下去掉电感项，再得到 $I_{NI}=I_p-V_{loop}/R_p$。这里电阻率随电子温度及杂质变化，故射频既可能增加非感应电流，也可能通过升温降低维持同一欧姆电流所需的环电压；剖面变化时还要用空间电流扩散模型取代单电阻模型。

设 $I_p=0.50$ MA、$R_p=2.0$ μΩ，纯欧姆维持需 1.00 V。射频期间测得 0.80 V：若独立诊断确认电阻仍为 2.0 μΩ，模型给出 $I_{NI}=100$ kA；若升温使电阻降至 1.6 μΩ，同样的 0.80 V 可维持全部 0.50 MA 欧姆电流。这个两情景比较说明为什么需结合温度、有效电荷、电流扩散及磁平衡重建。长脉冲验收还应使模型跨越电流扩散时间，比较整个时间序列。

推导起点与参考位置：[CFETR LHCD scoping study，§2，式 (1)–(4)](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)；[Poli 等，Fast evaluation of EC driven current，§2、式 (8)–(19)](https://pure.mpg.de/rest/items/item_3018972_4/component/file_3023894/content)。

## 高场侧注入如何兼顾可达性与沉积位置

高场侧发射的吸引力来自较低的 $\omega_{pe}/\Omega_e$，但系统设计还要同时决定波导谱、边缘耦合和沿程阻尼。[Wallace 等 CFETR 研究](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)在指定磁平衡与温度密度剖面下连接射线传播和 Fokker–Planck 电流预测；其结果属于所设设计工况的模型研究。高场侧刮削层的密度输入则由边缘诊断约束，见 [MIT 高场侧 LHCD 研究摘要](https://library.psfc.mit.edu/catalog/reports/2020/25rr/25rr013/abstract.php)。

### 磁场优势需要连同密度一起核算

从 $\omega_{pe}=\sqrt{n_ee^2/(\epsilon_0m_e)}$ 和 $\Omega_e=eB/m_e$ 相除，得到 $a=\sqrt{n_em_e/\epsilon_0}/B$。因此两位置 H、L 的比值为

$$
\frac{a_H}{a_L}=\sqrt{\frac{n_H}{n_L}}\frac{B_L}{B_H}.
$$


忽略离子修正时 $N_{acc}=a+\sqrt{1+a^2}$。取 $a_L=1$、$B_H/B_L=2$、$n_H/n_L=1.5$，得 $a_H=0.61237$，$N_{acc}$ 由 2.4142 降至 1.78498，使 $|N_\parallel|=2$ 局部可达；密度增至四倍则恰抵消此磁场优势。

### 环形几何会继续移动平行谱

沿磁场的波数是投影 $k_\parallel=\mathbf k\cdot\mathbf B/B$。在轴对称平衡中环向模数 $n_\phi$ 守恒，故 $k_\phi=n_\phi/R$，进而

$$
N_\parallel=\frac c\omega
\left(\frac{n_\phi B_\phi}{RB}+\frac{k_\theta B_\theta}{B}\right).
$$


这由波矢投影与环向相位 $n_\phi\phi$ 的空间梯度得到；$k_\theta$ 是局部极向波数。环向场占优时，第一项近似与 $1/R$ 成正比。作为单独的几何估算，同一环向模数从 R 到 R/2，会把这一贡献加倍；若原本 $N_\parallel\simeq2$，忽略极向项时变为约 4。局部可达性改善的同时，电子共振速度便从 c/2 降到 c/4，高能碰撞模型的效率尺度降低为原来的四分之一。真实射线中极向折射和磁剪切也会改变第二项，必须沿路求解。

高场侧方案需重选环向谱和极向发射位置，逐点检查慢支连续性、寄生损失与共振电子。以 $p_{abs}(\rho)$、吸收处 $N_\parallel$ 谱和 $j_{CD}(\rho)$ 联合评价；吸收过早偏外，过晚增加边界返回。 [CFETR 研究 §2、式 (1)–(4) 及 §4](https://library.psfc.mit.edu/catalog/reports/2020/21ja/21ja016/21ja016_full.pdf)。

[返回辅助加热](../README.md) · [编写说明](../../编写说明.md) · [返回知识库](../../README.md)
