# 等离子体波与波粒相互作用

等离子体波是粒子运动与自洽电磁场共同形成的集体扰动。识别一个波，至少需要同时说明背景组分、传播方向、频率范围、偏振及采用的模型。本页从均匀平衡附近的小振幅线性理论出发，依次连接冷流体、温流体、理想 MHD 和动力学响应；各公式旁列出适用条件，不能把不同近似的结果直接拼成一个普遍色散关系。内容为基础教学条目，未计算某台装置的可达性、吸收效率或运行参数。

## 平面波、符号约定与线性化

本页使用 SI 制，物理扰动取复表示的实部：

$$
\delta\mathbf E(\mathbf r,t)
=\operatorname{Re}\!\left[\widetilde{\mathbf E}
e^{i(\mathbf k\cdot\mathbf r-\omega t)}\right],
\qquad \partial_t\mapsto-i\omega,
\qquad \nabla\mapsto i\mathbf k.
$$

波数 $k=2\pi/\lambda$ 的单位为 $\mathrm{m^{-1}}$，角频率 $\omega=2\pi f$ 的单位为 $\mathrm{s^{-1}}$。如果取实 $\mathbf k$ 和 $\omega=\omega_r+i\gamma$，振幅随 $e^{\gamma t}$ 变化，因此 $\gamma<0$ 才是时间阻尼。若改为实 $\omega$、沿 $x$ 的复波数 $k=k_r+ik_i$，则 $k_i>0$ 表示向 $+x$ 的空间衰减。这两个问题的边界条件不同，不能直接把 $\operatorname{Im}k$ 当成增长率。来源：[Fitzpatrick，§5.2，式 (5.1)–(5.5)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node67.html)。

有磁场时取 $\mathbf B_0=B_0\widehat{\mathbf z}$、$B_0>0$，规定带符号回旋角频率与各组分等离子体角频率为

$$
\Omega_s=\frac{q_sB_0}{m_s},\qquad
\omega_{ps}^2=\frac{n_{s0}q_s^2}{\epsilon_0m_s}.
$$

电子的 $q_e=-e$、$\Omega_e<0$，正离子的 $\Omega_i>0$。除特别说明外，温度 $T_s$ 用 K 表示，热能写成 $k_BT_s$；若输入以 eV 表示的数值 $T_{s,\mathrm{eV}}$，须先用 $k_BT_s=T_{s,\mathrm{eV}}\times1.602176634\times10^{-19}\,\mathrm J$ 换算。本文的热速率定义为 $v_{ts}=\sqrt{k_BT_s/m_s}$，与另一些文献的 $\sqrt{2k_BT_s/m_s}$ 相差 $\sqrt2$，代入 Maxwell 分布或 Landau 参数前必须换算。来源：[Fitzpatrick，§5.3，式 (5.16)–(5.19)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)。

线性化指把 $n_s=n_{s0}+n_{s1}$、$\mathbf v_s=\mathbf v_{s1}$ 等代入原方程，只保留一阶小量。例如 $n_{s1}\mathbf E_1$、$\mathbf v_{s1}\times\mathbf B_1$ 是二阶项，但 $\mathbf v_{s1}\times\mathbf B_0$ 是一阶项，必须保留。均匀无流背景使 Fourier 分量彼此独立；有梯度的装置中，局域结果还要求背景变化尺度显著长于局域波长。冷近似忽略的是相应响应中的压力与速度展宽效应，并非声称实际温度等于零；接近共振时，即使温度不高，热效应也可能成为主导修正。来源：[Fitzpatrick，§5.1 Introduction](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node66.html)。

阅读不同计算结果时，可以先做一个最小对照：检查电荷符号、磁场方向、时间指数以及温度定义是否相同，再比较色散曲线。一个程序返回负的电子回旋频率，另一个返回正的电子回旋频率幅值，两者未必矛盾；真正需要对照的是它们在运动方程与共振分母中怎样使用。类似地，复振幅乘上统一的常数相位不会改变物理偏振，但仅把一个分量共轭会改变旋转方向。波动问题中的许多“物理差异”首先是 convention 差异，只有完成这一层换算才能判断。

## 从感应电流到介电张量和色散矩阵

在线性、均匀背景中，用导电率张量表示感应电流：

$$
\widetilde{\mathbf J}
=\boldsymbol\sigma(\omega,\mathbf k)\widetilde{\mathbf E},
\qquad
\boldsymbol\epsilon_r
=\mathbf I+\frac{i\boldsymbol\sigma}{\epsilon_0\omega}.
$$

$\boldsymbol\epsilon_r$ 是无量纲相对介电张量；绝对介电张量是 $\epsilon_0\boldsymbol\epsilon_r$，两者不能混写。这里把等离子体电流全部吸收到材料响应中，外部天线电流则应作为驱动项另列。各向异性意味着电流方向未必与电场方向一致，动力学响应还通常依赖 $\mathbf k$，因此一般不能用一个仅随频率变化的标量“介电常数”代替。来源：[MIT 22.611J，第 5 章 §5.1，式 (5.6)–(5.20)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

由 Faraday 方程 $\mathbf k\times\widetilde{\mathbf E}=\omega\widetilde{\mathbf B}$ 消去磁场，得到

$$
\mathbf k\times(\mathbf k\times\widetilde{\mathbf E})
+\frac{\omega^2}{c^2}\boldsymbol\epsilon_r
\widetilde{\mathbf E}=0.
$$

定义折射率向量 $\mathbf N=c\mathbf k/\omega$，则

$$
\mathbf M\widetilde{\mathbf E}=0,
\qquad
\mathbf M=\boldsymbol\epsilon_r
+\mathbf N\mathbf N-N^2\mathbf I,
\qquad \det\mathbf M=0.
$$

这是由 Maxwell 方程直接得到的代数条件。行列式只判断非零解能否存在；要知道该根是纵向波、横向波还是混合偏振，必须继续求零空间中的 $\widetilde{\mathbf E}$。例如标量响应下，$\mathbf E\parallel\mathbf k$ 给出 $\epsilon_r=0$，$\mathbf E\perp\mathbf k$ 给出 $N^2=\epsilon_r$，两种根的物理性质完全不同。磁化时二者通常耦合，不能预先删去任意电场分量。来源：[Fitzpatrick，§5.4，式 (5.40)–(5.55)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node69.html)。

还应区分“求自由模”和“求受迫场”：自由模满足齐次方程；给定天线、导体壁和密度剖面时，求的是含源项的边值问题。局域 $\det\mathbf M=0$ 并没有确定天线激发幅度、边界反射或全局功率。一个数值根也要回代矩阵、核查偏振与连续分支，特别不能把乘去分母时产生的额外根当成真实模式。

静电近似也可从此框架理解：先设 $\mathbf E_1\simeq-i\mathbf k\phi_1$，再由无外部电荷的 $\mathbf k\cdot\mathbf D_1=0$ 得到 $\mathbf k\cdot\boldsymbol\epsilon_r\cdot\mathbf k=0$。它通常是完整电磁问题在适当大折射率、近纵向偏振下的近似，不能无条件替代三维矩阵。实际使用时应确认被忽略的横向场和磁扰动小，并检查所选根是否连续接近完整色散的某个分支。尤其接近偏振耦合区，先强行设某分量为零，可能使原本存在的模转换从模型中消失。

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

这就是 Bohm–Gross 色散。系数 $3$ 对应沿传播方向的压力响应，不能因为背景粒子生活在三维空间就替换成 $5/3$。更可靠的解释是：对 Maxwellian 电子的纵向动力学介电函数作高相速度展开，在 $k\lambda_{De}\ll1$、$\omega_r/k\gg v_{te}$ 时得到同样的首个热修正。流体闭合复现了此极限中的实频率，却没有包含共振速度附近的粒子信息。来源：[Fitzpatrick，§7.2，式 (7.23)–(7.29)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node90.html)。

从该近似微分得到 $v_g\simeq3kv_{te}^2/\omega_r$，说明热压力使局部电子振荡能够传播。随着 $k\lambda_{De}$ 增大，不能只把这条抛物色散无限延长：相速度逐渐接近热速率，Landau 阻尼和高阶修正的重要性增加，应解完整动力学色散。高频分支上忽略离子的依据是其响应远小于电子响应，不是把离子质量设为无穷大的普遍定律；研究低频波时必须重新恢复离子运动。

一个不依赖装置参数的检查是取 $k\lambda_{De}=0.1$。由于 $\omega_{pe}\lambda_{De}=v_{te}$，近似式给出 $\omega_r/\omega_{pe}=\sqrt{1.03}\simeq1.0149$、$v_{\mathrm{ph}}/v_{te}\simeq10.149$，热修正较小而相速度显著大于热速率，与所用排序一致。若直接把同一式代到 $k\lambda_{De}=1$，实频率数值仍然能算出，但原来的展开小量已不小；“计算器给出结果”并不等于理论仍有效。这种把计算结果回代假设的检查，应与代数推导同等重视。

电子振荡还说明为什么宏观准中性模型和 Poisson 模型不能随意互换。对于远低于电子等离子体频率、尺度很大的过程，电子能快速调整，电荷分离通常很小，准中性近似十分有用；但本条研究的恰好是电荷分离本身的振荡。如果在推导开始时强行令每一点电子密度始终等于固定离子密度，就会把所研究的自由度提前删除。选择模型并非保留方程越多越好，而是应保留所关注频率与尺度上的恢复力、惯性和约束，并明确被删除的模式。

## 离子声波与电子 Boltzmann 响应

离子声波（ion-acoustic wave）主要由电子压力提供恢复力，由离子提供惯性。先取单价离子、$n_{e0}=n_{i0}=n_0$，无磁场或沿直磁场传播，电子近似等温且平行惯性可忽略。电子力平衡为

$$
0=en_e\partial_x\phi-k_BT_e\partial_xn_e,
\qquad
n_e=n_0\exp\!\left(\frac{e\phi}{k_BT_e}\right),
\qquad
\frac{n_{e1}}{n_0}=\frac{e\phi_1}{k_BT_e}.
$$

正电势吸引电子，因此指数为正号。该 Boltzmann 响应来自有条件的快速电子响应，不能用于任意跨磁场扰动，也不是“任何 Maxwellian 在任何瞬间都服从这个公式”。线性式还要求 $|e\phi_1|\ll k_BT_e$。来源：[MIT 22.611J，第 5 章 §5.4.2 Including the Ion Response、§5.9.8](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

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

在无漂移 Maxwellian、弱碰撞的经典情形，弱阻尼要求相速度处在 $v_{ti}\ll\omega_r/k\ll v_{te}$ 的窗口内。长波声速代入后，左侧条件要求 $T_e\gg T_i$；当 $T_e$ 与 $T_i$ 接近时，离子共振粒子数量增加，离子 Landau 阻尼通常显著。不能从流体方程有一个实根，就断言实验中一定存在清晰长寿命的离子声波。多离子组分、非 Maxwellian、强碰撞、漂移等情形需要重新分析。来源：[Fitzpatrick，§7.5，式 (7.49)–(7.52) 及温度条件讨论](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node93.html)。

准中性与完全没有电场也不同。长波极限中 $n_{i1}$ 与 $n_{e1}$ 的主阶相等，微小差值仍通过 Poisson 方程产生足以维持共同运动的电场；若一开始严格令差值为零并同时强加有限波数 Poisson 方程，反而会错误地消去声波的恢复机制。对有限 $T_i$，冷离子公式形式上在大波数趋近 $\omega_{pi}$，但相速度随之下降，最终可能违反 $v_{\mathrm{ph}}\gg v_{ti}$。这说明一个极限可以是流体公式的数学极限，却未必是原始物理排序允许达到的实验极限。

## 非磁化横电磁波与密度截止

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

最后一步用于电子高频响应占主导的普通电子—离子等离子体；第一式才保留全部冷组分。这个波同时包含电场、磁场和粒子振荡能。它与同一等离子体的纵向 Langmuir 模不能合并为一个分支：横向根来自 Ampère 方程中的电流及位移电流，纵向根来自电荷分离。来源：[Fitzpatrick，§5.7，横向与纵向分支](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node72.html)。

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

是衰逝解。$1/\kappa$ 是这一理想模型的幅度穿透长度，不应直接替代碰撞金属中的趋肤深度。单纯的衰逝不等于局部热耗散：在无耗散半无限介质界面，入射功率可主要被反射；有限厚度层还可能发生隧穿，须由两端边界匹配决定。来源：[Fitzpatrick，§6.3 Cutoffs](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node80.html)。

实际磁约束等离子体通常有强磁场，所谓“超过临界密度就不能传播”只对指定的非磁化横向分支或相应 O 模近似有效，不能排除 X 模、低频磁化分支或模转换路径。这个结论尤其不能直接用于判断 ICRF 天线能否耦合。计算密度截止前先确认使用的是 $f$ 还是 $\omega$，否则临界密度会误差一个 $4\pi^2$ 因子。

由临界密度公式还可直接看出 $n_{\mathrm{crit}}\propto f^2$：频率增加一倍，指定模型中的临界密度增加四倍。这是一条条件明确的缩放关系，而不是对加热效率的预测。即便入射波满足传播条件，界面阻抗不匹配仍能产生反射；即便透射进入等离子体，若介电响应没有耗散部分，也不会仅因存在粒子电流就转化为热。比较实验或仿真时，应分别提取入射、反射、透射和沉积功率，而不是把电场进入区域的深度直接称为吸收长度。

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

这就是常用 whistler 近似，强色散来自电子受磁场约束的电流响应。它不是对全部螺旋波放电几何都成立的完整色散：有限半径、斜传播、边界条件及碰撞会改变模式。此近似还需远离回旋共振，不能用于计算共振层吸收。来源：[Fitzpatrick，§5.9，式 (5.90)–(5.94) 及 whistler 频段](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node74.html)。

冷张量有两个容易实施的极限检查。若令所有 $\omega_{ps}$ 趋于零，$R,L,S,P$ 都趋于一而 $D\to0$，恢复真空 Maxwell 方程；若令 $B_0\to0$，则 $R=L=P$、$D=0$，恢复无磁场标量响应。后一极限要针对完整公式做，不能对已经要求 $\omega\ll|\Omega_e|$ 的 whistler 近似再令磁场为零，因为这样主动破坏了近似的前提。类似地，多离子组分各自贡献一个带其电荷和质量的响应项，不能用一个平均离子质量替换所有可能的回旋共振。

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

只要相应分母非零，$R=0$ 或 $L=0$ 给出 X 模截止；$S=0$ 且 $RL\ne0$ 给出该冷分支的共振。X 模一般同时含 $E_x$ 和 $E_y$，所以不能仅凭“电磁波”三个字就删除纵向电场。由第一行 $SE_x-iDE_y=0$ 可知，在 $S\to0$ 而 $D$ 有限时，归一化偏振趋向以 $E_x$ 为主；这提示热效应和短波动力学的重要性，而不是证明某个场能量会无限增大。来源：[Fitzpatrick，§5.4，式 (5.43)、(5.54)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node69.html)。

若在电子频率范围忽略离子响应，

$$
S\simeq1-\frac{\omega_{pe}^2}{\omega^2-\Omega_e^2},
\qquad
\omega_{\mathrm{UH}}^2\simeq\omega_{pe}^2+\Omega_e^2.
$$

上混杂频率（upper hybrid）结合了电子电荷分离恢复力和磁化运动，不等于单粒子回旋频率。该简单式限于这里的冷、高频、垂直传播近似；多组分完整 $S=0$ 还含离子项与其他根。接近 $N\to\infty$ 时，冷模型暗示波长越来越短，有限 Larmor 半径和非局域响应不能再被忽略。上混杂层、电子 Bernstein 波和 O–X–B 转换之间存在联系，但转换效率须解带梯度的热等离子体问题，不能仅由上述频率公式推出。来源：[Fitzpatrick，§5.10，式 (5.99)–(5.103)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node75.html)。

判断是否真的存在极点还要检查分子。$N^2=RL/S$ 是约去若干因子后得到的分式，如果分子和分母同时为零，就必须回到原矩阵判断极限。例如无磁场时 $R=L=S$，此式连续化简为 $N^2=S$，不会因为单独写着一个 $S$ 在分母就凭空产生上混杂共振。另一个常见混淆是把 O、X 模当作任意角度都严格线偏振的两类波；这里的简明定义依赖完全垂直传播。斜入射时需跟踪本征矢，模名称往往仅表示与相应垂直分支的连续联系。

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

第一因子给出剪切 Alfvén 波。其速度扰动垂直于 $\mathbf k$ 与 $\mathbf B_0$ 张成的平面，在该均匀模型中 $\mathbf k\cdot\mathbf v_1=0$，所以 $\rho_1=p_1=0$。恢复力是弯曲磁力线的磁张力；单位长度上的惯性由等离子体质量提供。波频率 $\omega=\pm k_\parallel v_A$ 显示完全垂直传播时这一分支退化为零频，不能仍写成 $\omega=kv_A$。来源：[Fitzpatrick，§5.8 Low-Frequency Wave Propagation](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node73.html)。

第二因子给出快、慢磁声波。设 $\cos\theta=k_\parallel/k$，则

$$
v_{f,s}^2=\frac12\left[v_A^2+c_M^2
\pm\sqrt{(v_A^2+c_M^2)^2-4v_A^2c_M^2\cos^2\theta}\right],
\qquad \omega^2=k^2v_{f,s}^2.
$$

正号为快分支，负号为慢分支。一般斜传播时它们包含密度、压力和磁压扰动。完全垂直传播给出 $v_f^2=v_A^2+c_M^2$、$v_s=0$；完全平行传播的两个速度是 $v_A$ 与 $c_M$，谁被称为“快”取决于两者大小。这个极限检查能防止把声波分支和磁分支永久贴上错误标签。来源：[Fitzpatrick，§8.4，式 (8.22)–(8.45)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node107.html)。

本条采用非相对论理想 MHD，要求 $v_A,c_M\ll c$，使忽略位移电流及相对论惯性与所用波速公式相容。它适合低频、长尺度描述，通常要求 $\omega\ll|\Omega_i|$、$k\rho_i\ll1$，并且 Hall、电子惯性、电阻与相关动力学修正可忽略；例如 $kd_i\ll1$、$d_i=c/\omega_{pi}$ 是常用的 Hall 小量条件之一。标量绝热压力闭合还需单独论证，尤其碰撞很弱时，低频本身不能消除压力各向异性、平行热流或 Landau 阻尼。ICRF 频段所谓 fast / slow 分支须从其冷/热介电色散识别，不能把以上远低于离子回旋频率的公式直接外推到共振层。来源：[MIT 22.611J，第 5 章 §5.6 Simple Example of MHD Dynamics](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/75c75c5df51f8fba1b2a903fde937ddc_chap5.pdf)。

由总压定义 $\beta=2\mu_0p_0/B_0^2$，可自行算得 $c_M^2/v_A^2=\Gamma\beta/2$。因此在这个标量闭合下，低 beta 通常使磁张力控制的速度大于声速；但关系中明确保留了绝热指数，不能把二者平方比简单等同于 beta。以上三类模是在无限均匀平衡中识别的局域分支。环形装置的磁剪切、曲率和密度剖面会形成连续谱、耦合或离散本征模，不能从某处的一个 $v_A$ 数值直接确定全装置本征频率与稳定性；需要把局域物理放回实际平衡和边界中。

## 相速度、群速度、截止与共振的区别

相速度描述固定相位的移动；在一个光滑、弱阻尼色散分支上，群速度描述窄带波包包络的一阶传播：

$$
\mathbf v_{\mathrm{ph}}=\frac{\omega_r}{k}\widehat{\mathbf k},
\qquad
\mathbf v_g=\nabla_{\mathbf k}\omega_r.
$$

第一式只是沿波法线选取的相位速度。在各向异性介质中，$\mathbf v_g$ 未必平行 $\mathbf k$；因此波前朝向与能量传播方向不能机械地画成同一根箭头。在强阻尼、宽频、强非均匀或分支混合区，群速度也不能无条件等同于信号前沿速度。来源：[Fitzpatrick，§6.7 Pulse Propagation](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node84.html)。

例如无磁场冷横波有

$$
v_{\mathrm{ph}}=\frac{\omega}{k}>c,
\qquad
v_g=\frac{c^2k}{\omega}<c,
\qquad v_{\mathrm{ph}}v_g=c^2.
$$

这个乘积关系仅属于此条色散，不是全部等离子体波的恒等式。相速度超过 $c$ 没有意味着能量或信息超光速，因为单一等相位面不携带独立新信息。对 Bohm–Gross 波和 whistler 波按各自色散求导，会得到不同关系；“折射率大”也不能单独说明信号传播快慢。

群速度的来由可以直接从两个邻近 Fourier 分量看出。若波数差为 $\Delta k$、频率差为 $\Delta\omega$，叠加后的慢包络含相位 $\Delta k\,x-\Delta\omega\,t$；当带宽趋小时，其移动速度就是 $d\omega/dk$。如果二阶及更高阶色散在传播时间内积累明显，不同部分的包络速度会分离，波包展宽，这时还要保留色散曲率。如果频谱同时覆盖两条本征分支，则必须分别传播它们的本征偏振，不能把总频谱随意拟合成一条群速度曲线。

在固定频率、固定传播方向的简单局域冷模型里，截止通常指一条分支 $N^2\to0$，共振通常指 $N^2\to\infty$。二者一端是长波极限，另一端是短波极限，不是同一现象。在分层介质中，沿界面波数守恒，实际法向转折点可以是 $k_x^2\to0$ 而总 $k$ 非零，不能把正常入射的 $N=0$ 判据不加修改地用于任意斜入射。来源：[Fitzpatrick，§5.6 Cutoff and Resonance](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node71.html)。

用局域色散拼接射线或 WKB 解，还要求波数随位置变化足够缓慢，例如一维条件 $|\partial_x k|/|k|^2\ll1$。截止及共振附近常会破坏这种近似，需使用局域连接解或全波边值解。反射是能量返回原侧，模转换是能量转入另一传播分支，吸收则要求场对粒子作净功；这三者可以并存但不能互相替代。冷奇点可以指示必须加入的新物理，却不自动给出有限吸收率。来源：[Fitzpatrick，§6.2 WKB Solutions](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node79.html)；[§6.4 Resonances，式 (6.29) 中正则化与边界条件](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node81.html)。

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

积分路径 $\mathcal L$ 按因果初值问题规定：从 $\operatorname{Im}\omega>0$ 的良定义积分作解析延拓，不能任意选择绕过极点的方向。弱阻尼展开 $\omega=\omega_r+i\gamma$ 后，

$$
\gamma\simeq-
\frac{\epsilon_{L,I}(\omega_r,k)}
{\partial_\omega\epsilon_{L,R}(\omega_r,k)},
\qquad
\epsilon_{L,I}=-\sum_s\frac{\pi q_s^2}{\epsilon_0m_sk^2}
\left.\partial_vF_{s0}\right|_{v=\omega_r/k}.
$$

对于通常的正频电子 Langmuir 分支，$\partial_\omega\epsilon_{L,R}>0$，无漂移 Maxwellian 在正共振速度处斜率为负，因此 $\gamma<0$。若存在束流或速度空间凸起，斜率可改变并提供自由能；此时要重新求整个色散，不能对所有模只看一个斜率便下结论。来源：[Fitzpatrick，§7.2，式 (7.23)–(7.31)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node90.html)。

Maxwellian 计算常使用 $\zeta_s=\omega/(\sqrt2kv_{ts})$ 和等离子体色散函数 $Z(\zeta)$；这里的 $\sqrt2$ 来自本页热速率 convention。即使场振幅衰减，理想 Vlasov 演化的总能量仍守恒：扰动转入越来越精细的速度空间结构，即相混合（phase mixing）。把这一过程称为宏观阻尼，并不等于已经证明发生不可逆 Maxwellian 热化；碰撞、粗粒化及后续分布演化需另行描述。大振幅粒子俘获或强阻尼下，以上线性小 $\gamma$ 公式也不再充分。来源：[Fitzpatrick，§7.4 Plasma Dispersion Function](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node92.html)；[§7.2，初值解与连续谱讨论](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node90.html)。

在诊断或数值计算中看到电场幅值下降，也不能只凭这一现象认定是 Landau 阻尼。波包离开观测窗口、几何扩散、碰撞耗散、边界吸收以及数值滤波都可能使局部幅值减小。要识别机制，应同时检查共振速度附近的分布变化、场能与粒子能交换、边界能量通量以及离散分辨率。相混合会不断生成更细的速度空间尺度，因此空间网格收敛并不替代速度网格收敛；有限速度网格造成的人工复现或数值耗散也不应被解释成新的物理增长或加热。

## 回旋共振、谐波与射频能量通道

磁化粒子的未扰动轨道包含平行运动和周期回旋；把沿轨道的波场展开成回旋谐波后，出现共振分母

$$
\omega-k_\parallel v_\parallel-\ell\Omega_s,
\qquad
\omega_r-k_\parallel v_\parallel=\ell\Omega_s,
\qquad \ell\in\mathbb Z.
$$

这里沿用带符号 $\Omega_s=q_sB_0/m_s$，$\ell$ 是谐波整数，不是折射率或密度。对正离子、正频率且 Doppler 修正较小时，$\ell=1$ 是基频、$\ell=2$ 是二次谐波；电子的同向回旋共振在该 signed convention 下对应相应负谐波。文献若把电子回旋频率定义为正的幅值，整数或极化符号也会相应改变。来源：[Fitzpatrick，§7.6 Waves in Magnetized Plasmas，式 (7.80)–(7.87)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node94.html)。

共振式中的 $k_\parallel v_\parallel$ 是粒子运动引起的 Doppler 位移。有限平行速度分布把理想冷共振拓宽为一段速度空间响应，而 $k_\perp\rho_s$ 通过回旋轨道上的相位变化控制谐波耦合。只有“频率等于回旋频率”仍不够：波必须有正确的偏振分量、能到达相应区域，并与足够多的粒子有效相互作用。非零 $k_\parallel$ 时，不同 $v_\parallel$ 的粒子也可以在不同位置满足同一射频的共振条件。来源：[Fitzpatrick，§7.7，式 (7.98)–(7.101)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node95.html)。

粒子能量方程尤其简单：

$$
\frac{d}{dt}\!\left(\frac12m_sv^2\right)
=q_s\mathbf E\cdot\mathbf v,
\qquad
\mathbf v\cdot(\mathbf v\times\mathbf B)=0.
$$

直接作功的是电场，静磁场通过改变轨道与相位匹配来组织能量交换。对于 ICRH，波能可先进入少数离子或特定谐波共振粒子的非热运动，再经库仑碰撞转移给电子和其他离子，同时也可能发生轨道损失；存在模转换时，还可能通过别的分支或电子吸收通道沉积。因此“射频发生器输出”“天线耦合功率”“某离子吸收”“整体热能增加”是不同环节，不能统一用一个加热功率数值代替。

最简冷圆偏振模型里的分母趋零，表示稳态线性响应发生奇异；它没有给出有限共振宽度、粒子分布演化和最终热化比例。若研究加热或电流驱动，需要含动力学吸收的全波或射线模型，再将分组分沉积与 Fokker–Planck、输运和能量守恒联系起来。相关工程入口为[离子回旋加热](../../辅助加热/离子回旋加热/README.md)，本条的共振公式不代替该系统的场谱和工况计算。来源：[Fitzpatrick，§7.7 最后两段：冷共振与无碰撞回旋阻尼的有限宽度](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node95.html)。

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

单位为 $\mathrm{W\,m^{-3}}$，$\dagger$ 表示共轭转置。重要的是导电率的 **Hermitian 部分** 对平均净作功有贡献，反 Hermitian 部分的二次型纯虚，对周期平均功率没有贡献。不能把“导电率虚部”和“介电张量虚部”混为同一耗散判据。该结论是对 $\langle\mathbf J\cdot\mathbf E\rangle$ 的直接代数分解，所用材料关系见 [Fitzpatrick，§5.2，式 (5.6)–(5.8)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node67.html)。

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

严格的反 Hermitian 部分是 $(\boldsymbol\epsilon_r-\boldsymbol\epsilon_r^\dagger)/2=i\boldsymbol\epsilon_{\mathrm{loss}}$；文献常说“介电张量的反 Hermitian 部分决定吸收”，其含义是以上关系，而非对张量每个元素单独取虚部。比如冷无碰撞张量的 $\pm iD$ 元素虽是纯虚，整体张量在实频率且远离奇点时仍为 Hermitian，因此并不产生有限周期平均耗散。来源：[Fitzpatrick，§5.3，式 (5.37)–(5.39)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node68.html)。

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

对非局域响应，应先用实际 $\mathbf J(\mathbf r)$ 与 $\mathbf E(\mathbf r)$ 计算局部作功；不能未经说明就在非均匀等离子体中套用纯局域介电矩阵。稳态能量检查应比较穿过边界的 Poynting 通量、体积分 $\int Q\,dV$、天线输入和壁耗散。若需区分电子与各离子吸收，要分解各组分电流 $\mathbf J_s$ 并分别计算 $Q_s$；只有总吸收守恒，并不能证明各组分沉积正确，更不能证明最终温度响应正确。

还要区分能量增长率与振幅增长率：若固定模结构的振幅随 $e^{\gamma t}$ 变化，相应二次型能量就随 $e^{2\gamma t}$ 变化。比较动力学根求得的 $\gamma$ 与时域能量拟合斜率时，必须处理这一因子二。波能还包含粒子有序振荡的贡献，不能只用真空电场能估计全部波能后再换算阻尼率；在色散强的等离子体中，这种遗漏可能直接影响数量级。

[返回基础原理](../README.md)
