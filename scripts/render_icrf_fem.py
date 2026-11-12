#!/usr/bin/env python3
"""Render actual Netgen geometry/mesh and NGSolve Maxwell fields.

Every curve/colour map is read from solver output. No prescribed antenna
patterns or interpolated convergence values are created here.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import hashlib
from xml.etree import ElementTree as ET

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.collections import LineCollection
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT/'site/assets/diagrams'
COLORS = dict(metal='#718493', strap='#127c86', gap='#d55469',
              plasma='#abd9e4', absorber='#cfb8dd')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,
                     'axes.titlesize':11,'axes.labelsize':9,
                     'svg.fonttype':'none','savefig.facecolor':'white'})


def source_name(path):
    return path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)


def cases_under(base):
    """Read per-case records, preferring files beside their actual field data."""
    cases=[]
    for path in sorted(base.rglob('results.json')):
        value=json.loads(path.read_text())
        if not isinstance(value,dict) or 'ndof' not in value:continue
        if not (path.parent/'fields.npz').is_file():continue
        value['_dir']=path.parent
        value['_geometry']=json.loads((path.parent.parent/'geometry.json').read_text())
        parameter_path=path.parent.parent.parent/'parameters.json'
        value['_parameters']=json.loads(parameter_path.read_text()) if parameter_path.is_file() else {}
        cases.append(value)
    return sorted(cases,key=lambda c:(c['strap_count'],c['phase_degree'],-c['maxh_m'],c['order']))


def finest(cases,straps,phase):
    matches=[c for c in cases if c['strap_count']==straps and abs(c['phase_degree']-phase)<1e-6]
    return min(matches,key=lambda c:(c['maxh_m'],-c['order'])) if matches else None


def save(fig,name,title,description):
    FIGURES.mkdir(parents=True,exist_ok=True)
    path=FIGURES/(name+'.svg')
    fig.savefig(path,bbox_inches='tight',pad_inches=.18)
    preview_dir=ROOT/'.build/icrf-fem-figures'
    preview_dir.mkdir(parents=True,exist_ok=True)
    fig.savefig(preview_dir/(name+'.png'),dpi=140,bbox_inches='tight',pad_inches=.18)
    # Explicit alternative text survives both direct SVG use and image viewing.
    ET.register_namespace('','http://www.w3.org/2000/svg')
    tree=ET.parse(path);root=tree.getroot();ns='{http://www.w3.org/2000/svg}'
    for tag in ['title','desc']:
        old=root.find(ns+tag)
        if old is not None:root.remove(old)
    title_node=ET.Element(ns+'title',{'id':'title'});title_node.text=title
    desc_node=ET.Element(ns+'desc',{'id':'desc'});desc_node.text=description
    root.insert(0,title_node);root.insert(1,desc_node)
    root.set('role','img');root.set('aria-labelledby','title desc')
    tree.write(path,encoding='unicode',xml_declaration=True)
    path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
    plt.close(fig)
    return path


def box_vertices(box):
    # Display horizontal radial x / depth toroidal z / vertical poloidal y.
    x0,x1=box['xmin'],box['xmax'];y0,y1=box['ymin'],box['ymax'];z0,z1=box['zmin'],box['zmax']
    return np.array([[x0,z0,y0],[x1,z0,y0],[x1,z1,y0],[x0,z1,y0],
                     [x0,z0,y1],[x1,z0,y1],[x1,z1,y1],[x0,z1,y1]])


def box3d(ax,box,color,alpha=1.):
    vertices=box_vertices(box)
    faces=[[vertices[i] for i in indexes] for indexes in
           [[0,1,2,3],[4,5,6,7],[0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7]]]
    ax.add_collection3d(Poly3DCollection(faces,facecolor=color,edgecolor='#364f5c',
                                       linewidth=.3,alpha=alpha))


def geometry_figure(single,double):
    shown=[c for c in [single,double] if c is not None]
    fig=plt.figure(figsize=(12.5,4.5))
    for index,case in enumerate(shown):
        geo=case['_geometry'];ax=fig.add_subplot(1,3,index+1,projection='3d')
        for box in geo['pec_boxes']:
            # Cutaway rendering hides these walls; solver STEP retains them.
            if box['label'] in ['top_wall','left_wall']:continue
            strap='strap' in box['label'] or 'return_above' in box['label']
            box3d(ax,box,COLORS['strap'] if strap else COLORS['metal'],alpha=1. if strap else .12)
        for gap in geo['gaps']:box3d(ax,gap,COLORS['gap'],alpha=1)
        lo,hi=np.array(geo['outer_bounds'])
        plasma=next(r for r in geo['domain_regions'] if r['name']=='plasma')
        ax.add_collection3d(Poly3DCollection([[(plasma['xmin'],lo[2],lo[1]),(plasma['xmin'],hi[2],lo[1]),
                                               (plasma['xmin'],hi[2],hi[1]),(plasma['xmin'],lo[2],hi[1])]],
                                               facecolor=COLORS['plasma'],alpha=.22,edgecolor='#5b9ead'))
        ax.set_xlim(-.17,.10);ax.set_ylim(lo[2],hi[2]);ax.set_zlim(lo[1],hi[1])
        ax.set_box_aspect((.27,hi[2]-lo[2],hi[1]-lo[1]));ax.view_init(23,-53)
        ax.set_xlabel('x [m]');ax.set_ylabel('z [m]');ax.set_zlabel('y [m]')
        ax.set_xticks([-.15,0.,.1]);ax.set_yticks([-.2,0.,.2]);ax.set_zticks([-.2,0.,.2])
        ax.set_title(f"{case['strap_count']}-strap actual PEC geometry")
        ax.tick_params(labelsize=7)
    case=shown[0];geo=case['_geometry'];ax=fig.add_subplot(1,3,3)
    gap=geo['gaps'][0];z=(gap['zmin']+gap['zmax'])/2
    draw_boxes_2d(ax,geo,'xy',z)
    ax.set_xlim(gap['xmin']-.022,gap['xmax']+.022)
    ax.set_ylim(gap['ymin']-.035,gap['ymax']+.035)
    ax.set_xlabel('x [m]');ax.set_ylabel('y [m]');ax.set_aspect('equal')
    ax.annotate(f"{1000*(gap['ymax']-gap['ymin']):.0f} mm\nsource gap",
                xy=((gap['xmin']+gap['xmax'])/2,(gap['ymin']+gap['ymax'])/2),
                xytext=(gap['xmax']+.008,gap['ymin']-.015),fontsize=8,
                arrowprops={'arrowstyle':'->','color':COLORS['gap']})
    ax.set_title('Feed gap: actual geometry section')
    fig.suptitle('Finite-thickness straps, galvanic bottom short and volume-current feed',fontsize=13,y=1.04)
    plasma_start=next(r for r in geo['domain_regions'] if r['name']=='plasma')['xmin']
    fig.text(.01,-.03,f'Cutaway display: upper/near wall hidden, other cavity walls transparent. Solver/STEP retain all PEC walls. Blue plane: plasma starts at x = {plasma_start:g} m.',fontsize=8)
    fig.subplots_adjust(wspace=.42)
    return save(fig,'icrf-fem-geometry','Actual single- and double-strap PEC CAD',
                'Geometry read from Netgen solver geometry.json, with source-gap detail. Two walls are hidden only in the cutaway display.')


def draw_boxes_2d(ax,geo,plane,fixedvalue):
    axes={'xy':('x','y','z'),'xz':('x','z','y'),'yz':('y','z','x')}
    first,second,fixed=axes[plane]
    for box in geo['pec_boxes']+geo['gaps']:
        if box[fixed+'min']-1e-8<=fixedvalue<=box[fixed+'max']+1e-8:
            color=COLORS['gap'] if box['label'].startswith('gap_') else COLORS['strap'] if 'strap' in box['label'] or 'return_above' in box['label'] else COLORS['metal']
            ax.add_patch(Rectangle((box[first+'min'],box[second+'min']),
                                  box[first+'max']-box[first+'min'],box[second+'max']-box[second+'min'],
                                  facecolor=color,edgecolor='#fff',linewidth=.25,zorder=3))


def limits_with_load(ax,geo,plane):
    axes={'xy':(0,1),'xz':(0,2),'yz':(1,2)};a,b=axes[plane]
    lo,hi=np.array(geo['outer_bounds'])
    ax.set_xlim(lo[a],hi[a]);ax.set_ylim(lo[b],hi[b]);ax.set_aspect('equal')
    ax.set_xlabel('xyz'[a]+' [m]');ax.set_ylabel('xyz'[b]+' [m]')
    if a==0:
        for region in geo['domain_regions']:
            if region['name'] in ['plasma','absorber']:
                ax.axvline(region['xmin'],color='#f9f9f9',lw=.8,ls='--',zorder=4)


def field_values(case,plane,kind):
    with np.load(case['_dir']/'fields.npz') as data:
        coords=data[plane+'_coords'];values=data[plane+'_'+kind]
        mask=data[plane+'_mask']&np.all(np.isfinite(values),axis=-1)
    power=case['delivered_power_w']
    values=np.sqrt(np.sum(np.abs(values)**2,axis=-1))/np.sqrt(power)
    return coords,np.ma.masked_where(~mask,values)


def mesh_segments(path,plane,fixedvalue):
    from ngsolve import Mesh
    mesh=Mesh(str(path));points=np.zeros((mesh.nv,3))
    for vertex in mesh.vertices:points[vertex.nr]=vertex.point
    directions={'xy':(0,1,2),'xz':(0,2,1),'yz':(1,2,0)};a,b,normal=directions[plane]
    segments=[];edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    for element in mesh.Elements():
        if len(element.vertices)!=4:continue
        tetra=points[[v.nr for v in element.vertices]];dist=tetra[:,normal]-fixedvalue
        if dist.min()>1e-12 or dist.max()<-1e-12:continue
        intersections=[]
        for i,j in edges:
            if abs(dist[i])<1e-12:intersections.append(tetra[i,[a,b]])
            if dist[i]*dist[j]<-1e-24:
                point=tetra[i]+dist[i]/(dist[i]-dist[j])*(tetra[j]-tetra[i]);intersections.append(point[[a,b]])
        if len(intersections)<3:continue
        polygon=np.unique(np.round(intersections,11),axis=0)
        if len(polygon)<3:continue
        center=polygon.mean(axis=0);angle=np.arctan2(polygon[:,1]-center[1],polygon[:,0]-center[0]);polygon=polygon[np.argsort(angle)]
        segments.extend(zip(polygon,np.roll(polygon,-1,axis=0)))
    return segments


def single_figure(case):
    geo=case['_geometry'];fig,axes=plt.subplots(1,2,figsize=(12,4.4))
    plane='xy';coords,values=field_values(case,plane,'E')
    positive=values.compressed();positive=positive[positive>0]
    norm=LogNorm(vmin=max(positive.min(),positive.max()*1e-5),vmax=positive.max())
    image=axes[0].pcolormesh(coords[:,:,0],coords[:,:,1],values,norm=norm,cmap='magma',shading='auto',rasterized=True)
    draw_boxes_2d(axes[0],geo,plane,0.);limits_with_load(axes[0],geo,plane)
    axes[0].set_title(r'Solved $|\mathbf{E}|/\sqrt{P_{\mathrm{in}}}$, $z=0$')
    fig.colorbar(image,ax=axes[0],label='V m$^{-1}$ W$^{-1/2}$',fraction=.035,pad=.025)
    segments=mesh_segments(case['_dir'].parent/'mesh.vol',plane,0.)
    axes[1].add_collection(LineCollection(segments,colors='#456979',linewidths=.35,rasterized=True))
    draw_boxes_2d(axes[1],geo,plane,0.);limits_with_load(axes[1],geo,plane)
    axes[1].set_title('Actual tetrahedra intersected with z = 0')
    fig.suptitle(f"Single strap: {case['nelements']:,} tetrahedra, {case['ndof']:,} complex DOFs",fontsize=13)
    frequency=case['_parameters'].get('frequency_hz',50e6)/1e6
    fig.text(.015,.025,f"{frequency:g} MHz; p={case['order']}; h_max = {case['maxh_m']:.4g} m. Complex-field norm scaled to 1 W delivered gap power. Dashed: plasma/absorber boundaries.",fontsize=8)
    fig.subplots_adjust(left=.06,right=.98,top=.84,bottom=.17,wspace=.30)
    return save(fig,'icrf-fem-single-field','Single-strap Maxwell field and actual tetrahedral mesh',
                'Direct NGSolve field samples and a geometric slice of the Netgen tetrahedral mesh. Fields normalized to one watt of delivered gap-source power, not one watt of core absorption.')


def double_figure(same,opposite):
    cases=[same,opposite];fig=plt.figure(figsize=(12.5,7.3))
    grid=fig.add_gridspec(2,5,width_ratios=[1,.035,.20,1,.035],left=.065,right=.93,
                         top=.88,bottom=.14,wspace=.23,hspace=.48)
    axes=np.array([[fig.add_subplot(grid[row,0]),fig.add_subplot(grid[row,3])] for row in range(2)])
    plane='xz';all_values={}
    for kind in ['E','H']:
        for i,case in enumerate(cases):all_values[(kind,i)]=field_values(case,plane,kind)
    for col,kind in enumerate(['E','H']):
        values_all=np.concatenate([all_values[(kind,i)][1].compressed() for i in range(2)])
        positive=values_all[values_all>0];norm=LogNorm(vmin=max(positive.min(),positive.max()*1e-5),vmax=positive.max())
        for row,case in enumerate(cases):
            coords,values=all_values[(kind,row)]
            image=axes[row,col].pcolormesh(coords[:,:,0],coords[:,:,2],values,norm=norm,cmap='magma' if kind=='E' else 'viridis',shading='auto',rasterized=True)
            draw_boxes_2d(axes[row,col],case['_geometry'],plane,0.);limits_with_load(axes[row,col],case['_geometry'],plane)
            axes[row,col].set_title(f"{case['phase_degree']:g} deg drive: "+rf'$|\mathbf{{{kind}}}|/\sqrt{{P_{{\mathrm{{in}}}}}}$')
        fig.colorbar(image,cax=fig.add_subplot(grid[:,1 if col==0 else 4]),
                     label=('V' if kind=='E' else 'A')+' m$^{-1}$ W$^{-1/2}$')
    fig.suptitle(f"Double strap: 3D Maxwell fields at y = 0 (p={same['order']}, h_max={same['maxh_m']:g} m)",fontsize=13,y=.985)
    fig.text(.04,.02,'Each complex field is divided by sqrt(its solved delivered power). Shared scales within columns; source runs use 1 A peak per gap. PEC is masked.',fontsize=8)
    return save(fig,'icrf-fem-double-fields','Double-strap in-phase and opposite-phase Maxwell E and H fields',
                'Four actual field maps from the two three-dimensional phase excitations, sharing colour scales within each field type and normalized to delivered power.')


def convergence_figure(cases):
    groups={}
    for c in cases:groups.setdefault((c['strap_count'],c['phase_degree'],c['order']),[]).append(c)
    groups={key:sorted(rows,key=lambda c:c['ndof']) for key,rows in groups.items() if len(rows)>=2}
    if not groups:return None
    fig,axes=plt.subplots(1,3,figsize=(13,4.4));styles=['o','s','^','D']
    for index,(key,rows) in enumerate(groups.items()):
        strap,phase,order=key;label=f"{strap} strap, {phase:g} deg, p={order}"
        n=np.array([r['ndof'] for r in rows]);effective=[]
        for r in rows:
            z=np.array(r['Z_ohm']);z=z[...,0]+1j*z[...,1]
            currents=np.array(r['peak_currents_a']);currents=currents[...,0]+1j*currents[...,1]
            effective.append(np.vdot(currents,z@currents)/np.vdot(currents,currents))
        effective=np.array(effective)
        axes[0].plot(n,effective.real,marker=styles[index%4],label=label)
        axes[1].plot(n,effective.imag,marker=styles[index%4],label=label)
        fractions=[r['artificial_absorber_power_w']/r['delivered_power_w'] for r in rows]
        axes[2].plot(n,fractions,marker=styles[index%4],label=label)
    for ax in axes:ax.set_xlabel('Complex DOFs');ax.grid(alpha=.25);ax.ticklabel_format(axis='x',style='sci',scilimits=(0,0))
    axes[0].set_ylabel('Re(Zeffective) [ohm]');axes[1].set_ylabel('Im(Zeffective) [ohm]')
    axes[2].set_ylabel('Artificial absorber / delivered power');axes[2].set_ylim(0,1)
    fig.suptitle('Mesh and element-order study: same geometry, source and load',fontsize=12,y=1.02)
    handles,labels=axes[0].get_legend_handles_labels()
    fig.legend(handles,labels,loc='lower center',bbox_to_anchor=(.5,-.025),ncol=3,frameon=False,fontsize=8)
    fig.tight_layout(rect=[0,.10,1,1])
    return save(fig,'icrf-fem-convergence','Computed mesh-refinement sequence of gap impedance and absorber fraction',
                'Only actually solved meshes are plotted. Effective impedance is I-dagger Z I divided by I-dagger I; artificial absorber fraction is distinct from physical plasma absorption.')


def render(base,additional=()):
    cases=cases_under(base)
    for path in additional:cases.extend(cases_under(path))
    if not cases:raise SystemExit('No completed solver cases with fields.npz found under '+str(base))
    single=finest(cases,1,0.);same=finest(cases,2,0.);opposite=finest(cases,2,180.)
    if same and opposite and (same['order'],same['maxh_m'])!=(opposite['order'],opposite['maxh_m']):
        common={(c['order'],c['maxh_m']) for c in cases if c['strap_count']==2 and c['phase_degree']==0}&{(c['order'],c['maxh_m']) for c in cases if c['strap_count']==2 and c['phase_degree']==180}
        if not common:raise ValueError('Phase comparison requires identical mesh settings and element order.')
        order,h=min(common,key=lambda pair:(pair[1],-pair[0]))
        same=next(c for c in cases if c['strap_count']==2 and c['phase_degree']==0 and c['order']==order and c['maxh_m']==h)
        opposite=next(c for c in cases if c['strap_count']==2 and c['phase_degree']==180 and c['order']==order and c['maxh_m']==h)
    output=[]
    if single or same:output.append(geometry_figure(single,same))
    if single:output.append(single_figure(single))
    if same and opposite:output.append(double_figure(same,opposite))
    convergence=convergence_figure(cases)
    if convergence:output.append(convergence)
    manifest={'input_base':str(base),'additional_input_bases':[str(p) for p in additional],
              'solved_cases':len(cases),'figures':[p.relative_to(ROOT).as_posix() for p in output],
              'data_sha256':{source_name(c['_dir']):{name:hashlib.sha256((c['_dir']/name).read_bytes()).hexdigest() for name in ['fields.npz','results.json']} for c in cases},
              'selected':[{'straps':c['strap_count'],'phase':c['phase_degree'],'maxh_m':c['maxh_m'],'ndof':c['ndof'],'source':str(c['_dir'])} for c in [single,same,opposite] if c]}
    (base/'figure-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    selected_preview=ROOT/'.build/icrf-fem-figures'/('icrf-fem-double-fields.png' if same and opposite else 'icrf-fem-single-field.png')
    if selected_preview.is_file():(base/'preview.png').write_bytes(selected_preview.read_bytes())
    print(json.dumps(manifest,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,default=ROOT/'.build/icrf-fem-final')
    parser.add_argument('--additional-inputs',type=Path,nargs='*',default=[])
    args=parser.parse_args();render(args.input.resolve(),[p.resolve() for p in args.additional_inputs])
