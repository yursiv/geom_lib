import numpy as np

import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
from matplotlib.path import Path

from shapely.geometry import Polygon


# Plots a Polygon to pyplot `ax`
def plot_polygon(ax, poly, **kwargs):
    path = Path.make_compound_path(
        Path(np.asarray(poly.exterior.coords)[:, :2]),
        *[Path(np.asarray(ring.coords)[:, :2]) for ring in poly.interiors])

    patch = PathPatch(path, **kwargs)
    collection = PatchCollection([patch], **kwargs)

    ax.add_collection(collection, autolim=True)
    ax.autoscale_view()
    return collection


# Input polygon with two holes
# (remember exterior point order is ccw, holes cw else
# holes may not appear as holes.)
polygon = Polygon(shell=((0, 0), (10, 0), (10, 10), (0, 10)),
                  holes=(((1, 3), (5, 3), (5, 1), (1, 1)),
                         ((9, 9), (9, 8), (8, 8), (8, 9))))

fig, ax = plt.subplots()
plot_polygon(ax, polygon, facecolor='lightblue', edgecolor='red')
