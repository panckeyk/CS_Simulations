# used to generate an array of evenly spaced values between two specified numbers 
#  instead of defining a step size, the total number of required values is specified and numpy automatically calculate the spacing between them

# syntax : 
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

# parameters : 
# start : Starting value (default 0)
# stop : Ending value of the range 
# num : Number of values to generate (default is 50)
# endpoint : Includes stop if True (default True)
# retstep : Return step size if True (default False)
# dtype : Output array data type 
# axis : Axis for generation when inputs are array-like (default 0)

# example code :
import numpy as np
a = np.linspace(1, 10, num=10)
print("array of evenly spaced values between 1 and 10 : ", a)