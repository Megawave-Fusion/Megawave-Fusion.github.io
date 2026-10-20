# 仿真计算：模型、软件与验证

聚变仿真通常是一条计算链：磁场和平衡提供几何，稳定性和湍流模型解释扰动与通量，加热和粒子模型计算源项，输运模型推进剖面，边缘模型提供排热与回收条件，工程计算接收面载荷和体热源。选软件首先要明确要预测的量、时空尺度、已有数据和可接受的近似，再决定使用哪一层模型。

本章按任务比较软件，并给出耦合接口、算例和核验方法。软件功能与获取条件按 **2026-10-20** 实际读取的官方文档、官方仓库和原始论文记录；引用固定版本时会单独注明。表中的“适合”是依据方程和工作流作出的选型判断，实际算力需用自己的目标算例测量。

可先从下表找到对应模型，再阅读软件比较；原理可与[流体与磁流体力学](../基础原理/流体与磁流体力学/README.md)、[动理学与碰撞](../基础原理/动理学与碰撞/README.md)、[输运与边界](../基础原理/输运与边界/README.md)对照。

软件对比入口：[平衡与优化](#平衡与磁场优化) · [MHD 稳定性](#线性稳定性与非线性-mhd) · [芯部输运](#芯部输运与集成放电建模) · [湍流闭合](#湍流闭合、准线性模型与代理模型) · [陀螺动理学](#陀螺动理学湍流：gene、gs2、cgyro、gtc-与-gkeyll) · [边缘与偏滤器](#边缘与偏滤器：平均输运和涨落分开比较) · [通用 PIC](#通用电磁-pic：smilei、warpx-与-epoch) · [RF 与 FP](#射频波与分布函数：射线、准光学、全波与-fp) · [快粒子](#中性束与快粒子：出生、慢化与三维轨道) · [中子学与工程](#中子学、cad-与热结构软件) · [获取条件](#获取条件和外部依赖)。

## 模型与求解器目录

### 从问题找到模型

| 要回答的问题 | 需要的模型与主要输入 | 应比较的输出 |
| --- | --- | --- |
| 已知磁测量和压力，等离子体边界、磁面和电流怎样分布 | 平衡重建；线圈/壁几何、磁测量、动理学约束（压力、电流等内部约束） | 边界、X 点、磁通、$q$ 或旋转变换、拟合残差 |
| 换一组仿星器边界或线圈，约束性质怎样改变 | 三维平衡与优化；目标函数、几何和电流约束 | 力平衡残差、磁场谱、线圈间距、优化目标及约束违反量 |
| 模是否增长，磁岛、ELM 或破裂阶段怎样演化 | 线性稳定性或非线性 MHD；平衡、耗散、闭合和边界 | 复频率、模结构、非线性饱和、能量与壁电流 |
| 为什么某半径热通量增加，是否存在 ITG/TEM/ETG | 线性/非线性 gyrokinetic；局部或全局剖面与磁几何 | 增长率、频率、谱、饱和通量与统计误差 |
| 加热时序改变后，温度、密度和电流如何演化 | 芯部输运；几何、初边值、输运闭合和源项 | $T_e,T_i,n_e,q$ 的时间轨迹、功率平衡及目标量敏感性 |
| 偏滤器靶板热流和脱靶怎样变化 | 边缘等离子体—中性粒子；上游通量、回收、抽气、原子数据 | 靶温、粒子与热流、辐射分布、压力和守恒残差 |
| RF/NBI 能量在哪里沉积，驱动多少电流，快粒子损失多少 | 射线/全波、Fokker–Planck、束出生和轨道模型 | 分物种吸收、分布尾部、电流、逃逸与壁负荷 |
| 包层增殖、屏蔽和部件热应力是否满足目标 | 中子/光子输运与热结构；核数据、CAD、材料和载荷 | TBR、核热、反应率、剂量相关量、温度与应力 |

平衡、湍流、芯部输运、边缘、加热及工程各组软件在下文逐组比较。先给目标量及其误差预算，能够避免用一个更复杂、却没有相应输入数据的模型替代一个边界明确的模型。

### 先选择尺度，再选择软件

平衡模型回答给定约束下磁面和力平衡如何组织；扰动增长率由相应的稳定性模型计算。MHD 演化描述集体流体行为，依赖单流体、双流体或其他闭合；电阻、粘性及热流模型会影响结果。输运模型描述剖面随时间演化，其通量闭合可以来自经验关系、约化模型或湍流计算，预测能力随所采用的通量闭合而变化。模型层级的理论入口见 [MIT 22.611J 课程讲义目录](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/pages/lecture-notes/)，尤其流体、MHD、Vlasov 和波动章节。

动理学模型保留速度分布，能够描述流体矩不足以唯一决定的共振或非热尾部。Gyrokinetic 模型平均去除快回旋相位，以相应磁化、频率和空间尺度排序换取较低计算成本；是否包含电磁扰动、碰撞、大幅剖面变化和有限拉莫尔半径效应必须逐项查证。各软件的 $\delta f$/full-$f$、静电/电磁与局部/全局能力须分别核对，具体比较见下文的陀螺动理学表。

全波求解器保留给定介电响应下的波动结构，射线方法则采用局部波长短于背景变化尺度的近似。是否需要全波取决于截止、模转换、干涉、衍射及边界及所需空间分辨率。Fokker–Planck 求解碰撞、源汇和波致扩散作用下的分布演化；热结构求解器把沉积热量转为温度和应力，中子学求解器追踪反应、输运和材料响应。跨模型比较前要核对各自忽略的物理项。

### 平衡与磁场优化

平衡重建是反问题：给定有限且带误差的诊断，寻找满足力平衡并与测量相容的电流和压力分布。设计平衡通常是正问题：给定线圈和剖面，求磁面及边界。轴对称托卡马克与三维仿星器的几何和假设不同，软件选择也不同。

| 软件 | 方程与表示 | 主要输入和输出 | 选型差异 |
| --- | --- | --- | --- |
| [EFIT / EFIT-AI](https://gafusion.github.io/OMFIT-source/modules/mod_EFIT.html) | 二维轴对称 Grad–Shafranov 平衡，可结合诊断约束重建 | 磁测量、MSE、压力/电流约束和机器几何 → 磁通、边界、$q$ 与 g/a 等文件 | 适合实验平衡与下游输入；内部电流剖面的可信度依赖诊断覆盖、参数化与拟合权重 |
| [FreeGS](https://github.com/freegs-plasma/freegs/blob/master/README.md) | Python 自由边界 GS，Picard 迭代与多重网格 | 线圈、剖面、形状约束 → 稳态磁通、X 点及线圈电流 | 适合磁形状设计、教学和自定义约束；稳态线圈解不包含完整控制电路时间演化 |
| [FreeGSNKE](https://github.com/FusionComputingLab/freegsnke) | 轴对称 GS 平衡与主动/被动导体电路演化 | 初态、线圈电压和剖面参数 → 形状及线圈/被动结构/等离子体总电流轨迹 | 可研究动态平衡和控制；当前采用 FreeGS4E 后端，所核 README 仍将电流扩散与输运耦合列为后续计划 |
| [VMEC / VMEC2000](https://princetonuniversity.github.io/STELLOPT/VMEC.html) | 在嵌套磁面假设下求三维理想 MHD 平衡；固定或自由边界 | 边界、压力、旋转变换或电流、磁通及外线圈场 → wout 等几何与剖面 | 适合仿星器几何和已有下游工具链；扫描径向与角向分辨率，检查力残差和近轴导数 |
| [DESC](https://desc-docs.readthedocs.io/en/stable/) | 三维嵌套磁面、伪谱离散、力残差优化和自动微分 | 边界与剖面 → 平衡、派生量和优化结果，可输出 VMEC 相关格式 | 适合梯度设计及平衡/线圈优化；JAX 编译、谱阶及目标函数会影响成本 |
| [SIMSOPT](https://simsopt.readthedocs.io/latest/mhd.html) | 组织线圈/表面、磁场、目标函数及外部物理求解器的优化框架 | 设计自由度和约束 → 线圈/边界方案及求解历史 | 适合组合多种指标；VMEC、SPEC 等后端需另装，成本取决于调用次数与求导方式 |

VMEC 和 DESC 都用嵌套磁面表示，磁岛和随机区不能直接从这一表示中产生。[DESC 与 VMEC 的原始比较论文](https://doi.org/10.1017/S0022377823000272)用共同的力平衡误差和具体案例讨论收敛，说明应比较达到同一误差目标的成本。优化还要检查线圈间距、曲率、工程载荷、快粒子约束和扰动敏感性；只降低一个准对称指标，不能替代这些约束。

FreeGSNKE 的[静态平衡比较论文摘要](https://arxiv.org/abs/2407.12432)描述了在一致 MAST-U 几何、导体电流和剖面条件下与 Fiesta、EFIT++ 的核对；本章仅据摘要引用这一比较范围。静态平衡的一致性证据不能直接转移成动态壁载荷的精度结论。

### 线性稳定性与非线性 MHD

线性本征问题给出某个平衡附近的增长率、频率和模结构；非线性演化才能研究模耦合、磁拓扑变化和饱和。理想 MHD、电阻 MHD、双流体及流体—动理学模型的闭合不同。目标为台基稳定边界时，可先做线性扫描；目标为 ELM 热脉冲或 VDE 壁载荷时，需要相应的时间演化、耗散、壁和源项模型。

| 软件 | 数值与物理特点 | 典型任务 | 应核对的限制 |
| --- | --- | --- | --- |
| [ELITE](https://fusion.gat.com/THEORY/elite/) | 托卡马克边缘中高环向模数的理想 MHD 线性本征分析 | Peeling–ballooning 稳定边界、台基扫描 | 平衡边缘分辨率和电流约束很关键；线性失稳阈值不直接给出崩塌热负荷；所引官网为历史功能说明 |
| [M3D-C1](https://m3dc1.pppl.gov/m3dc1_overview.html) | 高阶 $C^1$ 连续有限元与非结构网格，单/双流体扩展 MHD，隐式/半隐式推进 | 外加三维场响应、ELM、锯齿、VDE 与破裂相关研究 | 列清使用的流体项、壁、电阻率和边界；隐式稳定性不替代时间步收敛 |
| [NIMROD](https://nimrodteam.org/) | 两维谱有限元与第三维 Fourier，扩展 MHD 及可选动理学闭合/粒子 | 宏观稳定性、重联及多种磁约束构型 | 说明具体闭合和粒子模型，检查谱模数、耗散与源项对非线性结果的影响 |
| [JOREK](https://www.jorek.eu/) | 极向 Bézier 有限元、环向 Fourier，reduced/full MHD 及壁、杂质等可选模块 | 含 X 点/SOL 的 ELM、VDE、破裂缓解和壁相互作用 | 不同物理选项的耦合支持需逐项核对；中性粒子、杂质、壁与粒子设置影响载荷结论 |

[2021 年 M3D-C1、NIMROD、JOREK 的 VDE benchmark](https://m3dc1.pppl.gov/Papers/artola_PP_21.pdf)采用由 NSTX 出发的平衡、简化矩形电阻壁，并为控制成本把等离子体电阻率提高到所用 Spitzer 值的 10 倍；各代码还存在 reduced/full MHD 等差异。该研究可用于学习怎样对齐问题和比较载荷，不能据其代码间一致性给出所有破裂场景的统一精度排名。

### 芯部输运与集成放电建模

芯部输运把三维磁几何约化成磁面平均方程。“1D”一般指径向输运；“1.5D”常指径向输运与二维轴对称平衡联用，具体含义应查软件定义。解释性分析输入实测剖面，反推出满足粒子、能量和动量收支所需的通量；预测性分析给定闭合和源项，再演化未知剖面。同一个平台可以在不同通道分别采用这两种模式，比较前应列清哪些量被实验固定。

| 软件或平台 | 主要求解任务 | 适合怎样使用 | 比较时的关键条件 |
| --- | --- | --- | --- |
| [TRANSP](https://arxiv.org/abs/2406.07781) | 托卡马克粒子、功率、动量收支及电流扩散，包含加热、电流驱动和预测模块 | 有完整诊断和执行器输入的放电分析；结合 NUBEAM 研究快离子与加热收支 | 把解释与预测通道、采用的平衡、加热模块、输运闭合和实验约束逐项列出 |
| [ASTRA](https://w3.pppl.gov/~hammett/work/2009/Astra_ocr.pdf) | 通过模型描述语言和模块组织输运问题，原报告给出一维输运与二维平衡的闭合 | 检验自定义通量/源项假设，组织已有装置模型 | 本表采用 2002 年原报告的框架定义；现代发行版、插件和接口需另核对，不能照抄旧安装要求 |
| [JINTRAC：JETTO/SANCO 与 EDGE2D/EIRENE](https://scientific-publications.ukaea.uk/wp-content/uploads/MILITELLO_ASP_2022_NUCL-_FUSION_62_126033.PDF) | 芯部输运和杂质与 SOL/偏滤器多流体—中性粒子耦合 | 研究芯边界、加料、杂质和排热相互反馈 | 核对接口位置、返流/回收、原子数据、边缘输运系数与实际启用的子模块 |
| [TGYRO](https://gafusion.github.io/doc/tgyro/solver.html) | 迭代梯度，使新经典与湍流通量满足稳态源项积分 | 在给定边界温度、密度和源项下求稳态剖面，比较通量闭合 | 官方算法以 $\partial_t=0$ 为目标；稳态通量匹配不能直接解释整个升流、加热、降流时序 |
| [RAPTOR](https://crppwww.epfl.ch/~sauter/raptor/) | 面向快速执行、实时状态估计和非线性优化的径向输运 | 控制器开发、放电轨迹和可观测性研究 | 闭合的简化程度、观测器输入和执行器模型决定可用范围；实时性要在指定硬件与算例上测量 |
| [TORAX](https://arxiv.org/abs/2406.06718) | 基于 Python/JAX 的可微芯部输运，推进离子/电子热、粒子与电流扩散方程 | 快速参数扫描、梯度优化、代理模型与输运方程联用 | 区分给定的几何/源项与在线求解量；自动微分覆盖范围取决于所接模块是否可微 |

TORAX 的具体物理配置可查 [v1.4.3 的模型页](https://torax.readthedocs.io/en/v1.4.3/physics_models.html)及[版本发布记录](https://github.com/google-deepmind/torax/releases)：加热源、台基、旋转和边缘约化模块按版本配置。输入一串 EQDSK 并进行几何插值，与在每个时间步重新求自由边界平衡是两种不同的耦合方式。更换源模型或调用外部程序时，应重新检查导数、求解器配置和计算开销。

### 湍流闭合、准线性模型与代理模型

输运平台本身不唯一决定湍流预测。相同的输运方程，换用常数扩散、TGLF、QuaLiKiz、非线性 gyrokinetic 通量或神经网络代理，会得到不同的剖面与误差结构。

| 模型 | 怎样得到输运通量 | 相比直接非线性计算省下什么 | 需要保留的模型信息 |
| --- | --- | --- | --- |
| [TGLF](https://gafusion.github.io/doc/tglf.html) | 求解 gyro-Landau-fluid 线性模，配合准线性权重和饱和规则 | 约化速度空间响应，并用饱和规则表示非线性通量水平 | 饱和规则、波数范围、几何、电磁项和 $E\times B$ 剪切选项 |
| [QuaLiKiz](https://arxiv.org/abs/1708.01224) | 约化的准线性 gyrokinetic 模型，输出热、粒子与动量通量 | 用约化模结构和饱和模型，减少直接演化非线性湍流的工作量 | 模型版本、适用的局部参数与几何、碰撞和旋转处理 |
| [QLKNN](https://arxiv.org/abs/2105.01168) 等代理 | 学习已有物理模型的数据映射 | 避免每次调用原模型求解 | 教师模型、训练域、特征归一化、阈值附近误差和域外检测 |
| 非线性 gyrokinetic 通量 | 在指定方程与排序下直接演化湍流并做统计平均 | 保留所解析尺度上的非线性相互作用 | 相空间分辨率、尺寸、碰撞、饱和时间、平均窗和统计误差 |

TGLF 是 gyrofluid 线性响应加通量闭合，QuaLiKiz 是约化 gyrokinetic 准线性模型；二者的相似输出不表示采用同一组方程。代理模型对教师的拟合误差、教师对实验的偏差、输运迭代引入的误差应分别记录。阈值附近一点通量误差可能移动温度梯度；在刚性输运区，通量差异与最终剖面差异也未必成比例。对代理可先做独立参数留出，再在相同边界和源项下比较整段输运轨迹，最后检查独立放电。

### 陀螺动理学湍流：GENE、GS2、CGYRO、GTC 与 Gkeyll

这组软件要沿三个独立维度比较。采用 $\delta f$ 时，在相应扰动排序下把分布分成背景与主要演化的小扰动；full-$f$ 演化总分布；局部 flux-tube 在小径向区域采用给定平衡量与梯度，全局模型保留径向剖面变化；Eulerian 在相空间网格上演化分布，PIC 用带权标记采样分布。全局模型可以采用 $\delta f$，PIC 也可以是 gyrokinetic PIC。full-$f$ 不取消 gyrokinetic 排序；采用长波近似时也仍受其约束。

| 软件 | 主要方程与表示 | 合适的研究任务 | 选择时应区分的点 |
| --- | --- | --- | --- |
| [GENE](https://genecode.org/details.html) | Eulerian 五维 gyrokinetic，经典表述为 $\delta f$，有局部与全局模式 | 线性微稳定性、非线性离子/电子尺度湍流、径向非局域效应 | 电磁项、碰撞、物种和托卡马克/仿星器几何按输入配置；global 不等同于 full-$f$ |
| [GS2](https://gyrokinetics.gitlab.io/gs2/) | 沿场线的局部 flux-tube、扰动分布网格 gyrokinetic | 给定磁面附近的增长率、模结构、饱和通量与共同基准 | 对照动理学/绝热电子、碰撞和几何；局部计算不直接给出整半径剖面演化 |
| [CGYRO](https://gafusion.github.io/doc/cgyro.html) | Eulerian、径向谱表示，当前官方说明包括 global-spectral 方案 | 碰撞、电磁、多尺度湍流和径向剖面变化研究 | 旧的“仅局部”概述已不完整；局部/全局算法与径向处理依实际版本和设置 |
| [GTC](https://sun.ps.uci.edu/people/zlin/bib/wong24.pdf) | 全局环形 gyrokinetic PIC，可用 $\delta f$ 或 full-$f$，有混合电子等模型 | 全局湍流、快粒子与 Alfvén 模相关研究 | 选定电子与电磁模型，并扫描标记数、随机性和数值噪声；PIC 不表示逐圈解析完整回旋运动 |
| [Gkeyll](https://gkeyll.readthedocs.io/en/latest/) | 当前公开 GK 模块为 full-$f$、长波极限、模态间断 Galerkin 分布网格，静电 GK-Poisson | 非 Maxwellian 分布、开场线与鞘层相关动理学问题 | 与其 Vlasov-Maxwell 模块、历史论文中的电磁扩展分开；实际可用功能以所选模块为准 |

GENE 的 $\delta f$、local/global 定义可查[方法论文](https://www.genecode.org/PAPERS_2/JPCS_012011.pdf)；CGYRO 的全局算法由官方[参考文献表中的 2025 年论文](https://gafusion.github.io/doc/zreferences.html)支持，比较时应记录实现版本。Gkeyll 的[简单 GK 鞘层例子](https://gkeyll.readthedocs.io/en/latest/quickstart.html)展示了长波静电 full-$f$ 的边界问题，但该例不含完整电离、复合和辐射，不能直接当作反应堆偏滤器模型。

回旋平均通常将分布的相空间从三位置、三速度降到三位置、两速度，但成本仍由空间、平行速度、磁矩/垂直能量、物种和时间共同决定。局部线性扫描、全局非线性饱和与电子/离子多尺度研究对应的计算量相差很大；仅按软件名称给出“几核几小时”缺少物理依据。报告预算时应给出目标量误差随自由度和统计时间的变化。

### 边缘与偏滤器：平均输运和涨落分开比较

SOL 和偏滤器需要处理沿场输运、鞘层、原子分子过程、回收、杂质与辐射。平均输运模型通常需要给定横场扩散系数；三维湍流模型解析部分涨落，但仍需选择平行热流、中性粒子和边界闭合。

| 软件 | 等离子体和中性粒子处理 | 典型用途 | 关键差异与输入 |
| --- | --- | --- | --- |
| [SOLPS-ITER](https://solps-tutorials.readthedocs.io/) | 标准工作流为二维轴对称 B2.5 多流体与 EIRENE Monte Carlo 中性粒子耦合 | 偏滤器排热、脱靶、杂质/辐射、回收与抽气 | [横场粒子与热扩散系数](https://solps-tutorials.readthedocs.io/feature_blog/Diffusion_coefficients/)是模型输入；应检查网格、反应库及中性粒子统计 |
| [UEDGE](https://github.com/LLNL/UEDGE) | 二维等离子体及中性气体流体，有限体积与全隐式求解 | 边缘稳态扫描和瞬态输运 | 中性流体闭合与 EIRENE 的动理学中性模型不同；横场反常输运也需设定 |
| [BOUT++](https://bout-dev.readthedocs.io/en/latest/user_docs/introduction.html) / [Hermes-3](https://hermes3.readthedocs.io/en/latest/) | 曲线坐标流体框架 / 建立其上的多物种边缘模型，可配置维度与稳态、瞬态、湍流任务 | 边缘流体、涨落与模型开发 | 指明具体模型、物种、方程和组件；Hermes-3 的[中性流体闭合](https://hermes3.readthedocs.io/en/latest/equations.html)也须按维度选择 |
| [SOLEDGE3X](https://soledge3x.onrender.com/features/fluid_description/) | 漂移序多流体；所引方程页采用静电固定磁场，可运行平均输运或相应湍流问题 | 边缘输运、回收与壁相互作用 | [中性模型](https://soledge3x.onrender.com/features/neutrals/)可用简化扩散或经 STYX 耦合 EIRENE，不能把两种计算等量齐观 |

若目的是给靶板平均热流和中性压力做扫描，可先在平均输运模型中约束上游剖面、回收和辐射；若目的是解释 blob、间歇性负荷或横场输运机制，则需要相应的三维涨落模型与合成诊断。拟合实验得到的 $D_\perp,\chi_e,\chi_i$ 能解释该工况，不自动构成对新工况的预测能力。

### 通用电磁 PIC：Smilei、WarpX 与 EPOCH

完整 Vlasov–Maxwell PIC 保留快速电磁和粒子动力学，适合激光—等离子体、局部不稳定性或特定动理学机制。它与磁约束长期输运所用的回旋平均模型在解析尺度上不同；将电子快速尺度一直积分到宏观放电时间通常带来巨大的成本。

| 软件 | 本次核对的定位 | 选择依据 |
| --- | --- | --- |
| [Smilei](https://smileipic.github.io/Smilei/) | 通用相对论 PIC，官方算法说明宏粒子、网格 Maxwell 与 PIC 循环 | 适合需要完整快速动理学的课题，核对维度、碰撞、边界及粒子诊断 |
| [WarpX](https://warpx.readthedocs.io/en/latest/) | 通用 PIC，提供不同电磁、静电及混合场路径，并有网格加密和 CPU/GPU 运行能力 | 按具体算法、网格层级、硬件和版本做基准；具有聚变反应模块不等于具备整次托卡马克放电模型 |
| [EPOCH](https://github.com/epochpic/epoch) | 提供一、二、三维实现的等离子体 PIC 软件 | 可作为快速动理学问题的候选；本次只核对公开仓库定位与许可，具体扩展模块需继续阅读对应手册 |

### 射频波与分布函数：射线、准光学、全波与 FP

射线追踪用几何光学近似计算传播和局部吸收；准光学束追踪还描述有限束宽与衍射；全波求解给定频率、边界和介电响应下的场；Fokker–Planck（FP）求碰撞、波扩散、电场与源汇作用下的分布函数。这几层分别决定传播、场结构、非热尾部和电流。具体应用可对照[离子回旋](../辅助加热/离子回旋加热/README.md)、[电子回旋](../辅助加热/电子回旋加热/README.md)与[低杂波](../辅助加热/低杂波电流驱动/README.md)专题。

| 软件 | 物理层级 | 主要输出 | 模型边界与比较重点 |
| --- | --- | --- | --- |
| [GENRAY](https://www.compxco.com/genray.html) | 几何光学射线，具有 EC、LH、ICRF 等色散/吸收选项 | 射线路径、吸收及线性电流驱动；可向 FP 提供 RF 数据 | 核对色散与吸收模型、初始谱和功率；截止、模转换、干涉与衍射需检查近似是否成立 |
| [GRAY](https://baltig.cnr.it/ectoplasm/gray) | 用复 eikonal 描述 EC 高斯束的准光学传播 | 束传播、衍射、吸收与 EC 电流驱动 | 比单条射线多了束宽/衍射描述，但不等同于三维天线近场全波 |
| [TORIC](https://www-internal.psfc.mit.edu/~jwright/Publications/jcw_icnsp_submittedpaper/node2.html) | 轴对称环形几何、热等离子体有限拉莫尔半径（FLR）全波 | 波场、模式转换和分物种吸收 | “全波”仍有线性响应、几何和 FLR 模型近似，须写明所用版本 |
| [AORSA](https://github.com/ORNL-Fusion/aorsa) | 谱全波，保留离子拉莫尔半径与波长比的所有阶响应 | RF 场、沉积，按配置输出准线性系数 | 所谓所有阶不消除平衡梯度、线性响应和有限分辨率的近似；构建与大矩阵求解也是成本 |
| [CQL3D](https://www.compxco.com/cql3d.html) | 相对论、弹跳平均的碰撞/准线性 FP；常用两动量维加一径向维 | 非热电子/离子分布、加热、电流驱动和相关诊断量 | 名称中的 3D 不表示三维空间全轨道；RF 扩散和几何须由对应模型或上游求解器提供 |
| [LUKE](https://spcgit.epfl.ch/luke/tutorial.html) | 所引教程为相对论、弹跳平均电子 FP，一空间维加两动量维 | 电子分布、电流驱动与相关响应 | 核对背景、碰撞线性化、波输入、电场和输运；该教程基于 MATLAB |

TORIC 的[原始论文](https://doi.org/10.1088/0741-3335/41/1/002)说明其有限拉莫尔半径全波模型；AORSA 作者的[电导率修正说明](https://nstx.pppl.gov/DragNDrop/Science_Groups/core/TSGs/energetic_particles/archive/2011/RF%20Conference%202011/Abstracts/Contributed%20Abstracts/Poster%20Session%20A/A49_Jaeger_E_.pdf)区分 $k_\perp\rho$ 与 $\rho/L_{\rm eq}$ 两种展开参数。选择全波应来自具体的波效应需求，而非把求解器名称当作无近似的保证。

强非热情形中，场给出准线性扩散，分布改变吸收和介电响应，二者可能需要迭代。比较功率时统一天线/入射面、反射、金属/介质损耗、电子/离子吸收和出域功率。频域复场采用峰值幅度时，周期平均功率密度（W/m³）常写为 $\tfrac12\operatorname{Re}(\mathbf J\cdot\mathbf E^*)$；采用 RMS 幅度时因子相应改变，必须跟随软件约定，例如 [HFSS 的相量说明](https://ansyshelp.ansys.com/public/views/secured/electronics/v261/en/subsystems/HFSS/Content/HFSS/PeakVersusRMSPhasors.htm)。下文给出 RF—FP 功率矩的核对方法。

### 中性束与快粒子：出生、慢化与三维轨道

[NUBEAM 官方指南](https://w3.pppl.gov/~pshare/help/body_nubeam_hlp.html)在给定背景上做中性束相关出生、碰撞、慢化和快离子处理，再向背景模型返回源项。[ASCOT5](https://ascot4fusion.github.io/ascot5/)则提供三维场中的 test-particle 轨道计算；二者应围绕目标量和所用场、源、壁模型比较。

| 工具 | 在链条中的角色 | 输入与输出 | 需要检查什么 |
| --- | --- | --- | --- |
| [NUBEAM](https://w3.pppl.gov/ntcc/NUBEAM/abstract.html) | 中性束及聚变快离子的出生、慢化/热化与源项模块，常用于 TRANSP | 平衡、背景、注入器/束成分和原子过程 → 粒子、能量、动量源与分布/反应率 | 所引指南采用轴对称嵌套磁面；直接标量和 Plasma State 接口的单位分别查表 |
| ASCOT5 | 三维全轨道或导引中心轨道与碰撞、壁损失 | $\mathbf B,\mathbf E$、背景、加权粒子源、壁三角网格 → 分布、损失位置与壁负荷 | test-particle 不反馈改变背景；导心/全轨道转换、轨道步长和局部损失采样需收敛 |
| BBNBI / AFSI（ASCOT 工具链） | BBNBI 给束出生与穿透；AFSI 给聚变产物源 | 注入几何或反应物分布 → 可用于轨道跟踪的源 | 出生源、轨道损失和慢化沉积是不同阶段，接口中保留源率与能量/俯仰分布 |

如果问题是分析加热功率收支，可先沿集成平台的既有源模块建立预算；如果关心三维误差场、线圈纹波或局部壁热点，则需要对应的三维场、真实壁及轨道模型。一个损失百分比转为 W/m²，还要有粒子能量、标记权重、源率或统计时间和表面面积；热点统计往往比总损失比例需要更多有效样本。中性束的物理分段见[中性束注入](../辅助加热/中性束注入/README.md)。

### 中子学、CAD 与热结构软件

中子和光子在材料中的输运与带电快粒子磁轨道是不同的问题。工程计算链可写为“参数/CAD 几何 → 几何检查与材料赋值 → 核输运与核热 → 热流/体热源映射 → 温度和结构响应”。

| 工具 | 核心角色 | 适合比较的任务 | 需要补齐的输入或模型 |
| --- | --- | --- | --- |
| [OpenMC](https://docs.openmc.org/en/stable/usersguide/beginners.html) / [MCNP](https://mcnp.lanl.gov/how_to_get_the_mcnp_code.html) | 本章关注的固定源中子/光子 Monte Carlo 输运 | 氚产生、屏蔽、核热和反应率；对齐几何、核数据和源后做统计比较 | 同位素/密度、连续能核数据、温度、源空间/能谱/角分布及 tally 定义 |
| [Paramak](https://github.com/fusion-energy/paramak) / [DAGMC](https://github.com/svalinn/DAGMC) | 参数化聚变 CAD / 在 CAD 上提供输运几何与射线跟踪接口 | 自动扫描装置几何，保留材料区和复杂部件 | 仍需宿主输运器与核数据；检查水密性、重叠/缝隙、材料标签与体积 |
| [COMSOL 电磁热接口](https://doc.comsol.com/6.3/doc/com.comsol.help.heat/heat_ug_theory.07.088.html) | 通用有限元电磁与热等多物理耦合，模块组合依任务选择 | 天线/传输部件损耗、介质/导体发热及热响应 | 端口、材料频散/温度关系、热边界与授权模块；热等离子体动理学响应须另建或导入 |
| [Ansys HFSS/Maxwell—Mechanical](https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Mechanical/Content/Mechanical/Two-WayCoupling.htm) | 高频/低频电磁与热结构工作流 | 电磁损耗到温升，温度反馈材料属性与损耗 | 表面/体损耗映射、冷却、接触、材料与双向迭代收敛；所引说明为 2025 R1 |
| [MOOSE](https://mooseframework.inl.gov/modules/electromagnetics/index.html) | 可开发的有限元多物理框架 | 自定义方程、材料和场/热/力耦合 | 框架与具体应用分开核验；当前所读电磁模块文档的波问题为 1D/2D，不能据此假定现成的任意三维 RF 能力 |

[OpenMC 核数据说明](https://docs.openmc.org/en/stable/usersguide/data.html)要求把数据库路径、评价/处理版本与温度纳入输入；更换评价库可能改变 TBR 和反应率，增加历史数不能消除这种系统差异。damage-energy tally 到 dpa 还需要位移损伤模型与参数，氚产生比到燃料自持还需要燃耗、库存、处理损失及停机收支。

Ansys 的[热应力文档](https://ansyshelp.ansys.com/public/Views/Secured/corp/v242/en/wb_sim/ds_thermal_stress.html)说明如何把温度场传为结构热载荷。热结构选型要看材料非线性、接触、脉冲、冷却、网格和已有模型，而非只看是否写着“多物理”。表面热流 W/m²、体热源 W/m³ 和积分功率 W 分别传递；天线金属损耗、快粒子壁沉积与中子核热分别建账，芯部吸收功率不能直接作为天线金属热源。

### 有限差分、有限体积与 PIC

有限差分近似网格点上的导数；有限体积对控制体积分，用单元面通量更新体平均量。若内部公共面的通量在相邻单元取同值反号，总和中会相消，这正是离散守恒的重要结构。高阶重构、复杂边界或插值仍可能破坏正性、稳定性或整体守恒，需要单独测试。BOUT++ 官方将自身描述为曲线坐标下的结构化有限差分/体积框架，物理方程由模型指定；示例含流体与湍流模型。参见 [BOUT++ Introduction](https://bout-dev.readthedocs.io/en/stable/user_docs/introduction.html) 和 [Physics models](https://bout-dev.readthedocs.io/en/latest/user_docs/physics_models.html)。每套方程实现都可分别建立解析解和守恒测试。

PIC 用带权宏粒子表示分布，并在网格上求场。一个循环包含粒子处场插值、粒子推进、电荷/电流沉积和场更新。宏粒子代表具有给定统计权重的粒子群；统计噪声、网格加热、时间步误差和边界处理都影响结论。应分别扫描网格、时间步、每格粒子数和随机种子；显式电磁算法还需满足其稳定性约束。上述算法路径已核对 [Smilei 5.1 PIC algorithms](https://smileipic.github.io/Smilei/Understand/algorithms.html) 的 Quasi-particles、Time and space discretization 与 PIC loop，稳定条件由所选时间推进和场求解算法确定。

### 从守恒积分构造一个有限体积步

考虑常速 $v>0$ 的一维输运 $\partial_tu+\partial_x(vu)=0$。对宽度 $\Delta x$ 的单元积分，单元平均量的变化等于左端流入减右端流出。取迎风界面通量 $F_{i+1/2}=vu_i^n$，用显式时间积分得到

$$
u_i^{n+1}=u_i^n-\nu(u_i^n-u_{i-1}^n)
=(1-\nu)u_i^n+\nu u_{i-1}^n,\qquad
\nu=\frac{v\Delta t}{\Delta x}.
$$

当 $0\leq\nu\leq1$，更新值是两个旧值的凸组合，故保留非负性并保持在相邻值范围内。周期边界下对所有单元求和，通量相邻抵消，总量严格守恒。教学取四单元初值 $(0,1,2,1)$、$\Delta x=0.10$ m、$v=2.0$ m/s、$\Delta t=0.025$ s，$\nu=0.5$，更新为 $(0.5,0.5,1.5,1.5)$；以任意一致的密度单位计，积分总量均为 $0.4$。将时间步增至 $\nu=1.2$ 时，第二单元变为 $-0.2$，凸组合条件随之失效。[Clawpack《Advection》的 Conservation of mass 与 Riemann problem 两节](https://www.clawpack.org/riemann_book/html/Advection.html)给出守恒形式及迎风信息来源；以上离散步由这两个性质直接构造。

## 多物理耦合与数据接口

### 集成平台怎样组织软件

[IMAS Data Dictionary](https://imas-data-dictionary.readthedocs.io/en/latest/intro.html)定义 Interface Data Structures（IDS），规定数据含义、单位和坐标；访问层负责读写这些结构。[ITER 2025 年的开放发布公告](https://www.iter.org/node/20687/release-imas-infrastructure-and-physics-models-open-source)涉及基础设施和逐步发布的物理软件，应逐仓库核对许可及依赖。数据结构、模型接口和运行环境共同组成工作流。

[OMFIT 的 STEP](https://www.omfit.io/modules/mod_STEP.html)通过 OMAS 组织状态，将稳定性、输运、平衡和台基计算按步骤连接并保存历史。其[安装说明](https://omfit.io/install.html)明确指出，OMFIT 本体不包含模块调用的所有外部程序；可访问一个界面，不等于已经获得 EFIT、TRANSP 或其他求解器与数据库。软件目录、实际安装和输入数据是三份需要对应的清单。

| 层级 | 负责的工作 | 接口成功之后仍要检查什么 |
| --- | --- | --- |
| 物理求解器 | 解给定方程、生成通量/源项/平衡等 | 方程项、闭合、守恒、分辨率和模型适用性 |
| IMAS/IDS、OMAS 等数据表达 | 描述物理字段、坐标、版本和读写 | 源程序是否按字段定义填值、坐标变换和归一化是否正确 |
| OMFIT/STEP 等工作流 | 准备输入、调用程序、调度迭代、保存状态 | 模块是否真正启用、收敛条件、失败传播及状态是否过期 |
| HPC/容器/作业系统 | 提供依赖与计算资源 | 二进制、驱动、MPI、随机性与结果可重复程度 |

IMAS-Python 的 [IDS validation](https://imas-python.readthedocs.io/en/latest/validation.html)检查时间模式及坐标维度等一致性。字段形状正确后，仍需另算功率积分、物种收支及方向约定，才能判断两段程序在物理上是否闭合。

### 三条可以落地的计算链

**加热方案与放电剖面。** 先用指定平衡和实测或设计剖面计算 RF/NBI 的分物种源项，传入输运模型；剖面变化后更新波吸收、束出生和碰撞交换，必要时再更新平衡。先固定几何、核对单向功率映射，再增加反馈，能够定位每个接口的误差。用 TORAX/RAPTOR 做优化时，可在少量代表性状态上与所选波、轨道或输运教师模型对照，保存代理调用范围。

**芯部—偏滤器—壁。** 芯部给出越过分界面的功率与粒子流，边缘模型结合加料、回收和抽气返回上游状态、杂质和辐射；靶面热流再投影到实际 CAD 表面，交给热结构求解。检查闭合面和控制体边界，防止把辐射、回收能量或快粒子损失重复计入。该链可与[腔体材料](../腔体材料/README.md)及[工程系统](../工程系统/README.md)的载荷定义联用。

**聚变源—核热—温度应力。** 反应率与快离子模型提供中子空间、能谱和角分布；中子学求解各材料区的核热与反应率；工程模型再叠加表面热流、冷却和结构约束。保留每源粒子 tally 到 W 或 W/m³ 的归一化过程，以及核数据、材料密度和同位素组成版本。CAD 到输运网格、输运网格到有限元网格的两次映射分别检查总量。

这些是计算组织方案。选取其中一条时，应明确哪些模块已经真实相连、哪些载荷为外部给定，保存每次耦合调用的输入和输出版本。

### RF—分布函数—输运

射频场给出波粒能量交换和扩散系数；分布函数改变介电响应、碰撞功率和电流；输运改变温度、密度及共振位置。迭代耦合把这些更新传回上游，形成场、分布与剖面之间的反馈。最小接口应写明物种、坐标、体积元、功率单位、归一化、时间窗和损失口径。

用非相对论动能 $m_sv^2/2$ 定义 RF 算子贡献时，可检查

$$
P_{\mathrm{RF}\to s}^{\mathrm{FP}}
=\int dV\int d^3v\,\frac{m_sv^2}{2}\,Q_{\mathrm{RF},s}[f_s].
$$

这一功率矩的推导是对分布演化中的 RF 部分 $\partial_tf_s|_{\rm RF}=Q_{{\rm RF},s}$ 乘单粒子动能，再在相空间积分。速度、位置坐标不随时间变化时，时间导数可移出积分，左边就是该算子造成的动能变化率；若使用扩散算子，还可分部积分把能量变化写成扩散通量做功，必须同时保留或明确令零速度空间边界通量。

它应与同一物种、同一体积内的波吸收功率一致，精度受离散和耦合残差限制；相对论计算需换成相对论动能，动量坐标需换积分测度。快离子吸收进入快粒子库，其对背景的碰撞加热是两个能量库之间的转移。是否把逃逸粒子和边界通量纳入预算也须明确。

[Frank 等 2022 原论文摘要](https://arxiv.org/abs/2207.09011)报告了 TORLH 与 CQL3D 的功率自洽耦合，并指出其所研究的 C-Mod 情形中，全波修正未解释全部实验差异。本次读取摘要，只引用这一方法与结论边界，不据此断言所有 LHCD 场景都可忽略全波效应。

### 空间和时间映射

磁通坐标中的密度必须与正确体积元配套；极向磁通与环向磁通各有自己的坐标变换。保守重映射要求输出网格上的积分与输入预算一致。点值插值看起来平滑，仍可能改变总功率。将二维沉积投影为一维磁面平均会丢失环向和极向结构，应说明这种约化对局部热点或不稳定性是否适用。

耦合时间步需解析被关心的反馈时间尺度。隐式或松弛迭代用于改善数值收敛；可保存各物种能量残差、粒子残差和迭代变化量，检查更细耦合步长下的目标量是否稳定。

### 坐标、符号与单位必须随数据一起传递

同名径向坐标可能表示几何半径、归一化极向磁通或归一化环向磁通的平方根。例如 $\psi_N=(\psi-\psi_a)/(\psi_b-\psi_a)$ 与 $\rho_{\rm tor}=\sqrt{(\Phi-\Phi_a)/(\Phi_b-\Phi_a)}$ 定义不同，不能只改列名就互换；应由同一个平衡给出映射和体积 $V$。下标 $a,b$ 分别表示磁轴与所选边界。

[COCOS 原论文](https://www.epfl.ch/research/domains/swiss-plasma-center/wp-content/uploads/2018/10/Sauter_COCOS_Tokamak_Coordinate_Conventions.pdf)系统区分磁通是否含 $2\pi$、坐标定向和电流/磁场符号。它们会影响 $q$、$F=RB_\phi$、平行波数和同向/反向电流驱动。接口至少保存输入与输出 COCOS、磁通单位、磁轴/边界取值、环向角正向和电流定义，并对一个已知磁场方向的点做向量检查。

[TGYRO 方程与单位表](https://gafusion.github.io/doc/tgyro/equations.html)是实际例子：部分内部量使用 CGS，而本库工程预算使用 SI。由 $1\,\mathrm{erg}=10^{-7}$ J、$1\,\mathrm{cm^2}=10^{-4}$ m²、$1\,\mathrm{cm^3}=10^{-6}$ m³，有

$$
1\,\frac{\mathrm{erg}}{\mathrm{s\,cm^2}}=10^{-3}\,\mathrm{W\,m^{-2}},\qquad
1\,\frac{\mathrm{erg}}{\mathrm{s\,cm^3}}=0.1\,\mathrm{W\,m^{-3}}.
$$

因此 $2\times10^8\,\mathrm{erg\,s^{-1}\,cm^{-2}}$ 对应 $0.20\,\mathrm{MW\,m^{-2}}$。粒子能量、温度能量和归一化热通量也分别恢复单位；写在图上的“功率”必须明确是体积密度、面积通量、磁面输运通量还是已积分功率。

### 保守重映射的一个小算例

把源网格上的单元平均体热源 $s_i$（W/m³）映射到目标单元 $j$，若各单元内用常数重构，可按交叠体积写成

$$
\widetilde s_j=\frac{1}{\Delta\widetilde V_j}
\sum_i s_i\,\Delta V_{ij}^{\rm overlap}.
$$

对所有目标单元乘体积并求和，若新旧网格覆盖同一计算域，且交叠部分没有重复或遗漏，则 $\sum_j\widetilde s_j\Delta\widetilde V_j=\sum_i s_i\Delta V_i$。这是对控制体积分的直接分配；若物理边界改变，移出域的功率需另列。

用累计体积 $V$ 作坐标，原网格边界为 $(0,1,4)$ m³，平均热源为 $(2,1)$ MW/m³，总功率为 $2\times1+1\times3=5$ MW。新网格为 $(0,2,4)$ m³，第一个单元接收 $2\times1+1\times1=3$ MW，第二个接收 2 MW，得到平均值 $(1.5,1)$ MW/m³，总功率仍为 5 MW。

若对原单元中心 $V=(0.5,2.5)$ 的热源做线性点值插值，并在右端使用常数外延，新中心 $V=(1,3)$ 得到 $(1.75,1)$ MW/m³，积分为 5.5 MW，比原值多 10%。曲线平滑没有保证功率一致。高阶映射还可进一步检验非负性、极值和局部矩；此处的分片常数例子只展示守恒结构。

### 从每源中子 tally 到核热功率

[OpenMC tally 文档](https://docs.openmc.org/en/stable/usersguide/tallies.html)给出的量通常按每源粒子归一。对以一个 D–T 反应中子为一个源粒子的固定源问题，设某部件的积分核热 tally 为 $H$（eV/source），真实中子源率为 $\dot N_n$（s⁻¹），则

$$
P_{\rm heat}=H\,\dot N_n\,(1.602176634\times10^{-19})\quad\mathrm W.
$$

该式是每源释放能量乘每秒源数。若给定 D–T 聚变总功率 $P_{\rm fus}$、每次反应取 17.6 MeV 且产生一个中子，则 $\dot N_n=P_{\rm fus}/(17.6\times10^6 e)$，这里 $e$ 的数值为每 eV 对应的焦耳数。取 $P_{\rm fus}=500$ MW、$H=9.0$ MeV/source，得到 $\dot N_n\simeq1.7732\times10^{20}$ s⁻¹，部件核热为 $500\times9/17.6\simeq255.68$ MW；若部件体积为 10 m³，其体积平均热源为 25.568 MW/m³。$H$ 在此为教学给定值，未由真实包层计算取得。

如果 tally 为体积分 flux，OpenMC 常用单位为 particle·cm/source，应先除以 tally 体积（cm³）再乘源率，得到 particle/(cm²·s)。若用另一种源粒子定义、源权重或多源采样，必须相应重建归一化。耦合光子输运与 heating/heating-local 的选择也应随核热结果记录。

### 用两个能量库检验耦合交换

设快粒子能量库为 $W_f$、热等离子体能量库为 $W_t$。将快粒子慢化近似为时间常数 $\tau_f$、热损失近似为 $\tau_E$，则

$$
\dot W_f=P_{\rm inj}-W_f/\tau_f,\qquad
\dot W_t=W_f/\tau_f-W_t/\tau_E.
$$

相加后交换项消去，$\dot W_f+\dot W_t=P_{\rm inj}-W_t/\tau_E$，因而耦合接口的同一份沉积功率在两边分别是损失和增益。对瞬时注入后 $P_{\rm inj}=0$、$W_f(0)=W_0$、$W_t(0)=0$，先解第一个指数衰减，再对第二式用积分因子，得到

$$
W_f=W_0e^{-t/\tau_f},\quad
W_t=W_0\frac{\tau_E}{\tau_E-\tau_f}
\left(e^{-t/\tau_E}-e^{-t/\tau_f}\right).
$$

上述两指数式适用于 $\tau_E\ne\tau_f$。当 $\tau_E=\tau_f=\tau$ 时，积分因子直接给出 $W_t=W_0(t/\tau)e^{-t/\tau}$，也等于两指数式的连续极限；此时热能峰值位于 $t=\tau$。

教学取 $W_0=1.0$ MJ、$\tau_f=0.050$ s、$\tau_E=0.20$ s，$t=0.10$ s 时分别有 0.1353 MJ 和 0.6283 MJ，已损失的热量为 0.2364 MJ，三者相加为初始 1.0 MJ。令 $\dot W_t=0$ 可得热能峰值时刻 $\ln(\tau_E/\tau_f)/(1/\tau_f-1/\tau_E)=0.0924$ s。快粒子向电子和离子的真实慢化分配见 [IAEA《Fusion Physics》§5.1.4，书页 543–545 的能量转移](https://event.ipp-hgw.mpg.de/event/1032/contributions/1480/attachments/715/1166/IAEA%20-%20Fusion%20Physics.pdf)；这里用一阶能量库提取了耦合中必须满足的守恒结构。

## 验证、确认与不确定性

### 方程实现与物理适用性分开检查

代码验证（verification）检查程序是否正确求解指定方程，可用解析解、守恒恒等式和制造解。制造解先选择光滑函数，再补入使其精确满足方程的源项，因此能检验离散阶数和边界实现，其测试对象是所选方程的数值实现。BOUT++ 的相应方法证据见 [Dudson 等，Verification of BOUT++ by the Method of Manufactured Solutions](https://arxiv.org/abs/1602.06747)，相关构造与扩散算例见原文 §2、§4.4。

计算验证还要估计本次运行的离散误差。若已处于渐近区间，可检验目标量是否近似满足

$$
Q(h)=Q_\ast+C h^p.
$$

误差幂律来自离散算子的 Taylor 展开及稳定的误差传播。例如中心二阶差分满足 $[u(x+h)-2u(x)+u(x-h)]/h^2=u''(x)+h^2u^{(4)}(x)/12+O(h^4)$；当误差传播有界、边界也具有同阶精度时，目标量的主误差可写为 $Ch^p$，本例 $p=2$。若未知精确值，三个网格结果相减可消去 $Q_\ast$ 与 $C$：在固定加密比 2 下，$[Q(h)-Q(h/2)]/[Q(h/2)-Q(h/4)]\simeq2^p$，取对数即可估计实际阶数。

空间加密时同步控制时间误差，时间加密时保持足够细的空间网格。非单调结果、峰值漂移、人工耗散或尚未稳定的时间平均，会使简单阶数估计失效。速度空间范围、波数范围与粒子统计也需要独立扫描，并检查目标量随分辨率的变化。

物理确认（validation）比较模型与实验是否相容。应先用合成诊断把模拟结果经过视线积分、仪器响应和采样处理，再与可观测量比较。调参用的数据和检验预测能力的数据尽量分开，模型之间一致也可能只是共享了同一近似。通过比较的工况构成已检验的适用域。

### 不确定性与代理模型

输入不确定性来自测量、材料参数和边界条件；模型形式误差来自缺失机制或闭合；数值误差来自离散与有限采样。先做敏感性分析，识别真正影响目标量的输入，再采用与问题相称的抽样或传播方法；输入相关性应保留，基础传播规则见 [NIST TN 1297 附录 A](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)。

学习得到的代理模型可以加速扫描，但训练范围、外推检测和约束必须明确。随机打乱同一放电相邻时间点再分训练与测试，可能泄漏高度相关的信息；按独立放电或工况留出更能检验迁移。代理还可按未参加训练的工况检查预测误差与守恒残差。

### 跨软件对比要先对齐物理问题

比较 GENE、GS2 和 CGYRO 的线性模，先统一磁几何、电子模型、碰撞算子、物种与归一化，再扫描波数、速度域和数值分辨率；先比较增长率和频率，再比较模结构，最后进入非线性通量。比较 RF 软件时统一发射谱、天线端或入射面功率、介电模型与物种，再对照吸收与场结构。中子学对比则要固定几何、核数据库、材料和源分布，分别估计 Monte Carlo 统计误差。

| 类别 | 最先建立的基准 | 需要扫描的量 | 可与实验或独立数据比较的量 |
| --- | --- | --- | --- |
| 平衡与优化 | 解析平衡、力平衡和边界残差 | 网格/谱阶、拟合权重、诊断约束 | 磁测量、边界、独立压力与电流约束 |
| 线性/非线性 MHD | 已知极限的模增长率、能量收支 | 环向模数、耗散、网格、时间步 | 模频率、磁扰动、温度塌缩与壁电流 |
| Gyrokinetic/PIC | 线性色散、无源守恒及共同基准 | 波数/盒尺寸、速度域、粒子数、平均窗 | 合成散射谱、相关长度、通量及其误差 |
| 芯部输运 | 常系数解析解、源项积分、通量残差 | 径向网格、时间步、非线性容差、边界 | 独立时段或独立放电的剖面轨迹 |
| 边缘与中性粒子 | 粒子/功率收支和简化输运问题 | 网格、原子数据、回收、横场系数 | 靶板热流、光谱、上游密度与中性压力 |
| RF、FP 与轨道 | 冷/热极限色散、功率矩、轨道不变量 | 模数/网格、速度域、粒子数、耦合步长 | 吸收、电流、快粒子分布与局部壁负荷 |
| 中子学与热结构 | 简化几何反应率、均匀热源和导热解 | 历史数、方差缩减、核数据、网格与接触 | 基准实验反应率、温度、位移和应变 |

若两个程序解同一简化问题的结果不一致，先定位实现、坐标和数值误差；若所解方程不同，则把差异视为待研究的模型效应。用一个高保真计算校准简化模型之后，保留未用于校准的工况来检验预测。

### 稳态通量匹配为什么仍需要误差预算

在固定几何、无旋转功项、且只考虑净热源 $S$ 的简化磁面平均能量方程中，令 $r$ 为有长度单位的径向标签，$V'=dV/dr$，$Q$ 为使总径向输运功率等于 $V'Q$ 的通量定义。稳态下

$$
\frac{1}{V'}\frac{d(V'Q)}{dr}=S,
\qquad
P(r)=V'(r)Q(r)=\int_0^r V'(x)S(x)\,dx,
$$

其中取磁轴处净流出功率为零。积分源项给出所需输运功率，再调整剖面梯度，使选定输运闭合给出的 $Q$ 与之匹配。这是 [TGYRO 稳态求解算法](https://gafusion.github.io/doc/tgyro/solver.html)背后的守恒结构；实际多物种求解还须加入各自的交换和源项。

若在某磁面内净热源积分为 4.0 MW，而离散通量给出 3.8 MW，定义功率残差 $R_P=P_{\rm transport}-P_{\rm source}$，则 $R_P=-0.2$ MW，相对源功率为 $-5\%$。即使温度曲线几次迭代几乎重合，这个预算仍未闭合。源项误差、台基边界误差与求解残差应分别报告；收紧非线性容差只会降低其中一部分。

### 湍流与粒子计算中的统计误差

饱和湍流的时间序列通常相关，不能把每个输出步都算成独立样本。对近似平稳序列，记样本数为 $N$、归一化滞后自相关为 $\rho_k$、瞬时量的方差为 $\sigma_Q^2$，在平均窗足够长且相关和可收敛的条件下，样本均值方差近似为

$$
\operatorname{Var}(\overline Q)\simeq\frac{\sigma_Q^2}{N}
\left(1+2\sum_{k=1}^{\infty}\rho_k\right),\qquad
N_{\rm eff}=\frac{N}{1+2\sum_{k=1}^{\infty}\rho_k}.
$$

这来自把均值方差写成全部样本对协方差之和。教学取 $\rho_k=a^k$、$a=0.8$，几何级数给出分母 $1+2a/(1-a)=9$；900 个等间隔样本约相当于 100 个独立样本，均值标准误比误当作 900 个独立样本时大 3 倍。实际数据可以用块平均检查平均窗和误差估计的稳定性，剔除初始增长阶段并保存所选区间。相邻时间点相关性的基本处理可参见 [NIST 的自相关说明](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm)；这里的数值为显式几何相关模型的推导。

PIC 粒子统计、Monte Carlo 中性粒子和中子输运的随机误差，也要与网格、时间步和模型误差分开。增加历史数或粒子数能改善特定统计量的采样，不能自动补偿遗漏的碰撞、错误边界或不合适的输运闭合。

### 制造解怎样把求解误差变成可测量量

对 $0<x<1$ 上的方程 $u_t=D u_{xx}+S$，选择光滑目标函数 $u_M=e^{-t}\sin(\pi x)$，边界取 $u(0,t)=u(1,t)=0$，初值取 $\sin(\pi x)$。分别求导，再定义源项：

$$
\partial_tu_M=-e^{-t}\sin(\pi x),\quad
\partial_{xx}u_M=-\pi^2e^{-t}\sin(\pi x),\quad
S=(D\pi^2-1)e^{-t}\sin(\pi x).
$$

中心差分的误差数值也能直接推出：在 $x=0.5,t=0$，相邻函数值均为 $\cos(\pi h)$，所以二阶导数离散值为 $2[\cos(\pi h)-1]/h^2$。精确值为 $-\pi^2$，将 $\cos(\pi h)=1-(\pi h)^2/2+(\pi h)^4/24+\cdots$ 代入，误差首项为 $\pi^4h^2/12$，因而步长减半时误差近似缩为四分之一。

如此初值、边界和源项共同使 $u_M$ 成为精确解。取无量纲 $D=0.10$，在 $x=0.5,t=0$ 的源为 $-0.01304$。用中心二阶差分计算该点二阶导数，网格 $h=0.05$ 与 $0.025$ 的绝对误差分别为 $0.02028$ 和 $0.005072$，比值约为 4，由 $p=\ln(E_h/E_{h/2})/\ln2$ 得到阶数约 2。随后同时细化时间步，并使边界离散采用一致阶数，就能区分空间误差、时间误差和边界误差。[Dudson 等《Verification of BOUT++ using the method of manufactured solutions》§2 式 (2)–(5)、§4.4](https://arxiv.org/pdf/1602.06747)说明源项和边界制造方法；上述正弦算例可独立复算。

## 可复现计算

一份可复现记录应能回答“用什么方程、什么版本、什么输入得到哪些结果”。本库建议把代码提交、依赖版本、编译选项、机器精度、输入文件、网格、初边值、随机种子、执行命令、输出校验值及分析脚本作为同一运行清单保存。重启计算应记录检查点来源，禁止覆盖原始输入后仍沿用旧标签。

报告以目标量组织：给出网格和时间步敏感性、守恒残差、参数不确定性及适用工况；保留未收敛和失败运行。图片需带物理单位、坐标定义和色标，使读者能还原数值对应的物理量。跨版本结果变化时先定位方程、数据、数值设置或后处理的变化，再判断物理解释。[BOUT++ Running 文档](https://bout-dev.readthedocs.io/en/latest/user_docs/running_bout.html)说明其输出可记录核心 Git 修订与构建信息；项目自己的模型和输入版本仍需另存。

### 获取条件和外部依赖

软件可见的网页、公开论文、可下载源码和可再分发软件是不同层次的条件。下表记录本次读取的获取路径与许可名称；实际使用时保存下载版本及随附许可。代码、外接求解器、装置数据、训练权重和原子/核数据库分别登记。

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| EFIT-AI | [官方许可页](https://efit-ai.gitlab.io/efit/license.html)列 BSD-2-Clause，同时附用户协议与邮件申请流程 | 该页另列分发、研究与发表要求，目标发行版按团队提供的完整条款确认；机器与诊断配置另备 |
| FreeGS / FreeGSNKE | 公开；[FreeGS](https://github.com/freegs-plasma/freegs/blob/master/LICENSE)、[FreeGSNKE](https://raw.githubusercontent.com/FusionComputingLab/freegsnke/main/LICENSE)均为 LGPL v3 | 平衡后端、机器几何、线圈数据和装置数据库接口 |
| VMEC2000 / DESC / SIMSOPT | 所核仓库分别为 [VMEC2000 MIT](https://raw.githubusercontent.com/hiddenSymmetries/VMEC2000/master/LICENSE)、[DESC MIT](https://raw.githubusercontent.com/PlasmaControl/DESC/master/LICENSE)、[SIMSOPT MIT](https://raw.githubusercontent.com/hiddenSymmetries/simsopt/master/LICENSE) | 该 VMEC 结论限定 hiddenSymmetries/VMEC2000 发行版；外接求解器及 MPI/HDF5/JAX 等运行依赖另查 |
| ELITE / M3D-C1 / NIMROD | ELITE 当前公开源码/标准许可未确认；[M3D-C1](https://m3dc1.pppl.gov/M3DC1_License.pdf)、[NIMROD](https://nimrodteam.org/code_access/)按团队协议申请 | 后两者有分发限制及结果使用相关条款；获取申请与团队支持周期计入项目安排 |
| JOREK | [ITER 官方仓库](https://github.com/iterorganization/JOREK)已公开，README 列 LGPL-3.0-or-later | 核对第三方组件、所选模型及社区规则；旧 Wiki 权限与公开代码权限分开 |
| GENE / GS2 / GTC | [GENE](https://www.genecode.org/license.html)按个人学术申请，限制再分发，非学术另议；[GS2](https://bitbucket.org/gyrokinetics/gs2/raw/master/LICENCE)为 MIT；[GTC](https://sun.ps.uci.edu/gtc/)为 BSD-3-Clause | 电子模型、几何接口、编译库与输入基准；不可把三个项目的条件合并成一种许可 |
| CGYRO / TGLF / TGYRO | [GACODE 主仓库](https://github.com/gafusion/gacode/blob/master/LICENSE)为 Apache-2.0 | 各模型与数据输入分别配置；更新饱和规则后重跑基准 |
| Gkeyll | [主仓库](https://github.com/gkeyllorg/gkeyll)为 MIT | 按 core/moments/vlasov/gyrokinetic 等实际模块及依赖构建 |
| SOLPS-ITER / EIRENE | [SOLPS-ITER](https://github.com/iterorganization/SOLPS-ITER)已公开、顶层 EUPL-1.1；[安装说明](https://solps-tutorials.readthedocs.io/installing/solps-iter-codebase/)仍要求确认 EIRENE 注册/许可 | [EIRENE](https://www.eirene.de/cgi-bin/eirene/write_temp.cgi?temp_dat=Download/download)列专用 EPL 或 CC BY-NC-ND 条款，不能只看顶层仓库；反应数据也应登记 |
| UEDGE / BOUT++ / SOLEDGE3X | [UEDGE](https://github.com/LLNL/UEDGE)为 LGPL-2.1；[BOUT++](https://bout-dev.readthedocs.io/en/latest/user_docs/introduction.html)为 LGPL-3.0-or-later；[SOLEDGE3X](https://soledge3x.onrender.com/)按需获取 | BOUT++ 的具体应用与模型另查；SOLEDGE3X 未核实标准开源许可，不从论文开放性推断 |
| TRANSP / JINTRAC / ASTRA / RAPTOR | [TRANSP](https://transp.pppl.gov/releases.html)须签协议，[现行协议文本](https://transp.pppl.gov/files/LicenseAgreement.pdf)区分研究与商业使用；[RAPTOR](https://crppwww.epfl.ch/~sauter/raptor/)官方页仍要求签转移/CLA 协议 | JINTRAC 的[UKAEA 公开应用论文](https://scientific-publications.ukaea.uk/wp-content/uploads/UKAEA-CCFE-CP2525.PDF)明确按许可使用；ASTRA 本次未确认现代发行许可，历史报告不可替代当前条款 |
| TORAX / QuaLiKiz / QLKNN | [TORAX 主体](https://github.com/google-deepmind/torax/blob/main/LICENSE)为 Apache-2.0；[QuaLiKiz](https://gitlab.com/qualikiz-group/QuaLiKiz/-/blob/main/LICENSE)为 CeCILL-C | TORAX 第三方数据另列许可；QLKNN 按具体模型的代码、权重与训练数据发行包分别核对 |
| OMFIT / IMAS | [OMFIT](https://omfit.io/install.html)要求用户协议并授予仓库权限；[IMAS](https://www.iter.org/node/20687/release-imas-infrastructure-and-physics-models-open-source)已发布多项开放组件 | OMFIT 不附带所有外部程序；IMAS 许可按各基础设施/物理软件仓库与版本核对 |
| GENRAY / GRAY / CQL3D | [GENRAY](https://github.com/compxco/genray/blob/master/LICENSE)、[CQL3D](https://raw.githubusercontent.com/compxco/cql3d/master/LICENSE)为 GPL-3.0-or-later；[GRAY](https://baltig.cnr.it/ectoplasm/gray/-/blob/master/LICENSE.md)采用自有用户协议，含非商业研究及修改限制 | 公开仓库并不使三者具有同样的用途和修改条件 |
| AORSA / TORIC / LUKE / NUBEAM | [AORSA](https://raw.githubusercontent.com/ORNL-Fusion/aorsa/master/LICENSE)所核仓库为 MIT；其余三者本次未确认独立发行许可 | 核对实际发行方、平台协议和依赖；[NUBEAM](https://w3.pppl.gov/ntcc/NUBEAM/abstract.html)所用 ADAS 数据另有协议 |
| ASCOT5 | [官方仓库](https://github.com/ascot4fusion/ascot5)列 LGPL v3 | 场数据、壁 CAD、原子数据和源粒子包分别保存来源 |
| OpenMC / MCNP / Paramak / DAGMC | [OpenMC](https://raw.githubusercontent.com/openmc-dev/openmc/develop/LICENSE)、[Paramak](https://raw.githubusercontent.com/fusion-energy/paramak/main/LICENSE)为 MIT；[DAGMC](https://raw.githubusercontent.com/svalinn/DAGMC/develop/LICENSE.txt)主体 Simplified BSD，部分目录例外；[MCNP](https://mcnp.lanl.gov/how_to_get_the_mcnp_code.html)经 RSICC 受控分发 | 核数据、耗损链、CAD 工具和 MCNP 分发包的权限及版本各自确认 |
| COMSOL / Ansys / MOOSE | [COMSOL](https://www.comsol.com/documentation/6.3.0.290/COMSOL_SoftwareLicenseAgreement.pdf)、[Ansys](https://ansys.synopsys.com/content/dam/legal/wla-july-29-2021.pdf)按自有商业协议；[MOOSE](https://raw.githubusercontent.com/idaholab/moose/master/LICENSE)框架为 LGPL-2.1 | 商业产品的具体模块、并行/网络许可按所购授权；MOOSE 具体应用与材料模型另查 |
| Smilei / WarpX / EPOCH | [Smilei](https://smileipic.github.io/Smilei/Overview/licence.html)为 CeCILL-B；[WarpX](https://github.com/BLAST-WarpX/warpx)为 BSD-3-Clause-LBNL；[EPOCH](https://github.com/epochpic/epoch)为 GPL-3.0 | 对照实际求解器与加速器后端、物理模块和输入数据 |

### 如何比较算力与使用成本

有 GPU、MPI 或隐式求解器，只说明存在某种运行路径。可执行文件构建、数据准备、JIT 首次编译、作业排队、求解、I/O 和后处理应分别计时。比较 CPU/GPU 时记录硬件、精度、内存、并行布局与通信；使用 JAX 等异步后端时，计时前须确保设备计算已经完成。比较相同目标误差下的成本，才能判断加速是否改善实际任务。

一个可用的 benchmark 记录可包含：共同物理算例、目标量与参考值、启用的方程项、所有网格和时间步、统计误差或残差、峰值内存、冷启动/重复运行时间、核时或 GPU 时、编译器及数学库。对模型优化还应记录外层迭代次数与失败率；单次通量调用更快，不一定让整体优化更快。

| 课题起点 | 建议先做的最小基线 | 扩展到下一层的依据 |
| --- | --- | --- |
| 托卡马克形状与控制 | FreeGS 静态平衡及约束；已有实验则先建立可信的平衡重建 | 需要电压与被动结构响应时接动态平衡；出现非轴对称 MHD 问题再选相应演化模型 |
| 仿星器设计 | 固定边界平衡与共同力残差，再做单一设计目标扫描 | 逐步加入线圈可制造性、快粒子/输运和扰动约束 |
| 芯部剖面与控制 | 简化几何、明确源项、已知输运闭合下的 TORAX/RAPTOR 或既有平台基线 | 先完成守恒与时间/网格收敛，再更换准线性/代理/非线性通量模型 |
| RF/NBI 方案 | 统一背景和输入功率，先对比沉积/出生及总预算 | 分布明显非热时加 FP；三维损失影响目标时加轨道与真实壁 |
| 偏滤器设计 | 用边缘平均输运约束上游、回收、辐射与靶热流 | 涨落与局部瞬态成为目标时，增加对应三维模型和诊断 |
| 包层与第一壁 | 简化几何固定源核输运，核对源率和每源 tally | 几何/材料敏感性明确后接 CAD，再把载荷保守映射到热结构网格 |

这里的起步路径来自前文模型范围与接口要求。团队若已有可复现装置输入、许可和经过核对的工作流，优先在其上建立共同基准；迁移软件应有明确的新物理需求、维护收益或计算收益。

### 一次计算需要留下的记录

| 记录 | 最少内容 |
| --- | --- |
| 问题与模型 | 目标量、方程/闭合、几何、启用模块、忽略项及适用尺度 |
| 软件身份 | 仓库和 commit/tag、补丁、许可、编译器、MPI/BLAS/JAX/CUDA 等依赖 |
| 物理数据 | 平衡与 COCOS、源/剖面、材料/同位素、核/原子数据、训练权重及各自来源版本 |
| 数值设置 | 网格/谱阶/速度域、时间步、粒子数、随机种子、边界、求解容差、耦合/松弛设置 |
| 执行与输出 | 命令、硬件/并行布局、日志、重启来源、输入输出散列、单位与分析脚本 |
| 可信度证据 | 守恒和耦合残差、加密/统计收敛、共同基准、实验比较及不确定性 |

### 让一个时间积分结果可以从配置独立重建

考虑 $\dot W=-W/\tau$，前向 Euler 法写为 $W_{k+1}=(1-\Delta t/\tau)W_k$，重复 $N$ 步得到 $W_N=W_0(1-\Delta t/\tau)^N$。把输入明确写为 $W_0=10^6$ J、$\tau=0.10$ s、$\Delta t=0.001$ s、$N=100$，终点时间便固定为 0.10 s，输出应为 $366032.34$ J。解析值 $W_0e^{-1}=367879.44$ J 给出相对误差约 $0.502\%$。将步长减半并改为 200 步，输出变为 $366957.82$ J，误差约减半，符合一阶时间积分。

Euler 更新来自对时间导数取前向差分 $(W_{k+1}-W_k)/\Delta t=-W_k/\tau$；解析解则对原方程分离变量积分得到 $\ln[W(t)/W_0]=-t/\tau$。固定终点 $t=N\Delta t$，将数值结果的对数展开为 $N\ln(1-\Delta t/\tau)=-t/\tau-t\Delta t/(2\tau^2)+O(\Delta t^2)$，就解释了其全局相对误差的一阶步长标度。

这个案例的复现包应同时保存配置、计算脚本、原始数值和解析比较。对原始配置字节计算 SHA-256，可检查两次运行是否实际读取同一文件；改变步长时保留两份配置及各自散列，文件顺序和编码也属于字节身份。软件版本与命令记录解释运行环境，解析结果解释数值是否合理。[Python hashlib 文档的 SHA-256 与 file_digest 部分](https://docs.python.org/3/library/hashlib.html)给出文件摘要接口；[BOUT++ 制造解论文 §2](https://arxiv.org/pdf/1602.06747)说明为何可重跑的测试还需要已知解和收敛比较。

[返回知识库](../README.md)
