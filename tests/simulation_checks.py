#!/usr/bin/env python3
"""Independent checks of teaching examples, not software performance/validation.

Run with the standard library; reports go to ignored .build/simulation-research/.
"""
import hashlib
import json
import math
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
records = []


def check(name, actual, expected, *, rtol=1e-10, atol=1e-12):
    passed = math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol)
    records.append(dict(name=name, actual=actual, expected=expected,
                        rtol=rtol, atol=atol, passed=passed))
    assert passed, records[-1]


def remap(edges, source, target):
    """Transfer piecewise-constant cell averages by overlap in volume space."""
    return [sum(value * max(0., min(b, right) - max(a, left))
                for left, right, value in zip(edges, edges[1:], source)) / (b-a)
            for a, b in zip(target, target[1:])]


# Check the chapter example against hand-integrated source volumes.
old_edges, old_source = [0., 1., 4.], [2., 1.]
new_edges = [0., 2., 4.]
mapped = remap(old_edges, old_source, new_edges)
check('overlap remap: first cell [MW/m3]', mapped[0], 1.5)
check('overlap remap: second cell [MW/m3]', mapped[1], 1.)
check('remapped integrated power [MW]',
      sum(q*(b-a) for a, b, q in zip(new_edges, new_edges[1:], mapped)), 5.)
point_values = [2.+(1.-2.)*(1.-.5)/(2.5-.5), 1.]
check('clamped point interpolation power [MW]', sum(point_values)*2, 5.5)
check('point interpolation relative error', (sum(point_values)*2-5)/5, .1)

# Non-matching random partitions expose gaps/double counting in the mapping.
rng = random.Random(20261020)
errors = []
bounded = True
for _ in range(100):
    source_edges = [0., *sorted(rng.uniform(0., 4.) for _ in range(6)), 4.]
    target_edges = [0., *sorted(rng.uniform(0., 4.) for _ in range(9)), 4.]
    source_values = [rng.uniform(0., 10.) for _ in range(7)]
    target_values = remap(source_edges, source_values, target_edges)
    before = sum(q*(b-a) for a, b, q in
                 zip(source_edges, source_edges[1:], source_values))
    after = sum(q*(b-a) for a, b, q in
                zip(target_edges, target_edges[1:], target_values))
    errors.append(abs(before-after)/before)
    bounded &= all(min(source_values)-1e-10 <= q <= max(source_values)+1e-10
                   for q in target_values)
check('100 nonmatching partitions conserve integrated power', max(errors), 0., atol=1e-13)
check('100 nonnegative remaps retain source bounds', int(bounded), 1)

# Independently integrate a nonuniform source: V=C*r^2, S=S0*(1-r^2).
# Exact power at r=1 is C*S0/2. Midpoint integration should be second order.
C, S0 = 8., 2.
exact = C*S0/2
estimates = []
for cells in (100, 200):
    dr = 1/cells
    estimates.append(sum(2*C*(i+.5)*dr * S0*(1-((i+.5)*dr)**2)*dr
                         for i in range(cells)))
check('radial source integral refinement ratio',
      (estimates[0]-exact)/(estimates[1]-exact), 4., rtol=1e-8)
check('flux/source signed residual [MW]', 3.8-4., -.2)
check('relative flux/source residual', (3.8-4.)/4., -.05)

# SI conversions and the fixed-source nuclear heating example.
erg, cm = 1e-7, 1e-2
check('CGS heat flux -> W/m2', 2e8*erg/cm**2, 2e5)
check('CGS volume source -> W/m3', erg/cm**3, .1)
ev_j = 1.602176634e-19
source_rate = 500e6/(17.6e6*ev_j)
check('500 MW D-T neutron source: rounded example [1/s]', source_rate, 1.7732e20, rtol=3e-5)
power_w = 9e6*ev_j*source_rate
check('heating tally -> MW, independent MeV ratio', power_w/1e6, 500*9/17.6)
check('10 m3 volume-averaged heating [MW/m3]', power_w/10/1e6, 25.568181818181817)

# Exact finite-N covariance sum versus the long-window approximation.
N, a = 900, .8
inflation = 1+2*sum((1-k/N)*a**k for k in range(1, N))
asymptotic = (1+a)/(1-a)
check('long-window geometric covariance inflation', asymptotic, 9.)
check('effective independent samples: asymptotic', N/asymptotic, 100.)
check('standard-error ratio: asymptotic', math.sqrt(asymptotic), 3.)
check('finite-N standard error agrees within 0.3 percent',
      int(abs(math.sqrt(inflation/asymptotic)-1) < .003), 1)

out = ROOT/'.build/simulation-research/numerical-checks.json'
out.parent.mkdir(parents=True, exist_ok=True)
config = json.loads((ROOT/'site/site.json').read_text())
simulation = next(chapter for chapter in config['chapters'] if chapter['slug'] == 'simulation')
source_hashes = {source: hashlib.sha256((ROOT/source).read_bytes()).hexdigest()
                 for _, source in simulation['sections']}
report = dict(scope=__doc__.strip(), all_passed=True, count=len(records),
              source_sha256=source_hashes,
              checks=records)
out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(f'{len(records)} simulation teaching checks passed; no listed solver was installed or run.')
