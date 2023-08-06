import numpy as np
from shapely.geometry import LineString
from shapely.ops import unary_union

line = LineString(([0, 0], [2, 1], [3, 2], [3.5, 1], [5, 2]))
print(line)