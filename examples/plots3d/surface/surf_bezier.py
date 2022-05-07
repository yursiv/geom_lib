import numpy as np
from scipy.special import comb
from scipy import interpolate

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D

from matplotlib.widgets import MultiCursor

from matplotlib import cm

side_names = "u0", "u1", "v0", "v1"


def lerp(v_from, v_to, factor):
    return v_from + (1 - factor) * v_to


def coon(l1, l2, l3, l4, params_u, params_v, ui, vi):
    # https://en.wikipedia.org/wiki/Coons_patch
    #   p2       l2         p4
    #      ^>_____V_______^>
    #      |              |
    #      |              |
    # l1  U|              |U  l3
    #      |              |
    #      |              |
    #      |>_____V_______>
    #  p1  ^      l4      ^  p3

    u, v = params_u[ui], params_v[vi]

    p1, p2, p3, p4 = l1[0], l2[0], l3[0], l3[-1]

    surf1 = lerp(v, l1[ui], l3[ui])
    surf2 = lerp(u, l4[vi], l2[vi])

    surf3 = p1 * (1 - u) * (1 - v) + p2 * u * (1 - v) + p3 * (1 - u) * v + p4 * u * v

    return surf1 + surf2 - surf3


def bern(i, d, t):
    return comb(d, i) * (t ** (d - i)) * (1 - t) ** i


def bezier_surf_eval(poles, u, v, deg_u, deg_v):
    count_u, count_v = deg_u + 1, deg_v + 1

    co = [0, 0, 0]
    for i in range(count_u):
        for j in range(count_v):
            bu = bern(i, deg_u, u)
            bv = bern(j, deg_v, v)

            pole_co = poles[i][j]
            m = bu * bv
            co[0] += pole_co[0] * m
            co[1] += pole_co[1] * m
            co[2] += pole_co[2] * m

    return co


def calc_numpy_surface(poles, du, dv, resol=(16, 16)):
    params_u = np.linspace(0, 1, resol[0])
    params_v = np.linspace(0, 1, resol[1])

    cps = poles.tolist()

    coords = np.empty((*resol, 3), float)
    for vi, v in enumerate(params_v):
        for ui, u in enumerate(params_u):
            coords[ui, vi] = bezier_surf_eval(cps, u, v, deg_u=du, deg_v=dv)

    return np.array(coords, np.float32)


if __name__ == '__main__':
    poles = np.array([
        [[-1.8, -3.8, 1.2], [-1.1, -3.8, 1.5], [-0.4, -3.8, 1.5], [0.3, -3.8, 1.2]],
        [[-1.8, -3.4, 1.4], [-1.1, -3.4, 1.7], [-0.4, -3.4, 1.7], [0.3, -3.4, 1.4]],
        [[-1.8, -2.9, 1.4], [-1.1, -2.9, 1.7], [-0.4, -2.9, 1.7], [0.3, -2.9, 1.4]],
        [[-1.8, -2.5, 1.2], [-1.1, -2.5, 1.4], [-0.4, -2.5, 1.4], [0.3, -2.5, 1.2]],
    ], float)

    fig: Figure = plt.figure(figsize=(7, 7))
    ax: Axes3D = fig.add_subplot(111, projection='3d')

    px, py, pz = poles.reshape(-1, 3).T
    ax.scatter(px, py, pz)

    resol = 16, 16

    import time

    st = time.time()
    co = calc_numpy_surface(poles, du=3, dv=3, resol=resol)
    print("eval time: ", time.time() - st)

    x, y, z = co.reshape(-1, 3).T
    x.shape = resol
    y.shape = resol
    z.shape = resol

    ax.plot_surface(x, y, z, cmap=cm.gray, linewidth=1, antialiased=False)

    # ax.text(*p0, "p0", (1, 0, 0))
    # ax.text(*p1, "p1", (1, 0, 0))

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    dr = 1, 0, 0
    ax.text(0, 0, .5, "co: {0}".format((0, 0, .5)), dr)

    plt.show()
