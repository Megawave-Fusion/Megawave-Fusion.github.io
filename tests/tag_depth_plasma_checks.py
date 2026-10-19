#!/usr/bin/env python3
"""Independent quadrature, orbit, differential and conservation checks for 50 plasma Tags.

Run: python3 tests/tag_depth_plasma_checks.py --report .build/tag-depth/plasma-test-results.json
All examples are specified teaching models. Stdlib only; no network or website mutation.
"""
import argparse
import cmath
import json
import math
from pathlib import Path

E = 1.602176634e-19
ME = 9.1093837139e-31
MD = 3.3435837768e-27
EP = 8.8541878188e-12
MU = 1.25663706127e-6
C = 299792458.0
HB = 1.054571817e-34
PI = math.pi
RESULTS = []
CHECKS = []


def simpson(f, a, b, n=4096):
    assert n % 2 == 0
    h = (b-a)/n
    return h/3 * (f(a)+f(b)+sum((4 if i % 2 else 2)*f(a+i*h) for i in range(1,n)))


def der(f,x,h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)


def der2(f,x,h=1e-4):
    return (f(x+h)-2*f(x)+f(x-h))/h**2


def rk4(f,y,tend,n=4000):
    y=list(y); h=tend/n; t=0.0
    for _ in range(n):
        k1=f(t,y)
        k2=f(t+h/2,[v+h*w/2 for v,w in zip(y,k1)])
        k3=f(t+h/2,[v+h*w/2 for v,w in zip(y,k2)])
        k4=f(t+h,[v+h*w for v,w in zip(y,k3)])
        y=[v+h*(a+2*b+2*c+d)/6 for v,a,b,c,d in zip(y,k1,k2,k3,k4)]
        t+=h
    return y


def close(a,b,rtol=1e-8,atol=1e-11):
    assert abs(a-b) <= atol+rtol*abs(b), (a,b,abs(a-b))


def check(key):
    def register(f):
        CHECKS.append((key,f))
        return f
    return register


def gaussian(x):
    return math.exp(-x*x/2)/math.sqrt(2*PI)


def moment(k):
    return simpson(lambda x:x**k*gaussian(x),-12,12)


@check("unit")
def unit():
    # Integrate a shifted distribution; do not substitute equipartition into itself.
    u=math.sqrt(0.6)
    kin=0.5*simpson(lambda x:(x+u)**2*gaussian(x),-12,12)+moment(2)
    close(kin,1.8)
    return {"mean_energy_eV":kin*250,"gaussian_normalization":moment(0),
            "temperature_K":250*E/1.380649e-23}


@check("anisotropic")
def anisotropic():
    perp=2e19*300*E*moment(2); par=2e19*900*E*moment(2)
    close(perp,961.3059804)
    return {"Pperp_Pa":perp,"Pparallel_Pa":par,"internal_J_m3":(2*perp+par)/2}


@check("sinphi")
def sinphi():
    k=2*PI/.02; phi=lambda x:20*math.cos(k*x)
    # Spatial numerical differentiation and Poisson's equation.
    rho=-EP*der2(phi,0,1e-7)
    close(rho,EP*20*k*k,rtol=1e-6)
    electric=-der(phi,.005,1e-7)
    close(electric,20*k,rtol=1e-7)
    return {"rho_C_m3":rho,"relative_charge":rho/(1e19*E),"E_V_m":electric}


@check("shield")
def shield():
    # In units lambda_D=1 and Q/(4 pi eps0)=1.
    phi=lambda r:math.exp(-r)/r
    q=-3**2*der(phi,3)
    shell=simpson(lambda r:-r*math.exp(-r),1,3)
    close(q,4*math.exp(-3))
    close(shell,4*math.exp(-3)-2/math.e)
    return {"Qenclosed_over_Q":q,"Qshell_1_to_3_over_Q":shell}


@check("collective")
def collective():
    def nd(n,theta):
        length=math.sqrt(EP*theta/(n*E**2))
        return length,4*PI*n*length**3/3
    l0,n0=nd(1e19,200*E); l1,n1=nd(8e19,800*E)
    close(n1/n0,math.sqrt(8))
    close(l1/l0,1/math.sqrt(2))
    return {"lambda0_m":l0,"ND0":n0,"ND_adiabatic_final":n1}


@check("mobile")
def mobile():
    ratio=ME/MD
    # Normalized two-species slabs: xi''=-r(xi-xe), xe''=xi-xe.
    state=rk4(lambda t,y:[y[2],y[3],-ratio*(y[0]-y[1]),y[0]-y[1]],
              [1,0,0,0],2*PI/math.sqrt(1+ratio))
    close(state[0],1,rtol=1e-10);close(state[1],0,atol=1e-10)
    energy=lambda y:.5*y[2]**2/ratio+.5*y[3]**2+.5*(y[0]-y[1])**2
    close(energy(state),.5)
    return {"frequency_shift_fraction":math.sqrt(1+ratio)-1,
            "normalized_energy_residual":energy(state)-.5,
            "energy_J_m3":(1e18*E*1e-6)**2/(2*EP)}


@check("flux")
def flux():
    half=simpson(lambda v:v*gaussian(v),0,12)
    speed=math.sqrt(20*E/ME)
    value=1e18*speed*half
    close(half,1/math.sqrt(2*PI))
    return {"particle_flux_m2_s":value,"current_A_m2":E*value}


@check("magnetization")
def magnetization():
    ot=E*.1/MD*1e-6
    correlation=simpson(lambda t:math.exp(-t)*math.cos(ot*t),0,40,32768)
    expected=1/(1+ot**2)
    close(correlation,expected,rtol=1e-8)
    return {"Omega_tau":ot,"correlation_integral":correlation,
            "Dperp_m2_s":10*E*1e-6/MD*correlation}


@check("work")
def work():
    a=E*50/MD
    z,v=rk4(lambda t,y:[y[1],a],[0,2e4],2e-6,200)
    kinetic=MD*(v*v-(2e4)**2)/(2*E)
    close(kinetic,50*z,rtol=1e-10)
    return {"z_m":z,"vz_m_s":v,"deltaK_eV":kinetic,"qE_dz_eV":50*z}


@check("gyro")
def gyro():
    # qB/m=1, v_perp=1; integrate Cartesian Lorentz equation.
    x,y,vx,vy=rk4(lambda t,s:[s[2],s[3],s[3],-s[2]],
                  [0,0,1,0],PI/2,2000)
    close(x,1);close(y,-1);close(vx*vx+vy*vy,1)
    omega=E*.8/MD;rho=2e5/omega
    return {"quarter_orbit_x_m":x*rho,"quarter_orbit_y_m":y*rho,
            "quarter_time_s":PI/(2*omega),"speed_squared_error":vx*vx+vy*vy-1}


@check("trochoid")
def trochoid():
    # normalized E/B=1; check net drift over gyroperiod.
    def rhs(t,s):return [s[2],s[3],1+s[3],-s[2]]
    end=rk4(rhs,[0,0,0,0],2*PI)
    mid=rk4(rhs,[0,0,0,0],PI,2000)
    close(end[1],-2*PI);close(mid[0],2)
    close(.5*(mid[2]**2+mid[3]**2),mid[0])
    scale=5000/(E*.4/MD)
    return {"net_dy_m":end[1]*scale,"x_half_m":mid[0]*scale,
            "work_energy_normalized_residual":.5*(mid[2]**2+mid[3]**2)-mid[0]}


@check("gradB")
def gradB():
    # Full inhomogeneous orbit, not guiding-center equations.
    eps=.004
    def rhs(t,s):
        b=1+eps*s[0]
        return [s[2],s[3],b*s[3],-b*s[2]]
    times=40*PI
    end=rk4(rhs,[0,0,1,0],times,40000)
    # GC_y=y+vx/B removes the dominant gyrophase endpoint displacement.
    gc0=1
    gc1=end[1]+end[2]/(1+eps*end[0])
    drift=(gc1-gc0)/times
    close(drift,eps/2,rtol=2e-3)
    close(end[2]**2+end[3]**2,1,rtol=1e-8)
    return {"full_orbit_drift_normalized":drift,"first_order_drift":eps/2,
            "relative_difference":drift/(eps/2)-1,"SI_example_m_s":500.0}


@check("curv")
def curv():
    # Differentiate unit e_phi along an actual circular field line.
    phi=.4;R=1.5
    ex=lambda s:-math.sin(phi+s/R)
    ey=lambda s:math.cos(phi+s/R)
    kap=(der(ex,0),der(ey,0))
    close(kap[0],-math.cos(phi)/R);close(kap[1],-math.sin(phi)/R)
    vz=(400+2*800)/(1.2*R)
    return {"curvature_m_inverse":math.hypot(*kap),"drift_m_s":vz,"dz_20us_m":vz*2e-5}


@check("betatron")
def betatron():
    # Integrate Lorentz motion with Faraday E=(-Bdot/2) ez cross r.
    # Dimensionless B increases from 1 to 3 in 2000 initial cyclotron times.
    duration=2000.;bdot=2/duration
    def rhs(t,s):
        x,y,vx,vy=s;b=1+bdot*t
        return [vx,vy,.5*bdot*y+vy*b,-.5*bdot*x-vx*b]
    end=rk4(rhs,[1,0,0,-1],duration,200000)
    ratio=end[2]**2+end[3]**2
    close(ratio,3,rtol=8e-4)
    return {"orbit_final_perp_eV":300*ratio,"adiabatic_limit_eV":900,
            "orbit_mu_relative_change":ratio/3-1}


@check("mirror")
def mirror():
    omega=math.sqrt(2*1000*E/(MD*.5**2))
    s,v=rk4(lambda t,y:[y[1],-y[0]],[0,1],PI/2,2000)
    close(s,1);close(v,0)
    return {"turning_s_m":s*.5,"bounce_period_s":2*PI/omega,
            "energy_normalized":s*s+v*v}


@check("action")
def action():
    # Phase-space contour integral under harmonic orbit: p dq integrated over phase.
    m=MD;om=math.sqrt(2*1000*E/(m*.5**2));a=.5
    val=simpson(lambda ph:m*om*a*a*math.cos(ph)**2,0,2*PI)
    close(val,2*PI*1000*E/om,atol=1e-30)
    a1=a*math.sqrt(2/3);om1=1.5*om
    val1=simpson(lambda ph:m*om1*a1*a1*math.cos(ph)**2,0,2*PI)
    close(val1,val,atol=1e-30)
    return {"action_J_s":val,"final_turn_m":a1,"final_parallel_eV":1500.0}


@check("mixture")
def mixture():
    sig=math.sqrt(100*E/MD);U=5e5;u=.2*U
    # Quadrature in component-centered coordinates avoids losing a narrow Gaussian.
    m2=m3=0.
    for weight,center in ((.8,0),(.2,U)):
        m2+=weight*simpson(lambda x:(center+sig*x-u)**2*gaussian(x),-12,12)
        m3+=weight*simpson(lambda x:(center+sig*x-u)**3*gaussian(x),-12,12)
    q=.5*MD*1e18*m3
    close(q,20061502.6608,rtol=1e-9)
    return {"Pxx_Pa":MD*1e18*m2,"heat_flux_W_m2":q}


@check("stream")
def stream():
    # k sigma t=1; direct velocity integration of the translated initial data.
    density=simpson(lambda v:gaussian(v)*(1+.1*math.cos(-v)),-12,12)
    flux=simpson(lambda v:v*gaussian(v)*(1+.1*math.cos(PI/2-v)),-12,12)
    close(density-1,.1*math.exp(-.5))
    close(flux,.1*math.exp(-.5))
    return {"density_amplitude":density-1,"quadrature_flow_m_s":flux*1e4}


@check("tail")
def tail():
    fn=simpson(lambda x:4/math.sqrt(PI)*x*x*math.exp(-x*x),2,12)
    fe=simpson(lambda x:8/(3*math.sqrt(PI))*x**4*math.exp(-x*x),2,12)
    close(fn,.04601170568923137)
    close(fe,.15623562757772233)
    return {"tail_number":fn,"tail_energy":fe,"conditional_mean_over_theta":1.5*fe/fn}


@check("compression")
def compression():
    n,p=rk4(lambda t,y:[-y[0],-5*y[1]/3],[1,1],.3,2000)
    close(n,math.exp(-.3));close(p/n,math.exp(-.2))
    # Velocity integration by parts: integral v F'=-1 and v^3 F'=-3.
    a=simpson(lambda v:v*der(gaussian,v),-10,10)
    b=simpson(lambda v:v**3*der(gaussian,v),-10,10)
    close(a,-1);close(b,-3)
    return {"n_ratio":n,"temperature_ratio":p/n,"moment_vFp":a,"moment_v3Fp":b}


@check("closure")
def closure():
    q1=rk4(lambda t,y:[1-y[0]],[0],1,1000)[0]
    q3=rk4(lambda t,y:[1-y[0]],[0],3,3000)[0]
    close(q1,1-math.exp(-1));close(q3,1-math.exp(-3))
    return {"q_at_tau_over_qF":q1,"q_at_3tau_over_qF":q3,
            "harmonic_phase_rad":cmath.phase(1/(1-1j))}


@check("rutherford")
def rutherford():
    reduced=ME*MD/(ME+MD);b90=E*E/(4*PI*EP*reduced*(3e6)**2)
    th0=2*math.atan(.5)
    # Integrate differential angular cross section over the scattering cone.
    normalized=simpson(lambda th:2*PI*math.sin(th)/(4*math.sin(th/2)**4),th0,PI)
    close(normalized,4*PI,rtol=1e-8)
    return {"b90_m":b90,"theta_deg":math.degrees(th0),"crosssection_m2":normalized*b90*b90}


@check("log")
def coulomb_log():
    theta=100*E;g=math.sqrt(2*theta/ME)
    ld=math.sqrt(EP*theta/(1e19*E**2))
    classical=E**2/(4*PI*EP*ME*g*g);quantum=HB/(2*ME*g)
    bmin=max(classical,quantum)
    # Map b geometrically: direct integral of db/b with b=bmin exp(s).
    ln=simpson(lambda s:1.,0,math.log(ld/bmin))
    middle=math.sqrt(ld*bmin)
    close(math.log(middle/bmin),math.log(ld/middle))
    return {"bclassical_m":classical,"bquantum_m":quantum,"lnLambda":ln,"midpoint_m":middle}


@check("pitch")
def pitch():
    p1=lambda x:x;p2=lambda x:(3*x*x-1)/2
    def op(f,x):return .5*((1-x*x)*der2(f,x)-2*x*der(f,x))
    err1=max(abs(op(p1,x)+p1(x)) for x in [-.9,-.3,.2,.8])
    err2=max(abs(op(p2,x)+3*p2(x)) for x in [-.9,-.3,.2,.8])
    assert err1<1e-7 and err2<1e-7
    close(simpson(lambda x:p1(x),-1,1),0)
    close(simpson(lambda x:p2(x),-1,1),0)
    return {"l1_decay":math.exp(-1),"l2_decay":math.exp(-3),
            "angular_operator_max_error":max(err1,err2)}


@check("exchange")
def exchange():
    te,ti=rk4(lambda t,y:[-50*(y[0]-y[1]),50*(y[0]-y[1])],[10,1],.01,1000)
    close(te+ti,11)
    close(te-ti,9/math.e)
    return {"Te_keV":te,"Ti_keV":ti,"temperature_sum_keV":te+ti}


@check("OU")
def ou():
    # Integrate a differential collision operator over v and compare its moments.
    f=lambda v:math.exp(-(v-2)**2/8)/math.sqrt(8*PI)
    operator=lambda v:f(v)+v*der(f,v)+der2(f,v)
    rates=[simpson(lambda v,j=j:v**j*operator(v),-20,24,12000) for j in range(3)]
    close(rates[0],0,atol=1e-7);close(rates[1],-2,rtol=1e-7)
    close(rates[2],-14,rtol=1e-7)
    mean,second=rk4(lambda t,y:[-y[0],-2*(y[1]-1)],[2,8],1,1000)
    return {"operator_moment_rates":rates,"mean_at_tau":mean,"variance_at_tau":second-mean**2,
            "second_at_tau":second}


@check("BGKheat")
def bgk_heat():
    # Separable 3D Gaussian moments calculated by one-dimensional quadrature.
    m2,m4,m6=moment(2),moment(4),moment(6)
    x2v2=m4+2*m2*m2
    x2v4=m6+2*m2*m4+4*m4*m2+2*m2**3
    close(x2v2,5);close(x2v4,35)
    coefficient=.25*x2v4-1.25*x2v2
    close(coefficient,2.5)
    q=-coefficient*1e18*(20*E)*1e-7/ME*(2*E)
    return {"fourth_moment":x2v2,"sixth_moment":x2v4,"q_W_m2":q}


@check("screenlog")
def screenlog():
    # Log-coordinate quadrature resolves both the screened and unscreened intervals.
    integral=simpson(lambda s:math.exp(4*s)/(1+math.exp(2*s))**2,-25,math.log(100),16384)
    exact=.5*(math.log(10001)+1/10001-1)
    close(integral,exact)
    return {"screened_integral":integral,"hard_cutoff_log":math.log(100)}


@check("linear")
def linear():
    # Projection onto sin(2x) isolates the nonlinear harmonic.
    nonlinear=lambda x:math.cos(x)*der(math.cos,x)
    harmonic=simpson(lambda x:nonlinear(x)*math.sin(2*x),0,2*PI)/PI
    close(harmonic,-.5)
    return {"second_harmonic_m_s2":abs(harmonic)*20*100**2,"relative_to_linear":.01,
            "Burgers_crossing_s":1/(20*100)}


@check("dielectric")
def dielectric():
    eps=1-1/(2*(2+.1j))
    refr=cmath.sqrt(eps)
    close(refr*refr,eps)
    assert refr.imag>0
    return {"epsilon":[eps.real,eps.imag],"index":[refr.real,refr.imag],
            "amplitude_lambda0":math.exp(-2*PI*refr.imag),
            "energy_lambda0":math.exp(-4*PI*refr.imag)}


@check("BG")
def bg():
    m1=simpson(lambda v:v*der(gaussian,v),-12,12)
    m3=simpson(lambda v:v**3*der(gaussian,v),-12,12)
    close(m1,-1);close(m3,-3)
    a=.15;omega=math.sqrt(1-m3*a*a)
    return {"moment_vFp":m1,"moment_v3Fp":m3,"omega_over_wp":omega,
            "vphase_over_sigma":omega/a,"vgroup_over_sigma":-m3*a/omega}


@check("ion")
def ion():
    # Normalize cs=lambdaD=1, solve fluid continuity/momentum and Poisson residuals.
    k=.5;w=k/math.sqrt(1+k*k);phi=.01
    ne=phi;ni=k*k*phi/(w*w);u=k*phi/w
    close(w*ni,k*u);close(w*u,k*phi);close(ni-ne,k*k*phi)
    vg=der(lambda k:k/math.sqrt(1+k*k),k)
    return {"phase_m_s":w/k*1e5,"group_m_s":vg*1e5,"ne1_ni1":ne/ni}


@check("EM")
def electromagnetic():
    wp=math.sqrt(2e18*E*E/(EP*ME));w=2*PI*1e10
    alpha=math.sqrt(wp*wp-w*w)/C;skin=1/alpha
    # Differential Maxwell/Helmholtz residual on evanescent envelope.
    f=lambda x:math.exp(-x)
    close(der2(f,.7),f(.7),rtol=1e-7)
    return {"fpe_Hz":wp/(2*PI),"skin_m":skin,"amplitude_1cm":math.exp(-.01/skin)}


@check("whistler")
def whistler():
    wp=math.sqrt(1e18*E*E/(EP*ME));oc=E*.2/ME
    de=C/wp;k=.1/de
    disp=lambda k:oc*de*de*k*k
    vg=der(disp,k,h=k*1e-5)
    close(vg,2*disp(k)/k)
    return {"de_m":de,"omega_rad_s":disp(k),"vg_m_s":vg,"phase_m_s":disp(k)/k}


@check("OX")
def ox():
    w=.5;wp=.6;R=1-wp*wp/(w*(w-1));L=1-wp*wp/(w*(w+1))
    S=(R+L)/2;D=(R-L)/2;n2=R*L/S
    close(S*(S-n2)-D*D,0)
    cut=(math.sqrt(1+4*wp*wp)-1)/2
    close(1-wp*wp/(cut*(cut+1)),0)
    return {"R":R,"L":L,"X_N2":n2,"O_N2":1-wp*wp/w**2,"lower_cutoff_over_Omega":cut}


@check("MHDwaves")
def mhd_waves():
    aa=4+.5;bb=.5;dd=.5
    eigen=[(5+math.sqrt(17))/2,(5-math.sqrt(17))/2]
    for l in eigen:close((aa-l)*(dd-l)-bb*bb,0)
    close(eigen[0]*eigen[1],2)
    return {"fast_m_s":math.sqrt(eigen[0])*1e6,"slow_m_s":math.sqrt(eigen[1])*1e6,
            "shear_m_s":math.sqrt(2)*1e6,"eigenvalue_product":math.prod(eigen)}


@check("group")
def group():
    disp=lambda k:math.sqrt(1+k*k)
    v=der(disp,.75);second=der2(disp,.75)
    close(v,.6);close(second,.512,rtol=1e-6)
    # Integrate the quadratic-dispersion packet at its center; t chosen a=1.
    integ=simpson(lambda q:cmath.exp(-q*q/2-1j*q*q/2),-12,12)
    ratio=abs(integ)/math.sqrt(2*PI)
    close(ratio,2**(-.25))
    return {"vg_over_c":v,"normalized_second_derivative":second,
            "packet_peak_ratio_at_sqrt2_width":ratio,"normalized_spread_time":1/(.512*.02**2)}


def plasma_z(z,n=8192):
    # Entire continuation, obtained by solving Z'=-2(1+zZ), Z(0)=i sqrt(pi).
    return 1j*math.sqrt(PI)*cmath.exp(-z*z)-2*z*simpson(
        lambda s:cmath.exp(-z*z*(1-s*s)),0,1,n)


def langmuir_root(a,n=8192):
    w=complex(math.sqrt(1+3*a*a),-6.5e-5)
    for _ in range(12):
        z=w/(math.sqrt(2)*a);Z=plasma_z(z,n)
        eps=1+(1+z*Z)/(a*a)
        dz=-2*(1+z*Z)
        de=(Z+z*dz)/(a*a*math.sqrt(2)*a)
        dw=eps/de;w-=dw
        if abs(dw)<1e-13:break
    return w,abs(1+(1+w/(math.sqrt(2)*a)*plasma_z(w/(math.sqrt(2)*a),n))/(a*a))


@check("Landau")
def landau():
    w,res=langmuir_root(.2)
    wcoarse,_=langmuir_root(.2,4096)
    assert res<1e-10
    close(w,wcoarse,rtol=1e-8)
    gamma=-math.sqrt(PI/8)*.2**-3*math.exp(-1/(2*.2**2)-1.5)
    assert w.imag<0 and abs(w.imag/gamma-1)<.3
    return {"full_root_real_over_wp":w.real,"full_root_imag_over_wp":w.imag,
            "dielectric_residual":res,"quadrature_refinement_difference":abs(w-wcoarse),
            "asymptotic_gamma_over_wp":gamma,"asymptotic_relative_error":gamma/w.imag-1,
            "asymptotic_amplitude_1000":math.exp(1000*gamma)}


@check("Bessel")
def bessel():
    def fourier(l):
        return simpson(lambda t:cmath.exp(1j*(.2*math.sin(t)-l*t)),0,2*PI,8192)/(2*PI)
    coeff=[fourier(l) for l in range(13)]
    for val in coeff:assert abs(val.imag)<1e-12
    normalization=abs(coeff[0])**2+2*sum(abs(v)**2 for v in coeff[1:])
    close(normalization,1)
    close(coeff[1].real,.09950083263923601)
    return {"J0":coeff[0].real,"J1":coeff[1].real,"J2":coeff[2].real,
            "sum_Jl_squared_l_le_12":normalization,"weight_ratio":abs(coeff[2]/coeff[1])**2}


@check("power")
def power():
    ef=[3+0j,4j,0j];sig=[2+3j,1+4j,0j]
    jf=[s*v for s,v in zip(sig,ef)]
    average=simpson(lambda t:sum((j*cmath.exp(-1j*t)).real*(e*cmath.exp(-1j*t)).real
                                 for j,e in zip(jf,ef)),0,2*PI)/(2*PI)
    close(average,17)
    return {"direct_time_average_W_m3":average,"phasor_average_W_m3":
            .5*sum((j*e.conjugate()).real for j,e in zip(jf,ef))}


@check("twofluid")
def twofluid():
    n=1e19;J=1e6;u=1e4;M=MD+ME;w=J/(E*n)
    ui=u+ME/M*w;ue=u-MD/M*w
    direct=.5*n*(MD*ui*ui+ME*ue*ue)
    bulk=.5*n*M*u*u;relative=.5*n*MD*ME/M*w*w
    close(direct,bulk+relative)
    close(E*n*(ui-ue),J)
    close((MD*ui+ME*ue)/M,u)
    return {"ui_m_s":ui,"ue_m_s":ue,"relative_energy_J_m3":relative,
            "energy_identity_error":direct-bulk-relative}


@check("adiabatic")
def adiabatic():
    v0=.001;v1=v0/8;p0=2000;gamma=5/3
    work=simpson(lambda v:-p0*(v0/v)**gamma,v0,v1,16384)
    u0=p0*v0/(gamma-1);p1=p0*(v0/v1)**gamma;u1=p1*v1/(gamma-1)
    close(work,u1-u0)
    return {"work_pressure_integral_J":work,"U0_J":u0,"U1_J":u1,"p1_Pa":p1}


@check("Hall")
def hall():
    n=1e19;b=.5;l=.1
    va=b/math.sqrt(MU*n*MD);j=b/(MU*l)
    eh=j*b/(E*n);ec=va*b;di=math.sqrt(MD/(MU*n*E*E))
    close(eh/ec,di/l)
    return {"Hall_field_V_m":eh,"convective_field_V_m":ec,"di_m":di,"ratio":eh/ec}


@check("slab")
def slab():
    b=lambda x:math.sqrt(1-x*x/.25)
    p=lambda x:1e4+x*x/(2*MU*.25)
    x=.15;j=-der(b,x)/MU
    grad=der(p,x)
    close(j*b(x),grad,rtol=1e-8)
    total=lambda x:p(x)+b(x)**2/(2*MU)
    close(total(.15),total(.25))
    return {"B_T":b(x),"p_Pa":p(x),"pressure_gradient_Pa_m":grad,"JcrossB_N_m3":j*b(x)}


@check("fluxfreeze")
def flux_freeze():
    lengths=[.5,1,2];b0=[1,0,1];jac=math.prod(lengths)
    b=[lengths[i]*b0[i]/jac for i in range(3)]
    flux=[b[i]*math.prod(lengths[j] for j in range(3) if j!=i) for i in range(3)]
    for actual,expected in zip(flux,b0):close(actual,expected)
    return {"B_T":b,"face_flux_factors":flux,"volume_ratio":jac,
            "magnetic_energy_ratio":sum(v*v for v in b)/2}


@check("diffusion")
def diffusion():
    amp=.1;k=2*PI/.2;eta=1e-6;dm=eta/MU
    energy=simpson(lambda x:(amp*math.sin(k*x))**2/(2*MU),0,.2)/.2
    heat=simpson(lambda x:eta*(der(lambda y:amp*math.sin(k*y),x,1e-7)/MU)**2,0,.2)/.2
    rate=2*dm*k*k*energy
    close(heat,rate,rtol=1e-8)
    return {"initial_magnetic_J_m3":energy,"Ohmic_W_m3":heat,"minus_dWdt_W_m3":rate,
            "amplitude_tau_s":1/(dm*k*k),"energy_at_tau_J_m3":energy*math.exp(-2)}


@check("GS")
def grad_shafranov():
    A=.01;cc=.02;R=1;Z=.3
    psi=lambda r,z:A*r**4+cc*z*z
    radial=lambda r:psi(r,Z);vertical=lambda z:psi(R,z)
    lhs=der2(radial,R)-der(radial,R)/R+der2(vertical,Z)
    pp=-8*A/MU;ffp=-2*cc
    rhs=-MU*R*R*pp-ffp
    close(lhs,rhs,rtol=1e-7)
    # Independent full vector force balance, using analytic curl B components.
    val=psi(R,Z);F=math.sqrt(.25-4*cc*val);Fp=-2*cc/F
    br=-2*cc*Z/R;bz=4*A*R*R;bphi=F/R
    jr=Fp*br/MU;jz=Fp*bz/MU;jphi=-(8*A*R*R+2*cc)/(MU*R)
    force_r=jphi*bz-jz*bphi;force_z=jr*bphi-jphi*br
    close(force_r,pp*4*A*R**3);close(force_z,pp*2*cc*Z)
    return {"psi_Wb":val,"finite_difference_Delta":lhs,"RHS":rhs,
            "Jphi_A_m2":jphi,"force_balance_R":force_r,"force_balance_Z":force_z}


@check("energy")
def energy():
    def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
    dot=lambda a,b:sum(x*y for x,y in zip(a,b))
    u=[1000,0,0];b=[0,0,1];j=[0,1e4,0];eta=1e-7
    electric=[-x+eta*y for x,y in zip(cross(u,b),j)]
    field=dot(j,electric);mechanical=dot(u,cross(j,b));heat=eta*dot(j,j)
    close(field,mechanical+heat)
    return {"E_V_m":electric,"JE_W_m3":field,"mechanical_W_m3":mechanical,"heat_W_m3":heat}


@check("energyprinciple")
def energy_principle():
    b=.2;rho=MD*1e19;L=10;area=.01;amp=.001
    displacement=lambda z:amp*math.sin(PI*z/L)
    inertia=rho*area*simpson(lambda z:displacement(z)**2,0,L)
    dw=b*b*area/(2*MU)*simpson(lambda z:der(displacement,z)**2,0,L)
    omega=math.sqrt(2*dw/inertia);expected=b/math.sqrt(MU*rho)*PI/L
    close(omega,expected,rtol=1e-8)
    return {"deltaW_J":dw,"inertia_kg_m2":inertia,"omega_rad_s":omega}


@check("SP")
def sweet_parker():
    b=.1;n=1e22;l=1;eta=1e-4;dm=eta/MU
    va=b/math.sqrt(MU*n*MD);S=l*va/dm
    # Solve the two balance equations in logarithmic variables via Newton iteration.
    x,y=math.log(.1),math.log(1000.)
    for _ in range(3):
        f1=y+math.log(l)-math.log(va)-x
        f2=y+x-math.log(dm)
        dy=-(f1+f2)/2;dx=(f1-f2)/2;x+=dx;y+=dy
    delta,vin=math.exp(x),math.exp(y)
    close(vin*l,va*delta)
    close(vin*b,eta*b/(MU*delta))
    return {"S":S,"delta_m":delta,"vin_m_s":vin,"E_V_m":vin*b,
            "delta_over_di":delta/math.sqrt(MD/(MU*n*E*E))}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--report",type=Path)
    args=parser.parse_args()
    for key,func in CHECKS:
        try:
            results=func()
            RESULTS.append({"key":key,"status":"pass","method":func.__name__,"results":results})
        except Exception as exc:
            RESULTS.append({"key":key,"status":"fail","method":func.__name__,"error":str(exc)})
    assert len(RESULTS)==50, len(RESULTS)
    out={"checks":RESULTS,"passed":sum(x["status"]=="pass" for x in RESULTS),"total":len(RESULTS)}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(out,ensure_ascii=False,indent=2))
    if out["passed"]!=50:raise SystemExit(1)


if __name__=="__main__":
    main()

