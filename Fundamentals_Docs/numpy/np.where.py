# used for conditional selection and replacement in Numpy arrays 
# used to : 
# Find indices(index) that satisfy a condition
# Build a new array by choosing values from two options depending on a condition

# example : get indices where elements is greater than 20 
import numpy as np 
array = np.array([10, 20, 30, 40, 50])
indices = np.where(array > 20)

print("Original Array: ", array)
print("Indices where elements are greater than 20: ", indices)