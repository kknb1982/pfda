#Read a cimple csv
#Author: Kirstin Barnett

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

print (DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    count = 0
    total = 0
    
    for line in reader:
        total += line['age']
        count += 1
    print (f"average is {(total/count)}")
        