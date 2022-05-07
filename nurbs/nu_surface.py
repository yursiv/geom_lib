# https://github.com/orbingol/NURBS-Python
# https://github.com/orbingol/geomdl-examples

import os
from geomdl import BSpline
from geomdl import exchange
from geomdl.visualization import VisVTK as vis

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("D:/Python/geom/nurbs/ex_surface01.cpt", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.faces
# Set evaluation delta
surf.delta = 0.025

# Evaluate surface points
import time

st = time.time()
surf.evaluate()
print("eval time: ", time.time() - st)

# Import and use Matplotlib's colormaps
from matplotlib import cm

# Plot the control point grid and the evaluated surface
# vis_comp = vis.VisSurface()
# surf.vis = vis_comp
# surf.render(colormap=cm.cool)

# -----------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D

from matplotlib import cm

fig: Figure = plt.figure(figsize=(7, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')

pnts = np.array(surf.evalpts)
x, y, z = pnts.T
x.shape = 40, 40
y.shape = 40, 40
z.shape = 40, 40

# px, py, pz = poles.reshape(-1, 3).T
# ax.scatter(px, py, pz)

# x, y, z = co.reshape(-1, 3).T
# x.shape = (16, 16)
# y.shape = (16, 16)
# z.shape = (16, 16)

ax.plot_surface(x, y, z, cmap=cm.gray, linewidth=1, antialiased=False)
#
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')

# dr = 1, 0, 0
# ax.text(0, 0, .5, "co: {0}".format((0, 0, .5)), dr)

plt.show()
