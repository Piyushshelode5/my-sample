import sqlite3
x=sqlite3.connect("sample.db")
y='''DELETE studentinfo"
WHERE rollno =3'''
x.execute(y)
x.commit()
x.close