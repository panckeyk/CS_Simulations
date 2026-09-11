# axes module of matplotlib library is used to add a horizontal span (rectangle) across the axis.

# syntax : 
# Axes.axhspan(self, ymin, ymax, xmin=0, xmax=1, **kwargs)

# parameters : 
# ymin: This parameter is the lower limit of the horizontal span in data units.
# ymax: This parameter is the upper limit of the horizontal span in data units.
# xmin: This parameter is the lower limit of the vertical span in data units.
# xmax: This parameter is the upper limit of the vertical span in data units.

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.axhspan(1.25, 1.55, facecolor='g', alpha = 0.5)
ax.set_title('matplotlib.axes.Axes.axhspan() Example')

plt.show()