# function calculates the distance between each pair of the two collections of inputs.

# syntax : 
# scipy.stats.cdist(array, axis=0)

# parameters 
# array: Input array or object having the elements to calculate the distance between each pair of the two collections of inputs. 
# axis: Axis along which to be computed. By default axis = 0 
# Returns : distance between each pair of the two collections of inputs.

from scipy.spatial.distance import cdist
a = [[1, 3, 27], [3, 6, 8]]
arr1 = cdist(a, a) 

print(arr1)

