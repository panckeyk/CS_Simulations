# This mathematical function helps user to calculate exponential of all the elements in the input array.

# syntax : 
# numpy.exp(array, out = None, where = True, casting = 'same_kind', order = 'K', dtype = None)

# parameters :
# array    : [array_like]Input array or object whose elements, we need to test.
# out      : [ndarray, optional]Output array with same dimensions as Input array, 
#             placed with result.
# **kwargs : Allows you to pass keyword variable length of argument to a function. 
#            It is used when we want to handle named argument in a function.
# where    : [array_like, optional]True value means to calculate the universal 
#            functions(ufunc) at that position, False value means to leave the  
#            value in the output alone.

import numpy as np

in_array = [1, 3, 5]
print (&quot;Input array : &quot;, in_array)

out_array = np.exp(in_array)
print (&quot;Output array : &quot;, out_array)