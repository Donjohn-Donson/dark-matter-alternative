---
marp: true
theme: cu-physics-poster
size: poster
paginate: false
math: mathjax
---

<!--
  CU Boulder Physics — MARP Poster Template
  Export with:
    marp --html --allow-local-files poster.md -o poster.pdf

  The --html flag is REQUIRED for the <div> column layout to render.
-->

<!-- ============================================================
     CONFIGURATION — Edit the style variables and header below
     ============================================================ -->

<style>
:root {
  /* Override colors here if needed */
  /* --cu-gold: #CFB87C; */
  /* --cu-black: #000000; */
}
</style>

<!-- ============================================================
     HEADER — Title row + logo/author row
     ============================================================ -->

<div class="poster-header">
  <div class="header-title-row">
    <h1>Can a spatial mass distribution explain Galactic stability?</h1>
  </div>
  <div class="header-info-row">
    <img class="logo-left" src="../assets/Boulder_left_lockup_rev_2025.png" alt="CU Boulder">
    <div class="author-block">
      <div class="authors">Jonah Cooke</div>
      <div class="affiliations"><sup>1</sup>Department of Physics, University of Colorado Boulder &nbsp;&nbsp; <sup>2</sup>JILA, University of Colorado Boulder</div>
    </div>
    <img class="logo-right" src="../assets/Physics_rev_left.png" alt="CU Physics">
  </div>
</div>

<!-- ============================================================
     CONTENT — Three-column layout
     Change columns-3 to columns-2 for a two-column layout
     ============================================================ -->

<div class="content">
<div class="columns-3">

<!-- ======================== COLUMN 1 ======================== -->
<div class="column">

## Introduction
We have found little evendence for what dark matter is, for decades, and the primary piece of evidence, the linear rotation curve of galaxies leaves one wondering if there is a different explination for the behavior. My research explores wether or not a spatial mass distribution can solve the apperent motion. To do this I have modified the 2-body central force lagrangian 

$$\mathcal{L} = \frac{\mu \dot{r}^2}{2}+\frac{\mu r^2\dot{\phi}^2}{2}+\frac{GmM}{r},$$ 
to be defined in terms of a variable mass, $\mu(r)$. 

The idea comes from a feature in plasma physics, a wave traveling through a plasma has a frequency governed by $\omega^2 = \omega_p^2+c^2 k^2$. This is very similar in form to $E^2 = m^2c^4+p^2c^2$, and noting that $\omega_p \propto n$ in this compasison m is proportional to something that is often spatially dependant. A key feature of this is that with conserved omega we find as wavenumber decreases in magnitude the plasma frequency ($\omega_p$) increases. This implies a coupling between mass and momentum, however, einstein's equation cannot account for how masses interact unlike how the equation above can account for light traveling through a plasma, so a more advanced treatment is necisary.

The idea is to modify the above lagrangian, and find via the resulting Euler-Lagrange equations, and experimental data, find a mass distribution that satisfies the observed trajectories then to  see if the mass function predicts trajectories of other observced data!

> **Key Insight:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi accumsan fermentum magna, vel pretium arcu fermentum ac.



</div>

<!-- ======================== COLUMN 2 ======================== -->
<div class="column">


## Methods
### One dimensional case
The first challange was creating a method of pairing a lagrangian to a trajectory, I started by using a modified constant acceleration lagrangian:

$$
\mathcal{L} = -m(z)\sqrt{1-\dot{z}^2},
$$
then pairing this to a known trajectory:
$$
z(t) = \frac{1}{a}\left(\sqrt{a^2t^2+1}-1\right).
$$
Since this trajectory was a solution to the original lagrangian the method would be shown to be correct if the initial lagrangian were recovered. 

**add a brief summery of the method**

 The method recovered the expected Lagrangian and due to a lipshitz condition was unique at all points in space, and at all points in time (barring an expected singularity correspondinding to the rindler horizon).


### Two dimensional case
The one dimensional method maintains the same form as the static mass case throughout the whole of the calculation. The two dimensional case picks up some additional factors and though still  applicible, the method of calculation, relies on an analytic solution to the differential equation, which in the case of this system is unlikely. As a result a guess and check stratagy will be implemented. To this end a Runge-Kutta simulation has been created and tested on several known functions, namely, the newtonian and relativistic cases. The standard proceedure for the two body central foprce equation and the relativistic form is to put the differential equation in the form:

$$
F = -\partial_rV_{eff}(\vec r).
$$
The $V_{eff}(\vec r)$ terms for the newtonian, relativistic and spatial mass all include a centrafugal barrier term of the form $\frac{L^2}{2mr^2}$ and for the relativistic and spatial ODE's a correction term. The three ODE's are of the form,

$$
\begin{aligned}
V_{eff,\:classical} &= -\frac{GM}{r}+\frac{L^2}{2r}\\
V_{eff,\:relativistic} &= -\frac{GM}{r}+\frac{L^2}{2r} - \frac{GML^2}{r^3}\\
V_{eff,\:spatial} &= -\frac{GM}{r}+\frac{L^2}{2r} - \frac{GML^2}{r^3}\\
\end{aligned}
$$

</div>

<!-- ======================== COLUMN 3 ======================== -->
<div class="column">

## Column 3

<div class="references">

## References

1. Author, A. "Title of Article." *Journal Name* **1**, 1–10 (2025).

</div>

<div class="acknowledgments">

**Acknowledgments:** This work was supported by ...

</div>

</div>

</div><!-- end columns-3 -->
</div><!-- end content -->

<!-- ============================================================
     FOOTER
     ============================================================ -->

<div class="poster-footer">
  <span>Joco3414@colorado.edu</span>
  <span>ABC Conference 2026, City</span>
  <span>https://www.colorado.edu</span>
</div>
