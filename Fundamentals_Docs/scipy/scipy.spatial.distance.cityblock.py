# calculates the distance between two spatial points 
# (x1, y1) and (x2, y2) - first is sub1 and second is sub2

# example code : 
from scipy.spatial.distance import cityblock

location_a = [1,2]
location_b = [4,6]

blocks = cityblock(location_a, location_b)
print(blocks)
