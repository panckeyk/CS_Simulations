# part of array computation and analysis tools, which is used to find the smallest value in an array. It is an efficient method for determining minimum values accross various dimensions of an array 

# example code 
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Minimum value in array a: ", np.min(a))
print("Minimum value in array b: ", np.min(b))
print("Minimum value in array a and b: ", np.min([a, b]))