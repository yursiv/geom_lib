import numpy as np
from matplotlib import pyplot as plt


def distance_2d(pnt, x, y):
    return np.hypot(x - pnt[0], y - pnt[1])


gr_size =12
ys, xs = np.ogrid[-gr_size:gr_size, -gr_size:gr_size]

pnt = np.array([0, 0])
distances = distance_2d(pnt, xs, ys)  # distance to point (1, 2)

plt.figure()

plt.title('distance to point {0}'.format(pnt))
plt.imshow(distances, origin='lower', interpolation="none")

plt.xticks(np.arange(xs.shape[1]), xs.ravel())  # need to set the ticks manually
plt.yticks(np.arange(ys.shape[0]), ys.ravel())

plt.colorbar()

plt.show()
