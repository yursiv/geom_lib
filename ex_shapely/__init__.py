import shapely
from shapely.geometry import Point, Polygon

patch:Polygon = Point(0.0, 0.0).buffer(10.0)
print(patch)
print(patch.area)
print(patch.geom_type)
