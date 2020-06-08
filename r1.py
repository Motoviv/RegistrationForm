import sqlite3
db=sqlite3.connect('form.db')
cr=db.cursor()
cr.execute('create table regis(UNAME text,UPASS text,UCN text)')
db.commit()
db.close()
print('table created')

