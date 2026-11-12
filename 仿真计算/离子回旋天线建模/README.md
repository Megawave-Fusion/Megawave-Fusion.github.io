# 离子回旋天线建模

先建立能解释馈电、回流和负载的最小天线，再增加法拉第屏、真实等离子体和匹配网络。这里按建模过程给出结构、方程、输入与可核对的输出；芯部吸收和快尾另见[离子回旋加热模拟](../离子回旋加热模拟/README.md)，物理与设备见[离子回旋加热](../../辅助加热/离子回旋加热/README.md)。

| 要建的模型 | 适合先回答的问题 | 起步时保留的结构 |
| --- | --- | --- |
| 单电流带（strap）与回流腔 | 单元阻抗、局部场、几何敏感性 | 馈入、带、接地回流、金属腔和开口 |
| 双电流带 | 同相/反相/行进相位对谱与互耦的影响 | 两套端口、实际间距、共同边框 |
| 四电流带与谐振双环 | 两侧馈电、支路调谐与负载变化 | 辐射面和外部电路分别求解，再连接 |
| 三电流带 | 调电流幅相能否降低边框近场 | 中央/外侧带、侧限制器及感应电流 |
| 行波阵列（TWA） | 多单元耦合、带宽、方向谱与出口余功率 | 阵列多端口、电容、输入/输出与终端 |

前三类是常用的基线或装置结构；三带介绍 ASDEX Upgrade 的设计思路，TWA 介绍特定论文中的研究模型。带数不是完整型号，共轭 T 也不是带数的别名。资料读取至 2026-11-12；图和数值均明确区分文献模型与本库教学模型。

![五类天线的辐射带排列概览，馈电、回流与匹配网络分别建模。](/assets/diagrams/icrf-common-antennas.svg)

## 建模层级与几何参数卡

### 几何、负载和电路分三层

建立局部右手坐标：$x$ 指向等离子体，$y$ 为极向，$z$ 为环向。带的长向常近似沿 $y$，回流经侧壁/背板形成回路；局部磁场可倾斜，故 $E_\parallel=\mathbf E\cdot\mathbf B_0/B_0$，不能永远用 $E_z$ 代替。

| 参数卡 | 应保存的量 | 本文使用的明确基线 |
| --- | --- | --- |
| 几何与材料 | 带宽/高/厚、凹入、腔体、短路、屏、馈通与圆角 | Maquet 2023 单带：130/280/15 mm，凹入 40 mm，箱深/宽 200/200 mm，55 MHz |
| 等离子体 | 磁场方向、组分、密度剖面、坐标原点、碰撞和开放边界 | 先均匀张量，再一维剖面；上述尺寸不是完整 CAD 或放电输入 |
| 电路 | 端口模/参考面/阻抗、幅相、电容和终端 | 先输出每端口响应，再连接真实馈电；电容不由带长单独决定 |

先求真空 S/Z 与冷测量，再加负载；最后恢复曲率、屏栅和细节。2D 截面适合查色散与边界，有限长带的端部、馈电和旁路电流需三维模型。表中尺寸来自[Maquet 等 §2.2、表 1](https://arxiv.org/html/2309.14015v1)，不是可直接复刻 WEST 的完整工程设计。

![天线辐射面、回流腔、端口与边缘负载的建模层级。](/assets/diagrams/icrf-model-hierarchy.svg)

## 单电流带的回流路径与谐振近似

### 先闭合电流，再讨论场

最小三维模型包含一条带、馈入间隙或同轴线、短路连接和接地腔。只放一块悬浮矩形金属再加电压，可能改变回流与电容。网格先解析带边、馈电间隙、短路和开口；比较端口阻抗、表面电流及开口场，而不只看远处波纹。[TOPICA 原论文](https://iris.polito.it/handle/11583/1406792)同时处理带、腔体、屏与同轴馈电，适合作为几何完整性的参照。

电尺寸较小的电路起步模型可写为

$$
Z_s=R_{\rm load}+R_\Omega-i\omega L+\frac{i}{\omega C},\qquad
\omega_0=\frac1{\sqrt{LC}}.
$$

这里采用 $e^{-i\omega t}$、RMS 电压电流，$L,C$ 是提取/拟合的等效参数，不是材料常数。教学取 $L=100$ nH、$f_0=50$ MHz，得 $C=101.32$ pF。若带上电流幅相明显变化，就改用分布传输线或三维场；短路端、电容调谐和等离子体负载共同决定电流形状，不把所有 strap 都当自由空间半波振子。

谐振使输入虚部过零，未必使实部等于 50 Ω；电路通过还要检查带、间隙和馈通上的峰值电压。可对照 [WEST 模型的电容与调谐定义](https://west-ic-antenna.readthedocs.io/en/latest/introduction.html)。

## 双电流带的间距、相位与发射谱

### 电流谱先做解析检查

设两条宽 $w$ 的均匀薄带沿 $z$ 相隔 $d$，总带电流为 $I$ 与 $I e^{i\Delta\phi}$。每带面电流密度为 $K_y=I_p/w$（A/m），带宽以外为零。对空间变换 $\widetilde J(k_z)=\int K_y(z)e^{-ik_zz}dz$，归一化电流谱为

$$
\frac{|\widetilde J(k_z)|^2}{|I|^2}
=\operatorname{sinc}^2\!\left(\frac{k_zw}{2}\right)
\left|1+e^{i(\Delta\phi-k_zd)}\right|^2,
\quad \operatorname{sinc}u=\frac{\sin u}{u}.
$$

同相在 $k_z=0$ 相加，反相在该处相消；$\Delta\phi=\pm\pi/2$ 使谱偏向不同方向。这个量是规定电流的 Fourier 谱，功率谱还要用等离子体响应和 Poynting 通量计算。局部 $k_\parallel$ 则由波矢对总磁场投影得到。[TWA 论文 §4–5](https://arxiv.org/html/2301.10754v1)明确区分电流设计与实际开口功率谱。

教学取 $w=0.06$ m、$d=0.18$ m，反相阵列因子的第一对峰在 $k_z=\pm\pi/d=\pm17.45$ m⁻¹；乘单带包络后，该点谱值为 3.6476，完整谱峰位置略变。保持每带电流相同是谱检验；比较实际效率时应重归一到相同接受功率，并从含互耦的网络求实际带电流。

![有限带宽与双带相位共同决定规定电流谱，曲线不是等离子体功率谱。](/assets/diagrams/icrf-two-strap-spectrum.svg)

## 四电流带与共轭 T 的电路连接

### 辐射阵列和匹配拓扑分别建立

WEST 的公开模型为 2 个环向位置乘 2 个极向位置、共 4 条带，两侧馈电并用串联电容形成内部共轭 T。上下带的支路构成谐振双环（resonant double loop，RDL）；先把辐射面导出为四端口网络，再接电容、传输线与 T 点，保留上下及左右互耦。[WEST 结构与电路说明](https://west-ic-antenna.readthedocs.io/en/latest/introduction.html)、[理想双环负载例](https://west-ic-antenna.readthedocs.io/en/latest/coupling_to_ideal_load.html)。共轭 T 是网络拓扑，不能由带数直接推断，也不能据此推断 ITER 的完整带数。

在忽略支路互耦、两支路已经变换到同一 T 点的教学模型中，令 $Z_1=R+iX$、$Z_2=R-iX$，则

$$
Y_T=\frac1{Z_1}+\frac1{Z_2}=\frac{2R}{R^2+X^2},\qquad
Z_T=\frac{R^2+X^2}{2R}.
$$

取 $X=6$ Ω，$R=2,6,18$ Ω 分别给 $Z_T=10,6,10$ Ω。两支路同变与一侧独变应分开扫：不平衡时 T 点一般重新出现虚部。电路需检查有源反射、电容电压和支路电流，而不只要求某次静态 $S_{11}$ 最小。实际负载容忍与电弧检测见 [JET external conjugate-T 原论文 §2–5](https://arxiv.org/pdf/1309.4644)；这不是固定负载无限容忍的保证。

![四带辐射面与两个独立支路 T 点的概念连接，实际网络仍含带间互耦。](/assets/diagrams/icrf-four-strap-network.svg)

## 三电流带的边框电流与近场优化

### 中央带不是简单复制第三个端口

三带方案通过中央与两侧电流的幅相配合，改变天线框架、限制器上的感应电流和相关平行近场。优化模型应保留侧限制器、接地连接、磁场倾角和观测位置；只比较三条孤立带的自由空间远场，不能判断金属壁杂质源。ASDEX Upgrade 的实验证据见[三带天线首轮结果摘要](https://portal.fis.tum.de/en/publications/first-results-with-3-strap-icrf-antennas-in-asdex-upgrade/)，近场与谱的设计逻辑见 [Maquet 等 §1、§5](https://arxiv.org/html/2301.10754v1)。

一个仅用于理解低波数抑制的对称电流例是 $I(1,-2,1)$，位置为 $(-d,0,d)$：

$$
\widetilde J\propto I(e^{ik_zd}-2+e^{-ik_zd})
=2I[\cos(k_zd)-1]\simeq-I(k_zd)^2.
$$

这说明总电流和一阶空间矩同时相消；它不是 AUG 的通用最优电流比，也不保证近场最小。实际先在其余端口匹配终接时，提取单位入射功率波幅的端口场 $\mathbf E_p$，再按 $\mathbf E=\sum_p a_p\mathbf E_p$ 合成，在固定接受功率和电压约束下最小化指定表面上的 $E_\parallel$ 与边框电流；鞘层电压和溅射需进一步模型。

![规定两带和三带电流的低波数谱对比；只统一电流幅度平方和，不是等耦合功率比较。](/assets/diagrams/icrf-three-strap-spectrum.svg)

## 行波阵列的多端口与终端余功率

### 先算单元互耦，再闭合两端馈电

TWA 依靠耦合单元、电容与终端形成沿阵列的电流。Maquet 2023 的 WEST 研究以每排 7 单元为模型：先求七端口 S 矩阵，接各单元电容，再在首末单元设置输入/输出，得到两端口网络。其平板化几何及等效负载属于该论文的研究设定，不能写成已部署装置性能。[原论文 §2–5](https://arxiv.org/html/2301.10754v1)。

输入端 1 激励、输出端匹配时，按相同实参考阻抗定义

$$
\frac{P_{\rm coupled}+P_\Omega}{P_{\rm in}}
=1-|S_{11}|^2-|S_{21}|^2.
$$

这里 $P_{\rm coupled}$ 指净交给等离子体的功率，可包含其内部耗散及向等离子体传播区的净出射通量；它不一定已在天线计算域内热化。除两端口外只保留这一路和金属损耗时，上式闭合；仅在金属与其他损耗可忽略时，差值才等于目标等离子体耦合效率。教学取 $|S_{11}|=0.1$、$|S_{21}|=0.7$，有 1% 反射、49% 出口功率、50% 向等离子体交付或在金属中损耗。输出接假负载、回收环或另一网络时，终端反射会改变全阵列电流，必须重新连接求解。

![行波阵列由多端口电磁响应和电容网络连接成两端口，出口功率单独记账。](/assets/diagrams/icrf-twa-termination.svg)

## 同轴端口、互耦与参考面

### 从单端口激励得到共同网络

在均匀同轴截面设置 TEM 波端口，逐端口激励并匹配终接其余端口，得到 S 的各列；集总/电压间隙端口适合约化馈电，需保存参考导体、积分线及电压正方向。端口面应避开强不连续区，并核对所选高阶模。去嵌是移动参考面，重归一是改变参考阻抗，后处理设成 50 Ω 不会把真实天线负载变成 50 Ω。去嵌应沿已知的均匀馈线进行，不跨过任意不连续结构。[Ansys 端口后处理说明](https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v242/en/Subsystems/HFSS/Content/HFSS/PostProcessingWavePorts.htm)还区分网络参数和场的后处理；WEST 的[COMSOL 网络接口例](https://west-ic-antenna.readthedocs.io/en/latest/coupling_to_plasma_from_COMSOL.html)显式调整端口排序。

对所有端口相同的实 $Z_0>0$，RMS 复电压电流定义功率波：

$$
a_p=\frac{V_p+Z_0I_p}{2\sqrt{Z_0}},\quad
b_p=\frac{V_p-Z_0I_p}{2\sqrt{Z_0}},\quad
\mathbf b=\mathbf S\mathbf a,\quad
\mathbf Z=Z_0(\mathbf1+\mathbf S)(\mathbf1-\mathbf S)^{-1}.
$$

于是 $P_{\rm acc}=\mathbf a^\dagger\mathbf a-\mathbf b^\dagger\mathbf b=\operatorname{Re}(\mathbf I^\dagger\mathbf Z\mathbf I)$。若电压电流改用峰值相量，$a_p,b_p$ 的定义另除以 $\sqrt2$，最后的电压电流功率式乘 $1/2$。同时馈电时 $\Gamma_{{\rm act},p}=(\mathbf S\mathbf a)_p/a_p$（$a_p\ne0$），不等于单独的 $S_{pp}$。不同或复参考阻抗应采用相应广义功率波定义，见 [scikit-rf s2z 官方文档](https://scikit-rf.readthedocs.io/en/latest/api/generated/skrf.network.s2z.html)。磁化等离子体一般不保证互易，不能把 $S_{12}=S_{21}$ 当成所有模型的通过条件。

### 含互阻抗的双端口算例

规定被动网络 $\mathbf Z=\begin{pmatrix}2-20i&0.5-4i\\0.5-4i&2-20i\end{pmatrix}$ Ω，取 RMS 电流 $(100,100)$ A 或 $(100,-100)$ A。同相接受功率为 50 kW，反相为 30 kW；对角项都没变，差异来自互阻抗。这个给定网络检验不从几何预测加载，实际 Z 应由场求解或测量得到。[WEST 有源馈电示例](https://west-ic-antenna.readthedocs.io/en/latest/introduction.html)给出互耦改变匹配点的真实建模背景。

## 法拉第屏、有限电导与局部近场

### 理想屏用于起步，屏条几何用于应力

先用 PEC 带和腔体检查几何电流；理想屏边界可用于快速谱计算。关心屏条端部、间隙场、欧姆热或鞘层驱动时，加入屏条的截面、节距、倾角、端部连接及圆角；既要保持电流回路，也要恢复相对于总磁场的方向。屏存在不意味着 $E_\parallel$ 处处为零。TOPICA 的[三维结构模型](https://iris.polito.it/handle/11583/1406792)与 TWA 的[有/无屏对照 §5](https://arxiv.org/html/2301.10754v1)提供两种层级。

对良导体且趋肤近似成立，表面电阻与深度为

$$
\delta=\sqrt{\frac{2}{\omega\mu\sigma}},\qquad
R_s=\sqrt{\frac{\omega\mu}{2\sigma}},\qquad
P_\Omega=\int_A R_s|\mathbf H_{t,\rm RMS}|^2\,dA.
$$

教学给铜 $\sigma=5.8\times10^7$ S/m、$\mu=\mu_0$、50 MHz，得 $\delta=9.35$ μm、$R_s=1.845$ mΩ；涂层、接触和温升另用其实际材料数据。有限导体可用满足适用条件的表面阻抗避免体网格穿透全部趋肤深度，相关基础见 [MIT 电磁场教材 §10.7](https://web.mit.edu/6.013_book/www/chapter10/10.7.html)。

尖角最大场可能随网格发散。比较时保留真实圆角，并固定离壁距离/面积定义场指标。沿连接材料的规定磁力线保留复相位积分 $V_{\rm RF}=\int E_\parallel d\ell$，而不是先取各点 $|E_\parallel|$ 再相加；它是鞘层的 RF 驱动量，整流直流鞘势及粒子热流还需鞘层模型和背景输入，见 [Stix 鞘层边界研究摘要](https://arxiv.org/abs/2306.12930)。不能把单个网格点最大场直接乘任意长度。

## 边缘等离子体与开放边界

### 从色散基准增加到剖面负载

真空腔外先设均匀冷等离子体，检查波长、极化和旋转张量；再加入实测或规定的一维密度剖面、磁场倾角及多组分。最后用二维/三维剖面和真实曲率。密度剖面的坐标零点、梯度与截止位置共同影响穿过衰逝区的耦合。单谱、局部缓变近似给场幅因子 $\exp[-\int\kappa(x)dx]$，其平方用于估计两侧传播模之间的透射强度尺度；它不是纯衰逝场自身的径向净 Poynting 功率，也不替代完整负载计算。

在 $e^{-i\omega t}$ 下，局部波方程与张量旋转写为

$$
\nabla\times\mu_r^{-1}\nabla\times\mathbf E-k_0^2\boldsymbol\epsilon_r\mathbf E
=i\omega\mu_0\mathbf J_{\rm ext},\qquad
\boldsymbol\epsilon_{\rm lab}=\mathbf Q\boldsymbol\epsilon_B\mathbf Q^T.
$$

$\mathbf Q$ 的列为磁场局部基矢在实验室系的坐标。取正的阻尼率并验证被动介质做功非负；非负耗散对应张量的反厄米部分，不要求每个矩阵元素的虚部都为正。软件若采用 $e^{+i\omega t}$，复响应和激励一起转换，不能只抄非对角项符号。

### PML 和吸收层按实现分别核对

RAPLICASOL 使用冷张量与 PML；Maquet 2023 的 HFSS 实现为避开大 Stix $P$ 的数值困难，使用等效电导张量和优化吸收层 ABL，论文未实现 PML。ABL、碰撞耗散及芯部热吸收分开记账。扩大域、改变层厚与损耗渐变，检查带阻抗和返回波；真空辐射边界不能自动代表磁化等离子体的出射条件。软件实现和这一层基准见 [HFSS 作者论文 §2–3](https://arxiv.org/html/2309.14015v1)；[Tierens 等官方作者摘要](https://impact.ornl.gov/en/publications/validation-of-the-icrf-antenna-coupling-code-raplicasol-against-t/)列出双带/四带模型的共同几何、S/Z、匹配和 RF 场对照。

![从带、屏和真空腔，到密度剖面、传播域与吸收层的计算域示意。](/assets/diagrams/icrf-domain-boundaries.svg)

## 软件分工与可复算建模流程

### 每次增加一种复杂性

| 工具或模型 | 用于哪一步 | 必须另给的输入/边界 |
| --- | --- | --- |
| 本库解析电流谱与给定 Z 网络 | 检查幅相、功率波和归一化 | 规定电流或给定阻抗，不从 CAD 预测负载 |
| ANTITER | 平板/谱模型的负载、相位及吸收边界基准 | 具体版本的几何与等离子体近似 |
| TOPICA | 三维导体与谱等离子体响应连接、S/Z 及表面电流 | 常用分层等离子体响应；不是任意三维全局热等离子体 |
| RAPLICASOL / COMSOL | 三维天线近场、冷等离子体及 PML | 软件模型文件、张量、网格与 PML 实现 |
| HFSS 的论文实现 | 复杂导体、等效电导张量与 ABL | 论文方法的实现；默认材料库不等于完整等离子体模型 |
| WEST IC Antenna / scikit-rf | 把电磁多端口接入电容、馈线及有源匹配 | 共同端口、频率、单位、参考面和终端 |

方法依据：[TOPICA 原论文](https://iris.polito.it/handle/11583/1406792)、[HFSS 模型与 ANTITER 基准](https://arxiv.org/html/2309.14015v1)、[WEST COMSOL 接口](https://west-ic-antenna.readthedocs.io/en/latest/coupling_to_plasma_from_COMSOL.html)。商业工具主体、脚本、等离子体模块和外部数据的获取条件分别落实。

### 三维初始模型怎样搭建

| 操作 | 输入与设置 | 本阶段要留下的结果 |
| --- | --- | --- |
| 几何与材料 | 统一长度单位；画带、馈入、短路、回流腔，先用 PEC 与真空 | 接通的电流路径、带面/馈入方向、单端口真空阻抗 |
| 建端口 | 在均匀同轴段选 TEM 模；固定实参考阻抗与参考面 | 逐端口 S 参数、模阻抗、端口编号与方向 |
| 加等离子体 | 均匀冷张量检查通过后，替换为相同原点的一维剖面 | 波长、极化、截止位置、物理耗散与返回波 |
| 接馈电网络 | 导出共同参考面的多端口；加入电容/馈线，指定幅相与终端 | 实际带电流、有源反射、元件峰值电压和功率收支 |
| 恢复细节 | 加屏、曲率、圆角和有限电导；分项加密 | S/Z、近场与损耗相对前一级的变化及网格误差 |

用仓库内脚本运行下面的谱/网络小例子，无需安装电磁求解器：

```sh
.venv/bin/python scripts/icrf_antenna_examples.py
.venv/bin/python tests/icrf_antenna_checks.py
```

输出在 `.build/icrf-antenna/`：参数 JSON、双带电流谱 CSV、互耦功率与共轭 T 扫描，以及图示重建结果。正式三维模型沿“真空冷测 → 均匀色散 → 剖面负载 → 网络连接 → 几何细化”推进，分别扫描网格、端口距离、剖面平移及吸收层。检查接受功率等于金属、物理等离子体耗散和出域功率之和；比较 $R_c$ 时使用同一位置的电流定义，最后才把近场和实际带谱交给[ICRH 吸收与分布模型](../离子回旋加热模拟/README.md)。

[返回仿真计算总览](../README.md)
