# A quick summary of how to read in a csv using Pandas

# Author: Kirstin Barnett

import pandas as pd

datadir = "../datafiles/"
filename = "people-100.csv"

# to limit columns

df = pd.read_csv(datadir + filename, parse_dates=['Date of birth'])

# df.info() shows how data was read in
print(df.info())


