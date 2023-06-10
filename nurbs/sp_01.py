# https://github.com/SINTEF/Splipy/blob/8662fb48800d881d752554bb60182417fe092d22/doc/Tutorial/Knots%20and%20Bolts.ipynb

import splipy as sp
import numpy as np
from matplotlib import pyplot as plt

# create a set of cubic (order=4) B-spline basis functions
basis = sp.BSplineBasis(order=4, knots=[0, 0, 0, 0, 1, 2, 4, 4, 4, 4])
basis = sp.BSplineBasis(order=4, knots=[0, 0, 0, 0, 1, 1, 1, 1])

# 150 uniformly spaced evaluation points on the domain (0,4)
t = np.linspace(0, 1, 150)

# evaluate *all* basis functions on *all* points t. The returned variable B is a matrix
B = basis.evaluate(t)  # B.shape = (150,6), 150 visualization points, 6 basis functions

# plot the basis functions
plt.plot(t, B)
plt.show()
