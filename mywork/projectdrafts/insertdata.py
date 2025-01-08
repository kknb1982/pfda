import mysql.connector as msql
import requests
import gzip
import csv
from io import BytesIO, TextIOWrapper
import pandas as pd


# Data source
station = '00TG6'
url = "https://bulk.meteostat.net/v2/daily/" + station + ".csv.gz"
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Decompress the gzip file
data = gzip.GzipFile(fileobj=BytesIO(response.content))

# Read in the CSV file
df = pd.read_csv(data, usecols=[0,1,2,3],names =['Date', 'tavg', 'tmin', 'tmax'], parse_dates =['Date'])

# Insert column to record the station ID
df["station_ID"] = station

# Create columns for the year and month of the data
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Convert date column to string
df["Date"] = df["Date"].dt.strftime('%Y-%m-%d')

print(df.head())

try:
    con = msql.connect(host='localhost', database='weather', user='root', password='')

    if con.is_connected():
        cursor = con.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print(f"You're connected to database: ", record)
        
        for i, row in df.iterrows():
            sql = "INSERT INTO weather.ontario_data (date, average_temp, min_temp, max_temp) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, tuple(row))
       
        print("Record inserted")
        
        con.commit()

except msql.Error as err:
    print(err.msg)

finally:
    if con.is_connected():
        cursor.close()
        con.close()


# Connect to the database
#con = mysql.connector.connect(**db_config)
#cursor = con.cursor()

# download and decompress the data
#response = requests.get(csv_url)
#data = gzip.GzipFile(fileobj=BytesIO(response.content))

# Read the CSV file
#csv_reader = csv.reader(TextIOWrapper(data, 'utf-8'))

## Insert
#insert_query = """
#INSERT INTO ontario (date, average_temp, min_temp, max_temp)
#VALUES (%s, %s, %s, %s)
#"""

# Skip the header row if it exists
#next(csv_reader)

# Insert rows into the database
#for row in csv_reader:
 #   cursor.execute(insert_query, row)

# Commit the transaction
#con.commit()

# Close the cursor and connection
#cursor.close()
#con.close()