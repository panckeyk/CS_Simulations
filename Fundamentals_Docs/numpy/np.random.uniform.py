# used when every value in a given range has an equal probability of occuring 

# example code : 
# generate one random value from a uniform distribution 
# This generates a random floating-point number between 0 and 1, the default uniform range.
import numpy as np 
num = np.random.uniform()
print("one random value from a uniform distribution : \n", num)

# syntax: 
# numpy.random.uniform(low=0.0, high=1.0, size=None)

# parameters :
# low: Lower bound of the range (inclusive).
# high: Upper bound of the range (exclusive).
# size: Shape of the output array.

# example code :
# This example shows how to generate five random numbers between 0 and 1 multiple uniform distribution values
array = np.random.uniform(size=5)
print("array of 5 random values from a uniform distribution : \n", array)

