# used for handling large, multi-dimensional array and matrices

# types of arrays :
# one dimensional array 
# - stores elements in a single row 
import numpy as np

# example code : 
array = [1,2,3,4,5]
numpy_array = np.array(array)

print("list : ", array)
print("numpy array : ", numpy_array)
print("type of list : ", type(array))
print("type of numpy array : ", type(numpy_array))

# multi dimensional array
# - stores elements in multiple rows and 
# - storesdata in a two or more dimension 

# example code : 
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [9,10,11,12]
multiD_array = np.array([l1, l2, l3])
print("\n multi dimensional array : \n", multiD_array)



