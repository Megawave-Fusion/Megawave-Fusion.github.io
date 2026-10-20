# 面向等离子体的结构与材料

聚变部件同时承受热、粒子、中子、电磁力和启停循环。材料响应依赖温度、辐照与加工史；本页连接载荷、材料与部件设计，算例均为给定教学参数。

## 真空室与腔体结构

真空室形成低压边界，为诊断、加热、抽气与维护提供端口，并支承内部部件。第一壁位于其内部，直接面对等离子体。以 ITER 为例，双层钢制真空室还承担放射性物质的第一道约束屏障功能，壁间水和屏蔽块参与移热与屏蔽；各路线按自身载荷和维护需求确定结构。[ITER《Vacuum Vessel》，功能与 in-wall shielding 段](https://www.iter.org/machine/vacuum-vessel)。

### 压差、热变形与电磁载荷

抽空容器承受向内外压，抗屈曲需计入形状误差、加强筋、开孔和焊接变形。内压薄壁圆筒的 $\sigma_\theta=pr/t$ 仅描述均匀膜应力：$p$ 用 Pa，$r,t$ 用 m。教学取 $p=0.1$ MPa、$r=1$ m、$t=0.01$ m，得 10 MPa；外压稳定性须另求。

取长度 $\ell$ 的半圆筒，压力与两侧膜拉力平衡；热应变和磁力密度分别由膨胀系数定义及带电粒子 Lorentz 力求得：

$$
2pr\ell=2\sigma_\theta t\ell,\qquad
\epsilon_{\rm th}=\int\alpha\,dT\simeq\alpha\Delta T,\qquad
\mathbf f=\sum_s n_sq_s\mathbf u_s\times\mathbf B=\mathbf J\times\mathbf B.
$$

其中常 $\alpha$ 近似用于小温区，$\alpha$ 用 K⁻¹，$\mathbf f$ 用 N/m³。

支承或焊接约束把热膨胀转为应力，端口与焊缝可能集中载荷；时变磁场还产生涡流力。结构分析据此组合正常热循环、磁场变化与项目规定的故障载荷。

检漏检查贯通气道，无损检测检查其可检尺寸与方向的缺陷，尺寸计量检查安装几何。室温气密结果需与热循环、疲劳证据分别记录；表面放气进入[真空气体收支](../工程系统/README.md)。

依据：[真空与气体系统](../工程系统/README.md)。

### 约束刚度怎样把热膨胀变成应力

线弹性细杆的总轴向应变由机械与热两部分相加：$\epsilon=\sigma/E+\alpha\Delta T$。杆长为 $L$、面积为 $A$，若支架等效为刚度 $K_s$ 的弹簧，兼容条件是杆伸长与支架回缩之和为零。因此

$$
F\left(\frac{L}{EA}+\frac1{K_s}\right)+\alpha L\Delta T=0,
\quad
\sigma=-\frac{E\alpha\Delta T}{1+K_b/K_s},\quad K_b=\frac{EA}{L}.
$$

教学取 $E=180$ GPa、$\alpha=12\times10^{-6}$ K⁻¹、$\Delta T=150$ K。完全刚性支架使应力达到 $-324$ MPa；当 $K_s=K_b$ 时为 $-162$ MPa，负号表示压缩。改变支架柔度会直接改变力的传递，这是腔体滑动支承、柔性连接与热位移设计的基本依据。此例采用均匀温升、单轴小应变；腔体壳体的弯曲和温度梯度可在同一热弹性关系上继续建模。[Bower《Applied Mechanics of Solids》§3.2.2 与 §3.2 的热应变分解](https://solidmechanics.org/Text/Chapter3_2/Chapter3_2.php)给出本构起点。

## 第一壁与包层

第一壁包括面向等离子体的表面、支承与冷却结构；后方包层承担中子吸能、屏蔽及设计规定的增殖。装甲、热沉、承力层和增殖介质按各自功能集成。

D–T 中子与氦核分别携带约 14.1、3.5 MeV。中子深入部件散射和反应，辐射及带电粒子形成表面热负荷；第一壁、核热和偏滤器靶板须分别输入：

$$
P_{\rm nuc}=\int_V q'''(\mathbf x)\,dV,\qquad E_{\rm nuc}=\int P_{\rm nuc}\,dt.
$$

体热源 $q'''$ 用 W/m³，表面热流用 MW/m²，功率与能量分别用 W、J。

### 屏蔽包层与增殖包层

ITER 的主包层以屏蔽和移热为主要功能，测试包层模块用来检验未来增殖方案；燃料自持还涉及整套增殖与燃料循环。含锂增殖介质通过中子反应产生氚，同时需要提取、输送与冷却。包层的中子效率受结构吸收、开孔、材料组成及几何影响，整厂燃料闭合需要把这些中子学因素与回收效率合并核算。[ITER《Blanket》及《Tritium breeding》，主包层与 TBM 功能说明](https://www.iter.org/machine/blanket)；[ITER 氚增殖试验范围](https://www.iter.org/machine/supporting-systems/tritium-breeding)。

ITER 官方包层页面说明，2023 年决定把计划中的第一壁装甲由铍改为钨；旧版本图示和材料表必须标注日期。历史铍试验与各装置的材料方案按其设计版本分别记录。[ITER《Blanket》，First wall panels 段，2026-10-16 访问](https://www.iter.org/machine/blanket)。

屏蔽增厚会占用径向空间；冷却出口升温可能改善热循环效率，却加重蠕变、腐蚀与接头负担。中子学、热工、结构和维护应采用同一几何与载荷评价。

### 体积发热怎样转成冷却面负荷

取厚度 $d$ 的平板，$x=0$ 面绝热，$x=d$ 面固定在冷却温度 $T_c$，材料导热率 $k$ 为常数。给定教学体热源 $q'''(x)=q_0e^{-x/\ell}$，由局部能量守恒 $dq''/dx=q'''$、$q''(0)=0$ 积分得

$$
q''(x)=q_0\ell(1-e^{-x/\ell}),\qquad
T(0)-T_c=\frac{q_0\ell}{k}
\left[d-\ell(1-e^{-d/\ell})\right].
$$

第二式来自将 Fourier 定律 $dT/dx=-q''/k$ 再积分一次。取 $q_0=2.0$ MW/m³、$\ell=0.050$ m、$d=0.10$ m、$k=20$ W/(m·K)，冷却面接收 $86.5$ kW/m²，前表面比冷却面高约 284 K。这个完整例子把体热源、面热流和最高温度连起来；分布式冷却会缩短实际导热路径。这里的指数源是练习输入，中子学计算可为真实几何提供 $q'''(\mathbf x)$。[MIT 传热讲义 §16.3 的控制体与 Fourier 定律](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node117.html)给出推导框架，[ITER 包层说明](https://www.iter.org/machine/blanket)给出部件的屏蔽与排热作用。

## 偏滤器与排热部件

偏滤器沿开磁力线把热与粒子导向靶板，结合辐射、复合与抽气排热及氦灰。脱靶降低靶前温度和热负荷，其稳定性与杂质、核心约束耦合；靶板热量仍须计入沿场输运、辐射和再沉积。

总功率除以润湿面积 $P/A$ 只给面积平均热流，峰值由落点宽度、磁通膨胀、入射角和装配台阶决定。若一块表面均匀接受 5 MW、有效面积 $0.5\,\mathrm{m^2}$，平均为 $10\,\mathrm{MW\,m^{-2}}$；实际峰值可以更高。ITER 官方列出的靶板 $10\,\mathrm{MW\,m^{-2}}$ 稳态、$20\,\mathrm{MW\,m^{-2}}$ 慢瞬态热流属于其设计估计及资格验证背景，数值对应其指定的部件和热边界。[ITER《Divertor》，靶板热流与高热流原型试验段](https://www.iter.org/machine/divertor)。

### 温升、热冲击与疲劳

![相同稳态热流通过固体与冷却膜，温降由面热阻分配。](/assets/diagrams/system-material-thermal-resistance.svg)

均匀、常导热系数、无内热源的一维平板稳态模型给出

$$
\Delta T_{\rm solid}=\frac{q''d}{k},\qquad
\Delta T_{\rm film}=\frac{q''}{h}.
$$

$q''$ 用 $\mathrm{W\,m^{-2}}$，厚度 $d$ 用 m，$k$ 用 $\mathrm{W\,m^{-1}K^{-1}}$，换热系数 $h$ 用 $\mathrm{W\,m^{-2}K^{-1}}$。取教学参数 $q''=10\,\mathrm{MW\,m^{-2}},d=3\,\mathrm{mm},k=100\,\mathrm{W\,m^{-1}K^{-1}}$，固体内温差已达 300 K；如果 $h=10^5\,\mathrm{W\,m^{-2}K^{-1}}$，冷却边界另有 100 K 温差。接触热阻、真实几何和温度依赖物性还会改变结果，计算时应配套采用相应材料状态。

推导链为：无体热源时 $dq''/dx=0$，积分 Fourier 定律 $dT/dx=-q''/k$ 得固体温差；边界闭合 $q''=h(T_{\rm wall}-T_{\rm fluid})$ 给膜温差。瞬态由

$$
\rho c_p\partial_tT=k\nabla^2T,\qquad
\frac{\Delta T}{\Delta t}\sim\alpha_{\rm th}\frac{\Delta T}{\ell_T^2}
\quad\Longrightarrow\quad\ell_T\sim\sqrt{\alpha_{\rm th}\Delta t}.
$$

热扩散率 $\alpha_{\rm th}=k/(\rho c_p)$ 用 m²/s。同一面能量在更短时间内输入，热量更集中于浅层；低平均功率也可能引起脉冲开裂或熔化。疲劳评价还需应变范围、循环数、平均温度、驻留和初始缺陷；高热流试验应统一热流标定、脉冲及冷却边界。

### 短脉冲温升由热扩散决定

![半无限固体在 10 ms 与 40 ms 的解析热扩散剖面；参数与本节算例相同。](/assets/diagrams/system-material-heat-diffusion.svg)

对初始均温、热物性恒定的半无限固体，热方程为 $\partial_tT=\alpha_{\rm th}\partial_x^2T$，其中 $\alpha_{\rm th}=k/(\rho c_p)$。在表面施加恒定热流 $q''$ 后，取相似变量 $\xi=x/(2\sqrt{\alpha_{\rm th}t})$，令 $T-T_0=2q_s\sqrt{\alpha_{\rm th}t}F(\xi)/k$，其中 $q_s$ 为上述恒定表面热流。链式求导给出 $F\prime\prime+2\xi F\prime-2F=0$，表面与远场条件给出 $F\prime(0)=-1$、$F(\infty)=0$。积分并代回边界得到

$$
T-T_0=\frac{2q''\sqrt{\alpha_{\rm th}t}}{k}
\left[\frac{e^{-\xi^2}}{\sqrt\pi}-\xi\,{\rm erfc}(\xi)\right].
$$

令 $x=0$ 得表面温升 $2q''\sqrt{\alpha_{\rm th}t}/(k\sqrt\pi)$。教学取 $q''=5.0$ MW/m²、$k=100$ W/(m·K)、$\rho c_p=2.5$ MJ/(m³·K)，则 $\alpha_{\rm th}=4.0\times10^{-5}$ m²/s；10 ms 后表面升温 35.7 K，扩散长度 $\sqrt{\alpha_{\rm th}t}=0.632$ mm。脉冲增至 40 ms，温升与扩散长度都加倍。表面输入能量为 $q''t$，对解析温度剖面积分也得到相同储热量。半无限近似适用于热扩散区尚未到达背面冷却边界的阶段；长时间计算转向有限厚度热阻模型。[MIT §16.3 的能量平衡与导热方程](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node117.html)是上述恒物性解析解的起点。

## 材料数据与选型

钨的耐热与侵蚀特性须结合高 Z 杂质辐射、脆性、再结晶和辐照评价；CuCrZr 热沉的强化依赖热处理，低放射化钢则主要承担结构功能。各类材料的用途与限制如下。

| 材料类别 | 常见功能 | 必须一起考虑的限制 |
| --- | --- | --- |
| 钨及钨基材料 | 面向等离子体装甲 | 温度与织构相关脆性、表面侵蚀、杂质辐射、辐照后变化 |
| CuCrZr 等铜合金 | 高热流热沉与冷却结构 | 热处理态、过时效软化、蠕变、辐照和接头质量 |
| 低放射化钢 | 包层等承力结构候选 | 脆化、蠕变、腐蚀、成分与杂质控制 |
| 陶瓷与复合材料 | 电绝缘、功能层或增殖相关部件 | 热导率、辐照电导、开裂、热膨胀和连接 |
| 液态金属候选 | 可更新表面或包层介质 | 蒸发、腐蚀、磁流体压降、滞留和自由表面稳定性 |

上述分类说明不同材料的部件功能。IAEA 1994 年材料汇编的铜合金章已经清楚展示 CuCrZr 强度对热历史的依赖；材料数据按其温度和热处理状态选取。[Zinkle 与 Fabritsiev，Copper alloys for high heat flux structure applications，§2.2–2.3，IAEA Vol. 5，印刷页 163–192](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub23vol5_web.pdf)。EUROFER 相关原研究说明，对钢表面的优先溅射和富钨层也必须具体分析，以确定其表面侵蚀响应。[EUROfusion，Fe–W 模型薄膜研究，Introduction 与实验结果](https://scipub.euro-fusion.org/wp-content/uploads/WPPFCCP16_14829_submitted.pdf)。

### 中子损伤的量度

dpa 是按指定损伤模型计算的平均每原子位移量；永久缺陷密度还取决于复合与演化。常用形式为

$$
D_{\rm dpa}=\int dt\int dE\,\phi(E,t)\sigma_d(E).
$$

单个靶原子的反应概率为 $\phi(E,t)\sigma(E)dE\,dt$。将各反应道乘平均位移数并求和，定义损伤加权截面 $\sigma_d$，再作能量、时间积分即得 dpa；把权重换为氦产额则得到氦生成。两者均依赖能谱。

$\phi$ 是单位能量区间的中子通量谱，若 $E$ 用 eV，则单位为 $\mathrm{m^{-2}s^{-1}eV^{-1}}$；损伤截面 $\sigma_d$ 用 $\mathrm{m^2}$，积分结果无量纲。模型须注明位移阈能和截面库；不同损伤模型所得 dpa 不宜不加说明地混用。

中子同时引起嬗变与氦生成。氦含量常以 appm（原子百万分率）报告，He/dpa 比还依赖中子谱及材料。相同 dpa 下，不同温度、剂量率、气体生成和应力状态可能产生不同缺陷和力学性能。离子与中子辐照的比较还需匹配损伤深度、剂量率和气体生成。[Gilbert 等，Journal of Nuclear Materials 442 (2013), S755–S760，§2–3 的输运、dpa 与气体生成计算](https://arxiv.org/pdf/1311.5079)。

### 两群能谱算例：相同注量为何产生不同损伤

把连续能谱分成两个能群，先计算各群注量 $\Phi_g=\int\phi_gdt$，再以群平均损伤截面求 $d=\sum_g\Phi_g\sigma_{d,g}$。氦生成采用另一套截面，$c_{\rm He}=\sum_g\Phi_g\sigma_{{\rm He},g}$，原子分数乘 $10^6$ 才得到 appm。教学取两群注量分别为 $10^{24}$、$2\times10^{24}$ m⁻²，损伤截面为 1000、2000 barn，氦生成截面为 0.01、0.05 barn，并用 $1$ barn $=10^{-28}$ m²。

逐项相乘得到损伤 $0.10+0.40=0.50$ dpa，氦浓度 $1+10=11$ appm，即本例 22 appm/dpa。若把全部 $3\times10^{24}$ m⁻² 移到第一能群，总注量保持原值，结果却变为 0.30 dpa 和 3 appm。材料比较因此要保存能谱、核数据模型和温度；这些量共同决定辐照条件。所用数字是分组积分练习，方法与谱依赖的物理说明可定位 [Gilbert 等 2013，第 2–3 节的 neutron spectrum、damage 与 transmutation 分析](https://arxiv.org/pdf/1311.5079)。

## 等离子体与材料相互作用

物理溅射是入射粒子把动量与能量传给表面原子并使其逸出。溅射产额 $Y(E,\theta)$ 是每个入射粒子平均打出的靶原子数，无量纲，取决于粒子种类、能量、角度和表面组成。若入射通量为 $\Gamma_i$，最简单的毛侵蚀速度为

$$
v_{\rm er}=\frac{Y\Gamma_i}{n_{\rm solid}}.
$$

由原子计数 $Y\Gamma_iA\,dt=n_{\rm solid}A\,dx$ 得毛侵蚀率；加入再沉积通量后，净后退速度为

$$
v_{\rm net}=\frac{Y\Gamma_i-\Gamma_{\rm dep}}{n_{\rm solid}}.
$$

正值为侵蚀，负值为生长。

$\Gamma_i$ 用 $\mathrm{m^{-2}s^{-1}}$，固体原子数密度用 $\mathrm{m^{-3}}$，速度用 m/s。假设 $Y=10^{-3},\Gamma_i=10^{23}\,\mathrm{m^{-2}s^{-1}},n_{\rm solid}=6\times10^{28}\,\mathrm{m^{-3}}$，得到约 $1.7\,\mathrm{nm\,s^{-1}}$，作用 1000 s 对应约 $1.7\,\mu\mathrm m$。这是指定参数、忽略再沉积的教学例；实际净侵蚀还要减去沉积通量；变化的离子谱需要逐能量加权的 $Y$。Fe–W 表面的优先溅射实验进一步说明，表面组成会在轰击过程中改变。[EUROfusion，模型合金实验及结论](https://scipub.euro-fusion.org/wp-content/uploads/WPPFCCP16_14829_submitted.pdf)。

近局域平衡的等温稀溶质，由化学势与线性迁移响应得到 Fick 定律：

$$
\mu_H=\mu_0+k_BT\ln(c_H/c_0),\quad
\mathbf J_H=-\mathcal M c_H\nabla\mu_H
=-D_H\nabla c_H,\quad D_H=\mathcal M k_BT.
$$

陷阱会改变可动浓度及化学势，需要扩展模型。

氢同位素可反射、注入、扩散、俘获、脱附或穿透。滞留对应库存，渗透对应穿透通量；$D_H$ 用 m²/s、$c_H$ 用原子数/m³。陷阱、表面复合和辐照可能使单一扩散系数不足。TDS 给出加热释放，核反应分析等约束深度分布，须保留晶粒与预处理。Ye 等钨实验中，氘总滞留量与脱附峰随载入条件呈不同变化；推向整机氚库存还需同位素、工况和面积映射。

依据：[Ye 等，Comparison of deuterium retention in tungsten exposed to deuterium plasma and gas，2019，摘要](https://arxiv.org/abs/1909.06820)。

材料释放出的杂质又会改变边缘辐射与鞘层，形成反馈。射频近场引起的鞘层电压可能提高局部入射能量，应与[离子回旋加热](../辅助加热/离子回旋加热/README.md)中的天线和壁面问题合看，由局部鞘层电势与入射分布计算表面轰击能量。

### 侵蚀、辐照与热应力的耦合

对一个受热部件，表面侵蚀减小装甲厚度，中子改变热导率与韧性，温度梯度又控制热应力；三者会彼此改变边界条件。设平板温差按 $q''d/k$ 估算，当厚度减半而热导率也因假定损伤减半时，稳态温差可能不变，但剩余承载截面、允许缺陷尺度和抗冲击能力已经不同。这一给定比例算例展示了温度相同而结构裕量改变的情形；真实材料参数需要按辐照状态读取。

通量与注量满足 $\Phi=\int\Gamma\,dt$，单位分别为 m⁻²s⁻¹、m⁻²。相同注量下，温度、持续时间、缺陷复合和热疲劳仍可不同。中子试验还需能谱，等离子体试验需离子能量、角度与表面化学状态。

依据：[Gilbert 等，2013，中子谱与材料位置依赖](https://arxiv.org/pdf/1311.5079)。

### 从扩散方程求进入材料的粒子库存

设半无限材料初始无可移动氢，表面浓度维持 $c_s$，扩散系数 $D$ 为常数，忽略陷阱与表面反应。连续性方程和 Fick 定律结合为 $\partial_tc=D\partial_x^2c$。设 $c=c_sF(\xi)$、$\xi=x/(2\sqrt{Dt})$，链式求导得 $F\prime\prime+2\xi F\prime=0$。先积分为 $F\prime=C e^{-\xi^2}$，再用 $F(0)=1$、$F(\infty)=0$ 确定常数，得到

$$
c(x,t)=c_s\,{\rm erfc}\!\left(\frac{x}{2\sqrt{Dt}}\right),\quad
\frac{N}{A}=\int_0^\infty c\,dx
=2c_s\sqrt{\frac{Dt}{\pi}}.
$$

表面入射扩散通量为 $J(0,t)=c_s\sqrt{D/(\pi t)}$；将它对时间积分，正好恢复单位面积库存。取教学参数 $D=10^{-12}$ m²/s、$c_s=10^{24}$ m⁻³、$t=10^4$ s，得到 $N/A=1.13\times10^{20}$ m⁻²，特征深度 $2\sqrt{Dt}=0.20$ mm。把 $D$ 提高四倍，深度与库存均加倍；库存随时间平方根增长源于持续变宽的扩散层。真实表面的滞留可通过增加陷阱占据率方程、表面复合边界和温度依赖 $D(T)$ 扩展。扩散导致的 $t^{-1/2}$ 通量尺度也见 [Seidel《Accelerator Vacuum》§2 的 diffusion/outgassing 讨论](https://arxiv.org/html/2105.07675v1)。

## 制造、连接与检验

接头同时传热和传力；膨胀失配可集中应力。常膨胀系数相差 $10^{-5}$ K⁻¹、均匀温差 300 K 时，失配应变为 0.3%；应力和寿命还取决于中间层、几何、塑性及循环。

自由应变相减给出

$$
\Delta\epsilon_{\rm free}=\int(\alpha_1-\alpha_2)\,dT
\simeq(\alpha_1-\alpha_2)\Delta T=0.003.
$$

连接后再施加兼容与合力条件，才能求应力。

钎焊、扩散连接、热等静压或其他工艺要同时满足结合质量、热阻、冷却密封与基材组织要求。较高连接温度可能有利于结合，却使 CuCrZr 强化相与基材组织变化；因此接头和热影响区应使用加工后的物性。[IAEA 铜合金章，§2.2–2.3，连接热历史与软化讨论](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub23vol5_web.pdf)。

部件证据应连接炉批、热处理、尺寸、接头检查、代表性热循环及试后检查。无损检测附检出能力和盲区，热成像附发射率与标定。ITER 全尺寸偏滤器试验验证的是材料、连接、冷却和结构组合；允许缺陷、泄漏率与寿命裕量取自具体项目文件。

依据：[ITER《Divertor》，Divertor targets](https://www.iter.org/machine/divertor)。

### 两种材料连接后的应力分担

用两根等长、等截面且端部牢固相连的平行杆表示最简单的热失配。均匀温升后，两杆具有同一轴向应变 $\epsilon$；外部无轴向载荷，故 $\sigma_1A+\sigma_2A=0$。将 $\sigma_i=E_i(\epsilon-\alpha_i\Delta T)$ 代入，得到

$$
\epsilon=\frac{E_1\alpha_1+E_2\alpha_2}{E_1+E_2}\Delta T,\qquad
\sigma_1=\frac{E_1E_2}{E_1+E_2}(\alpha_2-\alpha_1)\Delta T,
\quad \sigma_2=-\sigma_1.
$$

取教学材料 $E_1=200$ GPa、$E_2=100$ GPa、$\alpha_1=5\times10^{-6}$ K⁻¹、$\alpha_2=15\times10^{-6}$ K⁻¹、$\Delta T=200$ K。共同应变为 $1.667\times10^{-3}$，低膨胀材料承受 $+133$ MPa 拉应力，高膨胀材料承受 $-133$ MPa 压应力，两杆合力为零。这说明约束应变由刚度加权决定。真实接头还会出现弯曲、端部剪切和塑性；有限元可沿同样的兼容与平衡条件建立几何模型。[Bower §3.2 的热弹性本构和应变能](https://solidmechanics.org/Text/Chapter3_2/Chapter3_2.php)提供推导依据。

## 材料物性数据与状态追踪

- [ITER：真空室](https://www.iter.org/machine/vacuum-vessel)、[包层](https://www.iter.org/machine/blanket)与[偏滤器](https://www.iter.org/machine/divertor)：部件功能及设计语境。
- [IAEA，Atomic and Plasma–Material Interaction Data for Fusion，Vol. 5，1994](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub23vol5_web.pdf)：历史材料物性综述，重点使用铜合金的热历史与疲劳机制。
- [Gilbert 等，2013](https://arxiv.org/pdf/1311.5079)：损伤、嬗变、气体生成与模型依赖。
- [EUROfusion：Fe–W 表面优先溅射研究](https://scipub.euro-fusion.org/wp-content/uploads/WPPFCCP16_14829_submitted.pdf)：表面组成演变的原始研究。

### 把一条物性数据转成可计算的材料卡

阅读材料表时，先把温度、材料状态和单位与数值一起抄入卡片。例如一张教学卡给出同一批材料在 400 K、600 K 的导热率分别为 120、100 W/(m·K)。在这一区间采用线性插值，

$$
k(T)=120+\frac{100-120}{600-400}(T-400),
$$

直线模型 $k=a+bT$ 的斜率为 $b=(100-120)/(600-400)=-0.10$ W/(m·K²)，代回任一点确定截距。

得到 500 K 时 $k=110$ W/(m·K)。再取厚度 3.0 mm，面热阻 $R''=d/k=2.73\times10^{-5}$ m²·K/W，5.0 MW/m² 的稳态热流给出约 136 K 温差。阅读卡应同时保存“线性插值”这一方法与区间，之后可用温度依赖热导率的积分替换常数近似。

资料追踪可沿 [IAEA《Atomic and Plasma-Material Interaction Data for Fusion》，卷 5，1994 年，铜合金章节的材料状态和热物性讨论](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub23vol5_web.pdf)展开：同一合金名下，加工、热处理与辐照状态需要分别建卡；数值、试样状态、测试方法和原图表页码组成一条完整数据记录。本例的 120 和 100 是教学输入。

[工程系统](../工程系统/README.md) · [返回知识库](../README.md)
