#!/usr/bin/env python3
"""ICRF analytical teaching models and original diagrams; no Maxwell solver is run."""
from pathlib import Path
import cmath
import csv
from html import escape
import json
import math

try:
    from .simulation_figures import plot
except ImportError:
    from simulation_figures import plot

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / 'site/assets/diagrams'
DEFAULTS = dict(frequency_hz=50e6, strap_width_m=.06, strap_spacing_m=.18,
                inductance_h=100e-9, conductivity_s_m=5.8e7,
                scope='Given-current spectra and prescribed passive RF networks; not CAD-derived plasma coupling.')


def sinc(value):
    return math.sin(value)/value if abs(value) > 1e-14 else 1.


def current_spectrum(k, positions, currents, width):
    """Fourier integral of uniform sheet current K=I/width; I is strap current in A."""
    return sinc(k*width/2)*sum(I*cmath.exp(-1j*k*z) for z, I in zip(positions, currents))


def matvec(matrix, vector):
    return [sum(a*b for a, b in zip(row, vector)) for row in matrix]


def accepted_power(z, currents):
    voltage = matvec(z, currents)
    return sum(i.conjugate()*v for i, v in zip(currents, voltage)).real


def power_waves(voltage, current, z0=50.):
    return ((voltage+z0*current)/(2*math.sqrt(z0)),
            (voltage-z0*current)/(2*math.sqrt(z0)))


def conjugate_t(r1, r2, x=6.):
    return 1/(1/complex(r1, x)+1/complex(r2, -x))


def text(x, y, value, size=14, color='#294f65', anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(value)}</text>'


def rect(x, y, w, h, fill='#fff', stroke='#bed0dc', radius=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def line(x1, y1, x2, y2, color='#6d8ea2', arrow=False, dash=''):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="2"'+(' marker-end="url(#arrow)"' if arrow else '')+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'


def save_svg(name, title, subtitle, body, height=520):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle)}</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0L7 3L0 6" fill="none" stroke="#6d8ea2"/></marker></defs><rect width="1000" height="{height}" rx="12" fill="#f4f8fb"/><g font-family="system-ui,-apple-system,PingFang SC,Microsoft YaHei,sans-serif">{text(32,38,title,22)}{text(32,65,subtitle,12,'#627d8f')}{body}</g></svg>'''
    (FIGURES/(name+'.svg')).write_text(svg)


def diagrams():
    FIGURES.mkdir(parents=True, exist_ok=True)
    panels=[('单电流带',1,['馈电 + 短路 + 回流腔','单元阻抗、带边与间隙场']),
            ('双电流带',2,['相位 Δφ 与实际电流','互耦、双向谱与方向性']),
            ('三电流带',3,['中央 / 外侧幅相配合','边框电流与近场优化']),
            ('四电流带（2×2）',4,['辐射面和匹配网络分开','上下 / 左右互耦']),
            ('行波阵列（研究例）',7,['单元耦合 + 电容 + 终端','输出余功率单独计入'])]
    body=''
    for index,(title,count,notes) in enumerate(panels):
        x=30+(index%3)*325;y=91+(index//3)*235
        body+=rect(x,y,310,217)+text(x+15,y+28,title,16)
        body+=rect(x+35,y+42,240,100,'#eef3f7','#90acbd',2)
        positions=[(x+155,y+52)] if count==1 else [(x+85+i*130/(count-1),y+52) for i in range(count)]
        if count==4:positions=[(x+108,y+49),(x+192,y+49),(x+108,y+98),(x+192,y+98)]
        for sx,sy in positions:
            body+=rect(sx-7,sy,14,75 if count!=4 else 34,'#59aebd','#348497',1)
        for j,note in enumerate(notes):body+=text(x+15,y+169+j*24,note,13)
    body+=text(690,379,'结构图只表示辐射带排列',15)+text(690,410,'馈电、回流、屏与磁场须另建',13)+text(690,438,'共轭 T 属于电路拓扑',13)
    save_svg('icrf-common-antennas','五类天线模型：从单元到阵列','结构示意，不按比例；带数、馈电网络与等离子体响应分别定义',body,580)

    body=rect(35,99,430,315)+text(55,126,'单电流带：局部侧视 / 连接示意',16)
    body+=rect(75,165,205,205,'#e3ebf0','#66879b',1)+rect(85,175,195,185,'#fff','#fff',0)
    body+=rect(220,206,14,133,'#58aaba','#348497',1)+line(80,339,226,339,'#348497')
    body+=line(113,207,226,207,'#b16383')+line(113,150,113,207,'#b16383')
    body+=text(95,147,'馈入参考面',12)+text(108,330,'短路 / 回流',12)
    body+=text(167,270,'真空腔',14)+text(208,190,'带',12)
    for yy in range(180,350,23):body+=rect(280,yy,10,13,'#8ca5b2','#8ca5b2',0)
    body+=text(270,390,'法拉第屏',12)+rect(328,170,104,185,'#d5eef0','#82bdc5',1)+text(340,262,'等离子体',13)
    body+=line(295,155,326,155,arrow=True)+text(300,144,'间距',11)
    body+=line(78,395,150,395,arrow=True)+text(155,400,'x →',12)
    body+=text(505,124,'从几何到结果，保留三个独立输入层',17)
    for yy,title,detail in [(151,'几何与导体','尺寸、短路、连接、屏、圆角'),(234,'等离子体负载','nₑ(x)、B₀、组分、张量与开放边界'),(317,'馈电网络','端口模、参考面、阻抗、电容与终端')]:
        body+=rect(505,yy,456,64)+text(520,yy+25,title,15)+text(520,yy+48,detail,13)
    body+=text(36,463,'同一结构先做真空冷测，再加均匀负载与剖面；金属连接决定回流路径。',13)
    save_svg('icrf-model-hierarchy','单带最小模型与三层输入','示意图中的馈入只表示电连接；波端口应位于实际建模的均匀同轴截面',body)

    kvalues=[-50+i*.125 for i in range(801)]
    plot('icrf-two-strap-spectrum','双带相位与有限宽度电流谱','w=0.06 m、d=0.18 m；相同每带 RMS 电流，非等耦合功率比较',[
        (label,[(k,abs(current_spectrum(k,[0,.18],[1,cmath.exp(1j*phase)],.06))**2) for k in kvalues])
        for label,phase in [('Δφ=0',0),('Δφ=π',math.pi),('Δφ=π/2',math.pi/2)]],
        'k_z（m⁻¹；近似环向）','|J̃|² / |I|²',xmin=-50,xmax=50,ymax=4,xticks=5)

    body=''
    for x,label in [(140,'左侧'),(630,'右侧')]:
        body+=text(x,114,label,16)+rect(x,144,160,82)+rect(x,257,160,82)
        body+=text(x+25,179,'上带 + 串联电容',13)+text(x+25,204,'等效支路 Z₁',12)
        body+=text(x+25,292,'下带 + 串联电容',13)+text(x+25,317,'等效支路 Z₂',12)
        body+=line(x-50,187,x,187)+line(x-50,300,x,300)+line(x-50,187,x-50,300)
        body+=line(x-95,244,x-50,244,arrow=True)+text(x-90,230,'T',14)
    body+=line(312,186,614,186,dash='7 5')+line(312,298,614,298,dash='7 5')
    body+=text(406,216,'四端口面保留互耦',14)+text(375,265,'电磁响应 + 外部电容/馈线',13)
    body+=text(50,399,'教学独立双支路：Z₁=R+iX，Z₂=R−iX ⇒ Z_T=(R²+X²)/(2R)',17)
    body+=text(50,435,'真实带间耦合并未画成独立电阻；需连接完整 S/Z 矩阵计算。',13)
    save_svg('icrf-four-strap-network','四带几何与共轭 T：两种描述层次','按 WEST 的 2 环向 × 2 极向布局示意；支路不是单个裸 strap 的输入阻抗',body)

    xs=[-8+i*.02 for i in range(801)]
    plot('icrf-three-strap-spectrum','规定三带电流的低波数抵消','薄线阵列：两带 (1,−1)/√2、三带 (1,−2,1)/√6；只统一 Σ|I|²，未统一耦合功率',[
        ('双带：零阶消除',[(x,abs(sum(I*cmath.exp(-1j*x*z) for z,I in zip([-.5,.5],[1/math.sqrt(2),-1/math.sqrt(2)])))**2) for x in xs]),
        ('三带：再消一阶矩',[(x,abs(sum(I*cmath.exp(-1j*x*z) for z,I in zip([-1,0,1],[1/math.sqrt(6),-2/math.sqrt(6),1/math.sqrt(6)])))**2) for x in xs])],
        'k_z d（无量纲）','阵列因子平方',xmin=-8,xmax=8,ymax=3,xticks=4)

    body=text(35,111,'端口 1：入射 100% / 反射 1%',16)+text(641,111,'端口 2：匹配终端接收 49%',16)
    body+=line(38,235,121,235,arrow=True)+rect(125,147,750,180,'#fff','#a7c1ce',3)
    for i in range(7):
        xx=185+i*100
        body+=rect(xx-8,188,16,95,'#59aebd','#348497',1)+text(xx-5,307,str(i+1),12)
        body+=line(xx,172,xx,188)+line(xx-10,161,xx+10,161)+line(xx-10,167,xx+10,167)
        body+=line(xx,148,xx,161)
    body+=line(875,235,955,235,arrow=True)+text(240,365,'七端口电磁响应 + 各单元电容 ⇒ 输入 / 输出两端口',17)
    body+=text(245,406,'区域内交付 / 损耗 50% = 1 − 0.1² − 0.7²',17)
    body+=text(35,464,'无金属与其他损耗时差值才是等离子体耦合功率；出口接回收网络需重新求解。',13)
    save_svg('icrf-twa-termination','TWA 的电路闭合与功率账本','7 单元为文献研究结构；100/1/49/50% 为本库给定 S 参数的独立教学例',body)

    body=''
    for x,w,title,detail,color in [(30,170,'天线 / 真空腔','端口、带与回流','#e6edf3'),(200,70,'屏','真实条/理想边界','#d5e4ed'),(270,185,'边缘剖面','密度 / 磁场 / 截止','#d9eff1'),(455,240,'传播区域','波长、极化、净能流','#dfebf6'),(695,195,'ABL 或 PML','按实现分别加密','#ece0f0')]:
        body+=rect(x,150,w,170,color,'#a8bdcc',0)
        body+=text(x+w/2,209,title,14,anchor='middle')
        if w>100:body+=text(x+w/2,242,detail,12,anchor='middle')
    body+=line(80,350,914,350,arrow=True)+text(920,355,'x',14)
    body+=text(35,120,'物理区与数值开放边界分开；示意顺序不代表任意装置固定的截止位置',13)
    body+=text(35,399,'检查：端口净输入 = 金属损耗 + 物理等离子体耗散 + 出射能流',17)
    body+=text(35,438,'HFSS 2023 作者实现：等效电导 + ABL；RAPLICASOL：冷张量 + PML。',14)
    body+=text(35,475,'数值吸收层的耗散代表出域波，不作为核心热吸收的计算结果。',13)
    save_svg('icrf-domain-boundaries','几何、密度剖面与开放边界','计算域层次示意，不是特定放电的空间尺寸或有限元网格',body)


def generate(out=None):
    out=Path(out) if out else ROOT/'.build/icrf-antenna'
    out.mkdir(parents=True,exist_ok=True)
    params=dict(DEFAULTS)
    params['resonant_capacitance_f']=1/((2*math.pi*params['frequency_hz'])**2*params['inductance_h'])
    (out/'parameters.json').write_text(json.dumps(params,ensure_ascii=False,indent=2)+'\n')
    with (out/'two-strap-spectrum.csv').open('w',newline='') as handle:
        writer=csv.writer(handle);writer.writerow(['kz_per_m','same_phase','opposite_phase','quadrature_phase'])
        for n in range(801):
            k=-50+n*.125
            writer.writerow([k,*[abs(current_spectrum(k,[0,.18],[1,cmath.exp(1j*phase)],.06))**2 for phase in [0,math.pi,math.pi/2]]])
    z=[[2-20j,.5-4j],[.5-4j,2-20j]]
    powers=[]
    for phase_deg in range(0,181,5):
        currents=[100,100*cmath.exp(1j*math.radians(phase_deg))]
        powers.append(dict(phase_degree=phase_deg,accepted_power_w=accepted_power(z,currents)))
    (out/'mutual-power.json').write_text(json.dumps(powers,indent=2)+'\n')
    with (out/'conjugate-t.csv').open('w',newline='') as handle:
        writer=csv.writer(handle);writer.writerow(['R_ohm','symmetric_ZT_real','symmetric_ZT_imag','one_side_ZT_real','one_side_ZT_imag'])
        for n in range(1,201):
            r=n*.1;symmetric=conjugate_t(r,r);one_side=conjugate_t(r,2.)
            writer.writerow([r,symmetric.real,symmetric.imag,one_side.real,one_side.imag])
    diagrams()
    print(f'Analytical spectra, prescribed-network scans and 7 SVG figures -> {out}')


if __name__=='__main__':
    generate()
