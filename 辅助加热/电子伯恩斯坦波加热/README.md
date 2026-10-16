# 电子伯恩斯坦波加热（EBW）

电子伯恩斯坦波是包含电子有限回旋半径效应的动理学波，通常表现为准静电、短波长分支。它可以在普通电子回旋电磁波已遇密度截止的区域传播，但不能像真空电磁波那样从发射器直接穿过真空。本页围绕“电磁波进入边缘 → 模转换 → EBW 传播 → 吸收/电流驱动”的完整链条展开，资料核验日期为 2026-10-16。

## 原理与适用条件

### 为什么能越过普通电子回旋波的密度限制

冷介电模型包含 O、X 等电磁分支，却丢掉了粒子在有限回旋轨道上采样波场的效应。保留有限温度后，色散在电子回旋谐波之间出现 Bernstein 分支。其性质依赖 $k_\perp\rho_e$，其中 $\rho_e=v_{te}/\Omega_e$、$v_{te}=\sqrt{2T_e/m_e}$，此处 $T_e$ 以 J 表示。$k_\perp$ 为 $\mathrm{m^{-1}}$、$\rho_e$ 为 m；它们的乘积无量纲。[Fitzpatrick：温等离子体垂直传播，图 7.9](https://farside.ph.utexas.edu/teaching/plasma/Plasmahtml/node96.html)

“没有普通 O/X 模的高密度截止”不等于“任何剖面中都能无损到达任意位置”。EBW 的波矢、群速度和吸收对密度、温度及磁场变化敏感，也可能先在外层谐波吸收。其准静电分支依赖等离子体响应，无法在真空作为同一支波远程传播，所以必须通过电磁波与 EBW 之间的模转换来注入或观测。[Urban 等，§1–§2](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

### O-X-B 与 X-B 转换

O-X-B 路线先从低密度侧注入适当斜角和偏振的 O 模，在接近 O 模截止的区域转换到连接慢 X 支的波，再在上杂共振附近转换为 EBW。上杂角频率为

$$
\omega_{UH}^2=\omega_{pe}^2+\Omega_e^2.
$$

频率单位均为 $\mathrm{rad\,s^{-1}}$。O-X 转换和 X-B 转换不是同一件事；它们的位置、敏感参数及损失都需分别计算。直接 X-B 注入则依靠 X 支通过适当的截止—共振结构耦合，倏逝层厚度对效率非常重要，不能把它简单说成“朝 UHR 发射就会全吸收”。[Urban 等，§2.1](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

对于局部一维平板、近平面波、适当磁场/密度梯度几何的 O-X 转换，定义 $Y=\Omega_e/\omega$、$\mathbf N=c\mathbf k/\omega$，最佳条件为

$$
N_{\parallel,opt}^{2}=\frac{Y}{1+Y},\qquad N_{pol}=0.
$$

这里 $N_{pol}$ 是沿 $\mathbf B\times\nabla n_e$ 方向的折射率分量，而不是“所有垂直分量均为零”。$Y$ 与全部分量应取 O 模截止附近的局部值。若 $Y=0.5$，则 $|N_{\parallel,opt}|=1/\sqrt3\simeq0.577$；实际真空发射角还需通过边缘折射和真实几何映射，不能直接把这个数值当作机械角度。[Urban 等，式 (1)](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

### 转换后吸收和电流驱动

EBW 到达电子回旋谐波附近时可强烈吸收。有限 $k_\parallel$ 与相对论效应使共振满足 $\omega-k_\parallel v_\parallel=s\Omega_e/\gamma$，因而冷谐波面只是参考位置。吸收后能否产生电流，还要看速度分布不对称、碰撞和捕获电子。EBW 的 $N_\parallel$ 可沿路显著演化，发射时选定方向并不意味着吸收处谱保持原样。对于过密球形托卡马克，EBW 是有吸引力的候选方案，但不能从“局部可吸收”直接推导“反应堆总效率足够”。[UKAEA：STEP EBW 电流驱动会议摘要，2023 年登记](https://scientific-publications.ukaea.uk/papers/electron-bernstein-wave-ebw-current-drive-profiles-and-efficiency-for-step/)

## 设备组成与接口

前端仍是微波源、传输线、真空窗、极化器和可调发射光学；特殊之处在于边缘转换层本身也是整个系统的一部分。发射器应能在所需角度范围调节，波束曲率和束宽应与转换窗口匹配。窄束可以提高局部功率密度，却具有较宽角谱，可能有更多功率落到转换角窗口之外。

密度诊断需要覆盖转换层及其梯度，而不能只测线平均密度或核心密度。反射计、Thomson 散射和磁平衡提供不同约束；偏振标定则需要追踪沿镜链和窗口后的实际椭圆偏振。测得边缘平均剖面还不够，因为涨落会使转换层位置与最佳入射条件随时间变化。[Urban 等，§2.1 对波束与涨落的讨论](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

接收 EBW 发射的系统采用相反的转换链：内部辐射先转成电磁波才能被外部天线看见。因而接收亮度同时包含电子温度、光学厚、模转换及接收模式匹配，不能默认“测得的辐射温度就是当地 $T_e$”。[Preinhaelter 等，MAST 发射实验论文，§II–§III](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/RSIVOL74p1437.pdf)

## 设计计算与仿真

O-X 局部转换的一项常用近似为

$$
C_{OX}\simeq\exp\left\{-\pi k_0L_n\sqrt{\frac{Y}{2}}
\left[2(1+Y)(N_\parallel-N_{\parallel,opt})^2+N_{pol}^2\right]\right\}.
$$

$k_0=\omega/c$ 为 $\mathrm{m^{-1}}$，$L_n=|n_e/(dn_e/dx)|$ 为 m，$x$ 沿局部密度梯度；指数无量纲，$C_{OX}$ 是功率比例。该式适用于相应一维、近平面波转换近似，表达的是 O-X 一步，而不是整条 O-X-B 链的实际效率。它揭示在固定偏离最佳角度时，较大的 $k_0L_n$ 使角窗口更窄；真实二维曲率、波束角谱、偏振错误和涨落仍需全波计算。[Urban 等，式 (2) 与后文限定](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

作为量纲算例，取 $Y=0.5$、$k_0L_n=10$、$N_{pol}=0$，最佳条件处该近似给 $C_{OX}=1$；若 $|N_\parallel-N_{\parallel,opt}|=0.1$，则约为 0.624。这个理想数值不包含 X-B 损失或核心吸收。总沉积可用预算式

$$
P_{dep}=P_{src}\eta_{tr}C_{OX}C_{XB}A_B
$$

表达，其中各无量纲因子依次为传输、O-X、X-B 和转换后 EBW 吸收比例；存在多程、分支耦合时要改用相应的能量流模型。即使每一项都达到 0.8，四项乘积也只有 0.4096，这说明不能只报告最有利的单项转换效率。

计算上先用全波模型处理截止和转换层，再把合适的输出分支交给热色散射线/波束与动理学吸收模型。不能在冷模型的 UHR 奇点上用网格耗散冒充物理 EBW 吸收。全波能量流、边界反射、网格与碰撞参数需独立收敛；吸收位置还应对剖面重建误差做敏感性分析。

模型中的边缘不确定性应直接传到效率区间。举例说，密度剖面向外移动会同时改变 O 模截止、上杂层和波束到达它们时的方向；单独扫描 $L_n$ 而固定其它几何只能检验一个理想因素。若时间平均剖面给出最佳转换，也不保证实际波动剖面的平均效率相同，因为指数函数的平均通常不等于把平均参数代回公式。做定量结论时需使用诊断时间分辨率所支持的剖面集合，并传播标定误差。[Urban 等，§2.1 的二维与密度涨落限制](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/NFVOL51p083050.pdf)

另一个独立检查是热化与电流的能量路径。若高次谐波在外层先吸收，仍可观察到边缘温度或辐射变化，但目标核心并未得到预期功率。若电子尾明显偏离 Maxwell 分布，用热电子模型解释发射和驱动可能给出不同偏差。因此在宣称核心 EBW 加热时，必须让转换证据、源的空间位置及电子能量变化相互一致，不能只引用“过密时仍看到微波”。[MAST 历史加热实验的不同沉积工况](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/AIPCONFPROC933p323.pdf)

## 控制与保护

角度、偏振和边缘剖面共同控制转换，因此一个固定的机械镜角不能适应所有放电。若密度梯度位置改变，原先匹配的束可能变为强反射；未转换功率可以进入壁面或诊断。保护链需要源功率、反射、杂散辐射、窗温和真空信息，而不是只看核心温度是否升高。

转换层局部场增强也可能产生非线性过程。MAST 的历史实验在某些工况下观察到与 UHR 相关的参数衰变信号，并且转换成功时仍可能因高谐波外层吸收而使核心加热很弱。这说明“发现转换层特征信号”与“满足核心加热目标”必须分开检验。[Shevchenko 等，Electron Bernstein Wave Studies in MAST，实验讨论](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/AIPCONFPROC933p323.pdf)

控制优化应同时记录转换、吸收及壁面能量去向；在没有真实窗、源与装置保护参数时，本文不规定统一的功率密度阈值。

## 测试与验收

先用低功率扫描测定极化、束宽和发射角，再将实测边缘剖面输入转换模型，比较最佳角度和角窗口的形状。角度匹配只验证部分传播链，不能据此给出未测量的核心吸收比例。

发射诊断可以帮助寻找转换窗口，但把发射转换反推为注入效率需要同频率、同模式、相应线性传播与接收耦合条件；非热电子尾或高功率非线性会破坏最简单的温度解释。MAST 2003 年论文在比较发射谱时明确讨论模型与测量的差异、磁平衡和吸收层位置的不确定性，是如何保留边界而不是只摘最高效率的实例。[Preinhaelter 等，§III 与图 6](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/RSIVOL74p1437.pdf)

加热验收应比较有/无功率或调制实验中的电子能量变化，并解释辐射、电子离子交换和输运；储能变化不全等于直接 EBW 沉积。电流驱动还需独立的电流剖面证据。多次角度与密度扫描能够识别可重复的模转换窗口，也能暴露平均剖面掩盖的波动影响。本页尚没有本团队的 EBW 实验测量记录。

## 文献与案例

本轮实际读取 Urban 等 2011 年原论文的波物理与转换公式、MAST 2003 年发射论文全文和 2007 年实验会议论文的相关实验章节。前者包含数值参数研究，后两者包含特定装置的历史证据；它们都不等于已验证未来反应堆全功率系统。STEP 资料本轮读取范围为机构会议摘要，正文只引用其研究性质和物理问题。

保留原入口：[斯图加特大学：伯恩斯坦波实验](https://www.igvp.uni-stuttgart.de/en/research/plasma-dynamics-and-diagnostics/projects/bernstein-wave/)。该地址本轮直接访问返回 404，暂作为历史入口保留，不以其未读取内容支持结论。相关电磁波基础见 [电子回旋加热](../电子回旋加热/README.md)。

[返回辅助加热](../README.md) · [编写说明](../../编写说明.md) · [返回知识库](../../README.md)
