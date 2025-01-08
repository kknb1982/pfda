import mysql.connector
import requests
import gzip
import csv
from io import BytesIO, TextIOWrapper

db_config = mysql.connector.connect(
    host='localhost',   
    user='root',
    password='',
    database='weather'
)

# Data source
station = '00TG6'
url = "https://bulk.meteostat.net/v2/daily/" + station + ".csv.gz"

# Connect to the database
con = mysql.connector.connect(**db_config)
cursor = con.cursor()

# download and decompress the data
response = requests.get(csv_url)
data = gzip.GzipFile(fileobj=BytesIO(response.content))

# Read the CSV file
csv_reader = csv.reader(TextIOWrapper(data, 'utf-8'))

## Insert
insert_query = """
INSERT INTO ontario (date, average_temp, min_temp, max_temp)
VALUES (%s, %s, %s, %s)
"""

# Skip the header row if it exists
next(csv_reader)

# Insert rows into the database
for row in csv_reader:
    cursor.execute(insert_query, row)

# Commit the transaction
con.commit()

# Close the cursor and connection
cursor.close()
con.close()