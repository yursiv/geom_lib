import numpy as np


import matplotlib as plt
from matplotlib.pyplot import plot

xvalues = np.arange(0, 5)
yvalues = np.arange(-1, 4)

xx, yy = np.meshgrid(xvalues, yvalues)
xx, yy = np.meshgrid(xvalues, yvalues)

plot(xx, yy, marker='.', color='k', linestyle='none')
