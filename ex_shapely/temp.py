# https://stackoverflow.com/questions/66010964/fastest-way-to-produce-a-grid-of-points-that-fall-within-a-polygon-or-shape
# https://stackoverflow.com/questions/70351106/how-to-find-the-intersection-time-of-a-parameterized-curve-with-a-shape/70390140#70390140

from shapely.geometry import Point
from shapely.prepared import prep

points = [...]  # large list of points
polygon = Point(0.0, 0.0).buffer(1.0)
prepared_polygon = prep(polygon)

print(prepared_polygon)
