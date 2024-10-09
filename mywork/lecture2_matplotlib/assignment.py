# Import weather data from a url

# Author: Kirstin Barnett

FILENAME = "weatherreadings1.csv"
DATADIR = "C:/Users/kirst/OneDrive - Atlantic TU/pfda/PFDA-courseware/assignment/"

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (DATADIR + FILENAME, parse_dates=['reportEndDateTime'])

y = df['dryBulbTemperature_Celsius']
x = df['reportEndDateTime']

fig, ax = plt.subplots()

ax.scatter(x,y)


#labels = ax.get_xticklabels()
#ax.xaxis.set_ticks(str(dateofmeasurement))

#plt.setp(labels, rotation = 45, horizontalalignment = 'right')
#ax.xaxis.set_major_formatter(xformatter)

#ax.set(xlabel = "Date", ylabel = "Temperature in degrees celsius", title = "A plot of the temperature over time") 
#ax.set_xticks(labels)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# Step 1: Read the CSV file
# Replace 'your_file.csv' with your actual file name and 'date_column' with your date column name
# df = pd.read_csv('your_file.csv', parse_dates=['date_column'])

# Step 2: Set the date column as the index (optional but useful for plotting)
# df.set_index('date_column', inplace=True)

# Step 3: Plot the data
# plt.figure(figsize=(10, 5))
# plt.plot(df.index, df['value_column'])  # Replace 'value_column' with your actual value column name
# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.title('Your Plot Title')

# plt.tight_layout()  # Adjust layout to make room for x-axis labels
# plt.show()