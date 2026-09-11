# used to stack 1-D arrays as columns into a 2-D array
# It takes a sequence of 1-D arrays and stack them as columns to make a single 2-D array. 2-D arrays are stacked as-is, just like with hstack function.

# Syntax  :  numpy.column_stack(tup)

# Parameters : 
# tup   : [sequence of ndarrays] Tuple containing arrays to be stacked. The arrays must have the same first dimension.
# Return  : [stacked 2-D array] The stacked 2-D array of the input arrays.
  
import numpy as geek

# input array
in_arr1 = geek.array(( 1, 2, 3 ))
print ("1st Input array : \n", in_arr1) 

in_arr2 = geek.array(( 4, 5, 6 ))
print ("2nd Input array : \n", in_arr2) 

# Stacking the two arrays 
out_arr = geek.column_stack((in_arr1, in_arr2))
print ("Output stacked array:\n ", out_arr)