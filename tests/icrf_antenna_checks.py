#!/usr/bin/env python3
"""Independent Fourier/time quadratures and limiting cases of ICRF teaching models."""
import cmath
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from icrf_antenna_examples import current_spectrum, accepted_power, power_waves, conjugate_t, matvec

checks=[]

def check(name,value,expected,rtol=1e-9,atol=1e-9):
    passed=abs(value-expected)<=atol+rtol*abs(expected)
    checks.append(dict(name=name,value=str(value),expected=str(expected),passed=passed))
    assert passed,checks[-1]


def integrate(function,left,right,cells=20000):
    dx=(right-left)/cells
    return dx*sum(function(left+(i+.5)*dx) for i in range(cells))


# Integrate actual sheet-current density, independent of the sinc implementation.
width=.06;spacing=.18
for k,phase in [(0,0),(0,math.pi),(17.4532925199433,math.pi),(-13.,math.pi/2)]:
    currents=[100,100*cmath.exp(1j*phase)]
    exact=sum(integrate(lambda z: I/width*cmath.exp(-1j*k*z),pos-width/2,pos+width/2)
              for I,pos in zip(currents,[0,spacing]))
    check(f'Fourier quadrature k={k}, phase={phase}',current_spectrum(k,[0,spacing],currents,width),exact)
check('Opposite phase cancels at zero wavenumber',abs(current_spectrum(0,[0,spacing],[1,-1],width)),0)
check('Opposite-phase finite-width spectrum at array peak',abs(current_spectrum(math.pi/spacing,[0,spacing],[1,-1],width))**2,3.647562611124159)
for k in [-31.,0.,11.]:
    positive=current_spectrum(k,[0,spacing],[1,1j],width)
    reversed=current_spectrum(-k,[0,spacing],[1,-1j],width)
    check(f'Reversed phase reverses spectral direction, k={k}',abs(positive)**2,abs(reversed)**2)

# Three-strap amplitude starts at k^2; intensity starts at k^4 near zero.
positions=[-spacing,0,spacing];currents=[1,-2,1]
check('Balanced three-strap total current',current_spectrum(0,positions,currents,width),0)
intensity=[abs(current_spectrum(k,positions,currents,width))**2 for k in [.002,.001]]
check('Three-strap low-k intensity refinement ratio',intensity[0]/intensity[1],16,rtol=2e-7)

# RMS network power checked against real-wave time integration (peak=sqrt(2)*RMS).
matrix=[[2-20j,.5-4j],[.5-4j,2-20j]]
for phase,expected in [(0,50000),(math.pi/2,40000),(math.pi,30000)]:
    currents=[100,100*cmath.exp(1j*phase)];voltages=matvec(matrix,currents)
    waveform=lambda theta:sum((math.sqrt(2)*v*cmath.exp(-1j*theta)).real*(math.sqrt(2)*i*cmath.exp(-1j*theta)).real for v,i in zip(voltages,currents))
    time_power=integrate(waveform,0,2*math.pi)/(2*math.pi)
    check(f'Real-wave time average at phase {phase}',time_power,expected,atol=1e-6)
    check(f'Complex-power equality at phase {phase}',accepted_power(matrix,currents),time_power,atol=1e-6)
    waves=[power_waves(v,i) for v,i in zip(voltages,currents)]
    check(f'Incident-minus-reflected power at phase {phase}',sum(abs(a)**2-abs(b)**2 for a,b in waves),expected,atol=1e-6)
for phase_deg in range(0,361,15):
    current=[100,100*cmath.exp(1j*math.radians(phase_deg))]
    # Hermitian resistance eigenvalues 1.5 and 2.5 constrain all drive phases.
    p=accepted_power(matrix,current)
    assert 29999.999999<=p<=50000.000001
check('Resistance-matrix eigenvalue bound over 25 phases',1,1)

for r,target in [(2,10),(6,6),(18,10)]:
    # Independent parallel branch voltages at V=1 RMS.
    branch_current=1/complex(r,6)+1/complex(r,-6)
    check(f'Conjugate-T impedance at R={r}',conjugate_t(r,r),target)
    check(f'Conjugate-T parallel current at R={r}',branch_current,1/target)
check('Unequal T loads acquire an imaginary part',int(abs(conjugate_t(6,2).imag)>1e-8),1)

omega=2*math.pi*50e6;inductance=100e-9;capacitance=1/(omega**2*inductance)
check('LC resonance capacitance [pF]',capacitance*1e12,101.32118364233781)
check('e^-iwt LC reactances cancel',-1j*omega*inductance+1j/(omega*capacitance),0)
mu=4e-7*math.pi;conductivity=5.8e7
depth=math.sqrt(2/(omega*mu*conductivity));resistance=math.sqrt(omega*mu/(2*conductivity))
check('Skin depth rounded teaching value [um]',depth*1e6,9.35,rtol=5e-4)
check('Surface resistance rounded teaching value [mohm]',resistance*1e3,1.845,rtol=5e-4)
# Joule heat integrated through depth equals surface-impedance heat for unit RMS H.
volume_loss=integrate(lambda x:2*math.exp(-2*x/depth)/(conductivity*depth**2),0,20*depth)
check('Surface vs volume Joule heating [W/m2] at H_RMS=1 A/m',volume_loss,resistance,rtol=2e-7)
check('TWA reflected + outgoing + internal fractions',.1**2+.7**2+.5,1)

out=ROOT/'.build/icrf-antenna/checks.json';out.parent.mkdir(parents=True,exist_ok=True)
source='仿真计算/离子回旋天线建模/README.md'
out.write_text(json.dumps(dict(scope=__doc__,all_passed=True,count=len(checks),checks=checks,
    source_sha256={source:hashlib.sha256((ROOT/source).read_bytes()).hexdigest()}),ensure_ascii=False,indent=2)+'\n')
print(f'{len(checks)} ICRF antenna teaching checks passed; no external EM solver or device data used.')
