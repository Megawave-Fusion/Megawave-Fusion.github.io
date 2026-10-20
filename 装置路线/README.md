# 聚变装置与约束构型

聚变路线按磁拓扑、压力、约束时间和载荷通道比较。高温、长脉冲或中子产生各有测量边界；净发电另需厂级收支。本页是原理与证据整理稿，资料访问日期为 2026-10-16。

## 托卡马克

![解析电流剖面的安全因子与静态磁镜的初始方向损失锥](/assets/diagrams/basic-devices.svg)

*解析电流剖面的安全因子与静态磁镜的初始方向损失锥。曲线与示意均按本条所列模型生成。*

### 螺旋磁场与安全因子

托卡马克以近似轴对称的环形磁面约束等离子体。外部环向场线圈提供主要环向磁场，等离子体环向电流产生极向场；外部极向场线圈同时参与位置、形状和平衡控制。两种场叠加使磁力线绕着磁面螺旋前进。环向场的曲率和梯度漂移使粒子偏离原磁面；极向场带来的螺旋运动有助于平均这种漂移。[IPP《Tokamak》，磁场组成与电流驱动段](https://www.ipp.mpg.de/9778/tokamak)。

安全因子 $q$ 表示磁力线绕极向一周时的环向圈数。在大环径比、近圆截面且局部磁场近似成立时，

$$
q(r)\simeq\frac{rB_\phi}{R_0B_\theta(r)},\qquad
B_\theta(r)\simeq\frac{\mu_0I_p(r)}{2\pi r}.
$$

$r,R_0$ 为小半径与主半径，单位 m；磁场单位 T；$I_p(r)$ 是所包围的电流，单位 A。式子来自磁力线几何和安培环路定律，强整形和球形托卡马克则需采用相应几何的平衡模型。举一个解析教学例：取 $r=0.5\,\mathrm m,R_0=2\,\mathrm m,B_\phi=3\,\mathrm T,I_p(r)=0.5\,\mathrm{MA}$，得到 $B_\theta=0.20\,\mathrm T,q\simeq3.75$。这里 $q$ 描述磁力线螺距。撕裂模对 $q=m/n$ 的有理磁面敏感，判断稳定性还要看电流、压力、剪切、旋转与壁面条件。[Fitzpatrick，撕裂模讲义，式 (4.35)–(4.40)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node71.html)。

近圆磁面的几何关系 $r\,d\theta/(R_0d\phi)=B_\theta/B_\phi$ 给出 $q$；安培环路 $2\pi rB_\theta=\mu_0I_p(r)$ 给出极向场。扰动相位 $m\theta-n\phi$ 沿场不变时，$m-nq=0$。

固定电感的磁通链、电路和平均功率满足

$$
\Psi=LI,\quad V=\dot\Psi+RI=L\dot I+RI,\qquad
\overline P=\Delta W/\Delta t,\quad A=R_0/a.
$$

### 电流维持、稳态和破裂

变压器感应电流需要磁通变化，可用的磁通摆幅有限，因此纯感应驱动通常是脉冲运行。非感应方案由外加波或束流驱动电流，并利用压力梯度产生的自举电流；稳态要求电流剖面、热量、密度、杂质和壁温都能维持。超导线圈使长时磁场成为可能，但不会自动解决等离子体电流维持及排热。[IPP《Tokamak》，末两段](https://www.ipp.mpg.de/9778/tokamak)。

磁能变化与电流变化通过电感相连：简化电路满足 $V=L\,dI/dt+RI$。托卡马克破裂可能伴随快速热能损失、随后电流下降、电磁载荷及逃逸电子。热能 $W$ 在较短时间 $\Delta t$ 释放时，平均释放功率约为 $W/\Delta t$；落点面积和辐射分配又决定局部热流，局部损伤由空间和时间分配共同决定。ITER 的破裂缓解资料说明其设计的后果控制与系统方案。[ITER《Disruption mitigation》，破裂后果与系统方案](https://www.iter.org/machine/supporting-systems/disruption-mitigation)。

球形托卡马克通过较小环径比 $A=R_0/a$ 改变平衡和稳定性条件，常研究较高的归一化压力，但中央柱、屏蔽和维护空间也更紧。常规与球形装置比较时，必须同时报告压力定义、磁场位置、等离子体体积及加热功率及其空间和时间分布。

### 从电流密度剖面推到有理磁面

在圆柱近似中，给定 $j_\phi(r)=j_0(1-r^2/a^2)$，先对面积积分：

$$
I_p(r)=2\pi\int_0^r j_\phi(r')r'dr'
=\pi j_0\left(r^2-\frac{r^4}{2a^2}\right).
$$

再由安培定律求 $B_\theta=\mu_0I_p(r)/(2\pi r)$，代入磁力线螺距定义，得到

$$
q(r)=\frac{2B_\phi}{\mu_0R_0j_0}
\frac{1}{1-r^2/(2a^2)},\qquad
j_0=\frac{2I_p(a)}{\pi a^2}.
$$

教学取 $a=0.60$ m、$R_0=2.5$ m、$B_\phi=3.0$ T、总电流 $1.0$ MA，求得 $j_0=1.77$ MA/m²、$q(0)=1.08$、$q(a)=2.16$。令 $q(r_s)=2$，解得 $r_s/a=\sqrt{0.92}=0.959$。这个计算展示了“电流分布→极向场→磁剪切→共振面”的因果链：总电流相同而中心峰化程度不同，也会得到不同的内部 $q$ 剖面。积分中的 $I_p$ 用 A，半径用 m；几何假设是大环径比、近圆磁面及近恒定环向场。[Fitzpatrick《Cylindrical Tokamak Equilibrium》，式 (3.1)–(3.3)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node50.html)提供所用场与安全因子的定义。

## 场反位形 FRC

FRC 是以极向磁场为主、环向磁场很小或没有宏观环向磁场的紧凑环形构型。环向电流产生与外加轴向场相反的内部磁场；分离面区分闭合磁力线区和外部开场线区。其较高的等离子体压力与外部磁压相平衡，适合用外部参考场定义

$$
\beta_{\rm ref}=\frac{2\mu_0\langle p\rangle}{B_{\rm ref}^{2}}.
$$

$p$ 用 Pa，$\beta$ 无量纲。必须写清体平均范围和 $B_{\rm ref}$：磁场反转附近可能有磁零点，把局部 $p/B^2$ 的大值直接称为整机高效率没有意义。高 $\beta$ 表示相对于参考磁场的压力较大，并不直接给出能量约束时间或聚变增益。

磁压为 $\int_0^B B\,dB/\mu_0=B^2/(2\mu_0)$。由 Lorentz 力平衡 $mv_\perp^2/\rho=|q|v_\perp B$，得 $\rho=v_\perp/|\Omega|$；局部磁化还要求 $\rho/a\ll1$。

FRC 的离子轨道可与装置尺度可比。定义 $\rho_i=v_\perp/\Omega_i$、$\Omega_i=Z_ieB/m_i$，则 $\rho_i/a\ll1$ 才有利于局部导引中心近似。教学例取氘离子垂直动能 $10\,\mathrm{keV}$、参考场 $0.5\,\mathrm T$，由 $v_\perp=\sqrt{2E_\perp/m_D}$ 得 $\rho_D\approx0.041\,\mathrm m$；若 $a=0.20\,\mathrm m$，比值约 0.20，有限轨道宽度需要纳入分析，靠近磁零点时更须完整轨道处理。

因此，纯理想 MHD 对倾斜模的预测与实验表现之间，可能需要离子动理学、快离子、流动和导电壁解释。Belova 等的混合模拟研究具体分析了倾斜模、旋转模和束离子稳定作用，揭示了构型与动理学稳定机制之间的联系。[PPPL-4150 / Physics of Plasmas 13, 056115 (2006)，摘要及动力学稳定性分析](https://bp-pub.pppl.gov/pub_report/2006/PPPL-4150.pdf)。

形成方式包括磁场反转的脉冲形成与等离子体合并；维持方案可涉及中性束注入或旋转磁场。旋转磁场通过电子响应驱动电流，其作用取决于频率、穿透和等离子体响应。诊断要分别给出分离面、磁通、密度、电子/离子温度、快离子分布、输入功率和持续时间。PPPL 的 PFRC 是其中一种特定射频驱动研究方案，具有自己的构型和运行参数。[PPPL《Princeton Field-Reversed Configuration》，概念说明](https://www.pppl.gov/Princeton-Field-Reversed-Configuration)。

### 抗磁压强怎样支持高比压

用长直、轴对称的轴向场模型理解 FRC 中段的抗磁平衡。取 $\mathbf B=B_z(r)\mathbf e_z$，安培定律给出 $J_\theta=-\mu_0^{-1}dB_z/dr$。径向力平衡 $dp/dr=J_\theta B_z$ 随即化为

$$
\frac{d}{dr}\left(p+\frac{B_z^2}{2\mu_0}\right)=0,
\qquad
p(r)=p_{\rm edge}+\frac{B_{\rm edge}^2-B_z(r)^2}{2\mu_0}.
$$

磁场幅值下降的区域因此由更大的粒子压强补足总压强。在 $B_z=0$ 处，取教学边界 $B_{\rm edge}=0.80$ T、$p_{\rm edge}\simeq0$，得到 $p=255$ kPa。对氘等离子体 $n_e=n_i=10^{20}$ m⁻³，各向同性动量通量给出 $p_s=n_s\Theta_s$，其中 $\Theta_s=k_BT_s$ 用 J，因而 $p=n_e(\Theta_e+\Theta_i)$。代入 $p=0.80^2/(2\mu_0)=2.55\times10^5$ Pa，再除以 $10^{20}$ m⁻³，得到温度能量之和 $2.55\times10^{-15}$ J，即 $15.9$ keV；例如 $\Theta_e=5.0$ keV 对应 $\Theta_i=10.9$ keV。计算用的是压力平衡和外部参考场。完整 FRC 的端部弯曲、轴向变化和非磁化离子轨道需要二维平衡与动理学模型；其重要尺度见 [Belova 等，PPPL-4150，摘要与第 I 节](https://bp-pub.pppl.gov/pub_report/2006/PPPL-4150.pdf)。

## 磁镜

磁镜以中部较弱、两端较强的磁场使部分带电粒子反射。若磁场沿轨道变化足够缓慢，磁矩 $\mu=mv_\perp^2/(2B)$ 近似守恒；在静态、可忽略电势差的条件下，总动能也守恒。粒子走向强场时，垂直能增加、平行能减少，到 $v_\parallel=0$ 处反射。这一反射机制按粒子的俯仰角选择被约束的轨道。[Fitzpatrick《Magnetic Mirrors》，式 (2.83)–(2.90)](https://farside.ph.utexas.edu/teaching/plasma/Plasma/node22.html)。

设镜比 $R_m=B_{\max}/B_{\min}$，中部俯仰角 $\alpha$ 为速度与磁场的夹角，则理想捕获条件为

$$
\sin^2\alpha>\frac1{R_m},\qquad
\alpha_{\rm lc}=\arcsin\!\left(R_m^{-1/2}\right).
$$

接近平行或反平行方向的两个锥区称为损失锥。若 $R_m=4$，半角为 $30^\circ$。对于中部初始速度方向各向同性的粒子，两端损失锥占总立体角的比例为 $1-\cos\alpha_{\rm lc}\approx13.4\%$。这个数只描述该理想瞬间的几何比例；稳态损失率还由散射与供源共同确定：碰撞会持续向损失锥散射粒子，电势差会改变逃逸条件，分布各向异性也可能驱动不稳定性。

由 $\mu B_{\min}=E\sin^2\alpha$、镜点 $\mu B_{\rm turn}=E$，得 $B_{\rm turn}=B_{\min}/\sin^2\alpha$。两锥立体角除以 $4\pi$ 给 $f_{\rm lc}=1-\cos\alpha_{\rm lc}$；这里只用磁化、慢变轨道的不变量。 [单粒子运动](../基础原理/单粒子运动/README.md)。

镜装置的工程特点是端部可用于加热、排气与能量收集，但端损失同时成为核心约束问题。镜比与约束时间的关系取决于工况：低碰撞与气体动力学工况、端部膨胀区和电子约束的机制不同。评价磁镜结果应将中心温度、径向剖面、端损失功率与注入束能量分开，分别报告高能束分布与热化背景温度。相关的碰撞与分布函数见[动理学与碰撞](../基础原理/动理学与碰撞/README.md)。

### 从反射条件求往返时间

在静磁场、沿场电势恒定的绝热模型中，粒子总能量 $E$ 与磁矩 $\mu$ 守恒，所以 $m\dot z^2/2=E-\mu B(z)$。设近轴磁场为 $B(z)=B_0(1+z^2/L^2)$，从中面以速率 $v$、俯仰角 $\alpha_0$ 出发，$\mu B_0=E\sin^2\alpha_0$，于是

$$
\dot z^2=v^2\cos^2\alpha_0
-\frac{v^2\sin^2\alpha_0}{L^2}z^2,\qquad
z_m=L\cot\alpha_0,\quad
\omega_b=\frac{v\sin\alpha_0}{L}.
$$

这与简谐振子的能量式相同，一次完整往返周期为 $2\pi/\omega_b$。取氘离子 $E=20$ keV、$\alpha_0=45^\circ$、$L=2.0$ m，先算 $v=1.384\times10^6$ m/s，再得到反射位置 $z_m=2.0$ m、周期 $12.8$ μs。若 $B_0=0.40$ T，反射点磁场为 $0.80$ T；镜喉最大场高于此值时轨道被反射。由同一组守恒量同时求位置和时间，比仅给出损失锥更能说明粒子运动。基础推导见 [Fitzpatrick《Magnetic Mirrors》，式 (2.83)–(2.90)](https://farside.ph.utexas.edu/teaching/plasma/Plasma/node22.html)。

## 仿星器

仿星器依靠外部三维线圈产生主要约束磁拓扑，不需要像通常的托卡马克那样依靠很大的环向等离子体电流产生磁场扭转。这提供了稳态运行的物理基础，却也把难题转移到三维粒子轨道、线圈制造与排热几何。实际仿星器仍可能有自举电流和其他电流，其剖面也会影响磁拓扑。[IPP《Stellarator》，外部线圈与优化段](https://www.ipp.mpg.de/9792/stellarator)。

旋转变换在本文约定为每绕环向一周的极向圈数，

$$
\iota=\lim_{N\to\infty}\frac{\Delta\theta}{2\pi N},\qquad \Delta\phi=2\pi N.
$$

$\theta,\phi$ 为适当磁面坐标中的极向与环向角。采用相同方向约定时 $\iota=1/q$。例如 $\iota=0.5$ 的磁力线每环向一圈走极向半圈；在理想有理磁面上两圈闭合。实际三维场可能含磁岛和随机区，因此需要 Poincaré 截面以识别完整磁面、岛链与随机区域。W7-X 的电子束磁面测绘提供了对真空磁拓扑的直接检验；高温输运另由温度、密度与功率测量研究。[Pedersen 等，Nature Communications 7, 13493 (2016)，Results 中旋转变换与磁面测量部分](https://www.nature.com/articles/ncomms13493)。

磁力线留在磁面上，也不保证粒子的漂移轨道都留在其中。优化的目标包括减少新经典输运、改善快粒子约束、控制自举电流和保持可制造线圈。W7-X 的实验剖面与输运计算对比支持了新经典优化的有效性，但湍流、杂质和长脉冲排热仍是独立问题。[Beidler 等，Nature 596, 221–226 (2021)，摘要与输运比较](https://www.nature.com/articles/s41586-021-03687-w)。

### 把旋转变换读成截面上的点列

在一张理想磁面上采用直磁力线角，$d\theta/d\phi=\iota$。每经过一次完整环向周转，$\phi$ 增加 $2\pi$，因此固定环向截面上的交点满足

$$
\theta_{k+1}=\theta_k+2\pi\iota\pmod{2\pi}.
$$

取 $\iota=2/5$、初始 $\theta_0=0$，前五个交点依次为 $0^\circ,144^\circ,288^\circ,72^\circ,216^\circ$，第五次周转回到起点；磁力线共走两圈极向、五圈环向。若旋转变换变为 $0.401$，每一环向周转相对原点列多走 $0.36^\circ$，100 次累积 $36^\circ$。这解释了长路径磁面测绘对微小磁场变化的灵敏性。加入共振扰动后，有理面附近可形成岛链，实际岛宽还取决于共振场分量与磁剪切。实验读图可对照 [Pedersen 等 2016，Results 的 Hamiltonians and magnetic surfaces、Measuring the magnetic topology，以及图 4 的 5/6 岛链](https://www.nature.com/articles/ncomms13493)。

## 其他路线

### RFP、球马克与 Z-pinch

反场箍缩 RFP 的环向与极向场可处于相近量级，环向场在边缘反号。球马克同时包含等离子体自身产生的环向和极向场，其紧凑环形磁拓扑不依赖穿过中心孔的常规环向场线圈；这与主要为极向场的 FRC 有本质区别。两者涉及电流维持、自组织和磁重联。低压力的理想化 Taylor 松弛态满足 $\nabla\times\mathbf B=\lambda\mathbf B$，$\lambda$ 的单位为 $\mathrm{m^{-1}}$，于是 $\mathbf J\times\mathbf B=0$。有限压力下，压力梯度需一并进入力平衡。[PPPL 暑期课程《Other Fusion Concepts》2025，Spheromak / Reversed Field Pinch 页](https://suli.pppl.gov/2025/course/SY%20-%202025-06%20-%20PPPL%20SULI%20-%20Other%20Fusion%20Concepts.pdf)。

固定闭合导体边界、$\mathbf B\cdot\mathbf n=0$，令 $W_B=\int B^2/(2\mu_0)dV$、$K=\int\mathbf A\cdot\mathbf B\,dV$。忽略边界项，约束变分 $\delta[W_B-\lambda K/(2\mu_0)]=\mu_0^{-1}\int(\nabla\times\mathbf B-\lambda\mathbf B)\cdot\delta\mathbf A\,dV=0$，即得 Taylor 方程。其假设是松弛时总磁螺度近似保持。

Z-pinch 由轴向电流产生周向磁场并压缩等离子体；长直柱外部近似 $B_\theta=\mu_0I/(2\pi r)$。这个场产生箍缩磁压力。箍缩、扭曲等 MHD 模可能限制寿命，剪切流等稳定方案必须由有诊断与误差的实验检验。RFP 则可通过磁涨落、温度和电流剖面测量研究自组织与输运，MST 是相应实验平台。[Wisconsin Plasma Physics Laboratory，MST 装置说明](https://wippl.wisc.edu/madison-symmetric-torus/)。

### 惯性约束与磁惯性约束

惯性约束 ICF 依靠快速压缩燃料，使反应在燃料显著膨胀前发生；关键量包括压缩密度、面密度 $\rho R$（$\mathrm{kg\,m^{-2}}$）和驱动对称性。靶增益 $G_{\rm target}=E_{\rm fusion}/E_{\rm driver,target}$ 的分母是到靶驱动能量。LLNL 报告 2022-12-05 的 NIF 实验以到靶激光能量 $2.05\,\mathrm{MJ}$ 得到约 $3.15\,\mathrm{MJ}$ 聚变产额，即 $G_{\rm target}\approx1.54$。这是 2022 年的靶增益结果；厂级账还包括驱动供电、冷却和热电转换。[LLNL，2023-04-12，点火实验的诊断报道](https://lmf.llnl.gov/news/diagnostics-were-crucial-to-llnls-historic-ignition-shot)。

磁惯性约束 MIF 在脉冲压缩中利用磁化降低能量损失。MagLIF 组合预磁化、预热与衬套压缩，三者共同影响压缩中的能量与粒子损失。Sandia 的 2022 年综述区分已测得的聚变相关状态与更大驱动装置的模拟展望，分别对应实验状态与模型预测。向电站延伸还须解决重复频率、驱动效率、耗材制造和腔室恢复。[Yager-Elorriaga 等，Nuclear Fusion 62 (2022)，Sandia 摘要](https://www.sandia.gov/research/publications/details/an-overview-of-magneto-inertial-fusion-on-the-z-machine-at-sandia-national-2022-04-01/)。

### 用时间尺度理解路线差异

约束路线的“长”与“短”必须相对于过程本身。假设一个系统的能量损失时间为 $\tau_E$，在没有加热、损失系数不变的教学模型里有 $dW/dt=-W/\tau_E$，故 $W(t)=W(0)e^{-t/\tau_E}$。维持十个 $\tau_E$ 的高温状态意味着持续补偿损失，粒子与能量仍通过输运持续交换；短脉冲惯性系统则利用膨胀前的一小段时间完成足够反应，比较时可将持续时间相对各自的损失或膨胀时间归一化。

中子也可由高能束与冷背景反应产生。反推热温度须约束分布、密度体积和反应机制；脉冲路线检查中子能谱、各向异性、时间宽度与背景扣除，磁约束还应核算快离子对反应率和储能的贡献。 [LLNL：点火实验诊断](https://lmf.llnl.gov/news/diagnostics-were-crucial-to-llnls-historic-ignition-shot)；[Sandia：MagLIF 综述摘要](https://www.sandia.gov/research/publications/details/an-overview-of-magneto-inertial-fusion-on-the-z-machine-at-sandia-national-2022-04-01/)。

### 用理想压缩尺度连接惯性与磁惯性方案

考虑粒子数固定、各向同性的单原子气体球，在快速可逆压缩中取 $U=3NT/2$、$p=NT/V$，其中 $T$ 以 J 表示。由 $dU=-p\,dV$ 得 $dT/T=-(2/3)dV/V$，积分得到 $TV^{2/3}=$ 常数。球半径缩小为原来的 $1/C$ 时，

$$
n_1=C^3n_0,\qquad T_1=C^2T_0.
$$

若磁通同时冻结且压缩各向同性，截面积按 $C^{-2}$ 缩小，故 $B_1=C^2B_0$，热离子回旋半径按 $\rho_i\propto\sqrt T/B$ 缩为 $1/C$。教学取 $C=5$、$T_0=0.20$ keV、$B_0=2$ T，则密度乘 125、温度升至 5.0 keV、磁场升至 50 T，而 $\rho_i/R$ 保持原比例。实际柱形压缩有另一组几何幂律，热传导、辐射与磁通扩散会改变结果；这几个损失通道也正是磁惯性研究需要计算的环节。[Sandia 的 MagLIF 总结论文摘要与研究范围](https://www.sandia.gov/research/publications/details/an-overview-of-magneto-inertial-fusion-on-the-z-machine-at-sandia-national-2022-04-01/)说明了预热、磁化和压缩结合的路线。

## 装置档案的记录内容

装置比较应首先固定系统边界。磁约束常用 $\tau_E=W/P_{\rm loss}$，其中 $W$ 用 J，$P_{\rm loss}$ 用 W；非稳态时由 $dW/dt=P_{\rm heat}-P_{\rm loss}$ 得 $P_{\rm loss}=P_{\rm heat}-dW/dt$。假设吸收加热为 10 MW、储能增长率为 2 MW、储能为 4 MJ，则 $\tau_E=0.50\,\mathrm s$，而直接用 $W/P_{\rm heat}$ 会得到 0.40 s。这里未包括未定义的束能库存，比较真实实验时必须统一热能与快离子能的口径。

一份可比较的档案至少对应同一放电或同一时间窗，使温度、密度与时长属于同一组状态。核心字段包括燃料组成、磁场位置、几何、电流、温度诊断、密度平均方式、吸收功率、脉冲时间、误差和原论文位置。测量值、重建值、模型外推和设计目标要分栏。$nT\tau_E$ 也须指明粒子种类与平均方式；不同路线的靶增益、等离子体增益和净电功率不应放在同一列直接排序。厂级能量边界见[工程系统](../工程系统/README.md)。

增益分母须区分源输出、天线/束口和实际吸收功率。余辉用整段时窗能量账并计入初始储能；温度反演同时保留仪器响应与分布模型。

### 从一条功率曲线建立可复算档案

脉冲档案可以直接附上少量取样点和积分方法。教学曲线在 $t=0,0.5,1.0,1.5,2.0$ s 的聚变功率分别为 $0,4,6,4,0$ MW，点间作线性插值。每一段的能量是梯形面积，

$$
E_{\rm fus}=\sum_k\frac{P_{k+1}+P_k}{2}(t_{k+1}-t_k)
=1+2.5+2.5+1=7.0\ {\rm MJ}.
$$

两秒窗口内平均聚变功率3.5 MW、峰值6 MW。若外部加热恒为10 MW，则输入20 MJ、积分增益0.35。将峰值、窗口平均与窗口积分并列，并记录时间轴、计量面和原始波形版本。 [LLNL 对历史点火实验的诊断说明：产额、入射激光能量与诊断不确定性段](https://lmf.llnl.gov/news/diagnostics-were-crucial-to-llnls-historic-ignition-shot)。

## 装置论文的阅读与证据定位

- [IPP：托卡马克](https://www.ipp.mpg.de/9778/tokamak)与[仿星器](https://www.ipp.mpg.de/9792/stellarator)：磁场与电流的入门说明。
- [Fitzpatrick：磁镜](https://farside.ph.utexas.edu/teaching/plasma/Plasma/node22.html)：磁矩、镜点与损失锥推导。
- [Belova 等，PPPL-4150，2006](https://bp-pub.pppl.gov/pub_report/2006/PPPL-4150.pdf)：FRC 混合模拟与稳定性边界。
- [PPPL：其他聚变构型课程，2025](https://suli.pppl.gov/2025/course/SY%20-%202025-06%20-%20PPPL%20SULI%20-%20Other%20Fusion%20Concepts.pdf)：紧凑环、箍缩与开放构型。
- [IAEA 聚变装置数据库](https://nucleus.iaea.org/sites/fusion-portal/SitePages/FFDB.aspx?web=1)：装置检索入口；具体性能仍以带日期的原始报告为准。

### 一篇装置论文怎样拆成三张阅读卡

以 [Pedersen 等 2016 年 W7-X 磁拓扑论文](https://www.nature.com/articles/ncomms13493)为例，可以按正文位置形成连续的阅读卡。“定义卡”摘录 Results 中旋转变换的约定：极向圈数除以环向圈数；将 $\iota=5/6$ 改写为六圈环向对应五圈极向。“方法卡”定位 Measuring the magnetic topology：电子束沿场运动，荧光探杆与相机把多次交点记录为截面。“结果卡”再定位图 4 与 Adjustment of iota：这里显示的是 5/6 岛链以及其径向位置。

由六个岛瓣取 $m=6$，按 $\iota=n/m$ 得 $n=5$，再核对作者的磁剪切、岛宽与误差场估计。笔记记录符号约定、正文位置和图号；加热、输运及稳态性能另以各自观测量核验。

[辅助加热系统](../辅助加热/README.md) · [编写说明](../编写说明.md) · [返回知识库](../README.md)
