import sqlite3
def inser(data1,data2,data3,data4,data5):
    id=1
    conn = sqlite3.connect('uData.db')
    print(data1,data2,data3,data4,data5)
    conn.execute(f'''
insert into user(id,fName,lName,userName,email,pass) VALUES (1,'{data1}','{data2}','{data3}','{data4}','{data5}')


''')

    conn.commit()

    conn.close()
    id+=1