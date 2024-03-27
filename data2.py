import sqlite3
x=sqlite3.connect("sample.db")
x.execute('''CREATE TABLE studentinfo(ROLLNO INTEGER varchar(50),NAME varchar(50),AGEVarchar(50),MOTHERNAME varchar(50),FATHERNAME varchar(50),CLASS varchar(50),SECTION varchar(50),DATEOFADDMISSION varchar(59),TOTALMARKS varchar(50))''')
x.commit()
x.close()
