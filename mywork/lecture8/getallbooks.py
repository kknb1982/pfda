import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

for row in cur.execute('select * from books'):
    print(f"row{row}")