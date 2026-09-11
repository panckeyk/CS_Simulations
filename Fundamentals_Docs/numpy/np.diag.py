# numpy.diag(a, k=0) : Extracts and construct a diagonal array 

# parameters : 
# a : array_like 
# k : [int, optional, 0 by default]
#           Diagonal we require; k>0 means diagonal above main diagonal or vice versa.

import numpy as geek

# matrix creation by array input
a = geek.matrix([[1, 21, 30], 
                 [63 ,434, 3], 
                 [54, 54, 56]])

print("Main Diagonal elements : \n", geek.diag(a), "\n")

print("Diagonal above main diagonal : \n", geek.diag(a, 1), "\n")

print("Diagonal below main diagonal : \n", geek.diag(a, -1))