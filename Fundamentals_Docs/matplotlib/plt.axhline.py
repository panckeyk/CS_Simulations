# used to add a horizontal line across the axis

# syntax :
# matplotlib.pyplot.axhline(y=0, xmin=0, xmax=1, **kwargs)

# Parameters: 
# y: float, the y-coordinate of the horizontal line
# xmin: float, the minimum x-coordinate of the line
# xmax: float, the maximum x-coordinate of the line
# **kwargs: additional keyword arguments to pass to the line properties

import numpy as np
import matplotlib.pyplot as plt

def first_example(): 
    t = np.linspace(-10, 10, 100)
    sig = 1/t 

    plt.axhline(y = 0, color ="green", linestyle ="--")
    plt.axhline(y = 0.5, color ="green", linestyle =":")
    plt.axhline(y = 1.0, color ="green", linestyle ="--")

    plt.axvline(color="black")

    plt.plot(t, sig, linewidth = 2, label = r"$\sigma(t) = \frac{1}{x}$")

    plt.xlim(-10, 10)
    plt.xlabel("t")
    plt.title("Graph of 1 / x")
    plt.legend(fontsize = 14)

    plt.show()

def second_example():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 13, 100)

    plt.rcParams['lines.linewidth'] = 2
    plt.figure()

    plt.plot(x, np.sin(x), label ='Line1', 
            color ='green', linestyle ="--")

    plt.plot(x, np.sin(x + 0.5), label ='Line2',
            color ='black', linestyle =":")

    plt.axhline(0, label ='Line3', color ='black')


    plt.title('Axhline() Example')
    l = plt.legend(loc ='upper right')

    # legend between blue and orange 
    # line
    l.set_zorder(2.5)

    plt.show()

first_example()
second_example()