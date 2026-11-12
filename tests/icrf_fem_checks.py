#!/usr/bin/env python3
"""Audit archived 3D FEM results/artifacts; this does not rerun the costly field solves."""
from pathlib import Path
import hashlib,json,math,zipfile

ROOT=Path(__file__).resolve().parents[1]
model=ROOT/'models/icrf-strap';data=json.loads((model/'results-summary.json').read_text());count=0
def check(condition,message):
    global count
    assert condition,message
    count+=1
def complex_array(row):
    return [complex(*x) for x in row]
check(data['source_sha256']==hashlib.sha256((model/'solve.py').read_bytes()).hexdigest(),'Solver source changed since archived run')
check(len(data['cases'])==9,'Expected three meshes x three excitations')
for c in data['cases']:
    z=[complex_array(row) for row in c['Z_ohm']];i=complex_array(c['peak_currents_a'])
    voltage=[sum(a*b for a,b in zip(row,i)) for row in z]
    pin=.5*sum(a.conjugate()*b for a,b in zip(i,voltage)).real
    check(math.isclose(pin,c['delivered_power_w'],rel_tol=1e-9),'Independent I-dagger Z I power differs')
    check(c['delivered_power_w']>0 and c['physical_plasma_absorption_w']>=0 and c['artificial_absorber_power_w']>=0,'Active source/load sign')
    check(math.isclose(pin,c['physical_plasma_absorption_w']+c['artificial_absorber_power_w'],rel_tol=1e-8),'Archived power budget does not close')
    check(c['linear_residual_relative']<1e-8,'Discrete linear equation residual')
    check(min(c['matrix_passivity_eigenvalues_ohm'])>=-1e-10,'Impedance fails passivity')
    check(c['order']==2 and c['ndof']>0 and c['nelements']>0,'Missing actual second-order mesh')
for name,phase,percent in [('single',0,5.5125349),('double',0,4.2923053),('double',180,1.4960321)]:
    rows=sorted([r for r in data['cases'] if r['model']==name and r['phase_degree']==phase],key=lambda r:r['maxh_m'],reverse=True)
    observed=100*abs(rows[-1]['delivered_power_w']-rows[-2]['delivered_power_w'])/rows[-1]['delivered_power_w']
    check(abs(observed-percent)<.02,'Reported mesh change is inconsistent')
with zipfile.ZipFile(ROOT/'site/assets/models/icrf-strap-fem.zip') as z:
    check(z.testzip() is None,'Corrupt ZIP')
    for line in z.read('icrf-strap-fem/SHA256SUMS.txt').decode().splitlines():
        expected,path=line.split('  ',1)
        check(hashlib.sha256(z.read('icrf-strap-fem/'+path)).hexdigest()==expected,'Corrupt package member: '+path)
    for name in ['single','double']:
        g=json.loads(z.read(f'icrf-strap-fem/{name}/geometry.json'))
        check(g['metal_solid_count']==1,'Disconnected metal return')
        check(all(math.isclose(v,.06*.015*.012,rel_tol=1e-8) for v in g['gap_volumes_m3'].values()),'Incorrect gap geometry volume')
print(f'{count} archived 3D FEM data/artifact checks passed; observed mesh errors retained.')
