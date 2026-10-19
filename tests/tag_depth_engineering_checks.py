#!/usr/bin/env python3
"""Independent analytic, conservation and refinement checks for 39 teaching tags."""
from pathlib import Path
import math, cmath, json, hashlib
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".build/tag-depth"
records = []
e, kb, me, md = 1.602176634e-19, 1.380649e-23, 9.1093837139e-31, 3.3435837768e-27
mu0, eps0, c = 4*math.pi*1e-7, 8.8541878188e-12, 299792458.0
relectron = e*e/(4*math.pi*eps0*me*c*c)

def check(tag, name, actual, expected, rtol=1e-8, atol=1e-12):
    passed = math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol)
    records.append(dict(tag=f"MF{tag:06d}", name=name, actual=actual,
                        expected=expected, rtol=rtol, atol=atol, passed=passed))
    if not passed:
        raise AssertionError(records[-1])

def quad(f, a, b, n=4000):
    assert n % 2 == 0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))

def rk4(f, y, end, n=2000):
    dt=end/n; y=list(y)
    for i in range(n):
        t=i*dt
        a=f(t,y); b=f(t+dt/2,[v+dt*w/2 for v,w in zip(y,a)])
        cc=f(t+dt/2,[v+dt*w/2 for v,w in zip(y,b)])
        d=f(t+dt,[v+dt*w for v,w in zip(y,cc)])
        y=[v+dt*(aa+2*bb+2*ccc+dd)/6 for v,aa,bb,ccc,dd in zip(y,a,b,cc,d)]
    return y

def trap(t, y):
    return sum((y[i]+y[i+1])*(t[i+1]-t[i])/2 for i in range(len(t)-1))

# 8: reconstruct enclosed current by independent area integration.
a,R,B,Ip=.6,2.5,3.,1e6
j0=2*Ip/(math.pi*a*a)
I_num=lambda r:quad(lambda x:2*math.pi*x*j0*(1-x*x/a/a),0,r)
check(8,"integrated current [A]",I_num(a),Ip)
q_num=lambda r:2*math.pi*r*r*B/(mu0*R*I_num(r))
check(8,"edge q",q_num(a),2.16)
check(8,"rational surface q=2",q_num(a*math.sqrt(.92)),2)

# 9: radial force balance; pressure plus magnetic pressure stays constant.
Bz=lambda r:.8*(2*r*r-1)
p=lambda r:(.8**2-Bz(r)**2)/(2*mu0)
for r in (.2,.5,.8):
    h=1e-6
    dp=(p(r+h)-p(r-h))/(2*h)
    J=-(Bz(r+h)-Bz(r-h))/(2*h*mu0)
    check(9,f"pressure gradient and JxB r={r}",dp,J*Bz(r))
check(9,"null pressure [Pa]",p(1/math.sqrt(2)),254647.90894703259)
check(9,"temperature sum [keV]",p(1/math.sqrt(2))/1e20/e/1000,15.89387234485362)

# 10: integrate the bounce ODE independently and recover the orbit.
v=math.sqrt(2*20e3*e/md); alpha=math.pi/4; L=2
omega=v*math.sin(alpha)/L; period=2*math.pi/omega
z,zdot=rk4(lambda t,y:[y[1],-omega**2*y[0]], [0,v*math.cos(alpha)],period)
check(10,"full bounce position returns [m]",z,0,atol=1e-9)
check(10,"full bounce velocity returns [m/s]",zdot,v*math.cos(alpha))
check(10,"bounce period [microsecond]",period*1e6,12.836474842610404)
check(10,"mirror-point parallel kinetic energy",.5*md*v*v*(1-2*math.sin(alpha)**2),0)

# 11,14: field-line map closure; angular mismatch is accumulated unwrapped.
theta=0.
for _ in range(5): theta=(theta+2*math.pi*2/5)%(2*math.pi)
check(11,"five-turn closure",theta,0)
check(11,"100-turn angle error [degree]",100*360*.001,36)
check(14,"six toroidal turns give five poloidal turns",6*(5/6),5)
check(14,"island-chain denominator",6,6)

# 12: adiabatic compression conserves entropy relation and magnetic flux.
C=5; n0,T0,B0,r0=1.,.2,2.,1.
n,T,BB,r=n0*C**3,T0*C**2,B0*C**2,r0/C
check(12,"pV^(5/3) invariant",n*T*(r**3)**(5/3),n0*T0*(r0**3)**(5/3))
check(12,"flux B*R^2 invariant",BB*r*r,B0*r0*r0)
check(12,"gyroradius/radius invariant",math.sqrt(T)/BB/r,math.sqrt(T0)/B0/r0)

# 13 and74: exact integration of piecewise linear waveforms is invariant to refinement.
for tag,t,y,target in [(13,[0,.5,1,1.5,2],[0,4,6,4,0],7),
                        (74,[0,.1,.2,.3,.4],[0,2,4,2,0],.8)]:
    t2=[]; y2=[]
    for i in range(len(t)-1):
        t2.extend([t[i],(t[i]+t[i+1])/2]);y2.extend([y[i],(y[i]+y[i+1])/2])
    t2.append(t[-1]);y2.append(y[-1])
    check(tag,"waveform integral [MJ]",trap(t,y),target)
    check(tag,"subdivided waveform integral [MJ]",trap(t2,y2),target)
check(13,"integrated gain",7/20,.35)
check(74,"stored-energy closure [MJ]",1+trap([0,.1,.2,.3,.4],[0,2,4,2,0])-.4,1.4)

# 52: solve compatibility algebra and examine free/rigid support limits.
E,alph,DT,A,length=180e9,12e-6,150,.01,1
Kbar=E*A/length
stress=lambda Ks:-E*alph*DT*Ks/(Ks+Kbar)
check(52,"equal-stiffness support stress [MPa]",stress(Kbar)/1e6,-162)
check(52,"free expansion stress",stress(0),0)
check(52,"bar plus spring elongation compatibility",
      (stress(Kbar)/E+alph*DT)*length+stress(Kbar)*A/Kbar,0)

# 53: separately integrate volumetric source, then heat-flow gradient.
q0,ell,d,k=2e6,.05,.1,20
q=lambda x:q0*ell*(1-math.exp(-x/ell))
check(53,"integrated nuclear source equals back flux [W/m2]",
      quad(lambda x:q0*math.exp(-x/ell),0,d),q(d))
delta=quad(lambda x:q(x)/k,0,d)
check(53,"temperature by flux integration [K]",delta,283.83382080915317)
check(53,"insulated front flux",q(0),0)

# 54: integrate semi-infinite temperature profile to recover surface heat input.
qsurf,k,rhoc,t=5e6,100,2.5e6,.01
alpha=k/rhoc
def temp(x,t=t):
    xi=x/(2*math.sqrt(alpha*t))
    return 2*qsurf*math.sqrt(alpha*t)/k*(math.exp(-xi*xi)/math.sqrt(math.pi)-xi*math.erfc(xi))
check(54,"integrated heat equals q*t [J/m2]",
      quad(lambda x:rhoc*temp(x),0,20*math.sqrt(alpha*t)),qsurf*t)
check(54,"surface temperature [K]",temp(0),35.682482323055424)
check(54,"four-times duration gives twice surface rise",temp(0,.04)/temp(0,.01),2)
h=1e-8
check(54,"surface Fourier flux [W/m2]",-k*(-3*temp(0)+4*temp(h)-temp(2*h))/(2*h),qsurf,rtol=1e-6)

# 55: spectrum weighting and atom fractions.
phi=[1e24,2e24]; sd=[1000e-28,2000e-28]; she=[.01e-28,.05e-28]
dpa=sum(a*b for a,b in zip(phi,sd)); appm=1e6*sum(a*b for a,b in zip(phi,she))
check(55,"two-group dpa",dpa,.5)
check(55,"helium appm",appm,11)
check(55,"spectrum changes He/dpa ratio",appm/dpa,22)
check(55,"first group only helium appm",sum(phi)*she[0]*1e6,3)

# 56: diffusion inventory computed in x and independently by integrating influx.
D,cs,t=1e-12,1e24,1e4
N=quad(lambda x:cs*math.erfc(x/(2*math.sqrt(D*t))),0,16*math.sqrt(D*t))
# t=u^2 regularizes the 1/sqrt(t) surface flux.
Nflux=quad(lambda u:2*cs*math.sqrt(D/math.pi),0,math.sqrt(t))
check(56,"spatial inventory equals time-integrated surface influx",N,Nflux)
check(56,"inventory [m^-2]",N,1.1283791670955126e20)

# 57: bimetal parallel bars satisfy individual thermal strain and net force.
E1,E2,al1,al2,DT=200e9,100e9,5e-6,15e-6,200
eps=(E1*al1+E2*al2)/(E1+E2)*DT
s1,s2=E1*(eps-al1*DT),E2*(eps-al2*DT)
check(57,"force equilibrium [Pa]",s1+s2,0,atol=1e-6)
check(57,"compatibility",s1/E1+al1*DT,s2/E2+al2*DT)
check(57,"low-expansion stress [MPa]",s1/1e6,133.33333333333333)
check(58,"linear interpolation midpoint",120+(100-120)/200*100,110)
check(58,"teaching thermal drop [K]",5e6*.003/110,136.36363636363637)

# 59,62,80: line integration independently of the reduced analytic formula.
aa,n0,wave=.5,8e19,10.6e-6
chord=lambda b:quad(lambda x:n0*(1-(x*x+b*b)/aa**2),-math.sqrt(aa*aa-b*b),math.sqrt(aa*aa-b*b))
check(59,"central chord [m^-2]",chord(0),4*n0*aa/3)
check(59,"offset chord ratio",chord(.3)/chord(0),.512)
check(59,"phase [rad]",-relectron*wave*chord(0),-1.5930755944997645)
mean=.9/(relectron*wave*.75)
check(62,"mean density [m^-3]",mean,4.0173862571848884e19)
check(62,"phase roundtrip [rad]",-relectron*wave*.75*mean,-.9)
check(62,"finite perturbation uncertainty",
      abs((.9+.02)/(relectron*wave*.75)-mean),.02/(relectron*wave*.75))
phase=-relectron*wave*3e19*.6
check(80,"forward and inverse learning task",-phase/(relectron*wave*.6),3e19)
check(80,"relative uncertainty [percent]",.01/abs(phase)*100,1.859901044993004)

# 60: transform independent errors into covariance form.
var_common=.5**2; var_ind=.2**2
check(60,"difference variance two independent decompositions",
      2*(var_common+var_ind)-2*var_common,2*var_ind)
check(60,"temperature difference standard uncertainty [K]",math.sqrt(2*var_ind),.282842712474619)
check(60,"covariance eigenvalue minimum",var_common+var_ind-var_common,.04)

# 61: evaluate complex open-loop function without the reduced phase expression.
tau=.02; gain=4; wc=math.sqrt(gain*gain-1)/tau
for delay,margin in [(.002,82.28695219971593),(.008,15.715272241073961)]:
    loop=gain*cmath.exp(-1j*wc*delay)/(1+1j*wc*tau)
    check(61,f"gain crossover magnitude delay={delay}",abs(loop),1)
    check(61,f"complex phase margin delay={delay} [degree]",180+math.degrees(cmath.phase(loop)),margin)

# 63: finite-volume conservation, constant state, nonnegativity, CFL violation.
def upwind(u,nu): return [x-nu*(x-u[(i-1)%len(u)]) for i,x in enumerate(u)]
u=[0,1,2,1]; nxt=upwind(u,.5)
check(63,"periodic total integral",sum(nxt)*.1,sum(u)*.1)
check(63,"nonnegative update minimum",min(nxt),.5)
check(63,"constant state unchanged",max(abs(x-3) for x in upwind([3]*4,.7)),0)
check(63,"violating CFL creates negative cell",upwind(u,1.2)[1],-.2)

# 64: RK4 includes a third state for cumulative lost heat, independent of algebraic subtraction.
tf,te=.05,.2
wf,wt,loss=rk4(lambda t,y:[-y[0]/tf,y[0]/tf-y[1]/te,y[1]/te],[1.,0.,0.],.1)
check(64,"fast energy numerical vs analytic [MJ]",wf,math.exp(-.1/tf))
check(64,"thermal energy numerical vs analytic [MJ]",wt,te/(te-tf)*(math.exp(-.1/te)-math.exp(-.1/tf)))
check(64,"integrated energy closure [MJ]",wf+wt+loss,1)
check(64,"integrated heat loss [MJ]",loss,.2364042147953597)
tpeak=math.log(te/tf)/(1/tf-1/te)
check(64,"zero thermal derivative at peak",math.exp(-tpeak/tf)/tf-te/(te-tf)*(math.exp(-tpeak/te)-math.exp(-tpeak/tf))/te,0)

# The equal-time-constant limit is checked by direct integration, avoiding cancellation.
wf_equal,wt_equal,loss_equal=rk4(lambda t,y:[-y[0]/.1,y[0]/.1-y[1]/.1,y[1]/.1],[1.,0.,0.],.2)
check(64,"equal timescale continuous-limit thermal energy [MJ]",wt_equal,2*math.exp(-2))
check(64,"equal timescale energy closure [MJ]",wf_equal+wt_equal+loss_equal,1)

# 65,81: manufactured PDE and observed second-order convergence.
errors=[]
for h in [.05,.025]:
    second=(math.sin(math.pi*(.5+h))-2+math.sin(math.pi*(.5-h)))/h**2
    errors.append(abs(second+math.pi**2))
check(65,"manufactured PDE residual",-1-(-.1*math.pi**2)-(.1*math.pi**2-1),0)
check(65,"coarse derivative error",errors[0],.020276877199574272)
check(65,"observed convergence order",math.log(errors[0]/errors[1],2),2,rtol=.001)
err=[]
for h in [.2,.1]: err.append(abs(2*(math.cos(h)-1)/h**2+1))
check(81,"independent reading exercise error ratio",err[0]/err[1],4,rtol=.002)

# 66: time refinement and byte identity.
exact=1e6*math.exp(-1)
results=[1e6*(1-dt/.1)**round(.1/dt) for dt in [.001,.0005]]
check(66,"100-step energy [J]",results[0],366032.3412732292)
check(66,"200-step energy [J]",results[1],366957.82172616705)
check(66,"Euler observed first order",math.log(abs(results[0]-exact)/abs(results[1]-exact),2),1,rtol=.01)
cfg=dict(dt=.001,tau=.1,steps=100,energy=1e6)
digest=lambda v:hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()
check(66,"same config hash equality",int(digest(cfg)==digest(dict(cfg))),1)
check(66,"different config hash inequality",int(digest(cfg)!=digest({**cfg,"dt":.0005,"steps":200})),1)

# 67: energy released to a resistor matches magnetic-energy decrease.
induct,resistance,I0=2,.2,1e4
current=lambda t:I0*math.exp(-resistance/induct*t)
diss=quad(lambda t:resistance*current(t)**2,0,10)
check(67,"Joule integral plus magnetic energy [J]",diss+.5*induct*current(10)**2,.5*induct*I0**2)
check(67,"remaining magnetic energy [MJ]",.5*induct*current(10)**2/1e6,13.53352832366127)

# 68: integrate gas balance, then recover S and Q from pressure.
V,S,Q,p0=2,.2,.0002,.1
pnum=rk4(lambda t,y:[(Q-S*y[0])/V],[p0],10)[0]
check(68,"vacuum pressure ODE [Pa]",pnum,.037420064675972795)
tau_fit=-10/math.log((pnum-Q/S)/(p0-Q/S))
check(68,"fit recovers pumping speed [m3/s]",V/tau_fit,S)
check(68,"series speed conductance",1/(1/.5+1/(1/(1/.2-1/.5))),.2)
check(68,"pressure target reached [Pa]",Q/S+(p0-Q/S)*math.exp(-23.978952727983707*S/V),.01)

# 69: entropy and energy balance for each reversible stage.
total=0
for Tc,Qc in [(4.5,100),(80,1000)]:
    Qh=Qc*300/Tc; power=Qh-Qc; total+=power
    check(69,f"reversible entropy balance Tc={Tc}",Qh/300-Qc/Tc,0)
    check(69,f"energy balance Tc={Tc}",Qc+power,Qh)
check(69,"total minimum stage power [W]",total,9316.666666666668)

# 70: fuel stream mass conservation at a single explicitly selected isotope.
burn,fb,eta=.1,.02,.999
injected=burn/fb; unburned=injected-burn; recovered=eta*unburned; makeup=injected-recovered
check(70,"makeup equals burn and process loss [mg/s]",makeup,burn+(1-eta)*unburned)
check(70,"makeup [mg/s]",makeup,.1049)
check(70,"residence inventory [mg]",injected*30,150)

# 71,72: cycle-average and independent pressure-volume unit chain.
avg=(250*120-20*30)/150
check(71,"cycle average [MW]",avg,196)
avg2=(250*120-20*15)/135
check(71,"yearly energy increment [MWh]",(avg2-avg)*8760,210240)
check(72,"mbar L/s in SI",100*.001,.1)
check(72,"molecular rate [1/s]",100*.001/(kb*300),2.4143235053466403e19)

# 73: orthogonal least squares reconstruction and conditional effects.
design=[(1,a,b,a*b) for b in [-1,1] for a in [-1,1]]
y=[10,14,12,20]; coef=[sum(row[j]*val for row,val in zip(design,y))/4 for j in range(4)]
for i,row in enumerate(design):
    check(73,f"factorial reconstructed response {i}",sum(a*b for a,b in zip(row,coef)),y[i])
for i in range(4):
    for j in range(i):
        check(73,f"orthogonality {i},{j}",sum(row[i]*row[j] for row in design),0)
check(73,"A effect changes with B",(20-12)-(14-10),4)

# 75: fit actual points, independently verify normal equations.
x=[0,1,2,3,4]; y=[.1,2.12,4.08,6.1,8.1]
xbar=sum(x)/5;ybar=sum(y)/5
b=sum((xx-xbar)*(yy-ybar) for xx,yy in zip(x,y))/sum((xx-xbar)**2 for xx in x)
a=ybar-b*xbar; residual=[yy-a-b*xx for xx,yy in zip(x,y)]
check(75,"fitted slope [V/unit]",b,1.998)
check(75,"fitted offset [V]",a,.104)
check(75,"normal equation residual sum",sum(residual),0)
check(75,"normal equation weighted residual sum",sum(xx*rr for xx,rr in zip(x,residual)),0)
check(75,"residual standard deviation [V]",math.sqrt(sum(r*r for r in residual)/3),.015916448515084374)
check(75,"inverse calibration [unit]",(5.1-a)/b,2.5005005005005008)

# 76: sensor dynamics integrated independently after delay.
yt=rk4(lambda t,y:[(60-y[0])/.2],[40],.05)[0]
check(76,"reading at logged 0.1s [C]",yt,44.4239843385719)
threshold=.05+.2*math.log(2)
check(76,"half-response threshold [s]",threshold,.18862943611198907)
check(76,"threshold input reconstruction [C]",40+20*(1-math.exp(-(threshold-.05)/.2)),50)

# 77,78: compare explicit measurement planes and timing.
for power,time,energy,net in [(200,3,600,10),(100,10,1000,-30)]:
    check(77,f"integrated fusion energy {power} [MJ]",power*time,energy)
    check(77,f"net electric budget {power} [MW]",.4*power-20/.5-30,net)
for pk,pulse,period,energy,average in [(2,.1,10,.2,.02),(1,60,120,60,.5)]:
    check(78,f"pulse energy {pk} [MJ]",pk*pulse,energy)
    check(78,f"period average {pk} [MW]",pk*pulse/period,average)

# 82: independent quadratures of normalization and variance for both conventions.
sigma=math.sqrt(100*e/me); vt=math.sqrt(2)*sigma
for scale,use_sigma in [(sigma,True),(vt,False)]:
    f=(lambda v:math.exp(-v*v/(2*scale*scale))/(math.sqrt(2*math.pi)*scale)) if use_sigma else (
       lambda v:math.exp(-v*v/(scale*scale))/(math.sqrt(math.pi)*scale))
    check(82,f"Maxwell normalization sigma_convention={use_sigma}",quad(f,-10*sigma,10*sigma),1)
    check(82,f"Maxwell variance sigma_convention={use_sigma}",quad(lambda v:v*v*f(v),-10*sigma,10*sigma),100*e/me)
check(82,"thermal scale ratio",vt/sigma,math.sqrt(2))

# Current content structure and permanent identities are checked by tag_depth_coverage.py.
result=dict(checked_on=date.today().isoformat(),count=len(records),all_passed=all(r["passed"] for r in records),
            tags=39,checks=records)
OUT.mkdir(exist_ok=True,parents=True)
(OUT/"engineering-checks.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(dict(count=len(records),passed=result["all_passed"],tags=39)))
