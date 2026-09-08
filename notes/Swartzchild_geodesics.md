# Analytic Solutions to Radial Schwarzschild Geodesics

*Information gathered from a Feynman CLI session (2026-09-08). Diagnostic/error output omitted; only the substantive answer is retained.*

**Question:** Are there analytic solutions to the radial Schwarzschild geodesics?

---

Yes — the purely radial case is the one corner of Schwarzschild geodesics where everything closes in **elementary** functions (no elliptic functions needed). The general non-radial case needs the Weierstrass $\wp$ function.

## Setup

With $f(r) = 1 - r_s/r$, $r_s = 2GM/c^2$, and $L = 0$, the conserved energy is $E = f\,\dot t$ and normalization gives the exact first integral

$$\left(\frac{dr}{d\tau}\right)^2 = E^2 - f(r) = E^2 - 1 + \frac{r_s}{r}$$

This is *identical in form* to the Newtonian radial Kepler energy equation — hence the Kepler-like closed forms. Note $r_s/r$ appears with no correction: radial GR infall in proper time is exactly Newtonian in this variable.

## Proper-time solutions $r(\tau)$

**Marginally bound, $E = 1$** (dropped from rest at infinity) — fully explicit:

$$r(\tau) = \left(r_0^{3/2} - \tfrac{3}{2}\sqrt{r_s}\,\tau\right)^{2/3}, \qquad \tau = \frac{2}{3\sqrt{r_s}}\left(r_0^{3/2} - r^{3/2}\right)$$

**Bound, $E < 1$** (released from rest at $r_0$, so $E^2 = 1 - r_s/r_0$) — cycloid, parametric in $\eta$:

$$r = \frac{r_0}{2}(1 + \cos\eta), \qquad \tau = \sqrt{\frac{r_0^3}{4 r_s}}\,(\eta + \sin\eta)$$

Total proper time from $r_0$ to the singularity: $\tau = \pi\sqrt{r_0^3 / (4 r_s)}$ — finite, and the horizon is unremarkable.

**Unbound, $E > 1$** — hyperbolic analogue with $a = r_s / (E^2 - 1)$:

$$r = \frac{a}{2}(\cosh\eta - 1), \qquad \tau = \frac{a}{2}\sqrt{\frac{a}{r_s}}\,(\sinh\eta - \eta)$$

**Numerical verification:** all three checked against direct high-accuracy numerical integration of $dr/d\tau = -\sqrt{E^2 - 1 + r_s/r}$ ($r_s = 1$, $r_0 = 10$, `scipy solve_ivp`, rtol $10^{-12}$): max $|r_{\rm num} - r_{\rm analytic}| \approx 6\times10^{-11}$ ($E<1$), $5\times10^{-10}$ ($E=1$), $9\times10^{-10}$ ($E>1$).

**Caveat:** for $E \neq 1$ the solution is *parametric*. Inverting $\tau(\eta)$ to get $r(\tau)$ in elementary form is the Kepler-equation problem — transcendental, no elementary inverse. Only $E = 1$ gives explicit $r(\tau)$.

## Coordinate time $t(r)$

Also elementary, via $dt/dr = -E / \big(f\sqrt{E^2 - f}\big)$. For $E = 1$:

$$\frac{t}{r_s} = \text{const} - \frac{2}{3}\left(\frac{r}{r_s}\right)^{3/2} - 2\left(\frac{r}{r_s}\right)^{1/2} + \ln\left|\frac{\sqrt{r/r_s} + 1}{\sqrt{r/r_s} - 1}\right|$$

The log diverges as $r \to r_s$: infinite coordinate time, finite proper time. For general $E$, $t(\eta)$ is still elementary (polynomial/trig-in-$\eta$ terms plus $\operatorname{artanh}$ / log terms).

**Radial null geodesics** are trivial: $t = \pm r_* + \text{const}$ with the tortoise coordinate $r_* = r + r_s \ln|r/r_s - 1|$.

## Contrast: non-radial

Once $L \neq 0$, $(dr/d\phi)^2$ becomes a quartic/cubic in $u = 1/r$ and the solution is elliptic: $u(\phi) = \frac{1}{4}\wp(\phi; g_2, g_3) + \ldots$ (Droste 1916, Hagihara 1931). Complete modern classifications and explicit $\wp$-formulas: Hackmann & Lämmerzahl and successors.

## Practical note for the `dark-matter-alternative` repo

The elementary radial solutions survive only because $E^2 - f(r)$ is a quadratic-in-$1/r$ form. If a modified metric has $f(r) = 1 - r_s/r + \alpha r^2$ (dS-like), $-\Lambda$ terms, or $+q^2/r^2$, you land in cubic/quartic territory and the radial solution itself becomes elliptic (Weierstrass $\wp$ in $\tau$). Logarithmic or MOND-like $f(r)$ terms generally kill closed form entirely. Worth knowing which family an ansatz falls into before committing to numerics.

## Sources

- *Revisiting timelike and null geodesics in the Schwarzschild spacetime* (2022) — arXiv:2203.12401 — <https://arxiv.org/abs/2203.12401>
- *Timelike and null geodesics in the Schwarzschild space-time: analytical solutions* (2023) — arXiv:2304.12823 — <https://arxiv.org/abs/2304.12823>
- Hackmann & Lämmerzahl, geodesics in Schwarzschild–(A)dS via $\wp$ — arXiv:1009.6117 — <https://arxiv.org/abs/1009.6117>
- *Complete set of solutions, Schwarzschild-type spacetimes* — arXiv:0912.2327 — <https://arxiv.org/abs/0912.2327>
- Textbook: MTW *Gravitation* §25.5 (cycloid infall); Chandrasekhar, *Mathematical Theory of Black Holes* Ch. 3.
