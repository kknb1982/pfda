import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

book = {}
book['title'] = input('Enter the title of the book: ')
book['author'] = input('Enter the author of the book: ')
book['isbn'] = input('Enter the ISBN of the book: ')

data = [book]

sql = "insert into books values (:title, :author, :isbn)"
cur.executemany(sql, data)
con.commit()

for row in cur.execute('select * from books'):
    print(f"row{row}")