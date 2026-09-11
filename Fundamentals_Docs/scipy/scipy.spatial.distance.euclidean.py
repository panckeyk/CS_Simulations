# calculates exact straight line distance between two spatial points (x1, y1) and (x2, y2) - first is sub1 and second is sub2

# example code :
from scipy.spatial.distance import euclidean

store_location = [0, 0]
customer_location = [3, 4]

distance = euclidean(store_location, customer_location)
print(distance)