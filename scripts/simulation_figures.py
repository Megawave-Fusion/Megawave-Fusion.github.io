"""Rebuild original SVG teaching diagrams from explicit, dimensionless models.

These are analytical/schematic teaching figures, not outputs of listed solvers.
"""
from pathlib import Path
from html import escape as esc
import math

OUT=Path(__file__).resolve().parents[1]/'site/assets/diagrams'
COLORS=['#087e95','#bb477b','#8b6b14','#6b67ac']

def frame(title,subtitle,body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 430" role="img" aria-labelledby="title desc"><title id="title">{esc(title)}</title><desc id="desc">{esc(subtitle)}</desc><defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0L7 3L0 6" fill="none" stroke="#6c899a"/></marker></defs><rect width="900" height="430" rx="14" fill="#f4f8fb"/><g font-family="system-ui,-apple-system,PingFang SC,Microsoft YaHei,sans-serif" fill="#203b50"><text x="35" y="39" font-size="21" font-weight="600">{esc(title)}</text><text x="35" y="66" fill="#627b8c" font-size="12">{esc(subtitle)}</text>{body}</g></svg>'''

def plot(name,title,subtitle,curves,xlabel,ylabel,xmax=1,ymax=1,xticks=5,yticks=4,extra='',xmin=0):
    body='';x0,y0,w,h=83,320,755,210
    for j in range(yticks+1):
        y=y0-h*j/yticks
        body+=f'<path d="M{x0} {y}H{x0+w}" stroke="#dce7ee"/><text x="{x0-12}" y="{y+4}" text-anchor="end" font-size="11">{ymax*j/yticks:.2g}</text>'
    for j in range(xticks+1):
        x=x0+w*j/xticks
        body+=f'<path d="M{x} {y0}v5" stroke="#7590a1"/><text x="{x}" y="{y0+21}" text-anchor="middle" font-size="11">{xmin+(xmax-xmin)*j/xticks:.2g}</text>'
    body+=f'<path d="M{x0} {y0-h}V{y0}H{x0+w}" fill="none" stroke="#7590a1"/><text x="{x0}" y="93" font-size="12">{esc(ylabel)}</text><text x="{x0+w}" y="{y0+45}" text-anchor="end" font-size="12">{esc(xlabel)}</text>'
    for i,(label,points) in enumerate(curves):
        points=' '.join(f'{x0+w*(x-xmin)/(xmax-xmin):.2f},{y0-h*y/ymax:.2f}' for x,y in points)
        c=COLORS[i%len(COLORS)]
        body+=f'<polyline points="{points}" stroke="{c}" fill="none" stroke-width="2.7" stroke-linejoin="round"/>'
        lx=90+i*245
        body+=f'<path d="M{lx} 397h24" stroke="{c}" stroke-width="3"/><text x="{lx+32}" y="401" font-size="12">{esc(label)}</text>'
    (OUT/(name+'.svg')).write_text(frame(title,subtitle,body+extra))

def flow(name,title,subtitle,steps,feedback=False):
    body='';width=180;gap=34;x0=(900-len(steps)*width-(len(steps)-1)*gap)/2
    for i,(label,lines) in enumerate(steps):
        x=x0+i*(width+gap);c=COLORS[i%4]
        body+=f'<rect x="{x}" y="132" width="{width}" height="146" rx="9" fill="white" stroke="#c9dce6"/><rect x="{x}" y="132" width="{width}" height="5" rx="2" fill="{c}"/><text x="{x+16}" y="165" font-size="15" font-weight="600">{esc(label)}</text>'
        for j,line in enumerate(lines):body+=f'<text x="{x+16}" y="{194+j*24}" font-size="12" fill="#536f82">{esc(line)}</text>'
        if i<len(steps)-1:body+=f'<path d="M{x+width+5} 206h{gap-10}" stroke="#6c899a" fill="none" marker-end="url(#arr)"/>'
    if feedback:
        last=x0+(len(steps)-1)*(width+gap)+width/2;first=x0+width/2
        body+=f'<path d="M{last} 285v42H{first}v-42" stroke="#a06f94" stroke-dasharray="6 5" fill="none" marker-end="url(#arr)"/><text x="450" y="351" text-anchor="middle" font-size="12" fill="#8d5d81">更新背景 / 分布，再核对收敛与功率</text>'
    body+='<text x="450" y="402" text-anchor="middle" fill="#718999" font-size="11">箭头表示计算数据交接；各模块的模型假设须分别保存</text>'
    (OUT/(name+'.svg')).write_text(frame(title,subtitle,body))

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    flow('sim-overview','从磁几何到可验证的预测','计算链示意；不表示每项研究都必须运行全部模块',[
        ('几何与背景',['平衡 / 磁场','密度、温度、组分']),('源与分布',['波吸收 / 束出生','碰撞、扩散、轨道']),('输运与负荷',['热 / 粒子 / 电流','边缘、核热与壁面']),('对照与复算',['守恒 / 收敛 / 误差','实验前向诊断'])],True)
    flow('sim-equilibrium','平衡重建与优化：输入约束不同','重建拟合实验；设计优化调整边界或线圈，二者的目标不可混用',[
        ('测量 / 设计变量',['磁探针、压力','边界、线圈、电流']),('平衡模型',['轴对称：EFIT / FreeGS','三维：VMEC / DESC']),('几何与残差',['ψ、q / 旋转变换','力平衡、拟合残差']),('下游 / 优化',['稳定性与输运','SIMSOPT 目标与约束'])],True)
    t=[i/100 for i in range(101)]
    plot('sim-mhd','线性增长率与扰动幅度','给定 γ 的单模教学模型 A(t)/A(0)=exp(γt)，不含非线性饱和',[
        ('γt₀ = +1',[(x,math.exp(x)) for x in t]),('γt₀ = −1',[(x,math.exp(-x)) for x in t])],'t / t₀','A / A₀',ymax=3)
    plot('sim-transport','源积分决定所需径向热通量','稳态圆柱、均匀沿轴，S=S₀(1−r²/a²)；Q 的单位是 W/m²',[
        ('S / S₀',[(x,1-x*x) for x in t]),('Q / (S₀a)',[(x,x/2-x**3/4) for x in t])],'r / a','归一化源与通量')
    flow('sim-gyrokinetic','陀螺动理学：三个选择维度','δf / full-f、局部 / 全局、网格 / 粒子是不同模型维度',[
        ('分布排序',['δf：围绕参考分布','full-f：演化全分布']),('径向范围',['flux tube：局部','global：剖面与边界']),('相空间离散',['网格：离散分布','PIC：加权标记']),('比较目标',['增长率与模结构','饱和通量及统计误差'])])
    flow('sim-edge','边缘排热与中性粒子回路','平均输运与涨落分开计算；原子过程改变粒子态与功率路径',[
        ('上游输入',['P_SOL、粒子通量','磁几何、杂质']),('等离子体',['平行 / 横向输运','辐射、复合与电离']),('中性粒子',['回收、荷交换','抽气与壁面边界']),('靶板观测',['热流、粒子流','温度、辐射与脱靶'])],True)
    flow('sim-numerics','守恒离散与粒子推进的检查点','离散方程满足什么守恒，需与连续方程的物理假设分别检查',[
        ('连续模型',['守恒律 / 场方程','初值与边界']),('离散与推进',['公共面数值通量','粒子沉积与推场']),('数值误差',['Δx、Δt、粒子数','稳定性与噪声']),('独立检验',['解析解 / 制造解','总量与阶数加密'])])
    flow('sim-rf-models','波模型与分布函数的接口','波长相对背景尺度、截止/模转换和所需输出决定模型',[
        ('发射条件',['位置、频率、偏振','实际角谱与净功率']),('波传播与吸收',['射线 / 准光学 / 全波','E、k、分物种功率']),('速度空间扩散',['RF 扩散 + 碰撞','非 Maxwell 分布']),('可比较输出',['有符号电流','碰撞热化与能量矩'])],True)
    flow('sim-icrh','ICRH：天线、热波、快尾与热化','直接 RF 吸收与随后碰撞给背景的热化功率分别记账',[
        ('端口与天线',['TOPICA / RAPLICASOL','电流谱、S/Z 与负载']),('热全波',['TORIC / AORSA','组分吸收与模转换']),('分布与轨道',['CQL3D / ORBIT-RF','快尾、轨道及损失']),('热源与观测',['Pₑ、Pᵢ、快尾储能','谱、诊断、背景输运'])],True)
    plot('sim-ecrh','有限束宽与定位：中心命中仍有有限宽度','横向 Gaussian 强度 I/I₀=exp[−2(x−d)²/w²]，取 w=20 mm；仅为束截面示意',[
        ('d = 0 mm',[(x,math.exp(-2*(x/20)**2)) for x in range(-60,61)]),('d = 20 mm',[(x,math.exp(-2*((x-20)/20)**2)) for x in range(-60,61)])],'x（mm）','I / I₀',xmax=60,xmin=-60,xticks=6)
    plot('sim-nbi','束停止与穿透：累计量分别归一','单能组份、常停止系数；仅含离化/荷交换时停止计入出生，孔径/结构损失另记',[
        ('剩余束 Γ / Γ₀',[(3*x,math.exp(-3*x)) for x in t]),('累计停止 / Γ₀',[(3*x,1-math.exp(-3*x)) for x in t])],'光学厚度 κs','归一化粒子流',xmax=3)
    flow('sim-lhcd','LHCD：发射谱与尾电子共同决定电流','每次模型比较使用同一净入射谱、平衡、碰撞和环向电场',[
        ('天线与谱',['ALOHA / 详细几何','净谱 P(N∥)']),('可达与传播',['GENRAY / TORLH','谱演化、SOL 与吸收']),('尾部与电流',['CQL3D：RF + 碰撞','平台、E∥ 与输运']),('共同检验',['波 / FP 功率矩','HXR、磁测与时序'])],True)
    flow('sim-ebw','O-X-B：转换与热波传播分段检验','冷全波的 O-X 窗口不等于已解析热 EBW 的 X-B 转换及吸收',[
        ('真空 O 波束',['角谱、偏振、束腰','截止层密度与磁场']),('O-X / X-B',['反射与转换能流','热响应、FLR 与短波']),('EBW 传播',['GENRAY / AMR','热色散、谐波吸收']),('分布与电流',['CQL3D / LUKE','准线性与有符号电流'])],True)
    c=299792458.;frequency=476e6;d=.05;phase=2*math.pi*frequency/c*3*d;n=8
    angles=[-5+i*.025 for i in range(401)];pattern=[]
    for N in angles:
        arg=phase-2*math.pi*frequency/c*N*d
        amp=sum(complex(math.cos(m*arg),math.sin(m*arg)) for m in range(n))
        pattern.append((N,abs(amp)**2/n**2))
    plot('sim-helicon','馈电相位如何选择方向谱','理想等幅 8 元线阵，476 MHz，间距 5 cm，相邻相位 85.7°；未含等离子体负载',[
        ('|Σ exp[im(Δφ−k∥d)]|² / 8²',pattern)],'N∥（谱峰位于 N∥=3）','归一化阵列因子',xmax=5,xmin=-5,xticks=5)
    flow('sim-engineering','从每源 tally 到工程热载荷','核数据、材料与几何同样属于输入；能量沉积与热应力分层求解',[
        ('源与几何',['D-T 源率（s⁻¹）','CAD、材料、核数据']),('核输运',['OpenMC / MCNP','eV/source、反应率']),('功率映射',['乘源率与 J/eV','保守转移到工程网格']),('热结构',['温度、边界与冷却','热应力、载荷时序'])])
    body=''
    for x,width,height,value,c in [(110,150,150,'2',COLORS[0]),(260,450,75,'1',COLORS[0]),(110,300,112.5,'1.5',COLORS[1]),(410,300,75,'1',COLORS[1])]:
        y=240 if c==COLORS[0] else 360;hh=height*.6
        body+=f'<rect x="{x}" y="{y-hh}" width="{width}" height="{hh}" fill="{c}" opacity=".2" stroke="{c}"/><text x="{x+width/2}" y="{y-hh-8}" text-anchor="middle" font-size="15">{value}</text>'
    body+='<text x="35" y="205" font-size="12">旧网格</text><text x="35" y="330" font-size="12">新网格</text><text x="760" y="199" font-size="14">∫ S dV = 5 MW</text><text x="760" y="335" font-size="14">∫ S dV = 5 MW</text><text x="110" y="387" font-size="12">0</text><text x="260" y="260" font-size="12">1</text><text x="410" y="387" font-size="12">2</text><text x="710" y="387" font-size="12">4　V (m³)</text>'
    (OUT/'sim-coupling.svg').write_text(frame('保守重映射保留积分功率','S 的单位 MW/m³；按体积重叠转移单元平均值，柱高按同一比例绘制',body))
    h=[i/100 for i in range(101)]
    plot('sim-validation','用加密比估计离散阶数','E(h)=Chᵖ，C=1；加密比 p=ln[E(h)/E(h/r)]/ln r；线性坐标曲线的斜率不等于 p',[
        ('一阶：E / C = h',[(x,x) for x in h]),('二阶：E / C = h²',[(x,x*x) for x in h])],'归一化网格尺度 h','归一化误差 E / C')
    plot('sim-reproducibility','时间步属于可复算输入','dW/dt=−νW；显式 Euler 取 νΔt=0.2，与解析解比较',[
        ('解析 exp(−νt)',[(3*x,math.exp(-3*x)) for x in t]),('Euler：0.8ⁿ',[(.2*i,.8**i) for i in range(16)])],'νt','W / W₀',xmax=3)
    print('Generated 18 original simulation teaching figures')

if __name__=='__main__':main()
