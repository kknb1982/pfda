## Read in weather station information

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Import the weather station data

df = pd.read_json("https://bulk.meteostat.net/v2/stations/lite.json.gz")

# df.columns() shows the column titles data was read in
print(df.columns)

print(df['country'].unique)