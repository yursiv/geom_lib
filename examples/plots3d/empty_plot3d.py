import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Create a figure with 3D ax
fig: Figure = plt.figure(figsize=(7, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')

grid_size = 32, 32

co = np.random.rand(3, *grid_size)
pnts_sizes = np.ones(grid_size, 'f') * 3
colors = np.random.rand(*grid_size)

ax.scatter(*co, s=pnts_sizes, c=colors)

plt.show()
