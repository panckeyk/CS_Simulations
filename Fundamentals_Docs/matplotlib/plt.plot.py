# used to create 2D plots such as line graphs and scatter plots
# The plot() function allows us to plot data points, customize line styles, markers and colors making it useful for various types of visualizations.
# In this article, we'll see how to use this function to plot data in Python.

# syntax : 
# matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)

# parameters:
# x, y: Represent horizontal and vertical coordinates for the data points.
# fmt: A format string that defines the line style, marker and colour.
# data: The optional parameter can be an object containing labelled data which makes it easier to handle datasets directly.

# example code :


import matplotlib.pyplot as plt  
import numpy as np

def line_plots(): 
    plt.plot([1, 2, 3, 4, 5])
    plt.title('Basic Line Plot')
    plt.show()

line_plots()

def multiple_line_plots():
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x, y1, label='Sin(x)', color='blue')
    plt.plot(x, y2, label='Cos(x)', color='red', linestyle='--')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Multiple Lines Plot')
    plt.legend()
    plt.show()

multiple_line_plots()

def scatter_plot(): 
    np.random.seed(42)
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.plot(x, y, marker='o', linestyle='', color='red', label='Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot Example')
    plt.legend()
    plt.show()

scatter_plot()

def plotting_multiple_curves():
    np.random.seed(19680801) 
    xdata = np.random.random([2, 10]) 
    xdata1 = xdata[0, :] 
    xdata2 = xdata[1, :] 
    xdata1.sort() 
    xdata2.sort() 
    ydata1 = xdata1 ** 2
    ydata2 = 1 - xdata2 ** 3
    plt.plot(xdata1, ydata1, color ='tab:blue') 
    plt.plot(xdata2, ydata2, color ='tab:orange') 
    plt.xlim([0, 1]) 
    plt.ylim([0, 1]) 
    plt.title('matplotlib.pyplot.plot() example 2') 
    plt.show()

plotting_multiple_curves()