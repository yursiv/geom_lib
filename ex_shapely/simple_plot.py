from shapely.geometry import Polygon
import matplotlib.pyplot as plt

polygon1 = Polygon([(0, 5), (1, 1), (3, 0), ])

# x, y = polygon1.exterior.xy
# plt.plot(x, y)
plt.plot(*polygon1.exterior.xy)
