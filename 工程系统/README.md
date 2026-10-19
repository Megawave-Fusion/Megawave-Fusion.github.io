# 聚变装置的配套工程

工程系统把等离子体物理转换为可供能、可移热、可维护的装置。磁体、电源、真空、冷却、燃料和屏蔽之间相互约束：一个子系统性能提高，可能增加另一个系统的负担。本页用能量、粒子与热量守恒连接各子系统的设计关系。

## 磁体与电源

### 场、储能与机械力

磁体用电流建立磁场，导体和支承同时承担电磁载荷。理想长螺线管近似 $B\simeq\mu_0n_{\rm turn}I$，其中 $n_{\rm turn}$ 为每米匝数；真实环形及三维线圈必须计算几何、回线、互感和铁磁材料。在线性、等效单回路条件下，

$$
W_m=\frac12LI^2,\qquad V=L\frac{dI}{dt}+RI.
$$

$L$ 用 H，$I$ 用 A，储能用 J，电压用 V。多线圈耦合时应改用 $W_m=\tfrac12\mathbf I^{\mathsf T}\mathbf L\mathbf I$。同样电流下，磁体电感不同，储能与停机时需要处理的能量就不同。教学例取 $L=1\,\mathrm H,I=20\,\mathrm{kA}$，得 $W_m=200\,\mathrm{MJ}$；若电流以 $1\,\mathrm{kA\,s^{-1}}$ 上升，仅感应项就需要 1 kV。稳态时电感电压趋近零，磁场储能仍由电流确定。

这些关系可从场与电路逐级得到。对长螺线管的矩形安培回路，外场近似为零，故 $B\ell=\mu_0(n_{\rm turn}\ell)I$。令回路磁通链为 $\Psi=LI$，Faraday 定律要求电源克服 $d\Psi/dt$，再加导体的 Ohm 压降，得到上式电压。输入的可逆磁功为 $dW_m=I\,d\Psi=LI\,dI$；从零电流积分便是 $LI^2/2$。多回路将磁通链写成 $\boldsymbol\Psi=\mathbf L\mathbf I$，在固定、对称电感矩阵下沿同一路径积分即得矩阵式；若线圈移动，还需在功率账中加入机械做功。

真空磁场能量密度为 $u_B=B^2/(2\mu_0)$，单位 $\mathrm{J\,m^{-3}}$，也给出磁压力的典型尺度 Pa。取 $B=10\,\mathrm T$ 得约 39.8 MPa。线圈中最大应力还取决于导体、线圈盒与支承的受力路径和几何。场强加倍使这一尺度增加四倍，说明“提高磁场、缩小装置”必须同时核算结构。ITER 的导体采用超导丝、铜与钢套管组合，是电、热、机械功能共同设计的实例。[ITER《Magnets》，导体与线圈系统说明](https://www.iter.org/machine/magnets)。

在真空线性介质中，每单位体积的建场功是 $\int_0^B H\,dB'=\int_0^B B'\,dB'/\mu_0=B^2/(2\mu_0)$。磁场作用的应力张量为 $\mathsf T_B=(\mathbf B\mathbf B-B^2\mathsf I/2)/\mu_0$：取法向垂直磁场时，法向应力幅值正是这个能量密度。代入 $10^2/[2(4\pi\times10^{-7})]=3.98\times10^7$ Pa，才得到上述磁压尺度。焦耳热同样由电功 $P=VI$ 和 $V_R=RI$ 相乘得到 $I^2R$。

### 常导、超导与失超保护

常导线圈的焦耳功率为 $I^2R$。超导材料则只在特定温度、磁场、电流密度和应变条件下维持低电阻状态，电流引线、接头、交流损耗与制冷依然消耗能量。失超指局部或整体退出超导状态，电阻出现后局部 $I^2R$ 热会继续升温。保护的物理任务是识别异常并把储能分配到设计允许的耗散路径，避免热点、绝缘过压和压力失控；保护设定由具体磁体的热、电与机械模型确定。

若教学模型中电感为 $L$、放电电阻为 $R_d$，忽略电感变化和其他电阻，有 $I(t)=I_0e^{-tR_d/L}$。增大 $R_d$ 可缩短 $L/R_d$，但初始电压 $I_0R_d$ 也增大，故快速释能与绝缘要求相互制约。这是简单电路推导，真实失超需耦合电路、传热与超导转变及局部热点发展。ITER 的低温系统还配置氦库存回收体系，用以处理失超等状态下的介质响应。[ITER《Cryogenics》，冷源、库存与分配系统](https://www.iter.org/machine/supporting-systems/cryogenics)。

电源不仅给出额定电流，还决定爬升速度、纹波、反馈带宽和故障时可控性。装置一般区分连续辅助用电和脉冲磁体、加热负荷；整流与变换环节的效率、无功、谐波及电网峰值约束要进入系统分析。ITER 的稳态配电与脉冲供电分开设计，是研究装置的具体实现；电站净输出另由全厂功率账计算。[ITER《Power supply》，两类配电系统](https://www.iter.org/machine/supporting-systems/power-supply)。

### 从电路衰减积分磁能去向

固定电感 $L$ 接到总电阻 $R$ 的理想闭合回路后，Kirchhoff 定律给出 $L\,dI/dt+RI=0$。分离变量积分得 $I=I_0e^{-t/\tau}$、$\tau=L/R$。磁能和电阻耗散分别为

$$
W_B(t)=\tfrac12LI_0^2e^{-2t/\tau},\qquad
E_R(t)=\int_0^t RI^2dt'
=\tfrac12LI_0^2(1-e^{-2t/\tau}).
$$

两项之和恒为初始磁能。教学取 $L=2.0$ H、$R=0.20$ Ω、$I_0=10$ kA，初始储能 100 MJ，时间常数 10 s，初始电压幅值 2.0 kV。10 s 后电流为 3.68 kA、磁能剩 13.5 MJ，电阻已接收 86.5 MJ。电流降为 $1/e$ 时能量已降为 $1/e^2$，这是电流时间常数与能量时间常数相差二倍的原因。此例按固定参数核对守恒；多线圈互感与随温度变化的电阻进入完整电路模型。系统范围可定位 [ITER 磁体说明的储能、超导与保护部分](https://www.iter.org/machine/magnets)。

## 真空与气体系统

真空系统先排出空气与水汽，再在放电中处理未燃燃料、氦灰和杂质。背景中性气压与等离子体压力分别计算；排气能力还需按放电气负荷核算。分子流状态下气体主要与壁面碰撞，管道导流能力会显著限制到达泵口的通量。

### 抽速、流导与压强

气体吞吐量 $Q_g$ 常用 $\mathrm{Pa\,m^3\,s^{-1}}$，抽速 $S$ 用 $\mathrm{m^3\,s^{-1}}$。等温、单一气体且抽速近似恒定时，

$$
Q_g=pS,\qquad
\frac1{S_{\rm eff}}=\frac1{S_{\rm pump}}+\frac1C,\qquad
p_{\rm steady}=\frac{Q_{\rm load}}{S_{\rm eff}}.
$$

$C$ 是泵前管道流导，单位同抽速。若泵口抽速为 $1.0\,\mathrm{m^3\,s^{-1}}$，管道流导仅 $0.20\,\mathrm{m^3\,s^{-1}}$，容器有效抽速为 $0.167\,\mathrm{m^3\,s^{-1}}$；面对 $10^{-3}\,\mathrm{Pa\,m^3\,s^{-1}}$ 气负荷，平衡压强为 $6.0\times10^{-3}\,\mathrm{Pa}$。更换更大的泵可能收益很小，应先判断是否受管道限制。气体种类、温度和流动状态改变时，流导和抽速也会变。[CERN 加速器学校讲义（Seidel）《Accelerator Vacuum》，§2 的吞吐量、抽速与串联流导](https://arxiv.org/html/2105.07675v1)。

抽速的定义是单位时间在入口压强 $p$ 下排走的气体体积，故 $Q_g=pS$。设容器、泵口压强分别为 $p_c,p_p$，在线性分子流模型中，同一吞吐量既满足 $Q_g=C(p_c-p_p)$，也满足 $Q_g=S_{\rm pump}p_p$。相加压降得 $p_c=Q_g(1/C+1/S_{\rm pump})$；再定义 $Q_g=S_{\rm eff}p_c$，便得到串联倒数式。稳态时排出量等于 $Q_{\rm load}$，最后一式随即成立。

有气体负荷时，等温容器的简化瞬态方程是

$$
V_{\rm ch}\frac{dp}{dt}=Q_{\rm load}-S_{\rm eff}p.
$$

若负荷与抽速恒定，则 $p(t)=p_\infty+(p_0-p_\infty)e^{-tS_{\rm eff}/V_{\rm ch}}$，$p_\infty=Q_{\rm load}/S_{\rm eff}$。它说明最终压强由气负荷决定，不会永远按指数下降。真实抽空还包含吸附水逐渐释放、材料扩散、微漏和温度变化，因此 $V_{\rm ch}/S_{\rm eff}$ 只是理想时间尺度。压强仪表也要注明气体校准和位置；残余气体分析测得的离子峰须考虑裂解谱及仪器响应。

低温泵通过低温表面的凝结或吸附捕集气体，其容量有限，工作与再生影响连续排气能力及燃料库存。ITER 的环室、束线和低温恒温器采用不同泵组，说明真空设计必须对应气种、气负荷和可维护性。[ITER《Vacuum system》，泵组与吸附面说明](https://www.iter.org/machine/supporting-systems/vacuum-system)。烘烤和清洁可减少放气，但材料、密封与传感器的温度能力必须一致。

### 由抽空曲线反求有效抽速

等温、固定容积 $V$ 的理想气体满足 $N=pV/(k_BT)$。将气负荷 $Q$ 与排气项 $S_{\rm eff}p$ 换成相同的 Pa·m³/s 单位，粒子守恒给出 $Vdp/dt=Q-S_{\rm eff}p$。恒定参数的解为

$$
p(t)=p_\infty+(p_0-p_\infty)e^{-t/\tau},
\qquad p_\infty=\frac Q{S_{\rm eff}},\quad
\tau=\frac V{S_{\rm eff}}.
$$

因此对 $\ln[p(t)-p_\infty]$ 作直线拟合，斜率就是 $-S_{\rm eff}/V$。教学数据取 $V=2.0$ m³、$p_0=0.100$ Pa、$p_\infty=0.001$ Pa，10 s 后测得 0.03742 Pa，可求 $\tau=10.0$ s、$S_{\rm eff}=0.200$ m³/s、$Q=2.00\times10^{-4}$ Pa·m³/s。达到 0.010 Pa 需 $10\ln11=24.0$ s。若泵口抽速为 0.500 m³/s，串联关系再给出连接流导 $C=0.333$ m³/s。曲线的指数阶段与后续表面放气阶段可按 [Seidel §2，式 (4)–(8) 和图 2 前后](https://arxiv.org/html/2105.07675v1)逐段解释。

## 冷却与低温

冷却将表面热、核热、焦耳热和设备损耗送往热汇。首先应由能量守恒区分峰值、脉冲平均与长期平均；短时过量热可以暂存在部件热容中，并在周期能量账中计入。对于单相流、进出口动能与势能变化可忽略的回路，

$$
\dot Q=\dot m(h_{\rm out}-h_{\rm in})
\simeq\dot m c_p(T_{\rm out}-T_{\rm in}).
$$

$\dot m$ 用 kg/s，焓 $h$ 用 J/kg。若移除 1 MW 热量，教学近似取水 $c_p=4.2\,\mathrm{kJ\,kg^{-1}K^{-1}}$、温升 20 K，所需质量流量约 $11.9\,\mathrm{kg\,s^{-1}}$。这给出热平衡所需流量；局部沸腾、流动分配与压降另行计算，真实工况用对应压力、温度的物性。

取稳态流体控制体，流入和流出质量相等，第一定律在无轴功时给出热收入等于流出焓流减流入焓流。定压比热定义为 $c_p=(\partial h/\partial T)_p$，所以焓差应先写为 $\int_{T_{\rm in}}^{T_{\rm out}}c_p\,dT$，恒定 $c_p$ 才化为乘积。流量代入为 $10^6/(4200\times20)=11.9$ kg/s。泵每推送体积 $dV$ 至高出 $\Delta p$ 的压力，至少做功 $\Delta p\,dV$；除以时间再除以效率，便得到下述泵耗电关系。

泵功率的尺度为 $P_{\rm pump}\simeq\Delta p\,\dot V/\eta_{\rm pump}$，其中体积流量用 $\mathrm{m^3\,s^{-1}}$。把流速无限提高会增加压降、泵功与可能的侵蚀，需同时核算换热和水力代价。温度、压力和流量共同决定冷却状态，平均出口温度正常也可能掩盖局部堵塞或热点。ITER 通过多个闭式回路与最终排热系统传递热量，实验产生的热最终排向环境，并不用于并网发电。[ITER《Cooling water》，回路及热排放链](https://www.iter.org/machine/supporting-systems/cooling-water)。

### 为什么少量低温热负荷也很昂贵

把热量从低温 $T_c$ 搬到高温 $T_h$，理想可逆制冷机的性能系数上限为 $\mathrm{COP}_{\rm Carnot}=T_c/(T_h-T_c)$，温度必须用 K。因此给定冷端热功率 $\dot Q_c$ 时，输入功率的下限为

$$
P_{\rm min}=\dot Q_c\left(\frac{T_h}{T_c}-1\right).
$$

取 $T_c=4.5\,\mathrm K,T_h=300\,\mathrm K$，每移走 1 W 冷端热负荷，理想情况下也至少需约 65.7 W 输入功率；实际不可逆过程使耗电更大。这解释了真空绝热、多层热屏蔽、支承热截断和电流引线优化为何重要。实际耗功可由各级制冷机性能计算。ITER 的多个温度级分别服务磁体、热屏蔽与低温泵，各级冷量分别换算为电输入。[ITER《Cryogenics》，温度级与冷量分配](https://www.iter.org/machine/supporting-systems/cryogenics)。

### 热平衡测量的检查方法

热量可以由冷却回路独立估计，也可以由已知电输入和设备储热估计，两者在同一时间窗内比较才有意义。瞬态控制体满足 $P_{\rm in}-P_{\rm out}=dU/dt$；当部件还在升温时，忽略右端会误把储热当作未测到的损失。周期运行时，在完整周期内比较 $\int P\,dt$，通常比只取峰值时刻更容易闭合能量账。

传感器误差也会进入热功率。对于 $\dot Q=\dot m c_p\Delta T$，若三项误差独立且较小，标准不确定度近似满足 $u_r(\dot Q)^2=u_r(\dot m)^2+u_r(c_p)^2+[u(\Delta T)/\Delta T]^2$。教学例中流量、比热和温差的相对标准不确定度分别为 2%、1%、3%，则热功率为约 3.7%，报告精度随不确定度确定。进出口温度的共同校准误差可能相关，传播式中需保留协方差项。这个传播式来自一阶微分，不包含模型偏差。

具体做法是先对乘积取一阶扰动：$\delta\dot Q/\dot Q=\delta\dot m/\dot m+\delta c_p/c_p+\delta(\Delta T)/\Delta T$。对该式平方后取方差，独立输入的交叉协方差为零，剩下三个方差之和；本例为 $\sqrt{0.02^2+0.01^2+0.03^2}=0.0374$。若温差由两支传感器相减，先用 $u^2(\Delta T)=u^2(T_{\rm out})+u^2(T_{\rm in})-2\operatorname{Cov}(T_{\rm out},T_{\rm in})$ 计算，再进入乘积传播。

### 多温度级冷量的最低耗功

可逆制冷循环从冷端移走热量 $\dot Q_c$ 并向热端排出 $\dot Q_h$。熵平衡给出 $\dot Q_c/T_c=\dot Q_h/T_h$，能量平衡给出 $P=\dot Q_h-\dot Q_c$，两式联立得到 $P_{\min}=\dot Q_c(T_h/T_c-1)$。多个冷端温度级分别计算后再相加：

$$
P_{\min,\rm total}=\sum_j\dot Q_j\left(\frac{T_h}{T_j}-1\right).
$$

教学取热端 300 K，4.5 K 级热负荷 100 W、80 K 级 1000 W。前者最低耗功 6.57 kW，后者 2.75 kW，合计 9.32 kW。虽然 80 K 级移走的热量更多，4.5 K 级却更耗功。这也说明热截断的意义：若支承结构传来的 100 W 热量改在 80 K 级截获，对应的可逆最低耗功从 6.57 kW 降为 0.275 kW。实际系统在各温度级具有不同的不可逆损失和设备效率，能量清单以逐级热负荷为输入。[ITER《Cryogenics》的不同温度级和服务对象](https://www.iter.org/machine/supporting-systems/cryogenics)可作为阅读大型系统冷量分配的实例。

## 燃料、注入与循环

D–T 燃料循环包括供给等离子体、回收未反应燃料、分离氦与杂质、同位素处理、再供给和库存测量。气体注入首先影响边缘中性粒子；丸注入通过固态燃料进入更深区域后消融，有助于改变粒子沉积剖面，但仍取决于丸与等离子体条件。核心密度由粒子平衡决定，其中壁面再循环、抽气与粒子输运同时存在。[ITER《Fuelling》，燃料注入与回收系统](https://www.iter.org/machine/supporting-systems/fuelling)。

### 燃烧消耗与循环流量

每次 D–T 反应消耗一个氚核。[LLNL 诊断说明，One Key Measurement 段](https://lmf.llnl.gov/news/diagnostics-were-crucial-to-llnls-historic-ignition-shot)给出每次反应约 17.6 MeV 总能量及以中子数推断反应次数的原理。把每次反应能取为 $E_{DT}\simeq17.6\,\mathrm{MeV}=2.82\times10^{-12}\,\mathrm J$，仅由能量与粒子守恒可得

$$
\dot N_{\rm burn}=\frac{P_{\rm fusion}}{E_{DT}},\qquad
\dot m_T=m_T\dot N_{\rm burn}.
$$

这里 $P_{\rm fusion}$ 表示聚变热功率。假想连续 1 GW D–T 聚变热功率对应约 $3.55\times10^{20}$ 次反应/s，按 $m_T\simeq5.01\times10^{-27}\,\mathrm{kg}$ 估算，氚燃烧约 $1.78\,\mathrm{mg\,s^{-1}}$，365 天满功率约 56 kg。若可用率较低，年度燃烧量按实际聚变热功率时序积分；循环库存另按流量与停留时间核算。

燃烧比例 $f_b$ 若按氚核数定义为所注入氚中被反应消耗的比例，则理想稳态氚注入率尺度为 $\dot N_{T,\rm inj}=\dot N_{\rm burn}/f_b$；这里每次 D–T 反应消耗一个氚核，所以氚燃烧率等于上式的反应次数率。若改用 D 与 T 的总核数，分子与分母都须采用同一计数口径。未燃部分回收再循环，所以低单程燃烧比例显著增大处理流量，新氚需求由燃烧和实际损失决定。必须严格区分注入、循环、外部补给与实际燃烧四种流量。

### 增殖、延迟与库存

常见增殖反应之一是 ${}^{6}\mathrm{Li}+n\rightarrow{}^{4}\mathrm{He}+T$。增殖比 TBR 定义为生成氚核数与消耗氚核数之比，但“生成”还需经提取和回收才成为可用燃料。损失、处理延迟、备用库存和新机启动要求，共同决定燃料自持所需的 TBR 裕量。ITER 测试包层模块旨在检验相关技术，用于研究后续燃料闭环所需的功能。[ITER《Tritium breeding》，TBM 试验目标与后续研究边界](https://www.iter.org/machine/supporting-systems/tritium-breeding)。

对包含所指定回收与储存系统的库存边界，质量守恒可写成

$$
\frac{dM_T}{dt}=\dot M_{\rm bred,rec}+\dot M_{\rm external}
-\dot M_{\rm burn}-\dot M_{\rm loss}-\lambda_T M_T.
$$

边界内部的搬运不应重复记为净收入。$\lambda_T=\ln2/t_{1/2}$，NIST 2000 年评估推荐半衰期 $4500\pm8$ 天，约 12.32 年；按这一值，隔离库存一年衰变约 5.5%。这一衰变项与实测流入、流出和材料滞留共同进入库存账。[Lucas 与 Unterweger，NIST，2000，摘要与推荐值](https://nvlpubs.nist.gov/nistpubs/jres/105/4/j54luc2.pdf)。材料滞留与渗透会使测量边界复杂化，见[等离子体与材料相互作用](../腔体材料/README.md)。

衰变项来自每个氚核单位时间相同的衰变概率：隔离库存满足 $dM_T/dt=-\lambda_TM_T$，积分为 $M_T(t)=M_T(0)e^{-\lambda_Tt}$。令 $M_T(t_{1/2})=M_T(0)/2$ 即得半衰期关系；一年损失份额为 $1-2^{-365/4500}=0.0547$。稳态环节的“流量×停留时间”也可由库存积分推出：若年龄为 $a$ 的粒子仍在环节内的概率为 $S(a)$，则恒定入口流量下 $M=\dot m_{\rm in}\int_0^\infty S(a)da=\dot m_{\rm in}\overline\tau$，其中 $\overline\tau$ 是平均停留时间。

### 单程燃烧率怎样决定循环流与处理库存

以氚质量为统一口径，设燃烧率 $\dot m_b$、单程燃烧比例 $f_b$，则注入率 $\dot m_{\rm inj}=\dot m_b/f_b$，未燃流为 $(1-f_b)\dot m_{\rm inj}$。若其回收率为 $\eta_r$，回流率为 $\dot m_r=\eta_r(1-f_b)\dot m_{\rm inj}$，稳态补充率由入口守恒给出

$$
\dot m_{\rm fresh}=\dot m_{\rm inj}-\dot m_r
=\dot m_b+(1-\eta_r)(1-f_b)\dot m_{\rm inj}.
$$

教学取 $\dot m_b=0.10$ mg/s、$f_b=0.020$、$\eta_r=0.999$，注入、未燃、回收分别为 5.00、4.90、4.8951 mg/s，补充量为 0.1049 mg/s。若所有注入燃料在一个处理环节平均停留 30 s，该环节的稳态在制库存按“流量×平均停留时间”为 150 mg。库存核算随后可加入滞留、衰变和增殖返回延迟。这个算例说明提升单程燃烧率会首先降低循环处理量和在制库存；补充量由实际燃烧与损失相加确定。[ITER《Fuelling》的 Fuel cycle 与 Tritium Plant 段](https://www.iter.org/machine/supporting-systems/fuelling)介绍相应系统边界。

## 屏蔽、维护与运行保障

屏蔽设计要根据中子与光子能谱、空间分布、开孔和散射计算，保护人员、磁体、电子学与结构的要求并不相同。对单能、窄束且忽略散射补入的理想模型，未碰撞通量满足 $\phi(x)=\phi_0e^{-\Sigma_t x}$，其中宏观截面 $\Sigma_t$ 用 $\mathrm{m^{-1}}$。聚变装置的真实屏蔽存在慢化、次级伽马、散射和端口贯穿，屏蔽厚度由包含这些过程的输运模型确定。

这一指数由薄层的碰撞计数得到：厚度 $dx$ 中发生一次相互作用的概率为 $\Sigma_tdx$，因此未碰撞束减少 $d\phi=-\Sigma_t\phi\,dx$。恒定截面下分离变量积分给出上述解；对混合材料，$\Sigma_t=\sum_jn_j\sigma_{t,j}$ 由各核素的靶数密度乘总微观截面相加。这一推导只跟踪未碰撞束，散射后的粒子需另列输运源项。

停堆后即时中子源消失，活化材料仍可能产生辐射；接近部件的时间需按活化与衰减计算。维护规划需要将部件寿命、冷却时间、转运、热室空间与可拆卸接口纳入一开始的布局。ITER 计划通过遥操作处理包层、偏滤器、束线及部件转运，说明机器人可达性和故障恢复本身就是装置功能的一部分。[ITER《Remote handling》，系统范围与维护条件](https://www.iter.org/machine/supporting-systems/remote-handling)。

### 从聚变热到净电力

热功率、发电机输出与电网净输出是不同量。定义系统边界后，可写

$$
P_{\rm net}=\eta_{\rm th}P_{\rm th,useful}
-P_{\rm heat,elec}-P_{\rm cryo}-P_{\rm pumps}-P_{\rm other}.
$$

$\eta_{\rm th}$ 是热到电效率，所有功率单位一致；辅助加热的电输入与等离子体吸收功率之间还隔着转换和传输损失。热回收若已经包含某项设备损耗，就在清单中标明已计入的归属。教学例取可用热功率 1000 MW、热效率 40%、厂用电合计 150 MW，得到净输出 250 MW；即使等离子体增益提高，仍须验证这条能量链和设备可用率。

对于只在运行时产生上述净输出、停机能耗暂忽略的示例，若年可用率为 70%，年净电量约 $250\times0.70\times8760=1.53\times10^6\,\mathrm{MWh}$。现实停机时也可能保留低温和维护用电，故要对全年时间序列积分。ITER 的冷却水资料明确其热量排向环境；其科学目标与电站净电目标按各自边界定义。[ITER《Cooling water》，排热路径](https://www.iter.org/machine/supporting-systems/cooling-water)。

工程可靠性因此与物理增益同样重要：一项易损部件若更换周期长，会影响整厂输出；保护动作若能避免严重损坏，可能提高长期可用率。每项控制、保护与验收要求必须能追溯到具体项目分析和试验，基本守恒关系为跨系统核对提供共同依据。

系统联调时，守恒量是跨接口核查的重要工具。例如真空泵排出的粒子数、燃料系统的供给量、壁面库存变化和等离子体粒子变化，应在定义清楚的边界内相容；回收流在总边界内按内部转移记账。热接口应标明热量在哪个温度级被排出，电接口应标明额定功率、脉冲功率与能量，机械接口则要说明载荷方向和作用时间。只有这些口径一致，子系统各自通过试验才可能组成整体可用的装置，并继续检查瞬态联合响应。

### 维护周期怎样进入全年净电量

设一个重复运行周期包含发电时间 $t_{\rm on}$ 和维护时间 $t_{\rm off}$，运行时净电输出 $P_{\rm on}$，停机时消耗 $P_{\rm idle}$。先对周期功率积分，再除以周期长度，得到

$$
\overline P=\frac{P_{\rm on}t_{\rm on}-P_{\rm idle}t_{\rm off}}
{t_{\rm on}+t_{\rm off}}
=A P_{\rm on}-(1-A)P_{\rm idle},
\quad A=\frac{t_{\rm on}}{t_{\rm on}+t_{\rm off}}.
$$

教学取运行 120 天、维护 30 天、运行净输出 250 MW、停机用电 20 MW，则 $A=0.80$，长期平均净输出为 196 MW，按 365 天折算约 171.7 万 MWh。若遥操作和部件接口改进使维护时间缩短为 15 天，则 $A=8/9$，平均净输出提高到 220 MW，同年长增加约 21.0 万 MWh。这里按周期平均折算，真实年度账本可逐日积分。由此能把一次部件更换的工期与全厂能量收益直接联系起来。[ITER《Remote handling》的维护系统与部件转运范围](https://www.iter.org/machine/supporting-systems/remote-handling)有助于确定哪些工序决定停机时间。

## 工程规格的单位与边界核对

- [ITER 配套系统](https://www.iter.org/machine/supporting-systems)：各系统官方入口。
- [ITER 磁体](https://www.iter.org/machine/magnets)、[电源](https://www.iter.org/machine/supporting-systems/power-supply)、[低温](https://www.iter.org/machine/supporting-systems/cryogenics)：装置级系统边界。
- [CERN 加速器学校讲义（Seidel）：Accelerator Vacuum，2021，§2](https://arxiv.org/html/2105.07675v1)：真空量、气负荷、抽速和流导。
- [ITER 燃料系统](https://www.iter.org/machine/supporting-systems/fuelling)与[氚增殖](https://www.iter.org/machine/supporting-systems/tritium-breeding)：公开燃料循环原理和试验边界。
- [NIST：氚半衰期评估，2000](https://nvlpubs.nist.gov/nistpubs/jres/105/4/j54luc2.pdf)：推荐值及标准不确定度。

### 沿单位链阅读一份真空规格

阅读 [Seidel《Accelerator Vacuum》§2 的气负荷、抽速和流导定义](https://arxiv.org/html/2105.07675v1)时，可以给一条规格做完整换算。假设文档记录某气体负荷为 1.0 mbar·L/s：先用 $1$ mbar $=100$ Pa、$1$ L $=10^{-3}$ m³，得到 $Q=0.100$ Pa·m³/s。若气体温度为 300 K，再由理想气体关系求分子率，

$$
\dot N=\frac{Q}{k_BT}
=2.41\times10^{19}\ {\rm s^{-1}}.
$$

最后读取物种栏：若对象为双原子分子，对应原子核率是分子率的两倍。这样一张阅读卡便包含原始单位、SI 值、温度、分子/原子口径以及所用公式。接着查看泵的抽速究竟在哪种气体和入口压强下标定，将同一气负荷除以有效抽速，才进入腔体压强计算。把规格中的每一次单位转换写出来，可以让真空、燃料与粒子平衡三组人员使用同一组输入。系统构成可继续参阅 [ITER Vacuum system](https://www.iter.org/machine/supporting-systems/vacuum-system)。

[腔体材料](../腔体材料/README.md) · [返回知识库](../README.md)
