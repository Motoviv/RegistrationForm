#to insert a table
import sqlite3
db=sqlite3.connect('form.db')
cr=db.cursor()
cr.execute('create table ins(URNO text,UPASS text,UPHY text,UCHE text,UMATHS text)')

db.commit()
db.close()
print('table created')

