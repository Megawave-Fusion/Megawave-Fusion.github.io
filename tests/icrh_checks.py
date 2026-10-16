#!/usr/bin/env python3
"""Independent ICRH teaching benchmarks; no third-party dependencies.

Run: python3 tests/icrh_checks.py
This tests prescribed-field nonrelativistic particle motion and ideal RF port
accounting. It does not establish a device's wave propagation, deposition,
antenna loading, confinement, or heating efficiency. No network is needed to run.
Source formulas and CODATA entries were checked online on 2026-10-16.
"""
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E_CHARGE = 1.602176634e-19  # C, exact SI
SPECIES = {
    "H+ (proton)": {"Z": 1, "A": 1, "mass_kg": 1.67262192595e-27},
    "D+ (deuteron)": {"Z": 1, "A": 2, "mass_kg": 3.3435837768e-27},
    "T+ (triton)": {"Z": 1, "A": 3, "mass_kg": 5.0073567512e-27},
    "He3++ (helion)": {"Z": 2, "A": 3, "mass_kg": 5.0064127862e-27},
    "He4++ (alpha)": {"Z": 2, "A": 4, "mass_kg": 6.6446573450e-27},
}
SOURCES = [
    {"url": "https://physics.nist.gov/cuu/Constants/Table/allascii.txt",
     "location": "2022 CODATA: elementary charge; proton, deuteron, triton, helion, alpha particle masses; nucleus/proton mass ratios",
     "use": "Bare nuclear masses, not neutral-atom masses or spin gyromagnetic ratios."},
    {"url": "https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/8ee3d6b6b57fa2c78ef138bb44713c33_chap2.pdf",
     "location": "Hutchinson, Chapter 2, Eqs. 2.1, 2.7-2.10; section 2.8 oscillating E field",
     "use": "Cartesian Lorentz signs, magnetic force does no work, forced gyro-motion. Circular transient solution derived by integrating factor here."},
    {"url": "https://farside.ph.utexas.edu/teaching/plasma/lectures1/node97.html",
     "location": "Electrostatic Waves, Eq. 7.117 orbit phase and Eq. 7.119 resonant denominator",
     "use": "omega - k_parallel v_parallel - n Omega resonance; kinematic resonance alone does not establish EM heating efficiency."},
    {"url": "https://space.physics.uiowa.edu/plasma-wave/polar/intro.html",
     "location": "Introduction, paragraphs on characteristic frequencies and resonant wave-particle interactions",
     "use": "Independent published-author source for f_c and Doppler resonance; energy-exchange direction depends on distribution."},
    {"url": "https://ximera.osu.edu/electromagnetics/electromagnetics/impedanceMatching/digInPoweronTL",
     "location": "Power Transfer on a transmission line, voltage/current traveling waves, incident/reflected/load power and load reflection coefficient",
     "use": "Lossless line, real positive reference impedance, peak phasors; reflected current has a minus sign."},
    {"url": "https://web.mit.edu/6.013_book/www/chapter14/14.6.html",
     "location": "Electromagnetic Fields and Energy, section 14.6, Standing Wave Ratio, Eqs. 9-10",
     "use": "Voltage envelope maximum/minimum and VSWR in terms of the reflection coefficient."},
]
checks = []


def check(name, actual, expected, *, rtol=1e-9, atol=0.0, evidence=None):
    passed = math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol)
    record = dict(name=name, actual=actual, expected=expected,
                  relative_tolerance=rtol, absolute_tolerance=atol, passed=passed)
    if evidence is not None:
        record["evidence"] = evidence
    checks.append(record)


def condition(name, passed, evidence):
    checks.append(dict(name=name, passed=bool(passed), evidence=evidence))


def rk4_step(t, y, dt, rhs):
    """Time-dependent Cartesian ODE integrator, independent of complex solution."""
    a = rhs(t, y)
    b = rhs(t + dt / 2, [v + dt * x / 2 for v, x in zip(y, a)])
    c = rhs(t + dt / 2, [v + dt * x / 2 for v, x in zip(y, b)])
    d = rhs(t + dt, [v + dt * x for v, x in zip(y, c)])
    return [v + dt * (aa + 2 * bb + 2 * cc + dd) / 6
            for v, aa, bb, cc, dd in zip(y, a, b, c, d)]


def orbit_frequency(charge, mass, field):
    """Measure a full turn by interpolated vy zero crossing, fixed SI time step."""
    def rhs(t, y):
        return [charge * field * y[1] / mass,
                -charge * field * y[0] / mass]
    dt = 1e-11
    y = [1e5, 0.0]
    crossed_half = False
    for j in range(10000):
        following = rk4_step(j * dt, y, dt, rhs)
        if y[1] < 0 <= following[1]:
            crossed_half = True
        if crossed_half and y[1] > 0 >= following[1]:
            period = (j + y[1] / (y[1] - following[1])) * dt
            return 1 / period
        y = following
    raise RuntimeError("No full gyro-orbit in the integration window")


frequency_table = []
for label, s in SPECIES.items():
    fc = s["Z"] * E_CHARGE * 5 / (2 * math.pi * s["mass_kg"])
    measured = orbit_frequency(s["Z"] * E_CHARGE, s["mass_kg"], 5)
    check(f"{label}: analytic frequency vs Cartesian orbit at 5 T [Hz]",
          measured, fc, rtol=2e-8)
    frequency_table.append(dict(species=label, mass_kg=s["mass_kg"],
                                Z=s["Z"], A=s["A"], f_MHz_per_T=fc / 5e6))

# A second constants route: CODATA tabulated nuclear/proton mass ratios.
# This is a cross-check of units/species/rounding, not an independent measurement.
codata_ratio = {"D+ (deuteron)": 1.9990075012699,
                "T+ (triton)": 2.99371703403,
                "He3++ (helion)": 2.993152671552,
                "He4++ (alpha)": 3.972599690252}
mp = SPECIES["H+ (proton)"]["mass_kg"]
ratios = []
for label, mass_ratio in codata_ratio.items():
    s = SPECIES[label]
    exact = s["Z"] * mp / s["mass_kg"]
    approximate = s["Z"] / s["A"]
    ratios.append(dict(species=label, exact_frequency_ratio_to_H=exact,
                       from_tabulated_mass_ratio=s["Z"] / mass_ratio,
                       Z_over_A_approximation=approximate,
                       approximation_relative_error=(approximate - exact) / exact))
condition("Same-B frequency ratios: tabulated mass-ratio route and finite Z/A approximation error",
          all(math.isclose(r["exact_frequency_ratio_to_H"], r["from_tabulated_mass_ratio"], rel_tol=1e-10)
              and abs(r["approximation_relative_error"]) < .008 for r in ratios), ratios)

# Doppler phase is sampled along z(t)=v_parallel*t, without substituting the
# resonance formula into the sampled field; the small interval prevents wrapping.
omega_rf = 2 * math.pi * 40e6
k_parallel = 5.0  # rad/m, SI dimension m^-1
v_parallel = 3e5  # m/s
t0, phase_dt = 2.3e-8, 1e-11
wave = lambda t: cmath.exp(1j * (k_parallel * (v_parallel * t) - omega_rf * t))
sampled_frequency = -cmath.phase(wave(t0 + phase_dt) / wave(t0)) / phase_dt
check("Doppler frequency from electric-field phase sampled along moving orbit [rad/s]",
      sampled_frequency, omega_rf - k_parallel * v_parallel, rtol=1e-11)


def bisect(fn, lo, hi):
    flo = fn(lo)
    if flo * fn(hi) > 0:
        raise ValueError("Root not bracketed")
    for _ in range(80):
        mid = (lo + hi) / 2
        if fn(mid) * flo > 0:
            lo, flo = mid, fn(mid)
        else:
            hi = mid
    return (lo + hi) / 2


md = SPECIES["D+ (deuteron)"]["mass_kg"]
b0, r0 = 5.0, 3.0
layer_table = []
for vp in [-v_parallel, 0.0, v_parallel]:
    # B(R)=B0*R0/R is a deliberately prescribed vacuum-toroidal approximation.
    # Solve the local phase mismatch independently by bisection.
    radius = bisect(lambda r: omega_rf - k_parallel * vp
                    - E_CHARGE * b0 * r0 / (md * r), .5, 10)
    formula = E_CHARGE * b0 * r0 / (md * (omega_rf - k_parallel * vp))
    check(f"Doppler-shifted D fundamental 1/R layer, v_parallel={vp:g} [m]",
          radius, formula, rtol=1e-13)
    layer_table.append(dict(v_parallel_m_s=vp, radius_m=radius))
r_fundamental = layer_table[1]["radius_m"]
r_second = bisect(lambda r: omega_rf - 2 * E_CHARGE * b0 * r0 / (md * r), 1, 10)
condition("1/R resonance layer moves outward for positive kv; second-harmonic radius doubles",
          layer_table[0]["radius_m"] < r_fundamental < layer_table[2]["radius_m"]
          and math.isclose(r_second, 2 * r_fundamental, rel_tol=1e-13),
          {"layers": layer_table, "second_harmonic_radius_m": r_second,
           "limitation": "Kinematic condition only; no assertion that a harmonic couples or lies inside a particular plasma."})

q, mass, bfield, e0 = E_CHARGE, md, 5.0, 1000.0
gyro = q * bfield / mass
accel = q * e0 / mass


def forced_solution(t, drive_omega):
    """w=vx+i*vy, E=(E0 cos(wt), -E0 sin(wt)); w(0)=0."""
    delta = gyro - drive_omega
    if abs(delta) < 1e-12 * gyro:
        return accel * t * cmath.exp(-1j * gyro * t)
    return accel * (cmath.exp(-1j * drive_omega * t)
                    - cmath.exp(-1j * gyro * t)) / (1j * delta)


def integrate_forced(drive_ratio, tau_end, steps=10000, linear=False):
    drive_omega = drive_ratio * gyro
    end_time = tau_end / gyro
    dt = end_time / steps
    # W independently integrates q E dot v. The magnetic term is retained in
    # the velocity equation, never included as an energy source.
    def rhs(t, y):
        ex = e0 * math.cos(drive_omega * t)
        ey = 0.0 if linear else -e0 * math.sin(drive_omega * t)
        return [q * ex / mass + gyro * y[1],
                q * ey / mass - gyro * y[0],
                q * (ex * y[0] + ey * y[1])]
    y = [0.0, 0.0, 0.0]
    for j in range(steps):
        y = rk4_step(j * dt, y, dt, rhs)
    return complex(y[0], y[1]), y[2], end_time


forced_cases = [("co-rotating resonant", 1.0, False),
                ("co-rotating detuned", .77, False),
                ("counter-rotating at positive cyclotron frequency", -1.0, False),
                ("linear polarization, sum of two half-amplitude rotations", 1.0, True)]
for label, ratio, linear in forced_cases:
    numerical, work, t = integrate_forced(ratio, 37.2, linear=linear)
    analytic = forced_solution(t, ratio * gyro)
    if linear:
        analytic = .5 * (analytic + forced_solution(t, -ratio * gyro))
    error = abs(numerical - analytic) / max(abs(analytic), e0 / bfield)
    check(f"Forced Lorentz initial-value solution: {label} (relative vector error)",
          error, 0, atol=2e-8,
          evidence={"numerical_velocity_m_s": [numerical.real, numerical.imag],
                    "analytic_velocity_m_s": [analytic.real, analytic.imag],
                    "time_s": t, "initial_velocity_m_s": [0, 0]})

coarse, _, t = integrate_forced(.77, 37.2, 1000)
fine, _, _ = integrate_forced(.77, 37.2, 2000)
truth = forced_solution(t, .77 * gyro)
ratio_errors = abs(coarse - truth) / abs(fine - truth)
condition("Direct forced-orbit integration has fourth-order step-size convergence",
          14 < ratio_errors < 18,
          {"coarse_relative_error": abs(coarse - truth) / abs(truth),
           "fine_relative_error": abs(fine - truth) / abs(truth),
           "error_ratio_for_halved_time_step": ratio_errors})

velocity, electric_work, _ = integrate_forced(1, 37.2)
kinetic_energy = mass * abs(velocity) ** 2 / 2
check("Direct electric-work integral equals kinetic energy, with static B doing zero work [J]",
      electric_work, kinetic_energy, rtol=2e-9)
v_short, _, _ = integrate_forced(1, 9.4)
v_long, _, _ = integrate_forced(1, 18.8)
check("Resonant zero-initial-velocity kinetic energy scales as t squared",
      abs(v_long) ** 2 / abs(v_short) ** 2, 4, rtol=1e-9)
beat_velocity, _, _ = integrate_forced(.77, 2 * math.pi / .23)
check("Detuned driven orbit returns to zero velocity at one beat period [m/s]",
      abs(beat_velocity), 0, atol=2e-6,
      evidence={"meaning": "Finite-time reversible single-particle exchange, not irreversible ensemble heating."})


def period_average(fn, samples=20000):
    # Equally spaced periodic trapezoidal quadrature, including neither duplicate
    # endpoint. Evaluates real instantaneous fields rather than phasor products.
    return sum(fn(2 * math.pi * j / samples) for j in range(samples)) / samples


z0, load, v_forward = 50.0, complex(30, 20), 1000.0
gamma = (load - z0) / (load + z0)
v_load = v_forward * (1 + gamma)
i_load = v_forward / z0 * (1 - gamma)
p_forward = v_forward ** 2 / (2 * z0)
p_reflected = abs(gamma) ** 2 * p_forward
p_load = .5 * (v_load * i_load.conjugate()).real
real_v = lambda phase: (v_load * cmath.exp(-1j * phase)).real
real_i = lambda phase: (i_load * cmath.exp(-1j * phase)).real
v_rms = math.sqrt(period_average(lambda phase: real_v(phase) ** 2))
i_rms = math.sqrt(period_average(lambda phase: real_i(phase) ** 2))
check("RMS voltage/current from real waveforms equal peak phasor magnitudes / sqrt(2)",
      max(abs(v_rms / (abs(v_load) / math.sqrt(2)) - 1),
          abs(i_rms / (abs(i_load) / math.sqrt(2)) - 1)), 0, atol=1e-12)
average_vi = period_average(lambda phase: real_v(phase) * real_i(phase))
p_rms = ((v_load / math.sqrt(2)) * (i_load / math.sqrt(2)).conjugate()).real
p_power_factor = v_rms * i_rms * math.cos(cmath.phase(load))
condition("Complex-load real power: instantaneous VI average = peak and RMS phasor conventions [W]",
          all(math.isclose(value, average_vi, rel_tol=1e-12)
              for value in [p_load, p_rms, p_power_factor]),
          {"waveform_average_W": average_vi, "peak_phasor_power_W": p_load,
           "RMS_phasor_power_W": p_rms, "RMS_times_power_factor_W": p_power_factor,
           "power_factor": math.cos(cmath.phase(load)),
           "apparent_power_VA": v_rms * i_rms})

rf_cases = []
for label, reflection in [("complex passive load", gamma),
                          ("matched load", 0j), ("short", -1 + 0j),
                          ("open-circuit limit", 1 + 0j),
                          ("pure reactive load", (20j - z0) / (20j + z0))]:
    v = v_forward * (1 + reflection)
    current = v_forward / z0 * (1 - reflection)
    direct = period_average(lambda phase: (v * cmath.exp(-1j * phase)).real
                            * (current * cmath.exp(-1j * phase)).real, 4000)
    wave_budget = p_forward * (1 - abs(reflection) ** 2)
    rf_cases.append(dict(case=label, waveform_power_W=direct,
                         traveling_wave_budget_W=wave_budget))
condition("Lossless real-Z0 forward/reflected power budget, including no-absorption limits",
          all(math.isclose(r["waveform_power_W"], r["traveling_wave_budget_W"],
                           rel_tol=1e-12, abs_tol=1e-9) for r in rf_cases), rf_cases)
check("Load reconstructed from total V/I includes the reflected-current minus sign [ohm]",
      abs(v_load / i_load - load), 0, atol=1e-12,
      evidence={"Gamma_real": gamma.real, "Gamma_imag": gamma.imag,
                "reflected_power_fraction": abs(gamma) ** 2,
                "forward_W": p_forward, "reflected_W": p_reflected,
                "accepted_W": p_load})
envelope = [abs(cmath.exp(-1j * phase) + gamma * cmath.exp(1j * phase))
            for phase in [math.pi * j / 20000 for j in range(20000)]]
check("Standing-wave voltage extrema vs reflection-coefficient VSWR",
      max(envelope) / min(envelope), (1 + abs(gamma)) / (1 - abs(gamma)), rtol=1e-7)

# Same matched input resistance and accepted power, different destinations.
# In the second circuit all real resistance is hardware loss. No port measurement
# can infer plasma absorption without an additional loss/deposition model.
matched_peak_current = 1000 / 50
budgets = []
for r_hardware, r_plasma in [(5.0, 45.0), (50.0, 0.0)]:
    hardware = .5 * matched_peak_current ** 2 * r_hardware
    plasma = .5 * matched_peak_current ** 2 * r_plasma
    budgets.append(dict(hardware_loss_W=hardware, plasma_absorbed_W=plasma,
                        port_accepted_W=10000.0, reflection_coefficient=0.0))
condition("Zero reflection does not determine plasma absorption: two explicit matched budgets",
          all(math.isclose(x["hardware_loss_W"] + x["plasma_absorbed_W"],
                           x["port_accepted_W"]) for x in budgets)
          and budgets[0]["plasma_absorbed_W"] != budgets[1]["plasma_absorbed_W"], budgets)

passed = all(item["passed"] for item in checks)
report = {
    "date": "2026-10-16", "result": "passed" if passed else "failed",
    "count": len(checks), "checks": checks, "sources": SOURCES,
    "constants": {"edition": "NIST 2022 CODATA", "elementary_charge_C": E_CHARGE,
                  "isotopes": SPECIES},
    "frequency_table": frequency_table,
    "conventions": {
        "SI": "omega and Omega in rad/s; f in Hz; k_parallel in rad/m; all masses kg; B tesla",
        "orbit": "B=B0 zhat; positive ion Omega=qB/m>0; w=vx+i vy; E=(E0 cos(omega t), -E0 sin(omega t)); v(0)=0",
        "phasors": "Real field Re[phasor exp(-i omega t)]; stated voltage/current phasors are peak, RMS=peak/sqrt(2)",
        "line": "Single propagating mode, lossless line and real positive Z0; powers referenced to the same plane",
    },
    "limitations": [
        "Numerical tests cover the explicitly listed benchmarks, not every statement in the knowledge base.",
        "Prescribed spatially uniform RF electric field and static B; nonrelativistic, collisionless test particle, no self-consistent fields or radiation.",
        "Resonant t-squared growth is a finite-time ideal initial-value result, not an unlimited practical heating law.",
        "B(R)=B0 R0/R is an assumed vacuum-toroidal magnitude approximation; Doppler layer roots do not include orbit width, poloidal field, equilibrium changes, or damping.",
        "Port acceptance and circuit losses do not establish core deposition, minority heating, species partition, or device efficiency.",
        "CODATA mass ratios are a consistency route, not statistically independent constants measurements.",
    ],
}
output = ROOT / ".build/reviews/icrh-checks.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(f"{sum(x['passed'] for x in checks)}/{len(checks)} ICRH checks passed -> {output.relative_to(ROOT)}")
if not passed:
    for item in checks:
        if not item["passed"]:
            print(json.dumps(item, ensure_ascii=False))
    raise SystemExit(1)
