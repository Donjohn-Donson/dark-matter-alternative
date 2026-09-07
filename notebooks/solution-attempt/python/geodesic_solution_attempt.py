"""Symbolic solution attempt for the dark-matter-alternative ODE.

Converted from geodesic-solution-attempt.ipynb so it can run in a plain virtual
environment without Jupyter. Results are printed to the terminal as pretty-printed
sympy (and as LaTeX for pasting into a document).

Run:
    python geodesic_solution_attempt.py
"""

import sys

import sympy as sp

# Windows terminals default to cp1252, which can't encode sympy's pretty-print
# box characters. Force UTF-8 output where the stream supports it.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

sp.init_printing(use_unicode=True)


def show(label, expr):
    """Print `expr` with a text label, both pretty-printed and as LaTeX."""
    print(f"\n{label}:")
    try:
        sp.pprint(expr)
    except UnicodeEncodeError:
        sp.pprint(expr, use_unicode=False)
    print(f"LaTeX: {sp.latex(expr)}")


# --- symbols and functions ---
r = sp.symbols("r", positive=True)
rs, L, E = sp.symbols("r_s L E", positive=True)
t = sp.symbols("t")

m = sp.Function("m")(r)
rdot = sp.Function("rdot")(r)    # \dot r as a function of r
rddot = sp.Function("rddot")(r)  # \ddot r as a function of r

# --- pieces of the equation ---
P = 1 - rs / r - rdot
A = rddot + rs / (2 * (r - rs) * r) * rdot**2
B = (1 - rs / r) * (L**2 / r**3 - rs * E**2 / (2 * r**2))

# --- original ODE ---
ode = sp.Eq(sp.diff(m, r) * P, m * A + B / m)
show("Original ODE", ode)

"""# --- attempt 1: direct dsolve (may recognize Bernoulli form) ---
try:
    sol_direct = sp.dsolve(ode, m, hint="Bernoulli", simplify=False)
    show("Direct solution", sol_direct)
except NotImplementedError:
    print("\nDirect dsolve failed - falling back to u = m^2 substitution.")"""

# --- attempt 2: linearize via u = m^2 ---
u = sp.Function("u")(r)
ode_u = sp.Eq(sp.diff(u, r) - (2 * A / P) * u, 2 * B / P)
show("Linearized ODE in u = m^2", ode_u)

sol_u = sp.dsolve(ode_u, u)
show("Solution for u(r)", sol_u)

m_sol = sp.sqrt(sol_u.rhs)
show("Recovered m(r) = sqrt(u(r))", m_sol)
