import numpy as np
from scipy.special import comb
from scipy import interpolate

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D

from matplotlib.widgets import MultiCursor

from matplotlib import cm

fig: Figure = plt.figure(figsize=(7, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')


# -------------------
def f(x, y):
    return x ** 2 + y ** 2


u, v = np.linspace(0, 5, 4), np.linspace(-2 * np.pi, 2 * np.pi, 4)
in_x, in_y = np.meshgrid(u, v)
in_z = f(in_x, in_y)

cx = [0.0, -6.3, 39.5, 1.7, -6.3, -13.2, 3.3, -6.3, -13.2, 5.0, -6.3, 39.5, 0.0, -2.1, 39.5, 1.7]
cy = [-2.1, -13.2, 3.3, -2.1, -13.2, 5.0, -2.1, 39.5, 0.0, 2.1, 47.8, 1.7, 2.1, -4.8, 3.3, 2.1]
cz = [1, 2, 2, 1,
      2, 3, 3, 2,
      6.3,  11.8, 3.3, 6.3,
      11.8, 5.0, 6.3, 64.5]
poles = np.stack([cx, cy, cz]).reshape(4, 4, 3)

tck = interpolate.bisplrep(in_x, in_y, in_z, kx=3, ky=3, s=0)

tck2 = [(0, 0, 0, 0, 1, 1, 1, 1),
        (0, 0, 0, 0, 1, 1, 1, 1),
        cz, 3, 3]

knots_u, knots_v, c, du, dv = tck

# tck[0] = [0, 0, 0, 0, 1, 1, 1,1]
# tck[1] = [0, 0, 0, 0, 1, 1, 1,1]

print("knots_u: ", knots_u)
print("knots_v: ", knots_v)
print("degree: ", du, dv)
print("c: ", [round(i, 2) for i in c])

px, py = np.linspace(knots_u[0], knots_u[-1], 8), np.linspace(knots_v[0], knots_v[-1], 8)
pz = interpolate.bisplev(px, py, tck)

# -------------------
sx, sy = np.meshgrid(px, py)
# ax.plot_surface(sx, sy, pz)

u, v = np.linspace(0, 1, 8),  np.linspace(0, 1, 8)
sx2, sy2 = np.meshgrid(u, v)
sz2 = interpolate.bisplev(px, py, tck)

ax.plot_surface(sx2, sy2, sz2)

cp_x, cp_y = np.linspace(knots_u[0], knots_u[-1], 4), np.linspace(knots_v[0], knots_v[-1], 4)
cp_x, cp_y = np.meshgrid(cp_x, cp_y)
cp_z = c
# ax.scatter(sx, sy, pz)  # , s=pnts_sizes

pnts_sizes = np.ones((4, 4), 'f') * 3
ax.scatter(in_x, in_y, in_z, s=pnts_sizes)

pnts_sizes = np.ones((4, 4), 'f') * 8
ax.scatter(cp_x, cp_y, cp_z, s=pnts_sizes)

# ax.scatter(*poles.reshape(-1, 3).T)

# cx, cy, cz = np.stack([cp_x.ravel(), cp_y.ravel(), cp_z.ravel()]).T.reshape(3, -1)
# print("cx = ", [round(x, 1) for x in cx])
# print("cy =  ", [round(y, 1) for y in cy])
# print("cz =  ", [round(z, 1) for z in cz])

plt.show()
