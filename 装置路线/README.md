# 装置路线

不同聚变路线解决的是同一个问题：在足够高的反应率下，让燃料保留足够长时间，并将粒子、热量和中子送往能够承受它们的部件。区别首先在磁拓扑、压力与约束时间，其次才是装置外形。这里介绍基本原理和证据边界，不把某次高温、长脉冲或中子产生直接称为发电成功。内容经来源与解析算例检查，仍为知识整理稿；资料访问日期为 2026-10-16。

## 托卡马克

### 螺旋磁场与安全因子

托卡马克以近似轴对称的环形磁面约束等离子体。外部环向场线圈提供主要环向磁场，等离子体环向电流产生极向场；外部极向场线圈同时参与位置、形状和平衡控制。两种场叠加使磁力线绕着磁面螺旋前进。只有环向场时，曲率和梯度漂移不能充分抵消，因此“把磁场弯成圆环”本身不够。[IPP《Tokamak》，磁场组成与电流驱动段](https://www.ipp.mpg.de/9778/tokamak)。

安全因子 $q$ 表示磁力线绕极向一周时的环向圈数。在大环径比、近圆截面且局部磁场近似成立时，

$$
q(r)\simeq\frac{rB_\phi}{R_0B_\theta(r)},\qquad
B_\theta(r)\simeq\frac{\mu_0I_p(r)}{2\pi r}.
$$

$r,R_0$ 为小半径与主半径，单位 m；磁场单位 T；$I_p(r)$ 是所包围的电流，单位 A。式子来自磁力线几何和安培环路定律，不能原样用于强整形、球形托卡马克的精确平衡。举一个解析教学例：取 $r=0.5\,\mathrm m,R_0=2\,\mathrm m,B_\phi=3\,\mathrm T,I_p(r)=0.5\,\mathrm{MA}$，得到 $B_\theta=0.20\,\mathrm T,q\simeq3.75$。这里的 $q$ 不是设备安全系数，更不意味着“超过某数就没有不稳定性”。撕裂模对 $q=m/n$ 的有理磁面敏感，判断稳定性还要看电流、压力、剪切、旋转与壁面条件。[Fitzpatrick，撕裂模讲义，式 (4.35)–(4.40)](https://farside.ph.utexas.edu/teaching/plasma1/Fusionhtml/node71.html)。

### 电流维持、稳态和破裂

变压器感应电流需要磁通变化，可用的磁通摆幅有限，因此纯感应驱动通常是脉冲运行。非感应方案由外加波或束流驱动电流，并利用压力梯度产生的自举电流；稳态要求电流剖面、热量、密度、杂质和壁温都能维持。超导线圈使长时磁场成为可能，但不会自动解决等离子体电流维持及排热。[IPP《Tokamak》，末两段](https://www.ipp.mpg.de/9778/tokamak)。

从磁能看，变化的电流不能瞬间消失：简化电路满足 $V=L\,dI/dt+RI$。托卡马克破裂可能伴随快速热能损失、随后电流下降、电磁载荷及逃逸电子。热能 $W$ 在较短时间 $\Delta t$ 释放时，平均释放功率约为 $W/\Delta t$；落点面积和辐射分配又决定局部热流，不能只按总能量评价损伤。ITER 的破裂缓解系统是面向未来运行的工程设计，不能写成已经在 ITER 等离子体上完成验证。[ITER《Disruption mitigation》，破裂后果与系统方案](https://www.iter.org/machine/supporting-systems/disruption-mitigation)。

球形托卡马克通过较小环径比 $A=R_0/a$ 改变平衡和稳定性条件，常研究较高的归一化压力，但中央柱、屏蔽和维护空间也更紧。常规与球形装置比较时，必须同时报告压力定义、磁场位置、等离子体体积及加热功率，而不能只比较峰值温度。

## 场反位形 FRC

FRC 是以极向磁场为主、环向磁场很小或没有宏观环向磁场的紧凑环形构型。环向电流产生与外加轴向场相反的内部磁场；分离面区分闭合磁力线区和外部开场线区。其较高的等离子体压力与外部磁压相平衡，适合用外部参考场定义

$$
\beta_{\rm ref}=\frac{2\mu_0\langle p\rangle}{B_{\rm ref}^{2}}.
$$

$p$ 用 Pa，$\beta$ 无量纲。必须写清体平均范围和 $B_{\rm ref}$：磁场反转附近可能有磁零点，把局部 $p/B^2$ 的大值直接称为整机高效率没有意义。高 $\beta$ 表示相对于参考磁场的压力较大，并不直接给出能量约束时间或聚变增益。

FRC 的离子轨道可与装置尺度可比。定义 $\rho_i=v_\perp/\Omega_i$、$\Omega_i=Z_ieB/m_i$，则 $\rho_i/a\ll1$ 才有利于局部导引中心近似。教学例取氘离子垂直动能 $10\,\mathrm{keV}$、参考场 $0.5\,\mathrm T$，由 $v_\perp=\sqrt{2E_\perp/m_D}$ 得 $\rho_D\approx0.041\,\mathrm m$；若 $a=0.20\,\mathrm m$，比值约 0.20，不能忽略有限轨道宽度，靠近磁零点时更须完整轨道处理。

因此，纯理想 MHD 对倾斜模的预测与实验表现之间，可能需要离子动理学、快离子、流动和导电壁解释。Belova 等的混合模拟研究具体分析了倾斜模、旋转模和束离子稳定作用，结论依赖构型与模型，不能概括成“FRC 天生稳定”。[PPPL-4150 / Physics of Plasmas 13, 056115 (2006)，摘要及动力学稳定性分析](https://bp-pub.pppl.gov/pub_report/2006/PPPL-4150.pdf)。

形成方式包括磁场反转的脉冲形成与等离子体合并；维持方案可涉及中性束注入或旋转磁场。旋转磁场通过电子响应驱动电流，不等于“任何射频都能维持任意 FRC”。诊断要分别给出分离面、磁通、密度、电子/离子温度、快离子分布、输入功率和持续时间。PPPL 的 PFRC 是其中一种特定射频驱动研究方案，而不是所有 FRC 的共同参数。[PPPL《Princeton Field-Reversed Configuration》，概念说明](https://www.pppl.gov/Princeton-Field-Reversed-Configuration)。

## 磁镜

磁镜以中部较弱、两端较强的磁场使部分带电粒子反射。若磁场沿轨道变化足够缓慢，磁矩 $\mu=mv_\perp^2/(2B)$ 近似守恒；在静态、可忽略电势差的条件下，总动能也守恒。粒子走向强场时，垂直能增加、平行能减少，到 $v_\parallel=0$ 处反射。这是速度空间选择机制，不是两端有完全封闭的“磁门”。[Fitzpatrick《Magnetic Mirrors》，式 (2.83)–(2.90)](https://farside.ph.utexas.edu/teaching/plasma/Plasma/node22.html)。

设镜比 $R_m=B_{\max}/B_{\min}$，中部俯仰角 $\alpha$ 为速度与磁场的夹角，则理想捕获条件为

$$
\sin^2\alpha>\frac1{R_m},\qquad
\alpha_{\rm lc}=\arcsin\!\left(R_m^{-1/2}\right).
$$

接近平行或反平行方向的两个锥区称为损失锥。若 $R_m=4$，半角为 $30^\circ$。对于中部初始速度方向各向同性的粒子，两端损失锥占总立体角的比例为 $1-\cos\alpha_{\rm lc}\approx13.4\%$。这个数只描述该理想瞬间的几何比例，不是稳态损失率：碰撞会持续向损失锥散射粒子，电势差会改变逃逸条件，分布各向异性也可能驱动不稳定性。

镜装置的工程特点是端部可用于加热、排气与能量收集，但端损失同时成为核心约束问题。单纯增大镜比并不能按同一比例增加约束时间；低碰撞与气体动力学工况、端部膨胀区和电子约束的机制不同。评价磁镜结果应将中心温度、径向剖面、端损失功率与注入束能量分开，尤其不能把高能束离子的平均能量直接当作热化离子温度。相关的碰撞与分布函数见[动理学与碰撞](../基础原理/动理学与碰撞/README.md)。

## 仿星器

仿星器依靠外部三维线圈产生主要约束磁拓扑，不需要像通常的托卡马克那样依靠很大的环向等离子体电流产生磁场扭转。这提供了稳态运行的物理基础，却也把难题转移到三维粒子轨道、线圈制造与排热几何。实际仿星器仍可能有自举电流和其他电流；“不需要主要驱动电流”不能写成“等离子体处处没有电流”。[IPP《Stellarator》，外部线圈与优化段](https://www.ipp.mpg.de/9792/stellarator)。

旋转变换在本文约定为每绕环向一周的极向圈数，

$$
\iota=\lim_{N\to\infty}\frac{\Delta\theta}{2\pi N},\qquad \Delta\phi=2\pi N.
$$

$\theta,\phi$ 为适当磁面坐标中的极向与环向角。采用相同方向约定时 $\iota=1/q$。例如 $\iota=0.5$ 的磁力线每环向一圈走极向半圈；在理想有理磁面上两圈闭合。实际三维场可能含磁岛和随机区，因此需要 Poincaré 截面，而不能用一张圆环示意图断言存在完整磁面。W7-X 的电子束磁面测绘提供了对真空磁拓扑的直接检验；该测量不等于同时验证高温等离子体的输运。[Pedersen 等，Nature Communications 7, 13493 (2016)，Results 中旋转变换与磁面测量部分](https://www.nature.com/articles/ncomms13493)。

磁力线留在磁面上，也不保证粒子的漂移轨道都留在其中。优化的目标包括减少新经典输运、改善快粒子约束、控制自举电流和保持可制造线圈。W7-X 的实验剖面与输运计算对比支持了新经典优化的有效性，但湍流、杂质和长脉冲排热仍是独立问题。[Beidler 等，Nature 596, 221–226 (2021)，摘要与输运比较](https://www.nature.com/articles/s41586-021-03687-w)。

## 其他路线

### RFP、球马克与 Z-pinch

反场箍缩 RFP 的环向与极向场可处于相近量级，环向场在边缘反号。球马克同时包含等离子体自身产生的环向和极向场，其紧凑环形磁拓扑不依赖穿过中心孔的常规环向场线圈；这与主要为极向场的 FRC 有本质区别。两者涉及电流维持、自组织和磁重联。低压力的理想化 Taylor 松弛态满足 $\nabla\times\mathbf B=\lambda\mathbf B$，$\lambda$ 的单位为 $\mathrm{m^{-1}}$，于是 $\mathbf J\times\mathbf B=0$。这不是所有高压实际等离子体的精确状态，有限压力平衡仍须满足力平衡。[PPPL 暑期课程《Other Fusion Concepts》2025，Spheromak / Reversed Field Pinch 页](https://suli.pppl.gov/2025/course/SY%20-%202025-06%20-%20PPPL%20SULI%20-%20Other%20Fusion%20Concepts.pdf)。

Z-pinch 由轴向电流产生周向磁场并压缩等离子体；长直柱外部近似 $B_\theta=\mu_0I/(2\pi r)$。这是磁压来源的估算，不是稳定性证明。箍缩、扭曲等 MHD 模可能限制寿命，剪切流等稳定方案必须由有诊断与误差的实验检验。RFP 则可通过磁涨落、温度和电流剖面测量研究自组织与输运，MST 是相应实验平台。[Wisconsin Plasma Physics Laboratory，MST 装置说明](https://wippl.wisc.edu/madison-symmetric-torus/)。

### 惯性约束与磁惯性约束

惯性约束 ICF 依靠快速压缩燃料，使反应在燃料显著膨胀前发生；关键量包括压缩密度、面密度 $\rho R$（$\mathrm{kg\,m^{-2}}$）和驱动对称性。靶增益 $G_{\rm target}=E_{\rm fusion}/E_{\rm driver,target}$ 的分母是到靶驱动能量。LLNL 报告 2022-12-05 的 NIF 实验以到靶激光能量 $2.05\,\mathrm{MJ}$ 得到约 $3.15\,\mathrm{MJ}$ 聚变产额，即 $G_{\rm target}\approx1.54$。这是有明确日期的实验结果，不能当作包含激光供电、冷却和发电效率的整厂净增益。[LLNL，2023-04-12，点火实验的诊断报道](https://lmf.llnl.gov/news/diagnostics-were-crucial-to-llnls-historic-ignition-shot)。

磁惯性约束 MIF 在脉冲压缩中利用磁化降低能量损失。MagLIF 组合预磁化、预热与衬套压缩；其中磁场和压缩各有作用，不能简单视为“小型托卡马克”。Sandia 的 2022 年综述区分已测得的聚变相关状态与更大驱动装置的模拟展望；后者不能作为现有装置的已实现增益。向电站延伸还须解决重复频率、驱动效率、耗材制造和腔室恢复。[Yager-Elorriaga 等，Nuclear Fusion 62 (2022)，Sandia 摘要](https://www.sandia.gov/research/publications/details/an-overview-of-magneto-inertial-fusion-on-the-z-machine-at-sandia-national-2022-04-01/)。

### 用时间尺度理解路线差异

约束路线的“长”与“短”必须相对于过程本身。假设一个系统的能量损失时间为 $\tau_E$，在没有加热、损失系数不变的教学模型里有 $dW/dt=-W/\tau_E$，故 $W(t)=W(0)e^{-t/\tau_E}$。维持十个 $\tau_E$ 的高温状态意味着持续补偿损失，而不是原来的热粒子从未离开；短脉冲惯性系统则利用膨胀前的一小段时间完成足够反应，不能把其纳秒尺度直接与磁约束的秒数比较。

诊断也必须区分热核反应与束靶反应。高能束与较冷背景燃料同样可以产生中子，因此看到中子只能首先证明发生了相应核反应；由产额反推热温度，还需要分布函数、密度体积、反应截面与反应机制的证据。对脉冲路线，应同时检查中子能谱、产额各向异性、时间宽度及背景扣除；对磁约束，则应检查快离子对反应率和储能的贡献。NIF 的诊断文章与 Sandia 的 MagLIF 综述都把诊断和模型解释作为结果的一部分，而非只报告一个最高数值。[LLNL：点火实验诊断](https://lmf.llnl.gov/news/diagnostics-were-crucial-to-llnls-historic-ignition-shot)；[Sandia：MagLIF 综述摘要](https://www.sandia.gov/research/publications/details/an-overview-of-magneto-inertial-fusion-on-the-z-machine-at-sandia-national-2022-04-01/)。

## 装置档案的记录内容

装置比较应首先固定系统边界。磁约束常用 $\tau_E=W/P_{\rm loss}$，其中 $W$ 用 J，$P_{\rm loss}$ 用 W；非稳态时由 $dW/dt=P_{\rm heat}-P_{\rm loss}$ 得 $P_{\rm loss}=P_{\rm heat}-dW/dt$。假设吸收加热为 10 MW、储能增长率为 2 MW、储能为 4 MJ，则 $\tau_E=0.50\,\mathrm s$，而直接用 $W/P_{\rm heat}$ 会得到 0.40 s。这里未包括未定义的束能库存，比较真实实验时必须统一热能与快离子能的口径。

一份可比较的档案至少对应同一放电或同一时间窗，而不是拼接最高温度、最长时长和最大密度。核心字段包括燃料组成、磁场位置、几何、电流、温度诊断、密度平均方式、吸收功率、脉冲时间、误差和原论文位置。测量值、重建值、模型外推和设计目标要分栏。$nT\tau_E$ 也须指明粒子种类与平均方式；不同路线的靶增益、等离子体增益和净电功率不应放在同一列直接排序。厂级能量边界见[工程系统](../工程系统/README.md)。

如果档案给出 $Q=P_{\rm fusion}/P_{\rm aux}$，还应确认 $P_{\rm aux}$ 是射频源输出、天线/束口功率，还是等离子体实际吸收功率；分母口径不同会直接改变数值。对加热关闭后的余辉，也不能用瞬时为零的外加功率制造“无限增益”的结论，应报告整段输入与产出的能量以及初始储能。温度由谱线展宽、散射或其他方法反演时，应同时保留仪器响应与分布模型。这些要求让不同路线有共同的证据语言，同时保留各自的物理特点。

## 参考资料

- [IPP：托卡马克](https://www.ipp.mpg.de/9778/tokamak)与[仿星器](https://www.ipp.mpg.de/9792/stellarator)：磁场与电流的入门说明。
- [Fitzpatrick：磁镜](https://farside.ph.utexas.edu/teaching/plasma/Plasma/node22.html)：磁矩、镜点与损失锥推导。
- [Belova 等，PPPL-4150，2006](https://bp-pub.pppl.gov/pub_report/2006/PPPL-4150.pdf)：FRC 混合模拟与稳定性边界。
- [PPPL：其他聚变构型课程，2025](https://suli.pppl.gov/2025/course/SY%20-%202025-06%20-%20PPPL%20SULI%20-%20Other%20Fusion%20Concepts.pdf)：紧凑环、箍缩与开放构型。
- [IAEA 聚变装置数据库](https://nucleus.iaea.org/sites/fusion-portal/SitePages/FFDB.aspx?web=1)：装置检索入口；具体性能仍以带日期的原始报告为准。

[辅助加热系统](../辅助加热/README.md) · [编写说明](../编写说明.md) · [返回知识库](../README.md)
