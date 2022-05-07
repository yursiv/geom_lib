import numpy as np
import matplotlib.pyplot as plt

def enrich(x, y):
    x2 = []
    y2 = []
    for i in range(len(x)-1):
        x2 += [x[i], (x[i] + x[i+1]) / 2]
        y2 += [y[i], (y[i] + y[i + 1]) / 2]
    x2 += [x[-1]]
    y2 += [y[-1]]
    assert len(x2) == len(y2)
    return x2, y2

# data = np.loadtxt('newsorted.txt')
# x = data[:, 0]
# y = data[:, 1]

x = np.linspace(0, 1, 100)
y = np.sin(x) + np.cos(x)

for _ in range(0):
    x, y = enrich(x, y)

dx = np.gradient(x, x)  # first derivatives
dy = np.gradient(y, x)

d2x = np.gradient(dx, x)  # second derivatives
d2y = np.gradient(dy, x)

cur = np.abs(d2y) / (np.sqrt(1 + dy ** 2)) ** 1.5  # curvature


# My interpolation with a lot of points made quickly
x2 = np.linspace(400, 600, num=100)
y2 = -0.0225*(x2 - 500)**2 + 250

dy2 = np.gradient(y2, x2)

d2y2 = np.gradient(dy2, x2)

cur2 = np.abs(d2y2) / (np.sqrt(1 + dy2 ** 2)) ** 1.5  # curvature

plt.figure(1)

plt.subplot(221)
plt.plot(x, y, 'b', x2, y2, 'r')
plt.legend(['new sorted values', 'My interpolation values'])
plt.title('y=f(x)')
plt.subplot(222)
plt.plot(x, cur, 'b', x2, cur2, 'r')
plt.legend(['new sorted values', 'My interpolation values'])
plt.title('curvature')
plt.subplot(223)
plt.plot(x, dy, 'b', x2, dy2, 'r')
plt.legend(['new sorted values', 'My interpolation values'])
plt.title('dy/dx')
plt.subplot(224)
plt.plot(x, d2y, 'b', x2, d2y2, 'r')
plt.legend(['new sorted values', 'My interpolation values'])
plt.title('d2y/dx2')

plt.show()