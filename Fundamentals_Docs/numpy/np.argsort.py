# returns the indices that would sort an array
# it gives you the indices that you would use to reoirder the elements in an array to be sorted 

# example code :
import numpy as np

a = np.array([3, 1, 2])
index = np.argsort(a)

print("array : ", a)
print("indices that would sort the array : ", index)
print("sorted array : ", a[index])
