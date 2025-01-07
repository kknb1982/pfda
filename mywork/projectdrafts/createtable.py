import mysql.connector as msql
from mysql.connector import Error

try:
    con = msql.connect(host='localhost', database='weather', user='root', password='')

    if con.is_connected():
        cursor = con.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print(f"You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS ontario_data')
        print('Creating table....')
        cursor.execute("CREATE TABLE ontario_data(station_ID varchar(8), date TIMESTAMP, average_temp float, min_temp float, max_temp float, month int, year int)")
        print("Table is created....")

except msql.Error as err:
    print(err.msg)

finally:
    if con.is_connected():
        cursor.close()
        con.close()