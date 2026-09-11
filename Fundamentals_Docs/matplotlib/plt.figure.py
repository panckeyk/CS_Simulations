# function is used to create a new figure for our plots. In Matplotlib a figure is like a blank space where all our plot elements such as axes, titles and labels are placed

# syntax : 
# matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)

# parameters : 
# num: A number to identify the figure.
# figsize: A tuple (width, height) in inches. This sets the size of the figure.
# dpi: Resolution of the figure.
# facecolor: Background colour of the figure.
# edgecolor: Colour of the border around the figure.
# frameon: If True frame around the figure is shown (default is True).
# clear: If True it clears any existing figure before creating a new one.
# kwargs: Other options we can use for extra customization.

# example code :
import matplotlib.pyplot as plt
import matplotlib.lines as lines 

def basic_figure_example():
    # Create a new figure with specified size
    fig = plt.figure() 

    # Add lines to the figure
    fig.add_artist(lines.Line2D([0, 1, 0.5], [0, 1, 0.3]))
    fig.add_artist(lines.Line2D([0, 1, 0.5], [1, 0, 0.2]))

    # Set title with custom font size and color
    plt.title('Simple Example of matplotlib.pyplot.figure()', fontsize=14, color='blue')

    # Show the plot
    plt.show()


def custom_figure_example():
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title('Figure with Custom Size')
    plt.show()

    # Show the plot
    plt.show()

def creating_multiple_figures():
    import matplotlib.pyplot as plt
    plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("First Figure")
    plt.show()
    plt.figure(figsize=(8, 6))
    plt.plot([1, 2, 3], [9, 4, 1])
    plt.title("Second Figure")
    plt.show()

    # Show the plots
    plt.show()

# basic_figure_example()
# custom_figure_example()
creating_multiple_figures()
