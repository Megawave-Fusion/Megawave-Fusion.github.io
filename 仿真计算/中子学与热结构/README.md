# 中子学与热结构

从聚变中子源、核数据和几何出发，逐步把反应率与核热传递到工程网格。

## 固定源核输运与核数据库

### OpenMC 与 MCNP 的共同输入

中子和光子在材料中的输运与带电快粒子磁轨道是不同的问题。工程计算链可写为“参数/CAD 几何 → 几何检查与材料赋值 → 核输运与核热 → 热流/体热源映射 → 温度和结构响应”。

| 工具 | 核心角色 | 适合比较的任务 | 需要补齐的输入或模型 |
| --- | --- | --- | --- |
| [OpenMC](https://docs.openmc.org/en/stable/usersguide/beginners.html) / [MCNP](https://mcnp.lanl.gov/how_to_get_the_mcnp_code.html) | 本章关注的固定源中子/光子 Monte Carlo 输运 | 氚产生、屏蔽、核热和反应率；对齐几何、核数据和源后做统计比较 | 同位素/密度、连续能核数据、温度、源空间/能谱/角分布及 tally 定义 |

[OpenMC 核数据说明](https://docs.openmc.org/en/stable/usersguide/data.html)要求把数据库路径、评价/处理版本与温度纳入输入；更换评价库可能改变 TBR 和反应率，增加历史数不能消除这种系统差异。damage-energy tally 到 dpa 还需要位移损伤模型与参数，氚产生比到燃料自持还需要燃耗、库存、处理损失及停机收支。

### 聚变源到材料体热源

**聚变源—核热—温度应力。** 反应率与快离子模型提供中子空间、能谱和角分布；中子学求解各材料区的核热与反应率；工程模型再叠加表面热流、冷却和结构约束。保留每源粒子 tally 到 W 或 W/m³ 的归一化过程，以及核数据、材料密度和同位素组成版本。CAD 到输运网格、输运网格到有限元网格的两次映射分别检查总量。

这些是计算组织方案。选取其中一条时，应明确哪些模块已经真实相连、哪些载荷为外部给定，保存每次耦合调用的输入和输出版本。

### 获取与运行依赖

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| OpenMC | [官方仓库许可](https://raw.githubusercontent.com/openmc-dev/openmc/develop/LICENSE)为 MIT | 核数据、耗损链的权限及版本各自确认 |
| MCNP | [官方获取说明](https://mcnp.lanl.gov/how_to_get_the_mcnp_code.html)要求经 RSICC 受控分发 | 核数据及 MCNP 分发包的权限与版本各自确认 |

## 参数 CAD 与输运几何

### Paramak 与 DAGMC 的职责

| 工具 | 核心角色 | 适合比较的任务 | 需要补齐的输入或模型 |
| --- | --- | --- | --- |
| [Paramak](https://github.com/fusion-energy/paramak) / [DAGMC](https://github.com/svalinn/DAGMC) | 参数化聚变 CAD / 在 CAD 上提供输运几何与射线跟踪接口 | 自动扫描装置几何，保留材料区和复杂部件 | 仍需宿主输运器与核数据；检查水密性、重叠/缝隙、材料标签与体积 |

几何交接保留长度单位、材料区域和体积。先排查重叠、缝隙和无材料体积，再对简单几何比较反应率；参数扫描中每一组尺寸应对应唯一的几何文件与材料映射。DAGMC 提供宿主输运器使用的几何能力，核数据与源仍由输运计算另行配置。

### 获取与运行依赖：参数 CAD 与输运几何

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| Paramak / DAGMC | [Paramak](https://raw.githubusercontent.com/fusion-energy/paramak/main/LICENSE)为 MIT；[DAGMC](https://raw.githubusercontent.com/svalinn/DAGMC/develop/LICENSE.txt)主体 Simplified BSD，部分目录例外 | CAD 工具与宿主输运器的权限及版本各自确认 |

## 电磁损耗、温度与热应力

### 商业工程求解器与 MOOSE

| 工具 | 核心角色 | 适合比较的任务 | 需要补齐的输入或模型 |
| --- | --- | --- | --- |
| [COMSOL 电磁热接口](https://doc.comsol.com/6.3/doc/com.comsol.help.heat/heat_ug_theory.07.088.html) | 通用有限元电磁与热等多物理耦合，模块组合依任务选择 | 天线/传输部件损耗、介质/导体发热及热响应 | 端口、材料频散/温度关系、热边界与授权模块；热等离子体动理学响应须另建或导入 |
| [Ansys HFSS/Maxwell—Mechanical](https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Mechanical/Content/Mechanical/Two-WayCoupling.htm) | 高频/低频电磁与热结构工作流 | 电磁损耗到温升，温度反馈材料属性与损耗 | 表面/体损耗映射、冷却、接触、材料与双向迭代收敛；所引说明为 2025 R1 |
| [MOOSE](https://mooseframework.inl.gov/modules/electromagnetics/index.html) | 可开发的有限元多物理框架 | 自定义方程、材料和场/热/力耦合 | 框架与具体应用分开核验；当前所读电磁模块文档的波问题为 1D/2D，不能据此假定现成的任意三维 RF 能力 |

Ansys 的[热应力文档](https://ansyshelp.ansys.com/public/Views/Secured/corp/v242/en/wb_sim/ds_thermal_stress.html)说明如何把温度场传为结构热载荷。热结构选型要看材料非线性、接触、脉冲、冷却、网格和已有模型，而非只看是否写着“多物理”。表面热流 W/m²、体热源 W/m³ 和积分功率 W 分别传递；天线金属损耗、快粒子壁沉积与中子核热分别建账，芯部吸收功率不能直接作为天线金属热源。

### 获取与运行依赖：电磁损耗、温度与热应力

| 软件 | 本次核对的代码获取或许可 | 需要单独落实的部分 |
| --- | --- | --- |
| COMSOL / Ansys / MOOSE | [COMSOL](https://www.comsol.com/documentation/6.3.0.290/COMSOL_SoftwareLicenseAgreement.pdf)、[Ansys](https://ansys.synopsys.com/content/dam/legal/wla-july-29-2021.pdf)按自有商业协议；[MOOSE](https://raw.githubusercontent.com/idaholab/moose/master/LICENSE)框架为 LGPL-2.1 | 商业产品的具体模块、并行/网络许可按所购授权；MOOSE 具体应用与材料模型另查 |

## 每源中子结果与实际核热
### 源率归一化与功率算例

[OpenMC tally 文档](https://docs.openmc.org/en/stable/usersguide/tallies.html)给出的量通常按每源粒子归一。对以一个 D–T 反应中子为一个源粒子的固定源问题，设某部件的积分核热 tally 为 $H$（eV/source），真实中子源率为 $\dot N_n$（s⁻¹），则

$$
P_{\rm heat}=H\,\dot N_n\,(1.602176634\times10^{-19})\quad\mathrm W.
$$

该式是每源释放能量乘每秒源数。若给定 D–T 聚变总功率 $P_{\rm fus}$、每次反应取 17.6 MeV 且产生一个中子，则 $\dot N_n=P_{\rm fus}/(17.6\times10^6 e)$，这里 $e$ 的数值为每 eV 对应的焦耳数。取 $P_{\rm fus}=500$ MW、$H=9.0$ MeV/source，得到 $\dot N_n\simeq1.7732\times10^{20}$ s⁻¹，部件核热为 $500\times9/17.6\simeq255.68$ MW；若部件体积为 10 m³，其体积平均热源为 25.568 MW/m³。$H$ 在此为教学给定值，未由真实包层计算取得。

如果 tally 为体积分 flux，OpenMC 常用单位为 particle·cm/source，应先除以 tally 体积（cm³）再乘源率，得到 particle/(cm²·s)。若用另一种源粒子定义、源权重或多源采样，必须相应重建归一化。耦合光子输运与 heating/heating-local 的选择也应随核热结果记录。

### 计算图解

![核源率归一、功率映射与工程响应的单位链。](/assets/diagrams/sim-engineering.svg)

核源率归一、功率映射与工程响应的单位链。

[返回仿真计算总览](../README.md)
