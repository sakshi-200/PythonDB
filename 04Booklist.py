import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()

curs.execute("select * from books")
rec=curs.fetchone()
print('List of books are : ')
while rec:
    print(rec[1])
    rec=curs.fetchone()
    
con.close()