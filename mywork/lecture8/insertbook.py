import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

result = cur.execute("select * from movies")
print(result.fetchone())

sql = """ 
    INSERT INTO movies VALUES 
        ('Finding Nemo', '2005', '8'),
        ('Tiddler', '202', '9.1')
    """
cur.execute(sql)
con.commit()

result = cur.execute('select * from movies')
print(result.fetchone())
con.close() 