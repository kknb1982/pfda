## How to use Matplotlib
# author: Kirstin Barnett


import matplotlib.pyplot as plt
import numpy as np

x = 0.5 + np.arange(9)
y = [1,8,9,1,2,5,7,8,5]
y2 = [1.3,8.4,9.5,1.0,2.8,5.1,7.7,8.6,5.5]

fig, ax = plt.subplots()
ax.bar(x,y2)

ax.set(xlabel = "leaf size", ylabel = "tree size", title = "made up")

def currencyformatter(x,pos):
    s = f"${x}M"
    return s

labels = ax.get_xticklabels()
plt.setp(labels, rotation = 45, horizontalalignment = 'right')
ax.xaxis.set_major_formatter(currencyformatter)

# ax.text(1, 8, "text test", fontsize=10, verticalalignment='center')

ax.annotate('blah',(2.2,9.5), xytext=(1,9), arrowprops=dict(facecolor = "black", shrink=0.05))
plt.show()