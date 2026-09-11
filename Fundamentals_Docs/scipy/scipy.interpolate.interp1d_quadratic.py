# Creates a one-dimensional piecewise quadratic interpolating function based on given data points.
# The function returns an interpolation function that can be used to evaluate the quadratic spline.

# syntax :
# scipy.interpolate.interp1d(x, y, kind='quadratic', axis=-1, copy=True, bounds_error=None, fill_value=nan, assume_sorted=False)

# parameters :
# x             : [1-D array_like] 1-D array of real values.
# y             : [array_like] N-D array of real values. The length of y along the interpolation axis must be equal to the length of x.
# kind          : [str or int, optional] Specifies the kind of interpolation. Set to 'quadratic' for second-order spline interpolation.
# axis          : [int, optional] Specifies the axis of y along which to interpolate. Default is the last axis (-1).
# copy          : [bool, optional] If True, the class makes internal copies of x and y. If False, references to x and y are used.
# bounds_error  : [bool, optional] If True, a ValueError is raised any time interpolation values are requested outside of the range of x.
# fill_value    : [array-like or (array-like, array_like) or "extrapolate", optional] Value used to fill requested points outside of the data range.
# assume_sorted : [bool, optional] If True, x is assumed to be in monotonically increasing order.

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Sample data points representing a curved relationship
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])

# Create the interpolation function using quadratic interpolation
f = interp1d(x, y, kind='quadratic')

# Define new, densely spaced x values to evaluate the quadratic spline
x_new = np.linspace(0, 5, num=100)
y_new = f(x_new)  # Evaluate the interpolation function

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'o', label='Original Data points')
plt.plot(x_new, y_new, '-', label='Quadratic Interpolation')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Interpolation using interp1d')
plt.grid(True)
plt.show()
