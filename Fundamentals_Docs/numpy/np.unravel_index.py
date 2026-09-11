# converts a flat index or array of flat indices into a tuple of coordinate arrays 

# syntax : 
# numpy.unravel_index(indices, shape, order = 'C')

# parameters : 
# indices  : [array_like] An integer array whose elements are indices into the flattened version of an array of dimensions shape.
# shape  : [tuple of ints] The shape of the array to use for unraveling indices.
# order  : [{‘C’, ‘F’}, optional] Determines whether the multi-index should be viewed as indexing in row-major (C-style) or column-major (Fortran-style) order.

import numpy as np 

sample = np.unravel_index([22, 41, 37], (7, 6))
print("Tuple of coordinate arrays: ", sample)