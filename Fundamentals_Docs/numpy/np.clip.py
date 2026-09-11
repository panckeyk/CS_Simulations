# function used to clip (limit) the values in an array 
# values outside the interval are clipped to the interval edges

# example : an interval of [0,1] is specified - values smaller than 0 become 0, and values larger than 1 become 1
# syntax : np.clip(a, a_min, a_max, out=None)
# paraneters :
# a : array containing elements to clip 
# a_min : minimum value 
# a_max : maximum value 
# out : output array to place the result  

import numpy as np

in_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
out_array = np.clip(in_array, a_min = 3, a_max = 7)

print("Original Array: ", in_array)
print("Clipped Array: ", out_array)