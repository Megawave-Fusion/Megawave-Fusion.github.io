#!/usr/bin/env python3
"""Reproduce the foundations Tag examples and independently check their balances."""
import cmath
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
e=1.602176634e-19
me=9.1093837139e-31
md=3.3435837768e-27
mu0=1.25663706127e-6
eps0=8.8541878188e-12
c=299792458.0
checks=[]
def check(tag,name,actual,expected,rtol=1e-7,atol=1e-10):
    ok=math.isclose(actual,expected,rel_tol=rtol,abs_tol=atol)
    row=dict(tag=tag,name=name,actual=actual,expected=expected,rtol=rtol,atol=atol,passed=ok)
    checks.append(row)
    if not ok:raise AssertionError(row)
def integral(f,a,b,n=12000):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*h) for j in range(1,n)))
def rk4(f,y,t0,t1,n=10000):
    h=(t1-t0)/n;t=t0
    for _ in range(n):
        a=f(t,y);b=f(t+h/2,y+h*a/2);d=f(t+h/2,y+h*b/2);g=f(t+h,y+h*d)
        y+=h*(a+2*b+2*d+g)/6;t+=h
    return y

check('MF000001','pulse fusion energy [MJ]',(5e19)**2*1e-22*10*2*17.6e6*e/1e6,14.0991543792)
tau=.30/math.log(12/8)
check('MF000002','decay ODE endpoint [MJ]',rk4(lambda t,w:-w/tau,12,0,.3),8)
check('MF000002','driven storage at one tau',rk4(lambda t,w:10-w/tau,0,0,tau),10*tau*(1-math.exp(-1)))
B0=math.sqrt(4-2*mu0*2e5)
check('MF000003','slab total pressure [Pa]',2e5+B0*B0/(2*mu0),4/(2*mu0))
# Numerical mean of real force times real velocity, independent of power formula.
for omega,expected in [(1,2.5),(.8,0.41237113402061887)]:
    X=1/(1-omega*omega-2j*.1*omega)
    power=integral(lambda t:math.cos(omega*t)*((-1j*omega*X)*cmath.exp(-1j*omega*t)).real,0,2*math.pi/omega)/(2*math.pi/omega)
    check('MF000004',f'cycle averaged work omega={omega}',power,expected)
    diss=integral(lambda t:.2*(((-1j*omega*X)*cmath.exp(-1j*omega*t)).real)**2,0,2*math.pi/omega)/(2*math.pi/omega)
    check('MF000004',f'work equals dissipation omega={omega}',power,diss)
check('MF000005','exponential footprint integral [W]',8*integral(lambda s:20e6*math.exp(-s/.03),0,1.5),4.8e6)
check('MF000006','volume Joule heating vs VI',1e-7*(.5e6/.5)**2*.5*10,1*.5e6)
check('MF000006','fixed current heating after fourfold Te [MW]',.5/8,.0625)
check('MF000006','fixed voltage heating after fourfold Te [MW]',1/(2e-6/8)/1e6,4)
check('MF000007','sum species storage [MJ]',1.5*(8e19+4e19+4e19)*12e3*e*30/1e6,13.84280611776)
check('MF000145','tritium consumption [g/day]',100e6/(17.6e6*e)*5.008e-27*86400*1000,15.34457983658703)
# Gaussian convolution variance from independent double quadrature (dimensionless).
va,vb=5,20/3
norm=lambda x,v:math.exp(-x*x/(2*v))/math.sqrt(2*math.pi*v)
varsum=integral(lambda x:x*x*norm(x,va),-12*math.sqrt(va),12*math.sqrt(va))+integral(lambda x:x*x*norm(x,vb),-12*math.sqrt(vb),12*math.sqrt(vb))
check('MF000146','relative temperature from Gaussian second moments [keV]',1.2*varsum,14)
check('MF000146','arithmetic-temperature rate error',math.sqrt(15/14)-1,.0350983390135313)
check('MF000147','density-temperature radial integral',integral(lambda r:2*r*(1-r*r)**4,0,1),.2)
check('MF000147','separate averaging ratio',(.5**2)*(.5**2)/.2,.3125)
Wf=rk4(lambda t,w:10-w/.2,0,0,.1)
heat=integral(lambda t:10*(1-math.exp(-t/.2)),0,.1)
check('MF000148','two-reservoir conservation [MJ]',Wf+heat,1)
check('MF000148','fast reservoir [MJ]',Wf,.7869386805747332)
Theta=15e3*e;react=2e-22;Q=10;eta=.8;B=1.69e-38*math.sqrt(15000)
nt=3*Theta/(react*(eta*3.5e6*e+17.6e6*e/Q)/4-B)
n=1e20;tr=3*n*Theta/(nt/n);rad=n*n*B;birth=n*n*react/4
check('MF000149','Lawson heat equals transport plus radiation [W/m3]',birth*(eta*3.5e6*e+17.6e6*e/Q),tr+rad)
check('MF000149','radiating n*tau',nt,2.092233005068707e20)
# Recover transfer amplitude and phase by integrating the time-domain ODE to periodic state.
w=2*math.pi;ts=.2
state=rk4(lambda t,y:(math.cos(w*t)-y)/ts,0,0,10)
exact=(cmath.exp(1j*w*10)/(1+1j*w*ts)).real
check('MF000150','slowing response ODE vs complex solution',state,exact,rtol=1e-6)
check('MF000150','slowing modulation amplitude',1/math.sqrt(1+(w*ts)**2),.6226769922994999)
fz=.01;Z=6;nf=1-Z*fz
check('MF000151','Zeff species sum',nf+Z*Z*fz,1.3)
check('MF000151','dilution and radiation [fraction]',nf**2,.8836)
a=.1;fstar=2*a/(4*a+1+math.sqrt(8*a+1))
fnum=rk4(lambda t,f:a*(1-2*f)**2-f,0,0,30)
check('MF000152','ash nonlinear ODE steady state',fnum,fstar)
check('MF000152','ash production balances exhaust',a*(1-2*fstar)**2,fstar)
pfus=500;pext=50
check('MF000153','electricity separate budget [MW]',.4*(1.1*pfus+.8*pext)-pext/.5-.1*pfus,86)
check('MF000153','zero-net Q', (1/.5-.4*.8)/(.4*1.1-.1),4.9411764705882355)
L=.2;half=.01;D=L*L*math.log(2)/(math.pi*math.pi*half)
check('MF000154','diffusion first-mode half decay',math.exp(-D*(math.pi/L)**2*half),.5)
# Finite differences check PDE without using a differentiated analytic expression.
profile=lambda x,t:math.sin(math.pi*x/L)*math.exp(-D*(math.pi/L)**2*t)
x,t=.071,.013;dx,dt=1e-5,1e-6
check('MF000154','diffusion PDE centered derivatives',(profile(x,t+dt)-profile(x,t-dt))/(2*dt),D*(profile(x+dx,t)-2*profile(x,t)+profile(x-dx,t))/(dx*dx),rtol=2e-7)
for nu,omega in [(.3,2),(2,2),(4,1)]:
    numeric=integral(lambda t:math.exp(-nu*t)*math.cos(omega*t),0,40/nu,n=120000)
    check('MF000155',f'Green-Kubo integral nu={nu},Omega={omega}',numeric,nu/(nu*nu+omega*omega))
check('MF000155','classical diffusivity [m2/s]',1e10*1e4/(1e8**2+1e4**2),.01,rtol=1e-7)
Er=(1e20-4e20)/(1e17+2e17)
check('MF000156','ambipolar charged flux',4e20+1e17*Er,1e20-2e17*Er)
check('MF000156','radial electric field [V/m]',Er,-1000)
j0=integral(lambda a:math.cos(math.cos(a)),0,2*math.pi)/(2*math.pi)
check('MF000157','gyroaverage J0 by angle quadrature',j0,.7651976865579666)
check('MF000157','Bessel fourth-order relative difference',(1-.25+1/64)/j0-1,.0005584,rtol=1e-4)
check('MF000158','pedestal dimensionless gradient',2*mu0*3*4**2*8e3/(2.5**2*.04),3.8603890522214406)
check('MF000158','ELM pulse versus mean [MW/m2]',20e3/(.0005*.2)*(.0005*50)/1e6,5)
check('MF000159','variable area quadrature',integral(lambda s:1/(1+3*s),0,1),math.log(4)/3)
check('MF000159','target surface heat flux [MW/m2]',100/4*math.sin(math.radians(2)),.8724874175625242)
for x in (.1,.001):
    exact=(1+2*x)**-.5-math.exp(-x)
    check('MF000160',f'Bohm expansion x={x}',exact/x**2,1,rtol=.21 if x==.1 else .003)
check('MF000160','Bohm exact density difference',(1.2)**-.5-math.exp(-.1),.008033511139317777)
# Recycled particles summed generation by generation, independent geometric series test.
check('MF000161','recycling generations [s^-1]',sum(1e21*.9**j for j in range(400)),1e22)
check('MF000161','ionization budget [kW]',9e21*30*e/1000,43.258769118)
check('MF000161','power-limited target flux [s^-1]',1e21+20e3/(30*e),5.161006049640508e21)
VA=5/math.sqrt(mu0*md*1e20)
check('MF000162','TAE frequency [kHz]',VA/(4*math.pi*2*3)/1e3,102.30523405038676)
# Explicit harmonic crossing with n=2, m=3: q=1.75.
n,m,R=2,3,3;q=(m+.5)/n
check('MF000162','adjacent harmonic crossing',(n-m/q)/R,-(n-(m+1)/q)/R)
Lp,I,tauI=5e-6,1e6,.01
check('MF000163','RL integrated heat equals initial magnetic energy',integral(lambda t:(Lp/tauI)*(I*math.exp(-t/tauI))**2,0,20*tauI),.5*Lp*I*I)
check('MF000163','initial induced field [V/m]',Lp*I/(2*math.pi*2*tauI),39.78873577297384)
Ec=1e20*e**3*15/(4*math.pi*eps0**2*me*c*c)
check('MF000163','critical field [V/m]',Ec,.07648648690047594)
check('MF000163','Dreicer field [V/m]',Ec*me*c*c/(10*e),3908.4514548241723)
out={'suite':'tag_depth_foundations','checks':checks,'count':len(checks),'tags':len(set(x['tag'] for x in checks)),'passed':all(x['passed'] for x in checks)}
p=ROOT/'.build/tag-depth/foundations-numerics.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'suite':out['suite'],'count':out['count'],'tags':out['tags'],'passed':out['passed']}))
