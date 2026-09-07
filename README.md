# Space-dependent particle mass as an alternative to dark matter

Honors thesis research by **Jonah Cooke** (Department of Physics, University of
Colorado Boulder). Advisor: **Yuan Shi**, Plasma Quantum Group.

## Idea in one paragraph

Rather than positing a new species of dark matter particle, this project explores
the hypothesis that every particle carries a *universal spatial mass profile*
`m = f · φ(x)`, where `f` is species-specific and `φ(x)` depends only on position.
Near Earth `φ ≈ const`, so local experiments cannot falsify it; on galactic scales
gradients in `φ` become observable and could reproduce the trajectory deviations
normally attributed to dark matter. The analogy comes from plasma physics, where a
photon's dispersion relation `ω² = ω_p² + k²` mirrors `E² = m² + p²`, making the
density-dependent plasma frequency behave as a space-dependent photon mass.

The work proceeds from Yuan Shi's 1D treatment (*Force, Metric, or Mass*,
arXiv:1908.02159) toward the 2D orbital / Schwarzschild case: modifying the
central-force and geodesic Lagrangians for a position-dependent mass, deriving the
effective potential, and testing candidate mass profiles numerically (RK4)
against known Newtonian and relativistic orbits.

## Repository layout

| Path | Contents |
|------|----------|
| `writeups/` | LaTeX documents (source only; build artifacts are git-ignored). Each folder's `.tex` is named after the folder. |
| `writeups/prospectus/` | Thesis prospectus / registration document + bibliography |
| `writeups/q1b-brainstorming/` | Working notes: known results, open questions, uniqueness study |
| `writeups/central-force-generalization/` | Generalization of the 2-body central-force equation |
| `writeups/elliptical-orbit-variable-mass/` | Note on the elliptical-orbit / variable-mass uniqueness issue |
| `writeups/implications-of-dynamic-mass-on-galactic-rotation-curves.pdf` | Compiled summary write-up |
| `presentations/` | Talks and the conference poster |
| `presentations/poster/` | Marp poster (`poster.md`, `poster-v2.md`), theme CSS, exported PDF |
| `presentations/group-pres-1/` | First group-meeting presentation (`group-pres-1.md`, `-v2.md`) |
| `presentations/20-min-pres/` | 20-minute honors-class presentation (Marp + HTML export) |
| `notebooks/` | Jupyter / Wolfram analysis |
| `notebooks/math/` | Symbolic derivations: modified Lagrangians, inverse problem, Schwarzschild, perihelion precession (RK4). Shared helpers in `modified_lagrangian.py` |
| `notebooks/central-force-generalization/` | Companion notebook to the write-up of the same name |
| `notebooks/galaxy-rotation/` | Galaxy rotation-curve models, `orbit-animation-rk4.ipynb`, and generated figures/animation frames |
| `notebooks/solution-attempt/` | Geodesic-solution attempts (`python/` with its own venv + `requirements.txt`, `wolfram/`) |
| `notebooks/scratch/` | Throwaway exploration notebooks |
| `assets/` | Shared images, plots, and videos referenced by write-ups and presentations. All names are lower-case with hyphens (no spaces). |
| `literature/` | Reference papers (PDFs) |

## Building

- **LaTeX:** each `writeups/*/` folder holds one `.tex` file named after the folder
  (e.g. `writeups/prospectus/prospectus.tex`); compile with `latexmk -pdf <file>.tex`.
  The prospectus and Q1B notes use `biber`, so run `latexmk` (or `pdflatex → biber → pdflatex ×2`).
- **Marp presentations:** open the `.md` files with the VS Code Marp extension, or
  export from the CLI, e.g.
  `marp --html --allow-local-files --theme-set presentations/poster/cu-physics-poster.css presentations/poster/poster.md -o presentations/poster/poster.pdf`
- **Notebooks:** `notebooks/solution-attempt/python/` ships a `requirements.txt`;
  recreate its environment with `python -m venv .venv && pip install -r requirements.txt`.
  Other notebooks mainly need `numpy`, `scipy`, `sympy`, and `matplotlib`.

## Notes

- LaTeX build products (`*.aux`, `*.log`, `*.synctex.gz`, …), `__pycache__/`,
  `.venv/`, and `.DS_Store` are git-ignored and were removed from version control
  during the September 2026 reorganization.
- Presentations and `.tex` files still contain relative paths pointing at the old
  layout and old file names; update those links as you touch each file. Asset
  files were renamed to lower-case-with-hyphens so they are safe to reference from
  Marp/HTML without URL-encoding.
