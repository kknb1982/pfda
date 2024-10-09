# How to plot on multiple axes
# Author: Kirstin Barnett

import matplotlib.pyplot as plt
import numpy as np

num_cols = 3
num_rows = 2

data = [
    [2,4,5,6,3,5,6,7],
    [9,8,7,6,5,4,3,2],
    [1,2,3,4,5,6,7,8],
    [5,5,5,5,5,5,5,5]
]

x = 0.5 + np.arange(8)

fig, axs = plt.subplots(ncols=num_cols, nrows=num_rows, figsize =(8,4))

count = 0

for row in range(num_rows):
    for col in range(num_cols):
        axs[row,col].plot(x,data[count]) 
        count =+ 1


plt.show()