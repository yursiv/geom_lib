import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

fig: Figure = plt.figure(figsize=(7, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')

# Make data.
grid_size = -5, 5

u = np.arange(*grid_size, 0.25)
v = np.arange(*grid_size, 0.25)
X, Y = np.meshgrid(u, v)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

# Plot the surface.
from matplotlib._cm import datad

surf = ax.plot_surface(X, Y, Z, cmap=cm.gray, linewidth=1, antialiased=True)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
