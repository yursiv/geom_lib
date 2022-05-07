# https://scask.ru/a_book_mm3d.php
# https://scask.ru/a_book_mm3d.php?id=109
# https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0405/DONAVANIK/bezier.html
# https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/surface/bezier-properties.html
# https://stackoverflow.com/questions/34650830/bicubic-bezier-patch-trouble-with-understanding


import time

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy.special import comb


def bezier_matrix(d):
    return np.array([[(-1) ** (i - j) * comb(j, i) * comb(d, j) for i in range(d + 1)] for j in range(d + 1)], int)


BM = [bezier_matrix(i) for i in range(16)]


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


def bsurface(poles, u, v):
    count_u, count_v, _ = poles.shape
    deg_u, deg_v = count_u - 1, count_v - 1

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


def bsurfaceM(cps: np.ndarray, resol=(16, 16)):
    """

    :param cps: np.ndrray((U, V, 3))
    :param resol: np.ndrray((C, 2))
    :return:
    """
    u, v = np.linspace(0, 1, resol[0]), np.linspace(0, 1, resol[1])

    count_u, count_v, _ = cps.shape
    deg_u, deg_v = count_u - 1, count_v - 1

    u_vec = np.array([u ** i for i in range(count_u)])
    v_vec = np.array([v ** i for i in range(count_v)])


    print("u: ", u.shape)
    print("v: ", v.shape)

    BM_u, BM_v = BM[deg_u], BM[deg_v]

    px, py, pz = cps.reshape(-1, 3).T
    px.shape = count_u, count_v
    py.shape = count_u, count_v
    pz.shape = count_u, count_v

    m1 = u_vec.T.dot(BM_u)
    m2 = BM_v.T.dot(v_vec)

    x = m1.dot(px).dot(m2)
    y = m1.dot(py).dot(m2)
    z = m1.dot(pz).dot(m2)

    return x, y, z


poles5x3 = np.array([
    [[1.8, -0.3, 0.], [1.8, 0.13, 0.1], [1.8, 0.5, 0.]],
    [[2., -0.3, 0.06], [2.1, 0.1, 0.1], [2.1, 0.5, 0.1]],
    [[2.3, -0.3, 0.1], [2.3, 0.13, 0.2], [2.3, 0.5, 0.1]],
    [[2.4, -0.3, 0.1], [2.5, 0.1, 0.15], [2.5, 0.5, 0.1]],
    [[2.6, -0.3, 0.], [2.6, 0.1, 0.1], [2.5, 0.5, 0.]]])

poles5x8 = np.array([[[1.5, -0.8, 0.2], [1.5, -0.5, 0.3], [1.5, -0.3, 0.4], [1.5, -0., 0.5], [1.5, 0.2, 0.5], [1.5, 0.5, 0.5], [1.5, 0.8, 0.4], [1.5, 1., 0.3]],
                     [[1.9, -0.8, 0.3], [1.9, -0.5, 0.5], [1.9, -0.3, 0.6], [1.9, -0., 0.7], [1.9, 0.2, 0.8], [1.9, 0.5, 0.7], [1.9, 0.8, 0.6], [1.9, 1., 0.5]],
                     [[2.2, -0.8, 0.3], [2.2, -0.5, 0.5], [2.2, -0.3, 0.7], [2.2, -0., 0.8], [2.2, 0.2, 0.9], [2.2, 0.5, 0.8], [2.2, 0.8, 0.7], [2.2, 1., 0.5]],
                     [[2.6, -0.8, 0.3], [2.6, -0.5, 0.5], [2.6, -0.3, 0.6], [2.6, -0., 0.7], [2.6, 0.2, 0.8], [2.6, 0.5, 0.7], [2.6, 0.8, 0.6], [2.6, 1., 0.5]],
                     [[3., -0.8, 0.2], [3., -0.5, 0.3], [3., -0.3, 0.4], [3., -0., 0.5], [3., 0.2, 0.5], [3., 0.5, 0.5], [3., 0.8, 0.4], [3., 1., 0.3]]],
                    dtype=np.float32)

fig: Figure = plt.figure(figsize=(7, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')

# --------------
px, py, pz = poles5x8.reshape(-1, 3).T
ax.scatter(px, py, pz)

resol = 16, 16
x, y, z = bsurfaceM(poles5x8, resol=resol)
ax.plot_wireframe(x, y, z, cmap=cm.gray, linewidth=.1, antialiased=False)

in_uv = .5, .25
out_co = bsurface(poles5x8, *in_uv)
ax.scatter(*out_co)

plt.show()
