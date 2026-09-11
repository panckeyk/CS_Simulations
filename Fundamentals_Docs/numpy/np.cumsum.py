# its a function that is used to compute the cumultataive sum of elements in an array 
# cumultative sum : sequence where each element is the sum of previous elements plus itself 

# example : 
# array = [1, 2, 3, 4, 5]
# cumsum = [1, 3, 6, 10, 15]

# example code : 
import numpy as np
array = np.array([1, 2, 3, 4, 5])
cumsum = np.cumsum(array)

print("Original Array: ", array)
print("Cumulative Sum: ", cumsum)