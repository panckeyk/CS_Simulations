# adds a color scale (color bar) to a plot, helping to interpret the relationship between data values and colors in colormapped plots

# example code : 
import matplotlib.pyplot as plt
import numpy as np

p = [100, 200, 150, 23, 30, 50, 156, 32, 67, 89] 
l = [50, 70, 100, 10, 10, 34, 56, 18, 35, 45]
r = [1, 0.53, 2, 0.76, 0.5, 2.125, 0.56, 1.28, 1.09, 1.02]

# scatterplot
plt.scatter(p, l, c=r, cmap="summer")

# add Colorbar
plt.colorbar(label="Like/Dislike Ratio", orientation="horizontal")  
plt.xlabel("Purchases")  
plt.ylabel("Likes")   
plt.title("Purchases vs Likes") 
plt.show()

