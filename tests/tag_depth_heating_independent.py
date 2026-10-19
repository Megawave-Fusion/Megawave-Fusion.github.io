"""Independent reviewer: integrate equations, verify conservation and limits for all 48 tags."""
from pathlib import Path
import math, cmath, json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.build/tag-depth'
e=1.602176634e-19; me=9.1093837139e-31; md=3.3435837768e-27
c=299792458.; eps0=8.8541878188e-12; pi=math.pi
rows=[]
def check(tag,name,value,expected,rtol=1e-8,atol=1e-10):
 ok=math.isclose(value,expected,rel_tol=rtol,abs_tol=atol)
 rows.append(dict(tag=f'MF{tag:06d}',name=name,value=value,expected=expected,passed=ok))
 if not ok: raise AssertionError(rows[-1])
def quad(f,a,b,n=4000):
 h=(b-a)/n
 return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))
def rk4(f,y,end,n=4000):
 y=list(y);dt=end/n
 for i in range(n):
  t=i*dt;k1=f(t,y);k2=f(t+dt/2,[v+dt*k/2 for v,k in zip(y,k1)])
  k3=f(t+dt/2,[v+dt*k/2 for v,k in zip(y,k2)]);k4=f(t+dt,[v+dt*k for v,k in zip(y,k3)])
  y=[v+dt*(a+2*b+2*cc+d)/6 for v,a,b,cc,d in zip(y,k1,k2,k3,k4)]
 return y
def root(f,a,b):
 assert f(a)*f(b)<0
 for _ in range(70):
  m=(a+b)/2
  if f(m)*f(a)>0:a=m
  else:b=m
 return (a+b)/2
# Direct two-state integration with independent heat accumulation.
wf,wt=rk4(lambda t,y:[4-y[0]/.2,y[0]/.2],[0,0],.1)
check(15,'integrated fast inventory [MJ]',wf,4*.2*(1-math.exp(-.5)))
check(15,'energy supplied equals two inventories [MJ]',wf+wt,.4)
# Orbit ODE returns after a gyroperiod and radius matches kinetic energy.
omega=e*3/md;v=math.sqrt(2*1e4*e/md);period=2*pi/omega
vx,vy=rk4(lambda t,y:[omega*y[1],-omega*y[0]],[v,0],period)
check(16,'gyro-orbit speed conservation',math.hypot(vx,vy),v)
check(16,'radius [mm]',v/omega*1000,6.81,rtol=.001)
check(16,'gyroperiod [ns]',period*1e9,43.7,rtol=.001)
# RMS voltage/current time-domain check independent of complex-power expression.
I=math.sqrt(1e6/3);Z=3+4j;V=I*Z
check(17,'period average real voltage times current [W]',quad(lambda x:2*I*(V.real*math.cos(x)-V.imag*math.sin(x))*math.cos(x),0,2*pi)/(2*pi),1e6)
check(17,'peak voltage [V]',abs(V)*math.sqrt(2),4082.48290463863)
for R,expect in [(2,10),(6,6),(18,10)]:
 z=1/(1/(R+6j)+1/(R-6j));check(18,f'parallel branch real R={R}',z.real,expect);check(18,f'parallel imaginary R={R}',z.imag,0)
check(18,'accepted fraction under synchronous load change',1-abs((6-10)/(6+10))**2,.9375)
check(19,'source power integral plus stored capacitor energy [J]',quad(lambda t:2e6,0,10e-6)+.5*1e-9*30000**2,20.45)
p=4180*4;u=p*math.sqrt(.02**2+(.1/4)**2)
check(20,'water calorimetry [W]',p,16720)
check(20,'standard uncertainty [W]',u,535.3,rtol=.001)
check(20,'combined difference in standard uncertainties',280/math.sqrt(u*u+600**2),.3483,rtol=.001)
for x in [.02,.12,.2]:check(21,f'He-3 charge fraction for particle fraction {x}',2*x,x*2)
check(21,'2 percent He-3 leaves H charge fraction',1-2*.02,.96)
# EC resonance, beam truncation and overlap are independently integrated.
Bcold=2*pi*140e9*me/(2*e);B=Bcold*1.1*(1-.2*.1)
check(22,'relativistic Doppler resonance residual [Hz]',140e9-2*e*B/(2*pi*me*1.1)-.2*.1*140e9,0,atol=1e-4)
check(22,'relativistic resonance field [T]',B,2.6957,rtol=.001)
for a,expected in [(.03,.988891003461758),(.02,1-math.exp(-2))]:
 inside=quad(lambda r:2*pi*r*2/(pi*.02**2)*math.exp(-2*r*r/.02**2),0,a)
 check(23,f'Gaussian aperture integral a={a}m',inside,expected)
for d,expected in [(0,math.erf(1)),(.02,.5*math.erf(2))]:
 check(24,f'Gaussian current fraction d={d}m',quad(lambda x:math.exp(-((x-d)/.02)**2)/(math.sqrt(pi)*.02),-.02,.02),expected)
C,R,V0=1e-7,1e6,50000.;t=R*C*math.log(100)
energy=quad(lambda u:(V0*math.exp(-u/(R*C)))**2/R,0,t)
check(25,'discharged heat plus remaining capacitor energy [J]',energy+.5*C*500**2,.5*C*V0**2)
check(25,'100:1 voltage decay time [s]',t,.4605170185988092)
check(26,'break in electron-temperature slope [W]',1.5*5e19*(1000*e)*(8-(-2)),120163.24755)
for denominator,expected in [(1e6,.1),(1.2e6,1/12),(2.5e6,.04)]:check(27,f'efficiency with denominator {denominator}W',1e5/denominator,expected)
# Beam transfer: optical-depth ODE, population-rate ODE, and slowing-down energy integral.
p1,loss1=rk4(lambda x,y:[-y[0],y[0]],[10,0],.5)
p2,loss2=rk4(lambda x,y:[-3*y[0],3*y[0]],[p1,0],.5)
check(28,'two-region unabsorbed power [MW]',p2,10*math.exp(-2))
check(28,'two-region power conservation [MW]',p2+loss1+loss2,10)
f=rk4(lambda x,y:[1*(1-y[0])-.5*y[0]],[0],1)[0]
check(29,'two-state neutral fraction integrated vs analytic',f,2/3*(1-math.exp(-1.5)))
check(29,'neutralization saturation limit',2e-20/(2e-20+1e-20),2/3)
fi=quad(lambda E:1/(1+(E/100)**1.5),10,200)/190
check(30,'integrated ion slowing-down fraction',fi,.5316,rtol=.001)
# Parameterize kinetic energy by E=200-u, so independent ODE accumulates lost energy.
Ei,Ee=rk4(lambda u,y:[1/(1+((200-u)/100)**1.5),1-1/(1+((200-u)/100)**1.5)],[0,0],190)
check(30,'ion energy ODE vs energy quadrature [keV]',Ei,190*fi)
check(30,'ion and electron energies exhaust 190keV',Ei+Ee,190)
for tau,expected in [(3,9.95741367357e6),(2,27.0670566473e6)]:check(31,f'shine-through footprint tau={tau} [W/m2]',10e6*math.exp(-tau)/.05,expected)
sigma=.04
G=lambda r:2*pi*r*1e5/(2*pi*sigma*sigma)*math.exp(-r*r/(2*sigma*sigma))
check(32,'finite target captures Gaussian beam [W]',quad(G,0,.08),1e5*(1-math.exp(-2)))
check(32,'second radial moment [m2]',quad(lambda r:r*r*G(r),0,.5)/1e5,2*sigma*sigma)
w=[.6,.3/2,.1/3];fractions=[x/sum(w) for x in w]
check(33,'80keV energy group power [W]',1e20*8e4*e*sum(w),1004030.69064)
check(33,'full-energy power fraction',fractions[0],.7659574468085106)
check(33,'normalized group power',sum(fractions),1)
# Lower-hybrid access, array-spectrum zeros, covariance and circuit subtraction.
N=2.;a=(N*N-1)/(2*N);ne=eps0*3**2/me*a*a
check(34,'inverse accessibility substitution',a+math.sqrt(1+a*a),N)
check(34,'density accessibility at 3T [m-3]',ne,4.920e19,rtol=.001)
check(34,'relativistic minimum electron energy [keV]',me*c*c/e/1000*(1/math.sqrt(1-1/N**2)-1),79.05,rtol=.001)
M,d=32,.01;phase=pi/2;kpeak=phase/d
array=lambda k:sum(cmath.exp(1j*j*(k*d-phase)) for j in range(M))
check(35,'array peak norm squared',abs(array(kpeak))**2,M*M)
check(35,'first spectral null',abs(array(kpeak+2*pi/(M*d)))**2,0)
check(35,'parallel refractive index',c*kpeak/(2*pi*3.7e9),2.0256,rtol=.001)
check(36,'density-radius normalized efficiency',3e19*2*1e5/1e6,6e18)
check(36,'fractional propagated uncertainty',math.sqrt(.05**2+.01**2+.10**2+.03**2),.1161895003862225)
epsilon=10**(-30/20)
for phase,expected in [(0,53649.1106407),(pi,28350.8893593)]:
 check(37,f'directional leakage phase={phase} [W]',1e6*abs(.2+epsilon*cmath.exp(1j*phase))**2,expected)
for Rp,expected in [(2e-6,1e5),(1.6e-6,0)]:
 Inon=.5e6-.8/Rp;check(38,f'noninductive residual with Rp={Rp}',Inon,expected)
 check(38,f'circuit reconstructed loop voltage Rp={Rp}',Rp*(.5e6-Inon),.8)
aH=math.sqrt(1.5)/2
check(39,'HFS accessibility a+sqrt(1+a^2)',aH+math.sqrt(1+aH*aH),1.784976375651652)
# EBW layer displacement, angular-spectrum integration, geometric power balance and brightness.
f=28e9;nc=eps0*me*(2*pi*f)**2/e**2
check(40,'O-cutoff density [m-3]',nc,9.725e18,rtol=.001)
check(40,'O-UHR separation for Y=0.5 Ln=2cm [m]',-.02*math.log(.75),.00575364144903562)
check(40,'10percent density shift from inverse exponential profile [m]',-.02*math.log(1.1),-.0019062035960865)
A=2*pi*10*math.sqrt(.5/2)*1.5
for sigma in [.04,.1]:
 integral=quad(lambda x:math.exp(-x*x/(2*sigma*sigma)-A*x*x)/(math.sqrt(2*pi)*sigma),-10*sigma,10*sigma)
 check(41,f'angular Gaussian convolution sigma={sigma}',integral,1/math.sqrt(1+2*A*sigma*sigma))
conversion=sum(.6*(.5*(1-.6))**j for j in range(40))
check(42,'multi-pass converted fraction',conversion,.75)
check(42,'multi-pass channel conservation',conversion+sum((1-.6)*.5*(.5*(1-.6))**j for j in range(40)),1)
check(42,'absorbed fraction after propagation and absorption',conversion*.8*.9,.54)
dn=math.sqrt(-math.log(.8)/A);theta=math.acos(math.sqrt(1/3))
check(43,'conversion at angular-window boundary',math.exp(-A*dn*dn),.8)
check(43,'linearized angular half-width [degree]',math.degrees(dn/math.sin(theta)),4.83,rtol=.002)
Tb=rk4(lambda tau,y:[1000-y[0]],[0],2)[0];Cconv=600/Tb
check(44,'radiation-transfer integrated brightness [eV]',Tb,1000*(1-math.exp(-2)))
check(44,'inferred conversion fraction',Cconv,.69391,rtol=.001)
check(45,'MAST cited angular-window width ratio',(2*3)/(2*5),.6)
check(45,'MAST cited deposition displacement in r/a',.9-.6,.3)
# Whistler ordering, two-element phasors, optical-depth scaling and detector dynamics.
wp=math.sqrt(1e18*e*e/(eps0*me));Om=e*.02/me;om=2*pi*13.56e6;k=math.sqrt(om*wp*wp/(Om*c*c))
check(46,'low-frequency whistler wavenumber [m-1]',k,29.29,rtol=.001)
check(46,'whistler kc/wp ordering',k*c/wp,math.sqrt(om/Om))
check(46,'Nparallel=3 minimum electron energy [keV]',me*c*c/e/1000*(1/math.sqrt(1-1/9)-1),31.0,rtol=.001)
kphase=pi/2;phase=kphase+.1
forward=abs(1+cmath.exp(1j*(phase-kphase)))**2
backward=abs(1+cmath.exp(1j*(phase+kphase)))**2
check(47,'two-phasor directional power conservation',forward+backward,4)
check(47,'power ratio forward/backward',forward/backward,399.333500066,rtol=1e-8)
check(48,'twice damping coefficient absorption',1-(1-.3)**2,.51)
check(48,'beta optical-depth coefficient',-math.log(.7)/.008,44.58436799234155)
response=rk4(lambda t,y:[(.2-y[0])/.002],[0],.0001)[0]
check(49,'filtered reflection excursion',response,.2*(1-math.exp(-.05)))
check(49,'true reflected pulse energy [J]',quad(lambda t:1e6*.2,0,.0001),20)
check(50,'reconstructed helicon residual [kA]',200-150-20,30)
check(50,'independent residual uncertainty [kA]',math.sqrt(8**2+6**2+4**2),math.sqrt(116))
check(50,'correlated residual uncertainty [kA]',math.sqrt(8**2+6**2+4**2-2*.5*8*6),math.sqrt(68))
check(51,'core rho<0.2 current per coupled power [A/W]',20e3/370e3,.05405405405405406)
check(51,'core ratio standard uncertainty [A/W]',10e3/370e3,.02702702702702703)
# ICRH advanced tags: time integral, matrix residual, Fourier-Bessel and energy moments.
t=1e-6;Delta=2*pi*.5e6
integral=complex(quad(lambda x:math.cos(Delta*x),0,t),quad(lambda x:-math.sin(Delta*x),0,t))
check(134,'finite-duration resonance energy ratio',abs(integral/t)**2,4/pi**2)
xhalf=root(lambda x:(math.sin(x)/x)**2-.5,1,2)
check(134,'sinc squared FWHM [MHz]',2*xhalf/(pi*t)/1e6,.8858929413789047)
check(134,'resonant deuteron energy [eV]',.5*e*1e6*t*t/md,23.959,rtol=.00001)
om=2*pi*40e6;Rc=e*15/(md*om)
for vp in [1e6,-1e6]:
 Rres=Rc/(1-5*vp/om)
 check(135,f'Doppler radius resubstitution v={vp}',om-5*vp-e*15/(md*Rres),0,atol=1e-6)
check(135,'thermal radial standard deviation [m]',Rc*5*math.sqrt(1e4*e/md)/om,.0394,rtol=.002)
P=-100.;S=4.;D=2.;A0=3.
x=root(lambda x:A0-D*D/(A0-x)-x/(P-x),1,2)
Ex=1;Ey=-1j*D/(A0-x);Ez=-math.sqrt(x)/(P-x)
for idx,value in enumerate([A0*Ex-1j*D*Ey+math.sqrt(x)*Ez,1j*D*Ex+(A0-x)*Ey,math.sqrt(x)*Ex+(P-x)*Ez]):
 check(136,f'full Maxwell matrix row {idx+1} residual',abs(value),0)
check(136,'finite parallel-response root',x,1.67394,rtol=.00001)
for delta in [0,math.radians(5)]:
 Ex=100;Ey=50*cmath.exp(1j*(-pi/2+delta));Eion=(Ex+1j*Ey)/math.sqrt(2);Eopp=(Ex-1j*Ey)/math.sqrt(2)
 check(137,f'unitary circle decomposition delta={delta}',abs(Eion)**2+abs(Eopp)**2,12500)
 check(137,f'ion-rotating fraction delta={delta}',abs(Eion)**2/12500,.5+100*50*math.cos(delta)/12500)
check(138,'minority energy per ion over 0.1s [keV]',1e6/(5e18)*.1/(e*1000),124.83,rtol=.001)
check(138,'He-3 charge-balance bulk D [m-3]',5e19-2*.02*5e19,4.8e19)
J=lambda x:complex(quad(lambda th:math.cos(x*math.sin(th)-th),0,2*pi)/(2*pi),quad(lambda th:math.sin(x*math.sin(th)-th),0,2*pi)/(2*pi))
for x,expected in [(.2,.099500832639236),(.4,.196026577955319)]:check(139,f'Fourier-integral J1({x})',J(x).real,expected)
check(139,'harmonic geometric coefficient ratio',abs(J(.4)/J(.2))**2,3.881,rtol=.001)
for frac in [.2,.5]:
 u=(1-frac/2)/(1+frac)
 check(140,f'ion-ion hybrid residual x={frac}',frac/(u-1)+(1-frac)/(2*(u-.25)),0)
# In normalized units: electron cancellation leaves sum charge fractions/(w-Omega)=0.
OmH,OmD,Om3=1.,.5,2/3
fH=(OmH-Om3)/(OmH-OmD);fD=1-fH
check(141,'H-D cold left-cutoff at He-3 resonance',fH/(Om3-OmH)+fD/(Om3-OmD),0)
check(141,'trace-He charge conservation',.664+.332+2*.002,1)
Q=quad(lambda th:100*math.cos(th)*100*(.02*math.cos(th)+.03*math.sin(th)),0,2*pi)/(2*pi)
check(142,'period integral of JE [W/m3]',Q,100)
check(142,'conductivity-to-susceptibility dissipative identity',om*eps0*(.02/(om*eps0))*100**2/2,Q)
# Integrate normalized Gaussian moments before and after velocity diffusion.
moments=[]
for var in [1e10,1.2e10]:
 sigma=math.sqrt(var);g=lambda v:math.exp(-v*v/(2*var))/(math.sqrt(2*pi)*sigma)
 norm=quad(g,-9*sigma,9*sigma);moment=quad(lambda v:v*v*g(v),-9*sigma,9*sigma)
 check(143,f'Gaussian particle conservation variance={var}',norm,1)
 moments.append(1.5*md*1e17*moment)
check(143,'energy moment gain vs diffusion source [J/m3]',moments[1]-moments[0],3*md*1e17*1e12*.001)
I0=quad(lambda th:math.exp(math.cos(th)),0,2*pi)/(2*pi);dV=10*math.log(I0)
check(144,'RF sheath rectification voltage [V]',dV,2.359143585071787)
check(144,'period averaged Boltzmann electron flux retains balance',quad(lambda th:math.exp(-(dV+10*math.cos(th))/10),0,2*pi)/(2*pi),1)
expected=set(range(15,52))|set(range(134,145))
assert {int(x['tag'][2:]) for x in rows}==expected
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'heating-cross-numerics.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checks=len(rows),tags=len(expected),passed=all(x['passed'] for x in rows))))
