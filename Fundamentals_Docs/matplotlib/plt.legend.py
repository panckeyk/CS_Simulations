# which is used to place a legend on the axes. In this article, we will learn about the Matplotlib Legends.

# syntax:
# matplotlib.pyplot.legend(["blue", "green"], bbox_to_anchor=(0.75, 1.15), ncol=2)

# attributes: 

# shadow: [None or bool] Whether to draw a shadow behind the legend.It’s Default value is None.
# markerscale: [None or int or float] The relative size of legend markers compared with the originally drawn ones.The Default is None.
# numpoints: [None or int] The number of marker points in the legend when creating a legend entry for a Line2D (line).The Default is None.
# fontsize: The font size of the legend.If the value is numeric the size will be the absolute font size in points.
# facecolor: [None or “inherit” or color] The legend’s background color.
# edgecolor: [None or “inherit” or color] The legend’s background patch edge color.

import numpy as np 
import matplotlib.pyplot as plt 

def legend_example():
    # X-axis values 
    x = [1, 2, 3, 4, 5] 

    # Y-axis values 
    y = [1, 4, 9, 16, 25] 

    # Function to plot 
    plt.plot(x, y) 

    # Function add a legend 
    plt.legend(['single element']) 

    # function to show the plot 
    plt.show()

legend_example()

def position_legend():
    # Y-axis values
    y1 = [2, 3, 4.5]

    # Y-axis values
    y2 = [1, 1.5, 5]

    # Function to plot
    plt.plot(y1)
    plt.plot(y2)

    # Function add a legend
    plt.legend(["blue", "green"], loc="lower right")

    # function to show the plot
    plt.show()

position_legend()

def multiple_legend():
    # X-axis values
    x = np.arange(5)

    # Y-axis values
    y1 = [1, 2, 3, 4, 5]

    # Y-axis values
    y2 = [1, 4, 9, 16, 25]

    # Function to plot
    plt.plot(x, y1, label='Numbers')
    plt.plot(x, y2, label='Square of numbers')

    # Function add a legend
    plt.legend()

    # function to show the plot
    plt.show()

multiple_legend()

def outside_legend():
    # X-axis values
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Y-axis values
    y1 = [0, 3, 6, 9, 12, 15, 18, 21, 24]
    # Y-axis values
    y2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Function to plot
    plt.plot(y1, label="y = x")
    plt.plot(y2, label="y = 3x")

    # Function add a legend
    plt.legend(bbox_to_anchor=(0.75, 1.15), ncol=2)
    plt.show()

outside_legend()