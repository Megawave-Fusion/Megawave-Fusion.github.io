# 聚变反应与燃烧

本专题把核反应、速度分布、热平衡和电站功率口径连接起来。默认讨论非相对论、热核 D-T 等离子体；$\Theta_s=k_BT_s$ 表示温度能量，代入 SI 公式时单位是 J。示例均为明确给定输入的教学计算。点火、等离子体增益和净电输出按各自的系统边界定义。

## 核反应道、质量亏损与产物能量

核反应释放的能量来自初末态静质量之差，$Q_{\rm nuc}=(\sum m_{\rm in}-\sum m_{\rm out})c^2$，这里的 $Q_{\rm nuc}$ 单位是能量；聚变增益另外用无量纲功率比定义。常用反应道为

$$
\begin{aligned}
\mathrm D+\mathrm T&\rightarrow{}^4\mathrm{He}+n+17.6\,\mathrm{MeV},\\
\mathrm D+\mathrm D&\rightarrow{}^3\mathrm{He}+n+3.27\,\mathrm{MeV},\\
\mathrm D+\mathrm D&\rightarrow\mathrm T+p+4.03\,\mathrm{MeV},\\
\mathrm D+{}^3\mathrm{He}&\rightarrow{}^4\mathrm{He}+p+18.35\,\mathrm{MeV}.
\end{aligned}
$$

总能量守恒给 $\sum K_{\rm out}-\sum K_{\rm in}=\Delta m\,c^2$。低入射能量时即表列释放能；使用同一核质量约定，若用原子质量则核对电子数与束缚能修正。

这些是低入射能量下的近似释放能，每个 D-D 分支按自身产额与释放能分别计数。D-T 产物在质心系具有大小相等、方向相反的动量；非相对论近似 $E=p^2/(2m)$ 给出 $E_n/E_\alpha=m_\alpha/m_n\simeq4$，所以约 14.1 MeV 由中子携带、3.5 MeV 由带电 alpha 粒子携带。真实实验室能谱还受反应物热运动、束流和观测方向影响。[Fitzpatrick：Nuclear Fusion Reactions，式 (1.1)–(1.5)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node6.html)；[NRL Plasma Formulary 2016，印刷页 44–45 的反应表](https://suli.pppl.gov/2016/course/NRL_FORMULARY_16.pdf)。

带电产物可以通过磁约束和碰撞向等离子体传能；中子主要在等离子体外的材料中输运、沉积能量并引起核反应。核心自加热按受约束带电产物的实际沉积功率计入。D-$^3$He 的主反应不直接产生中子，但含氘等离子体仍可能发生 D-D 反应及后续反应，总中子产额由各反应道共同决定。选择燃料还必须考虑反应率、辐射、燃料可得性和产物处理。

### 由单次反应推算燃料消耗

先在质心系用 $\mathbf p_n=-\mathbf p_\alpha$ 消去动量：$E_n+E_\alpha=Q_{\rm nuc}$、$E_n/E_\alpha=m_\alpha/m_n$，解得 $E_\alpha=Q_{\rm nuc}m_n/(m_n+m_\alpha)$。再把聚变功率除以单次能量，可由宏观功率返回反应计数：

$$
\dot N_{DT}=\frac{P_{\rm fus}}{E_{DT}},\qquad
\dot m_T=m_T\dot N_{DT},\qquad
\dot m_D=m_D\dot N_{DT}.
$$

用 $P_{\rm fus}=100\,\mathrm{MW}$、$E_{DT}=17.6\,\mathrm{MeV}$，得到 $\dot N_{DT}=3.546\times10^{19}\,\mathrm{s^{-1}}$。以 $m_T\simeq5.008\times10^{-27}\,\mathrm{kg}$、$m_D\simeq3.344\times10^{-27}\,\mathrm{kg}$ 计算，氚、氘的燃烧消耗分别为 0.178 和 0.119 mg/s；连续反应一天各消耗约 15.34 和 10.25 g。燃料系统的循环流量再由燃烧份额确定：若每次通过等离子体燃烧 1%，其余全部回收，氚的入口流量为燃烧消耗的 100 倍。

原始能量分配见 [Fitzpatrick，式 (1.3)–(1.5)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node6.html)；本例使用三位有效数字的核质量和释放能。

## 反应截面、反应率与速度分布平均

截面 $\sigma(E)$ 单位是 $\mathrm{m^2}$，描述给定相对碰撞能量下的核反应概率尺度；反应率系数 $\langle\sigma v\rangle$ 单位是 $\mathrm{m^3\,s^{-1}}$，已经对相对速度作平均。若 $F_a,F_b$ 为积分等于一、相互独立的速度概率密度，

$$
\langle\sigma v\rangle_{ab}=\iint F_a(\mathbf v_a)F_b(\mathbf v_b)
\sigma(v_r)v_r\,d^3v_a\,d^3v_b,
\qquad v_r=\lvert\mathbf v_a-\mathbf v_b\rvert.
$$

固定入射粒子，短时相对扫掠体积为 $\sigma(v_r)v_rdt$；乘两群速度分辨密度并积分即得 $n_an_b\langle\sigma v\rangle$。相同粒子交换编号仍是同一对，故除以二。

单位体积单位时间的反应数为 $R_{ab}=n_an_b\langle\sigma v\rangle_{ab}/(1+\delta_{ab})$，单位 $\mathrm{m^{-3}\,s^{-1}}$。相同粒子反应的二分之一避免把同一对粒子数两次；不同 D-D 分支还需各自的分支截面。对相同温度能量 $\Theta$、无相对整体漂移的 Maxwellian 组分，约化质量 $\mu=m_am_b/(m_a+m_b)$ 给出

$$
\langle\sigma v\rangle=\sqrt{\frac{8}{\pi\mu}}\,\Theta^{-3/2}
\int_0^\infty\sigma(E)E e^{-E/\Theta}\,dE.
$$

该式可从相对速度的三维高斯分布换元 $E=\mu v_r^2/2$ 得到。积分权重覆盖整个相对能量分布，并保留截面的强能量依赖。不同温度、束靶反应和非热尾部须重新平均。[Wurzel 与 Hsu：Lawson 综述，§III 的反应率与热核假设](https://arxiv.org/html/2105.10954v3)。

一个可独立检验积分程序的人工基准是令截面恒为 $\sigma_0$；积分得到 $\langle\sigma v\rangle=\sigma_0\sqrt{8\Theta/(\pi\mu)}$。这个恒截面模型用于检查归一化和积分器。D-T 计算采用注明版本和有效范围的截面数据；实验室靶静止系能量先换算成质心能量。

### 不同离子温度下的相对速度分布

对无相对平均流的独立 Maxwellian，任一方向上 $v_{a,x}-v_{b,x}$ 的方差为 $\Theta_a/m_a+\Theta_b/m_b$。令约化质量为 $\mu$，将该方差写为 $\Theta_r/\mu$，得到

$$
\Theta_r=\mu\left(\frac{\Theta_a}{m_a}+\frac{\Theta_b}{m_b}\right),\qquad
F_r(\mathbf v)=\left(\frac{\mu}{2\pi\Theta_r}\right)^{3/2}e^{-\mu v^2/(2\Theta_r)}.
$$

把 $4\pi v^2dv$ 积分测度和 $\sigma(v)v$ 相乘，再用 $v^3dv=2E\,dE/\mu^2$ 换元，便得到本条反应率积分，温度替换为 $\Theta_r$。取近似质量比 D:T=2:3，$\Theta_D=10\,\mathrm{keV}$、$\Theta_T=20\,\mathrm{keV}$，可得 $\Theta_r=14\,\mathrm{keV}$。若用恒定截面作积分基准，平均相对速率与 $\sqrt{\Theta_r}$ 成正比；将两温度简单平均为15 keV，会使该基准高出 $\sqrt{15/14}-1=3.51\%$。

反应率的分布平均定义见 [Wurzel 与 Hsu，§III.1](https://arxiv.org/html/2105.10954v3)。上述两温度推广由高斯卷积直接推得；若有相对平均流，$F_r$ 的中心也随之平移。

## 燃料配比、杂质稀释与剖面积分

固定燃料离子总密度 $n_f=n_D+n_T$ 时，写 $n_D=xn_f$、$n_T=(1-x)n_f$，则 $R_{DT}=x(1-x)n_f^2\langle\sigma v\rangle$。在固定温度、同样约束和均匀混合这些假设下，$x(1-x)=1/4-(x-1/2)^2$ 在等数密度 D-T 配比处最大。这是条件极值；注入配比不一定等于核心配比，输运、边界回收和排灰会改变剖面。

准中性要求 $n_e=n_D+n_T+\sum_Z Z n_Z$。若固定 $n_e$，杂质占用电子密度预算，燃料密度就下降。例如只有完全电离氦灰且 $f_{\rm He}=n_{\rm He}/n_e=0.05$，则 $n_f=(1-2f_{\rm He})n_e=0.9n_e$；相同温度和 D-T 配比下，反应率仅由稀释就变为无氦灰时的 $0.9^2=0.81$。这个教学例子没有把辐射和约束变化混入稀释效应。[TRANSP：Plasma composition，准中性、燃料与杂质组分输入](https://transp.pppl.gov/nml/Composition.html)。

整个等离子体的功率是

$$
P_{\rm fus}=E_{DT}\int_V n_D(\mathbf x)n_T(\mathbf x)
\langle\sigma v\rangle(\mathbf x)\,dV.
$$

中心温度、体积平均温度和密度加权温度分别记录。作为积分检查，圆柱内若 $n_D=n_T=n_0(1-r^2/a^2)/2$、温度和反应率系数恒定，则 $\langle(1-r^2/a^2)^2\rangle_V=1/3$；用中心密度直接乘全体积会高估三倍。若温度也有梯度，必须把非线性反应率留在积分内部。本算例给出了剖面平均的解析基准。

### 密度与温度同时有剖面时如何积分

取圆柱内 $n_D=n_T=n_0(1-r^2/a^2)^p/2$、$\Theta=\Theta_0(1-r^2/a^2)^q$，并在指定温区用局部幂律 $\langle\sigma v\rangle=K_0(\Theta/\Theta_0)^s$ 作教学模型。以 $u=r^2/a^2$ 换元，归一化体积测度 $2rdr/a^2$ 恰为 $du$，于是

$$
\frac{P_{\rm fus}}{VE_{DT}n_0^2K_0/4}
=\int_0^1(1-u)^{2p+qs}du=\frac1{2p+qs+1}.
$$

取 $p=q=1,s=2$，真实积分因子为 $1/5$。若分别先平均密度、温度，再代入反应式，因子则为 $(1/2)^2(1/2)^2=1/16$，低估为正确值的31.25%。这来自高密度与高温在空间上重合，以及反应率的非线性。实际截面表可直接放进相同的一维积分，保留密度、温度剖面的共定位关系。剖面积分框架见 [Wurzel 与 Hsu，§IV.1.2，式 (25)–(35)](https://arxiv.org/html/2105.10954v3)；上式幂律积分是该框架的解析算例。

## 热储能、功率平衡与约束时间

非相对论、各向同性热组分满足 $m_s\langle c_j^2\rangle=\Theta_s$，$\mathbf c=\mathbf v-\mathbf u_s$。三方向求和并对物种、体积积分，得 $W_{\rm th}=\int\sum_s(3/2)n_s\Theta_s\,dV$。

快离子非热能量、磁场能量和整体流动动能应单独列账。一个明确边界下的零维热平衡可写为

$$
\frac{dW_{\rm th}}{dt}=P_{\rm aux\to th}+P_{\rm Ohm}
+P_{\alpha\to\rm th}-P_{\rm tr}-P_{\rm rad}.
$$

$P_{\rm aux\to th}$ 表示外部加热最终转移给所选热群体的功率；NBI 或射频先产生快粒子时，要扣除其储能增长和损失，由快粒子能量预算求得同一时刻的热输入。$P_{\alpha\to\rm th}$ 是快 alpha 向热背景的实际沉积功率，其相对于 alpha 出生功率的延迟由慢化过程决定。$P_{\rm tr}$ 是穿过所选边界的非辐射热/粒子能量通量，$P_{\rm rad}$ 为该体积内净辐射损失；涉及压缩做功、粒子源焓或快速体积变化时，还须显式补齐对应项。

若定义总损失约束时间 $\tau_{E,\rm tot}=W_{\rm th}/(P_{\rm tr}+P_{\rm rad})$，稳态时分母等于总热输入；非稳态时须扣除 $dW_{\rm th}/dt$。也可定义仅输运的 $\tau_{E,\rm tr}=W_{\rm th}/P_{\rm tr}$，但这样辐射必须继续单列，使辐射在预算中只计一次。[Fitzpatrick：Lawson Criterion，式 (1.11)–(1.16)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node7.html)。

教学例：$W_{\rm th}=20\,\mathrm{MJ}$，总热输入为 15 MW，测得储能以 5 MW 增长，则损失为 10 MW、$\tau_{E,\rm tot}=2\,\mathrm s$，而直接做 $20/15$ 得到的 1.33 s 混淆了积累与损失。放电持续时间、粒子约束时间和能量约束时间各自记录。

### 两库模型：外部功率何时成为热功率

将快粒子能量记为 $W_f$，取恒定慢化时间 $\tau_s$、忽略快粒子直接损失，外部功率 $P_0$ 自 $t=0$ 注入快粒子库：

$$
\dot W_f=P_0-W_f/\tau_s,\qquad
\dot W_{\rm th}=W_f/\tau_s-P_{\rm loss}.
$$

在 $W_f(0)=0$ 时，$W_f=P_0\tau_s(1-e^{-t/\tau_s})$，所以瞬时热输入为 $P_0(1-e^{-t/\tau_s})$。两式相加后内部传能项消去，得到 $d(W_f+W_{\rm th})/dt=P_0-P_{\rm loss}$，这就是不重复计入慢化功率的检验。

取 $P_0=10\,\mathrm{MW}$、$\tau_s=0.20\,\mathrm s$，在 0.10 s 时快粒子储能为 0.787 MJ，瞬时热化功率为 3.93 MW。若此短时段令 $P_{\rm loss}=0$，总注入能量为 1.00 MJ，热能增加为 0.213 MJ；两库相加准确还原注入能量。自加热与外部沉积的物理过程见 [ITER，What is burning plasma?](https://www.iter.org/node/20687/what-burning-plasma)；恒定慢化时间是本例采用的零维闭合。

## Lawson 条件、有限增益与三乘积

考虑均匀、无杂质、等数密度 D-T，$n_e=n_i=n$ 且 $\Theta_e=\Theta_i=\Theta$。有 $w_{\rm th}=3n\Theta$、$p_{\rm fus}=n^2\langle\sigma v\rangle E_{DT}/4$。令 $\eta_\alpha$ 为 alpha 出生能最终沉积到该热等离子体的比例，并暂取准稳态。使用上一条的总损失约束时间，忽略外部加热的点火必要条件为

$$
n\tau_{E,\rm tot}\geq
\frac{12\Theta}{\eta_\alpha E_\alpha\langle\sigma v\rangle},
\qquad
n\Theta\tau_{E,\rm tot}\geq
\frac{12\Theta^2}{\eta_\alpha E_\alpha\langle\sigma v\rangle}.
$$

中间平衡为 $3n\Theta/\tau_{E,\rm tot}\le\eta_\alpha n^2\langle\sigma v\rangle E_\alpha/4$。约去一个 $n$ 即得门槛，再乘 $\Theta$ 得三乘积；系数12来自热能系数3与 D-T 配比系数 $1/4$。

这里三乘积用 $\Theta$ 的 J 单位；若改报 $\mathrm{keV\,s\,m^{-3}}$，须把温度能量转换为 keV。这个条件建立热平衡门槛；稳定性、排热和燃料循环分别由相应方程求解。[Fitzpatrick：Lawson Criterion，式 (1.15)–(1.20)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node7.html)。

更一般地，本条定义 $Q_p=P_{\rm fus}/P_{\rm ext}$，$P_{\rm ext}$ 为实际进入热等离子体的外部功率（本条将欧姆项并入）。若采用仅以辅助加热为分母的文献定义，应另行保留欧姆项。在固定有限 $Q_p$ 的功率平衡中，上式分母相应变为

$$
\langle\sigma v\rangle\left(\eta_\alpha E_\alpha+\frac{E_{DT}}{Q_p}\right).
$$

这是直接代入 $P_{\rm ext}=P_{\rm fus}/Q_p$ 得到的代数结果。$Q_p\to\infty$ 返回点火条件，减小 $Q_p$ 表示容许更多外部输入。不同温度、燃料混合和辐射定义都会改变具体阈值；惯性约束则采用包含压缩和解体过程的能量平衡。[Wurzel 与 Hsu：§III–IV 的增益定义与路线比较](https://arxiv.org/html/2105.10954v3)。

### 显式计入轫致辐射的阈值推导

沿用纯 D-T、均匀同温条件，这次以仅输运的 $\tau_{E,\rm tr}$ 写平衡。将 $p_{\rm tr}=3n\Theta/\tau_{E,\rm tr}$、$p_{\rm Br}=n^2C_B\sqrt{T_{e,\rm eV}}$ 代入热平衡并除以 $n^2$，得到

$$
n\tau_{E,\rm tr}=\frac{3\Theta}
{\tfrac14\langle\sigma v\rangle(\eta_\alpha E_\alpha+E_{DT}/Q_p)-C_B\sqrt{T_{e,\rm eV}}},
\qquad C_B=1.69\times10^{-38}.
$$

本例 $\Theta=2.4033\times10^{-15}$ J、$E_\alpha=5.6076\times10^{-13}$ J、$E_{DT}=2.8198\times10^{-12}$ J。加热系数为 $3.6529\times10^{-35}$ W·m³，轫致项为 $2.0698\times10^{-36}$ W·m³；$3\Theta$ 除以两者之差，即得下述 $n\tau_E$。

$C_B$ 的单位配套本页的 SI 密度与 eV 温度数值约定。分母正值表示辐射之后仍有功率可抵消输运。取 $\Theta=15\,\mathrm{keV}$、给定 $\langle\sigma v\rangle=2\times10^{-22}\,\mathrm{m^3s^{-1}}$、$\eta_\alpha=0.8$、$Q_p=10$，算得 $n\tau_{E,\rm tr}=2.09\times10^{20}\,\mathrm{s\,m^{-3}}$；相同输入、不显式扣辐射的总损失时间对应 $1.97\times10^{20}\,\mathrm{s\,m^{-3}}$。代回平衡可分别还原输运损失与辐射损失。

辐射项和增益边界的原始推导见 [Wurzel 与 Hsu，§III 的功率平衡与 §IV.1.2 式 (30)](https://arxiv.org/html/2105.10954v3)。

## Alpha 自加热、燃烧等离子体与点火

![按同一热输入边界比较稳态 alpha 份额与恒时标慢化响应](/assets/diagrams/basic-burning.svg)

*按同一热输入边界比较稳态 alpha 份额与恒时标慢化响应。曲线与示意均按本条所列模型生成。*

D-T 出生 alpha 功率约为 $P_{\alpha,\rm birth}=(3.5/17.6)P_{\rm fus}$。它先形成高能粒子分布，再通过碰撞向电子和离子传能，且可能因轨道或波粒作用损失；必须区分出生、存储、沉积和逸出。alpha 的约束与损失由完整轨道和波粒作用决定。[ITER：What is burning plasma?，alpha 加热及 Alfvén 波导致损失的说明](https://www.iter.org/node/20687/what-burning-plasma)。

若近似所有 alpha 能量被吸收，且忽略其他内部源，以 $E_\alpha/E_{DT}\simeq1/5$ 估算，alpha 在总加热中的份额为

$$
f_\alpha=\frac{P_{\alpha,\rm dep}}{P_{\rm ext}+P_{\alpha,\rm dep}}
\simeq\frac{Q_p}{Q_p+5}.
$$

所以 $Q_p=5$ 对应约一半、$Q_p=10$ 对应约三分之二的自加热；若沉积比例为 $\eta_\alpha$，则变为 $\eta_\alpha Q_p/(5+\eta_\alpha Q_p)$。这些比值由上述功率定义直接算出。

燃烧等离子体强调反应产物自加热成为重要乃至主导的热源；点火则要求在给定状态下不再依赖外部热输入维持热平衡。厂级净电进一步计入启动、磁体、诊断和冷却等耗电。实验识别通过功率、储能变化及不确定性预算完成。[ITER：Fusion Glossary，Alpha Heating 与 Burning Plasma](https://www.iter.org/fusion-glossary)。

### 慢化造成的自加热幅值与相位延迟

令 alpha 出生功率为 $P_b=P_{b0}+\Re(\widehat P_be^{i\omega t})$，用 $\dot W_\alpha=P_b-W_\alpha/\tau_s$、$P_{\alpha\to th}=W_\alpha/\tau_s$ 描述全部能量最终热化的恒时标模型。只取扰动部分并代入复指数，得到

$$
\widehat P_{\alpha\to th}=\frac{\widehat P_b}{1+i\omega\tau_s},\quad
\frac{|\widehat P_{\alpha\to th}|}{|\widehat P_b|}
=\frac1{\sqrt{1+(\omega\tau_s)^2}},\quad
\varphi=-\arctan(\omega\tau_s).
$$

若 $\tau_s=0.20\,\mathrm s$、出生功率调制频率 $f=1\,\mathrm{Hz}$，则 $\omega\tau_s=1.257$，热化功率振幅为出生调制振幅的 62.3%，相位落后 51.5°。因此用中子信号追踪反应率，再与电子/离子温度响应比较，可以研究热化时序。所用模型是出生功率到热化功率的传递环节；温度影响反应率的反馈环节另外加入。研究背景见 [ITER 2024 研究计划，§3.3.5.1–3.3.5.2](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。

## 辐射损失、有效电荷与原子过程

对多组分等离子体，$Z_{\rm eff}=\sum_i n_iZ_i^2/n_e$；$Z_i$ 是当时的电离态电荷数，低温边界按实际电离态分布求和。充分电离、光学薄、非相对论 Maxwellian 条件下，电子—离子轫致辐射的常用近似为

$$
p_{\rm Br}\simeq 1.69\times10^{-38}\,
Z_{\rm eff}\,n_e^2\sqrt{T_{e,\rm eV}}
\quad\mathrm{W\,m^{-3}},
\qquad T_{e,\rm eV}=\frac{\Theta_e}{1\,\mathrm{eV}}.
$$

热轫致谱 $j_{\mathcal E}\propto n_e\sum_i n_iZ_i^2\Theta_e^{-1/2}e^{-\mathcal E/\Theta_e}$ 对光子能量积分，给 $p_{\rm Br}\propto Z_{\rm eff}n_e^2\sqrt{\Theta_e}$。NRL 系数由 W/cm³、cm⁻³ 转为 SI 时，$1.69\times10^{-32}\times10^6(10^{-6})^2=1.69\times10^{-38}$；温度数值仍用 eV。

其中 $n_e$ 的数值用 $\mathrm{m^{-3}}$。这是把 NRL 的 $\mathrm{cm^{-3}}$ 密度和 $\mathrm{W\,cm^{-3}}$ 功率转换后的系数；它包含近似的量子修正处理，适用于上述充分电离的非相对论条件。教学输入 $n_e=10^{20}\,\mathrm{m^{-3}}$、$T_{e,\rm eV}=10^4$、$Z_{\rm eff}=1$ 给出约 $1.69\times10^4\,\mathrm{W\,m^{-3}}$。[NRL Plasma Formulary 2016，印刷页 58，式 (30)](https://suli.pppl.gov/2016/course/NRL_FORMULARY_16.pdf)。

边界和杂质通常还需束缚—束缚线辐射、复合辐射以及电离能量损失。有效辐射率常写为 $p_{{\rm rad},Z}=n_en_ZL_Z$，但 $L_Z$ 的单位、元素密度定义、密度依赖和电离态演化模型必须与原子数据库一致；快速输运、非平衡电离和光学厚条件需进一步求解电离态与辐射输运。电子回旋辐射还涉及自吸收和壁面反射，净损失按发射与再吸收之差计算。[TRANSP：Radiation，轫致、线及回旋辐射的分别处理](https://transp.pppl.gov/nml/radiation.html)。

按电离态、能级和辐射通道求和：$p_{{\rm rad},Z}=n_e\sum_jn_{Z,j}\langle\sigma v\rangle_j\mathcal E_j\equiv n_en_ZL_Z$。$L_Z$ 必须匹配所用占据率与原子模型。

核心杂质过多会稀释燃料并损害功率平衡；边缘适量辐射却可将集中靶板热流重新分配到较大区域。设计时联合控制核心杂质浓度、边缘辐射位置和靶板热流。

### 同一杂质同时改变稀释与轫致辐射

设唯一杂质的电荷数为 $Z$，以 $f_Z=n_Z/n_e$ 表示其浓度。准中性给出 $n_D+n_T=(1-Zf_Z)n_e$，而有效电荷的分子为 $(n_D+n_T)+Z^2n_Z$，所以

$$
Z_{\rm eff}=1+Z(Z-1)f_Z,\qquad
\frac{p_{DT}}{p_{DT,0}}=(1-Zf_Z)^2
$$

其中反应率比固定了 $n_e$、温度及等数密度 D-T 配比。取完全电离碳 $Z=6$、$f_C=0.01$，得到 $Z_{\rm eff}=1.30$、反应率比0.8836。若 $n_e=10^{20}\,\mathrm{m^{-3}}$、电子温度10 keV，近似轫致功率由16.9增至21.97 kW/m³。增加的30%来自电荷平方加权，减少的11.64%反应率来自燃料密度乘积，两种作用可以分别检查。

这一算例采用充分电离条件，仅计算轫致通道。组分与有效电荷输入见 [TRANSP，Plasma composition](https://transp.pppl.gov/nml/Composition.html)，辐射通道的独立处理见 [TRANSP，Radiated power](https://transp.pppl.gov/nml/radiation.html)。

## 热稳定性、氦灰与燃烧反馈

热平衡点不必然稳定。对固定密度、体积和组分的简化模型，令 $F(\Theta)=P_{\rm heat}(\Theta)-P_{\rm loss}(\Theta)$，有效热容 $C_\Theta=dW/d\Theta>0$。在 $F(\Theta_0)=0$ 附近有

$$
C_\Theta\frac{d\,\delta\Theta}{dt}=F'(\Theta_0)\delta\Theta.
$$

在平衡 $\dot\Theta_0=F(\Theta_0)=0$ 附近，热容导数只贡献二阶项，故

$$
\delta\Theta(t)=\delta\Theta(0)e^{\lambda t},\qquad
\lambda=\frac{F^{\prime}(\Theta_0)}{C_\Theta(\Theta_0)}.
$$

$F'<0$ 时此单变量热扰动衰减，$F'>0$ 时增长。温度升高同时改变反应率、辐射、输运和快粒子沉积，增长率由这些项的总导数决定。密度、杂质、alpha 慢化、控制延迟等加入后应研究多变量系统，单一斜率只是局部教学判据。燃烧控制还受执行器功率和响应速度限制。[ITER 研究计划 ITR-24-005，§3.3.5.2 的自加热与热稳定性问题](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。

每次 D-T 反应产生一个氦核。对进入所选热氦灰库的粒子，可写 $dN_{\rm He}/dt=\dot N_{\alpha\to\rm ash}-\dot N_{\rm He,net\,out}$；只有在慢化库近似稳态、损失已处理时，第一项才近似等于反应数率。灰粒子经过边界、回收和抽排后，净排出率可能远小于一次越过核心边界的通量。用有效 $\tau_{\rm He}^*=N_{\rm He}/\dot N_{\rm He,net\,out}$ 需要说明库存与排出边界，并与能量损失定义的 $\tau_E$ 分别列出。

教学稳态若灰源为 $10^{19}\,\mathrm{s^{-1}}$、有效排灰时间为 5 s，则灰库存为 $5\times10^{19}$ 个粒子；净排出变慢会增加灰库存并降低燃料密度。该预算把“约束反应产物以加热”和“及时排出热化灰”连接起来，两者发生在不同阶段。[ITR-24-005，§3.3.5 与表 19 的灰积累、燃料比例及多尺度反馈研究范围](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。

### 氦灰积累与燃料稀释的自洽稳态

固定 $n_e$、温度和体积，令 $f=n_{\rm He}/n_e$，无灰时的反应率密度为 $R_0$。若 alpha 全部进入热灰库，净排灰采用常时间 $\tau_h$，则燃料稀释与灰守恒组合为

$$
\frac{df}{dt}=k(1-2f)^2-\frac f{\tau_h},\qquad k=R_0/n_e.
$$

置 $a=k\tau_h$，稳态满足 $4af^2-(4a+1)f+a=0$。用数值稳定的形式写物理解为 $f_*=2a/[4a+1+\sqrt{8a+1}]$。当 $a=0.10$，算得 $f_*=0.07295$，反应率比 $(1-2f_*)^2=0.7295$。若先固定反应率再算库存，会得到 $f=0.10$；联立后稀释降低了灰源。

二次方程选取 $a\to0$ 时趋零且 $0\le f<1/2$ 的根：$f=[4a+1-\sqrt{8a+1}]/(8a)$。分子有理化得到稳定形式；对灰方程右侧关于 $f$ 求导便得扰动增长率。

进一步线性化得到扰动增长率 $\lambda=-4k(1-2f_*)-1/\tau_h<0$。在这个固定温度模型里，灰扰动会衰减；若把温度作为第二变量，就需计算二维 Jacobian 的迹与行列式。灰、自加热及控制反馈的研究框架见 [ITER 研究计划，§3.3.5.2 与表19](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。

## 从等离子体增益到净电输出

功率计算必须先画出边界。等离子体增益以聚变输出和等离子体外部热输入相比；墙插功率还包括加热器效率。设 $\eta_h=P_{\rm ext}/P_{\rm wall,heat}$，则加热耗电为 $P_{\rm ext}/\eta_h$。若热循环效率为 $\eta_{\rm th}$、进入热循环的可用热功率为 $P_{\rm th,useful}$，厂级净电示意式为

$$
P_{\rm net}=\eta_{\rm th}P_{\rm th,useful}
-\frac{P_{\rm ext}}{\eta_h}-P_{\rm other}.
$$

$P_{\rm other}$ 包括磁体低温、泵、燃料处理和其他辅机等。$P_{\rm th,useful}$ 需要独立热平衡，可能含中子反应热、被回收的辅助加热和其他项，所有热量按去向只计入一次。[Wurzel 与 Hsu：§III.7 Engineering gain](https://arxiv.org/html/2105.10954v3)。

纯教学预算取 $P_{\rm th,useful}=500\,\mathrm{MW}$、$\eta_{\rm th}=0.4$、$P_{\rm ext}=50\,\mathrm{MW}$、$\eta_h=0.5$、$P_{\rm other}=70\,\mathrm{MW}$，净电只有 $200-100-70=30\,\mathrm{MW}$。把加热效率改为 0.3，其余不变，净电转为约 $-36.7\,\mathrm{MW}$。

脉冲设备还需按完整周期积分，计入启动、间歇、储能往返损失和可用率；峰值正净电并不自动等于年度净供电。工程收支、经济性和核系统资格分别在[工程系统](../../工程系统/README.md)和[项目产业](../../项目产业/README.md)展开。

### 含热回收的净电增益门槛

固定聚变功率，设可回收聚变相关热为 $MP_{\rm fus}$，外部加热最终回收到热循环的比例为 $r_h$，其他耗电为 $p_oP_{\rm fus}$。这里 $M$ 合并热捕集及包层核反应增热，$r_h$ 与墙插效率 $\eta_h$ 分别描述热去向和电耗。由 $P_{\rm ext}=P_{\rm fus}/Q_p$ 代入厂级预算，得到

$$
\frac{P_{\rm net}}{P_{\rm fus}}=
\eta_{\rm th}M-p_o-
\frac{1/\eta_h-\eta_{\rm th}r_h}{Q_p}.
$$

当 $\eta_{\rm th}M>p_o$ 时，正净电要求 $Q_p>(1/\eta_h-\eta_{\rm th}r_h)/(\eta_{\rm th}M-p_o)$。设 $M=1.1,r_h=0.8,\eta_h=0.5,\eta_{\rm th}=0.4,p_o=0.1$，门槛为4.94；若 $P_{\rm fus}=500\,\mathrm{MW},Q_p=10$，热循环收入为236 MW电功率，加热耗电100 MW、其他耗电50 MW，净电86 MW。四个功率项逐一算出后，与无量纲式得到的0.172完全一致。系统边界定义见 [Wurzel 与 Hsu，§III.7，Engineering gain](https://arxiv.org/html/2105.10954v3)。

[返回基础原理](../README.md) · [输运与边界](../输运与边界/README.md)
