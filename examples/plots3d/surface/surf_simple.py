import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D

from matplotlib.widgets import MultiCursor

from matplotlib import cm

# Define dimensions
Nx, Ny, Nz = .5, .2, .1
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))

# Create a figure with 3D ax
fig: Figure = plt.figure(figsize=(7, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')
# Make data
samp_count = 32
u = np.linspace(0, 2 * np.pi, samp_count)
v = np.linspace(0, np.pi, samp_count)

x =  np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))


# Plot the surface
ax.plot_surface(x, y, z, cmap=cm.gray, linewidth=1, antialiased=False)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

dr = 1, 0, 0
ax.text(0, 0, .5, "co: {0}".format((0, 0, .5)), dr)


multi = MultiCursor(fig.canvas, (ax,), color='r', lw=1)

plt.show()




