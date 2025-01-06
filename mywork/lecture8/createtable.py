import mysql.connector

db = mysql.connector.connect(
    host='localhost',   
    user='root',
    password='',
    database='wsaa'
)

cursor = db.cursor()
sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

cursor.execute(sql)
cursor.close()
db.close()