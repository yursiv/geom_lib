""""Implements a b-spline surface as a 3-tuple of
scipy.interpolate.RectBivariateSpline instances, one
each for x, y and z.
"""

import math
import time

import numpy as np
from numpy import ndarray
from scipy.interpolate import RectBivariateSpline


# https://gist.github.com/subnivean/c622cc2b58e6376263b8
class BSplineSurf(object):
    def __init__(self, poles: ndarray, degree=(3, 3), bbox=[0, 1, 0, 1]):
        """Parametric (u,v) bspline surface.

        Parameters
        ----------
        poles : array_like
            3-D array of (x, y, z) data with shape (u.size, v.size, 3).

        degree: Tuple[int, int] surface u and v degrees

        bbox : array_like, optional
            Sequence of length 4 specifying the boundary of the rectangular
            approximation domain. See scipy.interpolate.RectBivariateSpline
            for more info.


        """
        self.poles = poles
        self.bbox = bbox

        self.degree_u = degree[0]
        self.degree_v = degree[1]

        self.pcount_u, self.pcount_v = poles.shape[:2]

        self.knots_u = self.get_uniform_knots(self.degree_u, self.pcount_u)
        self.knots_v = self.get_uniform_knots(self.degree_v, self.pcount_v)

        self.px = self.poles[:, :, 0]
        self.py = self.poles[:, :, 1]
        self.pz = self.poles[:, :, 2]

        self.u = np.linspace(0, 1, self.px.shape[0])
        self.v = np.linspace(0, 1, self.px.shape[1])

        # Create surface definitions
        self._xs = RectBivariateSpline(self.u, self.v, self.px, bbox=self.bbox, kx=self.degree_u, ky=self.degree_v, s=0)
        self._ys = RectBivariateSpline(self.u, self.v, self.py, bbox=self.bbox, kx=self.degree_u, ky=self.degree_v, s=0)
        self._zs = RectBivariateSpline(self.u, self.v, self.pz, bbox=self.bbox, kx=self.degree_u, ky=self.degree_v, s=0)

        self._xs.tck = self.knots_u, self.knots_v, self.px.ravel()
        self._ys.tck = self.knots_u, self.knots_v, self.py.ravel()
        self._zs.tck = self.knots_u, self.knots_v, self.pz.ravel()

    def values(self, uvs: ndarray):
        """Get point(s) on surface at (u, v).

        Parameters
        ----------
        u, v : scalar or array-like
            u and v may be scalar or vector

        mesh : boolean
            If True, will expand the u and v values into a mesh.
            For example, with u = [0, 1] and v = [0, 1]: if 'mesh'
            is True, the surface will be evaluated at [0, 0], [0, 1],
            [1, 0] and [1, 1], while if it is False, the evalation
            will only be made at [0, 0] and [1, 1]

        Returns
        -------
        If scalar values are passed for *both* u and v, returns
        a 1-D 3-element array [x,y,z]. Otherwise, returns an array
        of shape 3 x len(u) x len(v), suitable for feeding to Mayavi's
        mlab.mesh() plotting function (as mlab.mesh(*arr)).
        """
        u, v = uvs.T

        x = self._xs.ev(u, v)
        y = self._ys.ev(u, v)
        z = self._zs.ev(u, v)

        if u.shape == (1,) and v.shape == (1,):
            return np.array([x, y, z]).ravel()
        else:
            arr = np.array([x, y, z]).reshape(3, len(u), -1)
            return arr[:, :, 0]

    def utan(self, u, v, normalize=True, mesh=True):
        u = np.asarray([u]).reshape(-1, )
        v = np.asarray([v]).reshape(-1, )

        dxdu = self._xs(u, v, dx=1, dy=0, grid=mesh)
        dydu = self._ys(u, v, dx=1, dy=0, grid=mesh)
        dzdu = self._zs(u, v, dx=1, dy=0, grid=mesh)
        du = np.array([dxdu, dydu, dzdu]).T

        if mesh is True:
            du = du.swapaxes(0, 1)
        else:
            du = du[:, np.newaxis, :]

        if normalize:
            du /= np.sqrt((du ** 2).sum(axis=2))[:, :, np.newaxis]

        if u.shape == (1,) and v.shape == (1,):
            return du.reshape(3)
        else:
            arr = du.transpose(2, 0, 1)
            if mesh is True:
                return arr
            else:
                return arr[:, :, 0]

    def vtan(self, u, v, normalize=True, mesh=True):
        u = np.asarray([u]).reshape(-1, )
        v = np.asarray([v]).reshape(-1, )

        dxdv = self._xs(u, v, dx=0, dy=1, grid=mesh)
        dydv = self._ys(u, v, dx=0, dy=1, grid=mesh)
        dzdv = self._zs(u, v, dx=0, dy=1, grid=mesh)
        dv = np.array([dxdv, dydv, dzdv]).T

        if mesh is True:
            dv = dv.swapaxes(0, 1)
        else:
            dv = dv[:, np.newaxis, :]

        if normalize:
            dv /= np.sqrt((dv ** 2).sum(axis=2))[:, :, np.newaxis]

        if u.shape == (1,) and v.shape == (1,):
            return dv.reshape(3)
        else:
            arr = dv.transpose(2, 0, 1)
            if mesh is True:
                return arr
            else:
                return arr[:, :, 0]

    def normal(self, u, v, mesh=True):
        """Get normal(s) at (u, v).

        Parameters
        ----------
        u, v : scalar or array-like
            u and v may be scalar or vector (see below)

        Returns
        -------
        If scalar values are passed for *both* u and v, returns
        a 1-D 3-element array [x,y,z]. Otherwise, returns an array
        of shape 3 x len(u) x len(v), suitable for feeding to Mayavi's
        mlab.mesh() plotting function (as mlab.mesh(*arr)).
        """
        u = np.asarray([u]).reshape(-1, )
        v = np.asarray([v]).reshape(-1, )

        dxdus = self._xs(u, v, dx=1, grid=mesh)
        dydus = self._ys(u, v, dx=1, grid=mesh)
        dzdus = self._zs(u, v, dx=1, grid=mesh)
        dxdvs = self._xs(u, v, dy=1, grid=mesh)
        dydvs = self._ys(u, v, dy=1, grid=mesh)
        dzdvs = self._zs(u, v, dy=1, grid=mesh)

        normals = np.cross([dxdus, dydus, dzdus],
                           [dxdvs, dydvs, dzdvs],
                           axisa=0, axisb=0)

        if mesh is False:
            normals = normals[:, np.newaxis, :]

        normals /= np.sqrt((normals ** 2).sum(axis=2))[:, :, np.newaxis]

        if u.shape == (1,) and v.shape == (1,):
            return normals.reshape(3)
        else:
            arr = normals.transpose(2, 0, 1)
            if mesh is True:
                return arr
            else:
                return arr[:, :, 0]

    def copy(self):
        """Get a copy of the surface
        """
        from copy import deepcopy
        return deepcopy(self)

    # -----------

    def get_uniform_knots(self, degree, pcount, is_periodic=False):
        if is_periodic:
            return np.arange(0 - degree, pcount + degree + degree - 1)
        else:
            knots = np.clip(np.arange(pcount + degree + 1) - degree, 0, pcount - degree)
            return knots / knots[-1]


poles = np.array([[[2.8119884, 0.25286832, 2.21957],
                   [2.5603323, 0.34388292, 2.2235794],
                   [2.3167, 0.44774902, 2.2199354],
                   [2.0810902, 0.5644667, 2.2086387],
                   [1.853504, 0.69403595, 2.1896884],
                   [1.6339409, 0.8364567, 2.163085]],

                  [[2.7170234, 0.0046203, 2.1336858],
                   [2.4771035, 0.09496486, 2.1411932],
                   [2.2441177, 0.1981686, 2.1404853],
                   [2.0180645, 0.31423187, 2.1315615],
                   [1.7989451, 0.4431544, 2.1144218],
                   [1.5867596, 0.5849362, 2.0890663]],

                  [[2.6386054, -0.17864244, 1.9883013],
                   [2.409287, -0.093096, 2.0032988],
                   [2.1858125, 0.00531745, 2.0095177],
                   [1.9681816, 0.11659798, 2.006958],
                   [1.7563947, 0.24074572, 1.9956205],
                   [1.550452, 0.37776047, 1.9755044]],

                  [[2.5767345, -0.2969201, 1.783416],
                   [2.3568828, -0.22029991, 1.8098947],
                   [2.1417859, -0.13080499, 1.8270319],
                   [1.9314423, -0.02843513, 1.8348285],
                   [1.7258532, 0.08680961, 1.8332841],
                   [1.5250185, 0.21492922, 1.8223987]],

                  [[2.5314093, -0.3502127, 1.5190299],
                   [2.31989, -0.2866469, 1.5609809],
                   [2.1120358, -0.21019855, 1.5930283],
                   [1.9078455, -0.12086758, 1.6151721],
                   [1.7073202, -0.01865388, 1.6274127],
                   [1.5104592, 0.09644246, 1.6297495]],

                  [[2.5026312, -0.33851993, 1.1951427],
                   [2.29831, -0.29213664, 1.2565581],
                   [2.0965638, -0.23286311, 1.3075068],
                   [1.8973923, -0.16069914, 1.3479894],
                   [1.7007957, -0.07564469, 1.3780065],
                   [1.5067741, 0.02230018, 1.397557]]], dtype=np.float32)

if __name__ == '__main__':
    pass

    bs = BSplineSurf(poles, degree=(5, 5), bbox=[0.0, 1.0, 0., 1.])

    # grid uvs
    u = np.linspace(0, 1, 16 * 10 + 1)
    v = np.linspace(0, 1, 16 * 10 + 1)
    u, v = np.meshgrid(u, v)

    uvs = np.stack([u.ravel(), v.ravel()]).T

    st = time.time()
    pts = bs.values(uvs)
    print("nu time:", time.time() - st)
    eval_co = pts.T
