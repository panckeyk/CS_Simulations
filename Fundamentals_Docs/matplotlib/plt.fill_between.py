# used to fill area between two horizontal curves. Two points (x, y1) and (x, y2) define the curves

# this creates one or more polygons describing the filled areas.

# The 'where' parameter can be used to selectively fill some areas. By default, edges connect the given points directly. The 'step' parameter is used if the filling needs to be a step function.

# syntax :
# matplotlib.pyplot.fill_between(x, y1, y2=0, where=None, step=None, interpolate=False, *, data=None, **kwargs) 

# parameters : 
# x: It is array of length N. These are the y coordinates of the nodes that define the curves.

# y1:It is an array of length N or a scalar. This represents the x coordinates of the nodes that define the first curve.

# y2: It is an array of length N and is optional in nature. Its default value is 0. This represents the x coordinates of the nodes that define the second curve.

# where: it is an array of boolean values of length N. It is defined if there is a need to exclude some vertical regions from being filled. It is important to note that this definition means that an isolated true value in between two false values is where it will not do the filling. Adjacent False values results in not filling both sides of the True value.

# interpolate: It is an optional parameter that accepts boolean values. It is only relevant if where is used and two curves are crossing each other. Semantically where if generally used for y1>y2 or similar cases. By default the filled regions will be placed at the x-array positions defining a filled polygonal area. The section of x that has the intersection are simply clipped. Setting this parameter to True results in calculation of the actual point of intersection and extends to the filled regions till the points.

# step: This is an optional parameter that accepts one of the three values namely, 'pre', 'post' and 'mid'. This is used to specify where the steps will occur.
# pre: From every y position the x value is continued constantlyto the left, ie, the interval (x[i-1], x[i]) has the value y[i].
# post:From every y position the x value is continued constantly to the right, ie, the interval (x[i], x[i+1]) has the value y[i].
# mid: Half way between the x positions these steps occur.

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)

# plotting the lines
a1 = 4 - 2*x
a2 = 3 - 0.5*x
a3 = 1 -x

# The upper edge of
# polygon
a4 = np.minimum(a1, a2)

# Setting the y-limit
plt.ylim(0, 5)

# Plot the lines
plt.plot(x, a1,
        x, a2,
        x, a3)

# Filling between line a3 
# and line a4
plt.fill_between(x, a3, a4, color='green',
                 alpha=0.5)
plt.show()