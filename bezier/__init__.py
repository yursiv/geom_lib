# https://scask.ru/a_book_mm3d.php
# https://scask.ru/a_book_mm3d.php?id=109

import numpy as np
from scipy.special import comb
from scipy import interpolate

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D

from matplotlib import cm


def bern(i, d, t):
    return comb(d, i) * (t ** (d - i)) * (1 - t) ** i


def bezier_matrix(d):
    return np.array([[(-1) ** (i - j) * comb(j, i) * comb(d, j) for i in range(d + 1)] for j in range(d + 1)], int)


BM = [bezier_matrix(i) for i in range(16)]


def bcurve(cps: np.ndarray, t):
    count = cps.shape[0]
    t_vec = np.array([t ** i for i in range(count)])
    return t_vec.T.dot(BM[count - 1]).dot(cps)


def bsurface(cps: np.ndarray, uv: np.ndarray):
    params_count = uv.shape[0]
    u, v = uv.T

    count_u, count_v, _ = cps.shape

    deg_u, deg_v = count_u - 1, count_v - 1
    u_vec = np.array([u ** i for i in range(count_u)])
    v_vec = np.array([v ** i for i in range(count_v)])

    m1 = u_vec.T.dot(BM[deg_u])
    print("m1: ", m1.shape)

    pnts = m1.dot(cps).reshape(count_u, 3, -1).T.dot(BM[deg_v]).dot(v_vec)
    return pnts


# cps_u = np.linspace(0, 1, 4)
# cps_v = np.linspace(0, 1, 4)
#
# x, y = np.meshgrid(cps_u, cps_v)
# z = np.ones((4, 4))
# poles = np.stack([x, y, z], axis=2)

params = np.linspace((.5, 0), (.5, 1), 7)

poles4x4 = np.array([
    [[-1.8, -3.8, 1.2], [-1.1, -3.8, 1.5], [-0.4, -3.8, 1.5], [0.3, -3.8, 1.2]],
    [[-1.8, -3.4, 1.4], [-1.1, -3.4, 1.7], [-0.4, -3.4, 1.7], [0.3, -3.4, 1.4]],
    [[-1.8, -2.9, 1.4], [-1.1, -2.9, 1.7], [-0.4, -2.9, 1.7], [0.3, -2.9, 1.4]],
    [[-1.8, -2.5, 1.2], [-1.1, -2.5, 1.4], [-0.4, -2.5, 1.4], [0.3, -2.5, 1.2]],
], float)

poles5x3 = np.array([
    [[1.8949356, -0.30404282, 0.], [1.8949356, 0.13383025, 0.09819163], [1.8949356, 0.5717033, 0.]],
    [[2.0926487, -0.30404282, 0.06559345], [2.0926487, 0.13383025, 0.16378507], [2.0926487, 0.5717033, 0.06559345]],
    [[2.290362, -0.30404282, 0.11273874], [2.290362, 0.13383025, 0.21093038], [2.290362, 0.5717033, 0.11273874]],
    [[2.4880748, -0.30404282, 0.06559345], [2.4880748, 0.13383025, 0.16378507], [2.4880748, 0.5717033, 0.06559345]],
    [[2.685788, -0.30404282, 0.], [2.685788, 0.13383025, 0.09819163], [2.685788, 0.5717033, 0.]]])


# print(pnts)

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
    fig: Figure = plt.figure(figsize=(7, 7))
    ax: Axes3D = fig.add_subplot(111, projection='3d')

    # ax.scatter(px, py, pz)

    surf_co = bsurface(poles5x3, params)
    print("surf_co: ", surf_co.shape)
    x, y, z = surf_co[0, :, :]  # (7, 3, 7)
    x, y, z = surf_co[:, :, 0].T  # (7, 3, 7)
    ax.scatter(x, y, z)

    # --------------
    resol = 32, 32
    co = calc_numpy_surface(poles5x3, du=4, dv=2, resol=resol)

    x, y, z = co.reshape(-1, 3).T
    x.shape = resol
    y.shape = resol
    z.shape = resol

    ax.plot_surface(x, y, z, cmap=cm.gray, linewidth=1, antialiased=False)
    plt.show()
