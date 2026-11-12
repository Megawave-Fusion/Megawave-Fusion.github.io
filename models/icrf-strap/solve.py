#!/usr/bin/env python3
"""3D PEC strap/gap-source Maxwell FEM. SI, peak fields, exp(-i omega t).

Requires NGSolve/Netgen, numpy and scipy. Geometry is a connected PEC cavity
and shorted straps, not a prescribed floating current sheet. The finite outer
box is PEC; a collisional cold-plasma volume and separately reported artificial
absorber provide the load. This is a reproducible reduced model, not WEST CAD.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
import ngsolve as ng
from netgen.occ import Box, Glue, OCCGeometry, Y

EPS0 = 8.8541878128e-12
MU0 = 4e-7 * math.pi
E_CHARGE = 1.602176634e-19
M_E = 9.1093837139e-31
M_D = 3.3435837724e-27
C0 = 1 / math.sqrt(EPS0 * MU0)
DEFAULTS = dict(frequency_hz=50e6, magnetic_field_t=2., electron_density_m3=2e18,
                collision_ratio=.025, absorber_imaginary_epsilon=80.,
                strap_count=1, strap_width_m=.06, strap_thickness_m=.015,
                strap_center_x_m=-.035, strap_centers_z_m=[0.],
                strap_bottom_y_m=-.20, strap_top_y_m=.15,
                gap_height_m=.012, gap_peak_current_a=1., order=2,
                outer_bounds=[[-.16,-.225,-.27],[.65,.225,.27]],
                cavity_bounds=[[-.135,-.20,-.245],[0.,.20,.245]],
                plasma_start_x_m=.025, absorber_start_x_m=.45)


def complex_json(value):
    a=np.asarray(value)
    return np.stack((a.real,a.imag),axis=-1).tolist()


def box_record(label,lo,hi):
    return dict(label=label,xmin=lo[0],xmax=hi[0],ymin=lo[1],ymax=hi[1],zmin=lo[2],zmax=hi[2])


def validate_parameters(p,maxhs,phases):
    """Reject invalid physics and any geometry that disconnects the PEC return."""
    positive=['frequency_hz','electron_density_m3','collision_ratio','strap_width_m',
              'strap_thickness_m','gap_height_m','gap_peak_current_a']
    for key in positive:
        if not np.isfinite(p[key]) or p[key]<=0:
            raise ValueError(f'{key} must be finite and strictly positive')
    if not np.isfinite(p['magnetic_field_t']):raise ValueError('magnetic_field_t must be finite')
    if not np.isfinite(p['absorber_imaginary_epsilon']) or p['absorber_imaginary_epsilon']<0:
        raise ValueError('Artificial absorber must be passive (nonnegative imaginary epsilon)')
    if p['order']<1:raise ValueError('HCurl order must be at least 1')
    if any(not np.isfinite(h) or h<=0 for h in maxhs):raise ValueError('maxh values must be finite and positive')
    if any(not np.isfinite(phase) for phase in phases):raise ValueError('Phase values must be finite')
    olo,ohi=np.asarray(p['outer_bounds'][0]),np.asarray(p['outer_bounds'][1])
    clo,chi=np.asarray(p['cavity_bounds'][0]),np.asarray(p['cavity_bounds'][1])
    if any(a.shape!=(3,) or not np.all(np.isfinite(a)) for a in [olo,ohi,clo,chi]):
        raise ValueError('Box corners must have three finite SI coordinates')
    if not (np.all(olo<clo) and np.all(clo<chi) and np.all(chi<ohi) and abs(chi[0])<1e-12):
        raise ValueError('Cavity must lie strictly inside outer box and its open aperture must be x=0')
    xlo=p['strap_center_x_m']-p['strap_thickness_m']/2;xhi=xlo+p['strap_thickness_m']
    if not (clo[0]<xlo<xhi<0):raise ValueError('Finite-thickness strap must be inside cavity')
    if not (olo[1]<p['strap_bottom_y_m']<=clo[1]):
        raise ValueError('Strap bottom must contact cavity bottom PEC return')
    if not (p['strap_bottom_y_m']<p['strap_top_y_m']<p['strap_top_y_m']+p['gap_height_m']<chi[1]):
        raise ValueError('Source gap must fit between strap top and top return conductor')
    centers=p['strap_centers_z_m'];width=p['strap_width_m']
    if len(centers)!=p['strap_count'] or any(not np.isfinite(z) or z-width/2<=clo[2] or z+width/2>=chi[2] for z in centers):
        raise ValueError('Strap centers/width must fit inside cavity and match strap count')
    if any(abs(a-b)<=width for j,a in enumerate(centers) for b in centers[j+1:]):
        raise ValueError('Distinct strap/gap volumes must not intersect')
    if not (0<p['plasma_start_x_m']<p['absorber_start_x_m']<ohi[0]):
        raise ValueError('Required radial order: aperture 0 < plasma < absorber < outer wall')


def cold_epsilon(parameters):
    """Collisional electron + deuteron tensor; B along +z; signed cyclotron.

    From m(du/dt+nu*u)=q(E+u x B), with exp(-iwt). A positive
    anti-Hermitian part means passive absorption; no thermal/FLR model.
    """
    omega=2*math.pi*parameters['frequency_hz']
    nu=omega*parameters['collision_ratio'];B=parameters['magnetic_field_t']
    epsilon=np.eye(3,dtype=complex)
    for q,m,n in [(-E_CHARGE,M_E,parameters['electron_density_m3']),
                  (E_CHARGE,M_D,parameters['electron_density_m3'])]:
        wc=q*B/m;wp2=n*q*q/(EPS0*m);w=omega+1j*nu
        S=-wp2*w/(omega*(w*w-wc*wc))
        D=wc*wp2/(omega*(w*w-wc*wc))
        P=-wp2/(omega*w)
        epsilon+=np.array([[S,-1j*D,0],[1j*D,S,0],[0,0,P]])
    dissipation=(epsilon-epsilon.conj().T)/(2j)
    eigenvalues=np.linalg.eigvalsh(dissipation)
    if min(eigenvalues)<-1e-10:
        raise ValueError(f'Cold tensor is active, dissipative eigenvalues={eigenvalues}')
    return epsilon,eigenvalues


def make_geometry(p,maxh,out):
    """Subtract connected PEC solids; gap domains remain meshed vacuum."""
    outerlo,outerhi=p['outer_bounds'];clo,chi=p['cavity_bounds']
    outer=Box(tuple(outerlo),tuple(outerhi));outer.faces.name='outer_pec'
    # Shell at the back, top/bottom and sides; aperture x=0 stays open.
    shell_box=Box(tuple(outerlo),(0.,outerhi[1],outerhi[2]))
    cavity=Box(tuple(clo),tuple(chi))
    metal=shell_box-cavity
    metal.faces.name='metal_pec'
    boxes=[box_record('back_plate',outerlo,[clo[0],outerhi[1],outerhi[2]]),
           box_record('bottom_wall',[clo[0],outerlo[1],outerlo[2]],[0.,clo[1],outerhi[2]]),
           box_record('top_wall',[clo[0],chi[1],outerlo[2]],[0.,outerhi[1],outerhi[2]]),
           box_record('left_wall',[clo[0],clo[1],outerlo[2]],[0.,chi[1],clo[2]]),
           box_record('right_wall',[clo[0],clo[1],chi[2]],[0.,chi[1],outerhi[2]])]
    xlo=p['strap_center_x_m']-p['strap_thickness_m']/2;xhi=xlo+p['strap_thickness_m']
    gap_shapes=[];gaps=[]
    for index,z in enumerate(p['strap_centers_z_m']):
        zlo=z-p['strap_width_m']/2;zhi=z+p['strap_width_m']/2
        ybottom=p['strap_bottom_y_m'];ytop=p['strap_top_y_m'];g=p['gap_height_m']
        strap=Box((xlo,ybottom-.005,zlo),(xhi,ytop,zhi))
        # Overlap at the shell is deliberate: it proves galvanic return.
        feed=Box((xlo,ytop+g,zlo),(xhi,chi[1]+.005,zhi))
        strap.faces.name='metal_pec';feed.faces.name='metal_pec'
        metal=metal+strap+feed
        boxes.extend([box_record(f'strap_{index}',[xlo,ybottom,zlo],[xhi,ytop,zhi]),
                      box_record(f'return_above_gap_{index}',[xlo,ytop+g,zlo],[xhi,chi[1],zhi])])
        gap=Box((xlo,ytop,zlo),(xhi,ytop+g,zhi));gap.mat(f'gap_{index}')
        # These two faces terminate on metal, whereas the four lateral faces
        # are material interfaces to vacuum. Glue does not inherit the PEC tag
        # from the independently subtracted metal faces automatically.
        gap.faces.Min(Y).name='metal_pec'
        gap.faces.Max(Y).name='metal_pec'
        gap.maxh=min(maxh,.015)
        gap_shapes.append(gap);gaps.append(box_record(f'gap_{index}',[xlo,ytop,zlo],[xhi,ytop+g,zhi]))
    metal.faces.name='metal_pec'
    airvolume=outer-metal
    plasma=Box((p['plasma_start_x_m'],outerlo[1],outerlo[2]),
               (p['absorber_start_x_m'],outerhi[1],outerhi[2]))
    plasma.mat('plasma')
    absorber=Box((p['absorber_start_x_m'],outerlo[1],outerlo[2]),tuple(outerhi))
    absorber.mat('absorber')
    vacuum=airvolume-plasma-absorber
    for gap in gap_shapes:vacuum=vacuum-gap
    vacuum.mat('vacuum')
    shape=Glue([vacuum,*gap_shapes,plasma,absorber])
    # Glue retains separately created slab faces: re-tag ONLY the exterior box,
    # never the internal material interfaces, by their planar face centroids.
    for face in shape.faces:
        center=tuple(face.center)
        if any(abs(center[k]-outerlo[k])<1e-9 or abs(center[k]-outerhi[k])<1e-9 for k in range(3)):
            face.name='outer_pec'
    # Explicit material-boundary interfaces are interior; exterior surfaces are PEC.
    geo=OCCGeometry(shape)
    mesh=ng.Mesh(geo.GenerateMesh(maxh=maxh,grading=.3))
    mesh.Curve(1)
    for descriptor in mesh.ngmesh.FaceDescriptors():
        if descriptor.domout==0 and mesh.GetBoundaries()[descriptor.bc-1] not in {'outer_pec','metal_pec'}:
            raise ValueError(f'Unmarked exterior field face: bc={descriptor.bc}, name={mesh.GetBoundaries()[descriptor.bc-1]}')
    # Export both the vacuum/load partition and the actual PEC solids.
    shape.WriteStep(str(out/'field-domain.step'))
    metal.WriteStep(str(out/'pec-metal.step'))
    mesh.ngmesh.Save(str(out/'mesh.vol'))
    description=dict(coordinates='SI metres; x radial into load, y strap direction, z toroidal/B',
                     pec_boxes=boxes,gaps=gaps,outer_bounds=p['outer_bounds'],cavity_bounds=p['cavity_bounds'],
                     domain_regions=[dict(name='vacuum',xmax=p['plasma_start_x_m']),
                                     dict(name='plasma',xmin=p['plasma_start_x_m'],xmax=p['absorber_start_x_m']),
                                     dict(name='absorber',xmin=p['absorber_start_x_m'])],
                     outer_boundary='PEC, with separately reported volumetric artificial absorber',
                     materials=list(mesh.GetMaterials()),boundaries=list(mesh.GetBoundaries()),
                     boundary_areas_m2={name:float(ng.Integrate(ng.CoefficientFunction(1.),mesh,definedon=mesh.Boundaries(name)))
                                        for name in set(mesh.GetBoundaries())},
                     metal_solid_count=len(metal.solids),metal_connected_requirement='one connected PEC solid')
    if description['metal_solid_count']!=1:
        raise ValueError('PEC return is not a single connected metal solid')
    description['gap_volumes_m3']={f'gap_{j}':float(ng.Integrate(ng.CoefficientFunction(1.),mesh,definedon=mesh.Materials(f'gap_{j}')))
                                   for j in range(p['strap_count'])}
    expected_gap=p['strap_thickness_m']*p['strap_width_m']*p['gap_height_m']
    if any(abs(value-expected_gap)/expected_gap>1e-8 for value in description['gap_volumes_m3'].values()):
        raise ValueError('Gap domain volume differs from intended source volume')
    (out/'geometry.json').write_text(json.dumps(description,indent=2)+'\n')
    return mesh,description


def matrix_cf(a):
    return ng.CoefficientFunction(tuple(np.asarray(a).reshape(-1)),dims=(3,3))


def solve_mesh(p,maxh,out,phases):
    out.mkdir(parents=True,exist_ok=True)
    t0=time.perf_counter();mesh,geometry=make_geometry(p,maxh,out)
    eps,eigenvalues=cold_epsilon(p);eps_cf=matrix_cf(eps)
    identity=matrix_cf(np.eye(3,dtype=complex))
    # Smooth nonnegative ramp avoids a jump in the artificial conductivity.
    ramp=((ng.x-p['absorber_start_x_m'])/(p['outer_bounds'][1][0]-p['absorber_start_x_m']))**2
    epsilon=mesh.MaterialCF({'plasma':eps_cf,'absorber':eps_cf+1j*p['absorber_imaginary_epsilon']*ramp*identity},default=identity)
    fes=ng.HCurl(mesh,order=p['order'],complex=True,dirichlet='outer_pec|metal_pec')
    u,v=fes.TnT();omega=2*math.pi*p['frequency_hz'];k0=omega/C0
    form=ng.BilinearForm(fes,symmetric=False)
    form+=ng.curl(u)*ng.curl(v)*ng.dx(bonus_intorder=6)-k0*k0*((epsilon*u)*v)*ng.dx(bonus_intorder=6)
    tassemble=time.perf_counter()
    form.Assemble()
    # A direct sparse LU retains the gyrotropic, nonreciprocal tensor.
    try:
        inverse=form.mat.Inverse(fes.FreeDofs(),inverse='umfpack')
        inverse_kind='NGSolve UMFPACK'
        apply=lambda b:inverse*b
    except Exception:
        import scipy.sparse as sp
        import scipy.sparse.linalg as spla
        rows,cols,values=form.mat.COO();free=np.flatnonzero(np.array(fes.FreeDofs(),dtype=bool))
        lu=spla.splu(sp.coo_matrix((values,(rows,cols)),shape=(fes.ndof,fes.ndof)).tocsc()[free,:][:,free])
        def apply(b):
            result=b.CreateVector();result[:]=0
            result.FV().NumPy()[free]=lu.solve(b.FV().NumPy()[free])
            return result
        inverse_kind='SciPy SuperLU'
    factor_time=time.perf_counter()-tassemble
    area=p['strap_width_m']*p['strap_thickness_m']
    gp=[mesh.MaterialCF({f'gap_{j}':ng.CoefficientFunction((0.,1/area,0.))},default=ng.CoefficientFunction((0.,0.,0.)))
        for j in range(p['strap_count'])]
    solutions=[];Z=np.zeros((p['strap_count'],p['strap_count']),dtype=complex)
    for j in range(p['strap_count']):
        load=ng.LinearForm(fes);load+=1j*omega*MU0*(gp[j]*v)*ng.dx;load.Assemble()
        E=ng.GridFunction(fes,name=f'E_unit_gap_{j}');E.vec.data=apply(load.vec)
        solutions.append(E)
        for q in range(p['strap_count']):Z[q,j]=-ng.Integrate(E*gp[q],mesh)
    z_passivity=np.linalg.eigvalsh((Z+Z.conj().T)/2)
    if min(z_passivity)<-1e-8*max(float(np.linalg.norm(Z)),1.):
        raise ValueError(f'Extracted impedance has an active Hermitian part: {z_passivity}')
    cases=[];diss_cf=matrix_cf((eps-eps.conj().T)/(2j))
    for phase in phases:
        currents=np.ones(p['strap_count'],dtype=complex)*p['gap_peak_current_a']
        if p['strap_count']==2:currents[1]*=np.exp(1j*math.radians(phase))
        E=ng.GridFunction(fes,name='E_peak')
        E.vec[:]=0
        for current,solution in zip(currents,solutions):E.vec.data+=complex(current)*solution.vec
        H=ng.curl(E)/(1j*omega*MU0)
        J=sum((complex(current)*g for current,g in zip(currents,gp)),start=ng.CoefficientFunction((0.,0.,0.)))
        conjE=ng.Conj(E)
        absE2=sum(E[j]*conjE[j] for j in range(3))
        pin=-.5*complex(ng.Integrate(E*ng.Conj(J),mesh,order=10)).real
        plasma_density=.5*omega*EPS0*sum(conjE[j]*(diss_cf*E)[j] for j in range(3))
        physical=complex(ng.Integrate(plasma_density,mesh,definedon=mesh.Materials('plasma|absorber'),order=10)).real
        artificial_density=.5*omega*EPS0*p['absorber_imaginary_epsilon']*ramp*absE2
        artificial=complex(ng.Integrate(artificial_density,mesh,definedon=mesh.Materials('absorber'),order=10)).real
        voltages=Z@currents
        residual=abs(pin-physical-artificial)/max(abs(pin),1e-30)
        if pin<=0 or residual>1e-6:
            raise ValueError(f'Nonpassive or unbalanced result Pin={pin}, physical={physical}, artificial={artificial}, residual={residual}')
        caseout=out/f'phase-{phase:g}';caseout.mkdir(exist_ok=True)
        ecfs=[E[j].real for j in range(3)]+[E[j].imag for j in range(3)]
        hcfs=[H[j].real for j in range(3)]+[H[j].imag for j in range(3)]
        ng.VTKOutput(ma=mesh,coefs=[ng.CoefficientFunction(tuple(ecfs[:3])),ng.CoefficientFunction(tuple(ecfs[3:])),
                                 ng.CoefficientFunction(tuple(hcfs[:3])),ng.CoefficientFunction(tuple(hcfs[3:])),
                                 ng.sqrt(absE2.real)],
                     names=['E_real_V_m','E_imag_V_m','H_real_A_m','H_imag_A_m','E_abs_V_m'],
                     filename=str(caseout/'field'),subdivision=0).Do()
        E.Save(str(caseout/'E.sol'))
        sample_fields(mesh,E,H,p,geometry,caseout/'fields.npz')
        load=ng.LinearForm(fes);load+=1j*omega*MU0*(J*v)*ng.dx;load.Assemble()
        algebraic=load.vec.CreateVector();algebraic.data=form.mat*E.vec-load.vec
        arr=algebraic.FV().NumPy();free=np.array(fes.FreeDofs(),dtype=bool)
        algebraic_relative=float(np.linalg.norm(arr[free])/max(np.linalg.norm(load.vec.FV().NumPy()[free]),1e-30))
        case=dict(strap_count=p['strap_count'],phase_degree=phase,maxh_m=maxh,order=p['order'],
                  ndof=fes.ndof,nelements=mesh.ne,nvertices=mesh.nv,
                  Z_ohm=complex_json(Z),peak_currents_a=complex_json(currents),peak_voltages_v=complex_json(voltages),
                  delivered_power_w=pin,physical_plasma_absorption_w=physical,artificial_absorber_power_w=artificial,
                  pec_metal_loss_w=0.,outer_pec_flux_w=0.,power_balance_relative=residual,
                  linear_residual_relative=algebraic_relative,
                  matrix_passivity_eigenvalues_ohm=z_passivity.tolist(),
                  cold_epsilon=complex_json(eps),epsilon_dissipation_eigenvalues=eigenvalues.tolist(),
                  effective_delivered_resistance_ohm=2*pin/float(np.vdot(currents,currents).real),
                  inverse=inverse_kind,ngsolve_version=ng.__version__,numpy_version=np.__version__,
                  assembly_factor_seconds=factor_time,
                  elapsed_seconds=time.perf_counter()-t0,output=str(caseout),meshpath=str(out/'mesh.vol'),
                  geometrypath=str(out/'geometry.json'),name=f'{p["strap_count"]}-strap-phase-{phase:g}-h-{maxh:g}-p-{p["order"]}')
        (caseout/'results.json').write_text(json.dumps(case,indent=2)+'\n')
        cases.append(case)
        print(json.dumps({key:case[key] for key in ['strap_count','phase_degree','maxh_m','ndof','nelements','delivered_power_w','power_balance_relative','linear_residual_relative','elapsed_seconds']}),flush=True)
    return cases


def sample_fields(mesh,E,H,p,geometry,path):
    """Cellwise field samples on three physical planes; mask 0 denotes PEC."""
    grid={};n=59
    lo,hi=np.asarray(p['outer_bounds'][0]),np.asarray(p['outer_bounds'][1])
    settings=[('xy',(0,1),2,0.),('xz',(0,2),1,0.),('yz',(1,2),0,.05)]
    for name,axes,fixed,fixedvalue in settings:
        a=np.linspace(lo[axes[0]]+.0003,hi[axes[0]]-.0003,n)
        b=np.linspace(lo[axes[1]]+.0003,hi[axes[1]]-.0003,n)
        coords=np.zeros((n,n,3));coords[:,:,fixed]=fixedvalue
        aa,bb=np.meshgrid(a,b,indexing='xy');coords[:,:,axes[0]]=aa;coords[:,:,axes[1]]=bb
        valuesE=np.full((n,n,3),np.nan+1j*np.nan,dtype=complex);valuesH=valuesE.copy()
        mask=np.zeros((n,n),dtype=bool);material=np.full((n,n),-1,dtype=int)
        for i in range(n):
            for j in range(n):
                point=coords[i,j]
                inside_metal=any(box['xmin']-1e-8<=point[0]<=box['xmax']+1e-8 and
                                 box['ymin']-1e-8<=point[1]<=box['ymax']+1e-8 and
                                 box['zmin']-1e-8<=point[2]<=box['zmax']+1e-8 for box in geometry['pec_boxes'])
                if inside_metal:continue
                try:
                    mp=mesh(*point);valuesE[i,j]=np.asarray(E(mp));valuesH[i,j]=np.asarray(H(mp))
                    mask[i,j]=True;material[i,j]=0 if point[0]<p['plasma_start_x_m'] else 1 if point[0]<p['absorber_start_x_m'] else 2
                except Exception:pass
        grid.update({name+'_coords':coords,name+'_E':valuesE,name+'_H':valuesH,name+'_mask':mask,name+'_material':material})
    np.savez_compressed(path,**grid)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--straps',type=int,choices=[1,2],default=1)
    parser.add_argument('--maxh',type=float,nargs='+',default=[.075,.055,.04])
    parser.add_argument('--order',type=int,default=2)
    parser.add_argument('--out',type=Path,default=Path('.build/icrf-fem'))
    parser.add_argument('--config',type=Path)
    parser.add_argument('--phase',type=float,nargs='+',default=[0.,180.])
    args=parser.parse_args();p=dict(DEFAULTS)
    if args.config:p.update(json.loads(args.config.read_text()))
    p.update(strap_count=args.straps,order=args.order,
             strap_centers_z_m=[0.] if args.straps==1 else [-.09,.09])
    validate_parameters(p,args.maxh,args.phase)
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/'parameters.json').write_text(json.dumps(p,indent=2)+'\n')
    ng.SetNumThreads(2)
    cases=[]
    for maxh in args.maxh:
        with ng.TaskManager():cases+=solve_mesh(p,maxh,args.out/f'straps-{args.straps}-h-{maxh:g}',[0.] if args.straps==1 else args.phase)
    (args.out/'results.json').write_text(json.dumps(dict(convention='exp(-i omega t), peak phasors',parameters=p,cases=cases),indent=2)+'\n')


if __name__=='__main__':main()
