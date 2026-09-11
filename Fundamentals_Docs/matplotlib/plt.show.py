# used to display all figures

# syntax : 
# matplotlib.pyplot.show(*args, **kw)

# parameters:
# block : This parameter is used to override the blocking behavior described above.

# example code:
import matplotlib.pyplot as plt 
import numpy as np

def sample_usage_show():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) 
    plt.show()

sample_usage_show()

def second_example():
    x = np.linspace(0, 10, 500)
    y = np.sin(x**2)+np.cos(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, label ='Line 1')

    ax.plot(x, y - 0.6, label ='Line 2')

    ax.legend()

    fig.suptitle('matplotlib.pyplot.show() Example')
    plt.show()

second_example()