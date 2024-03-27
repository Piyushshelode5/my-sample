import sqlite3
x=sqlite3.connect("sample.db")
z=[("1","piyush","23","jyoti","vilas","12th","A","12/02/2019","89"),
   ("2","vansh","20","kavita","sunil","12th","A","25/06/2022","79"),
   ("3","nishant","20","dipali","vikas","10th","B","21/11/2021","69"),
   ("4","ritik","23","pradhnya","sunil","11th","A","18/06/2021","81"),
   ("5","anurag","19","rekha","vitthalrao","10th","C","12/05/2020","72"),
   ("6","shahu","20","manisha","kishor","11th","B","11/05/2020","59"),
   ("7","lalit","20","rekha","vilas","12th","A","17/07/2018","78"),
   ("8","rushikesh","19","seema","dipak","11th","B","16/06/2020","87"),
   ("9","mohit","20","gita","kishor","10th","A","11/08/2021","76"),
   ("10","aayush","21","vaishali","kishor","11th","A","23/05/2022","82")]
x.execute('''INSERT studentinfo VALUES ?,?,?,?,?,?,?,?,?,? "z''')
print("command executed succesfully")
x.commit()
x.close() 

