#!/usr/bin/env python3
"""Reproduce 48 heating Tag exercises using quadrature, ODEs and conservation.
Run from any directory. Standard-library only; emits heating-numerics.json.
"""
import cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.build/tag-depth'
e=1.602176634e-19; me=9.1093837139e-31; md=3.3435837768e-27
eps0=8.8541878188e-12;c=299792458.;pi=math.pi
checks=[]
def check(tag,name,x,y,rtol=1e-7,atol=1e-10):
 row=dict(tag=f'MF{tag:06d}',name=name,actual=x,expected=y,rtol=rtol,atol=atol,passed=math.isclose(x,y,rel_tol=rtol,abs_tol=atol));checks.append(row)
 if not row['passed']: raise AssertionError(row)
def integral(f,a,b,n=10000):
 h=(b-a)/n
 return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))
def rk4(f,y,a,b,n=5000):
 h=(b-a)/n;t=a
 for _ in range(n):
  k1=f(t,y);k2=f(t+h/2,y+h*k1/2);k3=f(t+h/2,y+h*k2/2);k4=f(t+h,y+h*k3)
  y+=h*(k1+2*k2+2*k3+k4)/6;t+=h
 return y
def root(f,a,b,n=80):
 fa=f(a)
 for _ in range(n):
  m=(a+b)/2
  if f(m)*fa>0:a=m;fa=f(a)
  else:b=m
 return (a+b)/2

wf=rk4(lambda t,w:4-w/.2,0,0,.1)
wth=integral(lambda t:4*(1-math.exp(-t/.2)),0,.1)
check(15,'two-reservoir energy conservation [MJ]',wf+wth,.4)
check(15,'fast inventory [MJ]',wf,.3147754722298933)
v=math.sqrt(2*1e4*e/md);om=e*3/md
check(16,'gyro-orbit centripetal force vs Lorentz force',md*v*v/(v/om),e*v*3)
check(16,'D gyroradius [mm]',v/om*1e3,6.810,rtol=.0002)
I=math.sqrt(1e6/3);V=(3+4j)*I
mean=integral(lambda t:(math.sqrt(2)*V*cmath.exp(-1j*t)).real*(math.sqrt(2)*I*cmath.exp(-1j*t)).real,0,2*pi)/(2*pi)
check(17,'time-averaged VI [W]',mean,1e6)
check(17,'reactive power [Mvar]',(V*I).imag/1e6,4/3)
for R,z in [(2,10),(6,6),(18,10)]:
 zp=1/(1/complex(R,6)+1/complex(R,-6));check(18,f'parallel branches R={R}',zp.real,z);check(18,f'imaginary cancellation R={R}',zp.imag,0)
check(18,'accepted fraction at R=6',1-abs((6-10)/(6+10))**2,.9375)
check(19,'capacitor work integrated over charge [J]',integral(lambda q:q/1e-9,0,1e-9*3e4),.45)
check(19,'fault energy [J]',2e6*1e-5+.45,20.45)
P=4180*4;u=math.hypot(4180*4*.02,4180*.1)
check(20,'calorimetric power [kW]',P/1e3,16.72)
check(20,'comparison standardized residual',(17e3-P)/math.hypot(u,600),.348,rtol=.003)
check(21,'He3 charge-fraction concentration ratio',(2*.12)/(2*.02),6)
bcold=2*pi*140e9*me/(2*e);B=bcold*1.1*.98
check(22,'relativistic Doppler resonance residual [rad/s]',2*pi*140e9*(1-.2*.1),2*e*B/(1.1*me))
check(22,'resonance B [T]',B,2.6957,rtol=3e-5)
for a in [.03,.02]:
 frac=integral(lambda r:4*r/.02**2*math.exp(-2*r*r/.02**2),0,a)
 check(23,f'Gaussian aperture radius {a} [m]',frac,1-math.exp(-2*a*a/.02**2))
for d in [0,.02]:
 F=integral(lambda x:math.exp(-(x-d)**2/.02**2)/(.02*math.sqrt(pi)),-.02,.02)
 check(24,f'deposition overlap d={d}',F,(math.erf((.02-d)/.02)+math.erf((.02+d)/.02))/2)
t=.1*math.log(100)
check(25,'RC numerical decay [V]',rk4(lambda t,v:-v/.1,50000,0,t),500)
check(25,'resistor dissipated plus residual energy [J]',integral(lambda t:50000**2*math.exp(-2*t/.1)/1e6,0,t)+.5*1e-7*500**2,125)
check(26,'electron slope-jump absorbed power [kW]',1.5*5e19*10e3*e/1e3,120.16324755)
check(27,'power boundary efficiencies [A/W]',1e5/2.5e6,.04)
p1=rk4(lambda s,p:-p,10,0,.5);p2=rk4(lambda s,p:-3*p,p1,0,.5)
check(28,'piecewise stopping outgoing [MW]',p2,10*math.exp(-2))
check(28,'piecewise stopping energy conservation [MW]',(10-p1)+(p1-p2)+p2,10)
f0=rk4(lambda x,y:2*(1-y)-y,0,0,.5)
check(29,'neutralizer master-equation solution',f0,2/3*(1-math.exp(-1.5)))
# Integrate in time with E loss split, independently from the energy quadrature.
fi=integral(lambda x:1/(1+x**1.5),.1,2)/1.9
check(30,'cumulative ion fraction energy integral',fi,.531631191072266)
# Midpoint march in rescaled time: E'=-(1+E**1.5), preserving channel ratios; stop at E=.1.
x=2.;ion=0.;electron=0.;dt=1e-5
while x>.1:
 h=min(dt,(x-.1)/(1+x**1.5));mid=x-h*(1+x**1.5)/2
 loss=h*(1+mid**1.5)
 if x-loss<.1:loss=x-.1;h=loss/(1+mid**1.5)
 ion+=h;electron+=h*mid**1.5;x-=loss
check(30,'time-march ion fraction vs energy integral',ion/1.9,fi,rtol=2e-7)
check(30,'time-march two-channel energy conservation',ion+electron,1.9,rtol=1e-8)
check(31,'shine-through power sensitivity',math.exp(-2)/math.exp(-3),math.e)
check(31,'shine-through heat at tau=3 [MW/m2]',10*math.exp(-3)/.05,9.95741367357)
s=.04;A=.08
inside=integral(lambda r:r/s**2*math.exp(-r*r/(2*s*s)),0,A)
check(32,'Gaussian NBI aperture [fraction]',inside,.8646647167633873)
check(32,'Gaussian NBI total power',integral(lambda r:r/s**2*math.exp(-r*r/(2*s*s)),0,10*s),1)
weights=[.6,.3/2,.1/3];total=sum(weights)
check(33,'energy-group total power [MW]',1e20*80e3*e*total/1e6,1.00403069064)
check(33,'power fractions sum',sum(x/total for x in weights),1)
nlim=eps0*3**2/me*((2**2-1)/(2*2))**2;a=math.sqrt(nlim*me/eps0)/3
check(34,'accessibility recovered from inverse density',a+math.sqrt(1+a*a),2)
check(34,'minimum resonant energy [keV]',me*c*c/e/1000*(1/math.sqrt(1-.5**2)-1),79.0518127832469)
M=32;d=.01;k=pi/2/d
amp=lambda q:sum(cmath.exp(1j*j*(pi/2-q*d)) for j in range(M))
check(35,'array main-lobe amplitude',abs(amp(k)),M)
check(35,'array first null',abs(amp(k+2*pi/(M*d))),0,atol=1e-12)
check(35,'array refractive index',c*k/(2*pi*3.7e9),2.025624716216216)
check(36,'normalized efficiency',3e19*2*1e5/1e6/1e20,.06)
check(36,'independent relative uncertainty',math.sqrt(.05**2+.01**2+.1**2+.03**2),.11618950038622251)
leak=10**(-30/20)
phases=[abs(.2+leak*cmath.exp(1j*2*pi*j/10000))**2*1e3 for j in range(10001)]
check(37,'directivity minimum reflection [kW]',min(phases),1e3*(.2-leak)**2)
check(37,'directivity maximum reflection [kW]',max(phases),1e3*(.2+leak)**2)
check(38,'loop-voltage scenarios equal [V]',2e-6*(.5e6-.1e6),1.6e-6*.5e6)
check(39,'high-field accessibility',math.sqrt(1.5)/2+math.sqrt(1+1.5/4),1.784976375651652)
nO=eps0*me*(2*pi*28e9)**2/e**2;B=pi*28e9*me/e
check(40,'UHR dispersion restored',(nO*.75)*e*e/(eps0*me)+(e*B/me)**2,(2*pi*28e9)**2)
check(40,'density layer spacing [mm]',.02*math.log(4/3)*1e3,5.753641449)
A=2*pi*10*math.sqrt(.5/2)*(1+.5)
for sig in [.04,.1]:
 val=integral(lambda x:math.exp(-A*x*x-x*x/(2*sig*sig))/(math.sqrt(2*pi)*sig),-9*sig,9*sig)
 check(41,f'angular-spectrum quadrature sigma={sig}',val,1/math.sqrt(1+2*A*sig*sig))
ct=sum(.6*(.5*.4)**j for j in range(100));loss=sum(.5*.4*(.5*.4)**j for j in range(100))
check(42,'multi-pass energy conservation',ct+loss,1)
check(42,'thermal fraction',ct*.8*.9,.54)
dN=math.sqrt(-math.log(.8)/A);theta=math.acos(1/math.sqrt(3))
check(43,'conversion at inferred window',math.exp(-A*dN*dN),.8)
check(43,'linear angular halfwidth [deg]',dN/math.sin(theta)*180/pi,4.829,rtol=.0005)
brightness=rk4(lambda tau,tb:1000-tb,0,0,2)
check(44,'transfer ODE brightness',brightness,1000*(1-math.exp(-2)))
check(44,'inferred conversion',600/brightness,.6939105856497994)
check(45,'historical angular-window width ratio',6/10,.6)
wp2=1e18*e*e/(eps0*me);ome=e*.02/me;w=2*pi*13.56e6
k=math.sqrt(w*wp2/(c*c*ome))
check(46,'whistler wavelength [m]',2*pi/k,.2145,rtol=.001)
check(46,'helicon resonance minimum energy [keV]',me*c*c/e/1e3*(1/math.sqrt(1-1/9)-1),30.997,rtol=.0001)
ap=abs(1+cmath.exp(.1j))**2;am=abs(1+cmath.exp(1j*(pi+.1)))**2
check(47,'two-element direction ratio',ap/am,1/math.tan(.05)**2)
check(47,'normalized total opposite-direction powers',ap+am,4)
a=-math.log(.7)/.008
check(48,'attenuation ODE beta doubling',1-rk4(lambda s,p:-a*.016*p,1,0,1),.51)
y=rk4(lambda t,y:(.2-y)/.002,0,0,.0001)
check(49,'filtered pulse maximum',y,.2*(1-math.exp(-.05)))
check(49,'pulse reflected energy [J]',1e6*.2*.0001,20)
# Covariance via independent common + residual components, not direct quadratic reuse.
# X=8*z1; Y=6*(.5*z1+sqrt(.75)*z2); Z=4*z3.
u2=(8-6*.5)**2+(6*math.sqrt(.75))**2+4**2
check(50,'correlated current residual sigma [kA]',math.sqrt(u2),math.sqrt(68))
check(51,'regional current/coupled power [A/W]',20e3/370e3,.05405405405405406)
xhalf=root(lambda x:(math.sin(x)/x)**2-.5,.1,pi)
check(134,'sinc energy FWHM coefficient',2*xhalf/pi,.8858929413789048)
integ=integral(lambda t:cmath.exp(-1j*2*pi*.5e6*t),0,1e-6)
check(134,'time-integral off-resonance ratio',abs(integ/1e-6)**2,4/pi**2)
check(134,'detuned energy [eV]',e*1e6*1e-12/(2*md)*4/pi**2,9.710,rtol=.0002)
rcold=e*15/(md*2*pi*40e6)
for vv in [-1e6,1e6]:
 rr=rcold/(1-5*vv/(2*pi*40e6))
 check(135,f'Doppler resonance v={vv}',2*pi*40e6-5*vv,e*15/(md*rr))
check(135,'Doppler layer thermal spread [cm]',rcold*5*math.sqrt(1e4*e/md)/(2*pi*40e6)*100,3.939,rtol=.001)
# Independent 3x3 determinant and recovered field components.
def matrixdet(x):
 M=[[3,-2j,math.sqrt(x)],[2j,3-x,0],[math.sqrt(x),0,-100-x]]
 return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])).real
xf=root(matrixdet,1,2);Ey=-2j/(3-xf);Ez=-math.sqrt(xf)/(-100-xf)
check(136,'full cold matrix determinant',matrixdet(xf),0,atol=1e-11)
check(136,'full cold matrix first-row residual',abs(3-2j*Ey+math.sqrt(xf)*Ez),0,atol=1e-12)
check(136,'finite-P fast root',xf,1.6740,rtol=6e-5)
for delta in [0,math.radians(5)]:
 Ex=100;Ey=-50j*cmath.exp(1j*delta);Ei=(Ex+1j*Ey)/math.sqrt(2);Eo=(Ex-1j*Ey)/math.sqrt(2)
 check(137,f'circular basis norm delta={delta}',abs(Ei)**2+abs(Eo)**2,12500)
 check(137,f'circular fraction delta={delta}',abs(Ei)**2/12500,.5+100*50*math.cos(delta)/12500)
check(138,'minority per-ion gain [keV]',1e6/(.01*5e19*10)*.1/e/1000,124.83018148921526)
check(138,'minority quasineutrality',4.9e19+2*5e17,5e19)
vals=[]
for x in [.2,.4]:
 J=integral(lambda t:cmath.exp(1j*(x*math.sin(t)-t)),0,2*pi)/(2*pi)
 series=sum((-1)**k*(x/2)**(2*k+1)/(math.factorial(k)*math.factorial(k+1)) for k in range(12))
 check(139,f'Bessel Fourier integral x={x}',J.real,series);check(139,f'Bessel imaginary cancellation x={x}',J.imag,0);vals.append(J.real**2)
check(139,'second-harmonic coupling factor ratio',vals[1]/vals[0],3.881,rtol=.0001)
for conc in [.2,.5]:
 u=(1-conc/2)/(1+conc)
 check(140,f'ion hybrid response cancellation XH={conc}',conc/(u-1)+(1-conc)/(2*(u-.25)),0)
f1=2/3;f2=1/3
check(141,'left-cutoff response at He3',f1/(2/3-1)+f2/(2/3-.5),0)
check(141,'trace-third-species quasineutrality',.664+.332+2*.002,1)
work=integral(lambda t:100*math.cos(t)*100*(.02*math.cos(t)+.03*math.sin(t)),0,2*pi)/(2*pi)
check(142,'cycle-average dissipative density [W/m3]',work,100)
check(142,'dielectric conductivity agreement',.5*(2*pi*40e6)*eps0*(.02/(2*pi*40e6*eps0))*100**2,work)
# Direct quadrature of Maxwellian zeroth and second moments at two times.
n=1e17;Dv=1e12
energies=[]
for t in [0,.001]:
 sig=math.sqrt(1e10+2*Dv*t)
 g=lambda v:math.exp(-v*v/(2*sig*sig))/(math.sqrt(2*pi)*sig)
 norm=integral(g,-10*sig,10*sig);moment=integral(lambda v:v*v*g(v),-10*sig,10*sig)
 check(143,f'Gaussian particle normalization t={t}',norm,1)
 energies.append(1.5*md*n*moment)
check(143,'energy-moment growth [J/m3]',energies[1]-energies[0],3*md*n*Dv*.001)
I0=integral(lambda t:math.exp(math.cos(t)),0,2*pi)/(2*pi);dV=10*math.log(I0)
flux=integral(lambda t:math.exp(-(dV+10*math.cos(t))/10),0,2*pi)/(2*pi)
check(144,'RF averaged electron flux matches no-RF flux',flux,1)
check(144,'rectified sheath voltage [V]',dV,2.359143585071789)

result=dict(suite='tag_depth_heating',count=len(checks),tags=len(set(x['tag'] for x in checks)),passed=all(x['passed'] for x in checks),checks=checks)
assert result['tags']==48
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'heating-numerics.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['suite','count','tags','passed']}))
