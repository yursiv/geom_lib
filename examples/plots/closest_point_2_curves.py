import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import fmin


def BCubic(t, P0, P1, P2, P3):
    a = P1 - P0
    b = P2 - P1
    c = P3 - P2

    return a * 3 * (1 - t) ** 2 + b * 6 * (1 - t) * t + c * 3 * t ** 2


def B(t):
    return BCubic(t, 4, 2, 3, 1)


def C(t):
    return BCubic(t, 1, 4, 3, 4)


def f(t):
    # L1 or manhattan distance
    return abs(B(t) - C(t))


init = 0  # 2
tmin = fmin(f, np.array([init]))
# Optimization terminated successfully.
# Current function value: 2.750000
#     Iterations: 23
#     Function evaluations: 46
print("min param: ", tmin)
# [0.5833125]
tmin = tmin[0]

t = np.linspace(0, 2, 100)

plt.plot(t, B(t), label='B')
plt.plot(t, C(t), label='C')
plt.plot(t, abs(B(t) - C(t)), label='|B-C|')
plt.plot(tmin, B(tmin), 'r.', markersize=12, label='min')

plt.axvline(x=tmin, linestyle='--', color='k')

plt.legend()

plt.show()
