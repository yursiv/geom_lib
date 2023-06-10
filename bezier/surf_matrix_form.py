# https://scask.ru/a_book_mm3d.php
# https://scask.ru/a_book_mm3d.php?id=109
# https://web.iitd.ac.in/~hegde/cad/lecture/L19_beziersurf.pdf

# https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0405/DONAVANIK/bezier.html
# https://stackoverflow.com/questions/34650830/bicubic-bezier-patch-trouble-with-understanding

# -----------MTU
# https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/surface/bezier-properties.html
# https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/


# https://dcain.etsin.upm.es/~leonardo/etema5.htm
# https://www.gamedeveloper.com/programming/an-in-depth-look-at-bicubic-bezier-surfaces
# http://www.cad.zju.edu.cn/home/zhx/GM/005/00-bcs2.pdf

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


# def bern1(d, i, t):
#     return comb(d, i) * (t ** (d - i)) * (1 - t) ** i

def bern(d, i, t):
    return comb(d, i) * (t ** i) * (1 - t) ** (d - i)


def bern_deriv1(d, i, t):
    return bern(d, i, t) * (i - d * t) / (t * (1 - t))


def bern_deriv2(d, i, t):
    return bern(d, i, t) * ((1 - d * t) ** 2 - d * t ** 2 - i * (1 - 2 * t)) / (t ** 2 * (1 - t) ** 2)


def surf_u_deriv1(cps: np.ndarray, u, v):
    count_u, count_v = cps.shape[:2]
    deg_u, deg_v = count_u - 1, count_v - 1

    du1 = np.array([0, 0, 0], float)
    for i in range(deg_u):
        for j in range(deg_v):
            du1 += cps[i, j, :] * bern_deriv1(deg_u, i, u) * bern(deg_v, j, v)

    return du1


def surf_v_deriv1(cps: np.ndarray, u, v):
    count_u, count_v = cps.shape[:2]
    deg_u, deg_v = count_u - 1, count_v - 1

    dv1 = np.array([0, 0, 0], float)
    for i in range(deg_u):
        for j in range(deg_v):
            dv1 += cps[i, j, :] * bern(deg_u, i, u) * bern_deriv1(deg_v, j, v)

    return dv1


def surf_uv_deriv1(cps: np.ndarray, u, v):
    count_u, count_v = cps.shape[:2]
    deg_u, deg_v = count_u - 1, count_v - 1

    duv = np.array([0, 0, 0], float)
    for i in range(deg_u):
        for j in range(deg_v):
            duv += cps[i, j, :] * bern_deriv1(deg_u, i, u) * bern_deriv1(deg_v, j, v)

    return duv


def surf_u_deriv2(cps: np.ndarray, u, v):
    count_u, count_v = cps.shape[:2]
    deg_u, deg_v = count_u - 1, count_v - 1

    du2 = np.array([0, 0, 0], float)
    for i in range(deg_u):
        for j in range(deg_v):
            du2 += cps[i, j, :] * bern_deriv2(deg_u, i, u) * bern(deg_v, j, v)

    return du2


def surf_v_deriv2(cps: np.ndarray, u, v):
    count_u, count_v = cps.shape[:2]
    deg_u, deg_v = count_u - 1, count_v - 1

    dv2 = np.array([0, 0, 0], float)
    for i in range(deg_u):
        for j in range(deg_v):
            dv2 += cps[i, j, :] * bern(deg_u, i, u) * bern_deriv2(deg_v, j, v)

    return dv2


def surf_derivatives(cps: np.ndarray, u, v):
    count_u, count_v = cps.shape[:2]
    deg_u, deg_v = count_u - 1, count_v - 1

    eps = .0001

    if u == 0:
        u = eps
    if u == 1:
        u = 1 - eps
    if v == 0:
        v = eps
    if v == 1:
        v = 1 - eps

    du1 = np.array([0, 0, 0], float)
    dv1 = np.array([0, 0, 0], float)
    duv = np.array([0, 0, 0], float)
    du2 = np.array([0, 0, 0], float)
    dv2 = np.array([0, 0, 0], float)

    for i in range(deg_u):
        for j in range(deg_v):
            bern_u = bern(deg_u, i, u)
            bern_v = bern(deg_v, j, v)

            bern_du1 = bern_deriv1(deg_u, i, u)
            bern_dv1 = bern_deriv1(deg_v, j, v)

            bern_du2 = bern_deriv2(deg_u, i, u)
            bern_dv2 = bern_deriv2(deg_v, j, v)

            cp = cps[i, j, :]

            du1 += cp * bern_du1 * bern_v
            dv1 += cp * bern_u * bern_dv1

            duv += cp * bern_du1 * bern_dv1

            du2 += cp * bern_du2 * bern_v
            dv2 += cp * bern_u * bern_dv2

    return du1, dv1, duv, du2, dv2


def gauss_curvature(du1, dv1, duv, du2, dv2):
    norm = np.cross(du1, dv1)
    norm_len = np.linalg.norm(norm)

    A = norm.dot(du2)
    B = norm.dot(duv)
    C = norm.dot(dv2)
    return (A * C - B ** 2) / (norm_len ** 4)


def mean_curvature(du1, dv1, duv, du2, dv2):
    norm = np.cross(du1, dv1)
    norm_len = np.linalg.norm(norm)

    A = norm.dot(du2)
    B = norm.dot(duv)
    C = norm.dot(dv2)

    dv1_len = np.linalg.norm(dv1)
    du1_len = np.linalg.norm(du1)

    r1 = A * dv1_len ** 2 - 2 * B * np.dot(du1, du2) + C * du1_len
    r2 = 2 * norm_len ** 3
    return r1 / r2


def bsurface(poles, u, v):
    count_u, count_v, _ = poles.shape
    deg_u, deg_v = count_u - 1, count_v - 1

    co = [0, 0, 0]
    for i in range(count_u):
        for j in range(count_v):
            bu = bern(deg_u, i, u)
            bv = bern(deg_v, j, v)

            pole_co = poles[i][j]
            m = bu * bv
            co[0] += pole_co[0] * m
            co[1] += pole_co[1] * m
            co[2] += pole_co[2] * m

    return co


mm1, mm2, cps_ = None, None, None


def bsurfaceM(cps: np.ndarray, uv: np.ndarray, grid=True):
    """
    :param cps: np.ndrray((U, V, 3))
    :param resol: np.ndrray((C, 2))
    :return:
    """
    u, v = uv.T

    count_u, count_v, _ = cps.shape
    deg_u, deg_v = count_u - 1, count_v - 1

    u_vec = np.array([u ** i for i in range(count_u)])
    v_vec = np.array([v ** i for i in range(count_v)])

    # print("u: ", u.shape)
    # print("v: ", v.shape)

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

    # global mm1, mm2, cps_
    if grid:
        return x, y, z
    else:
        return x[0, :], y[0, :], z[0, :]


# https://scask.ru/a_book_mm3d.php?id=92

# TODO
def iso_curve(cps: np.ndarray, param=.5, is_u=True):
    count_u, count_v = cps.shape[:2]
    deg_u, deg_v = count_u - 1, count_v - 1
    points = []

    if is_u:
        co = np.zeros(3, float)
        for j in range(count_v):
            co += 0

    return np.array(points, float)


poles3x3 = np.array([[[1.49, -0.8, 0.13],
                      [1.49, 0.11, 0.25],
                      [1.49, 1.03, 0.]],

                     [[2.24, -0.8, 0.41],
                      [2.24, 0.11, 0.53],
                      [2.24, 1.03, 0.28]],

                     [[2.99, -0.8, 0.13],
                      [2.99, 0.11, 0.25],
                      [2.99, 1.03, 0.]]], dtype=float)

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
                    dtype=float)

fig: Figure = plt.figure(figsize=(12, 7))
ax: Axes3D = fig.add_subplot(111, projection='3d')

# -------------- Surface
st = time.time()
resol = 32, 32

u, v = np.linspace(0, 1, resol[0]), np.linspace(0, 1, resol[1])
uv = np.stack([u, v], axis=1)

x, y, z = bsurfaceM(poles3x3, uv, grid=True)
# print("t1: ", time.time()-st)

ax.plot_wireframe(x, y, z, cmap=cm.gray, linewidth=.25, antialiased=True)

# uv = np.linspace((0, 0), (0, 1), resol[0])

# st = time.time()
# for i in range(100):
#     x, y, z = bsurfaceM(poles5x8, uv, grid=False)
# print("t2: ", time.time()-st)

# ax.scatter(x.ravel(), y.ravel(), z.ravel(), s=5)

# -------------- Poles
px, py, pz = poles3x3.reshape(-1, 3).T
ax.scatter(px, py, pz, s=3)
#
# -------------- Point On Surface
sx, sy, sz = bsurface(poles3x3, .5, .5)
ax.scatter(sx, sy, sz, s=3)

# uv = 0.2, .1
curvatures = []
normals = []
start_no = None

uvs = np.array([np.linspace(.2, .2, 32), np.linspace(0.2, .9, 32)], float).T
x, y, z = bsurfaceM(poles3x3, uvs, grid=False)
ax.scatter(x, y, z, s=3)
surf_pnts = np.stack([x, y, z], axis=1)

for uv, surf_co in zip(uvs, surf_pnts):
    # in_uv = np.array([(uv)])

    # ----------------------DERIVATIVES
    du1, dv1, duv, du2, dv2 = surf_derivatives(poles3x3, *uv)
    # surf_co = np.array([x[0], y[0], z[0]])

    norm = np.cross((du1 + dv1), (du2 + dv2))
    norm = np.cross(du1, dv1)
    n_len = np.linalg.norm(norm)
    norm = norm / n_len

    if start_no is None:
        start_no = norm
    else:
        dot = start_no.dot(norm)
        # print("no: ", dot)
        if dot < 0:
            norm = -norm

    normals.append(norm)
    #
    # lu1 = surf_co + du1 / np.linalg.norm(du1)
    # lv1 = surf_co + dv1 / np.linalg.norm(dv1)
    #
    # lines1 = np.stack([surf_co, lu1, surf_co, lv1], axis=1)
    # ax.plot(*lines1, linewidth=.5)
    #
    # lu2 = surf_co + du2 / np.linalg.norm(du2)
    # lv2 = surf_co + dv2 / np.linalg.norm(dv2)
    #
    # lines2 = np.stack([surf_co, lu2, surf_co, lv2], axis=1)
    # ax.plot(*lines2, linewidth=.5)

    # curv = mean_curvature(du1, dv1, duv, du2, dv2)
    curv = gauss_curvature(du1, dv1, duv, du2, dv2)
    curv = abs(curv)
    # print("curv: ", curv)
    # if abs(curv) > 2:
    #     continue
    curvatures.append(curv)

normals = np.array(normals)
curvatures = np.array(curvatures)
curvatures = curvatures / np.linalg.norm(curvatures)

norm_lines = np.stack([surf_pnts, surf_pnts + normals * curvatures[:, np.newaxis]], axis=1)
norm_lines.shape = -1, 2, 3
norm_lines2 = surf_pnts + normals * curvatures[:, np.newaxis]
print("time: ", time.time() - st)

# print(norm_lines.shape)
# for line in norm_lines:
#     ax.plot(*line.T, linewidth=1)


ax.plot(*norm_lines2.T, linewidth=1)
#
# ax.plot_wireframe(*norm_lines, cmap=cm.gray, linewidth=1, antialiased=False)


plt.show()
