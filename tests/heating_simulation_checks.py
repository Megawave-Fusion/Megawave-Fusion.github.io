#!/usr/bin/env python3
"""Independent quadratures of new heating teaching examples; no solver benchmark."""
from pathlib import Path
import json,math,hashlib

ROOT=Path(__file__).resolve().parents[1]
records=[]

def check(name,value,expected,rtol=1e-8,atol=1e-10):
    passed=math.isclose(value,expected,rel_tol=rtol,abs_tol=atol)
    records.append(dict(name=name,value=value,expected=expected,passed=passed))
    assert passed,records[-1]

def integrate(f,a,b,n=20000):
    h=(b-a)/n
    return h*sum(f(a+(i+.5)*h) for i in range(n))

# Beam energy groups: independently recover total energy from particle fluxes.
C=[.6,.3,.1];E=[80.,40.,80/3]
mean=sum(c*e for c,e in zip(C,E));power=[c*e/mean for c,e in zip(C,E)]
check('NBI neutral reference-plane mean energy [keV]',mean,188/3)
check('NBI full-energy power fraction',power[0],36/47)
check('NBI half-energy power fraction',power[1],9/47)
check('NBI third-energy power fraction',power[2],2/47)
check('NBI power reconstructed from group rates',sum(power),1)
# Integrate the removal density instead of using the cumulative formula.
stopped=integrate(lambda s:math.exp(-s),0,1)
check('NBI stopped fraction: rate-density integral',stopped,1-math.exp(-1))
check('NBI transmission plus stopped particles',stopped+math.exp(-1),1)
check('NBI fast reservoir closes [kW]',100-40-30-20,10)

# EC beam full width at half maximum and absorption by independent quadrature.
w=.02;half=w*math.sqrt(math.log(2)/2)
check('EC half-maximum value at half FWHM',math.exp(-2*(half/w)**2),.5)
check('EC intensity FWHM [mm]',2*half*1000,23.5482004503)
absorb=integrate(lambda s:2*math.exp(-2*s),0,.5)
check('EC integrated single-pass absorbed power [MW]',absorb,1-math.exp(-1))
check('ECCD dimensional current efficiency [A/W]',40e3/.8e6,.05)
# The current-profile width below differs from the intensity convention above.
a=.02
for d,expected in [(0,.8427007929497149),(.02,.49766113250947636)]:
    numeric=integrate(lambda x:math.exp(-((x-d)/w)**2)/(math.sqrt(math.pi)*w),-a,a)
    check(f'Gaussian line-current target overlap, offset={d} m',numeric,expected)

# Array peak from a direct complex sum; changing the sign reverses its direction.
c=299792458.;frequency=476e6;spacing=.05;n=8
k0=2*math.pi*frequency/c;phase=k0*3*spacing
check('476 MHz vacuum wavelength [m]',c/frequency,.6298160882352941)
check('Nparallel=3 adjacent phase: rounded text [degree]',math.degrees(phase),85.7,rtol=5e-4)
def pattern(N,phi):
    amplitude=sum(complex(math.cos(m*(phi-k0*N*spacing)),math.sin(m*(phi-k0*N*spacing))) for m in range(n))
    return abs(amplitude)**2/n**2
check('Array main lobe at Nparallel=3',pattern(3,phase),1)
check('Reversed phase main lobe at Nparallel=-3',pattern(-3,-phase),1)
check('Array phase/sign symmetry',pattern(-3,phase),pattern(3,-phase))
beta=1/3;kinetic=(1/math.sqrt(1-beta*beta)-1)*510.99895
check('Nparallel=3 resonant energy: rounded text [keV]',kinetic,31.0,rtol=3e-3)

# Momentum-space current needs relativistic velocity, not a bare momentum moment.
p=2.;gamma=math.sqrt(1+p*p)
check('Relativistic normalized current velocity',p/gamma,2/math.sqrt(5))
# O-X optimal angle has two conditions; this tests the parallel component only.
Y=.5;Nparallel=math.sqrt(Y/(1+Y))
check('O-X ideal parallel optimum at Y=0.5',Nparallel**2,1/3)

config=json.loads((ROOT/'site/site.json').read_text())
sources=[p for chapter in config['chapters'] if chapter['slug']=='simulation' for _,p in chapter['sections']]
out=ROOT/'.build/simulation-research/heating-numerical-checks.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(dict(scope=__doc__,count=len(records),all_passed=True,checks=records,
    source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}),ensure_ascii=False,indent=2)+'\n')
print(f'{len(records)} heating simulation checks passed; analytical teaching cases only.')
