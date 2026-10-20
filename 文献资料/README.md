# 学习路径与文献使用

本页以公开课程、原论文和机构资料组织学习入口，连接概念出处与结论强度。核对日期为 2026-10-16；阅读范围区分入口、指定章节与全文。

## 学习路径

### 从基本尺度走向一个完整问题

先学 [等离子体基本概念](../基础原理/等离子体基本概念/README.md)，能解释温度、密度、德拜屏蔽、准中性以及各条件何时失效；再读 [单粒子运动](../基础原理/单粒子运动/README.md)，区分回旋、漂移、导心与约束。随后进入 [动理学与碰撞](../基础原理/动理学与碰撞/README.md)，理解分布函数、矩、弛豫和非热粒子，避免把所有粒子群都用一个温度代表。

[流体与磁流体力学](../基础原理/流体与磁流体力学/README.md)建立宏观平衡和稳定性的语言，[等离子体波](../基础原理/等离子体波/README.md)连接色散、共振和波粒交换。顺序依据概念依赖安排，不要求把整本教材读完才进入具体问题。基础阶段可沿 [MIT 22.611J 讲义目录](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/pages/lecture-notes/)的单粒子、碰撞、流体及波动章节推进。

### 把专题读成一条证据链

选择 [ICRH](../辅助加热/离子回旋加热/README.md)、[ECRH](../辅助加热/电子回旋加热/README.md)、[NBI](../辅助加热/中性束注入/README.md) 或 [LHCD](../辅助加热/低杂波电流驱动/README.md) 后，依次回答：能量从哪里进入、怎样到达等离子体、哪些粒子吸收、如何热化或驱动电流、哪些诊断能检验、哪些损失仍未解释。这样可以把物理机制与电源、传输、壁面及控制接口连接起来。

每轮阅读记录问题/条件、公式/符号、观测量、来源位置、独立复算和未决项，再用 [诊断控制](../诊断控制/README.md)、[仿真计算](../仿真计算/README.md)、[实验运行](../实验运行/README.md)检查证据闭合。

### 用一条可完成的任务贯通基础到测量

以“由干涉相位得到含单位和误差的密度”为任务，学习顺序为电子响应、波色散、路径积分和误差传播，每步保留可检查的中间量。

冷、非磁化、高频电子的推导链为

$$
n_{\rm ref}^2=1-\frac{\omega_{pe}^2}{\omega^2},\quad
\Delta\phi=\frac\omega c\int(n_{\rm ref}-1)dl
\simeq-r_e\lambda\int n_e\,dl,
$$

其中 $\omega_{pe}^2=n_ee^2/(\epsilon_0m_e)$、$r_e=e^2/(4\pi\epsilon_0m_ec^2)$、$\omega=2\pi c/\lambda$。均匀直弦反算 $n_e=-\Delta\phi/(r_e\lambda L)$；仅相位有误差时，$u(n_e)/n_e=u(\phi)/|\Delta\phi|$。完整电子响应见[诊断方法](../诊断控制/README.md)。

例如先给定直线路径上恒定密度 $n_e=3.0\times10^{19}$ m⁻³、长度 $L=0.60$ m，则弦积分为 $N_e=n_eL=1.8\times10^{19}$ m⁻²。波长 10.6 μm 时，用 $\Delta\phi=-r_e\lambda N_e$ 预测相移约 $-0.538$ rad；接着将这相位反算回密度，检查单位链闭合。若相位标准不确定度为 0.010 rad，仅这一项产生约 $1.86\%$ 的相对密度不确定度。完成这一任务后，再将恒定密度替换为径向剖面，就自然进入多弦重建。色散到干涉的学习材料可用 [IPP 讲义式 (20)–(28)、(42)–(44)](https://www.ipp.mpg.de/2882460/anleitung.pdf)，误差传播接到 [NIST TN 1297 附录 A](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)。

## 论文、教材、课程与会议

### 可直接进入的公开资料

- [MIT 22.611J Introduction to Plasma Physics I，2003](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/pages/lecture-notes/)：基础课程讲义入口；适合按单粒子、碰撞、流体和波动建立概念顺序。
- [MIT 22.616 Plasma Transport Theory，2003](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/)：课程说明列出 Fokker–Planck、碰撞弛豫、经典与新经典输运；适合在基本动理学之后学习。
- [MIT 22.67J Principles of Plasma Diagnostics，2023](https://ocw.mit.edu/courses/22-67j-principles-of-plasma-diagnostics-fall-2023/download/)：公开视频、习题与材料入口。诊断页另引用实际读取的 Magnetics I 文字稿；这里只核对资源目录。
- [PPPL Diallo：Laser-Aided Plasma Diagnostics，2018](https://gss.pppl.gov/talks/LASER-AIDED-COURSE-2018v7.pdf)：已读取干涉、Thomson 散射及集体/非集体区分部分；讲义适合搭建原理框架，具体仪器误差仍需原论文。
- [NIST TN 1297](https://www.nist.gov/pml/nist-technical-note-1297)：测量不确定性的公开指南；附录 A 解释不确定度传播，第 6 节说明覆盖因子。

### 用原论文检验“方法有效”的范围

[Dudson 等，Verification of BOUT++ by the Method of Manufactured Solutions，2016](https://arxiv.org/abs/1602.06747)是数值方法验证的例子：作者以制造解检验实现与收敛阶数。原文 §2 给出制造源项与边界条件，§4.3 的波动方程和 §4.4 的扩散问题展示了收敛检验。

[Frank 等，2022](https://arxiv.org/abs/2207.09011)连接全波/FP 功率自洽与射线比较；选择模型时需回到具体工况及数值条件，不能从摘要的某次差异推广出通用结论。

依据：[Frank 等，Verifying raytracing/Fokker–Planck lower-hybrid current drive predictions with self-consistent full-wave/Fokker–Planck simulations，2022](https://arxiv.org/abs/2207.09011)。

会议摘要能证明作者报告过一项工作，但通常不足以核对完整误差分析。新闻适合确定机构声明、项目日期或公开结果入口；精确物理结论优先追溯论文、数据和补充材料。综述用于建立谱系，教材用于稳定概念，二者都不替代某个新结果的原始证据。

### 笔记必须保留版本与符号

同一个 DOI 可能关联在线先行、正式排版及勘误；预印本还应注明版本号。记录作者、题名、年份、期刊或机构、URL/DOI、实际阅读范围和核对日期，并保存引用的节、公式或图号。引用别人引用的结果时，未取得原文就明确写“转引”，不要假装直接核对。

读公式先检查 SI 与 Gaussian 单位制、温度是 K 还是以能量单位表达、$\omega$ 与 $f$ 是否相差 $2\pi$、回旋频率是否带电荷符号、傅里叶时间因子采用哪一号。磁通坐标、半径归一化和热速度定义也可能不同。同名量比较前先写转换关系，再讨论数值差异。

### 实际阅读一篇方法论文的推导与图表

以 [Dudson 等的 BOUT++ 制造解论文](https://arxiv.org/pdf/1602.06747)为一张完整阅读卡。先从 §2 找到作者要解决的问题：如何检查实现的偏微分方程与边界条件。接着把式 (2) 的源项构造 $S=\partial_tf_M-F(f_M)$ 抄成自己的符号，并与式 (4)–(5) 的边界构造相连。然后进入 §4.3 的波动方程测试，检查图 4 所画误差范数、横轴网格尺度和报告的约 1.97 收敛阶；随后在 §4.4 查看扩散测试。这样“方法—实现—证据”各有一个可回查位置。

若程序解 $\partial_tf=F(f)+S$，指定 $f_M$ 后令 $S=\partial_tf_M-F(f_M)$ 即逐项满足方程。中心差分的 Taylor 链为

$$
f(x+h)+f(x-h)-2f(x)
=h^2f''(x)+\frac{h^4}{12}f^{(4)}(x)+O(h^6).
$$

除以 $h^2$ 即得下面的二阶截断误差。

可以补做一个独立的小复算：对 $f(x)=\sin x$，在 $x=\pi/2$ 用中心差分，$D_h^2f=2(\cos h-1)/h^2$，精确二阶导数为 $-1$。Taylor 展开给出误差 $h^2/12+O(h^4)$，所以 $h=0.20$ 与 $0.10$ 的误差约为 $0.003329$ 和 $0.0008331$，比值趋近 4。这是理解论文二阶收敛图的一块可计算拼图。教材用于补齐推导，论文用于追踪测试对象与结果，课程可补例题，会议摘要则可用于定位后续全文与版本。

## 术语表

以下释义用于统一本库阅读口径，物理细节以链接专题为准。加热术语与系统归属见 [辅助加热](../辅助加热/README.md)；通用工程名词可与 [ITER Fusion Glossary](https://www.iter.org/fusion-glossary)核对，随后回到专题中的模型定义。

### 加热、驱动与粒子

| 缩写 | 中文 / 英文 | 使用注意 |
| --- | --- | --- |
| ICRH | 离子回旋共振加热 / Ion Cyclotron Resonance Heating | 说明物种、谐波和吸收路径 |
| ICRF | 离子回旋频段 / Ion Cyclotron Range of Frequencies | 频段名称不唯一决定吸收机制 |
| ECRH | 电子回旋共振加热 / Electron Cyclotron Resonance Heating | 注明波模、谐波和可达性 |
| ECCD | 电子回旋电流驱动 / Electron Cyclotron Current Drive | 电流方向和驱动效率单列 |
| NBI | 中性束注入 / Neutral Beam Injection | 注入功率、沉积功率与热化功率区分 |
| NBCD | 中性束电流驱动 / Neutral Beam Current Drive | 驱动电流包含快离子贡献与背景响应 |
| LHCD | 低杂波电流驱动 / Lower Hybrid Current Drive | 与 LHH 的加热目标区分 |
| EBW | 电子伯恩斯坦波 / Electron Bernstein Wave | 记录模转换和耦合条件 |
| CX | 电荷交换 / Charge Exchange | 电子转移导致粒子电荷状态改变 |
| EP | 高能粒子 / Energetic Particle | “高能”相对于所讨论背景与问题定义 |

### 约束、边界与工程

| 缩写 | 中文 / 英文 | 使用注意 |
| --- | --- | --- |
| FRC | 场反位形 / Field-Reversed Configuration | 与反场箍缩不同 |
| RFP | 反场箍缩 / Reversed-Field Pinch | 独立装置路线 |
| MHD | 磁流体力学 / Magnetohydrodynamics | 明确理想、电阻或扩展模型 |
| LCFS | 最后闭合磁面 / Last Closed Flux Surface | 几何和磁场重建约定要一致 |
| SOL | 刮削层 / Scrape-Off Layer | 关注开磁力线和材料边界连接 |
| PFC | 面向等离子体部件 / Plasma-Facing Component | 直接面对等离子体的表面及相应组件 |
| PWI | 等离子体与壁相互作用 / Plasma-Wall Interaction | 按入射粒子分布和表面状态描述 |
| ELM | 边缘局域模 / Edge Localized Mode | 不与整次放电破裂混称 |
| TBR | 氚增殖比 / Tritium Breeding Ratio | 核对产氚/耗氚边界，不直接等于全厂自持 |
| TRL | 技术成熟度等级 / Technology Readiness Level | 附技术对象、环境和退出证据 |
| Q | 增益 / Gain | 必须每次定义分子、分母和时间窗 |

### 诊断、计算与证据

| 缩写 | 中文 / 英文 | 使用注意 |
| --- | --- | --- |
| TS | 汤姆逊散射 / Thomson Scattering | 区分集体与非集体 |
| ECE | 电子回旋辐射 / Electron Cyclotron Emission | 亮温等于电子温度需要条件 |
| CXRS | 电荷交换复合光谱 / Charge Exchange Recombination Spectroscopy | 记录束、谱线和被动背景 |
| IR | 红外 / Infrared | 由辐亮度校正得温度，再由导热反演热流 |
| PIC | 网格粒子法 / Particle-In-Cell | 宏粒子权重及统计噪声需报告 |
| FP | Fokker–Planck | 注明碰撞、波致扩散、源汇及边界 |
| GK | 回旋动理学 / Gyrokinetics | 依赖时间尺度与磁化排序 |
| MMS | 制造解方法 / Method of Manufactured Solutions | 以已知解检查方程的数值实现 |
| V&V | 验证与确认 / Verification and Validation | 方程求解正确性与物理适用性分开 |
| UQ | 不确定性量化 / Uncertainty Quantification | 区分输入、模型和数值来源 |
| CODAC | 控制、数据访问与通信 / Control, Data Access and Communication | ITER 架构中的正常控制不代替独立保护 |

### 用归一化检查两种热速度约定

热速度常见两种记法：$\sigma=\sqrt{T/m}$ 是一维速度标准差，$v_{\rm th}=\sqrt{2T/m}$ 是 Maxwell 分布指数中常用的尺度；这里 $T$ 表示能量。把同一个一维分布写成两种形式，

$$
f(v)=\frac{n}{\sqrt{2\pi}\sigma}e^{-v^2/(2\sigma^2)}
=\frac{n}{\sqrt{\pi}v_{\rm th}}e^{-v^2/v_{\rm th}^2},
\qquad v_{\rm th}=\sqrt2\,\sigma .
$$

取 $z=v/\sigma$，高斯积分及分部积分给

$$
\int e^{-z^2/2}dz=\sqrt{2\pi},\qquad
\int z^2e^{-z^2/2}dz=\sqrt{2\pi},
$$

两式积分限均为 $(-\infty,\infty)$。故零阶矩为 $n$、二阶矩为 $n\sigma^2$；由 $T=m\langle v^2\rangle$ 得 $\sigma^2=T/m$。对应两种指数便有 $v_{\rm th}^2=2\sigma^2$。

对速度积分，两式都给 $\int f\,dv=n$；二阶矩也都给 $\int v^2f\,dv/n=T/m$。所以核对术语时，检查公式与矩比只比较“thermal speed”字样更直接。教学取电子温度 100 eV，先换成 $1.60218\times10^{-17}$ J，再得到 $\sigma=4.19\times10^6$ m/s、$v_{\rm th}=5.93\times10^6$ m/s。将后者误代入以 $\sigma$ 书写的指数会使计算温度增大一倍。[Fitzpatrick《Maxwellian Distribution》，式 (3.145)–(3.146)](https://farside.ph.utexas.edu/teaching/plasma/lectures1/node41.html)采用含因子 2 的尺度；术语卡应把符号、公式、单位和来源约定一起保存。

## 参考来源

正文附近的来源优先服务具体结论，结构化记录集中在 [来源索引](来源索引.json)。本库采用“证据类型 + 阅读范围 + 审核状态”三个独立维度：解析推导、数值仿真、实验测量和工程测试回答的问题不同；摘要、指定章节与全文表示核对深度；审核状态记录实际完成的检查。

引用从结论回到原文位置，并保留旧版、反例、失败算例和不一致测量。更新记录事实、条件与来源的变化；访问日期与发表日期分别保存。

### 把同一篇论文的不同入口归为一条可追踪记录

![同一文献的身份、版本、引用位置与复算记录分别追踪。](/assets/diagrams/system-literature-trace.svg)

整理 [arXiv 摘要入口](https://arxiv.org/abs/1602.06747)与[对应 PDF](https://arxiv.org/pdf/1602.06747)时，核对题名、作者、版本和日期，再记录本次实际读到的 §2、§4.4。两入口合并到同一文献身份；更新时保留旧版本及方程/图号变动。

依据：[arXiv:1602.06747 的摘要页](https://arxiv.org/abs/1602.06747)。

涉及正式出版物时，可以通过 [Crossref REST API 的 Quick start 与 Endpoints](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)读取 DOI 对应元数据，以题名、作者和年份交叉核对。实际维护一条引用时，按“文献身份→所用版本→具体位置→支持的句子→访问日期”连接起来：例如该论文 §2 支持制造源项的构造，§4.4 支持扩散离散的收敛测试；新写的教学正弦算例另列自己的复算记录。这样既能去掉重复入口，也能在原文更新后准确找到需要重查的知识条目。

[返回知识库](../README.md)
