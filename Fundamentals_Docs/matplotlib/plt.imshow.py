# used to display images in a plot 
# it allows you to visualize images as 2D data 
# this function is widely used for displaying images, matrices, or heatmaps where each value in the array corresponds to a color 

# example code : 
import numpy as np
import matplotlib.pyplot as plt

a = np.random.random((10, 10))

# Display the array as an image
plt.imshow(a, cmap='viridis', interpolation='nearest')
plt.colorbar()  
plt.show()

# Explanation:
# - np.random.random((10, 10)) creates a 10x10 array of random numbers between 0 and 1.
# - imshow() visualizes the array as an image, using the 'viridis' colormap and 'nearest' interpolation.
# - plt.colorbar() adds a colorbar to the side of the image, showing the value-to-color mapping.

# syntax :
# matplotlib.pyplot.imshow(X, cmap=None, norm=None, *, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, colorizer=None, origin=None, extent=None, interpolation_stage=None, filternorm=True, filterrad=4.0, resample=None, url=None, data=None, **kwargs)

def twoD_data():
    from matplotlib.colors import LogNorm 
      
    dx, dy = 0.015, 0.05
    y, x = np.mgrid[slice(-4, 4 + dy, dy), 
            slice(-4, 4 + dx, dx)] 
    z = (1 - x / 3. + x ** 5 + y ** 5) * np.exp(-x ** 2 - y ** 2) 
    z = z[:-1, :-1] 
    z_min, z_max = -np.abs(z).max(), np.abs(z).max() 

    c = plt.imshow(z, cmap ='Greens', vmin = z_min, vmax = z_max, 
            extent =[x.min(), x.max(), y.min(), y.max()], 
              interpolation ='nearest', origin ='lower') 
    plt.colorbar(c) 

    plt.title('matplotlib.pyplot.imshow() function Example', fontweight ="bold") 
    plt.show()

twoD_data()



