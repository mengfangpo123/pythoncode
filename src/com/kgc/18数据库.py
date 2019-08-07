from pymysql import *
con=connect("localhost","root","likai","mydb",3306)
cur=con.cursor()
count=cur.execute("select * from emp")
print(count)
fetchall = cur.fetchall()
for i in fetchall:
    print(i)
con.close()
