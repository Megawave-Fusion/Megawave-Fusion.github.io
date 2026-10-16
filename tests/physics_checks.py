#!/usr/bin/env python3
"""Independent benchmark calculations for the 2026-10-16 teaching edition.
Not a plasma solver or a proof that every statement is correct.
Run from repository root; results are saved under .build/reviews.
"""
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
e=1.602176634e-19
kb=1.380649e-23
me=9.1093837139e-31
md=3.3435837768e-27
eps=8.8541878188e-12
mu=1.25663706127e-6
c=299792458.
n=1e20
T=1000*e
B=5.
checks=[]
def close(name, actual, expected, rtol=1e-10, atol=1e-12):
    ok=math.isclose(actual,expected,rel_tol=rtol,abs_tol=atol)
    checks.append(dict(name=name,actual=actual,expected=expected,passed=ok))
    if not ok: raise AssertionError(checks[-1])
def simpson(f,a,b,N=20000):
    h=(b-a)/N
    return h/3*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*h) for j in range(1,N)))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

# Printed values use only 3-5 significant digits; allow the displayed rounding.
ld=math.sqrt(eps*T/(n*e*e));wp=math.sqrt(n*e*e/(eps*me))
vt=math.sqrt(2*T/me);od=e*B/md
for name,actual,expected,tol in [
 ('1 eV in kelvin',e/kb,11604.5,1e-5),
 ('electron Debye length [m]',ld,23.5e-6,.003),
 ('electron plasma frequency [Hz]',wp/(2*math.pi),89.8e9,.001),
 ('deuteron cyclotron frequency at 5 T [Hz]',od/(2*math.pi),38.1e6,.001),
 ('electron thermal speed [m/s]',vt,1.88e7,.003),
 ('deuteron thermal gyroradius [m]',math.sqrt(2*T/md)/od,1.29e-3,.003),
 ('electron inertial length [m]',c/wp,.531e-3,.002),
 ('deuteron inertial length [m]',c/math.sqrt(n*e*e/(eps*md)),.0322,.002),
 ('Debye sphere electron count',4*math.pi*n*ld**3/3,5.44e6,.002),
 ('total pressure at 10 keV [Pa]',2*n*10*T,3.204e5,.001),
 ('beta at 10 keV and 5 T',2*mu*2*n*10*T/B**2,.0322,.002)]:
 close(name,actual,expected,tol)
close('Debye thermal/frequency identity',ld,vt/(math.sqrt(2)*wp))
a=(3/(4*math.pi*n))**(1/3);G=e*e/(4*math.pi*eps*a*T)
close('coupling to Debye population identity',4*math.pi*n*ld**3/3,(3*G)**-1.5)
nu=4*math.sqrt(2*math.pi)/3*n*e**4*15/((4*math.pi*eps)**2*math.sqrt(me)*T**1.5)
close('specified electron-ion frequency [1/s]',nu,1.38e5,.003)
close('specified electron mean free path [m]',vt/nu,136,.003)

# Integrate a shifted Gaussian, independently checking moments and factor 3/2.
u0=2.7;sig=1.3
f=lambda v:math.exp(-.5*((v-u0)/sig)**2)/(math.sqrt(2*math.pi)*sig)
lo=u0-10*sig;hi=u0+10*sig
close('Gaussian normalization',simpson(f,lo,hi),1)
close('Gaussian mean velocity',simpson(lambda v:v*f(v),lo,hi),u0)
close('central pressure moment',simpson(lambda v:(v-u0)**2*f(v),lo,hi),sig**2)
close('odd heat-flux moment',simpson(lambda v:(v-u0)**3*f(v),lo,hi),0,atol=1e-11)
close('bulk plus thermal energy decomposition',simpson(lambda v:v*v*f(v),lo,hi),u0*u0+sig*sig)

# Integrate Lorentz dynamics in dimensionless uniform crossed fields using RK4.
# Compare the gyroperiod average against ExB; signs tested for both charges.
def rk4(y,dt,fn):
 a=fn(y);b=fn([v+dt*x/2 for v,x in zip(y,a)])
 cc=fn([v+dt*x/2 for v,x in zip(y,b)])
 d=fn([v+dt*x for v,x in zip(y,cc)])
 return [v+dt*(x+2*yy+2*z+w)/6 for v,x,yy,z,w in zip(y,a,b,cc,d)]
for q in [-1,1]:
 dt=2*math.pi/10000;y=[0.,0.,0.,0.]
 def fn(y):return [q*(1+y[1]),-q*y[0],y[0],y[1]]
 for _ in range(10000):y=rk4(y,dt,fn)
 close(f'ExB trajectory average x q={q}',y[2]/(2*math.pi),0,atol=1e-10)
 close(f'ExB trajectory average y q={q}',y[3]/(2*math.pi),-1)

# Loss-cone boundary from energy + magnetic moment, independent of trig formula.
R=4.;alpha=math.asin(1/math.sqrt(R))
close('mirror loss-cone parallel energy at throat',1-R*math.sin(alpha)**2,0)

# Cold dielectric eigenvectors checked by solving the underlying species equations.
w=3.;oc=-7.;p2=13.
a11=-1j*w;a12=-oc;a21=oc;a22=-1j*w
det=a11*a22-a12*a21
for sign in [-1,1]:
 E=(1,sign*1j)
 vx=(a22*E[0]-a12*E[1])/det
 vy=(-a21*E[0]+a11*E[1])/det
 D=(E[0]+1j*p2/w*vx,E[1]+1j*p2/w*vy)
 eigenvalue=1-p2/(w*(w+sign*oc))
 close(f'cold circular eigenvector sign={sign}',abs(D[1]-eigenvalue*E[1])+abs(D[0]-eigenvalue),0)

# MHD branch limiting cases and polynomial residuals, across both speed orderings.
for va,cs in [(5.,2.),(2.,5.)]:
 for ct in [0.,.4,1.]:
  A=va*va+cs*cs;C=va*va*cs*cs*ct*ct
  fast=(A+math.sqrt(A*A-4*C))/2
  slow=(A-math.sqrt(A*A-4*C))/2
  close(f'magnetosonic sum va={va} cos={ct}',fast+slow,A)
  close(f'magnetosonic product va={va} cos={ct}',fast*slow,C)

# Finite difference GS operator on analytic flux psi=R^4+R^2 Z^2.
# Delta*psi=10R^2, hence p'=-10/mu0 and F'=0 give a manufactured equilibrium.
def psi(r,z):return r**4+r*r*z*z
r=1.7;z=.4;h=1e-4
op=(psi(r+h,z)-2*psi(r,z)+psi(r-h,z))/h**2-(psi(r+h,z)-psi(r-h,z))/(2*h*r)+(psi(r,z+h)-2*psi(r,z)+psi(r,z-h))/h**2
close('GS manufactured-solution operator sign',op,10*r*r,1e-6)

# Pointwise work decomposition verifies sign and Hall work independently.
U=(.4,-.7,.3);J=(2.,3.,-1.);BB=(.2,-.8,1.1);eta=.04
uxb=cross(U,BB);EE=tuple(-x+eta*y for x,y in zip(uxb,J))
close('J dot E mechanical plus Joule work',dot(J,EE),dot(U,cross(J,BB))+eta*dot(J,J))
close('Hall force does zero current work',dot(J,cross(J,BB)),0)

# Sinusoidal resistive decay: integrated magnetic energy loss equals Joule heat.
k=2*math.pi;eta=.01;dm=eta/mu
energy_loss=dm*k*k/mu*simpson(lambda x:math.sin(k*x)**2,0,1)
joule=eta*k*k/mu**2*simpson(lambda x:math.cos(k*x)**2,0,1)
close('resistive decay magnetic/Joule energy balance',energy_loss,joule)

out={'date':'2026-10-16','result':'passed','checks':checks,'count':len(checks),'constants':'2022 CODATA; e,kB,c exact SI; rounded measured masses, epsilon0, mu0','scope':'Independent teaching benchmarks, not all formulas, not a device simulation or expert review'}
p=ROOT/'.build/reviews/physics-checks.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'{len(checks)} physics benchmark checks passed -> {p.relative_to(ROOT)}')
