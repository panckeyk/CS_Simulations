# function which creates a one-dimensional piecewise linear or spline interpolating function based on given data points
# function returns an interpolation function that can be used to compute interpolated values based on the provided data points.

# syntax :
# scipy.interpolate.interp1d(x , y , kind , axis , copy , bounds_error , fill_value , assume_sorted) 

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Sample data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 2, 5, 4])

# Create the interpolation function using linear interpolation
f = interp1d(x, y, kind='linear')

# Define new x values for interpolation
x_new = np.linspace(0, 4, num=10)
y_new = f(x_new)  # Evaluate the interpolation function

# Plot the results
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new, '-', label='Interpolated values')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Interpolation using interp1d')
plt.show()