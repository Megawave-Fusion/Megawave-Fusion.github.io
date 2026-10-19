"""Independent cross-review numerics; stdlib only, no author-test imports.

The inputs are the explicitly hypothetical teaching examples in the 39 tags.
Checks use quadrature, finite differences, RK4, and direct least squares.
Source-location and evidence-classification reviews are recorded separately.
"""
import argparse
import cmath
import json
import math
from pathlib import Path

checks = []


def check(tag, name, actual, expected, rtol=1e-8, atol=1e-10):
    passed = abs(actual - expected) <= atol + rtol * abs(expected)
    checks.append(dict(tag=f'MF{tag:06d}', check=name, actual=actual,
                       expected=expected, rtol=rtol, atol=atol, passed=passed))
    assert passed, checks[-1]


def quad(f, a, b, n=4096):
    h = (b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if j % 2 else 2)*f(a+j*h)
                              for j in range(1, n)))


def rk4(f, y, duration, n=4096):
    y = tuple(y)
    h = duration/n
    for j in range(n):
        t = j*h
        k1 = f(t, y)
        k2 = f(t+h/2, tuple(v+h*k/2 for v, k in zip(y, k1)))
        k3 = f(t+h/2, tuple(v+h*k/2 for v, k in zip(y, k2)))
        k4 = f(t+h, tuple(v+h*k for v, k in zip(y, k3)))
        y = tuple(v+h*(a+2*b+2*c+d)/6
                  for v, a, b, c, d in zip(y, k1, k2, k3, k4))
    return y


def run():
    checks.clear()
    pi, exp, sqrt = math.pi, math.exp, math.sqrt
    mu0, e, kb = 4*pi*1e-7, 1.602176634e-19, 1.380649e-23
    me, md, re = 9.1093837139e-31, 3.3435837768e-27, 2.8179403205e-15
    # Integrated current, numerical Ampere field, and rational surface.
    a, R, B, I = .6, 2.5, 3, 1e6
    j0 = 2*I/(pi*a*a)
    enclosed = lambda r: quad(lambda s: 2*pi*s*j0*(1-(s/a)**2), 0, r)
    check(8, 'current area integral / A', enclosed(a), I)
    r = a*sqrt(.92)
    check(8, 'q=2 surface from current integral', r*B/(R*mu0*enclosed(r)/(2*pi*r)), 2)
    check(8, 'central q limit', 2*B/(mu0*R*j0), 1.08)
    p = .8**2/(2*mu0)
    check(9, 'magnetic pressure / Pa', p, 254647.90894703253)
    check(9, 'sum of species thermal energies / keV', p/1e20/e/1000, 15.9, 5e-4)
    # Mirror trajectory integrated over a complete bounce.
    v = sqrt(2*20e3*e/md); w = v*math.sin(pi/4)/2
    T = 2*pi/w
    z, vz = rk4(lambda t,y: (y[1],-w*w*y[0]), (0,v/math.sqrt(2)), T)
    check(10, 'full bounce returns to midplane / m', z, 0, atol=1e-10)
    check(10, 'bounce period / microsecond', T*1e6, 12.836472, 1e-4)
    check(10, 'turning point / m', v/math.sqrt(2)/w, 2)
    points = [round((360*k*2/5)%360) for k in range(5)]
    check(11, 'five distinct Poincare intersections', len(set(points)), 5)
    check(11, '100-turn phase drift / degree', 100*360*(.401-.4), 36)
    # Work integral verifies adiabatic compression energy change (N=T0=V0=1).
    Uwork = 1.5 + quad(lambda x: exp(-2*x/3), math.log(1/125), 0)
    check(12, 'compression work gives T ratio 25', Uwork/1.5, 25)
    check(12, 'isotropic frozen flux B ratio', 5**2, 25)
    check(12, 'rho/R ratio preserved', (sqrt(25)/25)/(1/5), 1)
    def trap(t, p):
        return sum((t[i+1]-t[i])*(p[i+1]+p[i])/2 for i in range(len(t)-1))
    E = trap([0,.5,1,1.5,2], [0,4,6,4,0])
    check(13, 'piecewise pulse energy / MJ', E, 7)
    check(13, 'integrated energy gain', E/(10*2), .35)
    check(14, 'iota=5/6 closure after six toroidal turns / poloidal turns', 6*5/6, 5)
    check(14, 'number of distinct intersections', len({(5*k)%6 for k in range(6)}), 6)
    # Compatibility and force balance for constrained thermal expansion.
    eps_th = 12e-6*150; stress = -180e9*eps_th/2
    check(52, 'equal spring/bar stiffness stress / MPa', stress/1e6, -162)
    check(52, 'strain compatibility residual', stress/180e9 + stress/180e9 + eps_th, 0)
    q0, ell, d, k = 2e6, .05, .1, 20
    flux = quad(lambda x:q0*exp(-x/ell),0,d)
    dT = quad(lambda x:q0*ell*(1-exp(-x/ell))/k,0,d)
    check(53, 'nuclear heat integrated to surface flux / W m-2', flux, 86466.47167633873)
    check(53, 'integrated Fourier temperature rise / K', dT, 283.8338208091532)
    # Half-space heat equation: derivative residual, boundary flux, energy integral.
    F = lambda z: exp(-z*z)/sqrt(pi)-z*math.erfc(z)
    h = 1e-4
    for z in [.1,.7,2]:
        Fp = (F(z+h)-F(z-h))/(2*h)
        Fpp = (F(z+h)-2*F(z)+F(z-h))/h**2
        check(54, f'heat similarity ODE at xi={z}', Fpp+2*z*Fp-2*F(z), 0, atol=4e-8)
    alpha, q, k, t = 4e-5, 5e6, 100, .01
    check(54, 'surface temperature rise / K', 2*q*sqrt(alpha*t)*F(0)/k, 35.682482323055424)
    energy = quad(lambda z: 2.5e6*2*q*sqrt(alpha*t)*F(z)/k*2*sqrt(alpha*t),0,9)
    check(54, 'half-space stored heat equals q t / J m-2', energy,q*t)
    check(54, 'boundary slope -1', (F(h)-F(-h))/(2*h),-1)
    fluence = [1e24,2e24]
    dpa = sum(p*s*1e-28 for p,s in zip(fluence,[1000,2000]))
    he = sum(p*s*1e-28 for p,s in zip(fluence,[.01,.05]))*1e6
    check(55, 'two-group dpa', dpa,.5)
    check(55, 'two-group helium / appm', he,11)
    check(55, 'He/dpa ratio / appm per dpa',he/dpa,22)
    # Diffusion inventory from erfc spatial quadrature and surface-flux time integral.
    cs, D, t = 1e24,1e-12,1e4
    inventory = 2*cs*sqrt(D*t)*quad(math.erfc,0,9)
    check(56, 'diffused inventory / m-2',inventory,1.1283791670955126e20)
    # t=s^2 removes the integrable t^-1/2 singularity.
    inflow = quad(lambda s:2*cs*sqrt(D/pi),0,sqrt(t))
    check(56, 'integrated boundary influx equals inventory',inflow/inventory,1)
    for z in [.1,.7,2]:
        fp=(math.erfc(z+h)-math.erfc(z-h))/(2*h)
        fpp=(math.erfc(z+h)-2*math.erfc(z)+math.erfc(z-h))/h**2
        check(56,f'diffusion similarity ODE at xi={z}',fpp+2*z*fp,0,atol=4e-8)
    E1,E2,al1,al2,dt=200e9,100e9,5e-6,15e-6,200
    eps=(E1*al1+E2*al2)*dt/(E1+E2)
    s1,s2=E1*(eps-al1*dt),E2*(eps-al2*dt)
    check(57,'internal force balance / Pa',s1+s2,0,atol=1e-6)
    check(57,'first rod tensile stress / MPa',s1/1e6,133.33333333333333)
    check(58,'interpolated conductivity / W m-1 K-1',120+(500-400)*(100-120)/(600-400),110)
    check(58,'constant-k slab rise / K',5e6*.003/110,136.36363636363637)
    # Circuit ODE and independent Joule integral.
    If, = rk4(lambda t,y:(-.2*y[0]/2,), (1e4,),10)
    check(67,'circuit RK4 current at L/R / A',If,1e4/ math.e)
    heat=quad(lambda t:.2*(1e4*exp(-t/10))**2,0,10)
    check(67,'stored energy plus Joule heat / J',If**2+heat,1e8)
    tau=-10/math.log((.03742-.001)/(.1-.001))
    check(68,'inverse pumpdown time constant / s',tau,10,rtol=2e-4)
    check(68,'pumpdown target crossing / s',10*math.log(11),23.978952727983707)
    check(68,'series flow conductance / m3 s-1',1/(1/.2-1/.5),1/3)
    # Entropy equality independently fixes hot-side heat and electric work.
    pc=100/4.5*300-100 + 1000/80*300-1000
    check(69,'two-stage reversible refrigerator work / W',pc,9316.666666666668)
    check(69,'100W interception at 80K / W',100*(300/80-1),275)
    inj=.1/.02;recovered=(inj-.1)*.999;fresh=inj-recovered
    check(70,'fresh tritium supply / mg s-1',fresh,.1049)
    check(70,'stage inventory / mg',inj*30,150)
    check(70,'burn+processing loss=fresh',.1+(inj-.1)*(1-.999),fresh)
    avg=(120*250-30*20)/150
    check(71,'on/off net average / MW',avg,196)
    check(71,'annual exported energy / MWh',avg*8760,1716960)
    check(71,'reduced downtime annual change / MWh',((120*250-15*20)/135-avg)*8760,210240)
    check(72,'mbar L/s to molecules/s at 300K',100*1e-3/(kb*300),2.4143235053466403e19)
    # Direct geometric line integration, not Abel closed form.
    a,n0,lam=.5,8e19,10.6e-6
    cols=[]
    for b in [0,.3]:
        length=sqrt(a*a-b*b)
        col=quad(lambda x:n0*(1-(x*x+b*b)/a**2),-length,length)
        cols.append(col)
    check(59,'central line density / m-2',cols[0],5.333333333333333e19)
    check(59,'off-axis/central column ratio',cols[1]/cols[0],.512)
    check(59,'central plasma-minus-vacuum phase / rad',-re*lam*cols[0],-1.593,rtol=1e-4)
    check(60,'correlated temperature difference uncertainty / K',sqrt(2*(.2**2+.5**2)-2*.5**2),sqrt(.08))
    check(60,'independent calibration uncertainty / K',sqrt(2*(.2**2+.5**2)),.7615773105863909)
    w=sqrt(15)/.02
    for delay,expected in [(.002,82.287),(.008,15.715)]:
        L=4*cmath.exp(-1j*w*delay)/(1+1j*w*.02)
        check(61,f'loop magnitude at crossing, delay={delay}',abs(L),1)
        check(61,f'phase margin / degree, delay={delay}',180+cmath.phase(L)*180/pi,expected,rtol=1e-3)
    check(62,'phase-inverted average density / m-3',.9/(re*lam*.75),4.017387619964558e19,rtol=1e-5)
    check(62,'phase error propagated to density / m-3',.02/(re*lam*.75),8.927528044365685e17,rtol=1e-5)
    u=[0,1,2,1];flux=u[:];v=[u[i]-.5*(flux[i]-flux[i-1]) for i in range(4)]
    check(63,'finite-volume periodic total',sum(v)*.1,sum(u)*.1)
    check(63,'positive step minimum',min(v),.5)
    check(63,'over-CFL negative cell',u[1]-1.2*(u[1]-u[0]),-.2)
    def energy(tauE):
        return rk4(lambda t,y:(-y[0]/.05,y[0]/.05-y[1]/tauE,y[1]/tauE),(1,0,0),.1)
    wf,wt,loss=energy(.2)
    check(64,'RK4 fast energy / MJ',wf,.1353352832366127)
    check(64,'RK4 thermal energy / MJ',wt,.6282605019675947)
    check(64,'all reservoirs close / MJ',wf+wt+loss,1)
    wf,wt,loss=energy(.05)
    check(64,'equal-time-constant limit / MJ',wt,2*exp(-2))
    check(64,'equal-time-constant energy conservation / MJ',wf+wt+loss,1)
    d2=lambda h: (math.sin(pi*(.5+h))-2*math.sin(pi*.5)+math.sin(pi*(.5-h)))/h**2
    errors=[abs(d2(h)+pi*pi) for h in [.05,.025]]
    check(65,'manufactured source at center',.1*pi*pi-1,-.0130395598910642)
    check(65,'coarse spatial error',errors[0],.02027687719948368)
    check(65,'spatial observed order',math.log(errors[0]/errors[1],2),2,rtol=.001)
    ew=1e6
    for i in range(100):ew*=.99
    check(66,'iterated Euler endpoint / J',ew,366032.3412732292)
    check(66,'Euler relative error / percent',(1-ew/(1e6/math.e))*100,.502,rtol=2e-4)
    # Factorial coefficients from orthogonal projection.
    design=[(1,-1,-1,1),(1,1,-1,-1),(1,-1,1,-1),(1,1,1,1)]
    yy=[10,14,12,20]
    coeff=[sum(r[j]*y for r,y in zip(design,yy))/4 for j in range(4)]
    for j,x in enumerate([14,3,2,1]): check(73,f'factorial coefficient {j} / kW',coeff[j],x)
    check(74,'deposited pulse energy / MJ',trap([0,.1,.2,.3,.4],[0,2,4,2,0]),.8)
    check(74,'final thermal inventory / MJ',1+.8-.4,1.4)
    # Solve normal equations directly, avoiding copying coefficient shortcut.
    xx=[0,1,2,3,4];yy=[.10,2.12,4.08,6.10,8.10]
    n=len(xx); sx=sum(xx);sxx=sum(x*x for x in xx);sy=sum(yy);sxy=sum(x*y for x,y in zip(xx,yy))
    det=n*sxx-sx*sx
    a=(sy*sxx-sxy*sx)/det;b=(n*sxy-sx*sy)/det
    rss=sum((y-a-b*x)**2 for x,y in zip(xx,yy))
    check(75,'normal-equation offset',a,.104)
    check(75,'normal-equation slope',b,1.998)
    check(75,'residual sum of squares',rss,.00076)
    check(75,'inverse calibration', (5.1-a)/b,2.5005005005005003)
    check(75,'residual standard deviation',sqrt(rss/3),.01591644851508443)
    sensor,=rk4(lambda t,y:((60-y[0])/.2,),(40,),.05)
    check(76,'sensor reading at global t=.1s / C',sensor,44.4239843385719)
    check(76,'threshold timestamp / s',.05+.2*math.log(2),.18862943611198907)
    check(77,'example A Q',200/20,10)
    check(77,'example B Q',100/20,5)
    check(77,'example A net electric / MW',.4*200-20/.5-30,10)
    check(77,'example B net electric / MW',.4*100-20/.5-30,-30)
    check(78,'pulse A average / MW',2*.1/10,.02)
    check(78,'pulse B average / MW',1*60/120,.5)
    check(78,'pulse energy ratio B/A',60/.2,300)
    phase=-re*10.6e-6*3e19*.6
    check(80,'learning-chain phase / rad',phase,-.538,rtol=.001)
    check(80,'phase relative uncertainty / percent',.01/abs(phase)*100,1.86,rtol=.001)
    errs=[abs(2*(math.cos(h)-1)/h**2+1) for h in [.2,.1]]
    check(81,'sin second-derivative coarse error',errs[0],.0033288920620812)
    check(81,'sin second-derivative fine error',errs[1],.0008330556051643341)
    sigma=sqrt(100*e/me);vth=sqrt(2)*sigma
    check(82,'Gaussian normalization',quad(lambda z:exp(-z*z/2)/sqrt(2*pi),-9,9),1)
    check(82,'Gaussian variance',quad(lambda z:z*z*exp(-z*z/2)/sqrt(2*pi),-9,9),1)
    check(82,'thermal scale / m s-1',vth,5.930969580203117e6)
    # 79 and 83 are document-method tags: review uses source definitions and identity,
    # not invented physics equations. They are included in cross-tags.json.
    return checks


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--report',type=Path)
    args=parser.parse_args()
    result=run()
    report={'checks':result,'passed':sum(x['passed'] for x in result),
            'total':len(result),'numerical_tag_count':len({x['tag'] for x in result}),
            'source_only_tags':['MF000079','MF000083']}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False))
