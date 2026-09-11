# commonly used probability distribution that models natural data such as test scores, heights, sensor readings, and measurement variations 

# example code :
# generate one random numebr from a standard normal distribution (mean = 0, standard deiation = 1)

import numpy as np
x = np.random.normal()
print("one random number from a standard normal distribution : ", x)

# syntax : 
# numpy.random.normal(loc=0.0, scale=1.0, size=None)

# parameters :
# loc: Mean (center) of the distribution.
# scale: Standard deviation (spread).
# size: Shape of the output (single value, list, matrix, etc.).

# example code : 
# create a 1-D array of 5 random numbers drawn from a normal distribution 
import numpy as np
array = np.random.normal(size=5)
print("\n 1-D array of 5 random numbers from a normal distribution : \n", array)

# example code : 
# example generates a 2×3 matrix with mean = 10 and standard deviation = 2, useful for simulations.
import numpy as np
m = np.random.normal(loc=10, scale=2, size=(2, 3))
print("\n 2x3 matrix of random numbers from a normal distribution with mean=10 and std=2 : \n", m)
