# 电子伯恩斯坦波加热（EBW）

电子伯恩斯坦波是包含电子有限回旋半径效应的动理学波，通常表现为准静电、短波长分支。它可以在普通电子回旋电磁波已遇密度截止的区域传播，但不能像真空电磁波那样从发射器直接穿过真空。本页围绕“电磁波进入边缘 → 模转换 → EBW 传播 → 吸收/电流驱动”的完整链条展开，资料核验日期为 2026-10-16。 对应计算流程见[模拟专题](../../仿真计算/电子伯恩斯坦波模拟/README.md)。

## EBW 色散与 O-X-B 转换

### 为什么能越过普通电子回旋波的密度限制

冷介电模型包含 O、X 等电磁分支，却丢掉了粒子在有限回旋轨道上采样波场的效应。保留有限温度后，色散在电子回旋谐波之间出现 Bernstein 分支。其性质依赖 $k_\perp\rho_e$，其中 $\rho_e=v_{te}/\Omega_e$、$v_{te}=\sqrt{2T_e/m_e}$，此处 $T_e$ 以 J 表示。$k_\perp$ 为 $\mathrm{m^{-1}}$、$\rho_e$ 为 m；它们的乘积无量纲。[Fitzpatrick：温等离子体垂直传播，图 7.9](https://farside.ph.utexas.edu/teaching/plasma/Plasmahtml/node96.html)

有限回旋半径怎样进入色散，可以从最简单的垂直静电波推起。取均匀磁场、无碰撞 Maxwell 电子、静止离子及 $k_\parallel=0$，令电势扰动为 $\phi_1e^{ik_\perp x-i\omega t}$。在未扰动轨道 $x=X+\rho\sin\theta$ 上，将波因子展开为 $e^{ik_\perp\rho\sin\theta}=\sum_\ell J_\ell(k_\perp\rho)e^{i\ell\theta}$；线性 Vlasov 方程每个谐波的轨道积分便带分母 $\omega-\ell\Omega_e$。再对垂直 Maxwell 分布积分，使用 $\int_0^\infty ue^{-u^2}J_\ell^2(au)du=e^{-a^2/2}I_\ell(a^2/2)/2$，并把正负谐波配对，Poisson 方程给出

$$
\epsilon_L=1-\frac{2\omega_{pe}^2e^{-b}}{b}
\sum_{\ell=1}^{\infty}
\frac{\ell^2I_\ell(b)}{\omega^2-\ell^2\Omega_e^2}=0,
\qquad b=\frac{k_\perp^2v_{te}^2}{2\Omega_e^2}.
$$


这里 $J_\ell$、$I_\ell$ 分别是第一类普通、修正 Bessel 函数，$\Omega_e=eB/m_e>0$。这是垂直、静电极限的 Bernstein 色散；有限 $k_\parallel$ 和相对论效应另行加入热响应。式中回旋谐波的分母保留下来，且色散不再要求电磁 O 模的 $N^2=1-\omega_{pe}^2/\omega^2>0$，因而可在 O 模截止密度之上存在传播解。当 $b\to0$ 时只有 $I_1(b)\simeq b/2$ 留下，方程退为 $1-\omega_{pe}^2/(\omega^2-\Omega_e^2)=0$，连续回到上杂频率；这也检查了热色散的冷极限。[Fitzpatrick，垂直热色散与 Bernstein 分支](https://farside.ph.utexas.edu/teaching/plasma/Plasmahtml/node96.html)

EBW 的波矢、群速度和吸收由热色散及密度、温度、磁场剖面决定，可能先在外层谐波吸收。真空不支持此准静电分支，注入与观测都需电磁波—EBW 转换。 [Urban 等，§1–§2](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

### O-X-B 与 X-B 转换

O-X-B 路线先从低密度侧注入适当斜角和偏振的 O 模，在接近 O 模截止的区域转换到连接慢 X 支的波，再在上杂共振附近转换为 EBW。上杂角频率为

$$
\omega_{UH}^2=\omega_{pe}^2+\Omega_e^2.
$$


频率单位均为 $\mathrm{rad\,s^{-1}}$。上式可由刚才的 $b\to0$ 色散乘以 $\omega^2-\Omega_e^2$ 后移项得到；它描述垂直电子振荡同时受到电荷分离恢复力与磁场回旋力作用。O-X 与 X-B 两步转换的位置、敏感参数及损失分别计算。直接 X-B 注入则依靠 X 支通过适当的截止—共振结构耦合，倏逝层厚度对效率非常重要，直接影响转换功率。[Urban 等，§2.1](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

对于局部一维平板、近平面波、适当磁场/密度梯度几何的 O-X 转换，定义 $Y=\Omega_e/\omega$、$\mathbf N=c\mathbf k/\omega$，最佳条件为

$$
N_{\parallel,opt}^{2}=\frac{Y}{1+Y},\qquad N_{pol}=0.
$$


这里 $N_{pol}$ 是沿 $\mathbf B\times\nabla n_e$ 方向的折射率分量，与密度梯度方向的波矢分量分别定义。$Y$ 与全部分量应取 O 模截止附近的局部值。若 $Y=0.5$，则 $|N_{\parallel,opt}|=1/\sqrt3\simeq0.577$；实际真空发射角还需通过边缘折射和真实几何映射，由该映射求机械镜角。[Urban 等，式 (1)](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

最佳角的来源是两个冷波分支在 O 截止处的匹配。记 $X=\omega_{pe}^2/\omega^2$，忽略离子响应时平行介电量是 $P=1-X$；O 截止有 X=1。此处非共振圆偏振分量 $L=1-X/(1+Y)$，所以 $L=Y/(1+Y)$。在 $N_{pol}=0$ 的转换平面中，令慢 X 分支的截止 $N_\parallel^2=L$ 与 P=0 重合，就得到 $N_{\parallel,opt}^2=Y/(1+Y)$。偏离这个值会分开两支的转向点，在它们之间产生有限的倏逝间隙；下面的效率公式量化这一间隙。

### 转换后吸收和电流驱动

EBW 到达电子回旋谐波附近时可强烈吸收。有限 $k_\parallel$ 与相对论效应使共振满足 $\omega-k_\parallel v_\parallel=s\Omega_e/\gamma$，因而冷谐波面只是参考位置。吸收后能否产生电流，还要看速度分布不对称、碰撞和捕获电子。EBW 的 $N_\parallel$ 可沿路显著演化，发射时选定方向并不意味着吸收处谱保持原样。对于过密球形托卡马克，EBW 是有吸引力的候选方案，系统效率还包含转换、传输与电源效率。[UKAEA：STEP EBW 电流驱动会议摘要，2023 年登记](https://scientific-publications.ukaea.uk/papers/electron-bernstein-wave-ebw-current-drive-profiles-and-efficiency-for-step/)

### 由截止面与混杂面计算转换层的位置

O 模截止满足 $\omega_{pe}=\omega$，故 $n_O=\epsilon_0m_e\omega^2/e^2$。上混杂层满足 $\omega^2=\omega_{pe}^2+\Omega_e^2$，逐项移项后得到 $n_{UH}=n_O(1-Y^2)$，其中 $Y=|\Omega_e|/\omega$。若局部磁场变化小、密度按 $n(x)=n_*e^{x/L_n}$ 增长，两个密度面的间距为 $\Delta x=L_n\ln(n_O/n_{UH})$。这把频率、磁场和密度梯度联系到具体空间尺度。

取教学频率 28 GHz，选择磁场使 $Y=0.5$，即约 0.5001 T。O 截止密度为 $9.7251\times10^{18}$ m⁻³，上混杂密度为 $7.2938\times10^{18}$ m⁻³；$L_n=20$ mm 时，两面的间距为 5.754 mm。若整个密度剖面增大 10%，固定密度面沿 x 方向移动 $-L_n\ln1.1=-1.906$ mm。转换窗口的控制因而要跟踪边缘密度和梯度，毫米级层位移动就会改变波束与转换区的相交位置。这里只计算层位；转换份额另由角度、极化和完整波场求得。

推导起点与参考位置：[Urban 等 2011，EBW survey，§2.1，式 (1)–(3)](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

## EBW 发射光学与边缘诊断

微波源、传输、窗、极化器及发射光学连接边缘转换层。束曲率、束宽和方向共同优化：窄束提高局部强度，同时扩大角谱、降低平均转换。

密度诊断需要覆盖转换层及其梯度，并与线平均密度及核心密度共同重建剖面。反射计、Thomson 散射和磁平衡提供不同约束；偏振标定则需要追踪沿镜链和窗口后的实际椭圆偏振。测得边缘平均剖面还不够，因为涨落会使转换层位置与最佳入射条件随时间变化。[Urban 等，§2.1 对波束与涨落的讨论](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

接收 EBW 发射的系统采用相反的转换链：内部辐射先转成电磁波才能被外部天线看见。因而接收亮度同时包含电子温度、光学厚、模转换及接收模式匹配，反演当地 $T_e$ 时需逐项校正。[Preinhaelter 等，MAST 发射实验论文，§II–§III](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/RSIVOL74p1437.pdf)

### 把有限角谱积分成波束转换率

在最优极向角附近，把 O-X 公式简写为 $C(\delta N)=e^{-A\delta N^2}$，$A=2\pi k_0L_n\sqrt{Y/2}(1+Y)$。设入射功率角谱在 $\delta N$ 上为均值零、标准差 $\sigma_N$ 的归一化高斯，则 $\bar C=\int C(\delta N)e^{-\delta N^2/(2\sigma_N^2)}d\delta N/(\sqrt{2\pi}\sigma_N)$。合并两个二次指数并积分，得到 $\bar C=(1+2A\sigma_N^2)^{-1/2}$。

取 $Y=0.5$、$k_0L_n=10$，有 $A=47.1239$。$\sigma_N=0.04$ 时，平均转换率为 0.9322；角谱展宽到 0.10 时，降至 0.7175。即使波束中心始终对准最优角，有限发散角仍使一部分功率偏离窗口。天线光学设计因此要同时优化束腰、入射方向和到转换层的距离。这个算例采用一维角谱、固定梯度及最佳极向方向，二维角谱可以用同样的功率积分加入原公式的极向项。

![密度梯度越缓，近平面波转换窗口越窄；有限角谱需加权积分。](/assets/diagrams/heat-ebw.svg)

密度梯度越缓，近平面波转换窗口越窄；有限角谱需加权积分。

推导起点与参考位置：[Urban 等 2011，EBW survey，§2.1，式 (1)–(3)](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

## 模式转换、传播与吸收预算

O-X 局部转换的一项常用近似为

$$
C_{OX}\simeq\exp\left\{-\pi k_0L_n\sqrt{\frac{Y}{2}}
\left[2(1+Y)(N_\parallel-N_{\parallel,opt})^2+N_{pol}^2\right]\right\}.
$$


$k_0=\omega/c$ 为 $\mathrm{m^{-1}}$，$L_n=|n_e/(dn_e/dx)|$ 为 m，$x$ 沿局部密度梯度；指数无量纲，$C_{OX}$ 是功率比例。该式适用于相应一维、近平面波转换近似，表达的是 O-X 一步，全链效率还需继续计算 X-B 与 EBW 吸收。它揭示在固定偏离最佳角度时，较大的 $k_0L_n$ 使角窗口更窄；真实二维曲率、波束角谱、偏振错误和涨落仍需全波计算。[Urban 等，式 (2) 与后文限定](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

前式的具体系数采用 [Urban 等式 (2) 引述的一维模式转换渐近解](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)，需要冷波方程的完整两模匹配。这里用局部穿隧模型推导其标度：在最佳角附近，分支间隙对角度失配的一阶项在匹配点消失，最低阶间隙平方与 $(N_\parallel-N_{\parallel,opt})^2$、$N_{pol}^2$ 成正比。线性化密度后，可把间隙中的衰减波数写成 $\kappa_\xi^2=\delta^2-a^2\xi^2$，其中 $\xi$ 为按真空波数归一化的位置，$\delta^2$ 表示上述角失配二次型，a 与 $1/(k_0L_n)$ 成正比。两转向点是 $\xi=\pm\delta/a$。场幅沿倏逝区按 $\exp[-\int\kappa_\xi d\xi]$ 衰减，功率取幅度平方，故此约化模型给

$$
T_{gap}\simeq\exp\!\left[-2\int_{-\delta/a}^{\delta/a}
\sqrt{\delta^2-a^2\xi^2}\,d\xi\right]
=\exp(-\pi\delta^2/a).
$$


积分以 $a\xi=\delta\sin u$ 换元，是半椭圆面积 $\pi\delta^2/(2a)$。因 $1/a\propto k_0L_n$，它解释了“角失配平方×密度梯度尺度”进入指数，以及梯度较缓时角窗更窄；前式中 $\sqrt{Y/2}$、$2(1+Y)$ 和各方向权重仍取自引用的完整转换解。最佳角下局部间隙闭合，该近似给单位 O-X 转换；全系统随后仍有 X-B、传输及吸收损失。

作为量纲算例，取 $Y=0.5$、$k_0L_n=10$、$N_{pol}=0$，最佳条件处该近似给 $C_{OX}=1$；若 $|N_\parallel-N_{\parallel,opt}|=0.1$，则约为 0.624。这个理想数值不包含 X-B 损失或核心吸收。总沉积可用预算式

$$
P_{dep}=P_{src}\eta_{tr}C_{OX}C_{XB}A_B
$$


表达，其中各无量纲因子依次为传输、O-X、X-B 和转换后 EBW 吸收比例；存在多程、分支耦合时要改用相应的能量流模型。即使每一项都达到 0.8，四项乘积也只有 0.4096，总链路效率因此明显低于每个单项效率。

各系数按相邻功率面定义：

$$
P_O=\eta_{tr}P_{src},\quad P_X=C_{OX}P_O,\quad P_B=C_{XB}P_X,\quad P_{dep}=A_BP_B.
$$

相乘即得总预算；各损失只扣一次，采用相同时间窗。

计算上先用全波模型处理截止和转换层，再把合适的输出分支交给热色散射线/波束与动理学吸收模型。UHR 附近采用热响应处理物理吸收，并区分数值耗散。全波能量流、边界反射、网格与碰撞参数需独立收敛；吸收位置还应对剖面重建误差做敏感性分析。

剖面位移同时改变截止、UHR 位置和入射方向；仅扫描 $L_n$ 是单因素近似。涨落下通常有 $\langle C(\mathbf a)\rangle\ne C(\langle\mathbf a\rangle)$，应以时间分辨剖面集合传播转换与标定不确定度。 [Urban 等，§2.1 的二维与密度涨落限制](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

外层谐波吸收可产生边缘热/辐射信号而不加热核心。非热电子还会改变发射和驱动解释；核心沉积需同时符合转换、空间源位置及电子能量响应。 [MAST 历史加热实验的不同沉积工况](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/AIPCONFPROC933p323.pdf)。

### 逐次返回的转换与损耗账本

设每次到达转换层的波有份额 C 转换，余下的 $1-C$ 中有比例 r 再次返回同一层，其余在边界或传播中损失。第 j 次返回的功率比例为 $[r(1-C)]^j$，故总转换率是几何级数 $C_{tot}=C/[1-r(1-C)]$；总损失率为 $(1-r)(1-C)/[1-r(1-C)]$，两者相加为一。这里 r 把返回路径的反射、极化和传播统一作为给定有效系数。

取 C=0.60、r=0.50，第一次转换 60%，以后依次转换 12%、2.4% 等，总计 75%，剩余 25% 沿返回路径损失。再给定 X-B 转换率 0.80、EBW 吸收率 0.90，进入粒子的功率占初始入射的 $0.75\times0.80\times0.90=0.54$。1 MW 教学输入对应 540 kW。这个结果说明多次返回可提高累计转换，而每一级的损失仍在独立账本中；真实装置用全波传播或测量确定 r 及不同返回角谱，再进行逐次求和。

推导起点与参考位置：[Urban 等 2011，EBW survey，§2.1，式 (1)–(3)](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

## 转换窗口跟踪与杂散功率保护

角度、偏振和边缘剖面共同控制转换，因此机械镜角应跟踪每次放电的转换条件。若密度梯度位置改变，原先匹配的束可能变为强反射；未转换功率可以进入壁面或诊断。保护链需要源功率、反射、杂散辐射、窗温和真空信息，并与核心热响应联合分析。

转换层局部场增强也可能产生非线性过程。MAST 的历史实验在某些工况下观察到与 UHR 相关的参数衰变信号，并且转换成功时仍可能因高谐波外层吸收而使核心加热很弱。这说明“发现转换层特征信号”与“满足核心加热目标”必须分开检验。[Shevchenko 等，Electron Bernstein Wave Studies in MAST，实验讨论](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/AIPCONFPROC933p323.pdf)

控制同时记录转换、吸收和壁面能流，阈值由真实窗、源和部件参数确定。

### 把目标转换率反求角度容差

用前述局部关系 $C=e^{-A\delta N^2}$，要求 $C\ge C_{min}$，先取对数再开方，得到 $|\delta N|\le\sqrt{-\ln C_{min}/A}$。在平板且背景磁场平行界面的示例中，切向波数守恒；真空入射角 $\theta$ 相对磁场定义，则 $N_\parallel=\cos\theta$，小角度扰动满足 $\delta N\simeq-\sin\theta_{opt}\,\delta\theta$。因此可以把密度梯度决定的折射率窗口转为发射镜的角度窗口。

仍取 $Y=0.5$、$k_0L_n=10$、$A=47.1239$，并选 $C_{min}=0.80$。最优 $N_\parallel=\sqrt{Y/(1+Y)}=0.57735$，即 $\theta_{opt}=54.7356^\circ$；允许的 $|\delta N|$ 为 0.06881，小角近似给出约 ±4.83°。用 $\arccos(N_{opt}\pm\delta N)$ 可进一步保留两侧的非对称性。控制程序可对密度梯度逐时更新 A，并把角度读数及标定不确定度投影到这个窗口；本例的 80% 是教学目标，用于演示反求过程。

推导起点与参考位置：[Urban 等 2011，EBW survey，§2.1，式 (1)–(3)](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

## 伯恩斯坦辐射与模式转换测量

先用低功率扫描测定极化、束宽和发射角，再将实测边缘剖面输入转换模型，比较最佳角度和角窗口的形状。角度扫描约束转换窗口，核心吸收比例再由空间热响应与功率平衡测量。

发射诊断可以帮助寻找转换窗口，但把发射转换反推为注入效率需要同频率、同模式、相应线性传播与接收耦合条件；非热电子尾或高功率非线性会破坏最简单的温度解释。MAST 2003 年论文在比较发射谱时明确讨论模型与测量的差异、磁平衡和吸收层位置的不确定性，可用来练习剖面不确定度向发射谱的传播。[Preinhaelter 等，§III 与图 6](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/RSIVOL74p1437.pdf)

加热用有/无功率或调制能量响应检验，扣除辐射、物种交换与输运；电流另需剖面证据。重复角度/密度扫描检验窗口及涨落效应。

### 辐射转移怎样约束转换率的反演

在等温、无背向入射的 Rayleigh–Jeans 极限，沿视线的亮温满足 $dT_b/d\tau=T_e-T_b$。用积分因子解得出射亮温 $T_{b,plasma}=T_e(1-e^{-\tau})$。若波离开等离子体还需经总转换率 C 的 EBW-X-O 通道，观测值变为 $T_{b,obs}=CT_e(1-e^{-\tau})$，因此 $C=T_{b,obs}/[T_e(1-e^{-\tau})]$。三个温度在这里都以 eV 表示相同的温度能量尺度。

假设独立诊断给 $T_e=1000$ eV、亮温为 600 eV、光学厚度 $\tau=2$，则反演 $C=0.6939$。若先采用光学厚近似，得到的则是 0.6000；这约 0.094 的差来自有限发射厚度。验收时可改变频率或视线，比较不同光学厚度下的光谱与角度分布，并把传输窗、极化器和接收增益的损耗一并标定。Preinhaelter 等的 MAST 发射研究将这一辐射链与转换计算相连，为从被动观测约束主动发射角提供依据。

推导起点与参考位置：[Preinhaelter 等 2003，MAST EBW-X-O emission，§II–III、图 6](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/RSIVOL74p1437.pdf)；[Urban 等 2011，EBW survey，§2.1，式 (1)–(3)](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

## 边缘转换与外层谐波怎样决定核心加热

EBW 系统需要同时把电磁功率跨过边缘转换层，并让转换后的波抵达目标磁通面。转换良好时仍可能主要加热外层电子，因为波沿途可能先遇到高次谐波。忽略 Doppler 与相对论位移，用 $\omega=s eB/m_e$ 得到谐波场强 $B_s=m_e\omega/(se)$；再在 $B=B_0R_0/R$ 的教学几何中解出 $R_s=seB_0R_0/(m_e\omega)$。同一频率下，较高谐波位于较小磁场、较大 R 处，说明从低场侧进入的波可能先经过外层高谐波；实际吸收由热色散、沿路谱和分布共同决定。[Urban 等 §2.2–2.3](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

### 角度扫描和沉积半径描述两个环节

[Shevchenko 等 2007 年 MAST 论文图 1–2](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/AIPCONFPROC933p323.pdf)讨论了两种 60 GHz 工况：一类角窗口约 ±5°，计算沉积约在 $r/a=0.9$；有锯齿的 H 模工况窗口约 ±3°，计算沉积向内至 $r/a=0.6$，报告储能增加约 10%。角窗口全宽之比为 $6/10=0.60$，而沉积峰向内移动 0.3a；较宽的转换角窗口并不单独决定核心得到多少功率。

上述半径来自传播计算，储能变化包含输运与损失。被动角谱/亮温约束出射辐射链，主动热响应约束净输入；两者使用同一平衡和边缘剖面。 [Preinhaelter 等 2003 年 MAST 发射论文 §II–III](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/RSIVOL74p1437.pdf)。

### 先吸收的外层功率不会再到达核心

用两个串联吸收区说明谐波选择。令进入 EBW 分支的功率为 $P_B$，外层与核心的强度光学厚度分别为 $\tau_o$、$\tau_c$。对每一段积分 $dP/ds=-\alpha P$，外层出口为 $P_Be^{-\tau_o}$；再在核心段取入口与出口之差，得到

$$
P_o=P_B(1-e^{-\tau_o}),\qquad
P_c=P_Be^{-\tau_o}(1-e^{-\tau_c}),\qquad
P_{exit}=P_Be^{-(\tau_o+\tau_c)}.
$$


三项相加恰为 $P_B$。取教学输入 $P_B=1$ MW、$\tau_o=\ln5$、$\tau_c=\ln10$，外层、核心和剩余功率分别为 800、180、20 kW。若改变频率、磁场或波路，使外层光学厚度降至 0.1，而核心光学厚度暂保持 $\ln10$，则核心功率增至约 814.4 kW。该比较固定两区形状来单独显示沿程竞争，实际改变波路后还要更新转换率、谐波耦合与两区阻尼。

串联边缘与两区吸收：

$$
P_c=P_{src}\eta_{tr}C_{OX}C_{XB}e^{-\tau_o}(1-e^{-\tau_c}).
$$

联合扫描方向、频率、偏振、边缘密度与磁场，以核心热响应约束目标沉积。 [Urban 等的转换、传播与动理学计算](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)。

[返回辅助加热](../README.md) · [编写说明](../../编写说明.md) · [返回知识库](../../README.md)
