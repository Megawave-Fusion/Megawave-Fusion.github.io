#!/usr/bin/env python3
"""Independent foundations review: conservation, midpoint integration, and roots.

Authored by the heating reviewer. Does not import the author test or its outputs.
Values use SI unless a check name gives a scaled unit.
"""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.build/tag-depth'
E = 1.602176634e-19
ME = 9.1093837139e-31
MD = 3.3435837768e-27
MU0 = 1.25663706127e-6
EPS0 = 8.8541878188e-12
C = 299792458.0
PI = math.pi
checks = []

def ck(tag, name, actual, expected, rtol=2e-7, atol=1e-10):
    passed = math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol)
    row = dict(tag=f'MF{tag:06d}', name=name, actual=actual,
               expected=expected, rtol=rtol, atol=atol, passed=passed)
    checks.append(row)
    if not passed:
        raise AssertionError(row)

def midpoint(f, a, b, n=60000):
    h = (b-a)/n
    return h*math.fsum(f(a+(j+.5)*h) for j in range(n))

def bisect(f, lo, hi):
    flo = f(lo)
    assert flo*f(hi) <= 0
    for _ in range(90):
        m=(lo+hi)/2
        if flo*f(m) <= 0:
            hi=m
        else:
            lo=m; flo=f(m)
    return (lo+hi)/2

# Reaction-event and product-energy accounting.
events = 5e19*5e19*1e-22*10*2
ck(1, 'event-count pulse energy [MJ]', events*17.6e6*E/1e6, 14.0991543792)
ck(1, 'product power sum [MW]', (events/2)*(3.5+14.1)*E, 7.0495771896)
ck(1, 'alpha pulse energy [MJ]', events*3.5*E, 2.8038091095)

# Trapezoidal step solves the ODE directly; loss integral closes its budget.
tau=.3/math.log(1.5); h=.3/10000; w=12.; loss=0.
for _ in range(10000):
    wn=w*(1-h/(2*tau))/(1+h/(2*tau))
    loss += h*(w+wn)/(2*tau); w=wn
ck(2, 'implicit midpoint decay endpoint [MJ]', w, 8)
ck(2, 'stored plus lost energy [MJ]', w+loss, 12)
ck(2, 'steady heated energy [MJ]', 10*tau, 7.398910387129295)

# Reconstruct B from a parabolic pressure, then finite-difference Ampere/Lorentz.
pressure=lambda x:2e5*(1-x*x)
field=lambda x:math.sqrt(4-2*MU0*pressure(x))
x=.31; dx=1e-5
dp=(pressure(x+dx)-pressure(x-dx))/(2*dx)
jy=-(field(x+dx)-field(x-dx))/(2*dx*MU0)
ck(3, 'slab Lorentz force equals pressure gradient [N/m3]', jy*field(x), dp)
ck(3, 'on-axis field [T]', field(0), 1.8701, rtol=2e-5)

# Drive the actual two-dimensional oscillator to a periodic state.
for omega, pexpected in [(1.,2.5),(.8,.4123711340206186)]:
    ns=6000; h=2*PI/omega/ns; x=v=0.; work=diss=0.
    for j in range(35*ns):
        t=(j+.5)*h; force=math.cos(omega*t)
        vm=(v+.5*h*(force-x))/(1+.1*h+.25*h*h)
        x += h*vm; v=2*vm-v
        if j >= 34*ns:
            work += h*force*vm; diss += h*.2*vm*vm
    period=2*PI/omega
    ck(4, f'time-stepped mean work omega={omega}', work/period, pexpected, rtol=3e-6)
    ck(4, f'period work-dissipation equality omega={omega}', work, diss, rtol=2e-6)

foot=midpoint(lambda x:8*20e6*math.exp(-x/.03),0,1.2)
ck(5, 'target footprint recovers allocated power [MW]', foot/1e6, 4.8)
ck(5, 'doubled width unchanged total [MW]', midpoint(lambda x:8*10e6*math.exp(-x/.06),0,2.4)/1e6,4.8)
eta=1e-7; length=10; area=.5; current=.5e6
ck(6, 'volume heating equals voltage-current power [W]', eta*(current/area)**2*(length*area), current**2*eta*length/area)
ck(6, 'fourfold Te fixed-I response [MW]', current**2*(eta/8)*length/area/1e6,.0625)
ck(6, 'fourfold Te fixed-V response [MW]', 1/(eta*length/area/8)/1e6,4)

# Maxwellian kinetic-energy moment rather than substituting 3/2 directly.
g=lambda u:math.exp(-u*u/2)/math.sqrt(2*PI)
second=midpoint(lambda u:u*u*g(u),-10,10)
ck(7, 'one-dimensional Maxwell moment', second, 1)
thermal=.5*3*second*(8e19+4e19+4e19)*12e3*E*30
ck(7, 'species kinetic-energy integral [MJ]', thermal/1e6,13.84280611776)

nt=100e6*86400/(17.6e6*E)
ck(145, 'daily tritium burn [g]', nt*5.008e-27*1000,15.344579836587029)
ck(145, 'inverse-mass two-body product energy sum [MeV]',17.6/5+17.6*4/5,17.6)
ck(145, 'one-percent burn circulation [g/day]',nt*5.008e-27*1000/.01,1534.457983658703)

# Direct convolution at two relative velocities; no variance-sum substitution.
va=10/2; vb=20/3; mu=1.2
gauss=lambda u,var:math.exp(-u*u/(2*var))/math.sqrt(2*PI*var)
g0=midpoint(lambda u:gauss(u,va)*gauss(u,vb),-35,35)
g2=midpoint(lambda u:gauss(u,va)*gauss(u-2,vb),-35,35)
variance=-2/math.log(g2/g0)
ck(146, 'relative Gaussian temperature from convolution [keV]',mu*variance,14)
mean_speed=midpoint(lambda u:4*PI*u**3*(2*PI*variance)**-1.5*math.exp(-u*u/(2*variance)),0,40)
ck(146, 'constant-cross-section relative-speed moment',mean_speed,math.sqrt(8*variance/PI))
ck(146, 'arithmetic-temperature rate excess [%]',100*(math.sqrt(15/14)-1),3.50983390135313)

integral=midpoint(lambda r:2*r*(1-r*r)**4,0,1)
navg=midpoint(lambda r:2*r*(1-r*r),0,1)
ck(147, 'radial density-temperature covariance factor', integral,.2)
ck(147, 'averaged-input to integrated-rate ratio',navg**4/integral,.3125)
ck(147, 'five-percent helium dilution factor',(.5*(1-.1))**2/.25,.81)

# Two-energy-reservoir midpoint scheme keeps every transfer paired.
wf=wt=0.; dt=.1/10000
for _ in range(10000):
    wn=(wf+dt*(10-wf/(2*.2)))/(1+dt/(2*.2))
    wt += dt*(wf+wn)/(2*.2); wf=wn
ck(148, 'two-reservoir input budget [MJ]',wf+wt,1)
ck(148, 'thermalized energy [MJ]',wt,.2130613194252668)
ck(148, 'instantaneous thermal input [MW]',wf/.2,3.934693402873666)

# Root of the physical power ledger, with radiation explicit in the loss term.
n=1e20; theta=15e3*E; events=n*n*2e-22/4
heat=events*(.8*3.5e6+17.6e6/10)*E
rad=1.69e-38*n*n*math.sqrt(15000)
loss=lambda tau:3*n*theta/tau+rad
tau=bisect(lambda t:loss(t)-heat,.1,10)
ck(149, 'radiating Lawson root n*tau [s/m3]',n*tau,2.092233005068707e20)
ck(149, 'radiation counted exactly once [W/m3]',loss(tau),heat)
total_tau=3*n*theta/heat
ck(149, 'total-loss confinement n*tau [s/m3]',n*total_tau,1.9736842105263158e20)

# Fourier transform of the causal slowing kernel, independent of ODE stepping.
kernel=lambda t:math.exp(-t/.2)/.2
re=midpoint(lambda t:kernel(t)*math.cos(2*PI*t),0,10)
im=-midpoint(lambda t:kernel(t)*math.sin(2*PI*t),0,10)
ck(150,'slowing-kernel modulation amplitude',math.hypot(re,im),.6226769922994999,rtol=1e-6)
ck(150,'slowing-kernel phase [deg]',math.degrees(math.atan2(im,re)),-51.48811274603342,rtol=1e-6)
ck(150,'alpha heating at Q=10 (one-fifth convention)',(10/5)/(1+10/5),2/3)

species=[(.47,1),(.47,1),(.01,6)]
charge=sum(n*z for n,z in species); charge2=sum(n*z*z for n,z in species)
ck(151,'species quasineutral charge',charge,1)
ck(151,'effective charge from all species',charge2/charge,1.3)
ck(151,'fuel reaction-rate dilution',(.47*.47)/.25,.8836)
ck(151,'carbon bremsstrahlung [kW/m3]',1.69e-38*charge2*1e40*100/1e3,21.97)

# Locate the steady ash root and linearize numerically, independent quadratic solution.
rhs=lambda f:.1*(1-2*f)**2-f
fs=bisect(rhs,0,.5); dh=1e-5
ck(152,'steady ash root',fs,.07294901687515773)
ck(152,'ash equilibrium residual',rhs(fs),0)
growth=(rhs(fs+dh)-rhs(fs-dh))/(2*dh)
ck(152,'linear ash restoring rate [normalized]',growth,-math.sqrt(1.8))
ck(152,'ash-limited reaction fraction',(1-2*fs)**2,.7294901687515773)

ledger=lambda q:.4*(1.1*500+.8*500/q)-(500/q)/.5-.1*500
ck(153,'plant electric net power [MW]',ledger(10),86)
ck(153,'electric breakeven root Q',bisect(ledger,1,100),4.9411764705882355)

# Evolve the centered spatial Laplacian with an exact discrete-mode multiplier;
# then refine its eigenvalue to the continuum prediction.
D=.2**2*math.log(2)/(PI*PI*.01)
for cells in [200,400]:
    dx=.2/cells; lam=-4*D*math.sin(PI/(2*cells))**2/dx**2
    ck(154,f'discrete diffusion half-time cells={cells}',math.exp(lam*.01),.5,rtol=2e-5)
ck(154,'diffusion coefficient from half-time [m2/s]',D,.28092197109073153)

# Oscillatory correlation integral: time scaled by Omega, finite decay tail 30.
nu,om=.3,2.
cross=midpoint(lambda t:math.exp(-nu*t)*math.cos(om*t),0,30/nu,n=200000)
ck(155,'Green-Kubo signed correlation area',cross,nu/(nu*nu+om*om),rtol=2e-6)
ck(155,'strong-field diffusivity [m2/s]',1e10*1e4/(1e16+1e8),.01,rtol=2e-8)
ck(155,'banana scaling ratio at q=2,eps=.1',2**2/.1**1.5,126.49110640673516)

ion=lambda er:4e20+1e17*er; electron=lambda er:1e20-2e17*er
er=bisect(lambda er:ion(er)-electron(er),-10000,10000)
ck(156,'ambipolar field from flux root [V/m]',er,-1000)
ck(156,'ambipolar flux [m^-2 s^-1]',ion(er),3e20)

# Entire Bessel power series and direct flux phase multiplication.
j0=math.fsum((-1)**j/(4**j*math.factorial(j)**2) for j in range(18))
ck(157,'J0 from converged series',j0,.7651976865579666)
ck(157,'fourth-order gyroaverage excess [%]',100*((1-.25+1/64)/j0-1),.05584353553860222)
delta=.4
flux=midpoint(lambda y:math.cos(y)*math.sin(y+delta),0,2*PI)/(2*PI)
ck(157,'ExB density-phase flux sign',flux,.5*math.sin(delta))

alpha=2*MU0*3*16*8000/(6.25*.04)
ck(158,'normalized pedestal pressure gradient',alpha,3.8603890522214406)
period=.02; duration=.0005; area=.2; energy=20000
ck(158,'ELM peak heat flux [MW/m2]',energy/(duration*area)/1e6,200)
ck(158,'ELM average heat flux [MW/m2]',(energy/area)/period/1e6,5)

# Integrate parallel heat conduction in temperature to test the exponent 7/2.
thetalo=.5; thetahi=2.
ck(159,'conductive temperature integral',midpoint(lambda t:t**2.5,thetalo,thetahi),2/7*(thetahi**3.5-thetalo**3.5))
ck(159,'variable-area thermal resistance factor',midpoint(lambda s:1/(1+3*s),0,1),math.log(4)/3)
ck(159,'target normal heat flux [MW/m2]',25*math.sin(2*PI/180),.8724874175625242)

# Reconstruct densities from ion energy+continuity and electron Boltzmann response.
x=.1; u=math.sqrt(1+2*x); ni=1/u; ne=math.exp(-x)
ck(160,'sheath positive space charge at M=1',ni-ne,.008033511139317384)
ck(160,'ion flux conservation',ni*u,1)
for mach in [.8,1,1.2]:
    sagdeev=midpoint(lambda z:1/math.sqrt(1+2*z/mach**2)-math.exp(-z),0,.001,n=10000)
    ck(160,f'Bohm-entry sign M={mach}',float(sagdeev>=0),float(mach>=1))
floating=5*math.log(MD/(2*PI*ME))
ck(160,'deuterium floating drop at Te=10eV [V]',floating,31.851575,rtol=3e-4)

# Recycle with explicit generation inventory; apply finite power as source cap.
generation=1e21; target=0
for _ in range(500):
    target+=generation; generation*=.9
ck(161,'recycled target sum [s^-1]',target,1e22)
ck(161,'ionization power [kW]',(target-1e21)*30*E/1e3,43.258769118)
ck(161,'power-limited total target [s^-1]',1e21+20000/(30*E),5.161006049640508e21)

va=5/math.sqrt(MU0*MD*1e20)
ck(162,'TAE frequency scale [kHz]',va/(2*2*3)/(2*PI)/1e3,102.30523405038676)
n,m,R=2,3,3
q=bisect(lambda q:(n-m/q)+(n-(m+1)/q),1.51,1.99)
ck(162,'adjacent-harmonic crossing q',q,1.75)
ck(162,'crossing wave number equals 1/(2qR)',abs((n-m/q)/R),1/(2*q*R))

# RL decay with midpoint update: heat equals magnetic-energy decrement each step.
L=5e-6; I=1e6; resistance=L/.01; dt=.2/100000; heat=0; wi=.5*L*I*I
for _ in range(100000):
    In=I*(1-dt*resistance/(2*L))/(1+dt*resistance/(2*L))
    heat+=dt*resistance*((I+In)/2)**2; I=In
ck(163,'RL magnetic plus heat budget [J]',heat+.5*L*I*I,wi)
ck(163,'initial toroidal induced field [V/m]',resistance*1e6/(4*PI),39.78873577297384)
ED=1e20*E**3*15/(4*PI*EPS0**2*10*E)
EC=ED*10*E/(ME*C*C)
ck(163,'Dreicer field from thermal force [V/m]',ED,3908.4514548241723)
ck(163,'relativistic critical field [V/m]',EC,.07648648690047594)

assert len({x['tag'] for x in checks}) == 26
result=dict(suite='tag_depth_foundations_independent',count=len(checks),tags=26,
            passed=all(x['passed'] for x in checks),checks=checks)
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'foundations-cross-numerics.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('suite','count','tags','passed')}))
