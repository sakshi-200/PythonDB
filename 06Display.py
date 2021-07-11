import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()

ctg=input('Enter book category :')
curs.execute("select * from books where category ='%s'"%ctg)


rec=curs.fetchall()
print("List of books are: ")

for rec in rec:
    print(rec[1])

con.close()

