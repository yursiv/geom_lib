import numpy as np
from scipy.interpolate import RegularGridInterpolator

z = np.array([[4.0, 2.0, 4.0],
              [11.0, 20.0, 11.0],
              [0.5, 0.4, 0.5],
              [1.0, -5.0, 0.5]])

x1 = np.array([1., 2., 3., 4])
x2 = np.array([10.0, 11.0, 12.0])

f = RegularGridInterpolator((x1, x2), z, bounds_error=False, fill_value=None)

def convenient_f(x1, x2):
    x = np.vstack((x1.ravel(), x2.ravel())).T
    z = f(x)
    return z.reshape(x1.shape)


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import cm

X1, X2 = np.meshgrid(x1, x2, indexing='ij')
x1_surface, x2_surface = np.meshgrid(np.linspace(1, 4, 40), np.linspace(10, 12, 40), indexing='ij')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(X1.ravel(), X2.ravel(), z.ravel(), "ok")
ax.plot_surface(x1_surface, x2_surface, convenient_f(x1_surface, x2_surface), alpha=0.5, cmap=cm.gray)

plt.show()
