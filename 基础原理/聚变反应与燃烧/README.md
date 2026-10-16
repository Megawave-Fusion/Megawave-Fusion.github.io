# 聚变反应与燃烧

本专题把核反应、速度分布、热平衡和电站功率口径连接起来。默认讨论非相对论、热核 D-T 等离子体；$\Theta_s=k_BT_s$ 表示温度能量，代入 SI 公式时单位是 J。示例均为明确给定输入的教学计算，不是装置实测。点火、等离子体增益和净电输出各有不同的边界，不能用一个未定义的“Q”代替。

## 核反应道、质量亏损与产物能量

核反应释放的能量来自初末态静质量之差，$Q_{\rm nuc}=(\sum m_{\rm in}-\sum m_{\rm out})c^2$，这里的 $Q_{\rm nuc}$ 单位是能量，不是无量纲的聚变增益。常用反应道为

$$
\begin{aligned}
\mathrm D+\mathrm T&\rightarrow{}^4\mathrm{He}+n+17.6\,\mathrm{MeV},\\
\mathrm D+\mathrm D&\rightarrow{}^3\mathrm{He}+n+3.27\,\mathrm{MeV},\\
\mathrm D+\mathrm D&\rightarrow\mathrm T+p+4.03\,\mathrm{MeV},\\
\mathrm D+{}^3\mathrm{He}&\rightarrow{}^4\mathrm{He}+p+18.35\,\mathrm{MeV}.
\end{aligned}
$$

这些是低入射能量下的近似释放能，不能把不同 D-D 分支的能量全部记到同一次反应上。D-T 产物在质心系具有大小相等、方向相反的动量；非相对论近似 $E=p^2/(2m)$ 给出 $E_n/E_\alpha=m_\alpha/m_n\simeq4$，所以约 14.1 MeV 由中子携带、3.5 MeV 由带电 alpha 粒子携带。真实实验室能谱还受反应物热运动、束流和观测方向影响。[Fitzpatrick：Nuclear Fusion Reactions，式 (1.1)–(1.5)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node6.html)；[NRL Plasma Formulary 2016，印刷页 44–45 的反应表](https://suli.pppl.gov/2016/course/NRL_FORMULARY_16.pdf)。

带电产物可以通过磁约束和碰撞向等离子体传能；中子主要在等离子体外的材料中输运、沉积能量并引起核反应。因此 $P_{\rm fus}$ 不能全当作核心自加热。D-$^3$He 的主反应不直接产生中子，但含氘等离子体仍可能发生 D-D 反应及后续反应；“主通道无中子”不是整套燃料循环零中子的保证。选择燃料还必须考虑反应率、辐射、燃料可得性和产物处理。

## 反应截面、反应率与速度分布平均

截面 $\sigma(E)$ 单位是 $\mathrm{m^2}$，描述给定相对碰撞能量下的核反应概率尺度；反应率系数 $\langle\sigma v\rangle$ 单位是 $\mathrm{m^3\,s^{-1}}$，已经对相对速度作平均。若 $F_a,F_b$ 为积分等于一、相互独立的速度概率密度，

$$
\langle\sigma v\rangle_{ab}=\iint F_a(\mathbf v_a)F_b(\mathbf v_b)
\sigma(v_r)v_r\,d^3v_a\,d^3v_b,
\qquad v_r=\lvert\mathbf v_a-\mathbf v_b\rvert.
$$

单位体积单位时间的反应数为 $R_{ab}=n_an_b\langle\sigma v\rangle_{ab}/(1+\delta_{ab})$，单位 $\mathrm{m^{-3}\,s^{-1}}$。相同粒子反应的二分之一避免把同一对粒子数两次；不同 D-D 分支还需各自的分支截面。对相同温度能量 $\Theta$、无相对整体漂移的 Maxwellian 组分，约化质量 $\mu=m_am_b/(m_a+m_b)$ 给出

$$
\langle\sigma v\rangle=\sqrt{\frac{8}{\pi\mu}}\,\Theta^{-3/2}
\int_0^\infty\sigma(E)E e^{-E/\Theta}\,dE.
$$

该式可从相对速度的三维高斯分布换元 $E=\mu v_r^2/2$ 得到。积分权重不是只在 $E=\Theta$ 取值；用“平均能量处的截面 × 平均速度”替代会丢失截面的强能量依赖。不同温度、束靶反应和非热尾部须重新平均。[Wurzel 与 Hsu：Lawson 综述，§III 的反应率与热核假设](https://arxiv.org/html/2105.10954v3)。

一个可独立检验积分程序的人工基准是令截面恒为 $\sigma_0$；积分得到 $\langle\sigma v\rangle=\sigma_0\sqrt{8\Theta/(\pi\mu)}$。这只用于检查归一化和积分器，绝不是 D-T 截面模型。真实计算必须给出截面/拟合版本、能量定义和拟合有效范围，尤其不能把实验室靶静止系能量直接当成质心能量。

## 燃料配比、杂质稀释与剖面积分

固定燃料离子总密度 $n_f=n_D+n_T$ 时，写 $n_D=xn_f$、$n_T=(1-x)n_f$，则 $R_{DT}=x(1-x)n_f^2\langle\sigma v\rangle$。在固定温度、同样约束和均匀混合这些假设下，$x(1-x)=1/4-(x-1/2)^2$ 在等数密度 D-T 配比处最大。这是条件极值；注入配比不一定等于核心配比，输运、边界回收和排灰会改变剖面。

准中性要求 $n_e=n_D+n_T+\sum_Z Z n_Z$。若固定 $n_e$，杂质占用电子密度预算，燃料密度就下降。例如只有完全电离氦灰且 $f_{\rm He}=n_{\rm He}/n_e=0.05$，则 $n_f=(1-2f_{\rm He})n_e=0.9n_e$；相同温度和 D-T 配比下，反应率仅由稀释就变为无氦灰时的 $0.9^2=0.81$。这个教学例子没有把辐射和约束变化混入稀释效应。[TRANSP：Plasma composition，准中性、燃料与杂质组分输入](https://transp.pppl.gov/nml/Composition.html)。

整个等离子体的功率是

$$
P_{\rm fus}=E_{DT}\int_V n_D(\mathbf x)n_T(\mathbf x)
\langle\sigma v\rangle(\mathbf x)\,dV.
$$

中心温度、体积平均温度和密度加权温度不能随意互换。作为积分检查，圆柱内若 $n_D=n_T=n_0(1-r^2/a^2)/2$、温度和反应率系数恒定，则 $\langle(1-r^2/a^2)^2\rangle_V=1/3$；用中心密度直接乘全体积会高估三倍。若温度也有梯度，必须把非线性反应率留在积分内部。本算例只说明平均次序，并不拟合某个装置。

## 热储能、功率平衡与约束时间

非相对论、各向同性热组分的储能为 $W_{\rm th}=\int\sum_s(3/2)n_s\Theta_s\,dV$。快离子非热能量、磁场能量和整体流动动能应单独列账。一个明确边界下的零维热平衡可写为

$$
\frac{dW_{\rm th}}{dt}=P_{\rm aux\to th}+P_{\rm Ohm}
+P_{\alpha\to\rm th}-P_{\rm tr}-P_{\rm rad}.
$$

$P_{\rm aux\to th}$ 表示外部加热最终转移给所选热群体的功率；NBI 或射频先产生快粒子时，要扣除其储能增长和损失，不能把原始吸收功率直接当作同一时刻的热输入。$P_{\alpha\to\rm th}$ 是快 alpha 向热背景的实际沉积功率；在慢化时间不可忽略的瞬态中，不等于同一时刻的 alpha 出生功率。$P_{\rm tr}$ 是穿过所选边界的非辐射热/粒子能量通量，$P_{\rm rad}$ 为该体积内净辐射损失；涉及压缩做功、粒子源焓或快速体积变化时，还须显式补齐对应项。

若定义总损失约束时间 $\tau_{E,\rm tot}=W_{\rm th}/(P_{\rm tr}+P_{\rm rad})$，稳态时分母等于总热输入；非稳态时须扣除 $dW_{\rm th}/dt$。也可定义仅输运的 $\tau_{E,\rm tr}=W_{\rm th}/P_{\rm tr}$，但这样辐射必须继续单列，不能再用总损失的阈值公式重复扣除辐射。[Fitzpatrick：Lawson Criterion，式 (1.11)–(1.16)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node7.html)。

教学例：$W_{\rm th}=20\,\mathrm{MJ}$，总热输入为 15 MW，测得储能以 5 MW 增长，则损失为 10 MW、$\tau_{E,\rm tot}=2\,\mathrm s$，而直接做 $20/15$ 得到的 1.33 s 混淆了积累与损失。放电持续时间、粒子约束时间和能量约束时间也不是同一量。

## Lawson 条件、有限增益与三乘积

考虑均匀、无杂质、等数密度 D-T，$n_e=n_i=n$ 且 $\Theta_e=\Theta_i=\Theta$。有 $w_{\rm th}=3n\Theta$、$p_{\rm fus}=n^2\langle\sigma v\rangle E_{DT}/4$。令 $\eta_\alpha$ 为 alpha 出生能最终沉积到该热等离子体的比例，并暂取准稳态。使用上一条的总损失约束时间，忽略外部加热的点火必要条件为

$$
n\tau_{E,\rm tot}\geq
\frac{12\Theta}{\eta_\alpha E_\alpha\langle\sigma v\rangle},
\qquad
n\Theta\tau_{E,\rm tot}\geq
\frac{12\Theta^2}{\eta_\alpha E_\alpha\langle\sigma v\rangle}.
$$

这里三乘积用 $\Theta$ 的 J 单位；若改报 $\mathrm{keV\,s\,m^{-3}}$，须把温度能量转换为 keV，不能仅改单位标签。条件来自输入与损失比较，本身不保证稳定性、排热或可持续供燃料。[Fitzpatrick：Lawson Criterion，式 (1.15)–(1.20)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node7.html)。

更一般地，本条定义 $Q_p=P_{\rm fus}/P_{\rm ext}$，$P_{\rm ext}$ 为实际进入热等离子体的外部功率（本条将欧姆项并入）。若采用仅以辅助加热为分母的文献定义，应另行保留欧姆项。在固定有限 $Q_p$ 的功率平衡中，上式分母相应变为

$$
\langle\sigma v\rangle\left(\eta_\alpha E_\alpha+\frac{E_{DT}}{Q_p}\right).
$$

这是直接代入 $P_{\rm ext}=P_{\rm fus}/Q_p$ 的推导，不是额外经验定律。$Q_p\to\infty$ 返回点火条件，减小 $Q_p$ 表示容许更多外部输入。不同温度、燃料混合和辐射定义都会改变具体阈值；磁约束的 $\tau_E$ 也不能不加修改地替换成惯性约束脉宽。[Wurzel 与 Hsu：§III–IV 的增益定义与路线比较](https://arxiv.org/html/2105.10954v3)。

## Alpha 自加热、燃烧等离子体与点火

D-T 出生 alpha 功率约为 $P_{\alpha,\rm birth}=(3.5/17.6)P_{\rm fus}$。它先形成高能粒子分布，再通过碰撞向电子和离子传能，且可能因轨道或波粒作用损失；必须区分出生、存储、沉积和逸出。磁场使带电产物具有回旋运动，并不保证全部 alpha 永不逸出。[ITER：What is burning plasma?，alpha 加热及 Alfvén 波导致损失的说明](https://www.iter.org/node/20687/what-burning-plasma)。

若近似所有 alpha 能量被吸收，且忽略其他内部源，以 $E_\alpha/E_{DT}\simeq1/5$ 估算，alpha 在总加热中的份额为

$$
f_\alpha=\frac{P_{\alpha,\rm dep}}{P_{\rm ext}+P_{\alpha,\rm dep}}
\simeq\frac{Q_p}{Q_p+5}.
$$

所以 $Q_p=5$ 对应约一半、$Q_p=10$ 对应约三分之二的自加热；若沉积比例为 $\eta_\alpha$，则变为 $\eta_\alpha Q_p/(5+\eta_\alpha Q_p)$。这些比值是上述统一口径下的代数结果，不是任一装置的已实现纪录。

燃烧等离子体强调反应产物自加热成为重要乃至主导的热源；点火则要求在给定状态下不再依赖外部热输入维持热平衡。两者均不等于电站净发电，也不意味着整个启动、磁体、诊断和冷却系统可以断电。判断实验是否进入该状态，需要功率、储能变化及不确定性预算，不能只看温度峰值。[ITER：Fusion Glossary，Alpha Heating 与 Burning Plasma](https://www.iter.org/fusion-glossary)。

## 辐射损失、有效电荷与原子过程

对多组分等离子体，$Z_{\rm eff}=\sum_i n_iZ_i^2/n_e$；$Z_i$ 是当时的电离态电荷数，不能在低温边界直接取原子序数。充分电离、光学薄、非相对论 Maxwellian 条件下，电子—离子轫致辐射的常用近似为

$$
p_{\rm Br}\simeq 1.69\times10^{-38}\,
Z_{\rm eff}\,n_e^2\sqrt{T_{e,\rm eV}}
\quad\mathrm{W\,m^{-3}},
\qquad T_{e,\rm eV}=\frac{\Theta_e}{1\,\mathrm{eV}}.
$$

其中 $n_e$ 的数值用 $\mathrm{m^{-3}}$。这是把 NRL 的 $\mathrm{cm^{-3}}$ 密度和 $\mathrm{W\,cm^{-3}}$ 功率转换后的系数；它包含近似的量子修正处理，不能用于任意温度和电离态。教学输入 $n_e=10^{20}\,\mathrm{m^{-3}}$、$T_{e,\rm eV}=10^4$、$Z_{\rm eff}=1$ 给出约 $1.69\times10^4\,\mathrm{W\,m^{-3}}$。[NRL Plasma Formulary 2016，印刷页 58，式 (30)](https://suli.pppl.gov/2016/course/NRL_FORMULARY_16.pdf)。

边界和杂质通常还需束缚—束缚线辐射、复合辐射以及电离能量损失。有效辐射率常写为 $p_{{\rm rad},Z}=n_en_ZL_Z$，但 $L_Z$ 的单位、元素密度定义、密度依赖和电离态演化模型必须与原子数据库一致；单一温度曲线不能概括快速输运、非平衡电离或光学厚条件。电子回旋辐射还涉及自吸收和壁面反射，不能把真空单粒子辐射直接全计为净损失。[TRANSP：Radiation，轫致、线及回旋辐射的分别处理](https://transp.pppl.gov/nml/radiation.html)。

核心杂质过多会稀释燃料并损害功率平衡；边缘适量辐射却可将集中靶板热流重新分配到较大区域。应同时约束核心污染和边缘排热，而不是笼统追求辐射越少越好。

## 热稳定性、氦灰与燃烧反馈

热平衡点不必然稳定。对固定密度、体积和组分的简化模型，令 $F(\Theta)=P_{\rm heat}(\Theta)-P_{\rm loss}(\Theta)$，有效热容 $C_\Theta=dW/d\Theta>0$。在 $F(\Theta_0)=0$ 附近有

$$
C_\Theta\frac{d\,\delta\Theta}{dt}=F'(\Theta_0)\delta\Theta.
$$

$F'<0$ 时此单变量热扰动衰减，$F'>0$ 时增长。温度升高同时改变反应率、辐射、输运和快粒子沉积，不能只比较某一热源的斜率。密度、杂质、alpha 慢化、控制延迟等加入后应研究多变量系统，单一斜率只是局部教学判据。燃烧控制还受执行器功率和响应速度限制。[ITER 研究计划 ITR-24-005，§3.3.5.2 的自加热与热稳定性问题](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。

每次 D-T 反应产生一个氦核。对进入所选热氦灰库的粒子，可写 $dN_{\rm He}/dt=\dot N_{\alpha\to\rm ash}-\dot N_{\rm He,net\,out}$；只有在慢化库近似稳态、损失已处理时，第一项才近似等于反应数率。灰粒子经过边界、回收和抽排后，净排出率可能远小于一次越过核心边界的通量。用有效 $\tau_{\rm He}^*=N_{\rm He}/\dot N_{\rm He,net\,out}$ 需要说明库存与排出边界，不能直接等同于 $\tau_E$。

教学稳态若灰源为 $10^{19}\,\mathrm{s^{-1}}$、有效排灰时间为 5 s，则灰库存为 $5\times10^{19}$ 个粒子；净排出变慢会增加灰库存并降低燃料密度。该预算把“约束反应产物以加热”和“及时排出热化灰”连接起来，两者发生在不同阶段。[ITR-24-005，§3.3.5 与表 19 的灰积累、燃料比例及多尺度反馈研究范围](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。该文件为 2024 年研究计划，本文不据此声称其中运行目标已经实现。

## 从等离子体增益到净电输出

功率计算必须先画出边界。等离子体增益以聚变输出和等离子体外部热输入相比；墙插功率还包括加热器效率。设 $\eta_h=P_{\rm ext}/P_{\rm wall,heat}$，则加热耗电为 $P_{\rm ext}/\eta_h$。若热循环效率为 $\eta_{\rm th}$、进入热循环的可用热功率为 $P_{\rm th,useful}$，厂级净电示意式为

$$
P_{\rm net}=\eta_{\rm th}P_{\rm th,useful}
-\frac{P_{\rm ext}}{\eta_h}-P_{\rm other}.
$$

$P_{\rm other}$ 包括磁体低温、泵、燃料处理和其他辅机等。$P_{\rm th,useful}$ 需要独立热平衡，可能含中子反应热、被回收的辅助加热和其他项；不能无条件设为 $P_{\rm fus}$，也不能把已经回收的热再次相减。[Wurzel 与 Hsu：§III.7 Engineering gain](https://arxiv.org/html/2105.10954v3)。

纯教学预算取 $P_{\rm th,useful}=500\,\mathrm{MW}$、$\eta_{\rm th}=0.4$、$P_{\rm ext}=50\,\mathrm{MW}$、$\eta_h=0.5$、$P_{\rm other}=70\,\mathrm{MW}$，净电只有 $200-100-70=30\,\mathrm{MW}$。把加热效率改为 0.3，其余不变，净电转为约 $-36.7\,\mathrm{MW}$。这些输入是为展示系统边界而指定，不是 ITER 或某电站的设计数据。

脉冲设备还需按完整周期积分，计入启动、间歇、储能往返损失和可用率；峰值正净电并不自动等于年度净供电。工程收支、经济性和核系统资格分别在[工程系统](../../工程系统/README.md)和[项目产业](../../项目产业/README.md)展开。

[返回基础原理](../README.md) · [输运与边界](../输运与边界/README.md)
