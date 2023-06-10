# https://gis.stackexchange.com/questions/362370/divide-a-polygon-into-multiple-small-polygons-using-a-multilinestring
# https://stackoverflow.com/questions/63876018/cut-a-shapely-polygon-into-n-equally-sized-polygons
from shapely.geometry import Polygon, LineString
from shapely.ops import linemerge, unary_union, polygonize

poly = Polygon([(0, 0), (4, 0), (4, 4), (2, 5), (0, 4)])

lines = [
    LineString([(0, 1), (1, 1), (2, 1), (5, 1)]),
    LineString([(1, 1), (2, 1), (3, 3), (5, 3)]),
    LineString([(.5, -1), (.5, 5)]), poly.boundary]

lines = unary_union(lines)
lines = linemerge(lines)
polygons = polygonize(lines)

print("polys: ", polygons)

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

fig, ax = plt.subplots()
# for p in list(polygons)[2:]:
for p in polygons:
    plot_polygon(ax, p, facecolor='lightblue', edgecolor='red')
