# part of array computation and analysis tools, which is used to find the largest value in an array. It is an efficient method for determining maximum values across various dimensions of an array .

# example code : 
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Maximum value in array a: ", np.max(a))
print("Maximum value in array b: ", np.max(b))
print("Maximum value in array a and b: ", np.max([a, b]))
