#!/usr/bin/env python3
"""Package actual ICRF FEM outputs with inputs, CAD, mesh and full complex field."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parents[1]


def package(single,double):
    runs=[json.loads((Path(path)/'results.json').read_text()) for path in (single,double)]
    model=ROOT/'models/icrf-strap';target=ROOT/'site/assets/models/icrf-strap-fem.zip';target.parent.mkdir(parents=True,exist_ok=True)
    summary=dict(solver='NGSolve 6.2.2606; 3D complex HCurl; exp(-i omega t), peak phasors',
        model='Connected PEC strap/cavity, distributed gap current, collisional cold e/D plasma and finite PEC outer box with artificial absorber',
        source_sha256=hashlib.sha256((model/'solve.py').read_bytes()).hexdigest(),
        parameters={label:run['parameters'] for label,run in zip(['single','double'],runs)},cases=[])
    payload={}
    for name in ['solve.py','requirements.txt','README.txt']:
        if (model/name).exists():payload[name]=(model/name).read_bytes()
    for label,run in zip(['single','double'],runs):
        for case in run['cases']:
            row=dict(case);row.pop('output',None);row['model']=label;summary['cases'].append(row)
        finest=min(run['cases'],key=lambda c:c['maxh_m'])
        meshdir=Path(finest['output']).parent
        for name in ['geometry.json','pec-metal.step','field-domain.step','mesh.vol']:
            payload[f'{label}/{name}']=(meshdir/name).read_bytes()
        payload[f'{label}/parameters.json']=json.dumps(run['parameters'],indent=2).encode()
        for phase in sorted({c['phase_degree'] for c in run['cases']}):
            case=min((c for c in run['cases'] if c['phase_degree']==phase),key=lambda c:c['maxh_m'])
            directory=Path(case['output'])
            for name in ['E.sol','fields.npz','field.vtu','results.json']:
                payload[f'{label}/phase-{phase:g}/{name}']=(directory/name).read_bytes()
    preliminary=ROOT/'.build/icrf-fem-final'
    summary['first_order_mesh_study']=[]
    for result in sorted(preliminary.glob('straps-*-h-*/phase-*/results.json')):
        row=json.loads(result.read_text())
        if row['order']!=1:continue
        row.pop('output',None)
        summary['first_order_mesh_study'].append(row)
    data=(json.dumps(summary,ensure_ascii=False,indent=2)+'\n').encode()
    (model/'results-summary.json').write_bytes(data);payload['results-summary.json']=data
    payload['SHA256SUMS.txt']=('\n'.join(hashlib.sha256(content).hexdigest()+'  '+name for name,content in sorted(payload.items()))+'\n').encode()
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as archive:
        for name,content in sorted(payload.items()):
            info=zipfile.ZipInfo('icrf-strap-fem/'+name,date_time=(2026,11,12,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(info,content)
    print(f'{len(summary["cases"])} actual FEM cases; {len(payload)} input/result files; {target.stat().st_size/1e6:.2f} MB -> {target}')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--single',type=Path,default=ROOT/'.build/icrf-fem-final-single-p2')
    parser.add_argument('--double',type=Path,default=ROOT/'.build/icrf-fem-final-p2')
    args=parser.parse_args();package(args.single,args.double)
