# 离子回旋加热（ICRH / ICRF）

离子回旋加热用射频电场与离子的回旋运动交换能量，再通过碰撞、输运和对分布函数的改变影响背景等离子体。实际效果由波的传播与极化、组分、共振条件、快离子约束及能量转移共同决定。

本专题从单粒子共振推到快波与多离子吸收，再连接射频系统、计算与实验验证。公式使用 SI 制；温度写成 eV 或 keV 时表示温度能量。文中的教学算例、历史实验和装置设计参数分别注明，不能直接作为设备操作限值。

先修：[单粒子运动](../../基础原理/单粒子运动/README.md)、[等离子体波](../../基础原理/等离子体波/README.md)、[动理学与碰撞](../../基础原理/动理学与碰撞/README.md)。核对范围见[内容核验记录](../../核验记录.md)。

## 原理与适用条件

离子回旋加热（ion cyclotron resonance heating，ICRH）把射频功率耦合到磁化等离子体，由具有合适频率、空间结构和偏振的波与粒子交换能量。ICRF（ion cyclotron range of frequencies）强调离子回旋频段；它包含直接离子加热、模转换后的电子加热和电流驱动等应用，不能仅凭名称就断定最终受热对象。托卡马克中常从天线激发快磁声波，经传播到达目标区域，但发射机功率、穿过边界的功率、等离子体吸收功率以及热离子得到的功率是不同量。

本文采用 SI 制，实场写成复振幅的实部：

$$
\mathbf E(\mathbf r,t)=\operatorname{Re}\!\left[\widetilde{\mathbf E}
 e^{i\mathbf k\cdot\mathbf r-i\omega t}\right],\qquad
\mathbf B_0=B_0\hat{\mathbf z},\qquad
\Omega_s=\frac{q_sB_0}{m_s}.
$$

其中 \(\omega>0\)，\(\Omega_s\) **保留电荷符号**：正离子为正，电子为负。回旋频率的正数数值为 \(f_{cs}=|\Omega_s|/(2\pi)\)。密度 \(n_s\) 用 \(\mathrm{m^{-3}}\)，场强用 T，电场用 \(\mathrm{V\,m^{-1}}\)。温度若用 eV，表示温度能量，其数值乘 \(1.602176634\times10^{-19}\) 才得到 J。谐波阶数用整数 \(\ell\)，避免与密度混淆。

常规 ICRH 理论首先要求粒子有可辨认的回旋运动，背景在一个回旋周期内变化较慢，且平衡梯度尺度大于相关粒子的回旋半径。局部冷等离子体近似可用于理解传播和极化；吸收层中的有限温度、Doppler 展宽、有限 Larmor 半径和分布函数演化则通常需要动理学处理。若共振不在受约束区域、波到不了共振区、合适旋向的电场过弱，或者吸收产生的快离子迅速损失，满足频率条件也不保证有效加热。方案选择因此需要同时核对磁场、组分、天线谱、波传播和能量接收对象。

选择工作频率时，也要明确所用的是哪一种离子的基频或谐波，而不能仅给出一个“离子回旋频率”。同一磁场中，氢、氘、氚与氦的荷质比不同；同一频率又可能同时落在一种离子的基频和另一种离子的高次谐波附近。组成测量和杂质分析因此是物理输入，而不是波计算结束后才附加的修正。磁场随位置变化时，计算还必须使用与平衡一致的局部总场强；简单环向场表达式适合教学估算，不能替代装置平衡重建。

频率处在 ICRF 范围也不排除电子直接吸收。电子的回旋频率通常高得多，但具有合适平行相速度的波仍可通过平行电场与电子 Landau 共振，或者通过磁扰动的镜力与电子交换能量。这与“先由离子吸收，再碰撞传能给电子”是两条不同通道，实验分析和数值功率账本应分别列出。本文后续依次建立单粒子、波传播、不同组分方案三个层次，目的就是把这些条件放在同一个可检查的计算链条中。

来源：[Fukuyama，*Integrated Modeling for Heating and Current Drive*，2025，PDF 第 20–26 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[Kazakov 等，*Progress With Applications of Three-Ion ICRF Scenarios for Fusion Research: A Review*，2023，PDF 第 1–2 页](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)。

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

教学算例：氘离子 \(q_i=e\)、\(m_D=3.34358\times10^{-27}\,\mathrm{kg}\)，在严格共振的 \(E_0=10^3\,\mathrm{V\,m^{-1}}\) 中持续 \(1\,\mu\mathrm{s}\)，上述模型给出约 \(24.0\,\mathrm{eV}\)。有限作用时间的第一失谐零点满足 \(|\Delta|=2\pi/t\)，故这里对应 \(|\Delta f|=1\,\mathrm{MHz}\)；这不是碰撞线宽。对已有初始回旋速度的单粒子，能量变化还含初相位交叉项，不能说每个粒子都按同一公式增能。真实等离子体中的热化、展宽和自洽波耗散也不能由这个规定场模型单独推出。

来源：[Fukuyama 2025，PDF 第 20–21 页，波与粒子能量交换](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[Fitzpatrick，§7.7 *Parallel Wave Propagation*，式 7.98–7.101](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node95.html)。上面的有限时间解为在所列假设下直接积分所得。

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

因此频率和磁场共同选择共振层。取氘基频、\(f=40\,\mathrm{MHz}\)、\(B_0=5\,\mathrm T\)、\(R_0=3\,\mathrm m\)，有 \(B_{\mathrm{res}}\simeq5.245\,\mathrm T\)、\(R_{\mathrm{res}}\simeq2.860\,\mathrm m\)。这只是几何算例；尚须给出等离子体边界，才能判断该层是否位于等离子体内，更不能据此推断功率沉积效率。

保留平行运动时，把上式的 \(\omega\) 换成 \(\omega-k_\parallel v_\parallel\)。例如 \(k_\parallel=5\,\mathrm{m^{-1}}\)、\(v_\parallel=10^6\,\mathrm{m\,s^{-1}}\) 给出约 \(0.796\,\mathrm{MHz}\) 的 Doppler 位移。若定义一维热速度标准差 \(v_{ti}=\sqrt{k_BT_i/m_i}\)，在小位移、固定局部波数近似下，共振层径向展宽量级为 \(\Delta R\sim R_{\mathrm{res}}|k_\parallel|v_{ti}/\omega\)。有限轨道宽度、波谱和实际磁几何还会改变沉积宽度。

对具有有限轨道宽度的快离子，共振还可能只在一条完整轨道的某些片段上成立。粒子往返经过不同场强区域，其能量增量取决于入射相位和多次经过之间的相干性。局部共振条件仍是必要的分析入口，却不单独决定整条轨道上的平均扩散率。若把实际几何约化成一维径向沉积模型，应说明是否已平均轨道、如何处理被俘获粒子，以及是否保留天线激发的平行波数分布；否则单一的“共振半径”容易掩盖沉积峰与损失轨道之间的区别。

来源：[Fitzpatrick，§7.6 *Waves in Magnetized Plasmas*，式 7.68–7.74](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，PDF 第 21、32–36 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## 冷介电张量与 ICRF 快波传播

冷模型将各组分视为无压、无碰撞流体，适合首先辨认传播区、截止和极化，不能直接给出热粒子的吸收率。沿用本文时间约定，令 \(\omega_{ps}^2=n_sq_s^2/(\epsilon_0m_s)\)，可写

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

电子的 \(\Omega_e<0\) 必须直接代入，不能把它改成正数后仍保留相同分母。取 \(\mathbf k=(k_\perp,0,k_\parallel)\)、\(N_j=ck_j/\omega\)，Maxwell 方程给出

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

这一近似给出常用的 ICRF 快波传播描述：实系数条件下 \(N_\perp^2>0\) 对应局部传播，负值对应局部倏逝。分子零点可成为截止，分母趋零提示强色散和近似失效，必须检查完整色散及热效应。尤其在混杂层附近，不能因为形式上出现极点就宣布波能已转化为热。

这里的 ICRF fast wave 与 slow wave 是该频段色散分支的名称；它们不能逐项等同于低频理想 MHD 的快、慢磁声波。理想 MHD 还要求 \(\omega\ll|\Omega_i|\) 等尺度条件，而 ICRH 恰在离子回旋频率附近工作。名称相近不意味着近似模型可以互换。

来源：[Fitzpatrick，§5.3 *Cold-Plasma Dielectric Permittivity*，式 5.31–5.39](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)；[§5.4 *Cold-Plasma Dispersion Relation*，式 5.40–5.55](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node69.html)；[Fukuyama 2025，PDF 第 23–25 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

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

于是 \(|\widetilde E_x|^2+|\widetilde E_y|^2=|\widetilde E_{\mathrm{ion}}|^2+|\widetilde E_{\mathrm{opp}}|^2\)，同向基的介电本征值为 \(L=S-D\)。有些文献把旋转分量定义为除以 \(2\)，只要能量公式同步调整即可；不能混用两种归一化比较功率。

在上一条忽略平行电场的近似下，由 \(A\widetilde E_x-iD\widetilde E_y=0\) 得

$$
\left|\frac{\widetilde E_{\mathrm{ion}}}{\widetilde E_{\mathrm{opp}}}\right|^2
=\left|\frac{R-N_\parallel^2}{L-N_\parallel^2}\right|^2.
$$

对于只有一种主要离子的理想冷模型，接近其基频时 \(L\) 的极点可使快波的离子同向分量相对于反向分量受到抑制。这解释了一个关键现象：有回旋共振条件，不代表自洽快波恰好具有强烈的合适旋向电场。因此单组分热离子的快波基频加热往往较弱，多离子组分和谐波方案可以改变情况。

这里讨论的是色散决定的波场，不是外部任意规定的均匀圆电场，因而与前面的单粒子共振解没有矛盾。也不能把冷模型的精确极点当成具有有限能流的真实场解；有限温度、传播边界和阻尼决定实际场与功率分配。少数离子的冷响应在自己的精确回旋频率同样存在极点，少数离子加热的成功并不意味着这个数学奇点消失。

来源：[Fitzpatrick，§5.5 *Wave Polarization*，式 5.56–5.60](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node70.html)；[§5.9 *Parallel Wave Propagation*](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node74.html)；[Fukuyama 2025，PDF 第 24 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## 少数离子基频加热

少数离子加热让一种密度较低、荷质比不同的离子成为主要共振吸收者，主要组分则决定大部分波传播背景。典型教学例是氘等离子体中的氢少数离子，或氘中的 \({}^3\mathrm{He}\)。由于背景的主要回旋频率与少数离子的共振频率分开，少数离子共振区可以存在有利的波极化；吸收又会改变其分布函数，使尾部粒子持续获得垂直能量。

本文使用数密度归一化

$$
X_s=\frac{n_s}{n_e},\qquad \sum_{\text{ions }s}Z_sX_s=1,
$$

其中忽略净电荷密度。双电荷的 \({}^3\mathrm{He}^{2+}\) 在 \(X_s=0.01\) 时贡献的电子电荷份额为 \(0.02\)。若文献使用 \(n_H/(n_H+n_D)\) 或电荷浓度，需先换算再比较，不能看到同样的百分数就当作同一种配比。

浓度太低时，吸收路径长度、每个粒子得到的功率以及快离子能量可能成为限制；浓度提高后，介电响应、离子—离子混杂层和功率分配又会明显变化，并可能进入模转换占重要地位的区域。因此不存在对所有磁场、温度、天线谱和组分都适用的固定最优浓度。“少数”不仅是化学标签，还意味着在特定波动问题中的动力学角色。

在 \(B=5\,\mathrm T\) 的局部均匀场中，以离子核质量计算，氢、氘、氚和 \({}^3\mathrm{He}^{2+}\) 的基频约为 \(76.23\)、\(38.13\)、\(25.46\)、\(50.93\,\mathrm{MHz}\)。这些数值来自 \(f_{ci}=Z_i eB/(2\pi m_i)\)，可用于初步识别候选共振，却没有包含实际场梯度和 Doppler 位移。少数离子获得的能量随后可经 Coulomb 碰撞流向电子和主体离子；直接吸收强、热离子升温强和聚变性能提升是需要分别检验的结论。

来源：[Kazakov 等 2023 综述，PDF 第 2 页，少数离子加热与碰撞慢化](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)；[Fukuyama 2025，PDF 第 24–25、48 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[NIST 2022 基本物理常数表，proton / deuteron / triton / helion mass 条目](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)。

## 二次谐波与有限 Larmor 半径

在均匀规定电场、非相对论圆轨道的单粒子模型中，电场只含相应的基频旋转驱动；不能仅把频率设为 \(2\Omega_i\)，就自动得到与基频相同的长期能量增长。真实传播波具有垂直空间结构，粒子在一个回旋轨道中采样不同相位，这为高次谐波耦合提供了机制。

用 \(\rho_i=v_\perp/|\Omega_i|\) 表示某个粒子的 Larmor 半径，轨道上的相位包含

$$
e^{ik_\perp\rho_i\sin\theta}
=\sum_{\ell=-\infty}^{\infty}J_\ell(k_\perp\rho_i)e^{i\ell\theta}.
$$

这是 Fourier–Bessel 恒等式。实际做功还包含电场偏振与速度的回旋因子，完整耦合涉及相邻阶 Bessel 函数的组合，不能把某一个 \(J_\ell^2\) 直接当成普遍吸收系数。可以稳妥得出的结论是：有限轨道半径使粒子看到更丰富的谐波结构，且耦合强度依赖 \(k_\perp\rho_i\)、偏振和分布函数。

二次谐波满足

$$
\omega-k_\parallel v_\parallel=2\Omega_i.
$$

在冷极限且 \(k_\perp\rho_i\to0\) 时，相应有限 Larmor 半径效应削弱，因此不能把二次谐波加热写成对任意低温等离子体都同样高效。热离子或已存在的快离子可增强相关耦合；功率沉积又反过来改变分布函数，需要波场与动理学联合计算。即使冷模型在 \(2\Omega_i\) 没有与基频相同的单粒子极点，热等离子体仍可具有谐波阻尼，这正说明冷流体描述不足以计算该过程。

以 \(5\,\mathrm T\) 中氘为例，忽略 Doppler 位移的二次谐波约为 \(76.26\,\mathrm{MHz}\)，与氢基频 \(76.23\,\mathrm{MHz}\) 接近。原因是氘荷质比约为氢的一半。这种近邻关系意味着杂质或少量氢可能改变功率分配；不能只标注“氘二次谐波”就忽略同时满足条件的其他组分。实际分辨还需考虑精确质量、磁场分布、速度展宽和波极化。

来源：[Fitzpatrick，§7.6，式 7.68–7.74](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，PDF 第 21、24、32–36 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)。

## 离子—离子混杂层与模转换加热

有两种或更多离子时，介电响应的不同回旋项可以在相邻离子回旋频率之间相互抵消，形成离子—离子混杂结构（ion–ion hybrid，IIH）。在前述快波近似中，\(S-N_\parallel^2\simeq0\) 标记一个需要特别处理的位置；它一般不同于任何单一组分的精确回旋共振。其位置依赖离子荷质比、浓度和 \(N_\parallel\)，因此改变配比可以移动混杂层。

局部冷公式在此预测垂直波数显著增大，而短垂直尺度正会使有限 Larmor 半径效应变得重要。完整热色散关系可以包含离子 Bernstein 波（ion Bernstein wave，IBW）及离子回旋波（ion cyclotron wave，ICW）等分支。入射长波长快波到达非均匀区域后，部分能量可能转入这些短波长分支，这一过程称模转换。究竟转入哪个分支，取决于组分、磁剪切、波数和几何，不能把所有 ICRF 模转换都缩写为同一条路径。

模转换本身是波之间的能流重新分配，不等同于热吸收。若转换波再通过电子 Landau 阻尼、离子回旋阻尼等机制衰减，才把有序波能传给相应粒子。它因此可用于电子加热，也可能涉及离子吸收；实际电子、离子功率份额必须由热响应或诊断确认。即使冷无碰撞方程出现奇异层，也不能从一个无穷大的波数直接读出有限吸收功率。

描述转换效率还需知道入射方向、截止与转换层间距、局部梯度和天线谱。某些参数下存在倏逝区，功率要通过有限宽度区域耦合；若只画一条共振线而不求场结构，就遗漏了决定入射能否到达转换区的部分。实验上可用相位衬度成像等波动诊断识别短波长分支，并结合电子温度响应和功率平衡判断其加热作用，不能只以天线匹配改善作为模转换吸收的证明。

来源：[Lin 等，*Investigation of ICRF Mode Conversion at the Ion-ion Hybrid in Alcator C-Mod*，2003，MIT 作者摘要](https://library.psfc.mit.edu/catalog/reports/2000/03ja/03ja024/03ja024_abs.html)；[Lin 等，*ICRF mode conversion in three-ion species heating experiment and in flow drive experiment on the Alcator C-Mod tokamak*，2017，第 2 节](https://library.psfc.mit.edu/catalog/reports/2010/17ja/17ja050/17ja050_full.pdf)；[Kazakov 等 2023，PDF 第 2–3 页](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)。

## 三离子方案的极化设计与实验边界

三离子方案并不是“任意三种离子一起加热”。其基本思路是用两个非共振主要组分调节混杂结构，使离子同向旋转电场增强的区域与第三个少量共振组分重合。这样可以用较低的共振粒子浓度获得显著吸收。这里的“三”指波动响应中的离子种群，与三体碰撞、三体聚变或三个射频源没有对应关系。

对于三个近似热分布、忽略较大 Doppler 位移的种群，常用的荷质比条件是

$$
\left(\frac ZA\right)_2<
\left(\frac ZA\right)_3<
\left(\frac ZA\right)_1,
$$

其中 \(A\) 是质量数近似，第三种群为共振吸收者，两个主要种群分列两侧。典型写法 D–(\({}^3\mathrm{He}\))–H 对应 \(1/2<2/3<1\)，括号表示共振组分。该不等式提供方案选择的物理线索，但本身不是最佳浓度、吸收效率或沉积位置的完整设计公式；精确计算仍使用实际质量、热分布、密度剖面和波场。

2017 年 Kazakov 等在 Nature Physics 报告了 Alcator C-Mod 和 JET 的相关实验：经调整的多离子混合物可以在很低的共振离子浓度下有效产生高能 \({}^3\mathrm{He}\)，并通过其慢化加热等离子体。这是特定实验条件下的验证，不表示任意三离子组合都具有相同效果。2023 年作者综述进一步整理了多种应用，强调浓度、共振层与混杂层相对位置以及快离子演化的重要性。

还存在利用注入快离子平行速度的扩展方案：通过 \(k_\parallel v_\parallel\) 位移，一个与某主要组分具有相同荷质比的高能种群也可能在有利极化区域共振。因此广义“三种群”不一定等于三种不同化学元素或同位素。解释这类方案时，必须明确是热种群荷质比夹在两者之间，还是借助非零平行速度改变共振；不能把前述不等式无条件推广到所有快离子方案。

来源：[Kazakov 等，*Efficient generation of energetic ions in multi-ion plasmas by radio-frequency heating*，Nature Physics 13，973–978，2017，摘要及实验结论](https://www.nature.com/articles/nphys4167)；[Kazakov 等 2023 综述，PDF 第 2–4 页](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)。

## 从共振条件到可核验的吸收结论

建立一个可信的 ICRH 解释，需要把三个层次连起来：首先检查轨迹上是否存在近似相位同步；其次确认自洽波场在该区域具有合适的振幅、偏振和空间尺度；最后核算实际能量转移及粒子去向。单粒子共振公式只回答第一个层次，冷色散主要服务于第二个层次，而净吸收和分布演化需要包含耗散、相混合或动理学响应。

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

因此导电率的 **Hermitian 部分**决定平均做功；在本文 \(e^{-i\omega t}\) 约定下，若 \(\boldsymbol\sigma_s=-i\omega\epsilon_0\boldsymbol\chi_s\)，相同功率对应介电极化率的 \((\boldsymbol\chi_s-\boldsymbol\chi_s^{\dagger})/(2i)\) 部分。不能笼统地说所有响应张量都由“反 Hermitian 部分”吸收，否则会把导电率与介电率的关系混淆。

等价的显式功率公式为

$$
Q_s=\frac{\omega\epsilon_0}{2}
\widetilde{\mathbf E}^{\dagger}
\frac{\boldsymbol\chi_s-\boldsymbol\chi_s^{\dagger}}{2i}
\widetilde{\mathbf E}.
$$

对于冷、无碰撞、实频且远离奇点的稳定响应，介电张量可为 Hermitian，因而没有有限的净耗散；冷极点要求改进模型或规定因果极限，而不是允许把发散场直接代入功率公式。对热分布还需区分阻尼和驱动：适当的单调平衡分布常给出阻尼，具有自由能的非热分布则可能向波传能。射频加热所形成的高能尾部，也不能自动视为已经转成背景温度。

做定量判断时，应分别报告吸收物种、沉积位置、共振阶数、直接电子吸收、快离子碰撞传能及损失，并说明使用冷波、热全波还是耦合 Fokker–Planck 模型。这样才能把“找到共振层”推进到“验证加热有效”，也能定位模型之间的不一致，而不是把所有功率都归入一个未加区分的加热效率。

来源：[Fitzpatrick，§7.6，热磁化响应及共振分母](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)；[Fukuyama 2025，PDF 第 20–21、32–36 页](https://www.iter.org/sites/default/files/media/2025-07/l-8_fukuyama.pdf)；[Kazakov 等 2023，PDF 第 2 页，吸收与碰撞慢化的区分](https://pure.mpg.de/rest/items/item_3541989_4/component/file_3547501/content)。功率等式由实场周期平均和所列线性响应约定直接推出。

## 波吸收、快离子分布与碰撞传能

ICRH 中“波被某物种吸收”和“该物种热温度上升”是两个步骤。少数离子或谐波共振可首先形成非 Maxwell 高能尾部，且垂直与平行速度方向的展宽不同。用一个等效温度代替整个分布，可能保留总能量却改变吸收、碰撞传能、轨道损失和诊断响应。Alcator C-Mod 的公开研究已比较快离子诊断与 full-wave/Fokker–Planck 模型，并报告分布各向异性的影响；这属于特定实验和诊断范围内的证据，不是任何装置都满足同一分布的证明。[MIT PSFC，2006 年报告摘要，快离子电荷交换诊断及 AORSA/CQL3D 比较](https://library.psfc.mit.edu/catalog/reports/2000/06rr/06rr008/abstract.php)。

令局地分布函数满足 $\int f_h\,d^3v=n_h$，其中 $n_h$ 为数密度（$\mathrm{m^{-3}}$），因此 $f_h$ 的 SI 单位是 $\mathrm{s^3m^{-6}}$。在回旋平均、弹跳平均等近似适用时，可示意写成

$$
\partial_t f_h=C_h[f]+\mathcal Q_{\mathrm{RF}}[f_h]
+S_h-\mathcal L_h,
\qquad
\mathcal Q_{\mathrm{RF}}[f_h]
=\nabla_v\cdot(\mathbf D_{\mathrm{RF}}\cdot\nabla_v f_h).
$$

$h$ 标记被演化的共振粒子群；碰撞项、源和损失均须独立定义。此处用局地直角速度坐标展示准线性扩散结构，实际轨道平均坐标必须保留相空间 Jacobian。$\mathbf D_{\mathrm{RF}}$ 的单位是速度平方每秒，其大小、方向和共振条件由波场、谱和轨道决定，不是任意指定的“加热系数”。准线性描述还要求适当的相位去相关；强相干俘获不能自动归入普通扩散。

full-wave 解出场及各物种响应，再形成准线性算子并演化分布；更新后的分布改变介电响应，需返回波方程迭代。在相同功率归一化、坐标和积分范围下，至少核对

$$
P_{\mathrm{RF},h}^{\mathrm{wave}}
=\int d^3x\,d^3v\,\frac{m_hv^2}{2}
\mathcal Q_{\mathrm{RF}}[f_h].
$$

左右两侧单位均为 W。差异可能来自轨道映射、谱截断、速度边界或功率归一化，不能单靠强制缩放掩盖。已有 AORSA/CQL3D 和 TORIC/CQL3D 耦合研究提供此类建模路线；是否适用本装置仍需核对有限轨道宽度、多共振物种和边界损失。[作者研究摘要，2023 APS DPP：自洽 full-wave/Fokker–Planck 模型](https://meetings-archive.aps.org/dpp/2023/ki02/4/)。

共振粒子能量还满足独立预算：$dW_h/dt=P_{\mathrm{RF},h}+P_{\mathrm{src},h}-P_{h\to e}-\sum_iP_{h\to i}-P_{\mathrm{loss},h}$，其中传能按从该粒子群流出取正。电子、离子分流取决于分布、背景温度和组分，没有普遍固定比例。波直接加热电子与快离子随后碰撞加热电子应分开记录；在总等离子体预算中，内部碰撞交换相互抵消，不能把它们再加一次当成新输入。[Mayoral 等，JET 反转少数离子与模式转换实验，§1 的碰撞慢化及电子/离子传能讨论](https://scipub.euro-fusion.org/wp-content/uploads/2014/11/EFDP05026.pdf)。

## 设备组成与接口

典型能量路径为射频源和功率放大器、传输线及功率分配、匹配网络、真空馈通、天线电流带（strap）及邻近面对等离子体部件。假负载承担调试或特定网络中的反射功率，冷却和测量通道跨越整条链。实际位置与连接随设计改变，不能把这条功能路径当作固定的元件数量或采购方案。ITER 的公开工程介绍可用于理解射频源、传输和匹配的接口；其中目标功率属于项目设计描述，不等于已在等离子体中实现。[ITER，离子回旋系统工程链说明](https://www.iter.org/node/20687/how-pump-20-mw-power-1-gram-plasma)。

每个接口应标出参考平面、端口方向、频率范围、阻抗与功率定义。对单频峰值复振幅，令 $\widetilde V=Z\widetilde I$、$Z=R+iX$，平均有功功率是

$$
P=\frac12\operatorname{Re}(\widetilde V\widetilde I^*)
=\frac12R|\widetilde I|^2
=R|I_{\mathrm{RMS}}|^2.
$$

$V$、$I$、$Z$ 的单位分别为 V、A、$\Omega$。若仪器或仿真采用 RMS 复幅值，就不应再乘 $1/2$。电抗与谐振储能会造成很大的局地电压、电流，即使净有功功率相同，馈通、接触件和电流带的电应力也可能明显不同。须保存端口功率之外的电压电流峰值及其空间位置。[Ohio State Ximera，Power Transfer on a Transmission Line，峰值幅度下的入射、反射与净功率](https://ximera.osu.edu/electromagnetics/electromagnetics/impedanceMatching/digInPoweronTL)；[MIT，Electromagnetic Fields and Energy，第 14.6 节，传输线与反射系数](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)。

机械、电气和真空接口也不能分开验收后便假定组合有效。馈通陶瓷承担电场和真空边界，接触电阻造成局部热源，热膨胀改变接触与几何，磁场及感应电流又施加机械载荷。材料、冷却通路、连接方式、温度测点和维护可达性应对应同一版图纸。法拉第屏蔽的作用依其几何及电磁耦合而定，不能把安装屏蔽视为平行近场或鞘层驱动已被完全消除的证据。

## 设计计算与仿真

设计应连接核心吸收与边缘耦合两个问题。天线电流带的幅值、相位、间距及几何产生一段 $k_\parallel$ 谱，不是一个可脱离天线指定的单一波数。边缘密度剖面决定指定频率与谱分量的快波截止和衰逝区。增加天线至可传播区域的距离，通常削弱耦合；仅给核心密度或天线到最后闭合磁面的距离不足以确定加载。JET 的局地充气实验提供了改变天线前沿 SOL 密度、改善耦合的案例；能否复用于另一装置，还受燃料、辐射和边界工况约束。[EUROfusion，Experiments on Gas Puffing to Enhance ICRF Antenna Coupling](https://scipub.euro-fusion.org/archives/jet-archive/experiments-on-gas-puffing-to-enhance-icrf-antenna-coupling)。

对实正参考阻抗 $Z_0$ 的单端口，以同一平面上的入射和反射行波定义

$$
\Gamma=\frac{Z_L-Z_0}{Z_L+Z_0},\qquad
P_{\mathrm{acc}}=P_{\mathrm{fwd}}-P_{\mathrm{rev}}
=P_{\mathrm{fwd}}(1-|\Gamma|^2).
$$

该式给的是网络接受功率；馈线、金属、边缘鞘层等仍可能消耗其中一部分。若只有一个端口入射且其他端口匹配，$\Gamma=S_{11}$；多端口同时驱动时，应采用功率归一化的 $\mathbf b=\mathbf S\mathbf a$，在约定 $|a_p|^2$、$|b_p|^2$ 为 W 后，总净输入为 $\sum_p(|a_p|^2-|b_p|^2)$。单独检查每个孤立端口的 $S_{11}$，不能代替给定相位组合下的有源反射与互耦分析。[MIT，第 14.6 节](https://web.mit.edu/6.013_book/www/chapter14/14.6.html)；[Monakhov 等，JET 外部 conjugate-T 系统，§2–4](https://arxiv.org/pdf/1309.4644)。

以选定端口包围的稳态射频系统为边界，应让净输入等于馈线与金属损耗、各物种体吸收、另外单列的边缘损耗以及离开计算域的功率之和。各项须互斥，尤其不能把含边缘吸收的体积分再加一次鞘层功率；若边界改变，预算也要重写。瞬态另需计入储能变化。极低反射不等于极高核心吸收，极高体吸收也不证明最终热约束良好。

计算档案应同时保存磁平衡、组分、温度与密度剖面、SOL 与壁面、端口基模、相位、电流归一化及代码版本。至少独立增加空间分辨率、平行谱范围与采样密度；遇到高次谐波或非热尾部，再检查谐波和速度域范围。残差小表示离散方程求解充分，只有这些范围及分辨率检查才能判断沉积积分是否稳定。

## RF 鞘层、近场与杂质释放

天线周围平行射频电场可驱动与材料表面连接的场线上的射频鞘层。鞘层具有非线性电流—电压关系，射频振荡可以整流成额外的直流势差，改变入射离子能量和表面热负荷，并促进杂质溅射。这条边缘通道与核心离子回旋共振吸收不同，因此只优化核心共振位置并不能保证面对等离子体部件兼容。[Bobkov 等，Progress in reducing ICRF-specific impurity release in ASDEX Upgrade and JET，作者公开稿](https://scipub.euro-fusion.org/wp-content/uploads/WPMST1CP16_14736_submitted.pdf)。

常用的一个驱动指示量是沿相关磁力线的 $\int E_\parallel\,dl$，单位 V。但它不能直接等同于实际整流直流鞘层电压：完整结果还依赖两端边界、鞘层阻抗、粒子响应、磁场入射角和局地等离子体条件。线性、冷、体介电模型加理想金属边界，通常未包含全部非线性鞘层物理；把所有衰减都放进人为碰撞率也不能自动替代鞘层模型。

工程上，电流带排列、相位与功率平衡、天线框架上的感应电流、限制器几何和磁连接共同影响近场。ASDEX Upgrade 三电流带天线的实验工作说明，通过设计和电气调谐降低相关近场及感应电流，可以减小 ICRF 特有的钨释放；该案例支持一种设计原则，不能把其最优功率比直接变成本系统通用设定值。[Bobkov 等，First results with 3-strap ICRF antennas in ASDEX Upgrade，2016 年实验论文摘要](https://portal.fis.tum.de/en/publications/first-results-with-3-strap-icrf-antennas-in-asdex-upgrade/)。

评估时应把近场计算与红外热像、局地光谱杂质源、适用的电位或电流测量及核心杂质演化并列。表面发射率、观察角和视线积分会影响测量解释；核心杂质增加还含后续输运，不能仅从核心信号倒推出某一块天线表面的瞬时溅射率。降低反射、降低局部鞘层驱动和降低核心杂质是三个需要分别验证的目标。

## 控制与保护

控制目标不只是维持设定射频功率，还包括电流带相位与功率平衡、源端匹配以及对负载变化的响应。等离子体边缘密度随放电演化，ELM 等事件可使天线负载快速变化；机械调谐器、频率调节与功率回退具有不同带宽及功能，应结合传输链设计，而不能让一个慢速匹配回路承担全部异常处理。

负载容忍网络使发射机看到的反射对负载变化较不敏感，却也可能使某些电弧对源端反射信号不明显。JET 的 external conjugate-T 工作因此同时研究专门的电弧检测与实时匹配，说明“反射没有越限”不足以证明天线内部无放电。[Monakhov 等，Design and operations of load-tolerant external conjugate-T matching system，§5 的匹配及 AWACS 电弧检测](https://arxiv.org/pdf/1309.4644)。

每一保护通道应关联到明确的失效模式：方向耦合器监测行波，电压电流探头检查局部电应力，光学或其他电弧诊断检查异常放电，真空和冷却监测覆盖馈通与热负荷风险。某类传感器的必要性及冗余由实际设备确定；这些例子并不构成已经验证的保护配置。信号须包含单位、标定、采样率、有效量程和失效状态，动作须包含从检测到撤功率的延迟、执行链和复位条件。

阈值应来自部件额定值、热电分析及验收试验，并记录版本与适用工况。本页不提供可直接下装的通用功率、电压、温度或延迟数值。升功率前还应确认所有联锁在真实信号链中的动作，而不只是软件页面显示正常；测试要覆盖传感器失效、通信异常和复位后的再启动条件。保护触发记录应能同一时间轴对齐射频、真空、冷却和等离子体信号，以区分负载扰动、诊断伪信号及真正的部件异常。

## 测试与验收

低功率网络分析首先验证端口模型：在明确参考平面进行校准或去嵌入，检查传输链、匹配网络和天线多端口响应，再核对相位控制。真空或假负载测试能验证电路及部分功率链，但不能代替等离子体负载、鞘层和核心吸收试验。升功率后的温升、接触变化和非线性也可能使低功率结果失效，所以每一层验收应说明实际覆盖的物理条件。

功率测量需核查方向耦合器的方向性、校准与线缆衰减、峰值和 RMS 定义，以及大反射条件下入射/反射通道的串扰。两处参考平面的净功率差应与中间链路损耗相容；有条件的稳态量热测量可作交叉检验，瞬态则需考虑热容、冷却延迟和储能。仪器精度和系统误差必须随结果一同报告，而不是仅输出一个“耦合效率”。[Monakhov 等，JET 系统论文，§4 的电路与功率测量](https://arxiv.org/pdf/1309.4644)。

等离子体验证可比较电子温度响应、离子温度、储能、辐射、快离子谱及损失诊断。射频功率调制后温度变化的斜率包含沉积与输运效应，不能在任意时间窗都直接解释成局地吸收。JET 的 FFT/BIS 沉积分析明确限定密度响应和输运时间尺度。[Mayoral 等，§2.1 的调制、ECE 测量及分析假设](https://scipub.euro-fusion.org/wp-content/uploads/2014/11/EFDP05026.pdf)。快离子诊断也有其能量和俯仰角响应；合理做法是将模拟分布输入合成诊断，在实验可观测量上比较，并保留背景剖面、仪器响应和不确定度。[Tang 等，2005 APS DPP：C-Mod 中性粒子分析仪与 CQL3D 合成诊断比较](https://meetings-archive.aps.org/dpp/2005/kp1/30/)。

数值验收须把守恒、收敛和实验一致性分开：全波检查端口净输入与分组分吸收；FP 检查粒子数、碰撞成对能量及速度边界通量；耦合迭代检查波与粒子算子接收的射频功率一致。随后改变网格、谱截断、速度范围和轨道分辨率，确认目标观测量稳定。实验比较则另外检验剖面和信号，而非只核对总功率。所有结果应附输入、版本、原始测量、误差和通过判据；尚未执行的验收保持“待执行”，不得用程序正常退出代替。

## 文献与案例

本专题采用三类证据，并保留其边界。JET 的 external conjugate-T 论文是已运行装置的匹配、电弧检测和负载扰动案例；ASDEX Upgrade 的三电流带论文是已开展的杂质控制实验；它们能支持相应工程机制，不能直接成为本系统的额定参数。[JET 原论文](https://arxiv.org/abs/1309.4644)；[ASDEX Upgrade 原论文信息及摘要](https://portal.fis.tum.de/en/publications/first-results-with-3-strap-icrf-antennas-in-asdex-upgrade/)。

full-wave/Fokker–Planck 耦合论文与报告属于建模方法及所列放电的验证材料；ITER 的 SOL 充气优化论文属于对 ITER 条件的预测研究，文中计算出的改善不应写成 ITER 已测性能。阅读这些案例时，应记录背景组分、磁平衡、输入谱、分布假设、诊断覆盖和作者明确的局限。[2019 年 ITER SOL 密度调控预测研究](https://doi.org/10.1016/j.nme.2018.12.025)；[2023 年自洽耦合模型作者摘要](https://meetings-archive.aps.org/dpp/2023/ki02/4/)。

[ITER 当前辅助加热介绍](https://www.iter.org/machine/supporting-systems/external-heating-systems)在 2024 基线背景下列出的 ICRH 规划频率为 40–55 MHz，初期计划向等离子体提供 10 MW、后续阶段 20 MW；这些是计划参数，不是已经实现的加热记录（访问日期：2026-10-16）。历史入口 [IPP 等离子体加热课程](https://www.ipp.mpg.de/5436011/09_Plasma_Heating.pdf) 保留供后续阅读，但本轮获取受限，直接请求返回 401，未取得正文，未以它作为新增具体结论的依据。上述资料构成可追溯的学习与设计起点；本知识库没有据此宣称完成任何实际 ICRH 设备的安全认证、整机验收或装置工况优化。

[返回辅助加热](../README.md) · [编写说明](../../编写说明.md) · [返回知识库](../../README.md)
