# Import weather data from a url

# Author: Kirstin Barnett

FILENAME = "weatherreadings1.csv"
DATADIR = "C:/Users/kirst/OneDrive - Atlantic TU/pfda/PFDA-courseware/assignment/"

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (DATADIR + FILENAME)

y = df['dryBulbTemperature_Celsius']
x = df['reportEndDateTime']

fig, ax = plt.subplots()
ax.scatter(x,y)

ax.set(xlabel = "Date", ylabel = "Temperature in degrees celsius", title = "A plot of the temperature over time")

plt.show()

#def currencyformatter(x,pos):
    #s = f"${x}M"
    #return s

#labels = ax.get_xticklabels()
#plt.setp(labels, rotation = 45, horizontalalignment = 'right')
#ax.xaxis.set_major_formatter(currencyformatter)

# ax.text(1, 8, "text test", fontsize=10, verticalalignment='center')

#ax.annotate('blah',(2.2,9.5), xytext=(1,9), arrowprops=dict(facecolor = "black", shrink=0.05))




