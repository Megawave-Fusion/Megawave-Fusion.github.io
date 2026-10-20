# 离子回旋加热（ICRH / ICRF）

离子回旋加热用射频电场与离子的回旋运动交换能量，再通过碰撞、输运和对分布函数的改变影响背景等离子体。实际效果由波的传播与极化、组分、共振条件、快离子约束及能量转移共同决定。 对应计算流程见[模拟专题](../../仿真计算/离子回旋加热模拟/README.md)。

本专题从单粒子共振推到快波与多离子吸收，再连接射频系统、计算与实验验证。公式使用 SI 制；温度写成 eV 或 keV 时表示温度能量。文中的教学算例、历史实验和装置设计参数分别注明；设备参数由其实际工况和部件规格确定。

先修：[单粒子运动](../../基础原理/单粒子运动/README.md)、[等离子体波](../../基础原理/等离子体波/README.md)、[动理学与碰撞](../../基础原理/动理学与碰撞/README.md)。核对范围见[内容核验记录](../../核验记录.md)。

## 离子共振与局域磁化条件

ICRH 指离子回旋共振加热，ICRF 指该频段；应用包括直接离子吸收、模转换电子加热与电流驱动。托卡马克常以快磁声波输能，最终受热对象由波模、组分和阻尼决定。

本文采用 SI 制，实场写成复振幅的实部：

$$
\mathbf E(\mathbf r,t)=\operatorname{Re}\!\left[\widetilde{\mathbf E}
 e^{i\mathbf k\cdot\mathbf r-i\omega t}\right],\qquad
\mathbf B_0=B_0\hat{\mathbf z},\qquad
\Omega_s=\frac{q_sB_0}{m_s}.
$$


其中 \(\omega>0\)，\(\Omega_s\) **保留电荷符号**：正离子为正，电子为负。回旋频率的正数数值为 \(f_{cs}=|\Omega_s|/(2\pi)\)。密度 \(n_s\) 用 \(\mathrm{m^{-3}}\)，场强用 T，电场用 \(\mathrm{V\,m^{-1}}\)。温度若用 eV，表示温度能量，其数值乘 \(1.602176634\times10^{-19}\) 才得到 J。谐波阶数用整数 \(\ell\)，避免与密度混淆。

局域模型要求 $\rho_i/L_B\ll1$、$T_{ci}/\tau_{eq}\ll1$。冷模型辨认传播/极化，热响应处理 Doppler、FLR、吸收和分布演化；共振层、可达性、旋向场与快离子约束须同时成立。

工作频率同时标明离子荷质比与谐波阶数，并检查其它组分的邻近共振。组成和杂质进入介电响应；教学用环向场估算，装置计算用重建局部总场。

ICRF 电子可经平行电场 Landau 阻尼或磁镜力直接受能。功率账本将它们与“离子先吸收、再碰撞传电子”分开。

来源：[Fukuyama，*Integrated Modeling for Heating and Current Drive*，2025，PDF 第 20–26 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[Kazakov 等，*Progress With Applications of Three-Ion ICRF Scenarios for Fusion Research: A Review*，2023，PDF 第 1–2 页](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)。

### 从回旋周期检查局域近似

从向心力平衡 $m_iv_\perp^2/\rho_i=Z_ie v_\perp B$ 出发，先得 $\rho_i=m_iv_\perp/(Z_ieB)$，再以 $v_\perp=\sqrt{2E_\perp/m_i}$ 得 $\rho_i=\sqrt{2m_iE_\perp}/(Z_ieB)$。回旋周期为 $2\pi m_i/(Z_ieB)$。局域模型中的两个小参数分别是空间比 $\rho_i/L_B$ 和时间比 $T_{ci}/\tau_{eq}$，它们比较粒子一圈运动与背景变化。

取氘、$E_\perp=10$ keV、$B=3$ T、$L_B=0.5$ m、背景演化时间 1 ms，得到 $v_\perp=9.789\times10^5$ m/s、$\rho_D=6.81$ mm、$T_{cD}=43.7$ ns，两个比值约为 0.0136 和 $4.37\times10^{-5}$。若能量提高到 1 MeV，半径扩大十倍至 6.81 cm，局域空间展开的误差就更值得检查。工程上的磁场剖面和物理上的快离子能谱通过这个平方根关系直接联系起来；同一装置中的热离子与快离子因此可能需要不同轨道模型。

推导起点与参考位置：[Fitzpatrick，Waves in Magnetized Plasmas，式 (7.53)–(7.78)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，Wave heating 与 Ion cyclotron wave，PDF 页 20–25](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## 电场做功与有限时间的单粒子共振

非相对论粒子的动能 \(K=m v^2/2\) 满足

$$
\frac{dK}{dt}=q\mathbf E\cdot\mathbf v,
$$


因为 \(\mathbf v\cdot(\mathbf v\times\mathbf B)=0\)。静磁场负责弯曲轨迹，能量由电场提供。为直接看见相位累积，暂取空间均匀的规定电场，忽略碰撞、波场反作用、磁场梯度和射频磁力。对正离子定义 \(w=v_x+i v_y\)，施加与其回旋同向的圆电场

$$
\mathbf E_\perp(t)=E_0(\hat{\mathbf x}\cos\omega t-
\hat{\mathbf y}\sin\omega t).
$$


这里 \(E_0\) 是真实电场矢量的恒定大小。由 Lorentz 方程得

$$
\dot w+i\Omega_i w=\frac{q_iE_0}{m_i}e^{-i\omega t}.
$$


令初始垂直速度为零，乘积分因子 \(e^{i\Omega_i t}\) 后积分：

$$
w(t)=\frac{q_iE_0}{m_i}
\frac{e^{-i\omega t}-e^{-i\Omega_i t}}{i(\Omega_i-\omega)}.
$$


以 \(\Delta=\omega-\Omega_i\)、\(\operatorname{sinc}x=\sin x/x\) 表示，便有

$$
K_\perp(t)=\frac{q_i^2E_0^2t^2}{2m_i}
\operatorname{sinc}^2\!\left(\frac{\Delta t}{2}\right).
$$


严格共振时取连续极限，\(w=(q_iE_0/m_i)t e^{-i\Omega_i t}\)，于是速度振幅随时间增长，能量随 \(t^2\) 增长；失谐后相位逐渐滑动，不同时间段的做功相互抵消。若改用反向旋转电场，分母对应 \(\omega+\Omega_i\)，正频率下不出现这一基频共振。这说明偏振与频率同样重要。

教学算例：氘离子 \(q_i=e\)、\(m_D=3.34358\times10^{-27}\,\mathrm{kg}\)，在严格共振的 \(E_0=10^3\,\mathrm{V\,m^{-1}}\) 中持续 \(1\,\mu\mathrm{s}\)，上述模型给出约 \(24.0\,\mathrm{eV}\)。有限作用时间的第一失谐零点满足 \(|\Delta|=2\pi/t\)，故这里对应 \(|\Delta f|=1\,\mathrm{MHz}\)，它反映有限作用时间的频谱宽度。对已有初始回旋速度的单粒子，能量变化还含初相位交叉项，应将初相位纳入能量增量。热化、展宽和自洽波耗散随后由碰撞、分布函数及波场联合计算。

来源：[Fukuyama 2025，PDF 第 20–21 页，波与粒子能量交换](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[Fitzpatrick，§7.7 *Parallel Wave Propagation*，式 7.98–7.101](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node95.html)。上面的有限时间解为在所列假设下直接积分所得。

### 有限脉冲的半高宽与失谐算例

由规定圆电场的速度增量积分 $\delta u\propto\int_0^t e^{-i\Delta t'}dt'$，得到相对严格共振值的能量因子 $F=[\sin(\Delta t/2)/(\Delta t/2)]^2$。半高点满足 $(\sin x/x)^2=1/2$，在主峰内求根为 $x=1.391557$。由于 $\Delta=2\pi\Delta f$，正负两侧半高点相隔 $\mathrm{FWHM}=2x/(\pi t)=0.885893/t$。

取作用时间 1 μs，有限脉冲谱线的半高全宽为 0.8859 MHz。频率失谐 0.50 MHz 时，$x=\pi/2$，能量因子为 $4/\pi^2=0.405285$。沿用本节氘、$E_0=10^3$ V/m 的初始静止算例，严格共振约 23.959 eV，失谐后约 9.710 eV。把复指数直接做时间积分，再对积分模平方，能够独立检查 sinc 公式及角频率和普通频率之间的 $2\pi$；延长脉冲会使主峰变窄，也提高严格共振轨道的相干增能。

![有限相干作用时间给出 sinc² 失谐响应，脉冲越长主峰越窄。](/assets/diagrams/heat-icrh-resonance.svg)

有限相干作用时间给出 sinc² 失谐响应，脉冲越长主峰越窄。

推导起点与参考位置：[Fitzpatrick，Waves in Magnetized Plasmas，式 (7.53)–(7.78)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，Wave heating 与 Ion cyclotron wave，PDF 页 20–25](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## Doppler 位移、回旋谐波与共振层

传播波沿粒子轨迹的相位不仅随时间变化，也随粒子的平行运动和回旋运动变化。局部均匀磁场下，平行运动给出 \(k_\parallel v_\parallel t\)；垂直运动采样波的空间结构，产生以回旋频率为间隔的谐波。某个谐波与粒子长期保持相位关系的条件为

$$
\omega-k_\parallel v_\parallel=\ell\Omega_i,
\qquad \ell\in\mathbb Z.
$$


常见正离子基频与二次谐波方案分别取 \(\ell=1\)、\(2\)。这里 \(k_\parallel\) 是沿局部磁场的波数，单位 \(\mathrm{m^{-1}}\)，不是必然等于天线某个单独的几何波数。左侧是粒子沿场运动所见的频率；当 \(k_\parallel v_\parallel>0\) 时，所需的回旋频率降低。带有限宽度的速度分布因此对应一族共振位置，而不是所有粒子只在同一个无厚度曲面吸收。

在轴对称、环向场占主导的近似下，\(B(R)\simeq B_0R_0/R\)。忽略 Doppler 位移、轨道宽度以及极向场对总场强的修正，可得

$$
B_{\mathrm{res}}=\frac{m_i\omega}{\ell Z_i e},\qquad
R_{\mathrm{res}}=\frac{\ell Z_i e B_0R_0}{m_i\omega}.
$$


因此频率和磁场共同选择共振层。取氘基频、\(f=40\,\mathrm{MHz}\)、\(B_0=5\,\mathrm T\)、\(R_0=3\,\mathrm m\)，有 \(B_{\mathrm{res}}\simeq5.245\,\mathrm T\)、\(R_{\mathrm{res}}\simeq2.860\,\mathrm m\)。将这一几何位置与等离子体边界对照可判断层位是否在内部，沉积份额再由波场与阻尼求得。

保留平行运动时，把上式的 \(\omega\) 换成 \(\omega-k_\parallel v_\parallel\)。例如 \(k_\parallel=5\,\mathrm{m^{-1}}\)、\(v_\parallel=10^6\,\mathrm{m\,s^{-1}}\) 给出约 \(0.796\,\mathrm{MHz}\) 的 Doppler 位移。若定义一维热速度标准差 \(v_{ti}=\sqrt{k_BT_i/m_i}\)，在小位移、固定局部波数近似下，共振层径向展宽量级为 \(\Delta R\sim R_{\mathrm{res}}|k_\parallel|v_{ti}/\omega\)。有限轨道宽度、波谱和实际磁几何还会改变沉积宽度。

快离子沿轨道只在部分区段共振，多次穿越的相干性影响平均扩散。径向约化需注明轨道平均、俘获粒子和天线平行谱，不能用单一共振半径替代沉积及损失分布。

来源：[Fitzpatrick，§7.6 *Waves in Magnetized Plasmas*，式 7.68–7.74](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，PDF 第 21、32–36 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

### 共振层对平行速度的非线性响应

在 $B(R)=B_0R_0/R$ 的教学几何中，氘基频满足 $\omega-k_\parallel v_\parallel=eB_0R_0/(m_DR)$。解出 $R_{res}=R_{cold}/(1-k_\parallel v_\parallel/\omega)$，其中 $R_{cold}=eB_0R_0/(m_D\omega)$。小位移展开给 $\delta R/R_{cold}\simeq k_\parallel v_\parallel/\omega$；对零均值 Maxwell 平行速度，标准差为 $\sigma_R\simeq R_{cold}|k_\parallel|\sqrt{T_i/m_D}/\omega$，此处温度能量用 J。

取 $f=40$ MHz、$B_0R_0=15$ T·m、$k_\parallel=5$ m⁻¹，冷共振半径约 2.860 m。$v_\parallel=\pm10^6$ m/s 时，两个半径约为 2.918 m 和 2.804 m；有限位移的两侧并非完全对称。若 $T_i=10$ keV，$\sigma_{v\parallel}\simeq6.922\times10^5$ m/s，线性化的共振层标准差约 3.94 cm。该宽度来自速度分布在空间的映射，计算沉积还需把这一分布与波场、偏振和轨道停留时间加权。

推导起点与参考位置：[Fitzpatrick，Waves in Magnetized Plasmas，式 (7.53)–(7.78)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，Wave heating 与 Ion cyclotron wave，PDF 页 20–25](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## 冷介电张量与 ICRF 快波传播

冷模型将各组分视为无压、无碰撞流体，适合首先辨认传播区、截止和极化，热粒子吸收率另由动理学响应给出。沿用本文时间约定，令 \(\omega_{ps}^2=n_sq_s^2/(\epsilon_0m_s)\)，可写

$$
\boldsymbol\epsilon=
\begin{pmatrix}S&-iD&0\\iD&S&0\\0&0&P\end{pmatrix},
\quad S=\frac{R+L}{2},\quad D=\frac{R-L}{2},
$$


$$
R=1-\sum_s\frac{\omega_{ps}^2}{\omega(\omega+\Omega_s)},\quad
L=1-\sum_s\frac{\omega_{ps}^2}{\omega(\omega-\Omega_s)},\quad
P=1-\sum_s\frac{\omega_{ps}^2}{\omega^2}.
$$


这些分量可从各组分线性动量方程 $-i\omega m_s\mathbf v_s=q_s(\mathbf E+\mathbf v_s\times\mathbf B_0)$ 推出。令 $v_\pm=v_x\pm iv_y$、$E_\pm=E_x\pm iE_y$，相加、相减横向方程后得 $v_+=iq_sE_+/[m_s(\omega-\Omega_s)]$、$v_-=iq_sE_-/[m_s(\omega+\Omega_s)]$。再以 $\mathbf J_s=n_sq_s\mathbf v_s=-i\omega\mathbf P_s$ 求极化，并代入 $\mathbf D=\epsilon_0\mathbf E+\sum_s\mathbf P_s$，分别得到 L 与 R；平行方程则给 P。

电子的 \(\Omega_e<0\) 必须直接代入，使分母与电子旋向一致。取 \(\mathbf k=(k_\perp,0,k_\parallel)\)、\(N_j=ck_j/\omega\)，Maxwell 方程给出

$$
\begin{pmatrix}
S-N_\parallel^2&-iD&N_\perp N_\parallel\\
iD&S-N_\perp^2-N_\parallel^2&0\\
N_\perp N_\parallel&0&P-N_\perp^2
\end{pmatrix}\widetilde{\mathbf E}=0.
$$


当平行电子响应足够强、\(|P-N_\perp^2|\) 足够大，并且第三行导出的平行电场及其反馈可以忽略时，令 \(A=S-N_\parallel^2\)。前两行的行列式为 \(A(A-N_\perp^2)-D^2=0\)，故

$$
N_\perp^2\simeq
\frac{(R-N_\parallel^2)(L-N_\parallel^2)}{S-N_\parallel^2}.
$$


这一近似给出常用的 ICRF 快波传播描述：实系数条件下 \(N_\perp^2>0\) 对应局部传播，负值对应局部倏逝。分子零点可成为截止，分母趋零提示强色散和近似失效，必须检查完整色散及热效应。在混杂层附近，热色散和因果阻尼共同决定能流与吸收。

ICRF fast wave 与 slow wave 是该频段色散分支的名称。理想 MHD 还要求 \(\omega\ll|\Omega_i|\) 等尺度条件，而 ICRH 恰在离子回旋频率附近工作。两套近似按各自尺度条件选用。

来源：[Fitzpatrick，§5.3 *Cold-Plasma Dielectric Permittivity*，式 5.31–5.39](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)；[§5.4 *Cold-Plasma Dispersion Relation*，式 5.40–5.55](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node69.html)；[Fukuyama 2025，PDF 第 23–25 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

### 用完整矩阵检查快波约化式

记 $x=N_\perp^2$、$A=S-N_\parallel^2$。完整矩阵第三行先给 $E_z=-N_\perp N_\parallel E_x/(P-x)$，第二行给 $E_y=-iDE_x/(A-x)$。代回第一行得到 $A-D^2/(A-x)-xN_\parallel^2/(P-x)=0$。令 $|P|\to\infty$ 后，最后一项趋零，遂有 $x=A-D^2/A=[(R-N_\parallel^2)(L-N_\parallel^2)]/(S-N_\parallel^2)$。

取教学介电系数 R=6、L=2、$N_\parallel^2=1$，则 S=4、D=2、A=3。约化结果为 $N_\perp^2=5/3$、$E_y/E_x=-1.5i$。若保留 P=−100，数值解完整行列式得快波根约 1.67394，较约化值大约 0.44%，同时出现小的平行电场。把解代回全部三行并检查残差，能判断约化误差和符号约定。靠近 A=0 或 P=x 时则应直接使用完整方程，保留原先被舍去的耦合项。

推导起点与参考位置：[Fitzpatrick，Cold-Plasma Dielectric Permittivity，式 (5.31)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)；[Fukuyama 2025，Wave heating 与 Ion cyclotron wave，PDF 页 20–25](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## 圆偏振、离子旋向与基频耦合

“左旋”“右旋”在不同文献中可能按观察方向命名，最稳妥的做法是同时给出时间因子、磁场方向和旋转矢量。在本文约定下，正离子的自由回旋满足 \(v_x+i v_y\propto e^{-i\Omega_i t}\)。定义单位归一圆基

$$
\mathbf e_{\mathrm{ion}}=\frac{\hat{\mathbf x}-i\hat{\mathbf y}}{\sqrt2},\qquad
\mathbf e_{\mathrm{opp}}=\frac{\hat{\mathbf x}+i\hat{\mathbf y}}{\sqrt2},
$$


$$
\widetilde E_{\mathrm{ion}}=
\frac{\widetilde E_x+i\widetilde E_y}{\sqrt2},\qquad
\widetilde E_{\mathrm{opp}}=
\frac{\widetilde E_x-i\widetilde E_y}{\sqrt2}.
$$


于是 \(|\widetilde E_x|^2+|\widetilde E_y|^2=|\widetilde E_{\mathrm{ion}}|^2+|\widetilde E_{\mathrm{opp}}|^2\)，同向基的介电本征值为 \(L=S-D\)。有些文献把旋转分量定义为除以 \(2\)，只要能量公式同步调整即可；比较功率时应将归一化统一。

在上一条忽略平行电场的近似下，由 \(A\widetilde E_x-iD\widetilde E_y=0\) 得

$$
\left|\frac{\widetilde E_{\mathrm{ion}}}{\widetilde E_{\mathrm{opp}}}\right|^2
=\left|\frac{R-N_\parallel^2}{L-N_\parallel^2}\right|^2.
$$


单主要离子的冷模型在基频附近有 L 极点，可抑制快波同向场，故单组分基频加热偏弱。多组分与谐波方案改变极化；实际份额由热波场和阻尼求取。

这里的波场由色散自洽决定，前面的单粒子解则采用规定电场。有限温度、传播边界和阻尼决定实际场与功率分配；对少数离子也采用同样的热响应处理其冷回旋极点。

来源：[Fitzpatrick，§5.5 *Wave Polarization*，式 5.56–5.60](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node70.html)；[§5.9 *Parallel Wave Propagation*](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node74.html)；[Fukuyama 2025，PDF 第 24 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

### 从 Jones 分量算离子同向场份额

沿用 $e^{-i\omega t}$ 与本页圆基，$E_{ion}=(E_x+iE_y)/\sqrt2$、$E_{opp}=(E_x-iE_y)/\sqrt2$。令 $E_x=a$、$E_y=-ib$，直接展开得两个模平方分别为 $(a+b)^2/2$ 与 $(a-b)^2/2$，相加为 $a^2+b^2$。若相位从 $-\pi/2$ 偏离 $\delta$，同向份额成为 $1/2+ab\cos\delta/(a^2+b^2)$。

取峰值复幅 $E_x=100$ V/m、$E_y=-50i$ V/m，同向和反向圆分量幅值分别为 106.066 与 35.355 V/m，同向场模平方份额为 90%。相位偏离 5° 后，该份额为 89.848%。这只是给定位置的偏振分解；吸收计算把相应分量与组分响应及速度空间积分相乘。将探头或全波输出转换为统一圆基后，可以逐点检查极化变化，同时用两分量平方和守恒发现归一化错误。

推导起点与参考位置：[Fitzpatrick，Cold-Plasma Dielectric Permittivity，式 (5.31)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)；[Fitzpatrick，Waves in Magnetized Plasmas，式 (7.53)–(7.78)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)。

## 少数离子基频加热

少数离子加热让一种密度较低、荷质比不同的离子成为主要共振吸收者，主要组分则决定大部分波传播背景。典型教学例是氘等离子体中的氢少数离子，或氘中的 \({}^3\mathrm{He}\)。由于背景的主要回旋频率与少数离子的共振频率分开，少数离子共振区可以存在有利的波极化；吸收又会改变其分布函数，使尾部粒子持续获得垂直能量。

本文使用数密度归一化

$$
X_s=\frac{n_s}{n_e},\qquad \sum_{\text{ions }s}Z_sX_s=1,
$$


其中忽略净电荷密度。双电荷的 \({}^3\mathrm{He}^{2+}\) 在 \(X_s=0.01\) 时贡献的电子电荷份额为 \(0.02\)。若文献使用 \(n_H/(n_H+n_D)\) 或电荷浓度，需先换算再比较，以统一的密度定义比较配比。

低浓度增加每个吸收粒子的负荷；浓度升高又移动混杂层并改变极化/功率分配。最优配比随场、温度、谱和组分求解。

在 \(B=5\,\mathrm T\) 的局部均匀场中，以离子核质量计算，氢、氘、氚和 \({}^3\mathrm{He}^{2+}\) 的基频约为 \(76.23\)、\(38.13\)、\(25.46\)、\(50.93\,\mathrm{MHz}\)。这些数值来自 \(f_{ci}=Z_i eB/(2\pi m_i)\)，可用于初步识别候选共振，却没有包含实际场梯度和 Doppler 位移。少数离子获得的能量随后可经 Coulomb 碰撞流向电子和主体离子；直接吸收强、热离子升温强和聚变性能提升是需要分别检验的结论。

来源：[Kazakov 等 2023 综述，PDF 第 2 页，少数离子加热与碰撞慢化](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)；[Fukuyama 2025，PDF 第 24–25、48 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[NIST 2022 基本物理常数表，proton / deuteron / triton / helion mass 条目](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)。

### 每个少数离子的功率与浓度缩放

设一块体积 V 内少数离子密度为 $n_s=X_sn_e$，该组分实际吸收功率为 $P_s$。粒子数是 $N_s=X_sn_eV$，故每粒子的平均能量变化率为 $P_s/N_s$；这一步把总吸收与单粒子加速联系起来。在同一吸收功率保持固定的比较中，能量率与浓度成反比，而总吸收功率本身应由波计算随组分重新求解。

教学取 $n_e=5\times10^{19}$ m⁻³、$X_{He3}=0.01$、V=10 m³、$P_s=1$ MW，得到 $N_s=5\times10^{18}$，每粒子能量率 $2\times10^{-13}$ W，即 1.2483 MeV/s。暂忽略慢化和损失，0.10 s 内平均增能 124.83 keV；浓度加倍而所吸收功率保持固定时，该增能减半。准中性同时给出 $n_D=n_e-2n_{He3}$，所以两种浓度对应 $n_D=4.9\times10^{19}$ 与 $4.8\times10^{19}$ m⁻³。热化模型再把增长的快离子能量分配到电子、离子及损失。

推导起点与参考位置：[Kazakov 等 2023，三离子综述，PDF 页 2–3、式 (1) 与图 1–2](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)；[IAEA Fusion Physics，§5.1.2–5.1.4，书页 535–545；§5.2.1，书页 571–573](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)。

## 二次谐波与有限 Larmor 半径

均匀非相对论圆电场的相干驱动在基频；传播波的垂直相位结构通过有限回旋轨道产生高次谐波。

用 \(\rho_i=v_\perp/|\Omega_i|\) 表示某个粒子的 Larmor 半径，轨道上的相位包含

$$
e^{ik_\perp\rho_i\sin\theta}
=\sum_{\ell=-\infty}^{\infty}J_\ell(k_\perp\rho_i)e^{i\ell\theta}.
$$


这是 Fourier–Bessel 恒等式。实际做功还包含电场偏振与速度的回旋因子，完整耦合涉及相邻阶 Bessel 函数的组合，各系数连同偏振、共振分布一起进入吸收率。有限轨道半径使粒子看到更丰富的谐波结构，且耦合强度依赖 \(k_\perp\rho_i\)、偏振和分布函数。

二次谐波满足

$$
\omega-k_\parallel v_\parallel=2\Omega_i.
$$


在冷极限且 \(k_\perp\rho_i\to0\) 时，相应有限 Larmor 半径效应削弱，相应谐波通道耦合降低。热离子或已存在的快离子可增强相关耦合；功率沉积又反过来改变分布函数，需要波场与动理学联合计算。即使冷模型在 \(2\Omega_i\) 没有与基频相同的单粒子极点，热等离子体仍可具有谐波阻尼，这正说明冷流体描述不足以计算该过程。

以 \(5\,\mathrm T\) 中氘为例，忽略 Doppler 位移的二次谐波约为 \(76.26\,\mathrm{MHz}\)，与氢基频 \(76.23\,\mathrm{MHz}\) 接近。原因是氘荷质比约为氢的一半。这种近邻关系意味着杂质或少量氢可能改变功率分配，应同时纳入满足共振条件的其他组分。实际分辨还需考虑精确质量、磁场分布、速度展宽和波极化。

来源：[Fitzpatrick，§7.6，式 7.68–7.74](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，PDF 第 21、24、32–36 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

### 用 Fourier 积分检查有限轨道半径系数

在沿回旋相位的波因子展开中，$J_\ell(x)=(2\pi)^{-1}\int_0^{2\pi}e^{i(x\sin\theta-\ell\theta)}d\theta$，$x=k_\perp\rho_i$。对 x 作 Taylor 展开并逐项积分，可得 $J_1(x)=x/2-x^3/16+x^5/384+\cdots$。在只保留离子同向圆分量的谐波耦合项中，二次谐波含 $J_{2-1}=J_1$，因此小轨道半径时这一项的模平方先按 $x^2/4$ 增长。

取 x=0.20，数值 Fourier 积分给 $J_1=0.09950083$、平方为 0.00990042；x 增至 0.40 时，$J_1=0.19602658$、平方为 0.03842641，增加约 3.881 倍，接近小 x 估计的四倍。这个练习检查了有限 Larmor 半径的首项和高阶修正。完整加热率还对所有相关圆分量、平行电场、共振粒子分布和轨道求和，教学中的系数比较用于识别其中一条耦合通道的变化。

推导起点与参考位置：[Fitzpatrick，Waves in Magnetized Plasmas，式 (7.53)–(7.78)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，Wave heating 与 Ion cyclotron wave，PDF 页 20–25](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## 离子—离子混杂层与模转换加热

有两种或更多离子时，介电响应的不同回旋项可以在相邻离子回旋频率之间相互抵消，形成离子—离子混杂结构（ion–ion hybrid，IIH）。在前述快波近似中，\(S-N_\parallel^2\simeq0\) 标记一个需要特别处理的位置；它一般不同于任何单一组分的精确回旋共振。其位置依赖离子荷质比、浓度和 \(N_\parallel\)，因此改变配比可以移动混杂层。

局部冷公式在此预测垂直波数显著增大，而短垂直尺度正会使有限 Larmor 半径效应变得重要。完整热色散关系可以包含离子 Bernstein 波（ion Bernstein wave，IBW）及离子回旋波（ion cyclotron wave，ICW）等分支。入射长波长快波到达非均匀区域后，部分能量可能转入这些短波长分支，这一过程称模转换。究竟转入哪个分支，取决于组分、磁剪切、波数和几何，各分支分别计算其能流。

模转换首先重新分配各波分支的能流。若转换波再通过电子 Landau 阻尼、离子回旋阻尼等机制衰减，才把有序波能传给相应粒子。它因此可用于电子加热，也可能涉及离子吸收；实际电子、离子功率份额必须由热响应或诊断确认。冷奇异层附近的吸收功率由因果热响应及边界能流确定。

转换效率取决于入射方向、截止—转换层间距、梯度及谱。波动诊断识别短波支，温度/功率平衡约束传能，天线匹配约束输入。

来源：[Lin 等，*Investigation of ICRF Mode Conversion at the Ion-ion Hybrid in Alcator C-Mod*，2003，MIT 作者摘要](https://library.psfc.mit.edu/catalog/reports/2000/03ja/03ja024/03ja024_abs.html)；[Lin 等，*ICRF mode conversion in three-ion species heating experiment and in flow drive experiment on the Alcator C-Mod tokamak*，2017，第 2 节](https://library.psfc.mit.edu/catalog/reports/2010/17ja/17ja050/17ja050_full.pdf)；[Kazakov 等 2023，PDF 第 2–3 页](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)。

### 两离子混杂频率的组分推导

以 H-D 混合物为例，令 $x=n_H/n_e$、$n_D/n_e=1-x$，并用 $u=(\omega/\Omega_H)^2$。在离子极化项占优、忽略电子常数响应和 $N_\parallel^2$ 的 S=0 近似中，$\omega_{pD}^2/\omega_{pH}^2=(1-x)/(2x)$，所以混杂条件化为 $x/(u-1)+(1-x)/[2(u-1/4)]=0$。通分得 $u=(1-x/2)/(1+x)$，它始终位于两个回旋频率平方之间。

取 H 浓度 x=0.20，得到 u=0.75、$\omega/\Omega_H=0.86603$；x=0.50 时得到 u=0.50、比值 0.70711。若某处 $f_{cH}=50$ MHz，两种混杂频率分别约为 43.30 与 35.36 MHz，而氘基频为 25 MHz。这个简化计算展示组分如何移动混杂层。有限电子响应、平行折射率和温度会进一步移动层位，并改变转换波结构；在全波模型中可把上述结果作为组分扫描的初始定位，再检查完整 S 与热色散关系。

推导起点与参考位置：[Fitzpatrick，Cold-Plasma Dielectric Permittivity，式 (5.31)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)；[Mayoral 等，JET 反转少数离子与模转换，§1–2.1](https://scipub.euro-fusion.org/wp-content/uploads/2014/11/EFDP05026.pdf)；[Fukuyama 2025，Wave heating 与 Ion cyclotron wave，PDF 页 20–25](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## 三离子方案的极化设计与实验边界

三离子方案的基本思路是用两个非共振主要组分调节混杂结构，使离子同向旋转电场增强的区域与第三个少量共振组分重合。这样可以用较低的共振粒子浓度获得显著吸收。这里的“三”指参与波动响应的三个离子种群。

对于三个近似热分布、忽略较大 Doppler 位移的种群，常用的荷质比条件是

$$
\left(\frac ZA\right)_2<
\left(\frac ZA\right)_3<
\left(\frac ZA\right)_1,
$$


其中 \(A\) 是质量数近似，第三种群为共振吸收者，两个主要种群分列两侧。典型写法 D–(\({}^3\mathrm{He}\))–H 对应 \(1/2<2/3<1\)，括号表示共振组分。该不等式提供方案选择的物理线索；最佳浓度、吸收效率和沉积位置还需求解波动响应，精确计算使用实际质量、热分布、密度剖面和波场。

Kazakov 等 2017 年在 C-Mod/JET 验证了低浓度共振离子产生高能 $^3$He 并慢化加热的方案。2023 年综述进一步比较浓度、混杂/共振层相对位置和快离子演化；结论对应各实验工况。

扩展三种群方案可用快离子的 $k_\parallel v_\parallel$ 位移，使与主要组分同荷质比的粒子在有利极化区共振。“三种群”因而不必是三种元素；须区分热荷质比夹层与速度位移。

来源：[Kazakov 等，*Efficient generation of energetic ions in multi-ion plasmas by radio-frequency heating*，Nature Physics 13，973–978，2017，摘要及实验结论](https://www.nature.com/articles/nphys4167)；[Kazakov 等 2023 综述，PDF 第 2–4 页](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)。

### 三离子最佳配比的冷截止估算

在痕量第三离子极限，记两个主要离子的电荷份额 $f_j=Z_jX_j$，满足 $f_1+f_2=1$。利用准中性，将左旋介电系数在 $\omega\ll|\Omega_e|$、大等离子体响应下化为与 $-[f_1/(\omega-\Omega_1)+f_2/(\omega-\Omega_2)]$ 成正比。令该近似左截止落在 $\omega=\Omega_3$，通分后得 $\Omega_3=f_1\Omega_2+f_2\Omega_1$，从而 $X_1^*=(\Omega_1-\Omega_3)/[Z_1(\Omega_1-\Omega_2)]$，$X_2^*=(\Omega_3-\Omega_2)/[Z_2(\Omega_1-\Omega_2)]$，即 Kazakov 等式 (1)。

H-($^3$He)-D 中三个荷质比分别取 1、2/3、1/2，得到主要组分起点 $X_H^*=2/3$、$X_D^*=1/3$。再加入 $X_{He3}=0.002$ 时，若保持主要组分 2∶1 的电荷比，准中性给 $X_H=0.664$、$X_D=0.332$，双电荷氦贡献余下 0.004。原文的有限谱和有限痕量优化位于这一近似点附近，并讨论 H-D 约 70%–30% 的工况。将公式的几何配比与实测组分、热模型分开记录，就能解释为何实际最优值会相对这个起点移动。

推导起点与参考位置：[Kazakov 等 2023，三离子综述，PDF 页 2–3、式 (1) 与图 1–2](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)；[Fitzpatrick，Cold-Plasma Dielectric Permittivity，式 (5.31)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)。

## 从共振条件到可核验的吸收结论

ICRH 解释连接相位同步、自洽场与能量去向：单粒子式给共振，冷色散给传播/极化，热动理学给净吸收与分布。

设物种 \(s\) 的复电流为 \(\widetilde{\mathbf J}_s\)，时间平均局部功率密度为

$$
Q_s=\frac12\operatorname{Re}
\left(\widetilde{\mathbf E}^{\dagger}\widetilde{\mathbf J}_s\right),
\qquad [Q_s]=\mathrm{W\,m^{-3}}.
$$


这里 \(Q_s>0\) 表示场向该物种传能。若 \(\widetilde{\mathbf J}_s=\boldsymbol\sigma_s\widetilde{\mathbf E}\)，有

$$
Q_s=\frac12\widetilde{\mathbf E}^{\dagger}
\frac{\boldsymbol\sigma_s+\boldsymbol\sigma_s^{\dagger}}2
\widetilde{\mathbf E}.
$$


因此导电率的 **Hermitian 部分**决定平均做功；在本文 \(e^{-i\omega t}\) 约定下，若 \(\boldsymbol\sigma_s=-i\omega\epsilon_0\boldsymbol\chi_s\)，相同功率对应介电极化率的 \((\boldsymbol\chi_s-\boldsymbol\chi_s^{\dagger})/(2i)\) 部分。这个因子 i 的变换说明导电率与介电率采用不同的耗散分解。

等价的显式功率公式为

$$
Q_s=\frac{\omega\epsilon_0}{2}
\widetilde{\mathbf E}^{\dagger}
\frac{\boldsymbol\chi_s-\boldsymbol\chi_s^{\dagger}}{2i}
\widetilde{\mathbf E}.
$$


对于冷、无碰撞、实频且远离奇点的稳定响应，介电张量可为 Hermitian，因而没有有限的净耗散；冷极点要求改进模型或规定因果极限，以确定有限能流。对热分布还需区分阻尼和驱动：适当的单调平衡分布常给出阻尼，具有自由能的非热分布则可能向波传能。射频形成的高能尾部通过慢化逐步向背景传能。

分别报告吸收物种、半径、谐波、直接电子吸收、快离子碰撞传能及损失，并标明冷波、热全波或耦合 FP 模型。

来源：[Fitzpatrick，§7.6，热磁化响应及共振分母](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，PDF 第 20–21、32–36 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[Kazakov 等 2023，PDF 第 2 页，吸收与碰撞慢化的区分](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)。功率等式由实场周期平均和所列线性响应约定直接推出。

### 用时间平均直接验证复导电率做功

对单一场分量取 $\widetilde\sigma=\sigma_R+i\sigma_I$、峰值复幅 $\widetilde E=E_0$。实场为 $E=E_0\cos\omega t$，电流为 $J=E_0(\sigma_R\cos\omega t+\sigma_I\sin\omega t)$；对周期积分，交叉项为零，得到 $\langle JE\rangle=\sigma_RE_0^2/2$。再由 $\sigma=-i\omega\epsilon_0\chi$ 可得 $\operatorname{Im}\chi=\sigma_R/(\omega\epsilon_0)$，与介电耗散表达完全一致。

教学设 $\sigma=0.020+0.030i$ S/m、$E_0=100$ V/m、f=40 MHz，则平均吸收密度为 100 W/m³，在均匀 2 m³ 内为 200 W；对应 $\operatorname{Im}\chi\simeq8.9876$。直接离散采样一个周期并积分 $J(t)E(t)$ 可复算相同结果，而纯虚导电率只保留往返交换项。对张量响应则先计算 Hermitian 部分，再做 $\widetilde{\mathbf E}^{\dagger}\boldsymbol\sigma_H\widetilde{\mathbf E}/2$，这也给全波后处理提供了可以独立复核的功率表达。

推导起点与参考位置：[Fitzpatrick，Cold-Plasma Dielectric Permittivity，式 (5.31)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)；[Fitzpatrick，Waves in Magnetized Plasmas，式 (7.53)–(7.78)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)。

## 波吸收、快离子分布与碰撞传能

ICRH 中“波被某物种吸收”和“该物种热温度上升”是两个步骤。少数离子或谐波共振可首先形成非 Maxwell 高能尾部，且垂直与平行速度方向的展宽不同。用一个等效温度代替整个分布，可能保留总能量却改变吸收、碰撞传能、轨道损失和诊断响应。Alcator C-Mod 的公开研究已比较快离子诊断与 full-wave/Fokker–Planck 模型，并报告分布各向异性的影响；该比较对应所列放电与诊断响应。[MIT PSFC，2006 年报告摘要，快离子电荷交换诊断及 AORSA/CQL3D 比较](https://library.psfc.mit.edu/catalog/reports/2000/06rr/06rr008/abstract.php)。

令局地分布函数满足 $\int f_h\,d^3v=n_h$，其中 $n_h$ 为数密度（$\mathrm{m^{-3}}$），因此 $f_h$ 的 SI 单位是 $\mathrm{s^3m^{-6}}$。在回旋平均、弹跳平均等近似适用时，可示意写成

$$
\partial_t f_h=C_h[f]+\mathcal Q_{\mathrm{RF}}[f_h]
+S_h-\mathcal L_h,
\qquad
\mathcal Q_{\mathrm{RF}}[f_h]
=\nabla_v\cdot(\mathbf D_{\mathrm{RF}}\cdot\nabla_v f_h).
$$


$h$ 标记被演化的共振粒子群；碰撞项、源和损失均须独立定义。此处用局地直角速度坐标展示准线性扩散结构，实际轨道平均坐标必须保留相空间 Jacobian。$\mathbf D_{\mathrm{RF}}$ 的单位是速度平方每秒，其大小、方向和共振条件由波场、谱和轨道决定，并随波场迭代更新。准线性描述还要求适当的相位去相关；强相干俘获应使用保留相位的动力学模型。

full-wave 解出场及各物种响应，再形成准线性算子并演化分布；更新后的分布改变介电响应，需返回波方程迭代。在相同功率归一化、坐标和积分范围下，至少核对

$$
P_{\mathrm{RF},h}^{\mathrm{wave}}
=\int d^3x\,d^3v\,\frac{m_hv^2}{2}
\mathcal Q_{\mathrm{RF}}[f_h].
$$


左右两侧单位均为 W。差异可能来自轨道映射、谱截断、速度边界或功率归一化，应逐项定位误差来源。已有 AORSA/CQL3D 和 TORIC/CQL3D 耦合研究提供此类建模路线；是否适用本装置仍需核对有限轨道宽度、多共振物种和边界损失。[作者研究摘要，2023 APS DPP：自洽 full-wave/Fokker–Planck 模型](https://meetings-archive.aps.org/dpp/2023/ki02/4/)。

共振粒子能量还满足独立预算：$dW_h/dt=P_{\mathrm{RF},h}+P_{\mathrm{src},h}-P_{h\to e}-\sum_iP_{h\to i}-P_{\mathrm{loss},h}$，其中传能按从该粒子群流出取正。电子、离子分流取决于分布、背景温度和组分，没有普遍固定比例。波直接加热电子与快离子随后碰撞加热电子应分开记录；在总等离子体预算中，内部碰撞交换相互抵消，使总能量守恒。[Mayoral 等，JET 反转少数离子与模式转换实验，§1 的碰撞慢化及电子/离子传能讨论](https://scipub.euro-fusion.org/wp-content/uploads/2014/11/EFDP05026.pdf)。

### 速度扩散的粒子数与能量矩

用教学模型 $\partial_t f=D_v\nabla_v^2f$ 说明波致扩散的矩检查，$D_v$ 单位为 m²/s³，并假定分布及其梯度在速度无穷远衰减。先对速度积分，用散度定理得 $d\int f d^3v/dt=0$。再乘 $mv^2/2$，两次分部积分给 $dW/dt=(mD_v/2)\int f\nabla_v^2v^2d^3v=3mnD_v$，其中 $\nabla_v^2v^2=6$。

设氘密度 $n=10^{17}$ m⁻³、$D_v=10^{12}$ m²/s³，模型的能量输入密度为约 1003.1 W/m³。对初始各向同性 Gaussian 分布，每个速度分量方差按 $\sigma_v^2(t)=\sigma_{v0}^2+2D_vt$ 增长；取 $\sigma_{v0}=10^5$ m/s、t=1 ms，方差从 $10^{10}$ 增到 $1.2\times10^{10}$ m²/s²，能量密度增加 1.0031 J/m³。数值求解可同时比较粒子积分、二阶矩及边界通量。实际 ICRH 扩散张量集中在共振方向，碰撞项再把这个能量矩传递给热背景。

推导起点与参考位置：[Fitzpatrick，Waves in Magnetized Plasmas，式 (7.53)–(7.78)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，Wave heating 与 Ion cyclotron wave，PDF 页 20–25](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[IAEA Fusion Physics，§5.1.2–5.1.4，书页 535–545；§5.2.1，书页 571–573](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)。

## ICRF 功率链与电压电流应力

典型能量路径为射频源和功率放大器、传输线及功率分配、匹配网络、真空馈通、天线电流带（strap）及邻近面对等离子体部件。假负载承担调试或特定网络中的反射功率，冷却和测量通道跨越整条链。实际位置、元件数量与连接随具体设计改变。ITER 的公开工程介绍可用于理解射频源、传输和匹配的接口；其中目标功率属于项目设计描述，作为设计目标记录。[ITER，离子回旋系统工程链说明](https://www.iter.org/node/20687/how-pump-20-mw-power-1-gram-plasma)。

每个接口应标出参考平面、端口方向、频率范围、阻抗与功率定义。对单频峰值复振幅，令 $\widetilde V=Z\widetilde I$、$Z=R+iX$，平均有功功率是

$$
P=\frac12\operatorname{Re}(\widetilde V\widetilde I^*)
=\frac12R|\widetilde I|^2
=R|I_{\mathrm{RMS}}|^2.
$$


$V$、$I$、$Z$ 的单位分别为 V、A、$\Omega$。若仪器或仿真采用 RMS 复幅值，就不应再乘 $1/2$。电抗与谐振储能会造成很大的局地电压、电流，即使净有功功率相同，馈通、接触件和电流带的电应力也可能明显不同。须保存端口功率之外的电压电流峰值及其空间位置。[Ohio State Ximera，Power Transfer on a Transmission Line，峰值幅度下的入射、反射与净功率](https://ximera.osu.edu/electromagnetics/electromagnetics/impedanceMatching/digInPoweronTL)；[MIT，Electromagnetic Fields and Energy，第 14.6 节，传输线与反射系数](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)。

馈通电场/真空、接触热源、热膨胀、磁载荷和冷却须对应同版几何。法拉第屏后剩余平行近场与鞘层驱动由场计算和测量确定。

### 复功率与电压电流应力

采用 RMS 复幅值，复功率为 $\mathcal S=VI^*=|I|^2(R+iX)$。其实部给有功功率 $P=R|I|^2$，虚部给无功功率 $Q=X|I|^2$；由此逐步得到 $|I|=\sqrt{P/R}$、$|V|=\sqrt{P/R}\sqrt{R^2+X^2}$。无功量描述周期内往返交换的能量，匹配网络通过电抗变换调节源端阻抗，局部大电流和大电压仍由各支路决定。

教学负载取 $Z=3+4i\ \Omega$、$P=1$ MW，得到 $I_{RMS}=577.35$ A、$V_{RMS}=2.887$ kV、$Q=1.333$ Mvar，视在功率为 1.667 MVA。峰值电压是 $\sqrt2V_{RMS}=4.082$ kV。若在相同有功功率下电阻降为 1.5 Ω，电流增至 816.50 A；于是接触件的 $I^2R_c$ 热源随电流平方变化。这样的接口表同时列有功、峰值电压、电流和相位，能将功率链的需求落实到馈通与连接件的热电计算。

推导起点与参考位置：[MIT Electromagnetic Fields and Energy，§14.6，反射与阻抗变换](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)；[Monakhov 等 2013，JET external conjugate-T，§2–5](https://arxiv.org/pdf/1309.4644)。

## 天线加载与共轭 T 匹配

设计应连接核心吸收与边缘耦合两个问题。天线电流带的幅值、相位、间距及几何产生一段 $k_\parallel$ 谱，其分布由天线和边缘负载共同决定。边缘密度剖面决定指定频率与谱分量的快波截止和衰逝区。增加天线至可传播区域的距离，通常削弱耦合；仅给核心密度或天线到最后闭合磁面的距离不足以确定加载。JET 的局地充气实验提供了改变天线前沿 SOL 密度、改善耦合的案例；能否复用于另一装置，还受燃料、辐射和边界工况约束。[EUROfusion，Experiments on Gas Puffing to Enhance ICRF Antenna Coupling](https://scipub.euro-fusion.org/archives/jet-archive/experiments-on-gas-puffing-to-enhance-icrf-antenna-coupling)。

对实正参考阻抗 $Z_0$ 的单端口，以同一平面上的入射和反射行波定义

$$
\Gamma=\frac{Z_L-Z_0}{Z_L+Z_0},\qquad
P_{\mathrm{acc}}=P_{\mathrm{fwd}}-P_{\mathrm{rev}}
=P_{\mathrm{fwd}}(1-|\Gamma|^2).
$$


该式给的是网络接受功率；馈线、金属、边缘鞘层等仍可能消耗其中一部分。若只有一个端口入射且其他端口匹配，$\Gamma=S_{11}$；多端口同时驱动时，应采用功率归一化的 $\mathbf b=\mathbf S\mathbf a$，在约定 $|a_p|^2$、$|b_p|^2$ 为 W 后，总净输入为 $\sum_p(|a_p|^2-|b_p|^2)$。给定多端口相位组合后，应使用有源反射与互耦分析。[MIT，第 14.6 节](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)；[Monakhov 等，JET 外部 conjugate-T 系统，§2–4](https://arxiv.org/pdf/1309.4644)。

以选定端口包围的稳态射频系统为边界，应让净输入等于馈线与金属损耗、各物种体吸收、另外单列的边缘损耗以及离开计算域的功率之和。各项按互斥边界定义，含边缘吸收的体积分应扣除已另列的鞘层功率；若边界改变，预算也要重写。瞬态另需计入储能变化。反射、核心吸收和热约束分别对应传播、粒子做功和输运三个阶段。

保存平衡、组分、剖面、SOL/壁、端口模、幅相及版本；分别扩大空间、谱、谐波、速度和轨道范围，以沉积及电流稳定性检验收敛。

### 共轭 T 支路的负载响应

把两条相同电阻、相反电抗的支路写为 $Z_1=R+iX$、$Z_2=R-iX$。先相加导纳：$Y_T=1/Z_1+1/Z_2=2R/(R^2+X^2)$，再取倒数，得到纯实 $Z_T=(R^2+X^2)/(2R)$。在两支路电阻同步改变的简化模型中，虚部仍相消，而 $Z_T$ 对 R 呈先降后升的曲线，这是负载容忍性的电路起点。

取固定 $X=6\ \Omega$，基准 $R=2\ \Omega$ 时 $Z_T=10\ \Omega$；负载增至 $R=6\ \Omega$ 后 $Z_T=6\ \Omega$，以 10 Ω 为参考有 $\Gamma=-0.25$、接受功率份额 93.75%。进一步增至 $R=18\ \Omega$，$Z_T$ 又回到 10 Ω。这个练习只演示同步扰动：若两支路变化不同，重新计算复导纳便会出现虚部。设计仿真因此需要扫描共同负载变化与不平衡变化两个方向，并在实际传输线模型中检查峰值电应力。

![两支路同步扰动仍给纯实 T 点阻抗，但阻抗数值随电阻变化。](/assets/diagrams/heat-icrh-match.svg)

两支路同步扰动仍给纯实 T 点阻抗，但阻抗数值随电阻变化。

推导起点与参考位置：[Monakhov 等 2013，JET external conjugate-T，§2–5](https://arxiv.org/pdf/1309.4644)；[MIT Electromagnetic Fields and Energy，§14.6，反射与阻抗变换](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)。

## RF 鞘层、近场与杂质释放

天线周围平行射频电场可驱动与材料表面连接的场线上的射频鞘层。鞘层具有非线性电流—电压关系，射频振荡可以整流成额外的直流势差，改变入射离子能量和表面热负荷，并促进杂质溅射。这条边缘通道与核心离子回旋共振吸收不同，设计时应同时优化核心沉积和边缘负荷。[Bobkov 等，Progress in reducing ICRF-specific impurity release in ASDEX Upgrade and JET，作者公开稿](https://scipub.euro-fusion.org/wp-content/uploads/WPMST1CP16_14736_submitted.pdf)。

常用的一个驱动指示量是沿相关磁力线的 $\int E_\parallel\,dl$，单位 V。由它求实际整流鞘层电压时，还需考虑两端边界、鞘层阻抗、粒子响应、磁场入射角和局地等离子体条件。线性、冷、体介电模型加理想金属边界，通常未包含全部非线性鞘层物理；鞘层模型应显式包含非线性电流—电压响应。

工程上，电流带排列、相位与功率平衡、天线框架上的感应电流、限制器几何和磁连接共同影响近场。ASDEX Upgrade 三电流带天线的实验工作说明，通过设计和电气调谐降低相关近场及感应电流，可以减小 ICRF 特有的钨释放；该案例支持一种设计原则，最优功率比随天线和磁连接变化。[Bobkov 等，First results with 3-strap ICRF antennas in ASDEX Upgrade，2016 年实验论文摘要](https://portal.fis.tum.de/en/publications/first-results-with-3-strap-icrf-antennas-in-asdex-upgrade/)。

近场与红外、局地杂质源、电位/电流及核心杂质并列比较，校正发射率、观察角和视线积分。局地溅射与后续输运分开反演，反射、鞘驱动和核心杂质分别验证。

### 非线性电子通量如何产生鞘层整流

设电子为 Boltzmann 响应、离子只感受周期平均鞘势，鞘层电压降为 $V_s=V_{dc}+V_{rf}\cos\omega t$。平均电子通量正比于 $e^{-eV_{dc}/T_e}I_0(eV_{rf}/T_e)$，其中 $I_0(a)=(2\pi)^{-1}\int_0^{2\pi}e^{a\cos\theta}d\theta$。令平均电子通量仍等于给定离子通量，与无 RF 的浮动平衡相除并取对数，得到额外直流电压降 $\Delta V_{dc}=(T_e/e)\ln I_0(eV_{rf}/T_e)$。

取温度能量 10 eV、$V_{rf}=10$ V，则参数 a=1，$I_0(1)=1.26606588$，所以额外直流鞘降为 2.3591 V。小幅近似先取 $I_0(a)\simeq1+a^2/4$，再用 $\ln(1+x)\simeq x$，得到 $\Delta V_{dc}\simeq(T_e/e)a^2/4=2.5$ V；两次展开都以 $a\ll1$ 为条件，此例 a=1 时与精确周期平均相差约 6%。单电荷离子的附加落壁能量约 2.3591 eV。此局部算例假定 RF 电压已给定、电子快速响应、离子通量固定且无二次电子发射；装置计算再将天线近场、沿磁力线连接与鞘层响应自洽耦合。Bobkov 等的近场与杂质实验为这种整流机制提供工程背景。

推导起点与参考位置：[MIT 16.522，Lecture 9，式 (1)–(4) 的 Boltzmann 电子与壁通量](https://www.ocw.mit.edu/courses/16-522-space-propulsion-spring-2015/0bd5cd04b2040f2324f3d6a78e8fb15b_MIT16_522S15_Lecture9.pdf)；[Bobkov 等，Progress in reducing ICRF-specific impurity release，§1–3](https://scipub.euro-fusion.org/wp-content/uploads/WPMST1CP16_14736_submitted.pdf)。

## ELM 负载响应与快速撤功率

控制目标不只是维持设定射频功率，还包括电流带相位与功率平衡、源端匹配以及对负载变化的响应。等离子体边缘密度随放电演化，ELM 等事件可使天线负载快速变化；机械调谐器、频率调节与功率回退具有不同带宽及功能，应结合传输链设计，并让快慢回路分别承担相应动态任务。

负载容忍网络使发射机看到的反射对负载变化较不敏感，也可能减弱某些电弧在源端反射信号中的特征。JET 的 external conjugate-T 工作因此将专门的电弧检测与实时匹配结合，用多位置电信号识别天线内部放电。[Monakhov 等，Design and operations of load-tolerant external conjugate-T matching system，§5 的匹配及 AWACS 电弧检测](https://arxiv.org/pdf/1309.4644)。

行波、电应力、电弧、真空和冷却信号分别关联失效模式，记录单位、标定、采样率、量程和失效状态；动作记录检测至撤功率延迟、执行链及复位条件。

阈值来自部件额定、热电分析和验收并记录版本。联锁试验覆盖传感器失效、通信异常及重启；射频、真空、冷却和等离子体信号统一时间轴。

### 撤功率延迟如何变成附加能量

把故障发生到射频撤除之间的功率积分，得到 $E_{delay}=\int_0^{t_d}P(t)dt$。若这段时间功率近似恒定，则为 $P_0t_d$；同时还应加入可能释放到同一故障路径的网络储能。对等效电容，该项由 $dE=VdQ$、$Q=CV$ 积分得 $E_C=CV^2/2$。总故障能量的上界估算因而为 $P_0t_d+E_C$，并随放电路径的实际分流修正。

教学设定 $P_0=2$ MW、检测和执行总延迟 10 μs、故障路径等效电容 1 nF、初始电压 30 kV，则持续输入 20 J，电容贡献 0.45 J，总计 20.45 J。若延迟减为 5 μs，总计降至 10.45 J；进一步改进需同时考虑储能与撤功率尾部。该计算将传感器、逻辑、源关断三个时间段放到同一能量账本中。JET 共轭 T 系统的 AWACS 案例说明，快速保护还需观测支路波幅，才能覆盖源端反射不明显的内部电弧。

推导起点与参考位置：[Monakhov 等 2013，JET external conjugate-T，§2–5](https://arxiv.org/pdf/1309.4644)；[MIT Electromagnetic Fields and Energy，§14.6，反射与阻抗变换](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)。

## 射频量热与等离子体沉积诊断

低功率先在校准/去嵌入参考面检验多端口和相位；高功率再检验温升、接触及非线性。等离子体耦合、鞘层和核心吸收分别验证。

功率测量需核查方向耦合器的方向性、校准与线缆衰减、峰值和 RMS 定义，以及大反射条件下入射/反射通道的串扰。两处参考平面的净功率差应与中间链路损耗相容；有条件的稳态量热测量可作交叉检验，瞬态则需考虑热容、冷却延迟和储能。仪器精度和系统误差必须随结果一同报告，以明确耦合效率的精度。[Monakhov 等，JET 系统论文，§4 的电路与功率测量](https://arxiv.org/pdf/1309.4644)。

等离子体验证可比较电子温度响应、离子温度、储能、辐射、快离子谱及损失诊断。射频功率调制后温度变化的斜率包含沉积与输运效应，其局地吸收解释依赖所选时间窗。JET 的 FFT/BIS 沉积分析明确限定密度响应和输运时间尺度。[Mayoral 等，§2.1 的调制、ECE 测量及分析假设](https://scipub.euro-fusion.org/wp-content/uploads/2014/11/EFDP05026.pdf)。快离子诊断也有其能量和俯仰角响应；合理做法是将模拟分布输入合成诊断，在实验可观测量上比较，并保留背景剖面、仪器响应和不确定度。[Tang 等，2005 APS DPP：C-Mod 中性粒子分析仪与 CQL3D 合成诊断比较](https://meetings-archive.aps.org/dpp/2005/kp1/30/)。

数值检验分别记录：全波端口/物种功率；FP 粒子数、碰撞成对能量与速度边界；耦合 RF 功率一致性。加密网格、谱、速度域和轨道后，再以独立诊断及输入误差检验物理一致性。

### 量热与射频测量如何相互校验

稳态水冷量热从焓流守恒出发：$P_c=\dot m(h_{out}-h_{in})\simeq\dot m c_p\Delta T$。对相互独立的小误差，一阶传播给 $(u_P/P_c)^2=(u_{\dot m}/\dot m)^2+(u_{\Delta T}/\Delta T)^2$，此例把比热视为已知常数。与射频净输入 $P_{RF}$ 比较时，用合成标准不确定度 $\sqrt{u_P^2+u_{RF}^2}$ 衡量差值，而不是分别看两个仪表的末位数字。

取流量 $1.00\pm0.02$ kg/s、温差 $4.00\pm0.10$ K、$c_p=4180$ J/(kg·K)，得到 $P_c=16.72\pm0.54$ kW。若同一边界的射频测量为 $17.0\pm0.6$ kW，两者相差 0.28 kW，约为合成标准不确定度的 0.35 倍。瞬态试验则把固体和冷却水的储能变化加入功率平衡；因此应先对齐流量、温度与射频信号的传输延迟，再比较脉冲能量积分。

推导起点与参考位置：[Monakhov 等 2013，JET external conjugate-T，§2–5](https://arxiv.org/pdf/1309.4644)。

## 组分扫描怎样切换少数离子与模转换通道

改变少数离子浓度，不仅改变共振粒子数，还会移动快波的左截止与离子—离子混杂层，进而改变离子同向场和转换分支。因而 ICRH 的浓度扫描同时是波传播实验、快离子分布实验和加热通道实验；只比较最终温度会把这些过程混在一起。

[Mayoral 等 §1–2.1](https://scipub.euro-fusion.org/wp-content/uploads/2014/11/EFDP05026.pdf)讨论 JET 的 $(^3\mathrm{He})H$ 工况：约 3.6 T、2 MA、中心电子密度 $3\times10^{19}$ m⁻³，扫描 $n_{He3}/n_e$ 时在约 2% 附近出现显著模转换。同文引用的 $(^3\mathrm{He})D$ 有利模转换浓度约为 12%–20%。这是不同主体离子、传播层次和极化条件下的结果，不存在通用的“模转换固定百分比”。

### 先由准中性统一浓度，再比较波场

准中性给 $n_e=n_{main}+2n_{He3}$。令 $X=n_{He3}/n_e$，则主体单电荷离子的电子归一化数密度为 $n_{main}/n_e=1-2X$，氦的电荷份额为 $2X$。若改为按全部离子原子核计数，浓度是

$$
x_{He3}=\frac{n_{He3}}{n_{main}+n_{He3}}
=\frac{X}{1-X}.
$$


因此 X=0.02 对应电荷份额 0.04、原子核份额约 0.02041；X=0.12–0.20 对应电荷份额 0.24–0.40、原子核份额约 0.1364–0.2500。上述转换只是粒子计数，尚未决定功率份额。把统一后的浓度代入本页冷介电张量，求出 $L-N_\parallel^2=0$ 的左截止和 $S-N_\parallel^2=0$ 的混杂层，再与 $\omega-k_\parallel v_\parallel=\Omega_{He3}$ 共振区比较，才进入少数离子吸收与模转换的竞争。

### 调制相位区分直接电子吸收与慢化传能

少数离子先储能再慢化，会使电子热输入相对射频调制滞后；直接电子吸收则少了这一步。用线性两通道模型定量说明：设射频功率扰动为 $\delta P e^{i\omega_mt}$，其中比例 $f_d$ 直接进入电子、比例 $f_h$ 进入快离子；快离子扰动能量为 $\delta W_h$，以固定 $\tau_s$ 慢化，释放功率中比例 $g_e$ 进入电子。能量守恒给

$$
\frac{d\delta W_h}{dt}+\frac{\delta W_h}{\tau_s}=f_h\delta P e^{i\omega_mt}.
$$


令稳态响应 $\delta W_h=\widetilde W_he^{i\omega_mt}$，代入后解得 $\widetilde W_h=f_h\delta P\tau_s/(1+i\omega_m\tau_s)$。再把直接项与慢化项相加，得到电子加热的复响应

$$
\frac{\widetilde P_e}{\delta P}
=f_d+\frac{g_ef_h}{1+i\omega_m\tau_s}.
$$


各份额无量纲，$\tau_s$ 用 s，$\omega_m$ 是调制角频率而非载波频率。低频时两通道都跟随；$\omega_m\tau_s\gg1$ 时，快离子通道振幅衰减并滞后，电子输入逐渐以直接项为主。教学取 $f_d=0.20$、$f_h=0.80$、$g_e=0.50$、$\tau_s=0.05$ s、调制频率 10 Hz，得响应约 $0.2368-0.1156i$，模为 0.2635、相位约 −26.0°。这是电子输入功率响应；实际温度信号还要经过电子热容、输运和仪器响应，不能将其相位直接当作慢化时间。

JET 的调制、ECE 与快离子证据正可从这条能量路径联合解释：快离子尾约束离子吸收，快速电子热响应约束直接沉积，频率扫描帮助分离中间储能。其分析假设与测量范围见 [Mayoral 等 §2.1 的 FFT/BIS 方法](https://scipub.euro-fusion.org/wp-content/uploads/2014/11/EFDP05026.pdf)。天线方面的共轭 T 负载响应与电弧识别仍由 [Monakhov 等 JET 运行论文 §2–5](https://arxiv.org/pdf/1309.4644)约束；良好的匹配确定可输入功率，组分与热响应共同决定这份功率最终加热谁。

[返回辅助加热](../README.md) · [编写说明](../../编写说明.md) · [返回知识库](../../README.md)
