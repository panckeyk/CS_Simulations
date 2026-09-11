# used to create a rectangular grid out of two given one-dimensional arrays representing the cartesian indexing or matrix indexing 

# it returns a two 2-dimensional arrays representin the X and Y coordinates of all the points 

# example code :
import numpy as np
x = np.linspace(-4, 4, 9)
y = np.linspace(-5, 5, 11)

# The meshgrid function returns
# two 2-dimensional arrays 
x_1, y_1 = np.meshgrid(x, y)

print("x_1 = ")
print(x_1)
print("y_1 = ")
print(y_1)