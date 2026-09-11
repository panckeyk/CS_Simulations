# this function helps user to calculate trigonometric sine for all x(being the array elements)

# code example : 
import numpy as np
import math 

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("input array : ", in_array)

sin_values = np.sin(in_array)
print ("sine values of the input array : ", sin_values)