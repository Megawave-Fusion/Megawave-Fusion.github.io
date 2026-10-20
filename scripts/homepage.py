"""Small, source-driven landing page; scientific artwork is explicitly schematic."""


def homepage(chapters, sections, entries, references):
    routes = [
        ('01', '基础物理', '从轨道、碰撞到波与不稳定性', '/chapters/foundations/', r'm\dot{\mathbf v}=q(\mathbf E+\mathbf v\times\mathbf B)', 'cyan'),
        ('02', '加热与电流', '六套系统，各自的能量路径', '/chapters/heating/', r'P_{\rm abs}=\int_V\langle\mathbf J\cdot\mathbf E\rangle\,dV', 'pink'),
        ('03', '计算与验证', '按过程选模型，按误差选精度', '/chapters/simulation/', r'\partial_t f+\dot{\mathbf z}\cdot\nabla_{\mathbf z}f=C[f]+S', 'blue'),
        ('04', '输运与边界', '通量、约束与排热的共同账本（w 为能量密度）', '/sections/transport-boundary/', r'\partial_t w+\nabla\cdot\mathbf Q=S', 'green'),
        ('05', '工程与材料', '从核热源到部件温度与应力', '/sections/engineering/', r'\rho c_p\partial_tT=\nabla\cdot(k\nabla T)+Q', 'gold'),
        ('06', '诊断与实验', '把观测变成可检验的证据', '/sections/diagnostics/', r'\mathbf y=\mathcal H[\mathbf x]+\boldsymbol\epsilon', 'violet'),
    ]
    cards = ''.join(fr'''<a class="discovery-card {color}" href="{url}"><span class="route-number">{number} / EXPLORE</span><h3>{title}<span aria-hidden="true">↗</span></h3><p>{description}</p><div class="route-equation arithmatex">\({equation}\)</div></a>'''
                    for number, title, description, url, equation, color in routes)
    stats = ''.join(f'<div><strong>{count}</strong><span>{label}</span></div>' for count, label in
                    [(len(chapters), '知识章节'), (len(sections), '阅读专题'), (len(entries), '永久条目'), (len(references), '参考来源')])
    return f'''<section class="fusion-hero" aria-labelledby="hero-title">
<div class="hero-copy"><p class="orbit-kicker"><span></span> FUSION STACKS / 曦融兆波</p>
<h1 id="hero-title">从一个粒子，<br>到一座<span>聚变电站。</span></h1>
<p class="hero-description">沿着方程、图解与计算，读懂聚变科学与工程。</p>
<div class="fusion-actions"><a class="button primary" href="/sections/foundations/">开始探索 <span>↗</span></a><a class="button" href="/knowledge-tree/">打开三维知识树 <span>◎</span></a></div>
<div class="reaction-line" aria-label="氘氚聚变反应：产生氦四和中子，释放约17.6兆电子伏特"><span>²H + ³H</span><b>→</b><span>⁴He + n</span><small>17.6 MeV</small></div>
</div>
<div class="plasma-scene"><div class="scene-top"><span>MAGNETIC CONFINEMENT</span><button id="plasma-motion" type="button" hidden>暂停动画</button></div>
<div class="plasma-art"><svg class="plasma-fallback" viewBox="0 0 600 420" role="img" aria-label="环形等离子体与螺旋磁力线示意"><defs><radialGradient id="torus-glow"><stop stop-color="#f590d4" stop-opacity=".2"/><stop offset="1" stop-color="#091622" stop-opacity="0"/></radialGradient></defs><ellipse cx="300" cy="220" rx="275" ry="185" fill="url(#torus-glow)"/><g fill="none" stroke="#57e3ec" opacity=".5"><ellipse cx="300" cy="220" rx="220" ry="105"/><ellipse cx="300" cy="220" rx="150" ry="65"/><ellipse cx="300" cy="185" rx="185" ry="85"/><ellipse cx="300" cy="255" rx="185" ry="85"/></g><ellipse cx="300" cy="220" rx="185" ry="85" fill="none" stroke="#ff80c6" stroke-width="8" opacity=".7"/></svg><canvas id="plasma-canvas" aria-hidden="true"></canvas><div class="scene-label label-field">B<sub>φ</sub> + B<sub>θ</sub><small>螺旋磁力线</small></div><div class="scene-label label-core">PLASMA<small>环形约束区域</small></div></div>
<div class="scene-bottom"><span><i></i> 磁约束几何示意 · 不按比例</span><span>FIELD / PARTICLE / ENERGY</span></div></div>
</section>
<section class="home-metrics" aria-label="知识库规模">{stats}</section>
<section class="discovery" aria-labelledby="discovery-title"><div class="discovery-heading"><div><p class="orbit-kicker">FOLLOW THE PHYSICS</p><h2 id="discovery-title">选择一个问题，进入它的方程。</h2></div><a href="/contents/">完整目录 ↗</a></div><div class="discovery-grid">{cards}</div></section>
<div class="evidence-strip"><span class="evidence-dot"></span><p>原理 → 模型 → 计算 → 观测</p><a href="/verification/">资料与算例核验记录 ↗</a></div>'''
