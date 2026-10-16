#!/usr/bin/env python3
"""Independent teaching benchmarks for the broad content expansion.

These checks integrate or reconstruct selected results independently. They do
not certify every sentence, simulate a reactor, or validate external software.
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
e = 1.602176634e-19
me = 9.1093837139e-31
md = 3.3435837768e-27
eps0 = 8.8541878188e-12
c = 299792458.0
checks = []


def close(name, actual, expected, rtol=1e-8, atol=0):
    passed = math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol)
    checks.append(dict(name=name, actual=actual, expected=expected,
                       rtol=rtol, atol=atol, passed=passed))
    if not passed:
        raise AssertionError(checks[-1])


def integrate(fn, a, b, count=20000):
    step = (b - a) / count
    return step / 3 * (fn(a) + fn(b) + sum(
        (4 if i % 2 else 2) * fn(a + i * step) for i in range(1, count)))


# Maxwell relative speed integral vs. independently reduced energy integral.
# Work in dimensionless units to make numerical tolerance meaningful.
mu, theta, cross_section = 1.2, 2.3, 0.7
speed_distribution = lambda v: 4*math.pi*v*v*(mu/(2*math.pi*theta))**1.5*math.exp(-mu*v*v/(2*theta))
limit = 12*math.sqrt(theta/mu)
close('relative-speed Maxwell normalization', integrate(speed_distribution, 0, limit), 1)
rate_v = integrate(lambda v: speed_distribution(v)*v*cross_section, 0, limit)
rate_E = math.sqrt(8/(math.pi*mu))*theta**-1.5*integrate(
    lambda energy: cross_section*energy*math.exp(-energy/theta), 0, 50*theta)
close('fusion rate: speed integral vs energy integral', rate_v, rate_E)
close('constant-cross-section analytic benchmark', rate_v, cross_section*math.sqrt(8*theta/(math.pi*mu)))
close('unordered identical reacting pairs', len([(i,j) for i in range(200) for j in range(i+1,200)]), 200*199/2)
close('fuel dilution at five percent helium/ne', ((1-2*.05)/2)**2 / (.5**2), .81)
close('cylindrical density-product integral', integrate(lambda r: 2*r*(1-r*r)**2, 0, 1), 1/3)
close('transient loss-based confinement time [s]', 20e6/(15e6-5e6), 2)

# Derive the Lawson threshold by balancing power at the proposed n*tau.
theta, reactivity, alpha_energy, fusion_energy = 15e3*e, 2e-22, 3.5e6*e, 17.6e6*e
density, deposited = 1e20, .8
for gain in (1, 5, 10, 1e12):
    n_tau = 12*theta/(reactivity*(deposited*alpha_energy+fusion_energy/gain))
    loss = 3*density*theta/(n_tau/density)
    fusion_rate = density*density*reactivity/4
    heat = fusion_rate*(deposited*alpha_energy+fusion_energy/gain)
    close(f'finite-gain Lawson power balance Q={gain:g}', loss, heat)
close('Q=10 approximate alpha heating fraction', (10/5)/(1+10/5), 2/3)
ne, Te_eV = 1e20, 1e4
br_cgs_to_si = 1.69e-32*(ne/1e6)**2*math.sqrt(Te_eV)*1e6
close('bremsstrahlung cgs-to-SI [W/m3]', br_cgs_to_si, 16900)
close('steady ash inventory [particles]', 1e19*5, 5e19)
close('net electricity illustrative budget [MW]', .4*500-50/.5-70, 30)
close('net electricity lower heating efficiency [MW]', .4*500-50/.3-70, -36.66666666666667)

# Cylindrical source solution: integrate source independently of boundary flux.
S, D, radius, length = 3.2, .8, 1.7, 2.4
source = integrate(lambda r: S*2*math.pi*r*length, 0, radius)
dr = 1e-5
profile = lambda r: 2 + S*(radius*radius-r*r)/(4*D)
flux = -D*(profile(radius+dr)-profile(radius-dr))/(2*dr)
close('cylindrical boundary flux equals integrated source', flux*2*math.pi*radius*length, source)

# Use periodic samples of n and ExB velocity; check phase and radial sign.
N, k, Phi, B = 2.1, 1.7, .4, 2.3
for phase in (0, math.pi/6, -math.pi/2):
    flux = integrate(lambda y: N*math.cos(k*y)*k*Phi/B*math.sin(k*y+phase),
                     0, 2*math.pi/k)/(2*math.pi/k)
    close(f'turbulent cross-phase flux delta={phase:g}', flux, N*k*Phi/(2*B)*math.sin(phase), atol=1e-12)

# Solve parallel conduction ODE by RK4 from the target toward the upstream.
# theta_t=1, kappa=q=L=1; the endpoint must be (9/2)^(2/7).
T, ds = 1.0, 1/10000
for _ in range(10000):
    f = lambda v: v**-2.5
    a=f(T); b=f(T+ds*a/2); cc=f(T+ds*b/2); d=f(T+ds*cc)
    T += ds*(a+2*b+2*cc+d)/6
close('two-point model ODE vs integrated endpoint', T, (9/2)**(2/7))
for s in (.1, .5, .9):
    profile=lambda x:(4.5-3.5*x)**(2/7)
    derivative=(profile(s+1e-5)-profile(s-1e-5))/(2e-5)
    close(f'two-point profile local heat flux at s={s}', -profile(s)**2.5*derivative, 1)

# Bohm speed, floating potential and electron Maxwell flux reconstructed.
Theta = 10*e
cs = math.sqrt(Theta/md)
drop = Theta/(2*e)*math.log(md/(2*math.pi*me))
close('D Bohm speed at Te=10 eV [m/s]', cs, 2.19e4, rtol=.002)
close('D floating wall potential drop [V]', drop, 31.9, rtol=.002)
vscale=math.sqrt(Theta/me)
electron_flux=integrate(lambda v:v*math.exp(-v*v/(2*vscale*vscale))/(math.sqrt(2*math.pi)*vscale),
                        0, 12*vscale)
close('floating-wall current balance from integrated electrons', electron_flux*math.exp(-e*drop/Theta), cs)

# Interferometry: exact cold-plasma index vs its high-frequency expansion.
probe_frequency, density, path = 3e13, 3e19, 1.3
omega=2*math.pi*probe_frequency
wp2=density*e*e/(eps0*me)
# Rationalized sqrt(1-x)-1 avoids cancellation in the exact expression.
phase_exact=omega/c*path*(-wp2/omega**2)/(math.sqrt(1-wp2/omega**2)+1)
re=e*e/(4*math.pi*eps0*me*c*c)
phase_approx=-re*c/probe_frequency*density*path
close('interferometer high-frequency phase and sign', phase_exact, phase_approx, rtol=1e-6)

close('transient energy accumulation [MJ]', (5-4)*.20, .20)
close('coolant calorimetry [kW]', .5*4.18*2, 4.18)
close('standard error of independent mean [kW]', .20/math.sqrt(25), .040)
close('combined independent uncertainty [kW]', math.hypot(.040,.030), .050)
close('JET announced energy/time mean [MW]', 69/5, 13.8)

# Correlated uncertainty: transform two independent unit-variance variables.
# x=2z1, y=.9z1+1.2z2 yields cov(x,y)=1.8, var(y)=2.25.
covariance_form=4+2.25+2*1.8
independent_form=(2+.9)**2+1.2**2
close('covariance propagation vs independent-variable reconstruction', covariance_form, independent_form)

out = dict(date='2026-10-16', count=len(checks), all_passed=all(x['passed'] for x in checks),
           scope='Selected synthetic teaching benchmarks, not reactor validation or specialist certification',
           checks=checks)
dest=ROOT/'.build/reviews/expansion-benchmarks.json'
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(checks=out['count'], passed=out['all_passed'], report=str(dest))))
