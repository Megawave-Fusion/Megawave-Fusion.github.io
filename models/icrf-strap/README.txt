ICRF single/double strap — actual 3D Maxwell finite-element baseline
================================================================

The model was meshed and solved with NGSolve/Netgen 6.2.2606 on
2026-11-12. This package contains the geometry, actual tetrahedral mesh,
complex E/H results and mesh-study data, not just an array-factor calculation.
All lengths are SI metres. Fields and source currents are PEAK phasors with
exp(-i omega t). The supplied geometry is a flat, deliberately reduced model;
it is not the CAD or an experimentally validated prediction of WEST/AUG/ITER.

Contents
--------
solve.py                 Geometry + cold tensor + Maxwell assembly/solve/export
requirements.txt         Exact package versions used for this run
results-summary.json     Nine second-order cases plus nine first-order study rows
single/, double/         Actual finest-model output, grouped by geometry
  parameters.json        Frequency, geometry, source, density, collision, ABL
  pec-metal.step         Connected strap/short/feed-return/cavity solid
  field-domain.step      Meshed vacuum, gap, plasma and absorbing domains
  geometry.json          Named boundaries/materials/volumes/connectivity checks
  mesh.vol               Netgen volume mesh used by the selected solutions
  phase-0/               In-phase (or single-strap) solution
  phase-180/             Double-strap opposite-phase solution, when present
    field.vtu            E/H real and imaginary parts, magnitude, mesh
    E.sol                Full native complex Hcurl GridFunction
    fields.npz           Physical-plane samples for plots; no analytic pattern
    results.json         Source work, gap Z matrix, loss terms and residuals
SHA256SUMS.txt            File content hashes

Reproduce
---------
In the repository root, use an optional environment for the field solver:

  python3 -m venv .venv-fem
  .venv-fem/bin/python -m pip install -r models/icrf-strap/requirements.txt
  .venv-fem/bin/python models/icrf-strap/solve.py --straps 1 --order 2 --maxh .075 .055 .04 --out .build/icrf-fem-final-single-p2
  .venv-fem/bin/python models/icrf-strap/solve.py --straps 2 --order 2 --maxh .075 .055 .04 --out .build/icrf-fem-final-p2
  .venv-fem/bin/python scripts/render_icrf_fem.py --input .build/icrf-fem-final-single-p2 --additional-inputs .build/icrf-fem-final-p2

To also reproduce the preliminary order-one convergence curves, repeat the
two solve commands with --order 1 --maxh .1 .075 .055 and separate output
directories, then supply those directories as --additional-inputs to the
renderer. Their actual scalar results are archived in
results-summary.json under first_order_mesh_study. Full field/mesh files in
the ZIP are the selected finest order-two cases, not all preliminary runs.

Outside the repository, install requirements.txt and run solve.py directly.
For geometry/field inspection, open STEP in a CAD tool and field.vtu in
ParaView. The VTU uses linear visualization samples; the order-two solution
is preserved in E.sol and can be re-sampled from the original mesh/space.

Example for loading a native field (working directory: unpacked package):

  from ngsolve import Mesh, HCurl, GridFunction
  mesh = Mesh('single/mesh.vol')
  fes = HCurl(mesh, order=2, complex=True,
              dirichlet='outer_pec|metal_pec')
  E = GridFunction(fes)
  E.Load('single/phase-0/E.sol')

Physical model and source
-------------------------
Finite-thickness PEC straps are shorted to the bottom of the cavity. The
upper end is separated from the grounded return by a 12 mm vacuum source
gap. A uniform impressed current density in this gap is normalized to an
integrated current amplitude of 1 A. Both ends of the gap terminate on PEC;
its four lateral faces are vacuum/material interfaces. The code checks all
exterior face descriptors and the connected PEC-solid count before solving.

The voltage is the negative work-conjugate gap integral Vp=-int(E.gp)dV,
where Jext=sum(Ip gp) and each gp has unit transverse integral. It is NOT a
coax TEM-wave port. The stored Z matrix is this generalized gap impedance;
the model does not claim coax S11 or include a matching generator network.

The cold response is calculated from electrons and singly charged deuterons,
B=2 T along +z, ne=ni=2e18/m3, f=50 MHz, and prescribed nu/omega=0.025 for
both species. That collision ratio is a phenomenological input, not a
measured or self-consistent classical collision estimate. No thermal/FLR
response, RF sheath, Faraday screen, copper loss or real wall curvature is
included in these baseline runs.

The external rectangular box is PEC. A ramp i*80*((x-.45)/.20)^2 times the
identity tensor is added in the outer load from x=.45 to .65 m. Its loss is
reported separately from the prescribed cold-collision loss. This is a
finite-box absorber baseline, not a verified infinite-domain PML model.

Delivered power = -0.5 Re int(E.Jext*) dV
                = 0.5 Re(I-dagger Z I)
                = cold-collision loss + artificial-absorber loss.

Numerical accuracy
------------------
Order-one preliminary solutions showed large mesh dependence. The supplied
primary fields use order-two Hcurl elements, maxh=.04 m, and local gap mesh
control .015 m. The previous two order-two maxh values were .075 and .055 m.
The last two meshes change delivered power by 5.51% (single), 4.29% (double
in phase), 1.50% (double opposite phase), relative to the finest value.
These are observed mesh changes, not certified upper error bounds or a
claim of one-percent grid independence. Sharp-edge local maxima require
separate geometric/mesh refinement. Algebraic residual and power closure
near roundoff do not remove this discretization uncertainty.
