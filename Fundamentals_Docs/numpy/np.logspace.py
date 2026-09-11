# function is used to generate numbers that are evenly spaced on a logarithmic scale 
# Instead of creating values with equal linear differences, this function generates values that are evenly spaced according to powers of a base value.

# syntax : 
# numpy.logspace(start, stop, num = 50, endpoint=true, base=10.0, dtype=None)

# parameters : 
# start : Starting exponent of the sequence (base ** start)
# stop : Ending exponent of the sequence (base ** stop)
# num : Number of samples to generate. Default is 50.
# endpoint : Includes the stop value if True (default True)
# base : Base of the logarithm (default is 10)
# dtype : Data type of the output array 

# example code : 
import numpy as np
a = np.logspace(2, 3, num=4)
print(a)

