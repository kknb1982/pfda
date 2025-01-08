import mysql.connector

db = mysql.connector.connect(
    host='localhost',   
    user='root',
    password='',
    database='weather'
)

cursor = db.cursor()
TABLES = {}
TABLES['ontario'] = [
"CREATE TABLE ontario ("
" 'id' INT AUTO_INCREMENT PRIMARY KEY,"
" 'station_ID' INT,'"
"' date' DATE,"
"'average_temp' FLOAT,"
"'max_temp' FLOAT,"
"'min_temp' FLOAT,"
"'month' INT,"
"'year' INT"]

TABLES['countries'] = ["CREATE TABLE countries ("id' INT AUTO_INCREMENT PRIMARY KEY,"country_name' VARCHAR(50))"]

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print(f"Creating table {table_name}")
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        print(err.msg)

cursor.close()
db.close()