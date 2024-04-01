
# l=[]
# for i in data:
    
#     l.append(i)
# print(l)
# conn.close()
def check(v1,v2):
    import sqlite3
    conn=sqlite3.connect('uData.db')
    data=conn.execute('''

SELECT * FROM user

''')
    temp=''
    for i in data:
        temp=i
        for j in temp:
            if j==v1:
                for k in temp:
                    if k==v2:
                        return True
    return False
        



                 

    