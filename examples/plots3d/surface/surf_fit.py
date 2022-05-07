# https://stackoverflow.com/questions/35046233/how-do-i-fit-a-quadratic-surface-to-some-points-in-python

import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource


from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D

points = np.array([[175697888, -411724928, 0.429621160030365],
                   [175697888, -411725144, 0.6078286170959473],
                   [175698072, -411724640, 0.060898926109075546],
                   [175698008, -411725360, 0.6184252500534058],
                   [175698248, -411725720, 0.0771455243229866],
                   [175698448, -411724456, -0.5925689935684204],
                   [175698432, -411725936, -0.17584866285324097],
                   [175698608, -411726152, -0.24736160039901733],
                   [175698840, -411724360, -1.27967369556427],
                   [175698800, -411726440, -0.21100902557373047],
                   [175699016, -411726744, -0.12785470485687256],
                   [175699280, -411724208, -2.472576856613159],
                   [175699536, -411726688, -0.19858847558498383],
                   [175699760, -411724104, -3.5765910148620605],
                   [175699976, -411726504, -0.7432857155799866],
                   [175700224, -411723960, -4.770215034484863],
                   [175700368, -411726304, -1.2959377765655518],
                   [175700688, -411723760, -6.518451690673828],
                   [175700848, -411726080, -3.02254056930542],
                   [175701160, -411723744, -7.941056251525879],
                   [175701112, -411725896, -3.884831428527832],
                   [175701448, -411723824, -8.661275863647461],
                   [175701384, -411725720, -5.21607780456543],
                   [175701704, -411725496, -6.181706428527832],
                   [175701800, -411724096, -9.490276336669922],
                   [175702072, -411724344, -10.066594123840332],
                   [175702216, -411724560, -10.098011016845703],
                   [175702256, -411724864, -9.619892120361328],
                   [175702032, -411725160, -6.936516284942627]])


def poly_matrix(x, y, degree=2, log=False):
    """ generate Matrix use with lstsq """
    ncols = (degree + 1) ** 2
    G = np.zeros((x.size, ncols))
    ij = itertools.product(range(degree + 1), range(degree + 1))
    for k, (i, j) in enumerate(ij):
        G[:, k] = x ** i * y ** j

    if log:
        print("G: ", G.shape)
        for row in G:
            print([round(v, 1) for v in row])

    return G


def fit_surface(co: np.ndarray, degree=2, resol=(32, 32), axis="Z"):
    x, y, z = co.T
    x, y = x - x[0], y - y[0]  # this improves accuracy

    # make Matrix:
    G = poly_matrix(x, y, degree, log=True)

    # Solve for np.dot(G, m) = z:
    m = np.linalg.lstsq(G, z, rcond=-1)[0]

    # Evaluate it on a grid...
    xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), resol[0]), np.linspace(y.min(), y.max(), resol[1]))
    GG = poly_matrix(xx.ravel(), yy.ravel(), degree)
    zz = np.reshape(np.dot(GG, m), xx.shape)

    return x, y, z, xx, yy, zz


x, y, z, ox, oy, oz = fit_surface(points, degree=2, resol=(32, 32), axis="Z")

# Plotting (see http://matplotlib.org/examples/mplot3d/custom_shaded_3d_surface.html):
# fg, ax = plt.subplots(subplot_kw=dict(projection='3d'))
fig: Figure = plt.figure(figsize=(7, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')

ls = LightSource(270, 45)
rgb = ls.shade(oz, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
# surf = ax.plot_surface(xx, yy, zz, rstride=1, cstride=1, facecolors=rgb, linewidth=0, antialiased=False, shade=False)

ax.plot_wireframe(ox, oy, oz, rstride=1, cstride=1, linewidth=1)

ax.plot3D(x, y, z, "o")

fig.canvas.draw()
plt.show()
