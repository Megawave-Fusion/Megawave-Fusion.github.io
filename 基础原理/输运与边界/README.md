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

$D$ 单位 $\mathrm{m^2s^{-1}}$，夹带速度 $V_p$ 单位 $\mathrm{m\,s^{-1}}$；此处规定向外为正。换用无量纲磁通坐标时，梯度与通量中的度量必须同步转换。热流常近似为 $q_r=-n\chi\,\partial_r\Theta$；这只是导热项，完整能量通量还包括粒子携带的焓、流动能和其他通道。[Fitzpatrick：Perpendicular Closure Scheme，式 (2.303)–(2.304)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node42.html)。

有向外密度梯度不代表粒子总通量必定向外，因为对流与交叉驱动可能抵消扩散。由某次稳态剖面拟合出的有效 $D,\chi$ 也不必等于扰动实验中的增量响应；非局域输运、临界梯度和时变源均可能使简单闭合失效。首先检查积分守恒，再解释拟合系数。

教学验证：长圆柱中取恒定 $D$、均匀源 $S_0$、轴上正则且边界密度固定为 $n_a$。稳态解析解是 $n=n_a+S_0(a^2-r^2)/(4D)$，因此 $\Gamma_r=S_0r/2$。长度 $L$ 的边界粒子流 $2\pi aL\Gamma_r(a)=S_0\pi a^2L$ 恰好等于全体积源；遗漏圆柱散度中的 $1/r$ 会破坏这个预算。这是人工基准，不是托卡马克剖面拟合。

## 经典输运、新经典输运与香蕉轨道

均匀强磁场中，碰撞改变回旋轨道的导引中心，随机游走给出经典横向扩散的量级 $D_\perp\sim\rho^2\nu$。它要求磁化且轨道步长小于背景变化尺度；精确系数还随物种、碰撞算子与所讨论通量变化。环形磁场不均匀使部分粒子在低场侧反弹，漂移轨道投影形成“香蕉”，碰撞在这些较宽轨道之间散射，形成新经典输运。

对大环径比、近圆截面托卡马克，令 $\epsilon=r/R\ll1$、安全因子为 $q$，离子热速度约定为 $v_{ti}=\sqrt{2\Theta_i/m_i}$。代表性量级为

$$
\Delta_b\sim\frac{q\rho_i}{\sqrt{\epsilon}},\qquad
\omega_b\sim\frac{v_{ti}\sqrt{\epsilon}}{qR},\qquad
\nu_*\sim\frac{qR\nu_{ii}}{\epsilon^{3/2}v_{ti}}.
$$

这里 $\Delta_b$ 不规定全宽或半宽，故只给量级；具体系数依赖投射角与定义。$\nu_*\ll1$ 表示去俘获时间长于反弹周期，可进入香蕉区；随碰撞性增大还会转入平台区与 Pfirsch–Schlüter 区。用裸碰撞频率直接除以反弹频率会遗漏窄俘获域的散射尺度。[Fitzpatrick：Trapped and Passing Particles，轨道宽度、反弹和去俘获排序](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node27.html)。

香蕉区离子热扩散常具有 $\chi_i\sim q^2\rho_i^2\nu_{ii}/\epsilon^{3/2}$ 的量级；这不是所有密度、几何和碰撞性的通用公式。若算得轨道宽度接近剖面尺度，局域展开就不自洽。新经典理论提供碰撞基线，实际总通量还可能受湍流、三维磁场与中性粒子影响。[Fitzpatrick：Neoclassical Transport，式 (2.284)–(2.286)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node41.html)。

## 自举电流与双极输运

径向压强和温度梯度，在俘获/通行粒子的轨道及碰撞动量交换作用下，可以产生磁面平均的平行自举电流。它无需变压器环电压直接驱动，但维持梯度仍需能量与粒子预算。“自举”因此不是没有能源消耗的独立电源，也不能把总自举份额高直接等同于电流剖面适合稳态运行。

简单香蕉区模型给出 $j_{\rm bs}$ 与压强梯度、俘获比例和极向磁场的关系；多物种、碰撞性、三维磁场和强梯度会改变系数。实际应用应使用注明有效域的闭合，连同外部电流驱动一起演化 $q$ 剖面。磁岛内压强趋平时，局部自举电流缺失可参与新经典撕裂模驱动；岛宽、种子扰动和射频电流沉积位置因此都很重要。[Fitzpatrick：Neoclassical Tearing Modes，式 (14.198) 及其限制](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node181.html)。

长期准中性要求径向电荷通量满足双极条件 $\sum_s q_s\Gamma_s\simeq0$，而不是要求每个物种都没有径向通量。在轴对称托卡马克的新经典近似中，动量守恒使主要径向通量具有内禀双极性；径向电场不能仅靠这一最低阶条件唯一确定。普通非轴对称仿星器的离子与电子通量对 $E_r$ 的响应不同，双极条件往往参与确定 $E_r$，甚至可能有多个根。[Fitzpatrick：Neoclassical Transport，式 (2.271) 附近的对比](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node41.html)。

瞬态极化电流、外加非轴对称场及动量源会补充上述平衡。所谓电子根或离子根是特定输运问题的解，不能仅从电场正负判定全部稳定性；必须检查根的稳定性、剖面与诊断。

## 湍流、漂移波与回旋动理学

背景密度和温度梯度储存自由能。离子温度梯度模（ITG）、俘获电子模（TEM）、电子温度梯度模（ETG）等可在不同尺度和碰撞性下驱动涨落；电磁条件下还需考虑磁扰动产生的输运。模式名称并不代表整个放电只有一种不稳定性，线性增长率也不能直接替代饱和热通量。

以静电、局域直磁场 $\mathbf B=B\hat{\mathbf z}$ 为例，涨落漂移的径向分量为 $\widetilde v_x=-\partial_y\widetilde\phi/B$，湍流粒子通量是 $\Gamma_x^{\rm turb}=\langle\widetilde n\,\widetilde v_x\rangle$。取人工谐波 $\widetilde n=N\cos ky$、$\widetilde\phi=\Phi\cos(ky+\delta)$，在一个波长平均可得

$$
\Gamma_x^{\rm turb}=\frac{Nk\Phi}{2B}\sin\delta.
$$

所以只有密度涨落幅值不能确定输运，密度与电势之间的相位同样关键。该算式只检验符号、相关性和平均，不是湍流饱和预测。

回旋动理学通过对快速回旋相位平均，在 $\omega/\Omega_i\ll1$、$\rho_i/L\ll1$ 等排序下保留有限回旋半径与波粒共振。它通常把六维相空间降为五维，但仍须选择局域/全局、静电/电磁、碰撞及边界模型。[Abel 等：Multiscale Gyrokinetics，2013 v4，Introduction 的排序与回旋平均](https://arxiv.org/pdf/1209.4782)。接近鞘层、回旋频率或轨道尺度与背景相当时不能机械套用核心排序。[Fitzpatrick：Perpendicular Closure Scheme，微不稳定性与各向异性尺度](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node42.html)；[Wilson：输运与多尺度反馈讨论，§3](https://scientific-publications.ukaea.uk/wp-content/uploads/rsta.2017.0435.pdf)。

剪切 $E\times B$ 流和带状流可能削弱相关涡结构，但输运、流和梯度相互反馈。数值研究应报告网格、盒子大小、统计时间、守恒与噪声收敛，再与热通量或涨落谱比较；详见[仿真计算](../../仿真计算/README.md)。

## H 模、台基与边缘局域模

H 模的关键特征是边缘输运屏障及其形成的陡峭密度/温度梯度，核心压力可在台基顶上继续增长。台基高度、宽度和梯度是不同量：若近似线性，$\Delta p\simeq\lvert dp/dr\rvert\Delta r$；相同高度可来自不同宽度与梯度，稳定性未必相同。

L–H 转换阈值与跨分离面功率、密度、磁场、离子种类、几何和壁条件有关。总加热器额定功率不能直接替代跨分离面功率，因为核心辐射和储能变化会消耗部分预算。H 模也不表示湍流处处消失，或一定适合持续运行。

Type-I 边缘局域模（ELM）的 peeling–ballooning 图像把边缘电流与压强梯度驱动联系起来；并非所有 ELM 类型都能由同一极限解释。相关稳定性计算依赖完整平衡、自举电流和边界形状；台基预测还需输运约束。[Snyder：ITER School 2015，peeling–ballooning 稳定性与 EPED 台基课程](https://www.iter.org/sites/default/files/education/snyder_iterschool15_r3.pdf)。

ELM 瞬态损失能量 $\Delta W_{\rm ELM}$、频率 $f_{\rm ELM}$ 与平均功率约 $f_{\rm ELM}\Delta W_{\rm ELM}$ 不足以确定靶板峰值温升；还要知道沉积时间、空间分布和材料热扩散。抑制或缓解 ELM 应同时检查约束、粒子排出和杂质积累，不能只追求信号上“没有尖峰”。[腔体材料](../../腔体材料/README.md)进一步区分稳态热流与瞬态损伤。

## 刮削层、平行导热与两点模型

最后闭合磁面外侧的刮削层（SOL）中，磁力线通常连接材料表面。粒子与热先从核心横向进入 SOL，再沿磁场快速流向偏滤器或限器；磁通膨胀和倾斜入射使上游通量与靶板面热流不同。不能把整个排出功率直接除以真空室总面积来预测局部峰值。

在稳态、截面积恒定、无沿途源损失、电子导热主导且局域碰撞闭合适用的简化磁力管内，令 $s$ 从上游指向靶板，

$$
q_\parallel=-\kappa_0\Theta_e^{5/2}\frac{d\Theta_e}{ds},
\qquad
\Theta_u^{7/2}-\Theta_t^{7/2}
=\frac{7q_\parallel L_\parallel}{2\kappa_0}.
$$

第二式直接由第一式积分得到。此处温度能量用 J，因此 $\kappa_0$ 的单位为 $\mathrm{W\,m^{-1}\,J^{-7/2}}$；若输入 eV 或 K，系数必须转换。这个教学式保留温度依赖，尚未包含靶端鞘层条件、压力平衡、对流、辐射、离化、磁通膨胀与动量损失，不能单独预测脱靶。[MIT PSFC：Yunxing Ma 2012 学位论文，附录 C 式 (C.9)–(C.10)](https://library.psfc.mit.edu/catalog/reports/2010/12rr/12rr008/12rr008_full.pdf)。

一个无量纲积分检查是取 $\kappa_0=q_\parallel=L_\parallel=1$、$\Theta_t=1$，则 $\Theta_u=(9/2)^{2/7}$。代回沿程剖面应得到处处相同的导热通量，而不仅是端点温差正确。这些数值不带装置单位，仅验证积分关系。

低碰撞性下自由程可能与梯度尺度相当，局域 Spitzer–Härm 热流会失效；需要动理学或经验证的非局域闭合。横向间歇丝状结构也会使单一平均宽度掩盖壁面尾部负荷。因此边界计算须结合平行和横向通道及可测量量，而不能只用一条导热曲线。

## 鞘层、预鞘与 Bohm 判据

电子通常比离子更快到达吸收壁面，浮动壁会调整电势以使净电流为零。靠近壁面的薄鞘层容许显著电荷分离，核心的准中性近似在这里失效；连接核心与鞘层的预鞘则可在近似准中性下加速离子。

对一维、稳态、无碰撞、冷单价离子和 Boltzmann 电子，令鞘入口离子速度为 $u_s$。线性展开离子能量守恒与电子密度响应，并要求形成单调离子鞘，可得

$$
u_s\ge c_s,\qquad c_s=\sqrt{\Theta_e/m_i}.
$$

这是该模型的 Bohm 判据。温离子、多离子、非 Maxwellian 电子、碰撞鞘层或强二次电子发射需要相应推广，不能只把所有温度机械相加。[MIT OCW 16.55，Lecture 17，式 (12)–(14)](https://ocw.mit.edu/courses/16-55-ionized-gases-fall-2014/69c9b98ec3496da071f8cdd7a1486ff7_MIT16_55F14_Lecture17.pdf)。

在同样假设下，另取入口速度恰为 $u_s=c_s$；若入口电子密度为 $n_s$，无势垒时单向 Maxwellian 电子通量为 $n_s\sqrt{\Theta_e/(2\pi m_e)}$。令壁面电势 $\phi_w<\phi_s$，电子通量被因子 $\exp[e(\phi_w-\phi_s)/\Theta_e]$ 抑制；与 $n_sc_s$ 相等给出

$$
\phi_s-\phi_w=\frac{\Theta_e}{2e}\ln\frac{m_i}{2\pi m_e}.
$$

对氘、$\Theta_e=10\,\mathrm{eV}$，算得 $c_s\simeq2.19\times10^4\,\mathrm{m\,s^{-1}}$、电势落差约 31.9 V。这是浮动平面吸收壁教学模型，不是带偏压探针或真实偏滤器的通用读数。倾斜磁场还会引入磁预鞘；射频电势整流则需时变模型，与[ICRH 射频鞘层](../../辅助加热/离子回旋加热/README.md)相接。

## 中性粒子、回收与脱靶

到达壁面的粒子可被反射、吸附或以原子/分子形式重新进入等离子体；这些回收粒子再经历电离、激发、电荷交换与分子反应。回收系数需说明计量的是原子核数、分子数还是粒子通量。电荷交换可以把离子的能量与动量转移给中性粒子，而光辐射、电离和复合改变功率及粒子预算。

脱靶通常指靶端等离子体从高温、强附着状态进入冷却并降低靶负荷的运行状态。需要同时研究功率、动量和粒子平衡：仅看到靶温度下降，不能证明离子通量已经出现 rollover（随上游条件变化先增后降），也不能证明抽排和核心性能满足要求。

可用控制体积写 $\dot N_{\rm target}=\dot N_{\rm upstream}+\dot N_{\rm ion}-\dot N_{\rm rec}-dN/dt$，这里 $N$ 是控制体积内的等离子体离子库存，target/upstream 是离子流率，ion/rec 分别为电离生成及复合移除离子的速率；各项按离子所含原子核数统一计量，旁向通量存在时还应补项。若改统计包含中性态的全部原子核库存，电离/复合只在电荷态之间转移，不能作为总核数源汇。靶离子流减少可能来自电离源功率不足、净复合、动量损失改变流动等共同作用，不宜把所有脱靶归因于单一复合过程。[Dudson 等：SD1D 的粒子、能量与动量损失研究，作者摘要](https://scientific-publications.ukaea.uk/papers/the-role-of-particle-energy-and-momentum-losses-in-1d-simulations-of-divertor-detachment/)。

分子辅助复合/解离在部分低温高密度条件中可成为重要通道。MAST-U Super-X 的原始研究结合谱学与功率/粒子预算讨论了这些过程；其具体结论必须保留装置、气体和模型条件，不可直接给所有偏滤器套同一阈值。[Verhaegh 等：MAST-U 等离子体—原子—分子相互作用研究，作者摘要](https://scientific-publications.ukaea.uk/papers/the-role-of-plasma-atom-and-molecule-interactions-on-power-particle-balance-during-detachment-on-the-mast-upgrade-super-x-divertor/)。

稳定排热还要求辐射区位置、杂质穿透、泵速与核心稀释可控。诊断上应把光谱、红外靶热流、探针、密度和辐射测量合并核算；一个亮度图像不足以独立确定电子温度或全部损失。

## 快粒子轨道、Alfvén 共振与损失

NBI、ICRH 和聚变 alpha 产生的快粒子往往不满足热背景的 Maxwell 分布。其回旋半径、轨道宽度和慢化时间可能明显大于热粒子尺度；有限轨道、磁场波纹、磁岛和磁扰动会产生再分布或损失。必须分别报告受约束快粒子能量、对热背景的沉积和到壁面的逃逸功率。

局域剪切 Alfvén 波频率近似为 $\omega\simeq k_\parallel v_A$，$v_A=B/\sqrt{\mu_0\rho}$。在环形几何中，粒子与模的共振可以通过环向运动和反弹/通行运动的谐波组合表达，例如 $\omega-n\omega_\varphi-l\omega_b=0$；整数 $n,l$ 与频率须采用同一角坐标和符号约定。这是轨道共振条件的示意，不是只要满足等式就一定发生不稳定。

净增长还要比较快粒子分布梯度提供的驱动与热背景、连续谱等阻尼。Alfvén 本征模可使快粒子重新分布，也可能使其真正越出约束边界；中子率下降或某个探测器增强需要结合能量、空间与轨道信息判断，不能直接等同于总损失比例。

ITER 2024 研究计划把 alpha 约束、快粒子模和局部第一壁负荷列为燃烧等离子体研究问题，强调现有 NBI/ICRF 实验向燃烧条件外推时分布各向异性和归一化轨道尺度不同。[ITR-24-005，§3.3.5.1](https://www.iter.org/sites/default/files/media/2024-04/itr-24-005-ok1.pdf)。这提供研究背景，不是 ITER 已完成的性能验证。快粒子模型应与[辅助加热](../../辅助加热/README.md)、中子及快离子诊断共同核验。

## 破裂、热淬灭与逃逸电子

托卡马克破裂可能使热能快速下降（热淬灭），随后电流显著衰减（电流淬灭）。两阶段可伴随复杂重叠，不能视为严格固定时间表。快速热负荷、感应涡流/晕电流产生的机械载荷、以及逃逸电子束是不同损伤通道；ELM 主要发生于边缘，不能与整个等离子体破裂混称。

简化电路中，等离子体电流衰减通过电感产生环向电场。对足够高能的电子，碰撞阻力随速度的依赖容许电场持续加速；种子来源可包括热尾和 Dreicer 扩散过程，已有逃逸电子还可通过大角散射引发雪崩。Dreicer 特征场和相对论临界场不是同一个阈值；低于前者也不代表完全没有逃逸产生。部分电离、辐射反作用及输运会改变实际阈值和演化。[Hesslow 等：Dreicer runaway generation，§1–2 的特征场、种子与部分电离讨论](https://arxiv.org/html/1910.00356v2)。

EPFL 的 TCV 研究将破裂和逃逸电子产生、输运与终止分别测量，并研究注入和磁扰动的缓解作用。[EPFL Swiss Plasma Center：TCV Disruptions and Runaway Electrons](https://www.epfl.ch/research/domains/swiss-plasma-center/tcv-disruptions-and-runaway-electrons/)。这些实验为模型提供约束，但不能把一个装置上的良性终止自动推广到所有尺寸、壁材和电流。

运行判断需要预警时延、漏报/误报、执行器响应和最终壁负荷的共同证据。数据库应保留破裂前的密度、辐射、电流与磁扰动轨迹，避免只收成功放电而形成选择偏差；具体数据质量和反馈问题见[诊断控制](../../诊断控制/README.md)及[实验运行](../../实验运行/README.md)。

[返回基础原理](../README.md) · [聚变反应与燃烧](../聚变反应与燃烧/README.md)
