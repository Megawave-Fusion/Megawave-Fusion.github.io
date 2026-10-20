# 中性束注入（NBI / NBCD）

中性束先用电场把离子加速，再转为不带电的高速原子，使其穿过约束磁场进入等离子体。原子在等离子体内电离后成为快离子，随后贡献加热、粒子、动量与电流源。本页依据公开机构资料与 IAEA 教材补充，核验日期 2026-10-16，按束线、轨道和慢化三个环节组织。 对应计算流程见[模拟专题](../../仿真计算/中性束注入模拟/README.md)。

## 束停止、快离子慢化与电流

### 为什么先加速、再中性化

电场能有效加速带电粒子，却不能直接给中性原子提供相同的定向加速。若直接向强磁场注入低刚度离子束，洛伦兹力会使轨道偏转。因此束线把源、抽取加速、中性化、残余离子分离按功能串联。正离子中性化主要需要俘获电子；负离子只需剥离多余电子。高束能时两者截面不同，使负离子路线更适合 MeV 级氢同位素束，但负离子的产生和输运更困难。[IPP：中性束基本原理](https://www.ipp.mpg.de/3668214/nbi_principle)

沿静电加速区积分单粒子做功 $\Delta E=q\int\mathbf E\cdot d\mathbf l$，单电荷离子经过加速电压 V 得到 $E_b\simeq eV$，其中能量以 J 表示、电压以 V 表示；若以 eV 计能量，数值等于加速电压数值。每秒离子数是 $I_{acc}/e$，乘单粒子能量便得 $P_{acc}=I_{acc}V$。该式给加速束功率；中性化和束线损耗随后扣除。分子正离子若含 j 个近似等质量原子核，以共同速度解离后每个原子分得约 $E_b/j$，从而出现半能、三分之一能组分；各自沉积和穿透深度需分别求取。[TRANSP：束能组分输入](https://transp.pppl.gov/nml/beams.html)，[KSTAR 束线调试原论文，图 9 及其说明](https://www-pub.iaea.org/mtcd/meetings/PDFplus/2010/cn180/cn180_papers/ftp_p6-16.pdf)

### 电离、轨道与慢化是三个环节

设 $\Gamma_b(s)$ 为沿束路的中性粒子通量，单位 $\mathrm{m^{-2}s^{-1}}$，则忽略束散射几何变化的单束模型为

$$
\frac{d\Gamma_b}{ds}=-\kappa(s)\Gamma_b,\qquad
\Gamma_b(s)=\Gamma_b(0)\exp\left[-\int_0^s\kappa(s')ds'\right].
$$


$\kappa$ 是综合有效停止系数，单位 $\mathrm{m^{-1}}$；简单近似为 $\sum_j n_j\sigma_j$，$n_j$ 与 $\sigma_j$ 分别为 $\mathrm{m^{-3}}$、$\mathrm{m^2}$，对热靶粒子应先正确平均相对速度。高能束还需考虑多步激发—电离，截面按束能、密度及电子状态选取。未被停止的中性束称为 shine-through，会直接加热对面的壁；已电离却因大轨道而损失的快离子则是另一种损失。[IAEA 教材，§5.1.3、式 (5.6) 及图 5.6](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)

快离子从出生位置沿轨道继续输运并传能。它在磁场中运动、碰撞减速并发生俯仰角散射；电荷交换、磁场纹波及不稳定性还可能将其移出约束区。经典模型适用于相关扰动不强且碰撞描述有效的工况，有明显 Alfvén 活动时必须检验异常输运。[IAEA 教材，§2.5.2.1](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)

### 能量到底交给电子还是离子

在 $v_{ti}\ll v_b\ll v_{te}$、背景近 Maxwell 分布的经典近似中，可写

$$
-\frac{dE}{dt}=\frac{2E}{\tau_{se}}\left[1+\left(\frac{E_c}{E}\right)^{3/2}\right].
$$


$E,E_c$ 为 J，$\tau_{se}$ 为 s；$E_c$ 是电子与离子能量损失率相等的临界能量。第一项是电子通道，第二项是离子通道。束能高于 $E_c$ 时瞬时电子加热较强，慢化到低于 $E_c$ 后离子通道增强。瞬时离子份额为 $[1+(E/E_c)^{3/2}]^{-1}$，而从初始能量慢化到热能的**累计**份额还要沿能量积分，二者分别描述当前功率与完整慢化路径。例如 $E=2E_c$ 时瞬时离子份额约 26.1%，累计比例则依能量积分确定。[IAEA 教材，§5.1.4、式 (5.8)–(5.13)](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)

定向快离子形成电流，电子碰撞响应又形成部分抵消的回流，净 NBCD 由快离子电流与电子回流共同给出。俯仰角、捕获粒子、有效电荷和沉积位置均会影响净电流。切向束还注入环向动量：单能非相对论束的粒子率为 $\dot N=P_b/E_b$，单粒子动量为 $p_b=\sqrt{2m_bE_b}$，两者相乘得 $\dot p=P_b\sqrt{2m_b/E_b}$，单位 N。因此同一功率下提高束能会降低注入动量；环向转矩还需乘方向投影和力臂。[Fitzpatrick：等离子体旋转](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node89.html)，[IAEA 教材，§5.1.7–§5.1.8](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)

### 分段密度剖面中的束沉积

在给定能量的单束线上，令有效停止系数为 $\kappa(s)=n_e(s)\sigma_{stop}(s)$。由 $dP/ds=-\kappa P$，分离变量积分得 $P(s)=P_0\exp[-\int_0^s\kappa dl]$。第 j 区域的沉积为入口与出口功率之差，因此逐区计算既能给出沉积剖面，也能在末端得到直穿功率。

设入射 10 MW，两个区域长度各 0.5 m，停止系数依次为 1 和 3 m⁻¹。第一段出口为 $10e^{-0.5}=6.0653$ MW，第一段快离子出生功率为 3.9347 MW；第二段出口为 $10e^{-2}=1.3534$ MW，第二段出生功率为 4.7119 MW。两段出生功率和末端直穿相加恰为 10 MW。这里将全部停止视为电离并先固定有效截面；“出生功率”仍会在轨道损失、快离子储能和热化之间分流。将真实密度、温度、束能量和激发态数据放回 $\sigma_{stop}$ 后，再以电离位置为快离子轨道初始条件。

推导起点与参考位置：[IAEA Fusion Physics，§5.1.2–5.1.4，书页 535–545；§5.2.1，书页 571–573](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)。

## 离子源、中性化器与束线接口

离子源产生可抽取的离子；栅极系统决定束流电流密度、聚焦与发散；中性化器提供合适靶气柱密度；残余离子偏转或静电分离系统把未中性化组分送入专门收集器；束流管将中性束送入主机。低温泵限制气体引起的再电离和束损失，量热靶在调试时接收束功率。负离子源还有共抽电子热负荷以及负离子过早剥离的问题。[ITER：中性束试验设施](https://www.iter.org/project/iter-neutral-beam-test-facility)

束光学、高压、真空和热结构共同约束运行点。气压同时影响中性化、再电离与抽气；长束路上的束晕会形成壁热负荷，需在核心束宽之外保留尾部。

ITER 的 SPIDER 用于源的研发，MITICA 用于全尺寸束线原型验证。官方页面所列每束 16.5 MW、氘粒子能量 1 MeV、最长 3600 s 是系统需求/设计能力语境，其验证过程分别涵盖离子源、加速器和全束线。[ITER NBTF 的任务与两套试验台说明](https://www.iter.org/project/iter-neutral-beam-test-facility)

### 两电荷态中性化器的最小模型

把气体柱密度记为 $N_g=\int n_gdl$（m⁻²），考虑正离子与中性原子两态。若离子俘获电子截面为 $\sigma_{10}$，中性原子再电离截面为 $\sigma_{01}$，则 $dF_0/dN_g=\sigma_{10}(1-F_0)-\sigma_{01}F_0$。初始全为离子，积分得到 $F_0=\sigma_{10}[1-e^{-(\sigma_{10}+\sigma_{01})N_g}]/(\sigma_{10}+\sigma_{01})$；气体厚度增大后趋向两过程平衡的份额。

给定教学截面 $\sigma_{10}=2\times10^{-20}$ m²、$\sigma_{01}=10^{-20}$ m²、柱密度 $5\times10^{19}$ m⁻²，指数为 −1.5，中性份额为 0.51791。柱密度加倍时增至 0.63348，极厚极限为 2/3。这样可清楚看出增加气体的边际收益逐渐降低，同时束线抽气负担继续增加。该两态方程适用于所设正离子模型；负离子束需把负、零、正三种电荷态的转移联立，并考虑电子剥离和再电离各自的能量依赖。

推导起点与参考位置：[IAEA Fusion Physics，§5.1.2–5.1.4，书页 535–545；§5.2.1，书页 571–573](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)；[ITER Neutral Beam Test Facility，SPIDER/MITICA 与束线任务](https://www.iter.org/project/iter-neutral-beam-test-facility)。

## 束轨道与电子离子传能计算

对非相对论氘原子，$v_b=\sqrt{2E_b/m_D}$；100 keV 时约 $3.10\times10^6\,\mathrm{m\,s^{-1}}$，1 MeV 时约 $9.79\times10^6\,\mathrm{m\,s^{-1}}$。采用 $m_D\simeq3.344\times10^{-27}$ kg 的教学算例显示速度随能量平方根增长，能量提高十倍并不使速度提高十倍。

若一条理想均匀束路的积分光学厚度 $\tau_b=\int\kappa ds=2$，直穿份额为 $e^{-2}\simeq13.5\%$。允许的直穿负荷取决于壁面材料、束斑、脉宽和冷却，且需要对每个束能组分及每条束线射线积分。把固定平均密度代入整条束路，会漏掉边缘空洞、束切向半径和等离子体位移的影响。

计算链：源/中性化 → 束线传输 → 三维出生源 → 轨道/碰撞 → 热、粒子、动量和电流源。统一坐标、单位和时刻，并对标记数、时间步及能量预算分别收敛。 [IAEA 教材，§2.5.2.1 的模型比较](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)。

束停止源项还需要和快离子储能区分。对于一个控制体，可写

$$
\frac{dW_f}{dt}=P_{birth}-P_{fe}-P_{fi}-P_{loss}.
$$


其中 $W_f$ 为 J，各功率为 W。束刚开启时一部分能量积累在快离子群，故电子与离子加热之和可以暂时小于被电离的束功率；关束后快离子仍会继续慢化加热。若用稳态功率平衡解释开启/关闭瞬间，就可能把储能变化误判成异常损失。[IAEA 教材，§5.1.4 的慢化过程](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)

动量率 $\dot p$ 先沿束方向定义，再投影并乘力臂得到环向转矩。转速由源、输运和阻尼共同决定；改变注入方向或切向半径后须重算轨道约束。 [Fitzpatrick 的中性束旋转讨论](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node89.html)。

输入束组分时还要辨别粒子数份额、电流份额和功率份额。半能量粒子在相同粒子数下只携带一半能量，三类份额通过各组分能量和电荷换算。[TRANSP 的 FFULL/FHALF 定义](https://transp.pppl.gov/nml/beams.html)

### 把瞬时慢化分流积成累计离子加热

经典拖曳近似先写 $dv/dt=-(v/\tau_{se})[1+(v_c/v)^3]$。用 $E=mv^2/2$ 与 $dE/dt=mv\,dv/dt$，得到本页慢化方程的 $2E/\tau_{se}$ 因子，且 $E_c=mv_c^2/2$。慢化方程给离子所占瞬时份额 $f_i(E)=1/[1+(E/E_c)^{3/2}]$。粒子能量减少正量 $-dE$ 时，交给离子的能量为 $dE_i=f_i(E)(-dE)$。因此从 $E_0$ 降到 $E_f$ 的累计份额为 $F_i=\int_{E_f}^{E_0}f_i(E)dE/(E_0-E_f)$；令 $x=E/E_c$，便化为无量纲的一维定积分，电子份额由 $1-F_i$ 给出。

取 $E_c=100$ keV、$E_0=200$ keV、$E_f=10$ keV，积分区间为 0.1 至 2。数值积分给 $F_i\simeq0.53163$，即释放的 190 keV 中约 101.01 keV 给离子、88.99 keV 给电子。相比之下，起始时刻离子份额仅为 $1/(1+2^{3/2})=26.12\%$；随着粒子降能，离子通道逐渐增强。这里选择的终点和全部轨道段应落在所用经典慢化排序内。用时间步进直接分别积分电子、离子损失，可独立检查累计能量是否回到 190 keV。

![累计离子分流需沿整个慢化路径积分，不能用起始瞬时比例替代。](/assets/diagrams/heat-nbi.svg)

累计离子分流需沿整个慢化路径积分，不能用起始瞬时比例替代。

推导起点与参考位置：[IAEA Fusion Physics，§5.1.2–5.1.4，书页 535–545；§5.2.1，书页 571–573](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)。

## 直穿热负荷与注入许可

加速高压必须在源、真空、冷却和束线准备好后投入。击穿会改变电流路径和部件能量沉积，需由电源与保护装置限定故障能量；束流错位则可能在允许总功率下造成局部过热。主机端的密度、等离子体位置和束挡板状态也是注入许可的一部分，因为它们改变停止概率和束的最终落点。

部件负荷以热流 $q$（W/m²）和面能量 $\int qdt$（J/m²）评估。密度许可由直穿壁载荷反求，高压延迟由故障能量确定；源停机、加速停机和主机中止需在同一时间轴记录。 [ITER：中性束电源与一小时高压需求](https://www.iter.org/project/construction-archives/neutral-beam-power-supply)。

### 直穿热负荷对密度变化的灵敏度

对相同束能、几何与有效截面，直穿功率为 $P_{sh}=P_0e^{-\tau_b}$，其中 $\tau_b=\int\kappa dl$。对数微分得 $d\ln P_{sh}=-d\tau_b$；若只改变密度尺度，$\tau_b$ 与密度成比例。把束斑面积 A 纳入便得到平均热流 $q_{sh}=P_0e^{-\tau_b}/A$，它将沿程密度扰动映射为接收表面的负荷变化。

设入射功率 10 MW、束斑面积 0.05 m²。$\tau_b=3$ 时直穿功率为 0.4979 MW，平均热流为 9.957 MW/m²；降到 $\tau_b=2$ 时变为 1.3534 MW 和 27.067 MW/m²，增加因子为 e。围绕 $\tau_b=3$ 的 ±0.1 不确定度，则对应热流乘以 $e^{\mp0.1}$。保护模型可据此把沿程密度估计、束斑位置和量热测量联合起来，并用实际束斑峰值系数把平均热流进一步转换为局部峰值。

推导起点与参考位置：[IAEA Fusion Physics，§5.1.2–5.1.4，书页 535–545；§5.2.1，书页 571–573](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)；[ITER Neutral Beam Test Facility，SPIDER/MITICA 与束线任务](https://www.iter.org/project/iter-neutral-beam-test-facility)。

## 束斑量热与快离子诊断

束电流需校正电子污染；加速电压与能谱约束束能，量热靶和发射谱约束到靶功率、束斑、组分与发散。量热反演同时计入热惯性及反射/溅射损失。

进入等离子体后，中子率、快离子 D-alpha（FIDA）、中性粒子分析和快离子损失探测各看见分布的不同投影；多种诊断共同约束快离子径向与速度分布。可采用束调制比较慢化时间与诊断响应，再同时检查电子/离子温度和转动。若需要 NBCD，必须把快离子电流、电子回流、欧姆电流与自举电流分开，并包含电流扩散。[IAEA 教材，§2.5.2.1、§5.1.6–§5.1.8](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)

束线计量、快离子分布和热响应共同闭合功率与粒子账本。

### 束斑轮廓与孔径内功率

把横截面束功率密度写为 $q(r)=P\exp[-r^2/(2\sigma_b^2)]/(2\pi\sigma_b^2)$，其中 $\sigma_b$ 是每个横向坐标的标准差。对圆形接收孔积分，得到 $P_a/P=1-e^{-a^2/(2\sigma_b^2)}$；对整个平面求二阶矩，则有 $\langle r^2\rangle=2\sigma_b^2$。总功率、束宽和截断量可以通过同一归一化模型相互检查。

教学取 P=100 kW、$\sigma_b=40$ mm、a=80 mm，得孔内 86.466 kW、孔外 13.534 kW、中心热流 9.947 MW/m²。有限量热阵列需补偿未覆盖尾部；偏心椭圆束用横向均值和协方差描述。

推导起点与参考位置：[IAEA Fusion Physics，§5.1.2–5.1.4，书页 535–545；§5.2.1，书页 571–573](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)；[TRANSP，Neutral Beam inputs，能量组分与几何输入](https://transp.pppl.gov/nml/beams.html)。

## 分子束组分怎样改变穿透、加热与转矩

正离子源中的 $\mathrm D^+$、$\mathrm D_2^+$、$\mathrm D_3^+$ 都可携带一个正电荷经过同一加速电压。分子解离前，各自得到近似相同的总动能 $E_0=eV$；忽略解离能后，含 j 个核的分子产生 j 个约为 $E_0/j$ 的原子。因此全能、半能和三分之一能是同一束线中的不同速度群，进入等离子体后有各自的停止、轨道和慢化过程。[TRANSP 的束能组分输入](https://transp.pppl.gov/nml/beams.html)与 [KSTAR 调试论文图 9](https://www-pub.iaea.org/mtcd/meetings/PDFplus/2010/cn180/cn180_papers/ftp_p6-16.pdf)提供组分定义和诊断语境。

### 从分子离子电流到中性原子功率

若加速前 j 核分子离子电流为 $I_j$，每秒分子数是 $I_j/e$，完全解离后的原子数率就是 $jI_j/e$。若该能量组分实际成为可传输中性原子的比例是 $\eta_j$，则 $\dot N_j=\eta_jjI_j/e$，相应中性功率为 $P_j=\dot N_jE_0/j=\eta_jI_jV$。这解释了为什么源端电流份额、下游原子数份额和中性功率份额需要分别给出。

当诊断已直接给中性原子总数率 $\dot N$ 及数目份额 $a_j$，则不再重复乘 j，而是

$$
P_j=\dot Na_j\frac{E_0}{j},\qquad
f_{P,j}=\frac{a_j/j}{\sum_k a_k/k}.
$$


这由“每秒原子数×每原子能量”得到，$P_j$ 用 W，两个份额都无量纲。取 $\dot N=10^{20}$ s⁻¹、$E_0=80$ keV、$a_1,a_2,a_3=0.6,0.3,0.1$，加权和为 0.78333，总中性功率为 1.0040 MW；功率份额为 76.596%、19.149%、4.255%。把原子数份额直接当作功率份额，会高估低能组分的能量贡献。

### 各能量群分别形成粒子、热与动量源

对能量群 j，束停止方程先给 $P_{sh,j}=P_j e^{-\tau_j}$，其中 $\tau_j=\int\kappa_jds$。两侧相减得到快离子出生功率 $P_{birth,j}=P_j(1-e^{-\tau_j})$；再用每粒子能量相除，出生粒子率为 $\dot N_{birth,j}=P_{birth,j}/(E_0/j)$。低能组分即使功率份额小，也可能贡献显著的粒子数率。热电子和热离子真正得到的功率，还要对每个能量群沿前述慢化路径积分，并扣除轨道损失与快离子储能变化。

动量也按组分相加。由 $p_j=\sqrt{2m_D E_0/j}$ 和 $P_j=\dot N_jE_0/j$，得到沿束方向的动量输入率

$$
\dot p_j=P_j\sqrt{\frac{2m_Dj}{E_0}}.
$$


故单位中性功率的动量按 $\sqrt j$ 增大。出生转矩逐射线乘环向方向余弦和力臂；直穿动量到壁。各组份的停止、慢化和约束不同，穿透、离子加热与转矩的最优点须分别计算。 [IAEA《Fusion Physics》§5.1.3–5.1.4 的停止与慢化、§5.1.7–5.1.8 的电流和动量讨论](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)。

[返回辅助加热](../README.md) · [编写说明](../../编写说明.md) · [返回知识库](../../README.md)
