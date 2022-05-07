import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt
from matplotlib import cm

from matplotlib.figure import Figure
from matplotlib.axes import Axes

from mpl_toolkits.mplot3d.axes3d import Axes3D

fig: Figure = plt.figure(figsize=(7, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')

# x = np.arange(0, 4, 1)
# y = np.arange(0, 4, 1)

x = np.array([1, 1.5, 2.5, 3])
y = np.array([1, 1.5, 2.5, 3])

x, y = np.meshgrid(x, y)

z = np.array([
    [0, 1, 1, 0],
    [1, 2, 2, 1],
    [1, 3, 2, 1],
    [0, 1, 1, 0]])

# new grid is 40x40
tck = interpolate.bisplrep(x, y, z, s=0)

xnew = np.linspace(1, 3, num=24)
ynew = np.linspace(1, 3, num=24)
znew = interpolate.bisplev(xnew, ynew, tck)
xnew, ynew = np.meshgrid(xnew, ynew)

surf = ax.plot_surface(xnew, ynew, znew, cmap=cm.gray)

# -----
# xnew = np.linspace(.9, 3.1, num=40)
# ynew = np.linspace(.9, 3.1, num=40)
# znew = interpolate.bisplev(xnew, ynew, tck)
# xnew, ynew = np.meshgrid(xnew, ynew)
#
# ax.plot_wireframe(xnew, ynew, znew, rstride=1, cstride=1, linewidth=.2, color='k')


ax.scatter(x, y, z)

plt.show()
