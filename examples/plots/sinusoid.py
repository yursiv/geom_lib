import numpy as np

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig, ax = plt.subplots()
fig: Figure
ax: Axes

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

ax.plot(x, y)
plt.show()
