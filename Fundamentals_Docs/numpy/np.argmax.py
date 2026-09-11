# it returns indices of the max elements of the array in a particular axis
# syntax : 
# numpy.argmax(a, axis=None, out=None)
# parameters :
# a : input array to work on 
# axis : [int, optional] along a specified axis like 0 or 1 
# out : [array optional] provides a feature to insert output to the out array and it should be of appropriate shape and dtype 

import numpy as np

# 2d array example
array = np.arange(12).reshape(3, 4)
print("Original Array: \n", array)

# no axis mentioned, so works on entire array 
print("Indices of max elements: ", np.argmax(array))

# returning indices of the max element 
# as per the indices 
print("\n Indices of max elements along axis 0: ", np.argmax(array, axis=0))
print("\n Indices of max elements along axis 1: ", np.argmax(array, axis=1))
