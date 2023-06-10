import splipy as sp
import numpy as np
from matplotlib import pyplot as plt

basis = sp.BSplineBasis(order=4, knots=[0, 0, 0, 0, 1, 2, 4, 4, 4, 4])

# create a list of 6 controlpoints (we have 6 basis functions in our basis)
controlpoints = [[0, 0], [1.8, 0.2], [1, 1], [0.2, 0.2], [1.5, 0.1], [2, 0]]

curve = sp.Curve(basis, controlpoints)

t = np.linspace(0, 4, 150)  # 150 visualization points on our parametric domain [0,4]
x = curve.evaluate(t)  # compute (x,y)-coordinates of the curve evaluation
print(x.shape)  # 2 components at 150 evaluation points, this prints (150,2)

plt.plot(x[:, 0], x[:, 1])
plt.show()
