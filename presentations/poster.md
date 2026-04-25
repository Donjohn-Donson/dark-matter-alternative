---
marp: true
theme: cu-physics-poster
size: poster
paginate: false
math: mathjax
---

<!--
  CU Boulder Physics — MARP Poster
  Export:  marp --html --allow-local-files --theme-set themes/cu-physics-poster.css poster.md -o poster.pdf
  The poster canvas is 1587×1680 px (roughly A1 portrait at 96 dpi).
  Preview: VS Code Marp extension — add themes/cu-physics-poster.css to "markdown.marp.themes" in settings.json
-->

<style>
:root {
  --cu-gold:  #CFB87C;
  --cu-black: #000000;
}
</style>

<!-- HEADER -->

<div class="poster-header">
  <div class="header-title-row">
    <h1>Implications of space-dependent particle masses for galaxy spectra</h1>
  </div>
  <div class="header-info-row">
    <img class="logo-left" src="../assets/Boulder_left_lockup_rev_2025.png" alt="CU Boulder">
    <div class="author-block">
      <div class="authors">Jonah Cooke</div>
      <div class="affiliations">
        <sup>1</sup>Department of Physics, University of Colorado Boulder &nbsp;&nbsp;
        Advisor: Yuan Shi &nbsp;&nbsp; Plasma Quantum Group
      </div>
    </div>
    <img class="logo-right" src="../assets/Physics_rev_left.png" alt="CU Physics">
  </div>
</div>

<!-- CONTENT -->

<div class="content">
<div class="columns-3">

<!-- ======================== COLUMN 1 ======================== -->
<div class="column">

## Motivation

In 1980, Vera Rubin published the first substantial evidence for dark matter via galactic rotation curves. Yet no dark-matter particle has been detected. A second, less-discussed mystery is the **lopsidedness of galaxy spectra**: the kinematic center does not overlap with the luminosity center in more than 35% of observed galaxies.

These two anomalies motivate exploring whether an alternate mechanism, a spatially varying particle mass, can reproduce the observed dynamics without invoking unseen matter.

## Hypothesis

All particles share a universal spatial mass profile:
$$m = f\,\phi(\mathbf{x}),$$
where $f$ is particle-species-specific and $\phi(\mathbf{x})$ is a universal function of position. Near Earth, $\phi \approx \text{const}$, so local experiments cannot falsify the hypothesis. On galactic scales, deviations in $\phi$ become observable.

## Plasma Analogy

The inspiration comes from plasma physics. Photons in a plasma satisfy

$$\omega^2 = \omega_p^2 + k^2,$$

which mirrors Einstein's energy-momentum relation $E^2 = m^2 + p^2$. Identifying the photon mass with $\omega_p$ — which depends on local plasma density — shows that a spatially varying density acts as a spatially varying mass. Density gradients cause photon trajectories to curve, interpretable as a mass-gradient effect.

We generalise: if photons acquire an effective space-dependent mass via the medium, other particles (protons, electrons) may be subject to an analogous mechanism on cosmic scales.

> **Key Insight:** A space-dependent mass can produce trajectory deviations that mimic the gravitational effects attributed to dark matter, without requiring new particles.

</div>

<!-- ======================== COLUMN 2 ======================== -->
<div class="column">

## Methods

### One-Dimensional Case

To build the method, we start from a modified relativistic Lagrangian with a variable mass:

$$\mathcal{L} = -m(z)\sqrt{1-\dot{z}^2}.$$

This is paired with the constant-proper-acceleration trajectory

$$z(t) = \frac{1}{a}\!\left(\sqrt{a^2t^2+1}-1\right).$$

Using the Euler-Lagrange equations and the known trajectory, we invert the problem to recover $m(z)$. The method is validated because it exactly recovers the original (constant) mass. A Lipschitz condition guarantees **uniqueness** at every point in space and time, with an expected singularity at the Rindler horizon.

### Two-Dimensional Orbital Case

For orbital mechanics, the modified central-force Lagrangian is

$$\mathcal{L} = \frac{\mu(r)\,\dot{r}^2}{2}+\frac{\mu(r)\,r^2\dot{\phi}^2}{2}+\frac{GmM}{r},$$

where $\mu(r)$ is the position-dependent reduced mass. The Euler-Lagrange equations reduce to an ODE for $\mu(r)$ given an observed trajectory. Analytic inversion is generally intractable, so we compare candidate mass profiles by integrating the equations of motion with a **4th-order Runge-Kutta** scheme.

The effective potentials for the three cases take the form:

$$V_{\text{eff},\,\text{classical}} = -\frac{GM}{r}+\frac{L^2}{2\mu r^2}$$

$$V_{\text{eff},\,\text{relativistic}} = -\frac{GM}{r}+\frac{L^2}{2\mu r^2} - \frac{GML^2}{\mu r^3}$$

$$V_{\text{eff},\,\text{spatial}} = -\frac{GM}{r}+\frac{L^2}{2\mu(r)\,r^2} - \frac{GML^2}{\mu(r)\,r^3}$$

The RK4 integrator has been tested against known newtonian and relativistic analytic solutions.

</div>

<!-- ======================== COLUMN 3 ======================== -->
<div class="column">

## Results & Progress

- **1D case complete.** Recovered the expected Lagrangian from an observed trajectory; uniqueness proved via Lipschitz condition.
- **2D non-relativistic potential derived.** Found the modified $V_{\text{eff}}$ for the spatial-mass case and implemented RK4 simulation validated on classical and relativistic orbits.
- Analytic two-dimensional solution under investigation via a modified Schwarzschild action.

## Timeline

| Period | Milestone |
|--------|-----------|
| Nov – Feb | Reproduced 1D case; uniqueness proof |
| Mar – Apr | 2D non-relativistic modified potential |
| May | Mass distribution form + matching trajectory |
| Jun – Jul | Analytic or numerical form; compare to observational data |
| Aug | Begin thesis writing |

<div class="references">

## References

1. Rubin, V. C. *et al.* "Rotational Properties of 21 Sc Galaxies." *ApJ* **238**, 471 (1980).
2. Jog, C. J. & Combes, F. "Lopsided Spiral Galaxies." *Phys. Rep.* **471**, 75 (2009).
3. Shi, Y. "Force from a Metric with a Space-Dependent Mass." *arXiv:2103.XXXXX* (2021).
4. Hackmann, E. *et al.* "Complete Analytic Solution of the Geodesic Equation in Schwarzschild Spacetime." *PRL* **100**, 171101 (2008).

</div>

<div class="acknowledgments">

**Acknowledgments:** Research conducted under the supervision of Prof. Yuan Shi, Plasma Quantum Group, Department of Physics, University of Colorado Boulder.

</div>

</div>

</div><!-- end columns-3 -->
</div><!-- end content -->

<!-- FOOTER -->

<div class="poster-footer">
  <span>Joco3414@colorado.edu</span>
  <span>CU Boulder Physics — Spring 2026</span>
  <span>colorado.edu/physics</span>
</div>
