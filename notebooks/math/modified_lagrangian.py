from sympy import *

t, a, c, m_0 = symbols('t a c m_0', real = True)
z = Function('z')(t)
z_d = diff(z, t)
z_dd = diff(z, t, 2)

m = m_0/(a*z+1)
m_dz = diff(m, z)

m_dt = diff(m, t)

trajectory = 1/a*(sqrt((a*t)**2+1)-1)
trajectory_d = diff(trajectory, t)
trajectory_dd = diff(trajectory, t, 2)

L = -m*sqrt(1-z_d**2)

EOM = solve(Eq(diff(L, z), diff(diff(L, z_d), t)), z_dd)[0]
