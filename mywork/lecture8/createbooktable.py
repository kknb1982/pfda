import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

sql = 'CREATE TABLE movies(title, year, rating)'

cur.execute(sql)
con.close()