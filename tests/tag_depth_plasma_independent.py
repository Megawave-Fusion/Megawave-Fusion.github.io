#!/usr/bin/env python3
"""Independent arithmetic, quadrature and differential checks of the 50 plasma Tags."""
from pathlib import Path
import cmath
import json
import math as m
ROOT=Path(__file__).resolve().parents[1]
e=1.602176634e-19; me=9.1093837139e-31; md=3.3435837768e-27
eps=8.8541878188e-12; kb=1.380649e-23; c=299792458.; hbar=1.054571817e-34
rows=[]
def check(tag,name,value,expected,rtol=3e-5,atol=1e-12):
    ok=m.isclose(value,expected,rel_tol=rtol,abs_tol=atol)
    rows.append(dict(tag=f'MF{tag:06}',name=name,actual=value,expected=expected,rtol=rtol,atol=atol,passed=ok))
def quad(f,a,b,n=12000):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+h*j) for j in range(1,n,2))+2*sum(f(a+h*j) for j in range(2,n,2)))
def normal(x,sigma=1,mu=0):
    return m.exp(-(x-mu)**2/(2*sigma*sigma))/(m.sqrt(2*m.pi)*sigma)
def orbit(dt,steps,y,fn):
    for i in range(steps):
        k1=fn(y); k2=fn([a+dt*b/2 for a,b in zip(y,k1)])
        k3=fn([a+dt*b/2 for a,b in zip(y,k2)]);k4=fn([a+dt*b for a,b in zip(y,k3)])
        y=[a+dt*(b+2*d+2*f+g)/6 for a,b,d,f,g in zip(y,k1,k2,k3,k4)]
    return y
# Gaussian moments and dimensional inputs.
check(84,'temperature Kelvin',250*e/kb,2.90113e6)
check(84,'flow speed m/s',m.sqrt(150*e/me),5.13637e6)
check(85,'parallel pressure from velocity quadrature',2e19*md*quad(lambda v:v*v*normal(v,m.sqrt(900*e/md)),-10*m.sqrt(900*e/md),10*m.sqrt(900*e/md)),2883.92)
k=2*m.pi/.02
check(86,'Poisson charge imbalance',eps*k*k*20/(e*1e19),1.09086e-5)
check(87,'screening cloud integrated shell charge',-quad(lambda x:x*m.exp(-x),1,3),-.536611)
lam=m.sqrt(eps*200*e/(1e19*e*e)); nd=4*m.pi*1e19*lam**3/3
check(88,'adiabatically compressed Debye particle number',nd*m.sqrt(8),4.35348e6)
check(89,'two-species oscillator frequency',m.sqrt(1e18*e*e/eps*(1/me+1/md)),5.64223e10)
check(89,'relative-coordinate energy J/m3',(1e18*e*1e-6)**2/(2*eps),1.44958e-3)
s=m.sqrt(20*e/me)
check(90,'one-sided flux by Gaussian quadrature',1e18*quad(lambda v:v*normal(v,s),0,12*s),7.48231e23)
nu=1e6; Om=e*.1/md
check(91,'transverse friction matrix solution',10*e/md*nu/(nu*nu+Om*Om),19.9981)
check(92,'integrated parallel electric work eV',quad(lambda t:50*(2e4+e*50/md*t),0,2e-6),2.23959)
Om=e*.8/md; t=m.pi/(2*Om)
y=orbit(t/2000,2000,[0.,0.,0.,2e5,0.,1e5],lambda y:[y[3],y[4],y[5],Om*y[4],-Om*y[3],0.])
for j,z in enumerate([.00521725,-.00521725,.00409762]):check(93,f'RK4 orbit coordinate {j}',y[j],z)
Om=e*.4/md; T=2*m.pi/Om
y=orbit(T/4000,4000,[0.,0.,0.,0.],lambda y:[y[2],y[3],e*2000/md+Om*y[3],-Om*y[2]])
check(94,'full Lorentz cycle mean drift',y[1]/T,-5000,rtol=1e-8)
vp=m.sqrt(1200*e/md);rho=vp/(e*.6/md)
F=quad(lambda t:e*.3*(rho*m.sin(t))*(-vp*m.sin(t)),0,2*m.pi)/(2*m.pi)
check(95,'gyroaveraged force and drift',-F/(e*.6),500)
check(96,'toroidal magnetic-drift displacement m',(400+2*800)/(1.2*1.5)*20e-6,.0222222)
check(97,'Faraday betatron work eV',quad(lambda B:300/.2,.2,.6),600)
wb=m.sqrt(2*1000*e/(md*.5**2)); T=2*m.pi/wb
mirror=orbit(T/4/2000,2000,[0.,m.sqrt(2000*e/md)],lambda y:[y[1],-wb*wb*y[0]])
check(98,'mirror quarter-period turning point m',mirror[0],.5,rtol=1e-8)
J=4*md*wb*.5**2*quad(lambda a:m.cos(a)**2,0,m.pi/2)
check(99,'phase-space ellipse action J s',J,1.62591e-21,atol=1e-27)
# Kinetic moments evaluated independently of the closed-form examples.
a=.2; U=5e5; sig=m.sqrt(100*e/md); u=a*U
mix=lambda v:(1-a)*normal(v,sig)+a*normal(v,sig,U)
qx=1e18*md/2*quad(lambda v:((v-u)**3+2*sig*sig*(v-u))*mix(v),-12*sig,U+12*sig)
check(100,'mixture heat-flow velocity integral W/m2',qx,2.00615e7)
check(101,'free-streaming density Fourier integral',.1*quad(lambda v:normal(v)*m.cos(v),-12,12),.0606531)
check(101,'free-streaming flux Fourier integral m/s',.1e4*quad(lambda v:v*normal(v)*m.sin(v),-12,12),606.531)
fn=quad(lambda x:4/m.sqrt(m.pi)*x*x*m.exp(-x*x),2,12)
fe=quad(lambda x:8/(3*m.sqrt(m.pi))*x**4*m.exp(-x*x),2,12)
check(102,'Maxwellian number tail by quadrature',fn,.0460117)
check(102,'Maxwellian energy tail by quadrature',fe,.156236)
check(103,'compressed fluid pressure invariant',m.exp(-.5)*m.exp(.3)**(5/3),1,rtol=1e-12)
q=orbit(3/6000,6000,[0.],lambda y:[-10-y[0]])[0]
check(104,'heat-flux transient ODE kW/m2',q,-9.50213)
g=3e6; mr=me*md/(me+md); b90=e*e/(4*m.pi*eps*mr*g*g);angle=2*m.atan(.5)
sigma=quad(lambda x:2*m.pi*m.sin(x)*b90*b90/(4*m.sin(x/2)**4),angle,m.pi)
check(105,'Rutherford angular cross-section m2',sigma,9.95653e-21,atol=1e-27)
g=m.sqrt(200*e/me); l=m.sqrt(eps*100*e/(1e19*e*e)); qmin=hbar/(2*me*g)
check(106,'Coulomb logarithm with specified cutoff',m.log(l/qmin),14.6946)
h=1e-4;x=.3;P=lambda x:(3*x*x-1)/2
L=lambda x:(1-x*x)*(P(x+h)-P(x-h))/(2*h)
check(107,'Legendre l=2 collision eigenvalue',(L(x+h)-L(x-h))/(4*h),-3*P(x),rtol=5e-8)
y=orbit(.01/2000,2000,[10.,1.],lambda y:[-50*(y[0]-y[1]),50*(y[0]-y[1])])
check(108,'two-species temperature ODE electron keV',y[0],7.15546)
var=1+3*m.exp(-2);u=2/m.e
check(109,'relaxed Gaussian second raw moment',quad(lambda v:v*v*normal(v,m.sqrt(var),u),u-12*m.sqrt(var),u+12*m.sqrt(var)),1.94735)
# Conditional transverse Gaussian moments reduce the BGK heat integral to one dimension.
M2=quad(lambda x:x*x*normal(x),-12,12);M4=quad(lambda x:x**4*normal(x),-12,12);M6=quad(lambda x:x**6*normal(x),-12,12)
coef=.5*((M6+4*M4+8*M2)/2-2.5*(M4+2*M2))
check(110,'BGK conductivity coefficient from Gaussian moments',coef,2.5,rtol=1e-10)
check(110,'BGK heat flux W/m2',-coef*1e18*20*e*1e-7/me*(2*e),-2.81794e5)
check(111,'smooth dielectric screening quadrature',quad(lambda y:y**3/(1+y*y)**2,0,100),4.10527018,rtol=2e-9)
# Waves: signs, matrix roots, derivatives, and real-time power.
check(112,'quadratic convective harmonic amplitude ratio',20*100**2/2/(1e5*100),.01)
z=1-.25/(1+.05j);N=cmath.sqrt(z)
check(113,'passive Drude field attenuation',m.exp(-2*m.pi*N.imag),.955795)
check(114,'Bohm-Gross group speed in thermal units',.45/m.sqrt(1+3*.15**2),.435541)
check(115,'ion-acoustic group speed m/s',1e5/(1+.5**2)**1.5,71554.2)
wp=m.sqrt(2e18*e*e/(eps*me));skin=c/m.sqrt(wp*wp-(2*m.pi*1e10)**2)
check(116,'evanescent skin depth m',skin,.00609746)
wp=m.sqrt(1e18*e*e/(eps*me));de=c/wp; Om=e*.2/me
check(117,'whistler group speed m/s',2*Om*de*.1,3.73861e7)
R=1-.36/(.5*(.5-1));L=1-.36/(.5*(.5+1))
check(118,'X-mode eigenvalue from dielectric determinant',R*L/((R+L)/2),.857297)
check(119,'fast magnetosonic matrix root m/s',1e6*m.sqrt((5+m.sqrt(17))/2),2.13578e6)
h=1e-3;w=lambda k:m.sqrt(1+k*k)
check(120,'packet dispersion curvature by second difference',(w(.75+h)-2*w(.75)+w(.75-h))/(h*h),.512,rtol=1e-6)
gamma=-m.sqrt(m.pi/8)/.2**3*m.exp(-1/(2*.2**2)-1.5)
check(121,'long-wave Landau amplitude after normalized time 1000',m.exp(gamma*1000),.936941)
js=[quad(lambda a,l=l:m.cos(.2*m.sin(a)-l*a),0,2*m.pi)/(2*m.pi) for l in range(9)]
check(122,'gyroangle first harmonic coefficient',js[1],.0995008)
check(122,'gyroangle Parseval sum',js[0]**2+2*sum(v*v for v in js[1:]),1,rtol=1e-10)
check(123,'real-wave cycle power W/m3',quad(lambda t:(6*m.cos(t)+9*m.sin(t))*3*m.cos(t)+(-16*m.cos(t)+4*m.sin(t))*4*m.sin(t),0,2*m.pi)/(2*m.pi),17,rtol=1e-10)
# MHD: compare species sums, work integrals, local derivatives and mode energy.
mu0=1.25663706127e-6
n=1e19;M=md+me;w=1e6/(e*n);u=1e4
ui=u+me*w/M;ue=u-md*w/M
check(124,'two-fluid direct kinetic sum minus bulk energy',n*(md*ui*ui+me*ue*ue)/2-n*M*u*u/2,1.77386)
check(125,'adiabatic pressure work integral J',-quad(lambda V:2000*(.001/V)**(5/3),.001,.001/8),9,rtol=1e-8)
di=m.sqrt(md/(mu0*1e19*e*e));va=.5/m.sqrt(mu0*1e19*md)
check(126,'Hall field ratio from direct electric fields',(.5/(mu0*.1))*.5/(e*1e19)/(va*.5),di/.1,rtol=1e-12)
h=1e-6;B=lambda x:m.sqrt(1-x*x/.25)
Jy=-(B(.15+h)-B(.15-h))/(2*h*mu0)
check(127,'Ampere derivative times field Pa/m',Jy*B(.15),4.77465e5)
check(128,'affine frozen-flux magnetic energy ratio',(.5**2+2**2)/2,2.125)
k=2*m.pi/.2;eta=1e-6;Dm=eta/mu0;tau=1/(Dm*k*k)
check(129,'integrated Joule heating J/m3',quad(lambda t:eta*.1**2*k*k/(2*mu0**2)*m.exp(-2*t/tau),0,tau),1720.20)
psi=lambda R,Z:.01*R**4+.02*Z*Z;R=1.;Z=.3;h=1e-4
lap=(psi(R+h,Z)-2*psi(R,Z)+psi(R-h,Z))/h**2-(psi(R+h,Z)-psi(R-h,Z))/(2*h*R)+(psi(R,Z+h)-2*psi(R,Z)+psi(R,Z-h))/h**2
check(130,'Grad-Shafranov operator from finite differences',lap,.12,rtol=1e-7)
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
u=[1000,0,0];B=[0,0,1];J=[0,1e4,0];eta=1e-7;E=[-x+eta*y for x,y in zip(cross(u,B),J)]
check(131,'field work minus Lorentz mechanical power',dot(J,E)-dot(u,cross(J,B)),10,rtol=1e-12)
L=10.;xi=.001;A=.01;B=.2;rho=1e19*md
W=B*B*A/(2*mu0)*quad(lambda z:(xi*m.pi/L*m.cos(m.pi*z/L))**2,0,L)
I=rho*A*quad(lambda z:(xi*m.sin(m.pi*z/L))**2,0,L)
check(132,'energy-principle frequency from independent integrals rad/s',m.sqrt(2*W/I),3.06527e5)
va=.1/m.sqrt(mu0*1e22*md);Dm=1e-4/mu0;delta=m.sqrt(Dm/va)
check(133,'Sweet-Parker matched electric fields V/m',1e-4*.1/(mu0*delta),110.800)
check(133,'Sweet-Parker mass-flux balance m2/s',m.sqrt(Dm*va),va*delta,rtol=1e-12)

report=dict(count=len(rows),all_passed=all(r['passed'] for r in rows),checks=rows)
out=ROOT/'.build/tag-depth/plasma-independent-numerics.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
for r in rows:
    if not r['passed']:print(r)
assert report['all_passed']
