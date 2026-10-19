# 输运与边界

核心加热、跨磁面输运、开放磁力线排热和材料响应构成同一个守恒问题。本专题从可核算的方程出发连接这些区域。采用 SI 单位，$\Theta_s=k_BT_s$ 是以 J 表示的温度能量；使用 eV 数值时另行注明。局域公式用于解释机制，装置预测还需要几何、源项、边界条件与诊断约束。

## 守恒输运方程与有效扩散

粒子守恒的基本形式为 $\partial_t n+\nabla\cdot\boldsymbol\Gamma=S$，其中 $\boldsymbol\Gamma$ 单位 $\mathrm{m^{-2}s^{-1}}$，净源 $S$ 单位 $\mathrm{m^{-3}s^{-1}}$。沿嵌套磁面平均，并选有长度量纲的径向坐标 $r$，可写

$$
\frac{\partial n}{\partial t}
+\frac{1}{V'}\frac{\partial}{\partial r}(V'\Gamma_r)=S,
\qquad
V'=\frac{dV}{dr},\quad
\Gamma_r=-D\frac{\partial n}{\partial r}+V_p n.
$$

先在厚度 $dr$ 的薄磁壳内积分粒子守恒：壳体积为 $V'dr$，净径向流出为 $\partial_r(V'\Gamma_r)dr$；除以壳体积便得到上式的散度结构。这里 $n,S,\Gamma_r$ 取与该磁面体积测度一致的平均。扩散加夹带是局域线性闭合：将通量对密度梯度与密度展开，梯度项的负系数定义为 $D$，零梯度剩余通量除以 $n$ 定义为 $V_p$。热流关系同样是近局域平衡的线性导热闭合，以 $n\chi$ 定义温度能量梯度的响应系数；守恒律本身不决定这些输运系数。

$D$ 单位 $\mathrm{m^2s^{-1}}$，夹带速度 $V_p$ 单位 $\mathrm{m\,s^{-1}}$；此处规定向外为正。换用无量纲磁通坐标时，梯度与通量中的度量必须同步转换。热流常近似为 $q_r=-n\chi\,\partial_r\Theta$；这只是导热项，完整能量通量还包括粒子携带的焓、流动能和其他通道。[Fitzpatrick：Perpendicular Closure Scheme，式 (2.303)–(2.304)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node42.html)。

密度梯度驱动的扩散通量可被对流与交叉驱动抵消，净方向由各项之和确定。由某次稳态剖面拟合出的有效 $D,\chi$ 也不必等于扰动实验中的增量响应；非局域输运、临界梯度和时变源均可能使简单闭合失效。首先检查积分守恒，再解释拟合系数。

教学验证：长圆柱中取恒定 $D$、均匀源 $S_0$、轴上正则且边界密度固定为 $n_a$。稳态解析解是 $n=n_a+S_0(a^2-r^2)/(4D)$，因此 $\Gamma_r=S_0r/2$。长度 $L$ 的边界粒子流 $2\pi aL\Gamma_r(a)=S_0\pi a^2L$ 恰好等于全体积源；遗漏圆柱散度中的 $1/r$ 会破坏这个预算。这个解析解可用作圆柱输运程序的基准。

圆柱算例的求解步骤是 $(1/r)d(r\Gamma_r)/dr=S_0$。从轴积分，轴上正则性消去积分常数，故 $r\Gamma_r=S_0r^2/2$。再用 $\Gamma_r=-D\,dn/dr$，得到 $dn/dr=-S_0r/(2D)$；从 $r$ 积到边缘 $a$ 并代入 $n(a)=n_a$，便得到所列抛物线密度。

### 由瞬态衰减测扩散系数

在一维区间 $0<x<L$，边界固定为同一密度，减去稳态背景后有 $\partial_t\delta n=D\partial_x^2\delta n$、$\delta n(0,t)=\delta n(L,t)=0$。用分离变量 $\delta n=X(x)T(t)$，两侧除以 $DXT$，得到 $X''/X=T'/(DT)=-k^2$。边界选出 $k_j=j\pi/L$，每个模的解为

$$
\delta n_j=A_j\sin(j\pi x/L)\exp[-D(j\pi/L)^2t].
$$

对基模，振幅减半时间 $t_{1/2}$ 满足 $D=L^2\ln2/(\pi^2t_{1/2})$。取 $L=0.20\,\mathrm m$、$t_{1/2}=0.010\,\mathrm s$，得到 $D=0.281\,\mathrm{m^2s^{-1}}$；第二模因波数加倍，衰减率四倍。实际拟合可同时检验多个空间模，从而区分单一常扩散与随位置或时间变化的输运。局域输运闭合背景见 [Fitzpatrick，Perpendicular Closure Scheme](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node42.html)。

## 经典输运、新经典输运与香蕉轨道

均匀强磁场中，碰撞改变回旋轨道的导引中心，随机游走给出经典横向扩散的量级 $D_\perp\sim\rho^2\nu$。它要求磁化且轨道步长小于背景变化尺度；精确系数还随物种、碰撞算子与所讨论通量变化。环形磁场不均匀使部分粒子在低场侧反弹，漂移轨道投影形成“香蕉”，碰撞在这些较宽轨道之间散射，形成新经典输运。

对大环径比、近圆截面托卡马克，令 $\epsilon=r/R\ll1$、安全因子为 $q$，离子热速度约定为 $v_{ti}=\sqrt{2\Theta_i/m_i}$。代表性量级为

$$
\Delta_b\sim\frac{q\rho_i}{\sqrt{\epsilon}},\qquad
\omega_b\sim\frac{v_{ti}\sqrt{\epsilon}}{qR},\qquad
\nu_*\sim\frac{qR\nu_{ii}}{\epsilon^{3/2}v_{ti}}.
$$

这里 $\Delta_b$ 不规定全宽或半宽，故只给量级；具体系数依赖投射角与定义。$\nu_*\ll1$ 表示去俘获时间长于反弹周期，可进入香蕉区；随碰撞性增大还会转入平台区与 Pfirsch–Schlüter 区。用裸碰撞频率直接除以反弹频率会遗漏窄俘获域的散射尺度。[Fitzpatrick：Trapped and Passing Particles，轨道宽度、反弹和去俘获排序](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node27.html)。

香蕉区离子热扩散常具有 $\chi_i\sim q^2\rho_i^2\nu_{ii}/\epsilon^{3/2}$ 的量级，其系数随碰撞闭合和几何改变。若算得轨道宽度接近剖面尺度，局域展开就不自洽。新经典理论提供碰撞基线，实际总通量还可能受湍流、三维磁场与中性粒子影响。[Fitzpatrick：Neoclassical Transport，式 (2.284)–(2.286)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node41.html)。

这些新经典量级可以按轨道与随机游走逐步估计。大环径比场强相对变化为 $O(\epsilon)$，磁镜条件使被俘获粒子的平行速率为 $v_\parallel\sim v_{ti}\sqrt\epsilon$，俘获方向占比为 $f_t\sim\sqrt\epsilon$。平行连接长度为 $qR$，故反弹时间为 $qR/(v_{ti}\sqrt\epsilon)$；曲率/梯度径向漂移量级为 $v_{ti}\rho_i/R$，乘反弹时间便得到 $\Delta_b$。俯仰角扩散系数尺度为 $\nu_{ii}$，跨越宽度 $O(\sqrt\epsilon)$ 的俘获域需时间 $\epsilon/\nu_{ii}$，因此去俘获率为 $\nu_{ii}/\epsilon$；它除以反弹频率就是 $\nu_*$。最后用“俘获比例×步长平方×去俘获率”得 $\chi_i\sim\sqrt\epsilon(q^2\rho_i^2/\epsilon)(\nu_{ii}/\epsilon)$，即所列香蕉区标度。常直场的 $D_\perp\sim\rho^2\nu$ 则是每次散射移动一个回旋半径、等待约 $1/\nu$ 的同类随机游走估计。

### 速度自相关如何产生横向扩散

在均匀磁场的简化散射模型中，设单方向速度自相关为 $C_x(t)=(\Theta/m)e^{-\nu t}\cos\Omega t$。由位移 $\Delta x=\int_0^t v_xdt'$ 得 $\langle\Delta x^2\rangle=2\int_0^t(t-s)C_x(s)ds$；长时极限下 $D_x=\lim\langle\Delta x^2\rangle/(2t)$，因而

$$
D_x=\int_0^\infty C_x(s)ds
=\frac{\Theta}{m}\frac{\nu}{\nu^2+\Omega^2}.
$$

在 $\nu\ll|\Omega|$ 时，$D_x\simeq\rho_t^2\nu/2$，其中 $\rho_t=\sqrt{2\Theta/m}/|\Omega|$；因子1/2来自单方向热速度方差。取给定 $\Theta/m=10^{10}\,\mathrm{m^2s^{-2}}$、$|\Omega|=10^8\,\mathrm{s^{-1}}$、$\nu=10^4\,\mathrm{s^{-1}}$，得 $D_x\simeq0.0100\,\mathrm{m^2s^{-1}}$。该指数自相关模型把回旋与散射的作用分开，环形装置则进一步加入俘获轨道的步长和去俘获时间，见 [Fitzpatrick，Trapped and Passing Particles，式 (2.73)–(2.93)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node27.html)。

## 自举电流与双极输运

径向压强和温度梯度，在俘获/通行粒子的轨道及碰撞动量交换作用下，可以产生磁面平均的平行自举电流。它无需变压器环电压直接驱动，但维持梯度仍需能量与粒子预算。稳态设计将自举电流分布与外部驱动电流组合，形成所需的总电流剖面。

简单香蕉区模型给出 $j_{\rm bs}$ 与压强梯度、俘获比例和极向磁场的关系；多物种、碰撞性、三维磁场和强梯度会改变系数。实际应用应使用注明有效域的闭合，连同外部电流驱动一起演化 $q$ 剖面。磁岛内压强趋平时，局部自举电流缺失可参与新经典撕裂模驱动；岛宽、种子扰动和射频电流沉积位置因此都很重要。[Fitzpatrick：Neoclassical Tearing Modes，式 (14.198) 及其限制](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node181.html)。

长期准中性要求径向电荷通量满足双极条件 $\sum_s q_s\Gamma_s\simeq0$，各物种仍可有有限的径向通量。在轴对称托卡马克的新经典近似中，动量守恒使主要径向通量具有内禀双极性；径向电场进一步由动量平衡等条件确定。普通非轴对称仿星器的离子与电子通量对 $E_r$ 的响应不同，双极条件往往参与确定 $E_r$，甚至可能有多个根。[Fitzpatrick：Neoclassical Transport，式 (2.271) 附近的对比](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node41.html)。

瞬态极化电流、外加非轴对称场及动量源会补充上述平衡。所谓电子根或离子根是特定输运问题的解，其稳定性由根附近的输运响应和剖面共同决定。

### 由电荷守恒求双极电场

将各物种连续性方程乘以电荷后相加，反应源若守恒电荷便相消，得到 $\partial_t\rho_q+\nabla\cdot\mathbf j=0$。在稳态、轴上正则、无外部径向电流的模型里，径向总电流为零；氘和完全电离氦混合物因此满足 $\Gamma_e=\Gamma_D+2\Gamma_{\rm He}$。

在需要由输运求径向电场的非轴对称模型中，可在某个工作点附近线性化：$\Gamma_i=\Gamma_{i0}+a_iE_r$、$\Gamma_e=\Gamma_{e0}+a_eE_r$。对单价离子，代入双极条件得

$$
E_r=\frac{\Gamma_{e0}-\Gamma_{i0}}{a_i-a_e}.
$$

取 $\Gamma_{i0}=4\times10^{20}$、$\Gamma_{e0}=10^{20}\,\mathrm{m^{-2}s^{-1}}$，$a_i=10^{17}$、$a_e=-2\times10^{17}\,\mathrm{m^{-1}s^{-1}V^{-1}}$，解得 $E_r=-1000\,\mathrm{V\,m^{-1}}$，两通量均为 $3\times10^{20}\,\mathrm{m^{-2}s^{-1}}$。斜率是本例输入；轴对称新经典通量具有内禀双极性，需要由动量平衡等确定电场。几何差别的依据见 [Fitzpatrick，Neoclassical Transport，式 (2.271)及后文](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node41.html)。

## 湍流、漂移波与回旋动理学

背景密度和温度梯度储存自由能。离子温度梯度模（ITG）、俘获电子模（TEM）、电子温度梯度模（ETG）等可在不同尺度和碰撞性下驱动涨落；电磁条件下还需考虑磁扰动产生的输运。多种模式可共存；线性计算给出增长率，非线性演化决定饱和热通量。

以静电、局域直磁场 $\mathbf B=B\hat{\mathbf z}$ 为例，涨落漂移的径向分量为 $\widetilde v_x=-\partial_y\widetilde\phi/B$，湍流粒子通量是 $\Gamma_x^{\rm turb}=\langle\widetilde n\,\widetilde v_x\rangle$。取人工谐波 $\widetilde n=N\cos ky$、$\widetilde\phi=\Phi\cos(ky+\delta)$，在一个波长平均可得

$$
\Gamma_x^{\rm turb}=\frac{Nk\Phi}{2B}\sin\delta.
$$

在该坐标中 $\mathbf v_E=\mathbf E\times\mathbf B/B^2$、$\mathbf E=-\nabla\phi$，所以 $v_{E,x}=-\partial_y\phi/B$。将人工谐波求导得 $\widetilde v_x=k\Phi\sin(ky+\delta)/B$；与 $N\cos ky$ 相乘，利用一周期内 $\langle\cos ky\sin ky\rangle=0$、$\langle\cos^2ky\rangle=1/2$，便得到上述相位通量。

密度与电势的幅值、相位共同决定此谐波通量，非线性模型再决定它们如何达到饱和。

回旋动理学通过对快速回旋相位平均，在 $\omega/\Omega_i\ll1$、$\rho_i/L\ll1$ 等排序下保留有限回旋半径与波粒共振。它通常把六维相空间降为五维，但仍须选择局域/全局、静电/电磁、碰撞及边界模型。[Abel 等：Multiscale Gyrokinetics，2013 v4，Introduction 的排序与回旋平均](https://arxiv.org/pdf/1209.4782)。鞘层、接近回旋频率或宽轨道问题采用相应的尺度排序。[Fitzpatrick：Perpendicular Closure Scheme，微不稳定性与各向异性尺度](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node42.html)；[Wilson：输运与多尺度反馈讨论，§3](https://scientific-publications.ukaea.uk/wp-content/uploads/rsta.2017.0435.pdf)。

剪切 $E\times B$ 流和带状流可能削弱相关涡结构，但输运、流和梯度相互反馈。数值研究应报告网格、盒子大小、统计时间、守恒与噪声收敛，再与热通量或涨落谱比较；详见[仿真计算](../../仿真计算/README.md)。

### 把回旋平均写成可计算的积分

固定导引中心 $\mathbf R$，瞬时粒子位置为 $\mathbf R+\boldsymbol\rho(\vartheta)$。对单个垂直 Fourier 模 $\phi=\phi_k e^{i\mathbf k\cdot\mathbf x}$，绕一圈平均，取 $\mathbf k_\perp\cdot\boldsymbol\rho=k_\perp\rho\cos\vartheta$，有

$$
\langle\phi\rangle_\vartheta=
\phi_ke^{i\mathbf k\cdot\mathbf R}\frac1{2\pi}\int_0^{2\pi}e^{ia\cos\vartheta}d\vartheta
=J_0(a)\phi_ke^{i\mathbf k\cdot\mathbf R},\quad a=k_\perp\rho.
$$

展开指数后奇数项平均为零，利用 $\langle\cos^2\vartheta\rangle=1/2$、$\langle\cos^4\vartheta\rangle=3/8$，得 $J_0(a)=1-a^2/4+a^4/64+\cdots$。取 $k_\perp=1000\,\mathrm{m^{-1}}$、$\rho=1\,\mathrm{mm}$，一圈数值积分得到 $J_0(1)=0.76520$，四阶展开为0.765625，相差0.056%。这展示同一电势在轨道上的正负变化如何部分抵消；对整个物种还要继续按垂直速度分布平均。回旋平均和尺度排序见 [Abel 等，Multiscale Gyrokinetics，§5.1，式 (72)](https://arxiv.org/pdf/1209.4782v4)。

## H 模、台基与边缘局域模

H 模的关键特征是边缘输运屏障及其形成的陡峭密度/温度梯度，核心压力可在台基顶上继续增长。台基高度、宽度和梯度是不同量：若近似线性，$\Delta p\simeq\lvert dp/dr\rvert\Delta r$；相同高度可来自不同宽度与梯度，稳定性未必相同。

L–H 转换阈值与跨分离面功率、密度、磁场、离子种类、几何和壁条件有关。跨分离面功率由吸收加热扣除核心辐射和储能增长后求得。H 模内仍存在湍流，持续运行需要同时控制台基、排热与粒子收支。

Type-I 边缘局域模（ELM）的 peeling–ballooning 图像把边缘电流与压强梯度驱动联系起来；并非所有 ELM 类型都能由同一极限解释。相关稳定性计算依赖完整平衡、自举电流和边界形状；台基预测还需输运约束。[Snyder：ITER School 2015，peeling–ballooning 稳定性与 EPED 台基课程](https://www.iter.org/sites/default/files/education/snyder_iterschool15_r3.pdf)。

ELM 瞬态损失能量 $\Delta W_{\rm ELM}$、频率 $f_{\rm ELM}$ 与平均功率约 $f_{\rm ELM}\Delta W_{\rm ELM}$ 不足以确定靶板峰值温升；还要知道沉积时间、空间分布和材料热扩散。抑制或缓解 ELM 应同时检查约束、粒子排出和杂质积累，评价其对完整运行状态的影响。[腔体材料](../../腔体材料/README.md)进一步区分稳态热流与瞬态损伤。

### 台基梯度与 ELM 平均功率的分别核算

在大环径比圆截面模型中，常以 $\alpha=-(2\mu_0Rq^2/B^2)dp/dr$ 表示无量纲压力梯度。若台基近似线性，$dp/dr=-\Delta p/\Delta r$，代入得 $\alpha=2\mu_0Rq^2\Delta p/(B^2\Delta r)$。取 $R=3\,\mathrm m,q=4,B=2.5\,\mathrm T,\Delta p=8\,\mathrm{kPa},\Delta r=0.04\,\mathrm m$，得 $\alpha=3.86$；在相同高度下将宽度加倍，$\alpha$ 减半。具体稳定边界随磁剪切、电流与形状变化。压力梯度和边缘电流的联合驱动见 [Snyder，ITER School 2015，第15页](https://www.iter.org/sites/default/files/education/snyder_iterschool15_r3.pdf)。

这里 $\alpha$ 是所采用平衡模型的归一化定义：压力梯度力的曲率尺度为 $|dp/dr|/R$，弯曲磁力线的张力尺度为 $B^2/(\mu_0q^2R^2)$，两者的比值再乘惯用因子 2，即 $2\mu_0Rq^2|dp/dr|/B^2$。这说明其几何和量纲来源，临界值仍需稳定性方程。对于近线性的台基，积分 $\Delta p=-\int(dp/dr)dr$ 给出梯度与宽度关系。重复事件的平均功率则是总能量 $N_{\rm ELM}\Delta W$ 除以观察时长，使用 $f_{\rm ELM}=N_{\rm ELM}/\Delta t$ 得到 $f_{\rm ELM}\Delta W$。

另设每次 ELM 向指定靶区沉积20 kJ、频率50 Hz，则时间平均功率为1 MW。若每次在0.5 ms内均匀沉积到0.20 m²，脉冲期面热流为200 MW/m²。两个数通过占空比 $f\Delta t=0.025$ 相连：脉冲热流乘占空比是该区域的时间平均5 MW/m²。材料热响应需要使用脉冲的时间和空间分布。

## 刮削层、平行导热与两点模型

最后闭合磁面外侧的刮削层（SOL）中，磁力线通常连接材料表面。粒子与热先从核心横向进入 SOL，再沿磁场快速流向偏滤器或限器；磁通膨胀和倾斜入射使上游通量与靶板面热流不同。局部峰值由各通道的功率分配及有效沉积面积确定。

在稳态、截面积恒定、无沿途源损失、电子导热主导且局域碰撞闭合适用的简化磁力管内，令 $s$ 从上游指向靶板，

$$
q_\parallel=-\kappa_0\Theta_e^{5/2}\frac{d\Theta_e}{ds},
\qquad
\Theta_u^{7/2}-\Theta_t^{7/2}
=\frac{7q_\parallel L_\parallel}{2\kappa_0}.
$$

先由无源稳态能量守恒得到 $dq_\parallel/ds=0$，再分离变量：$\Theta_e^{5/2}d\Theta_e=-(q_\parallel/\kappa_0)ds$。从上游积分到靶端，左边是 $(2/7)(\Theta_t^{7/2}-\Theta_u^{7/2})$，移项便得到两点式。$5/2$ 的导热标度来自热通量估计 $n_ev_{te}\lambda_e\,\nabla\Theta_e$：$v_{te}\propto\Theta_e^{1/2}$、Coulomb 自由程 $\lambda_e\propto\Theta_e^2/n_e$，相乘消去密度；其具体系数由碰撞闭合计算。

第二式直接由第一式积分得到。此处温度能量用 J，因此 $\kappa_0$ 的单位为 $\mathrm{W\,m^{-1}\,J^{-7/2}}$；若输入 eV 或 K，系数必须转换。脱靶计算在此导热关系上联立靶端鞘层、压力、对流、辐射、电离和动量方程，并加入磁通膨胀。[MIT PSFC：Yunxing Ma 2012 学位论文，附录 C 式 (C.9)–(C.10)](https://library.psfc.mit.edu/catalog/reports/2010/12rr/12rr008/12rr008_full.pdf)。

一个无量纲积分检查是取 $\kappa_0=q_\parallel=L_\parallel=1$、$\Theta_t=1$，则 $\Theta_u=(9/2)^{2/7}$。代回沿程剖面应得到处处相同的导热通量，而不仅是端点温差正确。这些数值不带装置单位，仅验证积分关系。

低碰撞性下自由程可能与梯度尺度相当，局域 Spitzer–Härm 热流会失效；需要动理学或经验证的非局域闭合。横向间歇丝状结构也会使单一平均宽度掩盖壁面尾部负荷。因此边界计算须结合平行和横向通道及可测量量，共同重建完整的排热过程。

### 磁通膨胀下的两点模型

若无沿途功率损失而磁力管截面积 $A(s)$ 变化，守恒量为 $P=A(s)q_\parallel(s)$。因此导热式改写为 $\Theta^{5/2}d\Theta/ds=-P/[\kappa_0A(s)]$；两端积分后得到

$$
\Theta_u^{7/2}-\Theta_t^{7/2}
=\frac{7P}{2\kappa_0}\int_0^L\frac{ds}{A(s)}.
$$

取 $A(s)=A_u(1+bs/L)$，积分为 $[L/(A_ub)]\ln(1+b)$。靶端面积为上游四倍时 $b=3$，右端相对于恒面积情形的因子是 $\ln4/3=0.4621$，同时靶端平行热流为上游的四分之一。若上游 $q_u=100\,\mathrm{MW\,m^{-2}}$、磁力线与靶面夹角2°，则面法向热流为 $(q_u/4)\sin2^\circ=0.8725\,\mathrm{MW\,m^{-2}}$。此处 $A$ 始终为垂直磁场的截面积，最后一步才投影到靶面。

恒面积的积分起点见 [Yunxing Ma，MIT 2012，附录C，式 (C.9)–(C.10)](https://library.psfc.mit.edu/catalog/reports/2010/12rr/12rr008/12rr008_full.pdf)；上式为保留 $A(s)$ 后的守恒推广。

## 鞘层、预鞘与 Bohm 判据

电子通常比离子更快到达吸收壁面，浮动壁会调整电势以使净电流为零。靠近壁面的薄鞘层容许显著电荷分离，核心的准中性近似在这里失效；连接核心与鞘层的预鞘则可在近似准中性下加速离子。

对一维、稳态、无碰撞、冷单价离子和 Boltzmann 电子，令鞘入口离子速度为 $u_s$。线性展开离子能量守恒与电子密度响应，并要求形成单调离子鞘，可得

$$
u_s\ge c_s,\qquad c_s=\sqrt{\Theta_e/m_i}.
$$

这是该模型的 Bohm 判据。温离子、多离子、非 Maxwellian 电子、碰撞鞘层或强二次电子发射需要相应推广，按所选分布和闭合推导入口条件。[MIT OCW 16.55，Lecture 17，式 (12)–(14)](https://ocw.mit.edu/courses/16-55-ionized-gases-fall-2014/69c9b98ec3496da071f8cdd7a1486ff7_MIT16_55F14_Lecture17.pdf)。

在同样假设下，另取入口速度恰为 $u_s=c_s$；若入口电子密度为 $n_s$，无势垒时单向 Maxwellian 电子通量为 $n_s\sqrt{\Theta_e/(2\pi m_e)}$。令壁面电势 $\phi_w<\phi_s$，电子通量被因子 $\exp[e(\phi_w-\phi_s)/\Theta_e]$ 抑制；与 $n_sc_s$ 相等给出

$$
\phi_s-\phi_w=\frac{\Theta_e}{2e}\ln\frac{m_i}{2\pi m_e}.
$$

电子通量的中间积分为 $\Gamma_e=n_s\int_{v_c}^\infty v[m_e/(2\pi\Theta_e)]^{1/2}e^{-m_ev^2/(2\Theta_e)}dv$，其中势垒阈速满足 $m_ev_c^2/2=e(\phi_s-\phi_w)$。令积分变量为 $m_ev^2/(2\Theta_e)$，便得到单向通量乘指数抑制因子。再令它等于 $n_s\sqrt{\Theta_e/m_i}$，约去密度和温度平方根，取对数后就是所列浮动势降。

对氘、$\Theta_e=10\,\mathrm{eV}$，算得 $c_s\simeq2.19\times10^4\,\mathrm{m\,s^{-1}}$、电势落差约 31.9 V。此结果对应浮动平面吸收壁；外加偏压通过边界电势另行输入。倾斜磁场还会引入磁预鞘；射频电势整流则需时变模型，与[ICRH 射频鞘层](../../辅助加热/离子回旋加热/README.md)相接。

### Bohm 条件的密度展开推导

令 $x=e(\phi_s-\phi)/\Theta_e\ge0$、$M=u_s/c_s$。离子能量守恒给出 $u_i^2=u_s^2+2\Theta_ex/m_i$，再由 $n_iu_i=n_su_s$ 得 $n_i/n_s=(1+2x/M^2)^{-1/2}$；Boltzmann 电子有 $n_e/n_s=e^{-x}$。两式展开相减：

$$
\frac{n_i-n_e}{n_s}
=\left(1-\frac1{M^2}\right)x+
\left(\frac{3}{2M^4}-\frac12\right)x^2+O(x^3).
$$

单调负壁鞘层入口要求向壁侧形成正空间电荷，故最低阶给出 $M\ge1$。在临界 $M=1$ 时一阶项消失，二阶项为正的 $x^2$。算例取 $x=0.10$：精确离子密度为 $0.91287n_s$，电子密度为 $0.90484n_s$，电荷密度差为 $0.008034n_s$，与二阶估计 $0.0100n_s$ 同号并在 $x\to0$ 时趋近。推导对应 [MIT 16.55 Lecture17，第1–2页式 (1)–(14)](https://ocw.mit.edu/courses/16-55-ionized-gases-fall-2014/69c9b98ec3496da071f8cdd7a1486ff7_MIT16_55F14_Lecture17.pdf)。

## 中性粒子、回收与脱靶

到达壁面的粒子可被反射、吸附或以原子/分子形式重新进入等离子体；这些回收粒子再经历电离、激发、电荷交换与分子反应。回收系数需说明计量的是原子核数、分子数还是粒子通量。电荷交换可以把离子的能量与动量转移给中性粒子，而光辐射、电离和复合改变功率及粒子预算。

脱靶通常指靶端等离子体从高温、强附着状态进入冷却并降低靶负荷的运行状态。诊断联合跟踪靶温度、离子通量 rollover（随上游条件变化先增后降）、抽排和核心性能，以重建功率、动量和粒子平衡。

可用控制体积写 $\dot N_{\rm target}=\dot N_{\rm upstream}+\dot N_{\rm ion}-\dot N_{\rm rec}-dN/dt$，这里 $N$ 是控制体积内的等离子体离子库存，target/upstream 是离子流率，ion/rec 分别为电离生成及复合移除离子的速率；各项按离子所含原子核数统一计量，旁向通量存在时还应补项。若改统计包含中性态的全部原子核库存，电离/复合只在电荷态之间转移，在总核数预算中相消。靶离子流减少可能来自电离源功率不足、净复合、动量损失改变流动等共同作用，不宜把所有脱靶归因于单一复合过程。[Dudson 等：SD1D 的粒子、能量与动量损失研究，作者摘要](https://scientific-publications.ukaea.uk/papers/the-role-of-particle-energy-and-momentum-losses-in-1d-simulations-of-divertor-detachment/)。

分子辅助复合/解离在部分低温高密度条件中可成为重要通道。MAST-U Super-X 的原始研究结合谱学与功率/粒子预算讨论了这些过程；其具体结论必须保留装置、气体和模型条件，不可直接给所有偏滤器套同一阈值。[Verhaegh 等：MAST-U 等离子体—原子—分子相互作用研究，作者摘要](https://scientific-publications.ukaea.uk/papers/the-role-of-plasma-atom-and-molecule-interactions-on-power-particle-balance-during-detachment-on-the-mast-upgrade-super-x-divertor/)。

稳定排热还要求辐射区位置、杂质穿透、泵速与核心稀释可控。诊断上应把光谱、红外靶热流、探针、密度和辐射测量合并核算；一个亮度图像不足以独立确定电子温度或全部损失。

### 回收放大与电离功率限制

取稳态控制体积，忽略复合与旁向损失。设上游离子流率为 $\dot N_u$，到靶离子中有比例 $R$ 返回中性态，其中比例 $f_{\rm ion}$ 在该体积内再电离。用 $r=Rf_{\rm ion}$ 合并这两个过程，粒子预算成为 $\dot N_t=\dot N_u+r\dot N_t$，所以

$$
\dot N_t=\frac{\dot N_u}{1-r},\qquad
P_{\rm ion}=E_{\rm ion,eff}\frac{r\dot N_u}{1-r}.
$$

若 $\dot N_u=10^{21}\,\mathrm{s^{-1}},r=0.9$，则靶流率放大到 $10^{22}\,\mathrm{s^{-1}}$。设每次电离连同激发等平均耗能为30 eV，所需功率为43.3 kW。若可用于这些过程的功率仅20 kW，则电离源最大为 $4.16\times10^{21}\,\mathrm{s^{-1}}$，对应此模型的靶流率上限 $5.16\times10^{21}\,\mathrm{s^{-1}}$，原来设定的高回收状态就需要调整。30 eV是例题指定的有效成本；氢原子基态电离阈值为13.6 eV。电离功率与粒子平衡的研究背景见 [Dudson 等，SD1D 原论文摘要](https://scientific-publications.ukaea.uk/papers/the-role-of-particle-energy-and-momentum-losses-in-1d-simulations-of-divertor-detachment/)。

## 快粒子轨道、Alfvén 共振与损失

NBI、ICRH 和聚变 alpha 产生的快粒子往往不满足热背景的 Maxwell 分布。其回旋半径、轨道宽度和慢化时间可能明显大于热粒子尺度；有限轨道、磁场波纹、磁岛和磁扰动会产生再分布或损失。必须分别报告受约束快粒子能量、对热背景的沉积和到壁面的逃逸功率。

局域剪切 Alfvén 波频率近似为 $\omega\simeq k_\parallel v_A$，$v_A=B/\sqrt{\mu_0\rho}$。Alfvén 关系来自均匀磁场中的两条线性方程：横向动量满足 $\rho\partial_t\mathbf u_\perp=(B/\mu_0)\partial_\parallel\delta\mathbf B_\perp$，理想感应方程满足 $\partial_t\delta\mathbf B_\perp=B\partial_\parallel\mathbf u_\perp$。对前式再取时间导数并代入后式，得 $\partial_t^2\mathbf u_\perp=[B^2/(\mu_0\rho)]\partial_\parallel^2\mathbf u_\perp$；代入平面波便有 $\omega^2=k_\parallel^2v_A^2$。

在环形几何中，粒子与模的共振可以通过环向运动和反弹/通行运动的谐波组合表达，例如 $\omega-n\omega_\varphi-l\omega_b=0$；整数 $n,l$ 与频率须采用同一角坐标和符号约定。将轨道作用的 Fourier 相位写为 $\psi=n\varphi+l\vartheta_b-\omega t$，其中 $\vartheta_b$ 为反弹/通行相位，沿未扰动轨道求导得到 $\dot\psi=n\omega_\varphi+l\omega_b-\omega$。持续相互作用要求这相位近似不变，令导数为零便得到上述共振关系。

满足轨道共振后，再由驱动与阻尼确定模式增长率。

净增长还要比较快粒子分布梯度提供的驱动与热背景、连续谱等阻尼。Alfvén 本征模可使快粒子重新分布，也可能使其真正越出约束边界；中子率下降或某个探测器增强需要结合能量、空间与轨道信息判断，再计算全局损失比例。

ITER 2024 研究计划把 alpha 约束、快粒子模和局部第一壁负荷列为燃烧等离子体研究问题，强调现有 NBI/ICRF 实验向燃烧条件外推时分布各向异性和归一化轨道尺度不同。[ITR-24-005，§3.3.5.1](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。快粒子模型应与[辅助加热](../../辅助加热/README.md)、中子及快离子诊断共同核验。

### 由 Alfvén 速度估算轨道共振尺度

在大环径比、圆截面模型中，平行波数近似为 $k_{\parallel,m}=(n-m/q)/R$。这一平行波数由波相位 $n\varphi-m\theta$ 沿磁力线求导得到：近圆大环径比下 $d\varphi/dl\simeq1/R$、$d\theta/dl\simeq1/(qR)$，故 $k_\parallel=d(n\varphi-m\theta)/dl=(n-m/q)/R$。

相邻极向谐波 $m,m+1$ 在 $nq=m+1/2$ 处具有相反而等大的平行波数，大小为 $1/(2qR)$。环形耦合在两条剪切 Alfvén 连续谱相交处形成频率间隙，中心量级为

$$
\omega_{\rm TAE}\simeq\frac{v_A}{2qR},\qquad
f_{\rm TAE}\simeq\frac{v_A}{4\pi qR}.
$$

取纯氘质量密度 $\rho=m_Dn_D$、$n_D=10^{20}\,\mathrm{m^{-3}}$、$B=5\,\mathrm T$，得 $v_A=7.71\times10^6\,\mathrm{m\,s^{-1}}$。在 $q=2,R=3\,\mathrm m$ 时，中心频率约102.3 kHz。3.5 MeV alpha 的速率约 $1.30\times10^7\,\mathrm{m\,s^{-1}}$，所以其部分俯仰角可满足 $v_\parallel\simeq v_A$；本例对应 $v_\parallel/v\simeq0.594$。模驱动还取决于分布梯度和阻尼。频率间隙及频率修正见 [Gorelenkov，PPPL-4715，§II.B 式 (14)](https://bp-pub.pppl.gov/pub_report/2012/PPPL-4715.pdf)；alpha 约束背景见 [ITER 研究计划，§3.3.5.1](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。

## 破裂、热淬灭与逃逸电子

托卡马克破裂可能使热能快速下降（热淬灭），随后电流显著衰减（电流淬灭）。两阶段的时序与重叠由具体放电决定。快速热负荷、感应涡流/晕电流产生的机械载荷、以及逃逸电子束是不同损伤通道；ELM 主要发生于边缘，破裂则涉及整体约束与电流演化。

简化电路中，等离子体电流衰减通过电感产生环向电场。对足够高能的电子，碰撞阻力随速度的依赖容许电场持续加速；种子来源可包括热尾和 Dreicer 扩散过程，已有逃逸电子还可通过大角散射引发雪崩。Dreicer 场描述热速度附近的拖曳尺度，相对论临界场描述高能端的最低碰撞阻力尺度。部分电离、辐射反作用及输运会改变实际阈值和演化。[Hesslow 等：Dreicer runaway generation，§1–2 的特征场、种子与部分电离讨论](https://arxiv.org/html/1910.00356v2)。

EPFL 的 TCV 研究将破裂和逃逸电子产生、输运与终止分别测量，并研究注入和磁扰动的缓解作用。[EPFL Swiss Plasma Center：TCV Disruptions and Runaway Electrons](https://www.epfl.ch/research/domains/swiss-plasma-center/tcv-disruptions-and-runaway-electrons/)。这些实验为模型提供约束；跨装置比较时同时输入尺寸、壁材、电流与边界条件。

运行判断需要预警时延、漏报/误报、执行器响应和最终壁负荷的共同证据。数据库应保留破裂前的密度、辐射、电流与磁扰动轨迹，避免只收成功放电而形成选择偏差；具体数据质量和反馈问题见[诊断控制](../../诊断控制/README.md)及[实验运行](../../实验运行/README.md)。

### 电流淬灭的电感预算与两种临界场

在常电感 $L_p$、等效电阻 $R_p$ 的零外加电压电路中，$L_p\dot I+R_pI=0$，故 $I=I_0e^{-t/\tau_I}$、$\tau_I=L_p/R_p$。磁能 $W_B=L_pI^2/2$ 的导数为 $\dot W_B=-R_pI^2$，恰好供给电阻耗散；沿环向的感应电场大小为 $E_\phi=L_pI/(2\pi R\tau_I)$。

设 $L_p=5\,\mu\mathrm H,I_0=1\,\mathrm{MA},\tau_I=10\,\mathrm{ms},R=2\,\mathrm m$，初始磁能2.50 MJ，环电压500 V、电场39.8 V/m。充分电离、相对论碰撞模型的临界场和 Dreicer 特征场采用

$$
E_c=\frac{n_ee^3\ln\Lambda}{4\pi\varepsilon_0^2m_ec^2},\qquad
E_D=\frac{m_ec^2}{\Theta_e}E_c.
$$

这两个特征场是电力与 Coulomb 摩擦的平衡尺度。充分电离弱耦合模型的高速电子摩擦幅值为 $F_{\rm drag}\simeq n_ee^4\ln\Lambda/(4\pi\varepsilon_0^2m_ev^2)$，其 $v^{-2}$ 和 Coulomb 对数来自小角散射动量交换的冲量参数积分，详见[动理学与碰撞](../动理学与碰撞/README.md)。在高能相对论极限取最低摩擦尺度对应 $v\simeq c$，并令 $eE_c=F_{\rm drag}$，得到上式；以本页约定的热能尺度 $v^2=\Theta_e/m_e$ 替换，便得到 $E_D/E_c=m_ec^2/\Theta_e$。$E_D$ 是拖曳特征尺度，完整热分布的产生率仍需碰撞动力学，不能把这一步替换当作完整逃逸率计算。

取 $n_e=10^{20}\,\mathrm{m^{-3}},\ln\Lambda=15,\Theta_e=10\,\mathrm{eV}$，得到 $E_c=0.0765\,\mathrm{V/m}$、$E_D=3.91\times10^3\,\mathrm{V/m}$。本例 $E_c<E_\phi<E_D$，表明高能电子的持续加速条件和热电子整体的拖曳尺度相距很大；逃逸产生率还需分布动力学。两种场的定义及部分电离修正见 [Hesslow 等，2019，§1–2](https://arxiv.org/html/1910.00356v2)。

[返回基础原理](../README.md) · [聚变反应与燃烧](../聚变反应与燃烧/README.md)
