import sqlite3
conn=sqlite3.connect('uData.db')
conn.execute('''

create table user(id INT AUTO_INCREMENT PRIMAY KEY,
             userName VARCHAR(50),
             email VARCHAR(50),
             fName VARCHAR(50),
             lName VARCHAR(50),
             pass VARCHAR(50)
             
             
             )
   
              ''')
conn.close()