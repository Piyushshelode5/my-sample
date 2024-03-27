import sqlite3
x=sqlite3.connect("sample.db")
y='''UPDATE studentinfo
set totalmarks="81"
where rollno=5'''

x.execute(y)
x.commit()
x.close()



 