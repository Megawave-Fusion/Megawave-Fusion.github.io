# 文献资料

学习资料应帮助读者找到概念的来源，也帮助维护者判断一条结论究竟有多强。本页以公开课程、原论文和机构资料组织学习入口；核对日期为 2026-10-16。入口核对、章节阅读和全文审阅是不同工作，不因链接可以打开就称资料已被全面验证。

## 学习路径

### 从基本尺度走向一个完整问题

先学 [等离子体基本概念](../基础原理/等离子体基本概念/README.md)，能解释温度、密度、德拜屏蔽、准中性以及各条件何时失效；再读 [单粒子运动](../基础原理/单粒子运动/README.md)，区分回旋、漂移、导心与约束。随后进入 [动理学与碰撞](../基础原理/动理学与碰撞/README.md)，理解分布函数、矩、弛豫和非热粒子，避免把所有粒子群都用一个温度代表。

[流体与磁流体力学](../基础原理/流体与磁流体力学/README.md)建立宏观平衡和稳定性的语言，[等离子体波](../基础原理/等离子体波/README.md)连接色散、共振和波粒交换。顺序依据概念依赖安排，不要求把整本教材读完才进入具体问题。基础阶段可沿 [MIT 22.611J 讲义目录](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/pages/lecture-notes/)的单粒子、碰撞、流体及波动章节推进；本次核对课程目录及主题对应，不声称重审了全部讲义推导。

### 把专题读成一条证据链

选择 [ICRH](../辅助加热/离子回旋加热/README.md)、[ECRH](../辅助加热/电子回旋加热/README.md)、[NBI](../辅助加热/中性束注入/README.md) 或 [LHCD](../辅助加热/低杂波电流驱动/README.md) 后，依次回答：能量从哪里进入、怎样到达等离子体、哪些粒子吸收、如何热化或驱动电流、哪些诊断能检验、哪些损失仍未解释。这样可以把物理机制与电源、传输、壁面及控制接口连接起来。

每轮阅读产出一页说明：问题和适用条件、关键公式及符号、可观察量、来源位置、一个独立复算和未解决项。随后用 [诊断控制](../诊断控制/README.md)、[仿真计算](../仿真计算/README.md) 与 [实验运行](../实验运行/README.md)检查模型和证据是否真正闭合。能复述摘要，不等于能复现结论。

## 论文、教材、课程与会议

### 可直接进入的公开资料

- [MIT 22.611J Introduction to Plasma Physics I，2003](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/pages/lecture-notes/)：基础课程讲义入口；适合按单粒子、碰撞、流体和波动建立概念顺序。
- [MIT 22.616 Plasma Transport Theory，2003](https://ocw.mit.edu/courses/22-616-plasma-transport-theory-fall-2003/)：课程说明列出 Fokker–Planck、碰撞弛豫、经典与新经典输运；适合在基本动理学之后学习。本次核对课程说明。
- [MIT 22.67J Principles of Plasma Diagnostics，2023](https://ocw.mit.edu/courses/22-67j-principles-of-plasma-diagnostics-fall-2023/download/)：公开视频、习题与材料入口。诊断页另引用实际读取的 Magnetics I 文字稿；这里只核对资源目录。
- [PPPL Diallo：Laser-Aided Plasma Diagnostics，2018](https://gss.pppl.gov/talks/LASER-AIDED-COURSE-2018v7.pdf)：已读取干涉、Thomson 散射及集体/非集体区分部分；讲义适合搭建原理框架，具体仪器误差仍需原论文。
- [NIST TN 1297](https://www.nist.gov/pml/nist-technical-note-1297)：测量不确定性的公开指南；本次实际读取附录 A 的传播公式及第 6 节覆盖因子，用于本库计量说明。

### 用原论文检验“方法有效”的范围

[Dudson 等，Verification of BOUT++ by the Method of Manufactured Solutions，2016](https://arxiv.org/abs/1602.06747)是数值方法验证的例子：作者以制造解检验实现与收敛阶数。本次读取摘要，未独立重跑测试，因此这里只作为原论文和方法入口。

[Frank 等，Verifying raytracing/Fokker–Planck lower-hybrid current drive predictions with self-consistent full-wave/Fokker–Planck simulations，2022](https://arxiv.org/abs/2207.09011)把全波与 FP 功率自洽联系起来，并讨论特定算例中全波与射线的差异。本次读取摘要；不能把它扩写成“全波总能解决实验差异”或“所有低杂波场景都只需射线”。

会议摘要能证明作者报告过一项工作，但通常不足以核对完整误差分析。新闻适合确定机构声明、项目日期或公开结果入口；精确物理结论优先追溯论文、数据和补充材料。综述用于建立谱系，教材用于稳定概念，二者都不替代某个新结果的原始证据。

### 笔记必须保留版本与符号

同一个 DOI 可能关联在线先行、正式排版及勘误；预印本还应注明版本号。记录作者、题名、年份、期刊或机构、URL/DOI、实际阅读范围和核对日期，并保存引用的节、公式或图号。引用别人引用的结果时，未取得原文就明确写“转引”，不要假装直接核对。

读公式先检查 SI 与 Gaussian 单位制、温度是 K 还是以能量单位表达、\(\omega\) 与 \(f\) 是否相差 \(2\pi\)、回旋频率是否带电荷符号、傅里叶时间因子采用哪一号。磁通坐标、半径归一化和热速度定义也可能不同。同名量比较前先写转换关系，再讨论数值差异。

## 术语表

以下释义用于统一本库阅读口径，物理细节以链接专题为准。加热术语与系统归属见 [辅助加热](../辅助加热/README.md)；通用工程名词可与 [ITER Fusion Glossary](https://www.iter.org/fusion-glossary)核对，但简短词条不能替代严格模型定义。

### 加热、驱动与粒子

| 缩写 | 中文 / 英文 | 使用注意 |
| --- | --- | --- |
| ICRH | 离子回旋共振加热 / Ion Cyclotron Resonance Heating | 说明物种、谐波和吸收路径 |
| ICRF | 离子回旋频段 / Ion Cyclotron Range of Frequencies | 频段名称不唯一决定吸收机制 |
| ECRH | 电子回旋共振加热 / Electron Cyclotron Resonance Heating | 注明波模、谐波和可达性 |
| ECCD | 电子回旋电流驱动 / Electron Cyclotron Current Drive | 电流方向和驱动效率单列 |
| NBI | 中性束注入 / Neutral Beam Injection | 注入功率、沉积功率与热化功率区分 |
| NBCD | 中性束电流驱动 / Neutral Beam Current Drive | 不是束电流直接等于等离子体驱动电流 |
| LHCD | 低杂波电流驱动 / Lower Hybrid Current Drive | 与 LHH 的加热目标区分 |
| EBW | 电子伯恩斯坦波 / Electron Bernstein Wave | 记录模转换和耦合条件 |
| CX | 电荷交换 / Charge Exchange | 粒子电荷状态改变，不等于核反应 |
| EP | 高能粒子 / Energetic Particle | “高能”相对于所讨论背景与问题定义 |

### 约束、边界与工程

| 缩写 | 中文 / 英文 | 使用注意 |
| --- | --- | --- |
| FRC | 场反位形 / Field-Reversed Configuration | 与反场箍缩不同 |
| RFP | 反场箍缩 / Reversed-Field Pinch | 独立装置路线 |
| MHD | 磁流体力学 / Magnetohydrodynamics | 明确理想、电阻或扩展模型 |
| LCFS | 最后闭合磁面 / Last Closed Flux Surface | 几何和磁场重建约定要一致 |
| SOL | 刮削层 / Scrape-Off Layer | 关注开磁力线和材料边界连接 |
| PFC | 面向等离子体部件 / Plasma-Facing Component | 不是整个真空室的同义词 |
| PWI | 等离子体与壁相互作用 / Plasma-Wall Interaction | 入射粒子和表面条件不可省略 |
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
| IR | 红外 / Infrared | 辐亮度、表面温度、反演热流不是同一量 |
| PIC | 网格粒子法 / Particle-In-Cell | 宏粒子权重及统计噪声需报告 |
| FP | Fokker–Planck | 注明碰撞、波致扩散、源汇及边界 |
| GK | 回旋动理学 / Gyrokinetics | 依赖时间尺度与磁化排序 |
| MMS | 制造解方法 / Method of Manufactured Solutions | 检查实现，不能证明实验适用性 |
| V&V | 验证与确认 / Verification and Validation | 方程求解正确性与物理适用性分开 |
| UQ | 不确定性量化 / Uncertainty Quantification | 区分输入、模型和数值来源 |
| CODAC | 控制、数据访问与通信 / Control, Data Access and Communication | ITER 架构中的正常控制不代替独立保护 |

## 参考来源

正文附近的来源优先服务具体结论，结构化记录集中在 [来源索引](来源索引.json)。本库采用“证据类型 + 阅读范围 + 审核状态”三个独立维度：解析推导、数值仿真、实验测量和工程测试回答的问题不同；摘要、指定章节与全文表示核对深度；草稿或资料核对完成不等于专家审核完成。

引用链应能从结论回到原位置。旧版本、反例、失败算例和不一致测量也应保留，不能只收支持预期的材料。后续更新应指出变更的事实、适用条件和来源，避免以新的访问日期替换旧论文的发表日期。本轮公开资料核对不包含未公开的项目记录、供应商验收报告或装置原始数据。

[返回知识库](../README.md)
